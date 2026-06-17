# ISMISM Library

ISMISM Library is a corpus-backed interpretation system for the ISMISM transcript collection. It combines source transcripts, curated segment records, concept senses, matrix positions, relation graphs, close-reading cards, theme dossiers, audits, and command-line validation/query tools.

The repository is designed around three guarantees:

1. **Traceability** — every interpretive claim keeps row, segment, path, and quote anchors.
2. **Layer separation** — source corpus, curated library, documentation, and tools live in separate product modules.
3. **Validator-backed use** — normal work ends with reproducible validation and query smoke checks.

## Repository layout

```text
corpus/   source PDF, table of contents, raw transcript markdown, clean transcript markdown
library/  curated manifests, segments, concepts, positions, relations, close-reading cards, themes, audits
docs/     product contract, architecture, status, validation, query and usage guides
tools/    ingestion, validation, query helpers, and the ISMISM command runner
reviews/  product architecture review evidence
qa/       product acceptance evidence
skills/   operator protocol for agent-assisted curation
```

## Quick checks

```bash
python3 tools/ismism.py validate core
python3 tools/query/social_topics.py 内卷 --limit 3
python3 tools/query/concept.py 主体
```

For the full suite:

```bash
python3 tools/ismism.py validate all
```

## Current library size

- 363 corpus rows with raw and clean transcript markdown.
- 1676 concept senses across 1228 terms.
- 1044 relation records across 12 relation types.
- 741 close-reading cards across argument, process, and case forms.
- 18 theme dossiers with row manifests and exact quote evidence.

## Working rule

Do not edit transcript text unless the task is explicitly source correction. Normal work should extend or validate `library/` while preserving exact quote evidence against `corpus/clean-markdown/`.
