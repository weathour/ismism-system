#!/usr/bin/env python3
"""
Heavy full-corpus concept candidate-only scanner using local Ollama.

This is intentionally a pre-processing miner:
- scans corpus/clean-markdown via library/manifests/segments.jsonl
- extracts bounded windows for specified terms
- sends shards to a local model
- writes only to library/concepts/candidates/fullscan/<batch>/<term>/

It must never update formal concept registry files.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_MODEL = "gemma4:latest"
DEFAULT_API = "http://127.0.0.1:11434/api/generate"
DEFAULT_TERMS = [
    "中介", "实体", "物质", "符号", "符号秩序",
    "场域", "场域论", "本体论", "认识论", "目的论",
    "意识形态", "理论家", "实践单元", "闭合", "有限性", "误认", "跃迁",
    "主体性", "客体性", "历史性", "现实", "现实化", "生活",
    "异化", "物神化", "欲望", "他者", "大他者", "客体小a",
    "结构", "矛盾", "伦理", "规范性", "时间性", "空间性",
    "现象", "实存", "自由", "绝对", "普遍", "特殊",
]


@dataclass
class Segment:
    row_id: int
    segment_id: str
    toc_id: str
    title: str
    clean_path: Path


def compact(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def safe_name(s: str) -> str:
    return re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", s)


def load_segments(repo: Path) -> list[Segment]:
    out: list[Segment] = []
    path = repo / "library/manifests/segments.jsonl"
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        clean_rel = r["source_paths"]["clean_md_relpath"]
        clean_path = repo / clean_rel
        if not clean_path.exists():
            continue
        out.append(
            Segment(
                row_id=int(r["row_id"]),
                segment_id=r["segment_id"],
                toc_id=str(r["toc_id"]),
                title=str(r["title"]),
                clean_path=clean_path,
            )
        )
    return out


def extract_windows(text: str, term: str, windows_per_row: int, window_chars: int) -> list[str]:
    hits = [m.start() for m in re.finditer(re.escape(term), text)]
    windows: list[str] = []
    seen: set[str] = set()
    for pos in hits[:windows_per_row]:
        start = max(0, pos - window_chars // 2)
        end = min(len(text), pos + window_chars // 2)
        w = compact(text[start:end])
        if w and w not in seen:
            seen.add(w)
            windows.append(w)
    return windows


def pick_even(items: list[Any], limit: int) -> list[Any]:
    if limit <= 0 or len(items) <= limit:
        return items
    if limit == 1:
        return [items[0]]
    idxs = sorted({round(i * (len(items) - 1) / (limit - 1)) for i in range(limit)})
    return [items[i] for i in idxs]


def contexts_for_term(
    segments: list[Segment],
    repo: Path,
    term: str,
    max_rows: int,
    windows_per_row: int,
    window_chars: int,
) -> list[dict[str, Any]]:
    matches: list[tuple[Segment, str, list[str]]] = []
    for seg in segments:
        text = seg.clean_path.read_text(encoding="utf-8", errors="ignore")
        if term not in text:
            continue
        windows = extract_windows(text, term, windows_per_row, window_chars)
        if windows:
            matches.append((seg, text, windows))
    picked = pick_even(matches, max_rows)
    contexts: list[dict[str, Any]] = []
    for seg, _text, windows in picked:
        contexts.append(
            {
                "row_id": seg.row_id,
                "segment_id": seg.segment_id,
                "toc_id": seg.toc_id,
                "title": seg.title,
                "clean_path": str(seg.clean_path.relative_to(repo)),
                "context": "\n...\n".join(windows),
            }
        )
    return contexts


def chunks(items: list[Any], n: int) -> list[list[Any]]:
    return [items[i : i + n] for i in range(0, len(items), n)]


def build_prompt(term: str, shard_contexts: list[dict[str, Any]], max_items: int) -> str:
    ctx = "\n\n".join(
        f"### row_id={c['row_id']} | toc_id={c['toc_id']} | title={c['title']}\n{c['context']}"
        for c in shard_contexts
    )
    return f"""你是 ISMISM concept 术语候选预处理低模型，只做 candidate-only evidence mining。

术语：{term}

只允许从以下片段摘录 quote：

