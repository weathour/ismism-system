#!/usr/bin/env python3
"""Validate W10 further-absorption pilot cards.

The validator intentionally checks only local repository evidence. It treats
W10 as an additive draft layer and verifies that every card remains anchored to
W1 segment metadata and exact substrings in split_md_clean.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

CARD_TYPES = {
    "w10-argument-card": {"dir": "argument-cards", "id_prefix": "w10:arg:", "file_prefix": "w10-arg-"},
    "w10-process-card": {"dir": "process-cards", "id_prefix": "w10:proc:", "file_prefix": "w10-proc-"},
    "w10-case-card": {"dir": "case-cards", "id_prefix": "w10:case:", "file_prefix": "w10-case-"},
}
ACCEPTED_STATUS = {"pilot-draft"}
ACCEPTED_REGISTER = {"polemical", "technical", "pedagogical", "diagnostic", "speculative", "mixed"}
ACCEPTED_GAP_REVIEW = {"not_applicable", "followup_needed", "already_covered"}
REQUIRED_FIELDS = [
    "type",
    "status",
    "card_id",
    "filename_stem",
    "row_id",
    "segment_id",
    "toc_id",
    "title",
    "source_clean_path",
    "rhetorical_register",
    "w3_w5_gap_review",
    "claim_core",
    "evidence_quotes",
    "forbidden_use",
]


def strip_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        value = value[1:-1]
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value.strip()


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing opening frontmatter fence"]
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, [f"{path}: missing closing frontmatter fence"]

    meta: dict[str, Any] = {}
    current_key: str | None = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if not raw.startswith(" ") and not raw.startswith("\t"):
            if ":" not in raw:
                errors.append(f"{path}: malformed frontmatter line: {raw}")
                current_key = None
                continue
            key, value = raw.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "[]":
                meta[key] = []
                current_key = None
            elif value == "":
                meta[key] = []
                current_key = key
            else:
                meta[key] = strip_scalar(value)
                current_key = None
            continue

        stripped = raw.strip()
        if current_key == "evidence_quotes":
            if stripped.startswith("- "):
                meta.setdefault(current_key, []).append(strip_scalar(stripped[2:]))
            else:
                errors.append(f"{path}: malformed evidence quote line: {raw}")
        elif current_key == "context_quotes":
            if stripped.startswith("- "):
                payload = stripped[2:].strip()
                item: dict[str, Any] = {}
                if payload:
                    if ":" not in payload:
                        errors.append(f"{path}: malformed context quote item: {raw}")
                    else:
                        key, value = payload.split(":", 1)
                        item[key.strip()] = strip_scalar(value)
                meta.setdefault(current_key, []).append(item)
            elif meta.get("context_quotes") and ":" in stripped:
                key, value = stripped.split(":", 1)
                meta["context_quotes"][-1][key.strip()] = strip_scalar(value)
            else:
                errors.append(f"{path}: malformed context quote line: {raw}")
        elif current_key:
            errors.append(f"{path}: unsupported multiline field {current_key}: {raw}")
        else:
            errors.append(f"{path}: unexpected indented frontmatter line: {raw}")
    return meta, errors


def load_segments(repo: Path) -> dict[int, dict[str, Any]]:
    segments_path = repo / "knowledge/manifests/segments.jsonl"
    segments: dict[int, dict[str, Any]] = {}
    for line in segments_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        segments[int(record["row_id"])] = record
    return segments


def collect_repo_cards(repo: Path) -> tuple[list[Path], list[str]]:
    w10_root = repo / "knowledge/w10-absorption"
    paths: list[Path] = []
    errors: list[str] = []
    allowed_docs = {w10_root / "PLAN.md", w10_root / "index.md"}
    allowed_dirs = {w10_root / spec["dir"] for spec in CARD_TYPES.values()}
    for markdown_path in sorted(w10_root.rglob("*.md")):
        if markdown_path in allowed_docs:
            continue
        if markdown_path.parent in allowed_dirs:
            paths.append(markdown_path)
            continue
        errors.append(
            f"{markdown_path}: unexpected W10 markdown; only PLAN.md, index.md, "
            "and cards in argument-cards/process-cards/case-cards are allowed"
        )
    # Keep deterministic ordering independent of rglob traversal details.
    paths = sorted(paths)
    return paths, errors


def parse_backtick_cell(cell: str, field: str, line_number: int) -> tuple[str | None, str | None]:
    match = re.fullmatch(r"`([^`]+)`", cell.strip())
    if not match:
        return None, f"index.md:{line_number}: {field} cell must be a single backtick-wrapped value"
    return match.group(1), None


def body_after_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return ""
    return "\n".join(lines[end + 1 :])


def normalize_index_href(repo: Path, index_path: Path, href: str, line_number: int) -> tuple[str | None, str | None]:
    if "://" in href or href.startswith("/"):
        return None, f"index.md:{line_number}: card href must be a relative in-repo path, got {href!r}"
    href_path = href.split("#", 1)[0].split("?", 1)[0]
    if not href_path:
        return None, f"index.md:{line_number}: card href target is empty"
    try:
        rel = (index_path.parent / href_path).resolve().relative_to(repo.resolve()).as_posix()
    except ValueError:
        return None, f"index.md:{line_number}: card href points outside repo: {href!r}"
    return rel, None


def parse_index_entries(repo: Path, index_path: Path, index_text: str) -> tuple[list[dict[str, Any]], list[str]]:
    entries: list[dict[str, Any]] = []
    errors: list[str] = []
    link_re = re.compile(r"\[`([^`]+)`\]\(([^)]+)\)")
    in_pilot_table = False
    for line_number, raw in enumerate(index_text.splitlines(), 1):
        line = raw.strip()
        if line == "| card_id | type | row | toc | path |":
            in_pilot_table = True
            continue
        if not in_pilot_table:
            if line.startswith("|") and "w10:" in line:
                errors.append(f"index.md:{line_number}: W10 card row appears outside the Pilot cards table")
            continue
        if not line:
            in_pilot_table = False
            continue
        if not line.startswith("|"):
            in_pilot_table = False
            if "w10:" in line:
                errors.append(f"index.md:{line_number}: W10 card row appears outside the Pilot cards table")
            continue
        if set(line.replace("|", "").strip()) <= {"-", ":"}:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 5:
            errors.append(f"index.md:{line_number}: malformed W10 index row; expected 5 cells")
            continue
        card_id, err = parse_backtick_cell(cells[0], "card_id", line_number)
        if err:
            errors.append(err)
            continue
        card_type, err = parse_backtick_cell(cells[1], "type", line_number)
        if err:
            errors.append(err)
            continue
        toc_id, err = parse_backtick_cell(cells[3], "toc", line_number)
        if err:
            errors.append(err)
            continue
        try:
            row_id = int(cells[2])
        except ValueError:
            errors.append(f"index.md:{line_number}: row id is not an integer: {cells[2]}")
            continue
        match = link_re.search(cells[4])
        if not match:
            errors.append(f"index.md:{line_number}: card path link is malformed")
            continue
        display_path = strip_scalar(match.group(1))
        href_path, err = normalize_index_href(repo, index_path, match.group(2), line_number)
        if err:
            errors.append(err)
            continue
        entries.append(
            {
                "card_id": card_id,
                "type": card_type,
                "row_id": row_id,
                "toc_id": toc_id,
                "path": display_path,
                "href_path": href_path,
                "line_number": line_number,
            }
        )
    seen: set[tuple[str, str]] = set()
    for entry in entries:
        key = (str(entry["card_id"]), str(entry["path"]))
        if key in seen:
            errors.append(f"index.md:{entry['line_number']}: duplicate W10 index entry {key}")
        seen.add(key)
    return entries, errors


def validate_index_exact(expected_entries: list[dict[str, Any]], index_entries: list[dict[str, Any]]) -> list[str]:
    def key(entry: dict[str, Any]) -> tuple[str, str, int, str, str, str]:
        return (
            str(entry["card_id"]),
            str(entry["type"]),
            int(entry["row_id"]),
            str(entry["toc_id"]),
            str(entry["path"]),
            str(entry["href_path"]),
        )

    expected = {key(entry) for entry in expected_entries}
    actual = {key(entry) for entry in index_entries}
    errors: list[str] = []
    for missing in sorted(expected - actual):
        errors.append(f"index.md: missing exact W10 index entry {missing}")
    for stale in sorted(actual - expected):
        errors.append(f"index.md: stale or mismatched W10 index entry {stale}")
    return errors


def is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def check_quote(text: str, quote: str) -> bool:
    return quote in text


def toc_to_scalar(value: Any) -> str:
    """Return the frontmatter/index scalar used for normal and null TOC ids."""
    return "None" if value is None else str(value)


def validate_context_quote(repo: Path, segments: dict[int, dict[str, Any]], item: Any, card_path: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(item, dict):
        return [f"{card_path}: context quote must be an object with row/segment/path metadata"]
    for field in ["row_id", "segment_id", "toc_id", "source_clean_path", "quote"]:
        if not str(item.get(field, "")).strip():
            errors.append(f"{card_path}: context quote missing {field}")
    if errors:
        return errors
    try:
        row_id = int(str(item["row_id"]))
    except ValueError:
        return [f"{card_path}: context quote row_id is not an integer: {item.get('row_id')}"]
    segment = segments.get(row_id)
    if segment is None:
        return [f"{card_path}: context quote row_id not found in segments.jsonl: {row_id}"]
    expected_path = segment["source_paths"]["clean_md_relpath"]
    if str(item["segment_id"]) != segment["segment_id"]:
        errors.append(f"{card_path}: context quote segment_id mismatch for row {row_id}")
    if str(item["toc_id"]) != toc_to_scalar(segment.get("toc_id")):
        errors.append(f"{card_path}: context quote toc_id mismatch for row {row_id}")
    if str(item["source_clean_path"]) != expected_path:
        errors.append(f"{card_path}: context quote source_clean_path mismatch for row {row_id}")
    clean_path = repo / expected_path
    if not clean_path.exists():
        errors.append(f"{card_path}: context quote clean path missing: {expected_path}")
        return errors
    text = clean_path.read_text(encoding="utf-8")
    quote = str(item["quote"])
    if not check_quote(text, quote):
        errors.append(f"{card_path}: context quote is not an exact substring for row {row_id}: {quote[:80]}")
    return errors


def validate_card(repo: Path, segments: dict[int, dict[str, Any]], card_path: Path, seen_ids: set[str]) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    meta, parse_errors = parse_frontmatter(card_path)
    errors.extend(parse_errors)
    if parse_errors:
        return meta, errors

    for field in REQUIRED_FIELDS:
        if field not in meta or meta[field] == [] or not str(meta[field]).strip():
            errors.append(f"{card_path}: missing required field {field}")

    card_type = str(meta.get("type", ""))
    if card_type not in CARD_TYPES:
        errors.append(f"{card_path}: invalid type {card_type!r}")
    status = str(meta.get("status", ""))
    if status not in ACCEPTED_STATUS:
        errors.append(f"{card_path}: invalid status {status!r}; expected pilot-draft")

    card_id = str(meta.get("card_id", ""))
    if card_id:
        if card_id in seen_ids:
            errors.append(f"{card_path}: duplicate card_id {card_id}")
        seen_ids.add(card_id)

    try:
        row_id = int(str(meta.get("row_id", "")))
    except ValueError:
        errors.append(f"{card_path}: row_id is not an integer: {meta.get('row_id')}")
        row_id = -1
    segment = segments.get(row_id)
    if segment is None:
        errors.append(f"{card_path}: row_id not found in segments.jsonl: {row_id}")
        return meta, errors

    expected_clean = segment["source_paths"]["clean_md_relpath"]
    if str(meta.get("segment_id", "")) != segment["segment_id"]:
        errors.append(f"{card_path}: segment_id mismatch; expected {segment['segment_id']}")
    expected_toc = toc_to_scalar(segment.get("toc_id"))
    if str(meta.get("toc_id", "")) != expected_toc:
        errors.append(f"{card_path}: toc_id mismatch; expected {expected_toc}")
    if str(meta.get("source_clean_path", "")) != expected_clean:
        errors.append(f"{card_path}: source_clean_path mismatch; expected {expected_clean}")
    clean_path = repo / expected_clean
    if not clean_path.exists():
        errors.append(f"{card_path}: clean source does not exist: {expected_clean}")
        return meta, errors

    if card_type in CARD_TYPES:
        spec = CARD_TYPES[card_type]
        filename_stem = str(meta.get("filename_stem", ""))
        if filename_stem != card_path.stem:
            errors.append(f"{card_path}: filename_stem mismatch; expected {card_path.stem}")
        if not card_path.stem.startswith(spec["file_prefix"]):
            errors.append(f"{card_path}: filename prefix mismatch for {card_type}; expected {spec['file_prefix']}")
        if not card_id.startswith(spec["id_prefix"]):
            errors.append(f"{card_path}: card_id prefix mismatch for {card_type}; expected {spec['id_prefix']}")
        if f"{row_id:04d}" not in card_id:
            errors.append(f"{card_path}: card_id must contain zero-padded row_id {row_id:04d}")
        if f"{row_id:04d}" not in card_path.stem:
            errors.append(f"{card_path}: filename must contain zero-padded row_id {row_id:04d}")
        w10_root = repo / "knowledge/w10-absorption"
        if is_under(card_path, w10_root):
            expected_dir = w10_root / spec["dir"]
            if card_path.parent.resolve() != expected_dir.resolve():
                errors.append(f"{card_path}: card type must live under {spec['dir']}")

    register = str(meta.get("rhetorical_register", ""))
    if register not in ACCEPTED_REGISTER:
        errors.append(f"{card_path}: invalid rhetorical_register {register!r}")
    gap_review = str(meta.get("w3_w5_gap_review", ""))
    if gap_review not in ACCEPTED_GAP_REVIEW:
        errors.append(f"{card_path}: invalid w3_w5_gap_review {gap_review!r}")
    if not str(meta.get("claim_core", "")).strip():
        errors.append(f"{card_path}: claim_core must be non-empty")
    if not str(meta.get("forbidden_use", "")).strip():
        errors.append(f"{card_path}: forbidden_use must be non-empty")

    quotes = meta.get("evidence_quotes")
    if not isinstance(quotes, list) or not quotes:
        errors.append(f"{card_path}: evidence_quotes must be a non-empty list")
    else:
        clean_text = clean_path.read_text(encoding="utf-8")
        seen_quotes: set[str] = set()
        for quote in quotes:
            quote_s = str(quote).strip()
            if not quote_s:
                errors.append(f"{card_path}: empty evidence quote")
            elif quote_s in seen_quotes:
                errors.append(f"{card_path}: duplicate evidence quote: {quote_s[:100]}")
            elif not check_quote(clean_text, quote_s):
                errors.append(f"{card_path}: evidence quote not found in row {row_id} clean text: {quote_s[:100]}")
            seen_quotes.add(quote_s)

    context_quotes = meta.get("context_quotes", [])
    if context_quotes in ("[]", ""):
        context_quotes = []
    if context_quotes is None:
        context_quotes = []
    if not isinstance(context_quotes, list):
        errors.append(f"{card_path}: context_quotes must be a list when present")
    else:
        for item in context_quotes:
            errors.extend(validate_context_quote(repo, segments, item, card_path))

    if isinstance(quotes, list) and quotes:
        body = body_after_frontmatter(card_path)
        substantive_body = body.split("\n## Evidence Quotes", 1)[0]
        if "限定本行资本主义功能的一个环节" in substantive_body:
            errors.append(f"{card_path}: Capitalism W10 body still contains placeholder close-reading text")
        quote_refs = [int(match) for match in re.findall(r"\[q(\d+)\]", substantive_body)]
        if not quote_refs:
            errors.append(f"{card_path}: body must map substantive claims to evidence quotes using [q1] style references")
        max_quote = len(quotes)
        for ref in sorted(set(quote_refs)):
            if ref < 1 or ref > max_quote:
                errors.append(f"{card_path}: body quote reference [q{ref}] is out of range 1..{max_quote}")
        missing_refs = [f"q{i}" for i in range(1, max_quote + 1) if i not in quote_refs]
        if missing_refs:
            errors.append(f"{card_path}: body does not reference all evidence quotes: {', '.join(missing_refs)}")

    return meta, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate W10 absorption cards")
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument("--extra-card", action="append", default=[], help="Additional card path to validate, useful for adversarial fixtures")
    args = parser.parse_args(argv)

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    w10_root = repo / "knowledge/w10-absorption"
    plan_path = w10_root / "PLAN.md"
    index_path = w10_root / "index.md"
    if not plan_path.exists():
        errors.append("missing knowledge/w10-absorption/PLAN.md")
    if not index_path.exists():
        errors.append("missing knowledge/w10-absorption/index.md")
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""

    try:
        segments = load_segments(repo)
    except Exception as exc:  # pragma: no cover - defensive CLI surface
        print(f"validate_w10_absorption: failed to load segments.jsonl: {exc}", file=sys.stderr)
        return 2

    card_paths, discovery_errors = collect_repo_cards(repo)
    errors.extend(discovery_errors)
    card_paths.extend(Path(p).resolve() for p in args.extra_card)
    index_entries, index_errors = parse_index_entries(repo, index_path, index_text)
    errors.extend(index_errors)
    seen_ids: set[str] = set()
    type_counts = {card_type: 0 for card_type in CARD_TYPES}
    repo_card_count = 0
    expected_index_entries: list[dict[str, Any]] = []

    for card_path in card_paths:
        if not card_path.exists():
            errors.append(f"extra/repo card path does not exist: {card_path}")
            continue
        is_repo_card = is_under(card_path, w10_root)
        meta, card_errors = validate_card(repo, segments, card_path, seen_ids)
        errors.extend(card_errors)
        if is_repo_card:
            repo_card_count += 1
            if meta and meta.get("type") in type_counts:
                type_counts[str(meta["type"])] += 1
            index_row_id: int | None = None
            if meta:
                try:
                    index_row_id = int(str(meta.get("row_id", "")))
                except ValueError:
                    index_row_id = None
                    errors.append(f"{card_path}: cannot build expected index entry because row_id is not an integer")
            if meta and index_row_id is not None:
                expected_index_entries.append(
                    {
                        "card_id": str(meta.get("card_id", "")),
                        "type": str(meta.get("type", "")),
                        "row_id": index_row_id,
                        "toc_id": str(meta.get("toc_id", "")),
                        "path": card_path.relative_to(repo).as_posix(),
                        "href_path": card_path.relative_to(repo).as_posix(),
                    }
                )

    errors.extend(validate_index_exact(expected_index_entries, index_entries))

    if repo_card_count < 5:
        errors.append(f"expected at least 5 W10 repo cards, found {repo_card_count}")
    for card_type, count in type_counts.items():
        if count < 1:
            errors.append(f"expected at least one {card_type}, found {count}")

    if errors:
        print("validate_w10_absorption: FAIL")
        for err in errors:
            print(f"- {err}")
        print(json.dumps({"status": "FAIL", "cards": repo_card_count, "type_counts": type_counts, "errors": len(errors)}, ensure_ascii=False))
        return 1

    print("validate_w10_absorption: PASS")
    print(json.dumps({"status": "PASS", "cards": repo_card_count, "type_counts": type_counts, "errors": 0}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
