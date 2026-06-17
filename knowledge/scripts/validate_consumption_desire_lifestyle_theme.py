#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess,sys
from pathlib import Path
from typing import Any
ROOT=Path('knowledge/themes/consumption-desire-lifestyle')
MANIFEST=ROOT/'consumption-desire-lifestyle-row-manifest.jsonl'
EVIDENCE=ROOT/'consumption-desire-lifestyle-evidence-bank.jsonl'
W3_BATCH='W3-CONSUMPTION-DESIRE-LIFESTYLE-2026-06-16'
W5_BATCH='W5-CONSUMPTION-DESIRE-LIFESTYLE-2026-06-16'
FORBIDDEN=('人格障碍','人格类型','诊断标签','精神病人','患者','最终真理','万能解释器')
REQ_M={'schema_version','row_id','segment_id','toc_id','title','clean_md_path','field','char_count','keyword_hits','theme_class','core_status','current_absorption','recommended_action','evidence_quote_count','diagnostic_rationale'}
REQ_E={'schema_version','evidence_id','row_id','segment_id','toc_id','clean_md_path','quote','theme_tags','quote_role','trigger_keyword','diagnostic_slot'}
CLASSES={'consumerism-enjoyment-quantification','commodity-fetishism-objectification','market-money-exchange-carrier','lifestyle-luxury-identity-display','emotional-consumption-affect-management','advertising-marketing-consumer-engineering','desire-enjoyment-subjectivation-bridge','capitalism-production-consumption-bridge','necessity-luxury-social-reproduction-bridge','excluded-keyword-only'}
ROLES={'core','bridge','context','excluded'}
QUOTE_ROLES={'phenomenon-name','subject-position','mechanism','fantasy-misrecognition','institution-carrier','contradiction','practice-opening','cross-theme-bridge','boundary-exclusion'}
REL_TYPES={'boundary-between','route-from-to','tension-between','mediates-between','transitions-to','blocks-transition','misrecognizes-as','objectifies','subjectivizes','overcodes','represents-position','evidences-claim'}
SYNTHESIS_FILES=[
 ROOT/'consumption-desire-lifestyle-synthesis.md',
 ROOT/'commodity-fetishism-and-market-enjoyment-synthesis.md',
 ROOT/'emotional-identity-lifestyle-consumption-synthesis.md',
]
def load_jsonl(path:Path):
    out=[]
    with path.open(encoding='utf-8') as f:
        for i,line in enumerate(f,1):
            if not line.strip(): continue
            try: out.append(json.loads(line))
            except json.JSONDecodeError as exc: out.append({'__error__':f'{i}:{exc}'})
    return out
def add(errors:list[str],msg:str): errors.append(msg)
def load_segments(repo:Path):
    return {int(r['row_id']):r for r in load_jsonl(repo/'knowledge/manifests/segments.jsonl') if '__error__' not in r}
