# ISMISM 知识库消化状态（持续处理状态文件）

- created: 2026-05-08
- updated: 2026-06-15 CST
- current_phase: W1–W9 repo-local completion accepted; W10 further absorption pilot expanded; AI theme, Chinese Philosophy, and Religion Problem maximum absorption layers complete as draft/pilot-draft evidence layers
- executor: Codex long-run
- repository: `/home/weathour/文档/ismism-system`
- continuation_anchor: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- omx_notepad_anchor: `/home/weathour/文档/psychoanalytic-writing-lab/.omx/notepad.md`

## Must Read On Resume

任何 agent / 新上下文 / 压缩后恢复时，必须先读：

1. `ISMISM-MAINLINE-HANDOFF.md`
2. `knowledge/STATE.md`
3. `knowledge/DIGESTION_PROGRAM.md`
4. `knowledge/references/movement-patterns-guide.md` — 矩阵运动模式全谱系（6 族 × 6 子类 + 阅读协议 + 案例分析）
5. `knowledge/logs/operation-log.md`
6. `knowledge/qa/validation-report.md`
7. `knowledge/qa/concept-drift-report.md`
8. `knowledge/qa/evidence-claim-audit.md`
9. `knowledge/qa/rejected-interpretations.md`
10. `knowledge/qa/w5-relation-audit.md`
11. `knowledge/qa/w1-recovery-audit.md`
12. `knowledge/manifests/corpus-manifest.json`
13. `knowledge/manifests/missing-and-anomalies.md`
14. `knowledge/lexicon/term-senses.jsonl`
15. `knowledge/relations/relation-assets.jsonl`
16. `knowledge/w10-absorption/PLAN.md`
17. `knowledge/w10-absorption/index.md`
18. `knowledge/themes/ai/README.md`
19. `knowledge/themes/ai/ai-synthesis.md`
20. `knowledge/themes/chinese-philosophy/README.md`
21. `knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md`
22. `README.md`
23. `docs/archive/legacy-process-and-prototype-index.md`

仅在需要追溯旧方法/候选层时，再读：

24. `Zhuyi_Matrix_Engine/Phase0_Corpus/Matrix_Backbone.md`
25. `Zhuyi_Matrix_Engine/Phase1_Concepts/Boundary_Rules.md`

旧前端/产品设计文档与旧 clean-corpus handoff 指针已于 2026-06-12 删除；如需确认删除边界，读 `docs/archive/legacy-process-and-prototype-index.md`。

## Continuation Anchors

- Master program: `knowledge/DIGESTION_PROGRAM.md`
- Live state: `knowledge/STATE.md`
- Current repo mainline handoff: `ISMISM-MAINLINE-HANDOFF.md`
- Legacy/archive index: `docs/archive/legacy-process-and-prototype-index.md`
- Operation log: `knowledge/logs/operation-log.md`
- W10 pilot plan: `knowledge/w10-absorption/PLAN.md`
- W10 pilot index: `knowledge/w10-absorption/index.md`
- AI theme maximum absorption: `knowledge/themes/ai/README.md`
- AI theme validator: `knowledge/scripts/validate_ai_theme.py`
- AI theme audits: `knowledge/qa/ai-theme-absorption-audit.md`, `knowledge/qa/ai-theme-evidence-claim-audit.md`, `knowledge/qa/ai-theme-ultraqa-report.md`
- Chinese Philosophy maximum absorption: `knowledge/themes/chinese-philosophy/README.md`
- Chinese Philosophy validator/query: `knowledge/scripts/validate_chinese_philosophy_theme.py`, `knowledge/scripts/query_chinese_philosophy_theme.py`
- Chinese Philosophy audits: `knowledge/qa/chinese-philosophy-absorption-audit.md`, `knowledge/qa/chinese-philosophy-evidence-claim-audit.md`, `knowledge/qa/chinese-philosophy-ultraqa-report.md`
- Religion Problem maximum absorption: `knowledge/themes/religion/README.md`
- Religion Problem validator/query: `knowledge/scripts/validate_religion_theme.py`, `knowledge/scripts/query_religion_theme.py`
- Religion Problem audits: `knowledge/qa/religion-absorption-audit.md`, `knowledge/qa/religion-evidence-claim-audit.md`, `knowledge/qa/religion-ultraqa-report.md`
- W10 pilot audit: `knowledge/qa/w10-pilot-audit.md`
- absorption strength distribution: `knowledge/qa/absorption-strength-distribution.md`
- W10 → W3/W5 gap queue: `knowledge/qa/w10-w3-w5-gap-followups.md`
- Completion audit: `knowledge/qa/w1-recovery-audit.md`
- GPT-5.3 Spark start prompt: `knowledge/prompts/gpt53-spark-start.md`
- W3 start prompt: `knowledge/prompts/w3-start.md`
- External psychoanalytic-writing-lab pointer: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- OMX compaction note: `/home/weathour/文档/psychoanalytic-writing-lab/.omx/notepad.md`

## Current Known Corpus State

W1 已完成恢复并复核：

- TOC 行数：`363`
- `knowledge/manifests/segments.jsonl` 记录：`363`
- segments.jsonl`: 363
- `knowledge/manifests/chunks.jsonl` 记录：`1594`
- chunks.jsonl`: 1594
- row 176 status: available
- W2 segment cards complete; ready for W3
- `split_md/*.md` 现有：`363`（恢复后完整）
- `split_md_clean/*.md` 现有：`363`（恢复后完整；当前行 176 的 clean 通过拷贝 raw 暂补）
- `knowledge/manifests/chunks.jsonl`：`1594`（覆盖 363 个可用分段）
- 缺失文本段：`0`
- 缺失条目（当前恢复后）：`row 176 / 2-4-2-4` 不再缺失
- `split_pdf/`：存在且当前仅恢复了 `1` 个对应 PDF（`row 176`），其余仍属未再生层缺口
- Atlas_DB 仍为 `candidate-only`

## W1 Outputs

- `knowledge/scripts/build_w1_manifests.py`
- `knowledge/scripts/validate_w1_manifests.py`
- `knowledge/manifests/corpus-manifest.json`
- `knowledge/manifests/segments.jsonl`
- `knowledge/manifests/chunks.jsonl`
- `knowledge/manifests/missing-and-anomalies.md`
- `knowledge/README.md`
- `knowledge/qa/w1-completion-audit.md`
- `knowledge/qa/w1-recovery-audit.md`

## Active Batch

- batch_id: RELIGION-THEME-MAX-2026-06-15
- batch_type: Religion Problem maximum absorption over W3/W5/W10/theme surfaces
- status: complete as draft/pilot-draft additive layer; existing W1–W9 completion remains accepted
- completed_at: 2026-06-15 CST
- expected_outputs: `knowledge/themes/religion/*`; Religion W3/W5 batches; Religion W10 cards; `knowledge/scripts/validate_religion_theme.py`; Religion QA audits; updated navigation/handoff surfaces.

## Progress Counters

