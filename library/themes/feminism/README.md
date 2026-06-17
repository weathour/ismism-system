# Feminism / Gender / Sexuality / Social Reproduction Theme Package Layer

- status: theme package layer, draft-linked and validator-backed
- date: 2026-06-16
- manifest: `feminism-row-manifest.jsonl` (94 reviewed rows; 38 core / 46 bridge / 5 context / 5 excluded)
- evidence bank: `feminism-evidence-bank.jsonl` (309 exact quote records)
- concept batch: `concept-FEMINISM-2026-06-16` (78 draft term senses)
- relation batch: `relation-FEMINISM-2026-06-16` (65 draft relation assets)
- close-reading batch: `close-reading-FEMINISM-2026-06-16` (45 pilot-draft cards)
- validator: `python3 tools/validate/themes/feminism.py --repo . --final`
- query helper: `python3 tools/query/themes/feminism.py 女权 --limit 3`

This layer is **not** an external feminism/gender-studies encyclopedia. It absorbs how ISMISM internally handles false feminism, misogyny, patriarchal fantasy, female-essence mystification, sexualized body, erotic economy, love/romance/marriage/intimacy, family/birth/reproduction/social reproduction, and practice-oriented liberation.

## Central question

> ISMISM 如何把女权问题拆成男权幻想、厌女结构、性化身体、爱欲经济、爱情意识形态、家庭/生殖/社会再生产和实践解放问题？

## Files

- `feminism-row-manifest.jsonl` — reviewed candidate manifest.
- `feminism-evidence-bank.jsonl` — exact clean-text quote bank with `ev:feminism:*` ids.
- `feminism-taxonomy.md` — controlled taxonomy and row ownership map.
- `feminism-concept-relation-batch-notes.md` — concept/relation batch discipline and relation boundaries.

## Query examples

```bash
python3 tools/query/themes/feminism.py 女权 --limit 3
python3 tools/query/themes/feminism.py 厌女 --limit 3
python3 tools/query/themes/feminism.py 爱欲 --limit 3
python3 tools/query/themes/feminism.py --row 90
python3 tools/query/themes/feminism.py --class false-feminism-and-female-essence
```

## Interpretation rules

1. Start from manifest, then inspect evidence bank.
2. Treat concept/relation additions as `draft` and close-reading cards as `pilot-draft`.
3. Do not include every `身体`, `解放`, `家庭`, `女性`, or `爱欲` hit; use `theme_role` and quote roles.
4. Cross-theme links are valid only when the feminism/gender/social-reproduction function is explicit.
