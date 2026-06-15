---
name: ismism-knowledge-operator
description: Operate the standalone ISMISM knowledge-processing repository. Use when Codex is working in or from `ismism-system` to answer ISMISM questions, inspect terms/positions/relations, extend the knowledge layer, validate outputs, design external references, or avoid legacy frontend/Atlas misuse while preserving row, segment, and quote traceability.
---

# ISMISM Knowledge Operator

## Core stance

Treat `ismism-system` as a corpus-backed theory-processing repo, not a normal wiki, frontend app, or generic philosophy encyclopedia. Preserve row / segment / quote traceability before interpretation.

## Read first

When starting in this repo, read only what the task needs, but use this order:

1. `AGENTS.md`
2. `README.md`
3. `DIRECTORY_MAP.md`
4. `ISMISM-MAINLINE-HANDOFF.md`
5. `knowledge/STATE.md`
6. `knowledge/usage-protocol.md` and `knowledge/query-playbook.md` for query tasks
7. `knowledge/export-manifest.md` for external-consumer tasks
8. `knowledge/w10-absorption/PLAN.md` and `knowledge/w10-absorption/index.md` for further-absorption tasks
9. `knowledge/themes/ai/README.md` and `knowledge/themes/ai/ai-synthesis.md` for AI / VR / 智能 / 算法 / 机器人 theme tasks
10. `knowledge/themes/chinese-philosophy/README.md` and `knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md` for Chinese Philosophy theme tasks
11. `knowledge/themes/religion/README.md` and `knowledge/themes/religion/religion-synthesis.md` for Religion Problem / 宗教问题 theme tasks

For matrix movement or relation interpretation, also read `knowledge/references/movement-patterns-guide.md`.

## Source priority

When sources disagree, prefer:

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

## Query workflows

### Term meaning or ambiguity

Use:

```text
term → knowledge/lexicon/term-senses.jsonl → sense_id → evidence_quotes
→ source_segments.clean_md_path → checked quote → optional synthesis
```

Optional helper:

```bash
python3 knowledge/scripts/query_term.py <term>
python3 knowledge/scripts/trace_evidence.py <sense_id>
```

Do not merge senses merely because they share one Chinese word. Cite the exact `sense_id` when making interpretive claims.

### Matrix position or doctrine location

Use:

```text
doctrine / coordinate → 目录索引_结构化.csv → knowledge/position-cards/{coordinate}.md
→ associated rows → W3 terms → W5 relations
```

Optional helper:

```bash
python3 knowledge/scripts/query_position.py <coordinate-or-title>
```

Treat coordinates as identifiers, not display-only labels.

### Relation, transition, movement, boundary, or misrecognition

Use:

```text
relation-assets.jsonl → relation_type / relation_id → source and target senses
→ source_position / target_position → evidence_segment → W6 audit if needed
```

Optional helper:

```bash
python3 knowledge/scripts/query_relation.py --type <relation_type>
python3 knowledge/scripts/trace_evidence.py <relation_id>
```

Use controlled relation types. Do not replace them with vague “related to” language.

### Overview or synthesis

Use W7 syntheses as maps after checking W3/W4/W5, unless the user explicitly asks for a field overview. Do not treat a synthesis as independent evidence.

### Further absorption / close reading

Use W10 cards when the task asks for argument structure, staged practice/process, or figure/school case positioning that is too detailed for W2 and not captured by W3/W5. Treat W10 as pilot-draft, verify `evidence_quotes` against `split_md_clean/`, preserve `[q1]` claim-to-quote mapping, and check `w3_w5_gap_review` before treating W10 as sufficient.

### AI theme questions

Use the AI theme maximum absorption layer for questions about AI, VR, artificial intelligence, intelligence, algorithms, robots, strong/weak AI, AI embodiment, AI mortality, or AI regeneration.

```bash
python3 knowledge/scripts/query_ai_theme.py AI身体化
python3 knowledge/scripts/query_ai_theme.py 强AI
python3 knowledge/scripts/query_ai_theme.py AI可朽性
python3 knowledge/scripts/query_ai_theme.py --row 360
```

The theme path is:

```text
knowledge/themes/ai/ai-row-manifest.jsonl
→ ai-evidence-bank.jsonl
→ AI W3 draft senses / AI W5 draft relations / W10 AI cards
→ split_md_clean exact quote
```

Do not treat `knowledge/themes/ai/` as a source above the corpus; it is a query and synthesis surface.

### Religion Problem theme questions

Use the Religion Problem maximum absorption layer for questions about 宗教问题, 宗教实在论, 神圣秩序, 神创, 神义, 偶像, 拜物, 时间崇拜, 灵魂, 唯灵论, 魔法, 弃绝, 反偶像, 信仰, 命定, 救世, 神智, 神爱, 宗教意识形态, or post-religious practice structures.

```bash
python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3
python3 knowledge/scripts/query_religion_theme.py 偶像 --limit 3
python3 knowledge/scripts/query_religion_theme.py --row 45
python3 knowledge/scripts/query_religion_theme.py --class buddhist-liberation-bridge
```

The theme path is:

```text
knowledge/themes/religion/religion-row-manifest.jsonl
→ religion-evidence-bank.jsonl
→ Religion W3 draft senses / Religion W5 draft relations / W10 Religion cards
→ split_md_clean exact quote
```

Do not treat `knowledge/themes/religion/` as an external religious-studies encyclopedia or a source above the corpus; it is a query and synthesis surface for how ISMISM absorbs religious realism, sacred order, faith/idol/spirit/fetishism, salvation, ideology, and practice transformation.

## Editing discipline

- Do not overwrite `split_md/`.
- Do not casually rewrite `split_md_clean/` unless text cleaning is the explicit task.
- Do not edit `MASTER-SPEC.md` or `Zhuyi_Matrix_Engine/` unless the user explicitly asks and the change is justified.
- Keep W3 term senses and W5 relations in `draft` unless an explicit promotion audit exists.
- Prefer small auditable batches in `knowledge/`.
- Keep every new interpretive claim traceable to row / segment / quote evidence.
- Update `knowledge/logs/operation-log.md` for substantial changes.
- Do not write outside this repository during normal ISMISM work.

## Legacy boundaries

Old frontend/product surfaces were removed. Do not restore `src/`, `dist/`, old `docs/00-*` through `docs/16-*`, or old cleanup handoff snapshots unless the user explicitly requests historical recovery.

Use `Zhuyi_Matrix_Engine/Atlas_DB/*` only as candidate generator, evidence bridge, summary seed, or unresolved backlog. Never treat Atlas as final truth.

## Validation

Before delivery after edits, run the narrowest relevant validators. For broad changes, run:

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

## Chinese Philosophy theme

For Chinese philosophy / 儒家 / 道家 / 佛教 / 禅 / 唯识 / 中观 / 毛哲学 queries, start at `knowledge/themes/chinese-philosophy/README.md`, then use the row manifest, evidence bank, W3/W5 draft batches, W10 cards, and theme validator. Do not treat the theme layer as a canonical replacement for corpus evidence.

## Religion Problem theme

For Religion Problem / 宗教问题 queries, start at `knowledge/themes/religion/README.md`, then use the row manifest, evidence bank, W3/W5 draft batches, W10 cards, and theme validator. Classify “神 / 精神 / 道 / 爱 / 宗教 / 意识形态” hits by corpus function rather than by keyword alone.
