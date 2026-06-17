# Codex Plugin Usage

ISMISM Library can be installed or linked as a Codex plugin. The plugin identity is defined by `.codex-plugin/plugin.json`, and the operational behavior is provided by `skills/ismism-knowledge-operator/SKILL.md` plus the command-line tools under `tools/`.


## Installation

For local source-tree testing:

```bash
codex plugin marketplace add /absolute/path/to/ismism-system
codex plugin add ismism-system@ismism-system
```

From GitHub after publication:

```bash
codex plugin marketplace add weathour/ismism-system --ref main
codex plugin add ismism-system@ismism-system
```

Restart Codex or open a new session if the skill does not appear immediately. The repository includes a `plugins/ismism-system` marketplace compatibility alias so Codex CLI can install this single-plugin repository through its normal marketplace flow.

## Plugin identity

- Plugin name: `ismism-system`
- Display name: `ISMISM Library`
- Primary skill: `ismism-knowledge-operator`
- Primary command runner: `python3 tools/ismism.py`

## What the plugin gives Codex

The plugin exposes an agent-operable knowledge library with these responsibilities:

1. preserve corpus traceability through row, segment, clean transcript path, and exact quote anchors;
2. query concepts, relations, positions, social topics, themes, and evidence traces;
3. validate curated layers before any completion claim;
4. guide curation work through the repository-local skill protocol.

## Standard prompts

Use the plugin when the task asks Codex to work with ISMISM concepts, themes, relation records, close-reading cards, or evidence-backed diagnostic analysis.

Examples:

```text
Use ISMISM to analyze why a young person may lose desire under alienated social conditions.
Query ISMISM for concepts related to 主体 and 欲望.
Validate the ISMISM library after updating a theme dossier.
```


## Skill protocol

The primary skill is intentionally split for progressive disclosure:

- `skills/ismism-knowledge-operator/SKILL.md` keeps the core operating rules.
- `skills/ismism-knowledge-operator/references/task-routing.md` maps user requests to query paths.
- `skills/ismism-knowledge-operator/references/answer-contract.md` defines evidence-bound answer shapes.
- `skills/ismism-knowledge-operator/references/curation-protocol.md` defines safe edit workflows.
- `skills/ismism-knowledge-operator/references/validation-matrix.md` maps changed surfaces to validators.
- `skills/ismism-knowledge-operator/references/forward-tests.md` provides reusable skill test prompts.


## Use from any repository

After installation, the plugin should be invoked from any working repository through its skill. The skill does not require the current working directory to be the ISMISM repository. It resolves the plugin root through its bundled wrapper:

```bash
python3 <installed-skill-dir>/scripts/ismism.py query concept 欲望 --limit 3
python3 <installed-skill-dir>/scripts/ismism.py query social 消费主义 --limit 3
python3 <installed-skill-dir>/scripts/ismism.py root
```

In normal Codex use, ask for `$ismism-knowledge-operator`; Codex reads the installed `SKILL.md`, gets the skill directory, and runs the wrapper from there. Returned transcript paths are relative to the plugin root printed by `root`.

If you are maintaining the source checkout rather than using an installed cached copy, set `ISMISM_LIBRARY_ROOT=/absolute/path/to/ismism-system` before running the wrapper.

## Command contract

```bash
python3 tools/ismism.py validate core
python3 tools/ismism.py validate all
python3 tools/ismism.py validate residue
python3 tools/ismism.py query social 内卷 --limit 3
python3 tools/ismism.py query concept 主体 --limit 3
python3 tools/ismism.py query relation 主体 --limit 3
python3 tools/ismism.py query position 3-4-2
python3 tools/ismism.py query trace 176 --limit 5
```

## Development checks

Before publishing or reinstalling the plugin, run:

```bash
python3 <plugin-creator-skill>/scripts/validate_plugin.py .
python3 tools/ismism.py validate all
python3 tools/validate/library_contract.py --repo . --residue-only
```

The plugin manifest should stay minimal unless companion files are actually added. Do not list MCP servers, apps, hooks, icons, logos, or screenshots until those files exist and are validated.
