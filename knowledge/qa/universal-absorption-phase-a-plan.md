# Universal Absorption Phase A Plan

- date: 2026-06-16
- batch_ids: `W3-UNIVERSAL-A-2026-06-16`, `W5-UNIVERSAL-A-2026-06-16`
- status: execution plan generated before writing W3/W5/W10 Phase A records; kept as audit trail after execution
- purpose: reduce W1/W2-only concentration by adding row-level W3/W5/W10 overlap to high-volume theoretically central rows, without creating a new theme layer.

## Baseline gap population

- baseline W1/W2-only rows: 109
- baseline W1/W2-only clean-text volume: 1037221
- selected Phase A full-overlap target rows: 60
- selected target clean-text volume: 743053 (71.6% of baseline W1/W2-only volume)
- selected fields: {'1': 11, '2': 25, '3': 20, '4': 4}

## Selection rules

1. Include every explicit high-priority W1/W2-only row in Rings A/B/C/D.
2. Fill remaining capacity by clean-text volume, with Field 2 and Field 3 thinness prioritized by the source prompt.
3. Exclude rows only by capacity/context: excluded rows remain in the gap map with `context-backlog` tier and later-phase rationale.
4. Keep W3/W5 status as `draft`; keep W10 status as `pilot-draft`.
5. Use exact quote substrings from declared `split_md_clean` paths for all evidence.

## Phase A target rows

