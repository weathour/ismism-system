# W4 Position Card Audit

- created: 2026-06-08
- status: draft audit log
- scope: W4 position cards only
- validation script: `knowledge/scripts/validate_w4_position_cards.py`

---

## W4-L1 Audit — 4 一级位置卡

- batch_id: `W4-L1-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 在 W3 达到 100 条 draft sense、四轴术语已拆分后，启动 W4 L1 position cards。

### 1. Preconditions

| precondition | evidence | verdict |
|---|---|---|
| W3 ≥ 100 draft senses | `python3 knowledge/scripts/validate_w3_term_senses.py --repo .` → records=100 | PASS |
| 四轴术语已拆分 | `场域论/本体论/认识论/目的论` 均在 `term-senses.jsonl` 中有 draft senses | PASS |
| W2 segment cards available | rows 1, 96, 187, 276 segment cards used as primary evidence | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1.md` | created | L1 实在论 |
| `knowledge/position-cards/2.md` | created | L1 形而上学 |
| `knowledge/position-cards/3.md` | created | L1 观念论 |
| `knowledge/position-cards/4.md` | created | L1 实践 |
| `knowledge/position-cards/index.md` | created | W4-L1 coverage index; final 256-card coverage remains pending |
| `knowledge/scripts/validate_w4_position_cards.py` | created | partial-batch validator for W4 cards |

### 3. Validation

Command:

```bash
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
```

Observed result:

```text
PASS: 4 level-1 cards; approximate lengths 872/914/950/946.
```

### 4. Gate notes

- Required W4 sections present in all 4 cards: matrix coordinates, position definition, representative isms/schools, core mechanisms, adjacent-position relations, associated terms.
- Cards remain `status: draft`.
- No W3/W5 canonical promotion was performed.
- Cards avoid personality-diagnostic wording and do not present matrix positions as absolute truth.
- This is not the final W4 gate: L2/L3/L4 cards remain pending.

### 5. Next W4 work

1. Create 16 L2 position cards (`1-1` … `4-4`) in small auditable batches.
2. Continue W3 toward ≥300 senses; W4 should feed new structural and school terms into W3 candidates.
3. Keep all W4 cards draft until W6 audit.

---

## W4-L2-B1 Audit — field 1 二级位置卡（1-1 … 1-4）

- batch_id: `W4-L2-B1-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 在 W4 L1 完成后，先处理 field=1 的四张二级位置卡，以验证 L2 card 模式与 W3 term links。

### 1. Evidence base

| position | title | primary/support rows | segment cards | verdict |
|---|---|---:|---|---|
| 1-1 | 科学实在论 | 2 | `knowledge/segment-cards/0002_1-1.md` | PASS |
| 1-2 | 宗教实在论 | 24 | `knowledge/segment-cards/0024_1-2.md` | PASS |
| 1-3 | 庸俗唯我论（复习课） | 46 | `knowledge/segment-cards/0046_1-3.md` | PASS |
| 1-4 | 平庸主义 | 67, 75 | `knowledge/segment-cards/0067_1-4.md`; `knowledge/segment-cards/0075_1-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-1.md` | created | 科学实在论；field=1 / ontology=1 |
| `knowledge/position-cards/1-2.md` | created | 宗教实在论；field=1 / ontology=2 |
| `knowledge/position-cards/1-3.md` | created | 庸俗唯我论（复习课）；四轴读法训练位 |
| `knowledge/position-cards/1-4.md` | created | 平庸主义；含 row 75 子型提示 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L2 4/16 and total cards 8 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 4
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=4; lengths 793/738/764/728
```

### 4. Gate notes

- All four L2 cards declare `status: draft` and preserve `source_rows` / `source_segments`.
- No W3/W5 promotion was performed.
- Cards avoid personality-diagnostic wording and do not present the matrix as an absolute explanation.
- `1-3` is explicitly marked as a method-training node for four-axis reading, not as a personal description.
- `1-4` uses row 67/75 structurally and avoids treating “平庸主义” as a social identity label.

### 5. Next W4 work

1. Continue W4-L2-B2 with field 2 positions (`2-1` … `2-4`).
2. Use each L2 card to nominate new W3 candidates, but keep W3 senses `draft`.
3. After all 16 L2 cards, reassess whether the W4 validator should enforce L2 length bounds and stronger index coverage.

---

## W4-L2-B2 Audit — field 2 二级位置卡（2-1 … 2-4）

- batch_id: `W4-L2-B2-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 扩展二字头形而上学场域的四张 L2 cards，补齐 field=2 的 ontology=1–4 结构读法。

### 1. Evidence base

| position | title | primary/support rows | segment cards | verdict |
|---|---|---:|---|---|
| 2-1 | 在场形而上学 | 97 | `knowledge/segment-cards/0097_2-1.md` | PASS |
| 2-2 | 辩证形而上学 | 118, 119 | `knowledge/segment-cards/0118_2-2.md`; `knowledge/segment-cards/0119_2-2.md` | PASS |
| 2-3 | 我思形而上学 | 144, 145 | `knowledge/segment-cards/0144_2-3.md`; `knowledge/segment-cards/0145_2-3.md` | PASS |
| 2-4 | 反形而上学 | 166 | `knowledge/segment-cards/0166_2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-1.md` | created | 在场形而上学；field=2 / ontology=1 |
| `knowledge/position-cards/2-2.md` | created | 辩证形而上学；field=2 / ontology=2 |
| `knowledge/position-cards/2-3.md` | created | 我思形而上学；field=2 / ontology=3 |
| `knowledge/position-cards/2-4.md` | created | 反形而上学；field=2 / ontology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L2 8/16 and total cards 12 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 8
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=8; new field-2 lengths 831/804/811/853
```

### 4. Gate notes

- All four field-2 cards declare `status: draft` and preserve row/segment traceability.
- The cards distinguish `field=2` total position from `2-1` … `2-4` subpositions rather than using “形而上学” as an all-purpose explanation.
- `2-4` is written as a structural paradox of anti-metaphysics, not as a simple dismissal of listed schools.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L2-B3 with field 3 positions (`3-1` … `3-4`).
2. Track new W3 candidate terms from field 2 cards: 在场、缺席、差异、始基、辩证形而上学、虚无、否定性、我思、明证性、反形而上学、薄本体论、超定。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L2-B3 Audit — field 3 二级位置卡（3-1 … 3-4）

- batch_id: `W4-L2-B3-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 扩展三字头观念论场域的四张 L2 cards，补齐 field=3 的 ontology=1–4 结构读法。

### 1. Evidence base

| position | title | primary/support rows | segment cards | verdict |
|---|---|---:|---|---|
| 3-1 | 现象学 | 188, 189 | `knowledge/segment-cards/0188_3-1.md`; `knowledge/segment-cards/0189_3-1.md` | PASS |
| 3-2 | 德国观念论 | 210, 211 | `knowledge/segment-cards/0210_3-2.md`; `knowledge/segment-cards/0211_3-2.md` | PASS |
| 3-3 | 生存论 | 232, 233 | `knowledge/segment-cards/0232_3-3.md`; `knowledge/segment-cards/0233_3-3.md` | PASS |
| 3-4 | 符号学 | 254, 255 | `knowledge/segment-cards/0254_3-4.md`; `knowledge/segment-cards/0255_3-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-1.md` | created | 现象学；field=3 / ontology=1 |
| `knowledge/position-cards/3-2.md` | created | 德国观念论；field=3 / ontology=2 |
| `knowledge/position-cards/3-3.md` | created | 生存论；field=3 / ontology=3 |
| `knowledge/position-cards/3-4.md` | created | 符号学；field=3 / ontology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L2 12/16 and total cards 16 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 12
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=12; new field-3 lengths 845/810/818/853
```

### 4. Gate notes

- All four field-3 cards declare `status: draft` and preserve row/segment traceability.
- Cards keep `position:3` as a modern-观念论 field and do not reduce it to “主观唯心主义”.
- `3-4` is constrained as a structure/sign position; it does not treat 符号学 as an all-purpose explanatory key.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Finish W4-L2-B4 with field 4 positions (`4-1` … `4-4`).
2. Track W3 candidates from field 3 cards: 现象学、先验还原、自我给予性、意向性、德国观念论、Satz/Setzung、有限主义、生存论、决断、结构主义、能指链、反人道主义。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L2-B4 Audit — field 4 二级位置卡（4-1 … 4-4）

- batch_id: `W4-L2-B4-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 扩展四字头实践场域的四张 L2 cards，并完成 W4-L2 16/16 draft coverage。

### 1. Evidence base

| position | title | primary/support rows | segment cards | verdict |
|---|---|---:|---|---|
| 4-1 | 政治-经济-意识形态批判 | 277, 278 | `knowledge/segment-cards/0277_4-1.md`; `knowledge/segment-cards/0278_4-1.md` | PASS |
| 4-2 | 现实的正统化 | 299, 300 | `knowledge/segment-cards/0299_4-2.md`; `knowledge/segment-cards/0300_4-2.md` | PASS |
| 4-3 | 建设理想社会 | 321 | `knowledge/segment-cards/0321_4-3.md` | PASS |
| 4-4 | 不可能的乌托邦 | 342, 343 | `knowledge/segment-cards/0342_4-4.md`; `knowledge/segment-cards/0343_4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/4-1.md` | created | 政治-经济-意识形态批判；field=4 / ontology=1 |
| `knowledge/position-cards/4-2.md` | created | 现实的正统化；field=4 / ontology=2 |
| `knowledge/position-cards/4-3.md` | created | 建设理想社会；field=4 / ontology=3 |
| `knowledge/position-cards/4-4.md` | created | 不可能的乌托邦；field=4 / ontology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L2 16/16 and total cards 20 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16; new field-4 lengths 797/788/741/773
```

### 4. Gate notes

- W4-L2 is now complete at 16/16 draft cards.
- All field-4 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish critique,正统化,建设,不可能乌托邦 instead of treating “实践” as a single-purpose answer.
- No W3/W5 canonical promotion was performed.
- W4-L3 and W4-L4 remain pending; L2 completion is not a W4 final gate.

