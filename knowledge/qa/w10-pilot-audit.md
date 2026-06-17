# W10 Pilot Audit — Further Absorption Layer

- date: 2026-06-15 CST
- batch_id: W10-PILOT-B1-2026-06-15
- status: PASS
- scope: first W10 pilot batch; 5 cards across argument/process/case types

## Purpose

W10 was added after a 16-row inspection showed that the completed W1–W9 framework still under-captured several content forms:

1. dense argument sequences with strong rhetoric;
2. staged process / practice protocols;
3. figure or school case reconstructions that need more structure than W2 but are not W3 term senses or W5 relations.

W10 is an additive pilot layer. It does not rewrite corpus files, replace W2 cards, promote W3/W5 draft assets, or treat external generated material as canonical.

## Pilot Cards

| card_id | type | row | toc_id | focus |
|---|---|---:|---|---|
| `w10:arg:0076:contemporary-naturalism` | `w10-argument-card` | 76 | `1-4-1` | contemporary naturalism / analytic-philosophy critique |
| `w10:proc:0131:zhuangzi-eight-steps` | `w10-process-card` | 131 | `2-2-2-2` | Zhuangzi eight-step cultivation sequence |
| `w10:case:0173:john-stuart-mill` | `w10-case-card` | 173 | `2-4-2-1` | Mill as naturalistic idealism / utilitarian normativity |
| `w10:case:0258:early-lacan-metaphoric-symbolism` | `w10-case-card` | 258 | `3-4-1-2` | early Lacan as metaphoric symbolism |
| `w10:proc:0363:ai-regeneration` | `w10-process-card` | 363 | `4-4-4-4` | AI regeneration as speculative process |

## Schema / validator checks

`knowledge/scripts/validate_w10_absorption.py` checks:

- required metadata fields: `type`, `status`, `card_id`, `filename_stem`, `row_id`, `segment_id`, `toc_id`, `title`, `source_clean_path`, `rhetorical_register`, `w3_w5_gap_review`, `claim_core`, `evidence_quotes`, `forbidden_use`;
- accepted type enum: `w10-argument-card`, `w10-process-card`, `w10-case-card`;
- `pilot-draft` status for the current batch;
- stable `card_id` uniqueness;
- filename / card-id / row-id consistency;
- exact structured `index.md` matching for `{card_id, type, row_id, toc_id, path, href_path}`;
- rejection of unexpected markdown under `knowledge/w10-absorption/`;
- row, segment, TOC, and clean-path equality against `knowledge/manifests/segments.jsonl`;
- exact quote-substring checks against `split_md_clean/`;
- `[q1]`-style body claim-to-quote references, including all declared evidence quotes;
- `context_quotes` structure and exact substring checks when cross-row evidence is declared;
- bounded `rhetorical_register` values;
- non-empty `claim_core` and `forbidden_use`.

## Validation evidence

Commands run on 2026-06-15 CST:

```bash
python3 -m py_compile knowledge/scripts/validate_w10_absorption.py
ruff check knowledge/scripts/validate_w10_absorption.py
pyright knowledge/scripts/validate_w10_absorption.py
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
git diff --name-only -- split_md split_md_clean knowledge/lexicon knowledge/relations
```

Results:

- Python compile / ruff / pyright over `validate_w10_absorption.py`: PASS.
- W10 validator: PASS — 5 cards; type counts `argument=1`, `process=2`, `case=2`; errors=0.
- W10 → W3/W5 gap queue created: `knowledge/qa/w10-w3-w5-gap-followups.md`.
- Master validator: PASS — w3=544/200, w4=256, w5=60, W6=4/4, W7=6/6, W8=3/3/12queries, W9 repo-local metadata present, errors=0.
- W1 validator: PASS — 363 segments, 1594 chunks, 0 missing segments.
- W3 validator: PASS — records=544, terms=200, quotes=1141, errors=0, warnings=0.
- W5 validator: PASS — records=60, quotes=70, types=12/12, errors=0, warnings=0.
- W4 validators: PASS at L1=4, L2=16, L3=64, L4=172.
- `git diff --check`: PASS.
- `git diff --name-only -- split_md split_md_clean knowledge/lexicon knowledge/relations`: PASS empty output; no corpus/W3/W5 protected-layer rewrite.

## Adversarial validator check

Seven temporary adversarial checks were run and removed/restored afterward:

1. A malformed extra W10 card under `.omx/tmp/` with a non-existent evidence quote and no `[q1]` body mapping. Running:

```bash
python3 knowledge/scripts/validate_w10_absorption.py --repo . --extra-card <temporary-fixture>
```

correctly failed. The failure included exact quote-substring and body-mapping rejections.

2. A rogue markdown file under a temporary `knowledge/w10-absorption/rogue.*` directory correctly failed with `unexpected W10 markdown`, proving unknown W10 markdown cannot bypass validation.

3. A temporary stale row appended outside the Pilot cards table in `knowledge/w10-absorption/index.md` correctly failed with `W10 card row appears outside the Pilot cards table`.

4. A temporary broken Markdown href target in `index.md` correctly failed exact index validation, proving display text and link target must both point to the card.

5. A malformed row inserted inside the Pilot cards table correctly failed strict table parsing.

6. A temporary removal of the Lacan card’s `[q5]` body reference correctly failed `body does not reference all evidence quotes`, proving quote refs in the Evidence Quotes section alone do not satisfy claim mapping.

7. A temporary `row_id: not-an-int` mutation in the row 76 card correctly failed without traceback, proving invalid repo-card row metadata is reported as a structured validator error.

All fixtures and temporary edits were removed/restored after the checks.

## Manual quote trace spot-check

The row 76 card quotes were checked against:

`split_md_clean/1_实在论/1-4_复习/1-4-1_当代自然主义_反正科学可以解释一切_就干脆放弃思考吧_为什么分析哲学_总体上_不是哲/0076_1-4-1_当代自然主义_反正科学可以解释一切_就干脆放弃思考吧_为什么分析哲学_总体上_不是哲学_而是学术体系下的帮佣_p1727.md`

Each declared quote is an exact substring of that clean source.

## Boundary verdict

- Corpus integrity: preserved.
- Row/segment/quote traceability: validator-backed, including body `[q1]` claim mapping before the Evidence Quotes section, exact index display/href matching, and unknown W10 markdown rejection.
- W3/W5 draft status: unchanged.
- External material: not used as canonical evidence.
- Legacy frontend/product route: not restored.
- W10 status: pilot-draft only; suitable for further small-batch extension.
