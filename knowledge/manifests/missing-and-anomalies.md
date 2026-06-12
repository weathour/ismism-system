# W1 Missing and Anomalies Report

- generated_at: `2026-05-08T18:08:03+08:00`
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
- `split_pdf/` directory exists: **True**

## Blocking Missing Text Segment

No missing raw/clean text segments detected.

## Derived Layer Anomaly: `split_pdf/` partial

`split_pdf/` is a regenerable derived layer and currently contains only the recovered point for row 176:
- `2-4-2-4` (`0176_..._p4607.pdf`) exists.

All other rows are not yet regenerated in PDF slice form.

## Stale CSV Existence Flags

- stale `split_md_exists` flags: **0**
- stale `split_pdf_exists` flags: **362**

## Path Integrity

- raw referenced but missing: **0**
- clean referenced but missing: **0**
- raw actual but not referenced: **0**
- clean actual but not referenced: **0**

## Structural Noise, not errors

Duplicate `toc_id` values detected: **13**. These correspond to review/auxiliary rows sharing matrix positions and are retained as distinct `segment_id`s.

## Notes for downstream agents

- `split_md` 与 `split_md_clean` 已恢复为 `text_status=available`。
- 先进行 W2 时，请按 `segments.jsonl` 作为结构注册表，不以该文件中的旧注释替代实际 `text_status`。
