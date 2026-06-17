# ISMISM Digestion Program

The digestion program turns the corpus into auditable knowledge layers. It is not a product roadmap and has no external repository dependency.

## Objective

Build a stable, queryable, and traceable ISMISM knowledge layer over 363 corpus rows:

1. W1 corpus manifests and retrieval chunks.
2. W2 segment cards.
3. W3 draft term senses.
4. W4 draft position cards.
5. W5 draft relation assets.
6. QA/audit surfaces.
7. Syntheses and usage protocols.
8. W10 pilot-draft close-reading cards.
9. Theme maximum-absorption layers.

## Current checkpoint

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Working method

- Start from the row manifest and clean text.
- Add knowledge in small batches.
- Store exact quotes in evidence banks when a theme layer needs them.
- Keep W3/W5/W10 status conservative: draft or pilot-draft.
- Update current docs only when a new layer changes navigation, counts, or validation commands.
- Run targeted validators first, then the aggregate contract validator.

## Validation

```bash
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
