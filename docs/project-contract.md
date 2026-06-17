# ISMISM Library Project Contract

ISMISM Library is a Codex-native, corpus-first interpretation system. It is not a neutral encyclopedia, not a personal note dump, and not a standalone essay collection. Every curated layer must remain anchored to source rows, segment records, clean transcript paths, and exact quote evidence. The public positioning baseline is `docs/product-positioning.md`.

## Product modules

- `docs/product-positioning.md`: public positioning baseline and product direction.
- `corpus/`: source package and transcript markdown.
- `library/manifests/`: corpus and segment manifests.
- `library/segments/`: segment cards.
- `library/concepts/`: concept senses and concept notes.
- `library/positions/`: matrix position cards.
- `library/relations/`: relation graph records.
- `library/close-reading/`: argument, process, and case cards.
- `library/themes/`: theme dossiers with row manifests and quote banks.
- `library/audits/`: durable audit records.
- `library/syntheses/`: synthesis documents.
- `tools/`: ingestion, validation, and query commands.
- `.codex-plugin/plugin.json`: Codex plugin identity for loading the repository as `ismism-system`.
- `skills/`: Codex skill protocol for agent-assisted ISMISM operation.

## Traceability contract

A valid curated record must keep enough information to resolve:

1. row identifier;
2. segment identifier;
3. clean transcript path;
4. exact quote text where a claim depends on source wording;
5. concept, relation, position, or close-reading identifiers where cross-layer links are made.

## Completion contract

Substantial changes should pass:

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
python3 tools/validate/library_contract.py --repo . --residue-only
python3 <plugin-creator-skill>/scripts/validate_plugin.py .
```
