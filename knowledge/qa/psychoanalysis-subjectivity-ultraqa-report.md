# Psychoanalysis-Subjectivity UltraQA Report

- status: PASS/CLEAR
- date: 2026-06-16
- positive verification log: `/tmp/psycho-full-verify-final-3.log`
- negative-test log: `/tmp/psycho-negative-tests.log`
- negative scenarios passed in temp copy `/tmp/ismism-psycho-neg.uJLtfo`:
  1. corrupted `psychoanalysis-subjectivity-evidence-bank.jsonl` quote failed with `quote_not_found`, then restored and passed;
  2. W3 psychoanalysis-subjectivity record marked non-draft failed with `non_draft_status`, then restored and passed;
  3. W5 psychoanalysis-subjectivity record marked non-draft failed with `non_draft_status`, then restored and passed;
  4. W10 psycho-subj card quote corruption failed with `evidence quote not found`, then restored and passed;
  5. unknown synthesis marker `ev:psycho-subj:9999:99` failed theme validation, then restored and passed;
  6. temp-copy `split_md_clean/` mutation failed protected-corpus check, then restored and passed;
  7. `excluded-keyword-only` row misclassified as `core` failed final validator policy, then restored and passed.
  8. stale `Current latest checkpoint — Universal Absorption Phase B` marker in `README.md` failed final validator semantic-current checks, then restored and passed.
- final restored temp-copy checks passed for theme final, W3 batch, W5 batch, and W10 validator.
- delivered metrics exceed conservative target: 120 manifest rows / 387 evidence quotes / 89 W3 / 75 W5 / 58 W10.
