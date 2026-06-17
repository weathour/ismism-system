# ISMISM 全库消化纲领（v1）

- 创建日期：2026-05-08
- 适用仓库：`/home/weathour/文档/ismism-system`
- 执行环境：Codex + GPT-5.3 Spark（长程批处理）
- 总目标：将失败的 ISMISM 交互系统拆解并重建为一个可检索、可审计、可引用、可再综合的理论参照知识库。

## 0. 根本判断

ISMISM 当前不是一个应该被“继续救活”的前端产品，而是一个已经完成大量预处理的理论语料库。新的任务不是复活原来的 app，而是建立一个稳定的知识处理层：

```text
PDF / TOC / split_md / split_md_clean
→ corpus manifest / segment registry / chunk registry
→ segment cards
→ term senses
→ matrix position cards
→ relation assets
→ syntheses / usage protocol
→ 后续按需接入 psychoanalytic-writing-lab
```

本纲领的核心纪律：**先固定证据层，再生成解释层；先做可追溯对象，再做综合。**

## 1. 当前已知事实

> 注：本节最初记录 2026-05-08 的启动态；row 176 后续已经恢复，且 2026-06-17 已重做 clean 文本并移除 `split_pdf/` 派生分片。当前状态以 `knowledge/STATE.md`、`knowledge/manifests/corpus-manifest.json` 和 `knowledge/manifests/missing-and-anomalies.md` 为准。

截至 2026-05-08 的只读检查结果：

- 总 PDF 已保留：`主义主义 (未明子) (z-library.sk, 1lib.sk, z-lib.sk).pdf`
- 结构化目录已保留：`目录索引_结构化.csv` / `目录索引_结构化.md`
- TOC 行数：363
- 启动态 `split_md/` 实际 md 文件数：362；当前为 363
- 启动态 `split_md_clean/` 实际 md 文件数：362；当前为 363
- 启动态缺失 TOC 节点：`2-4-2-4`；当前 row 176 raw/clean 均可用
- `split_pdf/` 按可再生派生层处理；当前不保留 PDF 分片
- Atlas_DB 已有候选层：
  - `nodes.jsonl`: 371
  - `relations.jsonl`: 518
  - `evidence.jsonl`: 922
  - `file_distillates.jsonl`: 363
  - `candidate_nodes.jsonl`: 1062
  - `candidate_relations.jsonl`: 1425
  - `unresolved_queue.jsonl`: 701
- 前端原型存在，但不作为本任务主线：`src/`, `dist/`, `manualSeed.ts` 等只作为历史产品资产。

## 2. 真相层级

任何后续 agent 必须按以下优先级判断真相：

1. **原始证据层**：PDF、TOC、`split_md/`、`split_md_clean/`
2. **结构真相层**：`knowledge/manifests/segments.jsonl`、`chunks.jsonl`、hash、缺失报告
3. **局部解释层**：segment cards、term sense records、position cards
4. **关系解释层**：boundary / route / tension / mediation / transition cards
5. **综合层**：一级/二级/全局 synthesis
6. **历史候选层**：`Zhuyi_Matrix_Engine/Atlas_DB/*`，只能作为候选参考，不能直接当 canonical truth
7. **旧前端层**：`src/`, `dist/`，只记录失败原型，不牵引知识库工作

若聊天上下文与文件状态冲突，**以文件状态为准**。

## 3. 工作流总览

### W0：冻结旧系统与启动记录
目标：记录失败系统状态、明确不再继续救前端。

产物：
- `knowledge/STATE.md`
- `knowledge/logs/operation-log.md`
- `knowledge/qa/old-system-freeze-report.md`

### W1：结构 manifest
目标：把 363 个 TOC 节点和 362 个实际文本切片固定成可追溯对象。

产物：
- `knowledge/manifests/corpus-manifest.json`
- `knowledge/manifests/segments.jsonl`
- `knowledge/manifests/chunks.jsonl`
- `knowledge/manifests/missing-and-anomalies.md`

要求：
- 每个 TOC 节点必须有 `segment_id`、`toc_id`、标题、层级、父节点、页码、路径、存在状态。
- 缺失节点不得被静默删除，必须登记为 `status: missing`。
- `chunks.jsonl` 后续用于检索，不改变 segment truth。

### W2：segment cards
目标：每个实际 clean segment 生成一张可复用卡片。

产物：
- `knowledge/segment-cards/*.md`
- `knowledge/segment-cards/index.md`

每张卡至少包含：
- 元数据：segment_id、toc_id、path、page range、clean path、hash
- 忠实摘要：300–800 字
- 核心术语
- 关键命题
- 代表人物 / 主义 / 学派（若有）
- 证据引句 3–8 条
- 位置关系提示
- 不确定点 / 待审核项

纪律：此层不做大综合，不直接输出“ISMISM 总论”。

### W3：术语义项 registry
目标：拆分核心术语的不同义项，避免同词混用。

产物：
- `knowledge/lexicon/term-senses.jsonl`
- `knowledge/lexicon/core-terms.md`
- `knowledge/lexicon/ambiguous-terms.md`

首批重点术语：
- 主体、客体、实体、物质、历史、人民、理论、理论家、实践、实践单元
- 场、符号、符号秩序、本体论、认识论、目的论、意识形态
- 去主体化、主体化、客体化、中介、跃迁、误认、闭合、有限性

每个义项必须包含：
- `sense_id`
- 定义
- 所属轴：场域 / 本体论 / 认识论 / 目的论 / 复合
- 出现位置
- 证据 segment / 引句
- 禁止混用说明
- 状态：draft / reviewed / canonical / rejected

