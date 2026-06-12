# W3 Lexicon Audit — Batch 1

- batch_id: `W3-B1-2026-05-08`
- audited_at: 2026-05-08 18:47 CST
- objective: 启动 W3 术语义项 registry，并完成第一批 `主体`、`客体`、`实践` draft 义项。

## 1. W2 Gate Audit

- segment cards found: 363 / 363
- card row range: 1–363
- missing card rows: none
- duplicate card rows: none
- index rows parsed: 363 / 363
- index row range: 1–363
- missing index rows: none
- duplicate index rows: 0
- verdict: PASS — W2 coverage is sufficient to enter W3.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | created | 13 JSONL records, all status=draft |
| `knowledge/lexicon/core-terms.md` | created | human-readable index for 3 terms |
| `knowledge/lexicon/ambiguous-terms.md` | created | open ambiguity notes for 主体/客体/实践 |
| `knowledge/lexicon/term-candidate-stats.tsv` | created | candidate count table for W3 focus terms |
| `knowledge/qa/w3-lexicon-audit.md` | created | this audit |

## 3. JSONL Validation

- records: 13
- terms: 主体, 客体, 实践
- required fields checked: sense_id, term, sense_label, definition, axis, source_segments, evidence_quotes, position_context, contrast_with, forbidden_mix, confidence, status, audit_notes.
- status check: all first-batch records are `draft`; no canonical claims emitted.
- evidence quote validation: PASS — every `evidence_quotes[].quote` is an exact substring of its referenced segment card or clean markdown after whitespace normalization.

## 4. Evidence Coverage

### 主体
- `term:主体:s01` (矩阵中的主体侧维度): rows 46 `1-3`; quotes=2; confidence=high
- `term:主体:s02` (先验/反思主体性): rows 176 `2-4-2-4`, 188 `3-1`, 193 `3-1-1-3`; quotes=3; confidence=medium
- `term:主体:s03` (主体间性/人称化机制): rows 200 `3-1-3`, 201 `3-1-3-1`; quotes=3; confidence=high
- `term:主体:s04` (无意识/驱力主体与去主体化): rows 262 `3-4-2-1`, 276 `4`; quotes=4; confidence=high

### 客体
- `term:客体:s01` (矩阵中的客体/实体侧维度): rows 46 `1-3`; quotes=2; confidence=high
- `term:客体:s02` (意向对象/noema 的客体极): rows 188 `3-1`, 217 `3-2-2`; quotes=3; confidence=high
- `term:客体:s03` (小客体/客体小a): rows 46 `1-3`; quotes=3; confidence=medium
- `term:客体:s04` (异化/物神化中的对象化客体): rows 276 `4`, 344 `4-4-1`; quotes=4; confidence=high

### 实践
- `term:实践:s01` (目的论中的行动/伦理姿态): rows 46 `1-3`, 51 `1-3-1-4`; quotes=3; confidence=high
- `term:实践:s02` (第四主部的历史-政治实践场): rows 276 `4`; quotes=3; confidence=high
- `term:实践:s03` (人与物关系中的实践性): rows 322 `4-3-1`; quotes=3; confidence=high
- `term:实践:s04` (实践单元/可执行载体): rows 339 `4-3-4-2`, 352 `4-4-2-3`, 359 `4-4-4`; quotes=3; confidence=medium
- `term:实践:s05` (运动式主动活动/避免异化): rows 335 `4-3-3-3`; quotes=3; confidence=medium

## 5. Weak / Uncovered Requirements

- No W3 sense is canonical yet; all require human/theory review before downstream synthesis.
- `主体化`、`客体化`、`去主体化` are noted but not completed as separate terms in this batch.
- `实践单元` is represented as a `实践` sub-sense; whether it deserves an independent term remains open.
- Atlas_DB and old frontend assets were not used as evidence.

## 6. Next Batch

Recommended W3-B2: either `历史`、`人民`、`理论` or mechanism batch `主体化`、`客体化`、`去主体化`.

---

# W3 Lexicon Audit — Batch 2

- batch_id: `W3-B2-2026-05-08`
- audited_at: 2026-05-08 19:05 CST
- objective: 处理历史（history）在第二批中的首要义项，更新 W3 registry 的人类可读层与歧义注记。

## 1. W2 Gate Audit

- segment cards found: 363 / 363
- card row range: 1–363
- missing card rows: none
- duplicate card rows: none
- index rows parsed: 363 / 363
- index row range: 1–363
- missing index rows: none
- duplicate index rows: 0
- verdict: PASS — W2 coverage continues to support W3 second-batch work.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 18 JSONL records total, +5 `历史` entries this batch |
| `knowledge/lexicon/core-terms.md` | updated | added `历史` section with 5 draft senses |
| `knowledge/lexicon/ambiguous-terms.md` | updated | added `历史`高歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | this batch extension |

## 3. Evidence Coverage

- `term:历史:s01`（时间性历史范式/物质史）: row 276 `4`; 3 quotes; confidence=high
- `term:历史:s02`（4段位中的中介候选项）: rows 276 `4`, 299 `4-2`, 315 `4-2-3-4`; 3 quotes; confidence=high
- `term:历史:s03`（历史的哲学化/辩证法化）: row 289 `4-1-3`; 3 quotes; confidence=high
- `term:历史:s04`（史学研究实践）: row 279 `4-1-1`; 3 quotes; confidence=high
- `term:历史:s05`（历史的自我妥协与现实化）: row 315 `4-2-3-4`; 3 quotes; confidence=medium

