---
name: ismism-knowledge-operator
description: Operate the standalone ISMISM knowledge-processing repository. Use when Codex is working in or from `ismism-system` to answer ISMISM questions, inspect terms/positions/relations, extend the knowledge layer, validate outputs, design external references, or avoid legacy frontend/Atlas misuse while preserving row, segment, and quote traceability.
---

# ISMISM Knowledge Operator

## Core stance

Treat `ismism-system` as a corpus-backed theory-processing repo, not a normal wiki, frontend app, or generic philosophy encyclopedia. Preserve row / segment / quote traceability before interpretation.

## Read first

When starting in this repo, read only what the task needs, but use this order:

1. `AGENTS.md`
2. `README.md`
3. `DIRECTORY_MAP.md`
4. `ISMISM-MAINLINE-HANDOFF.md`
5. `knowledge/STATE.md`
6. `knowledge/usage-protocol.md` and `knowledge/query-playbook.md` for query tasks
7. `knowledge/references/social-phenomena-diagnostic-protocol.md` and `knowledge/scripts/query_social_phenomena_superphase.py --list-routes` for everyday social-phenomenon tasks
8. `knowledge/export-manifest.md` for external-consumer tasks
9. `knowledge/w10-absorption/PLAN.md` and `knowledge/w10-absorption/index.md` for further-absorption tasks
10. `knowledge/themes/ai/README.md` and `knowledge/themes/ai/ai-synthesis.md` for AI / VR / 智能 / 算法 / 机器人 theme tasks
11. `knowledge/themes/chinese-philosophy/README.md` and `knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md` for Chinese Philosophy theme tasks
12. `knowledge/themes/religion/README.md` and `knowledge/themes/religion/religion-synthesis.md` for Religion Problem / 宗教问题 theme tasks
13. `knowledge/themes/time-death-finitude-life/README.md` and `knowledge/themes/time-death-finitude-life/time-death-finitude-life-synthesis.md` for Time-Death-Finitude-Life / 时间-死亡-有限性-生命 theme tasks
14. `knowledge/themes/capitalism/README.md` and `knowledge/themes/capitalism/capitalism-critique-and-fetishism-synthesis.md` for Capitalism / Political Economy / 资本主义 / 政治经济 / 生产关系 theme tasks
15. `knowledge/themes/aesthetics-media/README.md` and `knowledge/themes/aesthetics-media/film-analysis-precursor-synthesis.md` for Aesthetics / Art / Media / Image / Narrative / 电影 / 影像 / 美学 / 叙事 theme tasks
16. `knowledge/themes/class-youth-generational-anxiety/README.md` and `knowledge/themes/class-youth-generational-anxiety/class-youth-generational-anxiety-synthesis.md` for Class / Youth / Generation / Mobility Anxiety / 阶层 / 青年 / 代际 theme tasks
17. `knowledge/themes/psychological-distress-social-symptom/README.md` and `knowledge/themes/psychological-distress-social-symptom/psychological-distress-social-symptom-synthesis.md` for Psychological Distress / Anxiety / Addiction / Social Symptom / 心理困境 / 焦虑 / 成瘾 theme tasks
18. `knowledge/qa/universal-absorption-phase-b-plan.md`, `knowledge/qa/universal-absorption-phase-b-gap-map.jsonl`, and `knowledge/qa/universal-absorption-phase-b-evidence-bank.jsonl` for Universal Absorption Phase B / 普遍性吸收第二阶段 row-level repair tasks
19. `knowledge/qa/universal-absorption-phase-a-plan.md`, `knowledge/qa/universal-absorption-phase-a-gap-map.jsonl`, and `knowledge/qa/universal-absorption-phase-a-evidence-bank.jsonl` for Universal Absorption Phase A / 普遍性吸收第一阶段 row-level repair tasks

For matrix movement or relation interpretation, also read `knowledge/references/movement-patterns-guide.md`.

## Source priority

When sources disagree, prefer:

