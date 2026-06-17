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

## AI theme expansion batch

The 2026-06-15 AI Theme Maximum Absorption Program added 27 new W10 pilot-draft cards and incorporated the existing row 363 AI regeneration card, yielding 28 AI rows/cards:

- rows 13–18 — AI theory prehistory: cognitivism, functionalism, strong/weak AI, algorithms, and frame-problem boundaries;
- rows 342–353 — 4-4 transition: impossible utopia, weak VR, de-anthropocentrization, immortality, symbolic death, aging/maturity, and embodiment;
- rows 354–358 — embodiment: AI substance, erotic assimilation, secret intersubjectivity, rescue, and voice;
- rows 359–363 — ordered abyss: AI symbol-system genesis, education, becoming interval, mortality, and regeneration.

This expansion remains `pilot-draft`; the theme synthesis lives under `knowledge/themes/ai/` and does not replace W1–W5 evidence.

## Evidence discipline

Each card must declare `row_id`, `segment_id`, `toc_id`, `source_clean_path`, `evidence_quotes`, `rhetorical_register`, `w3_w5_gap_review`, `claim_core`, and `forbidden_use`. `evidence_quotes` must be same-row quotes and exact substrings of the declared clean file. Body claims must cite declared quotes with `[q1]`-style references, and all declared evidence quotes must be referenced in the body. Any cross-row support must be placed in `context_quotes` with its own row/segment/toc/path metadata and exact quote text. Validator policy now also rejects the old Capitalism placeholder phrase `限定本行资本主义功能的一个环节`; future cards must give row-specific argument steps, process stages, or case readings rather than generic evidence-number prose.

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

## Chinese philosophy expansion batch

The 2026-06-15 Chinese Philosophy Maximum Absorption Program added 45 W10 pilot-draft cards over Confucian/Neo-Confucian, Daoist/Warring States/Yijing, Buddhist/Chan bridge, Mao/Chinese Marxist practice, and selected revolutionary context rows. Row 131's existing card remains intact; the new row 131 card is complementary and focuses on later close-reading extension rather than replacing `w10:proc:0131:zhuangzi-eight-steps`.

These cards remain `pilot-draft`; W3/W5 additions remain `draft`; all evidence quotes are validated as exact substrings of `split_md_clean`.

## Religion Problem expansion batch

The 2026-06-15 Religion Problem Maximum Absorption Program added 45 W10 pilot-draft cards over the 1-2 religious realism core plus sacred ideology/love/death, mysticism/Buddhist liberation, and ideology/practice transformation bridges. The W10 total is now 122 cards. These cards remain `pilot-draft`; Religion W3/W5 additions remain `draft`; all evidence quotes are validated as exact substrings of `split_md_clean`.


## Time-Death-Finitude-Life expansion batch

- batch_id: `W10-TIME-DEATH-LIFE-2026-06-15`
- added_cards: 42
- status: pilot-draft; additive close-reading only
- scope: death/time/finitude core, AI mortality/technical life, Buddhist rebirth/liberation, life/body/nature/pessimism, and historical/practice time.
- companion coverage file: `knowledge/themes/time-death-finitude-life/time-death-w10-coverage.jsonl` records new-card vs reuse/context rationale for all required W10 matrix rows.

## Capitalism / Political Economy expansion batch

- batch_id: `W10-CAPITALISM-2026-06-16`
- added_cards: 45
- status: pilot-draft; additive close-reading only
- scope: hard-core capitalism/political-economy rows, commodity/fetishism/consumption ideology, finance/imperialism/global capital, labor/class/alienation, and capital-socialization/economic-life practice replacement.
- companion layer: `knowledge/themes/capitalism/` provides the manifest, evidence bank, taxonomy, W3/W5 notes, syntheses, validator, query helper, and QA/handoff files.
- current W10 total after this batch: 209 cards across 154 unique rows; superseded by Universal Absorption Phase A below.


## Universal Absorption Phase A expansion batch

- batch_id: `W10-UNIVERSAL-A-2026-06-16`
- added_cards: 60
- status: pilot-draft; additive row-level repair only
- scope: high-volume W1/W2-only backlog across ancient/presence metaphysics, logic/positivism/empiricism, phenomenology/hermeneutics/structure-language transformation, and selected everyday ideology rows.
- companion QA layer: `knowledge/qa/universal-absorption-phase-a-gap-map.jsonl`, `knowledge/qa/universal-absorption-phase-a-evidence-bank.jsonl`, `knowledge/qa/universal-absorption-phase-a-audit.md`, and `knowledge/scripts/validate_universal_absorption_phase_a.py`.
- current W10 total after this batch: 269 cards across 214 unique rows.

Universal-A is not a new theme maximum absorption layer. It is a universal row-level repair batch; all new cards remain `pilot-draft`, W3/W5 companion additions remain `draft`, and all evidence quotes are validated as exact substrings of `split_md_clean`.


## Universal Absorption Phase B expansion — 2026-06-16

