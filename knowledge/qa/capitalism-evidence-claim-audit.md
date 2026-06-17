# Capitalism Evidence-Claim Audit

- date: 2026-06-16
- status: PASS

## Claim discipline

The Capitalism layer uses four marker families:

- `ev:cap:*` for exact quote-bank evidence.
- `term:*:sNN` for W3 draft term senses.
- `rel:capitalism:*` for W5 draft relation assets.
- `w10:*:capitalism-*` for W10 pilot close-reading cards.

The validator rejects unknown markers in synthesis files and checks that every claim bullet contains at least one parseable marker.

## Evidence checks

- Manifest quote counts match the evidence bank row-by-row.
- Evidence quotes are exact substrings of declared `split_md_clean` files.
- Core rows have at least three quote records.
- Taxonomy rows are owned by exactly one class.
- `--final` validation also checks W3/W5 JSONL raw byte-prefix append-only preservation, so shared stores cannot pass if old lines are reserialized or edited.

## Negative-test plan

1. Corrupt a capitalism evidence quote; `validate_capitalism_theme.py --final` must fail.
2. Duplicate a taxonomy row across two classes; validator must fail.
3. Add an unknown marker in a capitalism synthesis; validator must fail.
4. Duplicate a W10 evidence quote; `validate_w10_absorption.py` must fail.
5. Reinsert the rejected Capitalism W10 placeholder phrase; `validate_w10_absorption.py` must fail.

Hermetic negative-test transcripts passed and were restored inside the temp copy: `.omx/tmp/validate_capitalism_bad_quote_negative.txt`, `.omx/tmp/validate_capitalism_taxonomy_negative.txt`, `.omx/tmp/validate_capitalism_synthesis_marker_negative.txt`, `.omx/tmp/validate_w10_capitalism_duplicate_quote_negative.txt`, `.omx/tmp/validate_w10_capitalism_placeholder_negative.txt`.
