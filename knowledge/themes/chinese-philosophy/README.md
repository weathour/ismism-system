# Chinese Philosophy Maximum Absorption Layer

- status: pilot-draft maximum absorption layer
- created: 2026-06-15 CST
- scope: exact 70 rows across ancient Chinese philosophy, Buddhist/Chan bridge, Mao philosophy / Chinese Marxist practice, and revolutionary/dialectical context
- source discipline: corpus evidence and `split_md_clean` quotes remain authoritative; this directory is an index/synthesis surface.

## Files

| File | Function |
|---|---|
| `chinese-philosophy-row-manifest.jsonl` | 70-row candidate manifest with row/segment/path metadata, keyword hits, class, absorption state, and recommended action. |
| `chinese-philosophy-evidence-bank.jsonl` | 238 exact-substring quotes from declared clean files. |
| `chinese-philosophy-taxonomy.md` | Controlled Chinese philosophy theme axes and row/evidence links. |
| `chinese-philosophy-synthesis.md` | Total evidence-linked synthesis. |
| `ancient-chinese-philosophy-synthesis.md` | Ancient/Daoist/Buddhist/Names/Yijing synthesis. |
| `mao-philosophy-synthesis.md` | Mao philosophy / Chinese Marxist practice synthesis. |
| `chinese-philosophy-w3-w5-batch-notes.md` | Batch note for draft W3/W5 additions. |

## Counts

- manifest rows: 70
- quote-bank records: 238
- Chinese philosophy W3 draft senses: 60 (`batch_id=W3-CHINESE-PHILOSOPHY-2026-06-15`)
- Chinese philosophy W5 draft relations: 50 (`batch_id=W5-CHINESE-PHILOSOPHY-2026-06-15`)
- Chinese philosophy W10 new cards: 45

## Common queries

```bash
python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3
python3 knowledge/scripts/query_chinese_philosophy_theme.py --row 131
python3 knowledge/scripts/query_chinese_philosophy_theme.py --class buddhist-chan-bridge
```

## Interpretation rules

1. Start from `chinese-philosophy-row-manifest.jsonl` to identify rows and class.
2. Use `chinese-philosophy-evidence-bank.jsonl` for exact source quotes.
3. Use W3 senses for draft term meanings and W5 relations for row-bound movements.
4. Use W10 cards for close-reading argument/process/case structure.
5. Do not treat this theme layer as a neutral Chinese philosophy encyclopedia.
6. Do not promote W3/W5 records out of `draft`; W10 remains `pilot-draft`.
