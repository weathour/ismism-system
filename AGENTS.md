# AGENTS.md

This repository is a standalone ISMISM knowledge-processing repo.

Current mainline handoff:

1. `ISMISM-MAINLINE-HANDOFF.md`
2. `knowledge/STATE.md`
3. `knowledge/DIGESTION_PROGRAM.md`
4. `knowledge/references/movement-patterns-guide.md` (matrix movement taxonomy + reading protocol)
5. `DIRECTORY_MAP.md` (concise directory/function map)
6. `knowledge/w10-absorption/PLAN.md` and `knowledge/w10-absorption/index.md` (current further-absorption pilot)
7. `knowledge/themes/ai/README.md` and `knowledge/themes/ai/ai-synthesis.md` (AI theme maximum absorption layer)
8. `knowledge/themes/chinese-philosophy/README.md` and `knowledge/themes/chinese-philosophy/chinese-philosophy-synthesis.md` (Chinese Philosophy maximum absorption layer)
9. `knowledge/themes/religion/README.md` and `knowledge/themes/religion/religion-synthesis.md` (Religion Problem maximum absorption layer)

## Core orientation

Do not treat this repo as a normal wiki or a neutral philosophy encyclopedia.
Treat it as a combined:
- corpus repo
- theory-training repo
- diagnostic-method repo
- agent/scholar interaction workspace

## Priority order

When working here, prefer this order of concern:
1. preserve corpus integrity
2. preserve row/segment/quote traceability
3. preserve the hierarchy and method spine
4. extend the knowledge layer (`knowledge/`) in small auditable batches
5. only then consider interaction surfaces or presentation

## Truth sources inside this repo

When files disagree, prefer this order:
1. `目录索引_结构化.csv`
2. `split_md/` and `split_md_clean/`
3. `knowledge/manifests/*`
4. `knowledge/segment-cards/*`
5. `knowledge/lexicon/*`
6. `knowledge/position-cards/*`
7. `knowledge/relations/*`
8. `knowledge/qa/*`
9. `knowledge/syntheses/*`
10. `knowledge/w10-absorption/*` (pilot-draft close-reading aids)
11. `Zhuyi_Matrix_Engine/Phase*` method docs
12. `Zhuyi_Matrix_Engine/Atlas_DB/*`
13. repo-level tombstone docs in `docs/archive/`

## Important interpretation rule

Atlas is a legacy auxiliary layer.
Use it as:
- candidate generator
- evidence bridge
- summary seed
- unresolved backlog

Do not treat Atlas as the final truth layer.

Old frontend/product work was removed on 2026-06-12. The deleted route surfaces (`src/`, `dist/`, `docs/00-*` through `docs/16-*`, old cleanup handoff snapshots) must not be restored or allowed to drive current work unless the user explicitly asks for historical recovery.

## What this repo is building toward

The current target is first a stable, auditable knowledge layer. A future system may support:
- curriculum traversal
- case-based training
- provisional diagnosis
- disagreement handling
- scholar-in-the-loop refinement
- practice-oriented interpretation

## Safe editing rules

- Do not overwrite `split_md/` raw text.
- Do not casually rewrite `split_md_clean/` unless explicitly working on text cleaning.
- Keep legacy method docs in `Zhuyi_Matrix_Engine/` intact unless there is a clear migration reason.
- Prefer adding repo-level explanatory docs over mutating legacy source material.
- Keep path and filename compatibility where practical; existing scripts assume the current root layout.
- Keep W3 term senses and W5 relation assets in `draft` unless an explicit review step promotes them.

## Documentation expectations

Any substantial change should keep these clear:
- what the repo is for
- what layer changed
- what remains legacy
- what remains future design
- how an agent should resume work
- whether `DIRECTORY_MAP.md` or the repo-local skill draft needs a navigation update

## Current strategic stance

The repo has moved from old frontend/prototype rescue toward:
- corpus evidence layer
- segment-card layer
- term-sense layer
- relation-asset layer
- later syntheses / usage protocols
- W10 pilot further-absorption layer for argument / process / case close reading
- AI theme maximum absorption layer for AI / VR / 智能 / 算法 / 机器人
- Chinese Philosophy maximum absorption layer for 儒家 / 道家 / 佛教 / 禅 / 唯识 / 中观 / 毛哲学
- Religion Problem maximum absorption layer for 宗教实在论 / 神圣秩序 / 信仰 / 偶像 / 灵性 / 拜物 / 救赎 / 意识形态

Repo-local skill draft:
- `skills/ismism-knowledge-operator/SKILL.md` documents a thin operator protocol for future Codex/agent use. It should point back to repository truth sources rather than copying the knowledge layer.
