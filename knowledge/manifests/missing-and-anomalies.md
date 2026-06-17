# W1 Missing and Anomalies Report

- generated_at: `2026-06-17T12:54:31+08:00`
- record_status: `canonical`
- repository: `/home/weathour/文档/ismism-system`

## Summary

- TOC rows registered: **363**
- `segments.jsonl` records: **363**
- segments with available raw+clean text: **363**
- segments missing raw or clean text: **0**
- `chunks.jsonl` records: **1594** across **363** segments
- actual `split_md/*.md`: **363**
- actual `split_md_clean/*.md`: **363**
- `split_pdf/` directory exists: **False**

## Blocking Missing Text Segment

No missing raw/clean text segments detected.

## Derived Layer Status: `split_pdf/` absent

`split_pdf/` is intentionally absent in this repository after project cleanup. It remains a regenerable PDF-slice derived layer, not an interpretation source and not a raw/clean text source. `split_pdf_exists` in the CSV should reflect actual filesystem state; rows stay `0` unless the PDF slices are explicitly regenerated.

## Stale CSV Existence Flags

- stale `split_md_exists` flags: **0**
- stale `split_pdf_exists` flags: **0**

## Path Integrity

- raw referenced but missing: **0**
- clean referenced but missing: **0**
- raw actual but not referenced: **0**
- clean actual but not referenced: **0**

## Structural Noise, not errors

Duplicate `toc_id` values detected: **13**. These correspond to review/auxiliary rows sharing matrix positions and are retained as distinct `segment_id`s.

## Rule for downstream agents

Use `segments.jsonl` as the structural registry. Do not treat `split_pdf/` absence as a missing text segment. Row 176 / `2-4-2-4` remains available through raw/clean Markdown; regenerate PDF slices only if a future task explicitly needs that derived layer.
