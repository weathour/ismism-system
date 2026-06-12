# W3 启动提示词：ISMISM 术语义项 Registry

把下面整段作为新 Codex 会话 / goal 的起始提示词使用。

```text
你是在 Codex 环境中继续执行 ISMISM 知识库消化任务。

工作仓库：/home/weathour/文档/ismism-system
当前阶段：W3 术语义项 registry（term senses）

总目标：在 W1 结构 manifest 与 W2 segment cards 已完成的基础上，建立一个可检索、可审计、可引用的核心术语义项层，拆分“主体/客体/实践/历史/符号/场/本体论/认识论/目的论”等高风险词在不同语境中的不同含义，避免后续 W4/W5/W7 把同词不同义混用。

启动前必须先读：
1. knowledge/DIGESTION_PROGRAM.md
2. knowledge/STATE.md
3. knowledge/logs/operation-log.md
4. knowledge/qa/w1-recovery-audit.md
5. knowledge/manifests/corpus-manifest.json
6. knowledge/manifests/segments.jsonl
7. knowledge/manifests/chunks.jsonl
8. knowledge/manifests/missing-and-anomalies.md
9. knowledge/segment-cards/index.md
10. Zhuyi_Matrix_Engine/Phase0_Corpus/Matrix_Backbone.md
11. Zhuyi_Matrix_Engine/Phase1_Concepts/Boundary_Rules.md
12. README.md
13. docs/00-system-overview.md
14. docs/15-manual-seed-pack-v1.md
15. docs/16-frontend-pivot-map-chat-codex-v1.md
16. ISMISM-CLEANUP-HANDOFF.md

已知前置状态（必须核验，不要只相信本提示）：
- W1 已完成：segments.jsonl = 363；chunks.jsonl = 1594；raw/clean markdown = 363；row 176 已恢复。
- W2 已完成：knowledge/segment-cards/ 非 index 的段卡应为 363 张；index 应覆盖 row 1–363；STATE 中 segment cards 应为 363/363。
- split_pdf 是派生层，目前只有 row 176 对应 PDF，不阻断 W3。
- Atlas_DB 只能作为候选层，不得作为 canonical truth。
- 旧前端 src/dist/manualSeed 只作为历史资产，不牵引 W3。

W3 产物：
1. knowledge/lexicon/term-senses.jsonl
2. knowledge/lexicon/core-terms.md
3. knowledge/lexicon/ambiguous-terms.md
4. 建议增加：knowledge/qa/w3-lexicon-audit.md 或按批次追加审计说明

首批重点术语（从中选择，不要一次全做完）：
- 主体、客体、实体、物质、历史、人民、理论、理论家、实践、实践单元
- 场、符号、符号秩序、本体论、认识论、目的论、意识形态
- 去主体化、主体化、客体化、中介、跃迁、误认、闭合、有限性

每个义项记录至少包含：
- sense_id：建议格式 `term:<术语>:sNN`
- term：术语原词
- sense_label：短标签，说明该义项的语境功能
- definition：只根据 ISMISM 语料归纳的定义，不外加外部理论
- axis：场域 / 本体论 / 认识论 / 目的论 / 复合 / 未定
- source_segments：相关 segment_id / row_id / toc_id / segment-card path
- evidence_quotes：短引句，必须能回到 segment card 或 clean md
- position_context：若能定位，写 4×4×4×4 矩阵位置；若不能，写 unknown
- contrast_with：容易混用的其他义项或术语
- forbidden_mix：禁止混用说明
- confidence：low / medium / high
- status：draft / reviewed / canonical / rejected（初始必须 draft）
- audit_notes：证据薄弱、定义不稳、待复核之处

执行方法：
1. 先做 W2 完成审计：确认 363 张段卡存在、index 覆盖 1–363、无缺失 row_id。若不一致，先写 QA note，不进入 W3。
2. 建立术语候选统计：从 knowledge/segment-cards/*.md 的 Core Terms / Key Propositions / Evidence Anchors 抽取首批重点词出现位置；必要时回读 split_md_clean 原文。
3. 每批只处理 1–3 个术语。优先建议第一批：主体、客体、实践。
4. 对每个术语，不要写单一定义；先列不同语境，再判断是否构成多个义项。
5. 每个义项必须有证据 segment 与短引句；没有证据就标为 ambiguous，不要 canonical。
6. 生成/追加 term-senses.jsonl，同时更新 core-terms.md 和 ambiguous-terms.md。
7. 每批结束必须更新 knowledge/STATE.md 的 W3 进度、下一批建议与 handoff block。
8. 每批结束必须追加 knowledge/logs/operation-log.md。

严格禁止：
- 禁止把术语义项写成普通百科词条。
- 禁止用外部哲学常识覆盖 ISMISM 内部语料。
- 禁止把 Atlas_DB 候选节点直接当成义项。
- 禁止把“主体/客体/实践/历史”等词在不同层级中混成一个定义。
- 禁止在 W3 就写全局综合；综合留给 W7。
- 禁止继续旧前端或处理 RMH/GJW。

本次建议目标：
完成 W3 第一批术语义项草案：主体、客体、实践。输出 term-senses.jsonl 的 draft 记录，并同步生成 core-terms.md / ambiguous-terms.md 的初版。完成后停止，汇报证据覆盖、未定项和下一批建议。
```

如果使用 Codex goal 功能，建议 objective 写成：

```text
在 /home/weathour/文档/ismism-system 中启动 W3 术语义项 registry：基于已完成的 W1 manifests 与 W2 segment cards，先审计 W2 完整性，再为主体、客体、实践等首批核心术语生成可审计的义项记录，更新 knowledge/lexicon/*、knowledge/STATE.md 与 operation-log.md；不做旧前端、不处理 RMH/GJW、不进入全局综合。
```
