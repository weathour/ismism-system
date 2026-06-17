#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
THEME = ROOT / "library/themes/science-academia-research"
MANIFEST = THEME / "science-academia-research-row-manifest.jsonl"
EVIDENCE = THEME / "science-academia-research-evidence-bank.jsonl"

ALIASES = {
    "科学主义": ["科学主义", "科学化", "实证主义", "自然主义", "逻辑实证主义", "科学化自证"],
    "科研评价": ["科研", "科学研究", "论文", "指标", "学术管理", "论文指标机制"],
    "学术共同体": ["学术共同体", "科学共同体", "刊物", "研讨班", "读书会", "政府资助", "学术共同体再生产"],
    "科学话语": ["科学话语", "科学实在论", "科学秩序", "知识合法性生产", "科学话语现实化"],
    "专家权威": ["专家", "理工科", "科学家", "学者", "科研主体化", "专家话语"],
    "论文指标": ["论文", "指标", "论文指标机制", "学术管理"],
}

CANONICAL_QUERY = {
    "专家": "专家权威",
    "理工科": "专家权威",
    "科学家": "专家权威",
    "学者": "专家权威",
    "专家话语": "专家权威",
    "科研主体化": "专家权威",
}

PREFERRED_ROWS = {
    "科学主义": [184, 177, 176, 172, 76, 3],
    "科研评价": [2, 177, 179, 210, 293],
    "学术共同体": [10, 76, 277, 292, 9],
    "科学话语": [1, 3, 9, 10, 11],
    "专家权威": [76, 2, 86, 294, 191, 215],
    "论文指标": [2, 177, 179, 293],
}

def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Query Science / Academia / Research theme rows and quote evidence")
    parser.add_argument("query", nargs="?", default="科学主义", help="keyword, row id, class, evidence id, or aliases such as 科学主义/科研评价/学术共同体/科学话语/专家权威/论文指标")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--row", type=int)
    parser.add_argument("--class", dest="theme_class")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    theme = repo / "library/themes/science-academia-research"
    manifest = load_jsonl(theme / "science-academia-research-row-manifest.jsonl")
    evidence = load_jsonl(theme / "science-academia-research-evidence-bank.jsonl")
    ev_by_row: dict[int, list[dict[str, Any]]] = {}
    for ev in evidence:
        ev_by_row.setdefault(int(str(ev["row_id"])), []).append(ev)

    q = str(args.query or "").strip()
    canonical_q: str = CANONICAL_QUERY.get(q) or q
    raw_terms = [q] + ALIASES.get(q, []) + ([] if canonical_q == q else [canonical_q] + ALIASES.get(canonical_q, []))
    terms = list(dict.fromkeys(t for t in raw_terms if t)) if q else []
    rows: list[tuple[int, dict[str, Any]]] = []
    for rec in manifest:
        row_id = int(str(rec["row_id"]))
        if args.row is not None and row_id != args.row:
            continue
        if args.theme_class and rec.get("theme_class") != args.theme_class:
            continue
        hay = " ".join([
            str(row_id),
            str(rec.get("toc_id", "")),
            rec.get("title", ""),
            rec.get("theme_class", ""),
            rec.get("core_status", ""),
            rec.get("science_claim_function", ""),
            rec.get("diagnostic_rationale", ""),
            json.dumps(rec.get("keyword_hits", {}), ensure_ascii=False),
        ])
        ev_text = " ".join(
            ev.get("evidence_id", "") + " " + ev.get("quote", "") + " " + ev.get("trigger_keyword", "") + " " + ev.get("quote_role", "")
            for ev in ev_by_row.get(row_id, [])
        )
        if args.row is not None or args.theme_class or not terms or any(t and (t in hay or t in ev_text) for t in terms):
            score = 0
            if q and (q in hay or q in ev_text):
                score += 200
            score += sum(20 for t in terms if t and (t in hay or t in ev_text))
            preferred = PREFERRED_ROWS.get(canonical_q, PREFERRED_ROWS.get(q, []))
            if row_id in preferred:
                score += 1000 - (50 * preferred.index(row_id))
            if rec.get("core_status") == "core":
                score += 10
            rows.append((score, rec))
    rows.sort(key=lambda item: (-item[0], int(str(item[1]["row_id"]))))

    if args.json:
        payload = []
        for _, rec in rows[: args.limit]:
            payload.append({"row": rec, "evidence": ev_by_row.get(int(str(rec["row_id"])), [])[:3]})
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0 if payload else 1

    for _, rec in rows[: args.limit]:
        row_id = int(str(rec["row_id"]))
        print(f"row {row_id} | {rec.get('toc_id')} | {rec.get('theme_class')} | {rec.get('core_status')} | {rec.get('title')}")
        print(f"  clean: {rec.get('source_clean_path') or rec.get('clean_md_path')}")
        print(f"  function: {rec.get('science_claim_function')}")
        print(f"  overlap: {rec.get('overlap_status')} education={rec.get('education_theme_class')}")
        for ev in ev_by_row.get(row_id, [])[:3]:
            print(f"  {ev['evidence_id']} [{ev.get('quote_role')}:{ev.get('trigger_keyword')}]: {ev.get('quote','')[:260]}")
    return 0 if rows else 1

if __name__ == "__main__":
    raise SystemExit(main())
