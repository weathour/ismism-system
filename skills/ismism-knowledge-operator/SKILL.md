---
name: ismism-knowledge-operator
description: Operate the standalone ISMISM knowledge-processing repository; answer corpus-grounded questions, inspect terms/positions/relations, extend the knowledge layer, and validate outputs while preserving row, segment, clean-path, and quote traceability.
---

# ISMISM Knowledge Operator

Use this skill when working inside `ismism-system` on corpus retrieval, theme analysis, knowledge-layer extension, validation, or project publication hygiene.

## Current markers

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Read order

1. `PROJECT-SPEC.md`
2. `README.md`
3. `knowledge/STATE.md`
4. `ISMISM-MAINLINE-HANDOFF.md`
5. `DIRECTORY_MAP.md`
6. Relevant `knowledge/themes/<theme>/README.md`
7. Relevant validator/query helper
8. Relevant manifest/evidence bank/clean text

## Truth-source order

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

## Query helpers

- Social superphase: `python3 knowledge/scripts/query_social_phenomena_superphase.py 内卷 --limit 3`
- AI: `python3 knowledge/scripts/query_ai_theme.py AI --limit 3`
- Chinese Philosophy: `python3 knowledge/scripts/query_chinese_philosophy_theme.py 儒家 --limit 3`
- Religion: `python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3`
- Time-Death-Finitude-Life theme questions: `python3 knowledge/scripts/query_time_death_theme.py 时间 --limit 3`
- Capitalism: `python3 knowledge/scripts/query_capitalism_theme.py 资本主义 --limit 3`
- Feminism: `python3 knowledge/scripts/query_feminism_theme.py 女权 --limit 3`
- Psychoanalysis: `python3 knowledge/scripts/query_psychoanalysis_subjectivity_theme.py 精神分析 --limit 3`
- Aesthetics: `python3 knowledge/scripts/query_aesthetics_media_theme.py 电影 --limit 3`
- Labor / Workplace / Precarity / Involution: `python3 knowledge/scripts/query_labor_workplace_precarity_theme.py 内卷 --limit 3`
- Education: `python3 knowledge/scripts/query_education_examination_credentialism_theme.py 考试 --limit 3`
- Family: `python3 knowledge/scripts/query_family_intimacy_reproduction_theme.py 家庭 --limit 3`
- Consumption: `python3 knowledge/scripts/query_consumption_desire_lifestyle_theme.py 消费主义 --limit 3`
- Media: `python3 knowledge/scripts/query_media_platform_public_opinion_theme.py 平台 --limit 3`
- Governance: `python3 knowledge/scripts/query_governance_law_bureaucracy_theme.py 治理 --limit 3`
- Class / Youth: `python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 阶层 --limit 3`
- Psychological Distress: `python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 焦虑 --limit 3`
- Urban / Housing: `python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 城市 --limit 3`
- Health / Body: `python3 knowledge/scripts/query_health_body_risk_society_theme.py 身体 --limit 3`

## Active theme files

- `knowledge/themes/aesthetics-media/README.md`; `query_aesthetics_media_theme.py`; `validate_aesthetics_media_theme.py`.
- `knowledge/themes/capitalism/README.md`; `query_capitalism_theme.py`; `validate_capitalism_theme.py`.
- `knowledge/themes/feminism/README.md`; `query_feminism_theme.py`; `validate_feminism_theme.py`.
- `knowledge/themes/psychoanalysis-subjectivity/README.md`; `query_psychoanalysis_subjectivity_theme.py`; `validate_psychoanalysis_subjectivity_theme.py`.
- `knowledge/themes/time-death-finitude-life/README.md`; `query_time_death_theme.py`; `validate_time_death_theme.py`.
- Social-phenomena theme directories under `knowledge/themes/` with W5 validation at `--min-count 1044`.

## Work rules

- Do not overwrite `split_md/`.
- Do not change `split_md_clean/` unless the user explicitly asks for text cleaning.
- Do not promote W3/W5 beyond `draft` or W10 beyond `pilot-draft` without a separate review task.
- Do not add generated candidate runs, caches, local session state, or temporary files to the repository.
- For substantive claims, cite row/segment/clean-path/evidence-bank quote where possible.

## Validation commands

```bash
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
