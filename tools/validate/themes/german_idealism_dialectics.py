#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from field3_theme_validation import main
ALLOWED_CLASSES = ['idealism-overview-review', 'critical-philosophy-limits', 'science-of-knowledge-self-positing', 'system-freedom-schelling', 'dialectic-negativity-hegel', 'idealism-dialectics-bridge', 'excluded-keyword-only']
if __name__ == "__main__":
    raise SystemExit(main("german-idealism-dialectics", ALLOWED_CLASSES, sys.argv[1:]))
