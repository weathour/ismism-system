# Theme Absorption Protocol

Use this when creating a new major `library/themes/<theme>/` package or making a large boundary-changing extension to an existing theme. This protocol turns the historical theme-package workflow into a repeatable Codex skill path. It complements `curation-protocol.md`; it does not replace row, quote, validator, or source-order discipline.

## Contents

1. When to use
2. Non-negotiable boundaries
3. Standard theme package shape
4. End-to-end absorption sequence
   - 0. Preflight and donor pattern
   - 1. Scope charter
   - 2. Candidate row scan
   - 3. Row manifest
   - 4. Evidence bank
   - 5. Taxonomy and boundary map
   - 6. Concept, relation, and close-reading batches
   - 7. Syntheses
   - 8. README
   - 9. Query helper
   - 10. Validator
   - 11. Social-topic integration
   - 12. Validation sequence
   - 13. Query smoke checks
   - 14. Completion report
5. Minimal extension path for an existing theme
6. Common failure modes

## When to use

Use this protocol for requests such as:

- create / absorb / curate a new major theme package;
- extend a theme with new row classes, evidence-bank coverage, focused syntheses, query helper, validator, or social-router integration;
- promote a loose synthesis or recurring query route into a validator-backed theme dossier.

Do not use it for a small answer, one concept sense, one relation record, or a minor synthesis edit. For those, use `task-routing.md` and `curation-protocol.md` only.

## Non-negotiable boundaries

1. Start from `corpus/registry/toc.csv`, segment records, and `corpus/clean-markdown/`; never start from a desired thesis.
2. Preserve corpus bytes and row order. Do not edit `corpus/raw-markdown/` or `corpus/clean-markdown/` unless the user explicitly requested source correction.
3. Every included row needs a row-scoped rationale; every evidence record needs an exact quote that appears in the cited clean file.
4. Keep concept and relation additions conservative, usually `draft`; keep new close-reading cards conservative, usually `pilot-draft`, unless a separate promotion audit exists.
5. Do not import external encyclopedia, current-event, policy, clinical, legal, financial, housing, or medical claims into the theme.
6. A theme boundary is a product contract surface: if it changes, update README, taxonomy, query helper, validator, and relevant routing docs together.
7. Prefer small auditable batches. Put durable review evidence in `reviews/` and acceptance evidence in `qa/` when the change is nontrivial.

## Standard theme package shape

A mature theme usually contains:

```text
library/themes/<theme>/
  README.md
  <theme>-row-manifest.jsonl
  <theme>-evidence-bank.jsonl
  <theme>-taxonomy.md
  <theme>-concept-relation-notes.md
  <theme>-synthesis.md
  <focused-synthesis-1>.md
  <focused-synthesis-2>.md
```

Companion tool surfaces usually include:

```text
tools/query/themes/<theme_snake>.py
tools/validate/themes/<theme_snake>.py
```

If the theme is a social-topic route, also inspect and update:

```text
tools/query/social_topics.py
tools/internal/query_social_topics.py
tools/validate/social_topics.py
library/protocols/social-phenomena-diagnostic-protocol.md
library/syntheses/social-phenomena-*.md
```

Only update social routing when the theme genuinely answers user-facing social-topic prompts. Foundational theory themes can remain direct theme helpers without social-topic integration.

## End-to-end absorption sequence

### 0. Preflight and donor pattern

1. Read the current `README.md` of the nearest existing theme packages.
2. Pick one or two donor themes with the closest structure:
   - social diagnostics: Labor, Education, Consumption, Media-platform, Governance, Class-youth, Psychological-distress, Urban-housing, Health-body;
   - theory packages: Psychoanalysis-Subjectivity, Capitalism, Feminism, Religion, Chinese Philosophy, AI, Time-Death, Aesthetics-Media, Science-Academia.
3. Inspect the donor theme's row manifest, evidence bank, taxonomy, query helper, and validator before drafting new files.
4. Run `python3 tools/ismism.py validate core` before editing if the repository state is uncertain.

### 1. Scope charter

Write a short internal scope note before generating assets. It should define:

