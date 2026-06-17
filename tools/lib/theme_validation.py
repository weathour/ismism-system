#!/usr/bin/env python3
"""Shared product-era theme validators."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except Exception as exc:
                raise ValueError(f"{path}:{lineno}: JSON parse failed: {exc}") from exc
            if not isinstance(obj, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            out.append(obj)
    return out


def find_one(theme_dir: Path, pattern: str) -> Path:
    hits = sorted(theme_dir.glob(pattern))
    if not hits:
        raise FileNotFoundError(f"missing {pattern} in {theme_dir}")
    return hits[0]


def validate_theme(repo: Path, slug: str, check_quotes: bool = True) -> dict[str, Any]:
    errors: list[str] = []
    theme_dir = repo / "library" / "themes" / slug
    if not theme_dir.is_dir():
        return {"status": "FAIL", "theme": slug, "errors": [f"missing theme directory: {theme_dir.relative_to(repo)}"]}

    readme = theme_dir / "README.md"
    if not readme.is_file():
        errors.append(f"missing README.md for {slug}")

    try:
        manifest_path = find_one(theme_dir, "*row-manifest.jsonl")
        manifest = load_jsonl(manifest_path)
    except Exception as exc:
        return {"status": "FAIL", "theme": slug, "errors": [str(exc)]}

    try:
        evidence_path = find_one(theme_dir, "*evidence-bank.jsonl")
        evidence = load_jsonl(evidence_path)
    except Exception as exc:
        return {"status": "FAIL", "theme": slug, "errors": [str(exc)]}

    if not manifest:
        errors.append(f"{manifest_path.relative_to(repo)} is empty")
    if not evidence:
        errors.append(f"{evidence_path.relative_to(repo)} is empty")

    manifest_rows = set()
    for i, rec in enumerate(manifest, 1):
        row_id = rec.get("row_id")
        if row_id is None:
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: missing row_id")
            continue
        try:
            manifest_rows.add(int(row_id))
        except (TypeError, ValueError):
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: row_id not integer: {row_id!r}")
        clean = rec.get("clean_md_path") or rec.get("source_clean_path")
        if clean and not (repo / str(clean)).is_file():
            errors.append(f"{manifest_path.relative_to(repo)}:{i}: clean path missing: {clean}")

    evidence_rows = set()
    evidence_ids: set[str] = set()
    exact_checked = 0
    for i, rec in enumerate(evidence, 1):
        row_id = rec.get("row_id")
        if row_id is None:
            errors.append(f"{evidence_path.relative_to(repo)}:{i}: missing row_id")
        else:
            try:
                evidence_rows.add(int(row_id))
            except (TypeError, ValueError):
                errors.append(f"{evidence_path.relative_to(repo)}:{i}: row_id not integer: {row_id!r}")
        ev_id = str(rec.get("evidence_id", "")).strip()
        if ev_id:
            if ev_id in evidence_ids:
                errors.append(f"{evidence_path.relative_to(repo)}:{i}: duplicate evidence_id {ev_id}")
            evidence_ids.add(ev_id)
        clean = rec.get("clean_md_path") or rec.get("source_clean_path")
        quote = rec.get("quote")
        if check_quotes and quote:
            if not clean:
                errors.append(f"{evidence_path.relative_to(repo)}:{i}: quote record missing clean_md_path")
                continue
            clean_path = repo / str(clean)
            if not clean_path.is_file():
                errors.append(f"{evidence_path.relative_to(repo)}:{i}: clean path missing: {clean}")
                continue
            text = clean_path.read_text(encoding="utf-8")
            if str(quote) not in text:
                errors.append(f"{evidence_path.relative_to(repo)}:{i}: quote not exact substring for row {row_id}")
            else:
                exact_checked += 1

    missing_in_manifest = sorted(evidence_rows - manifest_rows)
    if missing_in_manifest:
        errors.append(f"evidence rows not present in manifest: {missing_in_manifest[:20]}")

    syntheses = sorted(p.name for p in theme_dir.glob("*synthesis.md"))
    taxonomy = sorted(p.name for p in theme_dir.glob("*taxonomy.md"))
    notes = sorted(p.name for p in theme_dir.glob("*concept-relation-notes.md"))
    summary = {
        "status": "PASS" if not errors else "FAIL",
        "theme": slug,
        "manifest": manifest_path.relative_to(repo).as_posix(),
        "manifest_rows": len(manifest),
        "unique_manifest_rows": len(manifest_rows),
        "evidence_bank": evidence_path.relative_to(repo).as_posix(),
        "evidence_records": len(evidence),
        "exact_quotes_checked": exact_checked,
        "syntheses": syntheses,
        "taxonomy_files": taxonomy,
        "concept_relation_notes": notes,
        "errors": errors,
    }
    return summary


def main(slug: str, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"Validate the {slug} theme package")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true", help="accepted for compatibility; product validator is data-based")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--skip-quote-check", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    summary = validate_theme(repo, slug, check_quotes=not args.skip_quote_check)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"validate_theme[{slug}]: {summary['status']} "
            f"manifest={summary.get('manifest_rows')} evidence={summary.get('evidence_records')} "
            f"quotes={summary.get('exact_quotes_checked')} syntheses={len(summary.get('syntheses', []))} "
            f"errors={len(summary.get('errors', []))}"
        )
        for err in summary.get("errors", [])[:80]:
            print("ERROR", err)
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: theme_validation.py <slug> [--repo .]", file=sys.stderr)
        raise SystemExit(2)
    slug = sys.argv[1]
    raise SystemExit(main(slug, sys.argv[2:]))
