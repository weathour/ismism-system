# 迁移说明

## 1. 迁移来源

原始来源目录：
- `/home/weathour/document/programs/codex-portable-skills/bundles/ismism/_bundle/source`

新仓库目录：
- `/home/weathour/文档/ismism-system`

## 2. 本次迁移的目标

目标不是立即重构全部内容，而是先完成：
- 独立建仓
- 迁入核心语料与方法资产
- 把仓库定位从“bundle 内部材料目录”提升为“独立系统仓库”
- 写清楚新定位与后续方向

## 3. 已迁入内容

- 总 PDF
- 结构化目录索引：CSV / Markdown
- `split_md/`
- `split_md_clean/`
- `Zhuyi_Matrix_Engine/`
- 现有脚本：
  - `clean_split_md_with_ollama.py`
  - `enrich_toc_csv_with_outputs.py`
  - `extract_split_pdf_to_md.py`
  - `generate_toc_csv.py`
  - `run_pdf_md_pipeline.py`
  - `split_pdf_by_toc.py`
- 历史 handoff：`ISMISM-CLEANUP-HANDOFF.md`

## 4. 本次刻意未迁入内容

### `split_pdf/`
原因：
- 体量大（原目录约 590M）
- 属于可再生派生物
- 可由总 PDF + TOC + 脚本重新生成
- 现阶段不应阻塞独立建仓与系统定位工作

### `graphify-out/`
原因：
- 可再生导航产物
- 不是语料真相层

### `_tmp_clean_smoke*`、`__pycache__/`、`_skill_build/`
原因：
- 临时 / 缓存 / 构建遗留物
- 不应进入新仓库真相层

## 5. 迁移策略说明

当前采用的是“保守迁移”：
- 先复制核心材料进入新仓库
- 不在原 bundle/source 上做破坏性删除
- 新仓库先承担后续工作的主位置
- 旧目录后续可视为 legacy source，待新仓稳定后再决定如何清理

## 6. 为什么不直接大改目录结构

这次迁移优先保留根层兼容性，因为：
- 现有脚本默认当前文件名和相对路径
- 现阶段重点是完成系统独立化，不是重写全部脚本
- 先稳定新仓，再逐步推进结构优化更安全

## 7. 迁移后的立场变化

迁移完成后，本仓库不再被视为某个上层项目里的附属数据目录。

它现在应被视为：
- ISMISM 独立工作主仓
- 后续方法整理、案例训练、agent 交互协议、学者协作都在这里推进