## 4. Additional Notes

- `历史`当前未与`人民`/`理论`批次合并归一，后续需在下一批补齐跨术语对齐关系（中介链条、历史客体/理论家定位）。
- 所有新增历史义项仍为 `draft`；暂不提升为 `canonical`。
- Atlas_DB 与旧前端产物未被用于新增证据。

---

# W3 Lexicon Audit — Batch 3

- batch_id: `W3-B3-2026-05-08`
- audited_at: 2026-05-08 19:18 CST
- objective: 处理 `人民`（人民/s01-s05）义项，更新 W3 registry 的可读与歧义记录。

## 1. W2 Gate Audit

- segment cards found: 363 / 363
- card row range: 1–363
- missing card rows: none
- duplicate card rows: none
- index rows parsed: 363 / 363
- index row range: 1–363
- missing index rows: none
- duplicate index rows: 0
- verdict: PASS — W2 coverage仍支持继续开展 W3。

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 23 JSONL records；新增 5 条 `term:人民` draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 `人民` section（5 条 draft） |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 `人民`歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `term:人民:s01`（人民性/复数化）: row 276 `4`; 2 quotes; confidence=high
- `term:人民:s02`（人民中介位）: rows 276 `4`; 299 `4-2`; 3 quotes; confidence=high
- `term:人民:s03`（人民理论化）: row 284 `4-1-2`; 3 quotes; confidence=high
- `term:人民:s04`（天然理论家）: row 298 `4-1-4-4`; 3 quotes; confidence=medium
- `term:人民:s05`（可数单元性）: row 288 `4-1-2-4`; 3 quotes; confidence=high

## 4. Additional Notes

- `人民`批次新增义项与 `历史`、`理论` 以及 `实践单元` 在链条语义上高耦合，建议后续在 `理论`批次中保持交叉审校。
- 人民相关证据均为 row 粗定位+clean-md 原文可追溯子串。
- 所有新增记录仍为 `draft`；未进行 canonical 认证。
- Atlas_DB 和旧前端资源未引入新证据。


# W3 Lexicon Audit — Batch 4

- batch_id: `W3-B4-2026-05-08`
- audited_at: 2026-05-08 19:30 CST
- objective: 处理 `理论`（理论/s01-s05）并更新 W3 人类可读/歧义层。

## 1. W2 Gate Audit

- segment cards found: 363 / 363
- card row range: 1–363
- missing card rows: none
- duplicate card rows: none
- index rows parsed: 363 / 363
- index row range: 1–363
- missing index rows: none
- duplicate index rows: 0
- verdict: PASS — W2 coverage仍支持继续开展 W3。

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 28 JSONL records total，新增 5 条 `理论` draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 `理论` section（5 条） |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 `理论`歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `term:理论:s01`（中介项）: row 276 `4`; 3 quotes; confidence=high
- `term:理论:s02`（符号系统性与历史性）: row 276 `4`; 3 quotes; confidence=high
- `term:理论:s03`（生产性：生产主体、客体与客体化）: row 276 `4`; 3 quotes; confidence=high
- `term:理论:s04`（理论与现实对象化—主体化回路）: row 285 `4-1-2-1`; 3 quotes; confidence=high
- `term:理论:s05`（理论的现实化/通俗化）: row 285 `4-1-2-1`; 3 quotes; confidence=high

## 4. Additional Notes

- `理论`与 `历史`、`人民` 在中介位上高度耦合；在 W5 relation 资产中建议继续对齐：
  - `理论:s01` 与 `人民:s02` / `历史:s02` 的位序映射；
  - `理论:s03` 与 `客体化`、`主体化` 机制词拆分关系映射。
- 所有新增记录仍为 `draft`；尚未 canonical。
- Atlas_DB 与旧前端未作为新增证据来源；仍采用 W1 manifests + W2 segment cards + split_md_clean 原文。


# W3 Lexicon Audit — Batch 5

- batch_id: `W3-B5-2026-05-08`
- audited_at: 2026-05-08 20:40 CST
- objective: 处理机制词 `主体化`、`客体化`、`去主体化`，并补齐与 `理论/历史/人民/实践` 的关系草图输入。

## 1. W2 Gate Audit

- segment cards found: 363 / 363
- card row range: 1–363
- missing card rows: none
- duplicate card rows: none
- index rows parsed: 363 / 363
- index row range: 1–363
- missing index rows: none
- duplicate index rows: 0
- verdict: PASS — W2 coverage supports W3 扩展批次。

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 31 records total，新增3条机制词 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 机制词 subsection 已保持 draft |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 机制词高歧义说明已存在，待转入 W5 关系资产 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计段目 |

## 3. Evidence Coverage

- `term:主体化:s01`（实体/关系的主体化）: row 139 `2-2-4`，row 276 `4`；quotes=3（其中含“外在维度->主体化”和“实体本身在进行主体化和去主体化”）。
- `term:客体化:s01`（对象化/外在化）: row 139 `2-2-4`，row 276 `4`；quotes=3（“外在维度…客体化”、齐泽克处“过程就是客体化、变成客体”、以及“去主体化也可以说是变成客体”）。
- `term:去主体化:s01`（desubjectivation）: rows 276 `4`，139 `2-2-4`，131 `2-2-2-2`；quotes=3（“去主体化实际上就是…过程”、可“变成客体”、庄子“第七步骤他就去主体化”）。