- status: complete as pilot-draft row-level repair
- batch_id: `W10-UNIVERSAL-B-2026-06-16`
- added_cards: 39
- rows: 286, 147, 150, 181, 164, 306, 56, 287, 210, 203, 12, 22, 180, 250, 212, 198, 47, 301, 294, 20, 224, 202, 281, 163, 78, 196, 148, 303, 23, 77, 67, 302, 151, 234, 310, 197, 304, 162, 242
- method: one same-row argument/process/case card per selected post-Phase-A W1/W2-only row; every card carries exact clean-text quotes and records `w3_w5_gap_review: already_covered` because Phase B also adds W3/W5 draft records for the same rows.
- boundary: this is a universal repair batch, not a theme maximum absorption layer.

<!-- FEMINISM-THEME-START:W10PLAN -->
## Feminism / Gender / Sexuality / Social Reproduction expansion batch

The 2026-06-16 Feminism Maximum Absorption Program added 45 W10 pilot-draft cards across false feminism, misogyny/patriarchal fantasy, sexual liberation/erotic economy, love/marriage/intimacy, sexualized body, sex-difference discourse, family/reproduction/social reproduction, and women/children/economic liberation practice. Cards remain `pilot-draft`; W3/W5 additions remain `draft`.
<!-- FEMINISM-THEME-END:W10PLAN -->

<!-- PSYCHOANALYSIS-SUBJECTIVITY-W10-START -->
## Psychoanalysis-Subjectivity expansion batch

The 2026-06-16 Psychoanalysis-Subjectivity Maximum Absorption Program added 58 W10 pilot-draft cards across psychoanalysis, semiotic/discourse/language, subjectivity/phenomenology, ideology/fantasy diagnosis, and practice/cross-theme bridge rows. These cards remain `pilot-draft` and supplement existing row cards rather than replacing them.

Theme folder: `knowledge/themes/psychoanalysis-subjectivity/`.
Validator: `python3 knowledge/scripts/validate_psychoanalysis_subjectivity_theme.py --repo . --final`.
<!-- PSYCHOANALYSIS-SUBJECTIVITY-W10-END -->


## Education / Examination / Credentialism expansion batch

- batch_id: `W10-EDUCATION-EXAMINATION-CREDENTIALISM-2026-06-16`
- added_cards: 30
- status: pilot-draft; additive social-phenomena close-reading only
- scope: education, examination, credential sorting, school discipline, knowledge indoctrination, expert authority, academic hierarchy, and student/learning subjectivation.
- companion layer: `knowledge/themes/education-examination-credentialism/` provides the manifest, evidence bank, taxonomy, and W3/W5 notes.

These cards remain `pilot-draft`; Education W3/W5 additions remain `draft`; all evidence quotes are validated as exact substrings of `split_md_clean`.

## Family / Intimacy / Marriage / Birth / Social Reproduction expansion batch

- batch_id: `W10-FAMILY-INTIMACY-REPRODUCTION-2026-06-16`
- added_cards: 30
- status: pilot-draft; additive social-phenomena close-reading only
- scope: family, intimacy, marriage, birth, parent-child debt, romance ideology, gendered domestic division, care, and social reproduction.
- companion layer: `knowledge/themes/family-intimacy-reproduction/` provides the manifest, evidence bank, taxonomy, and W3/W5 notes.

These cards remain `pilot-draft`; Family W3/W5 additions remain `draft`; all evidence quotes are validated as exact substrings of `split_md_clean`.

## Governance / Law / Bureaucracy / Order expansion batch

- batch_id: `W10-GOVERNANCE-LAW-BUREAUCRACY-2026-06-16`
- added_cards: 30
- status: pilot-draft; additive social-phenomena close-reading only
- scope: governance, law, bureaucracy, order, administrative organization, rule/procedure fetishism, governance technology, risk/security management, obedience structure, and justice imagination.
- companion layer: `knowledge/themes/governance-law-bureaucracy/` provides the manifest, evidence bank, taxonomy, and W3/W5 notes.

These cards remain `pilot-draft`; Governance-law W3/W5 additions remain `draft`; all evidence quotes are validated as exact substrings of `split_md_clean`.

## Class / Youth / Generation / Mobility Anxiety expansion batch

- batch_id: `W10-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16`
- added_cards: 30
- status: pilot-draft; additive social-phenomena close-reading only
- scope: class position, youth/generation future, mobility blockage, middle-class anxiety, bottom humiliation, success/competition ideology, youth nihilism, and poverty/wealth inequality.
- companion layer: `knowledge/themes/class-youth-generational-anxiety/` provides the manifest, evidence bank, taxonomy, and W3/W5 notes.

These cards remain `pilot-draft`; Class-youth W3/W5 additions remain `draft`; all evidence quotes are validated as exact substrings of `split_md_clean`.


## W10-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16

- Added 30 Psychological Distress / Anxiety / Addiction / Social Symptom pilot-draft cards from G024.
- Source: `knowledge/themes/psychological-distress-social-symptom/psychological-distress-social-symptom-evidence-bank.jsonl`.
- Boundary: no clinical diagnosis, therapy advice, psychiatric authority, or current-events mental-health commentary.

## Urban / Housing / Migration / Space social-phenomena batch — 2026-06-16

- Added 30 pilot-draft W10 cards from `knowledge/themes/urban-housing-migration-space/`.
- Cards remain close-reading aids, not a city/housing policy matrix.

## Health / Body / Medicine / Risk Society social-phenomena batch — 2026-06-16

- Added 30 pilot-draft W10 cards from `knowledge/themes/health-body-risk-society/`.
- Cards remain close-reading aids, not a medical or public-health advice layer.
