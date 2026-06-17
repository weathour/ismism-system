---
name: ismism-knowledge-operator
description: Operate the ISMISM Library with corpus traceability, product paths, validators, and query helpers.
---

# ISMISM Knowledge Operator

Use this skill when editing or querying the ISMISM Library.

## Source order

1. `corpus/registry/toc.csv`
2. `corpus/raw-markdown/` and `corpus/clean-markdown/`
3. `library/manifests/`
4. `library/segments/`
5. `library/concepts/`
6. `library/positions/`
7. `library/relations/`
8. `library/close-reading/`
9. `library/themes/`
10. `library/audits/`

## Required checks

```bash
python3 tools/ismism.py validate core
python3 tools/validate/library_contract.py --repo . --residue-only
```

Use theme validators when changing `library/themes/`.
