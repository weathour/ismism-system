# ISMISM Repository Directory Map

- updated: 2026-06-14 CST
- scope: concise map of the current repository structure and functional layers
- status: navigation aid; not a replacement for `AGENTS.md`, `ISMISM-MAINLINE-HANDOFF.md`, or `knowledge/STATE.md`

## One-line identity

`ismism-system` is a standalone ISMISM knowledge-processing repo: corpus evidence is preserved, interpretation is layered, and every serious claim should trace back to row / segment / quote evidence.

## Functional structure

```text
Root evidence + handoff docs
├── corpus evidence layer: PDF / TOC / split_md / split_md_clean
├── active knowledge layer: knowledge/
│   ├── W1 manifests
│   ├── W2 segment cards
│   ├── W3 term senses
│   ├── W4 position cards
│   ├── W5 relation assets
│   ├── W6 QA / audit
│   ├── W7 syntheses
│   ├── W8 usage / query / export protocol
│   └── W9 repo-local integration package
├── legacy candidate layer: Zhuyi_Matrix_Engine/
├── removed-route tombstone: docs/archive/
└── recovery scripts: root PDF/TOC/split utilities + knowledge/scripts validators
```

## Top-level paths

| Path | Current role | Use as truth? | Notes |
|---|---|---:|---|
| `README.md` | Human/agent entry summary | yes, for orientation | Start here for a quick status check. |
| `AGENTS.md` | Agent behavior and source-priority rules | yes, for procedure | Highest practical instruction surface in the repo. |
| `ISMISM-MAINLINE-HANDOFF.md` | Current mainline handoff | yes, for project state | Use with `knowledge/STATE.md`. |
| `MASTER-SPEC.md` | Original completion contract / hard metrics | contract, but some snapshots are historical | Do not treat old progress counts as current state. |
| `目录索引_结构化.csv` | TOC / row identity source | yes, canonical structure | First source when row identity conflicts. |
| `主义主义 (...).pdf` | Original PDF | yes, original source | Final fallback evidence. |
| `split_md/` | Raw split text | yes, corpus evidence | Do not overwrite. |
| `split_md_clean/` | Lightly cleaned split text | yes, checked wording | Do not casually rewrite. |
| `split_pdf/` | Regenerable PDF slice layer | no, derived | Currently only partial/recovery-oriented. |
| `knowledge/` | Active processing and knowledge layer | yes, after evidence layer | Main working layer. |
| `Zhuyi_Matrix_Engine/` | Legacy method / Atlas candidate layer | no, candidate only | Useful for seeds, not for final truth. |
| `docs/archive/` | Tombstone for removed routes | no, historical boundary | Prevents old frontend/product revival. |
| root `*.py` scripts | Recovery / regeneration utilities | procedural only | Do not run casually on corpus sources. |
| `skills/` | Repo-local skill drafts | procedural only | Not automatically installed outside this repo. |

## `knowledge/` map

| Path | Layer | Function |
|---|---|---|
| `knowledge/README.md` | overview | Knowledge-layer entry. |
| `knowledge/STATE.md` | state | Resume surface and current decisions. |
| `knowledge/DIGESTION_PROGRAM.md` | program | Historical/strategic phase plan. |
| `knowledge/manifests/` | W1 | Corpus manifest, segments registry, chunks registry, anomaly records. |
| `knowledge/segment-cards/` | W2 | 363 row-level evidence cards. |
| `knowledge/lexicon/` | W3 | Term senses, ambiguity controls, candidate statistics. |
| `knowledge/position-cards/` | W4 | 256 matrix position cards. |
| `knowledge/relations/` | W5 | Draft relation assets and relation-family cards. |
| `knowledge/qa/` | W6 | Validation, drift, evidence-claim, rejected-interpretation audits. |
| `knowledge/syntheses/` | W7 | Field and whole-system syntheses; maps, not independent evidence. |
| `knowledge/usage-protocol.md` | W8 | How to use layers safely. |
| `knowledge/query-playbook.md` | W8 | Standard query paths. |
| `knowledge/export-manifest.md` | W8 | File-level export contract. |
| `knowledge/integration/` | W9 | Repo-local external reference package and status records. |
| `knowledge/scripts/` | validation/build tools | Validators and deterministic builders. |
| `knowledge/references/` | method reference | Movement taxonomy and reading protocols. |
| `knowledge/logs/` | operation log | Chronological processing record. |
| `knowledge/prompts/` | resume prompts | Historical prompt handoffs. |
| `knowledge/templates/` | templates | Reusable knowledge-layer templates. |

