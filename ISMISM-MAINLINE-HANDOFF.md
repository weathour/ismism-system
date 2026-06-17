# ISMISM Mainline Handoff

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.

Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.
W3 1676/1228; W5 validator uses `--min-count 1044`.

## Current state

- W1 corpus manifests: 363 rows available; row 176 clean text redone and available.
- W2 segment cards: 363 draft cards.
- W3 term senses: 1676 draft senses / 1228 terms.
- W4 position cards: 4 / 16 / 64 / 172 by level; 256 total draft cards.
- W5 relation assets: 1044 draft relations / 12 relation types.
- W10 close-reading layer: 741 pilot-draft cards / 3 card types.
- Absorption: 6/363 rows remain W1/W2-only; 277 rows now have W3+W5+W10 overlap.

## Active theme layers

- Capitalism / Political Economy maximum absorption — `knowledge/themes/capitalism/capitalism-row-manifest.jsonl`.
- Time-Death-Finitude-Life maximum absorption — 85-row theme layer.
- Feminism / Gender / Sexuality / Social Reproduction maximum absorption — `knowledge/themes/feminism/feminism-row-manifest.jsonl`.
- Psychoanalysis / Subjectivity / Desire / Discourse / Language maximum absorption — `knowledge/themes/psychoanalysis-subjectivity/psychoanalysis-subjectivity-row-manifest.jsonl`.
- Aesthetics / Art / Media / Image / Narrative maximum absorption — `knowledge/themes/aesthetics-media/aesthetics-media-row-manifest.jsonl`.
- Labor / Workplace / Precarity / Involution maximum absorption.
- Education / Examination / Credentialism / Knowledge Discipline maximum absorption.
- Family / Intimacy / Marriage / Birth / Social Reproduction maximum absorption.
- Consumption / Desire / Commodity / Lifestyle maximum absorption.
- Media / Platform / Public Opinion / Traffic Society maximum absorption.
- Governance / Law / Bureaucracy / Order maximum absorption.
- Class / Youth / Generation / Mobility Anxiety maximum absorption.
- Psychological Distress / Anxiety / Addiction / Social Symptom maximum absorption.
- Urban / Housing / Migration / Space maximum absorption.
- Health / Body / Medicine / Risk Society maximum absorption.

## Resume protocol

1. Read `PROJECT-SPEC.md`, `README.md`, `knowledge/STATE.md`, and this file.
2. For a theme task, read that theme `README.md`, row manifest, evidence bank, validator, and query helper.
3. Preserve row/segment/quote traceability.
4. Run the smallest relevant validator first, then the aggregate validators before claiming completion.

## Standard validation set

```bash
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
