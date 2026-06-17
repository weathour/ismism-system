# Export Manifest

The exportable project surface is the corpus plus current knowledge layer.

## Include

- `PROJECT-SPEC.md`, `README.md`, `AGENTS.md`, `DIRECTORY_MAP.md`, `ISMISM-MAINLINE-HANDOFF.md`.
- `目录索引_结构化.csv`, `目录索引_结构化.md`.
- `split_md/`, `split_md_clean/`, root PDF if distribution rights permit.
- `knowledge/manifests/`, `segment-cards/`, `lexicon/`, `position-cards/`, `relations/`, `w10-absorption/`, `themes/`, `syntheses/`, `qa/`, `references/`, `scripts/`, `templates/`, `prompts/`.
- `skills/ismism-knowledge-operator/SKILL.md`.

## Exclude

- Runtime state, caches, virtual environments, generated candidate runs, temporary test folders, PDF slice regenerations unless explicitly requested.
- Local tool state such as `.omx/`, `omx_wiki/`, `.ruff_cache/`, `__pycache__/`.

## Validation marker

Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
