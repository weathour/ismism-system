#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess,sys
from pathlib import Path
from typing import Any
ROOT=Path('knowledge/themes/media-platform-public-opinion')
MANIFEST=ROOT/'media-platform-public-opinion-row-manifest.jsonl'
EVIDENCE=ROOT/'media-platform-public-opinion-evidence-bank.jsonl'
W3_BATCH='W3-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16'
W5_BATCH='W5-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16'
REL_TYPES={'boundary-between','route-from-to','tension-between','mediates-between','transitions-to','blocks-transition','misrecognizes-as','objectifies','subjectivizes','overcodes','represents-position','evidences-claim'}
CLASSES={'platform-traffic-behavior-engineering','public-opinion-judgment-public-sphere','fandom-idol-influencer-economy','media-communication-propaganda','attention-algorithm-data-capture','discourse-narrative-network-mediatization','cynicism-spectacle-affect-network','governance-platform-public-order-bridge','excluded-keyword-only'}
def load_jsonl(path:Path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
def add(errors,msg): errors.append(msg)
def load_segments(repo:Path): return {int(r['row_id']):r for r in load_jsonl(repo/'knowledge/manifests/segments.jsonl')}
def validate(repo:Path, final:bool):
    errors=[]; segs=load_segments(repo)
    manifest=load_jsonl(repo/MANIFEST); evidence=load_jsonl(repo/EVIDENCE)
    rows={}; evby={}
    for r in manifest:
        rid=int(r['row_id']); rows[rid]=r
        if r.get('theme_class') not in CLASSES: add(errors,f'bad class row {rid}')
        seg=segs.get(rid)
        if not seg: add(errors,f'missing segment row {rid}'); continue
        if r.get('clean_md_path')!=seg['source_paths']['clean_md_relpath']: add(errors,f'clean path mismatch row {rid}')
        if int(r.get('char_count',-1))!=int(seg['clean_md']['char_count']): add(errors,f'char_count mismatch row {rid}')
    ids=set()
    for ev in evidence:
        eid=ev['evidence_id']; rid=int(ev['row_id']); evby.setdefault(rid,[]).append(ev)
        if not re.fullmatch(r'ev:media-platform:\d{4}:\d{2}',eid): add(errors,f'bad evidence id {eid}')
        if eid in ids: add(errors,f'duplicate evidence {eid}')
        ids.add(eid)
        if rid not in rows: add(errors,f'evidence row outside manifest {eid}')
        q=ev['quote']; seg=segs.get(rid)
        if seg and q not in (repo/seg['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'quote not found {eid}')
    if len(manifest)!=119: add(errors,f'manifest {len(manifest)} != 119')
    if len(evidence)!=267: add(errors,f'evidence {len(evidence)} != 267')
    for rid,r in rows.items():
        if len(evby.get(rid,[]))!=int(r.get('evidence_quote_count',-1)): add(errors,f'evidence count mismatch row {rid}')
    w3=[r for r in load_jsonl(repo/'knowledge/lexicon/term-senses.jsonl') if r.get('batch_id')==W3_BATCH]
    w5=[r for r in load_jsonl(repo/'knowledge/relations/relation-assets.jsonl') if r.get('batch_id')==W5_BATCH]
    if len(w3)!=45: add(errors,f'W3 count {len(w3)} != 45')
    if len(w5)!=40: add(errors,f'W5 count {len(w5)} != 40')
    for r in w3:
        if r.get('status')!='draft': add(errors,f'W3 non-draft {r.get("sense_id")}')
        for q in r.get('evidence_quotes') or []:
            rid=int(q['row_id']); quote=q['quote']
            if quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W3 quote not found {r.get("sense_id")}')
    types=set()
    for r in w5:
        if r.get('status')!='draft': add(errors,f'W5 non-draft {r.get("relation_id")}')
        types.add(r.get('relation_type'))
        for pos in [r.get('source_position'),r.get('target_position')]:
            if not (repo/f'knowledge/position-cards/{pos}.md').exists(): add(errors,f'position card missing {r.get("relation_id")} {pos}')
        for ev in r.get('evidence_segment') or []:
            rid=int(ev['row_id']); quote=ev['quote']
            if quote not in (repo/segs[rid]['source_paths']['clean_md_relpath']).read_text(encoding='utf-8'): add(errors,f'W5 quote not found {r.get("relation_id")}')
    if types!=REL_TYPES: add(errors,f'W5 type coverage mismatch {sorted(REL_TYPES-types)}')
    cards=[]
    for p in (repo/'knowledge/w10-absorption').glob('*-cards/*.md'):
        txt=p.read_text(encoding='utf-8')
        if 'Media / Platform / Public Opinion / Traffic Society 社会现象层' in txt: cards.append(p)
    if len(cards)!=30: add(errors,f'Media-platform W10 cards {len(cards)} != 30')
    idx=(repo/'knowledge/w10-absorption/index.md').read_text(encoding='utf-8')
    for p in cards:
        if p.relative_to(repo).as_posix() not in idx: add(errors,f'W10 index missing {p}')
    for rel in [ROOT/'README.md',ROOT/'media-platform-public-opinion-taxonomy.md',ROOT/'media-platform-public-opinion-w3-w5-batch-notes.md',ROOT/'media-platform-public-opinion-synthesis.md',ROOT/'platform-traffic-attention-economy-synthesis.md',ROOT/'public-opinion-fandom-network-cynicism-synthesis.md',ROOT/'MEDIA-PLATFORM-PUBLIC-OPINION-MAXIMUM-ABSORPTION-HANDOFF.md',Path('knowledge/scripts/query_media_platform_public_opinion_theme.py')]:
        if not (repo/rel).exists(): add(errors,f'missing {rel}')
    if final:
        markers={
          Path('README.md'): ['Media / Platform / Public Opinion / Traffic Society maximum absorption','Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.'],
          Path('knowledge/README.md'): ['media-platform-public-opinion','Current latest checkpoint — Health / Body / Medicine / Risk Society'],
          Path('knowledge/STATE.md'): ['current_phase: Health / Body / Medicine / Risk Society maximum absorption','--min-count 1044'],
          Path('ISMISM-MAINLINE-HANDOFF.md'): ['Media / Platform / Public Opinion / Traffic Society maximum absorption','W3 1676/1228'],
          Path('DIRECTORY_MAP.md'): ['knowledge/themes/media-platform-public-opinion/','validate_media_platform_public_opinion_theme.py'],
          Path('AGENTS.md'): ['knowledge/themes/media-platform-public-opinion/README.md','Media / Platform / Public Opinion / Traffic Society'],
          Path('skills/ismism-knowledge-operator/SKILL.md'): ['query_media_platform_public_opinion_theme.py','--min-count 1044'],
          Path('knowledge/query-playbook.md'): ['query_media_platform_public_opinion_theme.py','媒介 / 平台 / 舆论 / 流量 / 短视频 / 直播'],
          Path('knowledge/qa/absorption-strength-distribution.md'): ['W10 pilot cards now cover 311 rows','W1/W2-only rows are now 6'],
          ROOT/'README.md': ['validate_media_platform_public_opinion_theme.py','query_media_platform_public_opinion_theme.py'],
        }
        for rel,vals in markers.items():
            text=(repo/rel).read_text(encoding='utf-8') if (repo/rel).exists() else ''
            for marker in vals:
                if marker not in text: add(errors,f'{rel} missing marker {marker!r}')
    diff=subprocess.run(['git','diff','--name-only','--','split_md','split_md_clean'],cwd=repo,text=True,capture_output=True)
    if diff.stdout.strip(): add(errors,'protected corpus diff '+diff.stdout.strip())
    return errors
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--final',action='store_true')
    args=ap.parse_args(); repo=Path(args.repo).resolve(); errors=validate(repo,args.final)
    print(f"validate_media_platform_public_opinion_theme: {'PASS' if not errors else 'FAIL'} manifest=119 evidence=267 w3=45 w5=40 w10=30 errors={len(errors)}")
    for e in errors[:100]: print('ERROR',e)
    sys.exit(1 if errors else 0)