| row | field | chars | toc | category | title |
|---:|---:|---:|---|---|---|
| 99 | 2 | 6913 | `2-1-1-1` | ancient-presence-metaphysics | 阿派朗（无界限）主义——哲学针对“地水火风”元素论的正面挑战 |
| 101 | 2 | 14471 | `2-1-1-3` | ancient-presence-metaphysics | 分形多元论——千古之谜：何为努斯？客观精神如何实体化？阿那克萨戈拉的分形几何与连续统思想 |
| 102 | 2 | 16587 | `2-1-1-4` | ancient-presence-metaphysics | 形而上辩证主义——赫拉克利特因何哭泣？火焰与灰烬的哲学，辩证法的开端 |
| 105 | 2 | 16766 | `2-1-2-2` | ancient-presence-metaphysics | 理念实在论、理想现实主义——柏拉图：追求完美的形而上学，注定残酷的政治理想 |
| 107 | 2 | 24972 | `2-1-2-4` | ancient-presence-metaphysics | 多产的不动论——如何理解四个芝诺悖论 |
| 109 | 2 | 8493 | `2-1-3-1` | ancient-presence-metaphysics | 反应多元论——要有多蠢，才会把恩培多克勒理解为四元素说 |
| 110 | 2 | 16719 | `2-1-3-2` | ancient-presence-metaphysics | 贫乏的原子论——太一分形，虚空降世，德谟克利特的笑与瞎 |
| 112 | 2 | 10427 | `2-1-3-4` | ancient-presence-metaphysics | 犬儒主义——真正的犬儒主义=极致的理性主义。安提斯泰尼与第欧根尼，苏格拉底的另类师徒孙 |
| 113 | 2 | 8503 | `2-1-4` | ancient-presence-metaphysics | 绝对主义——普罗泰格拉：“人是万物的尺度”，为什么是绝对主义，而不是相对主义？ |
| 114 | 2 | 13356 | `2-1-4-1` | ancient-presence-metaphysics | 相对主义——学会高尔吉亚的修辞学与辩护术，所有的辩论赛不过是游戏 |
| 115 | 2 | 12929 | `2-1-4-2` | ancient-presence-metaphysics | 怀疑主义——皮浪的哲学，智力英雄必备技能：探求“不动心”的平衡游戏；君主、辅臣、将领、幕僚的必修课 |
| 117 | 2 | 12194 | `2-1-4-4` | ancient-presence-metaphysics | 话语主义——在场形而上学的终结，对真理的解构性把握，最早的精神分析师：安提丰 |
| 159 | 2 | 18244 | `2-3-3-3` | logic-positivism-pragmatism | 逻辑原子主义——为什么罗素是一个蹩脚的前现代形而上学家 |
| 174 | 2 | 23898 | `2-4-2-2` | logic-positivism-pragmatism | 社会实证主义——现代社会学的形而上学背景是谁干的？涂尔干的局限与失败 |
| 179 | 2 | 13229 | `2-4-3-2` | logic-positivism-pragmatism | 逻辑还原主义——卡尔纳普在美国安身立命的吃饭家伙 |
| 183 | 2 | 12385 | `2-4-4-1` | logic-positivism-pragmatism | 逻辑实用主义——如何在学术界风生水起名利双收？奎因的小聪明形而上学 |
| 220 | 3 | 14423 | `3-2-2-3` | phenomenology-structure-language | 彻底的经验主义——最聪明的实用主义者威廉·詹姆斯，其实是一个平行进化的费希特主义者 |
| 190 | 3 | 12955 | `3-1-1` | phenomenology-structure-language | 先验现象学——胡塞尔的先验哲学计划 |
| 191 | 3 | 11825 | `3-1-1-1` | phenomenology-structure-language | 先验直觉主义——胡塞尔给所有意识普发的完整知识权，比经验主义更经验主义，比直觉主义更直觉主义，比先验主义更先验主义 |
| 218 | 3 | 12056 | `3-2-2-1` | phenomenology-structure-language | 理智直观主义——从先验主体性退回绝对整体主义，晚年费希特，怂了 |
| 241 | 3 | 15947 | `3-3-2-2` | phenomenology-structure-language | 诗性存在论——以诗代思，荷尔德林的癫疯循环 |
| 257 | 3 | 15614 | `3-4-1-1` | phenomenology-structure-language | 结构人本主义 |
| 260 | 3 | 13473 | `3-4-1-4` | phenomenology-structure-language | 陈述性的话语主义 |
| 270 | 3 | 15993 | `3-4-3-4` | phenomenology-structure-language | 局部的总体主义 |
| 58 | 1 | 14308 | `1-3-3-1` | everyday-ideology-normality | 自我中心主义——把人生当成修仙游戏，念叨“人不为己天诛地灭”，却被“我”这个字玩弄一辈子 |
| 60 | 1 | 12217 | `1-3-3-3` | everyday-ideology-normality | 排他的“集体主义”——冒充集体主义的自私，看似理性冷静的疯狂，自视宽容仁慈的邪恶 |
| 88 | 1 | 15356 | `1-4-3-2` | everyday-ideology-normality | 心理正常主义——自以为“正常”，面对“反常”脱口而出“精神B”“神经B”“脑子有WT”的人所陷入的庸俗意识形态 |
| 91 | 1 | 13223 | `1-4-4` | everyday-ideology-normality | 庸俗主义——人为什么会变得庸俗？变得比平庸更平庸。家里有娃的必看 |
| 92 | 1 | 11652 | `1-4-4-1` | everyday-ideology-normality | 顺从主义——“小人”的哲学，随大流、随波逐流、占小便宜、沾沾自喜、“人家都这样”背后的隐秘机制 |
| 252 | 3 | 13467 | `3-3-4-3` | phenomenology-structure-language | 幸福的幸存主义 |
| 175 | 2 | 13424 | `2-4-2-3` | logic-positivism-pragmatism | 自然神论的实证主义——斯宾塞的绅士哲学，绝非社会达尔文主义，亦非安那其先驱 |
| 211 | 3 | 12848 | `3-2` | phenomenology-structure-language | 复习课 |
| 157 | 2 | 12228 | `2-3-3-1` | metaphysics-system-backlog | 前定主义——为什么莱布尼兹不够莱布尼兹主义，而黑格尔才是真正的莱布尼兹主义 |
| 308 | 4 | 11731 | `4-2-2-2` | practice-coordination-backlog | 清楚的区分 |
| 269 | 3 | 11713 | `3-4-3-3` | phenomenology-structure-language | 倒错的好客主义 |
| 21 | 1 | 11431 | `1-1-4-2` | everyday-ideology-normality | 目的行为主义 |
| 316 | 4 | 11194 | `4-2-4` | practice-coordination-backlog | 再来一次！ |
| 282 | 4 | 11173 | `4-1-1-3` | practice-coordination-backlog | 国际性的理论协调 |
| 169 | 2 | 11118 | `2-4-1-2` | logic-positivism-pragmatism | 经验的观念论——“心灵是一块白板”绝大多数人都理解错了！洛克：观念论运动与先验哲学的伟大先驱 |
| 215 | 3 | 10981 | `3-2-1-3` | phenomenology-structure-language | 先验逻辑主义——“回到康德去”，真正的、死硬的唯心主义 |
| 225 | 3 | 10947 | `3-2-3-3` | phenomenology-structure-language | 生存论的存在主义（Existential Seynism）——与晚期谢林心心相印的晚期海德格尔 |
| 152 | 2 | 10885 | `2-3-2-1` | metaphysics-system-backlog | 理性动物主义 |
| 6 | 1 | 10844 | `1-1-1-2` | everyday-ideology-normality | 有机进化论 |
| 221 | 3 | 10818 | `3-2-2-4` | phenomenology-structure-language | 唯我的实在论、现实主义——早期维特根斯坦的《逻辑哲学论》是费希特先验唯我论迟到的讣告 |
| 259 | 3 | 10632 | `3-4-1-3` | phenomenology-structure-language | 分类性的叙事学 |
| 19 | 1 | 10554 | `1-1-4` | everyday-ideology-normality | 行为主义 |
| 265 | 3 | 10529 | `3-4-2-4` | phenomenology-structure-language | 螺旋的贱斥主义 |
| 66 | 1 | 10488 | `1-3-4-4` | everyday-ideology-normality | 颓废主义 |
| 52 | 1 | 10348 | `1-3-2` | everyday-ideology-normality | 本真主义——小布尔乔亚文青病的基本结构 |
| 154 | 2 | 10131 | `2-3-2-3` | metaphysics-system-backlog | 超越的内在论——路德据以掀起惊涛骇浪的现代精神 |
| 79 | 1 | 10115 | `1-4-1-3` | everyday-ideology-normality | 沉默主义——我们为什么会沉默？相互误解的两种沉默 |
| 167 | 2 | 10066 | `2-4-1` | logic-positivism-pragmatism | 经验主义——霍布斯的极简形而上学：利维坦和契约论的哲学基础 |
| 309 | 4 | 10057 | `4-2-2-3` | practice-coordination-backlog | 前沿注意 |
| 226 | 3 | 9741 | `3-2-3-4` | phenomenology-structure-language | 自身-辩证法——早期黑格尔 vs 晚期谢林，来看看黑格尔辩证法未成熟时是怎样的 |
| 205 | 3 | 9612 | `3-1-4` | phenomenology-structure-language | 现世的现象学——泰斗之背书：晚年狄尔泰重要的现象学“遗产” |
| 182 | 2 | 9572 | `2-4-4` | logic-positivism-pragmatism | 实用主义——杜威哲学的形而上学预设 |
| 239 | 3 | 9563 | `3-3-2` | phenomenology-structure-language | 真正的生存主义——以命代思、非此即彼的焚心以火者 |
| 264 | 3 | 9315 | `3-4-2-3` | phenomenology-structure-language | 哲学的墨守成规 |
| 158 | 2 | 9222 | `2-3-3-2` | metaphysics-system-backlog | 体系完美主义——沃尔夫并不那么蛇皮，他与康德可谓互有短长 |
| 145 | 2 | 9178 | `2-3` | metaphysics-system-backlog | 复习课 |

## Non-target handling

All remaining baseline W1/W2-only rows are preserved in `universal-absorption-phase-a-gap-map.jsonl` with explicit context/later-phase rationale. No row is promoted or excluded by title keyword alone.
