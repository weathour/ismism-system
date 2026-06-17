# W8 Query Playbook

- status: draft protocol
- created: 2026-06-09 CST
- scope: standard paths for common ISMISM knowledge queries.

## 1. “What does a term mean here?”

Path:

```text
term-senses.jsonl → core-terms.md → evidence quote in split_md_clean → optional synthesis
```

Example: `星丛` → `term:星丛:s01/s02` → row 229 → `part-3-idealism.md`.

Optional CLI:

```bash
python3 knowledge/scripts/query_term.py 星丛
python3 knowledge/scripts/trace_evidence.py term:星丛:s01
```

## 2. “Which sense of this term is used in this row?”

Path:

```text
row_id → segment card → term-senses filtered by source_segments.row_id → compare definitions
```

Example: row 285 → `学习`, `研究`, `现实理论化`, `可行性`.

## 3. “Where is a doctrine located in the matrix?”

Path:

```text
目录索引_结构化.csv → position card coordinate → segment card → W3 terms
```

Example: `静止的事件主义` → `3-4-2-2.md` → row 263 terms.

Optional CLI:

```bash
python3 knowledge/scripts/query_position.py 3-4-2
python3 knowledge/scripts/query_position.py 后结构主义
```

## 4. “How does one mechanism move into another?”

Path:

```text
relation-assets.jsonl → relation_type → source/target senses → evidence_segment
```

Example: objectification/subjectivization routes → W5 `objectifies` / `subjectivizes` records.

Optional CLI:

```bash
python3 knowledge/scripts/query_relation.py --type objectifies
python3 knowledge/scripts/query_relation.py --relation-id rel:w5b1:001
```

## 5. “What is the difference between two similar terms?”

Path:

```text
term-senses for both terms → forbidden_mix fields → ambiguous-terms.md → evidence rows
```

Example: `星丛` vs `星座`; `site` vs `position`; `数学化` vs `数学知识`.

## 6. “Can I use a synthesis directly?”

Path:

```text
synthesis claim → source tag → W3/W4/W5 record → clean row
```

Rule: synthesis is a map, not a source of independent claims.

## 7. “Is this relation too strong?”

Path:

```text
relation record → applicability_boundary → forbidden_interpretation → W6 evidence-claim-audit.md
```

Rule: do not generalize a relation beyond its row and position boundary.

## 8. “Is this term safe to use in a new synthesis?”

Path:

```text
term-senses → ambiguous-terms.md → concept-drift-report.md → source row
```

Rule: if the term has multiple senses, cite the exact sense ID.

## 9. “How do I answer a field overview question?”

Path:

```text
part-N synthesis → field position card → representative W3 terms → W5 relations
```

Example: field 4 overview → `part-4-praxis.md` → `4.md` → row 285 terms.

## 10. “How do I trace an evidence quote?”

Path:

```text
sense_id or relation_id → evidence row → segments.jsonl clean_md_path → exact substring check
```

Use `validate_w3_term_senses.py` or `validate_w5_relation_assets.py` when possible.

Optional CLI:

```bash
python3 knowledge/scripts/trace_evidence.py term:主体:s01
python3 knowledge/scripts/trace_evidence.py rel:w5b1:001
python3 knowledge/scripts/trace_evidence.py 276
```

## 11. “How do I add a new term sense?”

Path:

```text
candidate term → exact source row quotes → source_segments metadata → draft JSONL record → batch validation → audit note
```

Minimum: 2 exact quotes, valid axis, `forbidden_mix`, status `draft`.

## 12. “How do I resume the project?”

Path:

```text
ISMISM-MAINLINE-HANDOFF.md → knowledge/STATE.md → knowledge/DIGESTION_PROGRAM.md → latest operation-log entry
```

Then run W3/W4/W5 validators before editing.

## 13. “How do I query the AI / VR / 智能 theme?”

Path:

```text
knowledge/themes/ai/ai-row-manifest.jsonl
→ knowledge/themes/ai/ai-evidence-bank.jsonl
→ AI W3 senses / AI W5 relations / W10 AI cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_ai_theme.py AI身体化
python3 knowledge/scripts/query_ai_theme.py 强AI
python3 knowledge/scripts/query_ai_theme.py AI可朽性
python3 knowledge/scripts/query_ai_theme.py --row 360
```

Rule: the AI theme layer is a maximum-absorption index/synthesis surface, not a canonical source above corpus evidence. Treat W3/W5 AI additions as `draft` and W10 AI cards as `pilot-draft`.

## 14. “How do I query the Chinese Philosophy theme?”

Path:

