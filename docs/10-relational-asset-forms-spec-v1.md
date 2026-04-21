# ISMISM 关系型衍生资产规格（v1）

## 0. 这份文档讨论什么

这份文档专门回答一个问题：

> 既然 ISMISM 极度重视节点之间的运动、矛盾、中介、短路与跃迁，那么预生成的 LLM 衍生资产到底应该长成什么形式？

一句话结论：

> ISMISM 的预生成资产不应以“节点摘要”为中心，而应以“关系型资产”为中心；节点卡要有，但更重要的是路线卡、矛盾卡、中介卡、边界卡和投射链资产。

这份文档不是生命周期文档，而是“资产形态”文档。

---

## 1. 为什么必须重新思考资产形式

如果沿用普通知识产品的直觉，最容易生成的是：
- 节点摘要
- 节点关键词
- 节点定义

但对 ISMISM 来说，这远远不够。

原因很简单：
这套系统的核心不只是“某个节点讲了什么”，而是：
- 它如何从前一个点运动过来
- 它内部的核心矛盾是什么
- 它靠什么中介维持
- 它会在哪里短路
- 它会逼出什么下一环节
- 它会投向什么主体 / 组织 / 实践

所以如果预生成资产只是一堆节点摘要，系统就会变成：
- 可读
但不够：
- 可判
- 可比
- 可追踪
- 可推演

---

## 2. 关系型资产优先原则

建议把资产设计的重心从：
- node-centric（节点中心）

转向：
- relation-centric（关系中心）

这并不是取消节点卡，而是重新排序：

### 基础层
- 节点卡仍然要有

### 主价值层
- 路线资产
- 矛盾资产
- 中介资产
- 边界资产
- 投射资产

也就是说：
节点是挂点，关系才是动力学核心。

---

## 3. 资产总分类

我建议预生成资产至少分七类。

## 3.1 Node Card（节点卡）

仍然需要，但定位要降级为“入口资产”，而不是系统最核心资产。

建议字段：
- 节点名称
- 节点类型
- 所在位置
- 一句话定义
- 功能说明
- 相关高混淆点
- 相关证据入口

作用：
- 让地图和搜索有锚点

但节点卡不应承担全部工作。

---

## 3.2 Route Card（路线卡 / 运动卡）

这是最重要的关系型资产之一。

描述：
- 一个节点如何运动到另一个节点
- 或者一个阶段如何逼出下一个阶段

适用问题：
- 3 如何走向 4？
- 为什么 2 会逼出 3？
- 某个理论为什么会从裂口走向主体中介？

建议字段：
- `route_id`
- `start_node`
- `end_node`
- `middle_nodes`
- `trigger_conditions`
- `key_tensions`
- `mediation_shift`
- `typical_failure_modes`
- `evidence_anchors`
- `scholar_notes`

Route Card 的意义：
它是“动态地图”的基本单位。

---

## 3.3 Tension Card（张力卡 / 矛盾卡）

描述：
- 某节点或局部区域的核心矛盾

适用问题：
- 这里真正打架的是什么？
- 它卡住在哪？
- 是哪一维在冲突？

建议字段：
- `tension_id`
- `scope`
- `pole_a`
- `pole_b`
- `dimension`
- `surface_symptom`
- `deep_structure`
- `current_status`（未调和 / 暂时调和 / 已短路 / 已跃迁）
- `resolution_pattern`
- `evidence_anchors`

Tension Card 的意义：
它是“为什么会运动”的资产，而不是“运动结果”的资产。

---

## 3.4 Mediation Card（中介卡）

描述：
- 某个局部结构依靠什么中介来维持
- 这种中介是主体性的、历史性的、理论性的，还是实践性的

适用问题：
- 它靠什么维持自己？
- 这里的中心项是什么？
- 它是不是假中介？

建议字段：
- `mediation_id`
- `scope`
- `mediated_poles`
- `mediator`
- `mediator_type`
- `stability`
- `cost`
- `what_breaks_if_removed`
- `evidence_anchors`

Mediation Card 的意义：
它是“系统如何站住”的资产。

---

## 3.5 Short-Circuit Card（短路卡）

描述：
- 哪些结构会发生短路
- 短路后会导向什么

适用问题：
- 哪一步太快了？
- 哪两个层被错误直接打通了？
- 为什么这里会崩？

建议字段：
- `short_circuit_id`
- `scope`
- `bypassed_layers`
- `short_circuit_trigger`
- `visible_effect`
- `resulting_shift`
- `repair_strategy`
- `evidence_anchors`

这类资产非常适合支撑“误判分析”和“理论故障诊断”。

---

## 3.6 Boundary Card（边界卡）

描述：
- 两个相邻/高混淆节点的真实分界线

适用问题：
- 为什么它不是 B？
- A 和 B 表面像，但究竟差在哪？

建议字段：
- `boundary_id`
- `node_a`
- `node_b`
- `shared_surface`
- `real_divergence`
- `most_decisive_dimension`
- `common_misread`
- `fast_test`
- `evidence_anchors`

这类资产和 confusion pair 高度相关，是学习系统的高价值对象。

---

## 3.7 Projection Chain（投射链资产）

描述：
- 某个理论位置如何继续推向主体、组织、实践单元和历史后果

适用问题：
- 如果停在这里，会长成什么主体？
- 会导向什么组织倾向？
- 会落到什么实践单元？

