# ISMISM Library Status

## Current Known Corpus State

- `corpus/registry/toc.csv`: 363 rows.
- `library/manifests/segments.jsonl`: 363 segment records.
- `segments.jsonl`: 363
- `library/manifests/chunks.jsonl`: chunk records cover all available segments.
- `chunks.jsonl`: covers all available segments.
- `corpus/raw-markdown/`: 363 files.
- `corpus/clean-markdown/`: 363 files.
- row 176 clean text redone and available.

## Current Library Counts

- Concept senses: 1676 records, 1228 terms.
- Relations: 1044 records, 12 relation types.
- Close-reading cards: 741 records, 3 card types.
- Theme dossiers: 18 directories under `library/themes/`.
- Full concept+relation+close-reading row overlap: 277 rows.

## Current Product Surface

- Corpus package: `corpus/`.
- Curated library package: `library/`.
- Documentation package: `docs/`.
- Tool package: `tools/`.
- Review evidence: `reviews/`.
- Acceptance evidence: `qa/`.

## Validation Entry Points

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
python3 tools/validate/library_contract.py --repo . --residue-only
```
