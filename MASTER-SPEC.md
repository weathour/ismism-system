# ISMISM 知识库消化总纲（MASTER SPEC）

- 创建日期：2026-06-03
- 最后更新：2026-06-03
- 适用仓库：`/home/weathour/文档/ismism-system`
- 维护权限：仅人工修改，agent 不得编辑本文档
- 合并关系：本文档是 AGENTS.md 的上级总纲；AGENTS.md 给行为规则，本文档给完整工作契约（目标 / 路线 / 质量标准 / 硬指标）

---

## 一、仓库身份与硬边界

### 本仓库是什么

ISMISM（主义主义）理论知识的消化引擎。核心任务：把一本 PDF 和 363 个 TOC 节点转化为**可追溯、可审计、可引用、可再综合的知识库**。

三个定位合一：
- 语料库（corpus repo）
- 理论训练库（theory-training repo）
- 诊断方法库 + agent/学者协作空间

依赖关系：不依赖任何外部仓库。W9 才考虑接入 psychoanalytic-writing-lab，且只做轻量索引。

### 本仓库不是什么

- 不是前端产品——不救旧 `src/`
- 不是哲学百科——不追求覆盖全部哲学史
- 不是人格诊断工具——不输出任何对人的诊断标签
- 不是 psychoanalytic-writing-lab 的附属——W9 之不做 ismism-system 的工作

### 硬边界

```
禁止在 /home/weathour/文档/ismism-system 外部的路径进行任何写操作。
```

### 内部纪律（非边界，但在任何时候都必须遵守）

- 不覆盖 `split_md/` 原始语料
- 不把 `Zhuyi_Matrix_Engine/Atlas_DB/*` 当 canonical truth
- 不把 W3/W5 draft 提升为 canonical（除非 W6 审计通过）
- 不处理 RMH/GJW 相关内容
- 不在 segment card 层写全局总论
- 不把 4×4×4×4 矩阵当成主体诊断表
- 不让旧前端原型（`src/`/`dist/`）牵引当前工作
- 不无证据地把外部理论并入 ISMISM
- 不在没有 term-sense 的情况下重用"主体/客体/实践/历史"等高风险词
- 不靠聊天历史替代文件状态作为真相来源
- 不跨期跳跃（如 W4 未完成即做 W7）
- 不修改 `Zhuyi_Matrix_Engine/` 下任何文件

---

## 二、当前状态快照

### 各层进度

| 层 | 完成 | 目标 | 状态 |
|---|---|---|---|
| W1 corpus manifests | 363/363 | 363 | 完成 |
| W2 segment cards | 363/363 | 363 | 完成 |
| W3 term senses | 31 条 / 9 词 | ~600 条 / 200 词 | draft |
| W4 position cards | 0 | 4 一级 + 16 二级 + 64 三级 + 172 四级 | 未做 |
| W5 relation assets | 12 条 | 60+ 条 | draft |
| W6 audit | 0 | 每期 1 份审计报告 | 未做 |
| W7 syntheses | 0 | 6 份综合 | 未做 |
| W8 usage protocol | 0 | 3 份协议文档 | 未做 |
| W9 integration | 0 | 1 份索引 | 未做 |

### 当前产物清单

- W1：`knowledge/manifests/corpus-manifest.json` / `segments.jsonl` (363) / `chunks.jsonl` (1594)
- W2：`knowledge/segment-cards/*.md` (363) / `index.md`
- W3：`knowledge/lexicon/term-senses.jsonl` (31 条) / `core-terms.md` / `ambiguous-terms.md` / `term-candidate-stats.tsv`
- W5：`knowledge/relations/relation-assets.jsonl` (12 条) / `route-cards.md` / `tension-cards.md` / `mediation-cards.md` / `boundary-cards.md` / `misrecognition-cards.md`
- QA：`knowledge/qa/w1-recovery-audit.md` / `w3-lexicon-audit.md` / `w5-relation-audit.md`

