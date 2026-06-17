#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
THEME=ROOT/'knowledge/themes/health-body-risk-society'
MAN=THEME/'health-body-risk-society-row-manifest.jsonl'
EV=THEME/'health-body-risk-society-evidence-bank.jsonl'
ALIASES={
 '身体':['身体','身体性','身体化','肉身','生理'],
 '医疗':['医疗','治疗','治愈','医学','医生','医院','药','卫生'],
 '健康':['健康','疾病','风险','症状','病理','病'],
 '疫情':['疫情','免疫','公共卫生','卫生'],
 '污名':['污名','疾病污名','脆弱','残疾','反常'],
 '身体治理':['身体治理','身体规训','身体管理','治理','规训','权力'],
}
def load(p): return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()]
def main():
    ap=argparse.ArgumentParser(description='Query Health / Body / Medicine / Risk Society theme evidence')
    ap.add_argument('query',nargs='?',default='身体')
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
        for e in evby.get(rid,[])[:3 if args.evidence else 2]: print(f"  {e['evidence_id']} [{e.get('quote_role')}]: {e.get('quote')[:260]}")
if __name__=='__main__': main()