| Layer | Done | Total | Notes |
|---|---:|---:|---|
| segments manifest | 363 | 363 | complete; row 176 已恢复 |
| chunks manifest | 1594 | 1594 | complete（每段可用清洗文本） |
| segment cards | 363 | 363 | W2 complete; latest batch rows: 353,354,355,356,357,358,359,360,361,362,363 |
| core term senses | 705 | ≥500 senses / ≥200 terms | W3 batch 1–35 + W3-AI + W3-Chinese-Philosophy + W3-Religion draft complete; MASTER-SPEC W3 quantitative floors reached; all draft; W6 audit found no blocking issue |
| level-1 position cards | 4 | 4 | W4-L1 draft complete |
| level-2 position cards | 16 | 16 | W4-L2 draft complete for fields 1–4 (`1-1`–`4-4`) |
| level-3 position cards | 64 | 64 | W4-L3 complete (`1-1-1`–`4-4-4`) draft; no canonical promotion |
| level-4 light position cards | 172 | 172 | W4-L4-B1–B22 draft (`1-1-1-1`–`3-3-3-4` with row gaps and duplicate/auxiliary source rows); current count target follows MASTER-SPEC wording and is complete draft; W6 audit no blocking issue |
| relation assets | 191 | 60+ | W5-B1–B5 + W5-AI + W5-Chinese-Philosophy + W5-Religion draft; all 12 relation types covered; W5 quantitative gate reached; W6 relation strength audit found no blocking issue |
| W6 audit reports | 4 | 4 | validation, concept drift, evidence-claim, rejected-interpretations complete; no blocking issue |
| syntheses | 6 | 6 | W7 draft syntheses complete; source-tag check passed |
| usage protocol | 3 | 3 | W8 complete: usage protocol, query playbook, export manifest |
| W9 integration index | 1 | 1 repo-local draft | Prepared inside repo; accepted as sufficient for `ismism-system` on 2026-06-10 CST |
| W9 external status audit | 1 | 1 repo-local audit | `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`; records current external mismatch without outside write |
| W9 external status checker | 1 | 1 repo-local script | `knowledge/scripts/check_w9_external_status.py`; read-only checker for current external match state |
| W9 maintainer decision record | 1 | 1 repo-local decision | `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`; Option A accepted repo-local W9 as sufficient |
| W10 absorption cards | 122 | pilot batch + AI + Chinese Philosophy + Religion expansions | argument/process/case cards under `knowledge/w10-absorption/`; pilot-draft only; 28 AI rows/cards + 45 Chinese Philosophy cards + 45 Religion Problem cards |
| W10 validator | 1 | 1 script | `knowledge/scripts/validate_w10_absorption.py`; checks metadata, index, and quote substrings |
| W10 gap follow-up queue | 1 | pilot queue | `knowledge/qa/w10-w3-w5-gap-followups.md`; prevents W10 from bypassing later W3/W5 review |
| absorption strength distribution | 1 | 1 snapshot | `knowledge/qa/absorption-strength-distribution.md`; 143 rows remain W1/W2-only; 64.6% clean-text volume has W3/W5/W10 absorption; 85 rows now have W3+W5+W10 overlap |
| AI theme manifest | 60 | 60 candidates | `knowledge/themes/ai/ai-row-manifest.jsonl`; all candidates classified |
| AI theme quote bank | 208 | 208 exact quotes | `knowledge/themes/ai/ai-evidence-bank.jsonl`; validated exact substrings |
| AI theme W3/W5 | 37 / 30 | draft | `W3-AI-2026-06-15`; `W5-AI-2026-06-15` |
| Religion theme manifest | 80 | 80 candidates | `knowledge/themes/religion/religion-row-manifest.jsonl`; rows 24–45 core fully covered |
| Religion theme quote bank | 226 | 226 exact quotes | `knowledge/themes/religion/religion-evidence-bank.jsonl`; validated exact substrings |
| Religion theme W3/W5 | 64 / 51 | draft | `W3-RELIGION-2026-06-15`; `W5-RELIGION-2026-06-15` |
| final completion audit | 2 | 2 | `knowledge/qa/master-spec-completion-audit.md` + `master-spec-requirement-traceability.md`; repo-local completion accepted; external W9 is downstream/manual |

## Decisions Resolved in W1 Recovery

- 使用 `row 176 / split_pdf` 的单点重建 + `split_md` 直接回填；`split_md_clean` 暂以 `clean md=copy(raw md)` 过渡方式补齐。
- `segment_id` 方案维持：`ismism:seg:<row_id>`。
- `chunks.jsonl` 继续按 clean 文本切块后生成，仅用于检索。
- `split_pdf` 仍属于再生派生层；当前仅对 row 176 有对应文件，未全量重建并不阻断 W2。
- Atlas_DB 仍是候选层，不改变 canonical 真相。


## Current Absorption Strength Snapshot — 2026-06-15

Full details: `knowledge/qa/absorption-strength-distribution.md`.

| Tier | Rows | Row % | Clean-text % |
|---|---:|---:|---:|
| W1/W2 only | 143 | 39.4% | 35.4% |
| W1/W2 + W3 | 78 | 21.5% | 24.0% |
| W1/W2 + W5 only | 1 | 0.3% | 0.2% |
| W1/W2 + W3 + W5 | 28 | 7.7% | 6.9% |
| W1/W2 + W10 only | 18 | 5.0% | 4.9% |
| W1/W2 + W3 + W10 | 10 | 2.8% | 2.9% |
| W1/W2 + W5 + W10 | 0 | 0.0% | 0.0% |
| W1/W2 + W3 + W5 + W10 | 85 | 23.4% | 25.7% |

Operational reading: W1/W2 is complete, but deep absorption is uneven. AI, Chinese Philosophy, and Religion Problem theme work created 85 W3+W5+W10 full-overlap rows and moved deep absorption to 64.6% of clean-text volume. Future W10/W3/W5 batches should target remaining high-text W1/W2-only rows such as rows 107, 174, 159, 255, 160, and 105.

## Open Decisions

- 是否继续使用“row 176 clean 文件临时拷贝”方案，或再次运行 LLM clean 产出可复核的 `split_md_clean`。
- 是否继续为 row 176 增补对应 `split_pdf` 全量重建（建议通过 `split_pdf_by_toc.py` 全量再生），以去除后续大规模 `stale split_pdf_exists` 标注。
- W10 后续批次如何排序：根据 `knowledge/qa/absorption-strength-distribution.md`，优先覆盖高文本量、W3/W5 低覆盖或零覆盖的行；当前首选 backlog 包括 rows 85, 107, 174, 65, 159, 87, 255, 39, 160, 105；继续保持小批量、quote-substring 可验证。
- W9 repo-local sufficiency 已于 2026-06-10 CST 被用户/维护者接受；外部仓库落地现在是下游手工集成任务，不阻塞本仓库完成。
- 若未来仍需跨仓库 W9 落地，需要另行显式授权写入 `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`，并同时确认该授权优先于本仓库当前硬边界。

## Next Action

推荐下一步：若继续主题层，先读 `knowledge/themes/ai/README.md`、`knowledge/themes/chinese-philosophy/README.md` 与对应 QA audit；若继续非主题 W10，仍按吸收强度分布选择小批量高价值行，并记录 `w3_w5_gap_review`。恢复或交付前运行 AI/W10 与既有 validators。若未来需要实际接入 `psychoanalytic-writing-lab`，按 `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md` 由人工或另行授权流程处理外部文件。

