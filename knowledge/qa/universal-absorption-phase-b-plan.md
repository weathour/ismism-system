# Universal Absorption Phase B Plan

- date: 2026-06-16 CST
- status: execution plan generated from post-Phase-A W1/W2-only baseline
- mode: non-theme universal absorption repair
- batch ids: `W3-UNIVERSAL-B-2026-06-16`, `W5-UNIVERSAL-B-2026-06-16`, `W10-UNIVERSAL-B-2026-06-16`

## Baseline

Phase B starts from the Phase A handoff snapshot: 49 rows remained W1/W2-only, with 92.6% clean-text volume covered by at least one of W3/W5/W10 and 176 rows in full W3+W5+W10 overlap.

## Target selection

The gap map covers all 49 baseline rows. Phase B selects 39 field-numbered rows for full W3/W5/W10 overlap repair and leaves 10 rows as explicit context/exclusion backlog.

Target rule: include rows only when the clean text supports a row-specific concept, relation movement, and argument/process/case close reading. Title keywords alone are insufficient.

### Ring A — modern knowledge/science/logic/idealism repair

Targets include rows 147, 150, 162, 163, 164, 180, 181, 196, 197, 198, 202, 203, 210, 212, 224, 234, 242, and 250, with emphasis on induction, logic, anti-realism, judgment, German Idealism, phenomenological field, and subjectivity repair.

### Ring B — writing/communication/organization/practice repair

Targets include rows 281, 286, 287, 294, 301, 302, 303, 304, 306, and 310, treated as practical-method rows: writing, communication, organization, decision, program, review, and failure-mode repair.

### Ring C — everyday ideology / behavior technology repair

Targets include rows 12, 20, 22, 23, 47, 56, 67, 77, and 78, connecting cultural ontology, behavior analysis, sophistic discourse, normalizing technique, and everyday ideology to the method spine.

### Ring D — explicit context/exclusion review

Rows 3, 68, 69, 70, 71, 72, 73, 74, 297, and 307 remain W1/W2-only after Phase B by design. They are recorded in the gap map with context/exclusion rationale rather than mechanically absorbed.

## Planned outputs

- 117 exact evidence records (3 per target row).
- 78 W3 draft term senses (2 per target row).
- 78 W5 draft relation assets (2 per target row).
- 39 W10 pilot-draft cards (one per target row).
- Limited phase-level synthesis notes, distribution/navigation updates, and QA reports.

## Validation order

1. Validate Phase B exact evidence and batch shape with `validate_universal_absorption_phase_b.py`.
2. Validate W3/W5/W10 globally and by batch.
3. Rerun Phase A and existing theme validators.
4. Run negative temp-copy checks for evidence, W3 status, W10 evidence, synthesis markers, and protected corpus.
