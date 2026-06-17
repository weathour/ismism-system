# Relation Curation Guide

This guide defines how relation records are added to the ISMISM Library. It is a product-facing protocol, not a workflow transcript.

## Relation record purpose

Relation records connect two concept or position handles through an evidence-backed relation type. They should preserve the local row boundary and should not turn a suggestive passage into a universal rule.

## Required checks

1. Identify the source and target handles.
2. Select a controlled relation type from `library/relations/relation-types.md`.
3. Attach exact row evidence from `corpus/clean-markdown/`.
4. Write an applicability boundary and a forbidden interpretation.
5. Keep the record in `draft` unless an explicit review promotes it.
6. Run `python3 tools/validate/relations.py --repo . --min-count 1044 --require-type-min 2`.

## Curation sequence

- Start from an evidence row, not from an abstract thesis.
- Prefer an existing relation type before adding vocabulary.
- If the quote can support multiple relation types, create the narrowest defensible relation and record the ambiguity in the boundary.
- Re-run `python3 tools/ismism.py validate core` before relying on the new relation in synthesis or theme docs.
