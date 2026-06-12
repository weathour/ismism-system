# MASTER-SPEC Requirement Traceability Matrix

- created: 2026-06-09 CST
- scope: explicit hard metrics, phase gates, file contracts, and boundary rules in `MASTER-SPEC.md`.
- status: repo-local PASS; repo-local W9 accepted as sufficient on 2026-06-10 CST; external W9 remains downstream/manual.
- validator: `python3 knowledge/scripts/validate_master_spec_outputs.py --repo .`

This matrix is a resume-safe audit surface. It does not replace `MASTER-SPEC.md`; it maps each requirement to current evidence and the validator or file that proves it.

## A. Boundary and source-of-truth requirements

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| A1 | Repository work stays inside `/home/weathour/文档/ismism-system` | W9 external target inspected read-only but not updated; repo-local export package under `knowledge/integration/psychoanalytic-writing-lab/` | PASS |
| A2 | `MASTER-SPEC.md` remains human-maintained | No edits made to `MASTER-SPEC.md` | PASS |
| A3 | `split_md/` raw corpus not overwritten | Work products are in `knowledge/`; no raw corpus rewrite in this completion pass | PASS |
| A4 | `Zhuyi_Matrix_Engine/` remains intact | No migration or mutation made there | PASS |
| A5 | Atlas remains candidate-only | Active final surfaces cite W1/W2/W3/W4/W5 layers, not Atlas as canonical | PASS |
| A6 | Old frontend does not drive current work | Final validation excludes `src/`/`dist/`; current handoff marks them legacy | PASS |
| A7 | W3/W5 stay draft unless review promotes them | Master validator checks non-draft W3/W5 records and reports no errors | PASS |

## B. W3 term-sense layer

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W3.1 | `term-senses.jsonl` contains at least 200 terms | `validate_master_spec_outputs.py` reports `w3_terms=200`; W3 validator agrees | PASS |
| W3.2 | At least 500 sense records | `validate_master_spec_outputs.py` reports `w3_senses=544`; W3 validator agrees | PASS |
| W3.3 | Each sense has at least two evidence quotes | W3 validator reports `quotes=1141, errors=0`; master validator checks quote count | PASS |
| W3.4 | Evidence quotes trace to `split_md_clean` by substring | `validate_w3_term_senses.py --repo .` reports `errors=0` | PASS |
| W3.5 | Each sense has `axis` | Master validator checks non-empty `axis`; W3 validator passes | PASS |
| W3.6 | Each sense has `forbidden_mix` | Master validator checks non-empty `forbidden_mix`; W3 validator passes | PASS |
| W3.7 | Overlap risks recorded | `knowledge/lexicon/ambiguous-terms.md` present and populated through W3-B35 | PASS |
| W3.8 | All sense records remain `draft` | Master validator checks status and reports no non-draft W3 records | PASS |
| W3.9 | Source segment paths exist | `validate_w3_term_senses.py --repo .` reports `errors=0` | PASS |
| W3.10 | Sense IDs follow the required pattern | `validate_w3_term_senses.py --repo .` reports `errors=0` | PASS |

## C. W4 position-card layer

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W4.1 | Four level-1 cards | W4 validator: level 1 count `4`; master validator `w4_counts[1]=4` | PASS |
| W4.2 | Sixteen level-2 cards | W4 validator: level 2 count `16`; master validator `w4_counts[2]=16` | PASS |
| W4.3 | Sixty-four level-3 cards | W4 validator: level 3 count `64`; master validator `w4_counts[3]=64` | PASS |
| W4.4 | One hundred seventy-two level-4 cards | W4 validator: level 4 count `172`; master validator `w4_counts[4]=172` | PASS |
| W4.5 | Total position-card count equals 256 | Master validator reports `w4_total=256` | PASS |
| W4.6 | Cards include required template sections | W4 validator and master validator check required section headings | PASS |
| W4.7 | Index covers all cards | W4 validator and master validator check `knowledge/position-cards/index.md` entries | PASS |
| W4.8 | Cards avoid forbidden person-labelling language | W4 validator plus active-surface forbidden scan report no hits | PASS |
| W4.9 | Cards avoid absolute-truth wording for matrix positions | W4 validator plus active-surface forbidden scan report no hits | PASS |
| W4.10 | Cards carry source rows and source segments | W4 validator passes for all expected levels | PASS |

