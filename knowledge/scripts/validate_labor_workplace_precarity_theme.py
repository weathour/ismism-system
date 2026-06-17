#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

W3_BATCH='W3-LABOR-WORKPLACE-PRECARITY-2026-06-16'
W5_BATCH='W5-LABOR-WORKPLACE-PRECARITY-2026-06-16'
THEME='labor-workplace-precarity'
CLASSES={'labor-alienation-subjectivation','work-discipline-metrics','production-relations-labor-process','exploitation-class-worker','precarity-career-anxiety','social-reproduction-labor-life','practice-organization-liberation','education-workforce-credential-bridge','consumption-labor-desire-bridge'}

def norm(s:str)->str: return re.sub(r'\s+',' ',s).strip()

def load_jsonl(p:Path): return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    ap.add_argument('--final', action='store_true')
    args=ap.parse_args()
    repo=Path(args.repo)
    tdir=repo/'knowledge/themes/labor-workplace-precarity'
    errors=[]
    man=tdir/'labor-workplace-precarity-row-manifest.jsonl'; evp=tdir/'labor-workplace-precarity-evidence-bank.jsonl'
    for p in [tdir/'README.md', man, evp, tdir/'labor-workplace-precarity-taxonomy.md', tdir/'labor-workplace-precarity-w3-w5-batch-notes.md', tdir/'labor-workplace-precarity-synthesis.md', tdir/'work-discipline-and-involution-synthesis.md', tdir/'production-relations-and-practice-synthesis.md', tdir/'LABOR-WORKPLACE-PRECARITY-MAXIMUM-ABSORPTION-HANDOFF.md']:
        if not p.exists(): errors.append(f'missing {p}')
    manifest=load_jsonl(man) if man.exists() else []
    evidence=load_jsonl(evp) if evp.exists() else []
    if len(manifest)<90: errors.append(f'too few manifest rows {len(manifest)}')
    if len(evidence)<220: errors.append(f'too few evidence records {len(evidence)}')
    if len({m.get('row_id') for m in manifest})!=len(manifest): errors.append('duplicate manifest row')
    ev_ids=set()
    man_rows={m.get('row_id') for m in manifest}
    for m in manifest:
        if m.get('theme_class') not in CLASSES: errors.append(f'bad class row {m.get("row_id")}: {m.get("theme_class")}')
        if m.get('core_status') not in {'core','bridge','context','excluded'}: errors.append(f'bad role row {m.get("row_id")}')
    for e in evidence:
        if e.get('evidence_id') in ev_ids: errors.append(f'duplicate evidence {e.get("evidence_id")}')
        ev_ids.add(e.get('evidence_id'))
        if e.get('row_id') not in man_rows: errors.append(f'evidence row outside manifest {e.get("evidence_id")}')
        p=repo/e.get('clean_md_path','')
        if not p.exists(): errors.append(f'missing clean path {e.get("evidence_id")}'); continue
        if norm(e.get('quote','')) not in norm(p.read_text(errors='ignore')): errors.append(f'quote not found {e.get("evidence_id")}')
    w3=[r for r in load_jsonl(repo/'knowledge/lexicon/term-senses.jsonl') if r.get('batch_id')==W3_BATCH]
    w5=[r for r in load_jsonl(repo/'knowledge/relations/relation-assets.jsonl') if r.get('batch_id')==W5_BATCH]
    if len(w3)!=45: errors.append(f'W3 count {len(w3)} != 45')
    if len(w5)!=40: errors.append(f'W5 count {len(w5)} != 40')
    if any(r.get('status')!='draft' for r in w3+w5): errors.append('non-draft W3/W5')
    w10=list((repo/'knowledge/w10-absorption').glob(f'*/*{THEME}.md'))
    if len(w10)!=30: errors.append(f'W10 labor cards {len(w10)} != 30')
    readme=(tdir/'README.md').read_text() if (tdir/'README.md').exists() else ''
    for marker in ['social-phenomena-diagnostic-protocol.md','W3-LABOR-WORKPLACE-PRECARITY','W5-LABOR-WORKPLACE-PRECARITY','query_labor_workplace_precarity_theme.py']:
        if marker not in readme and args.final: errors.append(f'README missing marker {marker}')
    if args.final:
        docs=[repo/'README.md',repo/'knowledge/README.md',repo/'knowledge/STATE.md',repo/'ISMISM-MAINLINE-HANDOFF.md',repo/'DIRECTORY_MAP.md',repo/'AGENTS.md',repo/'knowledge/query-playbook.md',repo/'skills/ismism-knowledge-operator/SKILL.md']
        for d in docs:
            txt=d.read_text(errors='ignore') if d.exists() else ''
            if 'labor-workplace-precarity' not in txt and 'Labor / Workplace / Precarity' not in txt:
                errors.append(f'doc missing labor marker {d}')
    print(f"validate_labor_workplace_precarity_theme: {'PASS' if not errors else 'FAIL'} manifest={len(manifest)} evidence={len(evidence)} w3={len(w3)} w5={len(w5)} w10={len(w10)} errors={len(errors)}")
    for e in errors[:80]: print('ERROR', e)
    return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