def validate_manifest_evidence(repo:Path, segments:dict[int,dict[str,Any]], errors:list[str]):
    manifest=load_jsonl(repo/MANIFEST); evidence=load_jsonl(repo/EVIDENCE)
    rows={}; ev_ids=set(); ev_by_row={}
    for i,r in enumerate(manifest,1):
        if '__error__' in r: add(errors,f'manifest parse {r["__error__"]}'); continue
        miss=REQ_M-set(r)
        if miss: add(errors,f'manifest:{i} missing {sorted(miss)}')
        rid=int(r.get('row_id',-1)); rows[rid]=r
        seg=segments.get(rid)
        if not seg: add(errors,f'manifest row {rid} missing segment'); continue
        if r.get('segment_id')!=seg.get('segment_id'): add(errors,f'row {rid} segment mismatch')
        if r.get('clean_md_path')!=seg['source_paths']['clean_md_relpath']: add(errors,f'row {rid} clean path mismatch')
        if int(r.get('char_count',-1))!=int(seg['clean_md']['char_count']): add(errors,f'row {rid} char_count mismatch')
        if r.get('theme_class') not in CLASSES: add(errors,f'row {rid} bad class {r.get("theme_class")}')
        if r.get('core_status') not in ROLES: add(errors,f'row {rid} bad role {r.get("core_status")}')
    for i,ev in enumerate(evidence,1):
        if '__error__' in ev: add(errors,f'evidence parse {ev["__error__"]}'); continue
        miss=REQ_E-set(ev)
        if miss: add(errors,f'evidence:{i} missing {sorted(miss)}')
        eid=str(ev.get('evidence_id','')); rid=int(ev.get('row_id',-1)); ev_by_row.setdefault(rid,[]).append(ev)
        if not re.fullmatch(r'ev:consumption:\d{4}:\d{2}',eid): add(errors,f'bad evidence id {eid}')
        if eid in ev_ids: add(errors,f'duplicate evidence {eid}')
        ev_ids.add(eid)
        if rid not in rows: add(errors,f'{eid} row not in manifest')
        seg=segments.get(rid)
        if not seg: continue
        if ev.get('segment_id')!=seg.get('segment_id'): add(errors,f'{eid} segment mismatch')
        if ev.get('clean_md_path')!=seg['source_paths']['clean_md_relpath']: add(errors,f'{eid} clean path mismatch')
        if ev.get('quote_role') not in QUOTE_ROLES: add(errors,f'{eid} bad quote_role {ev.get("quote_role")}')
        q=str(ev.get('quote','')).strip(); text=(repo/seg['source_paths']['clean_md_relpath']).read_text(encoding='utf-8')
        if not q or q not in text: add(errors,f'{eid} quote_not_found')
        if any(p in q for p in FORBIDDEN): add(errors,f'{eid} forbidden pattern in quote')
    if len(manifest)!=93: add(errors,f'manifest rows {len(manifest)} != 93')
    if len(evidence)!=223: add(errors,f'evidence {len(evidence)} != 223')
    for rid,r in rows.items():
        cnt=len(ev_by_row.get(rid,[]))
        if cnt != int(r.get('evidence_quote_count',-1)): add(errors,f'row {rid} evidence count mismatch')
        if r.get('core_status')=='core' and cnt<2: add(errors,f'core row {rid} too few quotes')
        if r.get('core_status')=='bridge' and cnt<1: add(errors,f'bridge row {rid} too few quotes')
        if r.get('core_status')=='excluded' and any(ev.get('quote_role')!='boundary-exclusion' for ev in ev_by_row.get(rid,[])): add(errors,f'excluded row {rid} non-boundary quote')
    return rows, ev_by_row
