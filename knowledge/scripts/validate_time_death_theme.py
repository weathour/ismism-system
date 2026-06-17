#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

THEME_ROOT = Path("knowledge/themes/time-death-finitude-life")
MANIFEST = THEME_ROOT / "time-death-row-manifest.jsonl"
EVIDENCE = THEME_ROOT / "time-death-evidence-bank.jsonl"
TAXONOMY = THEME_ROOT / "time-death-taxonomy.md"
README = THEME_ROOT / "README.md"
W10_COVERAGE = THEME_ROOT / "time-death-w10-coverage.jsonl"
SYNTHESIS_FILES = [
    THEME_ROOT / "time-death-finitude-life-synthesis.md",
    THEME_ROOT / "life-body-immortality-synthesis.md",
    THEME_ROOT / "historical-time-and-practice-synthesis.md",
]
QUERY_HELPER = Path("knowledge/scripts/query_time_death_theme.py")
W3_BATCH = "W3-TIME-DEATH-LIFE-2026-06-15"
W5_BATCH = "W5-TIME-DEATH-LIFE-2026-06-15"

CLASS_ROWS: dict[str, set[int]] = {
    "death-finitude-core": {104, 111, 171, 213, 223, 235},
    "time-cosmos-cycle": {25, 118, 209, 227, 253},
    "aion-festival-eternity": {35, 64, 137},
    "immortality-afterlife": {32, 37},
    "mortality-symbolic-death": {38, 41, 42},
    "aging-maturity-finitude": {61},
    "soul-body-trace": {34, 36, 45},
    "memory-temporal-preservation": {116, 195},
    "buddhist-karma-rebirth-liberation": {120, 121, 122, 123, 124, 134, 140, 141, 186},
    "nirvana-renunciation-salvation": {40, 43, 81},
    "nihilism-pessimism-life-negation": {8, 85, 103, 160, 230},
    "natural-life-body": {76, 84, 132, 173, 175, 208, 326},
    "sexuality-reproduction-life-force": {31, 39},
    "phenomenological-temporality": {191, 206},
    "existential-finitude": {240, 241, 262},
    "historical-time-ideology": {289, 290, 291, 292, 293, 294, 295},
    "practice-against-historical-inertia": {327, 331, 332, 333, 334, 335, 341},
    "ai-immortality-mortality": {350, 351, 352, 357, 362, 363},
    "ai-life-embodiment-memory": {353, 354, 355, 356, 358, 359, 360, 361},
    "peripheral-or-noise": {44},
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
HARD_CORE = {35, 37, 40, 104, 111, 116, 118, 120, 121, 122, 123, 171, 209, 213, 223, 235, 350, 351, 352, 362}
AI_ROWS = set(range(350, 364))
BUDDHIST_CORE = {120, 121, 122, 123, 124, 140, 141, 186}
W10_MATRIX_ROWS = {
    35,
    37,
    40,
    104,
    111,
    116,
    118,
    171,
    209,
    213,
    223,
    235,
    350,
    351,
    352,
    353,
    354,
    355,
    356,
    357,
    358,
    359,
    360,
    361,
    362,
    363,
    120,
    121,
    122,
    123,
    124,
    140,
    141,
    186,
    76,
    81,
    84,
    85,
    132,
    173,
    175,
    230,
    253,
    326,
    227,
    289,
    290,
    291,
    292,
    293,
    294,
    295,
    327,
    331,
    332,
    333,
    334,
    335,
    341,
}
FINAL_DOC_MARKERS = {
    Path("README.md"): [
        "Time-Death-Finitude-Life maximum absorption layer",
        "85-row manifest, 289 quote-bank records",
        "validate_time_death_theme.py",
        "query_time_death_theme.py",
    ],
    Path("AGENTS.md"): [
        "knowledge/themes/time-death-finitude-life/README.md",
        "Time-Death-Finitude-Life maximum absorption layer",
        "时间 / 死亡 / 有限性 / 生命",
    ],
    Path("skills/ismism-knowledge-operator/SKILL.md"): [
        "knowledge/themes/time-death-finitude-life/README.md",
        "Time-Death-Finitude-Life theme questions",
        "query_time_death_theme.py",
        "validate_time_death_theme.py",
    ],
    Path("knowledge/STATE.md"): [
        "Time-Death-Finitude-Life maximum absorption",
        "validate_time_death_theme.py",
    ],
    Path("ISMISM-MAINLINE-HANDOFF.md"): [
        "Time-Death-Finitude-Life maximum absorption",
        "85-row",
    ],
    Path("DIRECTORY_MAP.md"): [
        "knowledge/themes/time-death-finitude-life/",
        "validate_time_death_theme.py",
        "query_time_death_theme.py",
    ],
    Path("knowledge/README.md"): [
        "time-death-finitude-life",
        "Time-Death-Finitude-Life",
    ],
    Path("knowledge/query-playbook.md"): [
        "query_time_death_theme.py",
        "时间 / 死亡 / 有限性 / 生命",
    ],
    Path("knowledge/qa/absorption-strength-distribution.md"): [],
}

FINAL_DOC_FORBIDDEN = {
    Path("README.md"): [
        "705 senses / 357 terms",
        "191 relations / 12 types",
        "122 cards / 3 card types",
        "143/363 rows remain W1/W2-only",
        "64.6% clean-text volume",
        "85 rows now have W3+W5+W10 overlap",
        "--min-count 191",
    ],
    Path("AGENTS.md"): [
        "Religion Problem maximum absorption layer)\n\n## Core orientation",
    ],
    Path("skills/ismism-knowledge-operator/SKILL.md"): [
        "--min-count 191",
    ],
    Path("ISMISM-MAINLINE-HANDOFF.md"): [
        "After the Religion Problem maximum absorption batch, 64.6%",
        "143 rows remain W1/W2-only",
        "Full W3+W5+W10 row overlap now covers 85 rows",
        "W10 进一步吸收 pilot 已扩展到 122",
        "143/363 行仍为 W1/W2-only",
        "85 行达到 W3+W5+W10 全重叠",
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
    return {
        int(row["row_id"]): row
        for _, row in load_jsonl(repo / "knowledge/manifests/segments.jsonl")
    }


def parse_required_int(value: Any, where: str, errors: list[str]) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        add(errors, f"{where}: bad row_id {value!r}")
        return None


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
            key, value = raw.split(":", 1)
            key = key.strip()
            value = value.strip()
            meta[key] = [] if value == "" else value.strip('"\'`')
        elif key == "evidence_quotes" and raw.strip().startswith("- "):
            quote = raw.strip()[2:].strip('"\'`')
            meta.setdefault("evidence_quotes", []).append(quote)
    return meta


def load_w10_ids(repo: Path) -> tuple[dict[str, Path], dict[int, list[str]], dict[str, dict[str, Any]]]:
    ids: dict[str, Path] = {}
    rows: dict[int, list[str]] = {}
    metas: dict[str, dict[str, Any]] = {}
    for path in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        meta = parse_w10_frontmatter(path)
        card_id = str(meta.get("card_id", ""))
        if not card_id:
            continue
        ids[card_id] = path
        metas[card_id] = meta
        row = parse_required_int(meta.get("row_id"), f"{path}:frontmatter", [])
        if row is not None:
            rows.setdefault(row, []).append(card_id)
    return ids, rows, metas


def load_w3_batch(repo: Path) -> tuple[list[dict[str, Any]], dict[int, list[str]], list[str]]:
    batch: list[dict[str, Any]] = []
    rows: dict[int, list[str]] = {}
    errors: list[str] = []
    seen: set[str] = set()
    path = repo / "knowledge/lexicon/term-senses.jsonl"
    for lineno, rec in load_jsonl(path):
        sense_id = str(rec.get("sense_id", ""))
        if sense_id in seen:
            add(errors, f"knowledge/lexicon/term-senses.jsonl:{lineno}: duplicate sense_id {sense_id}")
        seen.add(sense_id)
        if rec.get("batch_id") != W3_BATCH:
            continue
        batch.append(rec)
        for src_index, src in enumerate(rec.get("source_segments", []) or [], 1):
            where = f"knowledge/lexicon/term-senses.jsonl:{lineno}: {sense_id} source_segments[{src_index}]"
            row = parse_required_int(src.get("row_id"), where, errors)
            if row is None:
                continue
            rows.setdefault(row, []).append(sense_id)
            if row not in EXPECTED_ROWS:
                add(errors, f"{where}: source row outside Time-Death manifest: {row}")
    return batch, rows, errors


def load_w5_batch(repo: Path) -> tuple[list[dict[str, Any]], dict[int, list[str]], list[str]]:
    batch: list[dict[str, Any]] = []
    rows: dict[int, list[str]] = {}
    errors: list[str] = []
    seen: set[str] = set()
    path = repo / "knowledge/relations/relation-assets.jsonl"
    for lineno, rec in load_jsonl(path):
        relation_id = str(rec.get("relation_id", ""))
        if relation_id in seen:
            add(errors, f"knowledge/relations/relation-assets.jsonl:{lineno}: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if rec.get("batch_id") != W5_BATCH:
            continue
        batch.append(rec)
        for ev_index, ev in enumerate(rec.get("evidence_segment", []) or [], 1):
            where = f"knowledge/relations/relation-assets.jsonl:{lineno}: {relation_id} evidence_segment[{ev_index}]"
            row = parse_required_int(ev.get("row_id"), where, errors)
            if row is None:
                continue
            rows.setdefault(row, []).append(relation_id)
            if row not in EXPECTED_ROWS:
                add(errors, f"{where}: evidence row outside Time-Death manifest: {row}")
    return batch, rows, errors


def validate_manifest_evidence(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[dict[int, dict[str, Any]], dict[str, dict[str, Any]], dict[int, int]]:
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
        segment = segments.get(row)
        if not segment:
            add(errors, f"{MANIFEST}:{lineno}: row {row} not in segments.jsonl")
            continue
        expected_path = segment["source_paths"]["clean_md_relpath"]
        expected_toc = "None" if segment.get("toc_id") is None else str(segment.get("toc_id"))
        if rec.get("segment_id") != segment.get("segment_id"):
            add(errors, f"{MANIFEST}:{lineno}: row {row} segment_id mismatch")
        if str(rec.get("toc_id")) != expected_toc:
            add(errors, f"{MANIFEST}:{lineno}: row {row} toc_id mismatch")
        if rec.get("clean_md_path") != expected_path:
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean_md_path mismatch")
        if not (repo / expected_path).exists():
            add(errors, f"{MANIFEST}:{lineno}: row {row} clean file missing")
        theme_class = rec.get("theme_class")
        if theme_class not in THEME_CLASSES:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad theme_class {theme_class!r}")
        elif row not in CLASS_ROWS[theme_class]:
            add(errors, f"{MANIFEST}:{lineno}: row {row} assigned to {theme_class}, expected exact class map")
        if rec.get("core_status") not in CORE_STATUS:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad core_status")
        if rec.get("recommended_action") not in RECOMMENDED_ACTION:
            add(errors, f"{MANIFEST}:{lineno}: row {row} bad recommended_action {rec.get('recommended_action')!r}")
        if not isinstance(rec.get("keyword_hits"), dict):
            add(errors, f"{MANIFEST}:{lineno}: row {row} keyword_hits must be object")
        try:
            if int(rec.get("evidence_quote_count", -1)) < 0:
                add(errors, f"{MANIFEST}:{lineno}: row {row} bad evidence_quote_count")
        except (TypeError, ValueError):
            add(errors, f"{MANIFEST}:{lineno}: row {row} evidence_quote_count not int-like")

    if set(manifest_by_row) != EXPECTED_ROWS:
        add(
            errors,
            "manifest rows mismatch: "
            f"missing={sorted(EXPECTED_ROWS - set(manifest_by_row))}, "
            f"extra={sorted(set(manifest_by_row) - EXPECTED_ROWS)}",
        )
    if not 75 <= len(manifest_by_row) <= 85:
        add(errors, f"manifest row count outside [75,85]: {len(manifest_by_row)}")
    for row in sorted(AI_ROWS | BUDDHIST_CORE | HARD_CORE):
        if row not in manifest_by_row:
            add(errors, f"required core row missing from manifest: {row}")

    evidence_by_id: dict[str, dict[str, Any]] = {}
    count_by_row: dict[int, int] = {}
    for lineno, rec in load_jsonl(evidence_path):
        evidence_id = str(rec.get("evidence_id", ""))
        if not re.fullmatch(r"ev:tdlife:\d{4}:\d{2}", evidence_id):
            add(errors, f"{EVIDENCE}:{lineno}: bad evidence_id {evidence_id!r}")
        if evidence_id in evidence_by_id:
            add(errors, f"{EVIDENCE}:{lineno}: duplicate evidence_id {evidence_id}")
        evidence_by_id[evidence_id] = rec
        row = parse_required_int(rec.get("row_id"), f"{EVIDENCE}:{lineno}", errors)
        if row is None:
            continue
        if row not in manifest_by_row:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} not in Time-Death manifest")
            continue
        segment = segments[row]
        expected_path = segment["source_paths"]["clean_md_relpath"]
        expected_toc = "None" if segment.get("toc_id") is None else str(segment.get("toc_id"))
        if rec.get("segment_id") != segment.get("segment_id") or str(rec.get("toc_id")) != expected_toc:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} segment/toc mismatch")
        if rec.get("clean_md_path") != expected_path:
            add(errors, f"{EVIDENCE}:{lineno}: row {row} clean path mismatch")
        quote = str(rec.get("quote", ""))
        if not quote.strip():
            add(errors, f"{EVIDENCE}:{lineno}: empty quote")
            continue
        if quote not in (repo / expected_path).read_text(encoding="utf-8"):
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


def validate_taxonomy(
    repo: Path,
    manifest_by_row: dict[int, dict[str, Any]],
    evidence_by_id: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    path = repo / TAXONOMY
    if not path.exists():
        add(errors, f"missing {TAXONOMY}")
        return
    text = path.read_text(encoding="utf-8")
    tax_rows: dict[int, str] = {}
    for theme_class in THEME_CLASSES:
        if theme_class not in text:
            add(errors, f"taxonomy does not mention theme_class {theme_class}")
    for evidence_id in re.findall(r"ev:tdlife:\d{4}:\d{2}", text):
        if evidence_id not in evidence_by_id:
            add(errors, f"taxonomy references unknown evidence id {evidence_id}")
    for section in re.split(r"\n(?=## T\d+\.)", text):
        if not section.startswith("## T"):
            continue
        heading = section.splitlines()[0].strip()
        class_match = re.search(r"- theme_class: `([^`]+)`", section)
        rows_match = re.search(r"- rows: ([^\n]+)", section)
        if not class_match:
            add(errors, f"taxonomy section lacks theme_class: {heading}")
            continue
        theme_class = class_match.group(1)
        if theme_class not in THEME_CLASSES:
            add(errors, f"taxonomy section {heading} has bad theme_class {theme_class!r}")
        if not rows_match:
            add(errors, f"taxonomy section lacks rows: {heading}")
            continue
        for row_str in re.findall(r"row (\d+)", rows_match.group(1)):
            row = int(row_str)
            if row in tax_rows:
                add(errors, f"taxonomy row {row} appears in multiple theme nodes: {tax_rows[row]} and {theme_class}")
                continue
            tax_rows[row] = theme_class
            manifest_class = manifest_by_row.get(row, {}).get("theme_class")
            if manifest_class and manifest_class != theme_class:
                add(errors, f"taxonomy row {row} class mismatch: taxonomy={theme_class}, manifest={manifest_class}")
    missing = sorted(set(manifest_by_row) - set(tax_rows))
    extra = sorted(set(tax_rows) - set(manifest_by_row))
    if missing:
        add(errors, f"taxonomy missing manifest rows: {missing}")
    if extra:
        add(errors, f"taxonomy references extra rows: {extra}")


def validate_w3_w5_batches(repo: Path, errors: list[str]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    w3, _, w3_errors = load_w3_batch(repo)
    w5, _, w5_errors = load_w5_batch(repo)
    errors.extend(w3_errors)
    errors.extend(w5_errors)

    if not 55 <= len(w3) <= 75:
        add(errors, f"Time-Death W3 batch count outside [55,75]: {len(w3)}")
    for rec in w3:
        if rec.get("status") != "draft":
            add(errors, f"Time-Death W3 non-draft status: {rec.get('sense_id')}")

    if not 45 <= len(w5) <= 65:
        add(errors, f"Time-Death W5 batch count outside [45,65]: {len(w5)}")
    for rec in w5:
        if rec.get("status") != "draft":
            add(errors, f"Time-Death W5 non-draft status: {rec.get('relation_id')}")
    return w3, w5


def validate_w10_coverage(
    repo: Path,
    manifest_by_row: dict[int, dict[str, Any]],
    errors: list[str],
) -> dict[str, Path]:
    w10_ids, w10_rows, w10_metas = load_w10_ids(repo)
    coverage_path = repo / W10_COVERAGE
    if not coverage_path.exists():
        add(errors, f"missing {W10_COVERAGE}")
        coverage: list[dict[str, Any]] = []
    else:
        coverage = [rec for _, rec in load_jsonl(coverage_path)]

    cov_by_row: dict[int, dict[str, Any]] = {}
    new_cards: list[str] = []
    for rec in coverage:
        row = parse_required_int(rec.get("row_id"), str(W10_COVERAGE), errors)
        if row is None:
            continue
        if row in cov_by_row:
            add(errors, f"{W10_COVERAGE}: duplicate coverage row {row}")
        cov_by_row[row] = rec
        status = rec.get("status")
        if status not in {"new_card", "existing_card_reused_with_time-death-rationale", "audited_context_rationale"}:
            add(errors, f"{W10_COVERAGE}: row {row} bad status {status!r}")
        if row not in W10_MATRIX_ROWS:
            add(errors, f"{W10_COVERAGE}: row {row} outside W10 matrix")
        manifest_class = manifest_by_row.get(row, {}).get("theme_class")
        if rec.get("group") != manifest_class:
            add(errors, f"{W10_COVERAGE}: row {row} group/theme_class mismatch: {rec.get('group')!r} != {manifest_class!r}")
        if status == "new_card":
            card_id = str(rec.get("card_id", ""))
            new_cards.append(card_id)
            if card_id not in w10_ids:
                add(errors, f"{W10_COVERAGE}: row {row} new card id missing from W10 cards: {card_id}")
            if row not in w10_rows:
                add(errors, f"{W10_COVERAGE}: row {row} new card row not found in W10 rows")
            if "time-death-" not in card_id and "tdlife-" not in card_id:
                add(errors, f"{W10_COVERAGE}: row {row} new card id lacks time-death marker: {card_id}")
            claim_core = str(w10_metas.get(card_id, {}).get("claim_core", ""))
            if manifest_class and f"`{manifest_class}`" not in claim_core:
                add(errors, f"{W10_COVERAGE}: row {row} W10 claim_core lacks manifest theme_class `{manifest_class}`")
        elif status == "existing_card_reused_with_time-death-rationale":
            card_id = str(rec.get("existing_card_id", ""))
            if card_id not in w10_ids:
                add(errors, f"{W10_COVERAGE}: row {row} existing card id missing: {card_id}")
            if not str(rec.get("rationale", "")).strip():
                add(errors, f"{W10_COVERAGE}: row {row} missing reuse rationale")
        elif len(str(rec.get("rationale", "")).strip()) < 40:
            add(errors, f"{W10_COVERAGE}: row {row} context rationale too short")

    missing = sorted(W10_MATRIX_ROWS - set(cov_by_row))
    extra = sorted(set(cov_by_row) - W10_MATRIX_ROWS)
    if missing:
        add(errors, f"W10 coverage missing matrix rows: {missing}")
    if extra:
        add(errors, f"W10 coverage has extra rows: {extra}")
    if not 35 <= len(new_cards) <= 50:
        add(errors, f"Time-Death W10 new card count outside [35,50]: {len(new_cards)}")
    for row in sorted(AI_ROWS | BUDDHIST_CORE | HARD_CORE):
        if row in manifest_by_row and row in W10_MATRIX_ROWS and row not in cov_by_row:
            add(errors, f"required row {row} lacks W10 coverage/rationale")
    return w10_ids


def validate_syntheses(
    repo: Path,
    manifest_by_row: dict[int, dict[str, Any]],
    w10_ids: dict[str, Path],
    errors: list[str],
) -> None:
    evidence_ids = {str(row.get("evidence_id")) for _, row in load_jsonl(repo / EVIDENCE)}
    sense_ids = {str(row.get("sense_id")) for _, row in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")}
    relation_ids = {str(row.get("relation_id")) for _, row in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")}

    for path in [README, QUERY_HELPER, *SYNTHESIS_FILES]:
        if not (repo / path).exists():
            add(errors, f"missing final artifact {path}")

    for path in SYNTHESIS_FILES:
        full_path = repo / path
        if not full_path.exists():
            continue
        text = full_path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if not stripped.startswith("- claim:"):
                continue
            found = False
            for evidence_id in re.findall(r"ev:tdlife:\d{4}:\d{2}", stripped):
                found = True
                if evidence_id not in evidence_ids:
                    add(errors, f"{path}:{lineno}: unknown evidence marker {evidence_id}")
            for sense_id in re.findall(r"term:[^\s,，。;；)）`]+:s\d{2}", stripped):
                found = True
                if sense_id not in sense_ids:
                    add(errors, f"{path}:{lineno}: unknown term marker {sense_id}")
            for relation_id in re.findall(r"rel:tdlife:\d{3}", stripped):
                found = True
                if relation_id not in relation_ids:
                    add(errors, f"{path}:{lineno}: unknown relation marker {relation_id}")
            for w10_id in re.findall(r"w10:(?:arg|proc|case):\d{4}:[A-Za-z0-9-]+", stripped):
                found = True
                if w10_id not in w10_ids:
                    add(errors, f"{path}:{lineno}: unknown W10 marker {w10_id}")
            for row_str in re.findall(r"row (\d+)", stripped):
                found = True
                row = int(row_str)
                if row not in manifest_by_row:
                    add(errors, f"{path}:{lineno}: row marker outside Time-Death manifest row {row}")
            if not found:
                add(errors, f"{path}:{lineno}: claim bullet lacks trace marker")


def compute_current_global_markers(repo: Path) -> dict[Path, list[str]]:
    """Derive current global navigation markers instead of freezing theme-era totals."""
    segments = load_segments(repo)
    all_rows = set(segments)

    term_records = [rec for _, rec in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")]
    relation_records = [rec for _, rec in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")]

    w3_rows: set[int] = set()
    for rec in term_records:
        source_segments = rec.get("source_segments") or []
        if not isinstance(source_segments, list):
            continue
        for src in source_segments:
            if isinstance(src, dict) and src.get("row_id") is not None:
                w3_rows.add(int(src["row_id"]))

    w5_rows: set[int] = set()
    for rec in relation_records:
        evidence_segments = rec.get("evidence_segment") or []
        if not isinstance(evidence_segments, list):
            continue
        for ev in evidence_segments:
            if isinstance(ev, dict) and ev.get("row_id") is not None:
                w5_rows.add(int(ev["row_id"]))

    w10_rows: set[int] = set()
    w10_types: set[str] = set()
    w10_count = 0
    for path in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        meta = parse_w10_frontmatter(path)
        if not meta.get("card_id"):
            continue
        w10_count += 1
        card_type = meta.get("type") or meta.get("card_type")
        if card_type:
            w10_types.add(str(card_type))
        if meta.get("row_id") is not None:
            w10_rows.add(int(meta["row_id"]))

    any_rows = w3_rows | w5_rows | w10_rows
    full_rows = w3_rows & w5_rows & w10_rows
    total_chars = sum(int(segments[row]["clean_md"]["char_count"]) for row in all_rows)
    any_chars = sum(int(segments[row]["clean_md"]["char_count"]) for row in any_rows)
    any_pct = round(any_chars / total_chars * 100, 1)

    terms = {str(rec.get("term", "")) for rec in term_records if rec.get("term")}
    rel_types = {str(rec.get("relation_type", "")) for rec in relation_records if rec.get("relation_type")}
    min_count_marker = f"--min-count {len(relation_records)}"

    common = [
        f"{len(term_records)} senses / {len(terms)} terms",
        f"{len(relation_records)} relations / {len(rel_types)} types",
        f"{w10_count} cards / {len(w10_types)} card types",
        f"{len(all_rows - any_rows)}/{len(all_rows)} rows remain W1/W2-only",
        f"{any_pct}%",
        f"{len(full_rows)} rows now have W3+W5+W10 overlap",
        min_count_marker,
    ]
    distribution = [
        f"W3 term-sense absorption covers {len(w3_rows)} rows",
        f"W5 relation absorption covers {len(w5_rows)} rows",
        f"W10 close-reading absorption covers {len(w10_rows)} rows",
        f"{len(all_rows - any_rows)}/{len(all_rows)} rows remain W1/W2-only",
        f"{any_pct}%",
        f"{len(full_rows)} rows",
    ]
    return {
        Path("README.md"): common,
        Path("knowledge/STATE.md"): common,
        Path("ISMISM-MAINLINE-HANDOFF.md"): common[:3],
        Path("DIRECTORY_MAP.md"): [min_count_marker],
        Path("skills/ismism-knowledge-operator/SKILL.md"): [min_count_marker],
        Path("knowledge/qa/absorption-strength-distribution.md"): distribution,
    }


def validate_state_navigation(repo: Path, errors: list[str]) -> None:
    markers_by_path = {rel_path: list(markers) for rel_path, markers in FINAL_DOC_MARKERS.items()}
    for rel_path, markers in compute_current_global_markers(repo).items():
        markers_by_path.setdefault(rel_path, []).extend(markers)
    for rel_path, markers in markers_by_path.items():
        path = repo / rel_path
        if not path.exists():
            add(errors, f"missing state/navigation file {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                add(errors, f"{rel_path}: missing current Time-Death state marker {marker!r}")
        for stale_marker in FINAL_DOC_FORBIDDEN.get(rel_path, []):
            if stale_marker in text:
                add(errors, f"{rel_path}: stale current-state marker still present {stale_marker!r}")


def validate_final(repo: Path, manifest_by_row: dict[int, dict[str, Any]], errors: list[str]) -> None:
    validate_w3_w5_batches(repo, errors)
    w10_ids = validate_w10_coverage(repo, manifest_by_row, errors)
    validate_syntheses(repo, manifest_by_row, w10_ids, errors)
    validate_state_navigation(repo, errors)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Time-Death-Finitude-Life theme absorption artifacts")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    try:
        segments = load_segments(repo)
    except Exception as exc:  # noqa: BLE001 - report loader failure as validator exit code 2.
        print(f"validate_time_death_theme: failed to load segments: {exc}", file=sys.stderr)
        return 2

    manifest_by_row, evidence_by_id, _ = validate_manifest_evidence(repo, segments, errors)
    if manifest_by_row:
        validate_taxonomy(repo, manifest_by_row, evidence_by_id, errors)
    if args.final and manifest_by_row:
        validate_final(repo, manifest_by_row, errors)
    w3_count = 0
    w5_count = 0
    if (repo / "knowledge/lexicon/term-senses.jsonl").exists():
        w3_count = len(load_w3_batch(repo)[0])
    if (repo / "knowledge/relations/relation-assets.jsonl").exists():
        w5_count = len(load_w5_batch(repo)[0])
    summary = {
        "status": "FAIL" if errors else "PASS",
        "manifest_rows": len(manifest_by_row),
        "evidence_records": len(evidence_by_id),
        "w3_time_death_records": w3_count,
        "w5_time_death_records": w5_count,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"validate_time_death_theme: {summary['status']}")
        print(json.dumps({k: v for k, v in summary.items() if k not in {"errors", "warnings"}}, ensure_ascii=False))
        for error in errors[:160]:
            print("- " + error)
        for warning in warnings[:30]:
            print("WARN " + warning)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
