# Religion Problem Evidence-Claim Audit

- date: 2026-06-15 CST
- status: PASS
- scope: Religion Problem manifest/evidence/taxonomy/synthesis/W3/W5/W10 claim links
- validator: `python3 knowledge/scripts/validate_religion_theme.py --repo . --final`

## Claim discipline

- Every evidence-bank quote declares `row_id`, `segment_id`, `toc_id`, `clean_md_path`, `quote`, `theme_tags`, and `quote_role`.
- Every evidence quote is validated as an exact substring of its declared `clean_md_path`.
- Manifest `evidence_quote_count` values match quote-bank row counts.
- Taxonomy rows are uniquely owned by one declared `theme_class`; duplicate ownership is rejected.
- Synthesis claim bullets use only resolvable `ev:religion:*`, `term:*:sNN`, `rel:religion:*`, `w10:*`, and `row N` markers.
- W3 and W5 additions use exact quote evidence and remain `draft`.
- W10 cards use same-row evidence quotes and `[qN]` body references; duplicate evidence quotes are rejected by the W10 validator.

## Marker families used

- evidence: `ev:religion:0024:01` etc.
- terms: `term:宗教实在论:s01`, `term:偶像崇拜:s01`, `term:神爱论:s01` etc.
- relations: `rel:religion:001` through `rel:religion:051`.
- W10: 45 Religion card ids containing `:religion-`.
- rows: 80 manifest rows, with rows 24–45 as the core 1-2 religious-realism block.

## Negative-test evidence

All four requested validator-failure modes were exercised and restored:

1. Broken evidence quote failed with `quote not exact substring`.
2. Duplicate taxonomy row failed with `row 24 appears in multiple theme nodes`.
3. Unknown synthesis markers failed for evidence, term, relation, W10, and row markers.
4. Duplicate W10 evidence quote failed in `validate_w10_absorption.py`.

After restoration, `validate_religion_theme.py --final` and `validate_w10_absorption.py --repo .` passed again.