恢复工作时先运行：

1. `python3 knowledge/scripts/validate_w10_absorption.py --repo .`
2. `python3 knowledge/scripts/validate_ai_theme.py --repo . --final`
3. `python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final`
4. `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .`
5. `python3 knowledge/scripts/validate_w3_term_senses.py --repo .`
6. `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 140 --require-type-min 2`
7. `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4`
8. `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16`
9. `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64`
10. `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172`
11. `git diff --check`
12. 若需要审计跨仓库 W9，运行 `python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match` 与 `python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9`；当前预期为失败，除非外部文件已被人工/授权流程替换。

除非另有 review 决议，W3/W5 仍保持 `draft`，不得 canonical 提升。

## Handoff Block

如果上下文压缩或中断，请从这里恢复：

> 当前任务是维护 `/home/weathour/文档/ismism-system` 的 ISMISM 可追溯知识层。W1–W9 repo-local 完成状态已接受；当前计数：W1 corpus manifests 363/363，W2 segment cards 363/363，W3 term senses 705 draft senses / 357 terms，W4 position cards L1/L2/L3/L4 = 4/16/64/172，W5 relation assets 191 draft relations 且 12/12 relation types covered，W6 4 份审计报告完成且无 blocking issue，W7 6 份 syntheses 完成，W8 3 份 usage protocol docs 完成。W10 现在有 122 张 pilot-draft argument/process/case cards。AI Theme Maximum Absorption Program 已完成：`knowledge/themes/ai/` 覆盖 60 个 AI/VR/智能/算法/机器人候选行、208 条 exact quote、37 条 AI W3 draft senses、30 条 AI W5 draft relations、28 个 AI W10 row/card；Chinese Philosophy Maximum Absorption Program 已完成：`knowledge/themes/chinese-philosophy/` 覆盖 70 行、238 条 exact quote、60 条 W3 draft senses、50 条 W5 draft relations、45 张新增 W10 cards，并有 `chinese-philosophy-synthesis.md` / `ancient-chinese-philosophy-synthesis.md` / `mao-philosophy-synthesis.md`、`validate_chinese_philosophy_theme.py`、query helper 与三份 QA audit。Religion Problem Maximum Absorption Program 已完成：`knowledge/themes/religion/` 覆盖 80 行、226 条 exact quote、64 条 W3 draft senses、51 条 W5 draft relations、45 张 Religion W10 cards，并有三篇 synthesis、validator/query helper 与三份 QA audit。外部目标 `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md` 仍是下游手工集成事项，不阻塞本仓库完成。恢复后先运行 `validate_w10_absorption.py --repo .`、`validate_ai_theme.py --repo . --final`、`validate_chinese_philosophy_theme.py --repo . --final`、`validate_master_spec_outputs.py --repo .` 和 W3/W4/W5 validators。不要继续旧前端；Atlas 只能作 candidate；W3/W5 不得 canonical 升级；W10 仍是 pilot-draft。

主线交接见 `ISMISM-MAINLINE-HANDOFF.md`；旧 clean corpus handoff 与旧前端 README 快照已删除，删除边界见 `docs/archive/legacy-process-and-prototype-index.md`。


## W4 L1 Batch
- batch_id: W4-L1-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 1, 2, 3, 4
- outputs:
  - `knowledge/position-cards/1.md`
  - `knowledge/position-cards/2.md`
  - `knowledge/position-cards/3.md`
  - `knowledge/position-cards/4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/scripts/validate_w4_position_cards.py`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
- status: draft only; W4 lower layers pending; no canonical promotion

## W4 L2 Batch 1
- batch_id: W4-L2-B1-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 1-1, 1-2, 1-3, 1-4
- outputs:
  - `knowledge/position-cards/1-1.md`
  - `knowledge/position-cards/1-2.md`
  - `knowledge/position-cards/1-3.md`
  - `knowledge/position-cards/1-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 4` → PASS
- status: draft only; W4-L2 remaining 12 cards; no canonical promotion

## W4 L2 Batch 2
- batch_id: W4-L2-B2-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 2-1, 2-2, 2-3, 2-4
- outputs:
  - `knowledge/position-cards/2-1.md`
  - `knowledge/position-cards/2-2.md`
  - `knowledge/position-cards/2-3.md`
  - `knowledge/position-cards/2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 8` → PASS
- status: draft only; W4-L2 remaining 8 cards; no canonical promotion

## W4 L2 Batch 3
- batch_id: W4-L2-B3-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 3-1, 3-2, 3-3, 3-4
- outputs:
  - `knowledge/position-cards/3-1.md`
  - `knowledge/position-cards/3-2.md`
  - `knowledge/position-cards/3-3.md`
  - `knowledge/position-cards/3-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 12` → PASS
- status: draft only; W4-L2 remaining 4 cards; no canonical promotion

## W4 L2 Batch 4
- batch_id: W4-L2-B4-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 4-1, 4-2, 4-3, 4-4
- outputs:
  - `knowledge/position-cards/4-1.md`
  - `knowledge/position-cards/4-2.md`
  - `knowledge/position-cards/4-3.md`
  - `knowledge/position-cards/4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
- status: draft only; W4-L2 complete; W4-L3/W4-L4 pending; no canonical promotion

## W4 L3 Batch 1
- batch_id: W4-L3-B1-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 1-1-1, 1-1-2, 1-1-3, 1-1-4
- outputs:
  - `knowledge/position-cards/1-1-1.md`
  - `knowledge/position-cards/1-1-2.md`
  - `knowledge/position-cards/1-1-3.md`
  - `knowledge/position-cards/1-1-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 4` → PASS
- status: draft only; W4-L3 remaining 60 cards; W4-L4 pending; no canonical promotion

## W4 L3 Batch 2
- batch_id: W4-L3-B2-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 1-2-1, 1-2-2, 1-2-3, 1-2-4
- outputs:
  - `knowledge/position-cards/1-2-1.md`
  - `knowledge/position-cards/1-2-2.md`
  - `knowledge/position-cards/1-2-3.md`
  - `knowledge/position-cards/1-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 8` → PASS
- status: draft only; W4-L3 remaining 56 cards; W4-L4 pending; no canonical promotion

## W4 L3 Batch 3
- batch_id: W4-L3-B3-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 1-3-1, 1-3-2, 1-3-3, 1-3-4
- outputs:
  - `knowledge/position-cards/1-3-1.md`
  - `knowledge/position-cards/1-3-2.md`
  - `knowledge/position-cards/1-3-3.md`
  - `knowledge/position-cards/1-3-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 12` → PASS
- status: draft only; W4-L3 remaining 52 cards; W4-L4 pending; no canonical promotion

## W4 L3 Batch 4
- batch_id: W4-L3-B4-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 1-4-1, 1-4-2, 1-4-3, 1-4-4
- outputs:
  - `knowledge/position-cards/1-4-1.md`
  - `knowledge/position-cards/1-4-2.md`
  - `knowledge/position-cards/1-4-3.md`
  - `knowledge/position-cards/1-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 16` → PASS
- status: draft only; W4-L3 field 1 complete; W4-L3 remaining 48 cards; W4-L4 pending; no canonical promotion

## W3 Batch 1
- batch_id: W3-B1-2026-05-08
- completed_at: 2026-05-08 18:47 CST
- terms_processed: 主体, 客体, 实践
- sense_records: 13
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/lexicon/term-candidate-stats.tsv`
  - `knowledge/qa/w3-lexicon-audit.md`
