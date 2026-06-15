#!/usr/bin/env python3
"""Validate the Religion Problem maximum absorption layer.

This validator is local and conservative. It checks row/class ownership,
exact quote substrings, taxonomy consistency, Religion W3/W5 draft batch
coverage, Religion W10 pilot-card coverage, and evidence-linked synthesis
markers. It treats the theme layer as an index/synthesis surface, never as a
replacement for corpus/manifests/clean text truth sources.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

THEME_ROOT = Path("knowledge/themes/religion")
MANIFEST = THEME_ROOT / "religion-row-manifest.jsonl"
EVIDENCE = THEME_ROOT / "religion-evidence-bank.jsonl"
TAXONOMY = THEME_ROOT / "religion-taxonomy.md"
README = THEME_ROOT / "README.md"
SYNTHESIS_FILES = [
    THEME_ROOT / "religion-synthesis.md",
    THEME_ROOT / "religious-realism-synthesis.md",
    THEME_ROOT / "sacred-ideology-and-practice-synthesis.md",
]
QUERY_HELPER = Path("knowledge/scripts/query_religion_theme.py")
W3_BATCH = "W3-RELIGION-2026-06-15"
W5_BATCH = "W5-RELIGION-2026-06-15"

CLASS_ROWS: dict[str, set[int]] = {
    "religious-realism-cosmos": {24, 25},
    "creation-theodicy-godhead": {26, 27, 28, 29, 30},
    "idolatry-sacred-phenomenality": {31, 32, 33},
    "fetish-symbolic-object": {34},
    "time-death-immortality": {8, 35, 37, 95, 111, 171},
    "spiritualism-soul-technique": {36, 38},
    "magic-occult-knowledge": {39, 133},
    "renunciation-salvation": {40},
    "anti-idolatry-faith-transcendence": {41, 42},
    "messiah-big-other-love": {43, 45, 55},
    "mysticism-negative-theology": {44, 131, 153, 154, 238, 241},
    "buddhist-liberation-bridge": {120, 121, 122, 123, 124, 140, 141, 186},
    "secular-sacred-ideology": {1, 54, 59, 65, 81, 82, 85, 87, 88, 89, 90},
    "metaphysical-theology-origin": {102, 103, 104, 108, 109, 110, 125, 134, 137, 157, 170, 185},
    "modern-subjectivity-religion": {209, 213, 227, 240, 249, 250, 251, 273},
    "ideology-religion-historicization": {184, 231, 261, 295},
    "dogma-discipline-organization": {291, 333, 334},
    "practice-after-faith": {294},
    "peripheral-or-noise": set(),
}
EXPECTED_ROWS = set().union(*CLASS_ROWS.values())
THEME_CLASSES = set(CLASS_ROWS)
CORE_ROWS = set(range(24, 46))
CORE_STATUS = {"core", "peripheral", "noise-review"}
RECOMMENDED_ACTION = {
    "w3+w5+w10",
    "w3+w5+context-rationale",
    "w10+theme-index",
    "quote-bank+context-rationale",
    "quote-bank+noise-review",
    "not_applicable",
}
EXCLUDED_CANDIDATE_ROWS = {6, 7, 75, 91, 93, 195}


def load_jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    out: list[tuple[int, dict[str, Any]]] = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if line.strip():
                out.append((lineno, json.loads(line)))
    return out


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    return {int(rec["row_id"]): rec for _, rec in load_jsonl(repo / "knowledge/manifests/segments.jsonl")}


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def parse_w10_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, Any] = {}
    key: str | None = None
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        if not raw.strip():
            continue
        if not raw.startswith(" ") and ":" in raw:
            k, v = raw.split(":", 1)
            key = k.strip()
            v = v.strip()
            meta[key] = [] if v == "" else v.strip('"\'`')
        elif key == "evidence_quotes" and raw.strip().startswith("- "):
            meta.setdefault("evidence_quotes", []).append(raw.strip()[2:].strip('"\'`'))
    return meta


def load_w10_batch(repo: Path) -> tuple[dict[int, list[str]], dict[str, Path], list[str]]:
    rows: dict[int, list[str]] = {}
    ids: dict[str, Path] = {}
    errors: list[str] = []
    for p in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        meta = parse_w10_frontmatter(p)
        cid = str(meta.get("card_id", ""))
        if ":religion-" not in cid:
            continue
        ids[cid] = p
        try:
            row = int(str(meta.get("row_id", "")))
        except ValueError:
            errors.append(f"Religion W10 card has bad row_id: {p}")
            continue
        rows.setdefault(row, []).append(cid)
        quotes = meta.get("evidence_quotes", []) or []
        if len(quotes) != len(set(quotes)):
            errors.append(f"Religion W10 duplicate evidence quote in {p}")
    return rows, ids, errors


def load_w3_batch(repo: Path) -> tuple[list[dict[str, Any]], dict[int, list[str]], list[str]]:
    path = repo / "knowledge/lexicon/term-senses.jsonl"
    seen: set[str] = set()
    batch: list[dict[str, Any]] = []
    rows: dict[int, list[str]] = {}
    errors: list[str] = []
    for lineno, rec in load_jsonl(path):
        sid = str(rec.get("sense_id", ""))
        if sid in seen:
            errors.append(f"{path}:{lineno}: duplicate sense_id {sid}")
        seen.add(sid)
        if rec.get("batch_id") != W3_BATCH:
            continue
        batch.append(rec)
        for src in rec.get("source_segments", []) or []:
            try:
                row = int(src.get("row_id"))
            except Exception:
                continue
            rows.setdefault(row, []).append(sid)
    return batch, rows, errors


def load_w5_batch(repo: Path) -> tuple[list[dict[str, Any]], dict[int, list[str]], list[str]]:
    path = repo / "knowledge/relations/relation-assets.jsonl"
    seen: set[str] = set()
    batch: list[dict[str, Any]] = []
    rows: dict[int, list[str]] = {}
    errors: list[str] = []
    for lineno, rec in load_jsonl(path):
        rid = str(rec.get("relation_id", ""))
        if rid in seen:
            errors.append(f"{path}:{lineno}: duplicate relation_id {rid}")
        seen.add(rid)
        if rec.get("batch_id") != W5_BATCH:
            continue
        batch.append(rec)
        for ev in rec.get("evidence_segment", []) or []:
            try:
                row = int(ev.get("row_id"))
            except Exception:
                continue
            rows.setdefault(row, []).append(rid)
    return batch, rows, errors


def validate_manifest_and_evidence(repo: Path, segments: dict[int, dict[str, Any]], errors: list[str]) -> tuple[dict[int, dict[str, Any]], dict[str, dict[str, Any]], dict[int, int]]:
    manifest_path = repo / MANIFEST
    evidence_path = repo / EVIDENCE
    if not manifest_path.exists():
        add(errors, f"missing {MANIFEST}")
        return {}, {}, {}
    if not evidence_path.exists():
        add(errors, f"missing {EVIDENCE}")
        return {}, {}, {}

    manifest_by_row: dict[int, dict[str, Any]] = {}
    for lineno, rec in load_jsonl(manifest_path):
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
    if not (65 <= len(manifest_by_row) <= 80):
        add(errors, f"manifest row count outside [65,80]: {len(manifest_by_row)}")
    missing_core = sorted(CORE_ROWS - set(manifest_by_row))
    if missing_core:
        add(errors, f"manifest missing core 1-2 rows: {missing_core}")

    evidence_by_id: dict[str, dict[str, Any]] = {}
    count_by_row: dict[int, int] = {}
    for lineno, rec in load_jsonl(evidence_path):
        eid = str(rec.get("evidence_id", ""))
        if not re.fullmatch(r"ev:religion:\d{4}:\d{2}", eid):
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
            add(errors, f"{EVIDENCE}:{lineno}: row {row} not in Religion manifest")
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

    if not (220 <= len(evidence_by_id) <= 320):
        add(errors, f"evidence quote count outside [220,320]: {len(evidence_by_id)}")
    for row, rec in manifest_by_row.items():
        expected = int(rec.get("evidence_quote_count", -1))
        actual = count_by_row.get(row, 0)
        if expected != actual:
            add(errors, f"manifest/evidence count mismatch row {row}: manifest={expected}, evidence={actual}")
        if row in CORE_ROWS and actual < 3:
            add(errors, f"core 1-2 row {row} has too few evidence quotes: {actual}")
        if row not in CORE_ROWS and actual < 1 and rec.get("recommended_action") != "not_applicable":
            add(errors, f"bridge row {row} lacks evidence quote")
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
    for eid in re.findall(r"ev:religion:\d{4}:\d{2}", text):
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
    w3_batch, w3_rows, w3_errors = load_w3_batch(repo)
    w5_batch, w5_rows, w5_errors = load_w5_batch(repo)
    w10_rows, w10_ids_by_id, w10_errors = load_w10_batch(repo)
    errors.extend(w3_errors)
    errors.extend(w5_errors)
    errors.extend(w10_errors)

    evidence_ids = {str(rec.get("evidence_id")) for _, rec in load_jsonl(repo / EVIDENCE)}
    sense_ids = {str(rec.get("sense_id")) for _, rec in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")}
    relation_ids = {str(rec.get("relation_id")) for _, rec in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")}
    w10_ids = set(w10_ids_by_id)

    if not (50 <= len(w3_batch) <= 70):
        add(errors, f"Religion W3 batch count outside [50,70]: {len(w3_batch)}")
    for rec in w3_batch:
        if rec.get("status") != "draft":
            add(errors, f"Religion W3 non-draft status: {rec.get('sense_id')}")
        for src in rec.get("source_segments", []) or []:
            try:
                row = int(src.get("row_id"))
            except Exception:
                continue
            if row not in EXPECTED_ROWS:
                add(errors, f"Religion W3 source row outside manifest: {rec.get('sense_id')} row {row}")

    if not (45 <= len(w5_batch) <= 65):
        add(errors, f"Religion W5 batch count outside [45,65]: {len(w5_batch)}")
    for rec in w5_batch:
        if rec.get("status") != "draft":
            add(errors, f"Religion W5 non-draft status: {rec.get('relation_id')}")
        for ev in rec.get("evidence_segment", []) or []:
            try:
                row = int(ev.get("row_id"))
            except Exception:
                continue
            if row not in EXPECTED_ROWS:
                add(errors, f"Religion W5 evidence row outside manifest: {rec.get('relation_id')} row {row}")

    if not (35 <= len(w10_ids) <= 50):
        add(errors, f"Religion W10 card count outside [35,50]: {len(w10_ids)}")
    missing_core_w10 = sorted(CORE_ROWS - set(w10_rows))
    if missing_core_w10:
        add(errors, f"core 1-2 rows lack Religion W10 cards: {missing_core_w10}")
    for row in sorted(CORE_ROWS):
        if row not in w3_rows:
            add(errors, f"core row {row} lacks Religion W3 batch coverage")
        if row not in w5_rows:
            add(errors, f"core row {row} lacks Religion W5 batch coverage")

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
            for eid in re.findall(r"ev:religion:\d{4}:\d{2}", stripped):
                marker_found = True
                if eid not in evidence_ids:
                    add(errors, f"{path}:{lineno}: unknown evidence marker {eid}")
            for sid in re.findall(r"term:[^\s,，。;；)）`]+:s\d{2}", stripped):
                marker_found = True
                if sid not in sense_ids:
                    add(errors, f"{path}:{lineno}: unknown term marker {sid}")
            for rid in re.findall(r"rel:religion:\d{3}", stripped):
                marker_found = True
                if rid not in relation_ids:
                    add(errors, f"{path}:{lineno}: unknown relation marker {rid}")
            for wid in re.findall(r"w10:(?:arg|proc|case):\d{4}:[A-Za-z0-9-]+", stripped):
                marker_found = True
                if wid not in w10_ids:
                    add(errors, f"{path}:{lineno}: unknown Religion W10 marker {wid}")
            for row_s in re.findall(r"row (\d+)", stripped):
                marker_found = True
                row = int(row_s)
                if row not in manifest_by_row:
                    add(errors, f"{path}:{lineno}: row marker outside Religion manifest row {row}")
            if not marker_found:
                add(errors, f"{path}:{lineno}: claim bullet lacks trace marker")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate Religion Problem theme absorption artifacts")
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
        print(f"validate_religion_theme: failed to load segments: {exc}", file=sys.stderr)
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
        "w3_religion_records": len(load_w3_batch(repo)[0]) if (repo / "knowledge/lexicon/term-senses.jsonl").exists() else 0,
        "w5_religion_records": len(load_w5_batch(repo)[0]) if (repo / "knowledge/relations/relation-assets.jsonl").exists() else 0,
        "w10_religion_rows": len(load_w10_batch(repo)[0]),
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"validate_religion_theme: {summary['status']}")
        print(json.dumps({k: v for k, v in summary.items() if k not in {'errors','warnings'}}, ensure_ascii=False))
        for err in errors[:120]:
            print("- " + err)
        for warn in warnings[:30]:
            print("WARN " + warn)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
