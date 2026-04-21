# ISMISM 交施工方执行 Brief / Handoff Prompt（v1）

## 0. 用途

这份文档不是新的产品规格，而是把前面已经冻结的产品判断，压缩成一份可以直接交给施工方的人类 brief / AI handoff prompt。

适用对象：
- 人类前后端施工团队
- 产品原型实现团队
- AI coding agent / builder agent

一句话：

> 你们现在要施工的，不是“终局版 ISMISM”，而是一个边界明确、可真实运行的 scoped v1 理论工作台。

---

## 1. 项目定位

项目名：ISMISM

主仓库：`/home/weathour/文档/ismism-system`

当前分支：`main`

当前确认起点提交：`96cf9fc`

项目不是：
- 普通哲学史内容站
- 普通聊天机器人
- 先把语料全量自动摘要化的大工程
- 只靠检索就能使用的知识库

项目是：
- 一个交互式理论学习系统
- 一个结构化诊断系统
- 一个 scholar / researcher 可参与审核和修正的工作台

核心骨架：
- 以四维判定为方法骨架
- 以地图、线程、证据、关系型资产为工作骨架
- 以训练、纠偏、审核、升级为长期演进骨架

---

## 2. 施工前必须先读的文档

施工方不要直接看代码开工，先读文档。

最少必读顺序：
1. `README.md`
2. `AGENTS.md`
3. `docs/00-system-overview.md`
4. `docs/04-system-blueprint-v1.md`
5. `docs/05-map-system-spec-v1.md`
6. `docs/06-user-system-spec-v1.md`
7. `docs/07-session-and-run-state-spec-v1.md`
8. `docs/09-interaction-protocol-spec-v1.md`
9. `docs/10-relational-asset-forms-spec-v1.md`
10. `docs/11-artifact-lifecycle-and-review-spec-v1.md`
11. `docs/12-front-end-information-architecture-v1.md`
12. `docs/13-implementation-scope-and-handoff-gate-v1.md`

没有读完这些文档，不应擅自决定页面结构、线程模型、地图角色、资产状态或 v1 范围。

---

## 3. 这次施工的任务定义

你们这次要做的是：

### 3.1 目标

建设一个可运行的 ISMISM v1 / MVP，满足以下最小闭环：
- 用户可进入统一工作台
- 用户可浏览地图，并从地图进入任务
- 用户可在统一线程工作区中发起导学 / 诊断 / 比较类任务
- 每个线程同一时间只允许一个 active heavy run
- 系统结果不是纯聊天长文本，而是可渲染的结构化对象
- 系统支持最小资产生命周期与审核动作
- 系统支持最小训练闭环

### 3.2 这次不是要做什么

不是要：
- 一次完成全部语料结构化
- 一次完成全部模式
- 一次完成全部关系资产生成
- 一次完成完整多租户平台
- 一次完成移动端与复杂协作

也就是说：

> 先把系统“工作方式”做对，再扩规模；不要先把“规模”做出来，却没有工作方式。

---

## 4. 绝对不能违反的产品约束

以下约束视为 hard constraints。

### 4.1 不能把 ISMISM 做成普通聊天产品

不允许出现这种退化：
- 首页一个聊天框
- 地图只是附属按钮
- 所有模式都退化成 prompt 模板切换

### 4.2 地图不是装饰，是主入口之一

地图必须能：
- 浏览
- 高亮
- 选中节点 / 关系
- 打开对象详情
- 直接发起导学 / 诊断 / 比较线程

### 4.3 线程级 run 锁是硬约束

必须遵守：
- 同一线程同一时间只允许一个 active heavy run
- 但轻动作必须继续可用，例如：浏览地图、打开卡片、看证据、切换侧栏
- 不允许把“正在生成”实现成全站死锁

### 4.4 关系型资产优先级很高

前端和数据模型都要明确支持：
- Route Card
- Tension Card
- Mediation Card
- Boundary Card
- Short-Circuit Card
- Projection Chain

不要只做节点摘要卡。

### 4.5 生命周期状态必须可见

