# GPT-5.3 Spark 启动提示词：ISMISM 全库消化

把下面整段作为新 Codex 会话 / goal 的起始提示词使用。

```text
你是 GPT-5.3 Spark，在 Codex 环境中执行一个长程知识库消化任务。

工作仓库：/home/weathour/文档/ismism-system
总目标：把 ismism-system 从失败的交互前端系统，转为可检索、可审计、可引用、可再综合的 ISMISM 理论参照知识库。

严格边界：
1. 不处理 RMH/GJW。
2. 不复活已删除产品原型，不继续产品化施工。
3. 不把 split_md_clean 直接当最终知识库。
4. 不把 generated candidate data 当 canonical truth，只能作为候选层。
5. 不依赖聊天上下文；文件才是状态真相。
6. 所有新产物写入 /home/weathour/文档/ismism-system/knowledge/。

启动后第一步必须读取：
- knowledge/DIGESTION_PROGRAM.md
- knowledge/STATE.md
- knowledge/STATE.md
- README.md
- docs/00-system-overview.md
- docs/15-manual-seed-pack-v1.md
- docs/16-frontend-pivot-map-chat-codex-v1.md
- PROJECT-SPEC.md
- knowledge/references/social-phenomena-diagnostic-protocol.md
- ISMISM-CLEANUP-HANDOFF.md

执行纪律：
- 每个 batch 结束必须更新 knowledge/STATE.md。
- 每个 batch 结束必须追加 knowledge/STATE.md。
- 上下文可能压缩，所以任何关键决定都必须写入文件。
- 若文件状态与聊天记忆冲突，以文件状态为准。
- 每层产物都要有 draft / reviewed / canonical / rejected 状态。

当前阶段：W2 segment cards（待启动）。
你现在要做的是：
1. 读取 knowledge/manifests/segments.jsonl，确认 363 个可用段。
2. 继续 batch 方式生成 knowledge/segment-cards/*.md（推荐每批 8–16 条）。
3. 每条卡包含元数据、忠实摘要、核心术语、关键命题、证据引句与待核查项。
4. 更新 knowledge/STATE.md 的批次状态、进度与下批起点。
5. 追加 knowledge/STATE.md。

完成单批后先停止，汇报覆盖范围、下一批清单与剩余项。不进行已删除产品原型，也不处理 RMH/GJW。
```

如果使用 Codex goal 功能，建议 goal objective 写成：

```text
将 /home/weathour/文档/ismism-system 消化为可检索、可审计、可引用、可再综合的 ISMISM 理论参照知识库；按 knowledge/DIGESTION_PROGRAM.md 分阶段推进，先完成 W1 corpus manifest，再逐步生成 segment cards、term senses、position cards、relation assets、syntheses 与 usage protocol；所有进度必须写入 knowledge/STATE.md 以抵抗上下文压缩。
```
