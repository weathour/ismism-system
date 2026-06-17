#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    records = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Query Capitalism / Political Economy theme rows and exact quote evidence"
    )
    ap.add_argument(
        "query",
        nargs="?",
        default="",
        help="keyword such as 资本主义/资本/生产关系/拜物教/金融/帝国主义/异化/消费",
    )
    ap.add_argument("--repo", default=".")
    ap.add_argument("--row", type=int)
    ap.add_argument("--class", dest="theme_class")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    repo = Path(args.repo)
    theme = repo / "knowledge/themes/capitalism"
    manifest = load_jsonl(theme / "capitalism-row-manifest.jsonl")
    evidence = load_jsonl(theme / "capitalism-evidence-bank.jsonl")
    ev_by_row: dict[int, list[dict]] = {}
    for ev in evidence:
        ev_by_row.setdefault(ev["row_id"], []).append(ev)

    aliases = {
        "资本主义": ["资本主义", "capitalism", "资本", "生产关系"],
        "资本": ["资本", "capital", "金融资本", "资本社会化"],
        "生产关系": ["生产关系", "生产活动", "生产过程", "再政治化"],
        "拜物教": ["拜物", "物神", "商品拜物教", "商品"],
        "金融": ["金融", "global financial capital", "货币", "价值抽象"],
        "帝国主义": ["帝国主义", "殖民", "全球分工", "全球资本"],
        "异化": ["异化", "人我关系异化", "生产者"],
        "消费": ["消费", "享乐", "剩余快感", "市场"],
    }
    q = args.query.strip()
    terms = [q] + aliases.get(q, []) if q else []
    rows = []

    for rec in manifest:
        if args.row is not None and rec["row_id"] != args.row:
            continue
        if args.theme_class and rec["theme_class"] != args.theme_class:
            continue
        hay = " ".join(
            [
                rec.get("title", ""),
                rec.get("theme_class", ""),
                rec.get("notes", ""),
                json.dumps(rec.get("keyword_hits", {}), ensure_ascii=False),
            ]
        )
        ev_text = " ".join(ev.get("quote", "") for ev in ev_by_row.get(rec["row_id"], []))
        if terms and not any(t and (t in hay or t in ev_text) for t in terms):
            continue
        score = 0
        for t in terms:
            if t in rec.get("title", ""):
                score += 100
            if t in hay:
                score += 30
            if t in ev_text:
                score += 20
        if rec.get("core_status") == "core":
            score += 25
        rows.append((score, rec))

    rows.sort(key=lambda item: (-item[0], item[1]["row_id"]))
    for _, rec in rows[: args.limit]:
        print(f"row {rec['row_id']} | {rec['toc_id']} | {rec['theme_class']} | {rec['title']}")
        print(f"  clean: {rec['clean_md_path']}")
        for ev in ev_by_row.get(rec["row_id"], [])[:3]:
            print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not rows:
        print("No matching Capitalism / Political Economy theme rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