## Truth-source order

When files disagree, prefer:

1. `目录索引_结构化.csv`
2. `split_md/` and `split_md_clean/`
3. `knowledge/manifests/*`
4. `knowledge/segment-cards/*`
5. `knowledge/lexicon/*`
6. `knowledge/position-cards/*`
7. `knowledge/relations/*`
8. `knowledge/qa/*`
9. `knowledge/syntheses/*`
10. `Zhuyi_Matrix_Engine/Phase*` as method hints only
11. `Zhuyi_Matrix_Engine/Atlas_DB/*` as candidate data only
12. `docs/archive/*` as historical/tombstone data only

## Standard use paths

### Term question

```text
term → knowledge/lexicon/term-senses.jsonl → evidence_quotes
→ source_segments.clean_md_path → optional W7 synthesis
```

Optional CLI:

```bash
python3 knowledge/scripts/query_term.py 主体
python3 knowledge/scripts/query_term.py --sense-id term:主体:s01
python3 knowledge/scripts/query_term.py --row 276
```

### Position question

```text
coordinate or doctrine → 目录索引_结构化.csv
→ knowledge/position-cards/{coordinate}.md
→ related rows / W3 terms / W5 relations
```

Optional CLI:

```bash
python3 knowledge/scripts/query_position.py 3-4-2
python3 knowledge/scripts/query_position.py 后结构主义
```

### Relation or movement question

```text
relation type or mechanism → knowledge/relations/relation-assets.jsonl
→ source/target senses and positions → evidence_segment → W6 audit if strength is unclear
```

Optional CLI:

```bash
python3 knowledge/scripts/query_relation.py --type objectifies
python3 knowledge/scripts/query_relation.py --relation-id rel:w5b1:001
python3 knowledge/scripts/query_relation.py --row 276
```

### Overview question

```text
knowledge/syntheses/*.md → source tags → W3/W4/W5 records → checked row evidence
```

Optional evidence trace:

```bash
python3 knowledge/scripts/trace_evidence.py term:主体:s01
python3 knowledge/scripts/trace_evidence.py rel:w5b1:001
python3 knowledge/scripts/trace_evidence.py 276
```

## Lightweight query scripts

These scripts are read-only helpers over current file contracts. They do not replace validators or the source-priority rules.

| Script | Purpose |
|---|---|
| `knowledge/scripts/query_term.py` | Search W3 term-sense records by term, sense ID, or row. |
| `knowledge/scripts/query_position.py` | Search W4 position cards by coordinate or title text. |
| `knowledge/scripts/query_relation.py` | Search W5 relation assets by relation type, relation ID, endpoint, or evidence row. |
| `knowledge/scripts/trace_evidence.py` | Trace a term sense, relation, or row back to clean segment text and quote-substring checks. |
| `knowledge/scripts/ismism_query_lib.py` | Shared read-only helper library for the query scripts. |

### Editing or extending knowledge

```text
read handoff/state → edit smallest relevant knowledge layer batch
→ keep row/segment/quote traceability → run validators → log the operation
```

## Validation commands

Run before delivery or after substantial edits:

```bash
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
```

## Non-mainline boundaries

- Do not restore the deleted frontend/product route unless explicitly asked for historical recovery.
- Do not treat `Zhuyi_Matrix_Engine/Atlas_DB/*` as canonical truth.
- Do not promote W3 term senses or W5 relations out of `draft` without an explicit review/promotion step.
- Do not process RMH/GJW here.
- Do not use the matrix as a direct personality diagnosis table.
