#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path('knowledge/themes/consumption-desire-lifestyle')
MANIFEST=ROOT/'consumption-desire-lifestyle-row-manifest.jsonl'
EVIDENCE=ROOT/'consumption-desire-lifestyle-evidence-bank.jsonl'

def load_jsonl(path:Path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def main():
    ap=argparse.ArgumentParser(description='Query Consumption / Desire / Commodity / Lifestyle theme evidence')
    ap.add_argument('query', help='keyword, row id, theme class, role, or evidence id')
    ap.add_argument('--limit', type=int, default=10)
    args=ap.parse_args()
    q=args.query.strip()
    manifest=load_jsonl(MANIFEST); evidence=load_jsonl(EVIDENCE)
    byrow={r['row_id']:r for r in manifest}; evby={}
    for ev in evidence: evby.setdefault(ev['row_id'],[]).append(ev)
    hits=[]
    for r in manifest:
        blob=' '.join(str(r.get(k,'')) for k in ['row_id','toc_id','title','theme_class','core_status','diagnostic_rationale'])+' '+json.dumps(r.get('keyword_hits',{}),ensure_ascii=False)
        row_evs=evby.get(r['row_id'],[])
        ev_blob=' '.join(ev['evidence_id']+' '+ev.get('quote','')+' '+ev.get('trigger_keyword','')+' '+ev.get('quote_role','') for ev in row_evs)
        if q==str(r['row_id']) or q in blob or q in ev_blob:
            hits.append(r)
    for r in hits[:args.limit]:
        print(f"row {r['row_id']} | {r.get('toc_id')} | {r['theme_class']} | {r['core_status']} | {r['title']}")
        print(f"  clean: {r['clean_md_path']}")
        for ev in evby.get(r['row_id'],[])[:3]:
            print(f"  {ev['evidence_id']} [{ev['quote_role']}]: {ev['quote'][:220]}")
    if not hits:
        for ev in evidence[:args.limit]:
            if q in ev['evidence_id'] or q in ev['quote'] or q in ev.get('trigger_keyword',''):
                r=byrow[ev['row_id']]
                print(f"{ev['evidence_id']} row {ev['row_id']} {r['title']} [{ev['quote_role']}]: {ev['quote'][:260]}")
if __name__=='__main__': main()
