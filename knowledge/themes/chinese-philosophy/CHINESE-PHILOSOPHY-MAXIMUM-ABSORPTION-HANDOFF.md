# Chinese Philosophy Maximum Absorption — Historical Planning Handoff (Superseded)

- created: 2026-06-15 CST
- status: **superseded / historical planning artifact**; implementation completed on 2026-06-15 CST
- original intended mode: `$autopilot` strict lifecycle with Ultragoal-led, Team-assisted execution; retained only to document how the now-completed run was scoped.
- repo: `/home/weathour/文档/ismism-system`


## Supersession notice — current completed state

This file is no longer the live execution handoff. It is retained as the historical planning brief that seeded the completed Chinese Philosophy Maximum Absorption Program. The current operational entry points are:

- `knowledge/themes/chinese-philosophy/README.md`
- `knowledge/themes/chinese-philosophy/chinese-philosophy-row-manifest.jsonl`
- `knowledge/themes/chinese-philosophy/chinese-philosophy-evidence-bank.jsonl`
- `knowledge/themes/chinese-philosophy/chinese-philosophy-taxonomy.md`
- `knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md`
- `knowledge/themes/chinese-philosophy/ancient-chinese-philosophy-synthesis.md`
- `knowledge/themes/chinese-philosophy/mao-philosophy-synthesis.md`
- `knowledge/qa/chinese-philosophy-absorption-audit.md`
- `knowledge/qa/chinese-philosophy-evidence-claim-audit.md`
- `knowledge/qa/chinese-philosophy-ultraqa-report.md`

Final completed counts:

| Deliverable | Final count / status |
|---|---:|
| row manifest | 70 rows |
| evidence bank | 238 exact clean-text quote records |
| Chinese W3 batch | 60 `draft` senses (`W3-CHINESE-PHILOSOPHY-2026-06-15`) |
| Chinese W5 batch | 50 `draft` relations (`W5-CHINESE-PHILOSOPHY-2026-06-15`) |
| Chinese W10 cards | 45 new `pilot-draft` cards |
| W10 total after program | 77 cards |
| syntheses | 3 evidence-linked synthesis docs |
| QA/audit docs | 3 Chinese Philosophy QA docs |
| validator | `knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final` PASS |

