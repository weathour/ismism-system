#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

SLUG = "social-structure-production-reproduction"
PREFIX = "Social Structure / Production Relations / Reproduction / Institutional Production"


def load_jsonl(path: Path) -> list[dict]:
    records = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def main() -> int:
    ap = argparse.ArgumentParser(description=f"Query {PREFIX} theme rows and exact quote evidence")
    ap.add_argument("query", nargs="?", default="", help="keyword such as 生产关系/再生产/制度/阶级/城市/金融/消费/实践")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--row", type=int)
    ap.add_argument("--class", dest="theme_class")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    repo = Path(args.repo)
    theme = repo / "library/themes" / SLUG
    manifest = load_jsonl(theme / f"{SLUG}-row-manifest.jsonl")
    evidence = load_jsonl(theme / f"{SLUG}-evidence-bank.jsonl")
    ev_by_row: dict[int, list[dict]] = {}
    for ev in evidence:
        ev_by_row.setdefault(int(ev["row_id"]), []).append(ev)

    aliases = {
        "生产关系": ["生产关系", "生产活动", "生产过程", "生产力", "生产者"],
        "再生产": ["再生产", "社会再生产", "家庭", "妇女", "儿童", "照护", "生活必需品"],
        "制度": ["制度", "官僚", "国家机器", "合法性", "法权", "规则", "程序", "秩序"],
        "阶级": ["阶级", "阶层", "中产", "底层", "资产阶级", "无产阶级", "固化", "上升"],
        "空间": ["城市", "农村", "城乡", "住房", "迁移", "空间", "土地", "农业"],
        "教育": ["教育", "学校", "知识", "专家", "证书", "训练", "意识形态"],
        "金融": ["金融", "信用", "货币", "资本", "抽象", "代理"],
        "消费": ["消费", "市场", "商品", "生活方式", "必需品", "享乐"],
        "实践": ["实践", "解放", "社会化", "组织经济生活", "替代"],
    }
    q = args.query.strip()
    terms = [q] + aliases.get(q, []) if q else []
    rows = []
    for rec in manifest:
        if args.row is not None and int(rec["row_id"]) != args.row:
            continue
        if args.theme_class and rec.get("theme_class") != args.theme_class:
            continue
        hay = " ".join([
            rec.get("title", ""),
            rec.get("theme_class", ""),
            rec.get("core_status", ""),
            rec.get("diagnostic_rationale", ""),
            json.dumps(rec.get("keyword_hits", {}), ensure_ascii=False),
        ])
        ev_text = " ".join(ev.get("quote", "") for ev in ev_by_row.get(int(rec["row_id"]), []))
        if terms and not any(t and (t in hay or t in ev_text) for t in terms):
            continue
        score = 0
        for t in terms:
            if not t:
                continue
            if t in rec.get("title", ""):
                score += 100
            if t in hay:
                score += 30
            if t in ev_text:
                score += 20
        if rec.get("core_status") == "core":
            score += 25
        elif rec.get("core_status") == "bridge":
            score += 10
        rows.append((score, rec))

    rows.sort(key=lambda item: (-item[0], int(item[1]["row_id"])))
    for _, rec in rows[: args.limit]:
        print(f"row {rec['row_id']} | {rec['toc_id']} | {rec['theme_class']} | {rec['core_status']} | {rec['title']}")
        print(f"  clean: {rec['clean_md_path']}")
        for ev in ev_by_row.get(int(rec["row_id"]), [])[:3]:
            print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not rows:
        print("No matching Social Structure / Production Relations / Reproduction theme rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
