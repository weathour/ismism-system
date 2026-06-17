# Capitalism / Political Economy Absorption Audit

- date: 2026-06-16
- status: PASS
- layer: `knowledge/themes/capitalism/`

## Scope

- 88 reviewed rows in `capitalism-row-manifest.jsonl`.
- All Ring 1 rows included and core-classified.
- Ring 2–5 candidates are classified or explicitly retained as peripheral/noise-review.
- 271 exact-substring evidence records in `capitalism-evidence-bank.jsonl`.

## Added draft/pilot assets

- W3: 63 draft term senses under `W3-CAPITALISM-2026-06-16`.
- W5: 51 draft relation assets under `W5-CAPITALISM-2026-06-16`.
- W10: 45 Capitalism pilot-draft cards across hard-core, commodity/fetishism, finance/imperialism, labor/class/alienation, and practice replacement batches; bodies were regenerated after review to provide row-specific argument/process/case readings rather than placeholder evidence-number prose.

## Boundary checks

- This is not an external capitalism / Marxism / economics encyclopedia.
- Every substantive claim must resolve to `ev:cap:*`, `term:*`, `rel:capitalism:*`, `w10:*`, or row markers.
- `split_md/` and `split_md_clean/` are protected corpus layers and were not intentionally modified.
- W3/W5 remain `draft`; W10 remains `pilot-draft`.
- W3/W5 shared JSONL files preserve the pre-existing `HEAD` raw byte prefix; new lines are appended under allowed Time-Death/Capitalism batch IDs.

## Positive validation evidence

Initial positive suite passed before final review:

```bash
python3 knowledge/scripts/validate_capitalism_theme.py --repo .
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-CAPITALISM-2026-06-16
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-CAPITALISM-2026-06-16 --min-count 45
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_ai_theme.py --repo . --final
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/validate_religion_theme.py --repo . --final
python3 knowledge/scripts/validate_time_death_theme.py --repo . --final
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
```

Final command transcript: `.omx/tmp/capitalism_positive_validation_suite.txt`. Negative-test transcripts: `.omx/tmp/validate_capitalism_bad_quote_negative.txt`, `.omx/tmp/validate_capitalism_taxonomy_negative.txt`, `.omx/tmp/validate_capitalism_synthesis_marker_negative.txt`, `.omx/tmp/validate_w10_capitalism_duplicate_quote_negative.txt`, `.omx/tmp/validate_w10_capitalism_placeholder_negative.txt`.
