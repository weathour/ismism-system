#!/usr/bin/env python3
"""Shared helpers for lightweight read-only ISMISM queries."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable


def repo_root(path: str | Path) -> Path:
    root = Path(path).expanduser().resolve()
    if not (root / "knowledge").is_dir():
        raise SystemExit(f"repo root not found or missing knowledge/: {root}")
    return root


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSONL at {path}:{line_no}: {exc}") from exc
    return records


def term_records(root: Path) -> list[dict[str, Any]]:
    return load_jsonl(root / "knowledge" / "lexicon" / "term-senses.jsonl")


def relation_records(root: Path) -> list[dict[str, Any]]:
    return load_jsonl(root / "knowledge" / "relations" / "relation-assets.jsonl")


def segment_records(root: Path) -> list[dict[str, Any]]:
    return load_jsonl(root / "knowledge" / "manifests" / "segments.jsonl")


def segments_by_row(root: Path) -> dict[int, dict[str, Any]]:
    return {int(record["row_id"]): record for record in segment_records(root)}


def clean_path_for_row(root: Path, row_id: int) -> Path | None:
    record = segments_by_row(root).get(int(row_id))
    if not record:
        return None
    rel = (
        record.get("source_paths", {}).get("clean_md_relpath")
        or record.get("clean_md", {}).get("relpath")
    )
    return root / rel if rel else None


def row_title(root: Path, row_id: int) -> str:
    record = segments_by_row(root).get(int(row_id))
    if not record:
        return ""
    toc_id = record.get("toc_id") or ""
    title = record.get("title") or ""
    return f"{toc_id} {title}".strip()


def record_rows(record: dict[str, Any]) -> list[int]:
    rows: list[int] = []
    for key in ("source_segments", "evidence_quotes", "evidence", "evidence_segment"):
        value = record.get(key) or []
        if isinstance(value, dict):
            value = [value]
        if not isinstance(value, list):
            continue
        for item in value:
            if isinstance(item, dict) and item.get("row_id") is not None:
                try:
                    rows.append(int(item["row_id"]))
                except (TypeError, ValueError):
                    pass
    return sorted(set(rows))


def as_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def truncate(text: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", str(text)).strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 1)].rstrip() + "…"


def contains_any(haystack: Iterable[Any], needle: str) -> bool:
    needle = needle.lower()
    return any(needle in str(item).lower() for item in haystack)


def front_matter_and_body(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip().splitlines()
    meta: dict[str, Any] = {}
    for line in raw:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            parts = [p.strip().strip('"\'') for p in value[1:-1].split(",") if p.strip()]
            parsed: list[Any] = []
            for part in parts:
                try:
                    parsed.append(int(part))
                except ValueError:
                    parsed.append(part)
            value = parsed
        meta[key.strip()] = value
    return meta, text[end + 5 :]


def section_text(body: str, heading: str, *, max_chars: int = 800) -> str:
    marker = f"## {heading}"
    start = body.find(marker)
    if start == -1:
        return ""
    start = body.find("\n", start)
    if start == -1:
        return ""
    end_match = re.search(r"\n## ", body[start + 1 :])
    end = start + 1 + end_match.start() if end_match else len(body)
    return body[start:end].strip()[:max_chars].strip()


def verify_quote_in_row(root: Path, row_id: int, quote: str) -> dict[str, Any]:
    path = clean_path_for_row(root, row_id)
    result: dict[str, Any] = {"row_id": row_id, "quote": quote, "clean_md_path": str(path.relative_to(root)) if path else None}
    if not path or not path.exists():
        result["status"] = "MISSING_TEXT"
        return result
    text = path.read_text(encoding="utf-8")
    result["status"] = "PASS" if quote in text else "NOT_FOUND"
    return result
