# Validation Matrix

Run the smallest validation that proves the claim, then broaden for publication or plugin readiness.

## Cross-repository validation rule

When Codex is operating from another repository, run validators through the bundled wrapper:

```bash
python3 <this-skill-dir>/scripts/ismism.py validate core
python3 <this-skill-dir>/scripts/ismism.py validate all
python3 <this-skill-dir>/scripts/ismism.py validate residue
```

For direct validator scripts, resolve the plugin root first:

```bash
ISMISM_ROOT=$(python3 <this-skill-dir>/scripts/ismism.py root)
python3 "$ISMISM_ROOT/tools/validate/library_contract.py" --repo "$ISMISM_ROOT" --residue-only
```

## Common validators

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
python3 tools/ismism.py validate residue
python3 tools/validate/library_contract.py --repo . --bytes-only
python3 <plugin-creator-skill>/scripts/validate_plugin.py .
python3 <skill-creator-skill>/scripts/quick_validate.py skills/ismism-knowledge-operator
```

## Changed surface to validator map

| Changed surface | Required validation |
| --- | --- |
| `corpus/registry/`, manifests, segment paths | `python3 tools/validate/corpus_manifest.py --repo .` |
| `corpus/raw-markdown/`, `corpus/clean-markdown/`, `corpus/source/` | byte check plus `python3 tools/ismism.py validate core` |
| `library/concepts/` | `python3 tools/validate/concepts.py --repo .` |
| `library/positions/` | `python3 tools/validate/positions.py --repo .` |
| `library/relations/` | `python3 tools/validate/relations.py --repo . --min-count 1044 --require-type-min 2` |
| `library/close-reading/` | `python3 tools/validate/close_reading.py --repo .` |
| `library/themes/<theme>/` | matching `tools/validate/themes/<theme>.py --repo . --final` |
| social-topic router or social theme set | `python3 tools/validate/social_topics.py --repo . --final` |
| public docs, repo map, product contract | `python3 tools/validate/library_contract.py --repo . --residue-only` |
| `.codex-plugin/plugin.json` | plugin validation plus residue validation |
| `skills/ismism-knowledge-operator/` | skill quick validation plus plugin validation |
| `tools/ismism.py`, `tools/query/`, `tools/validate/` | targeted command smoke plus `python3 tools/ismism.py validate core` |

## Publication readiness

Before claiming public-ready state, run:

```bash
python3 tools/ismism.py validate all
python3 tools/validate/library_contract.py --repo . --residue-only
python3 <plugin-creator-skill>/scripts/validate_plugin.py .
git status --short
```

Report the exact pass/fail result and any skipped check. Do not claim readiness from documentation review alone.

## Validation failure handling

1. Read the first concrete error.
2. Fix the smallest affected surface.
3. Re-run the failed validator.
4. Re-run broader validators only after the targeted failure is clean.
5. If a validator cannot run, report the command, failure reason, and next-best evidence.
