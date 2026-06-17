# AI Theme Theme Package Layer

- status: pilot-draft theme package layer
- created: 2026-06-15 CST
- scope: AI / VR / 智能 / 算法 / 机器人 theme across 60 candidate rows
- source discipline: corpus evidence and `corpus/clean-markdown` quotes remain authoritative; this directory is an index/synthesis surface.

## Files

| File | Function |
|---|---|
| `ai-row-manifest.jsonl` | 60-row candidate manifest with row/segment/path metadata, keyword hits, class, absorption state, and recommended action. |
| `ai-evidence-bank.jsonl` | 208 exact-substring quotes from declared clean files. |
| `ai-taxonomy.md` | Controlled AI theme axes and row/evidence links. |
| `ai-synthesis.md` | Claim-level synthesis with concept/relation/close-reading/evidence links. |
| `ai-concept-relation-batch-notes.md` | Batch note for draft concept/relation AI additions. |
| `README.md` | This usage protocol. |

## Counts

- manifest rows: 60
- core rows: 28 (`13–18`, `342–363`)
- quote-bank records: 208
- AI concept draft senses: 37 (`batch_id=concept-AI-2026-06-15`)
- AI relation draft relations: 30 (`batch_id=relation-AI-2026-06-15`)
- AI close-reading rows/cards: 28 rows / 28 AI cards including existing `cr:proc:0363:ai-regeneration`

## Common queries

```bash
python3 tools/query/themes/ai.py AI身体化
python3 tools/query/themes/ai.py 强AI
python3 tools/query/themes/ai.py AI可朽性
python3 tools/query/themes/ai.py --row 360
python3 tools/query/themes/ai.py --class ai-body-memory-language
```

## Interpretation rules

1. Start from `ai-row-manifest.jsonl` to identify rows and class.
2. Use `ai-evidence-bank.jsonl` for exact source quotes.
3. Use concept senses for terms and relation relations for claim-to-claim movement.
4. Use close-reading cards for close-reading argument/process/case structure.
5. Do not treat AI/VR speculation as a real-world engineering fact.
6. Do not promote AI concept/relation records out of `draft` without separate review.

## Fast answers

- “AI身体化在哪些 row？” → rows 353–358, especially concept `term:AI身体化:s01`, `term:AI substance:s01`, `term:AI秘密间性:s01`, `term:AI语音:s01`; query `AI身体化`.
- “强AI/弱AI如何区分？” → rows 360–361; concept `term:强AI:s01`, `term:弱AI:s01`, relation `rel:ai-theme:019`, close-reading `cr:proc:0360:ai-education-strong-weak`.
- “AI可朽性与再生证据链是什么？” → rows 362–363; concept `term:AI可朽性:s01`, `term:AI再生:s01`, relation `rel:ai-theme:030`, close-reading `cr:proc:0362:ai-mortality-memory` and `cr:proc:0363:ai-regeneration`.
