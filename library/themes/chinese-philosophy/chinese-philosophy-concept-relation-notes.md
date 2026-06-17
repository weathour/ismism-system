# Chinese Philosophy concept/relation Batch Notes

- created: 2026-06-15 CST
- concept batch_id: `concept-CHINESE-PHILOSOPHY-2026-06-15`
- relation batch_id: `relation-CHINESE-PHILOSOPHY-2026-06-15`
- concept records planned/appended: 60
- relation relations planned/appended: 50
- status: draft only; no canonical promotion

## Scope

The batch covers the exact 70-row Chinese Philosophy manifest and gives every core non-context row concept and relation coverage. Revolutionary/dialectical context rows are partly concept-covered and retained in manifest/evidence/taxonomy for context rather than forced into core status.

## Discipline

- Quotes are exact substrings of declared `corpus/clean-markdown` files.
- concept records use `status=draft` and `schema_version=concept.term-sense.v0.1`.
- relation records use existing controlled relation types and `status=draft`.
- Relation prose is row-bound and avoids over-strong universal claims.

## Validation

```bash
python3 tools/validate/themes/chinese_philosophy.py --repo . --final
python3 tools/internal/validate_concepts.py --repo . --batch-id concept-CHINESE-PHILOSOPHY-2026-06-15
python3 tools/internal/validate_relations.py --repo . --batch-id relation-CHINESE-PHILOSOPHY-2026-06-15 --min-count 50
```
