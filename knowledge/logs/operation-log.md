# ISMISM 知识库消化操作日志

## 2026-05-08 — bootstrap program created

- Created `knowledge/DIGESTION_PROGRAM.md` as the master program for long-run digestion.
- Created `knowledge/STATE.md` as the compaction-resistant resume state.
- Created directory skeleton under `knowledge/` for manifests, segment cards, position cards, lexicon, relations, syntheses, QA, prompts, templates, and logs.
- Current next action: build W1 corpus manifest and segment registry.

## 2026-05-08 — cross-context continuation anchors added

- Verified the master program, state file, templates, and GPT-5.3 Spark start prompt under `knowledge/`.
- Added external pointer in `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md` so psychoanalytic-writing-lab treats ISMISM as an external reference library only after digestion is stable.
- Added OMX notepad priority context in `/home/weathour/文档/psychoanalytic-writing-lab/.omx/notepad.md` for compaction-resistant recovery.
- Current next action remains W1: build `knowledge/manifests/corpus-manifest.json`, `segments.jsonl`, and `missing-and-anomalies.md`.

## 2026-05-08 17:53 CST — W1 corpus manifest completed

- Read the required resume/state/method files before generation.
- Added deterministic W1 build script: `knowledge/scripts/build_w1_manifests.py`.
- Generated `knowledge/manifests/corpus-manifest.json`.
- Generated `knowledge/manifests/segments.jsonl` with 363 records from `目录索引_结构化.csv`.
- Verified actual raw/clean markdown existence: 362 available text segments, 1 missing text segment.
- Generated `knowledge/manifests/chunks.jsonl` with 1,589 retrieval chunks across 362 available clean segments.
- Generated `knowledge/manifests/missing-and-anomalies.md`, recording row 176 / `2-4-2-4` and the absent `split_pdf/` derived layer.
- Updated `knowledge/README.md` and `knowledge/STATE.md`.
- Stopped before W2 as requested; next action awaits user choice.

## 2026-05-08 17:54 CST — W1 completion audit passed

- Added validator script: `knowledge/scripts/validate_w1_manifests.py`.
- Validator result: PASS.
- Added audit report: `knowledge/qa/w1-completion-audit.md`.
- Confirmed no W2 segment cards were generated.

## 2026-05-08 18:10 CST — W1 recovery reconciliation pass

- Ran recovery consistency reconciliation for W1 after row 176 restoration.
- Updated `knowledge/manifests/missing-and-anomalies.md` to reflect: 0 missing raw/clean text segments; partial `split_pdf/` (only row 176).
- Created `knowledge/qa/w1-recovery-audit.md`.
- Updated `knowledge/README.md` and `knowledge/STATE.md` counts to current 363/1594 status.
- Re-ran `python knowledge/scripts/validate_w1_manifests.py` and result: PASS.

## 2026-05-08 18:16:02 CST — W2 segment cards batch
Generated W2 batch size=16 from row 1; rows=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:16:08 CST — W2 segment cards batch
Generated W2 batch size=16 from row 17; rows=17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:16:34 CST — W2 segment cards batch
Generated W2 batch size=16 from row 33; rows=33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:17:24 CST — W2 segment cards batch
Generated W2 batch size=16 from row 49; rows=49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:18:29 CST — W2 segment cards batch
Generated W2 batch size=16 from row 65; rows=65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:18:36 CST — W2 segment cards batch
Generated W2 batch size=16 from row 81; rows=81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:21:49 CST — W2 segment cards batch
Generated W2 batch size=16 from row 97; rows=97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:18 CST — W2 segment cards batch
Generated W2 batch size=16 from row 113; rows=113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:18 CST — W2 segment cards batch
Generated W2 batch size=16 from row 129; rows=129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:18 CST — W2 segment cards batch
Generated W2 batch size=16 from row 145; rows=145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:18 CST — W2 segment cards batch
Generated W2 batch size=16 from row 161; rows=161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:18 CST — W2 segment cards batch
Generated W2 batch size=16 from row 177; rows=177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:18 CST — W2 segment cards batch
Generated W2 batch size=16 from row 193; rows=193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 209; rows=209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 225; rows=225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 241; rows=241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 257; rows=257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 273; rows=273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 289; rows=289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 305; rows=305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 321; rows=321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=16 from row 337; rows=337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:26:19 CST — W2 segment cards batch
Generated W2 batch size=11 from row 353; rows=353,354,355,356,357,358,359,360,361,362,363. Updated knowledge/segment-cards/index.md and STATE.md.

## 2026-05-08 18:29 CST — W3 readiness analysis and prompt prepared

- Confirmed W2 completion state from actual artifacts: 363 non-index segment cards, index rows 1–363, no missing/duplicate row ids.
- Added W3 startup prompt: `knowledge/prompts/w3-start.md`.
- Updated `knowledge/STATE.md` current phase and next action to W3 term senses readiness.
- Did not start W3 lexicon generation yet; next recommended batch is 1–3 terms, preferably 主体 / 客体 / 实践.

## 2026-05-08 18:29 CST — STATE normalized for W3 handoff

- Cleaned stale W2 wording in `knowledge/STATE.md`: current state now records W2 complete and W3 ready.
- Active batch changed to W3 readiness checkpoint; W3 lexicon outputs remain pending.

## 2026-05-08 18:47 CST — W3 batch 1 started and completed as draft

- Objective: start W3 term-sense registry after W2 completion.
- W2 gate re-audited: 363 segment cards, index covers row 1–363, no missing/duplicate row_id.
- Created W3 lexicon artifacts:
  - `knowledge/lexicon/term-senses.jsonl` (13 draft records)
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/lexicon/term-candidate-stats.tsv`
  - `knowledge/qa/w3-lexicon-audit.md`
- First batch terms processed: `主体`, `客体`, `实践`.
- All W3 senses remain `draft`; no canonical elevation performed.
- Next W3 batch suggestion: `历史`/`人民`/`理论` or mechanism batch `主体化`/`客体化`/`去主体化`.

## 2026-05-08 18:48 CST — W3 batch 1 validation pass

- Revalidated `knowledge/lexicon/term-senses.jsonl`: 13 records, required fields present, all statuses `draft`.
- Verified every source segment card / clean markdown path exists.
- Verified every evidence quote is recoverable as an exact substring after whitespace normalization.

## 2026-05-08 19:05 CST — W3 batch 2 历史义项（第一项）完成

- 已按“先选第一个（历史）”策略完成 `历史` 术语义项整理（5 条 draft）：
  - `term:历史:s01`（时间性历史范式/物质史）
  - `term:历史:s02`（场域链路中的中介候选）
  - `term:历史:s03`（历史的哲学化/辩证法化）
  - `term:历史:s04`（史学研究实践）
  - `term:历史:s05`（历史的自我妥协与现实化）
- 追加更新：
  - `knowledge/lexicon/core-terms.md`（新增/同步 `历史` 小节）
  - `knowledge/lexicon/ambiguous-terms.md`（新增 `历史`歧义说明）
  - `knowledge/qa/w3-lexicon-audit.md`（新增 W3-B2 审计片段）
  - `knowledge/STATE.md`（批次推进与下一步目标）
- 下一子批建议：`人民`、`理论`（或机制词 `主体化`、`客体化`、`去主体化`）。

## 2026-05-08 19:18 CST — W3 batch 3 人民义项完成

- 已完成 `人民` 术语义项扩展（5 条 draft）并追加：
  - `term:人民:s01`（人民性，复数化/他者化主体位）
  - `term:人民:s02`（历史—人民→理论链中的中介位）
  - `term:人民:s03`（人民理论化）
  - `term:人民:s04`（人民作为天然理论家）
  - `term:人民:s05`（人民可数单元性/individuality）
- 已更新并同步 W3 人类可读层与歧义记录：
  - `knowledge/lexicon/core-terms.md`（新增 `人民` section）
  - `knowledge/lexicon/ambiguous-terms.md`（新增 `人民` ambiguity note）
- 已更新 W3 审计记录：
  - 追加 `knowledge/qa/w3-lexicon-audit.md` 的 Batch 3 审计段
- 已更新 `knowledge/STATE.md`（当前批次切为 W3-B3、W3 进度更新、下一建议改为 `理论`）。
- 下一批建议：`理论`（或机制词 `主体化`、`客体化`、`去主体化`）。
- 注意：本批尚未做任何 canonical 提升。

## 2026-05-08 19:20 CST — W3 人民批次证据精炼

- 按 row-level 证据可复核原则，对 `term:人民` 5 条义项的 `evidence_quotes` 做了精炼/对齐：
  - 修正 `人民:s01` 将“愚笨”改为文本中的“愚蠢”，并裁切为可检索的原文片段；
  - 将 `人民:s02` 的 `人民` 中介位证据按行重排（row 276/299）；
  - 将 `人民:s04` 的 `“4144”` 使用源文中的中文引号（smart quote）。
- 结果：`人民` 相关 5 条义项在 `row` 指定路径下均通过原文子串核验。
- 继续建议：进入下一项 `理论`。

## 2026-05-08 19:30 CST — W3 batch 4 理论义项完成

- 已完成 `理论` 术语义项扩展（5 条 draft）并追加：
  - `term:理论:s01`（中介项）
  - `term:理论:s02`（符号系统性与历史性）
  - `term:理论:s03`（理论的生产性）
  - `term:理论:s04`（理论-现实对象化/主体化回路）
  - `term:理论:s05`（理论现实化与通俗化）
- 已更新并同步 W3 人类可读层与歧义记录：
  - `knowledge/lexicon/core-terms.md`（新增 `理论` section）
  - `knowledge/lexicon/ambiguous-terms.md`（新增 `理论` ambiguity）
- 已更新 W3 审计记录：
  - 追加 `knowledge/qa/w3-lexicon-audit.md` 的 Batch 4 条目
- 已更新 `knowledge/STATE.md`（当前批次切为 W3-B4、核心义项计数更新、下一建议：机制词）。
- 所有新增记录仍为 `draft`，未进行 canonical 提升。

## 2026-05-08 20:40 CST — W3 batch 5 机制词义项完成

- 已完成机制词义项扩展（3 条 draft）并追加：
  - `term:主体化:s01`
  - `term:客体化:s01`
  - `term:去主体化:s01`
- 已更新 `knowledge/lexicon/term-senses.jsonl`（共计 31 条；新增3条机制词）。
- 已同步/更新 W3 人类可读层与歧义说明文件：
  - `knowledge/lexicon/core-terms.md`（机制词 subsection）
  - `knowledge/lexicon/ambiguous-terms.md`（机制词高歧义说明仍按 draft 保持）
- 已追加 `knowledge/qa/w3-lexicon-audit.md` 的 Batch 5 条目
- 已更新 `knowledge/STATE.md`（当前批次切为 W3-B5；核心义项计数更新为 31；下一步转入 W5 关系资产）。
- 所有新增记录仍为 `draft`，未进行 canonical 提升。

## 2026-05-08 20:50 CST — W5 batch 1 关系资产首批完成

- 已按低 token 模式启动 W5，只读取 W5 规范、STATE 与相关 term-senses。
- 新建 `knowledge/relations/relation-assets.jsonl`，首批 12 条 draft relations：
  - 机制转换：去主体化 → 客体化 → 客体/实践
  - 理论生产：理论 → 客体化/主体化
  - 机制张力：主体化/客体化/去主体化
  - 三元中介：历史/人民/理论
  - 主体落点：实践单元
  - 机制词/名词义项边界
- 新建关系卡与提示：
  - `knowledge/relations/relation-prompts.md`
  - `knowledge/relations/route-cards.md`
  - `knowledge/relations/tension-cards.md`
  - `knowledge/relations/mediation-cards.md`
  - `knowledge/relations/boundary-cards.md`
  - `knowledge/relations/misrecognition-cards.md`
- 新建 `knowledge/qa/w5-relation-audit.md`。
- 已更新 `knowledge/STATE.md`：当前阶段切为 W5-B1，relation assets 计数为 12。
- 所有关系均为 `draft`；未进行 canonical 提升。

## 2026-05-08 21:20 CST — 仓库主线交接与旧线归档

- 将仓库主线明确切换为：ISMISM 理论知识库消化与关系资产建模。
- 新建主线交接文档：
  - `ISMISM-MAINLINE-HANDOFF.md`
- 归档旧过程/旧原型快照：
  - `docs/archive/legacy-cleanup-handoff-2026-04-17.md`
  - `docs/archive/legacy-readme-frontend-prototype-2026-04-21.md`
  - `docs/archive/legacy-process-and-prototype-index.md`
- 重写根 `README.md`，以 `knowledge/` 处理层为当前入口。
- 将根 `ISMISM-CLEANUP-HANDOFF.md` 改为兼容性归档指针，禁止从旧 clean-corpus 主线恢复。
- 更新 `AGENTS.md`、`knowledge/README.md`、`knowledge/STATE.md`，明确旧前端/Atlas/过程杂项均为 legacy/candidate/derived，不牵引当前主线。

## 2026-05-08 22:04 CST — W3 candidate-only 本地 gemma4 后台任务启动

- 新增并使用脚本：`knowledge/scripts/generate_w3_candidates_with_ollama.py`。
- 启动后台任务：`W3-candidates-gemma4-10h`，模型 `gemma4:latest`，由 `timeout 10h` 限制最长运行时间。
- 处理范围：`中介`、`实体`、`物质`、`符号`、`符号秩序`、`场`、`本体论`、`认识论`、`目的论`、`意识形态`、`理论家`、`实践单元`、`闭合`、`有限性`、`误认`、`跃迁`。
- 输出目录：`knowledge/lexicon/candidates/`。
- 该任务只生成 candidate-only 文件，不修改正式 W3 registry，不更新 canonical。

## 2026-05-09 09:08 CST — W3 fullscan candidate-only 本地 gemma4 50小时任务启动

- 新增脚本：`knowledge/scripts/generate_w3_fullscan_candidates_with_ollama.py`。
- 启动后台任务：`W3-fullscan-gemma4-50h`，模型 `gemma4:latest`，由 `timeout 50h` 限制最长运行时间。
- 处理范围：指定术语的全 363 段 clean 文本扫描，命中 row 分片送入 gemma4：
  - `中介`、`实体`、`物质`、`符号`、`符号秩序`、`场域`、`场域论`、`本体论`、`认识论`、`目的论`
  - `意识形态`、`理论家`、`实践单元`、`闭合`、`有限性`、`误认`、`跃迁`
  - `主体性`、`客体性`、`历史性`、`现实`、`现实化`、`生活`
  - `异化`、`物神化`、`欲望`、`他者`、`大他者`、`客体小a`
  - `结构`、`矛盾`、`伦理`、`规范性`、`时间性`、`空间性`
  - `现象`、`实存`、`自由`、`绝对`、`普遍`、`特殊`
- 参数：`max_rows_per_term=180`、`windows_per_row=2`、`shard_size=6`、`window_chars=900`。
- 输出目录：`knowledge/lexicon/candidates/fullscan/W3-fullscan-gemma4-50h/`。
- PID 文件：`knowledge/lexicon/candidates/fullscan/W3-fullscan-gemma4-50h.pid`。
- 该任务只生成 candidate-only 分片与 summary，不修改正式 W3 registry，不更新 canonical。

## 2026-06-03 19:25 CST — W3 batch 6 频率驱动扩展与证据校验脚本

- 按 `MASTER-SPEC.md` 第一期路线恢复主线：当前 W3 未满足进入 W4 的前置条件，因此继续术语层扩展。
- 新增 W3 校验脚本：`knowledge/scripts/validate_w3_term_senses.py`，验证 JSONL 基础字段、`draft` 状态、source path、evidence quote 在 `split_md_clean/` 中的逐字子串匹配。
- 修正 `term:历史:s01-s05` 中 8 条旧 evidence_quote，使全库现有 quote 通过严格子串验证；未改动这些 sense 的 definition/status。
- 新增 `W3-B6-2026-06-03` draft 义项 14 条：
  - `实体` 5 条：矩阵实体侧、实体一元论、斯宾诺莎实体整体、actual entity、实体化力量；
  - `物质` 4 条：自我符号化、反物质/外在异性他者、小体论、物质现实否定性；
  - `意识形态` 5 条：连贯话语、国家机器质询、犬儒幌子/现实对立、暴力维持、意识形态闭合。
- 更新：`knowledge/lexicon/term-senses.jsonl`、`core-terms.md`、`ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`、`knowledge/STATE.md`。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B6-2026-06-03` → records=14, terms=3, quotes=29, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=45, terms=12, quotes=121, errors=0, warnings=0。
- 所有新增义项保持 `draft`；未进行 canonical 提升；Atlas/candidate 文件仅作线索，不作正式证据。

## 2026-06-03 19:45 CST — W3 batch 7 轴术语扩展

- 继续 MASTER-SPEC 第一期 C 类轴术语拆分，新增 `W3-B7-2026-06-03` draft 义项 12 条：
  - `本体论` 4 条：四轴维度、时间哲学本体论化、差异本体论单元、本体论化/守阵地策略；
  - `认识论` 4 条：四轴维度、被废掉/虚空化的认识论、认识论主体/实践单元、先验构造/差异性结构认识论；
  - `目的论` 4 条：贯穿性目的论维度、伦理/行为准则、宇宙/体系运行方向、目的论缺失/秩序支配。
