# Close-reading Layer

Close-reading cards are row-bound interpretation records. They capture argument flow, process stages, and case positioning when a concept record or relation record is too small to preserve the evidence structure.

## Role in the library

- status: pilot-draft
- source boundary: every claim must remain tied to one corpus row unless `context_quotes` explicitly declares another row.
- evidence rule: every quoted passage must be an exact substring of `corpus/clean-markdown/`.
- promotion rule: close-reading does not promote concept or relation assets out of draft status.

## Card types

| Type | Directory | Captures |
|---|---|---|
| `close-reading-argument` | `arguments/` | claim target, argument steps, rhetoric boundary |
| `close-reading-process` | `processes/` | stages, transitions, preconditions, failure modes |
| `close-reading-case` | `cases/` | figure/school positioning, standard-view contrast, local reconstruction |

## Required fields

Each card declares `row_id`, `segment_id`, `toc_id`, `source_clean_path`, `evidence_quotes`, `rhetorical_register`, `concept_relation_gap_review`, `claim_core`, and `forbidden_use`. Body claims cite declared quotes with `[q1]` markers and must reference every declared quote.

## Validation

```bash
python3 tools/validate/close_reading.py --repo .
```

Use `library/close-reading/index.md` for the generated card index.