{ctx}

输出 JSON 数组，最多 {max_items} 项。每项字段：
- quote: 必须是上方片段中的连续逐字子串，长度 20-100 字，不得改写，不得拼接。
- row_id: 必须使用片段标题中的真实 row_id 数字，不得使用 1/2/3 序号。
- possible_tag: 候选标签，简短中文。
- hit_reason: 为什么这条 quote 是「{term}」的候选材料。
- uncertainty_note: 仍不能判断什么；禁止写 N/A。

硬规则：
1. 只输出 JSON 数组，不要 markdown，不要解释。
2. 只做候选，不写正式 definition。
3. 不做 canonical 判断。
4. 不要 thinking，不要英文分析，不要编造。
5. 如果证据不足，宁可少输出。
"""


def call_ollama(api_url: str, model: str, prompt: str, timeout: int, temperature: float, num_ctx: int) -> dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": temperature, "top_p": 0.9, "num_ctx": num_ctx},
    }
    req = urllib.request.Request(
        api_url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_array(response: str) -> list[dict[str, Any]]:
    s = response.strip()
    s = re.sub(r"^```(?:json)?\s*", "", s)
    s = re.sub(r"\s*```$", "", s)
    m = re.search(r"\[[\s\S]*\]", s)
    if m:
        s = m.group(0)
    data = json.loads(s)
    if not isinstance(data, list):
        raise ValueError("response is not JSON array")
    return [x for x in data if isinstance(x, dict)]


def validate(items: list[dict[str, Any]], contexts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_row = {int(c["row_id"]): c["context"] for c in contexts}
    all_text = "\n".join(c["context"] for c in contexts)
    out = []
    for item in items:
        try:
            row_id = int(item.get("row_id"))
        except Exception:
            row_id = None
        quote = str(item.get("quote", "")).strip()
        if row_id is not None and quote and quote in by_row.get(row_id, ""):
            status = "quote_exact"
        elif quote and quote in all_text:
            status = "quote_exact_wrong_row"
        else:
            status = "quote_not_found_in_shard"
        if not str(item.get("uncertainty_note", "")).strip() or str(item.get("uncertainty_note", "")).strip().upper() == "N/A":
            status += ";bad_uncertainty"
        item["row_id"] = row_id
        item["validation_status"] = status
        out.append(item)
    return out


def write_shard_md(path: Path, term: str, batch_id: str, shard_no: int, contexts: list[dict[str, Any]], items: list[dict[str, Any]], model: str) -> None:
    lines = [
        f"# concept Fullscan Candidate Shard — {term} / {shard_no:03d}",
        "",
        f"- term: {term}",
        f"- batch_candidate: {batch_id}",
        "- status: candidate-only",
        "- do_not_import_directly: true",
        f"- model: {model}",
        "",
        "## Rows in shard",
        "",
        "| row_id | toc_id | title |",
        "|---:|---|---|",
    ]
    for c in contexts:
        title = str(c["title"]).replace("|", "\\|")
        lines.append(f"| {c['row_id']} | `{c['toc_id']}` | {title} |")
    lines.extend(["", "## Candidate items", ""])
    for i, it in enumerate(items, 1):
        lines.extend(
            [
                f"### C{i}: {it.get('possible_tag','')}",
                "",
                f"- row_id: {it.get('row_id')}",
                f"- validation_status: `{it.get('validation_status')}`",
                f"- quote: {it.get('quote')}",
                f"- hit_reason: {it.get('hit_reason')}",
                f"- uncertainty_note: {it.get('uncertainty_note')}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_summary(term_dir: Path, term: str, batch_id: str, contexts: list[dict[str, Any]], all_items: list[dict[str, Any]], shard_count: int) -> None:
    exact = [x for x in all_items if str(x.get("validation_status", "")).startswith("quote_exact")]
    bad = [x for x in all_items if not str(x.get("validation_status", "")).startswith("quote_exact")]
    summary = {
        "term": term,
        "batch_id": batch_id,
        "status": "candidate-only",
        "matched_rows": len(contexts),
        "shard_count": shard_count,
        "items_total": len(all_items),
        "items_quote_exact": len(exact),
        "items_non_exact": len(bad),
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    (term_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        f"# concept Fullscan Candidate Summary — {term}",
        "",
        f"- batch_candidate: {batch_id}",
        "- status: candidate-only",
        "- do_not_import_directly: true",
        f"- matched_rows: {len(contexts)}",
        f"- shard_count: {shard_count}",
        f"- items_total: {len(all_items)}",
        f"- items_quote_exact: {len(exact)}",
        f"- items_non_exact: {len(bad)}",
        "",
        "## Exact quote samples",
        "",
    ]
    for it in exact[:30]:
        lines.append(f"- row {it.get('row_id')} / {it.get('possible_tag')}: {it.get('quote')}")
    (term_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Heavy full-corpus concept candidate scan with local Ollama.")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--batch-id", default="concept-fullscan-gemma4")
    ap.add_argument("--terms", nargs="*", default=DEFAULT_TERMS)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--api-url", default=DEFAULT_API)
    ap.add_argument("--max-rows-per-term", type=int, default=160, help="0 means all matching rows")
    ap.add_argument("--windows-per-row", type=int, default=2)
    ap.add_argument("--window-chars", type=int, default=900)
    ap.add_argument("--shard-size", type=int, default=6)
    ap.add_argument("--max-items-per-shard", type=int, default=12)
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--num-ctx", type=int, default=8192)
    ap.add_argument("--sleep", type=float, default=0.0)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    segments = load_segments(repo)
    root = repo / "library/concepts/candidates/fullscan" / args.batch_id
    root.mkdir(parents=True, exist_ok=True)
    runlog = root / "runlog.jsonl"

    for term in args.terms:
        term_dir = root / safe_name(term)
        term_dir.mkdir(parents=True, exist_ok=True)
        if (term_dir / "summary.json").exists() and not args.overwrite:
            print(f"[skip] {term}: summary exists")
            continue
        contexts = contexts_for_term(
            segments,
            repo,
            term,
            args.max_rows_per_term,
            args.windows_per_row,
            args.window_chars,
        )
        shards = chunks(contexts, args.shard_size)
        all_items: list[dict[str, Any]] = []
        print(f"[term] {term}: matched_rows={len(contexts)} shards={len(shards)}")
        for idx, shard_contexts in enumerate(shards, 1):
            json_path = term_dir / f"shard-{idx:03d}.json"
            md_path = term_dir / f"shard-{idx:03d}.md"
            if json_path.exists() and md_path.exists() and not args.overwrite:
                d = json.loads(json_path.read_text(encoding="utf-8"))
                all_items.extend(d.get("items", []))
                continue
            t0 = time.time()
            status = "ok"
            err = None
            raw: dict[str, Any] = {}
            items: list[dict[str, Any]] = []
            try:
                prompt = build_prompt(term, shard_contexts, args.max_items_per_shard)
                raw = call_ollama(args.api_url, args.model, prompt, args.timeout, args.temperature, args.num_ctx)
                items = validate(parse_array(raw.get("response", "")), shard_contexts)
            except Exception as e:
                status = "error"
                err = repr(e)
            elapsed = round(time.time() - t0, 3)
            payload = {
                "term": term,
                "batch_id": args.batch_id,
                "shard_no": idx,
                "status": status,
                "error": err,
                "elapsed_sec": elapsed,
                "contexts": shard_contexts,
                "items": items,
                "raw_response": raw.get("response", "") if raw else "",
                "ollama_stats": {k: raw.get(k) for k in ["total_duration", "prompt_eval_count", "eval_count"]} if raw else {},
            }
            json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            write_shard_md(md_path, term, args.batch_id, idx, shard_contexts, items, args.model)
            all_items.extend(items)
            with runlog.open("a", encoding="utf-8") as f:
                f.write(json.dumps({k: payload[k] for k in ["term", "batch_id", "shard_no", "status", "error", "elapsed_sec", "ollama_stats"]}, ensure_ascii=False) + "\n")
            print(f"[{status}] {term} shard {idx}/{len(shards)} items={len(items)} elapsed={elapsed}s")
            if args.sleep:
                time.sleep(args.sleep)
        write_summary(term_dir, term, args.batch_id, contexts, all_items, len(shards))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