## D. W5 relation-asset layer

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W5.1 | At least 60 relation records | W5 validator and master validator report `60` | PASS |
| W5.2 | All 12 relation types covered | W5 validator reports `types=12/12`; master validator checks required type set | PASS |
| W5.3 | Each relation type has at least two examples | W5 validator with `--require-type-min 2` passes; master validator checks type counts | PASS |
| W5.4 | Each relation has source and target positions | `validate_w5_relation_assets.py` reports `errors=0` | PASS |
| W5.5 | Source and target positions exist in W4 | `validate_w5_relation_assets.py` reports `errors=0` | PASS |
| W5.6 | Each relation has evidence segment support | W5 validator reports `quotes=70, errors=0`; master validator checks `evidence_segment` | PASS |
| W5.7 | Each relation has applicability boundary and forbidden interpretation | W5 validator and master validator check required fields | PASS |
| W5.8 | Relations remain draft | Master validator checks no non-draft W5 records | PASS |

## E. W6 audit layer

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W6.1 | Sense-mixing audit exists | `knowledge/qa/concept-drift-report.md` | PASS |
| W6.2 | Relation-strength audit exists | `knowledge/qa/evidence-claim-audit.md` and `knowledge/qa/w5-relation-audit.md` | PASS |
| W6.3 | Evidence-chain audit exists | `knowledge/qa/validation-report.md` | PASS |
| W6.4 | Forbidden-item review exists | `knowledge/qa/rejected-interpretations.md` | PASS |
| W6.5 | No blocking issue remains before W7 | W6 reports and final audit state no blocking issue | PASS |
| W6.6 | Low-confidence handling recorded if needed | W6 reports state no downgrade required | PASS |

## F. W7 synthesis layer

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W7.1 | Field 1 synthesis exists | `knowledge/syntheses/part-1-realism.md` | PASS |
| W7.2 | Field 2 synthesis exists | `knowledge/syntheses/part-2-metaphysics.md` | PASS |
| W7.3 | Field 3 synthesis exists | `knowledge/syntheses/part-3-idealism.md` | PASS |
| W7.4 | Field 4 synthesis exists | `knowledge/syntheses/part-4-praxis.md` | PASS |
| W7.5 | Whole-system map exists | `knowledge/syntheses/whole-system-map.md` | PASS |
| W7.6 | Methodological core exists | `knowledge/syntheses/methodological-core.md` | PASS |
| W7.7 | Synthesis claims link to row/term/position/relation evidence | Master validator checks W7 term and relation refs plus source tags | PASS |
| W7.8 | No unsourced substantive bullets | Master validator checks bullet source tags | PASS |

## G. W8 usage-protocol layer

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W8.1 | Usage protocol exists | `knowledge/usage-protocol.md` | PASS |
| W8.2 | Query playbook exists | `knowledge/query-playbook.md` | PASS |
| W8.3 | Query playbook has at least 10 typical paths | Master validator reports `w8_query_paths=12` | PASS |
| W8.4 | Export manifest exists | `knowledge/export-manifest.md` | PASS |
| W8.5 | External interface contract is documented | `knowledge/export-manifest.md` and W9 protocol file | PASS |

## H. W9 lightweight integration

| ID | Requirement | Evidence | Current verdict |
|---|---|---|---|
| W9.1 | W8 is complete before W9 | W8 artifacts exist and pass master validator | PASS |
| W9.2 | Lightweight coordinate/term index is prepared | `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md` | PASS repo-local |
| W9.3 | Full library is not copied into the integration package | Repo-local W9 file is a compact protocol/index, not a corpus copy | PASS |
| W9.4 | External target file is current in psychoanalytic-writing-lab | Read-only diff shows the path exists as an older placeholder, but differs from `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`; repo-local W9 accepted as sufficient on 2026-06-10 CST | NON-BLOCKING downstream issue |
| W9.5 | Human/future-authorized copy path documented | `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md` | PASS |
| W9.6 | External mismatch is auditable without outside-repo write | `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md` records hashes and verification commands | PASS |
| W9.7 | External match state is machine-checkable | `knowledge/scripts/check_w9_external_status.py --repo . --expect-match` exits non-zero until the external target matches | PASS |
| W9.8 | Remaining W9 decision is explicitly documented | `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md` gives the accepted resolution options | PASS |

## I. Current final command evidence

Last observed repo-local master validation:

```text
MASTER-SPEC repo-local validation: status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, w9_status_script=True, w9_decision_record=True, errors=0
```

Full verification set to rerun on resume:

```bash
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
```

## J. Completion interpretation

- Repo-local completion is proven by current validators and artifacts.
- Repo-local W9 has been accepted as sufficient for `ismism-system` by maintainer decision on 2026-06-10 CST.
- Full cross-repository W9 completion is not proven, because the external target file is an older nonmatching placeholder and cannot be updated under the current hard boundary.
- The external mismatch remains a downstream/manual integration issue, not a blocker for this repository's completion claim.
