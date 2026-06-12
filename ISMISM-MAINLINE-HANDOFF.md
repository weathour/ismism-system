# ISMISM 主线交接文档

- created: 2026-05-08
- repository: `/home/weathour/文档/ismism-system`
- current mainline: **ISMISM 理论知识库消化与关系资产建模**
- supersedes / removed:
  - 旧 clean corpus handoff 指针与 archive snapshot 已于 2026-06-12 删除
  - 旧前端/交互原型 README snapshot 与旧产品文档已于 2026-06-12 删除
  - retained tombstone: `docs/archive/legacy-process-and-prototype-index.md`

## 1. 当前主线判断

本仓库现在不再以“救活前端原型”或“继续清洗流水线”为主线。

当前主线是：

```text
PDF / TOC / split_md / split_md_clean
→ W1 corpus manifests
→ W2 segment cards
→ W3 term senses
→ W4 position cards
→ W5 relation assets
→ W7 syntheses / usage protocol
```

根本纪律：

1. 先固定证据层，再生成解释层。
2. 所有解释对象必须可追溯到 row / segment / quote。
3. W3/W5 当前全部保持 `draft`，不得直接提升为 canonical。
4. 旧前端、Atlas、早期 handoff 都只能作为候选/历史材料，不牵引当前主线。

## 2. 当前进度快照

以 `knowledge/STATE.md` 为准。当前状态：

- W1 corpus manifest：完成
- W2 segment cards：完成
- W3 term senses：完成 35 批，544 条 draft 义项 / 200 terms；MASTER-SPEC W3 quantitative floors reached；全部 draft，W6 audit 前不提升 canonical；新增证据校验脚本；四轴术语已拆分；W4/W5 最低前置已达成
- W5 relation assets：完成 Batch 1–5，60 条 draft relations；12/12 relation types covered；12/12 types have ≥2 examples；W5 quantitative gate reached；W6 relation-strength audit passed
- W4 position cards：L1 已完成 4/4 draft；L2 已完成 16/16 draft；L3 已完成 64/64 draft（`1-1-1`–`4-4-4` complete）；L4 已完成 current 172/172 draft light cards (target reached at `3-3-3-4`; W6 audit no blocking issue)
- W6 audit：完成 4/4 reports；no blocking issues；no confidence downgrades required
- W7 syntheses：完成 6/6 draft syntheses；source-tag check passed
- W8 usage protocol：完成 3/3 protocol docs
- W9 integration：repo-local lightweight index prepared and accepted as sufficient for this repository on 2026-06-10 CST; external target remains downstream/manual
- Final audit：`knowledge/qa/master-spec-completion-audit.md` + `knowledge/qa/master-spec-requirement-traceability.md`; repo-local deliverables complete

关键计数：

| Layer | Done | Notes |
|---|---:|---|
| TOC / segments | 363 | row 176 已恢复 |
| chunks | 1594 | 用于检索 |
| segment cards | 363 | 覆盖 row 1–363 |
| term senses | 544 | 全部 draft；MASTER-SPEC W3 quantitative floors reached；W6 audit no blocking issue |
| relation assets | 60 | W5-B1–B5 draft; W5 quantitative gate reached; W6 audit no blocking issue |
| position cards | 256 | W4-L1 draft complete; W4-L2 (`1-1`–`4-4`) draft complete; W4-L3 64/64 (`1-1-1`–`4-4-4`) draft; W4-L4 current 172/172 draft |
| W6 audit reports | 4 | validation / concept drift / evidence-claim / rejected interpretations complete; no blocking issue |
| syntheses | 6 | W7 draft syntheses complete |
| usage protocol | 3 | W8 complete: usage protocol / query playbook / export manifest |
| W9 integration index | 1 | repo-local draft prepared and accepted as sufficient for this repository |
| W9 external status audit | 1 | repo-local audit records hashes and mismatch without outside write |
| W9 external status checker | 1 | repo-local read-only checker for current external match state |
| W9 maintainer decision record | 1 | Option A accepted: repo-local W9 is sufficient for `ismism-system` |
| final completion audit | 2 | completion audit + requirement traceability matrix; repo-local completion accepted |

## 3. 当前核心产物

### Live state / 日志

- `knowledge/STATE.md`
- `knowledge/logs/operation-log.md`
- `knowledge/DIGESTION_PROGRAM.md`

### W1：结构清单

- `knowledge/manifests/corpus-manifest.json`
- `knowledge/manifests/segments.jsonl`
- `knowledge/manifests/chunks.jsonl`
- `knowledge/manifests/missing-and-anomalies.md`
- `knowledge/qa/w1-recovery-audit.md`

### W2：分段卡

