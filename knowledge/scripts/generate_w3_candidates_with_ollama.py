#!/usr/bin/env python3
"""
Generate W3 candidate-only term sense material with a local Ollama model.

This script is deliberately NOT allowed to update formal W3 files such as:
- knowledge/lexicon/term-senses.jsonl
- knowledge/lexicon/core-terms.md
- knowledge/lexicon/ambiguous-terms.md

It only writes candidate files under knowledge/lexicon/candidates/ and a run log.
The intended low-model role is evidence mining + rough clustering; a stronger
model must later review and decide what enters the official registry.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_MODEL = "gemma4:latest"
DEFAULT_API = "http://127.0.0.1:11434/api/generate"
DEFAULT_TERMS = ["中介", "实体", "物质", "符号", "符号秩序"]


@dataclass
class Segment:
    row_id: int
    segment_id: str
    toc_id: str
    title: str
    clean_path: Path


def load_segments(path: Path, repo: Path) -> dict[int, Segment]:
    out: dict[int, Segment] = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            clean_rel = r["source_paths"]["clean_md_relpath"]
            out[int(r["row_id"])] = Segment(
                row_id=int(r["row_id"]),
                segment_id=r["segment_id"],
                toc_id=str(r["toc_id"]),
                title=str(r["title"]),
                clean_path=repo / clean_rel,
            )
    return out


def load_stats(path: Path) -> dict[str, list[int]]:
    out: dict[str, list[int]] = {}
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            rows: list[int] = []
            for item in row.get("top_clean_rows", "").split(";"):
                item = item.strip()
                if not item:
                    continue
                try:
                    rows.append(int(item.split(":", 1)[0]))
                except ValueError:
                    continue
            out[row["term"]] = rows
    return out


def compact(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract_context(text: str, term: str, max_chars: int) -> str:
    """Extract compact windows around term occurrences."""
    hits = [m.start() for m in re.finditer(re.escape(term), text)]
    if not hits:
        return compact(text[:max_chars])

    windows: list[str] = []
    budget_each = max(260, max_chars // min(len(hits), 4))
    for pos in hits[:4]:
        start = max(0, pos - budget_each // 2)
        end = min(len(text), pos + budget_each // 2)
        windows.append(compact(text[start:end]))
    joined = "\n...\n".join(windows)
    return joined[:max_chars]


def build_prompt(term: str, contexts: list[dict[str, Any]], max_quotes: int) -> str:
    context_text = "\n\n".join(
        [
            f"### row {c['row_id']} / {c['toc_id']} / {c['title']}\n{c['context']}"
            for c in contexts
        ]
    )
    return f"""你是 ISMISM W3 术语候选预处理低模型，只做 evidence mining 和粗聚类。

术语：{term}

原文片段如下（只允许从这些片段中摘 quote）：

{context_text}

任务：输出 JSON 数组，最多 {max_quotes} 项。每项必须包含：
- quote: 必须是上方原文片段中的连续逐字子串，长度 20–80 字；不要改写；不要合并不连续句子。
- row_id: quote 所在 row_id，必须是数字。
- possible_tag: 候选标签，简短中文。
- hit_reason: 为什么这条 quote 支持把「{term}」作为候选概念材料。
- uncertainty_note: 仍不能判断什么；禁止写 N/A。