### 5. Next W4 work

1. Plan W4-L3 batching for 64 third-level cards (`1-1-1` … `4-4-4`), with row/segment evidence and shorter draft card format.
2. Continue W3 toward ≥300 senses; field-4 cards nominate terms such as 三连批判、现实正统化、行动者、建设活动、脚手架、中介环节、不可能乌托邦、异化、主体间范式、后资本主义。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B1 Audit — 1-1 三级位置卡（1-1-1 … 1-1-4）

- batch_id: `W4-L3-B1-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 启动 64 张 W4-L3 cards，先处理 `1-1` 科学实在论下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-1-1 | 物理主义 | 4 | `knowledge/segment-cards/0004_1-1-1.md` | PASS |
| 1-1-2 | 建构论 | 9 | `knowledge/segment-cards/0009_1-1-2.md` | PASS |
| 1-1-3 | 认知主义 | 14 | `knowledge/segment-cards/0014_1-1-3.md` | PASS |
| 1-1-4 | 行为主义 | 19 | `knowledge/segment-cards/0019_1-1-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-1-1.md` | created | 物理主义；field=1 / ontology=1 / epistemology=1 |
| `knowledge/position-cards/1-1-2.md` | created | 建构论；field=1 / ontology=1 / epistemology=2 |
| `knowledge/position-cards/1-1-3.md` | created | 认知主义；field=1 / ontology=1 / epistemology=3 |
| `knowledge/position-cards/1-1-4.md` | created | 行为主义；field=1 / ontology=1 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 4/64 and total cards 24 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 4
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=4; lengths 413/407/429/438
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- The cards keep L3 as a position layer, not a general philosophical encyclopedia entry.
- No personality-diagnostic wording or matrix-as-final-truth wording was introduced.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `1-2-1` … `1-2-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 物理主义、科学教条主义、建构论、社会建构、构造论、认知主义、功能主义、心灵模型、行为主义、黑箱、控制论。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B2 Audit — 1-2 三级位置卡（1-2-1 … 1-2-4）

- batch_id: `W4-L3-B2-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3，处理 `1-2` 宗教实在论下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-2-1 | 神创论 | 26 | `knowledge/segment-cards/0026_1-2-1.md` | PASS |
| 1-2-2 | 偶像论／偶像崇拜 | 31 | `knowledge/segment-cards/0031_1-2-2.md` | PASS |
| 1-2-3 | 唯灵论 | 36 | `knowledge/segment-cards/0036_1-2-3.md` | PASS |
| 1-2-4 | 反偶像论 | 41 | `knowledge/segment-cards/0041_1-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-2-1.md` | created | 神创论；field=1 / ontology=2 / epistemology=1 |
| `knowledge/position-cards/1-2-2.md` | created | 偶像论／偶像崇拜；field=1 / ontology=2 / epistemology=2 |
| `knowledge/position-cards/1-2-3.md` | created | 唯灵论；field=1 / ontology=2 / epistemology=3 |
| `knowledge/position-cards/1-2-4.md` | created | 反偶像论；field=1 / ontology=2 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 8/64 and total cards 28 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 8
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=8; new lengths 395/428/462/461
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- The cards describe religious-realism subpositions structurally; they do not assess belief truth or assign identities to people.
- No personality-diagnostic wording or matrix-as-final-truth wording was introduced.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `1-3-1` … `1-3-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 神创论、造物者、被造物、偶像崇拜、神圣现象、唯灵论、灵性主义、反偶像论、现象化禁忌、激进否定性。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B3 Audit — 1-3 三级位置卡（1-3-1 … 1-3-4）

- batch_id: `W4-L3-B3-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3，处理 `1-3` 庸俗唯我论/四轴训练位下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-3-1 | 伪唯心主义 | 47 | `knowledge/segment-cards/0047_1-3-1.md` | PASS |
| 1-3-2 | 本真主义 | 52 | `knowledge/segment-cards/0052_1-3-2.md` | PASS |
| 1-3-3 | 唯意志主义 | 57 | `knowledge/segment-cards/0057_1-3-3.md` | PASS |
| 1-3-4 | 直觉主义／体验主义／意识流 | 62 | `knowledge/segment-cards/0062_1-3-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-3-1.md` | created | 伪唯心主义；field=1 / ontology=3 / epistemology=1 |
| `knowledge/position-cards/1-3-2.md` | created | 本真主义；field=1 / ontology=3 / epistemology=2 |
| `knowledge/position-cards/1-3-3.md` | created | 唯意志主义；field=1 / ontology=3 / epistemology=3 |
| `knowledge/position-cards/1-3-4.md` | created | 直觉主义／体验主义／意识流；field=1 / ontology=3 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 12/64 and total cards 32 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 12
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=12; new lengths 418/413/453/493
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- The cards treat 1-3 as a structural/method-training cluster rather than a personality category.
- The source titles contain polemical wording, but the cards avoid using it as a label for persons or groups.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `1-4-1` … `1-4-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 伪唯心主义、背景性无、本真主义、本真自我、唯意志主义、原初意志、直觉主义、体验主义、意识流、背景秩序。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B4 Audit — 1-4 三级位置卡（1-4-1 … 1-4-4）

- batch_id: `W4-L3-B4-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3，处理 `1-4` 平庸主义下的四个三级位置，并完成 L3 field 1 coverage。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-4-1 | 当代自然主义 | 76 | `knowledge/segment-cards/0076_1-4-1.md` | PASS |
| 1-4-2 | 世俗人道主义 | 81 | `knowledge/segment-cards/0081_1-4-2.md` | PASS |
| 1-4-3 | 心理主义 | 86 | `knowledge/segment-cards/0086_1-4-3.md` | PASS |
| 1-4-4 | 庸俗主义 | 91 | `knowledge/segment-cards/0091_1-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-4-1.md` | created | 当代自然主义；field=1 / ontology=4 / epistemology=1 |
| `knowledge/position-cards/1-4-2.md` | created | 世俗人道主义；field=1 / ontology=4 / epistemology=2 |
| `knowledge/position-cards/1-4-3.md` | created | 心理主义；field=1 / ontology=4 / epistemology=3 |
| `knowledge/position-cards/1-4-4.md` | created | 庸俗主义；field=1 / ontology=4 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 16/64 and total cards 36 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 16
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=16; new lengths 527/493/498/451
```

### 4. Gate notes

- L3 field 1 (`1-1-1` … `1-4-4`) is now complete at 16/16 draft cards.
- Cards describe 1-4 subpositions as structural closure strategies, not person labels.
- Source titles contain polemical wording, but cards avoid turning it into diagnostic or identity claims.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with field 2, likely `2-1-1` … `2-1-4`.
2. Feed L3 candidate terms into W3 queue: 当代自然主义、日常语言学派、世俗人道主义、心理主义、心理学主义、庸俗主义、目的论直通、前反思行为。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B5 Audit — 2-1 三级位置卡（2-1-1 … 2-1-4）

- batch_id: `W4-L3-B5-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 2，处理 `2-1` 在场形而上学下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-1-1 | 普遍主义 | 98 | `knowledge/segment-cards/0098_2-1-1.md` | PASS |
| 2-1-2 | 本质主义 | 103 | `knowledge/segment-cards/0103_2-1-2.md` | PASS |
| 2-1-3 | 合理主义 | 108 | `knowledge/segment-cards/0108_2-1-3.md` | PASS |
| 2-1-4 | 绝对主义 | 113 | `knowledge/segment-cards/0113_2-1-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-1-1.md` | created | 普遍主义；field=2 / ontology=1 / epistemology=1 |
| `knowledge/position-cards/2-1-2.md` | created | 本质主义；field=2 / ontology=1 / epistemology=2 |
| `knowledge/position-cards/2-1-3.md` | created | 合理主义；field=2 / ontology=1 / epistemology=3 |
| `knowledge/position-cards/2-1-4.md` | created | 绝对主义；field=2 / ontology=1 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 20/64 and total cards 40 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 20
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=20; new lengths 615/629/615/657
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards treat 普遍主义、本质主义、合理主义、绝对主义 as structural positions inside `2-1` 在场形而上学, not as final labels for persons or traditions.
- The batch distinguishes source titles, historical representative figures, and ISMISM matrix coordinates; no external material candidate was promoted as truth.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `2-2-1` … `2-2-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 普遍主义、topos、cosmos、本质主义、太一、真理/意见、合理主义、ratio、绝对主义、语用注册。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B6 Audit — 2-2 三级位置卡（2-2-1 … 2-2-4）

- batch_id: `W4-L3-B6-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 2，处理 `2-2` 辩证形而上学下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-2-1 | 无限主义 | 120 | `knowledge/segment-cards/0120_2-2-1.md` | PASS |
| 2-2-2 | 否定主义 | 125 | `knowledge/segment-cards/0125_2-2-2.md` | PASS |
| 2-2-3 | 超验主义 | 134 | `knowledge/segment-cards/0134_2-2-3.md` | PASS |
| 2-2-4 | 反二元对立 | 139 | `knowledge/segment-cards/0139_2-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-2-1.md` | created | 无限主义；field=2 / ontology=2 / epistemology=1 |
| `knowledge/position-cards/2-2-2.md` | created | 否定主义；field=2 / ontology=2 / epistemology=2 |
| `knowledge/position-cards/2-2-3.md` | created | 超验主义；field=2 / ontology=2 / epistemology=3 |
| `knowledge/position-cards/2-2-4.md` | created | 反二元对立；field=2 / ontology=2 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 24/64 and total cards 44 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 24
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=24; new lengths 614/583/632/653
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish religious/ethical/historical representative traditions from the ISMISM structural position; no tradition is treated as a final exhaustive identity.
- The 2-2 cards describe time, negation, ethical intuition, and anti-binary matrix operations as structural mechanisms, not as personality or diagnostic categories.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `2-3-1` … `2-3-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 无限主义、缘起、相依、否定主义、太一生水、反辅、超验主义、Over-soul、伦理直觉、反二元对立、拉矩阵、去客体化。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B7 Audit — 2-3 三级位置卡（2-3-1 … 2-3-4）

