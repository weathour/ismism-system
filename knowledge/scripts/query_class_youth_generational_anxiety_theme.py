#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path('knowledge/themes/class-youth-generational-anxiety')
MANIFEST=ROOT/'class-youth-generational-anxiety-row-manifest.jsonl'
EVIDENCE=ROOT/'class-youth-generational-anxiety-evidence-bank.jsonl'
ALIASES={
 '阶层':['阶层','阶级','地位','流动','上升','固化'],
 '青年':['青年','年轻','学生','毕业','下一代','代际'],
 '中产焦虑':['中产','小布尔乔亚','焦虑','体面'],
 '底层羞辱':['底层','穷光棍','穷屌丝','穷人','羞辱','鄙视','歧视'],
 '成功学':['成功学','成功','失败','奋斗','竞争','内卷'],
 '贫富差异':['贫富','穷人','富人','收入','工资','贫民区'],
}
def load(path): return [json.loads(l) for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]
def main():
    ap=argparse.ArgumentParser(description='Query Class / Youth / Generation / Mobility Anxiety theme evidence')
    ap.add_argument('query', nargs='?', default='阶层')
    ap.add_argument('--limit', type=int, default=5)
    ap.add_argument('--row', type=int)
    ap.add_argument('--class', dest='klass')
    ap.add_argument('--evidence', action='store_true')
    args=ap.parse_args(); kws=ALIASES.get(args.query,[args.query])
    manifest=load(MANIFEST); evidence=load(EVIDENCE); evby={}
    for e in evidence: evby.setdefault(e['row_id'],[]).append(e)
    rows=[]
    for m in manifest:
        if args.row and m['row_id']!=args.row: continue
        if args.klass and m['theme_class']!=args.klass: continue
        blob=' '.join([str(m.get('row_id')),m.get('toc_id',''),m.get('title',''),m.get('theme_class',''),m.get('core_status',''),m.get('diagnostic_rationale',''),json.dumps(m.get('keyword_hits',{}),ensure_ascii=False)])
        ev_blob=' '.join(e['evidence_id']+' '+e.get('quote','')+' '+e.get('trigger_keyword','') for e in evby.get(m['row_id'],[]))
        if args.row or args.klass or any(k in blob or k in ev_blob for k in kws): rows.append(m)
    for m in rows[:args.limit]:
        print(f"row {m['row_id']} | {m.get('toc_id')} | {m['theme_class']} | {m['core_status']} | {m['title']}")
        print(f"  clean: {m['clean_md_path']}")
        for e in evby.get(m['row_id'],[])[:3 if args.evidence else 2]:
            print(f"  {e['evidence_id']} [{e['quote_role']}]: {e['quote'][:260]}")
if __name__=='__main__': main()