硬规则：
1. 只做 candidate-only，不能写正式 definition。
2. 不要 canonical 判断。
3. 不要输出 markdown 解释，只输出 JSON 数组。
4. 不要 thinking，不要英文分析，不要编造。
5. 如果证据不足，宁可少输出。
"""


def call_ollama(
    api_url: str,
    model: str,
    prompt: str,
    timeout: int,
    temperature: float,
    num_ctx: int,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {
            "temperature": temperature,
            "top_p": 0.9,
            "num_ctx": num_ctx,
        },
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(api_url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_json_array(response: str) -> list[dict[str, Any]]:
    s = response.strip()
    # Strip possible code fences.
    s = re.sub(r"^```(?:json)?\s*", "", s)
    s = re.sub(r"\s*```$", "", s)
    # Extract first JSON array if the model wrapped it.
    m = re.search(r"\[[\s\S]*\]", s)
    if m:
        s = m.group(0)
    data = json.loads(s)
    if not isinstance(data, list):
        raise ValueError("response JSON is not an array")
    return [x for x in data if isinstance(x, dict)]


def validate_items(items: list[dict[str, Any]], contexts_by_row: dict[int, str]) -> list[dict[str, Any]]:
    validated: list[dict[str, Any]] = []
    for item in items:
        try:
            row_id = int(item.get("row_id"))
        except Exception:
            item["validation_status"] = "bad_row_id"
            validated.append(item)
            continue

        quote = str(item.get("quote", "")).strip()
        text = contexts_by_row.get(row_id, "")
        ok = bool(quote) and quote in text
        item["row_id"] = row_id
        item["validation_status"] = "quote_exact" if ok else "quote_not_found_in_context"
        if not str(item.get("uncertainty_note", "")).strip() or str(item.get("uncertainty_note", "")).strip().upper() == "N/A":
            item["validation_status"] += ";bad_uncertainty"
        validated.append(item)
    return validated


def write_candidate_md(path: Path, term: str, batch_id: str, contexts: list[dict[str, Any]], items: list[dict[str, Any]], meta: dict[str, Any]) -> None:
    lines: list[str] = []
    lines.append(f"# W3 Candidate Senses — {term}\n")
    lines.append(f"- term: {term}")
    lines.append(f"- batch_candidate: {batch_id}")
    lines.append("- status: candidate-only")
    lines.append("- generated_by: local-ollama-low-model")
    lines.append("- do_not_import_directly: true")
    lines.append(f"- model: {meta.get('model')}")
    lines.append(f"- created: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    lines.append("## 1. Top evidence rows\n")
    lines.append("| row_id | toc_id | title | context_chars |")
    lines.append("|---:|---|---|---:|")
    for c in contexts:
        title = str(c["title"]).replace("|", "\\|")
        lines.append(f"| {c['row_id']} | `{c['toc_id']}` | {title} | {len(c['context'])} |")

    lines.append("\n## 2. Candidate evidence items\n")
    for i, item in enumerate(items, 1):
        lines.append(f"### C{i}: {item.get('possible_tag', '')}\n")
        lines.append(f"- row_id: {item.get('row_id')}")
        lines.append(f"- validation_status: `{item.get('validation_status')}`")
        lines.append(f"- quote: {item.get('quote')}")
        lines.append(f"- hit_reason: {item.get('hit_reason')}")
        lines.append(f"- uncertainty_note: {item.get('uncertainty_note')}\n")

    lines.append("## 3. Do-not-decide notes\n")
    lines.append("- 本文件只作为候选证据材料，不得直接导入 `term-senses.jsonl`。")
    lines.append("- `quote_not_found_in_context` 项必须由高模型或脚本复核后才可使用。")
    lines.append("- `possible_tag` 不是正式 sense_label。")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate W3 candidate-only term evidence with Ollama.")
    ap.add_argument("--repo", default=".", help="repo root")
    ap.add_argument("--terms", nargs="*", default=DEFAULT_TERMS)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--api-url", default=DEFAULT_API)
    ap.add_argument("--batch-id", default="W3-B6-candidates")
    ap.add_argument("--top-rows", type=int, default=6)
    ap.add_argument("--max-context-chars", type=int, default=1200)
    ap.add_argument("--max-quotes", type=int, default=10)
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--num-ctx", type=int, default=8192)
    ap.add_argument("--sleep", type=float, default=0.0)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    segments = load_segments(repo / "knowledge/manifests/segments.jsonl", repo)
    stats = load_stats(repo / "knowledge/lexicon/term-candidate-stats.tsv")
    out_dir = repo / "knowledge/lexicon/candidates"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / f"{args.batch_id}-runlog.jsonl"

    for term in args.terms:
        safe_term = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", term)
        md_path = out_dir / f"{args.batch_id}-{safe_term}-candidates.md"
        json_path = out_dir / f"{args.batch_id}-{safe_term}-candidates.json"
        if md_path.exists() and json_path.exists() and not args.overwrite:
            print(f"[skip] {term}: candidate files exist")
            continue

        row_ids = stats.get(term, [])[: args.top_rows]
        contexts: list[dict[str, Any]] = []
        contexts_by_row: dict[int, str] = {}
        for row_id in row_ids:
            seg = segments.get(row_id)
            if not seg or not seg.clean_path.exists():
                continue
            text = seg.clean_path.read_text(encoding="utf-8", errors="ignore")
            ctx = extract_context(text, term, args.max_context_chars)
            contexts.append(
                {
                    "row_id": seg.row_id,
                    "segment_id": seg.segment_id,
                    "toc_id": seg.toc_id,
                    "title": seg.title,
                    "clean_path": str(seg.clean_path.relative_to(repo)),
                    "context": ctx,
                }
            )
            contexts_by_row[seg.row_id] = ctx

        if not contexts:
            print(f"[warn] {term}: no contexts")
            continue

        prompt = build_prompt(term, contexts, args.max_quotes)
        t0 = time.time()
        status = "ok"
        err = None
        response_text = ""
        items: list[dict[str, Any]] = []
        raw: dict[str, Any] = {}
        try:
            raw = call_ollama(args.api_url, args.model, prompt, args.timeout, args.temperature, args.num_ctx)
            response_text = raw.get("response", "")
            items = validate_items(parse_json_array(response_text), contexts_by_row)
        except Exception as e:
            status = "error"
            err = repr(e)
            items = []

        elapsed = time.time() - t0
        payload = {
            "term": term,
            "batch_id": args.batch_id,
            "status": status,
            "error": err,
            "model": args.model,
            "elapsed_sec": round(elapsed, 3),
            "ollama_stats": {k: raw.get(k) for k in ["total_duration", "prompt_eval_count", "eval_count"]} if raw else {},
            "contexts": contexts,
            "items": items,
            "raw_response": response_text,
        }
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_candidate_md(md_path, term, args.batch_id, contexts, items, {"model": args.model})
        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps({k: payload[k] for k in ["term", "batch_id", "status", "error", "elapsed_sec", "ollama_stats"]}, ensure_ascii=False) + "\n")
        print(f"[{status}] {term}: {len(items)} items, {elapsed:.1f}s -> {md_path.relative_to(repo)}")
        if args.sleep:
            time.sleep(args.sleep)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