Boundary status remains unchanged: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`; Atlas remains candidate-only.

## Historical purpose

Build a maximum absorption layer for 中国哲学 in this repository, covering:

1. 古代中国哲学：儒家、道家、法家、名家、周易/阴阳、宋明理学/心学等。
2. 佛教/禅/唯识/中观 as a bridge layer where it is actively used inside the ISMISM Chinese-philosophy constellation.
3. 毛哲学 / 中国化马克思主义：实践论、矛盾论、辩证唯物主义、历史唯物主义、群众性实践、组织/纪律/战略等。

This goal has now been completed as a queryable, auditable, quote-traceable theme layer comparable in ambition to the completed AI theme layer, while preserving the repository truth-source hierarchy.

## Hard boundaries

- Do not overwrite `split_md/` raw text.
- Do not casually rewrite `split_md_clean/`.
- Every claim must preserve row / segment / quote traceability.
- W3 term senses and W5 relation assets remain `draft`.
- W10 cards remain `pilot-draft`.
- Atlas remains candidate-only; do not use it as truth.
- Do not restore deleted frontend/product routes.
- Do not treat all keyword hits as core Chinese philosophy. The scan found about 288 broad hits, but most are noise/context.

## Historical recommended scope

Use a three-ring scope rather than a raw keyword search.

### Ring 1 — core Chinese philosophy rows

Approximate core: 51 rows.

#### A. 儒家 / 宋明理学 / 心学

Rows:

`46, 48, 49, 50, 57, 59, 81, 83, 89, 134, 137`

Focus:

- 孔子 / 孟子 / 儒家伦理结构
- 王阳明、朱熹、陆九渊、程朱、心学、理学
- 圣人、道学先生、大同、道德严酷主义等在 ISMISM 中的诊断用途

#### B. 道家 / 老庄 / 战国诸子 / 周易

Rows:

`119, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 139, 142, 143`

Focus:

- 老子 / 无为
- 庄子 / 坐忘 / 圣人工厂
- 杨朱
- 韩非 / 法家
- 周易 / 阴阳 / 历史符号主义
- 惠施 / 名家 / 方中方睨
- 反二元对立 / 矩阵运思

#### C. 佛教 / 禅宗 / 唯识 / 中观 bridge

Rows:

`120, 121, 122, 123, 124, 140, 141, 186`

Focus:

- 印度佛教进入中文哲学语境
- 唯识、阿赖耶、中观、龙树
- 禅宗、参话头
- 与道家、反二元、解脱技术的关系

Boundary: classify as `buddhist-chan-bridge`; do not collapse it into pure Confucian/Daoist Chinese antiquity.

#### D. 毛哲学 / 中国化马克思主义 / 实践论

Rows:

`184, 284, 285, 289, 290, 291, 292, 293, 327, 331, 332, 333, 334, 335, 341`

Focus:

- 正统辩证唯物主义
- 实践论 / 矛盾论
- 历史唯物主义
- 学习 / 研究 / 灌输
- 历史的哲学化
- 解放思想
- 战略-战役-战斗
- 纪律教育 / 组织工作
- 实事求是式实践方法

### Ring 2 — broader revolutionary / dialectical context

Rows:

`1, 34, 35, 94, 98, 110, 154, 162, 261, 269, 270, 280, 309, 321, 324, 325, 326, 328, 329, 330`

Use as context, quote-bank support, or secondary manifest rows. These are not automatically core Chinese philosophy rows.

### Ring 3 — broad keyword/noise review

A broad keyword scan found about 288 rows with hits such as 中国、儒、道家、佛教、禅、理学、毛、革命, etc. Most should be classified as peripheral or noise unless the clean text supports a real theme function.

Important false positives:

- `毛` can mean “hair” or occur in unrelated phrases.
- `理学` can be part of 心理学、物理学、伦理学, not 宋明理学.
- `革命` may be 科学革命 / 哥白尼革命 rather than political or Maoist philosophy.
- `中国` may be mere context rather than doctrine.

## Historical pre-absorption baseline over the proposed 70-row scope

Approximate scan summary:

| Scope | Rows | W3 rows | W5 rows | W10 rows |
|---|---:|---:|---:|---:|
| 儒家 / 理学 / 心学 core | 11 | 2 | 0 | 0 |
| 道家 / 老庄 / 战国 / 周易 core | 17 | 9 | 2 | 1 |
| 佛教 / 禅 / 唯识 / 中观 bridge | 8 | 5 | 0 | 0 |
| 毛哲学 / 中国化马克思主义 core | 15 | 7 | 3 | 0 |
| broader revolutionary context | 20 | 5 | 1 | 0 |
| unique total | 70 | 28 | 6 | 1 |

Historical interpretation before the completed run: this theme was much shallower than the completed AI theme, with only one W10 row in the proposed scope and no full W3+W5+W10 overlap as a theme program. This baseline is now superseded by the completed 70-row / 238-quote / 60-W3 / 50-W5 / 45-W10 Chinese Philosophy layer.

## Final target — completed

Completed theme layer:

`knowledge/themes/chinese-philosophy/`

Completed deliverables:

1. `chinese-philosophy-row-manifest.jsonl`
2. `chinese-philosophy-evidence-bank.jsonl`
3. `chinese-philosophy-taxonomy.md`
4. `chinese-philosophy-synthesis.md`
5. `ancient-chinese-philosophy-synthesis.md`
6. `mao-philosophy-synthesis.md`
7. `chinese-philosophy-w3-w5-batch-notes.md`
8. `README.md`
9. AI-style validator: `knowledge/scripts/validate_chinese_philosophy_theme.py`
10. Optional query helper: `knowledge/scripts/query_chinese_philosophy_theme.py`
11. QA docs:
    - `knowledge/qa/chinese-philosophy-absorption-audit.md`
    - `knowledge/qa/chinese-philosophy-evidence-claim-audit.md`
    - `knowledge/qa/chinese-philosophy-ultraqa-report.md`

## Expected scale — met

Completed maximum absorption scale:

- Manifest: 70 rows.
- Quote bank: 238 exact-substring quote records.
- W3 draft senses: 60 records.
- W5 draft relations: 50 records.
- W10 cards: 45 new Chinese Philosophy cards.
- Synthesis: one total synthesis plus two sub-syntheses:
  - 古代中国哲学综合
  - 毛哲学 / 中国化马克思主义综合

## Taxonomy axes used

- `confucian-ethical-subject` — 儒家伦理主体、圣人、道德严酷主义、礼/仁/大同的 ISMISM 使用。
- `neo-confucian-heart-mind` — 宋明理学/心学、王阳明、朱熹、陆九渊、心/理/圣人结构。
- `daoist-negativity-nonaction` — 老子、无为、否定性、太一生水。
- `zhuangzi-forgetting-transformation` — 庄子、坐忘、濠梁、圣人工厂、外天下/外物/外生。
- `legalist-practical-magic` — 韩非、法家、战国统治术/神秘学教育。
- `yijing-symbolic-history` — 周易、阴阳、历史符号主义。
- `names-anti-dualism` — 惠施、名家、方中方睨、反二元对立、矩阵运思。
- `buddhist-chan-bridge` — 佛教、禅、唯识、中观、阿赖耶、参话头。
- `mao-practice-contradiction` — 实践论、矛盾论、解放思想、实事求是。
- `chinese-marxist-organization` — 学习/研究、灌输、组织、纪律、战略-战役-战斗。
- `revolutionary-dialectical-context` — 阶级斗争、革命、辩证唯物主义/历史唯物主义外围桥接。
- `peripheral-or-noise` — keyword hit without strong theme function.

## Historical suggested W10 batches — completed

### W10 batch 1 — ancient core / Daoist-Warring States axis

Rows:

`125, 127, 128, 130, 131, 132, 133, 135, 140, 143`

Rationale: gives the theme an ancient-philosophy spine quickly. Row 131 already has W10 and should be integrated/expanded rather than duplicated.

### W10 batch 2 — Confucian / Neo-Confucian / Heart-mind axis

Rows:

`46, 48, 49, 50, 57, 59, 134, 137`

Rationale: builds a distinct Confucian and Neo-Confucian diagnostic line, historically shallow despite many strong clean-text hits before completion.

### W10 batch 3 — Mao philosophy / Chinese Marxist practice axis

Rows:

`184, 284, 285, 289, 290, 291, 292, 293, 327, 331, 332, 333, 334, 335, 341`

Rationale: turns scattered W3/W5 hints into a coherent Mao/practice/organization chain.

### W10 batch 4 — bridge and context completion

Rows:

`120, 121, 122, 123, 124, 141, 186, 1, 34, 94, 98, 110, 261, 280, 321, 324, 325, 326, 328, 329, 330`

Rationale: only after core axes are stable, absorb bridge/peripheral rows or classify them as context/noise.

## Durable subgoals — completed

G01. Chinese philosophy row manifest — completed

- Output: `knowledge/themes/chinese-philosophy/chinese-philosophy-row-manifest.jsonl`
- Cover about 70 rows.
- Fields should mirror the AI theme manifest: row_id, segment_id, toc_id, title, clean_md_path, field, char_count, keyword_hits, theme_class, core_status, current_absorption, recommended_action, evidence_quote_count, notes.

G02. Chinese philosophy validator and quote bank — completed

- Output: `knowledge/themes/chinese-philosophy/chinese-philosophy-evidence-bank.jsonl`
- Validator: `knowledge/scripts/validate_chinese_philosophy_theme.py`
- Every quote must be exact substring of declared clean file.

G03. Taxonomy — completed

- Output: `knowledge/themes/chinese-philosophy/chinese-philosophy-taxonomy.md`
- Each taxonomy node must link to manifest rows and/or quote IDs.

G04. W3 draft senses — completed

- Append about 50–70 records to `knowledge/lexicon/term-senses.jsonl`.
- Batch ID suggestion: `W3-CHINESE-PHILOSOPHY-2026-06-15` or current date.
- All status=draft.

G05. W5 draft relations — completed

- Append about 40–60 records to `knowledge/relations/relation-assets.jsonl`.
- Batch ID suggestion: `W5-CHINESE-PHILOSOPHY-2026-06-15` or current date.
- All status=draft.

G06. W10 ancient core batch — completed

- Rows: `125, 127, 128, 130, 131, 132, 133, 135, 140, 143`.

G07. W10 Confucian / Neo-Confucian batch — completed

- Rows: `46, 48, 49, 50, 57, 59, 134, 137`.

G08. W10 Mao / Chinese Marxist practice batch — completed

- Rows: `184, 284, 285, 289, 290, 291, 292, 293, 327, 331, 332, 333, 334, 335, 341`.

G09. W10 bridge/context batch — completed

- Rows selected from Ring 2 and Buddhist/Chan bridge; classify not-applicable/noise where necessary.

G10. Synthesis — completed

- Outputs:
  - `chinese-philosophy-synthesis.md`
  - `ancient-chinese-philosophy-synthesis.md`
  - `mao-philosophy-synthesis.md`

G11. Query and usage integration — completed

- Output: `knowledge/themes/chinese-philosophy/README.md`.
- Update `knowledge/query-playbook.md`, `DIRECTORY_MAP.md`, and possibly `knowledge/README.md`.
- Optional helper: `knowledge/scripts/query_chinese_philosophy_theme.py`.

G12. QA / audit / handoff — completed

- Outputs:
  - `knowledge/qa/chinese-philosophy-absorption-audit.md`
  - `knowledge/qa/chinese-philosophy-evidence-claim-audit.md`
  - `knowledge/qa/chinese-philosophy-ultraqa-report.md`
- Update `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, and operation log.

