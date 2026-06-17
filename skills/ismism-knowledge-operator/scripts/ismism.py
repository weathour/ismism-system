#!/usr/bin/env python3
"""Run ISMISM Library commands from any current working directory.

This wrapper is bundled inside the Codex skill so an installed plugin can query
or validate the ISMISM Library even when Codex is operating in another project.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def plugin_root() -> Path:
    override = os.environ.get("ISMISM_LIBRARY_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    # <plugin-root>/skills/ismism-knowledge-operator/scripts/ismism.py
    return Path(__file__).resolve().parents[3]


def main() -> int:
    root = plugin_root()
    if len(sys.argv) == 2 and sys.argv[1] in {"root", "--root", "print-root", "--print-root"}:
        print(root)
        return 0
    runner = root / "tools" / "ismism.py"
    if not runner.is_file():
        print(f"ISMISM runner not found: {runner}", file=sys.stderr)
        return 2
    return subprocess.run([sys.executable, str(runner), *sys.argv[1:]], cwd=root).returncode


if __name__ == "__main__":
    raise SystemExit(main())
