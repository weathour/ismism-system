# ISMISM Knowledge Layer

This directory is the canonical processing layer for converting `ismism-system` from a failed interaction/frontend prototype into a searchable, auditable, citable, and re-synthesizable ISMISM theoretical reference knowledge base.

Current repo-level handoff: `../ISMISM-MAINLINE-HANDOFF.md`.

## Read first

1. `DIGESTION_PROGRAM.md` — master program and phase plan.
2. `STATE.md` — live compaction-resistant state; resume from its `Next Action`.
3. `logs/operation-log.md` — chronological operation log.
4. `w10-absorption/PLAN.md` and `w10-absorption/index.md` — current pilot further-absorption layer.
5. `../DIRECTORY_MAP.md` — concise current directory/function map.

## Current artifacts

### W1 — corpus manifests

- `manifests/corpus-manifest.json` — corpus-level inventory, counts, source truth layers, path integrity, decisions.
- `manifests/segments.jsonl` — 363 TOC rows registered as stable segment objects.
- `manifests/chunks.jsonl` — 1,594 retrieval chunks across the 363 available clean text segments.
- `manifests/missing-and-anomalies.md` — W1 异常与派生层状态（`split_pdf/`仅部分恢复，包含 row 176）。
- `scripts/build_w1_manifests.py` — deterministic script that generated the W1 artifacts.

### W2 — segment cards

- `segment-cards/index.md`
- `segment-cards/*.md` — 363 draft segment cards.

### W3 — term senses

- `lexicon/term-senses.jsonl` — 544 draft term senses across 200 terms.
- `lexicon/core-terms.md`
- `lexicon/ambiguous-terms.md`
- `qa/w3-lexicon-audit.md`

### W5 — relation assets

- `relations/relation-assets.jsonl` — 60 draft relation assets covering 12 relation types.
- `relations/*-cards.md`
- `qa/w5-relation-audit.md`

### W4 — position cards

- `position-cards/index.md`
- `position-cards/*.md` — 256 draft position cards.

### W6/W7/W8/W9 — audit, synthesis, protocol, integration

- `qa/validation-report.md`, `qa/concept-drift-report.md`, `qa/evidence-claim-audit.md`, `qa/rejected-interpretations.md`
- `syntheses/*.md` — 6 draft syntheses.
- `usage-protocol.md`, `query-playbook.md`, `export-manifest.md`
- `integration/psychoanalytic-writing-lab/ismism-reference-protocol.md` — repo-local W9 lightweight index, accepted as sufficient for this repository on 2026-06-10 CST.

### W10 — further absorption pilot

- `w10-absorption/PLAN.md` — W10 scope, boundaries, and future batch plan.
- `w10-absorption/index.md` — pilot card index.
- `w10-absorption/argument-cards/*.md`, `process-cards/*.md`, `case-cards/*.md` — 5 pilot-draft close-reading cards across 3 card types.
- `scripts/validate_w10_absorption.py` — W10 metadata/index/quote-substring validator.
- `qa/w10-pilot-audit.md` — pilot audit and validation evidence.
- `qa/w10-ultraqa-report.md` — adversarial validator/QA report for the W10 pilot batch.
- `qa/absorption-strength-distribution.md` — row-level W1/W2 vs W3/W5/W10 absorption strength snapshot.
- `qa/w10-w3-w5-gap-followups.md` — queue for W10 rows that need later W3/W5 upstream-gap review.

### Read-only query helpers

- `scripts/query_term.py` — W3 term-sense lookup by term, sense ID, or row.
- `scripts/query_position.py` — W4 position-card lookup by coordinate or title.
- `scripts/query_relation.py` — W5 relation lookup by type, ID, endpoint, or evidence row.
- `scripts/trace_evidence.py` — trace term/relation/row evidence back to clean text.
- `scripts/validate_w10_absorption.py` — validate W10 cards against W1 segment metadata and clean text quote substrings.

## Current source status

- `目录索引_结构化.csv`: 363 rows.
- `split_md/`: 363 actual markdown files.
- `split_md_clean/`: 363 actual markdown files.
- Missing text segment: none (row 176 / `2-4-2-4` 已恢复可用)。
- `split_pdf/`: exists with 1 recovered segment (row 176), others pending regeneration; treated as regenerable derived layer.
- `Zhuyi_Matrix_Engine/Atlas_DB/*`: candidate layer only, not canonical truth.

## Non-goals

- Do not revive the old frontend.
- Do not process RMH/GJW here.
- Do not treat `split_md_clean/` as the finished knowledge base.
- Do not treat Atlas_DB as canonical truth.
- Do not promote W3/W5 draft records to canonical without a separate review step.
- Do not treat W10 pilot cards as canonical summaries; they are draft argument/process/case close-reading aids.