1. `目录索引_结构化.csv`
2. `split_md/` and `split_md_clean/`
3. `knowledge/manifests/*`
4. `knowledge/segment-cards/*`
5. `knowledge/lexicon/*`
6. `knowledge/position-cards/*`
7. `knowledge/relations/*`
8. `knowledge/qa/*`
9. `knowledge/syntheses/*`
10. `knowledge/w10-absorption/*` as pilot-draft close-reading aids
11. `Zhuyi_Matrix_Engine/Phase*` as method hints only
12. `Zhuyi_Matrix_Engine/Atlas_DB/*` as candidate data only
13. `docs/archive/*` as historical/tombstone data only

## Query workflows

### Term meaning or ambiguity

Use:

```text
term → knowledge/lexicon/term-senses.jsonl → sense_id → evidence_quotes
→ source_segments.clean_md_path → checked quote → optional synthesis
```

Optional helper:

```bash
python3 knowledge/scripts/query_term.py <term>
python3 knowledge/scripts/trace_evidence.py <sense_id>
```

Do not merge senses merely because they share one Chinese word. Cite the exact `sense_id` when making interpretive claims.

### Matrix position or doctrine location

Use:

```text
doctrine / coordinate → 目录索引_结构化.csv → knowledge/position-cards/{coordinate}.md
→ associated rows → W3 terms → W5 relations
```

Optional helper:

```bash
python3 knowledge/scripts/query_position.py <coordinate-or-title>
```

Treat coordinates as identifiers, not display-only labels.

### Relation, transition, movement, boundary, or misrecognition

Use:

```text
relation-assets.jsonl → relation_type / relation_id → source and target senses
→ source_position / target_position → evidence_segment → W6 audit if needed
```

Optional helper:

```bash
python3 knowledge/scripts/query_relation.py --type <relation_type>
python3 knowledge/scripts/trace_evidence.py <relation_id>
```

Use controlled relation types. Do not replace them with vague “related to” language.

### Overview or synthesis

Use W7 syntheses as maps after checking W3/W4/W5, unless the user explicitly asks for a field overview. Do not treat a synthesis as independent evidence.

### Further absorption / close reading

Use W10 cards when the task asks for argument structure, staged practice/process, or figure/school case positioning that is too detailed for W2 and not captured by W3/W5. Treat W10 as pilot-draft, verify `evidence_quotes` against `split_md_clean/`, preserve `[q1]` claim-to-quote mapping, and check `w3_w5_gap_review` before treating W10 as sufficient.

### Universal Absorption Phase B questions

Use Universal Absorption Phase B for post-Phase-A row-level backlog/coverage questions, especially modern knowledge/science/logic rows, Field 4 writing/communication/organization/practice rows, and Field 1 everyday ideology/behavior-technology rows moved from W1/W2-only into W3/W5/W10 overlap on 2026-06-16. It is not a theme layer.

```bash
python3 knowledge/scripts/query_universal_absorption_b.py 判断 --limit 3
python3 knowledge/scripts/query_universal_absorption_b.py 逻辑行为主义 --limit 3
python3 knowledge/scripts/query_universal_absorption_b.py 写作 --limit 3
python3 knowledge/scripts/validate_universal_absorption_phase_b.py --repo . --final
```

The path is:

```text
knowledge/qa/universal-absorption-phase-b-gap-map.jsonl
→ universal-absorption-phase-b-evidence-bank.jsonl
→ W3-UNIVERSAL-B / W5-UNIVERSAL-B / W10 Universal-B cards
→ split_md_clean exact quote
```

Do not treat Universal-B as a new external encyclopedia or as a replacement for existing independent theme layers.

### Universal Absorption Phase A questions

Use Universal Absorption Phase A for row-level backlog/coverage questions, especially high-volume rows moved from W1/W2-only into W3/W5/W10 overlap on 2026-06-16. It is not a theme layer.

