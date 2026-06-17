# UltraQA Report — Chinese Philosophy Maximum Absorption

- date: 2026-06-15 CST
- batch_id: CHINESE-PHILOSOPHY-MAX-2026-06-15
- status: PASS
- cycle_count: 2

## Goal and success criteria

- Goal: adversarially verify that the Chinese Philosophy maximum absorption layer is queryable, traceable, validator-covered, and safely integrated without mutating `split_md/` or `split_md_clean/`.
- Stop condition: Chinese theme validator, W10 validator, W3/W5/W4/master validators, query smoke test, exact-quote checks, taxonomy/bad-quote/unresolved-marker/duplicate-W10-quote negative checks, `git diff --check`, and protected-corpus diff all pass.
- Safety bounds applied: no corpus rewrite, no W3/W5 canonical promotion, no W10 promotion beyond `pilot-draft`, no external/production side effects; temporary negative-test edits restored before final validation.

## Scenario matrix

| ID | Scenario | Command/harness | Expected signal | Actual result | Status | Evidence |
|---|---|---|---|---|---|---|
| CH-UQA-001 | Valid Chinese theme validates end-to-end | `python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final` | PASS with 70 rows, 238 evidence records, 60 W3, 50 W5 | PASS | PASS | `.omx/tmp/final_validate_chinese_theme.txt` |
| CH-UQA-002 | Bad evidence quote is rejected | temporarily corrupt first evidence quote | non-zero FAIL naming quote substring error | FAIL observed as expected | PASS | `.omx/tmp/validate_chinese_bad_quote_negative.txt` |
| CH-UQA-003 | Duplicate taxonomy row is rejected | temporarily duplicate row 46 in another taxonomy section | non-zero FAIL naming duplicate ownership | FAIL observed as expected | PASS | `.omx/tmp/validate_chinese_taxonomy_negative.txt` |
| CH-UQA-004 | Unresolved synthesis markers are rejected | temporarily corrupt `ev:chphil:*`, `term:*:sNN`, `rel:chphil:*`, `w10:*`, and `row N` markers | non-zero FAIL naming every unknown marker family | FAIL observed as expected | PASS | `.omx/tmp/validate_chinese_all_synthesis_markers_negative.txt`; term-only regression: `.omx/tmp/validate_chinese_synthesis_marker_negative.txt` |
| CH-UQA-005 | Duplicate W10 evidence quote is rejected | temporarily duplicate a row 321 W10 `evidence_quotes` entry | non-zero FAIL naming duplicate evidence quote | FAIL observed as expected | PASS | `.omx/tmp/validate_w10_duplicate_quote_negative.txt` |
| CH-UQA-006 | W10 expanded cards/index remain valid | `python3 knowledge/scripts/validate_w10_absorption.py --repo .` | PASS | PASS, 77 cards | PASS | `.omx/tmp/final_validate_w10.txt` |
| CH-UQA-007 | W3/W5 batches remain draft and exact-quote valid | W3/W5 global + batch validators | PASS | PASS, W3=641/296 and W5=140 | PASS | `.omx/tmp/final_validate_w3*.txt`, `.omx/tmp/final_validate_w5*.txt` |
| CH-UQA-008 | Query helper retrieves traceable rows | `python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3` | row/quote/clean path output | rows 184, 289, 293 returned | PASS | `.omx/tmp/final_query_chinese_smoke.txt` |
| CH-UQA-009 | Existing repo contracts still pass | master + W4 L1/L2/L3/L4 validators | all PASS | all PASS | PASS | `.omx/tmp/final_validate_master.txt`, `.omx/tmp/final_validate_w4_l*.txt` |
| CH-UQA-010 | Protected source layers unchanged | `test -z "$(git diff --name-only -- split_md split_md_clean)"` | exit 0 | PASS | PASS | `.omx/tmp/final_protected_corpus_diff.txt` |
| CH-UQA-011 | Whitespace/conflict-marker check | `git diff --check` | exit 0 | PASS | PASS | `.omx/tmp/final_git_diff_check.txt` |

