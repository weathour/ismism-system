# W3 Fullscan Candidate Shard — 规范性 / 003

- term: 规范性
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 77 | `1-4-1-1` | 和平主义——拒斥一切暴力，所谓《无本体论的伦理学》 |
| 82 | `1-4-2-1` | 纵容主义——西欧发达国家的主流意识形态，白左的精神家园：“废除死刑”背后的意识形态阴谋 |
| 87 | `1-4-3-1` | 情绪主义——“情商”“情绪管理”“做人嘛开心最重要”背后的意识形态 |
| 88 | `1-4-3-2` | 心理正常主义——自以为“正常”，面对“反常”脱口而出“精神B”“神经B”“脑子有WT”的人所陷入的庸俗意识形态 |
| 105 | `2-1-2-2` | 理念实在论、理想现实主义——柏拉图：追求完美的形而上学，注定残酷的政治理想 |
| 106 | `2-1-2-3` | 范畴实在论、绝对现实主义——亚里士多德的把戏，老学究的帝师哲学，奴隶主的自我陶醉 |

## Candidate items

### C1: 规范性生成

- row_id: 77
- validation_status: `quote_exact`
- quote: 但是在这里面，我们是可以生成一种规范性的，没有客体的客体性。
- hit_reason: 直接提到了“规范性”的生成过程，是核心概念的讨论。
- uncertainty_note: 该句明确指出了规范性与无客体的客体性之间的关系。

### C2: 规范性来源

- row_id: 77
- validation_status: `quote_exact`
- quote: 由这个无客体的客体性出发，我们可以产生规范性。
- hit_reason: 明确指出“无客体的客体性”是产生“规范性”的出发点。
- uncertainty_note: 该句描述了规范性产生的逻辑起点。

### C3: 规范性生成

- row_id: 66
- validation_status: `quote_exact_wrong_row`
- quote: 但是在这里面，我们是可以生成一种规范性的，没有客体的客体性。
- hit_reason: 与 row_id=77 的内容重复，明确提到了“规范性”的生成。
- uncertainty_note: 该句再次强调了规范性在无客体的客体性中的生成。

### C4: 规范性生成

- row_id: 77
- validation_status: `quote_exact`
- quote: 但是在这里面，我们是可以生成一种规范性的，没有客体的客体性。
- hit_reason: 该句明确指出了规范性与无客体的客体性之间的关系。
- uncertainty_note: 该句是关于规范性概念的直接论述。

### C5: 规范性界定

- row_id: 82
- validation_status: `quote_exact`
- quote: 那么被宽容的那些就是不正常的、混乱的、污秽的、脆弱的。
- hit_reason: 在“宽容”的讨论中，将“被宽容的”与“不正常、混乱”等进行对立，涉及规范的划分。
- uncertainty_note: 此处通过列举“不正常”的特征来界定一种规范的边界。

### C6: 规范性局限

- row_id: 105
- validation_status: `quote_exact`
- quote: 它不能够普遍化的，也就说它经不起推敲的。
- hit_reason: 讨论了理念的完满性无法普遍化，这涉及到规范性原则的适用范围和局限。
- uncertainty_note: 此处讨论的是一种理想状态无法普遍化的局限性，与规范性相关。

### C7: 规范性维度

- row_id: 106
- validation_status: `quote_exact`
- quote: 它代表着一种规范性的维度nomative。就是这个事物，它自己都不知道自己要成为什么东西，但是它的本质知道。
- hit_reason: 直接使用了“规范性的维度nomative”这一术语，并解释了其含义。
- uncertainty_note: 该句是关于“规范性”维度（nomative）的直接定义和阐述。
