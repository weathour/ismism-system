# W3 Fullscan Candidate Shard — 误认 / 001

- term: 误认
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 2 | `1-1` | 科学实在论 |
| 9 | `1-1-2` | 建构论 |
| 45 | `1-2-4-4` | 神爱论，神圣的爱——永不失败的“爱情”：对大他者的一厢情愿 |
| 58 | `1-3-3-1` | 自我中心主义——把人生当成修仙游戏，念叨“人不为己天诛地灭”，却被“我”这个字玩弄一辈子 |
| 85 | `1-4-2-4` | 性解放主义——【爱欲经济学】5、性倒错的种类和机制：人道主义必然走向的虚无主义 |
| 91 | `1-4-4` | 庸俗主义——人为什么会变得庸俗？变得比平庸更平庸。家里有娃的必看 |

## Candidate items

### C1: 知识误认

- row_id: 2
- validation_status: `quote_exact`
- quote: 他甚至都不知道这是知识，或者他们都误认了这个知识。
- hit_reason: 直接提到了“误认了这个知识”，与术语高度相关。
- uncertainty_note: 指代的是知识的误认，但未说明误认的具体内容。

### C2: 概念误用

- row_id: 9
- validation_status: `quote_exact`
- quote: 一些蛇皮笨蛋对于德里达的一个，或者说对于结构的运动解构这个概念的一些误用、一些误认、误知。
- hit_reason: 明确提到了“误用、一些误认、误知”，指向概念层面的错误认知。
- uncertainty_note: 指代的是对德里达概念的误用和误认，范围较广。

### C3: 认知误认

- row_id: 58
- validation_status: `quote_exact`
- quote: 这些子女误认了一点，就是你的父亲 actually 他是 1-3-3-1。
- hit_reason: 明确指出“子女误认了一点”，指代了对父亲身份或状态的错误认知。
- uncertainty_note: 误认的对象是关于父亲身份的认知，但缺乏具体描述。

### C4: 错误认知

- row_id: 91
- validation_status: `quote_exact`
- quote: 这个东西他就只能是一种错误、犯错、误认，或者是就是压抑的不行了。
- hit_reason: 提到了“错误、犯错、误认”，属于认知层面的错误判断。
- uncertainty_note: 指代的是一种状态或行为的错误认知，上下文较为抽象。