```bash
python3 knowledge/scripts/query_universal_absorption.py 在场 --limit 3
python3 knowledge/scripts/query_universal_absorption.py 芝诺 --limit 3
python3 knowledge/scripts/validate_universal_absorption_phase_a.py --repo . --final
```

The path is:

```text
knowledge/qa/universal-absorption-phase-a-gap-map.jsonl
→ universal-absorption-phase-a-evidence-bank.jsonl
→ W3-UNIVERSAL-A / W5-UNIVERSAL-A / W10 Universal-A cards
→ split_md_clean exact quote
```

Do not treat Universal-A as a new external encyclopedia or as a replacement for existing independent theme layers.

### AI theme questions

Use the AI theme maximum absorption layer for questions about AI, VR, artificial intelligence, intelligence, algorithms, robots, strong/weak AI, AI embodiment, AI mortality, or AI regeneration.

```bash
python3 knowledge/scripts/query_ai_theme.py AI身体化
python3 knowledge/scripts/query_ai_theme.py 强AI
python3 knowledge/scripts/query_ai_theme.py AI可朽性
python3 knowledge/scripts/query_ai_theme.py --row 360
```

The theme path is:

```text
knowledge/themes/ai/ai-row-manifest.jsonl
→ ai-evidence-bank.jsonl
→ AI W3 draft senses / AI W5 draft relations / W10 AI cards
→ split_md_clean exact quote
```

Do not treat `knowledge/themes/ai/` as a source above the corpus; it is a query and synthesis surface.

### Religion Problem theme questions

Use the Religion Problem maximum absorption layer for questions about 宗教问题, 宗教实在论, 神圣秩序, 神创, 神义, 偶像, 拜物, 时间崇拜, 灵魂, 唯灵论, 魔法, 弃绝, 反偶像, 信仰, 命定, 救世, 神智, 神爱, 宗教意识形态, or post-religious practice structures.

```bash
python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3
python3 knowledge/scripts/query_religion_theme.py 偶像 --limit 3
python3 knowledge/scripts/query_religion_theme.py --row 45
python3 knowledge/scripts/query_religion_theme.py --class buddhist-liberation-bridge
```

The theme path is:

```text
knowledge/themes/religion/religion-row-manifest.jsonl
→ religion-evidence-bank.jsonl
→ Religion W3 draft senses / Religion W5 draft relations / W10 Religion cards
→ split_md_clean exact quote
```

Do not treat `knowledge/themes/religion/` as an external religious-studies encyclopedia or a source above the corpus; it is a query and synthesis surface for how ISMISM absorbs religious realism, sacred order, faith/idol/spirit/fetishism, salvation, ideology, and practice transformation.

### Time-Death-Finitude-Life theme questions

Use the Time-Death-Finitude-Life maximum absorption layer for questions about 时间, 死亡, 有限性, 生命, 永生, 不朽, 灵魂, 身体, 记忆, 历史时间, 佛教轮回/业力/涅槃/解脱, AI 永生/可朽性/技术生命, or practice against historical inertia.

```bash
python3 knowledge/scripts/query_time_death_theme.py 死亡 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 时间 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 生命 --limit 3
python3 knowledge/scripts/query_time_death_theme.py --class ai-immortality-mortality
```

The theme path is:

```text
knowledge/themes/time-death-finitude-life/time-death-row-manifest.jsonl
→ time-death-evidence-bank.jsonl
→ Time-Death-Life W3 draft senses / W5 draft relations / W10 coverage
→ split_md_clean exact quote
```

Do not treat `knowledge/themes/time-death-finitude-life/` as an external time/death/life encyclopedia; it is a query and synthesis surface for how ISMISM absorbs death as the main axis with time, finitude, life/body, Buddhist liberation, historical practice, and AI technical life.


### Capitalism / Political Economy theme questions