- batch_id: `W4-L3-B7-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 2，处理 `2-3` 我思形而上学下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-3-1 | 实体一元论 | 146 | `knowledge/segment-cards/0146_2-3-1.md` | PASS |
| 2-3-2 | 心物二元论 | 151 | `knowledge/segment-cards/0151_2-3-2.md` | PASS |
| 2-3-3 | 单子主义 | 156 | `knowledge/segment-cards/0156_2-3-3.md` | PASS |
| 2-3-4 | 宇宙平等主义 | 161 | `knowledge/segment-cards/0161_2-3-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-3-1.md` | created | 实体一元论；field=2 / ontology=3 / epistemology=1 |
| `knowledge/position-cards/2-3-2.md` | created | 心物二元论；field=2 / ontology=3 / epistemology=2 |
| `knowledge/position-cards/2-3-3.md` | created | 单子主义；field=2 / ontology=3 / epistemology=3 |
| `knowledge/position-cards/2-3-4.md` | created | 宇宙平等主义；field=2 / ontology=3 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 28/64 and total cards 48 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 28
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=28; new lengths 625/592/650/615
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish matrix position, historical representative candidates, and source polemics; none is treated as a person label or final truth.
- The 2-3 cards describe my-thought metaphysical mechanisms: entity unity, mind/matter split, monadic closure, and observer de-centering.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `2-4-1` … `2-4-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 实体一元论、奥卡姆剃刀、心物二元论、soul、单子主义、物自体、模态、宇宙平等主义、哥白尼原理、数学关系本体化。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B8 Audit — 2-4 三级位置卡（2-4-1 … 2-4-4）

- batch_id: `W4-L3-B8-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 2，处理 `2-4` 反形而上学下的四个三级位置，并完成 L3 field 2 coverage。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-4-1 | 经验主义 | 167 | `knowledge/segment-cards/0167_2-4-1.md` | PASS |
| 2-4-2 | 实证主义 | 172 | `knowledge/segment-cards/0172_2-4-2.md` | PASS |
| 2-4-3 | 逻辑实证主义 | 177 | `knowledge/segment-cards/0177_2-4-3.md` | PASS |
| 2-4-4 | 实用主义 | 182 | `knowledge/segment-cards/0182_2-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-4-1.md` | created | 经验主义；field=2 / ontology=4 / epistemology=1 |
| `knowledge/position-cards/2-4-2.md` | created | 实证主义；field=2 / ontology=4 / epistemology=2 |
| `knowledge/position-cards/2-4-3.md` | created | 逻辑实证主义；field=2 / ontology=4 / epistemology=3 |
| `knowledge/position-cards/2-4-4.md` | created | 实用主义；field=2 / ontology=4 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 32/64 and total cards 52 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 32
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=32; new lengths 644/644/614/639
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- L3 field 2 (`2-1-1` … `2-4-4`) is now complete at 16/16 draft cards.
- Cards describe anti-metaphysical positions as structural mechanisms and do not use them as identity labels for people or groups.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with field 3, likely `3-1-1` … `3-1-4`.
2. Feed L3 candidate terms into W3 queue: 经验主义、霍布斯、小体论、实证主义、孔德、人类宗教、逻辑实证主义、证实原则、清晰性、实用主义、工具主义、旁观论。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B9 Audit — 3-1 三级位置卡（3-1-1 … 3-1-4）

- batch_id: `W4-L3-B9-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 3，处理 `3-1` 现象学下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-1-1 | 先验现象学 | 190 | `knowledge/segment-cards/0190_3-1-1.md` | PASS |
| 3-1-2 | 实事现象学 | 195 | `knowledge/segment-cards/0195_3-1-2.md` | PASS |
| 3-1-3 | 生活世界现象学 | 200 | `knowledge/segment-cards/0200_3-1-3.md` | PASS |
| 3-1-4 | 现世的现象学 | 205 | `knowledge/segment-cards/0205_3-1-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-1-1.md` | created | 先验现象学；field=3 / ontology=1 / epistemology=1 |
| `knowledge/position-cards/3-1-2.md` | created | 实事现象学；field=3 / ontology=1 / epistemology=2 |
| `knowledge/position-cards/3-1-3.md` | created | 生活世界现象学；field=3 / ontology=1 / epistemology=3 |
| `knowledge/position-cards/3-1-4.md` | created | 现世的现象学；field=3 / ontology=1 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 36/64 and total cards 56 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 36
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=36; new lengths 554/572/577/613
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish phenomenological method, representative figures, and ISMISM matrix function; no tradition is treated as final truth.
- The 3-1 cards describe self-givenness, essence, intersubjectivity, lifeworld, historicity, and temporality as structural mechanisms rather than person labels.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `3-2-1` … `3-2-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 先验现象学、先验还原、本质还原、实事现象学、舍勒、主体间性、生活世界、现世现象学、时间性、历史性。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B10 Audit — 3-2 三级位置卡（3-2-1 … 3-2-4）

- batch_id: `W4-L3-B10-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 3，处理 `3-2` 德国观念论下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-2-1 | 批判哲学 | 212 | `knowledge/segment-cards/0212_3-2-1.md` | PASS |
| 3-2-2 | 知识学 | 217 | `knowledge/segment-cards/0217_3-2-2.md` | PASS |
| 3-2-3 | 体系自由主义 | 222 | `knowledge/segment-cards/0222_3-2-3.md` | PASS |
| 3-2-4 | 辩证法 | 227 | `knowledge/segment-cards/0227_3-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-2-1.md` | created | 批判哲学；field=3 / ontology=2 / epistemology=1 |
| `knowledge/position-cards/3-2-2.md` | created | 知识学；field=3 / ontology=2 / epistemology=2 |
| `knowledge/position-cards/3-2-3.md` | created | 体系自由主义；field=3 / ontology=2 / epistemology=3 |
| `knowledge/position-cards/3-2-4.md` | created | 辩证法；field=3 / ontology=2 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 40/64 and total cards 60 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 40
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=40; new lengths 640/642/677/631
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish Kantian critique, Fichtean self-positing, Schellingian system freedom, and Hegelian dialectical history without treating any as final truth.
- The 3-2 cards record mechanisms of judgment, setting, self/non-self, ground, freedom, symbolization, history, and ideology as structural positions rather than person labels.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `3-3-1` … `3-3-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 批判哲学、判断、先验统觉、知识学、自我/非我、设立、体系自由主义、根据、绝对者、辩证法、绝对精神、扬弃。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B11 Audit — 3-3 三级位置卡（3-3-1 … 3-3-4）

- batch_id: `W4-L3-B11-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 3，处理 `3-3` 生存论下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-3-1 | 存在主义（Beingism） | 234 | `knowledge/segment-cards/0234_3-3-1.md` | PASS |
| 3-3-2 | 真正的生存主义 | 239 | `knowledge/segment-cards/0239_3-3-2.md` | PASS |
| 3-3-3 | 同一生存论 | 244 | `knowledge/segment-cards/0244_3-3-3.md` | PASS |
| 3-3-4 | 虚构的生存论 | 249 | `knowledge/segment-cards/0249_3-3-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-3-1.md` | created | 存在主义（Beingism）；field=3 / ontology=3 / epistemology=1 |
| `knowledge/position-cards/3-3-2.md` | created | 真正的生存主义；field=3 / ontology=3 / epistemology=2 |
| `knowledge/position-cards/3-3-3.md` | created | 同一生存论；field=3 / ontology=3 / epistemology=3 |
| `knowledge/position-cards/3-3-4.md` | created | 虚构的生存论；field=3 / ontology=3 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 44/64 and total cards 64 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 44
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=44; new lengths 611/616/610/647
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish Beingism, Kierkegaardian choice, Nietzschean eternal return / will-to-power, and fictional/narrative existentialism as matrix mechanisms rather than lifestyle or identity labels.
- The 3-3 cards record finitude, mediation, decision, fiction, symbolization, narrative, and misrecognition as structural mechanisms, not as diagnostic categories for persons.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with `3-4-1` … `3-4-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: Beingism、此在、实存性、畏、真正的生存主义、抉择、质的辩证法、永恒轮回、权力意志、爱命运、虚构的生存论、叙事文本、符号身份。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B12 Audit — 3-4 三级位置卡（3-4-1 … 3-4-4）

- batch_id: `W4-L3-B12-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 3，处理 `3-4` 符号学下的四个三级位置，并完成 field 3 的 L3 draft coverage。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-4-1 | 结构主义 | 256 | `knowledge/segment-cards/0256_3-4-1.md` | PASS |
| 3-4-2 | 后结构主义 | 261 | `knowledge/segment-cards/0261_3-4-2.md` | PASS |
| 3-4-3 | 差异的辩证法 | 266 | `knowledge/segment-cards/0266_3-4-3.md` | PASS |
| 3-4-4 | 解释学 | 271 | `knowledge/segment-cards/0271_3-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-4-1.md` | created | 结构主义；field=3 / ontology=4 / epistemology=1 |
| `knowledge/position-cards/3-4-2.md` | created | 后结构主义；field=3 / ontology=4 / epistemology=2 |
| `knowledge/position-cards/3-4-3.md` | created | 差异的辩证法；field=3 / ontology=4 / epistemology=3 |
| `knowledge/position-cards/3-4-4.md` | created | 解释学；field=3 / ontology=4 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 48/64 and total cards 68 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 48
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=48; new lengths 591/633/627/606
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish structuralism, post-structuralism, differential dialectics, and hermeneutics as matrix mechanisms rather than universal explanatory keys.
- The 3-4 cards record signification, subjectivation, overdetermination, différance/decentering, horizon fusion, effective history, and hermeneutic circle as structural operations.
- L3 field 3 (`3-1-1` … `3-4-4`) is now complete at 16/16 draft cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 with field 4, likely `4-1-1` … `4-1-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 结构主义、共时性、意指关系、能指、所指、后结构主义、症候阅读、超定论、差异的辩证法、解构主义、解释学、视域融合、效果历史、解释学循环。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B13 Audit — 4-1 三级位置卡（4-1-1 … 4-1-4）

- batch_id: `W4-L3-B13-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 启动 W4-L3 field 4，处理 `4-1` 政治-经济-意识形态批判下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 4-1-1 | 资本主义史研究 | 279 | `knowledge/segment-cards/0279_4-1-1.md` | PASS |
| 4-1-2 | 灌输 | 284 | `knowledge/segment-cards/0284_4-1-2.md` | PASS |
| 4-1-3 | 历史的哲学化 | 289 | `knowledge/segment-cards/0289_4-1-3.md` | PASS |
| 4-1-4 | 精神化了的重复 | 294 | `knowledge/segment-cards/0294_4-1-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/4-1-1.md` | created | 资本主义史研究；field=4 / ontology=1 / epistemology=1 |
| `knowledge/position-cards/4-1-2.md` | created | 灌输；field=4 / ontology=1 / epistemology=2 |
| `knowledge/position-cards/4-1-3.md` | created | 历史的哲学化；field=4 / ontology=1 / epistemology=3 |
| `knowledge/position-cards/4-1-4.md` | created | 精神化了的重复；field=4 / ontology=1 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 52/64 and total cards 72 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 52
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=52; new lengths 669/647/703/740
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish capitalist historical research, indoctrination as a structural theory-education position, philosophical transformation of history, and spiritualized repetition after failed practical paradigms.
- The 4-1 cards explicitly preserve method boundaries: controversial mechanisms are recorded as matrix positions and usage boundaries, not endorsed as manipulation, diagnosis, or final theory.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 field 4 with `4-2-1` … `4-2-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 资本主义史研究、作为正题的 M 主义、灌输、理论家化、先生集群、历史的哲学化、卢卡奇主义、方法论总体化、精神化了的重复、危机常态化、事件重复、知识分子派别。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B14 Audit — 4-2 三级位置卡（4-2-1 … 4-2-4）

- batch_id: `W4-L3-B14-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 4，处理 `4-2` 现实的正统化下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 4-2-1 | 合律组织 | 301 | `knowledge/segment-cards/0301_4-2-1.md` | PASS |
| 4-2-2 | L主义 | 306 | `knowledge/segment-cards/0306_4-2-2.md` | PASS |
| 4-2-3 | 真正的国际主义 | 311 | `knowledge/segment-cards/0311_4-2-3.md` | PASS |
| 4-2-4 | 再来一次！ | 316 | `knowledge/segment-cards/0316_4-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/4-2-1.md` | created | 合律组织；field=4 / ontology=2 / epistemology=1 |
| `knowledge/position-cards/4-2-2.md` | created | L主义；field=4 / ontology=2 / epistemology=2 |
| `knowledge/position-cards/4-2-3.md` | created | 真正的国际主义；field=4 / ontology=2 / epistemology=3 |
| `knowledge/position-cards/4-2-4.md` | created | 再来一次！；field=4 / ontology=2 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 56/64 and total cards 76 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 56
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=56; new lengths 680/649/701/647
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish legal organization, L-ism/action mediation, true internationalism, and encore/repetition as matrix mechanisms under reality-orthodoxization.
- Controversial political/action materials are recorded only as structural historical positions with usage boundaries, not as practical instructions or normative endorsement.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 field 4 with `4-3-1` … `4-3-4` or another auditable 4-card batch.
2. Feed L3 candidate terms into W3 queue: 合律组织、合法性缝隙、L主义、窗口期、先锋中介、真正的国际主义、普遍主义空能指、无根性、再来一次、期待不可能性、失败性重复。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B15 Audit — 4-3 三级位置卡（4-3-1 … 4-3-4）

