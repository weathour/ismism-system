# Feminism UltraQA Report

- status: PASS/CLEAR
- date: 2026-06-16 CST
- final positive suite: `.omx/tmp/feminism_full_validation_final.log`
- negative-test transcript: `.omx/tmp/feminism_negative_tests.log`
- query smoke transcript: `.omx/tmp/feminism_query_smoke.log`

## Positive validation coverage

The final suite passed:

- `python3 -m py_compile` for feminism/query and shared validators.
- `ruff check` and `pyright` for feminism/query plus Universal A/B validators.
- `validate_feminism_theme.py --final`.
- global W3/W5/W10 validators and feminism W3/W5 batch validators.
- Master-Spec validator.
- Universal A/B, AI, Chinese Philosophy, Religion, Time-Death, and Capitalism theme validators.
- W4 level 1/2/3/4 validators.
- `git diff --check`.
- protected-corpus diff check: `test -z "$(git diff --name-only -- split_md split_md_clean)"`.

## Negative tests

Hermetic temp-copy tests passed as intended:

1. corrupt feminism evidence quote -> feminism final validator failed with exact-substring error;
2. blank feminism evidence quote -> feminism final validator failed with empty-quote error;
3. mark W3 feminism record non-draft -> W3 batch validator failed;
4. mark W5 feminism record non-draft -> W5 batch validator failed;
5. break W10 feminism evidence quote -> W10 validator failed;
6. unknown synthesis evidence marker -> feminism final validator failed;
7. mutate `split_md_clean/` in temp copy -> protected-corpus sha check failed;
8. promote `excluded-keyword-only` manifest row to `core` -> feminism final validator failed.

All temp mutations were restored before final pass checks in the temp copy. The main tree was not mutated by the negative harness.
