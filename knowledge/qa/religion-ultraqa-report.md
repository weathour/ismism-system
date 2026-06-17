# UltraQA Report — Religion Problem Maximum Absorption

- date: 2026-06-15 CST
- batch_id: RELIGION-THEME-MAX-2026-06-15
- status: PASS/CLEAR
- mode: docs-only / knowledge-layer UltraQA substitute under Autopilot lifecycle
- positive transcript: `.omx/tmp/religion_final_validation_suite.txt`
- negative transcripts: `.omx/tmp/validate_religion_bad_quote_negative.txt`, `.omx/tmp/validate_religion_taxonomy_negative.txt`, `.omx/tmp/validate_religion_synthesis_marker_negative.txt`, `.omx/tmp/validate_w10_religion_duplicate_quote_negative.txt`

## Positive validation matrix

| Check | Command | Result |
|---|---|---|
| Python syntax | `python3 -m py_compile knowledge/scripts/validate_religion_theme.py knowledge/scripts/query_religion_theme.py knowledge/scripts/validate_w3_term_senses.py knowledge/scripts/validate_w10_absorption.py` | PASS |
| Religion final validator | `python3 knowledge/scripts/validate_religion_theme.py --repo . --final` | PASS: 80 rows, 226 evidence, 64 W3, 51 W5, 45 W10 |
| W10 validator | `python3 knowledge/scripts/validate_w10_absorption.py --repo .` | PASS: 122 cards |
| AI regression | `python3 knowledge/scripts/validate_ai_theme.py --repo . --final` | PASS |
| Chinese Philosophy regression | `python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final` | PASS |
| Master spec | `python3 knowledge/scripts/validate_knowledge_contract.py --repo .` | PASS |
| W3 global + Religion batch | `python3 knowledge/scripts/validate_w3_term_senses.py --repo .`; `--batch-id W3-RELIGION-2026-06-15` | PASS: 705 global, 64 Religion batch |
| W5 global + Religion batch | `python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 191 --require-type-min 2`; `--batch-id W5-RELIGION-2026-06-15 --min-count 45` | PASS: 191 global, 51 Religion batch |
| W4 regression | levels 1/2/3/4 expected 4/16/64/172 | PASS |
| Query smoke | `query_religion_theme.py 宗教 --limit 3`; `query_religion_theme.py 偶像 --limit 3` | PASS |
| Whitespace diff | `git diff --check` | PASS |
| Corpus protection | `test -z "$(git diff --name-only -- split_md split_md_clean)"` | PASS |

## Adversarial/negative validation matrix

| Scenario | Expected failure | Result |
|---|---|---|
| Broken Religion evidence quote | `validate_religion_theme.py --final` rejects non-exact quote | PASS: failed with `quote not exact substring` |
| Duplicate taxonomy row ownership | Religion validator rejects row in two classes | PASS: failed with `row 24 appears in multiple theme nodes` |
| Unknown synthesis markers | Religion validator rejects unknown ev/term/rel/w10/row markers | PASS: failed on all unknown marker families |
| Duplicate W10 evidence quote | W10 validator rejects duplicate card evidence | PASS: failed with `duplicate evidence quote` |

All temporary negative edits were restored, and positive validators passed after restoration.

## Final verdict

PASS/CLEAR. The Religion Problem layer meets the requested maximum-absorption gates without corpus edits, W3/W5 promotion, or stale planning-only handoff state.
