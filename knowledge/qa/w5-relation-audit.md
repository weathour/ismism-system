# W5 Relation Audit — Batch 1

- batch_id: `W5-B1-2026-05-08`
- audited_at: 2026-05-08 CST
- objective: 建立机制词与核心术语的首批关系资产，保持低 token、draft-only。

## Artifacts

| artifact | status | notes |
|---|---|---|
| `knowledge/relations/relation-assets.jsonl` | created | 12 draft relations |
| `knowledge/relations/relation-prompts.md` | created | 低 token 继续提示 |
| `knowledge/relations/route-cards.md` | created | 2 route families |
| `knowledge/relations/tension-cards.md` | created | 2 tension families |
| `knowledge/relations/mediation-cards.md` | created | 2 mediation families |
| `knowledge/relations/boundary-cards.md` | created | 2 boundary notes |
| `knowledge/relations/misrecognition-cards.md` | created | 2 risk notes |

## Coverage

- mechanism conversion: `rel:w5b1:001`–`003`
- theory production: `rel:w5b1:004`–`005`
- mechanism tensions: `rel:w5b1:006`–`007`
- history/people/theory mediation: `rel:w5b1:008`–`010`
- subject/practice positioning: `rel:w5b1:011`
- mechanism/noun boundary: `rel:w5b1:012`

## Verdict

PASS for first draft relation batch. No W3 term sense was promoted to canonical.

---

# W5 Relation Audit — Batch 2

- batch_id: `W5-B2-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 扩展 W5 relation assets，补齐 W5-B1 未覆盖的 relation types，并按 MASTER-SPEC 回填/新增 `source_position`、`target_position`、`evidence_segment` 字段。

## Artifacts

| artifact | status | notes |
|---|---|---|
| `knowledge/relations/relation-assets.jsonl` | updated | 12 条 B1 relation 已回填字段；新增 14 条 B2 relation；总计 26 |
| `knowledge/relations/route-cards.md` | updated | 新增 Route R3/R4 |
| `knowledge/relations/tension-cards.md` | updated | 新增 Tension T3 |
| `knowledge/relations/mediation-cards.md` | updated | 新增 Mediation M3 |
| `knowledge/relations/boundary-cards.md` | updated | 新增 Boundary B3/B4 |
| `knowledge/relations/misrecognition-cards.md` | updated | 新增 Misrecognition M3/M4 |
| `knowledge/relations/overcode-cards.md` | created | 新增 Overcode O1/O2 |
| `knowledge/relations/evidence-claim-cards.md` | created | 新增 Evidence Claim E1/E2 |
| `knowledge/scripts/validate_w5_relation_assets.py` | created | relation JSONL / W4 position / W1 quote-substring validator |

## Coverage

- `blocks-transition`: `rel:w5b2:001`–`002`
- `misrecognizes-as`: `rel:w5b2:003`–`004`
- `overcodes`: `rel:w5b2:005`–`006`
- `evidences-claim`: `rel:w5b2:007`–`008`
- route/transition/tension/mediation/boundary/position coverage: `rel:w5b2:009`–`014`

## Validation snapshot

```text
relation count: 26
covered relation types: 12/12
relation types with >=2 examples: 11/12 (subjectivizes still has 1)
records missing source_position/target_position/evidence_segment: 0
all source_position/target_position cards exist: PASS
exact evidence_segment quote substring check: PASS (34 quotes)
validator: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . -> errors=0, warnings=0
```

Final integrity note: two W5-B2 forbidden-interpretation fields were softened to remove the over-strong relation wording `必然`; no evidence quote or source/target identity was changed.

## Verdict

PASS for W5-B2 draft expansion. W5 remains incomplete: target is ≥60 relations and all 12 relation types with ≥2 examples; only `subjectivizes` remains below 2 examples after this batch.

---

# W5 Relation Audit — Batch 3

- batch_id: `W5-B3-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 补齐 `subjectivizes` 第二例并扩展机制/边界/中介/误认/超编码/claim 关系，继续推进 W5 toward ≥60。