## 4. Additional Notes

- 机制词的“方向性”还未形成正式关系图，但已具备用于 W5 的对齐材料：`客体化/主体化`形成可逆候选；`去主体化`可与`主体`/`客体`/`理论生产`形成三类路径。
- 所有新增机制词记录保留 `draft`，未作 canonical 升级。

---

# W3 Lexicon Audit — Batch 6

- batch_id: `W3-B6-2026-06-03`
- audited_at: 2026-06-03 19:25 CST
- objective: 按 MASTER-SPEC 第一期频率驱动路线，处理 `实体`、`物质`、`意识形态`，并新增 W3 证据校验脚本。

## 1. W2 Gate Audit

- segment cards found: 363+index file（row 1–363 仍由 W2 index 覆盖；本批未改动 W2）
- source layer used: `knowledge/manifests/segments.jsonl` + `split_md_clean/` + W2 segment-card paths
- verdict: PASS — W2 coverage supports W3-B6 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/scripts/validate_w3_term_senses.py` | added | validates JSONL schema basics, draft status, source paths, and quote substring matches |
| `knowledge/lexicon/term-senses.jsonl` | appended + corrected | 45 records total;新增 14 条 draft 义项；同时修正 `历史` 8 条非逐字 evidence_quote |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B6 section（实体5、物质4、意识形态5） |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增三词高歧义与 open review items |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `实体`: 5 senses; rows 46, 146, 149, 214, 135; quotes=10; all draft.
- `物质`: 4 senses; rows 276, 280, 170, 168, 298; quotes=9; all draft.
- `意识形态`: 5 senses; rows 295, 231, 54, 291, 185, 166; quotes=10; all draft.

## 4. Validation

Commands run:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B6-2026-06-03
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 validation: records=14, terms=3, quotes=29, errors=0, warnings=0
W3 validation: records=45, terms=12, quotes=121, errors=0, warnings=0
```

## 5. Additional Notes

- 本批 candidate-only 文件只作为线索；正式证据均经 `split_md_clean/` 子串验证。
- `历史`旧批次中 8 条 evidence_quote 不满足严格逐字子串匹配，本批已修正为原文连续子串；未改动对应 definition/status。
- 所有 W3 义项仍为 `draft`；未进行 canonical 提升。
- 下一批建议继续 MASTER-SPEC 频率驱动：`符号`、`符号秩序`、`本体论/认识论/目的论`；同时保持每两批更新一次歧义记录。

---

# W3 Lexicon Audit — Batch 7

- batch_id: `W3-B7-2026-06-03`
- audited_at: 2026-06-03 19:45 CST
- objective: 处理 MASTER-SPEC 第一期 C 类轴术语中的 `本体论`、`认识论`、`目的论`，为 W4 位置卡前置条件补齐轴名义项。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B7 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 57 records total;新增 12 条轴术语 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B7 轴术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增轴术语高歧义与 open review items |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `本体论`: 4 senses; rows 46, 271, 267, 263; quotes=9; all draft.
- `认识论`: 4 senses; rows 46, 63, 285, 9; quotes=10; all draft.
- `目的论`: 4 senses; rows 46, 106, 95; quotes=8; all draft.

## 4. Validation

Command run:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B7-2026-06-03
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 validation: records=12, terms=3, quotes=27, errors=0, warnings=0
W3 validation: records=57, terms=15, quotes=148, errors=0, warnings=0
```

## 5. Additional Notes

- `场域论` 仍待下一批拆分；W4 前置的四轴术语尚未完全满足。
- 本批未使用 Atlas_DB 作为正式证据；仍全部依据 clean text 逐字子串。
- 所有新增记录保持 `draft`，未进行 canonical 提升。

---

# W3 Lexicon Audit — Batch 8

- batch_id: `W3-B8-2026-06-03`
- audited_at: 2026-06-03 20:20 CST
- objective: 补齐四轴术语 `场域论`，并处理高频符号簇 `符号`、`符号秩序`，继续推进 MASTER-SPEC 第一期 W3 扩展。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B8 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 70 records total; 新增 13 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B8 术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增符号簇与场域论歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `场域论`: 4 senses; rows 46, 1, 96, 127; quotes=9; all draft.
- `符号`: 5 senses; rows 1, 216, 254, 185, 108; quotes=10; all draft.
- `符号秩序`: 4 senses; rows 96, 108, 268, 127; quotes=8; all draft.

## 4. Validation

Command run:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B8-2026-06-03
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 validation: records=13, terms=3, quotes=27, errors=0, warnings=0
W3 validation: records=70, terms=18, quotes=175, errors=0, warnings=0
```

## 5. Additional Notes

- 四轴名（场域论/本体论/认识论/目的论）已具备 draft 义项，可作为 W4 前置材料的一部分。
- W3 仍未达到 W4 前置建议的 ≥100 条 sense，也远未达到 MASTER-SPEC 第一期 ≥300 条 sense；下一批仍应继续 W3。
- 所有新增记录保持 `draft`，未进行 canonical 提升；candidate-only 文件仅作线索。

---

# W3 Lexicon Audit — Batch 9

