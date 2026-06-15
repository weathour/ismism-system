#!/usr/bin/env python3
"""Validate the AI theme absorption layer.

This validator is intentionally local and conservative. It checks that the AI
manifest, quote bank, taxonomy/synthesis/README references, W3/W5 additions,
and W10 AI cards remain traceable to row/segment/clean quote evidence.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

THEME_ROOT = Path("knowledge/themes/ai")
MANIFEST = THEME_ROOT / "ai-row-manifest.jsonl"
EVIDENCE = THEME_ROOT / "ai-evidence-bank.jsonl"
TAXONOMY = THEME_ROOT / "ai-taxonomy.md"
SYNTHESIS = THEME_ROOT / "ai-synthesis.md"
README = THEME_ROOT / "README.md"
W3_BATCH = "W3-AI-2026-06-15"
W5_BATCH = "W5-AI-2026-06-15"

THEME_CLASSES = {
    "ai-theory-prehistory",
    "ai-vr-utopia",
    "ai-deanthropocentrization",
    "ai-body-memory-language",
    "ai-social-ethical-system",
    "ai-analogy",
    "peripheral-technical",
    "noise-review",
}
CORE_STATUS = {"core", "peripheral", "noise-review"}
RECOMMENDED_ACTION = {
    "w3+w5+w10",
    "w10+theme-index",
    "quote-bank+context-rationale",
    "quote-bank+noise-review",
    "not_applicable",
}
REQUIRED_KEY_ROWS = {350, 354, 356, 358, 359, 360, 361, 362, 363}
CORE_ROW_RANGE = set(range(13, 19)) | set(range(342, 364))


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


def parse_w10_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith(" "):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def load_w10_rows(repo: Path) -> dict[int, list[str]]:
    rows: dict[int, list[str]] = {}
    root = repo / "knowledge/w10-absorption"
    for p in root.glob("*-cards/*.md"):
        meta = parse_w10_frontmatter(p)
        if not meta.get("row_id"):
            continue
        try:
            row = int(meta["row_id"])
        except ValueError:
            continue
        rows.setdefault(row, []).append(meta.get("card_id") or p.stem)
    return rows


def load_w3_rows(repo: Path) -> dict[int, list[str]]:
    rows: dict[int, list[str]] = {}
    path = repo / "knowledge/lexicon/term-senses.jsonl"
    if not path.exists():
        return rows
    for _, rec in load_jsonl(path):
        if rec.get("batch_id") != W3_BATCH:
            continue
        sid = str(rec.get("sense_id", ""))
        for src in rec.get("source_segments", []) or []:
            try:
                row = int(src.get("row_id"))
            except Exception:
                continue
            rows.setdefault(row, []).append(sid)
    return rows


def load_w5_rows(repo: Path) -> dict[int, list[str]]:
    rows: dict[int, list[str]] = {}
    path = repo / "knowledge/relations/relation-assets.jsonl"
    if not path.exists():
        return rows
    for _, rec in load_jsonl(path):
        if rec.get("batch_id") != W5_BATCH:
            continue
        rid = str(rec.get("relation_id", ""))
        for ev in rec.get("evidence_segment", []) or []:
            try:
                row = int(ev.get("row_id"))
            except Exception:
                continue
            rows.setdefault(row, []).append(rid)
    return rows


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate AI theme absorption artifacts")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--final", action="store_true", help="enforce synthesis/README and W3+W5+W10 coverage gates")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    segments = load_segments(repo)
    manifest_path = repo / MANIFEST
    evidence_path = repo / EVIDENCE
    if not manifest_path.exists():
        add(errors, f"missing {MANIFEST}")
    if not evidence_path.exists():
        add(errors, f"missing {EVIDENCE}")
    if errors:
        print("validate_ai_theme: FAIL")
        for e in errors:
            print("- " + e)
        return 1

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
        if seg is None:
            add(errors, f"{MANIFEST}:{lineno}: row {row} not in segments.jsonl")
            continue
        expected = seg["source_paths"]["clean_md_relpath"]
        if rec.get("segment_id") != seg.get("segment_id"):
            add(errors, f"{MANIFEST}:{lineno}: row {row} segment_id mismatch")
        if rec.get("toc_id") != seg.get("toc_id"):
            add(errors, f"{MANIFEST}:{lineno}: row {row} toc_id mismatch")
        if rec.get("clean_md_path") != expected:
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean_md_path mismatch")
        if not (repo / expected).exists():
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean file missing {expected}")
        if rec.get("theme_class") not in THEME_CLASSES:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad theme_class {rec.get('theme_class')!r}")
        if rec.get("core_status") not in CORE_STATUS:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad core_status {rec.get('core_status')!r}")
        if rec.get("recommended_action") not in RECOMMENDED_ACTION:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad recommended_action {rec.get('recommended_action')!r}")
        if not isinstance(rec.get("keyword_hits"), dict) or not rec.get("keyword_hits"):
            add(errors, f"{MANIFEST}:{lineno}: row {row} keyword_hits missing")
        if int(rec.get("evidence_quote_count", -1)) < 0:
            add(errors, f"{MANIFEST}:{lineno}: row {row} evidence_quote_count invalid")

    if len(manifest_by_row) != 60:
        add(errors, f"manifest should cover exactly 60 AI candidate rows, found {len(manifest_by_row)}")
    missing_core = sorted(CORE_ROW_RANGE - set(manifest_by_row))
    if missing_core:
        add(errors, f"manifest missing core AI rows: {missing_core}")

    evidence_by_id: dict[str, dict[str, Any]] = {}
    evidence_count_by_row: dict[int, int] = {}
    for lineno, rec in evidence_records:
        eid = str(rec.get("evidence_id", ""))
        if not re.fullmatch(r"ev:ai:\d{4}:\d{2}", eid):
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
            add(errors, f"{EVIDENCE}:{lineno}: row {row} not in AI manifest")
            continue
        seg = segments[row]
        expected = seg["source_paths"]["clean_md_relpath"]
        if rec.get("segment_id") != seg.get("segment_id") or rec.get("toc_id") != seg.get("toc_id"):
            add(errors, f"{EVIDENCE}:{lineno}: row {row} segment/toc mismatch")
        if rec.get("clean_md_path") != expected:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} clean path mismatch")
        quote = str(rec.get("quote", ""))
        if not quote.strip():
            add(errors, f"{EVIDENCE}:{lineno}: empty quote")
            continue
        text = (repo / expected).read_text(encoding="utf-8")
        if quote not in text:
            add(errors, f"{EVIDENCE}:{lineno}: quote not exact substring for row {row}: {quote[:80]}")
        evidence_count_by_row[row] = evidence_count_by_row.get(row, 0) + 1

    for row, rec in manifest_by_row.items():
        expected_count = int(rec.get("evidence_quote_count", -1))
        actual_count = evidence_count_by_row.get(row, 0)
        if expected_count != actual_count:
            add(errors, f"manifest/evidence count mismatch row {row}: manifest={expected_count}, evidence={actual_count}")
        if rec.get("core_status") == "core" and actual_count < 3:
            add(errors, f"core row {row} has too few evidence quotes: {actual_count}")
        if rec.get("core_status") != "core" and actual_count < 1:
            add(errors, f"non-core row {row} lacks evidence quote")

    if (repo / TAXONOMY).exists():
        text = (repo / TAXONOMY).read_text(encoding="utf-8")
        for cls in THEME_CLASSES:
            if cls not in text:
                warnings.append(f"taxonomy does not mention theme_class {cls}")
        for eid in re.findall(r"ev:ai:\d{4}:\d{2}", text):
            if eid not in evidence_by_id:
                add(errors, f"taxonomy references unknown evidence id {eid}")
        for row_s in re.findall(r"row (\d+)", text):
            row = int(row_s)
            if row not in manifest_by_row:
                add(errors, f"taxonomy references row not in manifest: {row}")

        taxonomy_row_classes: dict[int, str] = {}
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
                    add(
                        errors,
                        f"taxonomy row {row} appears in multiple theme nodes: "
                        f"{taxonomy_row_classes[row]} and {section_class}",
                    )
                    continue
                taxonomy_row_classes[row] = section_class
                manifest_class = manifest_by_row.get(row, {}).get("theme_class")
                if manifest_class and manifest_class != section_class:
                    add(
                        errors,
                        f"taxonomy row {row} class mismatch: taxonomy={section_class}, "
                        f"manifest={manifest_class}",
                    )
        missing_taxonomy_rows = sorted(set(manifest_by_row) - set(taxonomy_row_classes))
        if missing_taxonomy_rows:
            add(errors, f"taxonomy missing manifest rows: {missing_taxonomy_rows}")
    else:
        add(errors, f"missing {TAXONOMY}")

    w3_rows = load_w3_rows(repo)
    w5_rows = load_w5_rows(repo)
    w10_rows = load_w10_rows(repo)
    if args.final:
        for path in [SYNTHESIS, README]:
            if not (repo / path).exists():
                add(errors, f"missing final artifact {path}")
        for row in REQUIRED_KEY_ROWS:
            if row not in w3_rows:
                add(errors, f"required key row {row} lacks AI W3 batch coverage")
            if row not in w5_rows:
                add(errors, f"required key row {row} lacks AI W5 batch coverage")
            if row not in w10_rows:
                add(errors, f"required key row {row} lacks W10 card coverage")
        for row in CORE_ROW_RANGE:
            rec = manifest_by_row.get(row)
            if not rec:
                continue
            if row not in w10_rows and "gap" not in str(rec.get("notes", "")).lower():
                add(errors, f"core row {row} lacks W10 coverage and has no gap rationale")
        if (repo / SYNTHESIS).exists():
            syn = (repo / SYNTHESIS).read_text(encoding="utf-8")
            # Each major claim bullet should carry at least one evidence/source marker.
            for lineno, line in enumerate(syn.splitlines(), 1):
                stripped = line.strip()
                if stripped.startswith("- claim:") and not re.search(r"(ev:ai:\d{4}:\d{2}|w10:|term:|rel:ai-theme:|row \d+)", stripped):
                    add(errors, f"{SYNTHESIS}:{lineno}: claim bullet lacks trace marker")

    summary = {
        "status": "FAIL" if errors else "PASS",
        "manifest_rows": len(manifest_by_row),
        "evidence_records": len(evidence_records),
        "w3_ai_rows": len(w3_rows),
        "w5_ai_rows": len(w5_rows),
        "w10_rows": len(w10_rows),
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"validate_ai_theme: {summary['status']}")
        print(json.dumps({k: v for k, v in summary.items() if k not in {'errors','warnings'}}, ensure_ascii=False))
        for err in errors[:80]:
            print("- " + err)
        for warn in warnings[:30]:
            print("WARN " + warn)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
