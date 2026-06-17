# Directory Map

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Root

| Path | Function |
| --- | --- |
| `PROJECT-SPEC.md` | Current project contract and validation gates. |
| `README.md` | Public orientation and quick validation commands. |
| `AGENTS.md` | Agent operating rules for this repository. |
| `ISMISM-MAINLINE-HANDOFF.md` | Current resume surface. |
| `目录索引_结构化.csv` / `.md` | Structured TOC and row registry. |
| `split_md/` | Raw Markdown slices. |
| `split_md_clean/` | Cleaned Markdown slices. |
| `knowledge/` | Active knowledge-processing layer. |
| `skills/ismism-knowledge-operator/SKILL.md` | Repo-local operator protocol. |

## Knowledge layer

| Path | Function |
| --- | --- |
| `knowledge/manifests/` | W1 corpus manifest, segments, chunks, missing/anomaly report. |
| `knowledge/segment-cards/` | W2 row-level draft segment cards. |
| `knowledge/lexicon/` | W3 draft term senses and term indexes. |
| `knowledge/position-cards/` | W4 matrix position cards. |
| `knowledge/relations/` | W5 relation assets and relation prompts. |
| `knowledge/qa/` | Current audit, validation, and review evidence. |
| `knowledge/syntheses/` | Cross-row and cross-theme synthesis outputs. |
| `knowledge/w10-absorption/` | Pilot-draft argument/process/case close-reading cards. |
| `knowledge/themes/` | Maximum-absorption theme layers. |
| `knowledge/scripts/` | Build, query, and validation scripts. |
| `knowledge/references/` | Stable protocols and method references. |
| `knowledge/templates/` | Generation templates. |

## Theme validation and query helpers

- `knowledge/themes/aesthetics-media/` — Aesthetics / Art / Media / Image / Narrative; `validate_aesthetics_media_theme.py`; `query_aesthetics_media_theme.py`.
- `knowledge/themes/ai/` — AI; `validate_ai_theme.py`; `query_ai_theme.py`.
- `knowledge/themes/capitalism/` — Capitalism / Political Economy; `validate_capitalism_theme.py`; `query_capitalism_theme.py`.
- `knowledge/themes/chinese-philosophy/` — Chinese Philosophy; `validate_chinese_philosophy_theme.py`; `query_chinese_philosophy_theme.py`.
- `knowledge/themes/class-youth-generational-anxiety/` — Class / Youth / Generation / Mobility Anxiety; `validate_class_youth_generational_anxiety_theme.py`; `query_class_youth_generational_anxiety_theme.py`.
- `knowledge/themes/consumption-desire-lifestyle/` — Consumption / Desire / Commodity / Lifestyle; `validate_consumption_desire_lifestyle_theme.py`; `query_consumption_desire_lifestyle_theme.py`.
- `knowledge/themes/education-examination-credentialism/` — Education / Examination / Credentialism; `validate_education_examination_credentialism_theme.py`; `query_education_examination_credentialism_theme.py`.
- `knowledge/themes/family-intimacy-reproduction/` — Family / Intimacy / Marriage / Birth; `validate_family_intimacy_reproduction_theme.py`; `query_family_intimacy_reproduction_theme.py`.
- `knowledge/themes/feminism/` — Feminism / Gender / Sexuality / Social Reproduction; `validate_feminism_theme.py`; `query_feminism_theme.py`.
- `knowledge/themes/governance-law-bureaucracy/` — Governance / Law / Bureaucracy / Order; `validate_governance_law_bureaucracy_theme.py`; `query_governance_law_bureaucracy_theme.py`.
- `knowledge/themes/health-body-risk-society/` — Health / Body / Medicine / Risk Society; `validate_health_body_risk_society_theme.py`; `query_health_body_risk_society_theme.py`.
- `knowledge/themes/labor-workplace-precarity/` — Labor / Workplace / Precarity; `validate_labor_workplace_precarity_theme.py`; `query_labor_workplace_precarity_theme.py`.
- `knowledge/themes/media-platform-public-opinion/` — Media / Platform / Public Opinion / Traffic Society; `validate_media_platform_public_opinion_theme.py`; `query_media_platform_public_opinion_theme.py`.
- `knowledge/themes/psychoanalysis-subjectivity/` — Psychoanalysis / Subjectivity / Desire / Discourse / Language; `validate_psychoanalysis_subjectivity_theme.py`; `query_psychoanalysis_subjectivity_theme.py`.
- `knowledge/themes/psychological-distress-social-symptom/` — Psychological Distress / Anxiety / Addiction / Social Symptom; `validate_psychological_distress_social_symptom_theme.py`; `query_psychological_distress_social_symptom_theme.py`.
- `knowledge/themes/religion/` — Religion Problem; `validate_religion_theme.py`; `query_religion_theme.py`.
- `knowledge/themes/time-death-finitude-life/` — Time-Death-Finitude-Life; `validate_time_death_theme.py`; `query_time_death_theme.py`.
- `knowledge/themes/urban-housing-migration-space/` — Urban / Housing / Migration / Space; `validate_urban_housing_migration_space_theme.py`; `query_urban_housing_migration_space_theme.py`.

## Core validators

```bash
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