- batch_id: `W3-B9-2026-06-03`
- audited_at: 2026-06-03 21:05 CST
- objective: 处理与 W5/W4 前置强相关的 `中介`、`理论家`、`实践单元`。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B9 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 新增 13 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B9 术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增中介/理论家/实践单元歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `中介`: 5 senses; rows 240, 245, 236, 246, 276, 232; quotes=10; all draft.
- `理论家`: 4 senses; rows 277, 284, 289, 283; quotes=8; all draft.
- `实践单元`: 4 senses; rows 276, 290, 285; quotes=8; all draft.

## 4. Validation

```text
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B9-2026-06-03
→ records=13, terms=3, quotes=26, errors=0, warnings=0
```

## 5. Additional Notes

- 本批补齐了多个已被 W5 关系资产引用、但此前尚未正式拆分的术语。
- 所有新增记录保持 `draft`，未进行 canonical 提升。

---

# W3 Lexicon Audit — Batch 10

- batch_id: `W3-B10-2026-06-03`
- audited_at: 2026-06-03 21:05 CST
- objective: 处理 W5 relation family 高相关的 `闭合`、`有限性`、`误认`、`跃迁`，并使 W3 达到 W4 前置建议的 ≥100 条 sense。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B10 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 100 records total; 新增 17 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B10 术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增闭合/有限性/误认/跃迁歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `闭合`: 5 senses; rows 185, 155, 228, 125, 103; quotes=10; all draft.
- `有限性`: 5 senses; rows 216, 155, 246, 244, 247; quotes=10; all draft.
- `误认`: 4 senses; rows 258, 261, 249; quotes=8; all draft.
- `跃迁`: 3 senses; rows 123, 122; quotes=6; all draft.

## 4. Validation

```text
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B10-2026-06-03
→ records=17, terms=4, quotes=34, errors=0, warnings=0

python3 knowledge/scripts/validate_w3_term_senses.py --repo .
→ records=100, terms=25, quotes=235, errors=0, warnings=0
```

## 5. Additional Notes

- W3 已达到 100 条 draft sense，满足 W4 position cards 的最低前置建议（W3 ≥100 且四轴术语已拆分）。
- 仍未达到 MASTER-SPEC 第一期合格门槛（≥300 条 sense）和最终 W3 硬指标（≥200 术语 / ≥500 sense）；后续应 W4 与 W3 扩展配合推进。
- 所有新增记录保持 `draft`，未进行 canonical 提升。

---

# W3 Lexicon Audit — Batch 11

- batch_id: `W3-B11-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC W3 扩展，处理高频/共现术语 `辩证法`、`欲望`、`他者`，补足 W4/W5 后续会频繁引用但此前尚未收录的 term-sense。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B11 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 112 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B11 术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增辩证法/欲望/他者歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `辩证法`: 4 senses; rows 184, 229, 289, 237; quotes=8; all draft.
- `欲望`: 4 senses; rows 94, 111, 262, 245; quotes=8; all draft.
- `他者`: 4 senses; rows 45, 171, 204, 209, 258; quotes=8; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B11-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 batch validation: records=12, terms=3, quotes=24, errors=0, warnings=0
W3 full validation: records=112, terms=28, quotes=259, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- W3 仍未达到 MASTER-SPEC 第一期 ≥300 sense 或最终 ≥500 sense；后续应继续 W3 扩展。

---

# W3 Lexicon Audit — Batch 12

- batch_id: `W3-B12-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC W3 扩展，处理高频/共现术语 `意识`、`驱力`、`语言`，并把此前已被 W4/W5 多次引用但尚未收录的基础结构词纳入 draft term-sense 层。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B12 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 124 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B12 术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增意识/驱力/语言歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `意识`: 4 senses; rows 40, 18, 62, 187; quotes=9; all draft.
- `驱力`: 4 senses; rows 111, 94, 40, 262; quotes=8; all draft.
- `语言`: 4 senses; rows 40, 185, 254, 274; quotes=10; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B12-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 batch validation: records=12, terms=3, quotes=27, errors=0, warnings=0
W3 full validation: records=124, terms=31, quotes=286, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- W3 仍未达到 MASTER-SPEC 第一期 ≥300 sense 或最终 ≥500 sense；后续应继续 W3 扩展，并与 W5 relation assets 并行推进。

---

# W3 Lexicon Audit — Batch 13

- batch_id: `W3-B13-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 执行 MASTER-SPEC 第一期 D 项“机制词补全”，围绕 row 139 `2-2-4` 的四运动矩阵补入 `去客体化`，并把既有单义项术语 `主体化`、`客体化` 扩展到 5 个 draft senses。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B13 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 136 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B13 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增主体化/客体化/去客体化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `主体化`: appended 4 senses; rows 263, 289, 230, 362; quotes=12; all draft.
- `客体化`: appended 4 senses; rows 289, 139, 284, 285; quotes=12; all draft.
- `去客体化`: created 4 senses; row 139; quotes=11; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B13-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 batch validation: records=12, terms=3, quotes=35, errors=0, warnings=0
W3 full validation: records=136, terms=32, quotes=321, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- row 139 四基本运动目前已覆盖：`主体化`、`客体化`、`去主体化`、`去客体化`。其中 `去主体化` 仍需下一批继续扩义。

---

# W3 Lexicon Audit — Batch 14

- batch_id: `W3-B14-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词补全”，把 row 139 四运动簇中的 `去主体化` 补足到 5 个义项，并新增 `时间化`、`空间化` 两个机制词。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B14 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 148 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B14 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增去主体化/时间化/空间化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `去主体化`: appended 4 senses; rows 139, 206, 140, 275; quotes=9; all draft.
- `时间化`: created 4 senses; rows 139, 123, 121, 208; quotes=10; all draft.
- `空间化`: created 4 senses; rows 139, 97, 127, 130; quotes=8; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B14-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 batch validation: records=12, terms=3, quotes=27, errors=0, warnings=0
W3 full validation: records=148, terms=34, quotes=348, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- row 139 四基本运动目前多义项覆盖：`主体化` 5、`客体化` 5、`去主体化` 5、`去客体化` 4。

