# Capitalism UltraQA / Docs QA Report

- date: 2026-06-16
- status: PASS / CLEAR

## QA targets

- Validator-first scaling: dedicated validator added before relying on new syntheses.
- Query smoke: `资本主义`, `资本`, `生产关系`, `拜物教`, `金融`, `帝国主义`, `异化`, `消费`.
- Regression: AI, Chinese Philosophy, Religion, Time-Death, project knowledge contract, W3/W5/W10/W4 validators; pyright and ruff static diagnostics for touched Python scripts.
- Negative tests: quote corruption, taxonomy duplicate ownership, unknown synthesis marker, duplicate W10 quote, and rejected W10 placeholder close-reading text.
- Corpus protection: no `split_md/` or `split_md_clean/` diff.

## Result

PASS/CLEAR. Positive validation suite: `.omx/tmp/capitalism_positive_validation_suite.txt`. Hermetic negative tests ran in a temporary copied repo, failed for the intended reasons, restored cleanly inside the temp copy, and left matching before/after checksums for guarded main-tree files: `.omx/tmp/validate_capitalism_bad_quote_negative.txt`, `.omx/tmp/validate_capitalism_taxonomy_negative.txt`, `.omx/tmp/validate_capitalism_synthesis_marker_negative.txt`, `.omx/tmp/validate_w10_capitalism_duplicate_quote_negative.txt`, `.omx/tmp/validate_w10_capitalism_placeholder_negative.txt`. `git diff --check` and protected corpus diff both passed.

## Review-blocker repairs

- `validate_capitalism_theme.py --final` now enforces W3/W5 JSONL raw byte-prefix append-only preservation against `HEAD`, allowing only the Time-Death and Capitalism batch IDs as new lines in this working state.
- `validate_w10_absorption.py` now rejects the prior Capitalism placeholder phrase `限定本行资本主义功能的一个环节`.
- The final positive suite includes pyright and ruff when installed; both passed in the current environment.

- Hermetic fixture guard: `.omx/tmp/capitalism_negative_main_before.sha256` and `.omx/tmp/capitalism_negative_main_after.sha256` matched after the negative harness.
