# Religion Problem Theme Package Layer

- status: pilot-draft theme package layer
- created: 2026-06-15 CST
- scope: 80-row Religion Problem / 宗教问题 theme across religious realism, sacred ideology, mysticism, Buddhist liberation, modern subjectivity, dogma, discipline, and practice.
- source discipline: corpus evidence and `corpus/clean-markdown` quotes remain authoritative; this directory is an index/synthesis surface.

## What this is not

This is not a neutral religious-studies encyclopedia. It absorbs how ISMISM handles religious realism, sacred order, faith/idol/spirit/fetishism, salvation, sacred love, and the transformation of religion into ideology and practice.

## Files

| File | Function |
|---|---|
| `religion-row-manifest.jsonl` | 80-row candidate manifest with row/segment/path metadata, keyword hits, class, absorption state, and recommended action. |
| `religion-evidence-bank.jsonl` | 226 exact-substring clean-text quote records. |
| `religion-taxonomy.md` | Controlled Religion Problem theme axes and row/evidence links. |
| `religion-synthesis.md` | Cross-field evidence-linked synthesis. |
| `religious-realism-synthesis.md` | Core 1-2 religious realism synthesis. |
| `sacred-ideology-and-practice-synthesis.md` | Bridge synthesis for secular sacred, mysticism, liberation, ideology, dogma, and practice. |
| `religion-concept-relation-batch-notes.md` | Batch note for draft concept/relation Religion additions. |

## Counts

- manifest rows: 80
- core rows: 22 (`24–45`)
- quote-bank records: 226
- Religion concept draft senses: 64 (`batch_id=concept-RELIGION-2026-06-15`)
- Religion relation draft relations: 51 (`batch_id=relation-RELIGION-2026-06-15`)
- Religion close-reading cards: 45 (`batch_id=close-reading-RELIGION-2026-06-15`)

## Common queries

```bash
python3 tools/query/themes/religion.py 宗教 --limit 3
python3 tools/query/themes/religion.py 偶像 --limit 3
python3 tools/query/themes/religion.py 神爱 --limit 3
python3 tools/query/themes/religion.py --row 34
python3 tools/query/themes/religion.py --class buddhist-liberation-bridge
```

## Interpretation rules

1. Start from `religion-row-manifest.jsonl` to identify row and theme class.
2. Use `religion-evidence-bank.jsonl` for exact source quotes.
3. Use Religion concept senses for terms and Religion relation relations for movement claims.
4. Use close-reading cards for close-reading argument/process/case structure.
5. Do not promote concept/relation records out of `draft`; do not promote close-reading out of `pilot-draft`.
6. Do not classify every occurrence of `神`, `精神`, `道`, `爱`, or `意识形态` as core; use `theme_class` and quote roles.