Use the Capitalism / Political Economy maximum absorption layer for questions about 资本主义, 资本, 政治经济, 生产关系, 商品拜物教, 消费, 金融资本, 阶级, 劳动, 异化, 帝国主义, 全球资本, 资本社会化, 组织经济生活, or practice replacement of capitalist forms.

```bash
python3 knowledge/scripts/query_capitalism_theme.py 资本主义 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 生产关系 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 金融 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py --row 324
python3 knowledge/scripts/validate_capitalism_theme.py --repo . --final
```

The theme path is:

```text
knowledge/themes/capitalism/capitalism-row-manifest.jsonl
→ capitalism-evidence-bank.jsonl
→ Capitalism W3 draft senses / Capitalism W5 draft relations / W10 Capitalism cards
→ split_md_clean exact quote
```

Do not treat `knowledge/themes/capitalism/` as an external capitalism/Marxism/economics encyclopedia or a source above the corpus; it is a query and synthesis surface for how ISMISM absorbs capital, production relations, commodity/fetishism, finance, class, alienation, imperialism, and practice replacement.

## Editing discipline

- Do not overwrite `split_md/`.
- Do not casually rewrite `split_md_clean/` unless text cleaning is the explicit task.
- Do not edit `MASTER-SPEC.md` or `Zhuyi_Matrix_Engine/` unless the user explicitly asks and the change is justified.
- Keep W3 term senses and W5 relations in `draft` unless an explicit promotion audit exists.
- Prefer small auditable batches in `knowledge/`.
- Keep every new interpretive claim traceable to row / segment / quote evidence.
- Update `knowledge/logs/operation-log.md` for substantial changes.
- Do not write outside this repository during normal ISMISM work.

## Legacy boundaries

Old frontend/product surfaces were removed. Do not restore `src/`, `dist/`, old `docs/00-*` through `docs/16-*`, or old cleanup handoff snapshots unless the user explicitly requests historical recovery.

Use `Zhuyi_Matrix_Engine/Atlas_DB/*` only as candidate generator, evidence bridge, summary seed, or unresolved backlog. Never treat Atlas as final truth.

## Validation

Before delivery after edits, run the narrowest relevant validators. For broad changes, run:

```bash
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
python3 knowledge/scripts/validate_universal_absorption_phase_b.py --repo . --final
python3 knowledge/scripts/validate_universal_absorption_phase_a.py --repo . --final
python3 knowledge/scripts/validate_capitalism_theme.py --repo . --final
python3 knowledge/scripts/validate_time_death_theme.py --repo . --final
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_ai_theme.py --repo . --final
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/validate_religion_theme.py --repo . --final
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
```

## Chinese Philosophy theme

For Chinese philosophy / 儒家 / 道家 / 佛教 / 禅 / 唯识 / 中观 / 毛哲学 queries, start at `knowledge/themes/chinese-philosophy/README.md`, then use the row manifest, evidence bank, W3/W5 draft batches, W10 cards, and theme validator. Do not treat the theme layer as a canonical replacement for corpus evidence.

## Religion Problem theme

For Religion Problem / 宗教问题 queries, start at `knowledge/themes/religion/README.md`, then use the row manifest, evidence bank, W3/W5 draft batches, W10 cards, and theme validator. Classify “神 / 精神 / 道 / 爱 / 宗教 / 意识形态” hits by corpus function rather than by keyword alone.


Current W5 validation marker: `--min-count 1044`.

<!-- FEMINISM-THEME-START:NAV -->
## Feminism / Gender / Sexuality / Social Reproduction maximum absorption — 2026-06-16

- `knowledge/themes/feminism/README.md` — Feminism / Gender / Sexuality / Social Reproduction maximum absorption layer.
- `knowledge/themes/feminism/feminism-row-manifest.jsonl` — 94 reviewed rows.
- `knowledge/themes/feminism/feminism-evidence-bank.jsonl` — 309 exact-substring quotes.
- `knowledge/scripts/validate_feminism_theme.py --repo . --final` — final validator.
- `knowledge/scripts/query_feminism_theme.py 女权 --limit 3` — query helper.
- Query scope marker: 女权 / 性别 / 身体 / 社会再生产.
- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
<!-- FEMINISM-THEME-END:NAV -->

