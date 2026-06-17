# Time-Death-Finitude-Life Theme Package Layer

- status: pilot-draft theme package layer
- created: 2026-06-15 CST
- scope: 85 reviewed rows around death as the main axis, with time / finitude / life / body / memory / Buddhist liberation / AI technical life as structured bridges.
- source discipline: corpus evidence and exact `corpus/clean-markdown` quotes remain authoritative; this directory is an index/synthesis surface.

## What this is not

This is not a neutral encyclopedia of time philosophy, death studies, Buddhism, AI, or life science. It absorbs how ISMISM internally handles death, time, finite subjectivity, life/body, memory preservation, rebirth/liberation, and technical life/mortality.

## Files

- `time-death-row-manifest.jsonl` — 85-row reviewed manifest.
- `time-death-evidence-bank.jsonl` — 289 exact-substring clean-text quotes.
- `time-death-taxonomy.md` — controlled theme-class ownership.
- `time-death-concept-relation-batch-notes.md` — concept/relation batch discipline.
- `time-death-close-reading-coverage.jsonl` — close-reading new-card/reuse/context rationale matrix.
- `time-death-finitude-life-synthesis.md`, `life-body-immortality-synthesis.md`, `historical-time-and-practice-synthesis.md` — evidence-marker syntheses.

## Counts

- manifest rows: 85
- quote-bank records: 289
- Time-death-life concept draft senses: 60 (`batch_id=concept-TIME-DEATH-LIFE-2026-06-15`)
- Time-death-life relation draft relations: 50 (`batch_id=relation-TIME-DEATH-LIFE-2026-06-15`)
- Time-death-life close-reading new cards: 42 (`batch_id=close-reading-TIME-DEATH-LIFE-2026-06-15`)
- required coverage: AI rows 350–363, Buddhist core 120–124/140/141/186, death-axis hard core rows.

## Common queries

```bash
python3 tools/query/themes/time_death_finitude_life.py 时间 --limit 3
python3 tools/query/themes/time_death_finitude_life.py 死亡 --limit 3
python3 tools/query/themes/time_death_finitude_life.py 生命 --limit 3
python3 tools/query/themes/time_death_finitude_life.py 永生 --limit 3
python3 tools/query/themes/time_death_finitude_life.py 有限 --limit 3
python3 tools/query/themes/time_death_finitude_life.py --class ai-immortality-mortality
python3 tools/query/themes/time_death_finitude_life.py --row 362
```

## Interpretation rules

1. Start from `time-death-row-manifest.jsonl`, then inspect quote-bank evidence.
2. Treat concept/relation records as `draft` and close-reading cards as `pilot-draft`.
3. Do not mechanically copy AI / Chinese Philosophy / Religion syntheses; this layer requires death/time/finitude/life-specific function.
4. Use `tools/validate/themes/time_death_finitude_life.py --final` before relying on a synthesis claim.
