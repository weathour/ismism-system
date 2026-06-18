# 生存论—伦理—意义 Theme Package Layer

- slug: existentialism-ethics-meaning
- 中文名：生存论—伦理—意义
- status: Field 3 theme package layer, draft-linked and validator-backed
- date: 2026-06-18
- manifest: `existentialism-ethics-meaning-row-manifest.jsonl` (36 reviewed rows)
- evidence bank: `existentialism-ethics-meaning-evidence-bank.jsonl` (58 exact quote records)
- concept/relation/close-reading batches: deferred in this run
- validator: `python3 tools/validate/themes/existentialism_ethics_meaning.py --repo . --final`
- query helper: `python3 tools/query/themes/existentialism_ethics_meaning.py 生存论 --limit 3`

不是存在主义文学史，也不是把所有“存在/自由/死亡/意义”词频都收编为生存论。

## Central question

ISMISM 如何把生存论、存在主义、虚无、自由、选择、伦理、本真和意义问题纳入现代反观念论与主体实践的诊断？

## Files
- `existentialism-ethics-meaning-row-manifest.jsonl`
- `existentialism-ethics-meaning-evidence-bank.jsonl`
- `existentialism-ethics-meaning-taxonomy.md`
- `existentialism-ethics-meaning-concept-relation-notes.md`
- `existentialism-ethics-meaning-synthesis.md`

## Current metrics

- reviewed rows: 36
- evidence quotes: 58
- role counts: {"context": 1, "excluded": 3, "bridge": 10, "core": 22}
- taxonomy class counts: {"existentialism-overview-review": 3, "excluded-keyword-only": 3, "existentialism-bridge": 10, "being-existence-ism": 5, "authentic-existence-choice": 5, "identity-existential-ethics": 5, "fictional-existence-meaning": 5}

## Query examples

- python3 tools/query/themes/existentialism_ethics_meaning.py 生存论 --limit 3
- python3 tools/query/themes/existentialism_ethics_meaning.py --row 232
- python3 tools/query/themes/existentialism_ethics_meaning.py --class being-existence-ism --limit 3

## Interpretation rules

1. Start from the row manifest, then inspect exact quotes in the evidence bank.
2. Treat bridge rows as bridge evidence only, not as full ownership transfer.
3. Concept/relation/close-reading batches are deferred and must remain draft/pilot-draft if later added.
4. Do not import external encyclopedia claims or current-event/professional-advice claims into this theme.