- theme slug and Chinese name;
- central question;
- inclusion keywords and downstream diagnostic labels;
- explicit exclusions and negative controls;
- likely cross-theme bridges;
- whether the theme is social-topic routed or direct-theme only;
- expected files and validators.

This can live in a review note under `reviews/` for large work, or in the draft README for a small single-session theme.

### 2. Candidate row scan

1. Start with `corpus/registry/toc.csv` and targeted searches in `corpus/clean-markdown/`.
2. Use multiple keyword families, not one label. Include synonyms, older terminology, row-title terms, and likely bridge terms.
3. Record negative controls: rows with keyword hits that are off-function or too generic.
4. Avoid deciding from keyword hits alone; read enough clean text to classify function.

Candidate rows should be classified as one of:

- `core`: central evidence for the theme function;
- `bridge`: row is primarily owned by another theme but supplies a traceable connection;
- `context`: useful boundary/background only;
- `excluded` / `noise-review`: keyword hit or apparent match that should not ground claims.

### 3. Row manifest

Create `<theme>-row-manifest.jsonl` with one JSON object per reviewed row. Reuse the schema pattern from the donor theme. A row record should include at least:

- `schema_version`;
- `row_id`, `segment_id`, `toc_id`, `title`, `clean_md_path`, `field`, `char_count`;
- `keyword_hits`;
- `theme_class`;
- `core_status` or `theme_role`;
- `current_coverage` / `current_layers` when relevant;
- `recommended_next_step`;
- `evidence_quote_count`;
- `diagnostic_rationale`, `notes`, or inclusion/exclusion rationale.

Manifest discipline:

- one theme class per row unless the donor schema explicitly supports multiple classes;
- row order should be stable and auditable;
- excluded/noise rows are valuable boundary controls and should remain visible when they explain query misses or false positives.

### 4. Evidence bank

Create `<theme>-evidence-bank.jsonl` after the manifest, not before it. Each evidence record should include:

- stable evidence id, usually `ev:<theme-prefix>:<row-id>:<n>`;
- `row_id`, `segment_id`, `toc_id`, `title`, `clean_md_path`;
- `theme_class` and/or role fields;
- exact `quote` copied from the cited clean text;
- quote role or rationale when the donor pattern uses it.

Evidence discipline:

1. Verify each quote as an exact substring of `clean_md_path`.
2. Keep excerpts short enough to support the claim without becoming a hidden transcript copy.
3. Do not use paraphrases as quote evidence.
4. Give bridge rows evidence for the bridge function, not merely the donor theme's function.

### 5. Taxonomy and boundary map

Create `<theme>-taxonomy.md` after the first manifest/evidence pass. Include:

- theme classes with short definitions;
- row ownership map by class;
- boundary notes for false positives and downstream labels;
- cross-theme bridge rules.

The taxonomy should be controlled vocabulary for the theme, not a general encyclopedia.

### 6. Concept, relation, and close-reading batches

Add these only after manifest/evidence are stable enough.

Concept batch:

- add row-bound senses to `library/concepts/term-senses.jsonl`;
- use a batch id such as `concept-<THEME-UPPER>-YYYY-MM-DD`;
- keep `status: draft` unless separately reviewed;
- include evidence quotes and `source_segments`.

Relation batch:

- add records to `library/relations/relation-assets.jsonl`;
- use allowed relation types and existing relation schema;
- relation claims must be narrower than evidence;
- include applicability boundary and forbidden interpretation;
- use a batch id such as `relation-<THEME-UPPER>-YYYY-MM-DD`.

Close-reading batch:

- choose argument/process/case card types deliberately;
- keep row id, segment id, toc id, clean path, and quote markers exact;
- keep cards `pilot-draft` unless reviewed;
- do not create close-reading cards just to inflate counts.

Write `<theme>-concept-relation-notes.md` to record batch ids, statuses, intended coverage, and boundary constraints.

### 7. Syntheses

Write the main `<theme>-synthesis.md` only after evidence, taxonomy, and draft concept/relation anchors exist. Add focused syntheses only when they clarify different routes inside the theme.

Synthesis rules:

- synthesize validated assets; do not make synthesis a hidden source layer;
- cite manifest/evidence ids, concept senses, relation ids, close-reading cards, or row ids;
- separate source-backed claims from interpretation;
- include boundary notes and cross-theme bridge conditions;
- avoid broad current-event or professional-advice conclusions.

### 8. README

The theme README is the operator's entry point. It should include:

- title and Chinese name when useful;
- status and date;
- purpose / central question;
- files list;
- counts: manifest rows, evidence quotes, core/bridge/context/excluded where applicable;
- concept/relation/close-reading batch ids and statuses;
- validator command;
- query helper command;
- scope markers and interpretation rules.

### 9. Query helper

Create `tools/query/themes/<theme_snake>.py` by copying the closest donor helper and narrowing it. The helper should support at least:

- keyword query;
- `--row <id>`;
- `--class <theme_class>` or equivalent;
- compact row output with evidence excerpts.

Then expose the helper through `tools/query/themes/` wrapper if this repository uses wrappers for the donor pattern.

### 10. Validator

Create `tools/validate/themes/<theme_snake>.py` by copying the closest donor validator and narrowing it. It should check at least:

- required files exist;
- manifest JSONL parses;
- evidence JSONL parses;
- every evidence quote is an exact substring of the cited clean file;
- manifest/evidence row ids line up;
- class/status fields use allowed values;
- synthesis files and README references exist when required;
- final mode count expectations, if the theme is being closed.

Do not weaken exact-quote checks to make a theme pass.

### 11. Social-topic integration, only if applicable

If the theme should answer everyday social prompts:

1. Add route metadata to social-topic query/validator surfaces following the donor theme pattern.
2. Add prompt keywords and downstream labels conservatively.
3. Add social synthesis bridge only when row evidence supports it.
4. Run social-topic validation.

If the theme is foundational or theoretical, keep it queryable through direct theme helper and concept/relation routes instead.

### 12. Validation sequence

Run targeted validators in dependency order:

```bash
python3 tools/validate/themes/<theme_snake>.py --repo . --final
python3 tools/validate/concepts.py --repo .
python3 tools/validate/relations.py --repo . --min-count <current-floor> --require-type-min 2
python3 tools/validate/close_reading.py --repo .
python3 tools/validate/library_contract.py --repo . --residue-only
```

If social routing changed:

```bash
python3 tools/validate/social_topics.py --repo . --final
```

Before claiming broad readiness:

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
```

Report exact commands and pass/fail results.

### 13. Query smoke checks

Run at least three query checks before closing a theme:

```bash
python3 tools/query/themes/<theme_snake>.py <central-keyword> --limit 3
python3 tools/query/themes/<theme_snake>.py --row <core-row-id>
python3 tools/query/themes/<theme_snake>.py --class <theme-class> --limit 3
```

For social themes, also run:

```bash
python3 tools/query/social_topics.py <user-facing-prompt> --limit 3
```

### 14. Completion report

A theme absorption completion report should state:

- files changed;
- manifest/evidence counts;
- concept/relation/close-reading batch ids and statuses;
- query helper and validator added or reused;
- social-router impact, if any;
- validators run and results;
- remaining draft statuses, boundary risks, and excluded/noise controls.

## Minimal extension path for an existing theme

For a smaller extension to an existing theme:

1. Read the existing README, manifest, evidence bank, taxonomy, helper, and validator.
2. Add new rows to manifest with conservative role/status.
3. Add exact quote records and update counts.
4. Update taxonomy and synthesis only where the new evidence changes coverage.
5. Update validator count expectations if the validator encodes them.
6. Run the theme validator, then residue validation, then `validate all` if the change is public or cross-theme.

## Common failure modes

- Keyword-only inclusion: a row is included because a word appears, not because the theme function is present.
- Synthesis-first drift: the theme thesis is written before manifest/evidence anchors exist.
- Hidden external claims: current events or encyclopedia facts enter README or synthesis without corpus evidence.
- Boundary mismatch: taxonomy says one thing, validator accepts another, and query helper prints a third.
- Draft promotion: concept/relation/close-reading assets are treated as final without review.
- Validator weakening: exact-quote or schema checks are relaxed instead of fixing records.
- Social over-routing: a foundational theory theme is forced into social-topic routing without user-facing diagnostic value.
