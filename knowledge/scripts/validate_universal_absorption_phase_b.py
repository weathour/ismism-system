#!/usr/bin/env python3
"""Validate Universal Absorption Phase B artifacts.

This validator is intentionally repository-grounded:
- gap-map rows must match W1 manifest segment metadata;
- evidence-bank quotes must be exact substrings of declared clean files;
- W3/W5 Universal-B batches must be draft and within requested counts;
- Universal-B W10 cards must be pilot-draft and covered by the normal W10 validator shape;
- optional phase syntheses may only cite known evidence/term/relation/W10 markers;
- --final enforces conservative absorption targets and protected corpus checksums.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

W3_BATCH = "W3-UNIVERSAL-B-2026-06-16"
W5_BATCH = "W5-UNIVERSAL-B-2026-06-16"
GAP_MAP = "knowledge/qa/universal-absorption-phase-b-gap-map.jsonl"
EVIDENCE_BANK = "knowledge/qa/universal-absorption-phase-b-evidence-bank.jsonl"
W3_PATH = "knowledge/lexicon/term-senses.jsonl"
W5_PATH = "knowledge/relations/relation-assets.jsonl"
W10_ROOT = "knowledge/w10-absorption"
SYNTHESIS_FILES = [
    "knowledge/syntheses/universal-absorption-phase-b-modern-knowledge-logic.md",
    "knowledge/syntheses/universal-absorption-phase-b-practice-communication.md",
]
REQUIRED_DOCS_FINAL = [
    GAP_MAP,
    "knowledge/qa/universal-absorption-phase-b-plan.md",
    EVIDENCE_BANK,
    "knowledge/qa/universal-absorption-phase-b-audit.md",
    "knowledge/qa/universal-absorption-phase-b-evidence-claim-audit.md",
    "knowledge/qa/universal-absorption-phase-b-ultraqa-report.md",
    "knowledge/qa/universal-absorption-phase-b-ai-slop-cleaner-report.md",
    "knowledge/qa/universal-absorption-phase-b-code-review-report.md",
    "knowledge/qa/universal-absorption-phase-b-handoff.md",
    "knowledge/STATE.md",
    "ISMISM-MAINLINE-HANDOFF.md",
    "DIRECTORY_MAP.md",
    "knowledge/README.md",
    "knowledge/logs/operation-log.md",
]
ALLOWED_REL_TYPES = {
    "boundary-between", "route-from-to", "tension-between", "mediates-between", "transitions-to",
    "blocks-transition", "misrecognizes-as", "objectifies", "subjectivizes", "overcodes",
    "represents-position", "evidences-claim",
}


def iter_jsonl(path: Path) -> Iterator[tuple[int, dict[str, Any]]]:
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                yield lineno, {"__parse_error__": str(exc)}
                continue
            if not isinstance(rec, dict):
                yield lineno, {"__parse_error__": "JSONL record is not an object"}
                continue
            yield lineno, rec


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    return {int(rec["row_id"]): rec for _, rec in iter_jsonl(repo / "knowledge/manifests/segments.jsonl")}


def load_card_meta(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, Any] = {}
    current: str | None = None
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        if not raw.startswith(" ") and ":" in raw:
            key, value = raw.split(":", 1)
            key, value = key.strip(), value.strip()
            if value == "":
                meta[key] = []
                current = key
            elif value == "[]":
                meta[key] = []
                current = None
            else:
                meta[key] = value.strip().strip('"').strip("'")
                current = None
        elif raw.strip().startswith("- ") and current:
            meta.setdefault(current, []).append(raw.strip()[2:].strip().strip('"').strip("'"))
    return meta


def add(errors: list[str], message: str) -> None:
    errors.append(message)


def check_quote(repo: Path, segments: dict[int, dict[str, Any]], row_id: int, quote: str, errors: list[str], label: str) -> None:
    seg = segments.get(row_id)
    if seg is None:
        add(errors, f"{label}: row {row_id} not found in segments")
        return
    clean_rel = seg["source_paths"]["clean_md_relpath"]
    clean = repo / clean_rel
    if not clean.exists():
        add(errors, f"{label}: clean file missing for row {row_id}: {clean_rel}")
        return
    if quote not in clean.read_text(encoding="utf-8"):
        add(errors, f"{label}: quote not exact substring for row {row_id}: {quote[:90]}")


def validate_gap_map(repo: Path, segments: dict[int, dict[str, Any]], errors: list[str]) -> set[int]:
    path = repo / GAP_MAP
    if not path.exists():
        add(errors, f"missing {GAP_MAP}")
        return set()
    seen: set[int] = set()
    targets: set[int] = set()
    required = {
        "row_id", "segment_id", "toc_id", "title", "field", "clean_md_path", "char_count",
        "current_layers", "gap_type", "priority_tier", "recommended_action", "inclusion_rationale",
        "exclusion_or_context_rationale",
    }
    for lineno, rec in iter_jsonl(path):
        if "__parse_error__" in rec:
            add(errors, f"gap-map:{lineno}: JSON parse error {rec['__parse_error__']}")
            continue
        missing = sorted(required - set(rec))
        if missing:
            add(errors, f"gap-map:{lineno}: missing fields {missing}")
            continue
        row_id = int(rec["row_id"])
        if row_id in seen:
            add(errors, f"gap-map:{lineno}: duplicate row {row_id}")
        seen.add(row_id)
        seg = segments.get(row_id)
        if not seg:
            add(errors, f"gap-map:{lineno}: unknown row {row_id}")
            continue
        if rec["segment_id"] != seg["segment_id"]:
            add(errors, f"gap-map:{lineno}: segment_id mismatch row {row_id}")
        if str(rec["toc_id"]) != str(seg.get("toc_id")):
            add(errors, f"gap-map:{lineno}: toc_id mismatch row {row_id}")
        if rec["clean_md_path"] != seg["source_paths"]["clean_md_relpath"]:
            add(errors, f"gap-map:{lineno}: clean path mismatch row {row_id}")
        if int(rec["char_count"]) != int(seg["clean_md"]["char_count"]):
            add(errors, f"gap-map:{lineno}: char_count mismatch row {row_id}")
        if rec["gap_type"] != "baseline_w1_w2_only":
            add(errors, f"gap-map:{lineno}: unexpected gap_type {rec['gap_type']}")
        layers = rec.get("current_layers")
        if not isinstance(layers, list) or "W1" not in layers or "W2" not in layers:
            add(errors, f"gap-map:{lineno}: current_layers must include W1 and W2")
        if rec.get("recommended_action") == "w3+w5+w10" or rec.get("priority_tier") == "target-full-overlap":
            targets.add(row_id)
    if len(seen) != 49:
        add(errors, f"gap-map: expected 49 baseline W1/W2-only rows, found {len(seen)}")
    if len(targets) < 35:
        add(errors, f"gap-map: expected at least 35 target rows, found {len(targets)}")
    return targets


def validate_evidence(repo: Path, segments: dict[int, dict[str, Any]], target_rows: set[int], errors: list[str]) -> set[str]:
    path = repo / EVIDENCE_BANK
    if not path.exists():
        add(errors, f"missing {EVIDENCE_BANK}")
        return set()
    ids: set[str] = set()
    by_row: dict[int, int] = {}
    required = {"evidence_id", "row_id", "segment_id", "toc_id", "clean_md_path", "quote", "absorption_tags", "quote_role"}
    for lineno, rec in iter_jsonl(path):
        if "__parse_error__" in rec:
            add(errors, f"evidence:{lineno}: JSON parse error {rec['__parse_error__']}")
            continue
        missing = sorted(required - set(rec))
        if missing:
            add(errors, f"evidence:{lineno}: missing fields {missing}")
            continue
        eid = str(rec["evidence_id"])
        if eid in ids:
            add(errors, f"evidence:{lineno}: duplicate evidence_id {eid}")
        ids.add(eid)
        row_id = int(rec["row_id"])
        by_row[row_id] = by_row.get(row_id, 0) + 1
        seg = segments.get(row_id)
        if not seg:
            add(errors, f"evidence:{lineno}: unknown row {row_id}")
            continue
        if rec["segment_id"] != seg["segment_id"] or str(rec["toc_id"]) != str(seg.get("toc_id")):
            add(errors, f"evidence:{lineno}: row metadata mismatch {row_id}")
        if rec["clean_md_path"] != seg["source_paths"]["clean_md_relpath"]:
            add(errors, f"evidence:{lineno}: clean path mismatch {row_id}")
        check_quote(repo, segments, row_id, str(rec["quote"]), errors, f"evidence:{eid}")
    for row_id in sorted(target_rows):
        if by_row.get(row_id, 0) < 3:
            add(errors, f"evidence: target row {row_id} has {by_row.get(row_id, 0)} quotes; expected >=3")
    return ids


def validate_w3(repo: Path, segments: dict[int, dict[str, Any]], target_rows: set[int], errors: list[str]) -> set[str]:
    ids: set[str] = set()
    rows: set[int] = set()
    count = 0
    for lineno, rec in iter_jsonl(repo / W3_PATH):
        if rec.get("batch_id") != W3_BATCH:
            continue
        count += 1
        sid = str(rec.get("sense_id", ""))
        ids.add(sid)
        if rec.get("status") != "draft":
            add(errors, f"w3:{lineno}:{sid}: status must be draft")
        if not re.fullmatch(r"term:.+:s\d{2}", sid):
            add(errors, f"w3:{lineno}: bad sense_id {sid}")
        src_rows: set[int] = set()
        source_segments = rec.get("source_segments") or []
        if not isinstance(source_segments, list):
            add(errors, f"w3:{lineno}:{sid}: source_segments must be a list")
            source_segments = []
        for src in source_segments:
            if not isinstance(src, dict):
                add(errors, f"w3:{lineno}:{sid}: bad source row")
                continue
            row_value = src.get("row_id")
            if row_value is None:
                add(errors, f"w3:{lineno}:{sid}: bad source row")
                continue
            try:
                row_id = int(row_value)
            except (TypeError, ValueError):
                add(errors, f"w3:{lineno}:{sid}: bad source row")
                continue
            src_rows.add(row_id)
            rows.add(row_id)
        quotes = rec.get("evidence_quotes") or []
        if not isinstance(quotes, list):
            add(errors, f"w3:{lineno}:{sid}: evidence_quotes must be a list")
            quotes = []
        if len(quotes) < 2:
            add(errors, f"w3:{lineno}:{sid}: too few evidence quotes")
        for q in quotes:
            if not isinstance(q, dict):
                add(errors, f"w3:{lineno}:{sid}: bad evidence quote")
                continue
            row_value = q.get("row_id")
            if row_value is None:
                add(errors, f"w3:{lineno}:{sid}: bad evidence quote row")
                continue
            try:
                row_id = int(row_value)
            except (TypeError, ValueError):
                add(errors, f"w3:{lineno}:{sid}: bad evidence quote row")
                continue
            if row_id not in src_rows:
                add(errors, f"w3:{lineno}:{sid}: quote row {row_id} not declared in source_segments")
            check_quote(repo, segments, row_id, str(q.get("quote", "")), errors, f"w3:{sid}")
    if not (60 <= count <= 90):
        add(errors, f"w3: expected 60-90 records for {W3_BATCH}, found {count}")
    missing = sorted(target_rows - rows)
    if missing:
        add(errors, f"w3: target rows without W3 source coverage: {missing[:20]}")
    return ids


def validate_w5(repo: Path, segments: dict[int, dict[str, Any]], target_rows: set[int], sense_ids: set[str], errors: list[str]) -> set[str]:
    ids: set[str] = set()
    rows: set[int] = set()
    count = 0
    for lineno, rec in iter_jsonl(repo / W5_PATH):
        if rec.get("batch_id") != W5_BATCH:
            continue
        count += 1
        rid = str(rec.get("relation_id", ""))
        ids.add(rid)
        if rec.get("status") != "draft":
            add(errors, f"w5:{lineno}:{rid}: status must be draft")
        if rec.get("relation_type") not in ALLOWED_REL_TYPES:
            add(errors, f"w5:{lineno}:{rid}: bad relation_type {rec.get('relation_type')}")
        for pos_field in ("source_position", "target_position"):
            pos = str(rec.get(pos_field, ""))
            if not (repo / f"knowledge/position-cards/{pos}.md").exists():
                add(errors, f"w5:{lineno}:{rid}: missing {pos_field} {pos}")
        for sid in rec.get("source_senses") or []:
            if str(sid).startswith("term:") and sid not in sense_ids:
                add(errors, f"w5:{lineno}:{rid}: source_sense missing {sid}")
        evs = rec.get("evidence_segment") or []
        if not isinstance(evs, list):
            add(errors, f"w5:{lineno}:{rid}: evidence_segment must be a list")
            evs = []
        if not evs:
            add(errors, f"w5:{lineno}:{rid}: missing evidence_segment")
        for ev in evs:
            if not isinstance(ev, dict):
                add(errors, f"w5:{lineno}:{rid}: bad evidence segment")
                continue
            row_value = ev.get("row_id")
            if row_value is None:
                add(errors, f"w5:{lineno}:{rid}: bad evidence row")
                continue
            try:
                row_id = int(row_value)
            except (TypeError, ValueError):
                add(errors, f"w5:{lineno}:{rid}: bad evidence row")
                continue
            rows.add(row_id)
            check_quote(repo, segments, row_id, str(ev.get("quote", "")), errors, f"w5:{rid}")
    if not (60 <= count <= 80):
        add(errors, f"w5: expected 60-80 records for {W5_BATCH}, found {count}")
    missing = sorted(target_rows - rows)
    if missing:
        add(errors, f"w5: target rows without W5 evidence coverage: {missing[:20]}")
    return ids


def validate_w10(repo: Path, segments: dict[int, dict[str, Any]], target_rows: set[int], errors: list[str]) -> set[str]:
    ids: set[str] = set()
    rows: set[int] = set()
    cards = sorted((repo / W10_ROOT).glob("*-cards/*universal-phase-b*.md"))
    for path in cards:
        meta = load_card_meta(path)
        cid = str(meta.get("card_id", ""))
        ids.add(cid)
        if meta.get("status") != "pilot-draft":
            add(errors, f"w10:{path}: status must be pilot-draft")
        row_id = int(meta.get("row_id", -1))
        rows.add(row_id)
        seg = segments.get(row_id)
        if not seg:
            add(errors, f"w10:{path}: unknown row {row_id}")
            continue
        if str(meta.get("segment_id")) != seg["segment_id"]:
            add(errors, f"w10:{path}: segment mismatch row {row_id}")
        if str(meta.get("source_clean_path")) != seg["source_paths"]["clean_md_relpath"]:
            add(errors, f"w10:{path}: clean path mismatch row {row_id}")
        quotes = meta.get("evidence_quotes") or []
        if len(quotes) < 3:
            add(errors, f"w10:{path}: expected >=3 evidence quotes")
        for q in quotes:
            check_quote(repo, segments, row_id, str(q), errors, f"w10:{cid}")
        body = path.read_text(encoding="utf-8").split("---", 2)[-1]
        for i in range(1, len(quotes) + 1):
            if f"[q{i}]" not in body:
                add(errors, f"w10:{path}: missing [q{i}] body reference")
    if not (35 <= len(cards) <= 50):
        add(errors, f"w10: expected 35-50 Universal-B cards, found {len(cards)}")
    missing = sorted(target_rows - rows)
    if missing:
        add(errors, f"w10: target rows without Universal-B W10 card: {missing[:20]}")
    return ids


def validate_synthesis_markers(repo: Path, evidence_ids: set[str], term_ids: set[str], relation_ids: set[str], w10_ids: set[str], errors: list[str]) -> None:
    for rel in SYNTHESIS_FILES:
        path = repo / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "external" in text.lower() and "not a final encyclopedia" not in text:
            add(errors, f"synthesis:{rel}: possible externalized claim without phase boundary")
        for kind, ident in re.findall(r"\[(E|T|R|W10):([^\]]+)\]", text):
            if kind == "E" and ident not in evidence_ids:
                add(errors, f"synthesis:{rel}: unknown evidence marker {ident}")
            elif kind == "T" and ident not in term_ids:
                add(errors, f"synthesis:{rel}: unknown term marker {ident}")
            elif kind == "R" and ident not in relation_ids:
                add(errors, f"synthesis:{rel}: unknown relation marker {ident}")
            elif kind == "W10" and ident not in w10_ids:
                add(errors, f"synthesis:{rel}: unknown W10 marker {ident}")


def compute_metrics(repo: Path) -> dict[str, Any]:
    segments = load_segments(repo)
    all_rows = set(segments)
    w3: set[int] = set()
    w5: set[int] = set()
    w10: set[int] = set()
    for _, rec in iter_jsonl(repo / W3_PATH):
        source_segments = rec.get("source_segments") or []
        if not isinstance(source_segments, list):
            continue
        for src in source_segments:
            if isinstance(src, dict) and "row_id" in src:
                w3.add(int(src["row_id"]))
    for _, rec in iter_jsonl(repo / W5_PATH):
        evidence_segments = rec.get("evidence_segment") or []
        if not isinstance(evidence_segments, list):
            continue
        for ev in evidence_segments:
            if isinstance(ev, dict) and "row_id" in ev:
                w5.add(int(ev["row_id"]))
    for path in (repo / W10_ROOT).glob("*-cards/*.md"):
        meta = load_card_meta(path)
        if meta.get("row_id"):
            w10.add(int(meta["row_id"]))
    any_rows = w3 | w5 | w10
    full = w3 & w5 & w10
    total_chars = sum(int(segments[r]["clean_md"]["char_count"]) for r in all_rows)
    any_chars = sum(int(segments[r]["clean_md"]["char_count"]) for r in any_rows)
    field_rows: dict[str, dict[str, int]] = {}
    for field in sorted({str(segments[r]["matrix_axes"].get("field")) for r in all_rows}):
        rows = {r for r in all_rows if str(segments[r]["matrix_axes"].get("field")) == field}
        field_rows[field] = {
            "rows": len(rows),
            "w1_w2_only": len(rows - any_rows),
            "w3": len(rows & w3),
            "w5": len(rows & w5),
            "w10": len(rows & w10),
            "full": len(rows & full),
        }
    return {
        "total_rows": len(all_rows),
        "w3_rows": len(w3),
        "w5_rows": len(w5),
        "w10_rows": len(w10),
        "any_rows": len(any_rows),
        "w1_w2_only_rows": len(all_rows - any_rows),
        "full_overlap_rows": len(full),
        "clean_text_volume_any_pct": round(any_chars / total_chars * 100, 2),
        "field_rows": field_rows,
    }


def check_protected_corpus(repo: Path, segments: dict[int, dict[str, Any]], errors: list[str]) -> None:
    for row_id, seg in segments.items():
        for layer, relkey in (("raw_md", "raw_md_relpath"), ("clean_md", "clean_md_relpath")):
            info = seg.get(layer) or {}
            expected = info.get("sha256")
            rel = seg["source_paths"].get(relkey)
            if not expected or not rel:
                continue
            path = repo / rel
            if not path.exists():
                add(errors, f"protected:{row_id}:{layer}: file missing {rel}")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected:
                add(errors, f"protected:{row_id}:{layer}: sha256 mismatch {rel}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate Universal Absorption Phase B artifacts")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    segments = load_segments(repo)

    target_rows = validate_gap_map(repo, segments, errors)
    evidence_ids = validate_evidence(repo, segments, target_rows, errors)
    term_ids = validate_w3(repo, segments, target_rows, errors)
    relation_ids = validate_w5(repo, segments, target_rows, term_ids, errors)
    w10_ids = validate_w10(repo, segments, target_rows, errors)
    validate_synthesis_markers(repo, evidence_ids, term_ids, relation_ids, w10_ids, errors)

    metrics = compute_metrics(repo)
    if args.final:
        for rel in REQUIRED_DOCS_FINAL:
            if not (repo / rel).exists():
                add(errors, f"final: missing required doc {rel}")
        if metrics["w1_w2_only_rows"] > 25:
            add(errors, f"final: W1/W2-only rows {metrics['w1_w2_only_rows']} exceeds Phase B conservative target 25")
        if metrics["clean_text_volume_any_pct"] < 96.0:
            add(errors, f"final: any-layer clean volume {metrics['clean_text_volume_any_pct']} below 96%")
        if metrics["full_overlap_rows"] < 205:
            add(errors, f"final: full overlap rows {metrics['full_overlap_rows']} below 205")
        if metrics["w10_rows"] < 240:
            add(errors, f"final: W10 rows {metrics['w10_rows']} below 240")
        if metrics["w3_rows"] < 320:
            add(errors, f"final: W3 rows {metrics['w3_rows']} below 320")
        if metrics["w5_rows"] < 240:
            add(errors, f"final: W5 rows {metrics['w5_rows']} below 240")
        check_protected_corpus(repo, segments, errors)

    summary = {
        "status": "FAIL" if errors else "PASS",
        "errors": errors,
        "target_rows": len(target_rows),
        "evidence_ids": len(evidence_ids),
        "w3_universal_records": len(term_ids),
        "w5_universal_records": len(relation_ids),
        "w10_universal_cards": len(w10_ids),
        "metrics": metrics,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"validate_universal_absorption_phase_b: {summary['status']}")
        print(json.dumps({k: v for k, v in summary.items() if k != "errors"}, ensure_ascii=False, indent=2))
        for err in errors[:120]:
            print("ERROR", err)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
