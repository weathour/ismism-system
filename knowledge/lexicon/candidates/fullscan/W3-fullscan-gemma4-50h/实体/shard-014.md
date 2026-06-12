# W3 Fullscan Candidate Shard — 实体 / 014

- term: 实体
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 164 | `2-3-4-3` | 物理归纳主义——培根：知识就是力量，而且是一种魔法力量 |
| 167 | `2-4-1` | 经验主义——霍布斯的极简形而上学：利维坦和契约论的哲学基础 |
| 168 | `2-4-1-1` | 乐于接受的小体主义——波义耳、聪明而怯懦者的形而上学 |
| 169 | `2-4-1-2` | 经验的观念论——“心灵是一块白板”绝大多数人都理解错了！洛克：观念论运动与先验哲学的伟大先驱 |
| 170 | `2-4-1-3` | 理念-精神二元论——“存在即被感知”到底是什么意思？贝克莱真的不是“主观唯心主义” |
| 171 | `2-4-1-4` | 人类有限主义 |

## Candidate items

### C1: 物理实体

- row_id: 164
- validation_status: `quote_exact`
- quote: 直接归纳的就是一个physical substance，直接归纳这些一个个的实体。
- hit_reason: 明确提到了“physical substance”和“实体”的归纳过程。
- uncertainty_note: 无法判断该实体是抽象概念还是具体物质。

### C2: 存在实体

- row_id: 167
- validation_status: `quote_exact`
- quote: 都是exist、等于都是存在的，都是entity、都是实体。
- hit_reason: 直接使用了“entity”和“实体”的词汇来指代可被认知的存在物。
- uncertainty_note: 不清楚这些“实体”是指物理实体还是概念实体。

### C3: 本体实体性

- row_id: 167
- validation_status: `quote_exact`
- quote: 那么苹果的自己的那个thisness，那个苹果的存在本身、苹果的支撑的那个实体性本身是什么？substance什么？
- hit_reason: 讨论了“实体性本身”和“substance”的概念，指向了某种支撑存在的本质。
- uncertainty_note: 不确定这个“实体性”是否可以被经验观察到。

### C4: 存在实体

- row_id: 167
- validation_status: `quote_exact`
- quote: 都是exist、等于都是存在的，都是entity、都是实体。
- hit_reason: 重复提及了“entity”和“实体”，指代可被认知的存在物。
- uncertainty_note: 与前一条记录内容高度重复，但仍是候选材料。

### C5: 物质实体

- row_id: 168
- validation_status: `quote_exact`
- quote: 小体（corpuscule）是不能够……Corpus有实体的意思。corpuscularian是小体论的，那么这个（corpuscularianism）就是小体论、小体主义。
- hit_reason: 提到了“小体（corpuscule）”和“小体论”，暗示了物质层面的实体概念。
- uncertainty_note: 不清楚“小体”在哲学上是否等同于现代意义上的物质实体。

### C6: 本体实体性

- row_id: 169
- validation_status: `quote_exact_wrong_row`
- quote: 那么苹果的自己的那个thisness，那个苹果的存在本身、苹果的支撑的那个实体性本身是什么？substance什么？
- hit_reason: 讨论了“实体性本身”和“substance”，指向了某种支撑存在的本质。
- uncertainty_note: 与row_id=167的讨论类似，但上下文不同。

### C7: 结构实体

- row_id: 169
- validation_status: `quote_not_found_in_shard`
- quote: 这个一般会把它叫做mode或者说substance and mode，实体和它的构成的形式。
- hit_reason: 明确提到了“substance and mode”的结构，涉及实体和其构成形式的关系。
- uncertainty_note: 不确定“mode”是否可以被视为一种独立于“substance”的实体。

### C8: 结构实体

- row_id: 169
- validation_status: `quote_not_found_in_shard`
- quote: 这个一般会把它叫做mode或者说substance and mode，实体和它的构成的形式。
- hit_reason: 再次提及“substance and mode”，强调了实体和其形式的关联。
- uncertainty_note: 与前一条记录内容重复，但仍是候选材料。

### C9: 精神实体

- row_id: 170
- validation_status: `quote_exact`
- quote: Spirit是一种精神性的实体，具有本体论地位。
- hit_reason: 明确将“Spirit”定义为具有“本体论地位”的“精神性的实体”。
- uncertainty_note: 该“Spirit”的本体论地位是否等同于传统意义上的实体，需要进一步界定。

### C10: 本体支撑体

- row_id: 170
- validation_status: `quote_exact`
- quote: 本体论上还有 Spirit，这个东西是具有本体性的，它具有本体论地位，是一个本体性的支撑。
- hit_reason: 强调了“Spirit”作为具有“本体论地位”的“本体性的支撑”。
- uncertainty_note: 该“支撑”的性质是精神性的，与物质实体有区别。

### C11: 实体性判断缺失

- row_id: 171
- validation_status: `quote_exact`
- quote: 在休谟那边的话，我们都不能够判断某个东西它到底有没有实体性。
- hit_reason: 描述了在休谟的体系中，对事物是否具有“实体性”的判断是无法做到的。
- uncertainty_note: 这不是一个实体，而是对实体概念的否定性论断。
