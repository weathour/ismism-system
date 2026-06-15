# ismism-system

ISMISM 的独立知识处理仓库。

当前主线不是继续旧前端原型，也不是继续早期 clean corpus 流水线，而是把 ISMISM 处理为一个：

- 可检索
- 可审计
- 可引用
- 可再综合
- 可接入后续写作/诊断系统

的理论知识库。

## 当前主线

```text
PDF / TOC / split_md / split_md_clean
→ W1 corpus manifests
→ W2 segment cards
→ W3 term senses
→ W4 position cards
→ W5 relation assets
→ W7 syntheses / usage protocol
→ W10 further absorption pilot
→ AI theme maximum absorption layer
→ Chinese Philosophy maximum absorption layer
→ Religion Problem maximum absorption layer
```

核心纪律：

> 先固定证据层，再生成解释层；所有解释对象必须能追溯到 row / segment / quote。

## 当前状态

最新状态见：

- `ISMISM-MAINLINE-HANDOFF.md`
- `DIRECTORY_MAP.md`
- `knowledge/STATE.md`
- `knowledge/logs/operation-log.md`

截至 2026-06-15 当前主线交接：

| Layer | Status |
|---|---|
| W1 corpus manifests | complete |
| W2 segment cards | complete, 363 cards |
| W3 term senses | complete draft, 705 senses / 357 terms |
| W4 position cards | complete draft, 256 cards |
| W5 relation assets | complete draft, 191 relations / 12 types |
| W6 audit | complete, 4 reports |
| W7 syntheses | complete draft, 6 syntheses |
| W8 usage protocol | complete, 3 protocol docs |
| W9 integration | repo-local lightweight index accepted as sufficient; external copy is downstream/manual |
| W10 further absorption | pilot-draft, 122 cards / 3 card types + validator |
| AI theme maximum absorption | 60-row manifest, 208 quote-bank records, 37 W3 draft senses, 30 W5 draft relations, 28 AI W10 rows/cards |
| Chinese Philosophy maximum absorption | 70-row manifest, 238 quote-bank records, 60 W3 draft senses, 50 W5 draft relations, 45 new Chinese W10 cards |
| Religion Problem maximum absorption | 80-row manifest, 226 quote-bank records, 64 W3 draft senses, 51 W5 draft relations, 45 new Religion W10 cards |
| absorption strength snapshot | 143/363 rows remain W1/W2-only; 64.6% clean-text volume has W3/W5/W10 absorption; 85 rows now have W3+W5+W10 overlap |

所有 W3/W5 产物当前仍是 `draft`，不得直接升为 canonical。

## 新上下文阅读顺序

1. `ISMISM-MAINLINE-HANDOFF.md`
2. `DIRECTORY_MAP.md`
3. `knowledge/STATE.md`
4. `knowledge/DIGESTION_PROGRAM.md`
5. `knowledge/logs/operation-log.md`
6. `knowledge/qa/w5-relation-audit.md`
7. `knowledge/lexicon/term-senses.jsonl`
8. `knowledge/relations/relation-assets.jsonl`
9. `knowledge/w10-absorption/PLAN.md` and `knowledge/w10-absorption/index.md`
10. `knowledge/qa/absorption-strength-distribution.md`
11. `knowledge/themes/ai/README.md` and `knowledge/themes/ai/ai-synthesis.md`
12. `knowledge/themes/chinese-philosophy/README.md` and `knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md`
13. `knowledge/themes/religion/README.md` and `knowledge/themes/religion/religion-synthesis.md`

如需查证，再读：

- `knowledge/segment-cards/index.md`
- `knowledge/segment-cards/*.md`
- `split_md_clean/...`
- `split_md/...`

## 当前核心目录

