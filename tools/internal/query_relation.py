#!/usr/bin/env python3
"""Query ISMISM relation assets."""
from __future__ import annotations

import argparse
from query_helpers import as_json, contains_any, record_rows, relation_records, repo_root, row_title, truncate


def matches(record, args) -> bool:
    if args.relation_id and record.get("relation_id") != args.relation_id:
        return False
    if args.type and record.get("relation_type") != args.type:
        return False
    if args.source and args.source not in str(record.get("source")):
        return False
    if args.target and args.target not in str(record.get("target")):
        return False
    if args.row is not None and int(args.row) not in record_rows(record):
        return False
    if args.query:
        fields = [record.get("relation_id"), record.get("source"), record.get("target"), record.get("relation_type"), record.get("definition")]
        if args.contains:
            if not contains_any(fields, args.query):
                return False
        elif args.query not in fields and not contains_any(fields, args.query):
            return False
    return True


def print_markdown(records, root, args) -> None:
    title = args.query or args.relation_id or args.type or "relations"
    print(f"# Relation query: {title}")
    print(f"matches: {len(records)}")
    for record in records[: args.limit]:
        print()
        print(f"## {record.get('relation_id')} — {record.get('relation_type')}")
        print(f"- source → target: {record.get('source')} → {record.get('target')}")
        print(f"- positions: {record.get('source_position')} → {record.get('target_position')}")
        print(f"- status/confidence: {record.get('status')} / {record.get('confidence')}")
        rows = record_rows(record)
        if rows:
            print(f"- evidence rows: {'; '.join(f'row {row} ({row_title(root, row)})' for row in rows)}")
        print(f"- definition: {truncate(record.get('definition', ''), args.definition_chars)}")
        boundary = record.get("applicability_boundary")
        if boundary:
            print(f"- applicability_boundary: {truncate(boundary, args.definition_chars)}")
        forbidden = record.get("forbidden_interpretation")
        if forbidden:
            print(f"- forbidden_interpretation: {truncate(forbidden, args.definition_chars)}")
        evidence = record.get("evidence_segment") or record.get("evidence") or []
        for item in evidence[: args.show_quotes]:
            print(f"  - quote row {item.get('row_id')}: {truncate(item.get('quote', ''), args.quote_chars)}")
    if len(records) > args.limit:
        print(f"\n... truncated: showing {args.limit}/{len(records)} relations")


def main() -> None:
    parser = argparse.ArgumentParser(description="Query relation assets.")
    parser.add_argument("query", nargs="?", help="relation_id/source/target/type/definition query")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--relation-id", help="exact relation_id")
    parser.add_argument("--type", help="exact relation_type")
    parser.add_argument("--source", help="substring filter for source")
    parser.add_argument("--target", help="substring filter for target")
    parser.add_argument("--row", type=int, help="filter by evidence row")
    parser.add_argument("--contains", action="store_true", help="substring search across primary fields")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--show-quotes", type=int, default=2)
    parser.add_argument("--definition-chars", type=int, default=260)
    parser.add_argument("--quote-chars", type=int, default=180)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not any([args.query, args.relation_id, args.type, args.source, args.target, args.row is not None]):
        parser.error("provide a query or at least one filter")
    root = repo_root(args.repo)
    records = [record for record in relation_records(root) if matches(record, args)]
    records.sort(key=lambda r: str(r.get("relation_id")))
    if args.json:
        print(as_json(records[: args.limit]))
    else:
        print_markdown(records, root, args)


if __name__ == "__main__":
    main()