- batch_id: `W4-L3-B15-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L3 field 4，处理 `4-3` 建设理想社会下的四个三级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 4-3-1 | 生活必须品 | 322 | `knowledge/segment-cards/0322_4-3-1.md` | PASS |
| 4-3-2 | 对于生产活动的解放——要抢在历史惯性前头积极做出改变 | 327 | `knowledge/segment-cards/0327_4-3-2.md` | PASS |
| 4-3-3 | 战略-战役-战斗的统合 | 332 | `knowledge/segment-cards/0332_4-3-3.md` | PASS |
| 4-3-4 | s主义的资本实现 | 337 | `knowledge/segment-cards/0337_4-3-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/4-3-1.md` | created | 生活必须品；field=4 / ontology=3 / epistemology=1 |
| `knowledge/position-cards/4-3-2.md` | created | 对于生产活动的解放；field=4 / ontology=3 / epistemology=2 |
| `knowledge/position-cards/4-3-3.md` | created | 战略-战役-战斗的统合；field=4 / ontology=3 / epistemology=3 |
| `knowledge/position-cards/4-3-4.md` | created | s主义的资本实现；field=4 / ontology=3 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 60/64 and total cards 80 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 60
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=60; new lengths 619/715/637/662
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish living necessities/logistics, liberation of production activity, strategy-campaign-battle integration, and s-capital realization as construction mechanisms.
- Practical and strategic language is kept at ontology/method-description level; no operational instruction or normative endorsement is added.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L3 field 4 with `4-4-1` … `4-4-4`, completing L3 64/64.
2. Feed L3 candidate terms into W3 queue: 生活必须品、后勤学、生产活动的解放、历史惯性、战略-战役-战斗的统合、不可能性中介、s主义的资本实现、再生产模型、正当性。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L3-B16 Audit — 4-4 三级位置卡（4-4-1 … 4-4-4）

- batch_id: `W4-L3-B16-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 完成 W4-L3 field 4，处理 `4-4` 不可能的乌托邦下的四个三级位置，并完成 W4-L3 64/64 draft coverage。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 4-4-1 | 计划良好的人性生活方式 | 344 | `knowledge/segment-cards/0344_4-4-1.md` | PASS |
| 4-4-2 | 去人类中心化 | 349 | `knowledge/segment-cards/0349_4-4-2.md` | PASS |
| 4-4-3 | 对合／内卷 | 354 | `knowledge/segment-cards/0354_4-4-3.md` | PASS |
| 4-4-4 | 有序的深渊 | 359 | `knowledge/segment-cards/0359_4-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/4-4-1.md` | created | 计划良好的人性生活方式；field=4 / ontology=4 / epistemology=1 |
| `knowledge/position-cards/4-4-2.md` | created | 去人类中心化；field=4 / ontology=4 / epistemology=2 |
| `knowledge/position-cards/4-4-3.md` | created | 对合／内卷；field=4 / ontology=4 / epistemology=3 |
| `knowledge/position-cards/4-4-4.md` | created | 有序的深渊；field=4 / ontology=4 / epistemology=4 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L3 64/64 and total cards 84 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64; new lengths 672/652/589/614
git diff --check: PASS
```

### 4. Gate notes

- All four L3 cards declare `status: draft` and preserve row/segment traceability.
- Cards distinguish planned human lifestyle, de-human-centerization, involution, and ordered abyss as speculative boundary mechanisms under impossible utopia.
- AI/VR materials are recorded as ontology/symbol-system models only; no technical implementation or operational instruction was added.
- W4-L3 is now complete at 64/64 draft cards; this does not authorize canonical promotion.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Begin W4-L4 light cards in auditable batches, or continue W3 expansion toward ≥300 draft senses.
2. Feed L3 candidate terms into W3 queue: 计划良好的人性生活方式、欲望再生产、去人类中心化、主体间 VR、对合、内卷、AI身体化、有序的深渊、ordered chaos、间隙、乱步时间。
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B1 Audit — 1-1-1 / 1-1-2 四级轻卡（1-1-1-1 … 1-1-2-4）

- batch_id: `W4-L4-B1-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 启动 W4-L4 light cards，处理科学实在论下 `1-1-1` 与 `1-1-2` 的八个四级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-1-1-1 | 科学独断论 | 5 | `knowledge/segment-cards/0005_1-1-1-1.md` | PASS |
| 1-1-1-2 | 有机进化论 | 6 | `knowledge/segment-cards/0006_1-1-1-2.md` | PASS |
| 1-1-1-3 | 科学消费主义 | 7 | `knowledge/segment-cards/0007_1-1-1-3.md` | PASS |
| 1-1-1-4 | 宇宙悲观主义 | 8 | `knowledge/segment-cards/0008_1-1-1-4.md` | PASS |
| 1-1-2-1 | 科学知识社会学 | 10 | `knowledge/segment-cards/0010_1-1-2-1.md` | PASS |
| 1-1-2-2 | 科学革命论 | 11 | `knowledge/segment-cards/0011_1-1-2-2.md` | PASS |
| 1-1-2-3 | 文化本体论 | 12 | `knowledge/segment-cards/0012_1-1-2-3.md` | PASS |
| 1-1-2-4 | 解构建构论 | 13 | `knowledge/segment-cards/0013_1-1-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-1-1-1.md`–`1-1-1-4.md` | created | 物理主义下四个目的论位置 |
| `knowledge/position-cards/1-1-2-1.md`–`1-1-2-4.md` | created | 建构论下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 8 and total cards 92 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 8
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=8; new lengths 373/340/366/356/354/333/360/347
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Cards remain light, parent-linked, and mechanism-oriented; no W3/W5 canonical promotion was performed.
- project knowledge contract wording for L4 count remains recorded as 172 leaf-related light cards; this batch starts L4 without resolving the full selection policy beyond auditable TOC order.

### 5. Next W4 work

1. Continue W4-L4 from `1-1-3-1` … `1-1-4-4` or the next audited leaf batch.
2. Keep updating `knowledge/position-cards/index.md` and W4 audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B2 Audit — 1-1-3 / 1-1-4 四级轻卡（1-1-3-1 … 1-1-4-4）

