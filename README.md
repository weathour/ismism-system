# ISMISM System

A standalone corpus-grounded knowledge-processing repository for 未明子《主义主义》. The project is ready to be treated as a fresh public repository: active materials live in the corpus files, `knowledge/`, and `skills/`; generated caches and discarded candidate layers are not part of the project contract.

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Current global counts are 1676 W3 senses / 1228 terms; 6/363 rows remain W1/W2-only; 277 rows now have W3+W5+W10 overlap.
99.9% clean-text volume has W3/W5/W10 absorption coverage.

Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## What is in scope

- Corpus registry: `目录索引_结构化.csv`, `目录索引_结构化.md`.
- Source text: `split_md/`, `split_md_clean/`, and the root PDF.
- Knowledge layer: `knowledge/manifests/`, `segment-cards/`, `lexicon/`, `position-cards/`, `relations/`, `w10-absorption/`, `themes/`, `syntheses/`, `references/`, `qa/`, `scripts/`.
- Operator surface: `skills/ismism-knowledge-operator/SKILL.md`.
- Project contract: `PROJECT-SPEC.md`.

## Theme layers

- AI maximum absorption layer — `knowledge/themes/ai/README.md`; `validate_ai_theme.py`; `query_ai_theme.py`.
- Chinese Philosophy maximum absorption layer — `knowledge/themes/chinese-philosophy/README.md`; `validate_chinese_philosophy_theme.py`; `query_chinese_philosophy_theme.py`.
- Religion Problem maximum absorption layer — `knowledge/themes/religion/README.md`; `validate_religion_theme.py`; `query_religion_theme.py`.
- Time-Death-Finitude-Life maximum absorption layer — `knowledge/themes/time-death-finitude-life/README.md`; 85-row manifest, 289 quote-bank records; `validate_time_death_theme.py`; `query_time_death_theme.py`.
- Capitalism / Political Economy maximum absorption layer — `knowledge/themes/capitalism/README.md`; `validate_capitalism_theme.py`; `query_capitalism_theme.py`.
- Feminism / Gender / Sexuality / Social Reproduction maximum absorption — `knowledge/themes/feminism/README.md`; `validate_feminism_theme.py`; `query_feminism_theme.py`.
- Psychoanalysis / Subjectivity / Desire / Discourse / Language maximum absorption — `knowledge/themes/psychoanalysis-subjectivity/README.md`; `validate_psychoanalysis_subjectivity_theme.py`; `query_psychoanalysis_subjectivity_theme.py`.
- Aesthetics / Art / Media / Image / Narrative maximum absorption — `knowledge/themes/aesthetics-media/README.md`; `validate_aesthetics_media_theme.py`; `query_aesthetics_media_theme.py`.
- Labor / Workplace / Precarity / Involution maximum absorption — `knowledge/themes/labor-workplace-precarity/README.md`; `validate_labor_workplace_precarity_theme.py`; `query_labor_workplace_precarity_theme.py`.
- Education / Examination / Credentialism / Knowledge Discipline maximum absorption — `knowledge/themes/education-examination-credentialism/README.md`; `validate_education_examination_credentialism_theme.py`; `query_education_examination_credentialism_theme.py`.
- Family / Intimacy / Marriage / Birth / Social Reproduction maximum absorption — `knowledge/themes/family-intimacy-reproduction/README.md`; `validate_family_intimacy_reproduction_theme.py`; `query_family_intimacy_reproduction_theme.py`.
- Consumption / Desire / Commodity / Lifestyle maximum absorption — `knowledge/themes/consumption-desire-lifestyle/README.md`; `validate_consumption_desire_lifestyle_theme.py`; `query_consumption_desire_lifestyle_theme.py`.
- Media / Platform / Public Opinion / Traffic Society maximum absorption — `knowledge/themes/media-platform-public-opinion/README.md`; `validate_media_platform_public_opinion_theme.py`; `query_media_platform_public_opinion_theme.py`.
- Governance / Law / Bureaucracy / Order maximum absorption — `knowledge/themes/governance-law-bureaucracy/README.md`; `validate_governance_law_bureaucracy_theme.py`; `query_governance_law_bureaucracy_theme.py`.
- Class / Youth / Generation / Mobility Anxiety maximum absorption — `knowledge/themes/class-youth-generational-anxiety/README.md`; `validate_class_youth_generational_anxiety_theme.py`; `query_class_youth_generational_anxiety_theme.py`.
- Psychological Distress / Anxiety / Addiction / Social Symptom maximum absorption — `knowledge/themes/psychological-distress-social-symptom/README.md`; `validate_psychological_distress_social_symptom_theme.py`; `query_psychological_distress_social_symptom_theme.py`.
- Urban / Housing / Migration / Space maximum absorption — `knowledge/themes/urban-housing-migration-space/README.md`; `validate_urban_housing_migration_space_theme.py`; `query_urban_housing_migration_space_theme.py`.
- Health / Body / Medicine / Risk Society maximum absorption — `knowledge/themes/health-body-risk-society/README.md`; `validate_health_body_risk_society_theme.py`; `query_health_body_risk_society_theme.py`.

## Common query examples

```bash
python3 knowledge/scripts/query_social_phenomena_superphase.py 内卷 --limit 3
python3 knowledge/scripts/query_psychoanalysis_subjectivity_theme.py 精神分析 --limit 3
python3 knowledge/scripts/query_capitalism_theme.py 资本主义 --limit 3
python3 knowledge/scripts/query_time_death_theme.py 时间 --limit 3
python3 knowledge/scripts/query_aesthetics_media_theme.py 电影 --limit 3
```

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

## Fresh-project rule

The repository should be developed from the current corpus and `knowledge/` contract only. Do not add generated cache folders, candidate runs, local session state, or unrelated product prototypes to the public project.
