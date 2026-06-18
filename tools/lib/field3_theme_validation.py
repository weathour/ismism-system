#!/usr/bin/env python3
"""Specialized Field 3 theme validators layered over exact-quote validation."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from theme_validation import load_jsonl, validate_theme

ALLOWED_ROLES = {"core", "bridge", "context", "excluded"}


def find_one(theme_dir: Path, pattern: str) -> Path:
    hits = sorted(theme_dir.glob(pattern))
    if not hits:
        raise FileNotFoundError(f"missing {pattern} in {theme_dir}")
    return hits[0]




def parse_int_field(value: Any, label: str) -> tuple[int | None, str | None]:
    if value is None:
        return None, f"missing {label}"
    try:
        return int(str(value)), None
    except (TypeError, ValueError):
        return None, f"invalid {label} {value!r}"


def parse_taxonomy_rows(text: str) -> dict[str, list[int]]:
    out: dict[str, list[int]] = {}
    for line in text.splitlines():
        m = re.match(r"^- ([a-z0-9-]+): rows (.+)$", line.strip())
        if not m:
            continue
        cls = m.group(1)
        ids = [int(x) for x in re.findall(r"\d+", m.group(2))]
        out[cls] = ids
    return out


def validate_field3_theme(repo: Path, slug: str, allowed_classes: list[str], final: bool = False) -> dict[str, Any]:
    summary = validate_theme(repo, slug, check_quotes=True)
    errors = list(summary.get("errors", []))
    theme_dir = repo / "library" / "themes" / slug
    allowed = set(allowed_classes)

    try:
        manifest_path = find_one(theme_dir, "*row-manifest.jsonl")
        evidence_path = find_one(theme_dir, "*evidence-bank.jsonl")
        taxonomy_path = find_one(theme_dir, "*taxonomy.md")
        notes_path = find_one(theme_dir, "*concept-relation-notes.md")
        synthesis_path = find_one(theme_dir, "*synthesis.md")
        readme_path = theme_dir / "README.md"
        manifest = load_jsonl(manifest_path)
        evidence = load_jsonl(evidence_path)
    except Exception as exc:
        errors.append(str(exc))
        summary["status"] = "FAIL"
        summary["errors"] = errors
        return summary

    row_ids: list[int] = []
    for i, rec in enumerate(manifest, 1):
        row_id = rec.get("row_id")
        row_id_int, row_id_error = parse_int_field(row_id, "row_id")
        if row_id_error or row_id_int is None:
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: {row_id_error}")
            continue
        row_ids.append(row_id_int)
        cls = rec.get("theme_class")
        role = rec.get("theme_role") or rec.get("core_status")
        if cls not in allowed:
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: invalid theme_class {cls!r}")
        if role not in ALLOWED_ROLES:
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: invalid theme_role/core_status {role!r}")
        if str(rec.get("segment_id")) != f"ismism:seg:{row_id_int}":
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: segment_id does not match row_id")
    duplicates = sorted({rid for rid in row_ids if row_ids.count(rid) > 1})
    if duplicates:
        errors.append(f"manifest duplicate row ids: {duplicates}")

    manifest_rows = set(row_ids)
    ev_counts: dict[int, int] = {}
    for i, rec in enumerate(evidence, 1):
        rid, row_id_error = parse_int_field(rec.get("row_id"), "row_id")
        if row_id_error or rid is None:
            errors.append(f"{evidence_path.relative_to(repo)}:{i}: {row_id_error}")
            continue
        ev_counts[rid] = ev_counts.get(rid, 0) + 1
        cls = rec.get("theme_class")
        role = rec.get("theme_role")
        if cls not in allowed:
            errors.append(f"{evidence_path.relative_to(repo)}:{i}: invalid theme_class {cls!r}")
        if role not in ALLOWED_ROLES:
            errors.append(f"{evidence_path.relative_to(repo)}:{i}: invalid theme_role {role!r}")
    missing_evidence = sorted(rid for rid in manifest_rows if ev_counts.get(rid, 0) == 0)
    if missing_evidence:
        errors.append(f"manifest rows without evidence: {missing_evidence}")

    taxonomy_text = taxonomy_path.read_text(encoding="utf-8")
    taxonomy_rows = parse_taxonomy_rows(taxonomy_text)
    if not taxonomy_rows:
        errors.append(f"{taxonomy_path.relative_to(repo)}: no row ownership map lines found")
    seen: dict[int, list[str]] = {}
    for cls, ids in taxonomy_rows.items():
        if cls not in allowed:
            errors.append(f"{taxonomy_path.relative_to(repo)}: unknown taxonomy class {cls}")
        for rid in ids:
            seen.setdefault(rid, []).append(cls)
    duplicated_tax = {rid: clss for rid, clss in seen.items() if len(clss) > 1}
    if duplicated_tax:
        errors.append(f"taxonomy duplicate row ownership: {duplicated_tax}")
    tax_rows = set(seen)
    if tax_rows != manifest_rows:
        errors.append(f"taxonomy rows do not match manifest rows: missing={sorted(manifest_rows-tax_rows)} extra={sorted(tax_rows-manifest_rows)}")

    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    for required in [f"tools/validate/themes/{slug.replace('-', '_')}.py", f"tools/query/themes/{slug.replace('-', '_')}.py"]:
        if required not in readme:
            errors.append(f"README missing reference to {required}")
    notes = notes_path.read_text(encoding="utf-8")
    if "deferred" not in notes and "defer" not in notes:
        errors.append(f"{notes_path.relative_to(repo)} should record deferred curated batches or batch ids")
    synthesis = synthesis_path.read_text(encoding="utf-8")
    if "ev:" not in synthesis or "Rows:" not in synthesis:
        errors.append(f"{synthesis_path.relative_to(repo)} lacks evidence ids or row references")

    if final:
        if len(manifest) < 30:
            errors.append(f"final mode requires at least 30 reviewed rows, got {len(manifest)}")
        if len(evidence) < 50:
            errors.append(f"final mode requires at least 50 evidence records, got {len(evidence)}")
        roles = {str(rec.get("theme_role") or rec.get("core_status")) for rec in manifest}
        for needed in ["core", "bridge", "context", "excluded"]:
            if needed not in roles:
                errors.append(f"final mode missing role {needed}")

    summary.update({
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "allowed_classes": allowed_classes,
        "taxonomy_rows": len(tax_rows) if 'tax_rows' in locals() else 0,
    })
    return summary


def main(slug: str, allowed_classes: list[str], argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"Validate Field 3 theme package {slug}")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    summary = validate_field3_theme(repo, slug, allowed_classes, final=args.final)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"validate_field3_theme[{slug}]: {summary['status']} "
            f"manifest={summary.get('manifest_rows')} evidence={summary.get('evidence_records')} "
            f"quotes={summary.get('exact_quotes_checked')} taxonomy_rows={summary.get('taxonomy_rows')} "
            f"errors={len(summary.get('errors', []))}"
        )
        for err in summary.get("errors", [])[:120]:
            print("ERROR", err)
    return 0 if summary["status"] == "PASS" else 1
