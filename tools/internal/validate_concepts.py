#!/usr/bin/env python3
"""
Validate concept term sense records against the current corpus evidence layer.

Checks are intentionally conservative:
- JSONL parses record-by-record.
- sense_id follows term:<term>:sNN.
- required fields are present and non-empty.
- every record remains draft unless explicitly excluded by a future audit.
- every evidence quote is an exact substring of its row's corpus/clean-markdown text.
- source segment/card/clean paths exist where declared.

This script does not modify files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


VALID_AXES = {"场域", "本体论", "认识论", "目的论", "复合"}


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    segments: dict[int, dict[str, Any]] = {}
    path = repo / "library/manifests/segments.jsonl"
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            segments[int(rec["row_id"])] = rec
    return segments


def rel_exists(repo: Path, rel: str | None) -> bool:
    return bool(rel) and (repo / rel).exists()


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate concept term-senses.jsonl evidence.")
    ap.add_argument("--repo", default=".", help="repository root")
    ap.add_argument(
        "--term-senses",
        default="library/concepts/term-senses.jsonl",
        help="term sense JSONL path relative to repo",
    )
    ap.add_argument("--batch-id", help="validate only records with this batch_id")
    ap.add_argument("--json", action="store_true", help="emit machine-readable summary")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    segments = load_segments(repo)
    path = repo / args.term_senses

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    checked_records = 0
    checked_quotes = 0
    terms: set[str] = set()
    seen_sense_ids: set[str] = set()

    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception as exc:  # pragma: no cover - defensive CLI path
                errors.append({"line": lineno, "kind": "json_parse", "detail": str(exc)})
                continue

            if args.batch_id and rec.get("batch_id") != args.batch_id:
                continue

            checked_records += 1
            sense_id = str(rec.get("sense_id", ""))
            term = str(rec.get("term", ""))
            terms.add(term)

            if sense_id in seen_sense_ids:
                errors.append({"line": lineno, "sense_id": sense_id, "kind": "duplicate_sense_id"})
            seen_sense_ids.add(sense_id)

            if not re.fullmatch(rf"term:{re.escape(term)}:s\d{{2}}", sense_id):
                errors.append({"line": lineno, "sense_id": sense_id, "kind": "bad_sense_id"})
            if rec.get("status") != "draft":
                errors.append({"line": lineno, "sense_id": sense_id, "kind": "non_draft_status", "status": rec.get("status")})
            if rec.get("axis") not in VALID_AXES:
                errors.append({"line": lineno, "sense_id": sense_id, "kind": "bad_axis", "axis": rec.get("axis")})
            for field in ("sense_label", "definition", "forbidden_mix", "batch_id", "schema_version"):
                if not str(rec.get(field, "")).strip():
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "empty_field", "field": field})

            source_segments = rec.get("source_segments")
            if not isinstance(source_segments, list) or not source_segments:
                errors.append({"line": lineno, "sense_id": sense_id, "kind": "missing_source_segments"})
                source_segments = []

            source_by_row: dict[int, dict[str, Any]] = {}
            for src in source_segments:
                try:
                    row_id = int(src.get("row_id"))
                except Exception:
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "bad_source_row", "source": src})
                    continue
                source_by_row[row_id] = src
                if row_id not in segments:
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "source_row_not_in_manifest", "row_id": row_id})
                    continue
                if not rel_exists(repo, src.get("clean_md_path")):
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "clean_path_missing", "row_id": row_id, "path": src.get("clean_md_path")})
                if src.get("segment_card_path") and not rel_exists(repo, src.get("segment_card_path")):
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "segment_card_missing", "row_id": row_id, "path": src.get("segment_card_path")})

            evidence_quotes = rec.get("evidence_quotes")
            if not isinstance(evidence_quotes, list) or len(evidence_quotes) < 2:
                errors.append({"line": lineno, "sense_id": sense_id, "kind": "too_few_evidence_quotes", "count": len(evidence_quotes or [])})
                evidence_quotes = evidence_quotes if isinstance(evidence_quotes, list) else []

            for q in evidence_quotes:
                checked_quotes += 1
                try:
                    row_id = int(q.get("row_id"))
                except Exception:
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "bad_quote_row", "quote": q})
                    continue
                quote = str(q.get("quote", "")).strip()
                if not quote:
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "empty_quote", "row_id": row_id})
                    continue
                if row_id not in segments:
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "quote_row_not_in_manifest", "row_id": row_id})
                    continue
                src = source_by_row.get(row_id, {})
                clean_rel = src.get("clean_md_path") or segments[row_id]["source_paths"]["clean_md_relpath"]
                clean_path = repo / clean_rel
                if not clean_path.exists():
                    errors.append({"line": lineno, "sense_id": sense_id, "kind": "quote_clean_path_missing", "row_id": row_id, "path": clean_rel})
                    continue
                text = clean_path.read_text(encoding="utf-8")
                if quote not in text:
                    errors.append(
                        {
                            "line": lineno,
                            "sense_id": sense_id,
                            "kind": "quote_not_found",
                            "row_id": row_id,
                            "quote_prefix": quote[:80],
                        }
                    )
                if row_id not in source_by_row:
                    warnings.append({"line": lineno, "sense_id": sense_id, "kind": "quote_row_not_declared_in_source_segments", "row_id": row_id})

    summary = {
        "checked_records": checked_records,
        "checked_terms": len(terms),
        "checked_quotes": checked_quotes,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"concept validation: records={checked_records}, terms={len(terms)}, "
            f"quotes={checked_quotes}, errors={len(errors)}, warnings={len(warnings)}"
        )
        for err in errors[:50]:
            print("ERROR", json.dumps(err, ensure_ascii=False))
        for warn in warnings[:20]:
            print("WARN", json.dumps(warn, ensure_ascii=False))

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