- 更新：`knowledge/lexicon/term-senses.jsonl`（57 条）、`core-terms.md`、`ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`、`knowledge/STATE.md`、`ISMISM-MAINLINE-HANDOFF.md`。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B7-2026-06-03` → records=12, terms=3, quotes=27, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=57, terms=15, quotes=148, errors=0, warnings=0。
- 所有新增义项保持 `draft`；`场域论` 尚待下一批补齐。

## 2026-06-03 20:20 CST — W3 batch 8 场域论与符号簇扩展

- 继续 MASTER-SPEC 第一期，新增 `W3-B8-2026-06-03` draft 义项 13 条：
  - `场域论` 4 条：四轴维度、实在论均匀世界场、二字头分裂/二重化场域、时间/空间场域配置；
  - `符号` 5 条：对象定位系统、卡西尔文化符号活动、能指/信号系统优先性、符号系统进入与第一人称意识、符号学框架超定论证能力；
  - `符号秩序` 4 条：二字头背景 symbolic order、语用内容超定秩序、金钱/资本自我增殖秩序、无为支点承载秩序。
- 更新：`knowledge/lexicon/term-senses.jsonl`（70 条）、`core-terms.md`、`ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`、`knowledge/STATE.md`、`ISMISM-MAINLINE-HANDOFF.md`。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B8-2026-06-03` → records=13, terms=3, quotes=27, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=70, terms=18, quotes=175, errors=0, warnings=0。
- 四轴术语已全部具备 draft 义项；W3 总量仍不足进入 W4 的建议前置（≥100 条 sense），下一步继续 `中介/理论家/实践单元/闭合/有限性` 等高频/共现词。

## 2026-06-03 21:05 CST — W3 batch 9/10 达到 W4 最低前置

- 新增 `W3-B9-2026-06-03` draft 义项 13 条：`中介`5、`理论家`4、`实践单元`4。
- 新增 `W3-B10-2026-06-03` draft 义项 17 条：`闭合`5、`有限性`5、`误认`4、`跃迁`3。
- 更新：`knowledge/lexicon/term-senses.jsonl`（100 条）、`core-terms.md`、`ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`、`knowledge/STATE.md`、`ISMISM-MAINLINE-HANDOFF.md`。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B9-2026-06-03` → records=13, terms=3, quotes=26, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B10-2026-06-03` → records=17, terms=4, quotes=34, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
- W3 已达到 W4 position cards 的最低前置建议（W3 ≥100 且四轴术语已拆分）；但 MASTER-SPEC 第一期正式门槛仍是 ≥300 sense，最终 W3 硬指标为 ≥200 terms / ≥500 senses。
- 下一步建议：启动 W4 L1 position cards（4 张一级强卡），并继续 W3 扩展；所有 W3 义项仍保持 `draft`，不得 canonical 提升。

## 2026-06-08 CST — W4 L1 position cards completed

- 在 W3 达到 100 条 draft sense 且四轴术语均已拆分后，启动 W4。
- 新建 W4 L1 cards：
  - `knowledge/position-cards/1.md` — 实在论
  - `knowledge/position-cards/2.md` — 形而上学
  - `knowledge/position-cards/3.md` — 观念论
  - `knowledge/position-cards/4.md` — 实践
  - `knowledge/position-cards/index.md` — W4-L1 partial index
- 新增 W4 校验脚本：`knowledge/scripts/validate_w4_position_cards.py`。
- 新增审计记录：`knowledge/qa/w4-position-audit.md`。
- 验证结果：`python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
- 所有 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升。
- 下一步：继续 W4-L2（16 张二级位置卡），同时继续 W3 扩展到 ≥300 sense。

## 2026-06-08 CST — W4 L2 batch 1 field-1 position cards completed

- 继续 W4 position-card 层，从 field=1 创建首批 4 张 L2 cards：
  - `knowledge/position-cards/1-1.md` — 科学实在论
  - `knowledge/position-cards/1-2.md` — 宗教实在论
  - `knowledge/position-cards/1-3.md` — 庸俗唯我论（复习课）
  - `knowledge/position-cards/1-4.md` — 平庸主义
- 更新 `knowledge/position-cards/index.md`：L2 coverage 从 0/16 更新为 4/16，total position cards 从 4 更新为 8。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L2-B1-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L2 field 2（`2-1`–`2-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 4` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L2 batch 2 field-2 position cards completed

- 继续 W4-L2，完成 field=2（形而上学）四张二级 cards：
  - `knowledge/position-cards/2-1.md` — 在场形而上学
  - `knowledge/position-cards/2-2.md` — 辩证形而上学
  - `knowledge/position-cards/2-3.md` — 我思形而上学
  - `knowledge/position-cards/2-4.md` — 反形而上学
- 更新 `knowledge/position-cards/index.md`：L2 coverage 从 4/16 更新为 8/16，total position cards 从 8 更新为 12。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L2-B2-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L2 field 3（`3-1`–`3-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 8` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L2 batch 3 field-3 position cards completed

- 继续 W4-L2，完成 field=3（观念论）四张二级 cards：
  - `knowledge/position-cards/3-1.md` — 现象学
  - `knowledge/position-cards/3-2.md` — 德国观念论
  - `knowledge/position-cards/3-3.md` — 生存论
  - `knowledge/position-cards/3-4.md` — 符号学
- 更新 `knowledge/position-cards/index.md`：L2 coverage 从 8/16 更新为 12/16，total position cards 从 12 更新为 16。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L2-B3-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L2 field 4（`4-1`–`4-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 12` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L2 batch 4 field-4 position cards completed; L2 complete

- 继续 W4-L2，完成 field=4（实践）四张二级 cards：
  - `knowledge/position-cards/4-1.md` — 政治-经济-意识形态批判
  - `knowledge/position-cards/4-2.md` — 现实的正统化
  - `knowledge/position-cards/4-3.md` — 建设理想社会
  - `knowledge/position-cards/4-4.md` — 不可能的乌托邦
- 更新 `knowledge/position-cards/index.md`：L2 coverage 从 12/16 更新为 16/16，total position cards 从 16 更新为 20。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L2-B4-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3（64 张三级卡）规划/启动及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
- W4-L2 已完成 16/16 draft cards；W4-L3/W4-L4 仍 pending；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 1 started; 1-1 subtree completed

- 启动 W4-L3（64 张三级位置卡）首批，完成 `1-1` 科学实在论下 4 张 cards：
  - `knowledge/position-cards/1-1-1.md` — 物理主义
  - `knowledge/position-cards/1-1-2.md` — 建构论
  - `knowledge/position-cards/1-1-3.md` — 认知主义
  - `knowledge/position-cards/1-1-4.md` — 行为主义
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 0/64 更新为 4/64，total position cards 从 20 更新为 24。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B1-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 后续批次（建议 `1-2-1`–`1-2-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 4` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 2 completed; 1-2 subtree completed

- 继续 W4-L3，完成 `1-2` 宗教实在论下 4 张三级 cards：
  - `knowledge/position-cards/1-2-1.md` — 神创论
  - `knowledge/position-cards/1-2-2.md` — 偶像论／偶像崇拜
  - `knowledge/position-cards/1-2-3.md` — 唯灵论
  - `knowledge/position-cards/1-2-4.md` — 反偶像论
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 4/64 更新为 8/64，total position cards 从 24 更新为 28。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B2-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 后续批次（建议 `1-3-1`–`1-3-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 8` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 3 completed; 1-3 subtree completed

- 继续 W4-L3，完成 `1-3` 庸俗唯我论（复习课）下 4 张三级 cards：
  - `knowledge/position-cards/1-3-1.md` — 伪唯心主义
  - `knowledge/position-cards/1-3-2.md` — 本真主义
  - `knowledge/position-cards/1-3-3.md` — 唯意志主义
  - `knowledge/position-cards/1-3-4.md` — 直觉主义／体验主义／意识流
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 8/64 更新为 12/64，total position cards 从 28 更新为 32。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B3-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 后续批次（建议 `1-4-1`–`1-4-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 12` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 4 completed; field 1 L3 complete

- 继续 W4-L3，完成 `1-4` 平庸主义下 4 张三级 cards：
  - `knowledge/position-cards/1-4-1.md` — 当代自然主义
  - `knowledge/position-cards/1-4-2.md` — 世俗人道主义
  - `knowledge/position-cards/1-4-3.md` — 心理主义
  - `knowledge/position-cards/1-4-4.md` — 庸俗主义
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 12/64 更新为 16/64，total position cards 从 32 更新为 36；L3 field 1 (`1-1-1`–`1-4-4`) 已完成 draft。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B4-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 2（建议 `2-1-1`–`2-1-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 16` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 5 completed; 2-1 subtree completed

- 继续 W4-L3 field 2，完成 `2-1` 在场形而上学下 4 张三级 cards：
  - `knowledge/position-cards/2-1-1.md` — 普遍主义
  - `knowledge/position-cards/2-1-2.md` — 本质主义
  - `knowledge/position-cards/2-1-3.md` — 合理主义
  - `knowledge/position-cards/2-1-4.md` — 绝对主义
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 16/64 更新为 20/64，total position cards 从 36 更新为 40。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B5-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 2 后续批次（建议 `2-2-1`–`2-2-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 20` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 6 completed; 2-2 subtree completed

- 继续 W4-L3 field 2，完成 `2-2` 辩证形而上学下 4 张三级 cards：
  - `knowledge/position-cards/2-2-1.md` — 无限主义
  - `knowledge/position-cards/2-2-2.md` — 否定主义
  - `knowledge/position-cards/2-2-3.md` — 超验主义
  - `knowledge/position-cards/2-2-4.md` — 反二元对立
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 20/64 更新为 24/64，total position cards 从 40 更新为 44。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B6-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 2 后续批次（建议 `2-3-1`–`2-3-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 24` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 7 completed; 2-3 subtree completed

- 继续 W4-L3 field 2，完成 `2-3` 我思形而上学下 4 张三级 cards：
  - `knowledge/position-cards/2-3-1.md` — 实体一元论
  - `knowledge/position-cards/2-3-2.md` — 心物二元论
  - `knowledge/position-cards/2-3-3.md` — 单子主义
  - `knowledge/position-cards/2-3-4.md` — 宇宙平等主义
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 24/64 更新为 28/64，total position cards 从 44 更新为 48。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B7-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 2 后续批次（建议 `2-4-1`–`2-4-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 28` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 8 completed; field 2 L3 complete

- 继续 W4-L3 field 2，完成 `2-4` 反形而上学下 4 张三级 cards：
  - `knowledge/position-cards/2-4-1.md` — 经验主义
  - `knowledge/position-cards/2-4-2.md` — 实证主义
  - `knowledge/position-cards/2-4-3.md` — 逻辑实证主义
  - `knowledge/position-cards/2-4-4.md` — 实用主义
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 28/64 更新为 32/64，total position cards 从 48 更新为 52；L3 field 2 (`2-1-1`–`2-4-4`) 已完成 draft。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B8-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 3（建议 `3-1-1`–`3-1-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 32` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 9 completed; 3-1 subtree completed

- 启动 W4-L3 field 3，完成 `3-1` 现象学下 4 张三级 cards：
  - `knowledge/position-cards/3-1-1.md` — 先验现象学
  - `knowledge/position-cards/3-1-2.md` — 实事现象学
  - `knowledge/position-cards/3-1-3.md` — 生活世界现象学
  - `knowledge/position-cards/3-1-4.md` — 现世的现象学
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 32/64 更新为 36/64，total position cards 从 52 更新为 56。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B9-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 3 后续批次（建议 `3-2-1`–`3-2-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 36` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 10 completed; 3-2 subtree completed

- 继续 W4-L3 field 3，完成 `3-2` 德国观念论下 4 张三级 cards：
  - `knowledge/position-cards/3-2-1.md` — 批判哲学
  - `knowledge/position-cards/3-2-2.md` — 知识学
  - `knowledge/position-cards/3-2-3.md` — 体系自由主义
  - `knowledge/position-cards/3-2-4.md` — 辩证法
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 36/64 更新为 40/64，total position cards 从 56 更新为 60。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B10-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 3 后续批次（建议 `3-3-1`–`3-3-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 40` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 11 completed; 3-3 subtree completed

- 继续 W4-L3 field 3，完成 `3-3` 生存论下 4 张三级 cards：
  - `knowledge/position-cards/3-3-1.md` — 存在主义（Beingism）
  - `knowledge/position-cards/3-3-2.md` — 真正的生存主义
  - `knowledge/position-cards/3-3-3.md` — 同一生存论
  - `knowledge/position-cards/3-3-4.md` — 虚构的生存论
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 40/64 更新为 44/64，total position cards 从 60 更新为 64。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B11-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 3 后续批次（建议 `3-4-1`–`3-4-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 44` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 12 completed; 3-4 subtree and field 3 L3 completed

- 继续 W4-L3 field 3，完成 `3-4` 符号学下 4 张三级 cards：
  - `knowledge/position-cards/3-4-1.md` — 结构主义
  - `knowledge/position-cards/3-4-2.md` — 后结构主义
  - `knowledge/position-cards/3-4-3.md` — 差异的辩证法
  - `knowledge/position-cards/3-4-4.md` — 解释学
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 44/64 更新为 48/64，total position cards 从 64 更新为 68；L3 field 3 (`3-1-1`–`3-4-4`) 已完成 draft。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B12-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 4（建议 `4-1-1`–`4-1-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 48` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 13 completed; 4-1 subtree completed

- 启动 W4-L3 field 4，完成 `4-1` 政治-经济-意识形态批判下 4 张三级 cards：
  - `knowledge/position-cards/4-1-1.md` — 资本主义史研究
  - `knowledge/position-cards/4-1-2.md` — 灌输
  - `knowledge/position-cards/4-1-3.md` — 历史的哲学化
  - `knowledge/position-cards/4-1-4.md` — 精神化了的重复
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 48/64 更新为 52/64，total position cards 从 68 更新为 72。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B13-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 4 后续批次（建议 `4-2-1`–`4-2-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 52` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 14 completed; 4-2 subtree completed

- 继续 W4-L3 field 4，完成 `4-2` 现实的正统化下 4 张三级 cards：
  - `knowledge/position-cards/4-2-1.md` — 合律组织
  - `knowledge/position-cards/4-2-2.md` — L主义
  - `knowledge/position-cards/4-2-3.md` — 真正的国际主义
  - `knowledge/position-cards/4-2-4.md` — 再来一次！
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 52/64 更新为 56/64，total position cards 从 72 更新为 76。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B14-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 4 后续批次（建议 `4-3-1`–`4-3-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 56` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 15 completed; 4-3 subtree completed

- 继续 W4-L3 field 4，完成 `4-3` 建设理想社会下 4 张三级 cards：
  - `knowledge/position-cards/4-3-1.md` — 生活必须品
  - `knowledge/position-cards/4-3-2.md` — 对于生产活动的解放——要抢在历史惯性前头积极做出改变
  - `knowledge/position-cards/4-3-3.md` — 战略-战役-战斗的统合
  - `knowledge/position-cards/4-3-4.md` — s主义的资本实现
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 56/64 更新为 60/64，total position cards 从 76 更新为 80。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B15-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L3 field 4 最后一批（建议 `4-4-1`–`4-4-4`）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 60` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L3 batch 16 completed; field 4 and W4-L3 completed

- 完成 W4-L3 field 4，完成 `4-4` 不可能的乌托邦下 4 张三级 cards：
  - `knowledge/position-cards/4-4-1.md` — 计划良好的人性生活方式
  - `knowledge/position-cards/4-4-2.md` — 去人类中心化
  - `knowledge/position-cards/4-4-3.md` — 对合／内卷
  - `knowledge/position-cards/4-4-4.md` — 有序的深渊
- 更新 `knowledge/position-cards/index.md`：L3 coverage 从 60/64 更新为 64/64，total position cards 从 80 更新为 84；W4-L3 (`1-1-1`–`4-4-4`) 已完成 draft。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L3-B16-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 light cards 或 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 1 started; 8 light cards created

- 启动 W4-L4 light cards，完成科学实在论下 `1-1-1` 与 `1-1-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-1-1-1.md` — 科学独断论
  - `knowledge/position-cards/1-1-1-2.md` — 有机进化论
  - `knowledge/position-cards/1-1-1-3.md` — 科学消费主义
  - `knowledge/position-cards/1-1-1-4.md` — 宇宙悲观主义
  - `knowledge/position-cards/1-1-2-1.md` — 科学知识社会学
  - `knowledge/position-cards/1-1-2-2.md` — 科学革命论
  - `knowledge/position-cards/1-1-2-3.md` — 文化本体论
  - `knowledge/position-cards/1-1-2-4.md` — 解构建构论
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 0 更新为 8，total position cards 从 84 更新为 92。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B1-2026-06-08` 审计记录。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 8` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 2 completed; 1-1 L4 subtree completed

- 继续 W4-L4 light cards，完成科学实在论下 `1-1-3` 与 `1-1-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-1-3-1.md` — 功能主义
  - `knowledge/position-cards/1-1-3-2.md` — 自由进化论
  - `knowledge/position-cards/1-1-3-3.md` — 认知自我主义
  - `knowledge/position-cards/1-1-3-4.md` — 认知无我论
  - `knowledge/position-cards/1-1-4-1.md` — 操作行为主义
  - `knowledge/position-cards/1-1-4-2.md` — 目的行为主义
  - `knowledge/position-cards/1-1-4-3.md` — 应用行为分析
  - `knowledge/position-cards/1-1-4-4.md` — 社会行为主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 8 更新为 16，total position cards 从 92 更新为 100；`1-1` subtree 的 L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B2-2026-06-08` 审计记录。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 16` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 3 completed; 1-2-1 and 1-2-2 L4 subtrees completed

- 继续 W4-L4 light cards，完成宗教实在论下 `1-2-1` 与 `1-2-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-2-1-1.md` — 自然神论
  - `knowledge/position-cards/1-2-1-2.md` — 神义论
  - `knowledge/position-cards/1-2-1-3.md` — 一元论诺斯替主义
  - `knowledge/position-cards/1-2-1-4.md` — 模态位格一元论
  - `knowledge/position-cards/1-2-2-1.md` — 传殖主义
  - `knowledge/position-cards/1-2-2-2.md` — 部分主义
  - `knowledge/position-cards/1-2-2-3.md` — 拜物教——读懂资本论的必修课：物神崇拜的符号学功能；偶像崇拜的第三种形式
  - `knowledge/position-cards/1-2-2-4.md` — 时间崇拜——偶像崇拜的终极形式：论时间之神 Aion、狄奥尼索斯与奥菲欧斯的三位一体，节庆、永恒、往生、死亡崇拜背后的意识形态机制
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 16 更新为 24，total position cards 从 100 更新为 108。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B3-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `1-2-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 24` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 4 completed; 1-2 L4 subtree completed

