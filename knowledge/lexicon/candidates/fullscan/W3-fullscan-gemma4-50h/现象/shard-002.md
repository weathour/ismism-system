# W3 Fullscan Candidate Shard — 现象 / 002

- term: 现象
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 10 | `1-1-2-1` | 科学知识社会学 |
| 12 | `1-1-2-3` | 文化本体论 |
| 13 | `1-1-2-4` | 解构建构论 |
| 14 | `1-1-3` | 认知主义 |
| 16 | `1-1-3-2` | 自由进化论 |
| 17 | `1-1-3-3` | 认知自我主义 |

## Candidate items

### C1: 意识结构

- row_id: 25
- validation_status: `quote_exact_wrong_row`
- quote: 所有比如说所有意识、内容意识、结构、精神结构。
- hit_reason: 直接提到了“意识”和“精神结构”，与“现象”的概念相关。
- uncertainty_note: 不确定是否指代哲学上的现象学意义上的现象。

### C2: 存在者现象化

- row_id: 25
- validation_status: `quote_exact_wrong_row`
- quote: 所有这些东西先普遍化，把存在者整体的给它符号学化。
- hit_reason: “存在者整体的给它符号学化”描述了一种将存在状态进行表征化的过程，与现象的表征相关。
- uncertainty_note: 不确定“符号学化”是否等同于“现象”的指代。

### C3: 意识现象

- row_id: 17
- validation_status: `quote_exact`
- quote: 现象性的意识的出现，是需要由意识的连续统，或者需要有核心自我来支撑的，需要的数据要有核心自我（core self）来支撑。
- hit_reason: 明确提到了“现象性的意识”，这是与“现象”高度相关的术语。
- uncertainty_note: 不确定“现象性”是否特指哲学上的现象学意义。

### C4: 现象性意识

- row_id: 17
- validation_status: `quote_exact`
- quote: 上述维度都是无意识的，上面这些维度都是现象学意义上的，或者现象性的意识的，它都没有现象性的意识，还没有现象性的意识。
- hit_reason: 多次提到“现象学意义上的”和“现象性的意识”，直接指向了“现象”的讨论范畴。
- uncertainty_note: 不确定是否仅限于现象学意义上的现象。
