# Current Known Corpus State

current_phase: Health / Body / Medicine / Risk Society maximum absorption
updated: 2026-06-17

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Current global counts are 1676 W3 senses / 1228 terms; 6/363 rows remain W1/W2-only; 277 rows now have W3+W5+W10 overlap.
99.9% clean-text volume has W3/W5/W10 absorption coverage.

Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Corpus and manifest state

- `segments.jsonl`: 363 records.
- `chunks.jsonl`: 1594 records.
- `split_md/`: 363 Markdown source slices.
- `split_md_clean/`: 363 clean Markdown source slices.
- row 176 clean text redone and available at `split_md_clean/2_形而上学_古代贵族的精神冒险_背景性的符号秩序与它自己的对立_比下_形而下学_有余_比上_观/0176_2-4-2-4_场域化存在主义4海德格尔2.md`.
- `split_pdf/` is not required for current validation; PDF slices remain regenerable if explicitly needed.

## Knowledge-layer counts

| Layer | Current state |
| --- | --- |
| W1 corpus manifests | 363/363 rows available |
| W2 segment cards | 363 draft segment cards |
| W3 term senses | 1676 draft senses / 1228 terms |
| W4 position cards | 4 / 16 / 64 / 172 by level; 256 total |
| W5 relation assets | 1044 draft relations / 12 relation types |
| W10 close reading | 741 pilot-draft cards / 3 card types |
| Absorption overlap | 6/363 rows remain W1/W2-only; 277 rows have W3+W5+W10 overlap |

## Active themes and validators

- AI — `validate_ai_theme.py`; `query_ai_theme.py`.
- Chinese Philosophy — `validate_chinese_philosophy_theme.py`; `query_chinese_philosophy_theme.py`.
- Religion Problem — `validate_religion_theme.py`; `query_religion_theme.py`.
- Time-Death-Finitude-Life maximum absorption — `validate_time_death_theme.py`; `query_time_death_theme.py`.
- Capitalism / Political Economy maximum absorption — `validate_capitalism_theme.py`; `query_capitalism_theme.py`.
- Feminism / Gender / Sexuality — `validate_feminism_theme.py`; `query_feminism_theme.py`.
- Psychoanalysis / Subjectivity / Desire / Discourse / Language maximum absorption — `validate_psychoanalysis_subjectivity_theme.py`; `query_psychoanalysis_subjectivity_theme.py`.
- Aesthetics / Art / Media / Image / Narrative — `validate_aesthetics_media_theme.py`; `query_aesthetics_media_theme.py`.
- Labor / Workplace / Precarity / Involution.
- Education / Examination / Credentialism / Knowledge Discipline.
- Family / Intimacy / Marriage / Birth / Social Reproduction.
- Consumption / Desire / Commodity / Lifestyle.
- Media / Platform / Public Opinion / Traffic Society.
- Governance / Law / Bureaucracy / Order.
- Class / Youth / Generation / Mobility Anxiety.
- Psychological Distress / Anxiety / Addiction / Social Symptom.
- Urban / Housing / Migration / Space.
- Health / Body / Medicine / Risk Society.

## Resume rule

Read `PROJECT-SPEC.md`, `README.md`, `ISMISM-MAINLINE-HANDOFF.md`, `DIRECTORY_MAP.md`, and the relevant theme README before editing. Keep every new claim tied to row, segment, clean path, or exact quote evidence.

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
