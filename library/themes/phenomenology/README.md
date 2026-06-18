# 现象学 Theme Package Layer

- slug: phenomenology
- 中文名：现象学
- status: Field 3 theme package layer, draft-linked and validator-backed
- date: 2026-06-18
- manifest: `phenomenology-row-manifest.jsonl` (36 reviewed rows)
- evidence bank: `phenomenology-evidence-bank.jsonl` (58 exact quote records)
- concept/relation/close-reading batches: deferred in this run
- validator: `python3 tools/validate/themes/phenomenology.py --repo . --final`
- query helper: `python3 tools/query/themes/phenomenology.py 现象学 --limit 3`

不是外部现象学史、不是胡塞尔百科，也不是把所有“意识/主体”词频都收编为现象学。

## Central question

ISMISM 如何把胡塞尔及其后继的现象学拆成意向性、还原、生活世界、主体间性、身体/现世和存在论化的哲学方法问题？

## Files
- `phenomenology-row-manifest.jsonl`
- `phenomenology-evidence-bank.jsonl`
- `phenomenology-taxonomy.md`
- `phenomenology-concept-relation-notes.md`
- `phenomenology-synthesis.md`

## Current metrics

- reviewed rows: 36
- evidence quotes: 58
- role counts: {"context": 1, "core": 22, "bridge": 10, "excluded": 3}
- taxonomy class counts: {"phenomenology-overview-review": 3, "transcendental-intentionality-reduction": 5, "eidetic-factual-phenomenology": 5, "lifeworld-intersubjectivity": 5, "worldly-ontological-phenomenology": 5, "phenomenology-bridge": 10, "excluded-keyword-only": 3}

## Query examples

- python3 tools/query/themes/phenomenology.py 现象学 --limit 3
- python3 tools/query/themes/phenomenology.py --row 188
- python3 tools/query/themes/phenomenology.py --class transcendental-intentionality-reduction --limit 3

## Interpretation rules

1. Start from the row manifest, then inspect exact quotes in the evidence bank.
2. Treat bridge rows as bridge evidence only, not as full ownership transfer.
3. Concept/relation/close-reading batches are deferred and must remain draft/pilot-draft if later added.
4. Do not import external encyclopedia claims or current-event/professional-advice claims into this theme.
