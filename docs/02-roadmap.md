# 路线图

## 总体路线

本仓库后续不以“页面数量增长”为成功标准，而以“系统能力增长”为标准。

建议分四期推进。

## Phase 1：仓库稳定化

目标：
- 独立仓库成立
- 语料与方法资产迁入
- 入口文档齐备
- 新定位明确
- 用户系统的宏观边界明确
- 前端信息架构与施工边界明确

交付物：
- `README.md`
- `AGENTS.md`
- `docs/00-system-overview.md`
- `docs/01-migration-notes.md`
- `docs/02-roadmap.md`
- `docs/03-agent-scholar-interaction.md`
- `docs/04-system-blueprint-v1.md`
- `docs/05-map-system-spec-v1.md`
- `docs/06-user-system-spec-v1.md`
- `docs/07-session-and-run-state-spec-v1.md`
- `docs/08-precomputed-llm-artifacts-strategy-v1.md`
- `docs/09-interaction-protocol-spec-v1.md`
- `docs/10-relational-asset-forms-spec-v1.md`
- `docs/11-artifact-lifecycle-and-review-spec-v1.md`
- `docs/12-front-end-information-architecture-v1.md`
- `docs/13-implementation-scope-and-handoff-gate-v1.md`

## Phase 2：方法骨架显化

目标：
- 把隐含在语料里的方法骨架单独提出来
- 让系统从“可读”转为“可学”

优先对象：
- 四维骨架：场域论 / 本体论 / 认识论 / 目的论
- 1/2/3/4 推进结构
- 实践单元
- 边界规则
- 常见误判
- 地图系统的真相层 / 状态层 / 任务层
- 节点类型、边类型、掌握层级与跳转逻辑

理想交付物：
- 方法总览文档
- 关键术语表
- 边界规则手册
- 最小诊断规则集

## Phase 3：案例训练化

目标：
- 把系统变成可以训练人的判断力的环境

优先对象：
- canonical case
- confusion pair
- hard case
- disputed case

理想交付物：
- 案例库
- 自测题
- 判定报告模板
- 纠偏说明模板

## Phase 4：agent / scholar 交互化

目标：
- 让 agent 不只是检索语料，而是按 ISMISM 框架与学者协作
- 明确线程状态、运行状态与重请求锁语义
- 明确用户系统与工作区边界
- 明确哪些 LLM 衍生资产需要预生成，哪些按需生成
- 明确交互协议本身如何承载关系型对象
- 明确关系型资产如何成为地图、判定与比较的核心中间层
- 明确资产从生成到进入主系统的生命周期和审核门槛
- 明确前端页面集合、统一工作台骨架与模式切换方式
- 明确 v1 的必须项、非目标与正式交施工方的 scoped gate
- 明确什么时候才算可以正式交给施工方

理想交付物：
- scholar mode prompt / protocol
- disagreement handling rules
- candidate revision workflow
- evidence-first dialogue format
- session / run state spec
- user system spec
- precomputed artifacts strategy
- interaction protocol spec
- relational asset forms spec
- artifact lifecycle and review spec
- front-end information architecture spec
- implementation scope and handoff gate spec

## 现在最重要的三件事

1. 冻结 v1 页面集合、施工边界与第一批种子资产范围
2. 抽出方法骨架，而不是继续只堆语料
3. 让地图、线程、训练与审核四条最小闭环先跑通，再逐步扩展更多模式与资产
