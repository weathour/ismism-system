# ISMISM 清洗任务 Handoff

更新时间：2026-04-17

## 项目状态

- 当前项目：**ISMISM 语料清洗与纳入 yxj-wiki**
- 项目状态：**active / ongoing**
- 未来若用户说“继续 ismism 项目”或“继续这个项目”，默认就是继续这条工作线。
- 继续时优先读取：
  1. 本文件 `ISMISM-CLEANUP-HANDOFF.md`
  2. `clean_split_md_with_ollama.py`
  3. `split_md_clean/1_实在论/_cleanup_report.jsonl`
  4. `/home/weathour/文档/yxj-wiki/wiki/_meta/architecture/08-ismism-corpus-full-integration-plan.md`

## 1. 任务目标

先不要急着把这套 ismism 语料直接入 llm-wiki。
当前优先做的是：

1. 保留原始 `split_md/` 不动
2. 用本地 Ollama `gemma4:latest` 做“轻清洗”
3. 输出一个平行的 `split_md_clean/` 层
4. 清洗目标仅限于：
   - 断裂换行
   - 缺失标点
   - 中英文空格混乱
   - 明显口语转写噪声
5. 不做：
   - 总结
   - 改写观点
   - 新增概念
   - 覆盖原文

## 2. 当前文件与脚本

项目根：
- `/home/weathour/document/programs/codex-portable-skills/bundles/ismism/_bundle/source`

关键路径：
- 原始切分文本：`split_md/`
- 清洗后平行层：`split_md_clean/`
- 当前脚本：`clean_split_md_with_ollama.py`
- 当前 handoff：`ISMISM-CLEANUP-HANDOFF.md`

## 3. 当前已验证的结论

### 质量判断
已抽查数篇清洗结果，结论：
- 质量达到“第一遍 clean corpus”可用标准
- 页码锚点 `## Page N` 保住了
- 没有出现新的 markdown 污染（如 `**`、代码块、引用块）
- 标点、断句、断行明显改善
- 总体仍基本保留原话

### 已知局限
这一步是“轻清洗”，不是“人工精修校对”：
- 如果原切片本来就是半句开头，clean 后仍可能是半句开头
- 个别词可能会被修得不够自然
- 少量口语冗余和错字会残留

因此它适合作为：
- 后续 chunk / 检索 / 提炼前的 clean corpus

但不应当被视为：
- 最终出版级文本

## 4. 当前运行状态

当前正式后台任务：
- process session id: `proc_a4414e90b876`

它在处理：
- `split_md/1_实在论`

输出到：
- `split_md_clean/1_实在论`

进度报告文件：
- `split_md_clean/1_实在论/_cleanup_report.jsonl`

截至本 handoff 记录时：
- `1_实在论` 总文件数：95
- 已尝试：5
- 已清洗成功：3
- 已超时：2

已知超时文件：
- `1-1_复习课/1-1-1_物理主义/0004_1-1-1_物理主义_p44.md`
- `1-1_复习课/1-1-1_物理主义/1-1-1-2_有机进化论/0006_1-1-1-2_有机进化论_p99.md`

## 5. 下一个对话如何继续

最稳妥的说法：

“继续处理 ismism 的 clean corpus。请先读取 `/home/weathour/document/programs/codex-portable-skills/bundles/ismism/_bundle/source/ISMISM-CLEANUP-HANDOFF.md`、检查 `split_md_clean/1_实在论/_cleanup_report.jsonl` 和 `proc_a4414e90b876` 的状态，再继续推进。”

如果后台进程还活着，优先：
1. poll 进程状态
2. 读取 `_cleanup_report.jsonl`
3. 检查 `split_md_clean/1_实在论/` 里已生成文件数
4. 决定继续等待、重试报错文件，还是扩展到下一个一级主题

如果后台进程已经结束或丢失，优先：
1. 读取 `_cleanup_report.jsonl`
2. 统计已完成文件和 error 文件
3. 不覆盖已完成结果，按需要重新启动脚本

## 6. 推荐恢复命令

继续处理 `1_实在论`，优先用：

```bash
cd /home/weathour/document/programs/codex-portable-skills/bundles/ismism/_bundle/source
python clean_split_md_with_ollama.py \
  --input-root split_md \
  --subdir '1_实在论' \
  --output-root split_md_clean \
  --timeout 180 \
  --max-batch-chars 4000
```

说明：
- 不带 `--overwrite` 时，脚本会跳过已存在 clean 文件
- 当前脚本已改为向 `_cleanup_report.jsonl` 追加记录，便于多轮接续

如果想专门重跑某些超时文件，可以单独针对其子目录运行，或临时提高 timeout。

## 7. 清洗完成后的后续计划

### Phase A：完成 clean corpus
目标：
- 跑完 `1_实在论`
- 单独重试超时文件
- 确认质量标准稳定

### Phase B：扩展到其余一级主题
按顺序处理：
- `2_形而上学`
- `3_观念论`
- `4_实践`

策略：
- 继续保持“原文不动 + clean 平行层”
- 先得到全书 clean corpus，再做结构提炼

### Phase C：建立 wiki-facing bridge layer
在 clean corpus 之上生成：
- `segments.jsonl`：段级/目录级注册清单
- `chunks.jsonl`：更小粒度的检索块

字段至少应包括：
- `segment_id`
- `toc_id`
- `title`
- `tree_level`
- `parent_toc_id`
- `path_titles`
- `page_start`
- `page_end`
- `raw_md_path`
- `clean_md_path`
- `chunk_id`（chunk 层）
- `text`

### Phase D：把 Atlas 当候选层，而不是最终 wiki
这些现成文件继续利用：
- `file_distillates.jsonl` -> 段级摘要 seed
- `nodes.jsonl` -> entity/concept seed
- `relations.jsonl` -> comparison/synthesis/query seed
- `evidence.jsonl` -> provenance bridge
- `unresolved_queue.jsonl` -> review backlog，不直接视作 wiki 真相层

### Phase E：selective llm-wiki 入库
清洗与 bridge 层完成后，再做：
1. 一个 corpus 级 `wiki/sources/` 页面
2. 4 个一级主题 synthesis 页面
3. 少量高价值 concepts / entities / queries / comparisons

不要做：
- 362 个 split 文件逐个变成 wiki 页面

## 8. 当前总原则

这套 ismism 材料当前应被视为：
- 一个需要 clean + segment + chunk 的大语料库

而不是：
- 一堆直接可以写入 wiki 的现成笔记

正确顺序是：
- 先 clean
- 再 bridge
- 再 selective promotion
