#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from field3_theme_validation import main
ALLOWED_CLASSES = ['semiotics-overview-review', 'structuralist-sign-system', 'poststructuralist-discourse-text', 'dialectics-of-difference', 'hermeneutics-understanding', 'semiotics-language-bridge', 'excluded-keyword-only']
if __name__ == "__main__":
    raise SystemExit(main("semiotics-language-hermeneutics", ALLOWED_CLASSES, sys.argv[1:]))
