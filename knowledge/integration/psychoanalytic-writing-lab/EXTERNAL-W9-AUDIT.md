# W9 External Target Audit

- created: 2026-06-09 CST
- status: repo-local W9 package ready and accepted as sufficient; external target mismatch observed read-only and documented as downstream/manual
- repo-local protocol: `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
- intended external target: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`

## Purpose

This audit records the current cross-repository W9 state without performing any outside-repo write. It exists because `MASTER-SPEC.md` requires a lightweight psychoanalytic-writing-lab index, while the repository hard boundary forbids this agent from updating files outside `/home/weathour/文档/ismism-system`.

Maintainer decision on 2026-06-10 CST accepts the repo-local W9 package under `knowledge/integration/psychoanalytic-writing-lab/` as sufficient for completing `ismism-system`. The external mismatch remains a downstream manual integration issue, not a completion blocker for this repository.

## Read-only observation

Observed on 2026-06-09 CST:

| file | size | sha256 | interpretation |
|---|---:|---|---|
| repo-local W9 protocol | 3698 bytes | `383247be4a31c38451c38d86bfa211a5a485ea45ceb0311d2e3df6de1de4b3da` | current W9 protocol prepared by this repo |
| external target | 2546 bytes | `482d920c0cc737ff9f4671b4a32e2286aa8c070807a2836e49e273e29196acf1` | older placeholder; differs from repo-local protocol |

The external target therefore cannot be counted as a current cross-repository W9 copy unless it is replaced with the repo-local protocol. For `ismism-system` itself, repo-local W9 has been accepted as sufficient; this mismatch is non-blocking.

## Verification commands

Run from `/home/weathour/文档/ismism-system`:

```bash
sha256sum knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md
sha256sum /home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md
cmp -s \
  knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md \
  /home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md \
  && echo 'W9 external target matches repo-local protocol' \
  || echo 'W9 external target differs from repo-local protocol'
```

For the integrated validator:

```bash
python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9
```

Expected current result: FAIL, because the external target differs from the repo-local protocol.

For a focused read-only status check:

```bash
python3 knowledge/scripts/check_w9_external_status.py --repo .
python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match
```

Expected current result: the first command reports `status=MISMATCH`; the second command exits non-zero until the external target matches the repo-local protocol.

## Boundary-safe resolution options

1. Repo-local W9 has been accepted as sufficient for `ismism-system`; keep the external target outside the completion claim.
2. If cross-repository W9 is mandatory, a human or a future explicitly authorized run must replace the external file using `COPY-INSTRUCTIONS.md`.
3. After replacement, rerun `python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9`; only a PASS there proves cross-repository W9 completion.

## Non-copying constraint

W9 remains a lightweight coordinate/term index. Do not copy the corpus, W3 JSONL, W4 cards, W5 relations, or W7 syntheses into the external workspace.
