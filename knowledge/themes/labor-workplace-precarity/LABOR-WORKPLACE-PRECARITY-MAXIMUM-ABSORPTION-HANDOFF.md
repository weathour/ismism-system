# Labor / Workplace / Precarity / Involution Maximum Absorption Handoff

- date: 2026-06-16 CST
- status: G004 closure handoff
- path: `knowledge/themes/labor-workplace-precarity/`
- protocol: `knowledge/references/social-phenomena-diagnostic-protocol.md`

## Completed artifacts

- `README.md`
- `labor-workplace-precarity-row-manifest.jsonl` — 98 reviewed rows
- `labor-workplace-precarity-evidence-bank.jsonl` — 247 exact-normalizable quotes
- `labor-workplace-precarity-taxonomy.md`
- `labor-workplace-precarity-w3-w5-batch-notes.md`
- `labor-workplace-precarity-synthesis.md`
- `work-discipline-and-involution-synthesis.md`
- `production-relations-and-practice-synthesis.md`
- `validate_labor_workplace_precarity_theme.py`
- `query_labor_workplace_precarity_theme.py`

## Added draft/pilot assets

- W3 batch: `W3-LABOR-WORKPLACE-PRECARITY-2026-06-16` — 45 draft senses
- W5 batch: `W5-LABOR-WORKPLACE-PRECARITY-2026-06-16` — 40 draft relations
- W10: 30 Labor pilot-draft cards

## Current global counts after Labor

- W3: 1271 draft senses / 866 terms
- W5: 684 draft relations / 12 relation types
- W10: 471 pilot-draft cards / 3 card types
- W3 rows: 336
- W5 rows: 280
- W10 rows: 293
- full W3+W5+W10 overlap: 253 rows
- W1/W2-only: 9 rows

## Validation commands

```bash
python3 knowledge/scripts/validate_labor_workplace_precarity_theme.py --repo . --final
python3 knowledge/scripts/validate_w3_term_senses.py --repo . --batch-id W3-LABOR-WORKPLACE-PRECARITY-2026-06-16
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --batch-id W5-LABOR-WORKPLACE-PRECARITY-2026-06-16 --min-count 40
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 684 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
```

## Boundaries

No `split_md/` or `split_md_clean/` edits. W3/W5 remain `draft`; W10 remains `pilot-draft`; External generated material is outside the project contract.