- batch_id: `W4-L4-B2-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理科学实在论下 `1-1-3` 与 `1-1-4` 的八个四级位置，完成 `1-1` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-1-3-1 | 功能主义 | 15 | `knowledge/segment-cards/0015_1-1-3-1.md` | PASS |
| 1-1-3-2 | 自由进化论 | 16 | `knowledge/segment-cards/0016_1-1-3-2.md` | PASS |
| 1-1-3-3 | 认知自我主义 | 17 | `knowledge/segment-cards/0017_1-1-3-3.md` | PASS |
| 1-1-3-4 | 认知无我论 | 18 | `knowledge/segment-cards/0018_1-1-3-4.md` | PASS |
| 1-1-4-1 | 操作行为主义 | 20 | `knowledge/segment-cards/0020_1-1-4-1.md` | PASS |
| 1-1-4-2 | 目的行为主义 | 21 | `knowledge/segment-cards/0021_1-1-4-2.md` | PASS |
| 1-1-4-3 | 应用行为分析 | 22 | `knowledge/segment-cards/0022_1-1-4-3.md` | PASS |
| 1-1-4-4 | 社会行为主义 | 23 | `knowledge/segment-cards/0023_1-1-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-1-3-1.md`–`1-1-3-4.md` | created | 认知主义下四个目的论位置 |
| `knowledge/position-cards/1-1-4-1.md`–`1-1-4-4.md` | created | 行为主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 16 and total cards 100 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 16
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=16; new lengths 343/337/359/361/349/355/344/360
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Cards keep behaviorist clinical/application language at structure-level and avoid prohibited person-label/diagnostic wording.
- `1-1` L4 subtree is now complete at 16 draft cards; no canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `1-2-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B3 Audit — 1-2-1 / 1-2-2 四级轻卡（1-2-1-1 … 1-2-2-4）

- batch_id: `W4-L4-B3-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理宗教实在论下 `1-2-1` 与 `1-2-2` 的八个四级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-2-1-1 | 自然神论 | 27 | `knowledge/segment-cards/0027_1-2-1-1.md` | PASS |
| 1-2-1-2 | 神义论 | 28 | `knowledge/segment-cards/0028_1-2-1-2.md` | PASS |
| 1-2-1-3 | 一元论诺斯替主义 | 29 | `knowledge/segment-cards/0029_1-2-1-3.md` | PASS |
| 1-2-1-4 | 模态位格一元论 | 30 | `knowledge/segment-cards/0030_1-2-1-4.md` | PASS |
| 1-2-2-1 | 传殖主义 | 32 | `knowledge/segment-cards/0032_1-2-2-1.md` | PASS |
| 1-2-2-2 | 部分主义 | 33 | `knowledge/segment-cards/0033_1-2-2-2.md` | PASS |
| 1-2-2-3 | 拜物教——读懂资本论的必修课：物神崇拜的符号学功能；偶像崇拜的第三种形式 | 34 | `knowledge/segment-cards/0034_1-2-2-3.md` | PASS |
| 1-2-2-4 | 时间崇拜——偶像崇拜的终极形式：论时间之神 Aion、狄奥尼索斯与奥菲欧斯的三位一体，节庆、永恒、往生、死亡崇拜背后的意识形态机制 | 35 | `knowledge/segment-cards/0035_1-2-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-2-1-1.md`–`1-2-1-4.md` | created | 神创论下四个目的论位置 |
| `knowledge/position-cards/1-2-2-1.md`–`1-2-2-4.md` | created | 偶像论／偶像崇拜下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 24 and total cards 108 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 24
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=24; new lengths 358/339/381/363/353/359/485/546
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- The batch distinguishes神创论的始因/神义/诺斯替/位格结构 from偶像论的传承、部分化、物神和时间崇拜 mechanisms.
- Source segment language that belongs to diagnostic or person-label registers was not imported into the new position cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `1-2-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B4 Audit — 1-2-3 / 1-2-4 四级轻卡（1-2-3-1 … 1-2-4-4）

- batch_id: `W4-L4-B4-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理宗教实在论下 `1-2-3` 与 `1-2-4` 的八个四级位置，并完成 `1-2` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-2-3-1 | 永生主义 | 37 | `knowledge/segment-cards/0037_1-2-3-1.md` | PASS |
| 1-2-3-2 | 回归式唯灵论 | 38 | `knowledge/segment-cards/0038_1-2-3-2.md` | PASS |
| 1-2-3-3 | 魔法师主义 | 39 | `knowledge/segment-cards/0039_1-2-3-3.md` | PASS |
| 1-2-3-4 | 弃绝主义 | 40 | `knowledge/segment-cards/0040_1-2-3-4.md` | PASS |
| 1-2-4-1 | 作为信仰的命定论 | 42 | `knowledge/segment-cards/0042_1-2-4-1.md` | PASS |
| 1-2-4-2 | 救世主主义 | 43 | `knowledge/segment-cards/0043_1-2-4-2.md` | PASS |
| 1-2-4-3 | 神智论 | 44 | `knowledge/segment-cards/0044_1-2-4-3.md` | PASS |
| 1-2-4-4 | 神爱论，神圣的爱 | 45 | `knowledge/segment-cards/0045_1-2-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-2-3-1.md`–`1-2-3-4.md` | created | 唯灵论下四个目的论位置 |
| `knowledge/position-cards/1-2-4-1.md`–`1-2-4-4.md` | created | 反偶像论下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 32 and total cards 116 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 32
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=32; new lengths 419/386/424/409/388/443/339/421
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Subtitles and source language with clinical/person-label flavor were not imported into the card titles or interpretive body; cards remain mechanism- and position-oriented.
- `1-2` 宗教实在论 L4 subtree is now complete at 16 draft light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `1-3-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B5 Audit — 1-3-1 / 1-3-2 四级轻卡（1-3-1-1 … 1-3-2-4）

- batch_id: `W4-L4-B5-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理庸俗唯我论下 `1-3-1` 与 `1-3-2` 的八个四级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-3-1-1 | 客观唯心主义 | 48 | `knowledge/segment-cards/0048_1-3-1-1.md` | PASS |
| 1-3-1-2 | 主观唯心主义 | 49 | `knowledge/segment-cards/0049_1-3-1-2.md` | PASS |
| 1-3-1-3 | 现实唯心主义 | 50 | `knowledge/segment-cards/0050_1-3-1-3.md` | PASS |
| 1-3-1-4 | 唯梦论 | 51 | `knowledge/segment-cards/0051_1-3-1-4.md` | PASS |
| 1-3-2-1 | 现代斯多亚主义 | 53 | `knowledge/segment-cards/0053_1-3-2-1.md` | PASS |
| 1-3-2-2 | 现代犬儒主义 | 54 | `knowledge/segment-cards/0054_1-3-2-2.md` | PASS |
| 1-3-2-3 | 现代爱情主义／现代新柏拉图主义 | 55 | `knowledge/segment-cards/0055_1-3-2-3.md` | PASS |
| 1-3-2-4 | 现代智者主义 | 56 | `knowledge/segment-cards/0056_1-3-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-3-1-1.md`–`1-3-1-4.md` | created | 伪唯心主义下四个目的论位置 |
| `knowledge/position-cards/1-3-2-1.md`–`1-3-2-4.md` | created | 本真主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 40 and total cards 124 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 40
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=40; new lengths 430/424/399/415/431/434/456/402
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical subtitles and insulting source phrasing were not imported into the card titles or interpretive summaries; cards remain structural and mechanism-focused.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `1-3-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B6 Audit — 1-3-3 / 1-3-4 四级轻卡（1-3-3-1 … 1-3-4-4）

- batch_id: `W4-L4-B6-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理庸俗唯我论下 `1-3-3` 与 `1-3-4` 的八个四级位置，并完成 `1-3` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-3-3-1 | 自我中心主义 | 58 | `knowledge/segment-cards/0058_1-3-3-1.md` | PASS |
| 1-3-3-2 | 道德严酷主义 | 59 | `knowledge/segment-cards/0059_1-3-3-2.md` | PASS |
| 1-3-3-3 | 排他的集体主义 | 60 | `knowledge/segment-cards/0060_1-3-3-3.md` | PASS |
| 1-3-3-4 | 厌女—虚无主义 | 61 | `knowledge/segment-cards/0061_1-3-3-4.md` | PASS |
| 1-3-4-1 | 伦理行动主义 | 63 | `knowledge/segment-cards/0063_1-3-4-1.md` | PASS |
| 1-3-4-2 | 随笔主义 | 64 | `knowledge/segment-cards/0064_1-3-4-2.md` | PASS |
| 1-3-4-3 | 唯美主义 | 65 | `knowledge/segment-cards/0065_1-3-4-3.md` | PASS |
| 1-3-4-4 | 颓废主义 | 66 | `knowledge/segment-cards/0066_1-3-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-3-3-1.md`–`1-3-3-4.md` | created | 唯意志主义下四个目的论位置 |
| `knowledge/position-cards/1-3-4-1.md`–`1-3-4-4.md` | created | 直觉主义／体验主义／意识流下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 48 and total cards 132 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 48
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=48; new lengths 452/447/449/468/406/452/368/391
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Potential person-label and polemical source wording was converted into structure-level mechanism descriptions; no diagnostic/personality language was introduced.
- `1-3` 庸俗唯我论 subtree is now complete at 16 draft light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `1-4-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B7 Audit — 1-4-1 / 1-4-2 四级轻卡（1-4-1-1 … 1-4-2-4）

- batch_id: `W4-L4-B7-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理平庸主义下 `1-4-1` 与 `1-4-2` 的八个四级位置。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-4-1-1 | 和平主义 | 77 | `knowledge/segment-cards/0077_1-4-1-1.md` | PASS |
| 1-4-1-2 | 客观主义 | 78 | `knowledge/segment-cards/0078_1-4-1-2.md` | PASS |
| 1-4-1-3 | 沉默主义 | 79 | `knowledge/segment-cards/0079_1-4-1-3.md` | PASS |
| 1-4-1-4 | 蒙昧主义 | 80 | `knowledge/segment-cards/0080_1-4-1-4.md` | PASS |
| 1-4-2-1 | 纵容主义 | 82 | `knowledge/segment-cards/0082_1-4-2-1.md` | PASS |
| 1-4-2-2 | 多元文化主义 | 83 | `knowledge/segment-cards/0083_1-4-2-2.md` | PASS |
| 1-4-2-3 | 环保主义 | 84 | `knowledge/segment-cards/0084_1-4-2-3.md` | PASS |
| 1-4-2-4 | 性解放主义 | 85 | `knowledge/segment-cards/0085_1-4-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-4-1-1.md`–`1-4-1-4.md` | created | 当代自然主义下四个目的论位置 |
| `knowledge/position-cards/1-4-2-1.md`–`1-4-2-4.md` | created | 世俗人道主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 56 and total cards 140 |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 56
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=56; new lengths 440/454/422/457/442/434/458/456
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Politically polemical subtitles were converted into structural mechanism descriptions; no person-diagnostic framing was introduced.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `1-4-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B8 Audit — 1-4-3 / 1-4-4 四级轻卡（1-4-3-1 … 1-4-4-4）