- status: draft only; no canonical term senses yet

## W3 Batch 2（部分）
- batch_id: W3-B2-2026-05-08
- completed_at: 2026-05-08 19:05 CST
- terms_processed: 历史（5义项）
- sense_records: 5
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- status: draft only; 人民/理论待处理

## W3 Batch 3
- batch_id: W3-B3-2026-05-08
- completed_at: 2026-05-08 19:18 CST (精炼复核：19:20 CST)
- terms_processed: 人民（5义项）
- sense_records: 5
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- status: draft only; 理论待处理

## W3 Batch 4
- batch_id: W3-B4-2026-05-08
- completed_at: 2026-05-08 19:30 CST
- terms_processed: 理论（5义项）
- sense_records: 5
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- status: draft only; 进入机制词前置对齐

## W3 Batch 5
- batch_id: W3-B5-2026-05-08
- completed_at: 2026-05-08 20:40 CST
- terms_processed: 主体化、客体化、去主体化（各1）
- sense_records: 3
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- status: draft only; W5 关系资产前置对齐

## W3 Batch 6
- batch_id: W3-B6-2026-06-03
- completed_at: 2026-06-03 19:25 CST
- terms_processed: 实体（5义项）、物质（4义项）、意识形态（5义项）
- sense_records: 14
- outputs:
  - `knowledge/scripts/validate_w3_term_senses.py`
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B6-2026-06-03` → records=14, terms=3, quotes=29, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=45, terms=12, quotes=121, errors=0, warnings=0
- status: draft only; no canonical term senses yet

## W3 Batch 7
- batch_id: W3-B7-2026-06-03
- completed_at: 2026-06-03 19:45 CST
- terms_processed: 本体论（4义项）、认识论（4义项）、目的论（4义项）
- sense_records: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B7-2026-06-03` → records=12, terms=3, quotes=27, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=57, terms=15, quotes=148, errors=0, warnings=0
- status: draft only; no canonical term senses yet

## W3 Batch 8
- batch_id: W3-B8-2026-06-03
- completed_at: 2026-06-03 20:20 CST
- terms_processed: 场域论（4义项）、符号（5义项）、符号秩序（4义项）
- sense_records: 13
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B8-2026-06-03` → records=13, terms=3, quotes=27, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=70, terms=18, quotes=175, errors=0, warnings=0
- status: draft only; no canonical term senses yet

## W3 Batch 9
- batch_id: W3-B9-2026-06-03
- completed_at: 2026-06-03 21:05 CST
- terms_processed: 中介（5义项）、理论家（4义项）、实践单元（4义项）
- sense_records: 13
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B9-2026-06-03` → records=13, terms=3, quotes=26, errors=0, warnings=0
- status: draft only; no canonical term senses yet

## W3 Batch 10
- batch_id: W3-B10-2026-06-03
- completed_at: 2026-06-03 21:05 CST
- terms_processed: 闭合（5义项）、有限性（5义项）、误认（4义项）、跃迁（3义项）
- sense_records: 17
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B10-2026-06-03` → records=17, terms=4, quotes=34, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
- status: draft only; W4 minimum precondition reached; no canonical term senses yet

## W5 Batch 1
- batch_id: W5-B1-2026-05-08
- completed_at: 2026-05-08 20:50 CST
- relation_records: 12
- families: mechanism conversion, theory production, mechanism tension, history/people/theory mediation, subject-as-practice-unit, mechanism/noun boundary
- outputs:
  - `knowledge/relations/relation-assets.jsonl`
  - `knowledge/relations/relation-prompts.md`
  - `knowledge/relations/route-cards.md`
  - `knowledge/relations/tension-cards.md`
  - `knowledge/relations/mediation-cards.md`
  - `knowledge/relations/boundary-cards.md`
  - `knowledge/relations/misrecognition-cards.md`
  - `knowledge/qa/w5-relation-audit.md`
- status: draft only; no canonical relation claims


## W2 Next Batch
- next_row: 17
- latest_batch_count: 16
- processed_cumulative: 16/363

## W2 Next Batch
- next_row: 33
- latest_batch_count: 16
- processed_cumulative: 32/363

## W2 Next Batch
- next_row: 49
- latest_batch_count: 16
- processed_cumulative: 48/363

## W2 Next Batch
- next_row: 65
- latest_batch_count: 16
- processed_cumulative: 64/363

## W2 Next Batch
- next_row: 81
- latest_batch_count: 16
- processed_cumulative: 80/363

## W2 Next Batch
- next_row: 97
- latest_batch_count: 16
- processed_cumulative: 96/363

## W2 Next Batch
- next_row: 113
- latest_batch_count: 16
- processed_cumulative: 112/363

## W2 Next Batch
- next_row: 129
- latest_batch_count: 16
- processed_cumulative: 128/363

## W2 Next Batch
- next_row: 145
- latest_batch_count: 16
- processed_cumulative: 144/363

## W2 Next Batch
- next_row: 161
- latest_batch_count: 16
- processed_cumulative: 160/363

## W2 Next Batch
- next_row: 177
- latest_batch_count: 16
- processed_cumulative: 176/363

## W2 Next Batch
- next_row: 193
- latest_batch_count: 16
- processed_cumulative: 192/363

## W2 Next Batch
- next_row: 209
- latest_batch_count: 16
- processed_cumulative: 208/363

## W2 Next Batch
- next_row: 225
- latest_batch_count: 16
- processed_cumulative: 224/363

## W2 Next Batch
- next_row: 241
- latest_batch_count: 16
- processed_cumulative: 240/363

## W2 Next Batch
- next_row: 257
- latest_batch_count: 16
- processed_cumulative: 256/363

## W2 Next Batch
- next_row: 273
- latest_batch_count: 16
- processed_cumulative: 272/363

## W2 Next Batch
- next_row: 289
- latest_batch_count: 16
- processed_cumulative: 288/363

## W2 Next Batch
- next_row: 305
- latest_batch_count: 16
- processed_cumulative: 304/363

## W2 Next Batch
- next_row: 321
- latest_batch_count: 16
- processed_cumulative: 320/363

## W2 Next Batch
- next_row: 337
- latest_batch_count: 16
- processed_cumulative: 336/363

## W2 Next Batch
- next_row: 353
- latest_batch_count: 16
- processed_cumulative: 352/363

## W2 Next Batch
- next_row: 364
- latest_batch_count: 11
- processed_cumulative: 363/363


## W4 L3 Batch 13
- batch_id: W4-L3-B13-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 4-1-1, 4-1-2, 4-1-3, 4-1-4
- outputs:
  - `knowledge/position-cards/4-1-1.md`
  - `knowledge/position-cards/4-1-2.md`
  - `knowledge/position-cards/4-1-3.md`
  - `knowledge/position-cards/4-1-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 52` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L3 remaining 12 cards; no canonical promotion


## W4 L3 Batch 14
- batch_id: W4-L3-B14-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 4-2-1, 4-2-2, 4-2-3, 4-2-4
- outputs:
  - `knowledge/position-cards/4-2-1.md`
  - `knowledge/position-cards/4-2-2.md`
  - `knowledge/position-cards/4-2-3.md`
  - `knowledge/position-cards/4-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 56` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L3 remaining 8 cards; no canonical promotion


## W4 L3 Batch 15
- batch_id: W4-L3-B15-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 4-3-1, 4-3-2, 4-3-3, 4-3-4
- outputs:
  - `knowledge/position-cards/4-3-1.md`
  - `knowledge/position-cards/4-3-2.md`
  - `knowledge/position-cards/4-3-3.md`
  - `knowledge/position-cards/4-3-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 60` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L3 remaining 4 cards; no canonical promotion


## W4 L3 Batch 16
- batch_id: W4-L3-B16-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 4-4-1, 4-4-2, 4-4-3, 4-4-4
- outputs:
  - `knowledge/position-cards/4-4-1.md`
  - `knowledge/position-cards/4-4-2.md`
  - `knowledge/position-cards/4-4-3.md`
  - `knowledge/position-cards/4-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L3 complete; W4-L4 and W3 expansion pending; no canonical promotion


