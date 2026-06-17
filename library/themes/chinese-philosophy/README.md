# Chinese Philosophy Theme Package Layer

- status: pilot-draft theme package layer
- created: 2026-06-15 CST
- scope: exact 70 rows across ancient Chinese philosophy, Buddhist/Chan bridge, Mao philosophy / Chinese Marxist practice, and revolutionary/dialectical context
- source discipline: corpus evidence and `corpus/clean-markdown` quotes remain authoritative; this directory is an index/synthesis surface.

## Files

| File | Function |
|---|---|
| `chinese-philosophy-row-manifest.jsonl` | 70-row candidate manifest with row/segment/path metadata, keyword hits, class, absorption state, and recommended action. |
| `chinese-philosophy-evidence-bank.jsonl` | 238 exact-substring quotes from declared clean files. |
| `chinese-philosophy-taxonomy.md` | Controlled Chinese philosophy theme axes and row/evidence links. |
| `chinese-philosophy-synthesis.md` | Total evidence-linked synthesis. |
| `ancient-chinese-philosophy-synthesis.md` | Ancient/Daoist/Buddhist/Names/Yijing synthesis. |
| `mao-philosophy-synthesis.md` | Mao philosophy / Chinese Marxist practice synthesis. |
| `chinese-philosophy-concept-relation-batch-notes.md` | Batch note for draft concept/relation additions. |

## Counts

- manifest rows: 70
- quote-bank records: 238
- Chinese philosophy concept draft senses: 60 (`batch_id=concept-CHINESE-PHILOSOPHY-2026-06-15`)
- Chinese philosophy relation draft relations: 50 (`batch_id=relation-CHINESE-PHILOSOPHY-2026-06-15`)
- Chinese philosophy close-reading new cards: 45

## Common queries

```bash
python3 tools/query/themes/chinese_philosophy.py 实践论 --limit 3
python3 tools/query/themes/chinese_philosophy.py --row 131
python3 tools/query/themes/chinese_philosophy.py --class buddhist-chan-bridge
```

## Interpretation rules

1. Start from `chinese-philosophy-row-manifest.jsonl` to identify rows and class.
2. Use `chinese-philosophy-evidence-bank.jsonl` for exact source quotes.
3. Use concept senses for draft term meanings and relation relations for row-bound movements.
4. Use close-reading cards for close-reading argument/process/case structure.
5. Do not treat this theme layer as a neutral Chinese philosophy encyclopedia.
6. Do not promote concept/relation records out of `draft`; close-reading remains `pilot-draft`.
