# Skill Strengthening Requirements / Skill 强化需求分析

## Purpose / 目标

Strengthen `skills/ismism-knowledge-operator/` from a thin repository navigation note into the primary Codex operating protocol for ISMISM Library. The skill should let a fresh Codex instance reliably query, interpret, curate, and validate the repository while preserving row, segment, path, quote, and validator traceability.

强化目标是：让 `skills/ismism-knowledge-operator/` 从一个简短导航说明，升级为 ISMISM Library 的主要 Codex 操作协议。一个新的 Codex 实例加载该 skill 后，应能稳定完成查询、解释、整理和验证，同时保留 row、segment、path、quote 与 validator 证据链。

## Current state / 当前状态

Current skill surface:

- `skills/ismism-knowledge-operator/SKILL.md`
- `skills/ismism-knowledge-operator/agents/openai.yaml`

Current strengths:

1. It has valid frontmatter and a clear skill name.
2. It identifies the source-order hierarchy.
3. It lists minimal validation commands.
4. It is short and cheap to load.

Current gaps:

1. **Trigger description is too narrow**: it does not explicitly cover social symptom analysis, concept disambiguation, relation traversal, row tracing, theme curation, or validation-only tasks.
2. **No task routing**: it does not map user intents to `tools/ismism.py query ...`, direct theme helpers, source reads, or validators.
3. **No answer contract**: it does not require outputs to distinguish evidence, interpretation, inference, and boundaries.
4. **No curation protocol**: it does not tell Codex how to add or revise concept senses, relation records, close-reading cards, theme evidence, or synthesis notes.
5. **No safety/product boundary**: it does not remind Codex that the library is not medical, legal, policy, current-event, or clinical advice.
6. **No progressive disclosure**: detailed protocols are not split into reference files, so future growth would either bloat `SKILL.md` or leave important guidance missing.
7. **No forward-test scenarios**: there is no reusable set of prompts to test whether the skill actually improves agent behavior.

## Target skill role / 目标 skill 角色

The strengthened skill should be the operational bridge between four layers:

```text
user question
→ skill routing and evidence discipline
→ ISMISM CLI / library files / source transcripts
→ evidence-bound answer or curated asset change
```

It should not duplicate the whole library. It should teach Codex how to use the library.

该 skill 不应复制知识库内容，而应说明如何操作知识库。

## Primary task classes / 主要任务类型

### 1. Evidence-backed interpretation / 证据支撑解释

Example user requests:

- Analyze desire loss, alienation, anxiety, involution, platform attention, family pressure, or consumer desire through ISMISM.
- Explain a concept such as `主体`, `欲望`, `犬儒`, `异化`, or `商品拜物`.
- Compare two concepts or themes.

Required behavior:

1. Start with query helpers for relevant concepts, relations, themes, and traces.
2. Read cited clean transcript paths when making interpretive claims.
3. Output a bounded synthesis with evidence anchors.
4. Explicitly separate source-backed claims from agent inference.
5. State non-advice boundary when the topic touches health, law, policy, housing, finance, or clinical psychology.

### 2. Query and navigation / 查询与导航

Example user requests:

- Query concept `主体`.
- Find relations around `欲望`.
- Show row trace for `176`.
- Find evidence for `内卷`.

Required behavior:

- Route to `python3 tools/ismism.py query concept|relation|position|trace|social ...` first.
- Use direct theme helpers only when the central task is a specific theme.
- Summarize results with row/path/quote anchors, not only command output.

### 3. Curation and library extension / 整理与扩展

Example user requests:

- Add a concept sense.
- Add a relation record.
- Add close-reading cards.
- Update a theme dossier or evidence bank.
- Extend a synthesis using existing evidence.

Required behavior:

1. Identify target layer and schema before editing.
2. Reuse existing IDs, naming conventions, and templates.
3. Preserve source quote exactness against `corpus/clean-markdown/`.
4. Run targeted validators plus product contract validation.
5. Record nontrivial review evidence in `reviews/` or acceptance evidence in `qa/` when appropriate.

### 4. Validation and publication readiness / 验证与发布准备

Example user requests:

- Validate the library.
- Check plugin readiness.
- Confirm no public-surface residue.
- Prepare for GitHub publication.