## W4 L4 Batch 1
- batch_id: W4-L4-B1-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-1-1-1, 1-1-1-2, 1-1-1-3, 1-1-1-4, 1-1-2-1, 1-1-2-2, 1-1-2-3, 1-1-2-4
- outputs:
  - `knowledge/position-cards/1-1-1-1.md`–`1-1-1-4.md`
  - `knowledge/position-cards/1-1-2-1.md`–`1-1-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 8` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 2
- batch_id: W4-L4-B2-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-1-3-1, 1-1-3-2, 1-1-3-3, 1-1-3-4, 1-1-4-1, 1-1-4-2, 1-1-4-3, 1-1-4-4
- outputs:
  - `knowledge/position-cards/1-1-3-1.md`–`1-1-3-4.md`
  - `knowledge/position-cards/1-1-4-1.md`–`1-1-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 16` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 3
- batch_id: W4-L4-B3-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-2-1-1, 1-2-1-2, 1-2-1-3, 1-2-1-4, 1-2-2-1, 1-2-2-2, 1-2-2-3, 1-2-2-4
- outputs:
  - `knowledge/position-cards/1-2-1-1.md`–`1-2-1-4.md`
  - `knowledge/position-cards/1-2-2-1.md`–`1-2-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 24` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 4
- batch_id: W4-L4-B4-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-2-3-1, 1-2-3-2, 1-2-3-3, 1-2-3-4, 1-2-4-1, 1-2-4-2, 1-2-4-3, 1-2-4-4
- outputs:
  - `knowledge/position-cards/1-2-3-1.md`–`1-2-3-4.md`
  - `knowledge/position-cards/1-2-4-1.md`–`1-2-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 32` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 5
- batch_id: W4-L4-B5-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-3-1-1, 1-3-1-2, 1-3-1-3, 1-3-1-4, 1-3-2-1, 1-3-2-2, 1-3-2-3, 1-3-2-4
- outputs:
  - `knowledge/position-cards/1-3-1-1.md`–`1-3-1-4.md`
  - `knowledge/position-cards/1-3-2-1.md`–`1-3-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 40` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 6
- batch_id: W4-L4-B6-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-3-3-1, 1-3-3-2, 1-3-3-3, 1-3-3-4, 1-3-4-1, 1-3-4-2, 1-3-4-3, 1-3-4-4
- outputs:
  - `knowledge/position-cards/1-3-3-1.md`–`1-3-3-4.md`
  - `knowledge/position-cards/1-3-4-1.md`–`1-3-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 48` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 7
- batch_id: W4-L4-B7-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 1-4-1-1, 1-4-1-2, 1-4-1-3, 1-4-1-4, 1-4-2-1, 1-4-2-2, 1-4-2-3, 1-4-2-4
- outputs:
  - `knowledge/position-cards/1-4-1-1.md`–`1-4-1-4.md`
  - `knowledge/position-cards/1-4-2-1.md`–`1-4-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 56` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 remaining per MASTER-SPEC target; no canonical promotion


## W4 L4 Batch 16
- batch_id: W4-L4-B16-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 2-4-3-1, 2-4-3-2, 2-4-3-3, 2-4-3-4, 2-4-4-1, 2-4-4-2, 2-4-4-3, 2-4-4-4
- outputs:
  - `knowledge/position-cards/2-4-3-1.md`–`2-4-3-4.md`
  - `knowledge/position-cards/2-4-4-1.md`–`2-4-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 128` → PASS
  - `git diff --check` → PASS
- status: draft only; fields 1 and 2 L4 complete; W4-L4 remaining per MASTER-SPEC target starts from `3-1-1-1`; no canonical promotion


## W4 L4 Batch 17
- batch_id: W4-L4-B17-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 3-1-1-1, 3-1-1-2, 3-1-1-3, 3-1-1-4, 3-1-2-1, 3-1-2-2, 3-1-2-3, 3-1-2-4
- outputs:
  - `knowledge/position-cards/3-1-1-1.md`–`3-1-1-4.md`
  - `knowledge/position-cards/3-1-2-1.md`–`3-1-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 136` → PASS
  - `git diff --check` → PASS
- status: draft only; `3-1` started through `3-1-2`; W4-L4 remaining per MASTER-SPEC target starts from `3-1-3-1`; no canonical promotion


## W4 L4 Batch 18
- batch_id: W4-L4-B18-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 3-1-3-1, 3-1-3-2, 3-1-3-3, 3-1-3-4, 3-1-4-1, 3-1-4-2, 3-1-4-3, 3-1-4-4
- outputs:
  - `knowledge/position-cards/3-1-3-1.md`–`3-1-3-4.md`
  - `knowledge/position-cards/3-1-4-1.md`–`3-1-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 144` → PASS
  - `git diff --check` → PASS
- status: draft only; `3-1` L4 complete; W4-L4 remaining per MASTER-SPEC target starts from `3-2-1-1`; no canonical promotion


## W4 L4 Batch 19
- batch_id: W4-L4-B19-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 3-2-1-1, 3-2-1-2, 3-2-1-3, 3-2-1-4, 3-2-2-1, 3-2-2-2, 3-2-2-3, 3-2-2-4
- outputs:
  - `knowledge/position-cards/3-2-1-1.md`–`3-2-1-4.md`
  - `knowledge/position-cards/3-2-2-1.md`–`3-2-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 152` → PASS
  - `git diff --check` → PASS
- status: draft only; `3-2` started through `3-2-2`; W4-L4 remaining per MASTER-SPEC target starts from `3-2-3-1`; no canonical promotion


