# Feminism Absorption Audit

- status: PASS
- date: 2026-06-16 CST
- layer: `knowledge/themes/feminism/`
- scope: 94 reviewed candidate rows; 38 core / 46 bridge / 5 context / 5 excluded.
- evidence: 309 exact-substring records in `knowledge/themes/feminism/feminism-evidence-bank.jsonl`.
- W3: 78 `draft` term senses under `W3-FEMINISM-2026-06-16`.
- W5: 65 `draft` relation assets under `W5-FEMINISM-2026-06-16`.
- W10: 45 `pilot-draft` cards under `W10-FEMINISM-2026-06-16`.

## Candidate-selection audit

All Ring A rows are present and classified as core: rows 90, 61, 330, 265, 85, 93, and 89. Ring B/C/D rows were included when clean-text function supported love/eros, sexualized body, discourse/psychoanalysis, family/reproduction, or practice-liberation functions. Additional Ring E hits were reviewed but kept as `context` or `excluded` where the term hit was only a weak signal.

Manifest role counts:

- `core`: 38 — direct feminism/gender/sexuality/reproduction function and W3/W5/W10 action.
- `bridge`: 46 — traceable bridge into body, eros, family, practice, capitalism, religion, phenomenology, psychoanalysis, or discourse.
- `context`: 5 — retained for query/boundary awareness without W3/W5/W10 escalation.
- `excluded`: 5 — keyword-only/off-function rows; validator prevents excluded keyword-only promotion.

## Boundary audit

- The layer is ISMISM-internal absorption, not an external feminism/gender-studies encyclopedia.
- Atlas was not used as final truth.
- `split_md/` and `split_md_clean/` were not modified; final protected-corpus check passed.
- Cross-theme references remain function-specific and marker-backed.
- W3/W5 remain `draft`; W10 remains `pilot-draft`.

## Validation evidence

- Full suite log: `.omx/tmp/feminism_full_validation_final.log`.
- Query smoke log: `.omx/tmp/feminism_query_smoke.log`.
- Negative-test log: `.omx/tmp/feminism_negative_tests.log`.
