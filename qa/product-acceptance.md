# Product Acceptance QA

- status: PASS
- acceptance status: CLEAR
- acceptance target: GitHub-ready product repository with no public construction-era residue, preserved corpus integrity, working query and validation entrypoints.

## UltraQA source

Final UltraQA verifier: native test-engineer agent `019ed49a-b232-7300-ba78-064bf5e97f6f`.

## Required gates

- Product contract validation: PASS.
- Corpus byte-integrity validation: PASS.
- Full validation suite: PASS.
- Social-topic route smoke: PASS.
- Representative query smoke: PASS.
- Ingest temp-run smoke: PASS.
- Segment index regeneration smoke: PASS.
- Public residue scan: PASS.
- `git diff --check` / `git diff --cached --check`: PASS.

## Acceptance evidence

- `python3 tools/validate/library_contract.py --repo .` passed with `files=23/23`, `segments=363`, `concepts=1676`, `relations=1044`, `close_reading=741`, `themes=18`, `residue=0`, `errors=0`.
- `python3 tools/validate/library_contract.py --repo . --residue-only` passed with `residue=0`.
- `python3 tools/ismism.py validate all` passed across corpus, concepts, positions, relations, close-reading, product contract, social topics, and all theme validators.
- `python3 tools/query/social_topics.py --smoke-all --limit 1` passed with `routes=30` and `failures=0`.
- Representative query smokes exited successfully for social topic, relation, position, and row-trace lookups.
- `git ls-files --others --exclude-standard | wc -l` returned `0` before acceptance.
- Old tracked roots are absent from the release state.

## Residual note

`git diff --check` and `git diff --cached --check` exited clean. Git may print a non-fatal rename-limit warning because this refactor intentionally moves a large number of files into the productized layout.
