#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
TDIR=ROOT/'library/themes/labor-workplace-precarity'
MANIFEST=TDIR/'labor-workplace-precarity-row-manifest.jsonl'
EVIDENCE=TDIR/'labor-workplace-precarity-evidence-bank.jsonl'
ALIASES={
    '内卷':['内卷','劳动','工作','指标','绩效','等级制','焦虑'],
    '打工人':['打工','劳动者','工作','工人','劳动','职业'],
    '加班':['加班','劳动时间','工作','时间'],
    '绩效':['绩效','指标','定价','等级制','考核'],
    '失业焦虑':['失业','就业','焦虑','不稳定','机会'],
    '劳动异化':['劳动','异化','物化','商品化'],
    '生产关系':['生产关系','生产力','生产过程','生产活动'],
    '工人':['工人','无产阶级','劳动者','阶级'],
}

def load(path):
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]

def main():
    ap=argparse.ArgumentParser(description='Query Labor / Workplace / Precarity theme evidence.')
    ap.add_argument('query', nargs='?', default='劳动')
    ap.add_argument('--limit', type=int, default=5)
    ap.add_argument('--row', type=int)
    ap.add_argument('--class', dest='klass')
    ap.add_argument('--evidence', action='store_true')
    args=ap.parse_args()
    manifest=load(MANIFEST); evidence=load(EVIDENCE)
    kws=ALIASES.get(args.query, [args.query])
    rows=[]
    for m in manifest:
        if args.row and m['row_id']!=args.row: continue
        if args.klass and m['theme_class']!=args.klass: continue
        blob=' '.join([m.get('title',''),m.get('theme_class',''),m.get('core_status',''),json.dumps(m.get('keyword_hits',{}),ensure_ascii=False)])
        if args.row or args.klass or any(k in blob for k in kws): rows.append(m)
    rows=rows[:args.limit]
    ev_by_row={}
    for e in evidence: ev_by_row.setdefault(e['row_id'],[]).append(e)
    for m in rows:
        print(f"row {m['row_id']} | {m.get('toc_id')} | {m['theme_class']} | {m['core_status']} | {m['title']}")
        print(f"  clean: {m['clean_md_path']}")
        for e in ev_by_row.get(m['row_id'],[])[:3 if args.evidence else 2]:
            print(f"  {e['evidence_id']} [{e['quote_role']}]: {e['quote'][:260]}")
if __name__=='__main__': main()