## Artifacts

| artifact | status | notes |
|---|---|---|
| `knowledge/relations/relation-assets.jsonl` | updated | 新增 14 条 B3 relation；总计 40 |
| `knowledge/relations/mechanism-cards.md` | created | 新增 B3 mechanism summary K1–K4 |
| `knowledge/relations/boundary-cards.md` | updated | 新增 Boundary B5/B6 |
| `knowledge/relations/mediation-cards.md` | updated | 新增 Mediation M4 |
| `knowledge/relations/misrecognition-cards.md` | updated | 新增 Misrecognition M5 |
| `knowledge/relations/overcode-cards.md` | updated | 新增 Overcode O3 |
| `knowledge/relations/evidence-claim-cards.md` | updated | 新增 Evidence Claim E3 |
| `knowledge/relations/relation-prompts.md` | updated | 新增 B3 continuation prompt |

## Coverage

- `subjectivizes`: `rel:w5b3:001`–`002`
- `transitions-to`: `rel:w5b3:003`, `rel:w5b3:006`
- `boundary-between`: `rel:w5b3:004`, `rel:w5b3:011`
- `objectifies`: `rel:w5b3:005`
- `mediates-between`: `rel:w5b3:007`
- `blocks-transition`: `rel:w5b3:008`, `rel:w5b3:010`
- `evidences-claim`: `rel:w5b3:009`
- `misrecognizes-as`: `rel:w5b3:012`
- `overcodes`: `rel:w5b3:013`
- `represents-position`: `rel:w5b3:014`

## Validation snapshot

```text
relation count: 40
covered relation types: 12/12
relation types with >=2 examples: 12/12
records missing source_position/target_position/evidence_segment: 0
all source_position/target_position cards exist: PASS
exact evidence_segment quote substring check: PASS (49 quotes)
validator: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . -> errors=0, warnings=0
batch validator: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B3-2026-06-08 -> errors=0, warnings=0
final W5 gate: still pending at 40/60 relations
```

## Verdict

PASS for W5-B3 draft expansion. W5 remains incomplete only on count target (needs ≥60 relations); all 12 relation types now have ≥2 examples. No W3/W5 item was promoted to canonical.

---

# W5 Relation Audit — Batch 4

- batch_id: `W5-B4-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 扩展 theory/practice、philosophization/dialecticization、symbolic economy 与 objectification 关系，推进 W5 count gate。

## Coverage

- 新增 10 条 draft relations：`rel:w5b4:001`–`010`
- total after B4: 50
- families: route, mediation, blocks-transition, tension, boundary, overcodes, objectifies, represents-position

## Validation snapshot

```text
validator: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B4-2026-06-08 -> records=10, quotes=11, errors=0, warnings=0
full validator after B4 -> records=50, quotes=60, types=12/12, errors=0, warnings=0
```

## Verdict

PASS for W5-B4 draft expansion. W5 remained incomplete after B4 only on count target.

---

# W5 Relation Audit — Batch 5

- batch_id: `W5-B5-2026-06-08`
- audited_at: 2026-06-08 CST
- objective: 补足 W5 ≥60 relation count gate while preserving all W5 as draft.

## Coverage

- 新增 10 条 draft relations：`rel:w5b5:001`–`010`
- total after B5: 60
- covered relation types: 12/12
- relation types with >=2 examples: 12/12

## Validation snapshot

```text
relation count: 60
covered relation types: 12/12
relation types with >=2 examples: 12/12
records missing source_position/target_position/evidence_segment: 0
all source_position/target_position cards exist: PASS
exact evidence_segment quote substring check: PASS (70 quotes)
validator: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . -> errors=0, warnings=0
batch validator: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-B5-2026-06-08 -> errors=0, warnings=0
final W5 gate: python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2 -> PASS
```

## Verdict

PASS for W5-B5 draft expansion. W5 MASTER-SPEC quantitative gate is now reached: 60 draft relations; all 12 relation types covered; all 12 types have >=2 examples. No W5 relation was promoted to canonical; W6 audit remains required before any promotion.