```text
knowledge/themes/chinese-philosophy/chinese-philosophy-row-manifest.jsonl
→ knowledge/themes/chinese-philosophy/chinese-philosophy-evidence-bank.jsonl
→ Chinese W3 senses / Chinese W5 relations / W10 cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3
python3 knowledge/scripts/query_chinese_philosophy_theme.py --row 131
python3 knowledge/scripts/query_chinese_philosophy_theme.py --class buddhist-chan-bridge
```

Rule: the Chinese Philosophy theme layer is a maximum-absorption index/synthesis surface, not a neutral encyclopedia or a source above corpus evidence. W3/W5 records remain `draft`; W10 remains `pilot-draft`.

## 15. “How do I query the Religion Problem / 宗教问题 theme?”

Path:

```text
knowledge/themes/religion/religion-row-manifest.jsonl
→ knowledge/themes/religion/religion-evidence-bank.jsonl
→ Religion W3 senses / Religion W5 relations / W10 Religion cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3
python3 knowledge/scripts/query_religion_theme.py 偶像 --limit 3
python3 knowledge/scripts/query_religion_theme.py --row 45
python3 knowledge/scripts/query_religion_theme.py --class buddhist-liberation-bridge
```

Rule: the Religion Problem layer is a maximum-absorption index/synthesis surface, not a neutral religious-studies encyclopedia or a source above corpus evidence. W3/W5 records remain `draft`; W10 remains `pilot-draft`.

## 16. “How do I query the Time / Death / Finitude / Life theme?”

中文主题名：时间 / 死亡 / 有限性 / 生命。

Path:

```text
knowledge/themes/time-death-finitude-life/time-death-row-manifest.jsonl
→ knowledge/themes/time-death-finitude-life/time-death-evidence-bank.jsonl
→ Time-Death-Life W3 senses / W5 relations / W10 coverage
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_time_death_theme.py 时间 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 死亡 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 生命 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 永生 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 有限 --limit 3
python3 knowledge/scripts/query_time_death_theme.py --class ai-immortality-mortality
```

Rule: the Time-Death-Finitude-Life layer is a maximum-absorption index/synthesis surface, not a neutral time/death/life encyclopedia. W3/W5 records remain `draft`; W10 remains `pilot-draft`.
## 17. “How do I query the Capitalism / Political Economy theme?”

中文主题名：资本主义 / 政治经济 / 生产关系。

Path:

```text
knowledge/themes/capitalism/capitalism-row-manifest.jsonl
→ knowledge/themes/capitalism/capitalism-evidence-bank.jsonl
→ Capitalism W3 senses / W5 relations / W10 Capitalism cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_capitalism_theme.py 资本主义 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 资本 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 生产关系 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 拜物教 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 金融 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 帝国主义 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 异化 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 消费 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py --class production-relations-forces
```

Rule: the Capitalism / Political Economy layer is a maximum-absorption index/synthesis surface, not a neutral capitalism, Marxism, economics, or political-theory encyclopedia. W3/W5 records remain `draft`; W10 remains `pilot-draft`.

<!-- FEMINISM-THEME-START:NAV -->
## Feminism / Gender / Sexuality / Social Reproduction maximum absorption — 2026-06-16

