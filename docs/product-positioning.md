# Product Positioning / 项目定位

## English

### One-sentence positioning

ISMISM Library is a Codex-native, evidence-bound interpretation library: it turns the ISMISM transcript corpus into traceable concepts, relations, close-reading records, theme dossiers, and validation-backed tools for agent-assisted analysis.

### What the project is

1. **A corpus-backed knowledge product** — source rows, segment records, transcript paths, and exact quote evidence remain the base layer for every curated claim.
2. **A Codex plugin first** — the public product surface is `.codex-plugin/plugin.json`, `skills/ismism-knowledge-operator/`, and `tools/ismism.py`, so Codex can query, validate, and extend the library with traceability.
3. **An interpretation engine, not a loose wiki** — concepts, positions, relations, close-reading cards, and themes are structured assets that support argument reconstruction and social-theoretical analysis.
4. **A verifiable curation system** — validators define whether the library is internally consistent enough to publish, reuse, or extend.

### Primary users

- Codex or other coding agents operating the repository as a plugin.
- Researchers, curators, and advanced readers who need evidence-backed interpretation rather than unsourced summaries.
- Future downstream builders who may expose the library through MCP, API, search UI, learning paths, or case-analysis workflows.

### Core use cases

- Ask a theory or social-life question and receive an evidence-anchored interpretation.
- Query concepts, relations, positions, themes, and source traces from the command line.
- Add or revise curated knowledge records while preserving source anchors.
- Validate the corpus/library/plugin surface before publishing or extending the project.

### What the project is not

- Not a general encyclopedia.
- Not a personal note dump.
- Not a generic chatbot wrapper.
- Not medical, legal, policy, or current-event advice.
- Not a frontend product yet; the current public form is plugin plus CLI plus curated library.

### Product direction

The next development should preserve this order:

1. **Plugin quality** — stronger skill prompts, clearer command outputs, stable install/use docs.
2. **Agent usability** — JSON query output, reusable analysis templates, and stricter evidence citation formats.
3. **Library depth** — more cross-theme relations, close-reading coverage, and synthesis documents.
4. **Distribution surfaces** — MCP/server interface, packaged CLI, documentation site, or public demo only after the library contract stays stable.

### Positioning formula

```text
ISMISM corpus + curated interpretation layers + validation tools + Codex skill
= evidence-bound interpretation plugin
```

## 中文

### 一句话定位

ISMISM Library 是一个面向 Codex 的、证据约束的解释型知识库：它把 ISMISM 文本语料转化为可追溯的概念、关系、细读记录、主题档案和验证工具，用于 agent 辅助的理论分析。

### 本项目是什么

1. **以语料为根基的知识产品**：source rows、segment records、transcript paths 和 exact quote evidence 是所有整理性主张的基础层。
2. **首先是 Codex plugin**：公开产品入口是 `.codex-plugin/plugin.json`、`skills/ismism-knowledge-operator/` 和 `tools/ismism.py`，使 Codex 能够查询、验证并继续扩展知识库。
3. **解释引擎，而不是松散 wiki**：概念、位置、关系、细读卡和主题档案都是结构化资产，用于支撑论证重建和社会理论分析。
4. **可验证的整理系统**：validators 决定这个知识库是否达到可发布、可复用、可继续扩展的内部一致性。

### 主要用户

- 将本仓库作为 plugin 操作的 Codex 或其他 coding agents。
- 需要证据支撑解释、而不是无来源摘要的研究者、整理者和深度读者。
- 未来希望把知识库接入 MCP、API、搜索界面、学习路径或案例分析流程的下游开发者。

### 核心使用场景

- 提出理论问题或现代生活问题，并得到带证据锚点的解释。
- 通过命令行查询 concepts、relations、positions、themes 和 source traces。
- 增补或修订整理后的知识记录，同时保留原文锚点。
- 在发布或扩展项目前验证 corpus、library 和 plugin surface。

### 本项目不是什么

- 不是通用百科。
- 不是个人笔记堆。
- 不是普通 chatbot 外壳。
- 不提供医疗、法律、政策或时事建议。
- 目前还不是前端产品；当前公开形态是 plugin + CLI + curated library。

### 产品发展方向

后续推进应保持这个顺序：

1. **插件质量**：强化 skill prompt，改善命令输出，稳定安装/使用文档。
2. **Agent 可用性**：增加 JSON 查询输出、可复用分析模板和更严格的证据引用格式。
3. **知识库深度**：扩展跨主题关系、细读覆盖和综合文档。
4. **分发界面**：只有在 library contract 稳定后，再推进 MCP/server interface、packaged CLI、文档站或公开 demo。

### 定位公式

```text
ISMISM 语料 + 结构化解释层 + 验证工具 + Codex skill
= 证据约束的解释型 plugin
```
