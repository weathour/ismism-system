# W3 Fullscan Candidate Shard — 绝对 / 001

- term: 绝对
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 4 | `1-1-1` | 物理主义 |
| 8 | `1-1-1-4` | 宇宙悲观主义 |
| 11 | `1-1-2-2` | 科学革命论 |
| 12 | `1-1-2-3` | 文化本体论 |
| 13 | `1-1-2-4` | 解构建构论 |
| 20 | `1-1-4-1` | 操作行为主义 |

## Candidate items

### C1: 绝对的信念

- row_id: 4
- validation_status: `quote_exact`
- quote: 他绝对不会有那种幻想。比如说闭上眼睛洗澡的时候，你再想我是不是往前跨一步就会掉到深渊，他觉得这种想象是不可能的。
- hit_reason: 直接提到了“绝对不会有”的判断，符合“绝对”的语义范围。
- uncertainty_note: 该表述描述的是一种信念的绝对性，但上下文是批判性的。

### C2: 绝对的缺乏

- row_id: 8
- validation_status: `quote_exact`
- quote: 如果这个绝对者它毫无伦理性，它具有这个时候你要意识到就是说在发生学机制之上，我知道你们的意思，我知道你们的恐慌。你们的恐慌就是说这个世界归根结底是无精神的，然后这个世界归根结底是没有爹管的、是无精神的，无根结底是无精神的世界本身，宇宙本身一些物质它是没有精神的，没有伦理维度的。
- hit_reason: 多次使用“绝对”一词，指代某种状态的彻底性或缺乏性。
- uncertainty_note: 这里的“绝对”是描述缺乏某种属性的彻底性，需要结合上下文理解。

### C3: 绝对的设定

- row_id: 17
- validation_status: `quote_exact_wrong_row`
- quote: 恶的无限一叠加变成绝对了。不能这样搞。it doesn't，他没用了。它要必须设立基本的一些一和零。
- hit_reason: 明确使用了“绝对”一词，指代一个无法逾越的界限或状态。
- uncertainty_note: 该表述是关于数学或逻辑结构上的绝对性限制。

### C4: 绝对的设定

- row_id: 18
- validation_status: `quote_exact_wrong_row`
- quote: 恶的无限一叠加变成绝对了。不能这样搞。it doesn't，他没用了。它要必须设立基本的一些一和零。
- hit_reason: 再次提到“绝对”，指代一个无法被概率化或超越的底层结构。
- uncertainty_note: 与 row_id=17 的内容高度重合，都指向底层结构的绝对性要求。
