#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path


def load_jsonl(path: Path):
    with path.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def main():
    ap = argparse.ArgumentParser(description='Query Religion Problem theme rows and exact quote evidence')
    ap.add_argument('query', nargs='?', default='', help='keyword, row id, or theme label such as 宗教/偶像/神爱/涅槃')
    ap.add_argument('--repo', default='.')
    ap.add_argument('--row', type=int)
    ap.add_argument('--class', dest='theme_class')
    ap.add_argument('--limit', type=int, default=10)
    args = ap.parse_args()
    repo=Path(args.repo)
    theme=repo/'knowledge/themes/religion'
    manifest=list(load_jsonl(theme/'religion-row-manifest.jsonl'))
    evidence=list(load_jsonl(theme/'religion-evidence-bank.jsonl'))
    ev_by_row={}
    for ev in evidence:
        ev_by_row.setdefault(ev['row_id'],[]).append(ev)
    q=args.query.strip()
    aliases={
        '宗教':['宗教','宗教实在论','cosmos','神圣','信仰'],
        '偶像':['偶像','崇拜','拜物','物神','神圣现象'],
        '神爱':['神爱','大他者','true love','真爱'],
        '涅槃':['涅槃','解脱','佛教','中观','禅'],
        '意识形态':['意识形态','教条','纪律','组织'],
    }
    terms=[q]+aliases.get(q,[]) if q else []
    rows=[]
    for rec in manifest:
        if args.row is not None and rec['row_id'] != args.row:
            continue
        if args.theme_class and rec.get('theme_class') != args.theme_class:
            continue
        hay=' '.join([str(rec.get('row_id')),rec.get('title',''),rec.get('toc_id',''),rec.get('theme_class',''),rec.get('notes',''),json.dumps(rec.get('keyword_hits',{}),ensure_ascii=False)])
        ev_text=' '.join(ev.get('quote','') for ev in ev_by_row.get(rec['row_id'],[]))
        if terms and not any(t in hay or t in ev_text for t in terms):
            continue
        score=0
        for t in terms:
            if t in rec.get('title',''): score+=100
            if t in hay: score+=30
            if t in ev_text: score+=20
        if rec.get('core_status')=='core': score+=25
        rows.append((score,rec))
    rows.sort(key=lambda x:(-x[0], x[1]['row_id']))
    for _,rec in rows[:args.limit]:
        print(f"row {rec['row_id']} | {rec['toc_id']} | {rec['theme_class']} | {rec['title']}")
        print(f"  clean: {rec['clean_md_path']}")
        for ev in ev_by_row.get(rec['row_id'],[])[:3]:
            print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not rows:
        print('No matching Religion Problem theme rows.')

if __name__ == '__main__':
    main()