## Commands run

- `[0] python3 -m py_compile knowledge/scripts/validate_chinese_philosophy_theme.py knowledge/scripts/query_chinese_philosophy_theme.py knowledge/scripts/validate_w3_term_senses.py knowledge/scripts/validate_w10_absorption.py`
- `[0] python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final`
- `[0] python3 knowledge/scripts/validate_w10_absorption.py --repo .`
- `[0] python3 knowledge/scripts/validate_knowledge_contract.py --repo .`
- `[0] python3 knowledge/scripts/validate_w3_term_senses.py --repo .`
- `[0] python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-CHINESE-PHILOSOPHY-2026-06-15`
- `[0] python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 140 --require-type-min 2`
- `[0] python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-CHINESE-PHILOSOPHY-2026-06-15 --min-count 40`
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4`
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16`
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64`
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172`
- `[0] python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3`
- `[0] git diff --check`
- `[0] test -z "$(git diff --name-only -- split_md split_md_clean)"`
- `[expected non-zero] Chinese validator after temporary bad quote` — confirmed exact-substring rejection; file restored.
- `[expected non-zero] Chinese validator after temporary duplicate taxonomy row` — confirmed duplicate row ownership rejection; file restored.
- `[expected non-zero] Chinese validator after temporary unresolved synthesis markers` — confirmed unknown evidence, term, relation, W10, and row marker rejection; file restored. Term-only regression evidence also retained.
- `[expected non-zero] W10 validator after temporary duplicate `evidence_quotes` entry` — confirmed duplicate quote rejection; file restored.

## Fixes applied during QA

- Strengthened `validate_w3_term_senses.py` to reject duplicate `sense_id` values.
- Strengthened `validate_w10_absorption.py` to handle `toc_id: None` rows used by row 127/130 W10 cards.
- Strengthened `validate_w10_absorption.py` to reject duplicate `evidence_quotes` within a W10 card.
- Strengthened `validate_chinese_philosophy_theme.py --final` to resolve synthesis markers (`ev:chphil:*`, `term:*:sNN`, `rel:chphil:*`, `w10:*`, `row N`) instead of only checking marker presence.
- Repaired initial Chinese W5 relation boundary prose that used a W5-validator-forbidden phrase.
- Repaired quote extraction so Chinese theme evidence and W10 cards use content lines rather than clean-file metadata/header lines.
- Repaired stale Chinese synthesis W3 references after the Chinese W3 batch integrated with pre-existing draft senses.
- Repaired duplicate row 321/324 W10 evidence quotes and added concrete follow-up rows to `qa/w10-w3-w5-gap-followups.md`.
- Repaired query helper so keyword-only hits such as `实践论` are searchable through manifest `keyword_hits`.

## Residual risks

- Validators prove row/quote/schema/taxonomy traceability, not final philosophical correctness; theme synthesis remains a draft synthesis surface.
- W3/W5 Chinese records remain `draft`; W10 Chinese cards remain `pilot-draft`.
- Revolutionary/dialectical context rows are intentionally contextual and should not be overpromoted as core Chinese philosophy doctrine.

## Evidence

Primary evidence: `knowledge/qa/chinese-philosophy-absorption-audit.md`, `knowledge/qa/chinese-philosophy-evidence-claim-audit.md`, `.omx/tmp/final_validate_*.txt`, `.omx/tmp/final_query_chinese_smoke.txt`, `.omx/tmp/validate_chinese_bad_quote_negative.txt`, `.omx/tmp/validate_chinese_taxonomy_negative.txt`, `.omx/tmp/validate_chinese_synthesis_marker_negative.txt`, `.omx/tmp/validate_chinese_all_synthesis_markers_negative.txt`, `.omx/tmp/validate_w10_duplicate_quote_negative.txt`, `.omx/tmp/final_git_diff_check.txt`, `.omx/tmp/final_protected_corpus_diff.txt`.