## W4 L4 Batch 20
- batch_id: W4-L4-B20-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 3-2-3-1, 3-2-3-2, 3-2-3-3, 3-2-3-4, 3-2-4-1, 3-2-4-2, 3-2-4-3, 3-2-4-4
- outputs:
  - `knowledge/position-cards/3-2-3-1.md`–`3-2-3-4.md`
  - `knowledge/position-cards/3-2-4-1.md`–`3-2-4-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 160` → PASS
  - `git diff --check` → PASS
- status: draft only; `3-2` L4 complete; W4-L4 remaining per MASTER-SPEC target starts from `3-3-1-1`; no canonical promotion


## W4 L4 Batch 21
- batch_id: W4-L4-B21-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 8
- positions_processed: 3-3-1-1, 3-3-1-2, 3-3-1-3, 3-3-1-4, 3-3-2-1, 3-3-2-2, 3-3-2-3, 3-3-2-4
- outputs:
  - `knowledge/position-cards/3-3-1-1.md`–`3-3-1-4.md`
  - `knowledge/position-cards/3-3-2-1.md`–`3-3-2-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 168` → PASS
  - `git diff --check` → PASS
- status: draft only; `3-3-1` and `3-3-2` L4 complete; W4-L4 remaining per MASTER-SPEC target starts from `3-3-3-1`; no canonical promotion


## W4 L4 Batch 22
- batch_id: W4-L4-B22-2026-06-08
- completed_at: 2026-06-08 CST
- cards_created: 4
- positions_processed: 3-3-3-1, 3-3-3-2, 3-3-3-3, 3-3-3-4
- outputs:
  - `knowledge/position-cards/3-3-3-1.md`–`3-3-3-4.md`
  - `knowledge/position-cards/index.md`
  - `knowledge/qa/w4-position-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100, terms=25, quotes=235, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W4-L4 current 172-card target complete at `3-3-3-4`; no canonical promotion


## W3 Batch 11
- batch_id: W3-B11-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `辩证法`, `欲望`, `他者`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B11-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=112, terms=28, quotes=259, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 112 senses / 28 terms; no canonical promotion


## W3 Batch 12
- batch_id: W3-B12-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `意识`, `驱力`, `语言`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B12-2026-06-08` → records=12, terms=3, quotes=27, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=124, terms=31, quotes=286, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 124 senses / 31 terms; no canonical promotion


## W3 Batch 13
- batch_id: W3-B13-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `主体化`, `客体化`, `去客体化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B13-2026-06-08` → records=12, terms=3, quotes=35, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=136, terms=32, quotes=321, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 136 senses / 32 terms; no canonical promotion


## W3 Batch 14
- batch_id: W3-B14-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `去主体化`, `时间化`, `空间化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B14-2026-06-08` → records=12, terms=3, quotes=27, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=148, terms=34, quotes=348, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 148 senses / 34 terms; no canonical promotion


## W3 Batch 15
- batch_id: W3-B15-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `对象化`, `符号化`, `现象化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B15-2026-06-08` → records=12, terms=3, quotes=25, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=160, terms=37, quotes=373, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 160 senses / 37 terms; no canonical promotion


## W3 Batch 16
- batch_id: W3-B16-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `去符号化`, `去现象化`, `本体论化`, `去本体论化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B16-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=172, terms=41, quotes=397, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 172 senses / 41 terms; no canonical promotion


## W3 Batch 17
- batch_id: W3-B17-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `实体化`, `去实体化`, `表象化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B17-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=184, terms=44, quotes=421, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 184 senses / 44 terms; no canonical promotion


## W3 Batch 18
- batch_id: W3-B18-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `去表象化`, `二元化`, `历史化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B18-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=196, terms=47, quotes=445, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` → PASS
  - `python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` → PASS
  - `git diff --check` → PASS
- status: draft only; W3 now 196 senses / 47 terms; no canonical promotion


## W3 Batch 19
- batch_id: W3-B19-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `去历史化`, `中心化`, `去中心化`, `重新中心化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B19-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=208, terms=51, quotes=469, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 208 senses / 51 terms; no canonical promotion


## W3 Batch 20
- batch_id: W3-B20-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `符号学`, `结构主义`, `能指`, `所指`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B20-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=220, terms=55, quotes=493, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 220 senses / 55 terms; no canonical promotion


## W3 Batch 21
- batch_id: W3-B21-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `差异`, `本质`, `存在`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B21-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=232, terms=58, quotes=517, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 232 senses / 58 terms; no canonical promotion


## W3 Batch 22
- batch_id: W3-B22-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `哲学化`, `辩证法化`, `认识论化`, `目的论化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B22-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=244, terms=62, quotes=541, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 244 senses / 62 terms; no canonical promotion

## W3 Batch 23
- batch_id: W3-B23-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `去目的论化`, `本体化`, `去辩证化`, `教科书化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B23-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=256, terms=66, quotes=565, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 256 senses / 66 terms; no canonical promotion

## W3 Batch 24
- batch_id: W3-B24-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `爱欲`, `力比多`, `享乐`, `献祭`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B24-2026-06-08` → records=12, terms=4, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=268, terms=70, quotes=589, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 268 senses / 70 terms; no canonical promotion

## W3 Batch 25
- batch_id: W3-B25-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `科学化`, `体系化`, `实证化`
- senses_created: 12
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B25-2026-06-08` → records=12, terms=3, quotes=24, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=280, terms=73, quotes=613, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 280 senses / 73 terms; no canonical promotion

## W3 Batch 26
- batch_id: W3-B26-2026-06-08
- completed_at: 2026-06-08 CST
- terms_processed: `共同体`, `主体间性`, `生活世界`, `事件性`, `平等主义`
- senses_created: 20
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B26-2026-06-08` → records=20, terms=5, quotes=40, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=300, terms=78, quotes=653, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - `git diff --check` → PASS
- status: draft only; W3 now 372 senses / 114 terms; W3 phase-1 ≥300 count gate reached; final W3 still pending; no canonical promotion


## W5 Batch 2
- batch_id: W5-B2-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 14
- total_relation_records: 26
- relation_types_covered: 12/12
- outputs:
  - `knowledge/relations/relation-assets.jsonl`
  - `knowledge/relations/route-cards.md`
  - `knowledge/relations/tension-cards.md`
  - `knowledge/relations/mediation-cards.md`
  - `knowledge/relations/boundary-cards.md`
  - `knowledge/relations/misrecognition-cards.md`
  - `knowledge/relations/overcode-cards.md`
  - `knowledge/relations/evidence-claim-cards.md`
  - `knowledge/qa/w5-relation-audit.md`
- status: draft only; B1 records backfilled with source_position/target_position/evidence_segment; W5 target ≥60 still pending; no canonical promotion
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=26, quotes=34, types=12/12, errors=0, warnings=0
  - final W5 gate check with `--min-count 140 --require-type-min 2` remains failing as expected: 26/60 records and `subjectivizes` count=1.
- note: `knowledge/scripts/validate_w5_relation_assets.py` now performs exact clean-text quote checks for W5 `evidence_segment` entries.