- `knowledge/themes/feminism/README.md` — Feminism / Gender / Sexuality / Social Reproduction maximum absorption layer.
- `knowledge/themes/feminism/feminism-row-manifest.jsonl` — 94 reviewed rows.
- `knowledge/themes/feminism/feminism-evidence-bank.jsonl` — 309 exact-substring quotes.
- `knowledge/scripts/validate_feminism_theme.py --repo . --final` — final validator.
- `knowledge/scripts/query_feminism_theme.py 女权 --limit 3` — query helper.
- Query scope marker: 女权 / 性别 / 身体 / 社会再生产.
- Global current counts: 1316 W3 draft senses / 911 terms; 724 W5 draft relations; 501 W10 pilot-draft cards.
- Current validator markers: 1316 senses / 911 terms; 724 relations / 12 types; 501 cards / 3 card types; 258 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 724`.
<!-- FEMINISM-THEME-END:NAV -->

## Aesthetics / Art / Media / Image / Narrative maximum absorption — 2026-06-16

Use for film-analysis precursor queries: 电影 / 影像 / 观看 / 美学 / 艺术 / 诗 / 小说 / 叙事 / 文本 / 符号 / 媒介.

```bash
python3 knowledge/scripts/query_aesthetics_media_theme.py 电影 --limit 3
python3 knowledge/scripts/query_aesthetics_media_theme.py 叙事 --limit 3
python3 knowledge/scripts/query_aesthetics_media_theme.py 美学 --limit 3
python3 knowledge/scripts/query_aesthetics_media_theme.py --row 259
python3 knowledge/scripts/query_aesthetics_media_theme.py --class categorical-narratology
```

Start at `knowledge/themes/aesthetics-media/aesthetics-media-row-manifest.jsonl` and then inspect `knowledge/themes/aesthetics-media/aesthetics-media-evidence-bank.jsonl`; do not treat it as a finished film-analysis matrix.

Aesthetics-Media short scope marker: 电影 / 影像 / 美学 / 叙事.

## Labor / Workplace / Precarity social phenomena queries — 2026-06-16

- Theme path: `knowledge/themes/labor-workplace-precarity/`
- Protocol: `knowledge/references/social-phenomena-diagnostic-protocol.md`
- Query helper: `python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 内卷 --limit 3`
- Short scope marker: 劳动 / 职场 / 内卷 / 不稳定生活 / 绩效 / 指标 / 失业焦虑.
- Use route: manifest → evidence bank → W3 draft senses → W5 draft relations → W10 pilot-draft cards → synthesis.

Examples:

```bash
python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 内卷 --limit 3
python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 绩效 --limit 3
python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 失业焦虑 --limit 3
python3 knowledge/scripts/query_labor_workplace_precarity_theme.py --class work-discipline-metrics --limit 3
```


## Education / Examination / Credentialism queries

- Start at `knowledge/themes/education-examination-credentialism/README.md`.
- Query helper: `python3 knowledge/scripts/query_education_examination_credentialism_theme.py 考试 --limit 3`.
- Validator: `python3 knowledge/scripts/validate_education_examination_credentialism_theme.py --repo . --final`.
- Scope marker: 教育 / 考试 / 学历 / 应试 / 文凭 / 分数 / 学校 / 学生 / 教师 / 专家 / 学术等级 / 知识规训.
- Current validator markers: 1316 senses / 911 terms; 724 relations / 12 types; 501 cards / 3 card types; 258 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 724`.


## Family / Intimacy / Marriage / Birth / Social Reproduction

- Query helper: `python3 knowledge/scripts/query_family_intimacy_reproduction_theme.py 家庭 --limit 3`
- Scope: 家庭 / 婚姻 / 亲密关系 / 生育 / 父母 / 孩子 / 儿童 / 爱情 / 父权 / 夫权 / 族权 / 家务 / 社会再生产.
- Boundary: no unsupported 彩礼-specific claim; use exact evidence rows and theme classes.
- Global current counts: 1361 W3 draft senses / 952 terms; 764 W5 draft relations; 531 W10 pilot-draft cards.
- Current validator markers: 1361 senses / 952 terms; 764 relations / 12 types; 531 cards / 3 card types; 259 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 764`.

## Consumption / Desire / Commodity / Lifestyle

- Query helper: `python3 knowledge/scripts/query_consumption_desire_lifestyle_theme.py 消费主义 --limit 3`
- Scope: 消费 / 消费主义 / 欲望 / 商品 / 生活方式 / 情绪消费 / 身份消费 / 奢侈品 / 品牌 / 自我品牌化 / 市场享乐.
- Boundary: `情绪消费`, `身份消费`, and `自我品牌化` are query-facing diagnostic labels backed by adjacent corpus wording; do not make unsupported current-events claims.
- Global current counts: 1406 W3 draft senses / 990 terms; 804 W5 draft relations; 561 W10 pilot-draft cards.
- Current validator markers: 1406 senses / 990 terms; 804 relations / 12 types; 561 cards / 3 card types; 260 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 804`.


## Media / Platform / Public Opinion / Traffic Society

```bash
python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 平台 --limit 3
python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 舆论 --limit 3
python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 流量 --limit 3
```

Scope marker: 媒介 / 平台 / 舆论 / 流量 / 短视频 / 直播 / 网红 / 粉丝 / 偶像 / 注意力 / 算法 / 数据 / 推荐 / 网络犬儒. Exact `热搜` and `饭圈` are downstream labels only unless future row evidence is added.

## Current global media-platform checkpoint markers

- Global current counts: 1451 W3 draft senses / 1035 terms; 844 W5 draft relations; 591 W10 pilot-draft cards.
- Global current counts: 1496 W3 draft senses / 1076 terms; 884 W5 draft relations; 621 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
## Governance / Law / Bureaucracy / Order

```bash
python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 治理 --limit 3
python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 官僚 --limit 3
python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 规则拜物 --limit 3
```

