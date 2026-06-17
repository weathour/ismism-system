#!/usr/bin/env python3
"""Validate the public ISMISM library contract.

The contract is defined by the current repository shape: corpus sources under
`corpus/`, curated knowledge assets under `library/`, public documentation under
`docs/`, and supported command-line tools under `tools/`. The validator checks
layout, minimum asset counts, public-surface hygiene, and byte-level integrity for
source corpus files recorded in `library/manifests/content-integrity.json`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

PRODUCT_TOP_LEVEL = {
    ".codex-plugin",
    "AGENTS.md",
    "README.md",
    "corpus",
    "docs",
    "examples",
    "library",
    "qa",
    "reviews",
    "skills",
    "tools",
}

PRODUCT_DIRS = (
    ".codex-plugin",
    "corpus/registry",
    "corpus/source",
    "corpus/raw-markdown",
    "corpus/clean-markdown",
    "library/manifests",
    "library/segments",
    "library/concepts",
    "library/positions",
    "library/relations",
    "library/close-reading",
    "library/themes",
    "library/audits",
    "library/protocols",
    "library/templates",
    "library/syntheses",
    "docs",
    "tools/ingest",
    "tools/internal",
    "tools/lib",
    "tools/validate",
    "tools/query",
    "skills/ismism-knowledge-operator",
    "skills/ismism-knowledge-operator/agents",
    "skills/ismism-knowledge-operator/references",
)

PRODUCT_FILES = (
    "README.md",
    "AGENTS.md",
    ".codex-plugin/plugin.json",
    "corpus/registry/toc.csv",
    "corpus/registry/toc.md",
    "corpus/source/ismism.pdf",
    "docs/product-positioning.md",
    "docs/plugin-usage.md",
    "docs/project-contract.md",
    "docs/repository-map.md",
    "docs/status.md",
    "docs/validation.md",
    "docs/query-guide.md",
    "examples/README.md",
    "docs/usage-protocol.md",
    "library/README.md",
    "library/manifests/corpus-manifest.json",
    "library/manifests/content-integrity.json",
    "library/manifests/segments.jsonl",
    "library/manifests/chunks.jsonl",
    "library/concepts/term-senses.jsonl",
    "library/positions/index.md",
    "library/relations/relation-assets.jsonl",
    "library/close-reading/README.md",
    "library/close-reading/index.md",
    "skills/ismism-knowledge-operator/SKILL.md",
    "skills/ismism-knowledge-operator/agents/openai.yaml",
    "skills/ismism-knowledge-operator/references/task-routing.md",
    "skills/ismism-knowledge-operator/references/answer-contract.md",
    "skills/ismism-knowledge-operator/references/curation-protocol.md",
    "skills/ismism-knowledge-operator/references/validation-matrix.md",
    "skills/ismism-knowledge-operator/references/forward-tests.md",
    "tools/ismism.py",
)

# Product-facing active surface. Dense JSONL assets are validated by targeted
# asset validators; the hygiene pass focuses on docs and executable wrappers.
PUBLIC_SURFACES = (
    "README.md",
    "AGENTS.md",
    ".codex-plugin/plugin.json",
    "docs",
    "library/README.md",
    "library/segments/index.md",
    "library/manifests/corpus-manifest.json",
    "library/manifests/missing-and-anomalies.md",
    "library/close-reading/README.md",
    "library/close-reading/index.md",
    "library/themes",
    "reviews",
    "qa",
    "tools/ismism.py",
    "tools/validate",
    "tools/query",
    "skills/ismism-knowledge-operator",
    "skills/ismism-knowledge-operator/agents",
    "skills/ismism-knowledge-operator/references",
)

def token(*parts: str) -> str:
    return "".join(parts)


LOCAL_RUNTIME_MARKER = token(".", "omx", "/")
OLD_ROOT_MARKERS = (
    token("split", "_", "md"),
    token("split", "_", "md", "_", "clean"),
    token("split", "_", "pdf"),
    token("know", "ledge", "/"),
    token("segment", "-", "cards"),
    token("position", "-", "cards"),
    token("w", "10", "-", "absorption"),
    token("Zhuyi", "_", "Matrix", "_", "Engine"),
    token("Relation", " Prompts"),
    token("Low", "-", "token", " prompt"),
    token("maximum", " absorption"),
    token("super", "phase"),
)
OLD_LABEL_MARKERS = (token("W", "10"), token("W", "3"), token("W", "5"))
PUBLIC_RESIDUE_PATTERNS = tuple(
    [("absolute home path", re.compile(r"/home/", flags=re.IGNORECASE)),
     ("local runtime path", re.compile(re.escape(LOCAL_RUNTIME_MARKER), flags=re.IGNORECASE)),
     ("temporary transcript path", re.compile(r"/tmp/[^`\s)]*", flags=re.IGNORECASE))]
    + [(f"old marker: {marker}", re.compile(re.escape(marker), flags=re.IGNORECASE)) for marker in OLD_ROOT_MARKERS]
    + [(f"old label: {marker}", re.compile(rf"\b{re.escape(marker)}\b")) for marker in OLD_LABEL_MARKERS]
)

FORBIDDEN_PRODUCT_CLAIMS = (
    "人格障碍",
    "人格类型",
    "诊断标签",
    "精神病人",
    "患者",
    "最终真理",
    "万能解释器",
)

MIN_COUNTS = {
    "segments": 363,
    "chunks": 1500,
    "concepts": 1500,
    "relations": 1000,
    "close_reading_cards": 700,
}

INTEGRITY_SCOPE = (
    "corpus/raw-markdown/",
    "corpus/clean-markdown/",
    "corpus/source/",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except Exception as exc:  # pragma: no cover - CLI diagnostics
                raise ValueError(f"{path}:{lineno}: {exc}") from exc
    return rows


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def check_shape(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    for entry in repo.iterdir():
        if entry.name.startswith("."):
            continue
        if entry.name not in PRODUCT_TOP_LEVEL:
            add(errors, f"unexpected top-level entry: {entry.name}")
    for rel in PRODUCT_DIRS:
        if not (repo / rel).is_dir():
            add(errors, f"missing product directory: {rel}")
    for rel in PRODUCT_FILES:
        if not (repo / rel).is_file():
            add(errors, f"missing product file: {rel}")
    summary["product_dirs"] = sum((repo / p).is_dir() for p in PRODUCT_DIRS)
    summary["product_files"] = sum((repo / p).is_file() for p in PRODUCT_FILES)


def check_counts(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    segments = load_jsonl(repo / "library/manifests/segments.jsonl")
    chunks = load_jsonl(repo / "library/manifests/chunks.jsonl")
    concepts = load_jsonl(repo / "library/concepts/term-senses.jsonl")
    relations = load_jsonl(repo / "library/relations/relation-assets.jsonl")
    cards = [p for p in (repo / "library/close-reading").glob("*/*.md")]
    summary.update(
        {
            "segments": len(segments),
            "chunks": len(chunks),
            "concepts": len(concepts),
            "relations": len(relations),
            "close_reading_cards": len(cards),
            "themes": len([p for p in (repo / "library/themes").iterdir() if p.is_dir()]),
        }
    )
    for key, min_value in MIN_COUNTS.items():
        if summary[key] < min_value:
            add(errors, f"{key} count {summary[key]} below product floor {min_value}")
    if summary["themes"] < 18:
        add(errors, f"theme count {summary['themes']} below product floor 18")


def iter_public_files(repo: Path) -> Iterable[Path]:
    seen: set[Path] = set()
    for rel in PUBLIC_SURFACES:
        p = repo / rel
        if not p.exists():
            continue
        if p.is_file():
            if p not in seen:
                seen.add(p)
                yield p
        else:
            for fp in p.rglob("*"):
                if fp.is_file() and fp.suffix.lower() in {".md", ".py", ".yaml", ".yml", ".txt"}:
                    if fp not in seen:
                        seen.add(fp)
                        yield fp


def check_public_residue(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    hits: list[str] = []
    for fp in iter_public_files(repo):
        text = fp.read_text(encoding="utf-8", errors="replace")
        for label, rx in PUBLIC_RESIDUE_PATTERNS:
            for m in rx.finditer(text):
                hits.append(f"{fp.relative_to(repo)}:{text[:m.start()].count(chr(10)) + 1}: {label}")
        for claim in FORBIDDEN_PRODUCT_CLAIMS:
            if claim in text:
                hits.append(f"{fp.relative_to(repo)}: forbidden product-surface claim {claim!r}")
    summary["public_residue_hits"] = len(hits)
    errors.extend(hits[:200])


def check_content_integrity(repo: Path, errors: list[str], summary: dict[str, Any]) -> None:
    manifest = repo / "library/manifests/content-integrity.json"
    if not manifest.is_file():
        add(errors, "missing content integrity manifest")
        summary["content_integrity"] = "missing"
        return
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    records = payload.get("records")
    if payload.get("schema") != "ismism.content-integrity.v1":
        add(errors, "unexpected content integrity schema")
    if not isinstance(records, list):
        add(errors, "content integrity records must be a list")
        summary["content_integrity"] = "invalid"
        return
    checked = 0
    for rec in records:
        rel = str(rec.get("path", ""))
        if not rel.startswith(INTEGRITY_SCOPE):
            add(errors, f"content integrity path outside scope: {rel}")
            continue
        path = repo / rel
        if not path.is_file():
            add(errors, f"content integrity target missing: {rel}")
            continue
        if path.stat().st_size != int(rec.get("size", -1)):
            add(errors, f"content size changed: {rel}")
        if sha256(path) != rec.get("sha256"):
            add(errors, f"content hash changed: {rel}")
        checked += 1
    summary["content_integrity"] = "checked"
    summary["content_checked"] = checked
    if checked < 700:
        add(errors, f"content integrity checked only {checked} assets; expected >=700")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate product-facing ISMISM library contract")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--residue-only", action="store_true")
    ap.add_argument("--bytes-only", action="store_true")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    summary: dict[str, Any] = {}

    if args.bytes_only:
        check_content_integrity(repo, errors, summary)
    elif args.residue_only:
        check_shape(repo, errors, summary)
        check_public_residue(repo, errors, summary)
    else:
        check_shape(repo, errors, summary)
        check_counts(repo, errors, summary)
        check_public_residue(repo, errors, summary)
        check_content_integrity(repo, errors, summary)

    summary["status"] = "PASS" if not errors else "FAIL"
    summary["errors"] = errors
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            "ISMISM product contract validation: "
            f"status={summary['status']}, "
            f"dirs={summary.get('product_dirs')}/{len(PRODUCT_DIRS)}, "
            f"files={summary.get('product_files')}/{len(PRODUCT_FILES)}, "
            f"segments={summary.get('segments')}, chunks={summary.get('chunks')}, "
            f"concepts={summary.get('concepts')}, relations={summary.get('relations')}, "
            f"close_reading={summary.get('close_reading_cards')}, themes={summary.get('themes')}, "
            f"residue={summary.get('public_residue_hits')}, bytes={summary.get('content_checked')}, "
            f"errors={len(errors)}"
        )
        for err in errors[:80]:
            print("ERROR", err)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
