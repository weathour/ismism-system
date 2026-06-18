# Field 3 Theme Absorption Acceptance Evidence

- status: opened during G001; final evidence to be appended through G005
- date: 2026-06-18

## Planned evidence slots

- G001 preflight and scope charter evidence: reviews/field3-theme-absorption-review.md
- G002 theme package file list and counts: pending
- G003 query helper and validator outputs: pending
- G004 discovery/suite synthesis query smokes: pending
- G005 final validators, negative checks, code review, ultraqa: pending

## G001 evidence

- python3 tools/ismism.py validate core: PASS (see review artifact baseline block)
- donor theme validator smokes: PASS (see review artifact donor block)
- corpus raw/clean edit boundary: no intended edits
## G002 evidence

Theme package assets generated for four mature Field 3 themes.

Counts:
- phenomenology: manifest 36 rows, evidence 58 exact quotes
- german-idealism-dialectics: manifest 36 rows, evidence 58 exact quotes
- existentialism-ethics-meaning: manifest 36 rows, evidence 58 exact quotes
- semiotics-language-hermeneutics: manifest 36 rows, evidence 58 exact quotes

Generic exact-quote theme validation before specialized validators:
- python3 tools/lib/theme_validation.py phenomenology --repo . --final: PASS
- python3 tools/lib/theme_validation.py german-idealism-dialectics --repo . --final: PASS
- python3 tools/lib/theme_validation.py existentialism-ethics-meaning --repo . --final: PASS
- python3 tools/lib/theme_validation.py semiotics-language-hermeneutics --repo . --final: PASS

Protected corpus diff after G002: empty.

## G003 evidence

Created shared query and validation utilities plus per-theme query/validator wrappers.

Changed tool surfaces:
- tools/lib/theme_query.py
- tools/lib/field3_theme_validation.py
- tools/internal/query_phenomenology_theme.py
- tools/internal/query_german_idealism_dialectics_theme.py
- tools/internal/query_existentialism_ethics_meaning_theme.py
- tools/internal/query_semiotics_language_hermeneutics_theme.py
- tools/query/themes/phenomenology.py
- tools/query/themes/german_idealism_dialectics.py
- tools/query/themes/existentialism_ethics_meaning.py
- tools/query/themes/semiotics_language_hermeneutics.py
- tools/validate/themes/phenomenology.py
- tools/validate/themes/german_idealism_dialectics.py
- tools/validate/themes/existentialism_ethics_meaning.py
- tools/validate/themes/semiotics_language_hermeneutics.py

Verification captured in qa/field3-theme-absorption/g003-smokes.txt:
- py_compile: PASS
- all four specialized theme validators: PASS
- keyword/row/class query smoke for all four themes: PASS
- protected corpus diff after G003: empty

## G004 evidence

Discovery and suite synthesis completed.

Added:
- library/syntheses/field-3-idealism-theme-suite-synthesis.md

Updated:
- docs/query-guide.md: added four Field 3 direct theme query examples
- docs/status.md: theme dossier count updated to 23
- README.md: current library counts updated from validation evidence

Verification:
- all four specialized theme validators: PASS after synthesis/docs updates
- four suite query smokes captured in qa/field3-theme-absorption/g004-query-smokes.txt: PASS
- social-topic routing intentionally unchanged
- protected corpus diff after G004: empty

## G005 final evidence

Final QA after cleanup passed. Durable outputs:
- qa/field3-theme-absorption/final-validation-output.txt
- qa/field3-theme-absorption/negative-tests.py
- qa/field3-theme-absorption/ai-slop-cleaner-report.md
- qa/field3-theme-absorption/final-query-phenomenology.txt
- qa/field3-theme-absorption/final-query-german.txt
- qa/field3-theme-absorption/final-query-existentialism.txt
- qa/field3-theme-absorption/final-query-semiotics.txt

Final validation summary:
- py_compile: PASS
- four specialized Field 3 theme validators: PASS
- four direct theme query smokes: PASS
- negative tests for corrupted quote, invalid class, duplicate taxonomy row, and missing README query reference: PASS, failures detected as expected
- ai-slop-cleaner/no-op report: PASS, no fallback-like findings
- concept/relation/close-reading layers: not edited in this Field 3 pass; full core/all validators still exercised existing layers
- python3 tools/ismism.py validate core: PASS
- python3 tools/ismism.py validate all: PASS, all 23 theme validators PASS
- python3 tools/validate/library_contract.py --repo . --residue-only: PASS residue=0
- git diff --check: PASS
- protected corpus diff: empty
- skill quick validation: PASS
- plugin validation: PASS

## Post-review fix evidence

Independent code review requested a static-diagnostic fix in `tools/lib/field3_theme_validation.py`. The fix added guarded row-id parsing before integer conversion and added an explicit no-match message in `tools/lib/theme_query.py`.

Post-fix validation is recorded in `qa/field3-theme-absorption/final-validation-output.txt`:
- targeted pyright: PASS, 0 errors
- py_compile: PASS
- four specialized validators: PASS
- validate core/all: PASS
- residue: PASS, 0
- git diff check: PASS
- protected corpus diff: empty


## Autopilot UltraQA acceptance evidence

- UltraQA cycle: PASS after 1 cycle.
- Scenario matrix: normal row/class queries, prompt-injection-like keyword, path-traversal-like class, zero-limit JSON, invalid row argparse rejection, negative validator sensitivity, flake rerun, all Field 3 validators, core/all validation, residue, diff check, protected corpus diff, dirty-worktree before/after.
- Evidence: `qa/field3-theme-absorption/ultraqa-report.md`; `qa/field3-theme-absorption/ultraqa-command-log.txt`.
- Protected corpus raw/clean diff: empty.