- `knowledge/segment-cards/index.md`
- `knowledge/segment-cards/*.md`

### W3：术语义项

- `knowledge/lexicon/term-senses.jsonl`
- `knowledge/lexicon/core-terms.md`
- `knowledge/lexicon/ambiguous-terms.md`
- `knowledge/qa/w3-lexicon-audit.md`

当前已处理术语：

- `主体`
- `客体`
- `实践`
- `历史`
- `人民`
- `理论`
- `主体化`
- `客体化`
- `去主体化`
- `实体`
- `物质`
- `意识形态`
- `本体论`
- `认识论`
- `目的论`
- `场域论`
- `符号`
- `符号秩序`
- `中介`
- `理论家`
- `实践单元`
- `闭合`
- `有限性`
- `误认`
- `跃迁`
- `辩证法`
- `欲望`
- `他者`
- `意识`
- `驱力`
- `语言`
- `去客体化`
- `时间化`
- `空间化`
- `对象化`
- `符号化`
- `现象化`
- `去符号化`
- `去现象化`
- `本体论化`
- `去本体论化`
- `实体化`
- `去实体化`
- `表象化`
- `去表象化`
- `二元化`
- `历史化`
- `去历史化`
- `中心化`
- `去中心化`
- `重新中心化`
- `符号学`
- `结构主义`
- `能指`
- `所指`
- `差异`
- `本质`
- `存在`
- `哲学化`
- `辩证法化`
- `认识论化`
- `目的论化`
- `去目的论化`
- `本体化`
- `去辩证化`
- `教科书化`
- `爱欲`
- `力比多`
- `享乐`
- `献祭`
- `科学化`
- `体系化`
- `实证化`
- `共同体`
- `主体间性`
- `生活世界`
- `事件性`
- `平等主义`


### W5：关系资产

- `knowledge/relations/relation-assets.jsonl`
- `knowledge/relations/relation-prompts.md`
- `knowledge/relations/route-cards.md`
- `knowledge/relations/tension-cards.md`
- `knowledge/relations/mediation-cards.md`
- `knowledge/relations/boundary-cards.md`
- `knowledge/relations/misrecognition-cards.md`
- `knowledge/qa/w5-relation-audit.md`

首批关系族：

1. `去主体化 → 客体化 → 客体/实践`
2. `理论 → 客体化/主体化`
3. `主体化 / 客体化 / 去主体化` 张力
4. `历史 / 人民 / 理论` 三元中介
5. `主体 → 实践单元`
6. 机制词与名词义项的边界

## 4. 恢复工作时的阅读顺序

新 agent / 新上下文必须先读：

1. `ISMISM-MAINLINE-HANDOFF.md`
2. `knowledge/STATE.md`
3. `knowledge/DIGESTION_PROGRAM.md`
4. `knowledge/references/movement-patterns-guide.md` — 矩阵运动模式分类学与阅读协议
5. `knowledge/logs/operation-log.md`
6. `knowledge/qa/w5-relation-audit.md`
7. `knowledge/lexicon/term-senses.jsonl`
8. `knowledge/relations/relation-assets.jsonl`

只在需要查证时再读：

- `knowledge/segment-cards/*.md`
- `split_md_clean/...`
- `split_md/...`
- 原 PDF

## 5. 旧内容与归档边界

以下内容已经归入历史/候选/派生层，不再作为当前主线推进目标。

### 已删除的旧 clean corpus / 前端产品路线

- 删除时间：2026-06-12 CST
- tombstone: `docs/archive/legacy-process-and-prototype-index.md`
- removed: `ISMISM-CLEANUP-HANDOFF.md`
- removed: old clean-corpus archive snapshot and old frontend README snapshot
- removed: `src/`, `dist/`, `index.html`, `package.json`, `package-lock.json`, `vite.config.*`, `tsconfig*`, `node_modules/`
- removed: `docs/00-*` through `docs/16-*` old product/frontend design documents

处理规则：

- 不继续按旧路线救前端。
- 若未来需要交互界面，必须从 `knowledge/` 处理层重新定义接口，而不是恢复旧 `src/`。
- 删除不影响 PDF/TOC/split/knowledge 主线。

### Atlas / Zhuyi Matrix Engine

- `Zhuyi_Matrix_Engine/`
- `Zhuyi_Matrix_Engine/Atlas_DB/*`

处理规则：

- 仅作为候选层、方法提示、关系种子。
- 不能替代 `split_md_clean`、segment cards、term senses 的证据链。

### 派生层 / 可再生层

- retained: `split_pdf/` — row 176 PDF slice only; regenerable derived layer.
- removed: `graphify-out/`, `dist/`, `node_modules/`, `__pycache__/` — rebuildable/cache outputs removed in the 2026-06-12 cleanup.