### 当前已拆术语（9 词 / 31 义项）

主体(4)  客体(4)  实践(5)  历史(5)  人民(5)  理论(5)  主体化(1)  客体化(1)  去主体化(1)

所有义项均为 `draft`，无 canonical。

---

## 三、最终完成判据（硬指标）

以下每一项都可以被脚本或人工验证。全部打勾才算"消化完成"。

### 术语层（W3）

```
□ term-senses.jsonl 包含 ≥ 200 个核心术语
□ 每个术语 2–5 个义项（总计 ≥ 500 条 sense record）
□ 每个义项含 ≥ 2 条 evidence_quotes
□ 每条 evidence_quote 可追溯到 split_md_clean 原文（子串匹配，可脚本验证）
□ 每个义项标注 axis 字段（场域 / 本体论 / 认识论 / 目的论 / 复合）
□ 每个义项标注 forbidden_mix 字段（不可混用说明）
□ ambiguous-terms.md 记录所有已识别的高风险交叠
□ 所有义项 status = draft（W6 审计通过前不升 canonical）
```

### 位置卡层（W4）

```
□ 4 张一级位置卡（每张 800–1500 字）
□ 16 张二级位置卡（每张 500–800 字）
□ 64 张三级位置卡（每张 300–500 字）
□ 172 张四级位置卡（每张 150–300 字）
□ 总计 256 张位置卡
□ 每张卡包含：位置定义、代表主义/学派、核心机制、与相邻位置的关系、关联术语列表
□ knowledge/position-cards/index.md 覆盖全部 256 个位置
□ 位置卡不含人格诊断语言
□ 位置卡不把"矩阵位"描述为"最终真理"
```

### 关系资产层（W5）

```
□ relation-assets.jsonl 包含 ≥ 60 条 relation
□ 覆盖全部 12 种关系类型（boundary-between, route-from-to, tension-between,
  mediates-between, transitions-to, blocks-transition, misrecognizes-as,
  objectifies, subjectivizes, overcodes, represents-position, evidences-claim）
□ 每条 relation 标注 source_position 和 target_position（引用 W4 位置卡坐标）
□ 每条 relation 含 ≥ 1 条 evidence_segment
□ 每条 relation 标注适用边界和禁止解释
□ 所有 relation 的 source/target 位置在 W4 位置卡中存在
```

### 综合层（W7）

```
□ 四个场域各一份综合（part-1-realism, part-2-metaphysics, part-3-idealism, part-4-praxis）
□ 一份全局系统图（whole-system-map.md）
□ 一份方法论核心（methodological-core.md）
□ 所有综合回链到 segment / term / position / relation
□ 所有综合无未溯源断言（每个论断必须标注来源）
```

### 使用协议层（W8）

```
□ usage-protocol.md（何时查术语 / 何时查位置 / 何时查关系）
□ query-playbook.md（10+ 条典型查询的标准路径）
□ export-manifest.md（外部系统调用接口定义）
```

---

## 四、七期消化路线

每一期的执行必须满足"前置条件"才能开始，必须通过"合格判据"才能进入下一期。

---

### 第一期：术语基础设施

| 项目 | 内容 |
|---|---|
| 前置条件 | W1/W2 已完成 |
| 输入 | `term-candidate-stats.tsv` + W2 segment cards + `split_md_clean/` |
| 输出 | `term-senses.jsonl` 从 31 条扩展到 ≥ 300 条 |

**批次规格**：
- 每批 2–3 个词
- 每批产出 5–15 条 sense
- 每两批跑一次 `ambiguous-terms.md` 更新

**内部阶段**：