---

# W3 Lexicon Audit — Batch 15

- batch_id: `W3-B15-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词补全”，新增 `对象化`、`符号化`、`现象化` 三组机制词，为后续 `去符号化` / `去现象化` 与 W5 关系资产做准备。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B15 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 160 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B15 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增对象化/符号化/现象化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `对象化`: created 4 senses; rows 280, 209, 192, 285; quotes=8; all draft.
- `符号化`: created 4 senses; rows 140, 266, 228, 185; quotes=9; all draft.
- `现象化`: created 4 senses; rows 5, 18, 40, 219; quotes=8; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B15-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results:

```text
W3 batch validation: records=12, terms=3, quotes=25, errors=0, warnings=0
W3 full validation: records=160, terms=37, quotes=373, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批建议继续处理 `去符号化`、`去现象化`、`本体论化/去本体论化` 等成对机制词。

---

# W3 Lexicon Audit — Batch 16

- batch_id: `W3-B16-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词补全”，新增 `去符号化`、`去现象化`、`本体论化`、`去本体论化` 四组方向性机制词，承接 W3-B15 的符号化/现象化并为 W5 成对关系资产做准备。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B16 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 172 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B16 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增去符号化/去现象化/本体论化/去本体论化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `去符号化`: created 3 senses; rows 140, 245, 236; quotes=6; all draft.
- `去现象化`: created 3 senses; rows 18, 139; quotes=6; all draft.
- `本体论化`: created 3 senses; rows 2, 276, 288; quotes=6; all draft.
- `去本体论化`: created 3 senses; rows 289, 238; quotes=6; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B16-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:

```text
W3 batch validation: records=12, terms=4, quotes=24, errors=0, warnings=0
W3 full validation: records=172, terms=41, quotes=397, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批建议继续处理 `去实体化`、`实体化`、`表象化`、`去表象化` 或转向 W5 为本批机制词建立 typed relations。

---

# W3 Lexicon Audit — Batch 17

- batch_id: `W3-B17-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词补全”，新增 `实体化`、`去实体化`、`表象化` 三组机制词，承接 W3-B16 的本体论化/去本体论化并为 `去表象化` 与 W5 成对关系资产做准备。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B17 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 184 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B17 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增实体化/去实体化/表象化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `实体化`: created 4 senses; rows 222, 219, 214, 228; quotes=8; all draft.
- `去实体化`: created 4 senses; rows 139, 100, 135, 131; quotes=8; all draft.
- `表象化`: created 4 senses; rows 4, 2, 41; quotes=8; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B17-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:

```text
W3 batch validation: records=12, terms=3, quotes=24, errors=0, warnings=0
W3 full validation: records=184, terms=44, quotes=421, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批建议继续处理 `去表象化`、`二元化`、`去二元化` 或进入 `历史化/去历史化` 等机制词。

---

# W3 Lexicon Audit — Batch 18

- batch_id: `W3-B18-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词补全”，新增 `去表象化`、`二元化`、`历史化` 三组机制/过程词，承接 W3-B17 的表象化与 row 139 的二元化/去二元化候选。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B18 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 196 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B18 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增去表象化/二元化/历史化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `去表象化`: created 4 senses; rows 62, 254, 273, 131; quotes=8; all draft.
- `二元化`: created 4 senses; rows 139, 143, 271, 262; quotes=8; all draft.
- `历史化`: created 4 senses; rows 289, 279, 295; quotes=8; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B18-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:

```text
W3 batch validation: records=12, terms=3, quotes=24, errors=0, warnings=0
W3 full validation: records=196, terms=47, quotes=445, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批建议继续处理 `去二元化`、`去历史化`、`中心化`、`去中心化`。


---

# W3 Lexicon Audit — Batch 19

- batch_id: `W3-B19-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词补全”，新增 `去历史化`、`中心化`、`去中心化`、`重新中心化` 四组中心/去中心/再中心机制词，承接 W3-B18 的历史化与二元化后续候选。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B19 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 208 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B19 机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增去历史化/中心化/去中心化/重新中心化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `去历史化`: created 2 senses; rows 131, 291; quotes=4; all draft.
- `中心化`: created 4 senses; rows 96, 219, 233, 156; quotes=8; all draft.
- `去中心化`: created 4 senses; rows 276, 233, 296, 315; quotes=8; all draft.
- `重新中心化`: created 2 senses; rows 119, 131; quotes=4; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B19-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:

```text
W3 batch validation: records=12, terms=4, quotes=24, errors=0, warnings=0
W3 full validation: records=208, terms=51, quotes=469, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批建议优先选择证据较丰富的 `符号学`、`结构主义`、`能指`、`所指` 等术语；`去二元化` 仍需谨慎避免单行证据过度扩张。


---

# W3 Lexicon Audit — Batch 20

