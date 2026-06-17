# UltraQA Report — W10 Further Absorption Pilot

- date: 2026-06-15 CST
- batch_id: W10-PILOT-B1-2026-06-15
- status: PASS
- cycle_count: 1

## Goal and success criteria

- Goal: adversarially verify that the W10 pilot layer, validator, index, cards, and documentation preserve row/segment/quote traceability without mutating corpus or W3/W5 protected layers.
- Stop condition: W10 baseline validation, existing W1/W3/W4/W5/master validators, adversarial validator fixtures, and protected-layer diff checks all pass with fixtures removed/restored.
- Safety bounds applied: no destructive cleanup, no corpus rewrite, no network/external side effects, temporary fixtures only, all temporary edits restored.

## Scenario matrix

| ID | User/attacker model | Scenario | Command/harness | Expected signal | Actual result | Status | Evidence | Cleanup |
|---|---|---|---|---|---|---|---|---|
| UQA-001 | normal maintainer | Valid W10 batch validates | `python3 knowledge/scripts/validate_w10_absorption.py --repo .` | PASS, 5 cards, 0 errors | PASS, 5 cards, type counts argument=1/process=2/case=2 | PASS | validator output | none needed |
| UQA-002 | malformed-card author | Extra card declares non-existent quote and no body `[q1]` mapping | `python3 ... --extra-card <temporary-fixture>` | non-zero FAIL | rejected exact quote-substring and body mapping | PASS | expected failure observed | fixture removed |
| UQA-003 | bypass attempt | Rogue markdown under W10 tree | temporary `knowledge/w10-absorption/rogue.*/*.md` then W10 validator | FAIL with unexpected W10 markdown | rejected | PASS | expected failure observed | fixture removed |
| UQA-004 | stale index editor | W10-looking card row outside Pilot cards table | temporary append to `index.md` | FAIL | rejected as row outside Pilot cards table | PASS | expected failure observed | index restored |
| UQA-005 | broken-link editor | Index display text points to real card but href target is broken | temporary href mutation in `index.md` | FAIL exact index validation | rejected | PASS | expected failure observed | index restored |
| UQA-006 | malformed-table editor | Malformed row inside Pilot cards table | temporary malformed table row | FAIL strict table parsing | rejected | PASS | expected failure observed | index restored |
| UQA-007 | quote-padding author | Evidence Quote section contains `[q5]`, but substantive body omits `[q5]` | temporary removal from Lacan card body | FAIL missing body ref | rejected | PASS | expected failure observed | card restored |
| UQA-008 | invalid metadata author | Repo card has non-integer `row_id` | temporary `row_id: not-an-int` in row 76 card | FAIL without traceback | structured FAIL: row_id not integer / cannot build expected index entry | PASS | expected failure observed | card restored |
| UQA-009 | regression maintainer | Existing knowledge validators still pass | master/W1/W3/W4/W5 validators | all PASS | all PASS | PASS | command outputs | none needed |
| UQA-010 | integrity auditor | Protected corpus/W3/W5 layers untouched | `git diff --name-only -- split_md split_md_clean knowledge/lexicon knowledge/relations` | empty output | empty output | PASS | protected diff check | none needed |
| UQA-011 | misleading success skeptic | Do not trust success text without exit status | compile/ruff/pyright/W10 commands checked by shell exit codes | zero exits required for PASS | zero exits for final positive commands; expected-fail fixtures checked by non-zero exits | PASS | command exit status and output | none needed |

## Commands run

- `[0] python3 -m py_compile knowledge/scripts/validate_w10_absorption.py` — syntax check.
- `[0] ruff check knowledge/scripts/validate_w10_absorption.py` — lint check.
- `[0] pyright knowledge/scripts/validate_w10_absorption.py` — static type check.
- `[0] python3 knowledge/scripts/validate_w10_absorption.py --repo .` — W10 validator baseline.
- `[0] python3 knowledge/scripts/validate_knowledge_contract.py --repo .` — W1–W9 aggregate regression.
- `[0] python3 knowledge/scripts/validate_w1_manifests.py` — W1 manifest regression.
- `[0] python3 knowledge/scripts/validate_w3_term_senses.py --repo .` — W3 draft term-sense regression.
- `[0] python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2` — W5 draft relation regression.
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4` — W4 L1 regression.
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16` — W4 L2 regression.
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64` — W4 L3 regression.
- `[0] python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172` — W4 L4 regression.
- `[0] git diff --check` — whitespace conflict check.
- `[0] git diff --name-only -- split_md split_md_clean knowledge/lexicon knowledge/relations` — protected-layer diff check; empty output required.
- `[expected non-zero]` adversarial W10 fixtures listed in the scenario matrix.

## Failures found

No unresolved product/schema failures remain. Expected-fail adversarial fixtures confirmed that the validator rejects malformed cards, unknown W10 markdown, stale/malformed index rows, broken hrefs, missing body quote refs, and bad `row_id` metadata.

## Fixes applied

- Strengthened `validate_w10_absorption.py` for unknown markdown, exact index display/href matching, body quote-reference coverage, strict Pilot table parsing, invalid `row_id` structured failures, and `w3_w5_gap_review` validation.
- Added `knowledge/qa/w10-w3-w5-gap-followups.md` so W10 pilot discoveries feed back into W3/W5 review rather than bypassing them.
- Updated W10 audit/log/navigation docs to record validator scope and protected-layer boundaries.

## Cleanup and rollback

- Temporary malformed-card fixture removed.
- Temporary rogue W10 markdown removed.
- Temporary `index.md` mutations restored.
- Temporary Lacan-card and row-76-card mutations restored.
- No child processes, external services, or persistent test harnesses remain.
- Intentional tracked changes are the W10 pilot layer, validator/templates, QA docs, and navigation/resume docs.

## Residual risks

- W10 semantic fit still requires scholar/agent review per batch; validators prove structure and quote traceability, not philosophical correctness.
- W10 remains `pilot-draft`; it must not be treated as canonical replacement for corpus/manifests/W2/W3/W5.
- Future batches should continue small-batch expansion and keep `w3_w5_gap_review` current.

## Evidence

Primary evidence is in this report, `knowledge/qa/w10-pilot-audit.md`, the W10 validator output, existing validator outputs, and the empty protected-layer diff check.
