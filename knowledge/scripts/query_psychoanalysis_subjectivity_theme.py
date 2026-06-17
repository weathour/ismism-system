#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path("knowledge/themes/psychoanalysis-subjectivity")
MANIFEST = ROOT / "psychoanalysis-subjectivity-row-manifest.jsonl"
EVIDENCE = ROOT / "psychoanalysis-subjectivity-evidence-bank.jsonl"
ROLE_RANK = {"core": 0, "bridge": 1, "context": 2, "excluded": 3}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Query Psychoanalysis-Subjectivity theme evidence")
    parser.add_argument("keyword", nargs="?", help="keyword to search in direct evidence first, then manifest hits")
    parser.add_argument("--row", type=int, help="filter by row_id")
    parser.add_argument("--class", dest="theme_class", help="filter by theme_class")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    manifest = load_jsonl(MANIFEST)
    evidence = load_jsonl(EVIDENCE)
    rows = {m["row_id"]: m for m in manifest}
    matches: list[tuple[tuple[int, int, int, str], dict[str, Any]]] = []

    for ev in evidence:
        row = rows.get(ev["row_id"])
        if not row:
            continue
        if args.row is not None and ev["row_id"] != args.row:
            continue
        if args.theme_class and ev["theme_class"] != args.theme_class:
            continue
        match_rank = 0
        if args.keyword:
            direct_haystack = "\n".join(
                [
                    ev.get("quote", ""),
                    ev.get("theme_class", ""),
                    " ".join(ev.get("absorption_tags") or []),
                    row.get("title", ""),
                ]
            )
            manifest_haystack = "\n".join([row.get("inclusion_rationale", ""), json.dumps(row.get("keyword_hits", {}), ensure_ascii=False)])
            if args.keyword in direct_haystack:
                match_rank = 0
            elif args.keyword in manifest_haystack:
                match_rank = 1
            else:
                continue
        item = {
            "evidence_id": ev["evidence_id"],
            "row_id": ev["row_id"],
            "toc_id": ev["toc_id"],
            "title": row["title"],
            "theme_class": ev["theme_class"],
            "theme_role": row["theme_role"],
            "clean_md_path": ev["clean_md_path"],
            "quote_role": ev["quote_role"],
            "quote": ev["quote"],
        }
        sort_key = (match_rank, ROLE_RANK.get(row["theme_role"], 9), ev["row_id"], ev["evidence_id"])
        matches.append((sort_key, item))

    results = [item for _, item in sorted(matches, key=lambda pair: pair[0])[: args.limit]]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(
                f"{item['evidence_id']} | row {item['row_id']} | {item['toc_id']} | "
                f"{item['theme_class']} | {item['theme_role']}"
            )
            print(f"  path: {item['clean_md_path']}")
            print(f"  title: {item['title']}")
            print(f"  quote: {item['quote']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
