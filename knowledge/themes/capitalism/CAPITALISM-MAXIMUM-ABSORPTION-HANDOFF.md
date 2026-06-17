# Capitalism / Political Economy Maximum Absorption Handoff

- date: 2026-06-16
- status: complete; final validation PASS; final review gate pending
- layer: `knowledge/themes/capitalism/`

## What changed

- Added an independent Capitalism / Political Economy theme layer, not a thin index over prior AI/Chinese/Religion/Time-Death layers.
- Created `capitalism-row-manifest.jsonl` with 88 reviewed rows.
- Created `capitalism-evidence-bank.jsonl` with 271 exact-substring quote records.
- Created `capitalism-taxonomy.md`, README, four syntheses, and W3/W5 batch notes.
- Appended W3 batch `W3-CAPITALISM-2026-06-16` with 63 draft senses.
- Appended W5 batch `W5-CAPITALISM-2026-06-16` with 51 draft relation assets.
- Added 45 W10 Capitalism pilot-draft close-reading cards and regenerated `knowledge/w10-absorption/index.md`.
- Added `knowledge/scripts/validate_capitalism_theme.py` and `knowledge/scripts/query_capitalism_theme.py`.

## Resume entry points

1. `knowledge/themes/capitalism/README.md`
2. `knowledge/themes/capitalism/capitalism-row-manifest.jsonl`
3. `knowledge/themes/capitalism/capitalism-evidence-bank.jsonl`
4. `knowledge/themes/capitalism/capitalism-taxonomy.md`
5. `knowledge/scripts/validate_capitalism_theme.py`
6. `knowledge/scripts/query_capitalism_theme.py`
7. `knowledge/qa/capitalism-absorption-audit.md`
8. `knowledge/qa/capitalism-evidence-claim-audit.md`
9. `knowledge/qa/capitalism-ultraqa-report.md`

## Validation commands

```bash
python3 knowledge/scripts/validate_capitalism_theme.py --repo . --final
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-CAPITALISM-2026-06-16
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-CAPITALISM-2026-06-16 --min-count 45
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 292 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
```

## Boundary

- Do not treat this layer as an external encyclopedia of capitalism, Marxism, economics, or political theory.
- Do not promote W3/W5 records out of `draft` or W10 out of `pilot-draft` without explicit review.
- Do not edit `split_md/` or `split_md_clean/` as part of theme work.
- Atlas remains candidate-only.

## Final validation evidence

- Positive suite: `.omx/tmp/capitalism_positive_validation_suite.txt` → PASS.
- Negative tests: bad quote, duplicate taxonomy ownership, unknown synthesis marker, and duplicate W10 quote all failed as intended and restored.
- Protected corpus: `test -z "$(git diff --name-only -- split_md split_md_clean)"` → PASS.
