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

理想交付物：
- scholar mode prompt / protocol
- disagreement handling rules
- candidate revision workflow
- evidence-first dialogue format
- session / run state spec
- user system spec
- precomputed artifacts strategy

## 现在最重要的三件事

1. 完成仓库定位与入口文档
2. 抽出方法骨架，而不是继续只堆语料
3. 设计交互协议、用户系统与运行纪律，并同步明确哪些 LLM 衍生资产要预生成