处理规则：

- 不作为理论真相层。
- 如未来需要浏览/构建缓存，必须从当前 `knowledge/` 契约重新生成，不恢复旧前端路线。

## 6. 历史下一步建议（已过时，保留为批处理记录）

> 当前 next action 以 `knowledge/STATE.md` 为准；本节以下内容是旧批处理阶段记录，不再作为恢复指令。

优先级 A：继续 W3 第一期频率驱动扩展

- 当前 W3=300 条，已满足 W4 前置 ≥100 条，并已达到 MASTER-SPEC 第一期 ≥300 sense count gate；但最终 ≥500 senses / ≥200 terms 仍未满足。
- W4-L2 已完成；W3 继续向 ≥300 条推进。
- 每批运行：`python3 knowledge/scripts/validate_w3_term_senses.py --repo .`。

优先级 B：继续 W4 position cards

- level-1：4 张已完成 draft
- level-2：已完成 16/16（`1-1`–`4-4`）
- level-3：已完成 64/64（`1-1-1`–`4-4-4` draft complete）；level-4：已完成 current 172/172 draft（target reached at `3-3-3-4`）；下一步建议继续 W3 toward ≥300、W5 toward 60+，并准备 W6 audit
- 并行优先：继续 W3 扩展至 ≥300 senses
- 目标：校正 W3/W5 的位置归属和方向边。

优先级 C：准备 W7 synthesis

- 等 W4/W5 稳定后再做。
- 不要现在直接写总论。

## 7. 禁止事项

- 不要继续旧前端救援线。
- 不要把 Atlas_DB 当 canonical。
- 不要把 W3/W5 draft 义项或关系升 canonical。
- 不要处理 RMH/GJW。
- 不要把 `split_md_clean/` 当最终理论知识库；它只是证据层。
- 不要大范围重写原始语料。

## 8. 一句话交接

如果只保留一句话：

> 本仓库现在的主线是把 ISMISM 作为可追溯理论知识库来消化：W1/W2 已完成，W3 已完成 26 批 300 条 draft senses（phase-1 ≥300 count gate reached），W4 已完成 L1、L2、L3 64/64 与 current L4 172/172（全部 draft，target reached at `3-3-3-4`），W5 已完成 B1+B2 共 26 条关系；旧清洗过程与前端原型均已归档为历史材料，下一步继续 W3 扩展、W5 relation assets，并准备 W6 audit。


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
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
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
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
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
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
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
- note: B1 records were backfilled with `source_position`, `target_position`, and `evidence_segment`; W5 target ≥60 remains pending; all draft.
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=26, quotes=34, types=12/12, errors=0, warnings=0
  - final W5 gate remains pending: needs ≥60 relations and `subjectivizes` second example.
- new validator: `knowledge/scripts/validate_w5_relation_assets.py` checks relation fields, W4 position-card existence, controlled relation types, W3 term-sense refs, and exact W1 clean-text quote substrings.

## W5 Batch 3
- batch_id: W5-B3-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 14
- total_relation_records: 40
- relation_types_covered: 12/12
- relation_types_with_2plus_examples: 12/12
- note: B3 added subjectivization/objectification/event-gap mechanisms and brought `subjectivizes` above the two-example gate; W5 target ≥60 remains pending; all draft.
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=40, quotes=49, types=12/12, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B3-2026-06-08` → records=14, quotes=15, errors=0, warnings=0
  - final W5 gate remains pending: needs +20 relations to reach ≥60.

## W5 Batch 4
- batch_id: W5-B4-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 10
- total_relation_records: 50
- note: expanded theory/practice, dialecticization, textbookification, symbolic economy, objectification relations; all draft.
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B4-2026-06-08` → records=10, quotes=11, errors=0, warnings=0

## W5 Batch 5
- batch_id: W5-B5-2026-06-08
- completed_at: 2026-06-08 CST
- relation_records_added: 10
- total_relation_records: 60
- relation_types_covered: 12/12
- relation_types_with_2plus_examples: 12/12
- note: W5 quantitative gate reached; all W5 remains draft; W6 audit required before any canonical promotion.
- validation:
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo .` → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B5-2026-06-08` → records=10, quotes=10, errors=0, warnings=0
  - `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` → PASS

