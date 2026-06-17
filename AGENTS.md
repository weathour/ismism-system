# ISMISM Library Agent Guide

This repository is an evidence-backed ISMISM Library product.

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
11. `library/syntheses/`
12. `library/protocols/`

## Operating priorities

1. Preserve corpus bytes and row order.
2. Preserve segment, row, path, and quote traceability.
3. Keep concept, relation, position, and close-reading layers validator-backed.
4. Keep public docs and tool names product-oriented.
5. Prefer small auditable changes and run validators before claiming completion.

## Normal validation

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
python3 tools/validate/library_contract.py --repo . --residue-only
```

## Editing boundaries

- Do not rewrite `corpus/raw-markdown/` or `corpus/clean-markdown/` unless the task is explicit source correction.
- Do not weaken exact quote checks.
- Do not add dependencies without an explicit requirement.
- Put durable review evidence in `reviews/` and acceptance evidence in `qa/`.
