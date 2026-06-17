# Forward Tests

Use these prompts to test whether the skill routes tasks and preserves evidence boundaries. Run them in a fresh context when possible. Do not provide expected answers to the testing agent.

## Interpretive query test

```text
Use $ismism-knowledge-operator to analyze how a young person can move from being a consumer of desire to a producer of desire under alienated modern social conditions. Keep the answer evidence-bound and distinguish source-backed claims from inference.
```

Expected behavior to check:

- runs concept/social/relation queries before answering;
- includes row or theme evidence route;
- avoids clinical or self-help absolutism;
- gives an inference boundary.

## Concept navigation test

```text
Use $ismism-knowledge-operator to explain the different ISMISM senses of 欲望 and identify which sense is relevant to consumer desire.
```

Expected behavior to check:

- uses concept query;
- separates multiple senses;
- cites rows and forbidden mixes.

## Row trace test

```text
Use $ismism-knowledge-operator to trace row 176 and explain what can and cannot be inferred from it.
```

Expected behavior to check:

- runs row trace;
- reads or cites clean path;
- avoids overextending the row.

## Curation test

```text
Use $ismism-knowledge-operator to propose the safe steps for adding one relation record connecting 欲望 and 商品化, but do not edit files.
```

Expected behavior to check:

- reads curation protocol and validation matrix;
- identifies schema, relation type, evidence requirement, and validators;
- does not invent unsupported relation evidence.

## Plugin readiness test

```text
Use $ismism-knowledge-operator to check whether this repository is ready to be used as a Codex plugin and report validation evidence.
```

Expected behavior to check:

- runs skill/plugin/product validators;
- reports exact commands;
- notes working tree status.
