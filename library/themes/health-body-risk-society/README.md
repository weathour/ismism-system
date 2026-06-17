# Health / Body / Medicine / Risk Society Evidence Package

- 中文名：健康—身体—医疗—风险社会证据包
- status: G031 theme package closure complete; concept/relation remain draft and close-reading remains pilot-draft
- date: 2026-06-16 CST
- protocol: `library/protocols/social-phenomena-diagnostic-protocol.md`
- manifest: `health-body-risk-society-row-manifest.jsonl` (120 reviewed rows)
- evidence bank: `health-body-risk-society-evidence-bank.jsonl` (330 exact-substring quote records)
- taxonomy: `health-body-risk-society-taxonomy.md`
- concept batch: `concept-HEALTH-BODY-RISK-SOCIETY-2026-06-16` (45 draft senses)
- relation batch: `relation-HEALTH-BODY-RISK-SOCIETY-2026-06-16` (40 draft relations)
- close-reading batch: 30 Health-body pilot-draft cards
- concept/relation notes: `health-body-risk-society-concept-relation-batch-notes.md`
- synthesis: `health-body-risk-society-synthesis.md`
- synthesis: `medicalization-risk-body-governance-synthesis.md`
- synthesis: `epidemic-stigma-vulnerability-synthesis.md`
- final validator: `tools/validate/themes/health_body_risk_society.py --repo . --final`
- query helper: `tools/query/themes/health_body_risk_society.py 身体 --limit 3`

This is not a medical encyclopedia, public-health guide, therapy manual, pandemic chronicle, clinical diagnosis table, or current health-policy commentary layer. It absorbs how ISMISM already lets health and bodily life appear: body/embodiment, medicine/treatment, health/disease/risk, epidemic/immunity, normality/pathology, stigma, and body governance.

## Scope markers

医疗 / 身体 / 身体性 / 身体化 / 肉身 / 生理 / 健康 / 疾病 / 风险 / 医疗化 / 健康主义 / 疫情 / 疫情记忆 / 身体治理 / 疾病污名 / 治疗 / 治愈 / 医学 / 医生 / 医院 / 卫生 / 免疫 / 症状 / 病理。

Boundary note: exact corpus hits for `医疗化`, `健康主义`, `身体治理`, `疫情记忆`, and `疾病污名` were not found in G029 search. They remain query-facing downstream labels only when row-level evidence such as 医疗、健康、疾病、风险、疫情、污名、治疗、医学、身体、身体性、身体化、卫生、免疫、症状 or 病理 supports the claim. Generic `身体` or `病` alone is not enough for a health-risk diagnosis.

## Counts

| Item | Count |
|---|---:|
| reviewed manifest rows | 120 |
| evidence quotes | 330 |
| core rows | 100 |
| bridge rows | 10 |
| excluded rows | 10 |

## Theme classes

- `body-embodiment-phenomenology` — 10 rows
- `body-governance-discipline` — 11 rows
- `epidemic-immunity-public-health` — 4 rows
- `excluded-keyword-only` — 10 rows
- `health-disease-risk` — 17 rows
- `medicalization-normality-pathology` — 20 rows
- `medicine-treatment-health-system` — 45 rows
- `stigma-vulnerability-disability` — 3 rows

## Interpretation rules

1. Start from manifest/evidence; do not upgrade a row from keyword presence alone.
2. Use the diagnostic grammar: phenomenon → subject-position → mechanism → fantasy/misrecognition → carrier → contradiction → practical opening.
3. Treat `医疗化`, `健康主义`, `身体治理`, `疫情记忆`, and `疾病污名` as downstream labels when exact strings are absent; require adjacent row evidence.
4. Keep claims inside corpus evidence; do not import external medical, public-health, psychiatry, nutrition, epidemiology, or policy claims.
5. G030 should add concept/relation draft records and close-reading pilot-draft cards without promoting prior draft statuses.
6. Cross-theme bridges to Psychological-distress, Feminism, Time-Death, Urban-housing, Governance-law, Labor, Family, and Capitalism require row-level quote support.
