#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path("library/themes/feminism")
ALIASES = {
    "女权": ["女权", "女性主义", "妇女", "夫权", "男权"],
    "厌女": ["厌女", "男权", "虚无主义"],
    "男权": ["男权", "父权", "夫权"],
    "女性本质": ["女性本质", "女性性", "femininity"],
    "性解放": ["性解放", "性倒错", "性压抑"],
    "爱欲": ["爱欲", "erotic", "Eros"],
    "爱情": ["爱情", "罗曼斯", "love"],
    "婚姻": ["婚姻", "婚事"],
    "家庭": ["家庭", "家族", "小孩"],
    "生殖": ["生殖", "生育", "传殖", "再生"],
    "社会再生产": ["社会再生产", "再生产", "家庭再生产", "人口再生产"],
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def build_terms(query: str) -> list[str]:
    if not query:
        return []
    return [query, *ALIASES.get(query, [])]


def row_matches(
    rec: dict[str, Any],
    ev_text: str,
    terms: list[str],
    row_filter: int | None,
    class_filter: str | None,
) -> bool:
    row = int(rec["row_id"])
    if row_filter is not None and row != row_filter:
        return False
    if class_filter and rec.get("theme_class") != class_filter:
        return False
    if not terms:
        return True
    haystack = " ".join(
        [
            str(rec.get("title", "")),
            str(rec.get("theme_class", "")),
            str(rec.get("theme_role", "")),
            json.dumps(rec.get("keyword_hits", {}), ensure_ascii=False),
        ]
    )
    return any(term and (term in haystack or term in ev_text) for term in terms)


def score_row(rec: dict[str, Any], ev_text: str, terms: list[str]) -> int:
    role = rec.get("theme_role")
    score = 25 if role == "core" else 10 if role == "bridge" else 0
    title = str(rec.get("title", ""))
    haystack = " ".join(
        [
            title,
            str(rec.get("theme_class", "")),
            str(rec.get("theme_role", "")),
            json.dumps(rec.get("keyword_hits", {}), ensure_ascii=False),
        ]
    )
    for term in terms:
        if term in title:
            score += 100
        if term in haystack:
            score += 30
        if term in ev_text:
            score += 20
    return score


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Query the ISMISM feminism/gender/sexuality/social-reproduction theme layer."
    )
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--row", type=int)
    parser.add_argument("--class", dest="theme_class")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)

    repo = Path(args.repo)
    manifest = load_jsonl(repo / ROOT / "feminism-row-manifest.jsonl")
    evidence = load_jsonl(repo / ROOT / "feminism-evidence-bank.jsonl")
    ev_by_row: dict[int, list[dict[str, Any]]] = {}
    for ev in evidence:
        ev_by_row.setdefault(int(ev["row_id"]), []).append(ev)

    terms = build_terms(args.query.strip())
    rows: list[tuple[int, dict[str, Any]]] = []
    for rec in manifest:
        row = int(rec["row_id"])
        ev_text = " ".join(str(ev.get("quote", "")) for ev in ev_by_row.get(row, []))
        if not row_matches(rec, ev_text, terms, args.row, args.theme_class):
            continue
        rows.append((score_row(rec, ev_text, terms), rec))

    rows.sort(key=lambda item: (-item[0], int(item[1]["row_id"])))
    for _score, rec in rows[: max(args.limit, 0)]:
        row = int(rec["row_id"])
        print(
            f"row {row} | {rec['toc_id']} | {rec['theme_class']} | "
            f"{rec['theme_role']} | {rec['title']}"
        )
        print(f"  clean: {rec['clean_md_path']}")
        for ev in ev_by_row.get(row, [])[:3]:
            print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not rows:
        print("No matching Feminism / Gender / Sexuality / Social Reproduction theme rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