- 继续 W4-L4 light cards，完成宗教实在论下 `1-2-3` 与 `1-2-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-2-3-1.md` — 永生主义
  - `knowledge/position-cards/1-2-3-2.md` — 回归式唯灵论
  - `knowledge/position-cards/1-2-3-3.md` — 魔法师主义
  - `knowledge/position-cards/1-2-3-4.md` — 弃绝主义
  - `knowledge/position-cards/1-2-4-1.md` — 作为信仰的命定论
  - `knowledge/position-cards/1-2-4-2.md` — 救世主主义
  - `knowledge/position-cards/1-2-4-3.md` — 神智论
  - `knowledge/position-cards/1-2-4-4.md` — 神爱论，神圣的爱
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 24 更新为 32，total position cards 从 108 更新为 116；`1-2` 宗教实在论 subtree 的 L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B4-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `1-3-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 32` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 5 completed; 1-3-1 and 1-3-2 L4 subtrees completed

- 继续 W4-L4 light cards，完成庸俗唯我论下 `1-3-1` 与 `1-3-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-3-1-1.md` — 客观唯心主义
  - `knowledge/position-cards/1-3-1-2.md` — 主观唯心主义
  - `knowledge/position-cards/1-3-1-3.md` — 现实唯心主义
  - `knowledge/position-cards/1-3-1-4.md` — 唯梦论
  - `knowledge/position-cards/1-3-2-1.md` — 现代斯多亚主义
  - `knowledge/position-cards/1-3-2-2.md` — 现代犬儒主义
  - `knowledge/position-cards/1-3-2-3.md` — 现代爱情主义／现代新柏拉图主义
  - `knowledge/position-cards/1-3-2-4.md` — 现代智者主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 32 更新为 40，total position cards 从 116 更新为 124。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B5-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `1-3-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 40` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 6 completed; 1-3 L4 subtree completed

- 继续 W4-L4 light cards，完成庸俗唯我论下 `1-3-3` 与 `1-3-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-3-3-1.md` — 自我中心主义
  - `knowledge/position-cards/1-3-3-2.md` — 道德严酷主义
  - `knowledge/position-cards/1-3-3-3.md` — 排他的集体主义
  - `knowledge/position-cards/1-3-3-4.md` — 厌女—虚无主义
  - `knowledge/position-cards/1-3-4-1.md` — 伦理行动主义
  - `knowledge/position-cards/1-3-4-2.md` — 随笔主义
  - `knowledge/position-cards/1-3-4-3.md` — 唯美主义
  - `knowledge/position-cards/1-3-4-4.md` — 颓废主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 40 更新为 48，total position cards 从 124 更新为 132；`1-3` subtree 的 L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B6-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `1-4-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 48` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 7 completed; 1-4-1 and 1-4-2 L4 subtrees completed

- 继续 W4-L4 light cards，完成平庸主义下 `1-4-1` 与 `1-4-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-4-1-1.md` — 和平主义
  - `knowledge/position-cards/1-4-1-2.md` — 客观主义
  - `knowledge/position-cards/1-4-1-3.md` — 沉默主义
  - `knowledge/position-cards/1-4-1-4.md` — 蒙昧主义
  - `knowledge/position-cards/1-4-2-1.md` — 纵容主义
  - `knowledge/position-cards/1-4-2-2.md` — 多元文化主义
  - `knowledge/position-cards/1-4-2-3.md` — 环保主义
  - `knowledge/position-cards/1-4-2-4.md` — 性解放主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 48 更新为 56，total position cards 从 132 更新为 140。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B7-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `1-4-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 56` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 8 completed; field 1 L4 coverage completed

- 继续 W4-L4 light cards，完成平庸主义下 `1-4-3` 与 `1-4-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/1-4-3-1.md` — 情绪主义
  - `knowledge/position-cards/1-4-3-2.md` — 心理正常主义
  - `knowledge/position-cards/1-4-3-3.md` — 泛性主义
  - `knowledge/position-cards/1-4-3-4.md` — 密契女性主义
  - `knowledge/position-cards/1-4-4-1.md` — 顺从主义
  - `knowledge/position-cards/1-4-4-2.md` — 粗俗主义
  - `knowledge/position-cards/1-4-4-3.md` — 四重竞争主义
  - `knowledge/position-cards/1-4-4-4.md` — 复仇主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 56 更新为 64，total position cards 从 140 更新为 148；field 1 L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B8-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-1-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 64` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 9 completed; field 2 L4 coverage started through 2-1-2

- 继续 W4-L4 light cards，完成在场形而上学下 `2-1-1` 与 `2-1-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-1-1-1.md` — 阿派朗（无界限）主义
  - `knowledge/position-cards/2-1-1-2.md` — 气动一元论
  - `knowledge/position-cards/2-1-1-3.md` — 分形多元论
  - `knowledge/position-cards/2-1-1-4.md` — 形而上辩证主义
  - `knowledge/position-cards/2-1-2-1.md` — 伦理智性主义
  - `knowledge/position-cards/2-1-2-2.md` — 理念实在论／理想现实主义
  - `knowledge/position-cards/2-1-2-3.md` — 范畴实在论／绝对现实主义
  - `knowledge/position-cards/2-1-2-4.md` — 多产的不动论
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 64 更新为 72，total position cards 从 148 更新为 156；field 2 L4 覆盖启动并推进至 `2-1-2`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B9-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-1-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 72` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 10 completed; 2-1 L4 subtree completed

- 继续 W4-L4 light cards，完成在场形而上学下 `2-1-3` 与 `2-1-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-1-3-1.md` — 反应多元论
  - `knowledge/position-cards/2-1-3-2.md` — 贫乏的原子论
  - `knowledge/position-cards/2-1-3-3.md` — 智性享乐主义
  - `knowledge/position-cards/2-1-3-4.md` — 犬儒主义
  - `knowledge/position-cards/2-1-4-1.md` — 相对主义
  - `knowledge/position-cards/2-1-4-2.md` — 怀疑主义
  - `knowledge/position-cards/2-1-4-3.md` — 记忆主义
  - `knowledge/position-cards/2-1-4-4.md` — 话语主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 72 更新为 80，total position cards 从 156 更新为 164；`2-1` L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B10-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-2-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 80` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 11 completed; 2-2 L4 coverage started through 2-2-2

- 继续 W4-L4 light cards，完成辩证形而上学下 `2-2-1` 与 `2-2-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-2-1-1.md` — 分子业力主义
  - `knowledge/position-cards/2-2-1-2.md` — 永恒时态主义
  - `knowledge/position-cards/2-2-1-3.md` — 灵魂示踪主义／种子形而上学
  - `knowledge/position-cards/2-2-1-4.md` — 摩尔唯心主义
  - `knowledge/position-cards/2-2-2-1.md` — 无为主义
  - `knowledge/position-cards/2-2-2-2.md` — 积极的神秘主义
  - `knowledge/position-cards/2-2-2-3.md` — 人道的自然主义
  - `knowledge/position-cards/2-2-2-4.md` — 实用的神秘主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 80 更新为 88，total position cards 从 164 更新为 172；`2-2` L4 draft 覆盖启动并推进至 `2-2-2`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B11-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-2-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 88` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 12 completed; 2-2 L4 subtree completed

- 继续 W4-L4 light cards，完成辩证形而上学下 `2-2-3` 与 `2-2-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-2-3-1.md` — 历史符号主义
  - `knowledge/position-cards/2-2-3-2.md` — 形而上神秘主义
  - `knowledge/position-cards/2-2-3-3.md` — 理性唯灵论
  - `knowledge/position-cards/2-2-3-4.md` — 诗的形而上学
  - `knowledge/position-cards/2-2-4-1.md` — 具有伦理热忱的虚无主义
  - `knowledge/position-cards/2-2-4-2.md` — 可辩的道德箴言
  - `knowledge/position-cards/2-2-4-3.md` — 新实用主义
  - `knowledge/position-cards/2-2-4-4.md` — 原始的现象学／分析哲学
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 88 更新为 96，total position cards 从 172 更新为 180；`2-2` L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B12-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-3-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 96` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 13 completed; 2-3 L4 coverage started through 2-3-2

- 继续 W4-L4 light cards，完成我思形而上学下 `2-3-1` 与 `2-3-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-3-1-1.md` — 渐进无限主义
  - `knowledge/position-cards/2-3-1-2.md` — 运动的静止主义
  - `knowledge/position-cards/2-3-1-3.md` — 实体整体主义
  - `knowledge/position-cards/2-3-1-4.md` — 辩证一元论
  - `knowledge/position-cards/2-3-2-1.md` — 理性动物主义
  - `knowledge/position-cards/2-3-2-2.md` — 理性神秘主义
  - `knowledge/position-cards/2-3-2-3.md` — 超越的内在论
  - `knowledge/position-cards/2-3-2-4.md` — 现代理性主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 96 更新为 104，total position cards 从 180 更新为 188；`2-3` L4 draft 覆盖启动并推进至 `2-3-2`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B13-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-3-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 104` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 14 completed; 2-3 L4 subtree completed

- 继续 W4-L4 light cards，完成我思形而上学下 `2-3-3` 与 `2-3-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-3-3-1.md` — 前定主义
  - `knowledge/position-cards/2-3-3-2.md` — 体系完美主义
  - `knowledge/position-cards/2-3-3-3.md` — 逻辑原子主义
  - `knowledge/position-cards/2-3-3-4.md` — 分割的整体主义
  - `knowledge/position-cards/2-3-4-1.md` — 数理还原主义
  - `knowledge/position-cards/2-3-4-2.md` — 稳定的干涉主义
  - `knowledge/position-cards/2-3-4-3.md` — 物理归纳主义
  - `knowledge/position-cards/2-3-4-4.md` — 时空绝对主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 104 更新为 112，total position cards 从 188 更新为 196；`2-3` L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B14-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-4-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 112` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 15 completed; 2-4 L4 coverage started through 2-4-2

- 继续 W4-L4 light cards，完成反形而上学下 `2-4-1` 与 `2-4-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-4-1-1.md` — 乐于接受的小体主义
  - `knowledge/position-cards/2-4-1-2.md` — 经验的观念论
  - `knowledge/position-cards/2-4-1-3.md` — 理念-精神二元论
  - `knowledge/position-cards/2-4-1-4.md` — 人类有限主义
  - `knowledge/position-cards/2-4-2-1.md` — 自然主义的规范论
  - `knowledge/position-cards/2-4-2-2.md` — 社会实证主义
  - `knowledge/position-cards/2-4-2-3.md` — 自然神论的实证主义
  - `knowledge/position-cards/2-4-2-4.md` — 科学的实证主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 112 更新为 120，total position cards 从 196 更新为 204；`2-4` L4 draft 覆盖启动并推进至 `2-4-2`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B15-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `2-4-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 120` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 16 completed; field 2 L4 subtree completed

- 继续 W4-L4 light cards，完成反形而上学下 `2-4-3` 与 `2-4-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/2-4-3-1.md` — 相对语法主义
  - `knowledge/position-cards/2-4-3-2.md` — 逻辑还原主义
  - `knowledge/position-cards/2-4-3-3.md` — 逻辑行为主义
  - `knowledge/position-cards/2-4-3-4.md` — 逻辑反实在论
  - `knowledge/position-cards/2-4-4-1.md` — 逻辑实用主义
  - `knowledge/position-cards/2-4-4-2.md` — 正统辩证唯物主义
  - `knowledge/position-cards/2-4-4-3.md` — 符号实用主义
  - `knowledge/position-cards/2-4-4-4.md` — 生存实用主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 120 更新为 128，total position cards 从 204 更新为 212；field 2 L4 draft 覆盖完成，下一步建议从 `3-1-1-1` 开始。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B16-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `3-1-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 128` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 17 completed; 3-1 L4 coverage started through 3-1-2

- 继续 W4-L4 light cards，完成现象学下 `3-1-1` 与 `3-1-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/3-1-1-1.md` — 先验直觉主义
  - `knowledge/position-cards/3-1-1-2.md` — 先验本质主义
  - `knowledge/position-cards/3-1-1-3.md` — 反思性的主体主义
  - `knowledge/position-cards/3-1-1-4.md` — 准先验辩证主义
  - `knowledge/position-cards/3-1-2-1.md` — 媒介性的客观主义
  - `knowledge/position-cards/3-1-2-2.md` — 本质心理主义
  - `knowledge/position-cards/3-1-2-3.md` — 现象学的唯美主义
  - `knowledge/position-cards/3-1-2-4.md` — 游戏的世界象征主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 128 更新为 136，total position cards 从 212 更新为 220；`3-1` L4 draft 覆盖启动并推进至 `3-1-2`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B17-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `3-1-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 136` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 18 completed; 3-1 L4 subtree completed

- 继续 W4-L4 light cards，完成现象学下 `3-1-3` 与 `3-1-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/3-1-3-1.md` — 主体间普遍主义
  - `knowledge/position-cards/3-1-3-2.md` — 本土方法论
  - `knowledge/position-cards/3-1-3-3.md` — 格式塔现象学
  - `knowledge/position-cards/3-1-3-4.md` — 自身性现象学
  - `knowledge/position-cards/3-1-4-1.md` — 追问的现象学
  - `knowledge/position-cards/3-1-4-2.md` — 性化的现象学
  - `knowledge/position-cards/3-1-4-3.md` — 存在论的现象学
  - `knowledge/position-cards/3-1-4-4.md` — 现象学伦理主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 136 更新为 144，total position cards 从 220 更新为 228；`3-1` L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B18-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `3-2-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 144` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 19 completed; 3-2 L4 coverage started through 3-2-2

- 继续 W4-L4 light cards，完成德国观念论下 `3-2-1` 与 `3-2-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/3-2-1-1.md` — 无限的有限主义
  - `knowledge/position-cards/3-2-1-2.md` — 先验经验主义
  - `knowledge/position-cards/3-2-1-3.md` — 先验逻辑主义
  - `knowledge/position-cards/3-2-1-4.md` — 符号形式主义
  - `knowledge/position-cards/3-2-2-1.md` — 理智直观主义
  - `knowledge/position-cards/3-2-2-2.md` — 先验观念论
  - `knowledge/position-cards/3-2-2-3.md` — 彻底的经验主义
  - `knowledge/position-cards/3-2-2-4.md` — 唯我的实在论、现实主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 144 更新为 152，total position cards 从 228 更新为 236；`3-2` L4 draft 覆盖启动并推进至 `3-2-2`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B19-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `3-2-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 152` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 CST — W4 L4 batch 20 completed; 3-2 L4 subtree completed

- 继续 W4-L4 light cards，完成德国观念论下 `3-2-3` 与 `3-2-4` 的 8 张四级轻卡：
  - `knowledge/position-cards/3-2-3-1.md` — 时间-本体论
  - `knowledge/position-cards/3-2-3-2.md` — 加倍的德国观念论
  - `knowledge/position-cards/3-2-3-3.md` — 生存论的存在主义
  - `knowledge/position-cards/3-2-3-4.md` — 自身-辩证法
  - `knowledge/position-cards/3-2-4-1.md` — 逻辑学
  - `knowledge/position-cards/3-2-4-2.md` — 否定辩证法
  - `knowledge/position-cards/3-2-4-3.md` — 爱欲辩证法
  - `knowledge/position-cards/3-2-4-4.md` — 意识形态学
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 152 更新为 160，total position cards 从 236 更新为 244；`3-2` L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B20-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `3-3-1-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 160` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。


## 2026-06-08 CST — W4 L4 batch 21 completed; 3-3-1 and 3-3-2 L4 coverage completed

- 继续 W4-L4 light cards，完成生存论下 `3-3-1` 与 `3-3-2` 的 8 张四级轻卡：
  - `knowledge/position-cards/3-3-1-1.md` — 分环节的生存论的存在论
  - `knowledge/position-cards/3-3-1-2.md` — 人道主义的存在主义
  - `knowledge/position-cards/3-3-1-3.md` — 政治的理性主义
  - `knowledge/position-cards/3-3-1-4.md` — 前本体论
  - `knowledge/position-cards/3-3-2-1.md` — 安放了的实存主义
  - `knowledge/position-cards/3-3-2-2.md` — 诗性存在论
  - `knowledge/position-cards/3-3-2-3.md` — 神-人伦理学
  - `knowledge/position-cards/3-3-2-4.md` — 超验-生存论
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 160 更新为 168，total position cards 从 244 更新为 252；`3-3-1` 与 `3-3-2` L4 draft 覆盖完成。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B21-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，将下一步指向 W4-L4 后续批次（建议 `3-3-3-1` 起）及 W3 toward ≥300。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 168` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。


## 2026-06-08 CST — W4 L4 batch 22 completed; current W4 position-card count target reached

- 继续 W4-L4 light cards，完成生存论下 `3-3-3` 的 4 张四级轻卡：
  - `knowledge/position-cards/3-3-3-1.md` — 斗争的生存论
  - `knowledge/position-cards/3-3-3-2.md` — 直接生存论
  - `knowledge/position-cards/3-3-3-3.md` — 共同体的生存论
  - `knowledge/position-cards/3-3-3-4.md` — 金融资本主义
- 更新 `knowledge/position-cards/index.md`：L4 coverage 从 168 更新为 172，total position cards 从 252 更新为 256；当前 MASTER-SPEC W4 count target reached at `3-3-3-4`。
- 更新 `knowledge/qa/w4-position-audit.md`，新增 `W4-L4-B22-2026-06-08` 审计记录。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，下一步转向 W3 toward ≥300、W5 toward 60+，并保留 W4 draft 待 W6 audit。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W4 cards 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。


## 2026-06-08 CST — W3 batch 11 completed; 辩证法/欲望/他者 term senses added

