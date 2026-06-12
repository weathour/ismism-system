# W3 Fullscan Candidate Shard — 现象 / 016

- term: 现象
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 179 | `2-4-3-2` | 逻辑还原主义——卡尔纳普在美国安身立命的吃饭家伙 |
| 180 | `2-4-3-3` | 逻辑行为主义——日常语言学派是如何继续逻辑实证主义的勾当的 |
| 183 | `2-4-4-1` | 逻辑实用主义——如何在学术界风生水起名利双收？奎因的小聪明形而上学 |
| 184 | `2-4-4-2` | 正统辩证唯物主义——原来“形而上学”才是真正的辩证法：论辩证法的片面、静止、只有量变和二元对立 |
| 185 | `2-4-4-3` | 符号实用主义——何为语言：只要会说话就一定会掌握的一门形而上学；共同体在现代化中必然采取的符号学策略 |
| 186 | `2-4-4-4` | 生存实用主义——揭秘禅宗的奥秘，参话头技术指南，前现代的分析师话语 |

## Candidate items

### C1: 感官体验

- row_id: 183
- validation_status: `quote_exact_wrong_row`
- quote: 一开始是现象主义，我第一人体验到的感官现象才是合法。
- hit_reason: 直接提到了“现象主义”和“第一人体验到的感官现象”，与“现象”高度相关。
- uncertainty_note: 指代的是哲学流派的观点，但核心概念是“现象”。

### C2: 内在报告

- row_id: 179
- validation_status: `quote_exact`
- quote: 你这里面的 logical 那些句法为什么具有优先性？我求求你告诉我，你那个真值表为什么具有优先性？真值表那种方法，这一系列的方法为什么在你自己内在心理当中的第一人称报告里面具有优先性？
- hit_reason: 提到了“第一人称报告”和“内在心理”，这是描述现象学关注的经验层面。
- uncertainty_note: 讨论的是优先性，但核心讨论对象是第一人称的经验报告。

### C3: 现象主义

- row_id: 179
- validation_status: `quote_exact`
- quote: 左边是现象主义、观念连接主义，或者说约定主义。
- hit_reason: 直接点明了“现象主义”这一哲学流派，与“现象”概念直接相关。
- uncertainty_note: 指代的是一种哲学立场，而非具体的现象本身。

### C4: 物理主义

- row_id: 179
- validation_status: `quote_not_found_in_shard`
- quote: 右边就是这个物理主义。什么东西可以算它合法的材料？
- hit_reason: 在对比现象主义后提出的对立面，讨论的是可被接受的“材料”，与经验观察相关。
- uncertainty_note: 侧重于对物理主义的描述，但上下文是关于合法材料的讨论。

### C5: 现象生成

- row_id: 186
- validation_status: `quote_exact`
- quote: 万法成办，或者说是你可以看着这里是一种唯识论的一种极简版经验主义观念论，就是差不多是贝克莱的一个极简版。眼色而生，万法成办，通过底层的感受性的东西就能够汇集成各式各样的现象。
- hit_reason: 明确提到了“现象”的生成过程，并与“感受性的东西”联系起来。
- uncertainty_note: 描述的是一种哲学模型，但核心是“现象”的汇集。

### C6: 直接体验

- row_id: 186
- validation_status: `quote_exact`
- quote: 你只要有体验，就已经悟了，不要再去想体验背后有啥了不起的东西。
- hit_reason: 强调“体验”本身就是“悟”，指向了对直接经验（现象）的关注。
- uncertainty_note: 这是对认知过程的指导性描述，但核心是“体验”这一现象。
