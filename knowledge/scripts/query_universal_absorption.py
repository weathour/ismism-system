#!/usr/bin/env python3
"""Query Universal Absorption Phase A evidence, W3 senses, and W5 relations."""
from __future__ import annotations

import argparse
import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any

W3_BATCH = "W3-UNIVERSAL-A-2026-06-16"
W5_BATCH = "W5-UNIVERSAL-A-2026-06-16"


def iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if isinstance(rec, dict):
            yield rec


def first_row_id(value: Any) -> Any:
    if isinstance(value, list) and value and isinstance(value[0], dict):
        return value[0].get("row_id")
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Query Universal Absorption Phase A evidence/W3/W5 surfaces")
    ap.add_argument("query")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    repo = Path(args.repo)
    query = args.query
    hits: list[tuple[str, Any, Any, str]] = []

    evidence_path = repo / "knowledge/qa/universal-absorption-phase-a-evidence-bank.jsonl"
    for rec in iter_jsonl(evidence_path):
        tags = rec.get("absorption_tags", [])
        tag_text = " ".join(str(tag) for tag in tags) if isinstance(tags, list) else str(tags)
        text = " ".join(str(rec.get(k, "")) for k in ["evidence_id", "title", "quote", "toc_id"])
        if query in f"{text} {tag_text}":
            hits.append(("evidence", rec.get("evidence_id"), rec.get("row_id"), str(rec.get("quote", ""))[:160]))

    for rec in iter_jsonl(repo / "knowledge/lexicon/term-senses.jsonl"):
        if rec.get("batch_id") != W3_BATCH:
            continue
        text = json.dumps(rec, ensure_ascii=False)
        if query in text:
            hits.append(("w3", rec.get("sense_id"), first_row_id(rec.get("source_segments")), str(rec.get("definition", ""))[:160]))

    for rec in iter_jsonl(repo / "knowledge/relations/relation-assets.jsonl"):
        if rec.get("batch_id") != W5_BATCH:
            continue
        text = json.dumps(rec, ensure_ascii=False)
        if query in text:
            hits.append(("w5", rec.get("relation_id"), first_row_id(rec.get("evidence_segment")), str(rec.get("definition", ""))[:160]))

    for kind, ident, row, preview in hits[: args.limit]:
        print(f"{kind}	{ident}	row={row}	{preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