- batch_id: `W4-L4-B8-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理平庸主义下 `1-4-3` 与 `1-4-4` 的八个四级位置，并完成 field 1 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 1-4-3-1 | 情绪主义 | 87 | `knowledge/segment-cards/0087_1-4-3-1.md` | PASS |
| 1-4-3-2 | 心理正常主义 | 88 | `knowledge/segment-cards/0088_1-4-3-2.md` | PASS |
| 1-4-3-3 | 泛性主义 | 89 | `knowledge/segment-cards/0089_1-4-3-3.md` | PASS |
| 1-4-3-4 | 密契女性主义 | 90 | `knowledge/segment-cards/0090_1-4-3-4.md` | PASS |
| 1-4-4-1 | 顺从主义 | 92 | `knowledge/segment-cards/0092_1-4-4-1.md` | PASS |
| 1-4-4-2 | 粗俗主义 | 93 | `knowledge/segment-cards/0093_1-4-4-2.md` | PASS |
| 1-4-4-3 | 四重竞争主义 | 94 | `knowledge/segment-cards/0094_1-4-4-3.md` | PASS |
| 1-4-4-4 | 复仇主义 | 95 | `knowledge/segment-cards/0095_1-4-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/1-4-3-1.md`–`1-4-3-4.md` | created | 心理主义下四个目的论位置 |
| `knowledge/position-cards/1-4-4-1.md`–`1-4-4-4.md` | created | 庸俗主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 64 and total cards 148; field 1 L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 64
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=64; new lengths 424/448/400/485/416/413/417/436
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Potentially person-diagnostic or polemical source phrases were converted to structure-level mechanism descriptions.
- Field 1 L4 draft coverage is complete at 64 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-1-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B9 Audit — 2-1-1 / 2-1-2 四级轻卡（2-1-1-1 … 2-1-2-4）

- batch_id: `W4-L4-B9-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理在场形而上学下 `2-1-1` 与 `2-1-2` 的八个四级位置，并启动 field 2 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-1-1-1 | 阿派朗（无界限）主义 | 99 | `knowledge/segment-cards/0099_2-1-1-1.md` | PASS |
| 2-1-1-2 | 气动一元论 | 100 | `knowledge/segment-cards/0100_2-1-1-2.md` | PASS |
| 2-1-1-3 | 分形多元论 | 101 | `knowledge/segment-cards/0101_2-1-1-3.md` | PASS |
| 2-1-1-4 | 形而上辩证主义 | 102 | `knowledge/segment-cards/0102_2-1-1-4.md` | PASS |
| 2-1-2-1 | 伦理智性主义 | 104 | `knowledge/segment-cards/0104_2-1-2-1.md` | PASS |
| 2-1-2-2 | 理念实在论／理想现实主义 | 105 | `knowledge/segment-cards/0105_2-1-2-2.md` | PASS |
| 2-1-2-3 | 范畴实在论／绝对现实主义 | 106 | `knowledge/segment-cards/0106_2-1-2-3.md` | PASS |
| 2-1-2-4 | 多产的不动论 | 107 | `knowledge/segment-cards/0107_2-1-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-1-1-1.md`–`2-1-1-4.md` | created | 普遍主义下四个目的论位置 |
| `knowledge/position-cards/2-1-2-1.md`–`2-1-2-4.md` | created | 本质主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 72 and total cards 156; field 2 L4 coverage started |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 72
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=72; new lengths 507/491/529/514/526/522/533/498
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical source subtitles were converted to structure-level mechanism descriptions.
- Field 2 L4 draft coverage is now started through `2-1-2`.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-1-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B10 Audit — 2-1-3 / 2-1-4 四级轻卡（2-1-3-1 … 2-1-4-4）

- batch_id: `W4-L4-B10-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理在场形而上学下 `2-1-3` 与 `2-1-4` 的八个四级位置，并完成 `2-1` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-1-3-1 | 反应多元论 | 109 | `knowledge/segment-cards/0109_2-1-3-1.md` | PASS |
| 2-1-3-2 | 贫乏的原子论 | 110 | `knowledge/segment-cards/0110_2-1-3-2.md` | PASS |
| 2-1-3-3 | 智性享乐主义 | 111 | `knowledge/segment-cards/0111_2-1-3-3.md` | PASS |
| 2-1-3-4 | 犬儒主义 | 112 | `knowledge/segment-cards/0112_2-1-3-4.md` | PASS |
| 2-1-4-1 | 相对主义 | 114 | `knowledge/segment-cards/0114_2-1-4-1.md` | PASS |
| 2-1-4-2 | 怀疑主义 | 115 | `knowledge/segment-cards/0115_2-1-4-2.md` | PASS |
| 2-1-4-3 | 记忆主义 | 116 | `knowledge/segment-cards/0116_2-1-4-3.md` | PASS |
| 2-1-4-4 | 话语主义 | 117 | `knowledge/segment-cards/0117_2-1-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-1-3-1.md`–`2-1-3-4.md` | created | 合理主义下四个目的论位置 |
| `knowledge/position-cards/2-1-4-1.md`–`2-1-4-4.md` | created | 绝对主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 80 and total cards 164; `2-1` L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 80
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=80; new lengths 480/485/483/524/483/492/496/510
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical source subtitles were converted to structure-level mechanism descriptions.
- `2-1` 在场形而上学 subtree L4 draft coverage is complete at 16 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-2-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B11 Audit — 2-2-1 / 2-2-2 四级轻卡（2-2-1-1 … 2-2-2-4）

- batch_id: `W4-L4-B11-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理辩证形而上学下 `2-2-1` 与 `2-2-2` 的八个四级位置，并启动 `2-2` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row(s) | segment card(s) | verdict |
|---|---|---:|---|---|
| 2-2-1-1 | 分子业力主义 | 121 | `knowledge/segment-cards/0121_2-2-1-1.md` | PASS |
| 2-2-1-2 | 永恒时态主义 | 122 | `knowledge/segment-cards/0122_2-2-1-2.md` | PASS |
| 2-2-1-3 | 灵魂示踪主义／种子形而上学 | 123 | `knowledge/segment-cards/0123_2-2-1-3.md` | PASS |
| 2-2-1-4 | 摩尔唯心主义 | 124 | `knowledge/segment-cards/0124_2-2-1-4.md` | PASS |
| 2-2-2-1 | 无为主义 | 126 | `knowledge/segment-cards/0126_2-2-2-1.md` | PASS |
| 2-2-2-2 | 积极的神秘主义 | 128, 129, 131 | `knowledge/segment-cards/0128_2-2-2-2.md`; `0129_2-2-2-2.md`; `0131_2-2-2-2.md` | PASS |
| 2-2-2-3 | 人道的自然主义 | 132 | `knowledge/segment-cards/0132_2-2-2-3.md` | PASS |
| 2-2-2-4 | 实用的神秘主义 | 133 | `knowledge/segment-cards/0133_2-2-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-2-1-1.md`–`2-2-1-4.md` | created | 无限主义下四个目的论位置 |
| `knowledge/position-cards/2-2-2-1.md`–`2-2-2-4.md` | created | 否定主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 88 and total cards 172; `2-2` L4 draft coverage started |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 88
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=88; new lengths 507/474/498/475/404/448/441/479
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Row `127` and `130` auxiliary/duplicate `toc_id: None` segment cards were not used as primary position evidence; `2-2-2-2` records all three titled source rows (`128`, `129`, `131`).
- Polemical source wording was converted to structure-level mechanism descriptions.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-2-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B12 Audit — 2-2-3 / 2-2-4 四级轻卡（2-2-3-1 … 2-2-4-4）

- batch_id: `W4-L4-B12-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理辩证形而上学下 `2-2-3` 与 `2-2-4` 的八个四级位置，并完成 `2-2` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-2-3-1 | 历史符号主义 | 135 | `knowledge/segment-cards/0135_2-2-3-1.md` | PASS |
| 2-2-3-2 | 形而上神秘主义 | 136 | `knowledge/segment-cards/0136_2-2-3-2.md` | PASS |
| 2-2-3-3 | 理性唯灵论 | 137 | `knowledge/segment-cards/0137_2-2-3-3.md` | PASS |
| 2-2-3-4 | 诗的形而上学 | 138 | `knowledge/segment-cards/0138_2-2-3-4.md` | PASS |
| 2-2-4-1 | 具有伦理热忱的虚无主义 | 140 | `knowledge/segment-cards/0140_2-2-4-1.md` | PASS |
| 2-2-4-2 | 可辩的道德箴言 | 141 | `knowledge/segment-cards/0141_2-2-4-2.md` | PASS |
| 2-2-4-3 | 新实用主义 | 142 | `knowledge/segment-cards/0142_2-2-4-3.md` | PASS |
| 2-2-4-4 | 原始的现象学／分析哲学 | 143 | `knowledge/segment-cards/0143_2-2-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-2-3-1.md`–`2-2-3-4.md` | created | 超验主义下四个目的论位置 |
| `knowledge/position-cards/2-2-4-1.md`–`2-2-4-4.md` | created | 反二元对立下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 96 and total cards 180; `2-2` L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 96
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=96; new lengths 456/510/506/493/504/445/475/511
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical source wording was converted to structure-level mechanism descriptions.
- `2-2` 辩证形而上学 subtree L4 draft coverage is complete at 16 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-3-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B13 Audit — 2-3-1 / 2-3-2 四级轻卡（2-3-1-1 … 2-3-2-4）

- batch_id: `W4-L4-B13-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理我思形而上学下 `2-3-1` 与 `2-3-2` 的八个四级位置，并启动 `2-3` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-3-1-1 | 渐进无限主义 | 147 | `knowledge/segment-cards/0147_2-3-1-1.md` | PASS |
| 2-3-1-2 | 运动的静止主义 | 148 | `knowledge/segment-cards/0148_2-3-1-2.md` | PASS |
| 2-3-1-3 | 实体整体主义 | 149 | `knowledge/segment-cards/0149_2-3-1-3.md` | PASS |
| 2-3-1-4 | 辩证一元论 | 150 | `knowledge/segment-cards/0150_2-3-1-4.md` | PASS |
| 2-3-2-1 | 理性动物主义 | 152 | `knowledge/segment-cards/0152_2-3-2-1.md` | PASS |
| 2-3-2-2 | 理性神秘主义 | 153 | `knowledge/segment-cards/0153_2-3-2-2.md` | PASS |
| 2-3-2-3 | 超越的内在论 | 154 | `knowledge/segment-cards/0154_2-3-2-3.md` | PASS |
| 2-3-2-4 | 现代理性主义 | 155 | `knowledge/segment-cards/0155_2-3-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-3-1-1.md`–`2-3-1-4.md` | created | 实体一元论下四个目的论位置 |
| `knowledge/position-cards/2-3-2-1.md`–`2-3-2-4.md` | created | 心物二元论下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 104 and total cards 188; `2-3` L4 draft coverage started |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 104
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=104; new lengths 466/456/449/430/441/452/447/457
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical source wording was converted to structure-level mechanism descriptions.
- `2-3` 我思形而上学 subtree L4 draft coverage is now started through `2-3-2`.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-3-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B14 Audit — 2-3-3 / 2-3-4 四级轻卡（2-3-3-1 … 2-3-4-4）

