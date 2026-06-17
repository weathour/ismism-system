# Aesthetics / Art / Media / Image / Narrative Theme Package Layer

- 中文名：美学—艺术—媒介—影像—叙事主题证据层
- status: theme package layer, draft-linked and validator-backed
- date: 2026-06-16
- purpose: film-analysis precursor absorption; this does **not** create a film-analysis matrix yet.
- manifest: `aesthetics-media-row-manifest.jsonl` (69 reviewed rows)
- evidence bank: `aesthetics-media-evidence-bank.jsonl` (192 exact quote records)
- concept batch: `concept-AESTHETICS-MEDIA-2026-06-16` (53 draft senses)
- relation batch: `relation-AESTHETICS-MEDIA-2026-06-16` (44 draft relations)
- close-reading batch: `close-reading-AESTHETICS-MEDIA-2026-06-16` (30 pilot-draft cards)
- validator: `python3 tools/validate/themes/aesthetics_media.py --repo . --final`
- query helper: `python3 tools/query/themes/aesthetics_media.py 电影 --limit 3`

This layer is **not** an external film-studies, aesthetics, media-studies, or narratology encyclopedia. It absorbs how ISMISM internally uses cinema examples, viewing, image, symbol, text, art, poetry, fiction, narrative, hermeneutics, mass culture, and media as structures that can later support deep film analysis.

## Central question

> ISMISM 如何把电影/影像/观看/艺术/诗/小说/文本/叙事/媒介当作主体、欲望、意识形态、时间、宗教与资本结构的显影面？

## Files

- `aesthetics-media-row-manifest.jsonl` — reviewed candidate manifest.
- `aesthetics-media-evidence-bank.jsonl` — exact clean-text quote bank with `ev:aesthetics-media:*` ids.
- `aesthetics-media-taxonomy.md` — controlled taxonomy and row ownership map.
- `aesthetics-media-concept-relation-batch-notes.md` — concept/relation batch discipline and relation boundaries.
- `aesthetics-media-synthesis.md` — total evidence-marker synthesis.
- `film-analysis-precursor-synthesis.md` — specific bridge from this layer to future film analysis.

## Query examples

```bash
python3 tools/query/themes/aesthetics_media.py 电影 --limit 3
python3 tools/query/themes/aesthetics_media.py 叙事 --limit 3
python3 tools/query/themes/aesthetics_media.py 美学 --limit 3
python3 tools/query/themes/aesthetics_media.py --row 259
python3 tools/query/themes/aesthetics_media.py --class categorical-narratology
```

## Interpretation rules

1. Start from manifest, then inspect evidence bank.
2. Treat concept/relation additions as `draft` and close-reading cards as `pilot-draft`.
3. Do not treat every `电影`, `艺术`, `诗`, `符号`, or `叙事` hit as core; use `theme_role` and quote roles.
4. For future film analysis, combine this layer with Psychoanalysis-Subjectivity, Capitalism, Feminism, Time-Death, Religion, and AI only when the row evidence makes the bridge explicit.
