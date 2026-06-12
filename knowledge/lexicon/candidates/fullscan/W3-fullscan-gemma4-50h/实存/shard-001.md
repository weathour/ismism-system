# W3 Fullscan Candidate Shard — 实存 / 001

- term: 实存
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 1 | `1` | 实在论 |
| 36 | `1-2-3` | 唯灵论——所谓“灵修”不过是人的好奇与自私所支撑的意识形态 |
| 40 | `1-2-3-4` | 弃绝主义——解脱痛苦追求涅槃：意识的符号学机制 |
| 54 | `1-3-2-2` | 现代犬儒主义——工薪阶层最容易陷入的意识形态陷阱 |
| 67 | `1-4` | 平庸主义——你为什么怎么也学不进哲学？前反思者中的拒绝反思者，你为什么如此平庸？ |
| 72 | `None` | 格的分析 |

## Candidate items

### C1: 存在性判断

- row_id: 1
- validation_status: `quote_exact`
- quote: Void是不是exist？它是外部外在、外部外显，它是不是真的实存的？或者应该不用exist，就是“Is void is”？它是不是存在的？
- hit_reason: 直接讨论了“Void”是否“实存”的问题，与“实存”概念高度相关。
- uncertainty_note: 无法判断该“实存”指代的是本体论上的实在性还是哲学上的存在状态。

### C2: 场域的实在性

- row_id: 1
- validation_status: `quote_exact`
- quote: Void它本来应该是存在者整体所存在的一个场，但是这个场本身在不在？它和不和存在者（构成）整体？它在不在下面？
- hit_reason: 探讨了“场”本身是否具有独立于“存在者整体”的“在场”或“存在”状态，涉及实存性。
- uncertainty_note: 讨论的是场域的本体论地位，是否构成一个独立存在的实体。

### C3: 场域的实在性

- row_id: 72
- validation_status: `quote_exact_wrong_row`
- quote: Void它本来应该是存在者整体所存在的一个场，但是这个场本身在不在？它和不和存在者（构成）整体？它在不在下面？
- hit_reason: 重复讨论了“Void”作为场域本身是否具有独立存在的状态，与“实存”的探讨一致。
- uncertainty_note: 与 row_id=1 的讨论高度重合，但从不同的语境（谬误之路）提出。

### C4: 标准本身的虚构性

- row_id: 72
- validation_status: `quote_exact`
- quote: 不存在超语言，不存在一种无条件地、永恒地免费划分有无，存在和虚无，存在者和不存在者的标准。
- hit_reason: 质疑了划分“有无”、“存在”和“虚无”的标准本身是否“实存”，指向了标准本身的非实在性。
- uncertainty_note: 讨论的是划分标准（本体论框架）的虚构性，而非某个具体实体的实存。

### C5: 存在者的本体论地位

- row_id: 67
- validation_status: `quote_not_found_in_shard`
- quote: 存在者单单是存在者，它本身是不存在的。就是平庸主义者他会有这种想法。
- hit_reason: 明确指出“存在者单单是存在者，它本身是不存在的”，直接讨论了存在者本身的实存性问题。
- uncertainty_note: 这是一个哲学论断，指存在者本身缺乏独立于框架的实存基础。

### C6: 存在依赖性

- row_id: 72
- validation_status: `quote_exact_wrong_row`
- quote: 存在者本身不能够自己存在，就是存在者必须依靠这个标准、框架才能存在。
- hit_reason: 阐述了“存在者”的存在依赖于外部“标准/框架”，质疑了其自足的实存性。
- uncertainty_note: 强调了存在者不是独立实存的，而是依赖于某种结构才能被确立。