- batch_id: `W3-B20-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项“机制词/核心词补全”，新增 `符号学`、`结构主义`、`能指`、`所指` 四组 3-4 结构主义/符号学核心词，为后续 W5 符号—结构—意指关系资产做准备。

## 1. W2 Gate Audit

- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B20 extension.

## 2. W3 Artifacts

| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 220 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B20 结构主义/符号学术语索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增符号学/结构主义/能指/所指歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage

- `符号学`: created 3 senses; rows 254, 256; quotes=6; all draft.
- `结构主义`: created 3 senses; rows 254, 256; quotes=6; all draft.
- `能指`: created 3 senses; rows 256, 254; quotes=6; all draft.
- `所指`: created 3 senses; rows 256, 253; quotes=6; all draft.

## 4. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B20-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:

```text
W3 batch validation: records=12, terms=4, quotes=24, errors=0, warnings=0
W3 full validation: records=220, terms=55, quotes=493, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes

- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批可继续处理 `差异`、`本质`、`存在` 或 `哲学化` 等高频术语；W5 应开始承接能指/所指与符号学/结构主义边界。


---

# W3 Lexicon Audit — Batch 21

- batch_id: `W3-B21-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项高风险核心词补全，新增 `差异`、`本质`、`存在` 三组多义核心词，为后续 W5 存在/本质、差异/二元化、entity/实体关系资产做准备。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B21 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 232 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B21 高风险核心词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增差异/本质/存在歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `差异`: created 4 senses; rows 143, 188, 276; quotes=8; all draft.
- `本质`: created 4 senses; rows 188, 214, 143, 206; quotes=8; all draft.
- `存在`: created 4 senses; rows 143, 206, 214; quotes=8; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B21-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=12, terms=3, quotes=24, errors=0, warnings=0
W3 full validation: records=232, terms=58, quotes=517, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批可继续处理 `哲学化`、`辩证法化`、`认识论化`、`目的论化` 或转入 W5 为 B20/B21 建立关系资产。


---

# W3 Lexicon Audit — Batch 22

- batch_id: `W3-B22-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项机制词补全，新增 `哲学化`、`辩证法化`、`认识论化`、`目的论化` 四组转化机制词，为 W5 中“化”机制边界和历史—理论家—辩证法化路线做准备。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B22 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 244 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B22 转化机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增哲学化/辩证法化/认识论化/目的论化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `哲学化`: created 3 senses; rows 289, 291, 263; quotes=6; all draft.
- `辩证法化`: created 3 senses; rows 289, 194; quotes=6; all draft.
- `认识论化`: created 3 senses; rows 188, 194, 272; quotes=6; all draft.
- `目的论化`: created 3 senses; rows 119, 268; quotes=6; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B22-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=12, terms=4, quotes=24, errors=0, warnings=0
W3 full validation: records=244, terms=62, quotes=541, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批可继续处理 `去目的论化`、`去认识论化`、`本体化`、`去存在化` 或转入 W5 为 B20–B22 建立关系资产。

---

# W3 Lexicon Audit — Batch 23

- batch_id: `W3-B23-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 MASTER-SPEC 第一期 D 项机制词补全，新增 `去目的论化`、`本体化`、`去辩证化`、`教科书化` 四组反向/制度化机制词，为后续 W5 的目的论/本体论/辩证法化边界资产准备证据。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B23 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 256 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B23 反向/制度化机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增去目的论化/本体化/去辩证化/教科书化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `去目的论化`: created 3 senses; rows 8, 207, 274; quotes=6; all draft.
- `本体化`: created 3 senses; rows 144, 142, 228; quotes=6; all draft.
- `去辩证化`: created 3 senses; rows 289, 266; quotes=6; all draft.
- `教科书化`: created 3 senses; rows 279, 289; quotes=6; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B23-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=12, terms=4, quotes=24, errors=0, warnings=0
W3 full validation: records=256, terms=66, quotes=565, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan: PASS (no configured forbidden patterns found)
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批继续 W3 toward ≥300：可优先处理 `科学化`、`体系化`、`实在化`、`爱欲`、`力比多` 等证据较丰富术语；或并行转入 W5 为 B20–B23 建立关系资产。

---

---

# W3 Lexicon Audit — Batch 24

- batch_id: `W3-B24-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W3 第一期高风险术语扩展，新增 `爱欲`、`力比多`、`享乐`、`献祭` 四组爱欲经济/献祭机制词，为后续 W5 的欲望—驱力—享乐—献祭边界资产准备证据。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B24 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 268 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B24 爱欲经济/献祭机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增爱欲/力比多/享乐/献祭歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `爱欲`: created 3 senses; rows 27, 29, 46; quotes=6; all draft.
- `力比多`: created 3 senses; rows 48, 75, 93, 140; quotes=6; all draft.
- `享乐`: created 3 senses; rows 7, 31, 46; quotes=6; all draft.
- `献祭`: created 3 senses; rows 31, 268; quotes=6; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B24-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=12, terms=4, quotes=24, errors=0, warnings=0
W3 full validation: records=268, terms=70, quotes=589, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan: PASS (no configured forbidden patterns found)
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批继续 W3 toward ≥300：还需 32 条 sense；可优先处理 `科学化`、`体系化`、`事件`、`真理程序`、`共同体` 等证据较丰富术语。

---

# W3 Lexicon Audit — Batch 25

