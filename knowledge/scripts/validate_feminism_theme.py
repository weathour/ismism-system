#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path("knowledge/themes/feminism")
W3_BATCH = "W3-FEMINISM-2026-06-16"
W5_BATCH = "W5-FEMINISM-2026-06-16"
CLASSES = {
    "false-feminism-and-female-essence",
    "misogyny-and-patriarchal-fantasy",
    "sexual-liberation-and-erotic-economy",
    "love-romance-marriage-intimacy",
    "sexualized-body-gaze-touch-otherness",
    "sex-difference-discourse-queer-symbolic-boundary",
    "family-birth-reproduction-social-reproduction",
    "women-children-economic-liberation-practice",
    "psychoanalysis-language-and-subjectivation",
    "cross-theme-context",
    "excluded-keyword-only",
}
ROLES = {"core", "bridge", "context", "excluded"}
RING_A = {90, 61, 330, 265, 85, 93, 89}
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
SYNTHESIS_FILES = [
    ROOT / "feminism-gender-and-patriarchal-fantasy-synthesis.md",
    ROOT / "sexuality-body-and-erotic-economy-synthesis.md",
    ROOT / "love-family-and-social-reproduction-synthesis.md",
    ROOT / "feminism-practice-and-liberation-synthesis.md",
]
FINAL_DOCS = {
    Path("README.md"): ["Feminism / Gender / Sexuality", "validate_feminism_theme.py"],
    Path("AGENTS.md"): ["knowledge/themes/feminism/README.md", "Feminism / Gender / Sexuality"],
    Path("knowledge/STATE.md"): ["Feminism / Gender / Sexuality", "validate_feminism_theme.py"],
    Path("ISMISM-MAINLINE-HANDOFF.md"): ["Feminism / Gender / Sexuality", "feminism-row-manifest.jsonl"],
    Path("DIRECTORY_MAP.md"): ["knowledge/themes/feminism/", "validate_feminism_theme.py"],
    Path("knowledge/README.md"): ["feminism", "Feminism / Gender / Sexuality"],
    Path("knowledge/query-playbook.md"): ["query_feminism_theme.py", "女权 / 性别 / 身体 / 社会再生产"],
    Path("skills/ismism-knowledge-operator/SKILL.md"): [
        "knowledge/themes/feminism/README.md",
        "query_feminism_theme.py",
    ],
}
ALLOWED_W3_APPEND_BATCHES = {
    W3_BATCH,
    "W3-TIME-DEATH-LIFE-2026-06-15",
    "W3-CAPITALISM-2026-06-16",
    "W3-UNIVERSAL-A-2026-06-16",
    "W3-UNIVERSAL-B-2026-06-16",
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
}
ALLOWED_W5_APPEND_BATCHES = {
    W5_BATCH,
    "W5-TIME-DEATH-LIFE-2026-06-15",
    "W5-CAPITALISM-2026-06-16",
    "W5-UNIVERSAL-A-2026-06-16",
    "W5-UNIVERSAL-B-2026-06-16",
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
}
STRIP_CHARS = chr(39) + chr(34) + "`"


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)


