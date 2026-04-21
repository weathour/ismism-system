# ISMISM 系统总览

## 1. 本仓库现在在做什么

本仓库把 ISMISM 从旧 bundle/source 目录中独立出来，作为一个单独系统来建设。

新的主问题不是：
- 如何把 300+ 主题塞进别的知识库

而是：
- 这样一套材料，最适合长成一个怎样的独立系统？

## 2. 当前系统判断

基于对主干材料与抽样章节的重新阅读，当前最合适的判断是：

ISMISM 是一个以哲学史材料为输入、以四维判定为骨架、以意识形态诊断与实践问题为落点的作者型理论训练系统。

它不是纯哲学史课程。
它也不是普通的知识库存储。
它更像一个：
- 学习系统
- 诊断系统
- 学者协作系统

## 3. 系统最重要的四个对象

### A. 语料对象
- 总 PDF
- 目录索引
- 原始切分文本
- 轻清洗文本

### B. 方法对象
- 场域论
- 本体论
- 认识论
- 目的论
- 1/2/3/4 的推进结构
- 实践单元

### C. 判定对象
- 某个思想家
- 某个主义
- 某段文本
- 某种主体姿态
- 某个实践路径

### D. 交互对象
- 学习者
- 研究者
- 学者
- agent

### E. 用户对象
- 用户身份与角色
- 初始化状态
- 学习进度
- 交互偏好
- 工作记忆
- 隐私与权限边界

详细见：`docs/06-user-system-spec-v1.md`

### F. 运行对象
- 会话（thread）
- 生成任务（run）
- 活跃请求锁
- cancel / retry / idempotency
- 浏览动作与推理动作的边界

详细见：`docs/07-session-and-run-state-spec-v1.md`

### G. 衍生资产对象
- 方法节点卡
- 案例卡
- confusion pair
- 证据锚点
- 预生成 LLM 资产的草稿 / 审核 / canonical 生命周期
- 关系型资产：路线卡、矛盾卡、中介卡、边界卡、推演链

详细见：
- `docs/08-precomputed-llm-artifacts-strategy-v1.md`
- `docs/10-relational-asset-forms-spec-v1.md`

### H. 协议对象
- 导学协议
- 判定协议
- 比较协议
- 追踪协议
- 张力分析协议
- 协作修正协议
- 关系型输出对象（Route / Tension / Mediation / Projection）

详细见：`docs/09-interaction-protocol-spec-v1.md`

### I. 生命周期对象
- draft / reviewed / canonical
- deprecated / superseded / rejected
- 审核者与升级路径
- 资产进入地图 / 诊断 / 训练主流程的准入规则
- 正式交施工方前的 handoff gate

详细见：`docs/11-artifact-lifecycle-and-review-spec-v1.md`

### J. 前端工作台对象
- 公共入口层 / 登录后工作台层 / scholar-review 层
- 顶栏 / 主导航 / 上下文侧栏 / 主工作区 / 右侧证据面板 / run dock
- 地图页 / 通用线程页 / 训练页 / scholar 审核页
- 对象详情页、侧板与可回跳关系

详细见：`docs/12-front-end-information-architecture-v1.md`

### K. 施工边界对象
- v1 必须做的页面与能力
- v1 明确不做的非目标
- 第一批种子节点 / 关系资产 / 训练案例范围
- 正式交施工方的 scoped handoff gate

详细见：`docs/13-implementation-scope-and-handoff-gate-v1.md`

## 4. 未来最适合的系统形态

我方当前采用的目标形态是：

### 4.1 课程模式
按结构学习：
- 1 实在论
- 2 形而上学
- 3 观念论
- 4 实践

### 4.2 地图模式
按结构导航：
- 主干
- 分支
- 复习课
- 高混淆点
- 跃迁关系
- 分层视图（理论真相层 / 学习状态层 / 当前任务层）
- 节点掌握程度与有理由的跳转

这部分的详细产品规格见：`docs/05-map-system-spec-v1.md`

### 4.3 诊断模式
输入一个对象，输出：
- provisional 判定
- 候选格位
- 证据
- 排除理由
- 不确定性

### 4.4 对话模式
让 agent 不只是回答，而是追问、比较、纠偏、推进。

### 4.5 案例训练模式
围绕：
- canonical case
- confusion pair
- hard case
- disputed case
展开训练。

### 4.6 实践推演模式
把理论位置继续推到：
- 主体形态
- 组织倾向
- 实践单元
- 历史后果

## 5. 当前最重要的系统结论

ISMISM 最适合被做成一个交互式理论学徒系统。

它的核心价值不是“告诉你结论”，而是“训练你给出可争论、可回溯、可修正的判断”。
