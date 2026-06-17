#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path
from typing import Any
ROOT=Path('knowledge/themes/education-examination-credentialism')
MANIFEST=ROOT/'education-examination-credentialism-row-manifest.jsonl'
EVIDENCE=ROOT/'education-examination-credentialism-evidence-bank.jsonl'
W3_BATCH='W3-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16'
W5_BATCH='W5-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16'
FORBIDDEN=('人格障碍','人格类型','诊断标签','精神病人','患者','最终真理','万能解释器')
REQ_M={'schema_version','row_id','segment_id','toc_id','title','clean_md_path','field','char_count','keyword_hits','theme_class','core_status','current_absorption','recommended_action','evidence_quote_count','diagnostic_rationale'}
REQ_E={'schema_version','evidence_id','row_id','segment_id','toc_id','clean_md_path','quote','theme_tags','quote_role','trigger_keyword','diagnostic_slot'}
CLASSES={'exam-credential-sorting','knowledge-discipline-indoctrination','school-discipline-training','academic-hierarchy-expert-authority','knowledge-production-authority','student-learning-subjectivation','education-workforce-labor-bridge','class-family-reproduction-education','excluded-keyword-only'}
ROLES={'core','bridge','context','excluded'}

def load_jsonl(path:Path):
    out=[]
    with path.open(encoding='utf-8') as f:
        for i,line in enumerate(f,1):
            if not line.strip(): continue
            try: out.append(json.loads(line))
            except json.JSONDecodeError as exc: out.append({'__error__':f'{i}:{exc}'})
    return out

def add(errors,msg): errors.append(msg)

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
        if not re.fullmatch(r'ev:edu:\d{4}:\d{2}',eid): add(errors,f'bad evidence id {eid}')
        if eid in ev_ids: add(errors,f'duplicate evidence {eid}')
        ev_ids.add(eid)
        if rid not in rows: add(errors,f'{eid} row not in manifest')
        seg=segments.get(rid)
        if not seg: continue
        if ev.get('segment_id')!=seg.get('segment_id'): add(errors,f'{eid} segment mismatch')
        if ev.get('clean_md_path')!=seg['source_paths']['clean_md_relpath']: add(errors,f'{eid} clean path mismatch')
        q=str(ev.get('quote','')).strip()
        text=(repo/seg['source_paths']['clean_md_relpath']).read_text(encoding='utf-8')
        if not q or q not in text: add(errors,f'{eid} quote_not_found')
        if any(p in q for p in FORBIDDEN): add(errors,f'{eid} forbidden pattern in quote')
    if len(manifest)<100: add(errors,f'too few manifest rows {len(manifest)}')
    if len(evidence)<260: add(errors,f'too few evidence {len(evidence)}')
    for rid,r in rows.items():
        cnt=len(ev_by_row.get(rid,[]))
        if cnt != int(r.get('evidence_quote_count',-1)): add(errors,f'row {rid} evidence count mismatch')
        if r.get('core_status')=='core' and cnt<3: add(errors,f'core row {rid} too few quotes')
        if r.get('core_status')=='bridge' and cnt<2: add(errors,f'bridge row {rid} too few quotes')
        if r.get('core_status')=='excluded' and any(ev.get('quote_role')!='boundary-exclusion' for ev in ev_by_row.get(rid,[])): add(errors,f'excluded row {rid} non-boundary quote')
    return rows, ev_by_row

