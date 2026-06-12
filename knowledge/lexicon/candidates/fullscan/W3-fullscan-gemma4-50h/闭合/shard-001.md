# W3 Fullscan Candidate Shard — 闭合 / 001

- term: 闭合
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 1 | `1` | 实在论 |
| 4 | `1-1-1` | 物理主义 |
| 17 | `1-1-3-3` | 认知自我主义 |
| 18 | `1-1-3-4` | 认知无我论 |
| 19 | `1-1-4` | 行为主义 |
| 22 | `1-1-4-3` | 应用行为分析 |

## Candidate items

### C1: 自我同一性

- row_id: 1
- validation_status: `quote_exact`
- quote: 有一种力量让他自我同一，不停地闭合起来。实事求是承认他的自我同一，才是四字头。
- hit_reason: 直接提到了“闭合”和“自我同一”，与术语高度相关。
- uncertainty_note: 无法判断是否是核心概念的直接论述。

### C2: 无法闭合性

- row_id: 4
- validation_status: `quote_exact`
- quote: 你不能永远不能把它闭合，物理探索也不能把它闭合。
- hit_reason: 直接使用了“闭合”一词，讨论了物理探索的局限性。
- uncertainty_note: 讨论的是物理探索的局限性，而非概念的闭合。

### C3: 无我论闭合

- row_id: 18
- validation_status: `quote_exact`
- quote: 归根结底又说，它是无我论闭合的，不能说有个自我存在的，那就是它实际上是一种女性癔症化的一个立场。
- hit_reason: 明确提到了“无我论闭合”，与术语高度相关。
- uncertainty_note: 讨论的是一种哲学立场上的“闭合”。

### C4: 过程的闭合屏蔽

- row_id: 18
- validation_status: `quote_not_found_in_shard`
- quote: 因为底层生成过程被他自己闭合地屏蔽了。你就会觉得“我要吃西瓜”这个念头是自己冒出来的，你就会觉得它是透明的。
- hit_reason: 描述了底层生成过程被“闭合地屏蔽”，与术语相关。
- uncertainty_note: 描述的是认知过程中的屏蔽现象。

### C5: 认识论闭合

- row_id: 19
- validation_status: `quote_exact`
- quote: 梅青格尔，闭合的认识论，闭合的。恰恰是由于这种认识论闭合、无我论，让你彻底遗忘掉，你闭合得太过分了，一点反思性都没有的，这种情况才会变成行为主义者。
- hit_reason: 多次提到“闭合的认识论”和“闭合”，与术语高度相关。
- uncertainty_note: 讨论的是一种认识论层面的“闭合”。
