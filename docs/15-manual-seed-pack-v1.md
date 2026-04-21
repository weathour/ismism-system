# ISMISM 手工 Seed Pack（v1 / spine-boundary-first）

这批 seed 不是全量资产化，而是为了 scoped v1 / MVP 先跑通：
- 地图主入口
- 通用线程工作区
- 结构化输出渲染
- 最小训练闭环
- 最小 Scholar / Review 工作台

## 策略

采用：
- **seed-first**
- **spine-boundary-first**

也就是：
1. 先把 1 / 2 / 3 / 4 主干与 16 个二级核心节点立起来
2. 先把四元轴边界规则立起来
3. 先做高混淆 boundary / route / tension / mediation 资产
4. 不先追求全量节点摘要或全量关系卡

前端当前采用 **map + chat 收缩方案**：前端显式主要保留大地图与聊天窗口，seed 更多作为内部查询/调用层存在。

## 当前种子文件

代码真相源：
- `src/data/manualSeed.ts`

配套工作台选择/派生逻辑：
- `src/workbench.ts`
- `src/appModel.ts`

页面与视图组件：
- `src/components/WorkbenchViews.tsx`

其中当前包含：
- 4 个 macro 节点
- 6 个 method 节点
- 16 个二级核心 spine 节点
- 18 个关系型资产
- 18 个证据锚点
- 8 个训练案例
- 一组 `dimensionLenses`，用于把节点投到四维镜（场域 / 本体 / 认识 / 目的）显示
- 一组 `themeProfiles`，把 1-1 / 2-3 / 3-4 / 4-1 四个主题做成专题深描卡

## 第二批补种重点

这次补的不是“更多摘要”，而是更高杠杆的桥接对象：
- `Boundary Card：2-3 vs 3-1`
- `Boundary Card：4-3 vs 4-4`
- `Route Card：2-3 → 3-1 → 3-4`
- `Route Card：4-1 批判 → 4-3 建设`
- `Tension Card：理论姿态 vs 实践单元`

训练新增：
- `2-3 vs 3-1`
- `4-3 vs 4-4`
- `从 3-4 符号学走向 4-1 批判实践`

## 当前地图显示策略

地图不再只是一张“两级树”，而是开始朝更合适的多视图工作台前进。

当前已经支持：
- **结构视图**：看 1/2/3/4 主干与二级核心节点
- **学习视图**：看训练与 draft/reviewed 信号
- **判定视图**：看候选 relation assets 与证据
- **比较视图**：看 A/B 节点之间的边界与张力资产
- **学者视图**：看当前节点下的待审核资产
- **四维镜**：把当前节点放进场域 / 本体 / 认识 / 目的四个维度里看，而不是只看目录层级
- **专题深描卡**：对 1-1 / 2-3 / 3-4 / 4-1 做四维展开、混淆对照、证据入口与对话追问

这意味着 v1 的地图正在从“层级导航树”走向“多视图认知导航系统”。

## 来源约束

本批 seed 主要基于：
- `split_md_clean/`
- `Zhuyi_Matrix_Engine/Phase0_Corpus/Matrix_Backbone.md`
- `Zhuyi_Matrix_Engine/Phase1_Concepts/Boundary_Rules.md`

其中：
- `Matrix_Backbone.md` 提供 16 个二级核心节点骨架
- `Boundary_Rules.md` 提供四元轴边界与训练校准规则
- `split_md_clean/` 提供节点与实践区的首批证据锚点

## 这批 seed 的产品用途

### 地图
- 用 1 / 2 / 3 / 4 + 16 个二级节点构成第一批 truth layer 骨架
- 允许从节点直接进入导学 / 诊断 / 比较线程
- 允许从节点直接得到 compare 候选与推荐跳转
- 允许用四维镜把当前节点重新放回方法轴而不是只看树形位置

### 线程
- 输出默认挂上：
  - node summary
  - candidate outputs
  - relation findings
  - evidence pack
  - uncertainty
  - recommended jumps
- 线程现在是本地一级对象：
  - 可新开线程
  - 可切换线程
  - 每条线程有自己的 run 状态与历史

### 训练
- 优先做：
  - 四元轴判别
  - 1-1 vs 1-2
  - 2-3 vs 3-1
  - 3-1 vs 3-2
  - 3-3 vs 3-4
  - 4-1 vs 4-2
  - 4-3 vs 4-4

### Review
- 故意保留一部分 `draft` / `reviewed` 资产
- 用来验证：
  - 生命周期状态可见
  - review note 可写
  - reviewed / canonical 升格动作可跑通

## 当前刻意没做

- 全量节点卡
- 全量关系卡
- 全量训练题
- Atlas-first 资产体系
- 自动化批量审核
- 真实后端持久化线程系统

## 下一步

下一阶段围绕这批 seed 做：
1. 继续把 map -> thread -> asset 的联动收紧
2. 把本地多线程工作流向更稳定的 v1 contract 推进
3. 继续把 seed 数据层与 UI 状态层解耦
4. 为后续接真实后端 / 推理接口留出更清晰的数据边界
