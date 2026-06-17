#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from theme_validation import main
if __name__ == "__main__":
    raise SystemExit(main("religion", sys.argv[1:]))
