# 符号学—语言—解释学 Theme Package Layer

- slug: semiotics-language-hermeneutics
- 中文名：符号学—语言—解释学
- status: Field 3 theme package layer, draft-linked and validator-backed
- date: 2026-06-18
- manifest: `semiotics-language-hermeneutics-row-manifest.jsonl` (36 reviewed rows)
- evidence bank: `semiotics-language-hermeneutics-evidence-bank.jsonl` (58 exact quote records)
- concept/relation/close-reading batches: deferred in this run
- validator: `python3 tools/validate/themes/semiotics_language_hermeneutics.py --repo . --final`
- query helper: `python3 tools/query/themes/semiotics_language_hermeneutics.py 符号学 --limit 3`

不是符号学/语言学百科，也不是把所有“语言/文本/符号/意义”词频都收编为结构主义。

## Central question

ISMISM 如何把符号学、结构主义、后结构主义、差异辩证法与解释学组织为语言、文本、话语、意义生成与理解条件的问题？

## Files
- `semiotics-language-hermeneutics-row-manifest.jsonl`
- `semiotics-language-hermeneutics-evidence-bank.jsonl`
- `semiotics-language-hermeneutics-taxonomy.md`
- `semiotics-language-hermeneutics-concept-relation-notes.md`
- `semiotics-language-hermeneutics-synthesis.md`

## Current metrics

- reviewed rows: 36
- evidence quotes: 58
- role counts: {"context": 1, "bridge": 10, "excluded": 3, "core": 22}
- taxonomy class counts: {"semiotics-overview-review": 3, "semiotics-language-bridge": 10, "excluded-keyword-only": 3, "structuralist-sign-system": 5, "poststructuralist-discourse-text": 5, "dialectics-of-difference": 5, "hermeneutics-understanding": 5}

## Query examples

- python3 tools/query/themes/semiotics_language_hermeneutics.py 符号学 --limit 3
- python3 tools/query/themes/semiotics_language_hermeneutics.py --row 254
- python3 tools/query/themes/semiotics_language_hermeneutics.py --class structuralist-sign-system --limit 3

## Interpretation rules

1. Start from the row manifest, then inspect exact quotes in the evidence bank.
2. Treat bridge rows as bridge evidence only, not as full ownership transfer.
3. Concept/relation/close-reading batches are deferred and must remain draft/pilot-draft if later added.
4. Do not import external encyclopedia claims or current-event/professional-advice claims into this theme.