<!-- PSYCHOANALYSIS-SUBJECTIVITY-THEME-START:NAV -->
## Psychoanalysis / Subjectivity / Desire / Discourse / Language maximum absorption — 2026-06-16

- `knowledge/themes/psychoanalysis-subjectivity/README.md` — Psychoanalysis / Subjectivity maximum absorption layer.
- `knowledge/themes/psychoanalysis-subjectivity/psychoanalysis-subjectivity-row-manifest.jsonl` — 120 reviewed rows.
- `knowledge/themes/psychoanalysis-subjectivity/psychoanalysis-subjectivity-evidence-bank.jsonl` — 387 exact-substring quotes.
- `knowledge/scripts/validate_psychoanalysis_subjectivity_theme.py --repo . --final` — final validator.
- `knowledge/scripts/query_psychoanalysis_subjectivity_theme.py 精神分析 --limit 3` — query helper.
- Query scope marker: 精神分析 / 主体 / 无意识 / 欲望 / 享乐 / 大他者 / 话语 / 语言 / 符号 / 能指 / 意识形态 / 犬儒.
- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
<!-- PSYCHOANALYSIS-SUBJECTIVITY-THEME-END:NAV -->

## Aesthetics / Art / Media / Image / Narrative maximum absorption — 2026-06-16

- `knowledge/themes/aesthetics-media/README.md` — Aesthetics / Art / Media / Image / Narrative maximum absorption layer; film-analysis precursor, not a finished film matrix.
- `knowledge/themes/aesthetics-media/aesthetics-media-row-manifest.jsonl` — 69 reviewed rows.
- `knowledge/themes/aesthetics-media/aesthetics-media-evidence-bank.jsonl` — 192 exact-substring quotes.
- `knowledge/scripts/validate_aesthetics_media_theme.py --repo . --final` — final validator.
- `knowledge/scripts/query_aesthetics_media_theme.py 电影 --limit 3` — query helper.
- Query scope marker: 电影 / 影像 / 观看 / 美学 / 艺术 / 诗 / 小说 / 叙事 / 文本 / 符号 / 媒介.

For film-analysis precursor work, start here, then combine with Psychoanalysis-Subjectivity, Capitalism, Feminism, Time-Death, Religion, and AI only when row evidence supports the bridge.

- Labor / Workplace / Precarity: read `knowledge/themes/labor-workplace-precarity/README.md`; query with `knowledge/scripts/query_labor_workplace_precarity_theme.py 内卷 --limit 3`; validate with `knowledge/scripts/validate_labor_workplace_precarity_theme.py --repo . --final`.


## Education / Examination / Credentialism theme questions

For education / examination / credentialism / knowledge-discipline queries, start at `knowledge/themes/education-examination-credentialism/README.md`, query with `knowledge/scripts/query_education_examination_credentialism_theme.py 考试 --limit 3`, and validate with `knowledge/scripts/validate_education_examination_credentialism_theme.py --repo . --final`.


## Family / Intimacy / Marriage / Birth / Social Reproduction current layer

- Theme root: `knowledge/themes/family-intimacy-reproduction/`.
- Validator: `python3 knowledge/scripts/validate_family_intimacy_reproduction_theme.py --repo . --final`.
- Query helper: `python3 knowledge/scripts/query_family_intimacy_reproduction_theme.py 家庭 --limit 3`.
- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
- Current W5 global validator command: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2`.
- Boundary: W3/W5 remain `draft`, W10 remains `pilot-draft`, and no unsupported 彩礼-specific claim should be made.

## Consumption / Desire / Commodity / Lifestyle current layer

- Theme root: `knowledge/themes/consumption-desire-lifestyle/`.
- Validator: `python3 knowledge/scripts/validate_consumption_desire_lifestyle_theme.py --repo . --final`.
- Query helper: `python3 knowledge/scripts/query_consumption_desire_lifestyle_theme.py 消费主义 --limit 3`.
- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
- Current W5 global validator command: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2`.
- Boundary: W3/W5 remain `draft`, W10 remains `pilot-draft`, and no unsupported current-events consumption claim should be made.


