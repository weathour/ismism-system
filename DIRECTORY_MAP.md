# ISMISM Repository Directory Map

- updated: 2026-06-15 CST
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
│   ├── W9 repo-local integration package
│   ├── W10 further absorption pilot
│   └── theme layers, including AI and Chinese Philosophy maximum absorption
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
| `knowledge/qa/` | W6/W10 | Validation, drift, evidence-claim, rejected-interpretation audits, W10 audit, and absorption-strength snapshot. |
| `knowledge/syntheses/` | W7 | Field and whole-system syntheses; maps, not independent evidence. |
| `knowledge/usage-protocol.md` | W8 | How to use layers safely. |
| `knowledge/query-playbook.md` | W8 | Standard query paths. |
| `knowledge/export-manifest.md` | W8 | File-level export contract. |
| `knowledge/integration/` | W9 | Repo-local external reference package and status records. |
| `knowledge/w10-absorption/` | W10 | Pilot-draft close-reading layer for argument, process, and case cards. |
| `knowledge/themes/ai/` | theme layer | AI / VR / 智能 / 算法 / 机器人 maximum absorption manifest, quote bank, taxonomy, synthesis, and usage protocol. |
| `knowledge/themes/chinese-philosophy/` | theme layer | Chinese Philosophy / 儒家 / 道家 / 佛教 / 禅 / 唯识 / 中观 / 毛哲学 maximum absorption manifest, quote bank, taxonomy, syntheses, and usage protocol. |
| `knowledge/themes/religion/` | theme layer | Religion Problem / 宗教问题 maximum absorption manifest, exact quote bank, taxonomy, syntheses, W3/W5 notes, and usage protocol. |
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
10. `knowledge/w10-absorption/*` as pilot-draft close-reading aids
11. `Zhuyi_Matrix_Engine/Phase*` as method hints only
12. `Zhuyi_Matrix_Engine/Atlas_DB/*` as candidate data only
13. `docs/archive/*` as historical/tombstone data only

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

### Religion Problem maximum absorption

```text
Religion Problem / 宗教问题 / 宗教实在论 / 偶像 / 拜物 / 神爱 / 解脱 question
→ knowledge/themes/religion/README.md
→ religion-row-manifest.jsonl + religion-evidence-bank.jsonl
→ Religion W3/W5 draft batches + W10 Religion cards
→ knowledge/qa/religion-absorption-audit.md / religion-evidence-claim-audit.md / religion-ultraqa-report.md
```

Optional CLI:

```bash
python3 knowledge/scripts/validate_religion_theme.py --repo . --final
python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3
```

### AI theme maximum absorption

```text
AI / VR / 智能 / 算法 / 机器人 question
→ knowledge/themes/ai/README.md
→ knowledge/themes/ai/ai-row-manifest.jsonl + ai-evidence-bank.jsonl
→ W3/W5 draft batches + W10 pilot cards
→ knowledge/qa/ai-theme-absorption-audit.md / ai-theme-evidence-claim-audit.md / ai-theme-ultraqa-report.md
```

Optional CLI:

```bash
python3 knowledge/scripts/validate_ai_theme.py --repo . --final
python3 knowledge/scripts/query_ai_theme.py AI可朽性 --limit 3
```

## Lightweight query scripts

These scripts are read-only helpers over current file contracts. They do not replace validators or the source-priority rules.

| Script | Purpose |
|---|---|
| `knowledge/scripts/query_term.py` | Search W3 term-sense records by term, sense ID, or row. |
| `knowledge/scripts/query_position.py` | Search W4 position cards by coordinate or title text. |
| `knowledge/scripts/query_relation.py` | Search W5 relation assets by relation type, relation ID, endpoint, or evidence row. |
| `knowledge/scripts/trace_evidence.py` | Trace a term sense, relation, or row back to clean segment text and quote-substring checks. |
| `knowledge/scripts/validate_w10_absorption.py` | Validate W10 card metadata, index coverage, and quote-substring traceability. |
| `knowledge/scripts/validate_ai_theme.py` | Validate AI theme manifest/evidence/synthesis and final W3/W5/W10 coverage gates. |
| `knowledge/scripts/validate_chinese_philosophy_theme.py` | Validate Chinese Philosophy manifest/evidence/taxonomy/synthesis and W3/W5/W10 coverage gates. |
| `knowledge/scripts/query_ai_theme.py` | Query AI theme rows and quotes by row, class, or common labels such as `AI身体化`, `强AI`, `AI可朽性`. |
| `knowledge/scripts/query_chinese_philosophy_theme.py` | Query Chinese Philosophy rows and quotes by row, class, or keywords such as `实践论`, `庄子`, `中观`. |
| `knowledge/scripts/validate_religion_theme.py` | Validate Religion Problem manifest/evidence/taxonomy/synthesis and W3/W5/W10 coverage gates. |
| `knowledge/scripts/query_religion_theme.py` | Query Religion Problem rows and quotes by row, class, or keywords such as `宗教`, `偶像`, `神爱`, `涅槃`. |
| `knowledge/scripts/ismism_query_lib.py` | Shared read-only helper library for the query scripts. |

### Editing or extending knowledge

```text
read handoff/state → edit smallest relevant knowledge layer batch
→ keep row/segment/quote traceability → run validators → log the operation
```

## Validation commands

Run before delivery or after substantial edits:

```bash
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_ai_theme.py --repo . --final
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/validate_religion_theme.py --repo . --final
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 191 --require-type-min 2
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

### Chinese philosophy maximum absorption

```text
Chinese philosophy / 儒家 / 道家 / 佛教 / 禅 / 唯识 / 中观 / 毛哲学 question
→ knowledge/themes/chinese-philosophy/README.md
→ chinese-philosophy-row-manifest.jsonl + chinese-philosophy-evidence-bank.jsonl
→ W3/W5 draft batches + W10 pilot cards
→ knowledge/qa/chinese-philosophy-absorption-audit.md / evidence-claim audit / ultraqa report
```

Optional CLI:

```bash
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3
```
