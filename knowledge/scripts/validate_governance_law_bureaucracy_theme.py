#!/usr/bin/env python3
from __future__ import annotations
import json,re,subprocess,sys
from pathlib import Path
ROOT=Path('knowledge/themes/governance-law-bureaucracy')
MANIFEST=ROOT/'governance-law-bureaucracy-row-manifest.jsonl'
EVIDENCE=ROOT/'governance-law-bureaucracy-evidence-bank.jsonl'
W3='W3-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16'
W5='W5-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16'
REL_TYPES={'boundary-between','route-from-to','tension-between','mediates-between','transitions-to','blocks-transition','misrecognizes-as','objectifies','subjectivizes','overcodes','represents-position','evidences-claim'}
def load_jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]
def add(errors,msg): errors.append(msg)
def main(repo='.', final=False):
    repo=Path(repo).resolve(); errors=[]
    manifest=load_jsonl(repo/MANIFEST); evidence=load_jsonl(repo/EVIDENCE)
    rows={int(r['row_id']):r for r in manifest}; ev_by_row={}
    segs={int(r['row_id']):r for r in load_jsonl(repo/'knowledge/manifests/segments.jsonl')}
    for ev in evidence: ev_by_row.setdefault(int(ev['row_id']),[]).append(ev)
    if len(manifest)!=124: add(errors,f'manifest {len(manifest)} !=124')
    if len(evidence)!=307: add(errors,f'evidence {len(evidence)} !=307')
    for ev in evidence:
        rid=int(ev['row_id']); q=ev['quote']; seg=segs[rid]
        if q not in (repo/seg['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'quote not found {ev.get("evidence_id")}')
    w3=[r for r in load_jsonl(repo/'knowledge/lexicon/term-senses.jsonl') if r.get('batch_id')==W3]
    w5=[r for r in load_jsonl(repo/'knowledge/relations/relation-assets.jsonl') if r.get('batch_id')==W5]
    if len(w3)!=45: add(errors,f'W3 count {len(w3)} !=45')
    if len(w5)!=40: add(errors,f'W5 count {len(w5)} !=40')
    term_ids={r.get('sense_id') for r in w3}
    for r in w3:
        if r.get('status')!='draft': add(errors,f'non-draft W3 {r.get("sense_id")}')
        if len(r.get('evidence_quotes') or [])<2: add(errors,f'W3 too few quotes {r.get("sense_id")}')
        for q in r.get('evidence_quotes') or []:
            rid=int(q['row_id']); quote=q['quote']
            if quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W3 quote not found {r.get("sense_id")}')
        for src in r.get('source_segments') or []:
            if not (repo/src.get('clean_md_path','')).exists(): add(errors,f'W3 clean path missing {r.get("sense_id")}')
            if not (repo/src.get('segment_card_path','')).exists(): add(errors,f'W3 segment card missing {r.get("sense_id")}')
    types=set()
    for r in w5:
        if r.get('status')!='draft': add(errors,f'non-draft W5 {r.get("relation_id")}')
        types.add(r.get('relation_type'))
        if r.get('source') not in term_ids or r.get('target') not in term_ids: add(errors,f'W5 source/target outside G018 W3 {r.get("relation_id")}')
        if not (repo/f"knowledge/position-cards/{r.get('source_position')}.md").exists(): add(errors,f'W5 source position missing {r.get("relation_id")}')
        if not (repo/f"knowledge/position-cards/{r.get('target_position')}.md").exists(): add(errors,f'W5 target position missing {r.get("relation_id")}')
        for ev in r.get('evidence_segment') or []:
            rid=int(ev['row_id']); quote=ev['quote']
            if quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W5 quote not found {r.get("relation_id")}')
    if types!=REL_TYPES: add(errors,f'W5 type coverage mismatch missing={sorted(REL_TYPES-types)} extra={sorted(types-REL_TYPES)}')
    cards=[]
    for p in (repo/'knowledge/w10-absorption').glob('*-cards/*.md'):
        txt=p.read_text(encoding='utf-8')
        if 'Governance / Law / Bureaucracy / Order 社会现象层' in txt or 'Governance / Law / Bureaucracy / Order W10 pilot-draft' in txt:
            cards.append(p)
            if 'status: pilot-draft' not in txt: add(errors,f'W10 not pilot-draft {p}')
            m=re.search(r'^row_id:\s*(\d+)',txt,flags=re.M)
            rid=int(m.group(1)) if m else -1
            fm=txt.split('---',2)[1]
            for qm in re.finditer(r'^  - (.+)$',fm,flags=re.M):
                quote=qm.group(1).strip()
                if quote and quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'):
                    add(errors,f'W10 quote not found {p}')
    if len(cards)!=30: add(errors,f'Governance-law W10 cards {len(cards)} !=30')
    idx=(repo/'knowledge/w10-absorption/index.md').read_text(encoding='utf-8')
    for p in cards:
        if p.relative_to(repo).as_posix() not in idx: add(errors,f'index missing {p}')
    for rel in [ROOT/'README.md', ROOT/'governance-law-bureaucracy-taxonomy.md', ROOT/'governance-law-bureaucracy-w3-w5-batch-notes.md', Path('knowledge/w10-absorption/PLAN.md')]:
        text=(repo/rel).read_text(encoding='utf-8') if (repo/rel).exists() else ''
        for marker in [W3,W5,'30 Governance-law pilot-draft']:
            if marker not in text and rel.name!='PLAN.md': add(errors,f'{rel} missing {marker}')
        if rel.name=='PLAN.md' and 'Governance / Law / Bureaucracy / Order expansion batch' not in text:
            add(errors,'W10 PLAN missing Governance batch')

    if final:
        markers={
          Path('README.md'): ['Governance / Law / Bureaucracy / Order maximum absorption', 'Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.'],
          Path('knowledge/README.md'): ['governance-law-bureaucracy', 'Current latest checkpoint — Health / Body / Medicine / Risk Society'],
          Path('knowledge/STATE.md'): ['current_phase: Health / Body / Medicine / Risk Society maximum absorption', '--min-count 1044'],
          Path('ISMISM-MAINLINE-HANDOFF.md'): ['Governance / Law / Bureaucracy / Order maximum absorption', 'W3 1676/1228'],
          Path('DIRECTORY_MAP.md'): ['knowledge/themes/governance-law-bureaucracy/', 'validate_governance_law_bureaucracy_theme.py'],
          Path('AGENTS.md'): ['knowledge/themes/governance-law-bureaucracy/README.md', 'Governance / Law / Bureaucracy / Order'],
          Path('skills/ismism-knowledge-operator/SKILL.md'): ['query_governance_law_bureaucracy_theme.py', '--min-count 1044'],
          Path('knowledge/query-playbook.md'): ['query_governance_law_bureaucracy_theme.py', '治理 / 法律 / 法治 / 法权 / 官僚 / 科层'],
          Path('knowledge/qa/absorption-strength-distribution.md'): ['W10 pilot cards now cover 311 rows', 'W1/W2-only rows are now 6'],
          ROOT/'README.md': ['validate_governance_law_bureaucracy_theme.py', 'query_governance_law_bureaucracy_theme.py'],
        }
        for rel,vals in markers.items():
            text=(repo/rel).read_text(encoding='utf-8') if (repo/rel).exists() else ''
            for marker in vals:
                if marker not in text: add(errors,f'{rel} missing marker {marker!r}')

    diff=subprocess.run(['git','diff','--name-only','--','split_md','split_md_clean'],cwd=repo,text=True,capture_output=True)
    if diff.stdout.strip(): add(errors,'protected corpus diff '+diff.stdout.strip())
    print(f'validate_governance_law_bureaucracy_theme: {"PASS" if not errors else "FAIL"} manifest={len(manifest)} evidence={len(evidence)} w3={len(w3)} w5={len(w5)} w10={len(cards)} errors={len(errors)}')
    for e in errors[:100]: print('ERROR',e)
    return 1 if errors else 0
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--final',action='store_true')
    args=ap.parse_args(); sys.exit(main(args.repo,args.final))
