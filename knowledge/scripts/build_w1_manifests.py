#!/usr/bin/env python3
"""Build W1 corpus manifests for ISMISM knowledge digestion.

This script treats `目录索引_结构化.csv` as the TOC source and verifies
actual filesystem state for split_md, split_md_clean, split_pdf, and the
root PDF. Only corpus and clean-text layers are modeled as source inputs.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE = ROOT / "knowledge"
MANIFESTS = KNOWLEDGE / "manifests"
CSV_PATH = ROOT / "目录索引_结构化.csv"
SOURCE_PDF_NAME = "主义主义 (未明子) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
SOURCE_PDF = ROOT / SOURCE_PDF_NAME
SCHEMA_SEGMENTS = "ismism.w1.segments.v1"
SCHEMA_CHUNKS = "ismism.w1.chunks.v1"
SCHEMA_CORPUS = "ismism.w1.corpus-manifest.v1"
GENERATED_AT = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def as_int(value: str | None) -> Optional[int]:
    if value is None or value == "":
        return None
    return int(value)


def file_info(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists() or not path.is_file():
        return None
    data = path.read_bytes()
    text = data.decode("utf-8", errors="replace")
    return {
        "relpath": rel(path),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "line_count": text.count("\n") + (0 if text.endswith("\n") else 1),
        "char_count": len(text),
    }


def count_files(directory: Path, pattern: str = "*") -> int:
    if not directory.exists():
        return 0
    return sum(1 for p in directory.rglob(pattern) if p.is_file())


def read_rows() -> List[Dict[str, str]]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def matrix_axes(toc_id: str) -> Dict[str, Any]:
    parts = [p for p in toc_id.split("-") if p]
    names = ["field", "ontology", "epistemology", "teleology"]
    axes = {name: (parts[i] if i < len(parts) else None) for i, name in enumerate(names)}
    return {
        **axes,
        "axis_count": len(parts),
        "is_numbered": bool(parts) and all(p.isdigit() for p in parts),
        "is_four_axis_position": len(parts) == 4 and all(p.isdigit() for p in parts),
    }


def split_path_list(value: str) -> List[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(" / ")]


def build_segments(rows: List[Dict[str, str]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    segments: List[Dict[str, Any]] = []
    anomalies: List[Dict[str, Any]] = []

    for row in rows:
        row_id = as_int(row.get("row_id"))
        assert row_id is not None
        raw_rel = row["split_md_relpath"]
        clean_rel = raw_rel.replace("split_md/", "split_md_clean/", 1)
        pdf_rel = row["split_pdf_relpath"]
        raw_path = ROOT / raw_rel
        clean_path = ROOT / clean_rel
        split_pdf_path = ROOT / pdf_rel

        raw_exists = raw_path.exists() and raw_path.is_file()
        clean_exists = clean_path.exists() and clean_path.is_file()
        split_pdf_file_exists = split_pdf_path.exists() and split_pdf_path.is_file()
        split_pdf_dir_exists = (ROOT / "split_pdf").exists()
        source_pdf_exists = SOURCE_PDF.exists()

        missing_reasons: List[str] = []
        if not raw_exists:
            missing_reasons.append("raw_md_missing")
        if not clean_exists:
            missing_reasons.append("clean_md_missing")
        if not split_pdf_dir_exists:
            # This is corpus-level derived-layer absence, not segment-level text failure.
            pass
        elif not split_pdf_file_exists:
            missing_reasons.append("split_pdf_file_missing")

        text_status = "available" if raw_exists and clean_exists else "missing_text"
        record: Dict[str, Any] = {
            "schema_version": SCHEMA_SEGMENTS,
            "record_status": "canonical",
            "segment_id": f"ismism:seg:{row_id}",
            "row_id": row_id,
            "toc_id": row.get("toc_id") or None,
            "toc_depth": as_int(row.get("toc_depth")),
            "tree_level": as_int(row.get("tree_level")),
            "title": row.get("title") or "",
            "parent_row_id": as_int(row.get("parent_row_id")),
            "parent_toc_id": row.get("parent_toc_id") or None,
            "path_titles": split_path_list(row.get("path_titles", "")),
            "path_ids": split_path_list(row.get("path_ids", "")),
            "page_start": as_int(row.get("page_start")),
            "next_page_start": as_int(row.get("next_page_start")),
            "page_end_inferred": (as_int(row.get("next_page_start")) - 1) if as_int(row.get("next_page_start")) is not None else None,
            "line_number": as_int(row.get("line_number")),
            "safe_title": row.get("safe_title") or "",
            "safe_toc_id": row.get("safe_toc_id") or "",
            "file_stub": row.get("file_stub") or "",
            "matrix_axes": matrix_axes(row.get("toc_id") or ""),
            "source_paths": {
                "csv_split_md_relpath": raw_rel,
                "raw_md_relpath": raw_rel,
                "clean_md_relpath": clean_rel,
                "split_pdf_relpath": pdf_rel,
                "source_pdf_relpath": SOURCE_PDF_NAME,
            },
            "existence": {
                "raw_md": raw_exists,
                "clean_md": clean_exists,
                "split_pdf_dir": split_pdf_dir_exists,
                "split_pdf_file": split_pdf_file_exists,
                "source_pdf": source_pdf_exists,
                "csv_split_md_exists_flag": row.get("split_md_exists"),
                "csv_split_pdf_exists_flag": row.get("split_pdf_exists"),
            },
            "text_status": text_status,
            "missing_reasons": missing_reasons,
            "raw_md": file_info(raw_path),
            "clean_md": file_info(clean_path),
        }
        segments.append(record)

        if text_status != "available":
            anomalies.append({
                "type": "missing_text_segment",
                "severity": "blocking_for_segment_card",
                "segment_id": record["segment_id"],
                "row_id": row_id,
                "toc_id": record["toc_id"],
                "title": record["title"],
                "page_start": record["page_start"],
                "raw_md_relpath": raw_rel,
                "clean_md_relpath": clean_rel,
                "missing_reasons": missing_reasons,
            })
        if row.get("split_md_exists") == "1" and not raw_exists:
            anomalies.append({
                "type": "stale_csv_flag",
                "severity": "warning",
                "field": "split_md_exists",
                "csv_value": row.get("split_md_exists"),
                "actual_value": raw_exists,
                "segment_id": record["segment_id"],
                "row_id": row_id,
                "toc_id": record["toc_id"],
                "title": record["title"],
            })
        if row.get("split_pdf_exists") == "1" and not split_pdf_file_exists:
            anomalies.append({
                "type": "stale_csv_flag",
                "severity": "expected_due_to_absent_split_pdf_dir" if not split_pdf_dir_exists else "warning",
                "field": "split_pdf_exists",
                "csv_value": row.get("split_pdf_exists"),
                "actual_value": split_pdf_file_exists,
                "segment_id": record["segment_id"],
                "row_id": row_id,
                "toc_id": record["toc_id"],
                "title": record["title"],
            })

    return segments, anomalies


def markdown_chunks(text: str, max_chars: int = 3000) -> List[str]:
    # Keep page markers with following text. Preamble before first page marker is retained.
    blocks = re.split(r"(?m)(?=^## Page\s+\d+\s*$)", text)
    chunks: List[str] = []
    current = ""

    def flush() -> None:
        nonlocal current
        if current.strip():
            chunks.append(current.strip() + "\n")
        current = ""

    for block in blocks:
        if not block.strip():
            continue
        if len(block) > max_chars:
            flush()
            paras = re.split(r"\n\s*\n", block)
            buf = ""
            for para in paras:
                para = para.strip()
                if not para:
                    continue
                if len(para) > max_chars:
                    if buf:
                        chunks.append(buf.strip() + "\n")
                        buf = ""
                    # Hard split very long paragraphs by Chinese/English sentence-ish boundaries.
                    sentences = re.split(r"(?<=[。！？!?；;])", para)
                    small = ""
                    for sent in sentences:
                        if len(small) + len(sent) + 1 > max_chars and small:
                            chunks.append(small.strip() + "\n")
                            small = ""
                        small += sent
                    if small.strip():
                        chunks.append(small.strip() + "\n")
                elif len(buf) + len(para) + 2 > max_chars and buf:
                    chunks.append(buf.strip() + "\n")
                    buf = para
                else:
                    buf = (buf + "\n\n" + para).strip() if buf else para
            if buf.strip():
                chunks.append(buf.strip() + "\n")
        elif len(current) + len(block) + 2 > max_chars and current:
            flush()
            current = block
        else:
            current = (current + "\n" + block).strip() if current else block
    flush()
    return chunks


def build_chunks(segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = []
    for seg in segments:
        if seg["text_status"] != "available":
            continue
        clean_rel = seg["source_paths"]["clean_md_relpath"]
        clean_path = ROOT / clean_rel
        text = clean_path.read_text(encoding="utf-8", errors="replace")
        parts = markdown_chunks(text)
        cursor = 0
        for idx, part in enumerate(parts, 1):
            pos = text.find(part.strip(), cursor)
            if pos < 0:
                pos = None
                end = None
            else:
                end = pos + len(part.strip())
                cursor = end
            page_markers = [int(x) for x in re.findall(r"(?m)^## Page\s+(\d+)\s*$", part)]
            chunks.append({
                "schema_version": SCHEMA_CHUNKS,
                "record_status": "canonical",
                "chunk_id": f"{seg['segment_id']}:chunk:{idx}",
                "segment_id": seg["segment_id"],
                "row_id": seg["row_id"],
                "toc_id": seg["toc_id"],
                "title": seg["title"],
                "chunk_index": idx,
                "chunk_count": len(parts),
                "clean_md_relpath": clean_rel,
                "char_start": pos,
                "char_end": end,
                "char_count": len(part),
                "page_markers_in_chunk": page_markers,
                "text": part,
            })
    return chunks



def write_jsonl(path: Path, records: Iterable[Dict[str, Any]]) -> int:
    count = 0
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False, sort_keys=False) + "\n")
            count += 1
    return count


def build_manifest(rows: List[Dict[str, str]], segments: List[Dict[str, Any]], chunks: List[Dict[str, Any]], anomalies: List[Dict[str, Any]]) -> Dict[str, Any]:
    raw_actual = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "split_md").rglob("*.md")) if (ROOT / "split_md").exists() else []
    clean_actual = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "split_md_clean").rglob("*.md")) if (ROOT / "split_md_clean").exists() else []
    raw_referenced = {s["source_paths"]["raw_md_relpath"] for s in segments}
    clean_referenced = {s["source_paths"]["clean_md_relpath"] for s in segments}
    raw_existing_referenced = {s["source_paths"]["raw_md_relpath"] for s in segments if s["existence"]["raw_md"]}
    clean_existing_referenced = {s["source_paths"]["clean_md_relpath"] for s in segments if s["existence"]["clean_md"]}
    duplicate_toc = {k: v for k, v in Counter(s["toc_id"] for s in segments).items() if k and v > 1}
    top_counter = Counter((s["toc_id"].split("-")[0] if s["toc_id"] else "") for s in segments)
    top_available_counter = Counter((s["toc_id"].split("-")[0] if s["toc_id"] else "") for s in segments if s["text_status"] == "available")
    missing_text = [s for s in segments if s["text_status"] != "available"]

    return {
        "schema_version": SCHEMA_CORPUS,
        "record_status": "canonical",
        "generated_at": GENERATED_AT,
        "repository_root": str(ROOT),
        "objective": "W1 corpus manifest: fix TOC rows, actual text-slice existence, missing/anomaly status, and retrieval chunks.",
        "source_truth_layers": {
            "primary": ["目录索引_结构化.csv", "split_md/", "split_md_clean/", SOURCE_PDF_NAME],
            "derived_absent": ["split_pdf/"],
        },
        "source_files": {
            "toc_csv": file_info(CSV_PATH),
            "source_pdf": file_info(SOURCE_PDF),
        },
        "directory_inventory": {
            "split_md_file_count": len(raw_actual),
            "split_md_clean_file_count": len(clean_actual),
            "split_pdf_dir_exists": (ROOT / "split_pdf").exists(),
            "split_pdf_file_count": count_files(ROOT / "split_pdf"),
        },
        "counts": {
            "toc_rows": len(rows),
            "segments_total": len(segments),
            "segments_available_text": sum(1 for s in segments if s["text_status"] == "available"),
            "segments_missing_text": len(missing_text),
            "chunks_total": len(chunks),
            "segments_with_chunks": len({c["segment_id"] for c in chunks}),
            "raw_md_referenced": len(raw_referenced),
            "raw_md_existing_referenced": len(raw_existing_referenced),
            "clean_md_referenced": len(clean_referenced),
            "clean_md_existing_referenced": len(clean_existing_referenced),
            "raw_md_extra_actual_not_referenced": len(set(raw_actual) - raw_referenced),
            "clean_md_extra_actual_not_referenced": len(set(clean_actual) - clean_referenced),
            "duplicate_toc_id_count": len(duplicate_toc),
            "anomaly_records": len(anomalies),
        },
        "distributions": {
            "tree_level": dict(sorted(Counter(str(s["tree_level"]) for s in segments).items())),
            "toc_depth": dict(sorted(Counter(str(s["toc_depth"]) for s in segments).items())),
            "top_level_all": dict(sorted(top_counter.items())),
            "top_level_available_text": dict(sorted(top_available_counter.items())),
        },
        "known_missing_text_segments": [
            {
                "segment_id": s["segment_id"],
                "row_id": s["row_id"],
                "toc_id": s["toc_id"],
                "title": s["title"],
                "page_start": s["page_start"],
                "raw_md_relpath": s["source_paths"]["raw_md_relpath"],
                "clean_md_relpath": s["source_paths"]["clean_md_relpath"],
                "missing_reasons": s["missing_reasons"],
            }
            for s in missing_text
        ],
        "duplicate_toc_ids": duplicate_toc,
        "path_integrity": {
            "raw_md_missing_referenced": sorted(raw_referenced - set(raw_actual)),
            "clean_md_missing_referenced": sorted(clean_referenced - set(clean_actual)),
            "raw_md_extra_actual_not_referenced": sorted(set(raw_actual) - raw_referenced),
            "clean_md_extra_actual_not_referenced": sorted(set(clean_actual) - clean_referenced),
        },
        "decisions": {
            "segment_id_scheme": "ismism:seg:<row_id>",
            "clean_md_path_scheme": "replace leading split_md/ with split_md_clean/ from CSV split_md_relpath",
            "segment_text_status": "available only when both raw_md and clean_md exist; split_pdf absence is corpus-level derived-layer absence, not segment text failure",
            "chunking": "deterministic clean-md chunks by page markers and paragraph boundaries, target max 3000 chars; chunks are retrieval units and do not alter segment truth",
        },
        "artifacts": {
            "segments_jsonl": "knowledge/manifests/segments.jsonl",
            "chunks_jsonl": "knowledge/manifests/chunks.jsonl",
            "corpus_manifest_json": "knowledge/manifests/corpus-manifest.json",
            "missing_and_anomalies_md": "knowledge/manifests/missing-and-anomalies.md",
            "build_script": "knowledge/scripts/build_w1_manifests.py",
        },
    }


def write_anomalies_md(path: Path, manifest: Dict[str, Any], anomalies: List[Dict[str, Any]]) -> None:
    missing = manifest["known_missing_text_segments"]
    lines: List[str] = []
    lines.append("# W1 Missing and Anomalies Report")
    lines.append("")
    lines.append(f"- generated_at: `{GENERATED_AT}`")
    lines.append(f"- record_status: `canonical`")
    lines.append(f"- repository: `{ROOT}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    c = manifest["counts"]
    lines.append(f"- TOC rows registered: **{c['toc_rows']}**")
    lines.append(f"- `segments.jsonl` records: **{c['segments_total']}**")
    lines.append(f"- segments with available raw+clean text: **{c['segments_available_text']}**")
    lines.append(f"- segments missing raw or clean text: **{c['segments_missing_text']}**")
    lines.append(f"- `chunks.jsonl` records: **{c['chunks_total']}** across **{c['segments_with_chunks']}** segments")
    lines.append(f"- actual `split_md/*.md`: **{manifest['directory_inventory']['split_md_file_count']}**")
    lines.append(f"- actual `split_md_clean/*.md`: **{manifest['directory_inventory']['split_md_clean_file_count']}**")
    lines.append(f"- `split_pdf/` directory exists: **{manifest['directory_inventory']['split_pdf_dir_exists']}**")
    lines.append("")
    lines.append("## Blocking Missing Text Segment")
    lines.append("")
    if missing:
        for item in missing:
            lines.append(f"### {item['segment_id']} / row {item['row_id']} / `{item['toc_id']}`")
            lines.append("")
            lines.append(f"- title: {item['title']}")
            lines.append(f"- page_start: {item['page_start']}")
            lines.append(f"- raw_md_relpath: `{item['raw_md_relpath']}`")
            lines.append(f"- clean_md_relpath: `{item['clean_md_relpath']}`")
            lines.append(f"- missing_reasons: `{', '.join(item['missing_reasons'])}`")
            lines.append("- impact: cannot generate a faithful segment card until raw/clean text is recovered or regenerated.")
            lines.append("")
    else:
        lines.append("No missing raw/clean text segments detected.")
        lines.append("")
    split_pdf_present = manifest["directory_inventory"]["split_pdf_dir_exists"]
    split_pdf_count = manifest["directory_inventory"]["split_pdf_file_count"]
    lines.append(f"## Derived Layer Status: `split_pdf/` {'present' if split_pdf_present else 'absent'}")
    lines.append("")
    if split_pdf_present:
        lines.append(f"`split_pdf/` is present with **{split_pdf_count}** files. It remains a regenerable PDF-slice derived layer, not an interpretation source and not a raw/clean text source. `split_pdf_exists` in the CSV should reflect actual filesystem state.")
    else:
        lines.append("`split_pdf/` is intentionally absent in this repository after project cleanup. It remains a regenerable PDF-slice derived layer, not an interpretation source and not a raw/clean text source. `split_pdf_exists` in the CSV should reflect actual filesystem state; rows stay `0` unless the PDF slices are explicitly regenerated.")
    lines.append("")
    lines.append("## Stale CSV Existence Flags")
    lines.append("")
    stale_md = [a for a in anomalies if a["type"] == "stale_csv_flag" and a["field"] == "split_md_exists"]
    stale_pdf = [a for a in anomalies if a["type"] == "stale_csv_flag" and a["field"] == "split_pdf_exists"]
    lines.append(f"- stale `split_md_exists` flags: **{len(stale_md)}**")
    lines.append(f"- stale `split_pdf_exists` flags: **{len(stale_pdf)}**")
    lines.append("")
    if stale_md:
        lines.append("### Stale `split_md_exists` rows")
        lines.append("")
        for a in stale_md:
            lines.append(f"- row {a['row_id']} / `{a['toc_id']}` / {a['title']}: CSV says `{a['csv_value']}`, actual `{a['actual_value']}`")
        lines.append("")
    lines.append("## Path Integrity")
    lines.append("")
    pi = manifest["path_integrity"]
    lines.append(f"- raw referenced but missing: **{len(pi['raw_md_missing_referenced'])}**")
    lines.append(f"- clean referenced but missing: **{len(pi['clean_md_missing_referenced'])}**")
    lines.append(f"- raw actual but not referenced: **{len(pi['raw_md_extra_actual_not_referenced'])}**")
    lines.append(f"- clean actual but not referenced: **{len(pi['clean_md_extra_actual_not_referenced'])}**")
    lines.append("")
    lines.append("## Structural Noise, not errors")
    lines.append("")
    lines.append(f"Duplicate `toc_id` values detected: **{manifest['counts']['duplicate_toc_id_count']}**. These correspond to review/auxiliary rows sharing matrix positions and are retained as distinct `segment_id`s.")
    lines.append("")
    lines.append("## Rule for downstream agents")
    lines.append("")
    lines.append("Use `segments.jsonl` as the structural registry. Do not treat `split_pdf/` absence as a missing text segment. Row 176 / `2-4-2-4` remains available through raw/clean Markdown; regenerate PDF slices only if a future task explicitly needs that derived layer.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    rows = read_rows()
    segments, anomalies = build_segments(rows)
    chunks = build_chunks(segments)
    manifest = build_manifest(rows, segments, chunks, anomalies)

    write_jsonl(MANIFESTS / "segments.jsonl", segments)
    write_jsonl(MANIFESTS / "chunks.jsonl", chunks)
    (MANIFESTS / "corpus-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_anomalies_md(MANIFESTS / "missing-and-anomalies.md", manifest, anomalies)

    print(json.dumps({
        "generated_at": GENERATED_AT,
        "segments": len(segments),
        "available_segments": manifest["counts"]["segments_available_text"],
        "missing_segments": manifest["counts"]["segments_missing_text"],
        "chunks": len(chunks),
        "split_pdf_dir_exists": manifest["directory_inventory"]["split_pdf_dir_exists"],
        "artifacts": manifest["artifacts"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
