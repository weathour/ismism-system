# W6 Concept Drift Report — Sense Mixing Audit

- created: 2026-06-09 CST
- scope: MASTER-SPEC W6 item 1: sample 30 senses for definition/evidence alignment and check high-risk multi-sense overlap.
- status: PASS — no blocking sense-mixing issue found.

## 1. Thirty-Sense Alignment Sample

Sampling rule: deterministic even-spacing over current `knowledge/lexicon/term-senses.jsonl` after W3-B35.

| sense_id | term | sense label | quote rows | verdict |
|---|---|---|---|---|
| term:主体:s01 | 主体 | 矩阵中的主体侧维度 | 46,46 | PASS |
| term:人民:s02 | 人民 | 人民作为历史-理论链中的中介位 | 276,299,299 | PASS |
| term:物质:s02 | 物质 | 经验论中的反物质/外在异性他者 | 170,170 | PASS |
| term:目的论:s04 | 目的论 | 目的论缺失/秩序支配 | 95,95 | PASS |
| term:理论家:s01 | 理论家 | 理论家作为自指称位置 | 277,277 | PASS |
| term:误认:s02 | 误认 | 想象界认同的致命误认 | 258,258 | PASS |
| term:意识:s01 | 意识 | 清醒意识结构/四格对应 | 40,40 | PASS |
| term:客体化:s05 | 客体化 | 理论把现实对象化 | 285,285,285 | PASS |
| term:对象化:s03 | 对象化 | 本质直观的想象性对象化 | 192,192 | PASS |
| term:去本体论化:s01 | 去本体论化 | 主体化作为去本体论化 | 289,289 | PASS |
| term:去表象化:s04 | 去表象化 | 见独中的体验转后台空转 | 131,131 | PASS |
| term:重新中心化:s01 | 重新中心化 | 分裂整合为目的论 | 119,119 | PASS |
| term:本质:s02 | 本质 | 主体经验构造出的 eidos | 214,188 | PASS |
| term:目的论化:s03 | 目的论化 | 有限经济学的有序算计 | 268,268 | PASS |
| term:享乐:s01 | 享乐 | 可计数的资本主义数量池 | 7,7 | PASS |
| term:共同体:s02 | 共同体 | 科学话语生产机构 | 10,10 | PASS |
| term:学习:s01 | 学习 | 理论/现实连续活动中的 study | 285,285 | PASS |
| term:忠诚:s01 | 忠诚 | 对 truth-event 的保持 | 263,263 | PASS |
| term:方法论:s02 | 方法论 | 与逻辑/数学/知识论交织的范式层 | 11,11 | PASS |
| term:分析:s01 | 分析 | 观察同时进行的分析 | 285,285 | PASS |
| term:报告:s01 | 报告 | 现实研究的文献/材料来源 | 285,285 | PASS |
| term:权力关系:s02 | 权力关系 | 通俗化说明中的谁在掌握资源 | 285,285 | PASS |
| term:主体性:s01 | 主体性 | position/site 中被坚持的空位 | 263,263 | PASS |
| term:数学知识:s02 | 数学知识 | 通向本体论知识/site 的中间层 | 263,263 | PASS |
| term:命名活动:s02 | 命名活动 | 被压抑后重新呼唤的符号化 | 229,229 | PASS |
| term:星座:s01 | 星座 | constellation 的星丛同位名 | 229,229 | PASS |
| term:伪连续:s02 | 伪连续 | 局部断裂/总体连续的和谐假象 | 229,229 | PASS |
| term:客体化运动:s01 | 客体化运动 | 透明客体结构的驱动形式 | 229,229 | PASS |
| term:超定:s01 | 超定 | 互相矛盾的方程组状态 | 263,263 | PASS |
| term:艺术:s02 | 艺术 | politics 艺术家的幻想位 | 263,263 | PASS |

Audit reading rule: a sampled sense passes when its definition is narrower than, and directly supported by, its quoted source rows; broader synthesis is allowed only if the quoted row context supplies it.

## 2. High-Risk Multi-Sense Overlap Review