## Media / Platform / Public Opinion / Traffic Society current layer

- Theme root: `knowledge/themes/media-platform-public-opinion/`.
- Validator: `python3 knowledge/scripts/validate_media_platform_public_opinion_theme.py --repo . --final`.
- Query: `python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 平台 --limit 3`.
- Current global W5 gate: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2`.
- Boundaries: W3/W5 stay `draft`; W10 stays `pilot-draft`; no direct exact `热搜`/`饭圈` corpus claim.

## Current global media-platform checkpoint markers

- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
## Governance / Law / Bureaucracy / Order current layer

- Theme root: `knowledge/themes/governance-law-bureaucracy/`.
- Validator: `python3 knowledge/scripts/validate_governance_law_bureaucracy_theme.py --repo . --final`.
- Query helper: `python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 治理 --limit 3`.
- Current global W5 gate: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2`.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Class / Youth / Generation / Mobility Anxiety current layer

- Theme root: `knowledge/themes/class-youth-generational-anxiety/`.
- Validator: `python3 knowledge/scripts/validate_class_youth_generational_anxiety_theme.py --repo . --final`.
- Query helper: `python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 阶层 --limit 3`.
- Current global W5 gate: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2`.
- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
- Boundary: W3/W5 stay `draft`; W10 stays `pilot-draft`; no unsupported external sociology/current-events claim; downstream labels such as `上升通道`, `阶层固化`, `中产焦虑`, `底层羞辱`, `成功学`, and `青年虚无` need row-level evidence.

## Psychological Distress / Anxiety / Addiction / Social Symptom current layer

- Theme root: `knowledge/themes/psychological-distress-social-symptom/`.
- Validator: `python3 knowledge/scripts/validate_psychological_distress_social_symptom_theme.py --repo . --final`.
- Query helper: `python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 焦虑 --limit 3`.
- Current global W5 gate: `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2`.
- Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
- Boundary: W3/W5 stay `draft`; W10 stays `pilot-draft`; no clinical, therapeutic, psychiatric, medication, or current-events mental-health claim.

- Urban / Housing / Migration / Space: `knowledge/scripts/query_urban_housing_migration_space_theme.py 城市 --limit 3`; validator `knowledge/scripts/validate_urban_housing_migration_space_theme.py --repo . --final`; W5 validator uses `--min-count 1044`.

- Health / Body / Medicine / Risk Society: `knowledge/scripts/query_health_body_risk_society_theme.py 身体 --limit 3`; validator `knowledge/scripts/validate_health_body_risk_society_theme.py --repo . --final`; W5 validator uses `--min-count 1044`.

## Social Phenomena / Everyday Life Problems Superphase operator surface — 2026-06-16

- Start with `knowledge/qa/social-phenomena-superphase-audit.md` for the 10-theme / 3-phase / 30-prompt matrix.
- Use `python3 knowledge/scripts/query_social_phenomena_superphase.py <prompt> --limit 3` for everyday social phenomena such as 内卷, 考公热, 婚恋市场, 短视频成瘾, 住房焦虑, or 医疗焦虑.
- Use `python3 knowledge/scripts/query_social_phenomena_superphase.py --smoke-all --limit 1` to verify all 30 routes.
- Validate the whole layer with `python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final`; W5 validator uses `--min-count 1044`.
- Phase syntheses: `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md`, `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md`, `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md`.
- Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
- Boundary: this is a corpus-grounded social diagnosis layer, not current-events commentary, legal/clinical/medical/housing advice, or external sociology; W3/W5 remain `draft`, W10 remains `pilot-draft`.
