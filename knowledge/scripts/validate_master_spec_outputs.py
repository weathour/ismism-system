#!/usr/bin/env python3
"""Validate repo-local MASTER-SPEC output gates.

This read-only validator complements the W3/W4/W5 validators.  It checks the
in-repository deliverables for W6/W7/W8/W9-readiness and the active-surface
forbidden-language rule.  By default it respects the repository hard boundary
and does not require the external psychoanalytic-writing-lab target to exist.
Use --require-external-w9 only when a human explicitly authorizes checking the
outside-repo integration target.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


FORBIDDEN_PATTERNS = (
    "人格障碍",
    "人格类型",
    "诊断标签",
    "精神病人",
    "患者",
    "最终真理",
    "万能解释器",
)

W6_REPORTS = (
    "knowledge/qa/validation-report.md",
    "knowledge/qa/concept-drift-report.md",
    "knowledge/qa/evidence-claim-audit.md",
    "knowledge/qa/rejected-interpretations.md",
)

W7_SYNTHESES = (
    "knowledge/syntheses/part-1-realism.md",
    "knowledge/syntheses/part-2-metaphysics.md",
    "knowledge/syntheses/part-3-idealism.md",
    "knowledge/syntheses/part-4-praxis.md",
    "knowledge/syntheses/whole-system-map.md",
    "knowledge/syntheses/methodological-core.md",
)

W8_DOCS = (
    "knowledge/usage-protocol.md",
    "knowledge/query-playbook.md",
    "knowledge/export-manifest.md",
)

W4_EXPECTED_COUNTS = {
    1: 4,
    2: 16,
    3: 64,
    4: 172,
}

W5_REQUIRED_TYPES = {
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

W9_REPO_LOCAL = "knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md"
W9_AUDIT = "knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md"
W9_STATUS_SCRIPT = "knowledge/scripts/check_w9_external_status.py"
W9_DECISION_RECORD = "knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md"
W9_EXTERNAL = "/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md"

ACTIVE_SURFACE_PATHS = (
    "knowledge/position-cards",
    "knowledge/lexicon/term-senses.jsonl",
    "knowledge/lexicon/core-terms.md",
    "knowledge/lexicon/ambiguous-terms.md",
    "knowledge/qa",
    "knowledge/relations",
    "knowledge/syntheses",
    "knowledge/usage-protocol.md",
    "knowledge/query-playbook.md",
    "knowledge/export-manifest.md",
    "knowledge/integration",
    "knowledge/STATE.md",
    "ISMISM-MAINLINE-HANDOFF.md",
    "knowledge/logs/operation-log.md",
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                out.append(json.loads(line))
            except Exception as exc:
                raise ValueError(f"{path}:{lineno}: JSON parse failed: {exc}") from exc
    return out


def add_error(errors: list[str], msg: str) -> None:
    errors.append(msg)


def check_exists(repo: Path, relpaths: tuple[str, ...], errors: list[str]) -> None:
    for rel in relpaths:
        if not (repo / rel).exists():
            add_error(errors, f"missing required file: {rel}")


def check_w3(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    try:
        records = load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")
    except Exception as exc:
        add_error(errors, str(exc))
        return
    terms = {str(r.get("term", "")) for r in records}
    quotes = sum(len(r.get("evidence_quotes", []) or []) for r in records)
    summary["w3_senses"] = len(records)
    summary["w3_terms"] = len(terms)
    summary["w3_quotes"] = quotes
    if len(records) < 500:
        add_error(errors, f"W3 has {len(records)} senses; expected >=500")
    if len(terms) < 200:
        add_error(errors, f"W3 has {len(terms)} terms; expected >=200")
    sparse_quotes = [
        r.get("sense_id")
        for r in records
        if len(r.get("evidence_quotes", []) or []) < 2
    ]
    if sparse_quotes:
        add_error(errors, f"W3 senses with <2 evidence_quotes: {sparse_quotes[:10]}")
    missing_axis = [r.get("sense_id") for r in records if not r.get("axis")]
    if missing_axis:
        add_error(errors, f"W3 senses missing axis: {missing_axis[:10]}")
    missing_forbidden = [r.get("sense_id") for r in records if not r.get("forbidden_mix")]
    if missing_forbidden:
        add_error(errors, f"W3 senses missing forbidden_mix: {missing_forbidden[:10]}")
    non_draft = [r.get("sense_id") for r in records if r.get("status") != "draft"]
    if non_draft:
        add_error(errors, f"W3 non-draft records found: {non_draft[:10]}")
    ambiguous = repo / "knowledge/lexicon/ambiguous-terms.md"
    if not ambiguous.exists() or len(ambiguous.read_text(encoding="utf-8").strip()) < 500:
        add_error(errors, "W3 ambiguous-terms.md missing or too short to evidence overlap tracking")


def card_level(path: Path) -> int | None:
    stem = path.stem
    if not re.fullmatch(r"\d(?:-\d){0,3}", stem):
        return None
    return stem.count("-") + 1


def check_w4(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    cards_dir = repo / "knowledge/position-cards"
    index = cards_dir / "index.md"
    if not cards_dir.exists():
        add_error(errors, "missing W4 directory: knowledge/position-cards")
        return
    if not index.exists():
        add_error(errors, "missing W4 index: knowledge/position-cards/index.md")
        idx_text = ""
    else:
        idx_text = index.read_text(encoding="utf-8")
    cards = sorted(p for p in cards_dir.glob("*.md") if p.name != "index.md")
    counts = {level: 0 for level in W4_EXPECTED_COUNTS}
    required_sections = (
        "## 矩阵坐标",
        "## 位置定义",
        "## 代表主义/学派",
        "## 核心机制",
        "## 与相邻位置的关系",
        "## 关联术语",
    )
    for path in cards:
        level = card_level(path)
        if level in counts:
            counts[level] += 1
        text = path.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                add_error(errors, f"{path.relative_to(repo)} missing section {section}")
        if "status: draft" not in text:
            add_error(errors, f"{path.relative_to(repo)} is not marked draft")
        if "已收录" not in text:
            add_error(errors, f"{path.relative_to(repo)} lacks collected-term marker")
        if f"knowledge/position-cards/{path.name}" not in idx_text:
            add_error(errors, f"W4 index does not list {path.name}")
    for level, expected in W4_EXPECTED_COUNTS.items():
        if counts[level] != expected:
            add_error(errors, f"W4 level {level} has {counts[level]} cards; expected {expected}")
    summary["w4_counts"] = counts
    summary["w4_total"] = sum(counts.values())


def check_w5(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    try:
        records = load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")
    except Exception as exc:
        add_error(errors, str(exc))
        return
    types = {str(r.get("relation_type", "")) for r in records}
    summary["w5_relations"] = len(records)
    summary["w5_types"] = len(types)
    if len(records) < 60:
        add_error(errors, f"W5 has {len(records)} relations; expected >=60")
    missing_types = sorted(W5_REQUIRED_TYPES - types)
    if missing_types:
        add_error(errors, f"W5 missing relation types: {missing_types}")
    type_counts = {t: 0 for t in W5_REQUIRED_TYPES}
    for r in records:
        t = str(r.get("relation_type", ""))
        if t in type_counts:
            type_counts[t] += 1
    thin_types = {t: c for t, c in sorted(type_counts.items()) if c < 2}
    if thin_types:
        add_error(errors, f"W5 relation types with <2 examples: {thin_types}")
    missing_boundary = [
        r.get("relation_id")
        for r in records
        if not r.get("applicability_boundary") or not r.get("forbidden_interpretation")
    ]
    if missing_boundary:
        add_error(errors, f"W5 relations missing boundary/forbidden fields: {missing_boundary[:10]}")
    missing_evidence = [
        r.get("relation_id")
        for r in records
        if not r.get("evidence_segment")
    ]
    if missing_evidence:
        add_error(errors, f"W5 relations missing evidence_segment: {missing_evidence[:10]}")
    non_draft = [r.get("relation_id") for r in records if r.get("status") != "draft"]
    if non_draft:
        add_error(errors, f"W5 non-draft records found: {non_draft[:10]}")
    summary["w5_type_counts"] = type_counts


def check_w7_tags(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    terms = {r["sense_id"] for r in load_jsonl(repo / "knowledge/lexicon/term-senses.jsonl")}
    rels = {r["relation_id"] for r in load_jsonl(repo / "knowledge/relations/relation-assets.jsonl")}
    checked = 0
    for rel in W7_SYNTHESES:
        path = repo / rel
        if not path.exists():
            add_error(errors, f"missing W7 synthesis: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for m in re.finditer(r"term:([^,\]\s]+:s\d\d)", text):
            sid = "term:" + m.group(1)
            if sid not in terms:
                add_error(errors, f"{rel}: missing W3 sense ref {sid}")
        for m in re.finditer(r"relation (rel:[^,\]\s]+)", text):
            rid = m.group(1)
            if rid not in rels:
                add_error(errors, f"{rel}: missing W5 relation ref {rid}")
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.startswith("- ") and not any(line.startswith(prefix) for prefix in ("- status:", "- scope:")):
                if "[row " not in line:
                    add_error(errors, f"{rel}:{lineno}: substantive bullet lacks source tag")
        checked += 1
    summary["w7_syntheses"] = checked


def check_w8(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    check_exists(repo, W8_DOCS, errors)
    summary["w8_docs"] = sum((repo / p).exists() for p in W8_DOCS)
    playbook = repo / "knowledge/query-playbook.md"
    if playbook.exists():
        text = playbook.read_text(encoding="utf-8")
        query_count = len(re.findall(r"^##\s+\d+\.", text, flags=re.MULTILINE))
        summary["w8_query_paths"] = query_count
        if query_count < 10:
            add_error(errors, f"W8 query-playbook has {query_count} numbered paths; expected >=10")
    else:
        summary["w8_query_paths"] = 0


def iter_active_files(repo: Path) -> list[Path]:
    files: list[Path] = []
    for rel in ACTIVE_SURFACE_PATHS:
        path = repo / rel
        if not path.exists():
            continue
        if path.is_file():
            files.append(path)
        else:
            files.extend(p for p in path.rglob("*") if p.is_file())
    return files


def check_forbidden(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    hits: list[str] = []
    for path in iter_active_files(repo):
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                hits.append(f"{path.relative_to(repo)} contains forbidden pattern {pattern!r}")
    summary["forbidden_hits"] = len(hits)
    for hit in hits[:50]:
        add_error(errors, hit)


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate repo-local MASTER-SPEC deliverables.")
    ap.add_argument("--repo", default=".", help="repository root")
    ap.add_argument("--require-external-w9", action="store_true", help="also require external W9 target file")
    ap.add_argument("--json", action="store_true", help="emit JSON summary")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    summary: dict[str, Any] = {}

    check_w3(repo, errors, summary)
    check_w4(repo, errors, summary)
    check_w5(repo, errors, summary)
    check_exists(repo, W6_REPORTS, errors)
    summary["w6_reports"] = sum((repo / p).exists() for p in W6_REPORTS)
    check_exists(repo, W7_SYNTHESES, errors)
    check_w7_tags(repo, errors, summary)
    check_w8(repo, errors, summary)
    check_exists(repo, (W9_REPO_LOCAL, W9_AUDIT, W9_STATUS_SCRIPT, W9_DECISION_RECORD), errors)
    summary["w9_repo_local"] = (repo / W9_REPO_LOCAL).exists()
    summary["w9_external_audit"] = (repo / W9_AUDIT).exists()
    summary["w9_status_script"] = (repo / W9_STATUS_SCRIPT).exists()
    summary["w9_decision_record"] = (repo / W9_DECISION_RECORD).exists()
    if args.require_external_w9:
        external = Path(W9_EXTERNAL)
        repo_local = repo / W9_REPO_LOCAL
        if not external.exists():
            add_error(errors, f"external W9 target missing: {W9_EXTERNAL}")
            summary["w9_external"] = False
        else:
            summary["w9_external"] = True
            if repo_local.exists() and external.read_text(encoding="utf-8") != repo_local.read_text(encoding="utf-8"):
                add_error(
                    errors,
                    "external W9 target exists but differs from repo-local W9 protocol; "
                    f"target={W9_EXTERNAL}",
                )
    else:
        summary["w9_external"] = "not_checked_by_repo_local_validator"
    check_exists(repo, ("knowledge/qa/master-spec-completion-audit.md",), errors)
    summary["master_audit"] = (repo / "knowledge/qa/master-spec-completion-audit.md").exists()
    check_exists(repo, ("knowledge/qa/master-spec-requirement-traceability.md",), errors)
    summary["master_traceability"] = (
        repo / "knowledge/qa/master-spec-requirement-traceability.md"
    ).exists()
    check_forbidden(repo, errors, summary)

    summary["status"] = "PASS" if not errors else "FAIL"
    summary["errors"] = errors

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            "MASTER-SPEC repo-local validation: "
            f"status={summary['status']}, "
            f"w3={summary.get('w3_senses')}/{summary.get('w3_terms')}, "
            f"w4={summary.get('w4_total')}, "
            f"w5={summary.get('w5_relations')}, "
            f"w6_reports={summary.get('w6_reports')}/4, "
            f"w7={summary.get('w7_syntheses')}/6, "
            f"w8={summary.get('w8_docs')}/3/{summary.get('w8_query_paths')}queries, "
            f"w9_repo_local={summary.get('w9_repo_local')}, "
            f"w9_external_audit={summary.get('w9_external_audit')}, "
            f"w9_status_script={summary.get('w9_status_script')}, "
            f"w9_decision_record={summary.get('w9_decision_record')}, "
            f"errors={len(errors)}"
        )
        for err in errors[:50]:
            print("ERROR", err)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
