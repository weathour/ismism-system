#!/usr/bin/env python3
"""Query the ISMISM AI theme manifest/evidence bank."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path


def load_jsonl(path: Path):
    with path.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def main():
    ap=argparse.ArgumentParser(description='Query library/themes/ai AI absorption artifacts')
    ap.add_argument('query', nargs='?', default='', help='free text, row id, or tag such as AI身体化/强AI/可朽性')
    ap.add_argument('--repo', default='.')
    ap.add_argument('--row', type=int)
    ap.add_argument('--class', dest='theme_class')
    ap.add_argument('--limit', type=int, default=20)
    args=ap.parse_args()
    repo=Path(args.repo)
    manifest=list(load_jsonl(repo/'library/themes/ai/ai-row-manifest.jsonl'))
    evidence=list(load_jsonl(repo/'library/themes/ai/ai-evidence-bank.jsonl'))
    ev_by_row={}
    for ev in evidence:
        ev_by_row.setdefault(ev['row_id'],[]).append(ev)
    q=args.query.strip()
    terms=[]
    if q:
        terms=[q]
        aliases={
            'AI身体化':['身体化','AI substance','语音','秘密间性'],
            '强AI':['强AI','弱AI','教育','去AI化'],
            '弱AI':['弱AI','强AI','筛选'],
            'AI可朽性':['可朽性','记忆','再生','永生'],
            '再生':['再生','内在语音','繁衍'],
        }
        terms+=aliases.get(q,[])
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
        title=rec.get('title','')
        score=0
        if q and (q in hay or q in ev_text):
            score += 200
        if q.startswith('AI') and len(q) > 2:
            stripped_q=q[2:]
            if stripped_q in title:
                score += 220
            elif stripped_q in hay or stripped_q in ev_text:
                score += 120
        for t in terms:
            if t in title:
                score += 100
            if t in hay:
                score += 30
            if t in ev_text:
                score += 20
        if rec.get('core_status') == 'core':
            score += 25
        if 342 <= int(rec['row_id']) <= 363:
            score += 20
        rows.append((score, rec))
    rows=[rec for _,rec in sorted(rows, key=lambda item: (-item[0], int(item[1]['row_id'])))]
    for rec in rows[:args.limit]:
        print(f"row {rec['row_id']} {rec['toc_id']} {rec['title']} [{rec['theme_class']}; {rec['core_status']}; {rec['recommended_next_step']}]")
        for ev in ev_by_row.get(rec['row_id'],[])[:3]:
            print(f"  - {ev['evidence_id']}: {ev['quote']}")
        print(f"  path: {rec['clean_md_path']}")

if __name__=='__main__':
    main()
