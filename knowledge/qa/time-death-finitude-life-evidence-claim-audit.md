# Time-Death-Finitude-Life Evidence-Claim Audit

- date: 2026-06-15 CST
- status: PASS
- purpose: verify that the new synthesis layer does not make independent claims without trace markers.

## Claim-marker discipline

Every `- claim:` line in the three synthesis files is checked by `validate_time_death_theme.py --final` for at least one valid marker family:

- `ev:tdlife:NNNN:NN`
- `term:*:sNN`
- `rel:tdlife:NNN`
- `w10:arg|proc|case:NNNN:*`
- `row N`

Files checked:

- `knowledge/themes/time-death-finitude-life/time-death-finitude-life-synthesis.md`
- `knowledge/themes/time-death-finitude-life/life-body-immortality-synthesis.md`
- `knowledge/themes/time-death-finitude-life/historical-time-and-practice-synthesis.md`

## Adversarial evidence

- Unknown synthesis marker negative test: `.omx/tmp/validate_time_death_synthesis_unknown_marker_negative.txt` rejected `ev:tdlife:9999:99`.
- Bad quote negative test: `.omx/tmp/validate_time_death_bad_quote_negative.txt` rejected a non-exact quote.
- Duplicate taxonomy row negative test: `.omx/tmp/validate_time_death_taxonomy_duplicate_negative.txt` rejected duplicate row ownership.
- Duplicate W10 quote negative test: `.omx/tmp/validate_w10_time_death_duplicate_quote_negative.txt` rejected repeated `evidence_quotes`.
- Malformed W3 row-reference negative test: `.omx/tmp/validate_time_death_w3_bad_row_negative.txt` rejected a non-integer Time-Death `source_segments[].row_id`.
- Malformed W5 row-reference negative test: `.omx/tmp/validate_time_death_w5_bad_row_negative.txt` rejected a non-integer Time-Death `evidence_segment[].row_id`.
- Stale navigation negative test: `.omx/tmp/validate_time_death_stale_readme_negative.txt` rejected an old root README `--min-count 191` marker.

## Verdict

PASS. The theme syntheses are evidence-linked maps over the manifest/evidence/W3/W5/W10 layers; they are not independent truth sources above clean text.