Scope: 治理 / 法律 / 法治 / 法权 / 官僚 / 科层 / 秩序 / 行政 / 制度 / 规则 / 纪律 / 服从 / 命令 / 风险 / 安全 / 审判 / 正义.

- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.


## Class / Youth / Generation / Mobility Anxiety

```bash
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 阶层 --limit 3
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 青年 --limit 3
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 底层羞辱 --limit 3
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 成功学 --limit 3
```

Scope: 阶层 / 青年 / 代际 / 上升通道 / 中产焦虑 / 底层羞辱 / 成功学 / 阶层固化 / 青年虚无 / 贫富差异.

Path:

```text
knowledge/themes/class-youth-generational-anxiety/class-youth-generational-anxiety-row-manifest.jsonl
→ class-youth-generational-anxiety-evidence-bank.jsonl
→ Class-youth W3 draft senses / W5 draft relations / W10 Class-youth cards
→ split_md_clean exact quote
```

Boundary: this is a corpus-grounded diagnostic theme for class/youth/mobility anxiety, not an external sociology/current-events commentary layer. W3/W5 remain `draft`; W10 remains `pilot-draft`.

- Global current counts: 1541 W3 draft senses / 1116 terms; 924 W5 draft relations; 651 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.


## Psychological Distress / Anxiety / Addiction / Social Symptom

```bash
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 焦虑 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 成瘾 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 症状 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 压抑 --limit 3
```

Scope: 心理困境 / 焦虑 / 抑郁 / 成瘾 / 社会症状 / 虚无 / 躺平 / 内耗 / 心理咨询 / 痛苦 / 绝望 / 犬儒 / 享乐 / 欲望 / 压抑 / 创伤.

Path:

```text
knowledge/themes/psychological-distress-social-symptom/psychological-distress-social-symptom-row-manifest.jsonl
→ psychological-distress-social-symptom-evidence-bank.jsonl
→ Psychological-distress W3 draft senses / W5 draft relations / W10 cards
→ split_md_clean exact quote
```

Boundary: this is a corpus-grounded social-symptom layer, not clinical diagnosis, therapy advice, psychiatry, medication guidance, or current-events mental-health commentary.

- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Urban / Housing / Migration / Space

- Scope: 城市 / 住房 / 房子 / 迁徙 / 城乡差异 / 公共空间 / 空间阶层化 / 城市漂泊.
- Query: `python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 城市 --limit 3`.
- Boundary: `住房` / `租房` / `房价` / `户籍` are downstream labels when exact terms are absent; require row evidence.

## Health / Body / Medicine / Risk Society

- Scope: 医疗 / 身体 / 健康 / 疾病 / 风险 / 医疗化 / 健康主义 / 疫情记忆 / 身体治理 / 疾病污名.
- Query: `python3 knowledge/scripts/query_health_body_risk_society_theme.py 身体 --limit 3`.
- Boundary: no medical advice, diagnosis, treatment, public-health guidance, or current-event policy claims.

## Social Phenomena Superphase — Phase 1 everyday life reproduction routes

Use `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` when a query crosses labor, credentialing, family/intimacy, and consumption. The Phase 1 question is: **How do labor, credentialing, family, and consumption reproduce everyday subjectivity?**

Route:

1. Labor/workplace: `query_labor_workplace_precarity_theme.py` for 内卷 / 打工人 / 绩效 / 加班 / 失业焦虑.
2. Education/credentialing: `query_education_examination_credentialism_theme.py` for 考试 / 考研 / 学历崇拜 / 专家崇拜 / 鸡娃.
3. Family/reproduction: `query_family_intimacy_reproduction_theme.py` for 家庭 / 婚恋市场 / 生育焦虑 / 父母控制 / 爱情意识形态.
4. Consumption/desire: `query_consumption_desire_lifestyle_theme.py` for 消费主义 / 情绪消费 / 身份消费 / 奢侈品 / 自我品牌化.

Smoke commands:

```bash
python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 内卷 --limit 3
python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 打工人 --limit 3
python3 knowledge/scripts/query_education_examination_credentialism_theme.py 考研 --limit 3
python3 knowledge/scripts/query_education_examination_credentialism_theme.py 学历 --limit 3
python3 knowledge/scripts/query_family_intimacy_reproduction_theme.py 婚恋 --limit 3
python3 knowledge/scripts/query_family_intimacy_reproduction_theme.py 生育 --limit 3
python3 knowledge/scripts/query_consumption_desire_lifestyle_theme.py 消费主义 --limit 3
python3 knowledge/scripts/query_consumption_desire_lifestyle_theme.py 情绪消费 --limit 3
```

