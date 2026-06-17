# ISMISM Library

**Languages:** [English](#english) | [中文](#中文)

---

## English

ISMISM Library is a Codex-plugin-ready, corpus-backed interpretation system for the ISMISM transcript collection. It combines source transcripts, curated segment records, concept senses, matrix positions, relation graphs, close-reading cards, theme dossiers, audits, and command-line validation/query tools.

The canonical positioning document is [`docs/product-positioning.md`](docs/product-positioning.md).

The repository is designed around four guarantees:

1. **Traceability** — every interpretive claim keeps row, segment, path, and quote anchors.
2. **Layer separation** — source corpus, curated library, documentation, and tools live in separate product modules.
3. **Validator-backed use** — normal work ends with reproducible validation and query smoke checks.
4. **Plugin operation** — Codex can load the repository as `ismism-system` and use `ismism-knowledge-operator` for traceable knowledge work.

### Repository layout

```text
.codex-plugin/ plugin manifest for Codex
corpus/        source PDF, table of contents, raw transcript markdown, clean transcript markdown
library/       curated manifests, segments, concepts, positions, relations, close-reading cards, themes, audits
docs/          product contract, architecture, status, validation, query, plugin, and usage guides
tools/         ingestion, validation, query helpers, and the ISMISM command runner
examples/      reproducible command examples
reviews/       product architecture review evidence
qa/            product acceptance evidence
skills/        operator protocol for agent-assisted curation
```

### Codex plugin

The Codex plugin manifest lives at `.codex-plugin/plugin.json`. Usage details are in `docs/plugin-usage.md`.

- Plugin name: `ismism-system`
- Display name: `ISMISM Library`
- Primary skill: `ismism-knowledge-operator`
- Primary command runner: `python3 tools/ismism.py`

### Quick checks

```bash
python3 tools/ismism.py validate core
python3 tools/query/social_topics.py 内卷 --limit 3
python3 tools/query/concept.py 主体
```

For the full suite:

```bash
python3 tools/ismism.py validate all
```

### Query examples

```bash
python3 tools/ismism.py query social 内卷 --limit 3
python3 tools/ismism.py query concept 主体 --limit 3
python3 tools/ismism.py query relation 主体 --limit 3
python3 tools/ismism.py query position 3-4-2
python3 tools/ismism.py query trace 176 --limit 5
```

### Current library size

- 363 corpus rows with raw and clean transcript markdown.
- 1676 concept senses across 1228 terms.
- 1044 relation records across 12 relation types.
- 741 close-reading cards across argument, process, and case forms.
- 18 theme dossiers with row manifests and exact quote evidence.

### Working rule

Do not edit transcript text unless the task is explicitly source correction. Normal work should extend or validate `library/` while preserving exact quote evidence against `corpus/clean-markdown/`.

---

## 中文

ISMISM Library 是一个可作为 Codex plugin 使用的、以 ISMISM 文本语料为基础的解释型知识库。它把源文本、段落记录、概念义项、矩阵位置、关系图谱、细读卡、主题档案、审查记录，以及命令行验证/查询工具组织成一个可追溯的知识系统。

项目定位文档见 [`docs/product-positioning.md`](docs/product-positioning.md)。

本仓库围绕四个保证设计：

1. **可追溯性**：每条解释性主张都保留 row、segment、路径和原文引文锚点。
2. **层级分离**：源语料、整理后的知识层、文档层、工具层相互分离。
3. **验证驱动**：常规工作应以可复现的验证和查询烟测结束。
4. **插件化操作**：Codex 可以将本仓库作为 `ismism-system` 加载，并通过 `ismism-knowledge-operator` 执行可追溯的知识工作。

### 仓库结构

```text
.codex-plugin/ Codex 插件 manifest
corpus/        源 PDF、目录注册表、原始 markdown、清洗 markdown
library/       manifests、segments、concepts、positions、relations、close-reading、themes、audits
docs/          项目契约、架构、状态、验证、查询、插件和使用说明
tools/         ingest、validate、query 工具和 ISMISM 命令入口
examples/      可复现命令示例
reviews/       产品架构审查证据
qa/            产品验收证据
skills/        面向 agent 辅助整理的操作协议
```

### Codex 插件

Codex 插件 manifest 位于 `.codex-plugin/plugin.json`，使用说明见 `docs/plugin-usage.md`。

- 插件名：`ismism-system`
- 展示名：`ISMISM Library`
- 核心 skill：`ismism-knowledge-operator`
- 核心命令入口：`python3 tools/ismism.py`

### 快速检查

```bash
python3 tools/ismism.py validate core
python3 tools/query/social_topics.py 内卷 --limit 3
python3 tools/query/concept.py 主体
```

完整验证：

```bash
python3 tools/ismism.py validate all
```

### 查询示例

```bash
python3 tools/ismism.py query social 内卷 --limit 3
python3 tools/ismism.py query concept 主体 --limit 3
python3 tools/ismism.py query relation 主体 --limit 3
python3 tools/ismism.py query position 3-4-2
python3 tools/ismism.py query trace 176 --limit 5
```

### 当前知识库规模

- 363 个 corpus rows，均有 raw 与 clean transcript markdown。
- 1676 个 concept senses，覆盖 1228 个 terms。
- 1044 条 relation records，覆盖 12 种 relation types。
- 741 张 close-reading cards，分为 argument、process、case 三类。
- 18 个 theme dossiers，包含 row manifests 和 exact quote evidence。

### 工作规则

除非任务明确要求 source correction，否则不要修改 transcript text。常规工作应扩展或验证 `library/`，并保持所有解释内容能够追溯到 `corpus/clean-markdown/` 中的精确引文证据。
