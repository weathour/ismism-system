# W3 Fullscan Candidate Shard — 符号 / 002

- term: 符号
- batch_candidate: W3-fullscan-smoke
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 195 | `3-1-2` | 实事现象学——令现象学从哲学史走入历史，屈居二号人物的天才，舍勒 |
| 242 | `3-3-2-3` | 神-人伦理学——尼采笔下的“查拉图斯特拉”走入现实，是如何从生存论的深渊里幸存的 |
| 288 | `4-1-2-4` | 现实的本体论化 |
| 363 | `4-4-4-4` | 再生 |

## Candidate items

### C1: 约定

- row_id: 195
- validation_status: `quote_exact`
- quote: 通过约、符号性的、郑重的约定来组织社会架构。
- hit_reason: 提到了“符号性的、郑重的约定”，与“符号”概念相关。
- uncertainty_note: 无法判断该约定是否等同于符号的意义。

### C2: 符号学

- row_id: 242
- validation_status: `quote_not_found_in_shard`
- quote: 它同时展开一个符号学本体论、本体论符号学秩序，把它展开出来。
- hit_reason: 直接提到了“符号学本体论”和“符号学秩序”，是核心候选材料。
- uncertainty_note: 无法判断该秩序的具体构成要素。

### C3: 符号学意义

- row_id: 363
- validation_status: `quote_exact`
- quote: 这个物质结构本身它……本身获得一个符号学意义上的自治性。
- hit_reason: 提到了“符号学意义上的自治性”，与符号的意义层面相关。
- uncertainty_note: 无法判断“符号学意义”的具体内涵。
