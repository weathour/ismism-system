#!/usr/bin/env python3
"""Validate W1 manifest artifacts against the W1 objective."""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K = ROOT / "knowledge"
M = K / "manifests"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_jsonl(path: Path):
    out = []
    with path.open(encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            try:
                out.append(json.loads(line))
            except Exception as e:
                fail(f"{path} line {n} invalid JSON: {e}")
    return out


def main() -> None:
    required = [
        M / "corpus-manifest.json",
        M / "segments.jsonl",
        M / "chunks.jsonl",
        M / "missing-and-anomalies.md",
        K / "STATE.md",
        K / "logs" / "operation-log.md",
    ]
    for p in required:
        if not p.exists() or p.stat().st_size == 0:
            fail(f"missing or empty required artifact: {p.relative_to(ROOT)}")

    manifest = json.loads((M / "corpus-manifest.json").read_text(encoding="utf-8"))
    segments = load_jsonl(M / "segments.jsonl")
    chunks = load_jsonl(M / "chunks.jsonl")
    rows = list(csv.DictReader((ROOT / "目录索引_结构化.csv").open(encoding="utf-8-sig", newline="")))

    # 基本规模一致性
    if len(rows) != 363:
        fail(f"expected 363 CSV rows, got {len(rows)}")
    if len(segments) != 363:
        fail(f"expected 363 segments, got {len(segments)}")
    if len({s['segment_id'] for s in segments}) != 363:
        fail("segment_id values are not unique")
    if len({s['row_id'] for s in segments}) != 363:
        fail("row_id values are not unique in segments")
    if sorted(s['row_id'] for s in segments) != list(range(1, 364)):
        fail("segment row_id coverage is not 1..363")

    actual_raw = sum(1 for _ in (ROOT / "split_md").rglob("*.md"))
    actual_clean = sum(1 for _ in (ROOT / "split_md_clean").rglob("*.md"))
    if actual_raw != 363:
        fail(f"expected 363 actual split_md files, got {actual_raw}")
    if actual_clean != 363:
        fail(f"expected 363 actual split_md_clean files, got {actual_clean}")

    available = [s for s in segments if s.get("text_status") == "available"]
    missing = [s for s in segments if s.get("text_status") != "available"]
    if len(missing) != 0:
        fail(f"expected 0 missing segments after recovery, got {len(missing)}")

    row_176 = next((s for s in segments if s.get("row_id") == 176), None)
    if row_176 is None:
        fail("row 176 segment not found")
    if row_176.get("toc_id") != "2-4-2-4":
        fail(f"row 176 toc_id mismatch: {row_176.get('toc_id')}")
    if row_176.get("text_status") != "available":
        fail(f"row 176 text_status must be available after recovery, got {row_176.get('text_status')}")
    if "raw_md_missing" in row_176.get("missing_reasons", []) or "clean_md_missing" in row_176.get("missing_reasons", []):
        fail(f"row 176 should no longer have missing reasons, got {row_176.get('missing_reasons')}")

    # split_pdf is now a derived layer; once recovery starts it may become partial or complete.
    split_pdf_exists = (ROOT / "split_pdf").exists()
    split_pdf_file_count = manifest["directory_inventory"].get("split_pdf_file_count")
    if split_pdf_exists and (not isinstance(split_pdf_file_count, int) or split_pdf_file_count < 0):
        fail("invalid split_pdf_file_count in manifest")

    c = manifest["counts"]
    expected_pairs = {
        "toc_rows": 363,
        "segments_total": 363,
        "segments_available_text": 363,
        "segments_missing_text": 0,
        "raw_md_existing_referenced": 363,
        "clean_md_existing_referenced": 363,
    }
    for key, val in expected_pairs.items():
        if c.get(key) != val:
            fail(f"manifest count {key} expected {val}, got {c.get(key)}")

    available_ids = {s["segment_id"] for s in available}
    chunk_ids = [ch["chunk_id"] for ch in chunks]
    if len(chunk_ids) != len(set(chunk_ids)):
        fail("chunk_id values are not unique")
    chunked_ids = {ch["segment_id"] for ch in chunks}
    if chunked_ids != available_ids:
        fail(
            f"chunks do not exactly cover available segments; "
            f"missing={len(available_ids - chunked_ids)} extra={len(chunked_ids - available_ids)}"
        )

    by_seg = defaultdict(list)
    for ch in chunks:
        if not ch.get("text"):
            fail(f"empty chunk text: {ch.get('chunk_id')}")
        by_seg[ch["segment_id"]].append(ch)
    for sid, items in by_seg.items():
        n = len(items)
        indexes = sorted(ch["chunk_index"] for ch in items)
        if indexes != list(range(1, n + 1)):
            fail(f"chunk indexes non-contiguous for {sid}")
        if any(ch["chunk_count"] != n for ch in items):
            fail(f"chunk_count mismatch for {sid}")

    # 产物文本一致性核查（恢复后不应再存在 blocking 的 row 176 记载）
    anomalies = (M / "missing-and-anomalies.md").read_text(encoding="utf-8")
    if "row 176" in anomalies and "No missing raw/clean text segments detected." not in anomalies:
        fail("missing-and-anomalies.md still shows missing blockers")
    if "raw_md_missing" not in anomalies:
        pass
    if "clean_md_missing" not in anomalies:
        pass

    state = (K / "STATE.md").read_text(encoding="utf-8")
    # This validator is now run in the post-W2/W9 repository as well as immediately
    # after W1.  Therefore it checks current W1 recovery facts, not the obsolete
    # "paused before W2" state from the first W1 bootstrap.
    for needle in ["W1 已完成恢复", "segments.jsonl`: 363", "chunks.jsonl`:", "row 176"]:
        if needle not in state:
            fail(f"STATE.md lacks {needle!r}")

    log = (K / "logs" / "operation-log.md").read_text(encoding="utf-8")
    for needle in ["W1 corpus manifest completed", "segments.jsonl", "missing-and-anomalies.md", "Stopped before W2"]:
        if needle not in log:
            fail(f"operation-log.md lacks {needle!r}")

    seg_card_files = [p for p in (K / "segment-cards").glob("*.md") if p.is_file()]
    # Segment cards may exist in the current repository.  They are outside the W1
    # manifest contract and should not make W1 corpus validation fail.

    print(json.dumps({
        "status": "PASS",
        "toc_rows": len(rows),
        "segments": len(segments),
        "available_segments": len(available),
        "missing_segments": len(missing),
        "chunks": len(chunks),
        "segments_with_chunks": len(chunked_ids),
        "missing_segment": None,
        "split_pdf_dir_exists": split_pdf_exists,
        "split_pdf_file_count": split_pdf_file_count,
        "segment_card_files_present": len(seg_card_files),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