| term | senses | reviewed distinction | verdict |
|---|---:|---|---|
| 主体 | 4 | term:主体:s01=矩阵中的主体侧维度; term:主体:s02=先验/反思主体性; term:主体:s03=主体间性/人称化机制; term:主体:s04=无意识/驱力主体与去主体化 | PASS — labels/definitions keep distinct evidence contexts |
| 客体 | 4 | term:客体:s01=矩阵中的客体/实体侧维度; term:客体:s02=意向对象/noema 的客体极; term:客体:s03=小客体/客体小a; term:客体:s04=异化/物神化中的对象化客体 | PASS — labels/definitions keep distinct evidence contexts |
| 实践 | 5 | term:实践:s01=目的论中的行动/伦理姿态; term:实践:s02=第四主部的历史-政治实践场; term:实践:s03=人与物关系中的实践性; term:实践:s04=实践单元/可执行载体; term:实践:s05=运动式主动活动/避免异化 | PASS — labels/definitions keep distinct evidence contexts |
| 理论 | 5 | term:理论:s01=中介项（历史-人民-理论三元链）; term:理论:s02=符号系统性与历史性（任意性信号系统）; term:理论:s03=理论的生产性：生产主体、客体与客体化过程; term:理论:s04=理论与现实的对象化-主体化回路; term:理论:s05=理论的现实化/通俗化目的向（popularize） | PASS — labels/definitions keep distinct evidence contexts |
| 现实 | 2 | term:现实:s01=study the reality 的研究对象; term:现实:s02=使理论重新主体化的反常/突破点 | PASS — labels/definitions keep distinct evidence contexts |
| 事件性 | 4 | term:事件性:s01=第一人称时间视域的过程性; term:事件性:s02=持存的事件性存在; term:事件性:s03=创造历史的政治活动性; term:事件性:s04=数学本体论失败的主体缺口 | PASS — labels/definitions keep distinct evidence contexts |
| 星丛 | 2 | term:星丛:s01=符号化剩余/主导性概念; term:星丛:s02=不可消解的他者与离散实践场 | PASS — labels/definitions keep distinct evidence contexts |
| 数学化 | 2 | term:数学化:s01=意识形态减法后的处理; term:数学化:s02=还需矛盾张力和本体论化 | PASS — labels/definitions keep distinct evidence contexts |
| 本体论更新 | 2 | term:本体论更新:s01=Event 的版本更新过程; term:本体论更新:s02=主体化传输的外部更新 | PASS — labels/definitions keep distinct evidence contexts |
| 主客体 | 2 | term:主客体:s01=星丛协调的主体/客体关系; term:主客体:s02=拒绝表象化中介的关系 | PASS — labels/definitions keep distinct evidence contexts |
| 不可还原性 | 2 | term:不可还原性:s01=主体内在客体性不可还原; term:不可还原性:s02=否定辩证法面对的失败界限 | PASS — labels/definitions keep distinct evidence contexts |
| 真理显现方式 | 2 | term:真理显现方式:s01=本体论不可能/可能双重性中的四种方式; term:真理显现方式:s02=主体忠诚的四种方式 | PASS — labels/definitions keep distinct evidence contexts |
| Being | 2 | term:Being:s01=在场/服务器正常运行状态; term:Being:s02=不可数的多作为本体论起点 | PASS — labels/definitions keep distinct evidence contexts |
| Event | 2 | term:Event:s01=不在场/缺失侧的事件; term:Event:s02=版本更新/本体论版本更新 | PASS — labels/definitions keep distinct evidence contexts |
| site | 2 | term:site:s01=事件哲学发生学点位; term:site:s02=承接更新的空/剩余位置 | PASS — labels/definitions keep distinct evidence contexts |
| position | 2 | term:position:s01=主体性坚持的位置; term:position:s02=本体论剩余中的位置 | PASS — labels/definitions keep distinct evidence contexts |
| 名称 | 2 | term:名称:s01=显相为名字的符号化剩余; term:名称:s02=先验语音论中的发声维度 | PASS — labels/definitions keep distinct evidence contexts |
| 内在张力 | 2 | term:内在张力:s01=语言/历史语言中的命名张力; term:内在张力:s02=离散符号系统需被倾听的张力 | PASS — labels/definitions keep distinct evidence contexts |

## 3. Findings

- No sampled definition was found to assert a stronger claim than its evidence quotes support.
- High-risk terms with multiple senses remain separated by row context, axis, and `forbidden_mix` notes.
- New W3-B30–B35 terms are intentionally granular and remain draft; they should not be merged in W7 without preserving row provenance.

## 4. Required Corrections

None. No `confidence: low` edits required by this audit.
