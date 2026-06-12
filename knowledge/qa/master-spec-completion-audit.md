# MASTER-SPEC Completion Audit

- created: 2026-06-09 CST
- scope: requirement-by-requirement audit against `MASTER-SPEC.md` after W9 repo-local readiness.
- verdict: COMPLETE for `ismism-system` after the 2026-06-10 maintainer decision accepting repo-local W9 as sufficient; the external W9 target remains a downstream manual integration issue.
- detailed traceability matrix: `knowledge/qa/master-spec-requirement-traceability.md`

## 1. Hard boundary

| requirement | evidence | verdict |
|---|---|---|
| No writes outside `/home/weathour/文档/ismism-system` | W9 external target was inspected read-only but not updated; repo-local draft created under `knowledge/integration/` | PASS |
| Do not edit `MASTER-SPEC.md` | not modified by this run | PASS |
| Do not edit `Zhuyi_Matrix_Engine/` | not modified by this run | PASS |
| Keep W3/W5 draft before promotion | W3/W5 validators report draft records; no canonical promotion performed | PASS |

## 2. W3 term layer

| requirement | evidence | verdict |
|---|---|---|
| ≥200 core terms | `validate_w3_term_senses.py` reports `terms=200` | PASS |
| ≥500 sense records | `validate_w3_term_senses.py` reports `records=544` | PASS |
| each sense has ≥2 quotes | W3 validator checks quote count and reports `errors=0` | PASS |
| quote substring traceability | W3 validator reports `quotes=1141, errors=0` | PASS |
| axis and forbidden_mix fields | W3 validator checks required fields and reports `errors=0` | PASS |
| all W3 status draft | W3 validator reports `errors=0`; W6 validation report confirms all draft | PASS |
| ambiguity notes updated | `knowledge/lexicon/ambiguous-terms.md` includes W3-B1–B35 notes | PASS |

## 3. W4 position-card layer

| requirement | evidence | verdict |
|---|---|---|
| 4 L1 cards | `validate_w4_position_cards.py --level 1 --expected-count 4` | PASS |
| 16 L2 cards | `validate_w4_position_cards.py --level 2 --expected-count 16` | PASS |
| 64 L3 cards | `validate_w4_position_cards.py --level 3 --expected-count 64` | PASS |
| 172 L4 cards | `validate_w4_position_cards.py --level 4 --expected-count 172` | PASS |
| total 256 position cards | `validate_master_spec_outputs.py --repo .` reports `w4=256` | PASS |
| index covers position cards | W4 validator and master validator pass for expected counts/index entries | PASS |
| required card sections present | W4 validator and master validator check required headings | PASS |
| forbidden active language absent | active-surface forbidden scan passes | PASS |

## 4. W5 relation layer

| requirement | evidence | verdict |
|---|---|---|
| ≥60 relations | W5 validator reports `records=60` | PASS |
| 12 relation types covered | W5 validator reports `types=12/12` | PASS |
| each type ≥2 examples | W5 validator with `--require-type-min 2` passes | PASS |
| source/target positions exist | W5 validator checks W4 references and passes | PASS |
| evidence_segment present and quote-checked | W5 validator reports `quotes=70, errors=0` | PASS |
| applicability and forbidden interpretation present | W5 validator checks required fields and passes | PASS |

## 5. W6 audit layer

| requirement | evidence | verdict |
|---|---|---|
| sense mixing audit | `knowledge/qa/concept-drift-report.md` | PASS |
| relation strength audit | `knowledge/qa/evidence-claim-audit.md` | PASS |
| evidence-chain integrity audit | `knowledge/qa/validation-report.md` | PASS |
| forbidden item review | `knowledge/qa/rejected-interpretations.md` | PASS |
| no blocking W6 issue | W6 reports state no blocking issue and no confidence downgrade required | PASS |

## 6. W7 synthesis layer

