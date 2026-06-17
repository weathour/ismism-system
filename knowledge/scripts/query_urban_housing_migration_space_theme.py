#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
THEME=ROOT/'knowledge/themes/urban-housing-migration-space'
MAN=THEME/'urban-housing-migration-space-row-manifest.jsonl'
EV=THEME/'urban-housing-migration-space-evidence-bank.jsonl'
ALIASES={
 '城市':['城市','都市','城镇','公共空间','城市空间'],
 '住房':['住房','房子','买房','居住','居所','租房','房价'],
 '迁徙':['迁徙','迁移','漂泊','城市漂泊','流动'],
 '城乡':['城乡','农村','乡村','城镇','土地'],
 '空间阶层化':['空间阶层化','空间','空间化','阶层','资本','土地'],
 '公共空间':['公共空间','公共','场所','地方'],
}
def load(p): return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()]
def main():
    ap=argparse.ArgumentParser(description='Query Urban / Housing / Migration / Space theme evidence')
    ap.add_argument('query',nargs='?',default='城市')
    ap.add_argument('--limit',type=int,default=5)
    ap.add_argument('--row',type=int)
    ap.add_argument('--class',dest='klass')
    ap.add_argument('--evidence',action='store_true')
    args=ap.parse_args(); kws=ALIASES.get(args.query,[args.query])
    man=load(MAN); ev=load(EV); evby={}
    for e in ev: evby.setdefault(int(e['row_id']),[]).append(e)
    rows=[]
    for m in man:
        rid=int(m['row_id'])
        if args.row and rid!=args.row: continue
        if args.klass and m.get('theme_class')!=args.klass: continue
        blob=' '.join([str(rid),str(m.get('toc_id')),m.get('title',''),m.get('theme_class',''),m.get('core_status',''),m.get('diagnostic_rationale',''),json.dumps(m.get('keyword_hits',{}),ensure_ascii=False)])
        ev_blob=' '.join(e['evidence_id']+' '+e.get('quote','')+' '+e.get('trigger_keyword','') for e in evby.get(rid,[]))
        if args.row or args.klass or any(k in blob or k in ev_blob for k in kws): rows.append(m)
    for m in rows[:args.limit]:
        rid=int(m['row_id'])
        print(f"row {rid} | {m.get('toc_id')} | {m.get('theme_class')} | {m.get('core_status')} | {m.get('title')}")
        print(f"  clean: {m.get('clean_md_path')}")
        for e in evby.get(rid,[])[:3 if args.evidence else 2]:
            print(f"  {e['evidence_id']} [{e.get('quote_role')}]: {e.get('quote')[:260]}")
if __name__=='__main__': main()
