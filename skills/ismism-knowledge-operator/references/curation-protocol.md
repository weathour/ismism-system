# Curation Protocol

Use this when editing curated ISMISM assets. Prefer small, auditable batches.

## Cross-repository curation boundary

When the skill is invoked from another repository, use ISMISM as a read-only library by default. Do not edit the user's current repository or the installed plugin copy unless the user explicitly requests that target.

If the user asks to curate ISMISM itself, resolve the library root first:

```bash
ISMISM_ROOT=$(python3 <this-skill-dir>/scripts/ismism.py root)
```

Then edit files under `$ISMISM_ROOT`, not under the unrelated current repository. If the installed plugin is a cached copy and the user expects source-repo changes, use `ISMISM_LIBRARY_ROOT=/path/to/source/ismism-system` to target the maintained source checkout.

## Universal edit workflow

1. Identify the target layer: manifests, segments, concepts, positions, relations, close-reading, themes, syntheses, docs, tools, or plugin metadata.
2. Read existing nearby records and templates before editing.
3. Preserve row id, segment id, clean path, and exact quote anchors.
4. Reuse existing identifiers and naming patterns; do not invent a parallel taxonomy.
5. Run targeted validators from `references/validation-matrix.md`.
6. Report changed files, pattern followed, validators, and remaining risks.

## Concept senses

Primary file: `library/concepts/term-senses.jsonl`.

Before adding or changing a sense:

- query the term first;
- inspect adjacent senses for `sense_id`, `sense_label`, `definition`, `forbidden_mix`, `source_segments`, and evidence quote shape;
- verify every quote appears in the cited clean transcript or already-validated source record;
- keep `status` conservative unless an explicit review step promotes it.

Run:

```bash
python3 tools/validate/concepts.py --repo .
python3 tools/validate/library_contract.py --repo . --residue-only
```

## Relation records

Primary file: `library/relations/relation-assets.jsonl`; template: `library/templates/relation-asset-template.md`.

Before editing:

- confirm allowed relation type from existing records or template;
- ensure source and target IDs exist or are intentionally provisional;
- include applicability boundary and forbidden interpretation;
- keep relation claims narrower than their evidence.

Run:

```bash
python3 tools/validate/relations.py --repo . --min-count 1044 --require-type-min 2
python3 tools/validate/library_contract.py --repo . --residue-only
```

## Close-reading cards

Primary directories: `library/close-reading/arguments/`, `processes/`, `cases/`; templates: `library/templates/close-reading-*-template.md`.

Before editing:

- choose one card type: argument, process, or case;
- keep `row_id`, `segment_id`, `toc_id`, `source_clean_path`, and `evidence_quotes` exact;
- map body claims to quote markers;
- keep card use boundary explicit.

Run:

```bash
python3 tools/validate/close_reading.py --repo .
python3 tools/validate/library_contract.py --repo . --residue-only
```

## Theme dossiers

Primary directories: `library/themes/<theme>/` plus theme validators under `tools/validate/themes/`.

For a new major theme package or a boundary-changing theme extension, read `references/theme-absorption-protocol.md` first.

Before editing:

- inspect the theme README, row manifest, evidence bank, and synthesis files;
- keep quote evidence exact and row-scoped;
- do not move a theme boundary without updating the theme validator and documentation;
- prefer adding evidence rows over broad unsourced synthesis.

Run the specific theme validator, then core residue validation. If the change affects social-topic routing, run social validation too.

## Syntheses and protocols

Synthesis files should summarize validated assets; they should not become a hidden source layer.

Before editing:

- cite the library assets being synthesized;
- keep uncertainty and boundary notes;
- avoid adding claims that cannot be traced back to rows, records, cards, or theme evidence.

Run product residue validation and any targeted validator for the referenced asset layer.

## Source correction

Only edit transcript files when the task explicitly requests source correction.

Before editing source text:

1. inspect `library/manifests/content-integrity.json`;
2. document why source correction is necessary;
3. update integrity records if bytes intentionally change;
4. run byte and core validation.

Do not silently normalize source text during ordinary curation.