至少要清楚表达：
- draft
- reviewed
- canonical

并保留后续扩展到：
- deprecated
- superseded
- rejected
- disputed-reviewed

### 4.6 第一版以桌面工作台为主

不要优先为移动端牺牲地图、证据、审核和对比体验。

---

## 5. 第一版必须交付的页面 / 工作区

第一版推荐冻结为以下 6 类页面 / 视图：

1. 工作台首页（Workbench Home）
2. 地图页（Map Workspace）
3. 通用线程工作区（承载 orient / diagnose / compare / trace / tension 等）
4. 训练页（Training Workspace）
5. Scholar / Review 页
6. 资产详情侧板 / 详情页

注意：
- 不要把每个模式都拆成完全不同网站
- 统一壳层下共享工作台骨架
- 模式差异更多体现在主面板模板，而不是整站分裂

---

## 6. 第一版必须具备的系统能力

至少要做成以下 8 件事：

1. 统一工作台壳层
   - 顶栏
   - 左侧一级导航
   - 中央主工作区
   - 右侧证据 / 资产 / 洞察面板
   - run 状态区

2. 地图主入口
   - 真相层基础地图
   - 用户状态层最小显示
   - 当前任务层最小高亮
   - 节点 / 关系详情打开
   - 从地图发起线程

3. 通用线程工作区
   - 单线程页
   - 当前上下文对象
   - 结构化输出渲染区
   - cancel / retry
   - 历史输出回看

4. 结构化输出渲染器
   至少支持：
   - 节点卡
   - Route Card
   - Tension Card
   - Boundary Card
   - 证据锚点
   - 候选位 / 排除链 / 不确定性

5. 运行纪律系统
   - 单线程单 active heavy run 锁
   - 显式状态展示
   - 失败 / 取消 / 重试语义清晰
   - light vs heavy action 边界清晰

6. 最小生命周期系统
   - asset status 显示
   - 来源与证据显示
   - 最小审核动作

7. 最小训练闭环
   - 题面
   - 作答
   - 反馈
   - 回结构补课跳转

8. 最小 scholar / review 工作台
   - 待审核资产列表
   - 打开资产
   - 看证据锚点
   - reviewed / canonical / rejected 等最小动作
   - review note

---

## 7. 第一版数据与资产策略

第一版采用“种子驱动”，不要等待全量完成。

建议第一批范围：
- 20–40 个核心节点
- 30–80 个高价值关系型资产
- 10–20 个 canonical / confusion / hard / disputed case
- 一小批高质量证据锚点

优先选择：
- 方法骨架核心节点
- 高混淆边界
- 能体现运动 / 矛盾 / 中介的典型关系
- 与实践单元方向强相关的对象
- 能形成训练纠偏的案例

数据来源允许：
- 手工整理
- 半手工整理
- LLM 生成 draft 后人工筛选

不要把“先全自动生成完”当成第一版前提。

补充说明：
- `split_md_clean/` 是当前优先文本层
- Atlas 可作为候选 / 历史 / 审核辅助层
- Atlas 不是第一版主真相层

---

## 8. 明确非目标（Out of Scope）

第一版明确不做：
- 全量自动资产化
- 复杂多租户 / 多组织协作
- 移动端优先
- 炫技型图谱编辑器
- 深度个性化推荐系统
- 先把 Atlas 全面产品化
- 先求高争议对象的最终权威定论

如果施工中有人提出这些功能，请默认视为后续阶段，而不是第一版范围内任务。

---

## 9. 推荐施工顺序

建议按下面顺序做，不要并行摊大饼：

### Step 1
统一工作台壳层 + 线程 / run 纪律

### Step 2
地图主入口 + 对象详情侧板

### Step 3
结构化输出渲染器 + 通用线程模板

### Step 4
最小生命周期系统 + scholar / review 工作台

### Step 5
最小训练闭环

### Step 6
再扩展更多模式、更多资产类型、更多自动化

---

## 10. 交付验收标准（Builder 自检）

施工方在声称“v1 可用”之前，至少应能回答以下问题并现场演示：

