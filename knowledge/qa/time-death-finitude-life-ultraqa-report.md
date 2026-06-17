# UltraQA Report — Time-Death-Finitude-Life Maximum Absorption

- date: 2026-06-15 CST
- batch_id: TIME-DEATH-FINITUDE-LIFE-MAX-2026-06-15
- status: PASS/CLEAR
- mode: docs-only / knowledge-layer UltraQA substitute under Autopilot lifecycle
- positive transcript: `.omx/tmp/time_death_final_validation_suite.txt`
- negative transcripts: `.omx/tmp/validate_time_death_bad_quote_negative.txt`, `.omx/tmp/validate_time_death_taxonomy_duplicate_negative.txt`, `.omx/tmp/validate_time_death_synthesis_unknown_marker_negative.txt`, `.omx/tmp/validate_w10_time_death_duplicate_quote_negative.txt`, `.omx/tmp/validate_time_death_w3_bad_row_negative.txt`, `.omx/tmp/validate_time_death_w5_bad_row_negative.txt`, `.omx/tmp/validate_time_death_stale_readme_negative.txt`

## Positive validation matrix

- Time-death final validator: PASS.
- W10 validator: PASS.
- AI / Chinese Philosophy / Religion regression validators: PASS.
- project knowledge contract repo-local validator: PASS.
- W3 global and time-death batch validators: PASS.
- W5 global and time-death batch validators: PASS.
- W4 L1–L4 validators: PASS.
- Query smoke tests for `时间`, `死亡`, `生命`, `永生`, `有限`: PASS.
- `git diff --check`: PASS.
- Protected corpus diff (`split_md`, `split_md_clean`): PASS.

## Adversarial/negative validation matrix

- Broken evidence quote rejected with `quote not exact substring`.
- Duplicate taxonomy row rejected with `appears in multiple theme nodes`.
- Unknown synthesis marker rejected with `unknown evidence marker`.
- Duplicate W10 quote rejected with `duplicate evidence quote`.
- Malformed Time-Death W3 `source_segments[].row_id` rejected with `bad row_id`.
- Malformed Time-Death W5 `evidence_segment[].row_id` rejected with `bad row_id`.
- Stale root README current-state marker rejected with `stale current-state marker`.
- All fixtures restored and positive time-death/W10 validators reran PASS.

## Final verdict

PASS/CLEAR for knowledge-layer QA. The remaining Autopilot gates are the independent code-review and verifier records, stored under `.omx/reviews/` after this report.