- batch_id: `W4-L4-B14-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理我思形而上学下 `2-3-3` 与 `2-3-4` 的八个四级位置，并完成 `2-3` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-3-3-1 | 前定主义 | 157 | `knowledge/segment-cards/0157_2-3-3-1.md` | PASS |
| 2-3-3-2 | 体系完美主义 | 158 | `knowledge/segment-cards/0158_2-3-3-2.md` | PASS |
| 2-3-3-3 | 逻辑原子主义 | 159 | `knowledge/segment-cards/0159_2-3-3-3.md` | PASS |
| 2-3-3-4 | 分割的整体主义 | 160 | `knowledge/segment-cards/0160_2-3-3-4.md` | PASS |
| 2-3-4-1 | 数理还原主义 | 162 | `knowledge/segment-cards/0162_2-3-4-1.md` | PASS |
| 2-3-4-2 | 稳定的干涉主义 | 163 | `knowledge/segment-cards/0163_2-3-4-2.md` | PASS |
| 2-3-4-3 | 物理归纳主义 | 164 | `knowledge/segment-cards/0164_2-3-4-3.md` | PASS |
| 2-3-4-4 | 时空绝对主义 | 165 | `knowledge/segment-cards/0165_2-3-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-3-3-1.md`–`2-3-3-4.md` | created | 单子主义下四个目的论位置 |
| `knowledge/position-cards/2-3-4-1.md`–`2-3-4-4.md` | created | 宇宙平等主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 112 and total cards 196; `2-3` L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 112
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=112; new lengths 490/492/478/475/474/489/457/464
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical source wording was converted to structure-level mechanism descriptions.
- `2-3` 我思形而上学 subtree L4 draft coverage is complete at 16 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-4-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B15 Audit — 2-4-1 / 2-4-2 四级轻卡（2-4-1-1 … 2-4-2-4）

- batch_id: `W4-L4-B15-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理反形而上学下 `2-4-1` 与 `2-4-2` 的八个四级位置，并启动 `2-4` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-4-1-1 | 乐于接受的小体主义 | 168 | `knowledge/segment-cards/0168_2-4-1-1.md` | PASS |
| 2-4-1-2 | 经验的观念论 | 169 | `knowledge/segment-cards/0169_2-4-1-2.md` | PASS |
| 2-4-1-3 | 理念-精神二元论 | 170 | `knowledge/segment-cards/0170_2-4-1-3.md` | PASS |
| 2-4-1-4 | 人类有限主义 | 171 | `knowledge/segment-cards/0171_2-4-1-4.md` | PASS |
| 2-4-2-1 | 自然主义的规范论 | 173 | `knowledge/segment-cards/0173_2-4-2-1.md` | PASS |
| 2-4-2-2 | 社会实证主义 | 174 | `knowledge/segment-cards/0174_2-4-2-2.md` | PASS |
| 2-4-2-3 | 自然神论的实证主义 | 175 | `knowledge/segment-cards/0175_2-4-2-3.md` | PASS |
| 2-4-2-4 | 科学的实证主义 | 176 | `knowledge/segment-cards/0176_2-4-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-4-1-1.md`–`2-4-1-4.md` | created | 经验主义下四个目的论位置 |
| `knowledge/position-cards/2-4-2-1.md`–`2-4-2-4.md` | created | 实证主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 120 and total cards 204; `2-4` L4 draft coverage started |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 120
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=120; new lengths 498/509/507/454/539/515/531/512
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Row 176 remains recovered and traceable; no raw/clean corpus mutation was performed.
- Polemical source wording was converted to structure-level mechanism descriptions.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `2-4-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B16 Audit — 2-4-3 / 2-4-4 四级轻卡（2-4-3-1 … 2-4-4-4）

- batch_id: `W4-L4-B16-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理反形而上学下 `2-4-3` 与 `2-4-4` 的八个四级位置，并完成 field 2 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 2-4-3-1 | 相对语法主义 | 178 | `knowledge/segment-cards/0178_2-4-3-1.md` | PASS |
| 2-4-3-2 | 逻辑还原主义 | 179 | `knowledge/segment-cards/0179_2-4-3-2.md` | PASS |
| 2-4-3-3 | 逻辑行为主义 | 180 | `knowledge/segment-cards/0180_2-4-3-3.md` | PASS |
| 2-4-3-4 | 逻辑反实在论 | 181 | `knowledge/segment-cards/0181_2-4-3-4.md` | PASS |
| 2-4-4-1 | 逻辑实用主义 | 183 | `knowledge/segment-cards/0183_2-4-4-1.md` | PASS |
| 2-4-4-2 | 正统辩证唯物主义 | 184 | `knowledge/segment-cards/0184_2-4-4-2.md` | PASS |
| 2-4-4-3 | 符号实用主义 | 185 | `knowledge/segment-cards/0185_2-4-4-3.md` | PASS |
| 2-4-4-4 | 生存实用主义 | 186 | `knowledge/segment-cards/0186_2-4-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/2-4-3-1.md`–`2-4-3-4.md` | created | 逻辑实证主义下四个目的论位置 |
| `knowledge/position-cards/2-4-4-1.md`–`2-4-4-4.md` | created | 实用主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 128 and total cards 212; fields 1 and 2 L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 128
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=128; new lengths 559/528/523/539/558/568/571/528
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- `2-4-4-3` keeps `语言` under 待继续拆分 only; W3-collected terms under 已收录 remain limited to existing W3 entries.
- Polemical source wording was converted to structure-level mechanism descriptions; no clinical/person-diagnostic labels were introduced.
- Field 2 L4 draft coverage is complete at 64 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `3-1-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B17 Audit — 3-1-1 / 3-1-2 四级轻卡（3-1-1-1 … 3-1-2-4）

- batch_id: `W4-L4-B17-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理现象学下 `3-1-1` 与 `3-1-2` 的八个四级位置，并启动 field 3 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-1-1-1 | 先验直觉主义 | 191 | `knowledge/segment-cards/0191_3-1-1-1.md` | PASS |
| 3-1-1-2 | 先验本质主义 | 192 | `knowledge/segment-cards/0192_3-1-1-2.md` | PASS |
| 3-1-1-3 | 反思性的主体主义 | 193 | `knowledge/segment-cards/0193_3-1-1-3.md` | PASS |
| 3-1-1-4 | 准先验辩证主义 | 194 | `knowledge/segment-cards/0194_3-1-1-4.md` | PASS |
| 3-1-2-1 | 媒介性的客观主义 | 196 | `knowledge/segment-cards/0196_3-1-2-1.md` | PASS |
| 3-1-2-2 | 本质心理主义 | 197 | `knowledge/segment-cards/0197_3-1-2-2.md` | PASS |
| 3-1-2-3 | 现象学的唯美主义 | 198 | `knowledge/segment-cards/0198_3-1-2-3.md` | PASS |
| 3-1-2-4 | 游戏的世界象征主义 | 199 | `knowledge/segment-cards/0199_3-1-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-1-1-1.md`–`3-1-1-4.md` | created | 先验现象学下四个目的论位置 |
| `knowledge/position-cards/3-1-2-1.md`–`3-1-2-4.md` | created | 实事现象学下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 136 and total cards 220; `3-1` L4 draft coverage started through `3-1-2` |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 136
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=136; new lengths 528/449/503/469/483/504/515/474
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Potentially clinical-sounding source vocabulary in row 197 was converted to structure-level discussion of belief/psychological structure; no person-diagnostic frame was introduced.
- W3-collected terms under 已收录 remain limited to existing W3 entries; new terms remain under 待继续拆分.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `3-1-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B18 Audit — 3-1-3 / 3-1-4 四级轻卡（3-1-3-1 … 3-1-4-4）

- batch_id: `W4-L4-B18-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理现象学下 `3-1-3` 与 `3-1-4` 的八个四级位置，并完成 `3-1` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-1-3-1 | 主体间普遍主义 | 201 | `knowledge/segment-cards/0201_3-1-3-1.md` | PASS |
| 3-1-3-2 | 本土方法论 | 202 | `knowledge/segment-cards/0202_3-1-3-2.md` | PASS |
| 3-1-3-3 | 格式塔现象学 | 203 | `knowledge/segment-cards/0203_3-1-3-3.md` | PASS |
| 3-1-3-4 | 自身性现象学 | 204 | `knowledge/segment-cards/0204_3-1-3-4.md` | PASS |
| 3-1-4-1 | 追问的现象学 | 206 | `knowledge/segment-cards/0206_3-1-4-1.md` | PASS |
| 3-1-4-2 | 性化的现象学 | 207 | `knowledge/segment-cards/0207_3-1-4-2.md` | PASS |
| 3-1-4-3 | 存在论的现象学 | 208 | `knowledge/segment-cards/0208_3-1-4-3.md` | PASS |
| 3-1-4-4 | 现象学伦理主义 | 209 | `knowledge/segment-cards/0209_3-1-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-1-3-1.md`–`3-1-3-4.md` | created | 生活世界现象学下四个目的论位置 |
| `knowledge/position-cards/3-1-4-1.md`–`3-1-4-4.md` | created | 现世的现象学下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 144 and total cards 228; `3-1` L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 144
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=144; new lengths 465/462/481/499/487/515/497/478
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Source wording on sexuality, selfhood, and ordinary life was converted to structural body/otherness/time descriptions.
- W3-collected terms under 已收录 remain limited to existing W3 entries; `语言` remains outside 已收录.
- `3-1` 现象学 subtree L4 draft coverage is complete at 16 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `3-2-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B19 Audit — 3-2-1 / 3-2-2 四级轻卡（3-2-1-1 … 3-2-2-4）

- batch_id: `W4-L4-B19-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理德国观念论下 `3-2-1` 与 `3-2-2` 的八个四级位置，并启动 `3-2` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-2-1-1 | 无限的有限主义 | 213 | `knowledge/segment-cards/0213_3-2-1-1.md` | PASS |
| 3-2-1-2 | 先验经验主义 | 214 | `knowledge/segment-cards/0214_3-2-1-2.md` | PASS |
| 3-2-1-3 | 先验逻辑主义 | 215 | `knowledge/segment-cards/0215_3-2-1-3.md` | PASS |
| 3-2-1-4 | 符号形式主义 | 216 | `knowledge/segment-cards/0216_3-2-1-4.md` | PASS |
| 3-2-2-1 | 理智直观主义 | 218 | `knowledge/segment-cards/0218_3-2-2-1.md` | PASS |
| 3-2-2-2 | 先验观念论 | 219 | `knowledge/segment-cards/0219_3-2-2-2.md` | PASS |
| 3-2-2-3 | 彻底的经验主义 | 220 | `knowledge/segment-cards/0220_3-2-2-3.md` | PASS |
| 3-2-2-4 | 唯我的实在论、现实主义 | 221 | `knowledge/segment-cards/0221_3-2-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-2-1-1.md`–`3-2-1-4.md` | created | 批判哲学下四个目的论位置 |
| `knowledge/position-cards/3-2-2-1.md`–`3-2-2-4.md` | created | 知识学下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 152 and total cards 236; `3-2` L4 draft coverage started through `3-2-2` |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 152
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=152; new lengths 494/493/463/486/487/485/513/519
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Polemical source phrasing was converted to structure-level descriptions of finite reason, process, logic, symbol form, self-positing, experience, and logical space.
- W3-collected terms under 已收录 remain limited to existing W3 entries; new candidate terms remain under 待继续拆分.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `3-2-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B20 Audit — 3-2-3 / 3-2-4 四级轻卡（3-2-3-1 … 3-2-4-4）

- batch_id: `W4-L4-B20-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理德国观念论下 `3-2-3` 与 `3-2-4` 的八个四级位置，并完成 `3-2` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-2-3-1 | 时间-本体论 | 223 | `knowledge/segment-cards/0223_3-2-3-1.md` | PASS |
| 3-2-3-2 | 加倍的德国观念论 | 224 | `knowledge/segment-cards/0224_3-2-3-2.md` | PASS |
| 3-2-3-3 | 生存论的存在主义 | 225 | `knowledge/segment-cards/0225_3-2-3-3.md` | PASS |
| 3-2-3-4 | 自身-辩证法 | 226 | `knowledge/segment-cards/0226_3-2-3-4.md` | PASS |
| 3-2-4-1 | 逻辑学 | 228 | `knowledge/segment-cards/0228_3-2-4-1.md` | PASS |
| 3-2-4-2 | 否定辩证法 | 229 | `knowledge/segment-cards/0229_3-2-4-2.md` | PASS |
| 3-2-4-3 | 爱欲辩证法 | 230 | `knowledge/segment-cards/0230_3-2-4-3.md` | PASS |
| 3-2-4-4 | 意识形态学 | 231 | `knowledge/segment-cards/0231_3-2-4-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-2-3-1.md`–`3-2-3-4.md` | created | 体系自由主义下四个目的论位置 |
| `knowledge/position-cards/3-2-4-1.md`–`3-2-4-4.md` | created | 辩证法下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 160 and total cards 244; `3-2` L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 160
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=160; new lengths 507/514/499/497/461/453/473/483
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Content was framed as structure-level relations among time, ontology, matter, Seyn, dialectic, logic, negativity, Eros, and ideology.
- W3-collected terms under 已收录 remain limited to existing W3 entries; `语言` remains outside 已收录.
- `3-2` 德国观念论 subtree L4 draft coverage is complete at 16 light cards.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `3-3-1-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B21 Audit — 3-3-1 / 3-3-2 四级轻卡（3-3-1-1 … 3-3-2-4）

- batch_id: `W4-L4-B21-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理生存论下 `3-3-1` 与 `3-3-2` 的八个四级位置，并完成 `3-3-1` 与 `3-3-2` subtree 的 L4 draft 覆盖。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-3-1-1 | 分环节的生存论的存在论 | 235 | `knowledge/segment-cards/0235_3-3-1-1.md` | PASS |
| 3-3-1-2 | 人道主义的存在主义 | 236 | `knowledge/segment-cards/0236_3-3-1-2.md` | PASS |
| 3-3-1-3 | 政治的理性主义 | 237 | `knowledge/segment-cards/0237_3-3-1-3.md` | PASS |
| 3-3-1-4 | 前本体论 | 238 | `knowledge/segment-cards/0238_3-3-1-4.md` | PASS |
| 3-3-2-1 | 安放了的实存主义 | 240 | `knowledge/segment-cards/0240_3-3-2-1.md` | PASS |
| 3-3-2-2 | 诗性存在论 | 241 | `knowledge/segment-cards/0241_3-3-2-2.md` | PASS |
| 3-3-2-3 | 神-人伦理学 | 242 | `knowledge/segment-cards/0242_3-3-2-3.md` | PASS |
| 3-3-2-4 | 超验-生存论 | 243 | `knowledge/segment-cards/0243_3-3-2-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-3-1-1.md`–`3-3-1-4.md` | created | 存在主义/Beingism 下四个目的论位置 |
| `knowledge/position-cards/3-3-2-1.md`–`3-3-2-4.md` | created | 真正的生存主义下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 168 and total cards 252; `3-3-1` and `3-3-2` L4 draft coverage complete |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 168
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=168; new lengths 494/474/437/491/463/445/485/439
git diff --check: PASS
```

### 4. Gate notes

- All eight L4 cards declare `status: draft` and preserve row/segment traceability.
- Content was framed as structure-level relations among Beingism, existential ontology, humanistic existentialism, body/perception, Ereignis, stages, poetic mediation, divine-human ethics, and transcendence.
- W3-collected terms under 已收录 remain limited to existing W3 entries; new candidate terms remain under 待继续拆分.
- No W3/W5 canonical promotion was performed.

### 5. Next W4 work

1. Continue W4-L4 from `3-3-3-1` … or the next auditable L4 batch.
2. Keep updating the index and audit after each L4 batch.
3. Keep all W4 cards draft until W6 audit/review.

---

## W4-L4-B22 Audit — 3-3-3 四级轻卡（3-3-3-1 … 3-3-3-4）

- batch_id: `W4-L4-B22-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 继续 W4-L4 light cards，处理生存论下 `3-3-3` 的四个四级位置，并使当前 project knowledge contract W4-L4 172-card count target 达成。