- `knowledge/` — 当前主线处理层；优先使用。
- `knowledge/manifests/` — W1 结构清单。
- `knowledge/segment-cards/` — W2 分段卡。
- `knowledge/lexicon/` — W3 术语义项。
- `knowledge/relations/` — W5 关系资产。
- `knowledge/qa/` — 审计记录。
- `knowledge/w10-absorption/` — W10 pilot-draft argument/process/case close-reading layer.
- `knowledge/themes/ai/` — AI / VR / 智能 / 算法 / 机器人 maximum absorption layer.
- `knowledge/themes/chinese-philosophy/` — Chinese Philosophy / 儒家 / 道家 / 佛教 / 禅 / 唯识 / 中观 / 毛哲学 maximum absorption layer.
- `knowledge/themes/religion/` — Religion Problem / 宗教问题 maximum absorption layer for religious realism, sacred order, faith/idol/spirit/fetishism, salvation, ideology, and practice transformation.
- `DIRECTORY_MAP.md` — 当前目录/功能结构的短导航。
- `skills/ismism-knowledge-operator/` — repo-local 薄 skill 草案；封装使用纪律，不复制知识内容。
- `split_md/` — 原始切分文本，证据层。
- `split_md_clean/` — 轻清洗文本，证据层。
- `目录索引_结构化.csv` — TOC 结构真相源。
- `主义主义 (未明子) (z-library.sk, 1lib.sk, z-lib.sk).pdf` — 原始 PDF。

## 已删除 / 非主线内容

为防止旧路线继续牵引当前工作，2026-06-12 已删除旧 clean-corpus handoff 指针、旧前端源码、旧产品文档、构建输出和压缩实验残留。保留的说明见：

- `docs/archive/legacy-process-and-prototype-index.md`

仍保留但不得作为当前解释真相的内容：

- `Zhuyi_Matrix_Engine/Atlas_DB/*` — 候选层，不是 canonical truth。
- `split_pdf/` — 可再生 PDF 分片派生层，不是解释层。
- 根目录 PDF/TOC/split 脚本 — 仅作恢复工具，未经明确任务不要运行。

已删除的旧路线包括：

- `src/`, `dist/`, `index.html`, `package.json`, `vite.config.*`, `tsconfig*`, `node_modules/`。
- `docs/00-*` 到 `docs/16-*` 的旧产品/前端设计文档。
- `ISMISM-CLEANUP-HANDOFF.md` 及旧 archive snapshots。
- `graphify-out/`, `compress_test/`, `*_compressed.md`, `__pycache__/`。

若未来需要交互界面，必须从 `knowledge/` 的导出契约重新设计，不从旧前端恢复。

## 当前下一步

本仓库内 W1–W9 知识层已完成并通过 repo-local validator；W10 首批进一步吸收为 pilot-draft。恢复或交付前优先运行：

```bash
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_ai_theme.py --repo . --final
python3 knowledge/scripts/validate_chinese_philosophy_theme.py --repo . --final
python3 knowledge/scripts/validate_religion_theme.py --repo . --final
python3 knowledge/scripts/validate_master_spec_outputs.py --repo .
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 191 --require-type-min 2
```

若未来需要真正接入 `psychoanalytic-writing-lab`，按 `knowledge/integration/psychoanalytic-writing-lab/COPY-INSTRUCTIONS.md` 由人工或另行授权流程处理外部文件。

若未来需要让 Codex/agent 以稳定协议使用本仓库，可参考 repo-local skill 草案：

- `skills/ismism-knowledge-operator/SKILL.md`

当前也提供只读轻量查询脚本：

```bash
python3 knowledge/scripts/query_term.py 主体
python3 knowledge/scripts/query_position.py 3-4-2
python3 knowledge/scripts/query_relation.py --type objectifies
python3 knowledge/scripts/trace_evidence.py term:主体:s01
python3 knowledge/scripts/query_ai_theme.py AI身体化
python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3
python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3
```

## 禁止事项

- 不要继续旧前端救援线。
- 不要把 Atlas_DB 当 canonical。
- 不要把 W3/W5 draft 义项或关系升 canonical。
- 不要处理 RMH/GJW。
- 不要大范围重写 `split_md/` 或 `split_md_clean/`。

## 一句话

> 本仓库现在的主线是 ISMISM 理论知识库消化：W1–W9 repo-local 完成状态已接受；W10 已扩展为 122 张 pilot-draft close-reading cards；AI theme、Chinese Philosophy theme 与 Religion Problem theme 已分别把 AI/VR、中国哲学/毛哲学、宗教问题主题提升为可查询、可审计、可综合的主题层；143/363 行仍为 W1/W2-only，64.6% clean-text volume 已有 W3/W5/W10 任一深吸收，85 行达到 W3+W5+W10 全重叠；旧清洗/前端产品路线已删除，保留 tombstone 说明。
