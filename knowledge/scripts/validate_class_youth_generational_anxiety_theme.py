#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess,sys
from pathlib import Path
from collections import Counter
ROOT=Path('knowledge/themes/class-youth-generational-anxiety')
MANIFEST=ROOT/'class-youth-generational-anxiety-row-manifest.jsonl'
EVIDENCE=ROOT/'class-youth-generational-anxiety-evidence-bank.jsonl'
W3='W3-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16'
W5='W5-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16'
REL_TYPES={'boundary-between','route-from-to','tension-between','mediates-between','transitions-to','blocks-transition','misrecognizes-as','objectifies','subjectivizes','overcodes','represents-position','evidences-claim'}
REQ_CLASSES={'class-stratification-mobility','youth-generation-future','middle-class-anxiety','bottom-shame-humiliation','success-competition-merit','class-solidification-channel-blockage','youth-nihilism-cynicism','poverty-wealth-inequality','labor-capital-class-bridge','excluded-keyword-only'}
def load_jsonl(p): return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]
def add(errors,msg): errors.append(msg)
def main(repo='.', final=False):
    repo=Path(repo).resolve(); errors=[]
    manifest=load_jsonl(repo/MANIFEST); evidence=load_jsonl(repo/EVIDENCE)
    segs={int(r['row_id']):r for r in load_jsonl(repo/'knowledge/manifests/segments.jsonl')}
    rows={int(r['row_id']):r for r in manifest}; evby={}
    if len(manifest)!=120: add(errors,f'manifest {len(manifest)} !=120')
    if len(evidence)!=310: add(errors,f'evidence {len(evidence)} !=310')
    classes=Counter(r.get('theme_class') for r in manifest)
    missing=REQ_CLASSES-set(classes)
    if missing: add(errors,f'missing classes {sorted(missing)}')
    for r in manifest:
        rid=int(r['row_id']); seg=segs.get(rid)
        if not seg: add(errors,f'missing segment row {rid}'); continue
        if r.get('clean_md_path')!=seg['source_paths']['clean_md_relpath']: add(errors,f'clean path mismatch row {rid}')
        if r.get('theme_class') not in REQ_CLASSES: add(errors, f'bad class row {rid}')
    ids=set()
    for ev in evidence:
        eid=ev.get('evidence_id'); rid=int(ev['row_id']); evby.setdefault(rid,[]).append(ev)
        if eid in ids: add(errors,f'duplicate evidence {eid}')
        ids.add(eid)
        if rid not in rows: add(errors,f'evidence row outside manifest {eid}')
        q=ev.get('quote','')
        if q not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'quote not found {eid}')
    for rid,r in rows.items():
        if len(evby.get(rid,[]))!=int(r.get('evidence_quote_count',-1)): add(errors,f'evidence count mismatch row {rid}')
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
    types=set(); type_counts=Counter()
    for r in w5:
        if r.get('status')!='draft': add(errors,f'non-draft W5 {r.get("relation_id")}')
        types.add(r.get('relation_type')); type_counts[r.get('relation_type')]+=1
        if r.get('source') not in term_ids or r.get('target') not in term_ids: add(errors,f'W5 source/target outside G021 W3 {r.get("relation_id")}')
        for pos in [r.get('source_position'),r.get('target_position')]:
            if not (repo/f'knowledge/position-cards/{pos}.md').exists(): add(errors,f'position card missing {r.get("relation_id")} {pos}')
        for ev in r.get('evidence_segment') or []:
            rid=int(ev['row_id']); quote=ev['quote']
            if quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W5 quote not found {r.get("relation_id")}')
    if types!=REL_TYPES: add(errors,f'W5 type coverage mismatch missing={sorted(REL_TYPES-types)} extra={sorted(types-REL_TYPES)}')
    cards=[]
    for p in (repo/'knowledge/w10-absorption').glob('*-cards/*.md'):
        txt=p.read_text(encoding='utf-8')
        if 'Class / Youth / Generation / Mobility Anxiety' in txt and ':class-youth-generational-anxiety' in txt:
            cards.append(p)
            if 'status: pilot-draft' not in txt: add(errors,f'W10 not pilot-draft {p}')
            m=re.search(r'^row_id:\s*(\d+)',txt,flags=re.M); rid=int(m.group(1)) if m else -1
            fm=txt.split('---',2)[1]
            for qm in re.finditer(r'^  - (.+)$',fm,flags=re.M):
                quote=qm.group(1).strip()
                if quote and quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W10 quote not found {p}')
    if len(cards)!=30: add(errors, f'Class-youth W10 cards {len(cards)} !=30')
    idx=(repo/'knowledge/w10-absorption/index.md').read_text(encoding='utf-8')
    for p in cards:
        if p.relative_to(repo).as_posix() not in idx: add(errors,f'index missing {p}')
    required=[ROOT/'README.md',ROOT/'class-youth-generational-anxiety-taxonomy.md',ROOT/'class-youth-generational-anxiety-w3-w5-batch-notes.md',ROOT/'class-youth-generational-anxiety-synthesis.md',ROOT/'mobility-anxiety-class-solidification-synthesis.md',ROOT/'youth-success-bottom-humiliation-synthesis.md',ROOT/'CLASS-YOUTH-GENERATIONAL-ANXIETY-MAXIMUM-ABSORPTION-HANDOFF.md']
    for rel in required:
        if not (repo/rel).exists(): add(errors,f'missing {rel}')
    if final:
        markers={
          Path('README.md'): ['Class / Youth / Generation / Mobility Anxiety maximum absorption', 'Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.'],
          Path('knowledge/README.md'): ['class-youth-generational-anxiety', 'Current latest checkpoint — Health / Body / Medicine / Risk Society'],
          Path('knowledge/STATE.md'): ['current_phase: Health / Body / Medicine / Risk Society maximum absorption', '--min-count 1044'],
          Path('ISMISM-MAINLINE-HANDOFF.md'): ['Class / Youth / Generation / Mobility Anxiety maximum absorption', 'W3 1676/1228'],
          Path('DIRECTORY_MAP.md'): ['knowledge/themes/class-youth-generational-anxiety/', 'validate_class_youth_generational_anxiety_theme.py'],
          Path('AGENTS.md'): ['knowledge/themes/class-youth-generational-anxiety/README.md', 'Class / Youth / Generation / Mobility Anxiety'],
          Path('skills/ismism-knowledge-operator/SKILL.md'): ['query_class_youth_generational_anxiety_theme.py', '--min-count 1044'],
          Path('knowledge/query-playbook.md'): ['query_class_youth_generational_anxiety_theme.py', '阶层 / 青年 / 代际 / 上升通道'],
          Path('knowledge/qa/absorption-strength-distribution.md'): ['W10 pilot cards now cover 311 rows', 'Full W3+W5+W10 row overlap is now 277 rows'],
          ROOT/'README.md': ['validate_class_youth_generational_anxiety_theme.py', 'query_class_youth_generational_anxiety_theme.py'],
        }
        for rel,vals in markers.items():
            text=(repo/rel).read_text(encoding='utf-8') if (repo/rel).exists() else ''
            for marker in vals:
                if marker not in text: add(errors,f'{rel} missing marker {marker!r}')
    diff=subprocess.run(['git','diff','--name-only','--','split_md','split_md_clean'],cwd=repo,text=True,capture_output=True)
    if diff.stdout.strip(): add(errors,'protected corpus diff '+diff.stdout.strip())
    print(f'validate_class_youth_generational_anxiety_theme: {"PASS" if not errors else "FAIL"} manifest={len(manifest)} evidence={len(evidence)} w3={len(w3)} w5={len(w5)} w10={len(cards)} errors={len(errors)}')
    for e in errors[:120]: print('ERROR',e)
    return 1 if errors else 0
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--final',action='store_true')
    args=ap.parse_args(); sys.exit(main(args.repo,args.final))
