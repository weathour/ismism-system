# AGENTS.md

This repository is a standalone ISMISM system repo.

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
2. preserve the hierarchy and method spine
3. make the system more learnable and diagnosable
4. improve agent/scholar interaction surfaces
5. only then optimize convenience or presentation

## Truth sources inside this repo

When files disagree, prefer this order:
1. `目录索引_结构化.csv`
2. `split_md/` and `split_md_clean/`
3. `Zhuyi_Matrix_Engine/Phase*` method docs
4. `Zhuyi_Matrix_Engine/Atlas_DB/*`
5. repo-level docs written later in `docs/`

## Important interpretation rule

Atlas is a legacy auxiliary layer.
Use it as:
- candidate generator
- evidence bridge
- summary seed
- unresolved backlog

Do not treat Atlas as the final truth layer.

## What this repo is building toward

The target system is not just storage. It should eventually support:
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

## Documentation expectations

Any substantial change should keep these clear:
- what the repo is for
- what layer changed
- what remains legacy
- what remains future design
- how an agent should resume work

## Current strategic stance

The repo should move from:
- corpus storage

toward:
- interactive theoretical apprentice system
- diagnostic workbench
- scholar-collaboration engine
