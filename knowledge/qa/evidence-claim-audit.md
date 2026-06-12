# W6 Evidence-Claim Audit — Relation Strength Review

- created: 2026-06-09 CST
- scope: MASTER-SPEC W6 item 2 plus relation evidence/claim boundary checks.
- status: PASS — no blocking over-strong relation issue found.

## 1. Relation Inventory

| relation_type | count |
|---|---:|
| blocks-transition | 5 |
| boundary-between | 6 |
| evidences-claim | 4 |
| mediates-between | 7 |
| misrecognizes-as | 3 |
| objectifies | 5 |
| overcodes | 4 |
| represents-position | 6 |
| route-from-to | 6 |
| subjectivizes | 3 |
| tension-between | 6 |
| transitions-to | 5 |

All 12 controlled relation types are present; all have at least 2 examples.

## 2. Twenty-Relation Strength Sample

Sampling rule: deterministic even-spacing over `knowledge/relations/relation-assets.jsonl` after W5-B5.

| relation_id | type | source_position | target_position | over-strength verdict |
|---|---|---|---|---|
| rel:w5b1:001 | transitions-to | 4 | 2-2-4 | PASS |
| rel:w5b1:004 | objectifies | 4 | 2-2-4 | PASS |
| rel:w5b1:007 | tension-between | 2-2-4 | 4 | PASS |
| rel:w5b1:010 | mediates-between | 4 | 4 | PASS |
| rel:w5b2:001 | blocks-transition | 3-1-3 | 3-1-1 | PASS |
| rel:w5b2:005 | overcodes | 3-4-3 | 1-2-2-3 | PASS |
| rel:w5b2:008 | evidences-claim | 3-1-3 | 3-1-3 | PASS |
| rel:w5b2:011 | mediates-between | 3-1-3 | 3-1-3 | PASS |
| rel:w5b2:014 | represents-position | 2-3-4 | 4-1-4 | PASS |
| rel:w5b3:003 | transitions-to | 4-1-3 | 2-2-4 | PASS |
| rel:w5b3:006 | transitions-to | 4-1-2 | 2-2-4 | PASS |
| rel:w5b3:009 | evidences-claim | 4-1-4 | 4-1-4 | PASS |
| rel:w5b3:012 | misrecognizes-as | 2-2-3-1 | 1-4-3 | PASS |
| rel:w5b4:001 | route-from-to | 4-1-2 | 4-1-2 | REVIEWED-PASS |
| rel:w5b4:004 | blocks-transition | 4-1-3 | 4-1-3 | PASS |
| rel:w5b4:008 | tension-between | 3-4-3 | 3-4-3 | PASS |
| rel:w5b5:001 | mediates-between | 4 | 4 | PASS |
| rel:w5b5:004 | represents-position | 1-3-1-4 | 3-1-3 | PASS |
| rel:w5b5:007 | objectifies | 3-4-4 | 3-4 | PASS |
| rel:w5b5:010 | tension-between | 3-3-2-4 | 4-1-3 | PASS |

## 3. Machine Gate

```bash
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
```

Observed: `records=60, quotes=70, types=12/12, errors=0, warnings=0`.

## 4. Lexical Over-Strength Scan Notes

The audit checked relation `definition`, `applicability_boundary`, and `forbidden_interpretation` for risky words such as `必然`, `一定`, `永远`, `完全决定`, `唯一`, `只能`.

- `rel:w5b1:008`: lexical hits ['唯一']; reviewed as boundary/forbidden wording, not over-strong relation claim.
- `rel:w5b2:009`: lexical hits ['唯一']; reviewed as boundary/forbidden wording, not over-strong relation claim.
- `rel:w5b4:001`: lexical hits ['唯一']; reviewed as boundary/forbidden wording, not over-strong relation claim.

Any risky lexical hit inside `forbidden_interpretation` is not treated as an over-strong claim because it marks a prohibited reading.

## 5. Findings

- No sampled relation rewrites a possible/located movement as universal necessity.
- No sampled one-way relation is written as bidirectional without an explicit relation type supporting that reading.
- All relation records remain `draft` and require W6/W7 human review before any canonical promotion.

## 6. Required Corrections

None. No `confidence: low` edits required by this audit.
