# Examples

Small reproducible entrypoints for using ISMISM Library after cloning the repository.

## Validate the library

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
```

## Query a social topic

```bash
python3 tools/ismism.py query social 内卷 --limit 3
```

## Query core library layers

```bash
python3 tools/ismism.py query concept 主体 --limit 3
python3 tools/ismism.py query relation 主体 --limit 3
python3 tools/ismism.py query position 3-4-2
python3 tools/ismism.py query trace 176 --limit 5
```

## Regenerate derived corpus metadata

```bash
python3 tools/internal/build_corpus_manifest.py
python3 tools/internal/build_segments.py --start-row 1 --batch-size 1 --rebuild-index
```

Both generation commands should preserve repository-relative paths and pass:

```bash
python3 tools/validate/library_contract.py --repo . --residue-only
```