1. 能否从地图点击一个节点，直接发起一条导学或诊断线程？
2. 同一线程正在跑 heavy run 时，地图浏览和对象详情是否仍可操作？
3. 结果是否以结构化对象呈现，而不是只有长文本？
4. 能否在同一工作区里看到证据锚点和关系型资产？
5. 一个资产是否能清楚显示它是 draft、reviewed 还是 canonical？
6. scholar / reviewer 是否能看到待审核资产并留 note？
7. 训练页能否把一次错误回答导回相应结构或路径？
8. 系统是否仍然保持“理论工作台”形态，而不是退化成聊天页？

如果这些问题有多个答不上来，就不应宣称第一版完成。

---

## 11. 施工方拿到任务后应如何回报

施工方在开始前应先提交一份简短实施回执，至少包含：
- 他们理解的 v1 页面集合
- 他们理解的 hard constraints
- 他们理解的非目标
- 他们计划的施工顺序
- 他们打算如何表达 thread / run 锁
- 他们打算如何渲染结构化对象
- 他们需要甲方补充的 seed 资产输入清单

这一步非常重要，因为它能迅速暴露是否“读懂了系统”，还是只是“准备开工写页面”。

---

## 12. 可直接转发给 AI Builder / 施工方的 Prompt

下面这段可以直接复制：

你现在接手的是 ISMISM 的 scoped v1 / MVP 施工任务。

项目仓库：`/home/weathour/文档/ismism-system`
分支：`main`
起始提交：`96cf9fc`

先阅读以下文档，再开始设计或编码：
1. `README.md`
2. `AGENTS.md`
3. `docs/00-system-overview.md`
4. `docs/04-system-blueprint-v1.md`
5. `docs/05-map-system-spec-v1.md`
6. `docs/06-user-system-spec-v1.md`
7. `docs/07-session-and-run-state-spec-v1.md`
8. `docs/09-interaction-protocol-spec-v1.md`
9. `docs/10-relational-asset-forms-spec-v1.md`
10. `docs/11-artifact-lifecycle-and-review-spec-v1.md`
11. `docs/12-front-end-information-architecture-v1.md`
12. `docs/13-implementation-scope-and-handoff-gate-v1.md`
13. `docs/14-builder-handoff-brief-v1.md`

你的任务不是做一个普通聊天产品，而是做一个统一工作台形态的理论系统 v1，核心必须包括：
- 工作台首页
- 地图页
- 通用线程工作区
- 训练页
- scholar / review 页
- 资产详情侧板 / 详情页

必须遵守以下硬约束：
- 地图是主入口之一，不是附属装饰
- 同一线程同一时间只允许一个 active heavy run
- 轻动作在 heavy run 期间仍必须可用
- 结果必须支持结构化对象渲染，不可只返回长文本
- 关系型资产必须是一等对象，不可只做节点摘要卡
- 生命周期状态必须可见，至少支持 draft / reviewed / canonical
- 第一版优先桌面工作台，不以移动端为主

第一版明确不做：
- 全量自动资产化
- 复杂多租户协作
- 移动端优先
- 炫技型图谱编辑器
- 深度推荐系统
- 先把所有 Atlas 产品化

推荐施工顺序：
1. 统一壳层 + 线程 / run 纪律
2. 地图入口 + 对象详情侧板
3. 结构化输出渲染器 + 通用线程模板
4. 生命周期最小实现 + scholar / review
5. 最小训练闭环

施工开始前，请先提交一份简短回执，说明：
- 你理解的 v1 页面集合
- 你理解的 hard constraints
- 你理解的 out-of-scope
- 你的施工顺序
- 你需要的第一批 seed 资产输入

不要在没有说明理由的情况下自行扩展范围，也不要把系统退化成普通聊天页。

---

## 13. 当前推荐结论

一句话总结：

> 可以正式把 ISMISM 交给施工方开做，但交出去的必须是一份收缩后的 v1 理论工作台施工任务，而不是一个无限扩张、边界不清的“先做起来再说”的大项目。