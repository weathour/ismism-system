#!/usr/bin/env python3
"""Query concept ISMISM term-sense records."""
from __future__ import annotations

import argparse
from pathlib import Path
from query_helpers import as_json, contains_any, record_rows, repo_root, row_title, term_records, truncate


def matches(record, args) -> bool:
    if args.sense_id and record.get("sense_id") != args.sense_id:
        return False
    if args.row is not None and int(args.row) not in record_rows(record):
        return False
    if args.query:
        q = args.query
        if args.contains:
            fields = [record.get("term"), record.get("sense_id"), record.get("sense_label"), record.get("definition")]
            if not contains_any(fields, q):
                return False
        elif record.get("term") != q and record.get("sense_id") != q:
            return False
    return True


def print_markdown(records, root: Path, args) -> None:
    title = args.query or args.sense_id or "all"
    print(f"# concept term query: {title}")
    print(f"matches: {len(records)}")
    for record in records[: args.limit]:
        print()
        print(f"## {record.get('sense_id')} — {record.get('term')} / {record.get('sense_label')}")
        print(f"- axis: {record.get('axis')}")
        print(f"- status: {record.get('status')} / confidence: {record.get('confidence')}")
        rows = record_rows(record)
        if rows:
            row_bits = [f"row {row} ({row_title(root, row)})" for row in rows]
            print(f"- source rows: {'; '.join(row_bits)}")
        print(f"- definition: {truncate(record.get('definition', ''), args.definition_chars)}")
        forbidden = record.get("forbidden_mix")
        if forbidden:
            print(f"- forbidden_mix: {truncate(forbidden, args.definition_chars)}")
        quotes = record.get("evidence_quotes") or []
        for quote in quotes[: args.show_quotes]:
            print(f"  - quote row {quote.get('row_id')}: {truncate(quote.get('quote', ''), args.quote_chars)}")
    if len(records) > args.limit:
        print(f"\n... truncated: showing {args.limit}/{len(records)} records")


def main() -> None:
    parser = argparse.ArgumentParser(description="Query concept term-sense records.")
    parser.add_argument("query", nargs="?", help="term or sense_id to query")
    parser.add_argument("--repo", default=".", help="repository root (default: .)")
    parser.add_argument("--sense-id", help="exact sense_id, e.g. term:主体:s01")
    parser.add_argument("--row", type=int, help="filter records linked to row_id")
    parser.add_argument("--contains", action="store_true", help="substring search instead of exact term/sense match")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--show-quotes", type=int, default=2)
    parser.add_argument("--definition-chars", type=int, default=260)
    parser.add_argument("--quote-chars", type=int, default=180)
    parser.add_argument("--json", action="store_true", help="emit full matching records as JSON")
    args = parser.parse_args()
    if not args.query and not args.sense_id and args.row is None:
        parser.error("provide a term/query, --sense-id, or --row")
    root = repo_root(args.repo)
    records = [record for record in term_records(root) if matches(record, args)]
    records.sort(key=lambda r: (str(r.get("term")), str(r.get("sense_id"))))
    if args.json:
        print(as_json(records[: args.limit]))
    else:
        print_markdown(records, root, args)


if __name__ == "__main__":
    main()