## Final validation contract — completed

Latest completed run evidence uses:

```bash
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count <new-total> --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
git diff --name-only -- split_md split_md_clean
```

Negative validator evidence was also produced and restored: bad quote, duplicate taxonomy row, unresolved synthesis marker families, and duplicate W10 evidence quote all fail as expected; final positive validation then passes.

## Original new-dialogue prompt — historical only

The prompt below is retained only to show the original user-facing launch brief. Do not treat it as current work unless intentionally replaying the completed program in a new repository state.

```text
$autopilot

执行 /home/weathour/文档/ismism-system 的 “Chinese Philosophy Maximum Absorption Program”（中国哲学最大吸收计划），并一直推进到全部完成、验证、审计和交接为止。用户明确授权：本任务需求已经足够清楚，跳过进一步 deep-interview 提问；不要向用户请求“是否继续”；除非遇到 destructive / credential-gated / external-production / irreversible 操作，否则自动继续。若某个子路径失败，尝试替代方案；若某个批次太大，自动拆分并通过 Ultragoal steering 增补子目标，不降低最终验收标准。

主执行策略：使用本轮 AI Theme Maximum Absorption Program 同款推进模式，即 Autopilot strict loop + Ultragoal-led Team-assisted execution。用户称其为 “ultrapilot 方法” 时，按本仓库实际可用工作流解释为：Autopilot lifecycle（requirements skip record → ralplan/plan artifact → ultragoal → code-review → ultraqa 或 docs-only/knowledge-layer QA 替代），其中 Ultragoal 负责 durable subgoals、ledger、checkpoint、resume；Team 只在 quote-bank、W3/W5、W10 制卡、QA spot-check 等可并行批量阶段使用；Ralph 只作为显式 fallback，不作为默认推进模式。

必须先读取：
1. AGENTS.md
2. ISMISM-MAINLINE-HANDOFF.md
3. knowledge/STATE.md
4. knowledge/DIGESTION_PROGRAM.md
5. knowledge/qa/absorption-strength-distribution.md
6. knowledge/themes/chinese-philosophy/CHINESE-PHILOSOPHY-MAXIMUM-ABSORPTION-HANDOFF.md
7. knowledge/themes/ai/README.md 和 knowledge/qa/ai-theme-ultraqa-report.md（作为已完成主题层范式参考，不复制内容）
8. knowledge/w10-absorption/PLAN.md
9. knowledge/w10-absorption/index.md
10. knowledge/manifests/segments.jsonl
11. knowledge/segment-cards/index.md
12. knowledge/lexicon/term-senses.jsonl
13. knowledge/relations/relation-assets.jsonl
14. DIRECTORY_MAP.md

最高目标：把本仓库中中国哲学主题（古代中国哲学 + 佛教/禅/唯识/中观桥接 + 毛哲学/中国化马克思主义）提升为一个可查询、可审计、可综合的 Chinese Philosophy 主题最大吸收层。核心行达到 W3 + W5 + W10 + theme synthesis + QA audit 的最高吸收强度；外围行至少完成 manifest、quote bank、classification、context rationale 或 not_applicable/noise 理由。

仓库纪律 / 硬约束：
1. 遵守 AGENTS.md 的真源顺序：目录索引_结构化.csv → split_md/split_md_clean → knowledge/manifests → segment-cards → lexicon → position-cards → relations → QA → syntheses → W10。
2. 不改写 split_md/ 原文。
3. 不随意改写 split_md_clean/。
4. 所有解释必须保留 row / segment / quote traceability。
5. W3 term senses 和 W5 relation assets 保持 draft，不提升 canonical。
6. W10 cards 保持 pilot-draft。
7. Atlas 只能作为候选，不作真相层。
8. 不恢复旧 frontend/product route。
9. 所有新增 Chinese philosophy 主题卡和 quote bank 必须使用 declared clean file 的 exact quote substring，并能被 validator 检查。
10. 如果当前 validator 不覆盖 Chinese philosophy 新目录，先新增专用 validator，再继续大规模写卡。
11. 优先小批量、可审计、可回滚；不要一次性生成不可验证的大段综合。
12. 不新增外部依赖；优先使用现有 Python/Markdown/JSONL 工具。

初始候选范围：
- 儒家 / 宋明理学 / 心学：46, 48, 49, 50, 57, 59, 81, 83, 89, 134, 137。
- 道家 / 老庄 / 战国诸子 / 周易：119, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 139, 142, 143。
- 佛教 / 禅 / 唯识 / 中观 bridge：120, 121, 122, 123, 124, 140, 141, 186。
- 毛哲学 / 中国化马克思主义 / 实践论：184, 284, 285, 289, 290, 291, 292, 293, 327, 331, 332, 333, 334, 335, 341。
- 扩展革命/辩证法上下文：1, 34, 35, 94, 98, 110, 154, 162, 261, 269, 270, 280, 309, 321, 324, 325, 326, 328, 329, 330。
- 同时用关键词 中国 / 中华 / 孔子 / 孟子 / 荀子 / 儒 / 道家 / 老子 / 庄子 / 列子 / 韩非 / 法家 / 名家 / 阴阳 / 易经 / 周易 / 佛教 / 禅 / 唯识 / 中观 / 阿赖耶 / 王阳明 / 朱熹 / 陆九渊 / 程朱 / 心学 / 理学 / 毛泽东 / 毛主席 / 毛选 / 毛主义 / 实践论 / 矛盾论 / 群众路线 / 新民主主义 / 阶级斗争 / 中国革命 / 文化大革命 / 马克思主义中国化 / 辩证唯物主义 / 历史唯物主义 复核 split_md_clean 与 manifests，形成约 70 行候选；不要把所有“毛”“理学”“革命”“中国”命中都自动当核心。

请将总目标拆成并执行以下 durable subgoals，必要时继续细分但不得弱化验收：

G01. Chinese philosophy row manifest — completed
产出：knowledge/themes/chinese-philosophy/chinese-philosophy-row-manifest.jsonl
覆盖约 70 行，字段至少包括：row_id, segment_id, toc_id, title, clean_md_path, field, char_count, keyword_hits, theme_class, core_status, current_absorption, recommended_action, evidence_quote_count, notes。
建议 theme_class：confucian-ethical-subject, neo-confucian-heart-mind, daoist-negativity-nonaction, zhuangzi-forgetting-transformation, legalist-practical-magic, yijing-symbolic-history, names-anti-dualism, buddhist-chan-bridge, mao-practice-contradiction, chinese-marxist-organization, revolutionary-dialectical-context, peripheral-or-noise。
验收：候选行都有记录；每条 row_id 与 segments.jsonl 一致；clean_md_path 存在。

G02. Chinese philosophy evidence bank + validator
产出：knowledge/themes/chinese-philosophy/chinese-philosophy-evidence-bank.jsonl；knowledge/scripts/validate_chinese_philosophy_theme.py。
核心行抽取 3–8 条 quote；外围行至少 1–3 条或明确 not_applicable/noise 理由。每条记录含 row_id, segment_id, toc_id, clean_md_path, quote, theme_tags, quote_role。
验收：validator 检查每条 quote 是 clean_md_path 的 exact substring。

G03. Taxonomy — completed
产出：knowledge/themes/chinese-philosophy/chinese-philosophy-taxonomy.md。
每个 taxonomy 节点至少回链到 row 或 quote-bank id；validator 应能检查 taxonomy row/class ownership，避免重复归类和 class mismatch。

G04. W3 Chinese philosophy term senses
产出：追加/维护 knowledge/lexicon/term-senses.jsonl，并记录专项批次说明。
新增约 50–70 条 Chinese philosophy 专项 draft senses，覆盖儒、圣人、心学、理学、无为、坐忘、太一生水、周易、阴阳、韩非/法家、惠施/名家、唯识、阿赖耶、中观、禅、实践论、矛盾论、辩证唯物主义、历史唯物主义、解放思想、组织/纪律/群众实践等。
验收：validate_w3_term_senses.py PASS；所有新增义项 status=draft；证据 quote 可回链。

G05. W5 Chinese philosophy relation assets
产出：追加/维护 knowledge/relations/relation-assets.jsonl，并记录专项批次说明。
新增约 40–60 条 draft relations，覆盖儒家伦理主体、心/理关系、道家否定性、庄子坐忘过程、法家实践魔法、周易符号历史、佛教/禅桥接、实践论与历史哲学化、解放思想与生产/组织实践、纪律教育与战略-战役-战斗等。
验收：validate_w5_relation_assets.py PASS；所有新增关系 status=draft；relation_type 使用既有允许类型或先更新 validator/文档并审计。

G06. W10 ancient Daoist/Warring States batch
产出：rows 125, 127, 128, 130, 131, 132, 133, 135, 140, 143 的 W10 cards；row 131 已有 W10 时需整合/扩展而非重复。

G07. W10 Confucian / Neo-Confucian batch — completed
产出：rows 46, 48, 49, 50, 57, 59, 134, 137 的 W10 cards。

G08. W10 Mao / Chinese Marxist practice batch — completed
产出：rows 184, 284, 285, 289, 290, 291, 292, 293, 327, 331, 332, 333, 334, 335, 341 的 W10 cards。

G09. W10 bridge/context batch — completed
产出：从 Buddhist/Chan bridge 与 broader revolutionary context 中选择必要 cards；其余给出 context/noise/not_applicable 理由。

G10. Theme synthesis
产出：knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md；ancient-chinese-philosophy-synthesis.md；mao-philosophy-synthesis.md。
要求：综合不独立造证；每个主要 claim 回链到 W3/W5/W10/quote-bank。

G11. Query / usage integration
产出：knowledge/themes/chinese-philosophy/README.md；更新 knowledge/query-playbook.md、DIRECTORY_MAP.md、knowledge/README.md；必要时新增 knowledge/scripts/query_chinese_philosophy_theme.py。

G12. QA / audit / handoff — completed
产出：knowledge/qa/chinese-philosophy-absorption-audit.md；knowledge/qa/chinese-philosophy-evidence-claim-audit.md；knowledge/qa/chinese-philosophy-ultraqa-report.md；更新 knowledge/STATE.md、ISMISM-MAINLINE-HANDOFF.md、DIRECTORY_MAP.md、operation-log。

最终验收：
1. 约 70 行候选全部分类入 manifest。
2. 核心古代中国哲学与毛哲学 rows 均有 W10 或明确 not_applicable/context 理由。
3. 新增 Chinese philosophy W3 draft senses 约 50–70 条。
4. 新增 Chinese philosophy W5 draft relations 约 40–60 条。
5. 新增 35–45 张左右 W10 cards 或经审计的等价完成量。
6. 三篇 synthesis 均有证据链。
7. 新增 Chinese philosophy QA audit、evidence-claim audit、UltraQA/docs QA report。
8. 所有 validators 通过，包括 theme 专用 validator、W10、master、W3、W5、W4、git diff --check、protected corpus diff。
9. 更新 handoff/state/navigation，使新 agent 能恢复工作。
10. 最终报告列出 changed files、row coverage、W3/W5/W10 counts、validators、remaining risks。

执行期间如果需要并行：可在某个 Ultragoal story 内启动 Team，例如 4:executor，用于分片处理 quote-bank、W10 cards、W3/W5 extraction、QA spot-check。Team workers 必须只处理分配范围，不拥有 Ultragoal ledger，不 checkpoint；Leader 汇总 Team evidence 后 checkpoint 当前 story。

完成条件：只有当 G01–G12 全部完成、验证通过、审计和 handoff 更新完成后，才标记 Ultragoal / Autopilot complete。不要以部分批次完成冒充总目标完成。
```
