# W3 Fullscan Candidate Shard — 矛盾 / 008

- term: 矛盾
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 92 | `1-4-4-1` | 顺从主义——“小人”的哲学，随大流、随波逐流、占小便宜、沾沾自喜、“人家都这样”背后的隐秘机制 |
| 93 | `1-4-4-2` | 粗俗主义——爱说脏话的色鬼和赌狗的意识形态，及其产生的原因 |
| 94 | `1-4-4-3` | 四重竞争主义——赢！胜利！牛逼！厉害！666！“争强好胜”的四种形式：胜利主义、躺赢主义、完胜主义与对抗 |
| 96 | `2` | 形而上学——古代贵族的精神冒险，背景性的符号秩序与它自己的对立，比下（形而下学）有余，比上（观念论）不足 |
| 98 | `2-1-1` | 普遍主义——泰勒斯真正的宝藏，哲学、科学、数学、逻辑学的共同本源 |
| 100 | `2-1-1-2` | 气动一元论——阿那克西美尼的哲学制毡术，气象万千之中隐藏的秘密 |

## Candidate items

### C1: 自相矛盾

- row_id: 92
- validation_status: `quote_exact`
- quote: 他甚至会自相矛盾：这边占了一点小便宜，那边又其实让自己吃了大亏；那边又占了点小便宜，又让自己吃了大亏；那边自以为占了点小亏可以占大便宜，那么其实又又是就那个小亏，就亏到底了。
- hit_reason: 直接描述了行为上的矛盾和不一致性。
- uncertainty_note: 描述了行为上的不一致性，与矛盾概念相关。

### C2: 矛盾

- row_id: 93
- validation_status: `quote_exact`
- quote: 这两个东西之间的矛盾就不会被体验，就是他的父亲就是理应当服从于大家长所设定的这个秩序。
- hit_reason: 明确指出了两个概念（父亲和大家长）之间存在未被体验的矛盾关系。
- uncertainty_note: 指出了两种角色设定的内在矛盾。

### C3: 对立与调和

- row_id: 45
- validation_status: `quote_exact_wrong_row`
- quote: 小便宜和大满足，不知道这两个对立的可以去看一杠1-4-4-2。这两个东西被调和，它被一个东西调和。
- hit_reason: 提到了“小便宜”和“大满足”这两个对立的维度，并讨论了它们被调和的过程。
- uncertainty_note: 讨论了两个对立维度（小便宜和大满足）的调和。

### C4: 零和博弈

- row_id: 94
- validation_status: `quote_exact`
- quote: 它既要获得欲望的满足，也要获得需求的满足。那这个东西岂是这么容易满足的？不是的。它必须通过抢走别人的，实际上它是在抢走别人的份额，它必须是一种竞争，而且它是一种零和博弈，这种叫不死不休的那种。
- hit_reason: 描述了竞争的本质是零和博弈，这本身就包含了一种对立和矛盾的结构。
- uncertainty_note: 描述了竞争的零和性质，暗示了对立面。

### C5: 敌对/反抗

- row_id: 20
- validation_status: `quote_not_found_in_shard`
- quote: 它就是持一个对于竞争本身、对于这个 antagonism，对于这个东西本身是 anti，持一个敌对的，就是他反抗，就反抗。
- hit_reason: 明确使用了“antagonism”（敌对）和“反抗”的概念，指向了对立面。
- uncertainty_note: 指出了对竞争本身的敌对立场，是矛盾的体现。

### C6: 二重化

- row_id: 96
- validation_status: `quote_exact`
- quote: 背景性秩序的内在二重化，比如说它分成两个部分，一个是Fate（命运）；还有一个是Economy（场域）。命运是秩序本身、符号学的强力、律令（law）的维度，而这个economy，把它写成场域本身，其实是society的维度、共同体的维度。
- hit_reason: 明确指出了背景性秩序的“内在二重化”，即Fate和Economy的对立结构。
- uncertainty_note: 指出了结构层面的二分法和对立。

### C7: 对抗/斗争

- row_id: 100
- validation_status: `quote_exact`
- quote: 而universal就是global capitalism它会导致universal Struggle，有这么一种struggle，或者说一种antagonism，就会有一种普遍的一种对抗，一种斗争，在这个global，贯穿于这个global capitalism道理的。
- hit_reason: 提到了“struggle”和“antagonism”，指出了普遍层面的对抗性。
- uncertainty_note: 指出了普遍层面的对抗性，与矛盾相关。
