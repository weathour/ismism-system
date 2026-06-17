#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SOCIAL_THEME_VALIDATORS = [
    'knowledge/scripts/validate_labor_workplace_precarity_theme.py',
    'knowledge/scripts/validate_education_examination_credentialism_theme.py',
    'knowledge/scripts/validate_family_intimacy_reproduction_theme.py',
    'knowledge/scripts/validate_consumption_desire_lifestyle_theme.py',
    'knowledge/scripts/validate_media_platform_public_opinion_theme.py',
    'knowledge/scripts/validate_governance_law_bureaucracy_theme.py',
    'knowledge/scripts/validate_class_youth_generational_anxiety_theme.py',
    'knowledge/scripts/validate_psychological_distress_social_symptom_theme.py',
    'knowledge/scripts/validate_urban_housing_migration_space_theme.py',
    'knowledge/scripts/validate_health_body_risk_society_theme.py',
]

PREEXISTING_THEME_VALIDATORS = [
    'knowledge/scripts/validate_aesthetics_media_theme.py',
    'knowledge/scripts/validate_psychoanalysis_subjectivity_theme.py',
    'knowledge/scripts/validate_feminism_theme.py',
    'knowledge/scripts/validate_capitalism_theme.py',
    'knowledge/scripts/validate_time_death_theme.py',
    'knowledge/scripts/validate_religion_theme.py',
    'knowledge/scripts/validate_chinese_philosophy_theme.py',
    'knowledge/scripts/validate_ai_theme.py',
]

GLOBAL_VALIDATORS = [
    ['python3','knowledge/scripts/validate_universal_absorption_phase_a.py','--repo','.','--final'],
    ['python3','knowledge/scripts/validate_universal_absorption_phase_b.py','--repo','.','--final'],
    ['python3','knowledge/scripts/validate_w3_term_senses.py','--repo','.'],
    ['python3','knowledge/scripts/validate_w5_relation_assets.py','--repo','.','--min-count','1044','--require-type-min','2'],
    ['python3','knowledge/scripts/validate_w10_absorption.py','--repo','.'],
    ['python3','knowledge/scripts/validate_master_spec_outputs.py','--repo','.'],
]

SUPERPHASE_FILES = {
    'knowledge/scripts/query_social_phenomena_superphase.py': [
        'ROUTES', 'smoke_all', '考公热', '医疗焦虑'
    ],
    'knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md': [
        'How do labor, credentialing, family, and consumption reproduce everyday subjectivity?', 'labor-workplace-precarity', 'consumption-desire-lifestyle'
    ],
    'knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md': [
        'How do private suffering, public affect, platform visibility, institutional order, and class anxiety mediate each other?', 'media-platform-public-opinion', 'class-youth-generational-anxiety'
    ],
    'knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md': [
        'How do social contradictions sediment into body, psyche, spatial life, and risk consciousness?', 'psychological-distress-social-symptom', 'health-body-risk-society'
    ],
    'knowledge/qa/social-phenomena-superphase-audit.md': [
        'Thirty prompt smoke routes', 'PASS routes=30 fallback_routes=19 failures=0', 'W3/W5 remain `draft`; W10 remains `pilot-draft`'
    ],
    'knowledge/qa/social-phenomena-superphase-final-closure.md': [
        'Social Phenomena Superphase Final Closure', 'W3: 1676 draft senses / 1228 terms', 'No `split_md/` or `split_md_clean/` source file was edited'
    ],
    'knowledge/query-playbook.md': [
        'Social Phenomena Superphase — final query router and smoke matrix', 'query_social_phenomena_superphase.py --smoke-all --limit 1', 'Thirty-prompt coverage:'
    ],
    'knowledge/logs/operation-log.md': [
        'Social Phenomena Superphase query and validation layer (G035)'
    ],
}

CURRENT_MARKER = 'Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.'
CURRENT_MARKER_FILES = [
    'README.md',
    'knowledge/README.md',
    'knowledge/STATE.md',
    'ISMISM-MAINLINE-HANDOFF.md',
    'DIRECTORY_MAP.md',
    'AGENTS.md',
    'skills/ismism-knowledge-operator/SKILL.md',
    'knowledge/query-playbook.md',
]

DISTRIBUTION_MARKERS = [
    'W10 close-reading absorption covers 311 rows',
    'W10 close-reading absorption covers 311 rows (741 cards).',
    'W10 pilot cards now cover 311 rows (741 cards).',
    'Full W3+W5+W10 row overlap is now 277 rows.',
]

