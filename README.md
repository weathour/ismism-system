# ismism-system

ISMISM 的独立仓库。这个仓库不再把 ISMISM 视为 `yxj-wiki` 的一个普通语料分支，而是把它定位为一个独立的“理论学习 / 诊断 / 交互系统”工程。

## 现在的定位

ISMISM 首先不是普通哲学史百科，也不是仅供检索的转写语料库。

它更适合被理解为：
- 以哲学史材料为输入的作者型理论系统
- 以四维判定（场域论 / 本体论 / 认识论 / 目的论）为骨架的训练体系
- 以主体位置分析、意识形态诊断、实践单元与交互式判定为落点的学徒系统

一句话版本：

> ISMISM 是一个交互式理论学徒与诊断系统，而不只是一个知识存储库。

## 本仓库当前包含什么

已迁入：
- 原始总 PDF
- 结构化目录索引（CSV / Markdown）
- `split_md/` 原始切分文本
- `split_md_clean/` 轻清洗平行层
- `Zhuyi_Matrix_Engine/` 及其 Atlas / Phase 文档
- 现有的切分 / 清洗 / 目录处理脚本
- 历史 handoff 文档

刻意未迁入：
- `split_pdf/`
- `graphify-out/`
- `_tmp_clean_smoke*`
- `__pycache__/`
- `_skill_build/`

原因：
- `split_pdf/` 体量大且属于可再生派生物，可由总 PDF + TOC + 脚本重新生成
- 其余目录属于临时产物或缓存，不应作为新仓库真相层

## 当前推荐阅读顺序

1. `docs/00-system-overview.md`
2. `docs/01-migration-notes.md`
3. `docs/02-roadmap.md`
4. `docs/03-agent-scholar-interaction.md`
5. `docs/04-system-blueprint-v1.md`
6. `docs/05-map-system-spec-v1.md`
7. `AGENTS.md`
8. `Zhuyi_Matrix_Engine/Phase0_Corpus/Matrix_Backbone.md`
9. `Zhuyi_Matrix_Engine/Phase1_Concepts/Boundary_Rules.md`
10. `Zhuyi_Matrix_Engine/Phase4_Skill_Suite/Main_Agent_Prompt.md`
11. `split_md_clean/4_实践/0276_4_实践_p7184.md`

## 当前仓库结构

- `split_md/`：原始切分文本
- `split_md_clean/`：轻清洗后的平行文本层
- `Zhuyi_Matrix_Engine/`：旧系统留下的理论骨架、Atlas 与执行蓝图
- `目录索引_结构化.csv`：当前层级结构真相源之一
- `*.py`：现有切分 / 清洗 / 目录处理脚本
- `docs/`：本仓库的新定位、迁移说明、路线图与交互设计

## 当前工作重点

短期内优先做这四件事：
- 把仓库从“语料搬运场”稳定成“独立系统仓”
- 明确方法骨架与课程骨架
- 建立案例化 / 诊断化 / 交互化的系统入口
- 为未来 agent 与学者协作留出稳定接口

## 不要误解成什么

- 不是中立哲学史教材
- 不是普通 wiki
- 不是单轮问答机器人知识库
- 不是只靠全文检索就能用起来的 corpus

## 未来目标

理想状态下，本仓库会长成一个三合一系统：
- 学习系统
- 诊断系统
- 学者协作系统

也就是：
- 能学
- 能判
- 能跟学者一起修正与推进
