# Task Routing

Route from user intent to the smallest evidence path that can answer the task.

## Query-first routes

| User intent | First command | Then read |
| --- | --- | --- |
| Explain a term or concept | `python3 tools/ismism.py query concept <term> --limit 5` | cited concept records, source rows, clean transcript paths |
| Traverse concept relations | `python3 tools/ismism.py query relation <term> --limit 5` | relation records and evidence rows |
| Locate a matrix position | `python3 tools/ismism.py query position <position-id>` | `library/positions/` card and cited segments |
| Trace one row | `python3 tools/ismism.py query trace <row-id> --limit 5` | returned clean transcript path and segment card |
| Analyze a social topic | `python3 tools/ismism.py query social <prompt> --limit 3` | routed theme evidence bank, synthesis, clean paths |
| Validate project state | `python3 tools/ismism.py validate core` | validator output; broaden only if needed |
| Validate all publication surfaces | `python3 tools/ismism.py validate all` plus plugin validation | `docs/validation.md` and plugin manifest |

## Multi-query analysis routes

For broad interpretation questions, combine queries instead of relying on one keyword.

1. Run a social route for the user-facing symptom or scenario.
2. Run concept queries for 2-4 central theoretical terms.
3. Run relation queries for the same central terms.
4. Use row trace on the highest-value rows before close interpretation.
5. Read exact clean transcript passages before making claims about wording or argumentative movement.

Example route for desire/alienation questions:

```bash
python3 tools/ismism.py query concept 欲望 --limit 5
python3 tools/ismism.py query concept 异化 --limit 5
python3 tools/ismism.py query relation 欲望 --limit 5
python3 tools/ismism.py query social 消费主义 --limit 3
```

## Direct theme helpers

Use direct theme helpers when the task names a specific theme dossier or when `query social` identifies the correct theme but more theme-local examples are needed.

```bash
python3 tools/query/themes/psychological_distress_social_symptom.py 焦虑 --limit 3
python3 tools/query/themes/consumption_desire_lifestyle.py 消费主义 --limit 3
python3 tools/query/themes/labor_workplace_precarity.py 内卷 --limit 3
```

## Fallback when a query misses

1. Try a synonym or shorter Chinese term.
2. Inspect `docs/query-guide.md` and `library/themes/` indexes.
3. Search only targeted library surfaces, for example `library/concepts/`, `library/relations/`, or one theme directory.
4. Report the miss as a library coverage gap if no evidence is found.

Do not fill a query miss with unsourced theory.