Boundary: Phase 1 is a synthesis route over existing row/quote-backed theme layers, not a new evidence layer and not current-events commentary. W3/W5 remain `draft`; W10 remains `pilot-draft`.

## Social Phenomena Superphase — Phase 2 platform / public order / class routes

Use `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` when a query crosses platform visibility, public affect, institutional order, and class/youth anxiety. The Phase 2 question is: **How do private suffering, public affect, platform visibility, institutional order, and class anxiety mediate each other?**

Route:

1. Media/platform: `query_media_platform_public_opinion_theme.py` for 平台 / 舆论 / 流量 / 短视频成瘾 / 直播 / 热搜舆论 / 网红.
2. Governance/order: `query_governance_law_bureaucracy_theme.py` for 治理 / 官僚手续 / 法律意识 / 规则拜物 / 风险管理.
3. Class/youth: `query_class_youth_generational_anxiety_theme.py` for 中产焦虑 / 青年虚无 / 阶层固化 / 底层羞辱 / 贫富差异.

Smoke commands:

```bash
python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 平台 --limit 3
python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 舆论 --limit 3
python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 直播 --limit 3
python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 治理 --limit 3
python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 官僚 --limit 3
python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 法律 --limit 3
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 阶层 --limit 3
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 青年 --limit 3
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 中产焦虑 --limit 3
```

Boundary: Phase 2 is a synthesis route over existing row/quote-backed theme layers, not a current platform/news/legal commentary layer. W3/W5 remain `draft`; W10 remains `pilot-draft`.

## Social Phenomena Superphase — Phase 3 body / psyche / space / risk routes

Use `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` when a query crosses psychological distress, spatial position, bodily vulnerability, medical naming, and risk consciousness. The Phase 3 question is: **How do social contradictions sediment into body, psyche, spatial life, and risk consciousness?**

Route:

1. Psychological distress: `query_psychological_distress_social_symptom_theme.py` for 抑郁焦虑 / 躺平 / 内耗 / 成瘾 / 社会矛盾私人化.
2. Urban/housing/space: `query_urban_housing_migration_space_theme.py` for 住房焦虑 / 房子 / 城市漂泊 / 迁徙 / 公共空间 / 城乡差异.
3. Health/body/risk: `query_health_body_risk_society_theme.py` for 医疗焦虑 / 身体 / 健康 / 疾病 / 风险 / 身体治理.

Smoke commands:

```bash
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 焦虑 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 成瘾 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 躺平 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 城市 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 房子 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 迁移 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 身体 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 医疗 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 风险 --limit 3
```

Boundary: Phase 3 is a synthesis route over existing row/quote-backed theme layers, not clinical advice, therapy guidance, medical guidance, housing advice, or current-events commentary. W3/W5 remain `draft`; W10 remains `pilot-draft`.

## Social Phenomena Superphase — final query router and smoke matrix

Use `knowledge/scripts/query_social_phenomena_superphase.py` for concrete everyday social-phenomenon prompts that may need phase routing and fallback terms. It covers 30 smoke prompts across Phase 1, Phase 2, and Phase 3.

```bash
python3 knowledge/scripts/query_social_phenomena_superphase.py 内卷 --limit 3
python3 knowledge/scripts/query_social_phenomena_superphase.py 考公热 --limit 3
python3 knowledge/scripts/query_social_phenomena_superphase.py 婚恋市场 --limit 3
python3 knowledge/scripts/query_social_phenomena_superphase.py 短视频成瘾 --limit 3
python3 knowledge/scripts/query_social_phenomena_superphase.py 住房焦虑 --limit 3
python3 knowledge/scripts/query_social_phenomena_superphase.py 医疗焦虑 --limit 3
python3 knowledge/scripts/query_social_phenomena_superphase.py --smoke-all --limit 1
```

Thirty-prompt coverage: 内卷 / 打工人 / 加班 / 绩效 / 失业焦虑 / 考公热 / 考研 / 学历崇拜 / 鸡娃 / 专家崇拜 / 婚恋市场 / 彩礼 / 生育焦虑 / 父母控制 / 消费主义 / 情绪消费 / 奢侈品 / 短视频成瘾 / 直播 / 热搜舆论 / 网红 / 官僚手续 / 法律意识 / 中产焦虑 / 青年虚无 / 躺平 / 抑郁焦虑 / 住房焦虑 / 城市漂泊 / 医疗焦虑.

Audit: `knowledge/qa/social-phenomena-superphase-audit.md`. Validator: `knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final`. Boundary: downstream labels use fallback terms when exact corpus hits are absent; no current-events commentary; W3/W5 remain `draft`; W10 remains `pilot-draft`.
