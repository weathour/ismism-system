#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

SLUG = "science-academia-research"
THEME_DIR = Path("library/themes") / SLUG
MANIFEST_NAME = "science-academia-research-row-manifest.jsonl"
EVIDENCE_NAME = "science-academia-research-evidence-bank.jsonl"
TAXONOMY_NAME = "science-academia-research-taxonomy.md"
GO_NOGO_NAME = "science-academia-research-go-no-go.md"

ALLOWED_CORE = {"core", "bridge", "context", "excluded"}
ALLOWED_CLASSES = {
    "scientific-discourse-reality-definition",
    "scientific-knowledge-sociology-paradigm",
    "scientism-naturalism-positivism",
    "academic-institution-community",
    "research-evaluation-paper-metrics",
    "expert-stem-subjectivation",
    "academic-practice-critical-counter-community",
    "technology-industry-science-bridge",
    "excluded-keyword-only",
}
ALLOWED_OVERLAP = {
    "science-core-distinct-function",
    "education-core-science-bridge",
    "education-owned-excluded",
    "not-in-education",
}
ALLOWED_REUSE = {
    "reuse-education-quote-with-new-function",
    "new-quote-required",
    "avoid-education-evidence",
    "not-applicable",
}
REQUIRED_MANIFEST_FIELDS = {
    "row_id",
    "segment_id",
    "toc_id",
    "title",
    "clean_md_path",
    "source_clean_path",
    "core_status",
    "theme_class",
    "overlap_status",
    "education_theme_class",
    "science_claim_function",
    "evidence_reuse_policy",
    "evidence_quote_count",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except Exception as exc:  # pragma: no cover - error path
                raise ValueError(f"{path}:{lineno}: invalid JSON: {exc}") from exc
            if not isinstance(obj, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            records.append(obj)
    return records


def checked_int(value: Any) -> int:
    if value is None:
        raise ValueError("missing integer value")
    return int(value)


def toc_rows(repo: Path) -> set[int]:
    out: set[int] = set()
    with (repo / "corpus/registry/toc.csv").open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            out.add(int(row["row_id"]))
    return out


def education_rows(repo: Path) -> dict[int, dict[str, Any]]:
    path = repo / "library/themes/education-examination-credentialism/education-examination-credentialism-row-manifest.jsonl"
    if not path.exists():
        return {}
    return {int(r["row_id"]): r for r in load_jsonl(path)}


def parse_taxonomy(path: Path) -> dict[int, str]:
    current: str | None = None
    ownership: dict[int, str] = {}
    duplicate_rows: list[int] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"##\s+T\d+\.\s+(.+)\s*$", line)
        if m:
            current = m.group(1).strip()
            continue
        if current and line.startswith("- rows:"):
            for rid_s in re.findall(r"row\s+(\d+)", line):
                rid = int(rid_s)
                if rid in ownership:
                    duplicate_rows.append(rid)
                ownership[rid] = current
    if duplicate_rows:
        ownership[-1] = "DUPLICATE:" + ",".join(map(str, sorted(set(duplicate_rows))))
    return ownership


def validate(repo: Path, final: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    theme = repo / THEME_DIR
    if not theme.is_dir():
        return {"status": "FAIL", "theme": SLUG, "errors": [f"missing theme dir: {THEME_DIR}"]}

    for name in ["README.md", MANIFEST_NAME, EVIDENCE_NAME, TAXONOMY_NAME, GO_NOGO_NAME]:
        if not (theme / name).is_file():
            errors.append(f"missing required file: {(THEME_DIR / name).as_posix()}")

    manifest = load_jsonl(theme / MANIFEST_NAME) if (theme / MANIFEST_NAME).exists() else []
    evidence = load_jsonl(theme / EVIDENCE_NAME) if (theme / EVIDENCE_NAME).exists() else []
    toc = toc_rows(repo)
    edu = education_rows(repo)
    taxonomy = parse_taxonomy(theme / TAXONOMY_NAME) if (theme / TAXONOMY_NAME).exists() else {}

    rows_seen: set[int] = set()
    evidence_counts: Counter[int] = Counter()
    exact_quotes = 0
    usable = 0

    for i, rec in enumerate(manifest, 1):
        missing = sorted(REQUIRED_MANIFEST_FIELDS - set(rec))
        if missing:
            errors.append(f"manifest:{i}: missing fields {missing}")
        row_id_raw = rec.get("row_id")
        try:
            row_id = checked_int(row_id_raw)
        except Exception:
            errors.append(f"manifest:{i}: row_id is not integer: {row_id_raw!r}")
            continue
        if row_id in rows_seen:
            errors.append(f"manifest:{i}: duplicate row_id {row_id}")
        rows_seen.add(row_id)
        if row_id not in toc:
            errors.append(f"manifest:{i}: row_id {row_id} not in toc.csv")
        if rec.get("segment_id") != f"ismism:seg:{row_id}":
            errors.append(f"manifest:{i}: segment_id mismatch for row {row_id}")
        clean = rec.get("source_clean_path") or rec.get("clean_md_path")
        if not clean or not (repo / str(clean)).is_file():
            errors.append(f"manifest:{i}: source clean path missing for row {row_id}: {clean}")
        core = rec.get("core_status")
        klass = rec.get("theme_class")
        overlap = rec.get("overlap_status")
        reuse = rec.get("evidence_reuse_policy")
        if core not in ALLOWED_CORE:
            errors.append(f"manifest:{i}: invalid core_status {core!r}")
        if klass not in ALLOWED_CLASSES:
            errors.append(f"manifest:{i}: invalid theme_class {klass!r}")
        if overlap not in ALLOWED_OVERLAP:
            errors.append(f"manifest:{i}: invalid overlap_status {overlap!r}")
        if reuse not in ALLOWED_REUSE:
            errors.append(f"manifest:{i}: invalid evidence_reuse_policy {reuse!r}")
        if core in {"core", "bridge"}:
            usable += 1
        science_function = str(rec.get("science_claim_function") or "").strip()
        if not science_function:
            errors.append(f"manifest:{i}: missing science_claim_function for row {row_id}")
        if row_id in edu:
            if overlap == "not-in-education":
                errors.append(f"manifest:{i}: row {row_id} appears in Education but overlap_status is not-in-education")
            if not rec.get("education_theme_class"):
                errors.append(f"manifest:{i}: row {row_id} appears in Education but education_theme_class is empty")
            elif rec.get("education_theme_class") != edu[row_id].get("theme_class"):
                errors.append(f"manifest:{i}: row {row_id} education_theme_class mismatch: {rec.get('education_theme_class')} != {edu[row_id].get('theme_class')}")
        else:
            if overlap != "not-in-education":
                errors.append(f"manifest:{i}: row {row_id} absent from Education but overlap_status={overlap}")
            if rec.get("education_theme_class") not in (None, ""):
                errors.append(f"manifest:{i}: row {row_id} absent from Education but education_theme_class is set")
        if overlap == "education-core-science-bridge" and core not in {"bridge", "context"}:
            errors.append(f"manifest:{i}: education-core-science-bridge row {row_id} must be bridge/context")
        if overlap == "education-owned-excluded" and core != "excluded":
            errors.append(f"manifest:{i}: education-owned-excluded row {row_id} must be excluded")
        if overlap == "science-core-distinct-function" and row_id not in edu:
            errors.append(f"manifest:{i}: science-core-distinct-function row {row_id} must be shared with Education")
        if row_id in taxonomy and taxonomy[row_id] != klass:
            errors.append(f"manifest:{i}: taxonomy class mismatch for row {row_id}: {taxonomy[row_id]} != {klass}")

    if -1 in taxonomy:
        errors.append(f"taxonomy duplicate row ownership: {taxonomy[-1]}")
    missing_tax = sorted(rows_seen - {r for r in taxonomy if r > 0})
    extra_tax = sorted({r for r in taxonomy if r > 0} - rows_seen)
    if missing_tax:
        errors.append(f"taxonomy missing manifest rows: {missing_tax[:30]}")
    if extra_tax:
        errors.append(f"taxonomy owns rows absent from manifest: {extra_tax[:30]}")

    evidence_ids: set[str] = set()
    evidence_tuples: set[tuple[int, str, str, str]] = set()
    for i, ev in enumerate(evidence, 1):
        row_id = ev.get("row_id")
        try:
            row_i = checked_int(row_id)
        except Exception:
            errors.append(f"evidence:{i}: row_id is not integer: {row_id!r}")
            continue
        if row_i not in rows_seen:
            errors.append(f"evidence:{i}: row {row_i} absent from manifest")
        evidence_counts[row_i] += 1
        ev_id = str(ev.get("evidence_id") or "").strip()
        if not ev_id:
            errors.append(f"evidence:{i}: missing evidence_id")
        elif ev_id in evidence_ids:
            errors.append(f"evidence:{i}: duplicate evidence_id {ev_id}")
        evidence_ids.add(ev_id)
        clean = ev.get("source_clean_path") or ev.get("clean_md_path")
        quote = ev.get("quote")
        if not clean or not (repo / str(clean)).is_file():
            errors.append(f"evidence:{i}: clean path missing: {clean}")
            continue
        if not quote:
            errors.append(f"evidence:{i}: missing quote")
            continue
        text = (repo / str(clean)).read_text(encoding="utf-8")
        if str(quote) not in text:
            errors.append(f"evidence:{i}: quote not exact substring for row {row_i}")
        else:
            exact_quotes += 1
        tuple_key = (
            row_i,
            str(quote),
            str(ev.get("quote_role") or ""),
            str(ev.get("trigger_keyword") or ""),
        )
        if tuple_key in evidence_tuples:
            errors.append(
                f"evidence:{i}: duplicate row/quote/role/trigger tuple for row {row_i}"
            )
        evidence_tuples.add(tuple_key)
        tags = ev.get("theme_tags") or []
        if tags and any(tag not in ALLOWED_CLASSES for tag in tags):
            errors.append(f"evidence:{i}: invalid theme_tags {tags}")

    by_row: dict[int, dict[str, Any]] = {}
    for rec in manifest:
        try:
            by_row[checked_int(rec.get("row_id"))] = rec
        except Exception:
            continue
    for row_id, rec in by_row.items():
        expected = checked_int(rec.get("evidence_quote_count") or 0)
        actual = evidence_counts[row_id]
        if expected != actual:
            errors.append(f"row {row_id}: evidence_quote_count={expected} but evidence has {actual}")

    if len(manifest) < 45:
        errors.append(f"manifest has fewer than 45 rows: {len(manifest)}")
    if usable < 45:
        errors.append(f"usable core/bridge rows below independent-theme threshold: {usable}")
    if len(evidence) < 180:
        errors.append(f"evidence record count below target floor 180: {len(evidence)}")

    if final:
        syntheses = sorted(theme.glob("*synthesis.md"))
        if len(syntheses) < 3:
            errors.append("final: expected at least 3 synthesis files")
        notes = theme / "science-academia-research-concept-relation-notes.md"
        if not notes.is_file():
            errors.append("final: missing concept/relation notes")
        if not (repo / "tools/query/themes/science_academia_research.py").is_file():
            errors.append("final: missing query helper wrapper")
        go_text = (theme / GO_NOGO_NAME).read_text(encoding="utf-8") if (theme / GO_NOGO_NAME).exists() else ""
        if "decision: GO" not in go_text:
            errors.append("final: go/no-go artifact does not record GO decision")
        coverage_index = theme / "science-academia-research-close-reading-coverage.jsonl"
        evidence_by_id = {str(ev.get("evidence_id")): ev for ev in evidence}
        manifest_by_row: dict[int, dict[str, Any]] = {}
        for rec in manifest:
            try:
                manifest_by_row[checked_int(rec.get("row_id"))] = rec
            except Exception:
                continue
        if not coverage_index.is_file():
            errors.append("final: missing close-reading coverage index")
        else:
            coverage = load_jsonl(coverage_index)
            if not 25 <= len(coverage) <= 40:
                errors.append(f"final: close-reading coverage should have 25-40 records, found {len(coverage)}")
            covered: set[int] = set()
            for x in coverage:
                if x.get("status") not in {"pilot-draft", "audited-rationale"}:
                    continue
                try:
                    covered.add(checked_int(x.get("row_id")))
                except Exception:
                    continue
            required = {2, 9, 10, 11, 76, 177, 184, 205, 277, 292}
            missing = sorted(required - covered)
            if missing:
                errors.append(f"final: close-reading hard-core coverage missing rows {missing}")
            for j, item in enumerate(coverage, 1):
                try:
                    rid = checked_int(item.get("row_id"))
                except Exception:
                    errors.append(f"final: coverage:{j}: bad row_id {item.get('row_id')!r}")
                    continue
                if rid not in manifest_by_row:
                    errors.append(f"final: coverage:{j}: row {rid} absent from manifest")
                    continue
                if manifest_by_row[rid].get("overlap_status") == "education-owned-excluded":
                    errors.append(f"final: coverage:{j}: row {rid} is education-owned-excluded")
                if item.get("status") not in {"pilot-draft", "audited-rationale"}:
                    errors.append(f"final: coverage:{j}: invalid status {item.get('status')!r}")
                markers = item.get("quote_markers")
                claim_map = item.get("claim_map")
                if not isinstance(markers, list) or len(markers) < 2:
                    errors.append(f"final: coverage:{j}: expected at least two quote markers")
                    markers = []
                if not isinstance(claim_map, list) or not claim_map:
                    errors.append(f"final: coverage:{j}: missing claim_map")
                    claim_map = []
                marker_names = {str(m.get("marker")) for m in markers if isinstance(m, dict)}
                for marker in markers:
                    if not isinstance(marker, dict):
                        errors.append(f"final: coverage:{j}: bad marker item")
                        continue
                    ev_id = str(marker.get("evidence_id") or "")
                    ev = evidence_by_id.get(ev_id)
                    if not ev:
                        errors.append(f"final: coverage:{j}: evidence_id {ev_id} not found")
                    else:
                        try:
                            ev_row = checked_int(ev.get("row_id"))
                        except Exception:
                            errors.append(f"final: coverage:{j}: evidence_id {ev_id} has bad row_id {ev.get('row_id')!r}")
                            continue
                        if ev_row != rid:
                            errors.append(f"final: coverage:{j}: evidence_id {ev_id} belongs to row {ev.get('row_id')}, not {rid}")
                        marker_role = marker.get("quote_role")
                        if marker_role != ev.get("quote_role"):
                            errors.append(
                                f"final: coverage:{j}: marker {marker.get('marker')} quote_role "
                                f"{marker_role!r} != evidence {ev.get('quote_role')!r}"
                            )
                        marker_trigger = marker.get("trigger_keyword")
                        if marker_trigger != ev.get("trigger_keyword"):
                            errors.append(
                                f"final: coverage:{j}: marker {marker.get('marker')} trigger_keyword "
                                f"{marker_trigger!r} != evidence {ev.get('trigger_keyword')!r}"
                            )
                for claim in claim_map:
                    marker = str(claim.get("marker") or "") if isinstance(claim, dict) else ""
                    if marker and marker not in marker_names:
                        errors.append(f"final: coverage:{j}: claim_map marker {marker} has no quote marker")
                if not str(item.get("forbidden_use") or "").strip():
                    errors.append(f"final: coverage:{j}: missing forbidden_use")
        dedup = theme / "science-academia-research-w3-w5-dedup-map.json"
        if not dedup.is_file():
            errors.append("final: missing concept/relation de-dup map")
        else:
            data = json.loads(dedup.read_text(encoding="utf-8"))
            for klass in ALLOWED_CLASSES - {"excluded-keyword-only"}:
                if klass not in data.get("class_coverage", {}):
                    errors.append(f"final: concept/relation de-dup map missing class coverage for {klass}")
            for item in data.get("new_w3", []) + data.get("new_w5", []):
                if item.get("status") != "draft":
                    errors.append(f"final: non-draft concept/relation addition in dedup map: {item}")
        for synth in syntheses:
            text = synth.read_text(encoding="utf-8")
            if "ev:sar:" not in text or "row " not in text:
                errors.append(f"final: synthesis lacks evidence markers: {synth.relative_to(repo)}")

    summary = {
        "status": "PASS" if not errors else "FAIL",
        "theme": SLUG,
        "manifest_rows": len(manifest),
        "unique_manifest_rows": len(rows_seen),
        "evidence_records": len(evidence),
        "exact_quotes_checked": exact_quotes,
        "usable_core_bridge_rows": usable,
        "core_status_counts": Counter(str(r.get("core_status")) for r in manifest),
        "theme_class_counts": Counter(str(r.get("theme_class")) for r in manifest),
        "overlap_status_counts": Counter(str(r.get("overlap_status")) for r in manifest),
        "final": final,
        "errors": errors,
    }
    # convert Counters to normal dicts for JSON stability.
    for key in ["core_status_counts", "theme_class_counts", "overlap_status_counts"]:
        summary[key] = dict(summary[key])
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the Science / Academia / Research theme")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    summary = validate(repo, final=args.final)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"validate_theme[{SLUG}]: {summary['status']} "
            f"manifest={summary['manifest_rows']} evidence={summary['evidence_records']} "
            f"quotes={summary['exact_quotes_checked']} usable={summary['usable_core_bridge_rows']} "
            f"errors={len(summary['errors'])}"
        )
        for err in summary["errors"][:100]:
            print("ERROR", err)
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
