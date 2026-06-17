# Social Phenomena Superphase Audit
- status: G035 validation/query audit
- date: 2026-06-16 CST
- scope: 现实社会现象与问题最大吸收超阶段
- method: `knowledge/references/social-phenomena-diagnostic-protocol.md`
- query layer: `knowledge/scripts/query_social_phenomena_superphase.py`
- validator: `knowledge/scripts/validate_social_phenomena_superphase.py`
- current markers: W3 1676 draft senses / 1228 terms; W5 1044 draft relations / 12 types; W10 741 pilot-draft cards / 3 card types; full W3+W5+W10 overlap 277 rows.

## Superphase assets

- `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md`
- `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md`
- `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md`

## Ten social-phenomena theme layers

- `knowledge/themes/labor-workplace-precarity/`
- `knowledge/themes/education-examination-credentialism/`
- `knowledge/themes/family-intimacy-reproduction/`
- `knowledge/themes/consumption-desire-lifestyle/`
- `knowledge/themes/media-platform-public-opinion/`
- `knowledge/themes/governance-law-bureaucracy/`
- `knowledge/themes/class-youth-generational-anxiety/`
- `knowledge/themes/psychological-distress-social-symptom/`
- `knowledge/themes/urban-housing-migration-space/`
- `knowledge/themes/health-body-risk-society/`

## Thirty prompt smoke routes