```
A) 频率驱动（B6–B10）：实体、物质、意识形态、符号秩序、辩证法、意识、驱力、欲望、他者
   每词 3–5 义项 → 约 35 条

B) 共现驱动：每做完一批术语，扫描其 source_segments 中新浮现的未收录术语，加入候选池
   → 约 10 词 / 30 条

C) 轴术语：场域论、本体论、认识论、目的论——每词 2–3 义项
   → 4 词 / 10 条

D) 机制词补全：从 row 139 (2-2-4) 系统性扫描
   - 去客体化（基本操作）
   - 复合机制词：时间的主体化、空间的客体化、历史的对象化、物质的符号化、符号的实在化……
   → 约 15 词 / 30 条
```

**本期待产**：~45 词 / ~105 条 sense

**合格判据**：
```
□ term-senses.jsonl 记录 ≥ 300 条
□ 覆盖频率前 15 词（从 candidate-stats.tsv 验证）
□ 覆盖四个轴名的义项拆分
□ 覆盖 row 139 全套机制词（基本四操作 + ≥ 10 个复合机制词）
□ ambiguous-terms.md 无遗漏（所有已知交叠已记录）
□ 每一条 sense 的 evidence_quotes 子串匹配率 100%（脚本验证）
```

---

### 第二期：位置卡层（W4）——术语最大增量来源

| 项目 | 内容 |
|---|---|
| 前置条件 | W3 术语 ≥ 100 条 sense；轴术语（场域论/本体论/认识论/目的论）已拆分 |
| 输入 | W2 segment cards + `目录索引_结构化.csv` + W3 term-senses |
| 输出 | 256 张位置卡 + 一批新的结构和学派术语 |

**位置卡模板**（每张卡必须包含）：
```markdown
# 位置 [坐标] — [标题]

## 矩阵坐标
field: X  ontology: X  epistemology: X  teleology: X

## 位置定义
（该位置在 ISMISM 四轴中的理论含义）

## 代表主义/学派
（该位置映射到哪些思想传统 / 哲学家 / 流派）

## 核心机制
（该位置的关键理论操作）

## 与相邻位置的关系
（向哪个方向运动、从哪里来、往哪里去）

## 关联术语
（该位置使用的核心术语，标注已收录/待收录）
```

**优先级**：
```
L1：4 张一级强卡（场域 1-4，每张 800-1500 字）
L2：16 张二级卡（每张 500-800 字）
L3：64 张三级卡（每张 300-500 字）
L4：172 张四级轻卡（每张 150-300 字，可从 segment card 自动生成初稿再人工精炼）
```

**每张卡的术语产出规则**：
- 关联术语字段标注该位置使用的核心术语
- 待收录术语立即写入候选池
- 该位置所属的主义/学派名入 candidate stats 并排队

**本期待产**：~67 词（~25 结构术语 + ~30 学派术语 + ~12 位置特定概念）

**合格判据**：
```
□ 256 张位置卡全部完成
□ knowledge/position-cards/index.md 覆盖全部坐标
□ 每张卡有关联术语字段
□ 位置卡不含人格诊断语言
□ 位置卡不把"矩阵位"说成"最终真理"
```

---

### 第三期：关系资产层（W5）

| 项目 | 内容 |
|---|---|
| 前置条件 | W4 位置卡 ≥ 一级+二级（20 张）已完成；W3 术语 ≥ 50 词 |
| 输入 | W4 位置卡 + W2 segment cards + W3 term-senses |
| 输出 | 60+ 条 relation + 关系术语 |

**每批规格**：围绕一个 relation family，8–15 条

**内部阶段**：

```
B2) route family：庄子八步、黑格尔辩证运动、拉康三界转换、观念论→实践路径……
    → 6–10 条路径，每条路径的步骤动词自动成为关系术语

B3) tension family：各位置间的结构性矛盾
    → 如 2-2-2-2(庄子) 与 4-1-1-1(庸俗唯物论) 的张力

B4) boundary family：场域之间如何过渡、哪些过渡不可逆
    → 边界、闭合、敞开、跨越……

B5) mediation family：中介关系的完整拓扑
    → 中介、中介项、中介化、去中介化……

B6) misrecognition family：误认链
    → 误认、意识形态幻象、符号化遮蔽……

B7) mechanism 关系：主体化/客体化/去主体化/去客体化 与 历史/实践/理论 的关系方向
```