## W5 Batch 3
- batch_id: W5-B3-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 14
- total_relation_records: 40
- relation_types_covered: 12/12
- relation_types_with_2plus_examples: 12/12
- focus: subjectivization/objectification mechanisms; event gap/closedness; lifeworld-intersubjectivity mediation; science/system boundary; community overcoding
- outputs:
  - `knowledge/relations/relation-assets.jsonl`
  - `knowledge/relations/mechanism-cards.md`
  - `knowledge/relations/boundary-cards.md`
  - `knowledge/relations/mediation-cards.md`
  - `knowledge/relations/misrecognition-cards.md`
  - `knowledge/relations/overcode-cards.md`
  - `knowledge/relations/evidence-claim-cards.md`
  - `knowledge/relations/relation-prompts.md`
  - `knowledge/qa/w5-relation-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=40, quotes=49, types=12/12, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B3-2026-06-08` → records=14, quotes=15, errors=0, warnings=0
  - final W5 gate check with `--min-count 140 --require-type-min 2` remains failing as expected only on count: 40/60 records.
- status: draft only; W5 target ≥60 still pending; no canonical promotion

## W5 Batch 4
- batch_id: W5-B4-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 10
- total_relation_records: 50
- focus: theory/practice route, philosophization/dialecticization route, textbookification block, symbolic economy tension, objectification in 4-3-1
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B4-2026-06-08` → records=10, quotes=11, errors=0, warnings=0
- status: draft only; no canonical promotion

## W5 Batch 5
- batch_id: W5-B5-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 10
- total_relation_records: 60
- relation_types_covered: 12/12
- relation_types_with_2plus_examples: 12/12
- focus: final W5 count-gate closure; history/people/theory mediation; intersubjective language; closure failure route; naming claim; language-game objectification; science community transition
- outputs:
  - `knowledge/relations/relation-assets.jsonl`
  - `knowledge/relations/mechanism-cards.md`
  - `knowledge/relations/boundary-cards.md`
  - `knowledge/relations/mediation-cards.md`
  - `knowledge/relations/route-cards.md`
  - `knowledge/relations/tension-cards.md`
  - `knowledge/relations/overcode-cards.md`
  - `knowledge/relations/evidence-claim-cards.md`
  - `knowledge/relations/relation-prompts.md`
  - `knowledge/qa/w5-relation-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B5-2026-06-08` → records=10, quotes=10, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 140 --require-type-min 2` → PASS
- status: W5 quantitative gate reached; all W5 records remain `draft`; W6 audit still required before any promotion

## W3 Batch 27
- batch_id: W3-B27-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `学习`, `研究`, `现实`, `通俗化`, `交谈`, `灌输`, `宣传`, `行动`, `信仰`, `忠诚`, `范式`, `知识`
- senses_created: 24
- total_w3_senses: 324
- total_w3_terms: 90
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B27-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=324, terms=90, quotes=701, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 28
- batch_id: W3-B28-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `科学史`, `历史主义`, `危机`, `常态范式`, `范式革命`, `共同信仰`, `方法论`, `知识论`, `学科矩阵`, `范例`, `不可通约性`, `基础主义`
- senses_created: 24
- total_w3_senses: 348
- total_w3_terms: 102
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B28-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=348, terms=102, quotes=749, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 29
- batch_id: W3-B29-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `书写`, `小册子`, `见微知著`, `观察`, `分析`, `反刍`, `现实理论化`, `理论现实化`, `理论劳动`, `自圆其说`, `可行性`, `严肃`
- senses_created: 24
- total_w3_senses: 372
- total_w3_terms: 114
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B29-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=372, terms=114, quotes=797, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 30
- batch_id: W3-B30-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `数据`, `报告`, `细节`, `突发状况`, `情绪感受`, `合理化`, `运动化`, `规律`, `回溯`, `政治经济关系`, `权力关系`, `心理状态`
- senses_created: 24
- total_w3_senses: 396
- total_w3_terms: 126
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B30-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=396, terms=126, quotes=845, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 31
- batch_id: W3-B31-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `回溯性逻辑`, `守阵地`, `剩余`, `site`, `position`, `state`, `版本更新`, `真理事件`, `主体性`, `主体化过程`, `空位置`, `数学化`
- senses_created: 24
- total_w3_senses: 420
- total_w3_terms: 138
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B31-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=420, terms=138, quotes=893, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 32
- batch_id: W3-B32-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `Being`, `Event`, `space`, `点位`, `立场`, `数学知识`, `本体论知识`, `减法`, `矛盾张力`, `知识框架`, `数据交换中介`, `整体降临`
- senses_created: 24
- total_w3_senses: 444
- total_w3_terms: 150
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B32-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=444, terms=150, quotes=941, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 33
- batch_id: W3-B33-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `星丛`, `名称`, `命名活动`, `语用实践场`, `不可消解之物`, `反体系`, `同一性原理`, `内在张力`, `语音`, `离散符号系统`, `无调性`, `具体普遍性`
- senses_created: 24
- total_w3_senses: 468
- total_w3_terms: 162
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B33-2026-06-09` → records=24, terms=12, quotes=48, errors=0, warnings=0
- status: draft only; W3 final target ≥500 senses / ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=468, terms=162, quotes=989, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 34
- batch_id: W3-B34-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `星座`, `名字`, `断裂的符号化`, `主客体`, `表征主义`, `先验语音论`, `声音`, `音乐`, `勋伯格`, `伪连续`, `局部断裂`, `总体连续`, `调性`, `难听`, `底层符号`, `被压抑`, `前符号化`, `不可还原性`, `不透明性`, `客体化运动`
- senses_created: 40
- total_w3_senses: 508
- total_w3_terms: 182
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B34-2026-06-09` → records=40, terms=20, quotes=80, errors=0, warnings=0
- status: draft only; W3 sense floor ≥500 reached, final target ≥200 terms still pending; no canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=508, terms=182, quotes=1069, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W3 Batch 35
- batch_id: W3-B35-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `本体论更新`, `高级学术话语`, `数学话语`, `数理逻辑`, `拓扑学`, `数论`, `离散数学`, `最小二乘法`, `超定`, `函数拟合`, `符号学工具`, `几何学配型`, `集合容器`, `不可数的多`, `真理显现方式`, `politics`, `amor`, `艺术`
- senses_created: 36
- total_w3_senses: 544
- total_w3_terms: 200
- outputs:
  - `knowledge/lexicon/term-senses.jsonl`
  - `knowledge/lexicon/core-terms.md`
  - `knowledge/lexicon/ambiguous-terms.md`
  - `knowledge/qa/w3-lexicon-audit.md`
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B35-2026-06-09` → records=36, terms=18, quotes=72, errors=0, warnings=0
- status: draft only; W3 quantitative floors ≥500 senses / ≥200 terms reached; W6 audit required before any canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

## W6 Audit — 2026-06-09
- batch_id: W6-AUDIT-2026-06-09
- completed_at: 2026-06-09 CST
- reports_created:
  - `knowledge/qa/validation-report.md`
  - `knowledge/qa/concept-drift-report.md`
  - `knowledge/qa/evidence-claim-audit.md`
  - `knowledge/qa/rejected-interpretations.md`
- audit_items:
  - sense mixing audit: PASS; 30-sense deterministic sample; no confidence downgrade required
  - relation strength audit: PASS; 20-relation deterministic sample; no confidence downgrade required
  - evidence-chain completeness: PASS; W3/W4/W5 machine gates passed
  - forbidden interpretation review: PASS over active surfaces; Atlas remains candidate-only
- status: no blocking issues; W3/W5 remain `draft`; no canonical promotion performed

## W7 Syntheses — 2026-06-09
- batch_id: W7-SYNTHESIS-2026-06-09
- completed_at: 2026-06-09 CST
- files_created:
  - `knowledge/syntheses/part-1-realism.md`
  - `knowledge/syntheses/part-2-metaphysics.md`
  - `knowledge/syntheses/part-3-idealism.md`
  - `knowledge/syntheses/part-4-praxis.md`
  - `knowledge/syntheses/whole-system-map.md`
  - `knowledge/syntheses/methodological-core.md`
- validation:
  - W7 tag check: all referenced W3 term IDs and W5 relation IDs exist; substantive bullet claims carry `[row ..., term:..., position ...]` source tags
  - forbidden-language scan: PASS
- status: W7 draft synthesis layer complete; W8 usage protocol pending

## W8 Usage Protocol — 2026-06-09
- batch_id: W8-USAGE-PROTOCOL-2026-06-09
- completed_at: 2026-06-09 CST
- files_created:
  - `knowledge/usage-protocol.md`
  - `knowledge/query-playbook.md`
  - `knowledge/export-manifest.md`
- validation:
  - forbidden-language scan over W8 files: PASS
  - Atlas/frontend/candidate-cache boundaries stated in protocol/export manifest
- status: W8 complete; W9 optional lightweight integration index or final completion audit pending

## W9 Integration Readiness — 2026-06-09
- batch_id: W9-INTEGRATION-READY-2026-06-09
- completed_at: 2026-06-09 CST
- repo_local_file:
  - `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
  - `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md`
  - `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`
  - `knowledge/scripts/check_w9_external_status.py`
  - `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
- intended_external_target: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- boundary: external target is not updated because MASTER-SPEC and AGENTS hard boundary prohibit writes outside `/home/weathour/文档/ismism-system`; read-only diff shows the existing external file differs from the repo-local protocol
- status: W9-ready inside repo; external replacement requires explicit human action or a future permission change

## MASTER-SPEC Final Completion Audit — 2026-06-09
- batch_id: MASTER-SPEC-FINAL-AUDIT-2026-06-09
- completed_at: 2026-06-09 CST
- audit_file: `knowledge/qa/master-spec-completion-audit.md`
- traceability_file: `knowledge/qa/master-spec-requirement-traceability.md`
- final_validation:
  - `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` → status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, w9_status_script=True, w9_decision_record=True, errors=0
  - `python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match` → currently expected FAIL because the external target is older and nonmatching
  - W3: records=544, terms=200, quotes=1141, errors=0, warnings=0
  - W4: PASS at 4/16/64/172
  - W5: records=60, quotes=70, types=12/12, errors=0, warnings=0
  - W6 reports: 4/4
  - W7 syntheses: 6/6; W7 tag check PASS
  - W8 docs: 3/3
  - W9 repo-local index: present; manual copy instructions present; `--require-external-w9` currently fails because the external target is older and nonmatching
  - forbidden-language scan over active knowledge surfaces: PASS
- verdict: in-repo deliverables complete and repo-local final validator PASS; repo-local W9 accepted as sufficient on 2026-06-10 CST, so the external W9 mismatch is downstream/manual and non-blocking

## W9 Maintainer Decision — 2026-06-10
- batch_id: W9-MAINTAINER-DECISION-2026-06-10
- completed_at: 2026-06-10 CST
- decision: Option A accepted — repo-local W9 package under `knowledge/integration/psychoanalytic-writing-lab/` satisfies W9 for this repository.
- decision_record: `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
- status: `ismism-system` repo-local completion no longer blocked by external W9 mismatch; no outside-repo write performed.


