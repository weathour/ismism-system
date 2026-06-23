# Social Structure / Production Relations / Reproduction / Institutional Production Theme Package

- 中文名：社会结构—生产关系—再生产—制度生产主题包
- status: foundational direct-theme package, draft-linked and validator-backed
- date: 2026-06-23 CST
- manifest: `social-structure-production-reproduction-row-manifest.jsonl` (153 reviewed rows)
- evidence bank: `social-structure-production-reproduction-evidence-bank.jsonl` (425 exact quote records)
- taxonomy: `social-structure-production-reproduction-taxonomy.md`
- concept/relation notes: `social-structure-production-reproduction-concept-relation-notes.md`
- validator: `python3 tools/validate/themes/social_structure_production_reproduction.py --repo . --final`
- query helper: `python3 tools/query/themes/social_structure_production_reproduction.py 生产关系 --limit 3`

This layer is **not** an external encyclopedia of sociology, political economy, constitutional history, policy, or current events. It absorbs how ISMISM internally makes social structure, production relations, social reproduction, state/bureaucratic form, class mobility, space, education, finance, consumption, and transformative practice usable as a single corpus-traceable diagnostic theme.

## Central question

当一个社会的生产活动、生产关系和再生产机制发生变化时，哪些制度、阶级、空间、教育、家庭、市场、金融和合法性形式会把旧关系维持下来，哪些实践入口又可能把它们重新组织？

## Counts

| Item | Count |
|---|---:|
| reviewed manifest rows | 153 |
| exact quote records | 425 |
| core rows | 109 |
| bridge rows | 34 |
| excluded/boundary rows | 10 |

## Theme classes

| theme_class | 定义 | rows | evidence |
|---|---|---:|---:|
| `theory-method-political-economy` | 把社会结构读成历史化的政治经济关系，而不是抽象伦理或单一朝代/政策叙事。 | 9 | 27 |
| `production-relations-institutional-form` | 把生产力、生产活动、生产关系与组织/制度形式放在同一诊断链条中。 | 7 | 21 |
| `labor-process-alienation-work-discipline` | 把劳动过程、异化、指标纪律和剥削作为生产关系在主体身上的显影。 | 12 | 34 |
| `social-reproduction-family-life` | 把家庭、性别分工、照护、生育、生活必需品和日常维持视为社会关系再生产机制。 | 18 | 52 |
| `state-bureaucracy-legitimacy` | 把国家机器、官僚、法律、规则、秩序和合法性视为生产/再生产关系的制度载体。 | 20 | 60 |
| `class-structure-mobility` | 把阶级、阶层、贫富、通道堵塞、羞辱和中产焦虑读成结构位置的再生产。 | 18 | 52 |
| `spatial-infrastructure-migration` | 把城乡、住房、迁移、空间和基础设施纳入生产关系的地域化/去地域化过程。 | 16 | 44 |
| `ideology-culture-education-reproduction` | 把教育、知识权威、文化和意识形态作为制度化再生产的软载体。 | 18 | 52 |
| `finance-capital-abstraction-deagency` | 把金融、信用、货币、资本抽象和代理控制作为生产关系的高阶中介。 | 5 | 15 |
| `market-consumption-lifestyle-reproduction` | 把市场、商品、消费、生活方式和必需/奢侈区分作为再生产的日常界面。 | 12 | 36 |
| `practice-socialization-transformation` | 把实践、资本社会化、组织经济生活和替代性制度设计作为解放出口。 | 8 | 22 |
| `boundary-keyword-only` | 关键词命中但不支撑本主题主张的边界样本，用于防止泛化。 | 10 | 10 |

## Query examples

```bash
python3 tools/query/themes/social_structure_production_reproduction.py 生产关系 --limit 3
python3 tools/query/themes/social_structure_production_reproduction.py --row 331
python3 tools/query/themes/social_structure_production_reproduction.py --class social-reproduction-family-life --limit 5
```

## Interpretation rules

1. Start from this manifest and evidence bank; do not treat `生产`, `制度`, `社会`, or `国家` keyword presence as sufficient evidence.
2. Keep source-backed claims separate from inference. Every close interpretation should cite row ids or `ev:sspr:*` evidence ids.
3. Treat institutions as carriers of production/reproduction relations only where row-level evidence supports the bridge.
4. This package is a foundational direct-theme helper, not yet a `query social` route.
5. Do not import external historical claims, current policy judgments, or professional advice into this theme.

## Cross-theme donor surfaces

This package absorbs and cross-indexes exact-quote evidence from Capitalism, Labor, Governance/Law/Bureaucracy, Family/Intimacy/Reproduction, Feminism, Class/Youth, Urban/Housing/Migration, Education/Credentialism, and Consumption/Desire/Lifestyle theme packages. Donor rows remain owned by their original themes; this package records their structural relation function.