- batch_id: `W3-B25-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W3 第一期机制词扩展，新增 `科学化`、`体系化`、`实证化` 三组方法/建制机制词，为后续 W5 的科学自称、体系能力、positivization/实证主义边界资产准备证据。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B25 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 280 records total; 新增 12 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B25 科学/体系/实证化机制词索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增科学化/体系化/实证化歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `科学化`: created 4 senses; rows 1, 10, 177, 184; quotes=8; all draft.
- `体系化`: created 4 senses; rows 86, 108, 135, 172; quotes=8; all draft.
- `实证化`: created 4 senses; rows 1, 10, 229, 243; quotes=8; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B25-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=12, terms=3, quotes=24, errors=0, warnings=0
W3 full validation: records=280, terms=73, quotes=613, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan: PASS (no configured forbidden patterns found)
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- 下一批继续 W3 toward ≥300：还需 20 条 sense；可用两批小批量或一批 20 条完成 phase-1 count gate，但仍需保持每词 2–5 senses 与 exact quote 验证。

---

# W3 Lexicon Audit — Batch 26

- batch_id: `W3-B26-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 以一批可审计的 5-term/20-sense 扩展关闭 MASTER-SPEC 第一期 W3 ≥300 sense count gate，新增 `共同体`、`主体间性`、`生活世界`、`事件性`、`平等主义` 五组高风险基础/关系术语。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B26 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 300 records total; 新增 20 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B26 phase-1 gate closure 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增共同体/主体间性/生活世界/事件性/平等主义歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `共同体`: created 4 senses; rows 1, 10, 11, 51; quotes=8; all draft.
- `主体间性`: created 4 senses; rows 200, 201, 34, 51; quotes=8; all draft.
- `生活世界`: created 4 senses; rows 188, 189, 200, 201; quotes=8; all draft.
- `事件性`: created 4 senses; rows 120, 123, 296; quotes=8; all draft.
- `平等主义`: created 4 senses; rows 80, 161, 165, 178; quotes=8; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B26-2026-06-08
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=20, terms=5, quotes=40, errors=0, warnings=0
W3 full validation: records=300, terms=78, quotes=653, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan: PASS (no configured forbidden patterns found)
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count gate status: W3 第一期 ≥300 senses 已达成；最终 W3 仍需扩展至 ≥500 senses / ≥200 terms，并进入 W5/W6/W7/W8/W9 后续阶段。

---

# W3 Lexicon Audit — Batch 27

- batch_id: `W3-B27-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 从 W3 phase-1 count gate 转入 MASTER-SPEC final W3 target，扩展 4-1-2/4-1-2-1 与科学革命/事件主义中的操作性术语，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B27 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 324 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B27 study/action/knowledge operation terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `学习`, `研究`, `现实`, `通俗化`, `交谈`: created 10 senses; row 285; quotes=20; all draft.
- `灌输`, `宣传`: created 4 senses; row 284; quotes=8; all draft.
- `行动`: created 2 senses; row 285; quotes=4; all draft.
- `信仰`, `忠诚`: created 4 senses; rows 11, 263, 284; quotes=8; all draft.
- `范式`, `知识`: created 4 senses; row 11; quotes=8; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B27-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=324, terms=90, quotes=701, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 324 senses / 90 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 28

- batch_id: `W3-B28-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 11 科学革命论拆分库恩范式/科学史/历史主义/基础主义术语，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B28 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 348 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B28 Kuhn/science-revolution terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `科学史`, `历史主义`: created 4 senses; row 11; quotes=8; all draft.
- `危机`, `常态范式`, `范式革命`: created 6 senses; row 11; quotes=12; all draft.
- `共同信仰`, `方法论`, `知识论`: created 6 senses; row 11; quotes=12; all draft.
- `学科矩阵`, `范例`, `不可通约性`, `基础主义`: created 8 senses; row 11; quotes=16; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B28-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=348, terms=102, quotes=749, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 348 senses / 102 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 29

- batch_id: `W3-B29-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 285 学习/研究的现实研究、书写传播与行动判断术语，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B29 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 372 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B29 writing/research/action operation terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `书写`, `小册子`: created 4 senses; row 285; quotes=8; all draft.
- `见微知著`, `观察`, `分析`, `反刍`: created 8 senses; row 285; quotes=16; all draft.
- `现实理论化`, `理论现实化`, `理论劳动`: created 6 senses; row 285; quotes=12; all draft.
- `自圆其说`, `可行性`, `严肃`: created 6 senses; row 285; quotes=12; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B29-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=372, terms=114, quotes=797, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 372 senses / 114 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 30

- batch_id: `W3-B30-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 285 学习/研究的现实来源、细节回溯、运动化合理化与关系还原术语，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B30 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 396 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B30 reality-source/regressive-analysis relation terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `数据`, `报告`: created 4 senses; row 285; quotes=8; all draft.
- `细节`, `突发状况`, `情绪感受`: created 6 senses; row 285; quotes=12; all draft.
- `合理化`, `运动化`, `规律`, `回溯`: created 8 senses; row 285; quotes=16; all draft.
- `政治经济关系`, `权力关系`, `心理状态`: created 6 senses; row 285; quotes=12; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B30-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=396, terms=126, quotes=845, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 396 senses / 126 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 31