def validate_w3_w5_w10(repo:Path, rows:dict[int,dict[str,Any]], errors:list[str]):
    segments=load_segments(repo)
    w3=[r for r in load_jsonl(repo/'knowledge/lexicon/term-senses.jsonl') if r.get('batch_id')==W3_BATCH]
    w5=[r for r in load_jsonl(repo/'knowledge/relations/relation-assets.jsonl') if r.get('batch_id')==W5_BATCH]
    if len(w3)!=45: add(errors,f'W3 count {len(w3)} != 45')
    if len(w5)!=40: add(errors,f'W5 count {len(w5)} != 40')
    for rec in w3:
        if rec.get('status')!='draft': add(errors,f'W3 non-draft {rec.get("sense_id")}')
        for q in rec.get('evidence_quotes') or []:
            rid=int(q.get('row_id')); quote=str(q.get('quote','')).strip()
            if rid not in rows: add(errors,f'W3 quote row outside manifest {rid}')
            if quote not in (repo/segments[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W3 quote not found {rec.get("sense_id")}')
    types=set()
    for rec in w5:
        types.add(rec.get('relation_type'))
        if rec.get('status')!='draft': add(errors,f'W5 non-draft {rec.get("relation_id")}')
        for ev in rec.get('evidence_segment') or []:
            rid=int(ev.get('row_id')); quote=str(ev.get('quote','')).strip()
            if rid not in rows: add(errors,f'W5 evidence outside manifest {rid}')
            if quote not in (repo/segments[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W5 quote not found {rec.get("relation_id")}')
    if types!=REL_TYPES: add(errors, f'W5 relation type coverage mismatch {sorted(REL_TYPES-types)}')
    cards=[]
    for p in (repo/'knowledge/w10-absorption').glob('*-cards/*.md'):
        text=p.read_text(encoding='utf-8')
        if 'Consumption / Desire / Commodity / Lifestyle 社会现象层' in text:
            cards.append(p)
    if len(cards)!=30: add(errors,f'Consumption W10 cards {len(cards)} != 30')
    idx=(repo/'knowledge/w10-absorption/index.md').read_text(encoding='utf-8')
    for p in cards:
        rel=p.relative_to(repo).as_posix()
        text=p.read_text(encoding='utf-8')
        if rel not in idx: add(errors,f'W10 index missing {rel}')
        if 'status: pilot-draft' not in text: add(errors,f'W10 not pilot-draft {rel}')
        if any(f in text for f in FORBIDDEN): add(errors,f'W10 forbidden pattern {rel}')
def validate_docs(repo:Path, errors:list[str], final:bool):
    for p in [ROOT/'README.md', ROOT/'consumption-desire-lifestyle-taxonomy.md', ROOT/'consumption-desire-lifestyle-w3-w5-batch-notes.md', ROOT/'CONSUMPTION-DESIRE-LIFESTYLE-MAXIMUM-ABSORPTION-HANDOFF.md', Path('knowledge/scripts/query_consumption_desire_lifestyle_theme.py')]+SYNTHESIS_FILES:
        if not (repo/p).exists(): add(errors,f'missing {p}')
    if not final: return
    current='Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.'
    markers={
        Path('README.md'): ['Consumption / Desire / Commodity / Lifestyle maximum absorption', current],
        Path('knowledge/README.md'): ['consumption-desire-lifestyle', 'Current latest checkpoint — Health / Body / Medicine / Risk Society'],
        Path('knowledge/STATE.md'): ['current_phase: Health / Body / Medicine / Risk Society maximum absorption', '--min-count 1044'],
        Path('ISMISM-MAINLINE-HANDOFF.md'): ['Consumption / Desire / Commodity / Lifestyle maximum absorption', 'W3 1676/1228'],
        Path('DIRECTORY_MAP.md'): ['knowledge/themes/consumption-desire-lifestyle/', 'validate_consumption_desire_lifestyle_theme.py'],
        Path('AGENTS.md'): ['knowledge/themes/consumption-desire-lifestyle/README.md', 'Consumption / Desire / Commodity / Lifestyle'],
        Path('skills/ismism-knowledge-operator/SKILL.md'): ['query_consumption_desire_lifestyle_theme.py', '--min-count 1044'],
        Path('knowledge/query-playbook.md'): ['query_consumption_desire_lifestyle_theme.py', '消费 / 消费主义 / 欲望 / 商品 / 生活方式'],
        Path('knowledge/qa/absorption-strength-distribution.md'): ['W5 relation absorption covers 301 rows', 'Full W3+W5+W10 row overlap is now 277 rows'],
        ROOT/'README.md': ['validate_consumption_desire_lifestyle_theme.py', 'query_consumption_desire_lifestyle_theme.py'],
    }
    for rel,vals in markers.items():
        path=repo/rel
        if not path.exists(): add(errors,f'missing doc {rel}'); continue
        text=path.read_text(encoding='utf-8')
        for marker in vals:
            if marker not in text: add(errors,f'{rel} missing marker {marker!r}')
def validate_protected(repo:Path, errors:list[str]):
    diff=subprocess.run(['git','diff','--name-only','--','split_md','split_md_clean'],cwd=repo,text=True,capture_output=True)
    if diff.stdout.strip(): add(errors,'protected corpus diff: '+diff.stdout.strip())
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--final',action='store_true')
    args=ap.parse_args(); repo=Path(args.repo).resolve(); errors=[]
    segments=load_segments(repo); rows,_=validate_manifest_evidence(repo,segments,errors)
    validate_w3_w5_w10(repo,rows,errors); validate_docs(repo,errors,args.final); validate_protected(repo,errors)
    print(f"validate_consumption_desire_lifestyle_theme: {'PASS' if not errors else 'FAIL'} manifest={len(rows)} evidence={len(load_jsonl(repo/EVIDENCE)) if (repo/EVIDENCE).exists() else 0} w3=45 w5=40 w10=30 errors={len(errors)}")
    for e in errors[:100]: print('ERROR',e)
    return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
