# Psychological Distress / Anxiety / Addiction / Social Symptom Evidence Package

- 中文名：心理困境—焦虑—成瘾—社会症状证据包
- status: G025 maximum absorption closure complete; W3/W5/W10 remain draft/pilot-draft
- date: 2026-06-16 CST
- protocol: `knowledge/references/social-phenomena-diagnostic-protocol.md`
- manifest: `psychological-distress-social-symptom-row-manifest.jsonl` (120 reviewed rows)
- evidence bank: `psychological-distress-social-symptom-evidence-bank.jsonl` (340 exact-normalizable quote records)
- taxonomy: `psychological-distress-social-symptom-taxonomy.md`
- W3 batch: `W3-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16` (45 draft senses)
- W5 batch: `W5-PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-2026-06-16` (40 draft relations)
- W10 batch: 30 Psychological-distress pilot-draft cards
- W3/W5 notes: `psychological-distress-social-symptom-w3-w5-batch-notes.md`
- synthesis: `psychological-distress-social-symptom-synthesis.md`
- synthesis: `anxiety-addiction-social-symptom-synthesis.md`
- synthesis: `private-psychologization-and-trauma-synthesis.md`
- final handoff: `PSYCHOLOGICAL-DISTRESS-SOCIAL-SYMPTOM-MAXIMUM-ABSORPTION-HANDOFF.md`
- final validator: `knowledge/scripts/validate_psychological_distress_social_symptom_theme.py --repo . --final`
- query helper: `knowledge/scripts/query_psychological_distress_social_symptom_theme.py 焦虑 --limit 3`

This is not a clinical psychology manual, psychiatric diagnosis table, therapy-industry survey, or current mental-health commentary layer. It absorbs how ISMISM already lets everyday psychic suffering appear as social symptom: anxiety/depression vocabulary, nihilism/flatness/cynicism, addictive enjoyment, symptom/pathology language, repression/trauma, psychologization of social contradiction, and bridges to desire/subjectivity/psychoanalysis.

## Scope markers

心理困境 / 焦虑 / 抑郁 / 成瘾 / 症状 / 社会症状 / 虚无 / 躺平 / 内耗 / 心理咨询 / 心理 / 痛苦 / 绝望 / 犬儒 / 享乐 / 欲望 / 压抑 / 抑制 / 创伤 / 疾病 / 治疗 / 治愈 / 神经症 / 精神病 / 社会矛盾私人化。

Boundary note: generic `心理`, philosophical `心理主义`, neuroscientific `神经`, metaphysical `虚无`, or psychoanalytic `欲望` is not automatically evidence for lived psychological distress. G023 keeps excluded rows as boundary controls and treats social-symptom diagnosis as a function: private suffering, compulsive enjoyment, pathological naming, repression/trauma, and the displacement of social contradiction into individual psychic management.

## Counts

| Item | Count |
|---|---:|
| reviewed manifest rows | 120 |
| evidence quotes | 340 |
| core rows | 100 |
| bridge rows | 10 |
| context rows | 0 |
| excluded rows | 10 |

## Theme classes

- `addiction-enjoyment-compulsion` — 21 rows
- `anxiety-depression-distress` — 52 rows
- `desire-subjectivity-psychoanalysis-bridge` — 5 rows
- `excluded-keyword-only` — 10 rows
- `nihilism-flatness-cynicism` — 3 rows
- `private-psychologization` — 2 rows
- `repression-trauma-psychic-wound` — 7 rows
- `social-contradiction-private-suffering` — 5 rows
- `symptom-pathology-medicalization` — 15 rows

## Interpretation rules

1. Start from the manifest, then inspect the evidence bank; do not upgrade a row from keyword presence alone.
2. Use the shared diagnostic grammar: phenomenon → subject-position → mechanism → fantasy/misrecognition → carrier → contradiction → practical opening.
3. Treat `躺平`, `内耗`, `心理咨询产业`, and `社会矛盾私人化` as downstream diagnostic labels when exact strings are absent; require adjacent evidence such as `心理`, `焦虑`, `痛苦`, `症状`, `治疗`, `欲望`, `享乐`, `虚无`, `犬儒`, `压抑`, or social/private contradiction wording.
4. Keep social phenomenon claims inside corpus evidence; do not import current-events psychology, psychiatry, therapy-market, or demographic claims.
5. G024 should add W3/W5 draft records and W10 pilot-draft cards without promoting prior draft statuses.
6. Cross-theme bridges to Psychoanalysis-Subjectivity, Labor, Education, Consumption, Media-platform, Class-youth, Feminism, and Health-body require row-level quote support.
