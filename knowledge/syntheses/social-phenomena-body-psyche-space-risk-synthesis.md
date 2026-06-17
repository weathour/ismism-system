# Social Phenomena Phase 3 — Body, Psyche, Space, and Risk Synthesis

- status: G034 cross-theme synthesis; evidence-routed, not canonical ontology
- phase: Social Phenomena / Everyday Life Problems Maximum Absorption Superphase
- integrates:
  - `knowledge/themes/psychological-distress-social-symptom/`
  - `knowledge/themes/urban-housing-migration-space/`
  - `knowledge/themes/health-body-risk-society/`
- method anchor: `knowledge/references/social-phenomena-diagnostic-protocol.md`
- boundary: not clinical diagnosis, therapy advice, medical/public-health guidance, housing advice, city-policy analysis, or current-events commentary.

## Core question

How do social contradictions sediment into body, psyche, spatial life, and risk consciousness?

This phase answers: when labor, education, family, consumption, platforms, institutions, and class position cannot be resolved as practice, their contradictions often reappear as private suffering, compulsive relief, spatial displacement, unstable dwelling, bodily symptom, medical naming, risk management, stigma, or health responsibility.

```text
social contradiction
→ private affect / anxiety / symptom
→ spatial location, dwelling, migration, public/private exposure
→ body, treatment, health/disease boundary, risk management
→ stigma, vulnerability, self-management, or renewed practice opening
```

This is the repository's body-psyche-space-risk route. It does not diagnose real people or prescribe solutions. It supplies a way to ask which row-backed mechanisms are at work when a phenomenon appears as `躺平`, `抑郁焦虑`, `住房焦虑`, `城市漂泊`, `医疗焦虑`, `健康主义`, or `身体治理`.

## Diagnostic axes

### 1. Psychological distress as the privatized return of social contradiction

The Psychological-distress layer reads anxiety, pain, despair, nihilism, addiction, repression, trauma, and symptom naming as a social-symptom surface rather than as private facts alone.

Evidence route:

- main synthesis: `knowledge/themes/psychological-distress-social-symptom/psychological-distress-social-symptom-synthesis.md`
- focused synthesis: `knowledge/themes/psychological-distress-social-symptom/anxiety-addiction-social-symptom-synthesis.md`
- focused synthesis: `knowledge/themes/psychological-distress-social-symptom/private-psychologization-and-trauma-synthesis.md`
- classes: `anxiety-depression-distress`, `addiction-enjoyment-compulsion`, `symptom-pathology-medicalization`, `repression-trauma-return`, `nihilism-cynicism-social-symptom`, `private-psychologization-bridge`

Diagnostic use: for `抑郁焦虑`, `躺平`, `内耗`, `成瘾`, `心理咨询产业`, or `社会矛盾私人化`, ask what pressure is being privatized, what enjoyment/repetition captures relief, and what social relation disappears when the problem is named as merely psychological.

### 2. Urban, housing, migration, and space as contradiction made positional

The Urban-housing layer reads space as a carrier of social contradiction: city/public visibility, house/dwelling as settlement, land/rural production relation, migration/drifting, public/private exposure, and spatial stratification.

Evidence route:

- main synthesis: `knowledge/themes/urban-housing-migration-space/urban-housing-migration-space-synthesis.md`
- focused synthesis: `knowledge/themes/urban-housing-migration-space/housing-migration-spatial-stratification-synthesis.md`
- focused synthesis: `knowledge/themes/urban-housing-migration-space/rural-urban-public-space-synthesis.md`
- classes: `urban-public-space`, `housing-dwelling-property`, `rural-urban-difference`, `migration-drifting-mobility`, `spatial-stratification`, `urban-capital-infrastructure-bridge`

Diagnostic use: for `住房焦虑`, `城市漂泊`, `城乡差异`, `公共空间`, `空间阶层化`, or `迁徙`, ask whether the problem is about occupying a stable place, moving between places, being visible in public, being excluded, or having social hierarchy sediment as position. `住房`, `租房`, `房价`, and `户籍` remain downstream labels unless exact corpus evidence is found through adjacent terms such as 房子/居住/买房/迁移/漂泊/土地.

### 3. Health, body, medicine, and risk as contradiction made somatic and governable

The Health-body layer reads the body as a site where social contradiction, life risk, medical naming, health/disease boundaries, treatment, vulnerability, stigma, and governance meet.

