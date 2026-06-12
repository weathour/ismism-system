# ISMISM Reference Protocol — Lightweight External Index Draft

- status: W9-ready repo-local draft
- created: 2026-06-09 CST
- intended external target: `psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- boundary: this file is prepared inside `ismism-system` only; no write outside this repository is performed by this agent.

## Purpose

This protocol lets an external writing workspace reference ISMISM without copying the full corpus or treating ISMISM as a subordinate wiki.

## Minimal lookup contract

External consumers should call back into this repository for evidence:

1. term lookup: `knowledge/lexicon/term-senses.jsonl`
2. position lookup: `knowledge/position-cards/{coordinate}.md`
3. relation lookup: `knowledge/relations/relation-assets.jsonl`
4. field overview: `knowledge/syntheses/part-*.md`
5. method overview: `knowledge/syntheses/methodological-core.md`
6. QA state: `knowledge/qa/validation-report.md` and W6 reports

## Coordinate map

| field | coordinate | synthesis | use |
|---|---|---|---|
| realism | `1` | `knowledge/syntheses/part-1-realism.md` | science, paradigm, community, crisis |
| metaphysics | `2` | `knowledge/syntheses/part-2-metaphysics.md` | eventality, time/space, ontology mechanisms |
| idealism | `3` | `knowledge/syntheses/part-3-idealism.md` | symbol systems, subjectivity, constellation, Event/site |
| praxis | `4` | `knowledge/syntheses/part-4-praxis.md` | study/research, reality/theory loop, feasibility, action |
| whole system | `1-4` | `knowledge/syntheses/whole-system-map.md` | cross-field movement |
| method | n/a | `knowledge/syntheses/methodological-core.md` | query and interpretation method |

## High-use terms

| use case | start with these W3 terms |
|---|---|
| term ambiguity | `主体`, `客体`, `理论`, `现实`, `星丛`, `Event`, `site`, `position` |
| science/paradigm | `科学史`, `范式`, `常态范式`, `范式革命`, `学科矩阵`, `不可通约性` |
| metaphysics | `事件性`, `本体论`, `时间化`, `空间化`, `本体论化`, `去本体论化` |
| idealism | `星丛`, `无调性`, `回溯性逻辑`, `本体论更新`, `数学话语`, `真理显现方式` |
| praxis | `学习`, `研究`, `现实理论化`, `理论现实化`, `可行性`, `严肃` |
| method | `观察`, `分析`, `回溯`, `中介`, `通俗化`, `理论劳动` |

## Citation rule

External writing must cite ISMISM claims with at least one of:

```text
[row N, term:<term>:sNN, position X-Y-Z-W]
[row N, relation rel:...]
[file knowledge/syntheses/<name>.md, claim source tag]
```

When a statement is based on a W7 synthesis, follow its source tag back to W3/W4/W5 before using it as evidence.

## Boundary rules

- Do not copy the full ISMISM corpus into an external workspace.
- Do not treat Atlas_DB as canonical evidence.
- Do not treat W3/W5 draft records as promoted truth.
- Do not use ISMISM to classify persons.
- Do not let old frontend/product files drive interpretation.
- Do not add external theory to ISMISM claims without row/segment/quote evidence.

## Validation before use

Run in `ismism-system` before relying on the export:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
```
