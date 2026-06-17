# W5 Relation Prompts — Batch 1

- batch_id: `W5-B1-2026-05-08`
- status: draft
- scope: 机制词与核心术语方向边首批，不升 canonical。

## Low-token prompt

读取 `knowledge/lexicon/term-senses.jsonl` 中以下 sense_id：`主体:s04`、`客体:s04`、`实践:s02/s04`、`历史:s02`、`人民:s02`、`理论:s01/s03`、`主体化:s01`、`客体化:s01`、`去主体化:s01`。基于已有 evidence_quote 建立关系资产，不重新扫描全库。

## First relation families

1. 机制转换：`去主体化 -> 客体化 -> 客体:s04`
2. 理论生产：`理论:s03 -> 客体化/主体化`
3. 三元中介：`历史:s02 / 人民:s02 / 理论:s01`
4. 主体落点：`实践:s04 -> 主体:s04`
5. 层级边界：机制词不得混同名词义项。

## Guardrails

- 只使用 `draft` 状态。
- 每条关系必须保留 evidence row/quote。
- 不将 W3 术语义项升为 canonical。
- 不从 generated candidate data 或已删除产品原型推断关系。

---

# W5 Relation Prompts — Batch 2 continuation

- batch_id: `W5-B2-2026-06-08`
- current W5 count after batch: 26 draft relations
- coverage added: `blocks-transition`, `misrecognizes-as`, `overcodes`, `evidences-claim` each now has 2 examples; older W5-B1 records were backfilled with `source_position`, `target_position`, and `evidence_segment` fields.

## Next relation families

1. Add another `subjectivizes` relation so all 12 relation types have at least 2 instances.
2. Continue toward ≥60 records with route/tension/boundary/mediation/misrecognition batches.
3. Keep every new relation with `source_position`, `target_position`, `evidence_segment`, applicability boundary, and forbidden interpretation.

---

# W5 Relation Prompts — Batch 3 continuation

- batch_id: `W5-B3-2026-06-08`
- current W5 count after batch: 40 draft relations
- coverage added: `subjectivizes` now has >=2 examples; all 12 relation types now have >=2 examples.

## Next relation families

1. Continue W5 to >=60 records; current gap is +20 relations.
2. Prefer route/tension/mediation/mechanism batches grounded in W3 senses after B20-B26.
3. Keep exact `evidence_segment.quote` substrings and W4-existing `source_position` / `target_position` coordinates.
4. Avoid over-strong relation prose; use “可读作 / 可发生 / 在该语境中” rather than universal claims.

---

# W5 Relation Prompts — Batch 4/5 completion note

- batch_id: `W5-B4-2026-06-08`, `W5-B5-2026-06-08`
- current W5 count after B5: 60 draft relations
- W5 project knowledge contract count gate: reached for relation count (60/60+) and type coverage (12/12 types, all >=2 examples).

## Next relation-layer task

Run W6 audit before any promotion:

1. sample relation strength and rewrite over-strong edges;
2. verify directionality (single-direction vs reciprocal);
3. keep all W5 as `draft` until explicit review;
4. continue W3 final expansion separately toward >=500 senses / >=200 terms.