| Prompt | Phase | Theme | Primary term | Evidence fallback terms | Synthesis | Boundary |
|---|---|---|---|---|---|---|
| 内卷 | Phase 1 — everyday life reproduction | `labor-workplace-precarity` | 内卷 | — | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | metric discipline / involution route; avoid generic competition moralism |
| 打工人 | Phase 1 — everyday life reproduction | `labor-workplace-precarity` | 打工人 | 劳动, 工作 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream labor-subject label; inspect exact labor/work evidence |
| 加班 | Phase 1 — everyday life reproduction | `labor-workplace-precarity` | 加班 | 工作, 劳动 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream workload label; do not infer labor law/policy claims |
| 绩效 | Phase 1 — everyday life reproduction | `labor-workplace-precarity` | 绩效 | 指标, 排名 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | metric/priceability route |
| 失业焦虑 | Phase 1 — everyday life reproduction | `labor-workplace-precarity` | 失业焦虑 | 失业, 焦虑 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | precarity/anxiety bridge; not labor-market statistics |
| 考公热 | Phase 1 — everyday life reproduction | `education-examination-credentialism` | 考公热 | 考试, 资格, 文凭 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream civil-service-exam label; use exam/credential evidence only |
| 考研 | Phase 1 — everyday life reproduction | `education-examination-credentialism` | 考研 | 考试, 学习, 学历 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream exam route; do not infer contemporary admissions facts |
| 学历崇拜 | Phase 1 — everyday life reproduction | `education-examination-credentialism` | 学历崇拜 | 学历, 文凭, 资格 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | credential fantasy route |
| 鸡娃 | Phase 1 — everyday life reproduction | `education-examination-credentialism` | 鸡娃 | 教育, 儿童, 学习 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream parenting/education pressure label; bridge to Family only with evidence |
| 专家崇拜 | Phase 1 — everyday life reproduction | `education-examination-credentialism` | 专家崇拜 | 专家, 权威, 学术 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | expert authority / knowledge legitimacy route |
| 婚恋市场 | Phase 1 — everyday life reproduction | `family-intimacy-reproduction` | 婚恋市场 | 婚恋, 婚姻, 爱情 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream marketized-intimacy label; inspect family/intimacy evidence |
| 彩礼 | Phase 1 — everyday life reproduction | `family-intimacy-reproduction` | 彩礼 | 婚姻, 家庭, 婚恋 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | no direct 彩礼 claim in theme; route through marriage/family evidence only |
| 生育焦虑 | Phase 1 — everyday life reproduction | `family-intimacy-reproduction` | 生育焦虑 | 生育, 孩子, 再生产 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | reproduction/future route; no demographic policy claim |
| 父母控制 | Phase 1 — everyday life reproduction | `family-intimacy-reproduction` | 父母控制 | 父母, 家庭, 孩子 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | parent/child authority route |
| 消费主义 | Phase 1 — everyday life reproduction | `consumption-desire-lifestyle` | 消费主义 | — | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | consumerism / enjoyment quantification route |
| 情绪消费 | Phase 1 — everyday life reproduction | `consumption-desire-lifestyle` | 情绪消费 | 消费主义, 享乐, 欲望 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | downstream label; use consumption/desire evidence |
| 奢侈品 | Phase 1 — everyday life reproduction | `consumption-desire-lifestyle` | 奢侈品 | 奢侈, 品牌, 消费 | `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` | lifestyle / identity consumption route |
| 短视频成瘾 | Phase 2 — platform / public order / class | `media-platform-public-opinion` | 短视频成瘾 | 短视频, 成瘾, 平台 | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | downstream platform-addiction label; bridge platform and psychological routes only with evidence |
| 直播 | Phase 2 — platform / public order / class | `media-platform-public-opinion` | 直播 | — | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | live-stream platform route |
| 热搜舆论 | Phase 2 — platform / public order / class | `media-platform-public-opinion` | 热搜舆论 | 舆论, 公共话语, 流量 | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | no direct 热搜 claim; route through public-opinion/traffic evidence |
| 网红 | Phase 2 — platform / public order / class | `media-platform-public-opinion` | 网红 | — | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | influencer/celebrity visibility route |
| 官僚手续 | Phase 2 — platform / public order / class | `governance-law-bureaucracy` | 官僚手续 | 官僚, 手续, 程序 | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | bureaucracy/procedure route; not legal advice |
| 法律意识 | Phase 2 — platform / public order / class | `governance-law-bureaucracy` | 法律意识 | 法律, 法, 权利 | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | law/rights/legalism route; not legal advice |
| 中产焦虑 | Phase 2 — platform / public order / class | `class-youth-generational-anxiety` | 中产焦虑 | — | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | middle-class anxiety route |
| 青年虚无 | Phase 2 — platform / public order / class | `class-youth-generational-anxiety` | 青年虚无 | 青年, 虚无, 犬儒 | `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` | downstream youth-nihilism label; require class/youth support |
| 躺平 | Phase 3 — body / psyche / space / risk | `psychological-distress-social-symptom` | 躺平 | — | `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` | social symptom / withdrawal route; not life advice |
| 抑郁焦虑 | Phase 3 — body / psyche / space / risk | `psychological-distress-social-symptom` | 抑郁焦虑 | 焦虑, 痛苦, 绝望 | `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` | not clinical diagnosis; route through anxiety/distress evidence |
| 住房焦虑 | Phase 3 — body / psyche / space / risk | `urban-housing-migration-space` | 住房焦虑 | 房子, 居住, 城市 | `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` | no direct 住房/房价 claim; route through house/dwelling evidence |
| 城市漂泊 | Phase 3 — body / psyche / space / risk | `urban-housing-migration-space` | 城市漂泊 | 城市, 漂泊, 迁移 | `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` | urban/drifting route |
| 医疗焦虑 | Phase 3 — body / psyche / space / risk | `health-body-risk-society` | 医疗焦虑 | 医疗, 身体, 风险 | `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` | not medical advice; route through medicine/body/risk evidence |

## Smoke command

```bash
python3 knowledge/scripts/query_social_phenomena_superphase.py --smoke-all --limit 1
```

Expected current result: `PASS routes=30 fallback_routes=19 failures=0`. Fallback routes are intentional: downstream social labels such as `考公热`, `彩礼`, `热搜舆论`, `住房焦虑`, and `医疗焦虑` are not treated as direct corpus hits when exact evidence is absent; they are routed through declared evidence-backed adjacent terms.

## Validation command

```bash
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```

The final validator checks superphase artifacts, 30 query routes, all social-phenomena theme validators, pre-existing theme validators, W3/W5/W10 validators, Universal-A/B, master validator, current marker presence, `git diff --check`, and protected corpus diff.

## Boundary

- This audit does not create a neutral sociology encyclopedia.
- It does not add W3/W5/W10 records. W3/W5 remain `draft`; W10 remains `pilot-draft`.
- It does not modify `split_md/` or `split_md_clean/`.
- It does not support current-events commentary, clinical advice, legal advice, medical advice, housing advice, or policy recommendation.
