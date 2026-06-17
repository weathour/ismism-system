#!/usr/bin/env python3
"""ISMISM Library command runner."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable

CORE_VALIDATORS = [
    [PY, "tools/validate/corpus_manifest.py", "--repo", "."],
    [PY, "tools/validate/concepts.py", "--repo", "."],
    [PY, "tools/validate/positions.py", "--repo", "."],
    [PY, "tools/validate/relations.py", "--repo", ".", "--min-count", "1044", "--require-type-min", "2"],
    [PY, "tools/validate/close_reading.py", "--repo", "."],
    [PY, "tools/validate/library_contract.py", "--repo", "."],
    [PY, "tools/validate/social_topics.py", "--repo", ".", "--final"],
]


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def validate(args: argparse.Namespace) -> None:
    if args.target in {"core", "all"}:
        for cmd in CORE_VALIDATORS:
            run(cmd)
    if args.target == "all":
        for path in sorted((ROOT / "tools" / "validate" / "themes").glob("*.py")):
            run([PY, str(path.relative_to(ROOT)), "--repo", ".", "--final"])
    if args.target == "residue":
        run([PY, "tools/validate/library_contract.py", "--repo", ".", "--residue-only"])


def query(args: argparse.Namespace) -> None:
    mapping = {
        "social": "tools/query/social_topics.py",
        "concept": "tools/query/concept.py",
        "relation": "tools/query/relation.py",
        "position": "tools/query/position.py",
        "trace": "tools/query/trace.py",
    }
    script = mapping[args.kind]
    run([PY, script, *args.rest])


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and query the ISMISM Library.")
    sub = parser.add_subparsers(dest="command", required=True)
    p_val = sub.add_parser("validate", help="run validation suites")
    p_val.add_argument("target", choices=["core", "all", "residue"])
    p_val.set_defaults(func=validate)
    p_query = sub.add_parser("query", help="run query helpers")
    p_query.add_argument("kind", choices=["social", "concept", "relation", "position", "trace"])
    p_query.add_argument("rest", nargs=argparse.REMAINDER)
    p_query.set_defaults(func=query)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