Required behavior:

- Run the smallest validator that proves the claim, then broaden if publication readiness is being claimed.
- For plugin changes, run plugin validation.
- For public docs or skill changes, run residue validation.
- Report exact command evidence and remaining gaps.

## Required output contract / 输出契约

For interpretive answers, the strengthened skill should require this compact structure unless the user asks otherwise:

1. **Conclusion**: direct answer in 2-4 bullets.
2. **Evidence route**: queried terms/themes/relations and key rows.
3. **Analysis**: source-backed interpretation.
4. **Inference boundary**: what is inferred rather than directly stated.
5. **Practical framing**: if applicable, non-clinical/non-legal/non-policy framing.
6. **Follow-up query options**: 2-3 concrete next queries or curation steps.

For curation/editing tasks, the output should include:

1. files changed;
2. schema or pattern followed;
3. validators run;
4. remaining risks or validation gaps;
5. commit hash if committed.

## Proposed skill structure / 建议 skill 结构

Keep `SKILL.md` concise and move details into one-level references.

```text
skills/ismism-knowledge-operator/
  SKILL.md
  agents/openai.yaml
  references/
    task-routing.md
    answer-contract.md
    curation-protocol.md
    theme-absorption-protocol.md
    validation-matrix.md
    forward-tests.md
```

### `SKILL.md`

Role:

- short trigger-focused frontmatter;
- core operating principles;
- source order;
- when to read each reference;
- minimal command contract;
- stop/validation rule.

### `references/task-routing.md`

Map user intents to query commands, source reads, and docs.

### `references/answer-contract.md`

Define evidence-bound answer shapes for concept explanation, social symptom analysis, comparison, and row trace interpretation.

### `references/curation-protocol.md`

Define safe edit workflows for concepts, relations, close-reading cards, themes, syntheses, and source correction.

### `references/theme-absorption-protocol.md`

Define the end-to-end workflow for creating or substantially extending major theme packages: scope, candidate scan, row manifest, evidence bank, taxonomy, concept/relation/close-reading batches, syntheses, query helper, validator, social-topic routing, and acceptance evidence.

### `references/validation-matrix.md`

Map changed surfaces to required validators.

### `references/forward-tests.md`

Provide realistic prompts for forward-testing the skill without leaking expected answers.

## Frontmatter requirements / Frontmatter 要求

The strengthened `description` should include all trigger contexts because Codex decides whether to load the skill from metadata alone. It should mention:

- ISMISM Library;
- corpus traceability;
- evidence-backed interpretation;
- concept/relation/theme/row trace query;
- curation and validation;
- Codex plugin operation.

Avoid long explanations in frontmatter; make it trigger-complete but compact.

## Validation requirements / 验证要求

After implementing the strengthened skill, run:

```bash
python3 tools/ismism.py validate core
python3 tools/validate/library_contract.py --repo . --residue-only
python3 /path/to/skill-creator/scripts/quick_validate.py skills/ismism-knowledge-operator
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

If `agents/openai.yaml` changes, ensure it still matches the revised skill intent.

## Acceptance criteria / 验收标准

1. `SKILL.md` stays concise and contains only operational essentials.
2. Detailed behavior is discoverable through direct `references/` files, not scattered docs.
3. The skill routes at least these requests correctly: concept query, relation query, social symptom analysis, row trace, theme update, full validation, plugin readiness.
4. Interpretive answers must include evidence route and inference boundary.
5. Curation tasks must run targeted validators and product residue validation.
6. Plugin validation passes.
7. Product contract residue validation remains zero.
8. No public docs or skill files reintroduce old directory names, private paths, or deprecated product labels.

## Implementation priority / 实施优先级

1. Rewrite `SKILL.md` and strengthen frontmatter.
2. Add `references/task-routing.md` and `references/validation-matrix.md`.
3. Add `references/answer-contract.md`.
4. Add `references/curation-protocol.md`.
5. Add `references/theme-absorption-protocol.md` for major theme package creation/extension.
6. Add `references/forward-tests.md`.
7. Validate skill and plugin.
8. Forward-test with at least two realistic prompts: one interpretive query and one curation/validation task.
