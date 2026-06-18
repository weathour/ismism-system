# 德国观念论—辩证法 Theme Package Layer

- slug: german-idealism-dialectics
- 中文名：德国观念论—辩证法
- status: Field 3 theme package layer, draft-linked and validator-backed
- date: 2026-06-18
- manifest: `german-idealism-dialectics-row-manifest.jsonl` (36 reviewed rows)
- evidence bank: `german-idealism-dialectics-evidence-bank.jsonl` (58 exact quote records)
- concept/relation/close-reading batches: deferred in this run
- validator: `python3 tools/validate/themes/german_idealism_dialectics.py --repo . --final`
- query helper: `python3 tools/query/themes/german_idealism_dialectics.py 德国观念论 --limit 3`

不是德国哲学通史，也不是把所有“自由/精神/否定”词频都收编为观念论。

## Central question

ISMISM 如何把康德、费希特、谢林、黑格尔和否定辩证法组织为现代主体、自由、体系与否定运动的问题？

## Files
- `german-idealism-dialectics-row-manifest.jsonl`
- `german-idealism-dialectics-evidence-bank.jsonl`
- `german-idealism-dialectics-taxonomy.md`
- `german-idealism-dialectics-concept-relation-notes.md`
- `german-idealism-dialectics-synthesis.md`

## Current metrics

- reviewed rows: 36
- evidence quotes: 58
- role counts: {"context": 1, "bridge": 10, "excluded": 3, "core": 22}
- taxonomy class counts: {"idealism-overview-review": 3, "idealism-dialectics-bridge": 10, "excluded-keyword-only": 3, "critical-philosophy-limits": 5, "science-of-knowledge-self-positing": 5, "system-freedom-schelling": 5, "dialectic-negativity-hegel": 5}

## Query examples

- python3 tools/query/themes/german_idealism_dialectics.py 德国观念论 --limit 3
- python3 tools/query/themes/german_idealism_dialectics.py --row 210
- python3 tools/query/themes/german_idealism_dialectics.py --class critical-philosophy-limits --limit 3

## Interpretation rules

1. Start from the row manifest, then inspect exact quotes in the evidence bank.
2. Treat bridge rows as bridge evidence only, not as full ownership transfer.
3. Concept/relation/close-reading batches are deferred and must remain draft/pilot-draft if later added.
4. Do not import external encyclopedia claims or current-event/professional-advice claims into this theme.