### 1. Evidence base

| position | title | primary row | segment card | verdict |
|---|---|---:|---|---|
| 3-3-3-1 | 斗争的生存论 | 245 | `knowledge/segment-cards/0245_3-3-3-1.md` | PASS |
| 3-3-3-2 | 直接生存论 | 246 | `knowledge/segment-cards/0246_3-3-3-2.md` | PASS |
| 3-3-3-3 | 共同体的生存论 | 247 | `knowledge/segment-cards/0247_3-3-3-3.md` | PASS |
| 3-3-3-4 | 金融资本主义 | 248 | `knowledge/segment-cards/0248_3-3-3-4.md` | PASS |

### 2. Outputs

| artifact | status | notes |
|---|---|---|
| `knowledge/position-cards/3-3-3-1.md`–`3-3-3-4.md` | created | 同一生存论下四个目的论位置 |
| `knowledge/position-cards/index.md` | updated | coverage updated to L4 172 and total cards 256; current W4 count target reached at `3-3-3-4` |

### 3. Validation

Commands:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
```

Observed results:

```text
W3 validation: records=100, terms=25, quotes=235, errors=0, warnings=0
W4 L1: PASS, count=4
W4 L2: PASS, count=16
W4 L3: PASS, count=64
W4 L4: PASS, count=172; new lengths 437/417/468/449
git diff --check: PASS
```

### 4. Gate notes

- All four L4 cards declare `status: draft` and preserve row/segment traceability.
- Content was framed as structure-level relations among struggle, directness, community, speculative thinking, finance, field tension, and symbolic order.
- W3-collected terms under 已收录 remain limited to existing W3 entries; financial and Nietzschean terms remain under 待继续拆分.
- W4-L4 reaches the current 172-card target but remains draft pending W6 audit; no W3/W5 canonical promotion was performed.

### 5. Next W4/W-program work

1. Do not continue beyond `3-3-3-4` without explicitly resolving the project knowledge contract/index 172-card target boundary.
2. Continue W3 expansion toward ≥300/≥500 senses and W5 relation assets toward 60+ relations.
3. Prepare W6 audit only after W3/W5 readiness decisions; keep all W4 cards draft.
