# W3 Fullscan Candidate Shard — 矛盾 / 015

- term: 矛盾
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 155 | `2-3-2-4` | 现代理性主义——一切现代哲学与科学的开端：笛卡尔为什么伟大，又在哪里蛇皮 |
| 156 | `2-3-3` | 单子主义——现代科学的形而上学基础：莱布尼兹是如何把笛卡尔的内在封闭的机械性转化为外在孤立的并列关系的 |
| 157 | `2-3-3-1` | 前定主义——为什么莱布尼兹不够莱布尼兹主义，而黑格尔才是真正的莱布尼兹主义 |
| 158 | `2-3-3-2` | 体系完美主义——沃尔夫并不那么蛇皮，他与康德可谓互有短长 |
| 159 | `2-3-3-3` | 逻辑原子主义——为什么罗素是一个蹩脚的前现代形而上学家 |
| 160 | `2-3-3-4` | 分割的整体主义——叔本华悲观主义背后的形而上学根源 |

## Candidate items

### C1: 逻辑转变

- row_id: 155
- validation_status: `quote_exact`
- quote: 所以在这里实现了一个矛盾，就是从logic of being变成了logic of essence，从存在的逻辑变成了本质的逻辑，变成了有一个构成性例外的逻辑。
- hit_reason: 直接提到了“矛盾”的实现，指从存在的逻辑到本质的逻辑的转变。
- uncertainty_note: 该段落描述了哲学逻辑上的一个结构性矛盾。

### C2: 矛盾论证

- row_id: 158
- validation_status: `quote_exact_wrong_row`
- quote: 康德在那边就已经推出两种矛盾了，这个我们后面讲到康德的时候会说到的。
- hit_reason: 提到了康德推导出的“两种矛盾”，与术语“矛盾”相关。
- uncertainty_note: 仅提及了矛盾的出现，未展开论述。

### C3: 逻辑矛盾

- row_id: 156
- validation_status: `quote_exact`
- quote: 它（我思）折射它（太一），它也折射它（反过来）。这种关系是一种不对称关系。因为按道理太一是包含了我思的，所以这个单子它就必须要是彼此封闭的，然后唯有一个太一是可以把它们统合到一块儿去了。就是也不叫统合它们，而是太一是这么一个单子，它对于其他东西的这个折射，就是维持其他东西的同一性，就是百分百、原原本本折射。
- hit_reason: 描述了单子论中，试图用一个整体来包含和折射其他部分时，可能出现的逻辑上的不一致或矛盾。
- uncertainty_note: 侧重于结构上的不一致性，可视为一种逻辑矛盾的体现。

### C4: 自相矛盾

- row_id: 157
- validation_status: `quote_exact`
- quote: 它无法实现一个所有东西都是被预先决定的一个效果，因为这个预先决定者pre-determiner，他的存在怎么样？他本身的存在就是个剩余。
- hit_reason: 指出了“预先决定”这一概念在逻辑上无法自我维持，存在内在的矛盾。
- uncertainty_note: 描述了预定论体系的逻辑上的自我矛盾。
