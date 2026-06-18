#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from field3_theme_validation import validate_field3_theme

SLUG = "phenomenology"
ALLOWED = [
    "phenomenology-overview-review",
    "transcendental-intentionality-reduction",
    "eidetic-factual-phenomenology",
    "lifeworld-intersubjectivity",
    "worldly-ontological-phenomenology",
    "phenomenology-bridge",
    "excluded-keyword-only",
]


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def make_repo() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    td = tempfile.TemporaryDirectory(prefix="field3-negative-")
    tmp = Path(td.name)
    (tmp / "library" / "themes").mkdir(parents=True)
    shutil.copytree(ROOT / "library" / "themes" / SLUG, tmp / "library" / "themes" / SLUG)
    (tmp / "corpus").symlink_to(ROOT / "corpus", target_is_directory=True)
    return td, tmp


def expect_fail(name: str, mutator) -> str:
    td, repo = make_repo()
    try:
        mutator(repo / "library" / "themes" / SLUG)
        summary = validate_field3_theme(repo, SLUG, ALLOWED, final=True)
        if summary["status"] != "FAIL":
            raise AssertionError(f"{name}: expected FAIL, got {summary['status']}")
        return f"{name}: PASS negative failure detected ({len(summary.get('errors', []))} errors)"
    finally:
        td.cleanup()


def corrupt_quote(theme_dir: Path) -> None:
    path = theme_dir / f"{SLUG}-evidence-bank.jsonl"
    rows = read_jsonl(path)
    rows[0]["quote"] += "__NOT_IN_SOURCE__"
    write_jsonl(path, rows)


def invalid_class(theme_dir: Path) -> None:
    path = theme_dir / f"{SLUG}-row-manifest.jsonl"
    rows = read_jsonl(path)
    rows[0]["theme_class"] = "invalid-class"
    write_jsonl(path, rows)


def duplicate_taxonomy(theme_dir: Path) -> None:
    path = theme_dir / f"{SLUG}-taxonomy.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("- transcendental-intentionality-reduction: rows ", "- transcendental-intentionality-reduction: rows 188, ", 1)
    path.write_text(text, encoding="utf-8")


def missing_readme_reference(theme_dir: Path) -> None:
    path = theme_dir / "README.md"
    text = path.read_text(encoding="utf-8").replace("tools/query/themes/phenomenology.py", "tools/query/themes/missing.py")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    checks = [
        ("corrupt evidence quote", corrupt_quote),
        ("invalid manifest class", invalid_class),
        ("duplicate taxonomy row", duplicate_taxonomy),
        ("missing README query reference", missing_readme_reference),
    ]
    for name, fn in checks:
        print(expect_fail(name, fn))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
