#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from typing import Any
ROOT=Path("knowledge/themes/aesthetics-media")
W3_BATCH="W3-AESTHETICS-MEDIA-2026-06-16"
W5_BATCH="W5-AESTHETICS-MEDIA-2026-06-16"
CLASSES={'ethical-art-action', 'zootopia-multiculturalism', 'aestheticism-gaze-fantasy', 'cinema-ecology-consumption', 'image-pragmatism', 'time-myth-festival', 'revenge-film-hero', 'myth-cosmic-narrative', 'guilt-film-symbolization', 'symbolic-narrative-review', 'everyday-novel-film', 'symbolic-pragmatism-media-industry', 'social-representation-media', 'language-games-symbol', 'poetry-metaphysics', 'sci-fi-future-right', 'sci-fi-transcendence-film', 'cinema-world-ontology', 'poetic-ontology', 'imaginary-symbolic-image', 'protagonist-narrative', 'music-poetry-metaphysics', 'hospitality-novel-film', 'aesthetic-stage-existence', 'velvet-film-example', 'movie-file-phenomenon', 'arrival-time-film', 'ordinary-film-conversation-method', 'erotic-art-industry', 'sci-fi-phase-image', 'sexualized-gaze-touch', 'hollywood-happy-ending', 'diary-novel-time', 'magic-image-hysteria', 'symbolic-form-myth-art', 'consciousness-stream-cinematic-experience', 'emotion-film-literature', 'text-abjection-poetics', 'hermeneutics-text', 'categorical-narratology', 'mass-culture-art-film', 'consciousness-projection-cinema', 'structuralism-symbol-image', 'everyday-media-ideology', 'hospitality-film-case', 'fetish-symbolic-representation', 'poststructuralism-image-text', 'local-totality-narrative-media', 'decadent-aesthetics-poetry', 'poetic-eternalism-novel-narrative', 'spiritual-narrative-story', 'dream-subjectivity-theatre', 'phenomenological-aestheticism', 'statement-discourse-narrative', 'phenomenological-hermeneutics-text', 'idol-symbolic-image', 'destiny-already-seen-film', 'logic-form-text', 'fictional-existentialism', 'structural-humanism-myth', 'picture-logic-image', 'culture-consumption-cinema', 'discourse-dream-text', 'semiotics-fantasy-image', 'cinema-immortality-viewer', 'cinematic-history-stage', 'metaphoric-symbolism-image', 'final-destination-ai-game', 'hollywood-everyday-consumption'}
ROLES={"core","bridge","context","excluded"}
REL_TYPES={"boundary-between","route-from-to","tension-between","mediates-between","transitions-to","blocks-transition","misrecognizes-as","objectifies","subjectivizes","overcodes","represents-position","evidences-claim"}
def load_jsonl(path:Path):
    return [(i,json.loads(line)) for i,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1) if line.strip()]
def load_segments(repo:Path):
    return {int(r['row_id']):r for _,r in load_jsonl(repo/'knowledge/manifests/segments.jsonl')}
def toc(v): return 'None' if v is None else str(v)
def add(errors,msg): errors.append(msg)
def check_quote(repo, rel, quote, where, errors):
    p=repo/rel
    if not p.exists(): add(errors,f"{where}: missing clean {rel}"); return
    if not str(quote).strip(): add(errors,f"{where}: empty quote"); return
    if str(quote) not in p.read_text(encoding='utf-8'): add(errors,f"{where}: quote not exact substring: {str(quote)[:80]}")
