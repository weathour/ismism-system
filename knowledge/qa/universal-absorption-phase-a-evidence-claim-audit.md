# Universal Absorption Phase A Evidence-Claim Audit

- date: 2026-06-16 CST
- status: PASS / exact-substring and marker traceability checked by validator plus spot checks

## Validator-level checks

`knowledge/scripts/validate_universal_absorption_phase_a.py` checks gap-map row/path consistency, evidence exact-substring validity, W3/W5 batch counts and draft status, W10 Universal-A card coverage, synthesis marker validity, final metrics, and protected corpus SHA-256 checks.

## Spot-check matrix

| Claim surface | Marker(s) | Row evidence | Audit result |
|---|---|---|---|
| Apeiron/unboundedness source model | `E:univ-a-0099-01`, `T:term:阿派朗:s01`, `R:rel:universal-a:001`, `W10:w10:arg:0099:universal-phase-a` | row 99 clean text | PASS: marker IDs exist and quote exactness is validator-checked. |
| Zeno/motion paradox repair | `E:univ-a-0107-*`, `T:term:芝诺悖论:s01`, `W10:w10:proc:0107:universal-phase-a` | row 107 clean text | PASS: W3/W5/W10 all point to row 107 or adjacent declared target with exact evidence. |
| Logical atomism transformation | `E:univ-a-0159-01`, `T:term:逻辑原子主义:s01`, `R:rel:universal-a:013` | row 159 clean text | PASS: synthesis marker resolves; relation evidence exact. |
| Transcendental phenomenology repair | `E:univ-a-0190-*`, `T:term:先验现象学:s01`, `W10:w10:arg:0190:universal-phase-a` | row 190 clean text | PASS: W10 body maps [q1]–[q3] to same-row quotes. |
| Structural/language displacement | `E:univ-a-0257-01`, `E:univ-a-0260-01`, `E:univ-a-0270-01` | rows 257/260/270 clean text | PASS: synthesis uses only declared evidence/term/relation/card markers. |
| Everyday normality repair | `E:univ-a-0088-*`, `T:term:心理正常主义:s01`, `W10:w10:arg:0088:universal-phase-a` | row 88 clean text | PASS: row remains bounded to ISMISM internal ideology/normality function, not a clinical diagnosis. |

## Boundary findings

- No standalone external philosophy-history claims are introduced by the phase syntheses.
- Every synthesis marker uses a parseable `E:`, `T:`, `R:`, or `W10:` ID.
- W3/W5 remain draft and W10 remains pilot-draft.

## Negative traceability tests

Hermetic temp-copy tests confirmed that traceability checks fail for the intended reasons before restoration:

1. Corrupting one Phase-A evidence quote fails Universal-A exact-substring validation.
2. Marking one Phase-A W3 record non-draft fails the W3 batch validator.
3. Breaking a W10 evidence quote fails W10 validation.
4. Adding an unknown synthesis marker fails Universal-A marker validation.
5. Tampering with `split_md_clean/` in a temp copy fails the protected-corpus final check.

Evidence transcript: `.omx/tmp/universal_negative_tests.log`.
