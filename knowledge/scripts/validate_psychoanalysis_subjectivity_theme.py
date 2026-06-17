#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path("knowledge/themes/psychoanalysis-subjectivity")
W3_BATCH = "W3-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16"
W5_BATCH = "W5-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16"
CLASSES = {
    "psychoanalysis-unconscious-desire",
    "big-other-fantasy-enjoyment",
    "subjectivity-subjectivation-intersubjectivity",
    "symbolic-order-signifier-language",
    "discourse-truth-and-language-game",
    "ideology-cynicism-normality-diagnosis",
    "symptom-repression-perversion-abjection",
    "phenomenology-body-otherness-bridge",
    "capitalism-fetishism-psychoanalysis-bridge",
    "religion-love-big-other-bridge",
    "feminism-sexuality-desire-bridge",
    "chinese-chan-analyst-discourse-bridge",
    "practice-analysis-transformation",
    "cross-theme-context",
    "excluded-keyword-only",
}
ROLES = {"core", "bridge", "context", "excluded"}
RING_A = {89, 117, 185, 186, 258, 262, 273, 274, 275}
SYNTHESIS_FILES = [
    "knowledge/themes/psychoanalysis-subjectivity/subjectivity-symbolic-order-and-big-other-synthesis.md",
    "knowledge/themes/psychoanalysis-subjectivity/psychoanalysis-unconscious-desire-and-symptom-synthesis.md",
    "knowledge/themes/psychoanalysis-subjectivity/discourse-language-game-and-truth-synthesis.md",
    "knowledge/themes/psychoanalysis-subjectivity/ideology-fantasy-and-practice-diagnosis-synthesis.md",
    "knowledge/themes/psychoanalysis-subjectivity/cross-theme-psychoanalytic-bridges-synthesis.md",
]
FINAL_DOCS = {
    Path("README.md"): ["Psychoanalysis / Subjectivity", "validate_psychoanalysis_subjectivity_theme.py"],
    Path("AGENTS.md"): ["knowledge/themes/psychoanalysis-subjectivity/README.md", "Psychoanalysis / Subjectivity"],
    Path("knowledge/STATE.md"): ["Psychoanalysis / Subjectivity", "validate_psychoanalysis_subjectivity_theme.py"],
    Path("ISMISM-MAINLINE-HANDOFF.md"): ["Psychoanalysis / Subjectivity", "W5 validator uses `--min-count 1044`"],
    Path("DIRECTORY_MAP.md"): ["psychoanalysis-subjectivity", "validate_psychoanalysis_subjectivity_theme.py"],
    Path("knowledge/README.md"): ["psychoanalysis-subjectivity", "Psychoanalysis / Subjectivity"],
    Path("knowledge/w10-absorption/index.md"): ["psycho-subj", "w10:"],
    Path("knowledge/w10-absorption/PLAN.md"): ["Psychoanalysis-Subjectivity", "58"],
}
CURRENT_DOCS = [
    Path("README.md"),
    Path("knowledge/README.md"),
    Path("knowledge/STATE.md"),
    Path("ISMISM-MAINLINE-HANDOFF.md"),
    Path("DIRECTORY_MAP.md"),
    Path("AGENTS.md"),
    Path("skills/ismism-knowledge-operator/SKILL.md"),
    Path("knowledge/query-playbook.md"),
    Path("knowledge/qa/absorption-strength-distribution.md"),
]
STALE_CURRENT_MARKERS = [
    "Current latest checkpoint — Universal Absorption Phase B",
    "current_phase: Feminism / Gender / Sexuality",
    "Current validator markers — Feminism maximum absorption",
    "Global current counts: 1084",
    "Current validator markers: 1084",
    "Current W5 validation marker: `--min-count 525`",
    "W5 current global validator command: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 525 --require-type-min 2`",
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    return {int(row["row_id"]): row for row in load_jsonl(repo / "knowledge/manifests/segments.jsonl")}


def add(errors: list[str], message: str) -> None:
    errors.append(message)


def clean_text(repo: Path, segments: dict[int, dict[str, Any]], row_id: int) -> str:
    segment = segments[row_id]
    return (repo / segment["source_paths"]["clean_md_relpath"]).read_text(encoding="utf-8")


def validate_manifest(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[list[dict[str, Any]], dict[int, dict[str, Any]]]:
    path = repo / ROOT / "psychoanalysis-subjectivity-row-manifest.jsonl"
    if not path.exists():
        add(errors, "missing manifest")
        return [], {}
    manifest = load_jsonl(path)
    rows: dict[int, dict[str, Any]] = {}
    required = {
        "row_id",
        "segment_id",
        "toc_id",
        "title",
        "field",
        "clean_md_path",
        "char_count",
        "keyword_hits",
        "theme_class",
        "theme_role",
        "current_layers",
        "recommended_action",
        "inclusion_rationale",
        "exclusion_or_context_rationale",
    }
    for line_number, record in enumerate(manifest, 1):
        missing = sorted(required - set(record))
        if missing:
            add(errors, f"manifest line {line_number} missing {missing}")
        row_id = int(record.get("row_id", -1))
        rows[row_id] = record
        segment = segments.get(row_id)
        if segment is None:
            add(errors, f"manifest row {row_id} not in segments")
            continue
        if record.get("segment_id") != segment.get("segment_id"):
            add(errors, f"row {row_id} segment_id mismatch")
        if record.get("clean_md_path") != segment["source_paths"]["clean_md_relpath"]:
            add(errors, f"row {row_id} clean path mismatch")
        if record.get("theme_class") not in CLASSES:
            add(errors, f"row {row_id} bad class {record.get('theme_class')}")
        if record.get("theme_role") not in ROLES:
            add(errors, f"row {row_id} bad role {record.get('theme_role')}")
        if record.get("theme_class") == "excluded-keyword-only" and record.get("theme_role") != "excluded":
            add(errors, f"row {row_id} excluded-keyword-only must remain excluded")
        if record.get("theme_role") == "core" and record.get("recommended_action") == "no-action":
            add(errors, f"row {row_id} core cannot have no-action recommendation")
        if record.get("theme_role") == "excluded" and not record.get("exclusion_or_context_rationale"):
            add(errors, f"row {row_id} excluded lacks rationale")
        if record.get("theme_role") == "core" and not record.get("inclusion_rationale"):
            add(errors, f"row {row_id} core lacks inclusion rationale")
    if len(manifest) < 90:
        add(errors, f"too few manifest rows: {len(manifest)}")
    core_count = sum(1 for record in manifest if record.get("theme_role") == "core")
    if core_count < 35:
        add(errors, f"too few core rows: {core_count}")
    missing_ring_a = sorted(RING_A - set(rows))
    if missing_ring_a:
        add(errors, f"Ring A rows missing: {missing_ring_a}")
    return manifest, rows


def validate_evidence(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    manifest_rows: dict[int, dict[str, Any]],
    errors: list[str],
) -> set[str]:
    path = repo / ROOT / "psychoanalysis-subjectivity-evidence-bank.jsonl"
    if not path.exists():
        add(errors, "missing evidence bank")
        return set()
    evidence = load_jsonl(path)
    evidence_ids: set[str] = set()
    by_row: dict[int, list[dict[str, Any]]] = {}
    for record in evidence:
        evidence_id = str(record.get("evidence_id", ""))
        row_id = int(record.get("row_id", -1))
        by_row.setdefault(row_id, []).append(record)
        if not re.fullmatch(r"ev:psycho-subj:\d{4}:\d{2}", evidence_id):
            add(errors, f"bad evidence id {evidence_id}")
        if evidence_id in evidence_ids:
            add(errors, f"duplicate evidence id {evidence_id}")
        evidence_ids.add(evidence_id)
        if row_id not in manifest_rows:
            add(errors, f"evidence {evidence_id} row not in manifest")
        segment = segments.get(row_id)
        if segment is None:
            continue
        if record.get("segment_id") != segment.get("segment_id"):
            add(errors, f"{evidence_id} segment_id mismatch")
        clean_relpath = segment["source_paths"]["clean_md_relpath"]
        if record.get("clean_md_path") != clean_relpath:
            add(errors, f"{evidence_id} clean path mismatch")
        quote = str(record.get("quote", "")).strip()
        if not quote or quote not in clean_text(repo, segments, row_id):
            add(errors, f"{evidence_id} quote_not_found")
    if len(evidence) < 280:
        add(errors, f"too few evidence records: {len(evidence)}")
    for row_id, record in manifest_rows.items():
        count = len(by_row.get(row_id, []))
        if record.get("theme_role") == "core" and count < 3:
            add(errors, f"core row {row_id} has too few evidence quotes")
        if record.get("theme_role") == "excluded" and count < 1:
            add(errors, f"excluded row {row_id} has no evidence quote")
    return evidence_ids


def validate_w3_w5(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[set[str], set[str]]:
    term_records = load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")
    relation_records = load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")
    term_ids = {str(record.get("sense_id")) for record in term_records}
    relation_ids = {str(record.get("relation_id")) for record in relation_records}
    w3_batch = [record for record in term_records if record.get("batch_id") == W3_BATCH]
    w5_batch = [record for record in relation_records if record.get("batch_id") == W5_BATCH]
    if len(w3_batch) < 75:
        add(errors, f"W3 batch too small: {len(w3_batch)}")
    if len(w5_batch) < 60:
        add(errors, f"W5 batch too small: {len(w5_batch)}")
    for record in w3_batch:
        if record.get("status") != "draft":
            add(errors, f"W3 non-draft {record.get('sense_id')}")
        for quote_record in record.get("evidence_quotes") or []:
            row_id = int(quote_record.get("row_id"))
            quote = str(quote_record.get("quote", "")).strip()
            if row_id not in segments or quote not in clean_text(repo, segments, row_id):
                add(errors, f"W3 bad quote {record.get('sense_id')} row {row_id}")
    for record in w5_batch:
        if record.get("status") != "draft":
            add(errors, f"W5 non-draft {record.get('relation_id')}")
        for quote_record in record.get("evidence_segment") or []:
            row_id = int(quote_record.get("row_id"))
            quote = str(quote_record.get("quote", "")).strip()
            if row_id not in segments or quote not in clean_text(repo, segments, row_id):
                add(errors, f"W5 bad quote {record.get('relation_id')} row {row_id}")
    return term_ids, relation_ids


def validate_w10(repo: Path, errors: list[str]) -> set[str]:
    card_ids: set[str] = set()
    psycho_cards = 0
    for path in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^card_id:\s*(\S+)", text, re.MULTILINE)
        if match:
            card_ids.add(match.group(1))
        if "psycho-subj" in path.name:
            psycho_cards += 1
            if "status: pilot-draft" not in text:
                add(errors, f"W10 non-pilot {path.relative_to(repo)}")
    if psycho_cards < 45:
        add(errors, f"W10 batch too small: {psycho_cards}")
    return card_ids


def validate_syntheses(
    repo: Path,
    evidence_ids: set[str],
    term_ids: set[str],
    relation_ids: set[str],
    card_ids: set[str],
    errors: list[str],
) -> None:
    for relpath in SYNTHESIS_FILES:
        path = repo / relpath
        if not path.exists():
            add(errors, f"missing synthesis {relpath}")
            continue
        text = path.read_text(encoding="utf-8")
        for evidence_id in re.findall(r"ev:psycho-subj:\d{4}:\d{2}", text):
            if evidence_id not in evidence_ids:
                add(errors, f"unknown evidence {evidence_id} in {relpath}")
        for term_id in re.findall(r"term:[^`\s,，。；;]+:s\d{2}", text):
            if term_id not in term_ids:
                add(errors, f"unknown term {term_id} in {relpath}")
        for relation_id in re.findall(r"rel:psycho-subj:\d{3}", text):
            if relation_id not in relation_ids:
                add(errors, f"unknown relation {relation_id} in {relpath}")
        for card_id in re.findall(r"w10:(?:arg|proc|case):\d{4}:psycho-subj[-a-z]+", text):
            if card_id not in card_ids:
                add(errors, f"unknown W10 {card_id} in {relpath}")


def validate_final_docs(repo: Path, errors: list[str]) -> None:
    for relpath, markers in FINAL_DOCS.items():
        path = repo / relpath
        if not path.exists():
            add(errors, f"missing final doc {relpath}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                add(errors, f"final doc {relpath} missing {marker!r}")


def load_metrics(repo: Path, errors: list[str]) -> dict[str, Any]:
    path = repo / ROOT / "metrics.json"
    if not path.exists():
        add(errors, "missing psychoanalysis-subjectivity metrics.json")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        add(errors, f"metrics.json invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        add(errors, "metrics.json is not an object")
        return {}
    return data


def validate_current_doc_consistency(repo: Path, errors: list[str]) -> None:
    metrics = load_metrics(repo, errors)
    if not metrics:
        return
    global_counts = (
        f"Global current counts: {metrics['global_w3_senses']} W3 draft senses / "
        f"{metrics['global_w3_terms']} terms; {metrics['global_w5_relations']} W5 draft relations; "
        f"{metrics['global_w10_cards']} W10 pilot-draft cards."
    )
    validator_markers = (
        f"Current validator markers: {metrics['global_w3_senses']} senses / "
        f"{metrics['global_w3_terms']} terms; {metrics['global_w5_relations']} relations / 12 types; "
        f"{metrics['global_w10_cards']} cards / 3 card types; {metrics['full_overlap_rows']} rows now "
        f"have W3+W5+W10 overlap; W5 validator uses `--min-count {metrics['w5_min_count']}`."
    )
    latest_checkpoint = (
        "Current latest checkpoint — Health / Body / Medicine / Risk Society "
        "maximum absorption"
    )
    semantic_requirements: dict[Path, list[str]] = {
        Path("README.md"): [
            latest_checkpoint,
            f"Current global counts are {metrics['global_w3_senses']} W3 senses / {metrics['global_w3_terms']} terms",
            f"{metrics['w1w2_only_rows']}/363 rows remain W1/W2-only",
            f"{metrics['full_overlap_rows']} rows now have W3+W5+W10 overlap",
        ],
        Path("knowledge/README.md"): [
            latest_checkpoint,
            f"Current global counts are {metrics['global_w3_senses']} W3 senses / {metrics['global_w3_terms']} terms",
            "themes/psychoanalysis-subjectivity/README.md",
        ],
        Path("knowledge/STATE.md"): [
            "current_phase: Health / Body / Medicine / Risk Society maximum absorption",
            validator_markers,
            f"{metrics['w1w2_only_rows']}/363 rows remain W1/W2-only",
        ],
        Path("ISMISM-MAINLINE-HANDOFF.md"): [
            latest_checkpoint,
            "Psychoanalysis / Subjectivity / Desire / Discourse / Language maximum absorption",
            validator_markers,
        ],
        Path("DIRECTORY_MAP.md"): [global_counts, validator_markers],
        Path("AGENTS.md"): [global_counts, validator_markers],
        Path("skills/ismism-knowledge-operator/SKILL.md"): [global_counts, validator_markers],
        Path("knowledge/query-playbook.md"): [global_counts, validator_markers],
        Path("knowledge/qa/absorption-strength-distribution.md"): [
            f"W3 term-sense absorption covers {metrics['global_w3_rows']} rows",
            f"W5 relation absorption covers {metrics['global_w5_rows']} rows",
            f"W10 close-reading absorption covers {metrics['global_w10_rows']} rows",
            f"{metrics['w1w2_only_rows']}/363 rows remain W1/W2-only",
            f"Full W3+W5+W10 row overlap is now {metrics['full_overlap_rows']} rows",
        ],
    }
    for relpath in CURRENT_DOCS:
        path = repo / relpath
        if not path.exists():
            add(errors, f"missing current doc {relpath}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in semantic_requirements.get(relpath, []):
            if marker not in text:
                add(errors, f"current doc {relpath} missing semantic marker {marker!r}")
        for stale in STALE_CURRENT_MARKERS:
            if stale in text:
                add(errors, f"current doc {relpath} contains stale current marker {stale!r}")


def validate_protected_corpus(repo: Path, errors: list[str]) -> None:
    diff = subprocess.run(
        ["git", "diff", "--name-only", "--", "split_md", "split_md_clean"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if diff.stdout.strip():
        add(errors, "protected corpus diff present: " + diff.stdout.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Psychoanalysis-Subjectivity theme layer")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    segments = load_segments(repo)
    manifest, manifest_rows = validate_manifest(repo, segments, errors)
    evidence_ids = validate_evidence(repo, segments, manifest_rows, errors)
    term_ids, relation_ids = validate_w3_w5(repo, segments, errors)
    card_ids = validate_w10(repo, errors)
    validate_syntheses(repo, evidence_ids, term_ids, relation_ids, card_ids, errors)
    if args.final:
        validate_final_docs(repo, errors)
        validate_current_doc_consistency(repo, errors)
        validate_protected_corpus(repo, errors)

    w3_batch = [
        record
        for record in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")
        if record.get("batch_id") == W3_BATCH
    ]
    w5_batch = [
        record
        for record in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")
        if record.get("batch_id") == W5_BATCH
    ]
    w10_count = len(list((repo / "knowledge/w10-absorption").glob("*-cards/*psycho-subj*.md")))
    output = {
        "manifest_rows": len(manifest),
        "evidence_records": len(evidence_ids),
        "w3_batch": len(w3_batch),
        "w5_batch": len(w5_batch),
        "w10_cards": w10_count,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(
            "psychoanalysis-subjectivity validation: "
            f"manifest={output['manifest_rows']}, evidence={output['evidence_records']}, "
            f"W3={output['w3_batch']}, W5={output['w5_batch']}, "
            f"W10={output['w10_cards']}, errors={len(errors)}, warnings={len(warnings)}"
        )
        for error in errors[:80]:
            print("ERROR", error)
        for warning in warnings[:30]:
            print("WARN", warning)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
