# W3 Fullscan Candidate Shard — 自由 / 005

- term: 自由
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 51 | `1-3-1-4` | 唯梦论——人生如梦，一樽还酹江月的哲学；兼论梦在主体性与主体间性上的核心特征 |
| 53 | `1-3-2-1` | 现代斯多亚主义——文化多元主义所炮制的古典学致幻剂 |
| 54 | `1-3-2-2` | 现代犬儒主义——工薪阶层最容易陷入的意识形态陷阱 |
| 55 | `1-3-2-3` | 现代爱情主义，现代新柏拉图主义——现代爱情背后的哲学，我们这个时代的罗曼斯崇拜 |
| 58 | `1-3-3-1` | 自我中心主义——把人生当成修仙游戏，念叨“人不为己天诛地灭”，却被“我”这个字玩弄一辈子 |
| 59 | `1-3-3-2` | 道德严酷主义——内在糜烂的道学先生，大他者的享乐工具，扣在康德头上的臭痰盂 |

## Candidate items

### C1: 个体自由

- row_id: 51
- validation_status: `quote_exact`
- quote: 主观唯心主义是站到一个体这边、个体的自由这里。
- hit_reason: 直接提到了“个体的自由”这一概念，与“自由”高度相关。
- uncertainty_note: 无法判断该“自由”是哲学上的绝对自由还是其他层面的自由。

### C2: 个人良心

- row_id: 51
- validation_status: `quote_exact`
- quote: 主观唯心主义是站在了个人良心这一边。
- hit_reason: 强调了“个人良心”的立场，这与个体自主和自由意志相关。
- uncertainty_note: 无法判断“个人良心”所代表的自由的边界和性质。

### C3: 个体自由

- row_id: 51
- validation_status: `quote_exact`
- quote: 主观唯心主义是站到一个体这边、个体的自由这里。
- hit_reason: 重复强调了“个体的自由”这一核心概念。
- uncertainty_note: 无法判断该“自由”是哲学上的绝对自由还是其他层面的自由。

### C4: 自由意志

- row_id: 13
- validation_status: `quote_exact_wrong_row`
- quote: 梦境里面的自我已经不是一个非常自由意识、自由意志意义上的自我，而是一种某种意义上他者化的自我。
- hit_reason: 明确讨论了“自由意志”的缺失和“他者化”的自我状态，与自由概念相关。
- uncertainty_note: 无法判断梦境中的“自由意志”与现实中的自由意志有何本质区别。

### C5: 自我认知

- row_id: 13
- validation_status: `quote_not_found_in_shard`
- quote: 梦境里面的自我，你醒来之后你都不太认识自己，竟然做了那么多疯狂的、没有理性的、不讲道理的事情。
- hit_reason: 描述了自我行为的非理性，暗示了主体控制和自由意志的缺失。
- uncertainty_note: 无法判断这种“不讲道理”的行为是否可以归类为一种自由的体现或丧失。

### C6: 潜在自由

- row_id: 54
- validation_status: `quote_exact`
- quote: 真正的虚伪在于“我本可以”。
- hit_reason: 指出了“我本可以”这一幻想，这是关于主体潜在自由选择的讨论。
- uncertainty_note: 无法判断“我本可以”的自由选择是否是真正的自由，还是纯粹的意识形态构建。

### C7: 自由选择

- row_id: 54
- validation_status: `quote_exact`
- quote: 这种自由选择，这种“我本来可以”撤销我虚伪的操作，我可以当这一切没发生。
- hit_reason: 直接提到了“自由选择”的概念，是讨论意识形态批判的核心点。
- uncertainty_note: 无法判断这种“自由选择”是否能真正实现主体摆脱意识形态的束缚。

### C8: 主体自由

- row_id: 59
- validation_status: `quote_exact`
- quote: 理性高于意志，在康德那边理性和主体的自由是高于意志。
- hit_reason: 明确指出“主体的自由”高于意志，这是哲学层面的自由论述。
- uncertainty_note: 无法判断康德所指的“自由”在现代语境下是否等同于我们日常理解的自由。
