# Universal Absorption Phase B Audit

- date: 2026-06-16 CST
- status: PASS / complete as draft-pilot row-level repair
- repo: `/home/weathour/文档/ismism-system`

## What moved

Phase B moved 39 rows from W1/W2-only into full W3+W5+W10 overlap.

- W1/W2-only rows: 49 → 10
- W3 rows: 289 → 328
- W5 rows: 205 → 244
- W10 rows: 214 → 253
- full W3+W5+W10 overlap: 176 → 215
- any W3/W5/W10 clean-text volume: 92.6% → 99.55%

## Deliverables

- `knowledge/qa/universal-absorption-phase-b-gap-map.jsonl`: 49 rows, including all post-Phase-A W1/W2-only rows.
- `knowledge/qa/universal-absorption-phase-b-evidence-bank.jsonl`: 117 exact-substring quotes.
- `knowledge/lexicon/term-senses.jsonl`: 78 Phase B W3 draft senses.
- `knowledge/relations/relation-assets.jsonl`: 78 Phase B W5 draft relations.
- `knowledge/w10-absorption/*-cards/*universal-phase-b*.md`: 39 W10 pilot-draft cards.

## Field repair

- Field 1 W1/W2-only rows: 10 → 1.
- Field 2 W1/W2-only rows: 9 → 0.
- Field 3 W1/W2-only rows: 11 → 0.
- Field 4 W1/W2-only rows: 12 → 2.

## Remaining backlog

The 10 remaining W1/W2-only rows are explicitly context/exclusion reviewed in the gap map: 3, 297, 307, 68, 69, 70, 71, 72, 73, 74.
