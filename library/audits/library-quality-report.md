# Library Quality Report

- status: PASS
- scope: product structure, corpus integrity, traceability layers, theme packages, public-surface hygiene

## Current size

| Layer | Count |
|---|---:|
| corpus rows | 363 |
| chunks | 1594 |
| concept senses | 1676 |
| relation assets | 1044 |
| close-reading cards | 741 |
| theme dossiers | 18 |
| source-integrity records | 731 |

## Contract

The library is valid when all of the following hold:

1. source files live under `corpus/` and match `library/manifests/content-integrity.json`;
2. curated assets live under `library/` and keep row, segment, path, and quote anchors;
3. docs and command-line wrappers expose only the product layout;
4. validation commands pass without errors.

## Verification command

```bash
python3 tools/ismism.py validate all
python3 tools/validate/library_contract.py --repo . --residue-only
python3 tools/validate/library_contract.py --repo . --bytes-only
```
