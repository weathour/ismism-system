# W3 Fullscan Candidate Shard — 现象 / 024

- term: 现象
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 241 | `3-3-2-2` | 诗性存在论——以诗代思，荷尔德林的癫疯循环 |
| 242 | `3-3-2-3` | 神-人伦理学——尼采笔下的“查拉图斯特拉”走入现实，是如何从生存论的深渊里幸存的 |
| 245 | `3-3-3-1` | 斗争的生存论 |
| 246 | `3-3-3-2` | 直接生存论 |
| 249 | `3-3-4` | 虚构的生存论 |
| 251 | `3-3-4-2` | 去中心化的科层主义 |

## Candidate items

### C1: 现象学

- row_id: 241
- validation_status: `quote_exact`
- quote: 你至少做一个马利翁那种人，诗学的什么现象学什么的东西，你至少要成为一个这种在智性成就上让我们给你承认你的地位
- hit_reason: 直接提到了“现象学”这一术语，与“现象”高度相关。
- uncertainty_note: 无法判断该“现象学”指代的是理论还是具体现象。

### C2: 认识论/现象

- row_id: 242
- validation_status: `quote_exact`
- quote: 不是现象性的认识，不是理性认识，不是知觉性的认识。
- hit_reason: 明确区分了“现象性”的认识，指出了认识的层次。
- uncertainty_note: 上下文是在讨论认识的类型，但未直接论述“现象”本身。

### C3: 可言说性/现象

- row_id: 246
- validation_status: `quote_exact`
- quote: 这个图像可以被描述出来、可以被说出来，他可以被说、可以被问、可以被说出来。
- hit_reason: 描述了某种状态（图像）可以通过语言和观看的方式被呈现出来，涉及现象的表征。
- uncertainty_note: 侧重于“可描述性”而非“现象”本身。

### C4: 主体性/敞开性

- row_id: 249
- validation_status: `quote_exact`
- quote: 他自己没有稳固了一个自我认识的损失，是敞开的，就是一切都有可能。
- hit_reason: 描述了一种主体认识上的“敞开”状态，这可以被视为一种未固化的现象状态。
- uncertainty_note: 更偏向于认识论上的“开放性”而非“现象”的指代。

### C5: 现象/结构

- row_id: 251
- validation_status: `quote_exact_wrong_row`
- quote: 他把这种永恒的我们存在一个精神性的综合机制，存在现象和本体的它的结构化的一个机制。
- hit_reason: 明确提到了“存在现象”和“本体”的结构化机制，直接关联了“现象”。
- uncertainty_note: 这里的“现象”是作为结构化机制的一部分被提及的。
