# Religion Problem Absorption Audit

- date: 2026-06-15 CST
- status: PASS
- scope: 80-row Religion Problem / 宗教问题 maximum absorption layer
- validation transcript: `.omx/tmp/religion_final_validation_suite.txt`
- negative-test transcript set: `.omx/tmp/validate_religion_bad_quote_negative.txt`, `.omx/tmp/validate_religion_taxonomy_negative.txt`, `.omx/tmp/validate_religion_synthesis_marker_negative.txt`, `.omx/tmp/validate_w10_religion_duplicate_quote_negative.txt`

## Coverage

| Layer | Count |
|---|---:|
| manifest rows | 80 |
| core 1-2 rows | 22 / 22 |
| exact quote-bank records | 226 |
| W3 Religion draft senses | 64 |
| W5 Religion draft relations | 51 |
| Religion W10 pilot-draft cards | 45 |
| syntheses | 3 |

## Scope confirmation

- Core rows 24–45 are all classified in `knowledge/themes/religion/religion-row-manifest.jsonl` and each has Religion W10 coverage.
- The manifest preserves `row_id`, `segment_id`, `toc_id`, `title`, `clean_md_path`, theme class, absorption status, and action notes.
- The quote bank preserves exact `split_md_clean/` substrings; final validator reports `validate_religion_theme: PASS` with 226 evidence records.
- W3 and W5 additions remain draft-only (`W3-RELIGION-2026-06-15`, `W5-RELIGION-2026-06-15`).
- W10 cards remain pilot-draft close-reading aids below corpus/W1–W5 truth layers.

## Excluded seed candidates

The requested 65–80 row manifest cap required excluding a small set of weak keyword candidates after clean-text review:

- row 6: keyword hits are evolutionary/scientific context rather than Religion Problem function.
- row 7: scientific consumptionism has no stable sacred/faith/idol function after clean-text review.
- row 75: review row retained outside manifest because religion terms are broad review-context only.
- row 91: vulgarism row is ideology-noise for this batch, no distinct sacred mechanism selected.
- row 93: crudeness row has profanity/ideology context but no Religion Problem function selected.
- row 195: phenomenology row has theological vocabulary only as background; not selected for 80-row cap.

## Boundary audit

- `split_md/` and `split_md_clean/` are protected source layers and were not edited.
- external material was not promoted to a truth layer.
- Chinese Philosophy overlap is handled through Religion-specific function and reuse rationale, not by treating Chinese Philosophy as source truth.
- The Religion layer is a query/synthesis/index surface for ISMISM’s treatment of religious realism, sacred order, faith/idol/spirit/fetishism, salvation, ideology, and practice transformation; it is not an external religious-studies encyclopedia.

## Validator evidence

Required positive checks passed on 2026-06-15 CST:

- `python3 knowledge/scripts/validate_religion_theme.py --repo . --final` → PASS, 80 manifest rows / 226 evidence records / 64 W3 / 51 W5 / 45 W10 Religion rows.
- `python3 knowledge/scripts/validate_w10_absorption.py --repo .` → PASS, 122 cards.
- AI and Chinese Philosophy regression validators → PASS.
- Master spec, W3, W4, W5 validators → PASS.
- `git diff --check` and protected corpus diff check → PASS.