- batch_id: `W3-B31-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 263 静止的事件主义/事件哲学术语群，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B31 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 420 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B31 event-philosophy terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `回溯性逻辑`, `版本更新`: created 4 senses; row 263; quotes=8; all draft.
- `守阵地`, `剩余`, `site`, `position`, `state`, `空位置`: created 12 senses; row 263; quotes=24; all draft.
- `真理事件`, `主体性`, `主体化过程`, `数学化`: created 8 senses; row 263; quotes=16; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B31-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=420, terms=138, quotes=893, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 420 senses / 138 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 32

- batch_id: `W3-B32-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 263 Being/Event 与版本更新中介术语群，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B32 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 444 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B32 Being/Event/version-update mediation terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `Being`, `Event`, `space`, `点位`, `立场`: created 10 senses; row 263; quotes=20; all draft.
- `数学知识`, `本体论知识`, `减法`, `矛盾张力`: created 8 senses; row 263; quotes=16; all draft.
- `知识框架`, `数据交换中介`, `整体降临`: created 6 senses; row 263; quotes=12; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B32-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=444, terms=150, quotes=941, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 444 senses / 150 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 33

- batch_id: `W3-B33-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 229 否定辩证法/星丛术语群，新增 12 个 terms / 24 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B33 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 468 records total; 新增 24 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B33 Adorno/negative-dialectics terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 12 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `星丛`, `名称`, `命名活动`, `语用实践场`, `不可消解之物`: created 10 senses; row 229; quotes=20; all draft.
- `反体系`, `同一性原理`, `具体普遍性`: created 6 senses; row 229; quotes=12; all draft.
- `内在张力`, `语音`, `离散符号系统`, `无调性`: created 8 senses; row 229; quotes=16; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B33-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=24, terms=12, quotes=48, errors=0, warnings=0
W3 full validation: records=468, terms=162, quotes=989, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 468 senses / 162 terms；最终 W3 ≥500 senses / ≥200 terms 仍未完成。

---

# W3 Lexicon Audit — Batch 34

- batch_id: `W3-B34-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: 继续 MASTER-SPEC final W3 target，围绕 row 229 否定辩证法的离散/无调性与不可还原性术语，新增 20 个 terms / 40 条 draft senses。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B34 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 508 records total; 新增 40 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B34 Adorno/atonal-discrete-objectivity terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 20 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `星座`, `名字`, `断裂的符号化`, `主客体`, `表征主义`: created 10 senses; row 229; quotes=20; all draft.
- `先验语音论`, `声音`, `音乐`, `勋伯格`: created 8 senses; row 229; quotes=16; all draft.
- `伪连续`, `局部断裂`, `总体连续`, `调性`, `难听`, `底层符号`: created 12 senses; row 229; quotes=24; all draft.
- `被压抑`, `前符号化`, `不可还原性`, `不透明性`, `客体化运动`: created 10 senses; row 229; quotes=20; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B34-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=40, terms=20, quotes=80, errors=0, warnings=0
W3 full validation: records=508, terms=182, quotes=1069, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 508 senses / 182 terms；W3 sense final floor 已达到，术语 final floor ≥200 terms 仍需至少 +18 terms。

---

# W3 Lexicon Audit — Batch 35

- batch_id: `W3-B35-2026-06-09`
- audited_at: 2026-06-09 CST
- objective: close MASTER-SPEC W3 quantitative floor by adding 18 terms / 36 draft senses from row 263 静止事件主义的数学话语与真理方式术语群。

## 1. W2 Gate Audit
- W2 segment-card layer unchanged; source rows resolved through `knowledge/manifests/segments.jsonl` and W2 card paths.
- verdict: PASS — W2 coverage supports W3-B35 extension.

## 2. W3 Artifacts
| artifact | status | evidence |
|---|---|---|
| `knowledge/lexicon/term-senses.jsonl` | appended | 544 records total; 新增 36 条 draft 义项 |
| `knowledge/lexicon/core-terms.md` | updated | 新增 W3-B35 mathematical-discourse/truth-mode terms 索引 |
| `knowledge/lexicon/ambiguous-terms.md` | updated | 新增 18 个新术语的歧义说明 |
| `knowledge/qa/w3-lexicon-audit.md` | appended | 本批审计条目 |

## 3. Evidence Coverage
- `本体论更新`, `高级学术话语`, `数学话语`: created 6 senses; row 263; quotes=12; all draft.
- `数理逻辑`, `拓扑学`, `数论`, `离散数学`, `最小二乘法`, `超定`, `函数拟合`: created 14 senses; row 263; quotes=28; all draft.
- `符号学工具`, `几何学配型`, `集合容器`, `不可数的多`: created 8 senses; row 263; quotes=16; all draft.
- `真理显现方式`, `politics`, `amor`, `艺术`: created 8 senses; row 263; quotes=16; all draft.

## 4. Validation
```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-B35-2026-06-09
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
```

Observed results after validation:
```text
W3 batch validation: records=36, terms=18, quotes=72, errors=0, warnings=0
W3 full validation: records=544, terms=200, quotes=1141, errors=0, warnings=0
W5 final gate validation: records=60, quotes=70, types=12/12, errors=0, warnings=0
W4 L1/L2/L3/L4 validations: PASS at counts 4/16/64/172
git diff --check: PASS
forbidden-language scan over active knowledge surfaces: PASS
```

## 5. Additional Notes
- 所有新增 records 保持 `draft`，未进行 canonical 提升。
- 本批不使用 Atlas_DB 作为证据；正式证据全部为 `split_md_clean/` 子串。
- Count status: W3 现为 544 senses / 200 terms；MASTER-SPEC W3 quantitative floors (≥500 senses / ≥200 terms) reached and final full validation passed after docs update.