REQUIRED_PROMPTS = [
    '内卷','打工人','加班','绩效','失业焦虑','考公热','考研','学历崇拜','鸡娃','专家崇拜',
    '婚恋市场','彩礼','生育焦虑','父母控制','消费主义','情绪消费','奢侈品','短视频成瘾','直播','热搜舆论',
    '网红','官僚手续','法律意识','中产焦虑','青年虚无','躺平','抑郁焦虑','住房焦虑','城市漂泊','医疗焦虑'
]


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def run(repo: Path, cmd: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, cwd=repo, text=True, capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr


def check_markers(repo: Path, errors: list[str]) -> None:
    for rel, markers in SUPERPHASE_FILES.items():
        p = repo / rel
        if not p.exists():
            add(errors, f'missing {rel}')
            continue
        text = p.read_text(encoding='utf-8')
        for marker in markers:
            if marker not in text:
                add(errors, f'{rel} missing marker {marker!r}')
    for rel in CURRENT_MARKER_FILES:
        p = repo / rel
        if not p.exists():
            add(errors, f'missing current marker file {rel}')
            continue
        if CURRENT_MARKER not in p.read_text(encoding='utf-8'):
            add(errors, f'{rel} missing current validator marker')
    dist = repo / 'knowledge/qa/absorption-strength-distribution.md'
    if not dist.exists():
        add(errors, 'missing absorption-strength-distribution.md')
    else:
        text = dist.read_text(encoding='utf-8')
        current_block = text.split('<!-- CURRENT-DISTRIBUTION-MARKERS-END -->', 1)[0]
        if '277 rows have W3+W5+W10 full overlap' not in current_block:
            add(errors, 'distribution current block missing full-overlap 277 marker')
        for marker in DISTRIBUTION_MARKERS:
            if marker not in text:
                add(errors, f'distribution missing marker {marker!r}')


def check_routes(repo: Path, errors: list[str], final: bool) -> None:
    code, out, err = run(repo, ['python3','knowledge/scripts/query_social_phenomena_superphase.py','--list-routes','--json'])
    if code != 0:
        add(errors, f'query route list failed: {err or out}')
        return
    try:
        routes = json.loads(out)
    except Exception as exc:
        add(errors, f'query route list bad json: {exc}')
        return
    prompts = [r.get('prompt') for r in routes]
    if len(routes) != 30:
        add(errors, f'query routes {len(routes)} !=30')
    missing = [p for p in REQUIRED_PROMPTS if p not in prompts]
    if missing:
        add(errors, f'missing required prompts {missing}')
    themes = {r.get('theme') for r in routes}
    required_themes = {
        'labor-workplace-precarity','education-examination-credentialism','family-intimacy-reproduction','consumption-desire-lifestyle',
        'media-platform-public-opinion','governance-law-bureaucracy','class-youth-generational-anxiety','psychological-distress-social-symptom',
        'urban-housing-migration-space','health-body-risk-society'
    }
    if not required_themes <= themes:
        add(errors, f'query routes missing themes {sorted(required_themes - themes)}')
    if final:
        code, out, err = run(repo, ['python3','knowledge/scripts/query_social_phenomena_superphase.py','--smoke-all','--limit','1'])
        if code != 0 or 'PASS routes=30' not in out:
            add(errors, f'superphase query smoke failed code={code}: {out[-1000:]} {err[-1000:]}')


def run_final_validators(repo: Path, errors: list[str]) -> None:
    commands: list[list[str]] = []
    for script in SOCIAL_THEME_VALIDATORS + PREEXISTING_THEME_VALIDATORS:
        commands.append(['python3', script, '--repo', '.', '--final'])
    commands.extend(GLOBAL_VALIDATORS)
    commands.append(['git','diff','--check'])
    for cmd in commands:
        code, out, err = run(repo, cmd)
        if code != 0:
            add(errors, f'command failed {" ".join(cmd)}\nSTDOUT:\n{out[-2000:]}\nSTDERR:\n{err[-2000:]}')
    code, out, err = run(repo, ['git','diff','--name-only','--','split_md','split_md_clean'])
    if code != 0:
        add(errors, f'protected corpus diff command failed: {err}')
    elif out.strip():
        add(errors, f'protected corpus modified: {out.strip()}')


def main(repo: str = '.', final: bool = False) -> int:
    root = Path(repo).resolve()
    errors: list[str] = []
    check_markers(root, errors)
    check_routes(root, errors, final)
    if final:
        run_final_validators(root, errors)
    status = 'PASS' if not errors else 'FAIL'
    print(f'validate_social_phenomena_superphase: {status} errors={len(errors)} final={final}')
    if final and not errors:
        print(json.dumps({
            'status': 'PASS',
            'social_theme_validators': len(SOCIAL_THEME_VALIDATORS),
            'preexisting_theme_validators': len(PREEXISTING_THEME_VALIDATORS),
            'query_routes': 30,
            'w3': '1676/1228',
            'w5': 1044,
            'w10': 741,
            'full_overlap_rows': 277,
        }, ensure_ascii=False))
    for e in errors[:160]:
        print('ERROR', e)
    return 1 if errors else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    ap.add_argument('--final', action='store_true')
    args = ap.parse_args()
    raise SystemExit(main(args.repo, args.final))
