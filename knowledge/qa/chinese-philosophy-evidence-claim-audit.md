# Chinese Philosophy Evidence-Claim Audit

- date: 2026-06-15 CST
- status: draft audit surface

## Checked claim families

1. Confucian/Neo-Confucian claims cite row-level quote bank IDs such as `ev:chphil:0048:01` and W10 cards such as `w10:arg:0049:wang-yangming-sage-temptation`.
2. Daoist/Zhuangzi/Yijing/Names claims cite quote IDs such as `ev:chphil:0125:01`, `ev:chphil:0131:01`, `ev:chphil:0143:01` and W10 cards such as `w10:arg:0143:huishi-fangzhongfangni`.
3. Buddhist/Chan bridge claims cite `ev:chphil:0124:01`, `ev:chphil:0140:01`, `ev:chphil:0186:01` and remain class-owned as `buddhist-chan-bridge`.
4. Mao/Chinese Marxist claims cite `ev:chphil:0184:01`, `ev:chphil:0331:01`, `ev:chphil:0334:01` plus W3/W5 IDs.
5. Revolutionary/dialectical context rows are not overpromoted to core unless W10 or W3/W5 coverage explicitly supports that row.

## Failure modes guarded by validator

- fabricated quote: `validate_chinese_philosophy_theme.py` checks each quote against declared clean file;
- class drift: taxonomy and manifest class ownership must match;
- duplicate taxonomy row: validator rejects multiple ownership;
- unmarked synthesis claim: `- claim:` lines must carry evidence/source markers;
- stale synthesis marker: `--final` resolves `ev:chphil:*`, `term:*:sNN`, `rel:chphil:*`, `w10:*`, and `row N` markers and rejects unknown IDs;
- duplicate W10 evidence quote: `validate_w10_absorption.py` rejects repeated `evidence_quotes` inside a W10 card.
