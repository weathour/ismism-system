#!/usr/bin/env python3
"""Shared lightweight query helper for ISMISM theme packages."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROLE_RANK = {"core": 0, "bridge": 1, "context": 2, "excluded": 3}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def find_one(theme_dir: Path, pattern: str) -> Path:
    hits = sorted(theme_dir.glob(pattern))
    if not hits:
        raise FileNotFoundError(f"missing {pattern} in {theme_dir}")
    return hits[0]


def main(slug: str, description: str | None = None, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=description or f"Query {slug} theme evidence")
    parser.add_argument("keyword", nargs="?", help="keyword to search in evidence and manifest metadata")
    parser.add_argument("--repo", default=".", help="repository root")
    parser.add_argument("--row", type=int, help="filter by row_id")
    parser.add_argument("--class", dest="theme_class", help="filter by theme_class")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    repo = Path(args.repo).resolve()
    theme_dir = repo / "library" / "themes" / slug
    manifest_path = find_one(theme_dir, "*row-manifest.jsonl")
    evidence_path = find_one(theme_dir, "*evidence-bank.jsonl")
    manifest = load_jsonl(manifest_path)
    evidence = load_jsonl(evidence_path)
    rows = {int(m["row_id"]): m for m in manifest}
    matches: list[tuple[tuple[int, int, int, str], dict[str, Any]]] = []

    for ev in evidence:
        row_id = int(ev["row_id"])
        row = rows.get(row_id)
        if not row:
            continue
        if args.row is not None and row_id != args.row:
            continue
        if args.theme_class and ev.get("theme_class") != args.theme_class:
            continue
        match_rank = 0
        if args.keyword:
            direct_haystack = "\n".join(
                [
                    str(ev.get("quote", "")),
                    str(ev.get("theme_class", "")),
                    " ".join(str(x) for x in (ev.get("absorption_tags") or [])),
                    str(row.get("title", "")),
                ]
            )
            manifest_haystack = "\n".join(
                [
                    str(row.get("diagnostic_rationale", "")),
                    str(row.get("exclusion_or_context_rationale", "")),
                    json.dumps(row.get("keyword_hits", {}), ensure_ascii=False),
                ]
            )
            if args.keyword in direct_haystack:
                match_rank = 0
            elif args.keyword in manifest_haystack:
                match_rank = 1
            else:
                continue
        item = {
            "evidence_id": ev.get("evidence_id"),
            "row_id": row_id,
            "toc_id": ev.get("toc_id") or row.get("toc_id"),
            "title": row.get("title"),
            "theme_class": ev.get("theme_class"),
            "theme_role": ev.get("theme_role") or row.get("theme_role") or row.get("core_status"),
            "clean_md_path": ev.get("clean_md_path") or row.get("clean_md_path"),
            "quote_role": ev.get("quote_role"),
            "quote": ev.get("quote"),
        }
        role_rank = ROLE_RANK.get(str(item["theme_role"]), 9)
        matches.append(((match_rank, role_rank, row_id, str(item["evidence_id"])), item))

    results = [item for _, item in sorted(matches, key=lambda pair: pair[0])[: max(0, args.limit)]]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            filters = []
            if args.keyword:
                filters.append(f"keyword={args.keyword}")
            if args.row is not None:
                filters.append(f"row={args.row}")
            if args.theme_class:
                filters.append(f"class={args.theme_class}")
            suffix = " (" + ", ".join(filters) + ")" if filters else ""
            print(f"No matching theme evidence for {slug}{suffix}.")
        for item in results:
            print(
                f"{item['evidence_id']} | row {item['row_id']} | {item['toc_id']} | "
                f"{item['theme_class']} | {item['theme_role']}"
            )
            print(f"  path: {item['clean_md_path']}")
            print(f"  title: {item['title']}")
            print(f"  quote: {item['quote']}")
    return 0