| requirement | evidence | verdict |
|---|---|---|
| part-1-realism.md | `knowledge/syntheses/part-1-realism.md` exists | PASS |
| part-2-metaphysics.md | `knowledge/syntheses/part-2-metaphysics.md` exists | PASS |
| part-3-idealism.md | `knowledge/syntheses/part-3-idealism.md` exists | PASS |
| part-4-praxis.md | `knowledge/syntheses/part-4-praxis.md` exists | PASS |
| whole-system-map.md | `knowledge/syntheses/whole-system-map.md` exists | PASS |
| methodological-core.md | `knowledge/syntheses/methodological-core.md` exists | PASS |
| source-tagged claims | custom W7 tag check passes | PASS |
| method terms represented in W3 | `methodological-core.md` uses existing W3 terms such as `观察`, `分析`, `回溯`, `现实理论化`, `理论现实化`, `可行性` | PASS |

## 7. W8 usage protocol layer

| requirement | evidence | verdict |
|---|---|---|
| usage-protocol.md | `knowledge/usage-protocol.md` exists | PASS |
| query-playbook.md with 10+ paths | `knowledge/query-playbook.md` exists and has 12 query paths | PASS |
| export-manifest.md | `knowledge/export-manifest.md` exists | PASS |
| query-playbook has 10+ paths | `validate_master_spec_outputs.py --repo .` reports `12queries` | PASS |

## 8. W9 lightweight integration

| requirement | evidence | verdict |
|---|---|---|
| lightweight coordinate/term index prepared | `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md` exists | PASS (repo-local) |
| manual external-copy instructions prepared | `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md` exists | PASS |
| external status audit recorded | `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md` records current hashes and mismatch status | PASS |
| external status checker available | `knowledge/scripts/check_w9_external_status.py --repo .` reports the current read-only match/mismatch state | PASS |
| maintainer decision record prepared | `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md` records the remaining decision options | PASS |
| external target file current at `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md` | read-only diff shows the path exists as an older placeholder, but differs from the repo-local W9 protocol; not updated because repo hard boundary forbids external writes | NON-BLOCKING downstream issue after repo-local W9 acceptance |
| full library not copied | repo-local file is a lightweight index only | PASS |

## 9. Final validation commands

Required final command set:

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

## 10. Repo-local final validator

`python3 knowledge/scripts/validate_master_spec_outputs.py --repo .` reports:

```text
MASTER-SPEC repo-local validation: status=PASS, w3=544/200, w5=60, w6_reports=4/4, w7=6/6, w8=3/3, w9_repo_local=True, errors=0
```

The current enhanced validator output is:

```text
MASTER-SPEC repo-local validation: status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, w9_status_script=True, w9_decision_record=True, errors=0
```

This validator intentionally does not require the outside-repo W9 target unless called with `--require-external-w9`, because the repository hard boundary forbids writing outside `ismism-system`.

When called with `--require-external-w9`, the validator now requires the external target to match the repo-local W9 protocol. A read-only check currently fails because the external file exists but is older and different. This strict cross-repository check is no longer required for `ismism-system` completion after the 2026-06-10 maintainer decision accepting repo-local W9 as sufficient.

## 11. Completion verdict

- In-repo MASTER-SPEC deliverables through W8 are complete.
- W9 is prepared as a repo-local lightweight index and has been accepted as sufficient for `ismism-system`.
- The external W9 target exists as an older placeholder but is not updated to the current repo-local W9 protocol because the same MASTER-SPEC hard boundary forbids outside-repo writes.
- Manual/future-authorized copy instructions are available at `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md`.
- Therefore, the repo-local completion claim is no longer blocked by W9. Cross-repository W9 remains optional/downstream unless a future task explicitly authorizes external replacement.

## 12. Maintainer decision

- decision_date: 2026-06-10 CST
- decision: repo-local W9 under `knowledge/integration/psychoanalytic-writing-lab/` satisfies W9 for this repository.
- decision_record: `knowledge/integration/psychoanalytic-writing-lab/MAINTAINER-DECISION-RECORD.md`