def parse_frontmatter(path:Path):
    lines=path.read_text(encoding='utf-8').splitlines(); meta={}; cur=None
    if not lines or lines[0].strip()!='---': return meta
    for raw in lines[1:]:
        if raw.strip()=='---': break
        if not raw.strip(): continue
        if not raw.startswith(' ') and ':' in raw:
            k,v=raw.split(':',1); cur=k.strip(); meta[cur]=v.strip() if v.strip() else []
        elif cur=='evidence_quotes' and raw.strip().startswith('- '): meta.setdefault(cur,[]).append(raw.strip()[2:])
    return meta
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--final',action='store_true'); ap.add_argument('--json',action='store_true'); args=ap.parse_args(argv)
    repo=Path(args.repo).resolve(); errors=[]; segs=load_segments(repo)
    required=[ROOT/'README.md',ROOT/'aesthetics-media-row-manifest.jsonl',ROOT/'aesthetics-media-evidence-bank.jsonl',ROOT/'aesthetics-media-taxonomy.md',ROOT/'aesthetics-media-synthesis.md',ROOT/'film-analysis-precursor-synthesis.md',Path('knowledge/scripts/query_aesthetics_media_theme.py')]
    for p in required:
        if not (repo/p).exists(): add(errors,f'missing {p}')
    manifest={}
    for ln,r in load_jsonl(repo/ROOT/'aesthetics-media-row-manifest.jsonl'):
        row=int(r.get('row_id',-1)); manifest[row]=r; s=segs.get(row)
        if not s: add(errors,f'manifest:{ln} bad row {row}'); continue
        if r.get('segment_id')!=s.get('segment_id'): add(errors,f'manifest:{ln} segment mismatch {row}')
        if str(r.get('toc_id'))!=toc(s.get('toc_id')): add(errors,f'manifest:{ln} toc mismatch {row}')
        if r.get('clean_md_path')!=s['source_paths']['clean_md_relpath']: add(errors,f'manifest:{ln} clean mismatch {row}')
        if r.get('theme_class') not in CLASSES: add(errors,f'manifest:{ln} bad class {r.get("theme_class")}')
        if r.get('theme_role') not in ROLES: add(errors,f'manifest:{ln} bad role')
    evidence={}; ev_counts={}
    for ln,r in load_jsonl(repo/ROOT/'aesthetics-media-evidence-bank.jsonl'):
        eid=str(r.get('evidence_id','')); evidence[eid]=r; row=int(r.get('row_id',-1)); ev_counts[row]=ev_counts.get(row,0)+1
        if row not in manifest: add(errors,f'evidence:{ln} row not in manifest {row}'); continue
        for f in ['segment_id','toc_id','clean_md_path','theme_class']:
            if r.get(f)!=manifest[row].get(f): add(errors,f'evidence:{ln} {f} mismatch {eid}')
        check_quote(repo,str(r.get('clean_md_path','')),str(r.get('quote','')),f'evidence:{ln}:{eid}',errors)
    core={row for row,r in manifest.items() if r.get('theme_role')=='core'}
    if len(manifest)<65: add(errors,f'manifest rows {len(manifest)} <65')
    if len(core)<25: add(errors,f'core rows {len(core)} <25')
    if len(evidence)<190: add(errors,f'evidence records {len(evidence)} <190')
    for row in core:
        if ev_counts.get(row,0)<3: add(errors,f'core row {row} has <3 evidence')
    w3=[]; sense_ids=set()
    for _,r in load_jsonl(repo/'knowledge/lexicon/term-senses.jsonl'):
        if r.get('sense_id'): sense_ids.add(str(r['sense_id']))
        if r.get('batch_id')==W3_BATCH: w3.append(r)
    if len(w3)!=53: add(errors,f'W3 count {len(w3)} != 53')
    for r in w3:
        if r.get('status')!='draft': add(errors,f"W3 {r.get('sense_id')} non-draft")
        if len(r.get('evidence_quotes',[]))<2: add(errors,f"W3 {r.get('sense_id')} <2 quotes")
        for q in r.get('evidence_quotes',[]):
            row=int(q.get('row_id',-1)); s=segs.get(row)
            if s: check_quote(repo,s['source_paths']['clean_md_relpath'],q.get('quote',''),f"W3 {r.get('sense_id')}",errors)
    w5=[]
    for _,r in load_jsonl(repo/'knowledge/relations/relation-assets.jsonl'):
        if r.get('batch_id')==W5_BATCH: w5.append(r)
    if len(w5)!=44: add(errors,f'W5 count {len(w5)} != 44')
    for r in w5:
        rid=r.get('relation_id')
        if r.get('status')!='draft': add(errors,f'W5 {rid} non-draft')
        if r.get('relation_type') not in REL_TYPES: add(errors,f'W5 {rid} bad relation type')
        for ref in [r.get('source'),r.get('target'),*(r.get('source_senses') or [])]:
            if isinstance(ref,str) and ref.startswith('term:') and ref not in sense_ids: add(errors,f'W5 {rid} missing sense {ref}')
        for ev in r.get('evidence_segment',[]):
            row=int(ev.get('row_id',-1)); s=segs.get(row)
            if s: check_quote(repo,s['source_paths']['clean_md_relpath'],ev.get('quote',''),f'W5 {rid}',errors)
    w10=[]
    for p in (repo/'knowledge/w10-absorption').glob('*-cards/*aesthetics-media*.md'):
        meta=parse_frontmatter(p)
        if meta.get('status')!='pilot-draft': add(errors,f'W10 {p} non-pilot')
        w10.append(meta)
    if len(w10)!=30: add(errors,f'W10 count {len(w10)} != 30')
    if args.final:
        docs={Path('README.md'):['Aesthetics / Art / Media / Image / Narrative','validate_aesthetics_media_theme.py'],Path('AGENTS.md'):['knowledge/themes/aesthetics-media/README.md','Aesthetics / Art / Media'],Path('knowledge/STATE.md'):['Aesthetics / Art / Media / Image / Narrative','validate_aesthetics_media_theme.py'],Path('ISMISM-MAINLINE-HANDOFF.md'):['Aesthetics / Art / Media / Image / Narrative','aesthetics-media-row-manifest.jsonl'],Path('DIRECTORY_MAP.md'):['knowledge/themes/aesthetics-media/','validate_aesthetics_media_theme.py'],Path('knowledge/README.md'):['themes/aesthetics-media/README.md','Aesthetics / Art / Media'],Path('knowledge/query-playbook.md'):['query_aesthetics_media_theme.py','电影 / 影像 / 美学 / 叙事'],Path('skills/ismism-knowledge-operator/SKILL.md'):['knowledge/themes/aesthetics-media/README.md','query_aesthetics_media_theme.py']}
        for path,needles in docs.items():
            text=(repo/path).read_text(encoding='utf-8') if (repo/path).exists() else ''
            for needle in needles:
                if needle not in text: add(errors,f'doc {path} missing {needle}')
    out={'status':'FAIL' if errors else 'PASS','manifest_rows':len(manifest),'evidence_records':len(evidence),'w3':len(w3),'w5':len(w5),'w10':len(w10),'errors':len(errors)}
    if errors:
        print('validate_aesthetics_media_theme: FAIL')
        for e in errors[:80]: print('-',e)
    else: print(f"validate_aesthetics_media_theme: PASS manifest={len(manifest)} evidence={len(evidence)} w3={len(w3)} w5={len(w5)} w10={len(w10)}")
    if args.json: print(json.dumps(out,ensure_ascii=False,indent=2))
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
