# W10 Further Absorption Plan

- status: pilot-draft
- created: 2026-06-15 CST
- scope: post-W1–W9 close-reading absorption layer

## Purpose

W10 captures what the current framework under-absorbs after W1–W9: row-level argument sequence, staged process structure, and figure/school case positioning. It is an additive layer below corpus evidence and existing W1–W5 contracts. It does not promote W3/W5 draft assets, rewrite W2 segment cards, or replace W7 syntheses.

## Why this layer exists

A 16-row inspection and follow-up coverage check showed that many high-value rows are not well served by term senses or relation assets alone. Some rows contain:

- dense polemical argument, where the reusable claim must be separated from rhetorical intensity;
- staged practices or transformation procedures;
- figure/school reconstructions that need more than a term record but less than a synthesis.

W10 is the first pilot response to that gap.

## Card types

| Type | Directory | Captures |
|---|---|---|
| `w10-argument-card` | `argument-cards/` | critique target, reconstructed claim, argument steps, rhetoric boundary |
| `w10-process-card` | `process-cards/` | stages, transitions, preconditions, failure modes |
| `w10-case-card` | `case-cards/` | figure/school positioning, ISMISM reconstruction, standard-view contrast |

## Pilot batch

The first batch covers five rows selected for depth and framework-gap value:

1. row 76 / `1-4-1` — contemporary naturalism and analytic-philosophy critique.
2. row 131 / `2-2-2-2` — Zhuangzi eight-step cultivation sequence.
3. row 173 / `2-4-2-1` — J. S. Mill as naturalistic idealism and utilitarian normativity.
4. row 258 / `3-4-1-2` — early Lacan as metaphoric symbolism.
5. row 363 / `4-4-4-4` — AI regeneration as speculative process.

## Evidence discipline

Each card must declare `row_id`, `segment_id`, `toc_id`, `source_clean_path`, `evidence_quotes`, `rhetorical_register`, `w3_w5_gap_review`, `claim_core`, and `forbidden_use`. `evidence_quotes` must be same-row quotes and exact substrings of the declared clean file. Body claims must cite declared quotes with `[q1]`-style references, and all declared evidence quotes must be referenced in the body. Any cross-row support must be placed in `context_quotes` with its own row/segment/toc/path metadata and exact quote text.

## Non-goals

- Do not edit `split_md/` or `split_md_clean/`.
- Do not treat W10 as canonical truth over W1–W5.
- Do not promote W3/W5 out of draft.
- Do not revive legacy frontend or Atlas as canonical source.
- Do not claim full-corpus W10 completion from the pilot.

## Validation

Run:

```bash
python3 knowledge/scripts/validate_w10_absorption.py --repo .
```

For substantial delivery, also run the existing master/W1/W3/W4/W5 validators and confirm no corpus diff under `split_md/` or `split_md_clean/`.

## Future batches

Future W10 batches should use coverage audits to prioritize high-text rows with no W3/W5 coverage, while preserving small auditable batches, quote-substring validation, claim-to-quote mapping, exact index validation, and an explicit `w3_w5_gap_review` so W10 does not bypass upstream W3/W5 extraction decisions. Rows marked `followup_needed` should be appended to `knowledge/qa/w10-w3-w5-gap-followups.md`.
