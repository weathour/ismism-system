# Validation Guide

## Core validation

```bash
python3 tools/validate/corpus_manifest.py --repo .
python3 tools/validate/concepts.py --repo .
python3 tools/validate/positions.py --repo .
python3 tools/validate/relations.py --repo . --min-count 1044 --require-type-min 2
python3 tools/validate/close_reading.py --repo .
python3 tools/validate/library_contract.py --repo .
python3 tools/validate/social_topics.py --repo . --final
```

Or run:

```bash
python3 tools/ismism.py validate core
```

## Theme validation

```bash
for f in tools/validate/themes/*.py; do
  python3 "$f" --repo . --final
done
```

## Product surface validation

```bash
python3 tools/validate/library_contract.py --repo . --residue-only
```

## Byte-preservation check after corpus moves

```bash
python3 tools/internal/validate_library_contract.py --repo . --bytes-only
```

## Codex plugin validation

```bash
python3 <plugin-creator-skill>/scripts/validate_plugin.py .
```

Run this after editing `.codex-plugin/plugin.json` or skill metadata.
