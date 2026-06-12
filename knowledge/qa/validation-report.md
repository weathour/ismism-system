# W6 Validation Report — Evidence Chain Integrity

- created: 2026-06-09 CST
- scope: W6 audit item 3 plus cross-layer machine gates after W3 final quantitative floor closure.
- status: PASS — no blocking evidence-chain issue found.

## 1. Current Layer Counts

| layer | observed | gate |
|---|---:|---|
| W1 segments | 363 | 363 |
| W2 segment cards | 363 | 363 |
| W3 term senses | 544 senses / 200 terms | ≥500 senses / ≥200 terms |
| W4 position cards | 4 / 16 / 64 / 172 | MASTER-SPEC current target |
| W5 relations | 60 | ≥60 |

## 2. Machine Gates Run

```bash
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 60 --require-type-min 2
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 1 --expected-count 4
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 2 --expected-count 16
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 3 --expected-count 64
python3 knowledge/scripts/validate_w4_position_cards.py --repo . --level 4 --expected-count 172
git diff --check
```

Observed W3 result: `records=544, terms=200, quotes=1141, errors=0, warnings=0`.

Observed W5 result: `records=60, quotes=70, types=12/12, errors=0, warnings=0`.

## 3. Ten-Sense Evidence Trace Sample

Sampling rule: deterministic even-spacing over `term-senses.jsonl` after W3-B35.

| sense_id | term | label | quote rows | verdict |
|---|---|---|---|---|
| term:主体:s01 | 主体 | 矩阵中的主体侧维度 | 46,46 | PASS |
| term:场域论:s04 | 场域论 | 时间/空间场域配置 | 127,127 | PASS |
| term:语言:s02 | 语言 | 天然形而上学/符号实用主义 | 185,185 | PASS |
| term:表象化:s02 | 表象化 | 新知识与物理秩序的比较中介 | 4,4 | PASS |
| term:目的论化:s01 | 目的论化 | 形而上学机制导向伦理学 | 119,119 | PASS |
| term:研究:s01 | 研究 | 历史唯物主义/政治经济学的现实研究 | 285,285 | PASS |
| term:理论现实化:s01 | 理论现实化 | 理论影响/描述现实 | 285,285 | PASS |
| term:Event:s01 | Event | 不在场/缺失侧的事件 | 263,263 | PASS |
| term:音乐:s02 | 音乐 | 辩证法体系的无调性类比 | 229,229 | PASS |
| term:艺术:s02 | 艺术 | politics 艺术家的幻想位 | 263,263 | PASS |

## 4. Whole-File Evidence Checks

- all W3 `evidence_quotes` exact-substring validated: PASS
- all W3 declared `clean_md_path` / `segment_card_path` paths exist: PASS
- all W3 statuses remain `draft`: PASS
- W5 relation evidence and W4 position references validated by owner script: PASS

## 5. W6 Verdict

No blocking evidence-chain issue found. No confidence downgrades required by this audit.
