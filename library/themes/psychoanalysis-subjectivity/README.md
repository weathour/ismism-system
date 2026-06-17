# Psychoanalysis / Subjectivity / Desire / Discourse / Language Theme Package Layer

- 中文名：精神分析—主体性—欲望—话语—语言主题证据层
- status: theme package layer, draft-linked and validator-backed
- date: 2026-06-16
- manifest: `psychoanalysis-subjectivity-row-manifest.jsonl` (120 reviewed rows)
- evidence bank: `psychoanalysis-subjectivity-evidence-bank.jsonl` (387 exact quote records)
- concept batch: `concept-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16` (89 draft senses)
- relation batch: `relation-PSYCHOANALYSIS-SUBJECTIVITY-2026-06-16` (75 draft relations)
- close-reading batch: 58 pilot-draft cards
- validator: `python3 tools/validate/themes/psychoanalysis_subjectivity.py --repo . --final`
- query helper: `python3 tools/query/themes/psychoanalysis_subjectivity.py 精神分析 --limit 3`

This layer is **not** an external Freud/Lacan encyclopedia, not a generic psychoanalysis history, and not a neutral language-philosophy survey. It absorbs how ISMISM internally handles psychoanalysis, subjectivity, desire, enjoyment, fantasy, big Other, unconscious, symptom/repression/perversion, dream, signifier/signified/symbolic order, discourse, statement, language games, ideology diagnosis, and practice transformation.

Central question: ISMISM 如何把“主体问题”拆成大他者、无意识、欲望、享乐、幻想、话语结构、语言游戏、符号秩序、意识形态诊断与实践转化问题？

## Files

- `psychoanalysis-subjectivity-row-manifest.jsonl`
- `psychoanalysis-subjectivity-evidence-bank.jsonl`
- `psychoanalysis-subjectivity-taxonomy.md`
- `psychoanalysis-subjectivity-concept-relation-batch-notes.md`
- `subjectivity-symbolic-order-and-big-other-synthesis.md`
- `psychoanalysis-unconscious-desire-and-symptom-synthesis.md`
- `discourse-language-game-and-truth-synthesis.md`
- `ideology-fantasy-and-practice-diagnosis-synthesis.md`
- `cross-theme-psychoanalytic-bridges-synthesis.md`

## Current metrics

- reviewed rows: 120 (53 core / 53 bridge / 2 context / 12 excluded)
- evidence quotes: 387
- concept/relation/close-reading additions: 89 / 75 / 58
- global counts after this layer: 1173 concept senses / 774 terms; 600 relation relations; 411 close-reading cards; relation validator min-count `600`.

## Query examples

```bash
python3 tools/query/themes/psychoanalysis_subjectivity.py 精神分析 --limit 3
python3 tools/query/themes/psychoanalysis_subjectivity.py --row 273
python3 tools/query/themes/psychoanalysis_subjectivity.py --class psychoanalysis-unconscious-desire
```

## Interpretation rules

Start from manifest and evidence bank; concept/relation remain `draft`; close-reading remains `pilot-draft`; anti-psychologism and anti-pansexualism are hard boundaries.