- 继续 MASTER-SPEC W3 term-sense 扩展，新增 12 条 draft sense：
  - `辩证法`：4 条（主体性否定、否定辩证法剩余、历史哲学化、现象学主客/主体间关系）
  - `欲望`：4 条（匮乏再生产、伊壁鸠鲁三类欲望、客体小a对象成因、驱力到欲望的能指链转换）
  - `他者`：4 条（神圣超越大他者、共同体/道德视角、现象学他者性、他者欲望/镜像协调）
- 更新 `knowledge/lexicon/term-senses.jsonl`：W3 从 100 更新为 112 records，terms 从 25 更新为 28。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`，下一步继续 W3 toward ≥300、W5 toward 60+，并保留 W3/W4/W5 draft 待 W6 audit。
- 验证结果：
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B11-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=112, terms=28, quotes=259, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- 所有新增 W3 senses 保持 `draft`；未进行 W3/W5 canonical 提升；未改动 raw/clean corpus 或 legacy Atlas/前端层。

## 2026-06-08 — W3 Batch 12 term-sense expansion (`意识` / `驱力` / `语言`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 112 更新为 124 records，terms 从 28 更新为 31。
- 新增 12 条 draft senses：
  - `意识:s01-s04`（清醒意识结构/四格对应、透明框架/不可专题化、意识流中介/自我区分、观念论体验流/意识内在存在）
  - `驱力:s01-s04`（死亡驱力/意识结构内核、对抗中的反需求/反欲望动力、无意识维持与意识转译、S1驱力到S2欲望）
  - `语言:s01-s04`（意识的背景性场域/二阶结构、天然形而上学/符号实用主义、本体论限制/有限性、语言游戏/工具式使用）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 124 draft senses / 31 terms；W4 仍保持 172/172 draft count target 完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B12-2026-06-08` → records=12, terms=3, quotes=27, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=124, terms=31, quotes=286, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 13 mechanism-term expansion (`主体化` / `客体化` / `去客体化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 124 更新为 136 records，terms 从 31 更新为 32。
- 新增/追加 12 条 draft senses：
  - `主体化:s02-s05`（事件中的本体论更新过程、历史实践生成中的去本体论化、否定性作为主体化力量、本体成主体的发生学过程）
  - `客体化:s02-s05`（历史实践生成中的本体论化、去主体化的外在客体化、灌输中的重新客体化、理论把现实对象化）
  - `去客体化:s01-s04`（反二元矩阵的基本运动、认知主体的自我去客体化、主客二元对立的禁闭前提、客体突破符号学束缚）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 136 draft senses / 32 terms；row 139 四基本运动目前已覆盖，但 `去主体化` 仍需继续扩义。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B13-2026-06-08` → records=12, terms=3, quotes=35, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=136, terms=32, quotes=321, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 14 mechanism-term expansion (`去主体化` / `时间化` / `空间化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 136 更新为 148 records，terms 从 32 更新为 34。
- 新增/追加 12 条 draft senses：
  - `去主体化:s02-s05`（反二元矩阵的基本运动、意向性结构的去先验主体化、去符号化导致的主体性消解、separation式否定）
  - `时间化:s01-s04`（矩阵搭配中的时间化操作、时间化的先验范畴、主体彻底时间化/解脱路径、我思向世界存在的时间化）
  - `空间化:s01-s04`（矩阵搭配中的空间化操作、时间空间化/非时间化凝固、最低限度空间化的时间/天道、去空间化/化掉空间化时间）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 148 draft senses / 34 terms；row 139 四基本运动多义项簇已成形。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B14-2026-06-08` → records=12, terms=3, quotes=27, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=148, terms=34, quotes=348, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 15 mechanism-term expansion (`对象化` / `符号化` / `现象化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 148 更新为 160 records，terms 从 34 更新为 37。
- 新增 12 条 draft senses：
  - `对象化:s01-s04`（生命外化异己力量为对象性客体、意向性相关项/noema对象化、本质直观的想象性对象化、学习/研究中的自我对象化）
  - `符号化:s01-s04`（fabrication编织出的符号化世界、原初实体之后的符号化、逻辑学中的动力/机制/成果三段、现实预先符号化）
  - `现象化:s01-s04`（物理秩序驱动的世界现象化、透明性中的去现象化显现、神性拒绝现象化、先验反思把现象化机制拿来看）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 160 draft senses / 37 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B15-2026-06-08` → records=12, terms=3, quotes=25, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=160, terms=37, quotes=373, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 16 mechanism-term expansion (`去符号化` / `去现象化` / `本体论化` / `去本体论化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 160 更新为 172 records，terms 从 37 更新为 41。
- 新增 12 条 draft senses：
  - `去符号化:s01-s03`（涅槃/主体性状态的去符号化、生存从符号系统中抽离、意向对象抽离符号学网络）
  - `去现象化:s01-s03`（透明性中的外部现象去现象化、高阶现象过程被剪成直觉、矩阵运动中的现象去主体化面）
  - `本体论化:s01-s03`（数学关系的最低限度本体论化、原初物质自我本体论化、现实/制度框架的本体论化）
  - `去本体论化:s01-s03`（主体化作为去本体论化、partiality 的破局力量、原初意志隐匿/去存在化）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 172 draft senses / 41 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B16-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=172, terms=41, quotes=397, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 17 mechanism-term expansion (`实体化` / `去实体化` / `表象化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 172 更新为 184 records，terms 从 41 更新为 44。
- 新增 12 条 draft senses：
  - `实体化:s01-s04`（否定性物质促成存在、先验观念论中的实体化阶段、怀特海 actual entity 机制、符号运动成为理念）
  - `去实体化:s01-s04`（矩阵运动中的去实体化、气的稀疏/施动方向、阳爻的轻虚退场力量、体验去实体化/表象不稳固）
  - `表象化:s01-s04`（物理学秩序的表象化、新知识与物理秩序的比较中介、数量关系在均质场中的表象化、存在裂隙的可见面）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 184 draft senses / 44 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B17-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=184, terms=44, quotes=421, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 18 mechanism-term expansion (`去表象化` / `二元化` / `历史化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 184 更新为 196 records，terms 从 44 更新为 47。
- 新增 12 条 draft senses：
  - `去表象化:s01-s04`（表象扰动反回本体、imaginary 的真挚体验/直觉、审查机制的后台撤回、见独中的体验转后台空转）
  - `二元化:s01-s04`（矩阵运动中的二元化、差异要求规则化为高/低、理解中的主客/局部整体二元化、二元能指的不可能性动力学）
  - `历史化:s01-s04`（历史的哲学化/辩证法化、自然哲学被 historicized、意识形态置入范式史、断裂史/否定辩证化）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 196 draft senses / 47 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B18-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=196, terms=47, quotes=445, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 19 mechanism-term expansion (`去历史化` / `中心化` / `去中心化` / `重新中心化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 196 更新为 208 records，terms 从 47 更新为 51。
- 新增 12 条 draft senses：
  - `去历史化:s01-s02`（见独无古今/去时间化、图像哲学的非生成特权）
  - `中心化:s01-s04`（偏离常态的中心生成、自我意识撤回成中心、生存论中介者过度中心化、单子网络中的中心服务器）
  - `去中心化:s01-s04`（主体他者化/复数化、卡夫卡式无头科层制、集合论本体论的平等主义、向人民负责的妥协）
  - `重新中心化:s01-s02`（分裂整合为目的论、见独觉醒后的再获中心）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 208 draft senses / 51 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B19-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=208, terms=51, quotes=469, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 20 structure/sign-term expansion (`符号学` / `结构主义` / `能指` / `所指`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 208 更新为 220 records，terms 从 51 更新为 55。
- 新增 12 条 draft senses：
  - `符号学:s01-s03`（非索绪尔语言学的广义场、反现象学的中介性批判、sign/意指关系的两面结构）
  - `结构主义:s01-s03`（代表运动而非代表人物、不同符号中的同一结构、共时性结构及意识根基取消）
  - `能指:s01-s03`（声音/字形的粗糙面、任意性与差异体系、优先性/漂浮无根）
  - `所指:s01-s03`（概念效果/缺失、由他者差异设定、能指所指短路/无限游戏）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 220 draft senses / 55 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B20-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=220, terms=55, quotes=493, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 21 core-term expansion (`差异` / `本质` / `存在`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 220 更新为 232 records，terms 从 55 更新为 58。
- 新增 12 条 draft senses：
  - `差异:s01-s04`（原初关系中的概念生成、先于高低指派的回溯条件、本质直观中的差异分类学、实践中的本体论差异）
  - `本质:s01-s04`（现象学本质直观的结构、主体经验构造出的 eidos、时态性中的主体姿态、与存在生生连接）
  - `存在:s01-s04`（无有/彼的本体化风险、此在整体与在世存在、存在与本质无优先性、entity/存在化成果）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 232 draft senses / 58 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B21-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=232, terms=58, quotes=517, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W3 Batch 22 transformation-term expansion (`哲学化` / `辩证法化` / `认识论化` / `目的论化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 232 更新为 244 records，terms 从 58 更新为 62。
- 新增 12 条 draft senses：
  - `哲学化:s01-s03`（历史的理论家重构、教条的哲学化/去公转化、守阵地的本体论化策略）
  - `辩证法化:s01-s03`（历史以辩证法方式重构、先验现象学的源头拯救、理论家引导历史必然性）
  - `认识论化:s01-s03`（先验本质主义丰富认识维度、原初运动可被体验化、本体论结构经解释变成认识）
  - `目的论化:s01-s03`（形而上学机制导向伦理学、缓和矛盾的伦理体系、有限经济学的有序算计）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 244 draft senses / 62 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B22-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=244, terms=62, quotes=541, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 23 reverse/institutional mechanism expansion (`去目的论化` / `本体化` / `去辩证化` / `教科书化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 244 更新为 256 records，terms 从 62 更新为 66。
- 新增 12 条 draft senses：
  - `去目的论化:s01-s03`（宇宙悲观主义的无目的化、时间性意识的空间化消散、分析性话语的去目的/去主人化）
  - `本体化:s01-s03`（认识论维度成为规则制定者、伦理行动被本体化、存在论/符号化阶段中的纯有把握）
  - `去辩证化:s01-s03`（理论家的辩证法化姿态、政策/宣传替代理论层阶、意义之海中的差异限缩）
  - `教科书化:s01-s03`（ML传统下的正统教科书运动、反题理论教育的正统化、自然辩证法的意识形态功能/谦抑行动）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 256 draft senses / 66 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B23-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=256, terms=66, quotes=565, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 24 love-economy/sacrifice mechanism expansion (`爱欲` / `力比多` / `享乐` / `献祭`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 256 更新为 268 records，terms 从 66 更新为 70。
- 新增 12 条 draft senses：
  - `爱欲:s01-s03`（始因/第一推动、符号禁忌维持的共同体秩序、主体性剩余的中心化材料）
  - `力比多:s01-s03`（目的论维度中的运行能量、爱欲经济学的调节/平衡力量、本体论奠基与 essence 构造）
  - `享乐:s01-s03`（可计数的资本主义数量池、符号学结构出的生命形态、审美/性化剩余的放任结构）
  - `献祭:s01-s03`（符号通向里世界的功能、偶像神圣性的现象层转移、巴塔耶普遍经济学中的解放）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 268 draft senses / 70 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B24-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=268, terms=70, quotes=589, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 25 science/system/positivization mechanism expansion (`科学化` / `体系化` / `实证化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 268 更新为 280 records，terms 从 70 更新为 73。
- 新增 12 条 draft senses：
  - `科学化:s01-s04`（纯宇宙秩序场、科学知识社会学的话语自建制、逻辑实证主义的目的论动员、科学/意识形态二分中的自我辩护）
  - `体系化:s01-s04`（逻各斯的自我一致符号系统、神圣背景秩序的整体铺设、不对称性的把握/失去体系性、实证主义者作为系统化普罗大众）
  - `实证化:s01-s04`（无无法成为积极存在、科学知识社会学的经验化循环、星丛激发知识命名、经验科学的封闭取向）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 280 draft senses / 73 terms。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B25-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=280, terms=73, quotes=613, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W3 Batch 26 phase-1 count-gate closure (`共同体` / `主体间性` / `生活世界` / `事件性` / `平等主义`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 280 更新为 300 records，terms 从 73 更新为 78；W3 第一期 ≥300 sense count gate 已达成。
- 新增 20 条 draft senses：
  - `共同体:s01-s04`（虚假历史主义中的共同体意志、科学话语生产机构、范式共同信仰与规范关系、梦境中的认同网络）
  - `主体间性:s01-s04`（生活世界的原初社会维度、认识起点与前反思机制、物神化机制支撑的语言/认同、梦境他者的同等真实体验）
  - `生活世界:s01-s04`（胡塞尔晚年转向的前科学场、主体间性/他者性的敞开维度、调和形而下/形而上的中介、日常语用学实践侧）
  - `事件性:s01-s04`（第一人称时间视域的过程性、持存的事件性存在、创造历史的政治活动性、数学本体论失败的主体缺口）
  - `平等主义:s01-s04`（优于等级制的本体论姿态、哥白尼式宇宙论观察平等、伽森狄的伦理追求与形而上学预设、相对语法主义的表面平等/保守主义）
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 300 draft senses / 78 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B26-2026-06-08` → records=20, terms=5, quotes=40, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=300, terms=78, quotes=653, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS。
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS。
  - `git diff --check` → PASS。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.


## 2026-06-08 — W5 Batch 2 relation expansion and schema-field backfill

- 回填 `knowledge/relations/relation-assets.jsonl` 中 W5-B1 的 `source_position`、`target_position`、`evidence_segment` 字段。
- 追加 W5-B2 14 条 draft relations；W5 从 12 更新为 26 records。
- 新增覆盖 relation types：`blocks-transition`、`misrecognizes-as`、`overcodes`、`evidences-claim`。
- 当前 12/12 relation types 已覆盖；11/12 types 有 ≥2 examples，`subjectivizes` 仍需第二例。
- 更新 route/tension/mediation/boundary/misrecognition cards，新增 `overcode-cards.md` 与 `evidence-claim-cards.md`。
- 更新 `knowledge/qa/w5-relation-audit.md`、`knowledge/STATE.md`、`ISMISM-MAINLINE-HANDOFF.md`。
- 新增 `knowledge/scripts/validate_w5_relation_assets.py`，用于校验 W5 relation JSONL、W4 position-card 存在性、W3 term-sense refs 与 W1 clean-text exact quote substrings。
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=26, quotes=34, types=12/12, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B2-2026-06-08` → records=14, quotes=22, errors=0, warnings=0。
  - final W5 gate remains pending: `--min-count 60 --require-type-min 2` fails as expected at 26/60 and `subjectivizes` count=1。
- status: all W5 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W5 Batch 3 mechanism relation expansion

- 追加 `knowledge/relations/relation-assets.jsonl`：新增 W5-B3 14 条 draft relations；W5 从 26 更新为 40 records。
- B3 focus：事件性缺口→主体化、实践/理论主体化回路、主体化/客体化震荡、生活世界/主体间性中介、科学化/体系化边界与误认、共同体超编码。
- `subjectivizes` 从 1 更新为 3 examples；当前 12/12 relation types 均有 ≥2 examples。
- 新增 `knowledge/relations/mechanism-cards.md`；更新 boundary/mediation/misrecognition/overcode/evidence-claim cards 与 relation prompts。
- 更新 `knowledge/qa/w5-relation-audit.md`、`knowledge/STATE.md`、`ISMISM-MAINLINE-HANDOFF.md`。
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=40, quotes=49, types=12/12, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B3-2026-06-08` → records=14, quotes=15, errors=0, warnings=0。
  - final W5 gate remains pending: `--min-count 60 --require-type-min 2` fails as expected only on count target (40/60)。
- status: all W5 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W5 Batch 4 relation expansion toward count gate

- 追加 `knowledge/relations/relation-assets.jsonl`：新增 W5-B4 10 条 draft relations；W5 从 40 更新为 50 records。
- B4 focus：理论/实践路线、哲学化→辩证法化、教科书化阻断、符号经济张力、4-3-1 实践对象化。
- 更新 mechanism/boundary/mediation/route/tension/overcode cards 与 relation prompts。
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B4-2026-06-08` → records=10, quotes=11, errors=0, warnings=0。
- status: all W5 records remain `draft`; no canonical promotion; Atlas not used as evidence.

## 2026-06-08 — W5 Batch 5 quantitative gate closure

- 追加 `knowledge/relations/relation-assets.jsonl`：新增 W5-B5 10 条 draft relations；W5 从 50 更新为 60 records。
- B5 focus：历史/人民/理论中介、主体间性语言、闭合失败路线、命名 claim、语言游戏工具化、科学共同体科学化、体系化普罗大众候选位置。
- 更新 `knowledge/qa/w5-relation-audit.md`、`knowledge/STATE.md`、`ISMISM-MAINLINE-HANDOFF.md`。
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B5-2026-06-08` → records=10, quotes=10, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` → PASS。
- status: W5 quantitative gate reached; all W5 records remain `draft`; W6 audit still required before any promotion; Atlas not used as evidence.

## 2026-06-09 — W3 Batch 27 final-W3 expansion (`学习` / `研究` / `现实` / `通俗化` / `交谈` / `灌输` / `宣传` / `行动` / `信仰` / `忠诚` / `范式` / `知识`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 300 更新为 324 records，terms 从 78 更新为 90。
- 新增 24 条 draft senses，集中在 4-1-2/4-1-2-1 操作性术语、row 11 科学革命论范式/知识、row 263 事件主义信仰/忠诚。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 324 draft senses / 90 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B27-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=324, terms=90, quotes=701, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 28 final-W3 expansion (`科学史` / `历史主义` / `危机` / `常态范式` / `范式革命` / `共同信仰` / `方法论` / `知识论` / `学科矩阵` / `范例` / `不可通约性` / `基础主义`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 324 更新为 348 records，terms 从 90 更新为 102。
- 新增 24 条 draft senses，围绕 row 11 科学革命论拆分库恩范式、科学史、历史主义/基础主义、学科矩阵与范例等术语。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 348 draft senses / 102 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B28-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=348, terms=102, quotes=749, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 29 final-W3 expansion (`书写` / `小册子` / `见微知著` / `观察` / `分析` / `反刍` / `现实理论化` / `理论现实化` / `理论劳动` / `自圆其说` / `可行性` / `严肃`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 348 更新为 372 records，terms 从 102 更新为 114。
- 新增 24 条 draft senses，围绕 row 285 学习/研究拆分书写传播、现实研究、现实理论化/理论现实化、行动判断等操作性术语。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 372 draft senses / 114 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B29-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence.
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=372, terms=114, quotes=797, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 30 final-W3 expansion (`数据` / `报告` / `细节` / `突发状况` / `情绪感受` / `合理化` / `运动化` / `规律` / `回溯` / `政治经济关系` / `权力关系` / `心理状态`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 372 更新为 396 records，terms 从 114 更新为 126。
- 新增 24 条 draft senses，围绕 row 285 学习/研究继续拆分现实来源、细节/突发状况、合理化/运动化、规律/回溯，以及政治经济关系/权力关系/心理状态等还原层。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 396 draft senses / 126 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B30-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence。
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=396, terms=126, quotes=845, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 31 final-W3 expansion (`回溯性逻辑` / `守阵地` / `剩余` / `site` / `position` / `state` / `版本更新` / `真理事件` / `主体性` / `主体化过程` / `空位置` / `数学化`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 396 更新为 420 records，terms 从 126 更新为 138。
- 新增 24 条 draft senses，围绕 row 263 静止的事件主义拆分回溯性逻辑、守阵地、剩余/site/position/state、版本更新、真理事件、主体性/主体化过程、空位置与数学化。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 420 draft senses / 138 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B31-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence。
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=420, terms=138, quotes=893, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 32 final-W3 expansion (`Being` / `Event` / `space` / `点位` / `立场` / `数学知识` / `本体论知识` / `减法` / `矛盾张力` / `知识框架` / `数据交换中介` / `整体降临`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 420 更新为 444 records，terms 从 138 更新为 150。
- 新增 24 条 draft senses，围绕 row 263 继续拆分 Being/Event/space、点位/立场、减法/数学知识/本体论知识、矛盾张力、知识框架、数据交换中介与整体降临。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 444 draft senses / 150 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B32-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence。
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=444, terms=150, quotes=941, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 33 final-W3 expansion (`星丛` / `名称` / `命名活动` / `语用实践场` / `不可消解之物` / `反体系` / `同一性原理` / `内在张力` / `语音` / `离散符号系统` / `无调性` / `具体普遍性`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 444 更新为 468 records，terms 从 150 更新为 162。
- 新增 24 条 draft senses，围绕 row 229 否定辩证法拆分星丛、命名/名称、语用实践场、不可消解之物、反体系/同一性原理、内在张力/语音、离散符号系统/无调性与具体普遍性。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 468 draft senses / 162 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B33-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence。
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=468, terms=162, quotes=989, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 34 final-W3 expansion (`星座` / `名字` / `断裂的符号化` / `主客体` / `表征主义` / `先验语音论` / `声音` / `音乐` / `勋伯格` / `伪连续` / `局部断裂` / `总体连续` / `调性` / `难听` / `底层符号` / `被压抑` / `前符号化` / `不可还原性` / `不透明性` / `客体化运动`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 468 更新为 508 records，terms 从 162 更新为 182。
- 新增 40 条 draft senses，围绕 row 229 否定辩证法继续拆分星座/名字、主客体/表征主义、先验语音论/声音/音乐/勋伯格、伪连续/局部断裂/总体连续/调性/难听、底层符号/被压抑、前符号化/不可还原性/不透明性/客体化运动等术语。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 508 draft senses / 182 terms；W3 sense floor ≥500 reached；final ≥200 terms still pending。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B34-2026-06-09` → records=40, terms=20, quotes=80, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence。
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=508, terms=182, quotes=1069, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W3 Batch 35 final quantitative floor closure (`本体论更新` / `高级学术话语` / `数学话语` / `数理逻辑` / `拓扑学` / `数论` / `离散数学` / `最小二乘法` / `超定` / `函数拟合` / `符号学工具` / `几何学配型` / `集合容器` / `不可数的多` / `真理显现方式` / `politics` / `amor` / `艺术`)

- 追加 `knowledge/lexicon/term-senses.jsonl`：W3 从 508 更新为 544 records，terms 从 182 更新为 200。
- 新增 36 条 draft senses，围绕 row 263 静止事件主义拆分数学话语、本体论更新、数学/符号学工具、空间几何配型、不可数多与真理显现方式。
- 更新 `knowledge/lexicon/core-terms.md`、`knowledge/lexicon/ambiguous-terms.md`、`knowledge/qa/w3-lexicon-audit.md`。
- 更新 `knowledge/STATE.md` 与 `ISMISM-MAINLINE-HANDOFF.md`：当前 W3 进度 544 draft senses / 200 terms；MASTER-SPEC W3 quantitative floors reached；W6 audit before canonical promotion。
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B35-2026-06-09` → records=36, terms=18, quotes=72, errors=0, warnings=0。
- status: all W3 records remain `draft`; no canonical promotion; Atlas not used as evidence。
- final validation after docs update:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - `git diff --check` → PASS。
  - forbidden-language scan over active knowledge surfaces → PASS。

## 2026-06-09 — W6 audit reports completed

- Created W6 audit reports:
  - `knowledge/qa/validation-report.md`
  - `knowledge/qa/concept-drift-report.md`
  - `knowledge/qa/evidence-claim-audit.md`
  - `knowledge/qa/rejected-interpretations.md`
- Audit coverage:
  - sense mixing: 30 deterministic W3 samples + high-risk multi-sense groups; PASS
  - relation strength: 20 deterministic W5 samples + type/count gate; PASS
  - evidence-chain integrity: W3/W4/W5 validators and 10 W3 quote traces; PASS
  - forbidden interpretations: active-surface scan + Atlas/legacy boundary review; PASS
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - forbidden-language scan over active knowledge surfaces including W6 reports → PASS。
- status: W6 audit complete; no blocking issue; no confidence downgrade; W3/W5 remain `draft`; no canonical promotion; next W7 syntheses.

## 2026-06-09 — W7 synthesis layer completed

- Created 6 required W7 draft syntheses:
  - `knowledge/syntheses/part-1-realism.md`
  - `knowledge/syntheses/part-2-metaphysics.md`
  - `knowledge/syntheses/part-3-idealism.md`
  - `knowledge/syntheses/part-4-praxis.md`
  - `knowledge/syntheses/whole-system-map.md`
  - `knowledge/syntheses/methodological-core.md`
- Validation:
  - custom W7 tag check → PASS (all referenced W3 term IDs and W5 relation IDs exist; substantive bullet claims source-tagged)。
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0。
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172。
  - forbidden-language scan over active knowledge surfaces including W6/W7 files → PASS。
- status: W7 complete; W8 usage protocol pending; W3/W5 remain `draft`; no canonical promotion.

## 2026-06-09 — W8 usage protocol completed

- Created W8 protocol files:
  - `knowledge/usage-protocol.md`
  - `knowledge/query-playbook.md`
  - `knowledge/export-manifest.md`
- Validation:
  - forbidden-language scan over W8 files → PASS。
  - `git diff --check` → PASS。
- status: W8 complete; W9 optional lightweight integration index or final completion audit pending.

## 2026-06-09 — W9 repo-local lightweight integration index prepared

- Created repo-local W9 file:
  - `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
- Intended external target recorded but not written:
  - `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- Boundary reason: MASTER-SPEC/AGENTS hard boundary prohibits writing outside `/home/weathour/文档/ismism-system`.
- status: W9-ready inside repo; external copy requires explicit human action or future permission change; final completion audit pending.

## 2026-06-09 — MASTER-SPEC final completion audit

- Created `knowledge/qa/master-spec-completion-audit.md`.
- Final validation observed:
  - W3 → records=544, terms=200, quotes=1141, errors=0, warnings=0。
  - W5 → records=60, quotes=70, types=12/12, errors=0, warnings=0。
  - W4 → PASS at 4/16/64/172。
  - W7 tag check → PASS。
  - W6 reports → 4/4 present。
  - W7 syntheses → 6/6 present。
  - W8 docs → 3/3 present。
  - W9 repo-local index → present。
  - forbidden-language scan over active knowledge surfaces → PASS。
- Verdict: in-repo deliverables complete through W8 plus W9-ready index; external W9 target not written because current rules forbid writing outside repository. Persistent goal remains active unless user deems repo-local W9 sufficient or authorizes the external target in a later turn.

## 2026-06-09 — MASTER-SPEC repo-local final validator added

- Added `knowledge/scripts/validate_master_spec_outputs.py` for repo-local final gate validation.
- Validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → status=PASS, w3=544/200, w5=60, w6_reports=4/4, w7=6/6, w8=3/3, w9_repo_local=True, errors=0。
- Updated final audit/state/handoff with the reusable validator command.
- External W9 target remains intentionally outside the repo-local validator unless `--require-external-w9` is used after explicit authorization.

## 2026-06-09 — W9 manual copy instructions added

- Added `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md` with human/future-authorized copy and verification commands for the external W9 target.
- No outside-repo write was performed.
- `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → PASS.

## 2026-06-09 — STATE resume block refreshed after final validation

- Updated `knowledge/STATE.md` Open Decisions / Next Action / Handoff Block to remove stale W3/W5-forward language from the active resume surface.
- Current resume stance now records: W1–W8 repo-local completion, W9 repo-local package present, external W9 target unresolved due hard boundary.
- Validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → PASS.
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0.
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` → records=60, quotes=70, types=12/12, errors=0, warnings=0.
  - W4 L1/L2/L3/L4 validators → PASS at 4/16/64/172.
  - `git diff --check` → PASS.
  - forbidden-language scan over active knowledge surfaces → PASS.

## 2026-06-09 — MASTER-SPEC traceability matrix and enhanced final validator

- Added `knowledge/qa/master-spec-requirement-traceability.md`, a requirement-by-requirement traceability matrix covering boundary rules, W3/W4/W5/W6/W7/W8/W9 gates, evidence files, and current verdicts.
- Enhanced `knowledge/scripts/validate_master_spec_outputs.py` to check:
  - W4 count total and per-level counts (`4/16/64/172`, total `256`), required card sections, draft status, collected-term markers, and index coverage.
  - W3 quote-count, axis, `forbidden_mix`, draft status, and ambiguity-surface presence.
  - W5 full required type set, per-type minimum examples, evidence segment fields, boundary fields, and draft status.
  - W8 query-playbook path count (`>=10`).
  - presence of both final audit and traceability matrix.
- Updated `knowledge/qa/master-spec-completion-audit.md`, `knowledge/STATE.md`, and `ISMISM-MAINLINE-HANDOFF.md` to reference the traceability matrix and enhanced validator output.
- Validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, errors=0.
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0.
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` → records=60, quotes=70, types=12/12, errors=0, warnings=0.
  - W4 L1/L2/L3/L4 validators → PASS at 4/16/64/172.
  - `git diff --check` → PASS.
  - forbidden-language scan over active knowledge surfaces → PASS.
- Status unchanged: repo-local completion is proven; external W9 target remains unresolved under the current hard boundary.

## 2026-06-09 — External W9 target read-only status clarified

- Per completion-audit discipline, performed a read-only check of `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`.
- Finding: the external path exists, but it is an older placeholder and differs from the repo-local W9 protocol at `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`.
- No outside-repo write or update was performed.
- Enhanced `knowledge/scripts/validate_master_spec_outputs.py --require-external-w9` so that a mandatory external W9 check requires the external file to match the repo-local W9 protocol, not merely exist.
- Updated STATE, handoff, final audit, traceability matrix, and copy instructions to distinguish repo-local PASS from cross-repo W9 mismatch.
- Status: default repo-local validation remains PASS; `--require-external-w9` correctly fails until a human/future-authorized run replaces the older external file.

## 2026-06-09 — W9 external mismatch audit artifact added

- Added `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`.
- The audit records read-only W9 file sizes and SHA-256 hashes:
  - repo-local protocol: `383247be4a31c38451c38d86bfa211a5a485ea45ceb0311d2e3df6de1de4b3da` / 3698 bytes.
  - external target: `482d920c0cc737ff9f4671b4a32e2286aa8c070807a2836e49e273e29196acf1` / 2546 bytes.
- Updated copy instructions, final audit, traceability matrix, STATE, and handoff to reference the new audit artifact.
- Enhanced final validator output to report `w9_external_audit=True`.
- Validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, errors=0.
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9` → expected FAIL because the external target differs from the repo-local protocol.
  - W3/W4/W5 validators → PASS.
  - `git diff --check` → PASS.
  - forbidden-language scan over active knowledge surfaces → PASS.
- Status unchanged: repo-local MASTER-SPEC completion is proven; cross-repository W9 remains unresolved until authorized replacement or maintainer acceptance of repo-local W9.

## 2026-06-09 — W9 read-only status checker added

- Added `knowledge/scripts/check_w9_external_status.py`, a read-only checker comparing the repo-local W9 protocol with the intended psychoanalytic-writing-lab target.
- The checker supports:
  - `python3 knowledge/scripts/check_w9_external_status.py --repo .` for current status.
  - `python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match` for a cross-repository W9 gate.
- Updated W9 audit/copy instructions, final audit, traceability matrix, STATE, handoff, and final validator metadata to reference the checker.
- Current read-only result: `status=MISMATCH`, repo-local SHA-256 `383247be4a31c38451c38d86bfa211a5a485ea45ceb0311d2e3df6de1de4b3da`, external SHA-256 `482d920c0cc737ff9f4671b4a32e2286aa8c070807a2836e49e273e29196acf1`.
- Validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, w9_status_script=True, errors=0.
  - W3/W4/W5 validators → PASS.
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9` → expected FAIL because external target differs.
  - `git diff --check` → PASS.
  - forbidden-language scan over active knowledge surfaces → PASS.
- Status unchanged: repo-local completion remains proven; cross-repository W9 remains unresolved until maintainer acceptance of repo-local W9 or explicit external replacement.

## 2026-06-09 — W9 maintainer decision record added

- Added `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md` to make the final W9 boundary conflict explicit and decision-ready.
- The decision record gives three resolution options:
  - accept repo-local W9 as sufficient for `ismism-system`;
  - explicitly authorize replacement of the one external W9 file;
  - leave W9 unresolved.
- Enhanced `knowledge/scripts/validate_master_spec_outputs.py` to require the decision record as part of repo-local final audit metadata.
- Updated final audit, traceability matrix, STATE, and handoff references.
- Validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, w9_status_script=True, w9_decision_record=True, errors=0.
  - `python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match` → expected FAIL because the external target differs from the repo-local protocol.
- Status: all meaningful repo-local completion/audit/resolution artifacts are now present. The only remaining path to full cross-repository W9 completion is maintainer acceptance or explicit authorization to update the external target.

## 2026-06-10 — W9 repo-local sufficiency accepted

- User/maintainer selected Option A: repo-local W9 package under `knowledge/integration/psychoanalytic-writing-lab/` satisfies W9 for this repository.
- Updated decision/audit/resume surfaces:
  - `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
  - `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`
  - `knowledge/qa/master-spec-completion-audit.md`
  - `knowledge/qa/master-spec-requirement-traceability.md`
  - `knowledge/STATE.md`
  - `ISMISM-MAINLINE-HANDOFF.md`
- No outside-repo write was performed. The external target mismatch remains documented as a downstream/manual integration issue, not a completion blocker for `ismism-system`.


## 2026-06-12 — Wrong-route cleanup pass

- Removed legacy frontend/product route surfaces: `src/`, `dist/`, `index.html`, `package.json`, `package-lock.json`, `vite.config.*`, `tsconfig*`, `node_modules/`, and old `docs/00-*` through `docs/16-*`.
- Removed old clean-corpus compatibility pointer and obsolete archive snapshots: `ISMISM-CLEANUP-HANDOFF.md`, `docs/archive/legacy-cleanup-handoff-2026-04-17.md`, and `docs/archive/legacy-readme-frontend-prototype-2026-04-21.md`.
- Removed rebuildable/cache/experiment leftovers: `graphify-out/`, `compress_test/`, `__pycache__/`, three `split_md_clean/**/*_compressed.md` files, and one malformed empty quoted directory under `split_md_clean/`.
- Retained `Zhuyi_Matrix_Engine/` as legacy candidate/method auxiliary layer; retained `split_pdf/` as regenerable derived layer; retained root PDF/TOC/split evidence layers and `knowledge/` active layer.
- Updated `README.md`, `ISMISM-MAINLINE-HANDOFF.md`, `knowledge/STATE.md`, and `docs/archive/legacy-process-and-prototype-index.md` to make the deletion boundary explicit.
- Validator follow-up: updated `knowledge/scripts/validate_w1_manifests.py` so W1 corpus validation checks current post-recovery W1 facts and no longer fails merely because W2 segment cards now exist. Validation after cleanup: master/W1/W3/W4/W5 validators PASS; `git diff --check` PASS.

## 2026-06-14 — Directory map and repo-local operator skill draft added

- Added `DIRECTORY_MAP.md` as a concise current map of repository directories, functional layers, source priority, standard query paths, validators, and non-mainline boundaries.
- Added repo-local thin skill draft `skills/ismism-knowledge-operator/SKILL.md` plus `agents/openai.yaml`.
- The skill draft is procedural only: it points future agents to repository truth sources and does not duplicate `knowledge/` content.
- Updated `README.md`, `AGENTS.md`, and `knowledge/README.md` to reference the new navigation surfaces.

## 2026-06-15 — Lightweight read-only query scripts added

- Added read-only query helpers:
  - `knowledge/scripts/ismism_query_lib.py`
  - `knowledge/scripts/query_term.py`
  - `knowledge/scripts/query_position.py`
  - `knowledge/scripts/query_relation.py`
  - `knowledge/scripts/trace_evidence.py`
- Added examples to `DIRECTORY_MAP.md`, `README.md`, `knowledge/README.md`, `knowledge/query-playbook.md`, and `skills/ismism-knowledge-operator/SKILL.md`.
- Smoke examples:
  - `python3 knowledge/scripts/query_term.py 主体 --limit 2`
  - `python3 knowledge/scripts/query_position.py 3-4-2`
  - `python3 knowledge/scripts/query_relation.py --type objectifies --limit 1`
  - `python3 knowledge/scripts/trace_evidence.py term:主体:s01`

## 2026-06-15 — W10 further absorption pilot batch added

- Added W10 as a pilot-draft, additive further-absorption layer for close reading after W1–W9 completion.
- Created `knowledge/w10-absorption/PLAN.md` and `knowledge/w10-absorption/index.md`.
- Added five pilot cards across all three W10 card types:
  - `knowledge/w10-absorption/argument-cards/w10-arg-0076-contemporary-naturalism.md`
  - `knowledge/w10-absorption/process-cards/w10-proc-0131-zhuangzi-eight-steps.md`
  - `knowledge/w10-absorption/case-cards/w10-case-0173-john-stuart-mill.md`
  - `knowledge/w10-absorption/case-cards/w10-case-0258-early-lacan-metaphoric-symbolism.md`
  - `knowledge/w10-absorption/process-cards/w10-proc-0363-ai-regeneration.md`
- Added W10 templates and validator:
  - `knowledge/templates/w10-argument-card-template.md`
  - `knowledge/templates/w10-process-card-template.md`
  - `knowledge/templates/w10-case-card-template.md`
  - `knowledge/scripts/validate_w10_absorption.py`
- Added `knowledge/qa/w10-pilot-audit.md` with validation and adversarial fixture evidence.
- Added `knowledge/qa/w10-w3-w5-gap-followups.md` so `w3_w5_gap_review: followup_needed` rows feed back into future W3/W5 review instead of bypassing upstream extraction.
- Updated navigation/resume surfaces: `AGENTS.md`, `README.md`, `DIRECTORY_MAP.md`, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, and `skills/ismism-knowledge-operator/SKILL.md`.
- Validation:
  - `python3 -m py_compile knowledge/scripts/validate_w10_absorption.py`, `ruff check`, and `pyright` → PASS.
  - `python3 knowledge/scripts/validate_w10_absorption.py --repo .` → PASS, 5 cards, type counts argument=1/process=2/case=2, errors=0.
  - Temporary malformed-card adversarial check via `--extra-card` → expected FAIL; fixture removed.
  - Temporary rogue W10 markdown under `knowledge/w10-absorption/rogue.*` → expected FAIL; fixture removed.
  - Temporary stale `index.md` row outside the Pilot cards table → expected FAIL; index restored.
  - Temporary broken `index.md` href target → expected FAIL; index restored.
  - Temporary malformed Pilot cards table row → expected FAIL; index restored.
  - Temporary missing body `[q5]` reference in Lacan card → expected FAIL; card restored.
  - Temporary non-integer `row_id` in row 76 card → expected FAIL without traceback; card restored.
  - UltraQA report added: `knowledge/qa/w10-ultraqa-report.md`.
  - Existing master/W1/W3/W4/W5 validators → PASS.
  - `git diff --check` → PASS.
  - `git diff --name-only -- split_md split_md_clean knowledge/lexicon knowledge/relations` → empty; no protected-layer rewrite.
- Status: W10 is pilot-draft only; W1–W9 repo-local completion remains accepted; W3/W5 remain draft; validator now rejects unknown W10 markdown, stale/malformed index rows, broken index hrefs, missing body quote refs, and invalid `w3_w5_gap_review`.

## 2026-06-15 — Absorption strength distribution documented

- Added `knowledge/qa/absorption-strength-distribution.md` as the handoff snapshot for row-level absorption strength after W10 pilot batch 1.
- Current distribution: W1/W2-only = 220 rows / 60.6%; W1/W2+W3 = 109 rows / 30.0%; W1/W2+W3+W5 = 28 rows / 7.7%; W10 pilot covers 5 rows.
- Clean-text volume with any W3/W5/W10 deep absorption: 44.0%; W1/W2-only clean-text volume: 56.0%.
- Updated `ISMISM-MAINLINE-HANDOFF.md`, `knowledge/STATE.md`, `knowledge/README.md`, `README.md`, and `DIRECTORY_MAP.md` so future agents can resume from the distribution rather than infer it ad hoc.
- Next W10 backlog recommendation: high-text W1/W2-only rows 85, 133, 107, 174, 124, 65, 159, 87, 342, and 255.

## 2026-06-15 — AI Theme Maximum Absorption Program completed

- Added `knowledge/themes/ai/` as a pilot-draft AI / VR / 智能 / 算法 / 机器人 maximum absorption layer.
- Created:
  - `knowledge/themes/ai/ai-row-manifest.jsonl` — 60 candidate rows with row/segment/toc/path metadata, controlled `theme_class`, `core_status`, `recommended_action`, and absorption state.
  - `knowledge/themes/ai/ai-evidence-bank.jsonl` — 208 exact-substring clean-text quotes.
  - `knowledge/themes/ai/ai-taxonomy.md` and `knowledge/themes/ai/ai-synthesis.md` — evidence-linked AI taxonomy and synthesis.
  - `knowledge/themes/ai/README.md` and `knowledge/themes/ai/ai-w3-w5-batch-notes.md` — usage and batch notes.
- Appended AI W3 draft batch `W3-AI-2026-06-15`: 37 draft term senses; all quotes exact-substring validated.
- Appended AI W5 draft batch `W5-AI-2026-06-15`: 30 draft relation assets; all quotes exact-substring validated and relation types remain controlled.
- Expanded W10 from 5 to 32 pilot-draft cards by adding AI cards for rows 13–18 and 342–362, while preserving existing row 363 `w10:proc:0363:ai-regeneration`.
- Added validators/helpers:
  - `knowledge/scripts/validate_ai_theme.py`
  - `knowledge/scripts/query_ai_theme.py`
- Added QA/audit surfaces:
  - `knowledge/qa/ai-theme-absorption-audit.md`
  - `knowledge/qa/ai-theme-evidence-claim-audit.md`
  - `knowledge/qa/ai-theme-ultraqa-report.md`
- Updated navigation/resume surfaces: `README.md`, `knowledge/README.md`, `knowledge/query-playbook.md`, `DIRECTORY_MAP.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, and `skills/ismism-knowledge-operator/SKILL.md`.
- Boundary: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`; Atlas not used as truth; old frontend/product routes not restored.

## 2026-06-15 — Absorption strength distribution refreshed after AI theme absorption

- Updated `knowledge/qa/absorption-strength-distribution.md` from the old W10-pilot-only snapshot to the current post-AI-theme distribution.
- Current distribution: W1/W2-only = 198 rows / 54.5%; W1/W2+W3 = 104 rows / 28.7%; W1/W2+W3+W5 = 28 rows / 7.7%; W1/W2+W10-only = 11 rows / 3.0%; W1/W2+W3+W10 = 4 rows / 1.1%; W1/W2+W3+W5+W10 = 17 rows / 4.7%.
- Clean-text volume with any W3/W5/W10 deep absorption: 48.6%; W1/W2-only clean-text volume: 51.4%.
- W3 row coverage = 153; W5 row coverage = 46; W10 row coverage = 32; any W3/W5/W10 = 165 rows.
- First full-overlap rows now exist: rows 14, 15, 18, 349, 350, 351, 352, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363.
- Updated `README.md`, `knowledge/STATE.md`, and `ISMISM-MAINLINE-HANDOFF.md` summary numbers.

## 2026-06-15 — Chinese philosophy maximum absorption handoff drafted

- Added `knowledge/themes/chinese-philosophy/CHINESE-PHILOSOPHY-MAXIMUM-ABSORPTION-HANDOFF.md` as a planning handoff for a future Chinese Philosophy Maximum Absorption Program.
- Scope proposal: about 70 rows across Confucian/Neo-Confucian, Daoist/Warring States/Yijing, Buddhist/Chan bridge, Mao/Chinese Marxist practice, and broader revolutionary/dialectical context.
- Expected target scale: about 70 manifest rows, 200–300 quote-bank records, 50–70 W3 draft senses, 40–60 W5 draft relations, 35–45 W10 cards, three synthesis docs, validator/query helper, QA/audit/handoff updates.
- Boundary: this is a handoff/planning artifact only; no Chinese philosophy theme implementation has begun.

## 2026-06-15 — Chinese Philosophy Maximum Absorption Program implemented

- Added `knowledge/themes/chinese-philosophy/` maximum absorption layer over exact 70-row scope.
- Created 70-row manifest and 238 exact-substring quote-bank records.
- Appended W3 draft batch `W3-CHINESE-PHILOSOPHY-2026-06-15` with 60 senses.
- Appended W5 draft batch `W5-CHINESE-PHILOSOPHY-2026-06-15` with 50 relation assets.
- Added 45 W10 pilot-draft cards and regenerated W10 index.
- Added validator/query helper and QA/audit surfaces.
- Updated navigation/handoff files; final validation evidence is recorded in `.omx/tmp/final_*` files and `knowledge/qa/chinese-philosophy-ultraqa-report.md`.

## 2026-06-15 — Chinese Philosophy review repairs and UltraQA cycle 2 completed

- Repaired code-review findings from the Chinese Philosophy maximum absorption pass:
  - corrected stale W3 synthesis markers (`term:*:s02` where the Chinese batch coexists with earlier `s01` senses),
  - strengthened `validate_chinese_philosophy_theme.py --final` to resolve synthesis markers (`ev:chphil:*`, `term:*:sNN`, `rel:chphil:*`, `w10:*`, and `row N`),
  - strengthened `validate_w10_absorption.py` to reject duplicate W10 `evidence_quotes`,
  - replaced duplicated row 321/324 W10 evidence quotes with exact clean-text content quotes,
  - refreshed current handoff/navigation counts after Chinese absorption.
- Added negative-test evidence:
  - bad Chinese quote rejected: `.omx/tmp/validate_chinese_bad_quote_negative.txt`,
  - duplicate taxonomy row rejected: `.omx/tmp/validate_chinese_taxonomy_negative.txt`,
  - unresolved synthesis marker rejected: `.omx/tmp/validate_chinese_synthesis_marker_negative.txt`; all marker families rejected: `.omx/tmp/validate_chinese_all_synthesis_markers_negative.txt`,
  - duplicate W10 evidence quote rejected: `.omx/tmp/validate_w10_duplicate_quote_negative.txt`.
- Final validation evidence after restoration:
  - `python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final` → PASS, 70 manifest rows, 238 evidence records, 60 W3 Chinese records, 50 W5 Chinese records.
  - `python3 knowledge/scripts/validate_w10_absorption.py --repo .` → PASS, 77 cards.
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → PASS, W3=641/296, W5=140.
  - W3/W5 global + Chinese batch validators, AI theme validator, W4 L1–L4 validators, query smoke, `git diff --check`, and protected-corpus diff all PASS.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`.

## 2026-06-15 — Chinese Philosophy superseded planning handoff repaired

- Updated `knowledge/themes/chinese-philosophy/CHINESE-PHILOSOPHY-MAXIMUM-ABSORPTION-HANDOFF.md` from an active planning handoff into an explicit superseded/historical planning artifact.
- Added current completed counts and live entry points so it no longer contradicts the completed Chinese Philosophy layer.
- Reran final validation suite after the handoff repair: Chinese theme, W10, AI theme, master, W3/W5 global and Chinese batches, W4 L1–L4, query smoke, `git diff --check`, and protected-corpus diff all PASS; evidence refreshed under `.omx/tmp/final_*`.

## 2026-06-15 — Chinese Philosophy final code review cleared

- Final code-review cycle returned APPROVE / CLEAR after the superseded-handoff repair.
- Review confirmed coherent final counts, positive validation evidence, negative validator evidence, protected corpus boundary, and draft/pilot-draft status boundaries.
- Review artifact saved at `.omx/reviews/chinese-philosophy-code-review-cycle3.md`.

## 2026-06-15 — Stop-hook stale Autopilot state cleared

- Stop hook reported an active Autopilot `deep-interview` phase after the Chinese Philosophy run had already completed.
- Fresh state inspection found a duplicate stale session-scoped file at `/home/weathour/.omx-runs/run-20260615060505-5d6b/.omx/state/sessions/019eca71-597a-7941-9663-c922d8de0c24/autopilot-state.json` with `active=true/current_phase=deep-interview`.
- The completed session state remains preserved at session `omx-1781503505846-g137pl` with `active=false/current_phase=complete`.
- Cleared only the stale duplicate session via `omx state clear --input '{"mode":"autopilot","session_id":"019eca71-597a-7941-9663-c922d8de0c24"}' --json`.
- Reconfirmed `omx state list-active --json` returns no active modes.


## 2026-06-15 — Religion Problem Maximum Absorption Program implemented

- Added `knowledge/themes/religion/` maximum absorption layer over 80-row Religion Problem scope.
- Created 80-row manifest and 226 exact-substring quote-bank records.
- Appended W3 draft batch `W3-RELIGION-2026-06-15` with 64 senses.
- Appended W5 draft batch `W5-RELIGION-2026-06-15` with 51 relation assets.
- Added 45 W10 pilot-draft cards and regenerated W10 index (W10 total now 122 cards).
- Added `validate_religion_theme.py`, `query_religion_theme.py`, three syntheses, README, batch notes, completed handoff, and QA/audit surfaces.
- Updated navigation/state/handoff surfaces and absorption-strength distribution.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`; Atlas not used as truth.

## 2026-06-15 — Religion Problem final validation, negative tests, review, and UltraQA completed

- Final positive validation suite passed and is recorded at `.omx/tmp/religion_final_validation_suite.txt`.
- Required negative tests passed as expected and were restored:
  - bad quote rejected: `.omx/tmp/validate_religion_bad_quote_negative.txt`,
  - duplicate taxonomy row rejected: `.omx/tmp/validate_religion_taxonomy_negative.txt`,
  - unknown synthesis markers rejected: `.omx/tmp/validate_religion_synthesis_marker_negative.txt`,
  - duplicate W10 quote rejected: `.omx/tmp/validate_w10_religion_duplicate_quote_negative.txt`.
- Updated Religion audit files to final PASS/PASS-CLEAR: `knowledge/qa/religion-absorption-audit.md`, `knowledge/qa/religion-evidence-claim-audit.md`, `knowledge/qa/religion-ultraqa-report.md`.
- Independent native subagent review returned APPROVE/CLEAR; verifier returned PASS/CLEAR. Review artifact: `.omx/reviews/religion-code-review.md`.
- Reconfirmed protected corpus boundary: no `split_md/` or `split_md_clean/` diff.
- Mandatory Ultragoal ai-slop-cleaner pass completed as a no-op/inspection pass; report saved at `.omx/reviews/religion-ai-slop-cleaner-report.md`. No fallback-like slop found and no files changed by the cleanup pass.
- Final architect closure recheck returned CLEAR after G13 Ultragoal checkpoint and Autopilot state closure; `omx state list-active --json` returned no active modes.
- Stop-hook stale Autopilot duplicate cleared: session `019ecb57-3ac3-7222-82f6-77f509fc072a` had stale `active=true/current_phase=deep-interview`; current completed session `omx-1781503505846-g137pl` remains `active=false/current_phase=complete`. Fresh Religion validator, W10 validator, protected-corpus check, and Ultragoal 13/13 status passed before cleanup; `omx state list-active --json` returned no active modes after cleanup.

## 2026-06-15 — Time-Death-Finitude-Life Maximum Absorption Program implemented

- Added `knowledge/themes/time-death-finitude-life/` maximum absorption layer over 85 reviewed rows centered on death as the main axis.
- Created 85-row manifest and 289 exact-substring quote-bank records.
- Appended W3 draft batch `W3-TIME-DEATH-LIFE-2026-06-15` with 60 senses.
- Appended W5 draft batch `W5-TIME-DEATH-LIFE-2026-06-15` with 50 relation assets.
- Added 42 W10 pilot-draft Time-Death-Life cards and regenerated W10 index (W10 total now 164 cards).
- Added `validate_time_death_theme.py`, `query_time_death_theme.py`, three syntheses, README, batch notes, completed handoff, and QA/audit surfaces.
- Positive validation suite passed and is recorded at `.omx/tmp/time_death_positive_validation_suite.txt`.
- Required negative tests passed as expected and were restored: bad quote, duplicate taxonomy row, unknown synthesis marker, duplicate W10 quote.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`; Atlas not used as truth.

## 2026-06-15 — Time-Death-Finitude-Life final navigation/state repair

- batch_id: TIME-DEATH-FINITUDE-LIFE-MAX-2026-06-15
- action: repaired final architecture review blockers after initial implementation: root `README.md`, `AGENTS.md`, `skills/ismism-knowledge-operator/SKILL.md`, and current-state sections of `ISMISM-MAINLINE-HANDOFF.md` now include Time-Death-Finitude-Life counts/navigation and current W3/W5/W10 totals.
- validator hardening: `knowledge/scripts/validate_time_death_theme.py --final` now checks root README, AGENTS, repo-local skill draft, and rejects stale current-state markers such as old W5/W10 counts or old W5 min-count commands.
- negative test: `.omx/tmp/validate_time_death_stale_readme_negative.txt` confirms stale root README `--min-count 191` is rejected; restored positive validator PASS.
- boundary: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`.
## 2026-06-16 — Capitalism / Political Economy Maximum Absorption Program implemented

- Added `knowledge/themes/capitalism/` maximum absorption layer over 88 reviewed rows for 资本主义 / 政治经济 / 生产关系.
- Created 88-row manifest and 271 exact-substring quote-bank records.
- Appended W3 draft batch `W3-CAPITALISM-2026-06-16` with 63 senses.
- Appended W5 draft batch `W5-CAPITALISM-2026-06-16` with 51 relation assets.
- Added 45 W10 pilot-draft Capitalism cards and regenerated W10 index (W10 total now 209 cards).
- Added `validate_capitalism_theme.py`, `query_capitalism_theme.py`, four syntheses, README, batch notes, completed handoff, and QA/audit surfaces.
- Current global totals: 828 senses / 461 terms; 292 relations / 12 types; 209 cards / 3 card types.
- Absorption snapshot: 109/363 rows remain W1/W2-only; 73.9% clean-text volume has W3/W5/W10 absorption; 116 rows have W3+W5+W10 overlap.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`; Atlas not used as truth.

## 2026-06-16 CST — Universal Absorption Phase A completed

- Created `knowledge/qa/universal-absorption-phase-a-gap-map.jsonl` covering 109 baseline W1/W2-only rows and `knowledge/qa/universal-absorption-phase-a-plan.md`.
- Created `knowledge/qa/universal-absorption-phase-a-evidence-bank.jsonl` with 180 exact-substring quotes across 60 target rows.
- Appended `W3-UNIVERSAL-A-2026-06-16`: 100 W3 draft term senses.
- Appended `W5-UNIVERSAL-A-2026-06-16`: 90 W5 draft relation assets.
- Added 60 Universal-A W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `knowledge/scripts/validate_universal_absorption_phase_a.py` and `knowledge/scripts/query_universal_absorption.py`.
- Added phase-level syntheses under `knowledge/syntheses/universal-absorption-phase-a-*.md`.
- Updated absorption distribution: W1/W2-only 109→49; any clean-text volume 73.9%→92.6%; full overlap 116→176 rows; Field 2 W1/W2-only 34→9; Field 3 W1/W2-only 31→11.
- Draft discipline preserved: W3/W5 `draft`, W10 `pilot-draft`; no `split_md/` or `split_md_clean/` edits.

## 2026-06-16 — Universal Absorption Phase A final review hardening

- Addressed independent code-review and architecture WATCH findings before final Ultragoal closure.
- Hardened `validate_universal_absorption_phase_a.py` nested JSONL type guards and reformatted `query_universal_absorption.py`; `ruff` and `pyright` pass.
- Added Universal-A validation to broad delivery checklists and updated W10 PLAN with the Universal-A 60-card expansion / 269-card total.
- Updated `validate_time_death_theme.py` so current global navigation markers are derived from ledgers and W10 cards instead of frozen Universal-A constants.
- Reran full final validation suite, negative tests, theme validators, W4 checks, query smoke, `git diff --check`, and protected-corpus diff check; all PASS.

## 2026-06-16 — Universal Absorption Phase A independent review closure

- Independent `code-reviewer` re-review returned APPROVE after Ruff/Pyright/type-guard fixes.
- Independent `architect` re-review returned CLEAR after W10 PLAN, broad validator checklist, and Time-Death dynamic-marker fixes.
- Durable evidence recorded in `knowledge/qa/universal-absorption-phase-a-code-review-report.md`.

## 2026-06-16 CST — Universal Absorption Phase B completed

- Created `knowledge/qa/universal-absorption-phase-b-gap-map.jsonl` covering 49 post-Phase-A W1/W2-only rows and `knowledge/qa/universal-absorption-phase-b-plan.md`.
- Created `knowledge/qa/universal-absorption-phase-b-evidence-bank.jsonl` with 117 exact-substring quotes across 39 target rows.
- Appended `W3-UNIVERSAL-B-2026-06-16`: 78 W3 draft term senses.
- Appended `W5-UNIVERSAL-B-2026-06-16`: 78 W5 draft relation assets.
- Added 39 Universal-B W10 pilot-draft cards and updated `knowledge/w10-absorption/index.md`.
- Added `knowledge/scripts/validate_universal_absorption_phase_b.py` and `knowledge/scripts/query_universal_absorption_b.py`.
- Added phase-level syntheses under `knowledge/syntheses/universal-absorption-phase-b-*.md`.
- Updated absorption distribution: W1/W2-only 49→10; any clean-text volume 92.6%→99.55%; full overlap 176→215 rows; Field 1 10→1; Field 2 9→0; Field 3 11→0; Field 4 12→2.
- Draft discipline preserved: W3/W5 `draft`, W10 `pilot-draft`; no `split_md/` or `split_md_clean/` edits.

## 2026-06-16 CST — Universal Absorption Phase B final review closure

- Independent `code-reviewer` re-review returned APPROVE after the Master-Spec report-token blocker was removed.
- Independent `architect` re-review returned CLEAR after current navigation/status surfaces were aligned to Phase B counts and W5 `--min-count 460`.
- Fresh validation evidence: `.omx/tmp/phase_b_final_closure_validation.txt` (`FINAL_CLOSURE_VALIDATION_PASS`), `.omx/tmp/phase_b_final_post_review_sweep.txt` (`FINAL_POST_REVIEW_SWEEP_PASS`), and `.omx/tmp/phase_b_nav_patch_validation.txt` (`NAV_PATCH_VALIDATION_PASS`).
- Durable review evidence recorded in `knowledge/qa/universal-absorption-phase-b-code-review-report.md`; handoff status updated to complete.

<!-- FEMINISM-THEME-START:OPLOG -->
## 2026-06-16 — Feminism / Gender / Sexuality / Social Reproduction maximum absorption

- Added `knowledge/themes/feminism/` with manifest (94), evidence bank (309), taxonomy, syntheses, W3/W5 notes, and handoff.
- Appended `W3-FEMINISM-2026-06-16` (78 draft senses) and `W5-FEMINISM-2026-06-16` (65 draft relations).
- Added `W10-FEMINISM-2026-06-16` (45 pilot-draft cards) and regenerated W10 index.
- Added `validate_feminism_theme.py` and `query_feminism_theme.py`; protected corpus unchanged.

- Final validation: `.omx/tmp/feminism_full_validation_final.log` PASS; W3=1084/712, W5=525, W10=353, full-overlap rows=229.
- Negative tests: `.omx/tmp/feminism_negative_tests.log` PASS, including corrupt quote, blank quote, W3/W5 non-draft, W10 broken quote, unknown synthesis marker, protected corpus mutation, and excluded-row promotion.
- Independent review: `knowledge/qa/feminism-code-review-report.md` records code-reviewer APPROVE and architect CLEAR.
- Navigation/state current markers aligned to `--min-count 525`; no stale current guidance markers remain.
<!-- FEMINISM-THEME-END:OPLOG -->
## 2026-06-16 — Psychoanalysis / Subjectivity / Desire / Discourse / Language maximum absorption

- Created `knowledge/themes/psychoanalysis-subjectivity/` with 120 reviewed rows and 387 exact quotes.
- Appended `W3-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16` (89 draft senses) and `W5-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16` (75 draft relations).
- Added 58 W10 pilot-draft cards and updated W10 index/plan.
- Updated state/navigation/distribution docs; W5 validator uses `--min-count 600`.

## 2026-06-16 — Aesthetics / Art / Media / Image / Narrative maximum absorption

- Created `knowledge/themes/aesthetics-media/` with 69 reviewed rows and 192 exact quotes as a film-analysis precursor layer.
- Appended `W3-AESTHETICS-MEDIA-2026-06-16` (53 draft senses) and `W5-AESTHETICS-MEDIA-2026-06-16` (44 draft relations).
- Added `W10-AESTHETICS-MEDIA-2026-06-16` (30 pilot-draft cards) and updated W10 index.
- Added `validate_aesthetics_media_theme.py` and `query_aesthetics_media_theme.py`.
- Updated current distribution: W3 rows 336, W5 rows 277, W10 rows 286, full W3+W5+W10 overlap 248 rows, W5 min-count 644.
- Validation: Aesthetics-Media, W3, W5, W10, Universal-A/B, AI, Chinese Philosophy, Religion, Time-Death, Capitalism, Feminism, Psychoanalysis, and master validator all PASS.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`; Atlas remains candidate-only.

## 2026-06-16 — Labor / Workplace / Precarity / Involution maximum absorption

- Created `knowledge/references/social-phenomena-diagnostic-protocol.md` as the shared protocol for reality/social-phenomenon absorption.
- Created `knowledge/themes/labor-workplace-precarity/` with 98 reviewed rows and 247 exact-normalizable quotes.
- Appended `W3-LABOR-WORKPLACE-PRECARITY-2026-06-16` (45 draft senses) and `W5-LABOR-WORKPLACE-PRECARITY-2026-06-16` (40 draft relations).
- Added 30 Labor W10 pilot-draft cards and rebuilt W10 index.
- Added Labor syntheses, handoff, validator, and query helper.
- Updated current counts: W3 1271/866; W5 684; W10 471; full W3+W5+W10 overlap 253 rows; W5 min-count 684.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`.

## 2026-06-16 — Education / Examination / Credentialism evidence package (G005)

- Created `knowledge/themes/education-examination-credentialism/` as the second Social Phenomena / Everyday Life Problems theme evidence package.
- Added `education-examination-credentialism-row-manifest.jsonl` with 109 reviewed rows: 66 core, 36 bridge, 7 excluded boundary rows.
- Added `education-examination-credentialism-evidence-bank.jsonl` with 281 exact-normalizable quotes.
- Added `education-examination-credentialism-taxonomy.md` and README scope/counts/interpretation rules.
- Validation: `/tmp/validate_education_g005.py` PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits.
- Boundary reaffirmed: G005 is evidence-only; W3/W5 remain for G006 and must stay `draft`; W10 remains `pilot-draft`.

## 2026-06-16 — Education / Examination / Credentialism W3/W5/W10 absorption (G006)

- Appended `W3-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16` (40 draft relations) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Education W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `education-examination-credentialism-w3-w5-batch-notes.md`; README updated with batch markers.
- Validation: W3 education batch PASS; W3 global PASS (1316 senses / 911 terms); W5 education batch PASS; W5 global PASS (724 relations); W10 PASS (501 cards); master validator PASS; `git diff --check` PASS; protected corpus unchanged.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits.

## 2026-06-16 — Education / Examination / Credentialism closure (G007)

- Added Education syntheses: `education-examination-credentialism-synthesis.md`, `credential-sorting-and-meritocracy-synthesis.md`, and `knowledge-discipline-and-expert-authority-synthesis.md`.
- Added `EDUCATION-EXAMINATION-CREDENTIALISM-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_education_examination_credentialism_theme.py` and `query_education_examination_credentialism_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Education closure: W3 1316/911; W5 724; W10 501; W5 rows 284; W10 rows 299; full W3+W5+W10 overlap 258 rows; W5 min-count 724.
- Validation: Education final, W3, W5, W10, Universal-A/B, AI, Chinese Philosophy, Religion, Time-Death, Capitalism, Feminism, Psychoanalysis, Aesthetics, Labor, master validator, `git diff --check`, and protected corpus check all PASS (`/tmp/ismism-g007-validation-rerun.log`).

## 2026-06-16 — Family / Intimacy / Marriage / Birth / Social Reproduction evidence package (G008)

- Created `knowledge/themes/family-intimacy-reproduction/` as the third Social Phenomena / Everyday Life Problems theme evidence package.
- Added `family-intimacy-reproduction-row-manifest.jsonl` with 86 reviewed rows: 39 core, 38 bridge, 9 excluded boundary rows.
- Added `family-intimacy-reproduction-evidence-bank.jsonl` with 240 exact-normalizable quotes.
- Added `family-intimacy-reproduction-taxonomy.md` and README scope/counts/interpretation rules.
- Boundary note: `彩礼` and `婚恋市场` remain downstream diagnostic scope markers, but the current corpus scan found no direct exact `彩礼` quote, so G008 makes no unsupported 彩礼-specific claim.
- Validation: `/tmp/validate_family_g008.py` PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits.
- Boundary reaffirmed: G008 is evidence-only; W3/W5 remain for G009 and must stay `draft`; W10 remains `pilot-draft`.

## 2026-06-16 — Family / Intimacy / Marriage / Birth / Social Reproduction W3/W5/W10 absorption (G009)

- Appended `W3-FAMILY-INTIMACY-REPRODUCTION-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-FAMILY-INTIMACY-REPRODUCTION-2026-06-16` (40 draft relations) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Family W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `family-intimacy-reproduction-w3-w5-batch-notes.md`; README updated with batch markers.
- Validation: W3 Family batch PASS; W3 global PASS (1361 senses / 952 terms); W5 Family batch PASS; W5 global PASS (764 relations / 12 relation types); W10 PASS (531 cards); `git diff --check` PASS; protected corpus unchanged.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no unsupported 彩礼-specific claim was introduced.

## 2026-06-16 — Family / Intimacy / Marriage / Birth / Social Reproduction closure (G010)

- Added Family syntheses: `family-intimacy-reproduction-synthesis.md`, `romance-ideology-and-intimacy-synthesis.md`, and `gendered-family-and-social-reproduction-synthesis.md`.
- Added `FAMILY-INTIMACY-REPRODUCTION-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_family_intimacy_reproduction_theme.py` and `query_family_intimacy_reproduction_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Family closure: W3 1361/952; W5 764; W10 531; W5 rows 285; W10 rows 299; full W3+W5+W10 overlap 259 rows; W5 min-count 764.
- Hardened older theme validators so Capitalism/Feminism append-only checks allow Family batches and Psychoanalysis/Labor/Education final checks accept the current Family checkpoint while preserving their theme-local assets.
- Validation: Family final/query, W3, W5, W10, Universal-A/B, AI, Chinese Philosophy, Religion, Time-Death, Capitalism, Feminism, Psychoanalysis, Aesthetics, Labor, Education, master validator, `git diff --check`, and protected corpus check all PASS (`/tmp/ismism-g010-validation.log`).
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no unsupported 彩礼-specific claim was introduced.

## 2026-06-16 — Consumption / Desire / Commodity / Lifestyle evidence package (G011)

- Created `knowledge/themes/consumption-desire-lifestyle/` as the fourth Social Phenomena / Everyday Life Problems theme evidence package.
- Added `consumption-desire-lifestyle-row-manifest.jsonl` with 93 reviewed rows: 38 core, 45 bridge, and 10 excluded boundary rows.
- Added `consumption-desire-lifestyle-evidence-bank.jsonl` with 223 exact-normalizable quotes.
- Added `consumption-desire-lifestyle-taxonomy.md` and README scope/counts/interpretation rules.
- Boundary note: `情绪消费`, `身份消费`, and `自我品牌化` remain downstream diagnostic scope markers even where the corpus uses adjacent exact words such as `情绪`, `身份`, `品牌`, `广告`, `营销`, and `生活方式`; G011 makes no unsupported current-events claim beyond row-level evidence.
- Validation: `/tmp/validate_consumption_g011.py` PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits.
- Boundary reaffirmed: G011 is evidence-only; W3/W5 remain for G012 and must stay `draft`; W10 remains `pilot-draft`.

## 2026-06-16 — Consumption / Desire / Commodity / Lifestyle W3/W5/W10 absorption (G012)

- Appended `W3-CONSUMPTION-DESIRE-LIFESTYLE-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-CONSUMPTION-DESIRE-LIFESTYLE-2026-06-16` (40 draft relations, covering all 12 relation types) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Consumption W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `consumption-desire-lifestyle-w3-w5-batch-notes.md`; README and taxonomy updated with G012 batch markers.
- Validation: G011/G012 Consumption temp validators PASS; W3 Consumption batch PASS; W3 global PASS (1406 senses / 990 terms); W5 Consumption batch PASS; W5 global PASS (804 relations / 12 relation types); W10 PASS (561 cards); master validator PASS; `git diff --check` PASS; protected corpus unchanged (`/tmp/ismism-g012-validation.log`).
- Current row coverage after G012: W3 rows 337; W5 rows 287; W10 rows 299; any W3/W5/W10 rows 355; full W3+W5+W10 overlap 260 rows.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits.

## 2026-06-16 — Consumption / Desire / Commodity / Lifestyle closure (G013)

- Added Consumption syntheses: `consumption-desire-lifestyle-synthesis.md`, `commodity-fetishism-and-market-enjoyment-synthesis.md`, and `emotional-identity-lifestyle-consumption-synthesis.md`.
- Added `CONSUMPTION-DESIRE-LIFESTYLE-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_consumption_desire_lifestyle_theme.py` and `query_consumption_desire_lifestyle_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Consumption closure: W3 1406/990; W5 804; W10 561; W3 rows 337; W5 rows 287; W10 rows 299; any W3/W5/W10 rows 355; W1/W2-only rows 8; full W3+W5+W10 overlap 260 rows; W5 min-count 804.
- Hardened older theme validators so append-only checks and current/global documentation checks accept the Consumption checkpoint while preserving theme-local evidence boundaries.
- Validation: Consumption final/query, W3, W5, W10, Universal-A/B, AI, Chinese Philosophy, Religion, Time-Death, Capitalism, Feminism, Psychoanalysis, Aesthetics, Labor, Education, Family, master validator, `git diff --check`, and protected corpus check all PASS (`/tmp/ismism-g013-validation.log`).
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; downstream diagnostic labels such as `情绪消费`, `身份消费`, and `自我品牌化` are retained only where row-level evidence or adjacent lexical evidence supports them.

## 2026-06-16 — Media / Platform / Public Opinion / Traffic Society evidence package (G014)

- Created `knowledge/themes/media-platform-public-opinion/` as the fifth Social Phenomena / Everyday Life Problems theme evidence package.
- Added `media-platform-public-opinion-row-manifest.jsonl` with 119 reviewed rows: 46 core, 63 bridge, and 10 excluded boundary rows.
- Added `media-platform-public-opinion-evidence-bank.jsonl` with 267 exact-normalizable quotes.
- Added `media-platform-public-opinion-taxonomy.md` and README scope/counts/interpretation rules.
- Boundary note: `热搜` and `饭圈` remain downstream diagnostic labels because the current corpus has no direct exact hits for those strings; G014 grounds the layer in exact adjacent evidence such as `平台`, `舆论`, `流量`, `短视频`, `直播`, `网红`, `粉丝`, `偶像`, `注意力`, `算法`, `数据`, `推荐`, `媒介`, `媒体`, `传媒`, `传播`, `公共话语`, and `犬儒`.
- Validation: `/tmp/validate_media_platform_g014.py` PASS; master validator PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits (`/tmp/ismism-g014-validation.log`).
- Boundary reaffirmed: G014 is evidence-only; W3/W5 remain for G015 and must stay `draft`; W10 remains `pilot-draft`; no current-events or external media-studies claim was introduced.

## 2026-06-16 — Media / Platform / Public Opinion / Traffic Society W3/W5/W10 absorption (G015)

- Appended `W3-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16` (40 draft relations, covering all 12 relation types) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Media-platform W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `media-platform-public-opinion-w3-w5-batch-notes.md`; README and taxonomy updated with G015 batch markers.
- Validation: G014/G015 Media-platform temp validators PASS; W3 Media-platform batch PASS; W3 global PASS (1451 senses / 1035 terms); W5 Media-platform batch PASS; W5 global PASS (844 relations / 12 relation types); W10 PASS (591 cards); master validator PASS; `git diff --check` PASS; protected corpus unchanged (`/tmp/ismism-g015-validation.log`).
- Current row coverage after G015: W3 rows 337; W5 rows 287; W10 rows 302; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 260 rows.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; exact `热搜`/`饭圈` remain unsupported as direct corpus claims.

## 2026-06-16 — Media / Platform / Public Opinion / Traffic Society closure (G016)

- Added Media-platform syntheses: `media-platform-public-opinion-synthesis.md`, `platform-traffic-attention-economy-synthesis.md`, and `public-opinion-fandom-network-cynicism-synthesis.md`.
- Added `MEDIA-PLATFORM-PUBLIC-OPINION-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_media_platform_public_opinion_theme.py` and `query_media_platform_public_opinion_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Media-platform closure: W3 1451/1035; W5 844; W10 591; W3 rows 337; W5 rows 287; W10 rows 302; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 260 rows; W5 min-count 844.
- Hardened older theme validators so append-only checks and current/global documentation checks accept the Media-platform checkpoint while preserving theme-local evidence boundaries.
- Validation: Media-platform final/query, W3, W5, W10, Universal-A/B, AI, Chinese Philosophy, Religion, Time-Death, Capitalism, Feminism, Psychoanalysis, Aesthetics, Labor, Education, Family, Consumption, master validator, `git diff --check`, and protected corpus check all PASS (`/tmp/ismism-g016-validation.log`).
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; exact `热搜` and `饭圈` remain downstream labels without direct exact corpus claims.

## 2026-06-16 — Governance / Law / Bureaucracy / Order evidence package (G017)

- Created `knowledge/themes/governance-law-bureaucracy/` as the sixth Social Phenomena / Everyday Life Problems theme evidence package.
- Added `governance-law-bureaucracy-row-manifest.jsonl` with 124 reviewed rows: 66 core, 48 bridge, and 10 excluded boundary rows.
- Added `governance-law-bureaucracy-evidence-bank.jsonl` with 307 exact-normalizable quotes.
- Added `governance-law-bureaucracy-taxonomy.md` and README scope/counts/interpretation rules.
- Boundary note: high-frequency `法`, `秩序`, `国家`, `政治`, and `规则` language is not enough; `规则拜物` and `治理技术` remain downstream diagnostic labels unless row-level exact quotes support rule/procedure/legal-form substitution or governance-control mechanisms.
- Validation: `/tmp/validate_governance_g017.py` PASS; master validator PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits (`/tmp/ismism-g017-validation.log`).
- Boundary reaffirmed: G017 is evidence-only; W3/W5 remain for G018 and must stay `draft`; W10 remains `pilot-draft`; no current-events, policy, or external jurisprudence claim was introduced.

## 2026-06-16 — Governance / Law / Bureaucracy / Order W3/W5/W10 absorption (G018)

- Appended `W3-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16` (40 draft relations, covering all 12 relation types) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Governance-law W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `governance-law-bureaucracy-w3-w5-batch-notes.md`; README and taxonomy updated with G018 batch markers.
- Validation: G017/G018 Governance-law temp validators PASS; W3 Governance-law batch PASS; W3 global PASS (1496 senses / 1076 terms); W5 Governance-law batch PASS; W5 global PASS (884 relations / 12 relation types); W10 PASS (621 cards); master validator PASS; `git diff --check` PASS; protected corpus unchanged (`/tmp/ismism-g018-validation.log`).
- Current row coverage after G018: W3 rows 343; W5 rows 292; W10 rows 305; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 268 rows.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no external law/policy/current-events claim was introduced.

## 2026-06-16 — Governance / Law / Bureaucracy / Order closure (G019)

- Added Governance-law syntheses: `governance-law-bureaucracy-synthesis.md`, `law-bureaucracy-rule-fetishism-synthesis.md`, and `discipline-risk-security-governance-synthesis.md`.
- Added `GOVERNANCE-LAW-BUREAUCRACY-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_governance_law_bureaucracy_theme.py` and `query_governance_law_bureaucracy_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Governance-law closure: W3 1496/1076; W5 884; W10 621; W3 rows 343; W5 rows 292; W10 rows 305; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 268 rows; W5 min-count 884.
- Hardened older theme validators so append-only checks and current/global documentation checks accept the Governance-law checkpoint while preserving theme-local evidence boundaries.
- Validation: Governance-law final/query, W3, W5, W10, Universal-A/B, AI, Chinese Philosophy, Religion, Time-Death, Capitalism, Feminism, Psychoanalysis, Aesthetics, Labor, Education, Family, Consumption, Media-platform, master validator, `git diff --check`, and protected corpus check all PASS (`/tmp/ismism-g019-validation.log`).
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no external law/policy/current-events claim was introduced.

## 2026-06-16 — Class / Youth / Generation / Mobility Anxiety evidence package (G020)

- Created `knowledge/themes/class-youth-generational-anxiety/` as the seventh Social Phenomena / Everyday Life Problems theme evidence package.
- Added `class-youth-generational-anxiety-row-manifest.jsonl` with 120 reviewed rows: 91 core, 8 bridge, and 21 excluded boundary rows.
- Added `class-youth-generational-anxiety-evidence-bank.jsonl` with 310 exact-normalizable quotes.
- Added `class-youth-generational-anxiety-taxonomy.md` and README scope/counts/interpretation rules.
- Boundary note: generic `阶级`, metaphysical `虚无`, logical `地位`, broad `上升`, and ontological `底层` language are not enough; downstream labels such as `上升通道`, `阶层固化`, `中产焦虑`, `底层羞辱`, `成功学`, and `青年虚无` require row-level or adjacent exact evidence.
- Validation: `/tmp/validate_class_youth_g020.py` PASS; master validator PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits (`/tmp/ismism-g020-validation.log`).
- Boundary reaffirmed: G020 is evidence-only; W3/W5 remain for G021 and must stay `draft`; W10 remains `pilot-draft`; no current-events, policy, or external sociology claim was introduced.

## 2026-06-16 — Class / Youth / Generation / Mobility Anxiety W3/W5/W10 absorption (G021)

- Appended `W3-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16` (40 draft relations, covering all 12 relation types) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Class-youth W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `class-youth-generational-anxiety-w3-w5-batch-notes.md`; README and taxonomy updated with G021 batch markers.
- Validation: G020/G021 Class-youth temp validators PASS; W3 Class-youth batch PASS; W3 global PASS (1541 senses / 1116 terms); W5 Class-youth batch PASS; W5 global PASS (924 relations / 12 relation types); W10 PASS (651 cards); master validator PASS; `git diff --check` PASS; protected corpus unchanged (`/tmp/ismism-g021-validation.log`).
- Current row coverage after G021: W3 rows 343; W5 rows 295; W10 rows 306; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 270 rows.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no external sociology/current-events claim was introduced.


## 2026-06-16 — Class / Youth / Generation / Mobility Anxiety closure (G022)

- Added Class-youth syntheses: `class-youth-generational-anxiety-synthesis.md`, `mobility-anxiety-class-solidification-synthesis.md`, and `youth-success-bottom-humiliation-synthesis.md`.
- Added `CLASS-YOUTH-GENERATIONAL-ANXIETY-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_class_youth_generational_anxiety_theme.py` and `query_class_youth_generational_anxiety_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Class-youth closure: W3 1541/1116; W5 924; W10 651; W3 rows 343; W5 rows 295; W10 rows 306; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 270 rows; W5 min-count 924.
- Hardened older theme validators so append-only checks and current/global documentation checks accept the Class-youth checkpoint while preserving theme-local evidence boundaries.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no external sociology/current-events claim was introduced.

## 2026-06-16 — Psychological Distress / Anxiety / Addiction / Social Symptom evidence package (G023)

- Created `knowledge/themes/psychological-distress-social-symptom/` as the eighth Social Phenomena / Everyday Life Problems theme evidence package.
- Added `psychological-distress-social-symptom-row-manifest.jsonl` with 120 reviewed rows: 100 core, 10 bridge, and 10 excluded boundary rows.
- Added `psychological-distress-social-symptom-evidence-bank.jsonl` with 340 exact-normalizable quotes.
- Added `psychological-distress-social-symptom-taxonomy.md` and README scope/counts/interpretation rules.
- Boundary note: generic `心理`, philosophical `心理主义`, neuroscientific `神经`, metaphysical `虚无`, or psychoanalytic `欲望` is not automatically evidence for lived psychological distress; downstream labels such as `躺平`, `内耗`, `心理咨询产业`, and `社会矛盾私人化` require row-level or adjacent exact evidence.
- Validation: `/tmp/validate_psychological_distress_g023.py` PASS; master validator PASS; `git diff --check` PASS; no `split_md/` or `split_md_clean/` edits (`/tmp/ismism-g023-validation.log`).
- Boundary reaffirmed: G023 is evidence-only; W3/W5 remain for G024 and must stay `draft`; W10 remains `pilot-draft`; no clinical, therapy-industry, psychiatric, or current-events claim was introduced.

## 2026-06-16 — Psychological Distress / Anxiety / Addiction / Social Symptom W3/W5/W10 absorption (G024)

- Appended `W3-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16` (45 draft senses) to `knowledge/lexicon/term-senses.jsonl`.
- Appended `W5-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16` (40 draft relations, covering all 12 relation types) to `knowledge/relations/relation-assets.jsonl`.
- Added 30 Psychological-distress W10 pilot-draft cards and rebuilt `knowledge/w10-absorption/index.md`.
- Added `psychological-distress-social-symptom-w3-w5-batch-notes.md`; README and taxonomy updated with G024 batch markers.
- Validation: G023/G024 Psychological-distress temp validators PASS; W3 Psychological-distress batch PASS; W3 global PASS (1586 senses / 1149 terms); W5 Psychological-distress batch PASS; W5 global PASS (964 relations / 12 relation types); W10 PASS (681 cards); master validator PASS; `git diff --check` PASS; protected corpus unchanged (`/tmp/ismism-g024-validation.log`).
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no clinical, therapy-industry, psychiatric, medication, or current-events claim was introduced.


## 2026-06-16 — Psychological Distress / Anxiety / Addiction / Social Symptom closure (G025)

- Added Psychological-distress syntheses: `psychological-distress-social-symptom-synthesis.md`, `anxiety-addiction-social-symptom-synthesis.md`, and `private-psychologization-and-trauma-synthesis.md`.
- Added `PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-MAXIMUM-ABSORPTION-HANDOFF.md`.
- Added `validate_psychological_distress_social_symptom_theme.py` and `query_psychological_distress_social_symptom_theme.py`.
- Updated README, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, query playbook, repo-local skill pointer, and absorption distribution current markers.
- Current counts after Psychological-distress closure: W3 1676/1228; W5 964; W10 681; W3 rows 343; W5 rows 297; W10 rows 308; any W3/W5/W10 rows 357; W1/W2-only rows 6; full W3+W5+W10 overlap 273 rows; W5 min-count 964.
- Hardened older theme validators so append-only checks and current/global documentation checks accept the Psychological-distress checkpoint while preserving theme-local evidence boundaries.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no clinical, therapy-industry, psychiatric, medication, or current-events mental-health claim was introduced.

## 2026-06-16 — G028 Urban / Housing / Migration / Space closed

Closed Urban-housing theme with manifest/evidence, W3/W5/W10 absorption, syntheses, query helper, final validator, and navigation updates. Current markers: W3 1676/1228; W5 1004; W10 711; full overlap 275.

## 2026-06-16 — G031 Health / Body / Medicine / Risk Society closed

Closed Health-body theme with manifest/evidence, W3/W5/W10 absorption, syntheses, query helper, final validator, and navigation updates. Current markers: W3 1676/1228; W5 1044; W10 741; full overlap 277.

## 2026-06-16 — Social Phenomena Phase 1 everyday life reproduction synthesis (G032)

- Added `knowledge/syntheses/social-phenomena-everyday-life-reproduction-synthesis.md` integrating Labor, Education, Family, and Consumption theme routes.
- Updated `knowledge/query-playbook.md` with Phase 1 everyday-life reproduction routes and smoke commands.
- No W3/W5/W10 records were added; this is a cross-theme synthesis/navigation layer only.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no current-events or policy claim was introduced.

## 2026-06-16 — Social Phenomena Phase 2 platform public order synthesis (G033)

- Added `knowledge/syntheses/social-phenomena-platform-public-order-synthesis.md` integrating Media-platform, Governance-law, and Class-youth theme routes.
- Updated `knowledge/query-playbook.md` with Phase 2 platform/public-order/class routes and smoke commands.
- No W3/W5/W10 records were added; this is a cross-theme synthesis/navigation layer only.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no platform/current-events/legal/policy claim was introduced.

## 2026-06-16 — Social Phenomena Phase 3 body psyche space risk synthesis (G034)

- Added `knowledge/syntheses/social-phenomena-body-psyche-space-risk-synthesis.md` integrating Psychological-distress, Urban-housing, and Health-body theme routes.
- Updated `knowledge/query-playbook.md` with Phase 3 body/psyche/space/risk routes and smoke commands.
- No W3/W5/W10 records were added; this is a cross-theme synthesis/navigation layer only.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; no clinical, therapy, medical, housing, policy, or current-events claim was introduced.

## 2026-06-16 — Social Phenomena Superphase query and validation layer (G035)

- Added `knowledge/scripts/query_social_phenomena_superphase.py` with 30 concrete prompt routes and evidence-backed fallback terms.
- Added `knowledge/qa/social-phenomena-superphase-audit.md` documenting the 10 themes, 3 phase syntheses, and 30 prompt smoke matrix.
- Updated `knowledge/query-playbook.md` with final Social Phenomena Superphase query router commands.
- Added `knowledge/scripts/validate_social_phenomena_superphase.py` for final superphase artifact/query/theme/global validation.
- Boundary reaffirmed: W3/W5 remain `draft`; W10 remains `pilot-draft`; no `split_md/` or `split_md_clean/` edits; downstream social labels are routed through declared evidence-backed fallback terms when direct corpus hits are absent.

## 2026-06-16 — Social Phenomena Superphase final handoff surfaces (G036)

- Updated `README.md`, `knowledge/README.md`, `knowledge/STATE.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, `AGENTS.md`, and `skills/ismism-knowledge-operator/SKILL.md` with Social Phenomena Superphase navigation.
- Added `knowledge/qa/social-phenomena-superphase-final-closure.md`.
- Existing Health-body validator markers were retained for backward-compatible theme validators while adding the final superphase marker.

## 2026-06-16 — Social Phenomena Superphase ai-slop-cleaner pass (G036)

- Ran mandatory final ai-slop-cleaner inspection pass over G032–G036 superphase changed/new surfaces.
- Report: `.omx/reviews/social-phenomena-ai-slop-cleaner-report.md`.
- Classification: superphase query `fallbacks` are grounded evidence-routing fallbacks for downstream labels with no direct corpus hits, not masking fallback slop.
- Cleanup result: no files changed by cleaner pass.

## 2026-06-16 — Social Phenomena Superphase independent review gate (G036)

- Independent code-reviewer returned APPROVE.
- Independent architect returned CLEAR.
- Final quality gate evidence appended to `knowledge/qa/social-phenomena-superphase-final-closure.md`.
- Residual risk accepted: query helpers are lightweight traceability routers, not semantic rankers; future user-facing diagnosis may improve ranking later.

## 2026-06-17 — Legacy non-mainline deletion pass

- Removed `split_pdf/`, which only held a single row 176 PDF slice and is a regenerable derived layer, not a raw/clean text or interpretation source.
- Removed `Zhuyi_Matrix_Engine/ismism_executable_blueprint.md` as a garbled obsolete execution blueprint; retained `Zhuyi_Matrix_Engine/Atlas_DB/*` as candidate-only legacy material.
- Removed `omx_wiki/` session side-branch notes and `.ruff_cache/` tool cache; retained active `.omx/` runtime state.
- Updated `目录索引_结构化.csv` so `split_pdf_exists=0` matches filesystem state, then regenerated W1 manifests via `knowledge/scripts/build_w1_manifests.py`.
- Boundary reaffirmed: no `split_md/` or `split_md_clean/` edits; W3/W5 remain `draft`; W10 remains `pilot-draft`.

## 2026-06-17 — Row 176 clean text redone

- Checkpoint commit before editing: `c119b9e chore: checkpoint knowledge layers and legacy cleanup`.
- Rejected a local Ollama `gemma4:latest` row176 clean attempt because spot audit found terminology drift (`2字头` / `联结` risk).
- Replaced row176 clean with deterministic high-fidelity light cleanup: page headings preserved 27/27; raw non-empty line substrings missing from clean = 0; prior W3 quote `因为阿芬那留斯那边主体性是一个常项` still present.
- Regenerated W1 manifests/chunks and refreshed `knowledge/segment-cards/0176_2-4-2-4.md` clean hash/summary.
- Added `.ruff_cache/` and `omx_wiki/` to `.gitignore` after `omx_wiki/` was regenerated by session tooling, then removed that regenerated side-branch again.
- Added `knowledge/qa/row176-clean-redo-audit.md`.