Evidence route:

- main synthesis: `knowledge/themes/health-body-risk-society/health-body-risk-society-synthesis.md`
- focused synthesis: `knowledge/themes/health-body-risk-society/medicalization-risk-body-governance-synthesis.md`
- focused synthesis: `knowledge/themes/health-body-risk-society/epidemic-stigma-vulnerability-synthesis.md`
- classes: `body-embodiment-phenomenology`, `medicine-treatment-health-system`, `health-disease-risk`, `epidemic-immunity-public-health`, `medicalization-normality-pathology`, `body-governance-discipline`, `stigma-vulnerability-disability`

Diagnostic use: for `医疗焦虑`, `健康主义`, `疾病污名`, `身体治理`, `疫情记忆`, or `风险社会`, ask how a bodily difference or vulnerability is named, treated, normalized, governed, stigmatized, or made the individual's responsibility. This layer cannot be used for medical advice or public-health claims.

## Cross-theme sedimentation map

| Movement | Diagnostic question | Evidence-routed interpretation |
|---|---|---|
| contradiction → psyche | What pressure returns as private suffering, anxiety, compulsive relief, trauma, or nihilism? | The symptom is read as a social-symptom surface only when row evidence connects pain/symptom to a social relation or displaced contradiction. |
| psyche → space | Where does suffering locate itself: home, city, public space, route, edge, migration, dwelling, or exclusion? | Spatial life turns relation into position, visibility, route, or lack of settlement. |
| space → body | How does location become bodily exposure, fatigue, vulnerability, discipline, treatment, or risk? | Body is not pure nature; it is the site where social arrangements are felt, named, managed, and resisted. |
| body → institution | Who names the body: medicine, family, workplace, school, platform, law, or self-management discourse? | Medicalization/risk governance can help, but can also hide social contradiction behind diagnosis and responsibility. |
| risk → psyche | Does risk awareness open collective care or return as self-blame and anxiety? | Risk society can convert shared vulnerability into individualized vigilance. |
| stigma → space | Is the vulnerable body included, hidden, expelled, managed, or made spectacular? | Disease/abnormality can become a public/private boundary and spatial exclusion mechanism. |

## Practical diagnostic route

For a concrete Phase 3 query:

1. Start with the everyday label, but immediately translate it into a route: psychological distress, spatial position, or body/risk.
2. Run the matching theme query helper and inspect exact evidence records.
3. Check whether the theme class supports the claim; do not rely on a generic keyword.
4. Identify the subject-position: anxious subject, addicted/repetitive subject, drifting/migrating subject, dwelling-seeking subject, patient, healthy/unhealthy body, stigmatized/vulnerable body.
5. Identify the mechanism: privatization, compulsion, spatialization, stratification, medicalization, risk management, body governance, stigma.
6. Ask what practical opening remains: collective practice, spatial reorganization, care, de-privatization, or critique of medical/risk/family/platform/institutional overcoding.
7. Keep W3/W5 as draft handles and W10 as pilot-draft close-reading aids.

## Query routes

```bash
# Psychological distress / anxiety / addiction / social symptom
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 焦虑 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 成瘾 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 躺平 --limit 3
python3 knowledge/scripts/query_psychological_distress_social_symptom_theme.py 内耗 --limit 3

# Urban / housing / migration / space
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 城市 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 房子 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 迁移 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 公共空间 --limit 3
python3 knowledge/scripts/query_urban_housing_migration_space_theme.py 漂泊 --limit 3

# Health / body / medicine / risk society
python3 knowledge/scripts/query_health_body_risk_society_theme.py 身体 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 医疗 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 疾病 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 风险 --limit 3
python3 knowledge/scripts/query_health_body_risk_society_theme.py 健康 --limit 3
```

## Boundary and failure modes

- Do not diagnose real people, advise treatment, infer medication/therapy need, or make public-health recommendations.
- Do not treat housing/urban/medical labels as direct evidence when the exact corpus lacks those terms; use adjacent row evidence and state downstream-label status.
- Do not collapse social contradiction into individual weakness, bad health habits, personal psychology, or city-choice advice.
- Do not collapse body into biology: in this route body is experience, vulnerability, discipline, risk, and social relation carrier.
- W3/W5 remain `draft`; W10 remains `pilot-draft`.
