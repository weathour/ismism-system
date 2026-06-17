# Library Audits

This directory contains product-level quality records for the ISMISM Library.
Detailed traceability lives in the canonical data assets themselves:

- corpus integrity: `library/manifests/content-integrity.json`
- row and chunk manifests: `library/manifests/segments.jsonl`, `library/manifests/chunks.jsonl`
- concepts: `library/concepts/term-senses.jsonl`
- relations: `library/relations/relation-assets.jsonl`
- close readings: `library/close-reading/`
- theme row/evidence packages: `library/themes/*/`

Use `python3 tools/ismism.py validate all` before publishing or extending the library.
