# W3 Fullscan Candidate Shard — 生活 / 004

- term: 生活
- batch_candidate: W3-fullscan-gemma4-50h
- status: candidate-only
- do_not_import_directly: true
- model: gemma4:latest

## Rows in shard

| row_id | toc_id | title |
|---:|---|---|
| 38 | `1-2-3-2` | 回归式唯灵论 |
| 39 | `1-2-3-3` | 魔法师主义——为什么魔法归根结底是一种自恋的、倒错的癔症 |
| 40 | `1-2-3-4` | 弃绝主义——解脱痛苦追求涅槃：意识的符号学机制 |
| 41 | `1-2-4` | 反偶像论——揭秘“信仰钢印”背后的意识形态机制 |
| 42 | `1-2-4-1` | 作为信仰的命定论——如何用哲学理解祥林嫂？ |
| 44 | `1-2-4-3` | 神智论 |

## Candidate items

### C1: 具身生活

- row_id: 38
- validation_status: `quote_not_found_in_shard`
- quote: 他们还是过一种生命性的生活，具身性的一种生活，具身性的生活，它还是成为具身性的存在。
- hit_reason: 直接提到了“生命性的生活”和“具身性的生活”，与“生活”高度相关。
- uncertainty_note: 该描述侧重于存在状态，但明确指出了生活方式的维度。

### C2: 共同体生活

- row_id: 38
- validation_status: `quote_exact`
- quote: 他们追求的不是长生，而是追求：就算我肉体死亡也没事儿。他们认为肉体死亡也没事。因为不追求长生，实际上他们不追求过共同的生活、过人类共同体生活、凡俗的人类共同体生活。
- hit_reason: 明确提到了“共同的生活”、“人类共同体生活”和“凡俗的人类共同体生活”，是关于群体生活状态的描述。
- uncertainty_note: 描述的是不追求某种生活状态，但指出了生活共同体的概念。

### C3: 具身生活

- row_id: 39
- validation_status: `quote_exact_wrong_row`
- quote: 他还是过一种生命性的生活，具身性的一种生活，具身性的生活，它还是成为具身性的存在。
- hit_reason: 与 row_id=38 的内容重复，再次强调了“生命性的生活”和“具身性的生活”，是关于生活状态的描述。
- uncertainty_note: 重复的证据，但内容指向“生活”的具身性层面。

### C4: 生活方式

- row_id: 39
- validation_status: `quote_exact`
- quote: 他追求的是一种生活方式。但是他又不是和共同体融洽相处的。在列维对于magician的生活方式的描述，他会明确说这些肯定是惹人厌的、会被人误解的、会受人讨厌的。
- hit_reason: 直接使用了“生活方式”这一词汇，并描述了其在社会互动中的状态。
- uncertainty_note: 侧重于社会接受度，但核心讨论的是一种生活方式。

### C5: 共同体生活

- row_id: 39
- validation_status: `quote_exact`
- quote: 他也是觉得在共同体里面让自己受益是有意义的，无论如何magician是觉得过共同体生活、过凡俗生活是有一定的意义的。
- hit_reason: 明确提到了“共同体生活”和“凡俗生活”，是关于社会融入和生活意义的讨论。
- uncertainty_note: 指出了在共同体中生活的重要性，是关于社会生活维度的。

### C6: 命运承受

- row_id: 42
- validation_status: `quote_exact`
- quote: 他本来有个盼头，盼头在这种命运面前、痛苦的命运面前，啥都不是。这种创伤不是一般人能承受得了的。
- hit_reason: 描述了在巨大创伤面前，个体对未来生活（盼头）的脆弱性，涉及生命体验的极限。
- uncertainty_note: 侧重于心理承受力，但与生命体验的脆弱性相关联。
