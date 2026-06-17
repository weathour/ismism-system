#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterator


def load_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def main() -> int:
    parser = argparse.ArgumentParser(description="Query Time-Death-Finitude-Life theme rows and exact quote evidence")
    parser.add_argument(
        "query",
        nargs="?",
        default="",
        help="keyword, row id, or theme label such as 时间/死亡/生命/永生/有限/AI可朽性/涅槃",
    )
    parser.add_argument("--repo", default=".")
    parser.add_argument("--row", type=int)
    parser.add_argument("--class", dest="theme_class")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    repo = Path(args.repo)
    root = repo / "knowledge/themes/time-death-finitude-life"
    manifest = list(load_jsonl(root / "time-death-row-manifest.jsonl"))
    evidence = list(load_jsonl(root / "time-death-evidence-bank.jsonl"))
    evidence_by_row: dict[int, list[dict[str, Any]]] = {}
    for item in evidence:
        evidence_by_row.setdefault(int(item["row_id"]), []).append(item)

    query = args.query.strip()
    aliases = {
        "时间": ["时间", "时刻", "历史时间", "实践时间", "Aion", "节庆"],
        "死亡": ["死亡", "死", "可朽性", "符号性死亡", "死亡恐惧"],
        "生命": ["生命", "生活", "身体", "自然生命", "技术生命", "拟生命"],
        "永生": ["永生", "不朽", "AI永生", "灵魂", "再生"],
        "有限": ["有限", "有限性", "可朽性", "有限主体", "衰老", "成熟"],
        "佛教": ["佛教", "业力", "轮回", "涅槃", "解脱", "阿赖耶", "唯识", "中观", "禅"],
        "AI可朽性": ["AI", "可朽性", "记忆", "再生", "身体化"],
        "涅槃": ["涅槃", "弃绝", "解脱", "中观", "轮回"],
    }
    terms = [query] + aliases.get(query, []) if query else []
    rows: list[tuple[int, dict[str, Any]]] = []
    for rec in manifest:
        row_id = int(rec["row_id"])
        if args.row is not None and row_id != args.row:
            continue
        if args.theme_class and rec.get("theme_class") != args.theme_class:
            continue
        haystack = " ".join(
            [
                str(row_id),
                rec.get("title", ""),
                str(rec.get("toc_id", "")),
                rec.get("theme_class", ""),
                rec.get("notes", ""),
                json.dumps(rec.get("keyword_hits", {}), ensure_ascii=False),
            ]
        )
        evidence_text = " ".join(ev.get("quote", "") for ev in evidence_by_row.get(row_id, []))
        if terms and not any(term in haystack or term in evidence_text for term in terms):
            continue
        score = 0
        for term in terms:
            if term in rec.get("title", ""):
                score += 100
            if term in haystack:
                score += 30
            if term in evidence_text:
                score += 20
        if rec.get("core_status") == "core":
            score += 25
        if 350 <= row_id <= 363:
            score += 20
        rows.append((score, rec))

    rows.sort(key=lambda item: (-item[0], int(item[1]["row_id"])))
    for _, rec in rows[: args.limit]:
        row_id = int(rec["row_id"])
        print(f"row {row_id} | {rec['toc_id']} | {rec['theme_class']} | {rec['core_status']} | {rec['title']}")
        print(f"  clean: {rec['clean_md_path']}")
        for ev in evidence_by_row.get(row_id, [])[:3]:
            print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not rows:
        print("No matching Time-Death-Finitude-Life theme rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
