#!/usr/bin/env python3
"""Trace concept/relation/row evidence back to clean segment text."""
from __future__ import annotations

import argparse
from query_helpers import as_json, clean_path_for_row, relation_records, repo_root, row_title, segment_records, term_records, truncate, verify_quote_in_row


def trace_term(root, sense_id: str):
    matches = [r for r in term_records(root) if r.get("sense_id") == sense_id]
    if not matches:
        raise SystemExit(f"sense_id not found: {sense_id}")
    record = matches[0]
    checks = []
    for item in record.get("evidence_quotes") or []:
        checks.append(verify_quote_in_row(root, int(item["row_id"]), item.get("quote", "")))
    return {"kind": "term", "id": sense_id, "term": record.get("term"), "status": record.get("status"), "checks": checks}


def trace_relation(root, relation_id: str):
    matches = [r for r in relation_records(root) if r.get("relation_id") == relation_id]
    if not matches:
        raise SystemExit(f"relation_id not found: {relation_id}")
    record = matches[0]
    checks = []
    for item in (record.get("evidence_segment") or record.get("evidence") or []):
        checks.append(verify_quote_in_row(root, int(item["row_id"]), item.get("quote", "")))
    return {"kind": "relation", "id": relation_id, "relation_type": record.get("relation_type"), "status": record.get("status"), "checks": checks}


def trace_row(root, row_id: int, preview_chars: int = 0):
    matches = [r for r in segment_records(root) if int(r.get("row_id")) == int(row_id)]
    if not matches:
        raise SystemExit(f"row_id not found: {row_id}")
    record = matches[0]
    path = clean_path_for_row(root, row_id)
    data = {
        "kind": "row",
        "row_id": row_id,
        "toc_id": record.get("toc_id"),
        "title": record.get("title"),
        "segment_id": record.get("segment_id"),
        "text_status": record.get("text_status"),
        "clean_md_path": str(path.relative_to(root)) if path else None,
        "raw_md_path": record.get("source_paths", {}).get("raw_md_relpath"),
    }
    if preview_chars and path and path.exists():
        data["preview"] = path.read_text(encoding="utf-8")[:preview_chars]
    return data


def print_trace(data) -> None:
    if data["kind"] == "row":
        print(f"# Row trace: {data['row_id']}")
        print(f"- toc/title: {data.get('toc_id')} {data.get('title')}")
        print(f"- segment_id: {data.get('segment_id')}")
        print(f"- text_status: {data.get('text_status')}")
        print(f"- clean_md_path: `{data.get('clean_md_path')}`")
        print(f"- raw_md_path: `{data.get('raw_md_path')}`")
        if data.get("preview"):
            print("\n## Preview")
            print(data["preview"])
        return
    print(f"# Evidence trace: {data['id']}")
    print(f"- kind: {data['kind']}")
    print(f"- status: {data.get('status')}")
    if data.get("term"):
        print(f"- term: {data.get('term')}")
    if data.get("relation_type"):
        print(f"- relation_type: {data.get('relation_type')}")
    ok = all(check.get("status") == "PASS" for check in data["checks"])
    print(f"- trace_status: {'PASS' if ok else 'CHECK'}")
    for check in data["checks"]:
        print()
        print(f"## row {check['row_id']} — {row_title(ROOT, check['row_id'])}")
        print(f"- quote_status: {check.get('status')}")
        print(f"- clean_md_path: `{check.get('clean_md_path')}`")
        print(f"- quote: {truncate(check.get('quote', ''), 220)}")


ROOT = None


def main() -> None:
    global ROOT
    parser = argparse.ArgumentParser(description="Trace a term sense, relation, or row to clean segment evidence.")
    parser.add_argument("identifier", help="sense_id, relation_id, or row_id, e.g. term:主体:s01 / rel:w5b1:001 / 276")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--preview-chars", type=int, default=0, help="for row traces, include clean text preview")
    parser.add_argument("--limit", type=int, default=None, help="accepted for CLI consistency; trace returns one record")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    ROOT = repo_root(args.repo)
    ident = args.identifier
    if ident.startswith("term:"):
        data = trace_term(ROOT, ident)
    elif ident.startswith("rel:"):
        data = trace_relation(ROOT, ident)
    else:
        try:
            row_id = int(ident)
        except ValueError as exc:
            raise SystemExit("identifier must start with term:, rel:, or be an integer row_id") from exc
        data = trace_row(ROOT, row_id, preview_chars=args.preview_chars)
    if args.json:
        print(as_json(data))
    else:
        print_trace(data)


if __name__ == "__main__":
    main()
