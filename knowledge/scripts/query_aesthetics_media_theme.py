#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
ROOT=Path("knowledge/themes/aesthetics-media")
ALIASES={
  "电影":["电影","影片","影院","好莱坞","科幻"],
  "影像":["影像","图像","视觉","观看","凝视","镜头"],
  "美学":["美学","审美","唯美","艺术","景观"],
  "艺术":["艺术","诗","诗性","文学","文艺","音乐"],
  "叙事":["叙事","故事","小说","虚构","主角","主人公"],
  "媒介":["媒介","媒体","电影产业","电视","报纸","视觉产品"],
  "文本":["文本","修辞","解释学","语言游戏","符号"],
}
def load_jsonl(path:Path)->list[dict[str,Any]]:
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def terms(q:str)->list[str]: return [q,*ALIASES.get(q,[])] if q else []
def main(argv=None)->int:
    ap=argparse.ArgumentParser(description='Query the ISMISM Aesthetics / Art / Media / Image / Narrative theme layer.')
    ap.add_argument('query',nargs='?',default=''); ap.add_argument('--repo',default='.'); ap.add_argument('--row',type=int); ap.add_argument('--class',dest='theme_class'); ap.add_argument('--limit',type=int,default=10)
    args=ap.parse_args(argv); repo=Path(args.repo)
    manifest=load_jsonl(repo/ROOT/'aesthetics-media-row-manifest.jsonl'); evidence=load_jsonl(repo/ROOT/'aesthetics-media-evidence-bank.jsonl')
    ev_by_row={}
    for ev in evidence: ev_by_row.setdefault(int(ev['row_id']),[]).append(ev)
    ts=terms(args.query.strip()); out=[]
    for rec in manifest:
        row=int(rec['row_id']); ev_text=' '.join(ev['quote'] for ev in ev_by_row.get(row,[]))
        if args.row is not None and row!=args.row: continue
        if args.theme_class and rec.get('theme_class')!=args.theme_class: continue
        hay=' '.join([rec.get('title',''),rec.get('theme_class',''),rec.get('theme_role',''),json.dumps(rec.get('keyword_hits',{}),ensure_ascii=False),ev_text])
        if ts and not any(t and t in hay for t in ts): continue
        score=(30 if rec.get('theme_role')=='core' else 15 if rec.get('theme_role')=='bridge' else 3)+sum(50 for t in ts if t and t in rec.get('title',''))+sum(10 for t in ts if t and t in ev_text)
        out.append((score,row,rec))
    out.sort(key=lambda x:(-x[0],x[1]))
    for _,row,rec in out[:max(args.limit,0)]:
        print(f"row {row} | {rec['toc_id']} | {rec['theme_class']} | {rec['theme_role']} | {rec['title']}")
        print(f"  clean: {rec['clean_md_path']}")
        for ev in ev_by_row.get(row,[])[:3]: print(f"  {ev['evidence_id']}: {ev['quote']}")
    if not out: print('No matching Aesthetics / Art / Media / Image / Narrative theme rows.')
    return 0
if __name__=='__main__': raise SystemExit(main())
