# W9 Maintainer Decision Record

- created: 2026-06-09 CST
- status: accepted repo-local W9 sufficient
- scope: final unresolved W9 condition in `MASTER-SPEC.md`
- repo-local W9 protocol: `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
- external target: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`

## Maintainer decision — 2026-06-10 CST

Decision: **Option A — Accept repo-local W9 as sufficient**.

```text
Maintainer decision: repo-local W9 package under `knowledge/integration/psychoanalytic-writing-lab/` satisfies W9 for this repository. The external target is a downstream manual integration task, not a completion blocker for ismism-system.
```

Effect:

- `ismism-system` may be considered complete against its repo-local W9 requirement.
- The external target mismatch remains documented, but it is no longer a completion blocker for this repository.
- No outside-repo write is authorized or performed by this decision.

## Current evidence

Repo-local MASTER-SPEC validation passes:

```bash
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
```

Current observed output:

```text
MASTER-SPEC repo-local validation: status=PASS, w3=544/200, w4=256, w5=60, w6_reports=4/4, w7=6/6, w8=3/3/12queries, w9_repo_local=True, w9_external_audit=True, w9_status_script=True, w9_decision_record=True, errors=0
```

Strict cross-repository W9 validation currently fails:

```bash
python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match
python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9
```

Reason: the external target exists but differs from the repo-local W9 protocol. The mismatch is recorded in `EXTERNAL-W9-AUDIT.md`.

## Boundary conflict

`MASTER-SPEC.md` simultaneously creates two constraints:

1. hard boundary: this agent must not write outside `/home/weathour/文档/ismism-system`;
2. W9 ideal target: a lightweight index in `psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`.

Because the external target is outside this repository, this agent cannot update it under the current rules.

## Decision options

The maintainer has selected Option A. The other options remain recorded for future downstream integration decisions.

### Option A — Accept repo-local W9 as sufficient

Decision statement to record:

```text
Maintainer decision: repo-local W9 package under `knowledge/integration/psychoanalytic-writing-lab/` satisfies W9 for this repository. The external target is a downstream manual integration task, not a completion blocker for ismism-system.
```

After this decision, repo-local validation is sufficient evidence for completion.

### Option B — Authorize external replacement

Decision statement to record:

```text
Maintainer decision: for W9 only, updating `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md` with the repo-local protocol is explicitly authorized and overrides the no-outside-write boundary for that one file.
```

After the external replacement, rerun:

```bash
python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match
python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9
```

Both commands must pass before cross-repository W9 is complete.

### Option C — Leave W9 unresolved

Decision statement to record:

```text
Maintainer decision: no external replacement and no repo-local sufficiency acceptance at this time.
```

Under this option, the repository remains repo-local complete but the persistent MASTER-SPEC goal remains blocked at W9.

## No automatic action

This file is only a decision record/template. It does not authorize outside-repo writes by itself.