def load_jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    records: list[tuple[int, dict[str, Any]]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            records.append((line_number, json.loads(line)))
    return records


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    return {
        int(record["row_id"]): record
        for _line, record in load_jsonl(repo / "knowledge/manifests/segments.jsonl")
    }


def toc(value: Any) -> str:
    return "None" if value is None else str(value)


def check_quote(repo: Path, clean_relpath: str, quote: str, where: str, errors: list[str]) -> None:
    path = repo / clean_relpath
    if not path.exists():
        add_error(errors, f"{where}: missing clean {clean_relpath}")
        return
    if not quote.strip():
        add_error(errors, f"{where}: empty quote")
        return
    if quote not in path.read_text(encoding="utf-8"):
        add_error(errors, f"{where}: quote not exact substring: {quote[:100]}")


def parse_frontmatter(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, Any] = {}
    current_key: str | None = None
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        if not raw.strip():
            continue
        if not raw.startswith(" ") and ":" in raw:
            key, value = raw.split(":", 1)
            current_key = key.strip()
            if value.strip():
                meta[current_key] = value.strip().strip(STRIP_CHARS)
            else:
                meta[current_key] = []
            continue
        if current_key == "evidence_quotes" and raw.strip().startswith("- "):
            meta.setdefault(current_key, []).append(raw.strip()[2:].strip(STRIP_CHARS))
    return meta


def validate_manifest_evidence(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> tuple[dict[int, dict[str, Any]], dict[str, dict[str, Any]], dict[int, int]]:
    manifest: dict[int, dict[str, Any]] = {}
    evidence: dict[str, dict[str, Any]] = {}
    evidence_counts: dict[int, int] = {}
    required = [
        ROOT / "README.md",
        ROOT / "feminism-row-manifest.jsonl",
        ROOT / "feminism-evidence-bank.jsonl",
        ROOT / "feminism-taxonomy.md",
        Path("knowledge/scripts/query_feminism_theme.py"),
    ]
    for relpath in required:
        if not (repo / relpath).exists():
            add_error(errors, f"missing {relpath}")
    manifest_path = repo / ROOT / "feminism-row-manifest.jsonl"
    if not manifest_path.exists():
        return manifest, evidence, evidence_counts

    for line_number, record in load_jsonl(manifest_path):
        row = int(record.get("row_id", -1))
        manifest[row] = record
        segment = segments.get(row)
        if not segment:
            add_error(errors, f"manifest:{line_number}: bad row {row}")
            continue
        if record.get("segment_id") != segment.get("segment_id"):
            add_error(errors, f"manifest:{line_number}: segment mismatch {row}")
        if str(record.get("toc_id")) != toc(segment.get("toc_id")):
            add_error(errors, f"manifest:{line_number}: toc mismatch {row}")
        expected_clean = segment["source_paths"]["clean_md_relpath"]
        if record.get("clean_md_path") != expected_clean:
            add_error(errors, f"manifest:{line_number}: clean path mismatch {row}")
        if record.get("theme_class") not in CLASSES:
            add_error(errors, f"manifest:{line_number}: bad class")
        if record.get("theme_role") not in ROLES:
            add_error(errors, f"manifest:{line_number}: bad role")
        if record.get("theme_class") == "excluded-keyword-only" and record.get("theme_role") != "excluded":
            add_error(errors, f"manifest:{line_number}: excluded row {row} must stay excluded")
        if record.get("theme_role") in {"context", "excluded"} and not record.get(
            "exclusion_or_context_rationale"
        ):
            add_error(errors, f"manifest:{line_number}: missing context/exclusion rationale {row}")

    evidence_path = repo / ROOT / "feminism-evidence-bank.jsonl"
    for line_number, record in load_jsonl(evidence_path):
        evidence_id = str(record.get("evidence_id", ""))
        evidence[evidence_id] = record
        row = int(record.get("row_id", -1))
        if row not in manifest:
            add_error(errors, f"evidence:{line_number}: row not in manifest {row}")
            continue
        for field in ["segment_id", "toc_id", "clean_md_path", "theme_class"]:
            if record.get(field) != manifest[row].get(field):
                add_error(errors, f"evidence:{line_number}: {field} mismatch {evidence_id}")
        check_quote(
            repo,
            str(record.get("clean_md_path", "")),
            str(record.get("quote", "")),
            f"evidence:{line_number}:{evidence_id}",
            errors,
        )
        evidence_counts[row] = evidence_counts.get(row, 0) + 1

    if len(manifest) < 75:
        add_error(errors, f"manifest rows {len(manifest)} <75")
    core_rows = {row for row, record in manifest.items() if record.get("theme_role") == "core"}
    if len(core_rows) < 25:
        add_error(errors, f"core rows {len(core_rows)} <25")
    if len(evidence) < 240:
        add_error(errors, f"evidence records {len(evidence)} <240")
    missing_ring_a = RING_A - set(manifest)
    if missing_ring_a:
        add_error(errors, f"missing Ring A rows {sorted(missing_ring_a)}")
    for row in core_rows:
        if evidence_counts.get(row, 0) < 3:
            add_error(errors, f"core row {row} has <3 evidence")
    return manifest, evidence, evidence_counts


def validate_w3_batch(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> set[str]:
    records = [
        record
        for _line, record in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")
        if record.get("batch_id") == W3_BATCH
    ]
    sense_ids: set[str] = set()
    if not 60 <= len(records) <= 90:
        add_error(errors, f"W3 batch count {len(records)} outside [60,90]")
    for record in records:
        sense_id = str(record.get("sense_id", ""))
        sense_ids.add(sense_id)
        if record.get("status") != "draft":
            add_error(errors, f"W3 {sense_id}: non-draft")
        quotes = record.get("evidence_quotes", [])
        if not isinstance(quotes, list) or len(quotes) < 2:
            add_error(errors, f"W3 {sense_id}: <2 quotes")
            continue
        for ev in quotes:
            row = int(ev.get("row_id", -1))
            segment = segments.get(row)
            if not segment:
                add_error(errors, f"W3 {sense_id}: bad row {row}")
                continue
            check_quote(
                repo,
                segment["source_paths"]["clean_md_relpath"],
                str(ev.get("quote", "")),
                f"W3 {sense_id}",
                errors,
            )
    return sense_ids


def validate_w5_batch(
    repo: Path,
    sense_ids: set[str],
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> set[str]:
    records = [
        record
        for _line, record in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")
        if record.get("batch_id") == W5_BATCH
    ]
    relation_ids: set[str] = set()
    if len(records) < 50:
        add_error(errors, f"W5 batch count {len(records)} <50")
    for record in records:
        relation_id = str(record.get("relation_id", ""))
        relation_ids.add(relation_id)
        if record.get("status") != "draft":
            add_error(errors, f"W5 {relation_id}: non-draft")
        if record.get("relation_type") not in REL_TYPES:
            add_error(errors, f"W5 {relation_id}: bad type")
        refs = [record.get("source"), record.get("target"), *(record.get("source_senses") or [])]
        for ref in refs:
            if isinstance(ref, str) and ref.startswith("term:") and ref not in sense_ids:
                add_error(errors, f"W5 {relation_id}: missing sense {ref}")
        for ev in record.get("evidence_segment", []):
            row = int(ev.get("row_id", -1))
            segment = segments.get(row)
            if not segment:
                add_error(errors, f"W5 {relation_id}: bad row {row}")
                continue
            check_quote(
                repo,
                segment["source_paths"]["clean_md_relpath"],
                str(ev.get("quote", "")),
                f"W5 {relation_id}",
                errors,
            )
    return relation_ids


def validate_w10_cards(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> set[str]:
    card_ids: set[str] = set()
    for path in (repo / "knowledge/w10-absorption").glob("*-cards/*.md"):
        meta = parse_frontmatter(path)
        card_id = str(meta.get("card_id", ""))
        if ":feminism-" not in card_id:
            continue
        card_ids.add(card_id)
        if meta.get("status") != "pilot-draft":
            add_error(errors, f"{path}: non pilot-draft")
        row = int(str(meta.get("row_id", -1)))
        segment = segments.get(row)
        if not segment:
            add_error(errors, f"{path}: bad row {row}")
            continue
        quotes = meta.get("evidence_quotes", [])
        if not isinstance(quotes, list) or len(quotes) < 2:
            add_error(errors, f"{path}: <2 quotes")
            continue
        for quote in quotes:
            check_quote(
                repo,
                segment["source_paths"]["clean_md_relpath"],
                str(quote),
                str(path),
                errors,
            )
    if not 35 <= len(card_ids) <= 55:
        add_error(errors, f"W10 feminism card count {len(card_ids)} outside [35,55]")
    return card_ids


def validate_syntheses(
    repo: Path,
    evidence_ids: set[str],
    sense_ids: set[str],
    relation_ids: set[str],
    card_ids: set[str],
    errors: list[str],
) -> None:
    pattern = re.compile(
        r"ev:feminism:\d{4}:\d{2}|"
        r"term:[^\s`\],。；，、)]+:s\d{2}|"
        r"rel:feminism:\d{3}|"
        r"w10:(?:arg|proc|case):\d{4}:feminism-[a-z0-9-]+"
    )
    known = evidence_ids | sense_ids | relation_ids | card_ids
    for relpath in SYNTHESIS_FILES:
        path = repo / relpath
        if not path.exists():
            add_error(errors, f"missing synthesis {relpath}")
            continue
        markers = pattern.findall(path.read_text(encoding="utf-8"))
        if len(markers) < 8:
            add_error(errors, f"{relpath}: too few markers {len(markers)}")
        for marker in markers:
            if marker not in known:
                add_error(errors, f"{relpath}: unknown marker {marker}")


def validate_docs(repo: Path, errors: list[str]) -> None:
    for relpath, markers in FINAL_DOCS.items():
        path = repo / relpath
        if not path.exists():
            add_error(errors, f"missing final doc {relpath}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                add_error(errors, f"{relpath}: missing marker {marker!r}")


def validate_protected_corpus(
    repo: Path,
    segments: dict[int, dict[str, Any]],
    errors: list[str],
) -> None:
    for row, segment in segments.items():
        for key in ["raw_md", "clean_md"]:
            path = repo / segment[key]["relpath"]
            if not path.exists():
                add_error(errors, f"protected corpus row {row}: missing {path}")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != segment[key]["sha256"]:
                add_error(errors, f"protected corpus row {row}: sha mismatch for {path}")


def validate_append_only(repo: Path, relpath: str, allowed_batches: set[str], errors: list[str]) -> None:
    try:
        base = subprocess.check_output(["git", "show", f"HEAD:{relpath}"], cwd=repo, text=True)
    except subprocess.CalledProcessError:
        return
    current = load_jsonl(repo / relpath)
    base_records = [json.loads(line) for line in base.splitlines() if line.strip()]
    if len(current) < len(base_records):
        add_error(errors, f"{relpath}: fewer records than HEAD")
        return
    for index, base_record in enumerate(base_records):
        if current[index][1] != base_record:
            add_error(errors, f"{relpath}: existing HEAD record {index + 1} changed")
            return
    for line_number, record in current[len(base_records) :]:
        if str(record.get("batch_id", "")) not in allowed_batches:
            add_error(errors, f"{relpath}:{line_number}: appended batch not allowed {record.get('batch_id')}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    segments = load_segments(repo)
    manifest, evidence, _counts = validate_manifest_evidence(repo, segments, errors)
    sense_ids = validate_w3_batch(repo, segments, errors)
    relation_ids = validate_w5_batch(repo, sense_ids, segments, errors)
    card_ids = validate_w10_cards(repo, segments, errors)
    validate_syntheses(repo, set(evidence), sense_ids, relation_ids, card_ids, errors)

    if args.final:
        validate_docs(repo, errors)
        validate_protected_corpus(repo, segments, errors)
        validate_append_only(
            repo,
            "knowledge/lexicon/term-senses.jsonl",
            ALLOWED_W3_APPEND_BATCHES,
            errors,
        )
        validate_append_only(
            repo,
            "knowledge/relations/relation-assets.jsonl",
            ALLOWED_W5_APPEND_BATCHES,
            errors,
        )

    output = {
        "status": "FAIL" if errors else "PASS",
        "manifest_rows": len(manifest),
        "evidence_records": len(evidence),
        "w3_batch": len(sense_ids),
        "w5_batch": len(relation_ids),
        "w10_cards": len(card_ids),
        "errors": errors,
    }
    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(
            f"validate_feminism_theme: {output['status']} "
            f"manifest={output['manifest_rows']} evidence={output['evidence_records']} "
            f"w3={output['w3_batch']} w5={output['w5_batch']} "
            f"w10={output['w10_cards']} errors={len(errors)}"
        )
        for error in errors[:120]:
            print("ERROR", error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