## W3 Batch 27
- batch_id: W3-B27-2026-06-09
- completed_at: 2026-06-09 CST
- terms_processed: `学习`, `研究`, `现实`, `通俗化`, `交谈`, `灌输`, `宣传`, `行动`, `信仰`, `忠诚`, `范式`, `知识`
- senses_created: 24
- total_w3_senses: 324
- total_w3_terms: 90
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
- validation:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B35-2026-06-09` → records=36, terms=18, quotes=72, errors=0, warnings=0
- status: draft only; W3 quantitative floors ≥500 senses / ≥200 terms reached; W6 audit required before any canonical promotion
- validation-finalized:
  - `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=544, terms=200, quotes=1141, errors=0, warnings=0
  - W4 L1/L2/L3/L4 validations → PASS at 4/16/64/172
  - W5 final gate validation → records=60, quotes=70, types=12/12, errors=0, warnings=0
  - `git diff --check` → PASS
  - forbidden-language scan over active knowledge surfaces → PASS

### W6：审计报告

- `knowledge/qa/validation-report.md`
- `knowledge/qa/concept-drift-report.md`
- `knowledge/qa/evidence-claim-audit.md`
- `knowledge/qa/rejected-interpretations.md`

## W6 Audit — 2026-06-09
- batch_id: W6-AUDIT-2026-06-09
- completed_at: 2026-06-09 CST
- reports_created: `validation-report.md`, `concept-drift-report.md`, `evidence-claim-audit.md`, `rejected-interpretations.md`
- verdict: no blocking issues; no confidence downgrades required; W3/W5 remain draft; no canonical promotion performed
- next: W7 syntheses (4 field syntheses + whole-system-map + methodological-core)

### W7：综合层

- `knowledge/syntheses/part-1-realism.md`
- `knowledge/syntheses/part-2-metaphysics.md`
- `knowledge/syntheses/part-3-idealism.md`
- `knowledge/syntheses/part-4-praxis.md`
- `knowledge/syntheses/whole-system-map.md`
- `knowledge/syntheses/methodological-core.md`

## W7 Syntheses — 2026-06-09
- batch_id: W7-SYNTHESIS-2026-06-09
- completed_at: 2026-06-09 CST
- files_created: 6/6 required syntheses under `knowledge/syntheses/`
- validation: referenced W3 term IDs and W5 relation IDs exist; substantive bullet claims source-tagged; forbidden scan passed
- next: W8 usage protocol (`usage-protocol.md`, `query-playbook.md`, `export-manifest.md`)

### W8：使用协议

- `knowledge/usage-protocol.md`
- `knowledge/query-playbook.md`
- `knowledge/export-manifest.md`

## W8 Usage Protocol — 2026-06-09
- batch_id: W8-USAGE-PROTOCOL-2026-06-09
- completed_at: 2026-06-09 CST
- files_created: `knowledge/usage-protocol.md`, `knowledge/query-playbook.md`, `knowledge/export-manifest.md`
- validation: forbidden scan passed; source-layer and export boundaries recorded
- next: W9 optional lightweight integration index or MASTER-SPEC final completion audit

### W9：轻量接入索引（repo-local）

- `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
- `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`
- `knowledge/scripts/check_w9_external_status.py`
- `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
- intended external target: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- note: read-only check shows the external target exists as an older placeholder but differs from the repo-local protocol; current repo rules forbid updating outside `ismism-system`; this is downstream/manual after repo-local W9 acceptance

## W9 Integration Readiness — 2026-06-09
- batch_id: W9-INTEGRATION-READY-2026-06-09
- completed_at: 2026-06-09 CST
- repo_local_file: `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
- manual_copy_instructions: `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md`
- external_status_audit: `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`
- external_status_checker: `knowledge/scripts/check_w9_external_status.py`
- maintainer_decision_record: `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
- intended_external_target: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- boundary: external target is not updated because repository rules forbid writes outside `ismism-system`; read-only diff shows the current external file differs from the repo-local protocol
- next: repo-local completion is accepted; external copy remains optional/downstream unless separately authorized

## MASTER-SPEC Final Completion Audit — 2026-06-09
- batch_id: MASTER-SPEC-FINAL-AUDIT-2026-06-09
- completed_at: 2026-06-09 CST
- audit_file: `knowledge/qa/master-spec-completion-audit.md`
- validation: `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` PASS; W3/W4/W5 gates PASS; W6 4/4 reports; W7 6/6 syntheses; W8 3/3 docs; W9 repo-local index present; forbidden active-surface scan PASS
- completion note: repo-local W9 was accepted as sufficient on 2026-06-10 CST; external W9 target remains older/nonmatching but is now a downstream manual integration issue, not a blocker for `ismism-system`

## W9 Maintainer Decision — 2026-06-10
- decision: Option A accepted — repo-local W9 under `knowledge/integration/psychoanalytic-writing-lab/` satisfies W9 for this repository.
- decision_record: `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
- boundary: no outside-repo write was performed; the external target mismatch remains documented in `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`.
