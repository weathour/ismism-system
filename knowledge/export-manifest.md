# W8 Export Manifest

- status: draft protocol
- created: 2026-06-09 CST
- scope: stable read interfaces for external or future local systems. This is not a runtime API; it is a file-level contract.

## 1. Exportable layers

| layer | file or directory | format | stability |
|---|---|---|---|
| W1 segments | `knowledge/manifests/segments.jsonl` | JSONL | canonical |
| W2 segment cards | `knowledge/segment-cards/*.md` | Markdown | curated evidence cards |
| W3 term senses | `knowledge/lexicon/term-senses.jsonl` | JSONL | draft interpretation |
| W4 position cards | `knowledge/position-cards/*.md` | Markdown | draft interpretation |
| W5 relations | `knowledge/relations/relation-assets.jsonl` | JSONL | draft interpretation |
| W6 QA | `knowledge/qa/*.md` | Markdown | audit layer |
| W7 syntheses | `knowledge/syntheses/*.md` | Markdown | draft synthesis |

## 2. W3 term-sense record contract

Required fields:

```text
sense_id, term, sense_label, definition, axis, evidence_quotes,
position_context, contrast_with, forbidden_mix, source_segments,
confidence, status, audit_notes, schema_version, batch_id, created, updated
```

Export rule: consumers must preserve `sense_id`, `status`, `evidence_quotes`, and `source_segments`.

## 3. W5 relation record contract

Required fields:

```text
relation_id, source, target, relation_type, definition, evidence,
applicability_boundary, forbidden_interpretation, status, confidence,
source_senses, batch_id, created, source_position, target_position,
evidence_segment
```

Export rule: consumers must preserve `relation_type`, `applicability_boundary`, and `forbidden_interpretation` to prevent over-generalization.

## 4. Position-card contract

Every position card should expose:

```text
coordinate, title, matrix axes, position definition, representative doctrines,
core mechanism, adjacent-position relations, associated terms, source rows
```

Export rule: position coordinates are identifiers; do not rewrite them into display-only labels.

## 5. Recommended read endpoints

These are file paths for future tooling:

```text
GET terms: knowledge/lexicon/term-senses.jsonl
GET positions: knowledge/position-cards/index.md + knowledge/position-cards/{coordinate}.md
GET relations: knowledge/relations/relation-assets.jsonl
GET syntheses: knowledge/syntheses/*.md
GET QA state: knowledge/qa/validation-report.md and related W6 reports
```

## 6. Non-exportable as truth

Do not export the following as canonical interpretation:

- `Zhuyi_Matrix_Engine/Atlas_DB/*`
- old frontend `src/` / `dist/`
- raw candidate caches under `knowledge/lexicon/candidates/`
- historical archive docs as current state

They may be exposed only as legacy/candidate material with labels.

## 7. Validation commands for consumers

Before using an exported package, run:

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
```