def validate_w3_w5_w10(repo:Path, rows:dict[int,dict[str,Any]], errors:list[str]):
    w3=[r for r in load_jsonl(repo/'knowledge/lexicon/term-senses.jsonl') if r.get('batch_id')==W3_BATCH]
    w5=[r for r in load_jsonl(repo/'knowledge/relations/relation-assets.jsonl') if r.get('batch_id')==W5_BATCH]
    if len(w3)!=45: add(errors,f'W3 count {len(w3)} != 45')
    if len(w5)!=40: add(errors,f'W5 count {len(w5)} != 40')
    segments=load_segments(repo)
    for rec in w3:
        if rec.get('status')!='draft': add(errors,f'W3 non-draft {rec.get("sense_id")}')
        for q in rec.get('evidence_quotes') or []:
            rid=int(q.get('row_id')); quote=str(q.get('quote','')).strip()
            if rid not in rows: add(errors,f'W3 {rec.get("sense_id")} quote row outside manifest {rid}')
            if quote not in (repo/segments[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W3 quote not found {rec.get("sense_id")}')
    senses={r.get('sense_id') for r in w3}
    for rec in w5:
        if rec.get('status')!='draft': add(errors,f'W5 non-draft {rec.get("relation_id")}')
        if rec.get('source') not in senses or rec.get('target') not in senses: add(errors,f'W5 source/target not education W3 {rec.get("relation_id")}')
        for ev in rec.get('evidence_segment') or []:
            rid=int(ev.get('row_id')); quote=str(ev.get('quote','')).strip()
            if rid not in rows: add(errors,f'W5 evidence outside manifest {rid}')
            if quote not in (repo/segments[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W5 quote not found {rec.get("relation_id")}')
    cards=[]
    for p in (repo/'knowledge/w10-absorption').glob('*-cards/*education-examination-credentialism.md'):
        text=p.read_text(encoding='utf-8')
        m=re.search(r'^row_id:\s*(\d+)',text,re.M)
        if m: cards.append((p,int(m.group(1))))
    if len(cards)!=30: add(errors,f'Education W10 card count {len(cards)} != 30')
    for p,rid in cards:
        if rid not in rows: add(errors,f'W10 card row outside manifest {p}')
        text=p.read_text(encoding='utf-8')
        if 'status: pilot-draft' not in text: add(errors,f'W10 not pilot-draft {p}')
        if any(f in text for f in FORBIDDEN): add(errors,f'W10 forbidden pattern {p}')

def validate_docs(repo:Path, errors:list[str], final:bool):
    required={
        Path('README.md'): ['Education / Examination / Credentialism', 'Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.'],
        Path('knowledge/README.md'): ['education-examination-credentialism', 'Current latest checkpoint — Health / Body / Medicine / Risk Society'],
        Path('knowledge/STATE.md'): ['current_phase: Health / Body / Medicine / Risk Society maximum absorption', '--min-count 1044'],
        Path('ISMISM-MAINLINE-HANDOFF.md'): ['Education / Examination / Credentialism / Knowledge Discipline maximum absorption', 'W3 1676/1228'],
        Path('DIRECTORY_MAP.md'): ['knowledge/themes/education-examination-credentialism/', 'validate_education_examination_credentialism_theme.py'],
        Path('AGENTS.md'): ['knowledge/themes/education-examination-credentialism/README.md', 'Education / Examination / Credentialism'],
        Path('skills/ismism-knowledge-operator/SKILL.md'): ['query_education_examination_credentialism_theme.py', '--min-count 1044'],
        Path('knowledge/query-playbook.md'): ['query_education_examination_credentialism_theme.py', '教育 / 考试 / 学历'],
        Path('knowledge/qa/absorption-strength-distribution.md'): ['W10 close-reading absorption covers 311 rows', 'Full W3+W5+W10 row overlap is now 277 rows'],
        ROOT/'README.md': ['validate_education_examination_credentialism_theme.py', 'query_education_examination_credentialism_theme.py'],
    }
    if not final: return
    for rel,markers in required.items():
        path=repo/rel
        if not path.exists(): add(errors,f'missing doc {rel}'); continue
        text=path.read_text(encoding='utf-8')
        for marker in markers:
            if marker not in text: add(errors,f'{rel} missing marker {marker!r}')

def validate_protected(repo:Path, errors:list[str]):
    diff=subprocess.run(['git','diff','--name-only','--','split_md','split_md_clean'],cwd=repo,text=True,capture_output=True)
    if diff.stdout.strip(): add(errors,'protected corpus diff: '+diff.stdout.strip())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--final',action='store_true')
    args=ap.parse_args(); repo=Path(args.repo).resolve(); errors=[]
    segments=load_segments(repo)
    rows,_=validate_manifest_evidence(repo,segments,errors)
    validate_w3_w5_w10(repo,rows,errors)
    validate_docs(repo,errors,args.final)
    validate_protected(repo,errors)
    if errors:
        print(f'validate_education_examination_credentialism_theme: FAIL errors={len(errors)}')
        for e in errors[:80]: print('-',e)
        return 1
    print(f'validate_education_examination_credentialism_theme: PASS manifest={len(rows)} evidence={sum(1 for _ in load_jsonl(repo/EVIDENCE))} w3=45 w5=40 w10=30 errors=0')
    return 0
if __name__=='__main__': sys.exit(main())
