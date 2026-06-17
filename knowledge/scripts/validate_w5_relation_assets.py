#!/usr/bin/env python3
"""
Validate W5 relation assets against the current corpus/position evidence layers.

Checks are intentionally conservative and read-only:
- JSONL parses record-by-record.
- relation_id values are unique.
- controlled relation_type values are used.
- every relation remains draft unless explicitly changed by a future audit.
- required project knowledge contract fields are non-empty.
- source_position and target_position point to existing W4 position cards.
- every evidence_segment quote is an exact substring of its row's split_md_clean text.
- term:*:sNN sources/targets/source_senses point to existing W3 term sense IDs.

Use --min-count 60 --require-type-min 2 for the final project knowledge contract W5 gate.
Use defaults for an in-progress W5 integrity check.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_TYPES = {
    "boundary-between",
    "route-from-to",
    "tension-between",
    "mediates-between",
    "transitions-to",
    "blocks-transition",
    "misrecognizes-as",
    "objectifies",
    "subjectivizes",
    "overcodes",
    "represents-position",
    "evidences-claim",
}

REQUIRED_FIELDS = (
    "relation_id",
    "source",
    "target",
    "source_position",
    "target_position",
    "relation_type",
    "definition",
    "evidence_segment",
    "applicability_boundary",
    "forbidden_interpretation",
    "status",
    "batch_id",
)

FORBIDDEN_PATTERNS = (
    "人格障碍",
    "人格类型",
    "诊断标签",
    "精神病人",
    "患者",
    "最终真理",
    "万能解释器",
)


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    segments: dict[int, dict[str, Any]] = {}
    path = repo / "knowledge/manifests/segments.jsonl"
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            segments[int(rec["row_id"])] = rec
    return segments


def load_sense_ids(repo: Path) -> set[str]:
    sense_ids: set[str] = set()
    path = repo / "knowledge/lexicon/term-senses.jsonl"
    if not path.exists():
        return sense_ids
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            sid = rec.get("sense_id")
            if sid:
                sense_ids.add(str(sid))
    return sense_ids


def term_ref_to_sense_id(ref: Any) -> str | None:
    """Convert term:<term>:sNN relation refs to term:<term>:sNN W3 sense IDs."""
    if not isinstance(ref, str):
        return None
    if not re.fullmatch(r"term:.+:s\d{2}", ref):
        return None
    return ref


def add_error(errors: list[dict[str, Any]], line: int, rid: str, kind: str, **detail: Any) -> None:
    item: dict[str, Any] = {"line": line, "relation_id": rid, "kind": kind}
    item.update(detail)
    errors.append(item)


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate W5 relation-assets.jsonl evidence.")
    ap.add_argument("--repo", default=".", help="repository root")
    ap.add_argument(
        "--relations",
        default="knowledge/relations/relation-assets.jsonl",
        help="relation assets JSONL path relative to repo",
    )
    ap.add_argument("--batch-id", help="validate only records with this batch_id")
    ap.add_argument("--min-count", type=int, default=1, help="minimum checked relation count")
    ap.add_argument(
        "--require-type-min",
        type=int,
        default=1,
        help="minimum examples required for every controlled relation type among checked records",
    )
    ap.add_argument(
        "--enforce-type-coverage",
        action="store_true",
        help="also enforce all controlled relation types when --batch-id is used",
    )
    ap.add_argument("--json", action="store_true", help="emit machine-readable summary")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    segments = load_segments(repo)
    sense_ids = load_sense_ids(repo)
    path = repo / args.relations

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    checked_records = 0
    checked_quotes = 0
    ids: set[str] = set()
    type_counts: collections.Counter[str] = collections.Counter()

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
            rid = str(rec.get("relation_id", ""))

            if rid in ids:
                add_error(errors, lineno, rid, "duplicate_relation_id")
            ids.add(rid)

            for field in REQUIRED_FIELDS:
                value = rec.get(field)
                if value is None or value == "" or value == []:
                    add_error(errors, lineno, rid, "empty_required_field", field=field)

            relation_type = rec.get("relation_type")
            if relation_type not in REQUIRED_TYPES:
                add_error(errors, lineno, rid, "bad_relation_type", relation_type=relation_type)
            else:
                type_counts[str(relation_type)] += 1

            if rec.get("status") != "draft":
                add_error(errors, lineno, rid, "non_draft_status", status=rec.get("status"))

            for pos_field in ("source_position", "target_position"):
                pos = rec.get(pos_field)
                if pos and not (repo / f"knowledge/position-cards/{pos}.md").exists():
                    add_error(errors, lineno, rid, "position_card_missing", field=pos_field, position=pos)

            for ref_field in ("source", "target"):
                sid = term_ref_to_sense_id(rec.get(ref_field))
                if sid and sid not in sense_ids:
                    add_error(errors, lineno, rid, "term_sense_ref_missing", field=ref_field, sense_id=sid)

            source_senses = rec.get("source_senses", [])
            if source_senses and not isinstance(source_senses, list):
                add_error(errors, lineno, rid, "bad_source_senses_type")
                source_senses = []
            for ref in source_senses:
                sid = term_ref_to_sense_id(ref)
                if sid and sid not in sense_ids:
                    add_error(errors, lineno, rid, "source_sense_missing", sense_id=sid)

            for prose_field in ("definition", "applicability_boundary", "forbidden_interpretation"):
                prose = str(rec.get(prose_field, ""))
                if "必然" in prose:
                    add_error(errors, lineno, rid, "overstrong_relation_prose", field=prose_field, pattern="必然")
                for pattern in FORBIDDEN_PATTERNS:
                    if pattern in prose:
                        add_error(errors, lineno, rid, "forbidden_pattern", field=prose_field, pattern=pattern)

            evidence_segment = rec.get("evidence_segment")
            if not isinstance(evidence_segment, list) or not evidence_segment:
                add_error(errors, lineno, rid, "missing_evidence_segment")
                evidence_segment = []

            if rec.get("evidence") and rec.get("evidence") != rec.get("evidence_segment"):
                warnings.append({"line": lineno, "relation_id": rid, "kind": "evidence_alias_differs"})

            for ev in evidence_segment:
                checked_quotes += 1
                if not isinstance(ev, dict):
                    add_error(errors, lineno, rid, "bad_evidence_item", evidence=ev)
                    continue
                try:
                    row_id = int(ev.get("row_id"))
                except Exception:
                    add_error(errors, lineno, rid, "bad_evidence_row", evidence=ev)
                    continue
                quote = str(ev.get("quote", "")).strip()
                if not quote:
                    add_error(errors, lineno, rid, "empty_evidence_quote", row_id=row_id)
                    continue
                if row_id not in segments:
                    add_error(errors, lineno, rid, "evidence_row_not_in_manifest", row_id=row_id)
                    continue
                segment_id = ev.get("segment_id")
                expected_segment_id = segments[row_id].get("segment_id")
                if segment_id and segment_id != expected_segment_id:
                    add_error(
                        errors,
                        lineno,
                        rid,
                        "segment_id_mismatch",
                        row_id=row_id,
                        segment_id=segment_id,
                        expected_segment_id=expected_segment_id,
                    )
                clean_rel = segments[row_id]["source_paths"]["clean_md_relpath"]
                clean_path = repo / clean_rel
                if not clean_path.exists():
                    add_error(errors, lineno, rid, "quote_clean_path_missing", row_id=row_id, path=clean_rel)
                    continue
                text = clean_path.read_text(encoding="utf-8")
                if quote not in text:
                    add_error(
                        errors,
                        lineno,
                        rid,
                        "quote_not_found",
                        row_id=row_id,
                        quote_prefix=quote[:80],
                    )

    if checked_records < args.min_count:
        errors.append({"kind": "too_few_relations", "count": checked_records, "min_count": args.min_count})

    enforce_type_coverage = bool(args.enforce_type_coverage or not args.batch_id)
    missing_types = sorted(REQUIRED_TYPES - set(type_counts)) if enforce_type_coverage else []
    for relation_type in missing_types:
        errors.append({"kind": "missing_relation_type", "relation_type": relation_type})

    low_types: dict[str, int] = {}
    if enforce_type_coverage:
        low_types = {
            relation_type: count
            for relation_type, count in sorted(type_counts.items())
            if count < args.require_type_min
        }
        for relation_type, count in low_types.items():
            errors.append(
                {
                    "kind": "relation_type_below_min",
                    "relation_type": relation_type,
                    "count": count,
                    "required": args.require_type_min,
                }
            )

    summary = {
        "checked_records": checked_records,
        "checked_quotes": checked_quotes,
        "type_counts": dict(sorted(type_counts.items())),
        "type_coverage_enforced": enforce_type_coverage,
        "missing_types": missing_types,
        "type_min_required": args.require_type_min,
        "types_below_min": low_types,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"W5 validation: records={checked_records}, quotes={checked_quotes}, "
            f"types={len(type_counts)}/12, errors={len(errors)}, warnings={len(warnings)}"
        )
        print("type_counts=" + json.dumps(dict(sorted(type_counts.items())), ensure_ascii=False))
        for err in errors[:80]:
            print("ERROR", json.dumps(err, ensure_ascii=False))
        for warn in warnings[:30]:
            print("WARN", json.dumps(warn, ensure_ascii=False))

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