建议字段：
- `projection_id`
- `source_node`
- `subject_form`
- `organization_tendency`
- `practice_unit_tendency`
- `historical_effect`
- `risk_of_distortion`
- `counter_projection`
- `evidence_anchors`

Projection Chain 是 ISMISM 区别于普通哲学系统的关键资产。

---

## 4. 哪类资产最值得优先预生成

优先级建议如下。

## 第一优先级
- 方法节点卡
- Route Card
- Boundary Card
- Tension Card

原因：
这些最直接服务：
- 地图
- 判定
- 比较
- 学习

## 第二优先级
- canonical case 卡
- confusion pair 卡
- Mediation Card
- 证据锚点索引

## 第三优先级
- Projection Chain
- Short-Circuit Card
- 高难 disputed case 草稿

不是因为第三优先级不重要，而是它更容易受体系口径变化影响。

---

## 5. 资产不应只按“节点文件”存放

产品上一个常见陷阱是：
每个资产都归到某个节点下面。

这对 ISMISM 不够，因为：
- 一条路线跨多个节点
- 一张边界卡天然属于两个节点
- 一张张力卡可能属于一整个分支
- 一个投射链可能从理论层跨到实践层

所以从宏观设计看，资产应至少允许三种归属方式：

1. `node_attached`
- 主要挂在某个节点上

2. `pair_attached`
- 主要挂在一对节点之间

3. `scope_attached`
- 挂在一个区域/分支/阶段上

这能避免强行把关系资产塞进单节点容器里。

---

## 6. 资产与地图的关系

地图要想真正强，不能只读取 node card。

地图至少应能消费：
- Node Card
- Route Card
- Boundary Card
- Tension Card
- Projection Chain

地图中的高价值可视反馈，应更多来自：
- 哪些边被点亮
- 哪些张力在工作
- 哪些路线被推荐
- 哪些边界正是当前冲突点

而不是只点亮一个节点。

也就是说：
地图的可视化重点应慢慢从“点”转向“点与边”。

---

## 7. 资产与交互协议的关系

交互协议如果只返回节点解释，那么这些关系资产就永远只是仓库里的文档。

所以交互协议必须能输出：
- relation objects
- route objects
- tension objects
- mediation objects
- projection chains

这样一次 diagnose / compare / trace / project 才能真正挂接到这些资产上。

换句话说：
- 交互协议负责调用它们
- 资产系统负责提供稳定锚点

---

## 8. 资产与预生成策略的关系

不是所有关系型资产都适合一开始就做满。

### 适合优先预生成的
- 方法节点卡
- 核心 Route Card
- 核心 Boundary Card
- 关键 Tension Card
- confusion pair

### 更适合后续按需增长的
- 长链路 Route Card
- 高难 Projection Chain
- disputed Short-Circuit Card
- Scholar 高争议修正版资产

也就是说：
关系型资产也需要分“稳定锚点”和“高上下文资产”。

---

## 9. 资产的粒度建议

一个危险倾向是：
把资产做得过大，写成长文。

对系统复用来说，更合理的是：
- 小而清晰
- 可组合
- 可被多种模式复用

例如：
不要一开始就写“3 到 4 的 5000 字总论”。
更合理的是拆成：
- 一个 Route Card：3 -> 4
- 一个 Tension Card：主体中介不足
- 一个 Mediation Card：历史 / 人民 / 理论家三项
- 一个 Projection Chain：实践单元的引入

这样系统后续更容易调用和组合。

---

## 10. 资产的展示原则

这些资产将来未必都以独立页面展示，但产品上都应能被渲染成卡片或摘要块。

建议：
- Node Card = 节点卡
- Route Card = 运动卡
- Tension Card = 矛盾卡
- Mediation Card = 中介卡
- Boundary Card = 边界卡
- Projection Chain = 推演卡

如果未来做 Web，这会非常适合前端组件化。

---

## 11. 为什么这比“全量摘要”更值钱

因为摘要只能告诉你：
- 这里讲了什么

而这些关系资产还能告诉你：
- 为什么会走到这里
- 它和旁边节点究竟差在哪
- 哪个矛盾在推动它变化
- 如果接受它，会继续通向哪里

而这恰恰是 ISMISM 最独特、最不可替代的部分。

---

## 12. 当前推荐的产品结论

一句话总结：

> ISMISM 的高价值预生成资产不应主要是“节点摘要”，而应主要是“关系型资产”。

更具体一点：
- 节点卡是基础
- 关系卡才是核心
- 运动、矛盾、中介、边界、投射，这些才是未来系统真正的中间知识对象

---

## 13. 下一份文档最适合写什么

继续只做宏观文档、不开始施工的话，下一份最适合写：

1. `artifact-lifecycle-and-review-spec-v1`
   - draft / reviewed / canonical 的升级规则
2. `workspace-and-permission-spec-v1`
   - 私有层 / 团队层 / 公共层
3. `front-end-information-architecture-v1`
   - 首页、地图页、诊断页、比较页、学者页的宏观布局

如果只能先写一个，我建议：
- `artifact-lifecycle-and-review-spec-v1`

因为一旦关系型资产开始生成，就必须立刻明确：
- 哪些只是草稿
- 哪些可复用
- 哪些能进入系统主流程
