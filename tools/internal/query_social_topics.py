#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parents[2]

@dataclass(frozen=True)
class Route:
    prompt: str
    route_group: str
    theme: str
    helper: str
    primary: str
    fallbacks: tuple[str, ...]
    synthesis: str
    boundary: str

ROUTES: tuple[Route, ...] = (
    # Route group 1 — everyday life reproduction
    Route('内卷','social-everyday-life-reproduction','labor-workplace-precarity','tools/query/themes/labor_workplace_precarity.py','内卷',(), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','metric discipline / involution route; avoid generic competition moralism'),
    Route('打工人','social-everyday-life-reproduction','labor-workplace-precarity','tools/query/themes/labor_workplace_precarity.py','打工人',('劳动','工作'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream labor-subject label; inspect exact labor/work evidence'),
    Route('加班','social-everyday-life-reproduction','labor-workplace-precarity','tools/query/themes/labor_workplace_precarity.py','加班',('工作','劳动'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream workload label; do not infer labor law/policy claims'),
    Route('绩效','social-everyday-life-reproduction','labor-workplace-precarity','tools/query/themes/labor_workplace_precarity.py','绩效',('指标','排名'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','metric/priceability route'),
    Route('失业焦虑','social-everyday-life-reproduction','labor-workplace-precarity','tools/query/themes/labor_workplace_precarity.py','失业焦虑',('失业','焦虑'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','precarity/anxiety bridge; not labor-market statistics'),
    Route('考公热','social-everyday-life-reproduction','education-examination-credentialism','tools/query/themes/education_examination_credentialism.py','考公热',('考试','资格','文凭'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream civil-service-exam label; use exam/credential evidence only'),
    Route('考研','social-everyday-life-reproduction','education-examination-credentialism','tools/query/themes/education_examination_credentialism.py','考研',('考试','学习','学历'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream exam route; do not infer contemporary admissions facts'),
    Route('学历崇拜','social-everyday-life-reproduction','education-examination-credentialism','tools/query/themes/education_examination_credentialism.py','学历崇拜',('学历','文凭','资格'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','credential fantasy route'),
    Route('鸡娃','social-everyday-life-reproduction','education-examination-credentialism','tools/query/themes/education_examination_credentialism.py','鸡娃',('教育','儿童','学习'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream parenting/education pressure label; bridge to Family only with evidence'),
    Route('专家崇拜','social-everyday-life-reproduction','education-examination-credentialism','tools/query/themes/education_examination_credentialism.py','专家崇拜',('专家','权威','学术'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','expert authority / knowledge legitimacy route'),
    Route('婚恋市场','social-everyday-life-reproduction','family-intimacy-reproduction','tools/query/themes/family_intimacy_reproduction.py','婚恋市场',('婚恋','婚姻','爱情'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream marketized-intimacy label; inspect family/intimacy evidence'),
    Route('彩礼','social-everyday-life-reproduction','family-intimacy-reproduction','tools/query/themes/family_intimacy_reproduction.py','彩礼',('婚姻','家庭','婚恋'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','no direct 彩礼 claim in theme; route through marriage/family evidence only'),
    Route('生育焦虑','social-everyday-life-reproduction','family-intimacy-reproduction','tools/query/themes/family_intimacy_reproduction.py','生育焦虑',('生育','孩子','再生产'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','reproduction/future route; no demographic policy claim'),
    Route('父母控制','social-everyday-life-reproduction','family-intimacy-reproduction','tools/query/themes/family_intimacy_reproduction.py','父母控制',('父母','家庭','孩子'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','parent/child authority route'),
    Route('消费主义','social-everyday-life-reproduction','consumption-desire-lifestyle','tools/query/themes/consumption_desire_lifestyle.py','消费主义',(), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','consumerism / enjoyment quantification route'),
    Route('情绪消费','social-everyday-life-reproduction','consumption-desire-lifestyle','tools/query/themes/consumption_desire_lifestyle.py','情绪消费',('消费主义','享乐','欲望'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','downstream label; use consumption/desire evidence'),
    Route('奢侈品','social-everyday-life-reproduction','consumption-desire-lifestyle','tools/query/themes/consumption_desire_lifestyle.py','奢侈品',('奢侈','品牌','消费'), 'library/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md','lifestyle / identity consumption route'),
    # Route group 2 — platform, public order, class
    Route('短视频成瘾','social-platform-public-order-class','media-platform-public-opinion','tools/query/themes/media_platform_public_opinion.py','短视频成瘾',('短视频','成瘾','平台'), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','downstream platform-addiction label; bridge platform and psychological routes only with evidence'),
    Route('直播','social-platform-public-order-class','media-platform-public-opinion','tools/query/themes/media_platform_public_opinion.py','直播',(), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','live-stream platform route'),
    Route('热搜舆论','social-platform-public-order-class','media-platform-public-opinion','tools/query/themes/media_platform_public_opinion.py','热搜舆论',('舆论','公共话语','流量'), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','no direct 热搜 claim; route through public-opinion/traffic evidence'),
    Route('网红','social-platform-public-order-class','media-platform-public-opinion','tools/query/themes/media_platform_public_opinion.py','网红',(), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','influencer/celebrity visibility route'),
    Route('官僚手续','social-platform-public-order-class','governance-law-bureaucracy','tools/query/themes/governance_law_bureaucracy.py','官僚手续',('官僚','手续','程序'), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','bureaucracy/procedure route; not legal advice'),
    Route('法律意识','social-platform-public-order-class','governance-law-bureaucracy','tools/query/themes/governance_law_bureaucracy.py','法律意识',('法律','法','权利'), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','law/rights/legalism route; not legal advice'),
    Route('中产焦虑','social-platform-public-order-class','class-youth-generational-anxiety','tools/query/themes/class_youth_generational_anxiety.py','中产焦虑',(), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','middle-class anxiety route'),
    Route('青年虚无','social-platform-public-order-class','class-youth-generational-anxiety','tools/query/themes/class_youth_generational_anxiety.py','青年虚无',('青年','虚无','犬儒'), 'library/syntheses/social-phenomena-platform-public-order-synthesis.md','downstream youth-nihilism label; require class/youth support'),
    # Route group 3 — body, psyche, space, risk
    Route('躺平','social-body-psyche-space-risk','psychological-distress-social-symptom','tools/query/themes/psychological_distress_social_symptom.py','躺平',(), 'library/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md','social symptom / withdrawal route; not life advice'),
    Route('抑郁焦虑','social-body-psyche-space-risk','psychological-distress-social-symptom','tools/query/themes/psychological_distress_social_symptom.py','抑郁焦虑',('焦虑','痛苦','绝望'), 'library/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md','not clinical diagnosis; route through anxiety/distress evidence'),
    Route('住房焦虑','social-body-psyche-space-risk','urban-housing-migration-space','tools/query/themes/urban_housing_migration_space.py','住房焦虑',('房子','居住','城市'), 'library/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md','no direct 住房/房价 claim; route through house/dwelling evidence'),
    Route('城市漂泊','social-body-psyche-space-risk','urban-housing-migration-space','tools/query/themes/urban_housing_migration_space.py','城市漂泊',('城市','漂泊','迁移'), 'library/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md','urban/drifting route'),
    Route('医疗焦虑','social-body-psyche-space-risk','health-body-risk-society','tools/query/themes/health_body_risk_society.py','医疗焦虑',('医疗','身体','风险'), 'library/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md','not medical advice; route through medicine/body/risk evidence'),
)

ROUTE_BY_PROMPT = {r.prompt: r for r in ROUTES}


def run_helper(route: Route, term: str, limit: int) -> tuple[int, str, str]:
    cmd = [sys.executable, route.helper, term, '--limit', str(limit)]
    proc = subprocess.run(cmd, cwd=REPO, text=True, capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr


def resolve(query: str) -> Route | None:
    if query in ROUTE_BY_PROMPT:
        return ROUTE_BY_PROMPT[query]
    for route in ROUTES:
        if query in route.prompt or route.prompt in query:
            return route
    for route in ROUTES:
        if query == route.primary or query in route.fallbacks:
            return route
    return None


def route_query(route: Route, limit: int) -> dict:
    tried: list[dict] = []
    for term in (route.primary, *route.fallbacks):
        code, out, err = run_helper(route, term, limit)
        tried.append({'term': term, 'exit': code, 'stdout_lines': len(out.splitlines()), 'stderr': err.strip()})
        if code == 0 and out.strip():
            return {
                'prompt': route.prompt,
                'theme': route.theme,
                'route_group': route.route_group,
                'synthesis': route.synthesis,
                'helper': route.helper,
                'term_used': term,
                'fallback_used': term != route.primary,
                'boundary': route.boundary,
                'stdout': out,
                'tried': tried,
                'ok': True,
            }
    return {
        'prompt': route.prompt,
        'theme': route.theme,
        'route_group': route.route_group,
        'synthesis': route.synthesis,
        'helper': route.helper,
        'term_used': None,
        'fallback_used': False,
        'boundary': route.boundary,
        'stdout': '',
        'tried': tried,
        'ok': False,
    }


def print_result(result: dict, as_json: bool = False) -> None:
    if as_json:
        clean = dict(result)
        if len(clean.get('stdout','')) > 4000:
            clean['stdout'] = clean['stdout'][:4000] + '\n...<truncated>...'
        print(json.dumps(clean, ensure_ascii=False, indent=2))
        return
    print(f"prompt: {result['prompt']}")
    print(f"theme: {result['theme']}")
    print(f"route_group: {result['route_group']}")
    print(f"synthesis: {result['synthesis']}")
    print(f"helper: {result['helper']}")
    print(f"term_used: {result['term_used']}")
    if result['fallback_used']:
        print('fallback: yes — primary downstream label had no direct hit; using evidence-backed fallback term')
    print(f"boundary: {result['boundary']}")
    print('--- evidence route output ---')
    print(result['stdout'].rstrip())


def smoke_all(limit: int, as_json: bool = False) -> int:
    results = [route_query(route, limit) for route in ROUTES]
    failures = [r for r in results if not r['ok']]
    summary = {
        'status': 'PASS' if not failures and len(results) >= 30 else 'FAIL',
        'routes': len(results),
        'fallback_routes': sum(1 for r in results if r['fallback_used']),
        'failures': [{'prompt': r['prompt'], 'tried': r['tried']} for r in failures],
        'prompts': [{'prompt': r['prompt'], 'theme': r['theme'], 'route_group': r['route_group'], 'term_used': r['term_used'], 'fallback_used': r['fallback_used'], 'stdout_lines': len(r['stdout'].splitlines())} for r in results],
    }
    if as_json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"query_social_topics smoke: {summary['status']} routes={summary['routes']} fallback_routes={summary['fallback_routes']} failures={len(failures)}")
        for item in summary['prompts']:
            fb = ' fallback' if item['fallback_used'] else ''
            print(f"- {item['prompt']} -> {item['theme']} term={item['term_used']} lines={item['stdout_lines']}{fb}")
        for failure in summary['failures']:
            print('ERROR', failure)
    return 0 if summary['status'] == 'PASS' else 1


def list_routes(as_json: bool = False) -> None:
    if as_json:
        print(json.dumps([asdict(r) for r in ROUTES], ensure_ascii=False, indent=2))
    else:
        for r in ROUTES:
            print(f"{r.prompt}\t{r.phase}\t{r.theme}\tprimary={r.primary}\tfallbacks={','.join(r.fallbacks)}")


def main() -> int:
    ap = argparse.ArgumentParser(description='Route concrete social-phenomena prompts to ISMISM theme query helpers.')
    ap.add_argument('query', nargs='?', help='Concrete prompt, e.g. 内卷 / 考公热 / 婚恋市场 / 短视频成瘾 / 住房焦虑 / 医疗焦虑')
    ap.add_argument('--limit', type=int, default=3)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--list-routes', action='store_true')
    ap.add_argument('--smoke-all', action='store_true')
    args = ap.parse_args()
    if args.list_routes:
        list_routes(args.json); return 0
    if args.smoke_all:
        return smoke_all(args.limit, args.json)
    if not args.query:
        ap.error('provide a query, --list-routes, or --smoke-all')
    route = resolve(args.query)
    if not route:
        print(f'No social topics router route for {args.query!r}. Use --list-routes.', file=sys.stderr)
        return 2
    result = route_query(route, args.limit)
    print_result(result, args.json)
    return 0 if result['ok'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
