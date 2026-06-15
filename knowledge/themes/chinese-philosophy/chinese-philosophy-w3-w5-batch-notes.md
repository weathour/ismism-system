# Chinese Philosophy W3/W5 Batch Notes

- created: 2026-06-15 CST
- W3 batch_id: `W3-CHINESE-PHILOSOPHY-2026-06-15`
- W5 batch_id: `W5-CHINESE-PHILOSOPHY-2026-06-15`
- W3 records planned/appended: 60
- W5 relations planned/appended: 50
- status: draft only; no canonical promotion

## Scope

The batch covers the exact 70-row Chinese Philosophy manifest and gives every core non-context row W3 and W5 coverage. Revolutionary/dialectical context rows are partly W3-covered and retained in manifest/evidence/taxonomy for context rather than forced into core status.

## Discipline

- Quotes are exact substrings of declared `split_md_clean` files.
- W3 records use `status=draft` and `schema_version=w3.term-sense.v0.1`.
- W5 records use existing controlled relation types and `status=draft`.
- Relation prose is row-bound and avoids over-strong universal claims.

## Validation

```bash
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-CHINESE-PHILOSOPHY-2026-06-15
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-CHINESE-PHILOSOPHY-2026-06-15 --min-count 50
```
