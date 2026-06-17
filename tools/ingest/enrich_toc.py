#!/usr/bin/env python3
"""Populate derived PDF-slice and raw-markdown references in the corpus registry."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from slice_source_pdf import build_output_path, load_rows


def find_repo_root(csv_path: Path, *paths: Path) -> Path:
    for path in (csv_path, *paths):
        for parent in (path, *path.parents):
            if (parent / "corpus").is_dir() and (parent / "library").is_dir():
                return parent
    # Product default: corpus/registry/toc.csv -> repository root.
    if csv_path.parent.name == "registry" and csv_path.parent.parent.name == "corpus":
        return csv_path.parent.parent.parent
    return Path.cwd().resolve()


def repo_rel(path: Path, repo: Path) -> str:
    try:
        return path.relative_to(repo).as_posix()
    except ValueError:
        return path.as_posix()

def enrich_csv(csv_path: Path, pdf_slices_dir: Path, raw_markdown_dir: Path) -> None:
    repo_root = find_repo_root(csv_path, pdf_slices_dir, raw_markdown_dir)
    rows = load_rows(csv_path)
    rows_by_id = {row["row_id"]: row for row in rows}

    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        original_rows = list(reader)

    canonical_fields = [
        "pdf_slice_relpath",
        "corpus/raw-markdown_relpath",
        "pdf_slice_exists",
        "corpus/raw-markdown_exists",
    ]
    deprecated_fields = {"raw_markdown_relpath", "raw_markdown_exists"}
    fieldnames = [field for field in fieldnames if field not in deprecated_fields]
    for field in canonical_fields:
        if field not in fieldnames:
            fieldnames.append(field)

    enriched_rows: list[dict] = []
    for original_row in original_rows:
        row_id = int(original_row["row_id"])
        parsed_row = rows_by_id[row_id]

        pdf_path = build_output_path(pdf_slices_dir, rows_by_id, parsed_row)
        md_path = raw_markdown_dir / pdf_path.relative_to(pdf_slices_dir).with_suffix(".md")

        original_row.pop("raw_markdown_relpath", None)
        original_row.pop("raw_markdown_exists", None)
        original_row["pdf_slice_relpath"] = repo_rel(pdf_path, repo_root) if pdf_path.exists() else ""
        original_row["corpus/raw-markdown_relpath"] = repo_rel(md_path, repo_root)
        original_row["pdf_slice_exists"] = "true" if pdf_path.exists() else "false"
        original_row["corpus/raw-markdown_exists"] = "true" if md_path.exists() else "false"
        enriched_rows.append(original_row)

    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_rows)

    print(f"enriched {len(enriched_rows)} rows in {csv_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Populate derived registry paths for source slices and raw markdown.")
    parser.add_argument("--csv", default="corpus/registry/toc.csv", help="Corpus registry CSV path.")
    parser.add_argument("--pdf-slices-dir", default="corpus/pdf-slices", help="Derived PDF slice root.")
    parser.add_argument("--raw-markdown-dir", default="corpus/raw-markdown", help="Raw markdown root.")
    args = parser.parse_args()

    enrich_csv(Path(args.csv).resolve(), Path(args.pdf_slices_dir).resolve(), Path(args.raw_markdown_dir).resolve())


if __name__ == "__main__":
    main()
