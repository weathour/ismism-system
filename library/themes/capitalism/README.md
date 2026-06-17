# Capitalism / Political Economy Theme Package Layer

- status: theme package layer, draft-linked and validator-backed
- date: 2026-06-16
- manifest: `capitalism-row-manifest.jsonl` (88 reviewed rows)
- evidence bank: `capitalism-evidence-bank.jsonl` (271 exact quote records)
- validator: `python3 tools/validate/themes/capitalism.py --repo . --final`
- query helper: `python3 tools/query/themes/capitalism.py 资本主义 --limit 3`

This layer is **not** an external encyclopedia of capitalism, Marxism, economics, or political theory. It absorbs how ISMISM internally handles capital, commodity/fetishism, consumption, finance, class, labor, alienation, production relations, imperialism, global capital, economic-life organization, capital socialization, and practice-based replacement of capitalist forms.

## Files

- `capitalism-row-manifest.jsonl` — one-class-per-row reviewed manifest.
- `capitalism-evidence-bank.jsonl` — exact clean-text quote bank with `ev:cap:*` ids.
- `capitalism-taxonomy.md` — controlled taxonomy and row ownership map.
- `capitalism-concept-relation-batch-notes.md` — concept/relation batch ids and boundaries.
- `capitalism-critique-and-fetishism-synthesis.md`
- `political-economy-and-production-synthesis.md`
- `capital-socialization-and-practice-synthesis.md`
- `finance-imperialism-and-global-capital-synthesis.md`

## Query examples

```bash
python3 tools/query/themes/capitalism.py 资本主义 --limit 3
python3 tools/query/themes/capitalism.py --row 324
python3 tools/query/themes/capitalism.py --class production-relations-forces
```

## Validation

```bash
python3 tools/validate/themes/capitalism.py --repo . --final
python3 tools/internal/validate_concepts.py --repo . --batch-id concept-CAPITALISM-2026-06-16
python3 tools/internal/validate_relations.py --repo . --batch-id relation-CAPITALISM-2026-06-16 --min-count 51
python3 tools/internal/validate_close_reading.py --repo .
```

## Boundary

Existing AI / Chinese Philosophy / Religion / Time-Death rows can be linked as traceable context, but capitalism-specific claims must explain capital, production relations, commodity/fetishism, finance, class, alienation, imperialism, or practice replacement functions.
