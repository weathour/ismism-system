# W10 Further Absorption Index

- status: pilot-draft
- layer: draft additive close-reading layer after W1–W9
- validator: `python3 knowledge/scripts/validate_w10_absorption.py --repo .`

W10 is not a canonical replacement for corpus/manifests/segment cards. It records pilot argument, process, and case structures that W3/W5/W7 do not fully capture.

## Pilot cards

| card_id | type | row | toc | path |
|---|---|---:|---|---|
| `w10:arg:0076:contemporary-naturalism` | `w10-argument-card` | 76 | `1-4-1` | [`knowledge/w10-absorption/argument-cards/w10-arg-0076-contemporary-naturalism.md`](argument-cards/w10-arg-0076-contemporary-naturalism.md) |
| `w10:proc:0131:zhuangzi-eight-steps` | `w10-process-card` | 131 | `2-2-2-2` | [`knowledge/w10-absorption/process-cards/w10-proc-0131-zhuangzi-eight-steps.md`](process-cards/w10-proc-0131-zhuangzi-eight-steps.md) |
| `w10:case:0173:john-stuart-mill` | `w10-case-card` | 173 | `2-4-2-1` | [`knowledge/w10-absorption/case-cards/w10-case-0173-john-stuart-mill.md`](case-cards/w10-case-0173-john-stuart-mill.md) |
| `w10:case:0258:early-lacan-metaphoric-symbolism` | `w10-case-card` | 258 | `3-4-1-2` | [`knowledge/w10-absorption/case-cards/w10-case-0258-early-lacan-metaphoric-symbolism.md`](case-cards/w10-case-0258-early-lacan-metaphoric-symbolism.md) |
| `w10:proc:0363:ai-regeneration` | `w10-process-card` | 363 | `4-4-4-4` | [`knowledge/w10-absorption/process-cards/w10-proc-0363-ai-regeneration.md`](process-cards/w10-proc-0363-ai-regeneration.md) |

## Card-type counts

- argument cards: 1
- process cards: 2
- case cards: 2

## Boundaries

- `evidence_quotes` are same-row evidence only.
- `context_quotes` must carry their own full row/segment/path metadata.
- `rhetorical_register` separates polemical/speculative tone from reusable `claim_core`.
- Body claims use `[q1]`-style references back to declared `evidence_quotes`.
- `w3_w5_gap_review` records whether W10 exposed a follow-up need rather than silently bypassing W3/W5.
- `forbidden_use` blocks unsafe export, personality diagnosis, or external factual claims beyond the source row.
