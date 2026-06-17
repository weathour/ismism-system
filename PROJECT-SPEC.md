# ISMISM Project Spec

ISMISM is a corpus-grounded knowledge-processing project for 未明子《主义主义》. The repository is organized as a standalone, GitHub-ready knowledge layer: corpus registry, cleaned text, segment cards, term senses, position cards, relation assets, close-reading absorption cards, theme layers, syntheses, query helpers, and validators.

## Source-of-truth order

1. `目录索引_结构化.csv`
2. `split_md/`
3. `split_md_clean/`
4. `knowledge/manifests/*`
5. `knowledge/segment-cards/*`
6. `knowledge/lexicon/*`
7. `knowledge/position-cards/*`
8. `knowledge/relations/*`
9. `knowledge/w10-absorption/*`
10. `knowledge/themes/*`
11. `knowledge/syntheses/*`
12. `knowledge/qa/*`

## Non-negotiable boundaries

- Do not overwrite `split_md/`.
- Do not rewrite `split_md_clean/` unless the task explicitly targets text cleaning.
- Keep W3 term senses and W5 relation assets in `draft` unless a separate review process promotes them.
- Keep W10 cards in `pilot-draft`.
- Every substantive claim must remain traceable to row, segment, clean-text path, or exact quote evidence.
- No external-repository dependency is required for validation.

## Current validation marker

Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Current global counts are 1676 W3 senses / 1228 terms; 6/363 rows remain W1/W2-only; 277 rows now have W3+W5+W10 overlap.

## Core validation commands

```bash
python3 knowledge/scripts/build_w1_manifests.py
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