## W10 Further Absorption Pilot — 2026-06-15
- batch_id: W10-PILOT-B1-2026-06-15
- completed_at: 2026-06-15 CST
- status: pilot-draft additive layer; does not alter W1–W9 completion state.
- files_created:
  - `knowledge/w10-absorption/PLAN.md`
  - `knowledge/w10-absorption/index.md`
  - `knowledge/w10-absorption/argument-cards/w10-arg-0076-contemporary-naturalism.md`
  - `knowledge/w10-absorption/process-cards/w10-proc-0131-zhuangzi-eight-steps.md`
  - `knowledge/w10-absorption/case-cards/w10-case-0173-john-stuart-mill.md`
  - `knowledge/w10-absorption/case-cards/w10-case-0258-early-lacan-metaphoric-symbolism.md`
  - `knowledge/w10-absorption/process-cards/w10-proc-0363-ai-regeneration.md`
  - `knowledge/scripts/validate_w10_absorption.py`
  - `knowledge/qa/w10-pilot-audit.md`
  - `knowledge/qa/w10-ultraqa-report.md`
  - `knowledge/qa/absorption-strength-distribution.md`
- validation: see `knowledge/qa/w10-pilot-audit.md` and `knowledge/qa/w10-ultraqa-report.md`.
- next: expand W10 in small batches, prioritizing rows with high text volume and low W3/W5 coverage.

## Chinese Philosophy Maximum Absorption Program complete — 2026-06-15

- batch_id: CHINESE-PHILOSOPHY-MAX-2026-06-15
- status: complete as draft/pilot-draft additive theme layer after final validation.
- outputs: `knowledge/themes/chinese-philosophy/` manifest/evidence/taxonomy/README/syntheses/batch notes; Chinese W3 batch `W3-CHINESE-PHILOSOPHY-2026-06-15` (60 draft senses); Chinese W5 batch `W5-CHINESE-PHILOSOPHY-2026-06-15` (50 draft relations); 45 new W10 pilot-draft cards; validator/query helper; QA/audit reports.
- boundaries: no corpus rewrite; W3/W5 remain draft; W10 remains pilot-draft; Atlas not used as truth.


## Religion Problem Maximum Absorption Program complete — 2026-06-15

- status: complete as draft/pilot-draft additive theme layer.
- scope: Religion Problem / 宗教问题 across 80 rows; core rows 24–45 fully covered.
- artifacts: `knowledge/themes/religion/README.md`, `religion-row-manifest.jsonl`, `religion-evidence-bank.jsonl`, `religion-taxonomy.md`, `religion-synthesis.md`, `religious-realism-synthesis.md`, `sacred-ideology-and-practice-synthesis.md`, `religion-w3-w5-batch-notes.md`, completed handoff.
- W3/W5/W10: 64 Religion W3 draft senses (`W3-RELIGION-2026-06-15`), 51 Religion W5 draft relations (`W5-RELIGION-2026-06-15`), 45 Religion W10 pilot-draft cards.
- QA: `knowledge/qa/religion-absorption-audit.md`, `knowledge/qa/religion-evidence-claim-audit.md`, `knowledge/qa/religion-ultraqa-report.md`.
- boundary: Religion theme is an index/synthesis layer over corpus evidence, not a replacement for W1–W5 truth layers or an external religious-studies encyclopedia.
