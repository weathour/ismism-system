# Universal Absorption Phase A UltraQA Report

- date: 2026-06-16 CST
- status: PASS / CLEAR
- goal: adversarial QA for Universal-A artifacts, validators, exact evidence, negative tests, and protected corpus boundaries

## Scenario matrix

| ID | User/attacker model | Scenario | Command/harness | Expected signal | Actual result | Status | Cleanup |
|---|---|---|---|---|---|---|---|
| UQA-001 | normal maintainer | Full positive validator suite | final validation commands | all exit 0 | PASS in final suite | PASS | no temp files kept |
| UQA-002 | malformed evidence | Corrupt one Universal-A evidence quote in temp copy | temp-copy negative harness | universal validator exits non-zero with quote error | expected FAIL captured | PASS | temp copy removed |
| UQA-003 | draft discipline attacker | Mark one W3 Universal-A record non-draft in temp copy | W3 batch validator | exits non-zero with non_draft_status | expected FAIL captured | PASS | temp copy removed |
| UQA-004 | W10 evidence attacker | Duplicate/break W10 evidence quote in temp copy | W10 validator | exits non-zero with duplicate/exactness error | expected FAIL captured | PASS | temp copy removed |
| UQA-005 | marker injection attacker | Add unknown synthesis marker in temp copy | universal validator | exits non-zero unknown marker | expected FAIL captured | PASS | temp copy removed |
| UQA-006 | corpus tampering attacker | Modify split_md_clean in temp copy | universal final protected-corpus check | exits non-zero sha256 mismatch | expected FAIL captured | PASS | temp copy removed |
| UQA-007 | prompt-injection/misleading success | Query helper receives override-like input | query helper smoke | query is treated as inert text; no state mutation | PASS | PASS | no temp files |
| UQA-008 | dirty worktree guard | Check protected corpus diff after edits | `git diff --name-only -- split_md split_md_clean` | empty | PASS | PASS | N/A |
| UQA-009 | hung command guard | Validation commands run bounded by shell/tool timeouts | command suite | no unbounded wait | PASS | PASS | N/A |

## Commands run

- `[0] ruff check ...` and `[0] pyright ...` — lint/type diagnostics for Universal-A query/validator and prior-theme validator compatibility edits.
- `[0] python3 -m py_compile ...` — syntax/static compile check for Universal-A, W3/W5/W10, Time-Death, Capitalism, and query helper scripts.
- `[0] python3 knowledge/scripts/validate_universal_absorption_phase_a.py --repo . --final` — final Universal-A gap/evidence/W3/W5/W10/synthesis/metric/protected-corpus gate.
- `[0] python3 knowledge/scripts/validate_w10_absorption.py --repo .` — W10 index/card/evidence parity.
- `[0] python3 knowledge/scripts/validate_w3_term_senses.py --repo .` and `--batch-id W3-UNIVERSAL-A-2026-06-16` — global and Universal-A W3 gates.
- `[0] python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 382 --require-type-min 2` and Universal-A batch gate — global and Universal-A W5 gates.
- `[0] python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` — repository master-spec regression.
- `[0] validate_ai_theme.py`, `validate_chinese_philosophy_theme.py`, `validate_religion_theme.py`, `validate_time_death_theme.py`, `validate_capitalism_theme.py` with `--final` — prior theme independence regressions.
- `[0] validate_w4_position_cards.py` for L1/L2/L3/L4 — W4 regression.
- `[0] query_universal_absorption.py` smoke queries for `在场`, `形而上学`, `芝诺`, `逻各斯`, `实证主义`, `现象学`, `语言游戏`.
- `[0] git diff --check` and `[0] test -z "$(git diff --name-only -- split_md split_md_clean)"` — whitespace and protected-corpus checks.
- Evidence transcript: `.omx/tmp/universal_final_validation_suite.txt` ends with `FINAL_VALIDATION_SUITE_PASS`.
- Negative-test transcript: `.omx/tmp/universal_negative_tests.log` captures five intended failures and restored passing state.

## Failures found

- First query smoke exposed metadata/header quote selection; artifacts were regenerated with stricter quote selection and validators reran PASS.
- MASTER-SPEC initially caught a forbidden/clinical-context quote pattern in one evidence record; the quote was replaced with an exact row-specific clean-text substring and MASTER-SPEC reran PASS.
- Prior-theme final validators exposed stale global-marker assumptions after Universal-A changed repository totals; Time-Death now derives current global navigation markers from ledgers/W10 cards, Capitalism uses semantic append-only checks, and both reran PASS.

## Cleanup and rollback

- Temporary negative-test copies were removed.
- No generated harness was intentionally kept in the repository.
- Main tree protected corpus remained unchanged.

## Docs QA result

PASS / CLEAR. Required state, handoff, distribution, navigation, log, operator-skill, audit, claim-audit, UltraQA, ai-slop-cleaner, independent code-review, and handoff files are present and updated with Universal-A metrics; no stale planning-only status remains in the phase handoff.

## Residual risks

- Universal-A is broad and draft/pilot-draft; future phases should review remaining 49 W1/W2-only rows and should not promote W3/W5/W10 records without a separate audit.
