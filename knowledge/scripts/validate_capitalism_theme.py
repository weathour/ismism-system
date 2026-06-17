#!/usr/bin/env python3
"""Validate the Capitalism / Political Economy maximum absorption layer.

This validator is deliberately repo-local and conservative. It checks row/class
ownership, exact quote substrings, taxonomy consistency, Capitalism W3/W5 draft
batches, Capitalism W10 pilot-card coverage, and parseable synthesis markers.
It treats this theme as an ISMISM evidence layer, not an external economics or
Marxism encyclopedia.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

THEME_ROOT = Path("knowledge/themes/capitalism")
MANIFEST = THEME_ROOT / "capitalism-row-manifest.jsonl"
EVIDENCE = THEME_ROOT / "capitalism-evidence-bank.jsonl"
TAXONOMY = THEME_ROOT / "capitalism-taxonomy.md"
README = THEME_ROOT / "README.md"
QUERY_HELPER = Path("knowledge/scripts/query_capitalism_theme.py")
W3_BATCH = "W3-CAPITALISM-2026-06-16"
W5_BATCH = "W5-CAPITALISM-2026-06-16"
APPEND_ONLY_ALLOWED_BATCHES = {
    "knowledge/lexicon/term-senses.jsonl": {
        "W3-TIME-DEATH-LIFE-2026-06-15",
        W3_BATCH,
        "W3-UNIVERSAL-A-2026-06-16",
        "W3-UNIVERSAL-B-2026-06-16",
        "W3-FEMINISM-2026-06-16",
        "W3-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16",
        "W3-AESTHETICS-MEDIA-2026-06-16",
        "W3-LABOR-WORKPLACE-PRECARITY-2026-06-16",
        "W3-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16",
        "W3-FAMILY-INTIMACY-REPRODUCTION-2026-06-16",
        "W3-CONSUMPTION-DESIRE-LIFESTYLE-2026-06-16",
        "W3-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16",
        "W3-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16",
        "W3-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16",
        "W3-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16",
        "W3-URBAN-HOUSING-MIGRATION-SPACE-2026-06-16",
        "W3-HEALTH-BODY-RISK-SOCIETY-2026-06-16",
    },
    "knowledge/relations/relation-assets.jsonl": {
        "W5-TIME-DEATH-LIFE-2026-06-15",
        W5_BATCH,
        "W5-UNIVERSAL-A-2026-06-16",
        "W5-UNIVERSAL-B-2026-06-16",
        "W5-FEMINISM-2026-06-16",
        "W5-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16",
        "W5-AESTHETICS-MEDIA-2026-06-16",
        "W5-LABOR-WORKPLACE-PRECARITY-2026-06-16",
        "W5-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16",
        "W5-FAMILY-INTIMACY-REPRODUCTION-2026-06-16",
        "W5-CONSUMPTION-DESIRE-LIFESTYLE-2026-06-16",
        "W5-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16",
        "W5-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16",
        "W5-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16",
        "W5-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16",
        "W5-URBAN-HOUSING-MIGRATION-SPACE-2026-06-16",
        "W5-HEALTH-BODY-RISK-SOCIETY-2026-06-16",
    },
}
SYNTHESIS_FILES = [
    THEME_ROOT / "capitalism-critique-and-fetishism-synthesis.md",
    THEME_ROOT / "political-economy-and-production-synthesis.md",
    THEME_ROOT / "capital-socialization-and-practice-synthesis.md",
    THEME_ROOT / "finance-imperialism-and-global-capital-synthesis.md",
]

CLASS_ROWS: dict[str, set[int]] = {
    "capitalism-core-critique": {275, 277, 279, 280},
    "political-economy-method": {255, 261, 276, 278, 285, 290, 291, 292, 293, 295},
    "commodity-fetishism-symbolic-order": {34, 36, 320},
    "consumption-enjoyment-market": {7, 52, 53, 85, 268, 343, 347},
    "finance-capital-abstraction": {247, 248, 317, 318},
    "production-relations-forces": {321, 322, 323, 324, 327, 331, 342},
    "labor-alienation-subjectivation": {2, 17, 230, 328, 344},
    "class-bourgeois-proletarian": {9, 174, 184, 298, 305, 311, 312, 313, 314, 315},
    "imperialism-global-capital": {83, 319, 325, 336},
    "capital-socialization-practice": {332, 333, 334, 335, 337, 341},
    "economic-life-organization": {326, 329, 330},
    "reproduction-legitimacy": {300, 304, 309, 340},
    "agriculture-delocalization": {338},
    "de-agency-financial-mediation": {339},
    "ideology-culture-capital": {82, 159, 253, 270, 274, 294},
    "ecology-industry-capital": {84},
    "gender-family-economic-liberation": {90},
    "peripheral-or-noise": {75, 201, 273, 281, 282, 284, 286, 287, 289, 308, 316},
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
REQUIRED_RING1 = {248, 275, 277, 279, 280, 323, 324, 330, 331, 335, 337, 338, 339, 341}
W10_REQUIRED_PRIORITY = {248, 275, 277, 279, 280, 323, 330, 337, 338, 339}
REL_TYPES = {
    "boundary-between",
    "route-from-to",
    "tension-between",
    "mediates-between",
    "transitions-to",
    "blocks-transition",
    "misrecognizes-as",
    "objectifies",
    "subjectivizes",
    "overcodes",
    "represents-position",
    "evidences-claim",
}
FINAL_DOC_MARKERS = {
    Path("README.md"): [
        "Capitalism / Political Economy maximum absorption layer",
        "validate_capitalism_theme.py",
        "query_capitalism_theme.py",
    ],
    Path("AGENTS.md"): [
        "knowledge/themes/capitalism/README.md",
        "Capitalism / Political Economy maximum absorption layer",
    ],
    Path("knowledge/STATE.md"): [
        "Capitalism / Political Economy maximum absorption",
        "validate_capitalism_theme.py",
    ],
    Path("ISMISM-MAINLINE-HANDOFF.md"): [
        "Capitalism / Political Economy maximum absorption",
        "capitalism-row-manifest.jsonl",
    ],
    Path("DIRECTORY_MAP.md"): [
        "knowledge/themes/capitalism/",
        "validate_capitalism_theme.py",
        "query_capitalism_theme.py",
    ],
    Path("knowledge/README.md"): ["capitalism", "Capitalism / Political Economy"],
    Path("knowledge/query-playbook.md"): [
        "query_capitalism_theme.py",
        "资本主义 / 政治经济 / 生产关系",
    ],
    Path("skills/ismism-knowledge-operator/SKILL.md"): [
        "knowledge/themes/capitalism/README.md",
        "query_capitalism_theme.py",
    ],
}


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def load_jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    out: list[tuple[int, dict[str, Any]]] = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if line.strip():
                out.append((lineno, json.loads(line)))
    return out


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    return {int(rec["row_id"]): rec for _, rec in load_jsonl(repo / "knowledge/manifests/segments.jsonl")}


def toc_to_scalar(value: Any) -> str:
    return "None" if value is None else str(value)


def validate_quote(repo: Path, clean_rel: str, quote: str, where: str, errors: list[str]) -> None:
    clean_path = repo / clean_rel
    if not clean_path.exists():
        add(errors, f"{where}: clean path missing {clean_rel}")
        return
    text = clean_path.read_text(encoding="utf-8")
    if quote not in text:
        add(errors, f"{where}: quote not exact substring: {quote[:100]}")


def parse_w10_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    meta: dict[str, Any] = {}
    key: str | None = None
    if not lines or lines[0].strip() != "---":
        return meta
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


def load_w10_capitalism(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[dict[int, list[str]], set[str]]:
    rows: dict[int, list[str]] = {}
    ids: set[str] = set()
    for p in sorted((repo / "knowledge/w10-absorption").glob("*-cards/*.md")):
        meta = parse_w10_frontmatter(p)
        cid = str(meta.get("card_id", ""))
        if ":capitalism-" not in cid:
            continue
        ids.add(cid)
        try:
            row = int(str(meta.get("row_id", "")))
        except (TypeError, ValueError):
            add(errors, f"Capitalism W10 card has bad row_id: {p}")
            continue
        rows.setdefault(row, []).append(cid)
        quotes = meta.get("evidence_quotes", []) or []
        if len(quotes) != len(set(quotes)):
            add(errors, f"Capitalism W10 duplicate evidence quote in {p}")
        seg = segments.get(row)
        if seg:
            clean_rel = seg["source_paths"]["clean_md_relpath"]
            for idx, quote in enumerate(quotes, 1):
                validate_quote(repo, clean_rel, str(quote), f"{p}:evidence_quotes[{idx}]", errors)
    return rows, ids


def validate_manifest_evidence(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[dict[int, dict[str, Any]], dict[str, dict[str, Any]], dict[int, int]]:
    manifest_path = repo / MANIFEST
    evidence_path = repo / EVIDENCE
    for p in [
        manifest_path,
        evidence_path,
        repo / TAXONOMY,
        repo / README,
        repo / QUERY_HELPER,
        *[repo / f for f in SYNTHESIS_FILES],
    ]:
        if not p.exists():
            add(errors, f"missing {p.relative_to(repo)}")
    if not manifest_path.exists() or not evidence_path.exists():
        return {}, {}, {}

    manifest: dict[int, dict[str, Any]] = {}
    for lineno, rec in load_jsonl(manifest_path):
        row = rec.get("row_id")
        if not isinstance(row, int):
            add(errors, f"{MANIFEST}:{lineno}: row_id must be int")
            continue
        if row in manifest:
            add(errors, f"{MANIFEST}:{lineno}: duplicate row {row}")
        manifest[row] = rec
        seg = segments.get(row)
        if not seg:
            add(errors, f"{MANIFEST}:{lineno}: row {row} not in segments.jsonl")
            continue
        if rec.get("segment_id") != seg.get("segment_id"):
            add(errors, f"{MANIFEST}:{lineno}: row {row} segment_id mismatch")
        if str(rec.get("toc_id")) != toc_to_scalar(seg.get("toc_id")):
            add(errors, f"{MANIFEST}:{lineno}: row {row} toc_id mismatch")
        if rec.get("clean_md_path") != seg["source_paths"]["clean_md_relpath"]:
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean path mismatch")
        if str(rec.get("field")) != str(seg["matrix_axes"].get("field")):
            add(errors, f"{MANIFEST}:{lineno}: row {row} field mismatch")
        cls = rec.get("theme_class")
        if cls not in THEME_CLASSES:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad theme_class {cls!r}")
        elif row not in CLASS_ROWS[cls]:
            add(errors, f"{MANIFEST}:{lineno}: row {row} assigned to {cls}, expected exact class map")
        if rec.get("core_status") not in CORE_STATUS:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad core_status")
        if rec.get("recommended_action") not in RECOMMENDED_ACTION:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad recommended_action {rec.get('recommended_action')!r}")
        if not isinstance(rec.get("keyword_hits"), dict):
            add(errors, f"{MANIFEST}:{lineno}: row {row} keyword_hits must be object")
        if row in REQUIRED_RING1 and rec.get("core_status") != "core":
            add(errors, f"{MANIFEST}:{lineno}: Ring1 row {row} must be core")

    if set(manifest) != EXPECTED_ROWS:
        add(
            errors,
            "manifest rows mismatch: "
            f"missing={sorted(EXPECTED_ROWS-set(manifest))}, "
            f"extra={sorted(set(manifest)-EXPECTED_ROWS)}",
        )
    if not 75 <= len(manifest) <= 90:
        add(errors, f"manifest row count outside [75,90]: {len(manifest)}")
    missing_ring1 = sorted(REQUIRED_RING1 - set(manifest))
    if missing_ring1:
        add(errors, f"manifest missing Ring1 rows: {missing_ring1}")

    evidence: dict[str, dict[str, Any]] = {}
    count_by_row: dict[int, int] = {}
    for lineno, rec in load_jsonl(evidence_path):
        eid = str(rec.get("evidence_id", ""))
        if not re.fullmatch(r"ev:cap:\d{4}:\d{2}", eid):
            add(errors, f"{EVIDENCE}:{lineno}: bad evidence_id {eid!r}")
        if eid in evidence:
            add(errors, f"{EVIDENCE}:{lineno}: duplicate evidence_id {eid}")
        evidence[eid] = rec
        row_raw = rec.get("row_id")
        if row_raw is None:
            add(errors, f"{EVIDENCE}:{lineno}: bad row_id")
            continue
        try:
            row = int(row_raw)
        except (TypeError, ValueError):
            add(errors, f"{EVIDENCE}:{lineno}: bad row_id")
            continue
        if row not in manifest:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} not in manifest")
            continue
        seg = segments[row]
        if rec.get("segment_id") != seg.get("segment_id") or str(rec.get("toc_id")) != toc_to_scalar(
            seg.get("toc_id")
        ):
            add(errors, f"{EVIDENCE}:{lineno}: row {row} segment/toc mismatch")
        clean_rel = seg["source_paths"]["clean_md_relpath"]
        if rec.get("clean_md_path") != clean_rel:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} clean path mismatch")
        quote = str(rec.get("quote", ""))
        if not quote.strip():
            add(errors, f"{EVIDENCE}:{lineno}: empty quote")
        else:
            validate_quote(repo, clean_rel, quote, f"{EVIDENCE}:{lineno}:{eid}", errors)
        count_by_row[row] = count_by_row.get(row, 0) + 1

    for row, rec in manifest.items():
        if int(rec.get("evidence_quote_count", -1)) != count_by_row.get(row, 0):
            add(
                errors,
                f"manifest/evidence quote count mismatch for row {row}: "
                f"manifest={rec.get('evidence_quote_count')} evidence={count_by_row.get(row,0)}",
            )
        if rec.get("core_status") == "core" and count_by_row.get(row, 0) < 3:
            add(errors, f"core row {row} has fewer than 3 quotes")
    return manifest, evidence, count_by_row


def validate_taxonomy(
    repo: Path,
    manifest: dict[int, dict[str, Any]],
    evidence: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    path = repo / TAXONOMY
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    current: str | None = None
    owner: dict[int, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("- theme_class:"):
            m = re.search(r"`([^`]+)`", line)
            current = m.group(1) if m else None
            if current not in THEME_CLASSES:
                add(errors, f"taxonomy bad theme_class {current!r}")
        elif line.startswith("- rows:") and current:
            rows = [int(x) for x in re.findall(r"row (\d+)", line)]
            for row in rows:
                if row in owner:
                    add(errors, f"taxonomy duplicate row ownership row {row}: {owner[row]} and {current}")
                owner[row] = current
                if row not in manifest:
                    add(errors, f"taxonomy row {row} not in manifest")
                elif manifest[row].get("theme_class") != current:
                    add(
                        errors,
                        f"taxonomy class mismatch row {row}: "
                        f"taxonomy={current}, manifest={manifest[row].get('theme_class')}",
                    )
        elif "ev:cap:" in line:
            for eid in re.findall(r"ev:cap:\d{4}:\d{2}", line):
                if eid not in evidence:
                    add(errors, f"taxonomy unknown evidence id {eid}")
    missing = sorted(set(manifest) - set(owner))
    if missing:
        add(errors, f"taxonomy missing manifest rows: {missing}")


def validate_w3(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[set[str], list[dict[str, Any]]]:
    path = repo / "knowledge/lexicon/term-senses.jsonl"
    all_ids: set[str] = set()
    batch: list[dict[str, Any]] = []
    seen: set[str] = set()
    for lineno, rec in load_jsonl(path):
        sid = str(rec.get("sense_id", ""))
        if sid in seen:
            add(errors, f"{path}:{lineno}: duplicate sense_id {sid}")
        seen.add(sid)
        all_ids.add(sid)
        if rec.get("batch_id") != W3_BATCH:
            continue
        batch.append(rec)
        if rec.get("status") != "draft":
            add(errors, f"{path}:{lineno}: Capitalism W3 non-draft {sid}")
        if not re.fullmatch(r"term:.+:s\d{2}", sid):
            add(errors, f"{path}:{lineno}: bad Capitalism sense_id {sid}")
        source_rows = {
            int(src.get("row_id"))
            for src in rec.get("source_segments", [])
            if str(src.get("row_id", "")).isdigit()
        }
        quotes = rec.get("evidence_quotes", [])
        if not isinstance(quotes, list) or len(quotes) < 2:
            add(errors, f"{path}:{lineno}: Capitalism W3 {sid} needs at least 2 evidence quotes")
            continue
        for q in quotes:
            try:
                row = int(q.get("row_id"))
            except (TypeError, ValueError):
                add(errors, f"{path}:{lineno}: bad quote row for {sid}")
                continue
            if row not in source_rows:
                add(errors, f"{path}:{lineno}: quote row {row} not declared in source_segments for {sid}")
            seg = segments.get(row)
            if not seg:
                add(errors, f"{path}:{lineno}: quote row {row} missing from segments")
                continue
            validate_quote(
                repo,
                seg["source_paths"]["clean_md_relpath"],
                str(q.get("quote", "")),
                f"{path}:{lineno}:{sid}",
                errors,
            )
    if not 55 <= len(batch) <= 75:
        add(errors, f"Capitalism W3 batch count outside [55,75]: {len(batch)}")
    return all_ids, batch


def validate_w5(
    repo: Path,
    sense_ids: set[str],
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    path = repo / "knowledge/relations/relation-assets.jsonl"
    batch: list[dict[str, Any]] = []
    seen: set[str] = set()
    for lineno, rec in load_jsonl(path):
        rid = str(rec.get("relation_id", ""))
        if rid in seen:
            add(errors, f"{path}:{lineno}: duplicate relation_id {rid}")
        seen.add(rid)
        if rec.get("batch_id") != W5_BATCH:
            continue
        batch.append(rec)
        if not re.fullmatch(r"rel:capitalism:\d{3}", rid):
            add(errors, f"{path}:{lineno}: bad Capitalism relation_id {rid}")
        if rec.get("status") != "draft":
            add(errors, f"{path}:{lineno}: Capitalism W5 non-draft {rid}")
        if rec.get("relation_type") not in REL_TYPES:
            add(errors, f"{path}:{lineno}: bad relation_type {rec.get('relation_type')!r}")
        for field in ["source", "target"]:
            val = str(rec.get(field, ""))
            if val.startswith("term:") and val not in sense_ids:
                add(errors, f"{path}:{lineno}: missing sense ref {field}={val}")
        evs = rec.get("evidence_segment", [])
        if not isinstance(evs, list) or not evs:
            add(errors, f"{path}:{lineno}: missing evidence_segment for {rid}")
            continue
        for ev in evs:
            try:
                row = int(ev.get("row_id"))
            except (TypeError, ValueError):
                add(errors, f"{path}:{lineno}: bad evidence row for {rid}")
                continue
            seg = segments.get(row)
            if not seg:
                add(errors, f"{path}:{lineno}: evidence row {row} missing from segments")
                continue
            validate_quote(
                repo,
                seg["source_paths"]["clean_md_relpath"],
                str(ev.get("quote", "")),
                f"{path}:{lineno}:{rid}",
                errors,
            )
    if not 45 <= len(batch) <= 65:
        add(errors, f"Capitalism W5 batch count outside [45,65]: {len(batch)}")
    return batch


def validate_syntheses(
    repo: Path,
    evidence: dict[str, dict[str, Any]],
    sense_ids: set[str],
    w10_ids: set[str],
    errors: list[str],
) -> None:
    rel_ids = {
        str(rec.get("relation_id"))
        for _, rec in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")
        if rec.get("batch_id") == W5_BATCH
    }
    for rel_path in SYNTHESIS_FILES:
        path = repo / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        claim_lines = [
            ln
            for ln in text.splitlines()
            if ln.strip().startswith("- ")
            and not ln.strip().startswith("- status")
            and not ln.strip().startswith("- boundary")
        ]
        if not claim_lines:
            add(errors, f"{rel_path}: no claim bullets")
        for line in claim_lines:
            markers = re.findall(
                r"ev:[\w-]+:\d{4}:\d{2}|term:[^`\s]+:s\d{2}|"
                r"rel:[\w-]+:\d{3}|w10:(?:arg|proc|case):\d{4}:[\w-]+|row \d+",
                line,
            )
            if not markers:
                add(errors, f"{rel_path}: claim lacks parseable marker: {line[:100]}")
            for marker in markers:
                if marker.startswith("ev:") and marker not in evidence:
                    add(errors, f"{rel_path}: unknown evidence marker {marker}")
                elif marker.startswith("term:") and marker not in sense_ids:
                    add(errors, f"{rel_path}: unknown term marker {marker}")
                elif marker.startswith("rel:") and marker not in rel_ids:
                    add(errors, f"{rel_path}: unknown relation marker {marker}")
                elif marker.startswith("w10:") and marker not in w10_ids:
                    add(errors, f"{rel_path}: unknown W10 marker {marker}")
                elif marker.startswith("row ") and int(marker.split()[1]) not in EXPECTED_ROWS:
                    add(errors, f"{rel_path}: row marker not in Capitalism manifest {marker}")
        # Also catch any malformed/unknown explicit markers anywhere in the doc.
        for marker in re.findall(r"ev:[\w:-]+|rel:[\w:-]+|w10:[\w:-]+", text):
            marker = marker.rstrip(".,;)]")
            if marker.startswith("ev:") and re.fullmatch(r"ev:[\w-]+:\d{4}:\d{2}", marker) and marker not in evidence:
                add(errors, f"{rel_path}: unknown evidence marker {marker}")
            if marker.startswith("rel:") and re.fullmatch(r"rel:[\w-]+:\d{3}", marker) and marker not in rel_ids:
                add(errors, f"{rel_path}: unknown relation marker {marker}")
            if (
                marker.startswith("w10:")
                and re.fullmatch(r"w10:(?:arg|proc|case):\d{4}:[\w-]+", marker)
                and marker not in w10_ids
            ):
                add(errors, f"{rel_path}: unknown W10 marker {marker}")


def validate_final_docs(repo: Path, errors: list[str]) -> None:
    for rel_path, markers in FINAL_DOC_MARKERS.items():
        path = repo / rel_path
        if not path.exists():
            add(errors, f"final doc missing {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                add(errors, f"final doc {rel_path} missing marker {marker!r}")
    readme_text = (repo / README).read_text(encoding="utf-8") if (repo / README).exists() else ""
    if "not** an external encyclopedia" not in readme_text:
        add(errors, "Capitalism README must state it is not an external encyclopedia")


def _jsonl_records_from_text(
    text: str,
    rel_path: str,
    origin: str,
    errors: list[str],
) -> list[tuple[int, dict[str, Any]]]:
    records: list[tuple[int, dict[str, Any]]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as exc:
            add(errors, f"{rel_path}:{origin}:{lineno}: invalid JSON: {exc}")
            continue
        if not isinstance(rec, dict):
            add(errors, f"{rel_path}:{origin}:{lineno}: JSONL record is not an object")
            continue
        records.append((lineno, rec))
    return records


def _record_label(rec: dict[str, Any]) -> str:
    for key in ("relation_id", "sense_id", "evidence_id", "card_id"):
        if key in rec:
            return f"{key}={rec[key]!r}"
    return f"batch_id={rec.get('batch_id')!r}"


def validate_jsonl_append_only(repo: Path, rel_path: str, allowed_batches: set[str], errors: list[str]) -> None:
    """Validate semantic JSONL append-only behavior for generated knowledge ledgers.

    Earlier theme validators compared byte prefixes against HEAD. Universal Phase A
    legitimately normalizes JSONL serialization while appending later draft batches,
    so this check now preserves the stricter invariant that every HEAD record remains
    present, in order, with equal parsed JSON content; only records after the HEAD
    prefix may be new, and their batch_id must be explicitly allow-listed.
    """
    path = repo / rel_path
    if not path.exists():
        add(errors, f"append-only check missing file {rel_path}")
        return
    try:
        base_text = subprocess.check_output(
            ["git", "-C", str(repo), "show", f"HEAD:{rel_path}"],
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        add(errors, f"append-only check could not read HEAD:{rel_path}: {stderr}")
        return

    current_text = path.read_text(encoding="utf-8")
    base_errors = len(errors)
    base_records = _jsonl_records_from_text(base_text, rel_path, "HEAD", errors)
    current_records = _jsonl_records_from_text(current_text, rel_path, "current", errors)
    if len(errors) != base_errors:
        return

    if len(current_records) < len(base_records):
        add(
            errors,
            f"{rel_path}: current JSONL has {len(current_records)} records, fewer than HEAD {len(base_records)}",
        )
        return

    for idx, ((base_lineno, base_rec), (cur_lineno, cur_rec)) in enumerate(
        zip(base_records, current_records),
        1,
    ):
        if cur_rec != base_rec:
            add(
                errors,
                f"{rel_path}: existing HEAD record {idx} changed "
                f"(HEAD line {base_lineno}, current line {cur_lineno}, {_record_label(base_rec)})",
            )
            return

    for cur_lineno, rec in current_records[len(base_records) :]:
        batch = str(rec.get("batch_id", ""))
        if batch not in allowed_batches:
            add(errors, f"{rel_path}:{cur_lineno}: appended batch_id {batch!r} not in {sorted(allowed_batches)}")


def validate_append_only_gates(repo: Path, errors: list[str]) -> None:
    for rel_path, allowed_batches in APPEND_ONLY_ALLOWED_BATCHES.items():
        validate_jsonl_append_only(repo, rel_path, allowed_batches, errors)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate Capitalism / Political Economy maximum absorption theme")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    try:
        segments = load_segments(repo)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"failed to load segments: {exc}", file=sys.stderr)
        return 2

    manifest, evidence, _ = validate_manifest_evidence(repo, segments, errors)
    validate_taxonomy(repo, manifest, evidence, errors)
    sense_ids, w3_batch = validate_w3(repo, segments, errors)
    w5_batch = validate_w5(repo, sense_ids, segments, errors)
    w10_rows, w10_ids = load_w10_capitalism(repo, segments, errors)
    w10_count = sum(len(v) for v in w10_rows.values())
    if not 35 <= w10_count <= 50:
        add(errors, f"Capitalism W10 card count outside [35,50]: {w10_count}")
    missing_w10 = sorted(W10_REQUIRED_PRIORITY - set(w10_rows))
    if missing_w10:
        add(errors, f"Capitalism W10 missing priority rows: {missing_w10}")
    validate_syntheses(repo, evidence, sense_ids, w10_ids, errors)
    if args.final:
        validate_final_docs(repo, errors)
        validate_append_only_gates(repo, errors)

    summary = {
        "status": "FAIL" if errors else "PASS",
        "manifest_rows": len(manifest),
        "evidence_records": len(evidence),
        "w3_batch": len(w3_batch),
        "w5_batch": len(w5_batch),
        "w10_cards": w10_count,
        "errors": errors,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"validate_capitalism_theme: {summary['status']} manifest={summary['manifest_rows']} "
            f"evidence={summary['evidence_records']} w3={summary['w3_batch']} w5={summary['w5_batch']} "
            f"w10={summary['w10_cards']} errors={len(errors)}"
        )
        for err in errors[:120]:
            print("ERROR", err)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
