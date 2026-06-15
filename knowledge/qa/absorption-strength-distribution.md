# Absorption Strength Distribution — 2026-06-15 CST

- status: current row-level coverage snapshot after W10 pilot batch 1
- scope: `knowledge/manifests/segments.jsonl`, `knowledge/lexicon/term-senses.jsonl`, `knowledge/relations/relation-assets.jsonl`, and `knowledge/w10-absorption/*-cards/*.md`
- purpose: show where the repository is deeply absorbed versus still only structurally indexed

## Summary

The repository now has complete structural coverage but uneven interpretive depth:

- W1/W2 covers all 363 rows.
- W3 term-sense absorption covers 139 rows.
- W5 relation absorption covers 29 rows.
- W10 close-reading absorption currently covers 5 pilot rows.
- Any of W3/W5/W10 covers 143 rows, or 44.0% of clean-text volume.
- 220 rows remain W1/W2-only; these are structurally traceable but not yet deeply absorbed.

## Row-level strength tiers

| Strength tier | Meaning | Rows | Row % | Clean-text % |
|---|---|---:|---:|---:|
| W1/W2 only | manifest + segment card only | 220 | 60.6% | 56.0% |
| W1/W2 + W3 | term-sense absorption | 109 | 30.0% | 34.2% |
| W1/W2 + W5 only | relation asset without W3 row coverage | 1 | 0.3% | 0.2% |
| W1/W2 + W3 + W5 | term + relation absorption | 28 | 7.7% | 7.6% |
| W1/W2 + W10 only | close-reading pilot without W3/W5 | 3 | 0.8% | 1.2% |
| W1/W2 + W3 + W10 | term + close-reading pilot | 2 | 0.6% | 0.8% |
| W1/W2 + W5 + W10 | relation + close-reading pilot | 0 | 0.0% | 0.0% |
| W1/W2 + W3 + W5 + W10 | full row-level overlap | 0 | 0.0% | 0.0% |

Interpretation: W10 has begun to fill the W2↔W7 close-reading gap, but the strongest overlap layer is still W3+W5, not yet W3+W5+W10.

## Coverage by matrix field

| Field | Rows | W3 rows | W5 rows | W10 rows | W1/W2-only rows | Notes |
|---|---:|---:|---:|---:|---:|---|
| 1 实在论 | 88 | 29 | 4 | 1 | 58 | medium-low deep absorption; one new W10 argument card at row 76 |
| 2 形而上学 | 89 | 36 | 7 | 2 | 52 | medium absorption; W10 now covers one process row and one case row |
| 3 观念论 | 89 | 49 | 11 | 1 | 39 | strongest W3/W5 absorption concentration |
| 4 实践 | 88 | 23 | 7 | 1 | 64 | weakest broad absorption despite strong hubs such as row 276/285/289 |
| unknown / nonstandard | 9 | 2 | 0 | 0 | 7 | auxiliary/nonstandard rows remain shallow |

## Current high-strength hubs

Rows with the densest existing W3/W5 absorption include:

- row 263 / `3-4-2-2` — 静止的事件主义; strongest W3 sense concentration.
- row 285 / `4-1-2-1` — 学习／研究; strong W3 and W5 coverage.
- row 229 / `3-2-4-2` — 否定辩证法; strong W3 and W5 coverage.
- row 276 / `4` — 实践; W5 relation hub.
- row 289 / `4-1-3` — 历史的哲学化; W3/W5 bridge.
- row 139 / `2-2-4` — 反二元对立; matrix-method hub.
- row 46 / `1-3` — 庸俗唯我论复习课; matrix-axis explanation hub.

## Current W10 pilot rows

| Row | TOC | W10 type | Existing W3? | Existing W5? | Absorption gain |
|---:|---|---|---|---|---|
| 76 | `1-4-1` | `w10-argument-card` | no | no | reconstructed argument chain and rhetoric boundary |
| 131 | `2-2-2-2` | `w10-process-card` | yes | no | staged Zhuangzi eight-step protocol |
| 173 | `2-4-2-1` | `w10-case-card` | no | no | Mill case reconstruction as naturalistic idealism |
| 258 | `3-4-1-2` | `w10-case-card` | yes | no | early Lacan as metaphoric symbolism case |
| 363 | `4-4-4-4` | `w10-process-card` | no | no | AI regeneration as speculative process |

## High-priority low-absorption backlog

Largest W1/W2-only rows by clean-text volume:

1. row 85 / `1-4-2-4` — 性解放主义
2. row 133 / `2-2-2-4` — 韩非子的道家魔法
3. row 107 / `2-1-2-4` — 四个芝诺悖论
4. row 174 / `2-4-2-2` — 涂尔干 / 社会实证主义
5. row 124 / `2-2-1-4` — 唯识论 / 阿赖耶
6. row 65 / `1-3-4-3` — 唯美主义
7. row 159 / `2-3-3-3` — 逻辑原子主义 / 罗素
8. row 87 / `1-4-3-1` — 情绪主义
9. row 342 / `4-4` — 不可能的乌托邦
10. row 255 / `3-4` — 复习课

## Operational implication

Next W10 batches should not be uniform expansion. Prefer small batches over high-text, low-W3/W5 rows, while recording `w3_w5_gap_review` so W10 discoveries become W3/W5 follow-up rather than a bypass of upstream extraction.
