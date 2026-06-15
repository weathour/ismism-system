---
name: ismism-knowledge-operator
description: Operate the standalone ISMISM knowledge-processing repository. Use when Codex is working in or from `ismism-system` to answer ISMISM questions, inspect terms/positions/relations, extend the knowledge layer, validate outputs, design external references, or avoid legacy frontend/Atlas misuse while preserving row, segment, and quote traceability.
---

# ISMISM Knowledge Operator

## Core stance

Treat `ismism-system` as a corpus-backed theory-processing repo, not a normal wiki, frontend app, or generic philosophy encyclopedia. Preserve row / segment / quote traceability before interpretation.

## Read first

When starting in this repo, read only what the task needs, but use this order:

1. `AGENTS.md`
2. `README.md`
3. `DIRECTORY_MAP.md`
4. `ISMISM-MAINLINE-HANDOFF.md`
5. `knowledge/STATE.md`
6. `knowledge/usage-protocol.md` and `knowledge/query-playbook.md` for query tasks
7. `knowledge/export-manifest.md` for external-consumer tasks
8. `knowledge/w10-absorption/PLAN.md` and `knowledge/w10-absorption/index.md` for further-absorption tasks

For matrix movement or relation interpretation, also read `knowledge/references/movement-patterns-guide.md`.

## Source priority

When sources disagree, prefer:

1. `目录索引_结构化.csv`
2. `split_md/` and `split_md_clean/`
3. `knowledge/manifests/*`
4. `knowledge/segment-cards/*`
5. `knowledge/lexicon/*`
6. `knowledge/position-cards/*`
7. `knowledge/relations/*`
8. `knowledge/qa/*`
9. `knowledge/syntheses/*`
10. `knowledge/w10-absorption/*` as pilot-draft close-reading aids
11. `Zhuyi_Matrix_Engine/Phase*` as method hints only
12. `Zhuyi_Matrix_Engine/Atlas_DB/*` as candidate data only
13. `docs/archive/*` as historical/tombstone data only

## Query workflows

### Term meaning or ambiguity

Use:

```text
term → knowledge/lexicon/term-senses.jsonl → sense_id → evidence_quotes
→ source_segments.clean_md_path → checked quote → optional synthesis
```

Optional helper:

```bash
python3 knowledge/scripts/query_term.py <term>
python3 knowledge/scripts/trace_evidence.py <sense_id>
```

Do not merge senses merely because they share one Chinese word. Cite the exact `sense_id` when making interpretive claims.

### Matrix position or doctrine location

Use:

```text
doctrine / coordinate → 目录索引_结构化.csv → knowledge/position-cards/{coordinate}.md
→ associated rows → W3 terms → W5 relations
```

Optional helper:

```bash
python3 knowledge/scripts/query_position.py <coordinate-or-title>
```

Treat coordinates as identifiers, not display-only labels.

### Relation, transition, movement, boundary, or misrecognition

Use:

```text
relation-assets.jsonl → relation_type / relation_id → source and target senses
→ source_position / target_position → evidence_segment → W6 audit if needed
```

Optional helper:

```bash
python3 knowledge/scripts/query_relation.py --type <relation_type>
python3 knowledge/scripts/trace_evidence.py <relation_id>
```

Use controlled relation types. Do not replace them with vague “related to” language.

### Overview or synthesis

Use W7 syntheses as maps after checking W3/W4/W5, unless the user explicitly asks for a field overview. Do not treat a synthesis as independent evidence.

### Further absorption / close reading

Use W10 cards when the task asks for argument structure, staged practice/process, or figure/school case positioning that is too detailed for W2 and not captured by W3/W5. Treat W10 as pilot-draft, verify `evidence_quotes` against `split_md_clean/`, preserve `[q1]` claim-to-quote mapping, and check `w3_w5_gap_review` before treating W10 as sufficient.

## Editing discipline

- Do not overwrite `split_md/`.
- Do not casually rewrite `split_md_clean/` unless text cleaning is the explicit task.
- Do not edit `MASTER-SPEC.md` or `Zhuyi_Matrix_Engine/` unless the user explicitly asks and the change is justified.
- Keep W3 term senses and W5 relations in `draft` unless an explicit promotion audit exists.
- Prefer small auditable batches in `knowledge/`.
- Keep every new interpretive claim traceable to row / segment / quote evidence.
- Update `knowledge/logs/operation-log.md` for substantial changes.
- Do not write outside this repository during normal ISMISM work.

## Legacy boundaries

Old frontend/product surfaces were removed. Do not restore `src/`, `dist/`, old `docs/00-*` through `docs/16-*`, or old cleanup handoff snapshots unless the user explicitly requests historical recovery.

Use `Zhuyi_Matrix_Engine/Atlas_DB/*` only as candidate generator, evidence bridge, summary seed, or unresolved backlog. Never treat Atlas as final truth.

## Validation

Before delivery after edits, run the narrowest relevant validators. For broad changes, run:

```bash
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
```
