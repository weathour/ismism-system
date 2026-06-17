#!/usr/bin/env python3
"""Validate position position-card drafts.

The validator supports partial position batches.  The current project knowledge contract route first
requires four L1 cards before the 16/64/256 lower layers are expanded.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_SECTIONS = [
    "## 矩阵坐标",
    "## 位置定义",
    "## 代表主义/学派",
    "## 核心机制",
    "## 与相邻位置的关系",
    "## 关联术语",
]
FORBIDDEN_PATTERNS = [
    r"人格障碍",
    r"人格类型",
    r"诊断标签",
    r"精神病人",
    r"患者",
    r"最终真理",
    r"万能解释器",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def chineseish_len(text: str) -> int:
    """Approximate Chinese card length by counting CJK chars and words."""
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin_words = len(re.findall(r"[A-Za-z][A-Za-z0-9_-]+", text))
    return cjk + latin_words


def section_text(text: str, section: str) -> str:
    start = text.find(section)
    if start < 0:
        return ""
    rest = text[start + len(section) :]
    m = re.search(r"\n## ", rest)
    return rest[: m.start()] if m else rest


def validate_card(path: Path, expected_level: int | None) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            fail(f"{path.relative_to(ROOT)} missing section {sec}")
    if expected_level is not None and f"level: {expected_level}" not in text:
        fail(f"{path.relative_to(ROOT)} does not declare level: {expected_level}")
    if "status: draft" not in text:
        fail(f"{path.relative_to(ROOT)} must remain status: draft")
    if not re.search(r"source_rows:\s*\[[0-9, ]+\]", text):
        fail(f"{path.relative_to(ROOT)} lacks source_rows")
    if not re.search(r"source_segments:\s*\[ismism:seg:[0-9, ism:seg:]*\]", text):
        fail(f"{path.relative_to(ROOT)} lacks source_segments")
    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, text):
            fail(f"{path.relative_to(ROOT)} contains forbidden wording matching {pat!r}")
    assoc = section_text(text, "## 关联术语")
    if "已收录" not in assoc:
        fail(f"{path.relative_to(ROOT)}关联术语 section must mark collected terms")
    length = chineseish_len(text)
    if expected_level == 1 and not (800 <= length <= 2500):
        fail(f"{path.relative_to(ROOT)} L1 approximate length out of range: {length}")
    return {"path": str(path.relative_to(ROOT)), "length": length}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(ROOT))
    ap.add_argument("--level", type=int, default=1)
    ap.add_argument("--expected-count", type=int, default=4)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    cards_dir = repo / "library/positions"
    if not cards_dir.exists():
        fail("library/positions does not exist")
    cards = sorted(p for p in cards_dir.glob("*.md") if p.name != "index.md")
    level_cards = []
    for p in cards:
        text = p.read_text(encoding="utf-8")
        if f"level: {args.level}" in text:
            level_cards.append(p)
    if len(level_cards) != args.expected_count:
        fail(f"expected {args.expected_count} level-{args.level} cards, got {len(level_cards)}")
    summaries = [validate_card(p, args.level) for p in level_cards]
    index = cards_dir / "index.md"
    if not index.exists():
        fail("library/positions/index.md missing")
    idx_text = index.read_text(encoding="utf-8")
    for p in level_cards:
        if f"library/positions/{p.name}" not in idx_text:
            fail(f"index.md does not list {p.name}")
    print(
        {
            "status": "PASS",
            "level": args.level,
            "count": len(level_cards),
            "cards": summaries,
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
