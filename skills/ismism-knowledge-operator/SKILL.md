---
name: ismism-knowledge-operator
description: Operate ISMISM Library as a Codex plugin for corpus-traceable interpretation, query, curation, and validation. Use when working with ISMISM concepts, relations, positions, themes, close-reading cards, row traces, evidence-backed social or theory analysis, library edits, plugin readiness, or publication checks.
---

# ISMISM Knowledge Operator

Use this skill to operate ISMISM Library without breaking corpus traceability. The skill must work from any user repository after plugin installation; do not assume the current working directory is the ISMISM repository.

## Cross-repository operation

Prefer the bundled wrapper whenever Codex is not already in the ISMISM plugin root:

```bash
python3 <this-skill-dir>/scripts/ismism.py query concept 主体 --limit 3
python3 <this-skill-dir>/scripts/ismism.py query social 内卷 --limit 3
python3 <this-skill-dir>/scripts/ismism.py root
```

Resolve `<this-skill-dir>` from the path of the loaded `SKILL.md` file. The wrapper locates the plugin root from its own path and runs `tools/ismism.py` there. To read a returned relative path, first get the root:

```bash
ISMISM_ROOT=$(python3 <this-skill-dir>/scripts/ismism.py root)
sed -n '1,80p' "$ISMISM_ROOT/<returned-relative-path>"
```

Use `ISMISM_LIBRARY_ROOT=/absolute/path/to/ismism-system` only when intentionally overriding the bundled plugin copy. Treat the ISMISM root as read-only when answering from another repository unless the user explicitly asks for ISMISM curation.

## Core rules

1. Start from evidence: row id, segment id, clean transcript path, exact quote, or validator output.
2. Separate source-backed claims from agent inference.
3. Read cited `corpus/clean-markdown/` text before making close interpretive claims.
4. Do not rewrite `corpus/raw-markdown/` or `corpus/clean-markdown/` unless the task is explicit source correction.
5. Do not present ISMISM output as medical, legal, policy, financial, housing, clinical, or current-event advice.
6. Validate before claiming completion after any edit.

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

## Load references by task

- Querying or choosing tools: read `references/task-routing.md`.
- Writing an interpretive answer: read `references/answer-contract.md`.
- Editing curated assets: read `references/curation-protocol.md` and `references/validation-matrix.md`.
- Validating publication/plugin readiness: read `references/validation-matrix.md`.
- Testing this skill itself: read `references/forward-tests.md`.

## Command contract

When already in the plugin root, these commands are valid:

```bash
python3 tools/ismism.py query social 内卷 --limit 3
python3 tools/ismism.py query concept 主体 --limit 3
python3 tools/ismism.py query relation 主体 --limit 3
python3 tools/ismism.py query position 3-4-2
python3 tools/ismism.py query trace 176 --limit 5
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
python3 tools/ismism.py validate residue
```

From any other repository, replace `python3 tools/ismism.py` with `python3 <this-skill-dir>/scripts/ismism.py`. Use direct helpers under `tools/query/themes/` or `tools/validate/themes/` only after resolving the plugin root.

## Stop rule

A task is complete only when the answer or edit includes evidence anchors and the smallest sufficient validation has passed. If validation cannot run, state the exact gap and use the next-best check.
