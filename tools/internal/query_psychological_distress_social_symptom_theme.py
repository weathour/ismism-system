#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
THEME=ROOT/'library/themes/psychological-distress-social-symptom'
MAN=THEME/'psychological-distress-social-symptom-row-manifest.jsonl'
EV=THEME/'psychological-distress-social-symptom-evidence-bank.jsonl'
def load(p): return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()]
def main():
    ap=argparse.ArgumentParser(description='Query Psychological Distress / Anxiety / Addiction / Social Symptom theme evidence')
    ap.add_argument('query',nargs='?',default='')
    ap.add_argument('--row',type=int)
    ap.add_argument('--class',dest='klass')
    ap.add_argument('--limit',type=int,default=5)
    args=ap.parse_args(); man=load(MAN); ev=load(EV); evby={}
    for e in ev: evby.setdefault(int(e['row_id']),[]).append(e)
    rows=[]
    for r in man:
        hay=' '.join([str(r.get('row_id')),r.get('title',''),r.get('theme_class',''),r.get('core_status',''),' '.join(r.get('keyword_hits',{}).keys()),r.get('diagnostic_rationale','')])
        if args.row and int(r['row_id'])!=args.row: continue
        if args.klass and r.get('theme_class')!=args.klass: continue
        if args.query and args.query not in hay and not any(args.query in e.get('quote','') for e in evby.get(int(r['row_id']),[])): continue
        rows.append(r)
    for r in rows[:args.limit]:
        rid=int(r['row_id'])
        print(f"row {rid} | {r.get('toc_id')} | {r.get('theme_class')} | {r.get('core_status')} | {r.get('title')}")
        print(f"  clean: {r.get('clean_md_path')}")
        for e in evby.get(rid,[])[:3]: print(f"  {e['evidence_id']} [{e.get('quote_role')}]: {e.get('quote')}")
if __name__=='__main__': main()