**本期待产**：~30 词（关系/过程术语）

**合格判据**：
```
□ relation-assets.jsonl 记录 ≥ 60 条
□ 全部 12 种关系类型有 ≥ 2 条实例
□ 每条 relation 的 source/target 在 W4 位置卡中存在
□ 每条 relation 有 evidence_segment
□ 关系不写"必然"（仅写"可发生""常出现"）
□ 关系不跨越不存在的矩阵坐标
```

---

### 第四期：审计与纠偏（W6）

| 项目 | 内容 |
|---|---|
| 前置条件 | W3/W4/W5 各有足够产出 |
| 输入 | 全部 knowledge/ 层产物 |
| 输出 | 审计报告 + 低置信度标记 + 修正建议 |

**审计项目**（每项产出一份报告）：

```
1) 义项混用审计
   - 抽查 30 条 sense，检查 definition 是否与 evidence_quotes 对齐
   - 检查是否有两个义项的 definition 在核心含义上重叠

2) 关系过强审计
   - 抽查 20 条 relation，检查是否把"可能"写成"必然"
   - 检查是否有单向关系被写成双向

3) 证据链完整性
   - 随机抽 10 个义项，追溯到 split_md_clean 原文验证
   - 检查 source_segments 路径是否全部存在

4) 禁止事项复核
   - 对照本文档的禁止事项清单逐条验证
   - 检查是否使用了 Atlas_DB 作为 canonical 证据
   - 检查位置卡是否含人格诊断语言
```

**处理方式**：审计不达标的不删除，只标注 `confidence: low` + `audit_notes`，留到 W7 综合时修正。

**合格判据**：
```
□ 四项审计全部完成并输出报告
□ 无阻断级问题（如有，必须在进入 W7 前修复）
□ 所有不达标义项已加 low confidence 标记
```

---

### 第五期：综合层（W7）

| 项目 | 内容 |
|---|---|
| 前置条件 | W6 审计无阻断问题；W4 位置卡 ≥ 一级+二级；W5 关系 ≥ 40 条 |
| 输入 | 全部 knowledge/ 层产物 |
| 输出 | 6 份综合 + 方法论术语 |

**产出清单**：

```
1) part-1-realism.md        场域 1（实在论）综合
2) part-2-metaphysics.md    场域 2（形而上学）综合
3) part-3-idealism.md       场域 3（观念论）综合
4) part-4-praxis.md         场域 4（实践）综合
5) whole-system-map.md      全局系统图：四场域间的运动 +
                            ISMISM 自身在矩阵中的坐标
6) methodological-core.md   方法论核心：如何使用矩阵做思想诊断
```

**每份综合的强制回链要求**：每个论断必须标注来源，格式为 `[row X, term:Y:sZ, position A-B-C-D]`。

**本期待产**：~15 词（方法论/操作术语：诊断、回溯、映射、打开、压缩、折叠、展开、遍历、闭合度、连贯性……）

**合格判据**：
```
□ 6 份综合全部完成
□ 所有论断有来源标注
□ 无未溯源断言
□ 方法论术语已入 term-senses.jsonl
```

---

### 第六期：使用协议（W8）

| 项目 | 内容 |
|---|---|
| 前置条件 | W7 综合完成 |
| 输入 | 全部 knowledge/ 层产物 |
| 输出 | 3 份协议文档 |

**产出清单**：

```
1) usage-protocol.md    agent 使用手册：何时查术语 / 何时查位置 / 何时查关系
2) query-playbook.md    10+ 条典型查询的标准路径
                        （如"这个主义在矩阵的哪个位置？""康德到黑格尔如何运动？"）
3) export-manifest.md   外部系统调用接口定义
```

