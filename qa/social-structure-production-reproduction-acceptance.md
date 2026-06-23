# Social Structure / Production Reproduction Theme Acceptance

- date: 2026-06-23 CST
- acceptance target: validator-backed theme dossier for society/production/reproduction/institution analysis

## Acceptance criteria

- [x] Row manifest exists and is parseable.
- [x] Evidence bank exists and uses exact clean-text quotes.
- [x] README, taxonomy, concept/relation notes, main synthesis, and focused syntheses exist.
- [x] Query helper supports keyword, `--row`, `--class`, and `--limit`.
- [x] Validator wrapper exists.
- [x] The package remains direct-theme only and does not alter social-topic routing.
- [x] Targeted validator pass recorded after generation: `python3 tools/validate/themes/social_structure_production_reproduction.py --repo . --final --json` PASS, 153 manifest rows, 425 exact quote checks.
- [x] Query smoke pass recorded after generation: `python3 tools/query/themes/social_structure_production_reproduction.py 生产关系 --limit 4`, `--row 331`, and `--class production-relations-institutional-form --limit 3` returned expected row/evidence output.
- [x] Core validation pass recorded after generation: `python3 tools/ismism.py validate core` PASS; product contract reports themes=24 and residue=0.
