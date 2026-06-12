# W8 Usage Protocol — ISMISM Knowledge Layer

- status: draft protocol
- created: 2026-06-09 CST
- scope: how an agent or scholar should choose between term senses, position cards, relation assets, syntheses, and corpus evidence.

## 1. Source order

Use this order when a question touches interpretation:

1. `目录索引_结构化.csv` for row / TOC identity.
2. `split_md_clean/` for exact wording.
3. `knowledge/manifests/segments.jsonl` for row metadata and file paths.
4. `knowledge/segment-cards/` for row-level evidence cards.
5. `knowledge/lexicon/term-senses.jsonl` for W3 sense selection.
6. `knowledge/position-cards/` for W4 coordinate interpretation.
7. `knowledge/relations/relation-assets.jsonl` for W5 movement / boundary / mediation / tension.
8. `knowledge/qa/*` for W6 audit state.
9. `knowledge/syntheses/*` for W7 cross-layer summaries.

Atlas and legacy frontend docs are not truth layers.

## 2. When to query W3 term senses

Use W3 first when the question asks what a term means, or when a high-risk term appears: `主体`, `客体`, `实践`, `历史`, `理论`, `现实`, `星丛`, `Event`, `site`, `通俗化`, `回溯`.

Required path:

```text
term → matching sense_id → evidence_quotes → source_segments.clean_md_path → optional synthesis
```

Do not merge senses just because they share a Chinese word.

## 3. When to query W4 position cards

Use W4 first when the question asks where a doctrine, field, route, or coordinate sits in the matrix.

Required path:

```text
coordinate → position card → associated row(s) → W3 terms → W5 relations
```

For field-level questions, start with `1.md`, `2.md`, `3.md`, or `4.md`, then descend to L2/L3/L4.

## 4. When to query W5 relation assets

Use W5 first when the question asks how one term, position, or mechanism moves into another.

Controlled relation types:

```text
boundary-between, route-from-to, tension-between, mediates-between,
transitions-to, blocks-transition, misrecognizes-as, objectifies,
subjectivizes, overcodes, represents-position, evidences-claim
```

Required path:

```text
relation_type → relation_id → source/target senses → source/target positions → evidence_segment
```

Do not replace controlled relation types with vague “related to” language.

## 5. When to use W7 syntheses

Use syntheses after W3/W4/W5 lookup, not before it, unless the user asks for a field overview.

Recommended entry points:

- field 1 overview: `knowledge/syntheses/part-1-realism.md`
- field 2 overview: `knowledge/syntheses/part-2-metaphysics.md`
- field 3 overview: `knowledge/syntheses/part-3-idealism.md`
- field 4 overview: `knowledge/syntheses/part-4-praxis.md`
- cross-field movement: `knowledge/syntheses/whole-system-map.md`
- usage method: `knowledge/syntheses/methodological-core.md`

Each synthesis claim is a pointer back to row / term / position / relation evidence.

## 6. Answer discipline

When answering from this repo:

1. State which layer was consulted.
2. Quote or paraphrase only from checked source rows.
3. Include row IDs and sense IDs for interpretive claims.
4. Keep W3/W5 status as draft unless a future promotion audit says otherwise.
5. Distinguish evidence from inference.
6. State uncertainty when a term or relation is not yet represented.

## 7. Write discipline

When adding new material:

1. Do not write outside this repository.
2. Do not overwrite `split_md/`.
3. Do not rewrite `split_md_clean/` unless text cleaning is the explicit task.
4. Do not edit `MASTER-SPEC.md` or `Zhuyi_Matrix_Engine/`.
5. Keep row / segment / quote traceability.
6. Keep W3/W5 `draft` unless an explicit promotion audit exists.
