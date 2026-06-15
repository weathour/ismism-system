#!/usr/bin/env python3
"""Validate the Chinese Philosophy maximum absorption layer.

The validator is local and conservative. It checks row/class ownership,
exact quote substrings, taxonomy consistency, Chinese W3/W5 batch discipline,
W10 coverage/rationales, and evidence-linked synthesis markers.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

THEME_ROOT = Path("knowledge/themes/chinese-philosophy")
MANIFEST = THEME_ROOT / "chinese-philosophy-row-manifest.jsonl"
EVIDENCE = THEME_ROOT / "chinese-philosophy-evidence-bank.jsonl"
TAXONOMY = THEME_ROOT / "chinese-philosophy-taxonomy.md"
README = THEME_ROOT / "README.md"
SYNTHESIS_FILES = [
    THEME_ROOT / "chinese-philosophy-synthesis.md",
    THEME_ROOT / "ancient-chinese-philosophy-synthesis.md",
    THEME_ROOT / "mao-philosophy-synthesis.md",
]
QUERY_HELPER = Path("knowledge/scripts/query_chinese_philosophy_theme.py")
W3_BATCH = "W3-CHINESE-PHILOSOPHY-2026-06-15"
W5_BATCH = "W5-CHINESE-PHILOSOPHY-2026-06-15"

CLASS_ROWS: dict[str, set[int]] = {
    "confucian-ethical-subject": {46, 50, 59, 81, 83, 89, 134, 137},
    "neo-confucian-heart-mind": {48, 49, 57},
    "daoist-negativity-nonaction": {119, 125, 126, 127, 132},
    "zhuangzi-forgetting-transformation": {128, 129, 130, 131},
    "legalist-practical-magic": {133},
    "yijing-symbolic-history": {135, 136, 138},
    "names-anti-dualism": {139, 142, 143},
    "buddhist-chan-bridge": {120, 121, 122, 123, 124, 140, 141, 186},
    "mao-practice-contradiction": {184, 289, 290, 291, 327, 331},
    "chinese-marxist-organization": {284, 285, 292, 293, 332, 333, 334, 335, 341},
    "revolutionary-dialectical-context": {1, 34, 35, 94, 98, 110, 154, 162, 261, 269, 270, 280, 309, 321, 324, 325, 326, 328, 329, 330},
    "peripheral-or-noise": set(),
}
EXPECTED_ROWS = set().union(*CLASS_ROWS.values())
THEME_CLASSES = set(CLASS_ROWS)
CORE_STATUS = {"core", "peripheral", "noise-review"}
RECOMMENDED_ACTION = {
    "w3+w5+w10",
    "w3+w5+context-rationale",
    "w10+theme-index",
    "quote-bank+context-rationale",
    "quote-bank+noise-review",
    "not_applicable",
}
CORE_CLASSES = THEME_CLASSES - {"revolutionary-dialectical-context", "peripheral-or-noise"}
REQUIRED_W10_ROWS = {
    125, 127, 128, 130, 131, 132, 133, 135, 140, 143,
    46, 48, 49, 50, 57, 59, 134, 137,
    184, 284, 285, 289, 290, 291, 292, 293, 327, 331, 332, 333, 334, 335, 341,
    120, 121, 122, 123, 124, 141, 186, 119, 139, 142, 321, 324,
}


def load_jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    out: list[tuple[int, dict[str, Any]]] = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            out.append((lineno, json.loads(line)))
    return out


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    return {int(rec["row_id"]): rec for _, rec in load_jsonl(repo / "knowledge/manifests/segments.jsonl")}


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def parse_w10_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith(" ") or not line.strip() or line.lstrip().startswith("-"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def load_w10_rows(repo: Path) -> dict[int, list[str]]:
    rows: dict[int, list[str]] = {}
    for p in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        meta = parse_w10_frontmatter(p)
        try:
            row = int(str(meta.get("row_id", "")))
        except ValueError:
            continue
        rows.setdefault(row, []).append(str(meta.get("card_id") or p.stem))
    return rows


def load_w3_batch(repo: Path) -> tuple[list[dict[str, Any]], dict[int, list[str]], list[str]]:
    path = repo / "knowledge/lexicon/term-senses.jsonl"
    all_ids: set[str] = set()
    duplicates: list[str] = []
    batch: list[dict[str, Any]] = []
    rows: dict[int, list[str]] = {}
    for lineno, rec in load_jsonl(path):
        sid = str(rec.get("sense_id", ""))
        if sid in all_ids:
            duplicates.append(f"{path}:{lineno}: duplicate sense_id {sid}")
        all_ids.add(sid)
        if rec.get("batch_id") != W3_BATCH:
            continue
        batch.append(rec)
        for src in rec.get("source_segments", []) or []:
            try:
                row = int(src.get("row_id"))
            except Exception:
                continue
            rows.setdefault(row, []).append(sid)
    return batch, rows, duplicates


def load_w5_batch(repo: Path) -> tuple[list[dict[str, Any]], dict[int, list[str]], list[str]]:
    path = repo / "knowledge/relations/relation-assets.jsonl"
    all_ids: set[str] = set()
    duplicates: list[str] = []
    batch: list[dict[str, Any]] = []
    rows: dict[int, list[str]] = {}
    for lineno, rec in load_jsonl(path):
        rid = str(rec.get("relation_id", ""))
        if rid in all_ids:
            duplicates.append(f"{path}:{lineno}: duplicate relation_id {rid}")
        all_ids.add(rid)
        if rec.get("batch_id") != W5_BATCH:
            continue
        batch.append(rec)
        for ev in rec.get("evidence_segment", []) or []:
            try:
                row = int(ev.get("row_id"))
            except Exception:
                continue
            rows.setdefault(row, []).append(rid)
    return batch, rows, duplicates


def validate_manifest_and_evidence(repo: Path, segments: dict[int, dict[str, Any]], errors: list[str]) -> tuple[dict[int, dict[str, Any]], dict[str, dict[str, Any]], dict[int, int]]:
    manifest_path = repo / MANIFEST
    evidence_path = repo / EVIDENCE
    if not manifest_path.exists():
        add(errors, f"missing {MANIFEST}")
        return {}, {}, {}
    if not evidence_path.exists():
        add(errors, f"missing {EVIDENCE}")
        return {}, {}, {}

    manifest_records = load_jsonl(manifest_path)
    evidence_records = load_jsonl(evidence_path)
    manifest_by_row: dict[int, dict[str, Any]] = {}
    for lineno, rec in manifest_records:
        row = rec.get("row_id")
        if not isinstance(row, int):
            add(errors, f"{MANIFEST}:{lineno}: row_id must be int")
            continue
        if row in manifest_by_row:
            add(errors, f"{MANIFEST}:{lineno}: duplicate row {row}")
        manifest_by_row[row] = rec
        seg = segments.get(row)
        if not seg:
            add(errors, f"{MANIFEST}:{lineno}: row {row} not in segments.jsonl")
            continue
        expected_path = seg["source_paths"]["clean_md_relpath"]
        expected_toc = "None" if seg.get("toc_id") is None else str(seg.get("toc_id"))
        if rec.get("segment_id") != seg.get("segment_id"):
            add(errors, f"{MANIFEST}:{lineno}: row {row} segment_id mismatch")
        if str(rec.get("toc_id")) != expected_toc:
            add(errors, f"{MANIFEST}:{lineno}: row {row} toc_id mismatch")
        if rec.get("clean_md_path") != expected_path:
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean_md_path mismatch")
        if not (repo / expected_path).exists():
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean file missing {expected_path}")
        cls = rec.get("theme_class")
        if cls not in THEME_CLASSES:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad theme_class {cls!r}")
        elif row not in CLASS_ROWS[cls]:
            add(errors, f"{MANIFEST}:{lineno}: row {row} assigned to {cls}, expected exact class map")
        if rec.get("core_status") not in CORE_STATUS:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad core_status {rec.get('core_status')!r}")
        if rec.get("recommended_action") not in RECOMMENDED_ACTION:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad recommended_action {rec.get('recommended_action')!r}")
        if not isinstance(rec.get("keyword_hits"), dict):
            add(errors, f"{MANIFEST}:{lineno}: row {row} keyword_hits must be object")
        try:
            if int(rec.get("evidence_quote_count", -1)) < 0:
                add(errors, f"{MANIFEST}:{lineno}: row {row} bad evidence_quote_count")
        except Exception:
            add(errors, f"{MANIFEST}:{lineno}: row {row} evidence_quote_count not int-like")

    if set(manifest_by_row) != EXPECTED_ROWS:
        add(errors, f"manifest rows mismatch: missing={sorted(EXPECTED_ROWS-set(manifest_by_row))}, extra={sorted(set(manifest_by_row)-EXPECTED_ROWS)}")

    evidence_by_id: dict[str, dict[str, Any]] = {}
    count_by_row: dict[int, int] = {}
    for lineno, rec in evidence_records:
        eid = str(rec.get("evidence_id", ""))
        if not re.fullmatch(r"ev:chphil:\d{4}:\d{2}", eid):
            add(errors, f"{EVIDENCE}:{lineno}: bad evidence_id {eid!r}")
        if eid in evidence_by_id:
            add(errors, f"{EVIDENCE}:{lineno}: duplicate evidence_id {eid}")
        evidence_by_id[eid] = rec
        try:
            row = int(rec.get("row_id"))
        except Exception:
            add(errors, f"{EVIDENCE}:{lineno}: bad row_id")
            continue
        if row not in manifest_by_row:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} not in Chinese philosophy manifest")
            continue
        seg = segments[row]
        expected_path = seg["source_paths"]["clean_md_relpath"]
        expected_toc = "None" if seg.get("toc_id") is None else str(seg.get("toc_id"))
        if rec.get("segment_id") != seg.get("segment_id") or str(rec.get("toc_id")) != expected_toc:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} segment/toc mismatch")
        if rec.get("clean_md_path") != expected_path:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} clean path mismatch")
        quote = str(rec.get("quote", ""))
        if not quote.strip():
            add(errors, f"{EVIDENCE}:{lineno}: empty quote")
            continue
        text = (repo / expected_path).read_text(encoding="utf-8")
        if quote not in text:
            add(errors, f"{EVIDENCE}:{lineno}: quote not exact substring for row {row}: {quote[:80]}")
        count_by_row[row] = count_by_row.get(row, 0) + 1

    for row, rec in manifest_by_row.items():
        expected = int(rec.get("evidence_quote_count", -1))
        actual = count_by_row.get(row, 0)
        if expected != actual:
            add(errors, f"manifest/evidence count mismatch row {row}: manifest={expected}, evidence={actual}")
        if rec.get("core_status") == "core" and actual < 3:
            add(errors, f"core row {row} has too few evidence quotes: {actual}")
        if rec.get("core_status") != "core" and actual < 1 and rec.get("recommended_action") != "not_applicable":
            add(errors, f"non-core row {row} lacks evidence quote")
    return manifest_by_row, evidence_by_id, count_by_row


def validate_taxonomy(repo: Path, manifest_by_row: dict[int, dict[str, Any]], evidence_by_id: dict[str, dict[str, Any]], errors: list[str]) -> None:
    path = repo / TAXONOMY
    if not path.exists():
        add(errors, f"missing {TAXONOMY}")
        return
    text = path.read_text(encoding="utf-8")
    taxonomy_row_classes: dict[int, str] = {}
    for cls in THEME_CLASSES:
        if cls not in text:
            add(errors, f"taxonomy does not mention theme_class {cls}")
    for eid in re.findall(r"ev:chphil:\d{4}:\d{2}", text):
        if eid not in evidence_by_id:
            add(errors, f"taxonomy references unknown evidence id {eid}")
    for section in re.split(r"\n(?=## T\d+\.)", text):
        if not section.startswith("## T"):
            continue
        heading = section.splitlines()[0].strip()
        class_match = re.search(r"- theme_class: `([^`]+)`", section)
        rows_match = re.search(r"- rows: ([^\n]+)", section)
        if not class_match:
            add(errors, f"taxonomy section lacks theme_class: {heading}")
            continue
        section_class = class_match.group(1)
        if section_class not in THEME_CLASSES:
            add(errors, f"taxonomy section {heading} has bad theme_class {section_class!r}")
        if not rows_match:
            add(errors, f"taxonomy section lacks rows: {heading}")
            continue
        for row_s in re.findall(r"row (\d+)", rows_match.group(1)):
            row = int(row_s)
            if row in taxonomy_row_classes:
                add(errors, f"taxonomy row {row} appears in multiple theme nodes: {taxonomy_row_classes[row]} and {section_class}")
                continue
            taxonomy_row_classes[row] = section_class
            manifest_class = manifest_by_row.get(row, {}).get("theme_class")
            if manifest_class and manifest_class != section_class:
                add(errors, f"taxonomy row {row} class mismatch: taxonomy={section_class}, manifest={manifest_class}")
    missing = sorted(set(manifest_by_row) - set(taxonomy_row_classes))
    extra = sorted(set(taxonomy_row_classes) - set(manifest_by_row))
    if missing:
        add(errors, f"taxonomy missing manifest rows: {missing}")
    if extra:
        add(errors, f"taxonomy references extra rows: {extra}")


def validate_final(repo: Path, manifest_by_row: dict[int, dict[str, Any]], errors: list[str]) -> None:
    w3_batch, w3_rows, w3_dups = load_w3_batch(repo)
    w5_batch, w5_rows, w5_dups = load_w5_batch(repo)
    w10_rows = load_w10_rows(repo)
    evidence_ids = {str(rec.get("evidence_id")) for _, rec in load_jsonl(repo / EVIDENCE)}
    sense_ids = {str(rec.get("sense_id")) for _, rec in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")}
    relation_ids = {str(rec.get("relation_id")) for _, rec in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")}
    w10_ids: set[str] = set()
    for p in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        meta = parse_w10_frontmatter(p)
        if meta.get("card_id"):
            w10_ids.add(str(meta["card_id"]))
    errors.extend(w3_dups)
    errors.extend(w5_dups)

    if not (50 <= len(w3_batch) <= 70):
        add(errors, f"Chinese W3 batch count outside [50,70]: {len(w3_batch)}")
    for rec in w3_batch:
        if rec.get("status") != "draft":
            add(errors, f"Chinese W3 non-draft status: {rec.get('sense_id')}")
        for src in rec.get("source_segments", []) or []:
            try:
                row = int(src.get("row_id"))
            except Exception:
                continue
            if row not in EXPECTED_ROWS:
                add(errors, f"Chinese W3 source row outside manifest: {rec.get('sense_id')} row {row}")

    if not (40 <= len(w5_batch) <= 60):
        add(errors, f"Chinese W5 batch count outside [40,60]: {len(w5_batch)}")
    for rec in w5_batch:
        if rec.get("status") != "draft":
            add(errors, f"Chinese W5 non-draft status: {rec.get('relation_id')}")
        for ev in rec.get("evidence_segment", []) or []:
            try:
                row = int(ev.get("row_id"))
            except Exception:
                continue
            if row not in EXPECTED_ROWS:
                add(errors, f"Chinese W5 evidence row outside manifest: {rec.get('relation_id')} row {row}")

    core_rows = {row for cls in CORE_CLASSES for row in CLASS_ROWS[cls]}
    for row in sorted(core_rows):
        if row not in w3_rows:
            add(errors, f"core row {row} lacks Chinese W3 batch coverage")
        if row not in w5_rows:
            add(errors, f"core row {row} lacks Chinese W5 batch coverage")
        if row not in w10_rows:
            notes = str(manifest_by_row.get(row, {}).get("notes", "")).lower()
            action = str(manifest_by_row.get(row, {}).get("recommended_action", ""))
            if "context" not in notes and "context-rationale" not in action:
                add(errors, f"core row {row} lacks W10 and lacks context rationale")

    for row in sorted(REQUIRED_W10_ROWS):
        if row not in w10_rows:
            add(errors, f"required W10 row {row} lacks W10 card coverage")

    for row, ids in w10_rows.items():
        if any(cid.startswith("w10:") and row not in EXPECTED_ROWS and "ai" not in cid for cid in ids):
            # Existing non-theme W10 cards are allowed; only warn via no-op. Chinese validator is theme scoped.
            pass

    for path in [README, QUERY_HELPER, *SYNTHESIS_FILES]:
        if not (repo / path).exists():
            add(errors, f"missing final artifact {path}")
    for path in SYNTHESIS_FILES:
        full = repo / path
        if not full.exists():
            continue
        text = full.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if not stripped.startswith("- claim:"):
                continue
            marker_found = False
            for eid in re.findall(r"ev:chphil:\d{4}:\d{2}", stripped):
                marker_found = True
                if eid not in evidence_ids:
                    add(errors, f"{path}:{lineno}: unknown evidence marker {eid}")
            for sid in re.findall(r"term:[^\s,，。;；)）`]+:s\d{2}", stripped):
                marker_found = True
                if sid not in sense_ids:
                    add(errors, f"{path}:{lineno}: unknown term marker {sid}")
            for rid in re.findall(r"rel:chphil:\d{3}", stripped):
                marker_found = True
                if rid not in relation_ids:
                    add(errors, f"{path}:{lineno}: unknown relation marker {rid}")
            for wid in re.findall(r"w10:(?:arg|proc|case):\d{4}:[A-Za-z0-9-]+", stripped):
                marker_found = True
                if wid not in w10_ids:
                    add(errors, f"{path}:{lineno}: unknown W10 marker {wid}")
            for row_s in re.findall(r"row (\d+)", stripped):
                marker_found = True
                row = int(row_s)
                if row not in manifest_by_row:
                    add(errors, f"{path}:{lineno}: row marker outside Chinese manifest row {row}")
            if not marker_found:
                add(errors, f"{path}:{lineno}: claim bullet lacks trace marker")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate Chinese Philosophy theme absorption artifacts")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    try:
        segments = load_segments(repo)
    except Exception as exc:
        print(f"validate_chinese_philosophy_theme: failed to load segments: {exc}", file=sys.stderr)
        return 2

    manifest_by_row, evidence_by_id, _ = validate_manifest_and_evidence(repo, segments, errors)
    if manifest_by_row:
        validate_taxonomy(repo, manifest_by_row, evidence_by_id, errors)
    if args.final and manifest_by_row:
        validate_final(repo, manifest_by_row, errors)

    summary = {
        "status": "FAIL" if errors else "PASS",
        "manifest_rows": len(manifest_by_row),
        "evidence_records": len(evidence_by_id),
        "w3_chinese_records": len(load_w3_batch(repo)[0]) if (repo / "knowledge/lexicon/term-senses.jsonl").exists() else 0,
        "w5_chinese_records": len(load_w5_batch(repo)[0]) if (repo / "knowledge/relations/relation-assets.jsonl").exists() else 0,
        "w10_rows": len(load_w10_rows(repo)),
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"validate_chinese_philosophy_theme: {summary['status']}")
        print(json.dumps({k: v for k, v in summary.items() if k not in {'errors','warnings'}}, ensure_ascii=False))
        for err in errors[:100]:
            print("- " + err)
        for warn in warnings[:30]:
            print("WARN " + warn)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