### W4：matrix position cards
目标：把 4×4×4×4 矩阵从目录变成结构化位置系统。

产物：
- `knowledge/position-cards/1.md` 到一级位置
- `knowledge/position-cards/1-1.md` 等 16 个二级强卡
- `knowledge/position-cards/*.md` 三级/四级轻卡
- `knowledge/position-cards/index.md`

优先级：
1. 先做 4 个一级强卡
2. 再做 16 个二级强卡
3. 再做 64 个三级中卡
4. 最后做 256 个四级轻卡

位置卡必须区分：
- 标题不是定义
- 位置不是人格诊断
- 矩阵位不是最终真理，只是 ISMISM 内部结构位

### W5：relation assets
目标：抽取 ISMISM 真正有价值的“位置之间如何运动”。

产物：
- `knowledge/relations/relation-assets.jsonl`
- `knowledge/relations/boundary-cards.md`
- `knowledge/relations/route-cards.md`
- `knowledge/relations/tension-cards.md`
- `knowledge/relations/mediation-cards.md`
- `knowledge/relations/misrecognition-cards.md`

关系类型至少包括：
- `boundary-between`
- `route-from-to`
- `tension-between`
- `mediates-between`
- `transitions-to`
- `blocks-transition`
- `misrecognizes-as`
- `objectifies`
- `subjectivizes`
- `overcodes`
- `represents-position`
- `evidences-claim`

每条关系必须有：
- 源位置 / 目标位置
- 关系类型
- 简短定义
- 证据 segment / 引句
- 适用边界
- 禁止解释
- 状态

### W6：审计与反驳层
目标：防止 LLM 生成漂亮但不可验证的概括。

产物：
- `knowledge/qa/validation-report.md`
- `knowledge/qa/concept-drift-report.md`
- `knowledge/qa/evidence-claim-audit.md`
- `knowledge/qa/rejected-interpretations.md`

每轮批处理都要有 audit pass，重点查：
- 术语义项是否混用
- 关系是否过强
- 证据是否支撑结论
- 是否把 Atlas 候选当真相
- 是否把四元矩阵当万能解释器

### W7：综合层
目标：在局部卡片充分后，形成可读但可追溯的综合。

产物：
- `knowledge/syntheses/part-1-realism.md`
- `knowledge/syntheses/part-2-metaphysics.md`
- `knowledge/syntheses/part-3-idealism.md`
- `knowledge/syntheses/part-4-praxis.md`
- `knowledge/syntheses/whole-system-map.md`
- `knowledge/syntheses/methodological-core.md`

每个综合必须回链到：
- segment cards
- term senses
- position cards
- relation assets
- 关键证据引句

### W8：使用协议与检索 playbook
目标：让后续任何 agent 都知道如何调用知识库。

产物：
- `knowledge/README.md`
- `knowledge/usage-protocol.md`
- `knowledge/query-playbook.md`
- `knowledge/export-manifest.md`

### W9：接入 psychoanalytic-writing-lab（后置）
目标：在 ISMISM 自身消化稳定后，再把它作为外部参照库接入精神分析写作。

产物：
- `psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md`
- 只允许轻量索引，不复制全库。

## 4. 状态与上下文压缩生存协议

任何长程处理 agent 必须遵守：

1. 每次启动先读：
   - `knowledge/DIGESTION_PROGRAM.md`
   - `knowledge/STATE.md`
   - `knowledge/logs/operation-log.md`
2. 不依赖聊天历史恢复任务。
3. 每完成一个 batch，必须更新：
   - `knowledge/STATE.md`
   - `knowledge/logs/operation-log.md`
   - 对应产物 index / validation note
4. 每次上下文接近压缩，必须先写入 `STATE.md` 的“handoff block”。
5. 若中断后恢复，只按 `STATE.md` 的 `Next Action` 继续。
6. 如果发现状态文件和产物不一致，先写 QA note，不继续大批生成。

## 5. 批处理建议

GPT-5.3 Spark 高强度处理时建议：

- manifest 构建：一次完成
- chunk 生成：一次脚本化完成，再抽查
- segment cards：每批 8–16 个 segment
- term senses：每批 1–3 个高频术语
- position cards：每批 4–8 个位置
- relation assets：每批围绕一个 route / boundary family
- audit：每个生成批后立刻做，不拖到最后

## 6. 禁止事项

- 禁止直接把 362 个 clean md 变成普通 wiki 页面。
- 禁止在 segment card 层写全局总论。
- 禁止把 Atlas_DB 作为 canonical truth。
- 禁止把 4×4×4×4 矩阵当成主体诊断表。
- 禁止让旧前端原型继续牵引消化工作。
- 禁止无证据地把外部理论并入 ISMISM。
- 禁止在没有 `term-sense` 的情况下重用“主体/客体/实践/历史”等高风险词。

## 7. 完成判据

第一阶段完成：
- `segments.jsonl` 覆盖 363 个 TOC 节点
- `chunks.jsonl` 覆盖所有现有 clean md
- 缺失节点登记清楚

第二阶段完成：
- 362 张 segment cards 生成并通过抽查

第三阶段完成：
- 首批核心术语义项表完成
- 4 + 16 个 position strong cards 完成
- 关系资产初版完成

最终完成：
- 四大一级综合 + 全局综合完成
- usage protocol / query playbook 完成
- QA 报告没有阻断项
- 可被外部项目稳定调用