**合格判据**：
```
□ 三份文档全部完成
□ query-playbook 至少 10 条典型查询
□ export-manifest 定义清晰的接口契约
```

---

### 第七期：接入精神分析写作（W9）

| 项目 | 内容 |
|---|---|
| 前置条件 | W8 完成 |
| 输入 | 本仓库全部 knowledge/ 层 |
| 输出 | psychoanalytic-writing-lab 中的轻量索引 |

```
□ psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md
□ 只做坐标映射和术语索引，不复制全库
```

---

## 五、质量门

每个工作期结束时必须通过对应门禁才能进入下一期。门禁项均可验证。

### W3 门

```
□ evidence_quotes 子串匹配率 100%（脚本验证）
□ source_segments 路径全部存在（脚本验证）
□ 无义项定义互相矛盾（人工抽查 20%）
□ forbidden_mix 字段无空值
□ sense_id 格式符合 term:<词>:s<序号>
```

### W4 门

```
□ 每张卡有关联术语字段
□ 位置卡数 = 目标数
□ 位置卡不含人格诊断语言
□ 位置卡不把"矩阵位"说成"最终真理"
```

### W5 门

```
□ source/target 位置在 W4 中存在
□ 关系不写"必然"
□ 关系不跨越不存在的位置（如 5-x-x-x）
□ 每条 relation 有 evidence_segment
```

### W6 门（贯穿）

```
□ 每项审计产出独立报告
□ 无阻断问题遗留
```

### W7 门

```
□ 所有论断有来源标注
□ 无未溯源断言
```

---

## 六、Agent 标准操作流程

### 首次进入仓库

```
1. 读 AGENTS.md
2. 读 本文档（MASTER-SPEC.md）
3. 读 knowledge/STATE.md（确认当前进度）
4. 读 ISMISM-MAINLINE-HANDOFF.md
5. 判断当前处于哪个工作期
```

### 每批次操作（标准 6 步）

```
1. 读 STATE.md 的 Active Batch 行，确认本批任务
2. 执行本批任务（生成产物文件）
3. 跑对应质量门脚本验证
4. 更新 STATE.md（进度计数器 + 下一批锚点）
5. 更新 knowledge/logs/operation-log.md
6. 如本批发现新的候选术语，写入候选池
```

### 上下文压缩恢复

```
1. 读 AGENTS.md
2. 读 本文档 第二节（当前状态快照，以文件实际内容为准）
3. 读 STATE.md 的 Handoff Block
4. 从 Next Action 继续
5. 不要依赖聊天历史
```

### Agent 禁止行为

```
- 不依赖聊天历史恢复任务状态（必须读文件）
- 不在没有读 STATE.md 的情况下开始新批次
- 不跨期操作（前置条件不满足即拒绝）
- 不修改本文档（MASTER-SPEC.md）
- 不在 /home/weathour/文档/ismism-system 以外写文件
```

---

## 七、文件体系契约

