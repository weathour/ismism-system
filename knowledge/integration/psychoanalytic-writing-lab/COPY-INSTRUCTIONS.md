# W9 External Copy Instructions

- status: manual / future-authorized action only
- created: 2026-06-09 CST
- source file inside this repo: `knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md`
- intended external target: `/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- external status audit: `knowledge/integration/psychoanalytic-writing-lab/EXTERNAL-W9-AUDIT.md`

## Why this is manual

`MASTER-SPEC.md` and the repository instructions forbid this agent from writing outside `/home/weathour/文档/ismism-system`.

Therefore the W9 external target is not updated by this agent. A read-only check on 2026-06-09 found that the external target path already exists as an older placeholder, but it differs from the repo-local W9 protocol prepared here. The repo-local W9 file is ready and validated; a human, or a future run with explicit outside-repo write authorization, may replace the older external file with it.

Current hashes are recorded in `EXTERNAL-W9-AUDIT.md`.

## Copy command for a human shell

Run from `/home/weathour/文档/ismism-system`:

```bash
mkdir -p /home/weathour/文档/psychoanalytic-writing-lab/docs/method
cp knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md \
  /home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md
```

## Verification command

```bash
cmp -s \
  knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md \
  /home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md \
  && echo 'W9 external target matches repo-local draft'
```

Or use the repo-local checker:

```bash
python3 knowledge/scripts/check_w9_external_status.py --repo . --expect-match
python3 knowledge/scripts/validate_master_spec_outputs.py --repo . --require-external-w9
```

## Do not copy full library

W9 requires only a lightweight coordinate/term index. Do not copy `split_md/`, `split_md_clean/`, W3 JSONL, W4 cards, W5 relations, or W7 syntheses into the external repo.
