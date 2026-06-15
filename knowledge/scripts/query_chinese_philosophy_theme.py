#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
THEME = ROOT / 'knowledge/themes/chinese-philosophy'

def load_jsonl(path):
    with path.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def main():
    ap = argparse.ArgumentParser(description='Query Chinese Philosophy theme rows and quotes')
    ap.add_argument('query', nargs='?', help='keyword to search in title, class, notes, or quotes')
    ap.add_argument('--row', type=int)
    ap.add_argument('--class', dest='theme_class')
    ap.add_argument('--limit', type=int, default=10)
    args = ap.parse_args()
    manifest = list(load_jsonl(THEME/'chinese-philosophy-row-manifest.jsonl'))
    evidence = list(load_jsonl(THEME/'chinese-philosophy-evidence-bank.jsonl'))
    ev_by_row = {}
    for ev in evidence:
        ev_by_row.setdefault(ev['row_id'], []).append(ev)
    rows = []
    for rec in manifest:
        if args.row is not None and rec['row_id'] != args.row:
            continue
        if args.theme_class and rec['theme_class'] != args.theme_class:
            continue
        if args.query:
            keyword_hits = rec.get('keyword_hits') or {}
            hay = '\n'.join(
                [
                    rec.get('title',''),
                    rec.get('theme_class',''),
                    rec.get('recommended_action',''),
                    rec.get('notes',''),
                    ' '.join(str(k) for k in keyword_hits),
                ]
                + [e.get('quote','') for e in ev_by_row.get(rec['row_id'], [])]
            )
            if args.query not in hay:
                continue
        rows.append(rec)
    for rec in rows[:args.limit]:
        print(f"row {rec['row_id']} | {rec['toc_id']} | {rec['theme_class']} | {rec['title']}")
        print(f"  clean: {rec['clean_md_path']}")
        for ev in ev_by_row.get(rec['row_id'], [])[:3]:
            print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not rows:
        print('No matching Chinese philosophy theme rows.')

if __name__ == '__main__':
    main()