| 文件 | 职责 | 谁可以写 | 读取时机 |
|---|---|---|---|
| `AGENTS.md` | 行为规则 | 仅人工 | 首次必读 |
| `MASTER-SPEC.md`（本文档） | 总纲 + 硬指标 + 路线 | 仅人工 | 首次必读 |
| `ISMISM-MAINLINE-HANDOFF.md` | 主线交接说明 | 人工/agent | 恢复时必读 |
| `knowledge/STATE.md` | 进度 + 批次锚点 | agent（每批更新） | 每批必读 |
| `knowledge/DIGESTION_PROGRAM.md` | 消化蓝图 | 仅人工 | 首次必读 |
| `knowledge/logs/operation-log.md` | 操作日志 | agent（每批追加） | 审计时读 |
| `knowledge/lexicon/term-senses.jsonl` | 术语义项（机器） | agent（每批追加） | 术语查询 |
| `knowledge/lexicon/core-terms.md` | 术语义项（人类索引） | agent（每批更新） | 术语浏览 |
| `knowledge/lexicon/ambiguous-terms.md` | 歧义风险注记 | agent（每两批更新） | 防混用 |
| `knowledge/lexicon/term-candidate-stats.tsv` | 频率统计 | 仅脚本生成 | 候选词参考 |
| `knowledge/relations/relation-assets.jsonl` | 关系资产 | agent（每批追加） | 关系查询 |
| `knowledge/segment-cards/*.md` | 分段卡 | agent（W2） | 证据查证 |
| `knowledge/position-cards/*.md` | 位置卡 | agent（W4） | 坐标查询 |
| `split_md_clean/*.md` | 干净语料 | 仅人工 | 证据追溯 |
| `split_md/*.md` | 原始语料 | 禁止写入 | 证据最终仲裁 |
| `目录索引_结构化.csv` | TOC 结构 | 只读 | 坐标映射 |
| `Zhuyi_Matrix_Engine/Atlas_DB/*` | 历史候选 | 禁止写入 | 仅参考 |
| `src/` `dist/` | 旧前端 | 禁止触碰 | 禁止 |

---

## 八、术语义项 Schema（强制规范）

每条 term-sense record 必须包含以下全部字段。验证脚本 `knowledge/scripts/validate_term_senses.py` 会在每批完成后自动检查。

### 必填字段

```
sense_id          格式: "term:<词>:s<序号>"        例: "term:主体:s01"
term              中文词源                           例: "主体"
sense_label       义项名（≤ 15 字）                  例: "矩阵中的主体侧维度"
definition        定义（50–300 字）
axis              轴归属: 场域 | 本体论 | 认识论 | 目的论 | 复合
evidence_quotes   数组，每项: {row_id: int, quote: str}
                  每个义项 ≥ 2 条
source_segments   数组，每项: {segment_id, row_id, toc_id, title,
                  segment_card_path, clean_md_path}
                  每个义项 ≥ 1 个 source segment
contrast_with     数组，列出不可混用的其他 sense_id
forbidden_mix     中文说明：不要把该义项当成什么（必填，不可为空）
confidence        "high" | "medium" | "low"
status            "draft" | "reviewed" | "canonical" | "rejected"
audit_notes       审核备注（可空字符串但不可缺字段）
schema_version    固定: "w3.term-sense.v0.1"
batch_id          格式: "W3-B<序号>-YYYY-MM-DD"
created           日期 "YYYY-MM-DD"
updated           日期 "YYYY-MM-DD"
```

### 验证要求

```bash
python3 knowledge/scripts/validate_term_senses.py
```

检查项：
- 必填字段完整性（缺字段 → fail）
- evidence_quotes 每条 quote 在对应 clean_md 中可子串匹配（不匹配 → fail）
- source_segments 每个路径存在（路径不存在 → fail）
- sense_id 格式符合 `term:<词>:s<序号>`（格式错误 → fail）
- forbidden_mix 字段非空（为空 → fail）

---

## 九、最终术语构成目标

| 品类 | 目标数量 | 主要来源 |
|---|---|---|
| 知识本体术语（主体、客体、实体、物质、意识、驱力、欲望……） | ~55 | W3 频率/共现驱动 |
| 结构术语（场域、轴、维度、闭合、敞开、场域转换……） | ~25 | W4 位置卡强制标注 |
| 学派/主义术语（现象学、实证主义、辩证法、先验观念论……） | ~30 | W4 位置卡标题 + 关联字段 |
| 机制术语（客体化、去主体化、去客体化 + 复合机制词……） | ~45 | W3 + row 139 展开 + W5 |
| 关系/过程术语（中介、跃迁、张力、误认、边界……） | ~30 | W5 关系资产命名 |
| 方法论/操作术语（诊断、回溯、映射、打开、压缩……） | ~15 | W7 综合驱动 |

**总计 ~200 词 / ~500–600 条义项**

---

*文档结束。任何 agent 进入仓库后必须先读本文档。*
