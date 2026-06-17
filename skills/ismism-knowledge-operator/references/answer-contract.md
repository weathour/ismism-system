# Answer Contract

Use compact, evidence-bound answers. Do not dump raw command output unless the user explicitly asks for it.

## Default interpretive answer shape

1. **Conclusion** — 2-4 bullets answering the question directly.
2. **Evidence route** — commands or library paths used, key rows, and clean transcript paths.
3. **Analysis** — interpretation tied to quoted evidence or curated records.
4. **Inference boundary** — what the source supports vs what the agent inferred.
5. **Practical framing** — when relevant, state that this is conceptual interpretation, not professional advice.
6. **Next queries** — 2-3 concrete follow-up queries or curation steps.

## Evidence line format

Prefer this compact anchor format:

```text
row <id> | <toc_id/title or theme> | <clean path> | quote: <short exact excerpt>
```

Keep excerpts short. If a claim depends on wording, read the clean transcript path and cite the row/path.

## Claim discipline

Classify claims internally before writing:

- **Source-backed**: directly supported by exact quotes, row trace, concept sense, relation record, or close-reading card.
- **Library-backed synthesis**: supported by several curated records, but not one sentence in the transcript.
- **Agent inference**: a reasonable bridge from the library to the user's case; label it as inference.
- **Out of scope**: advice or facts that the corpus does not establish.

Do not present agent inference as corpus fact.

## Concept explanation

For a concept answer:

1. list distinct senses if query returns multiple senses;
2. state which sense fits the user's question;
3. include row/path/quote anchors;
4. mention forbidden mixes or boundary notes when available.

## Social symptom analysis

For an everyday-life or social-symptom answer:

1. route through `query social` and relevant concepts/relations;
2. identify mechanism, subject position, object of desire/fear, and social mediation;
3. avoid clinical labeling or policy prescriptions;
4. end with possible practices only as conceptual/practical framing, not diagnosis or treatment.

## Comparison answer

For comparing terms, themes, or positions:

1. query each side separately;
2. compare definitions and evidence rows before giving synthesis;
3. include one overlap and one difference;
4. mark unresolved gaps if one side has weaker evidence.

## Row trace answer

For one row:

1. run `query trace`;
2. read the clean transcript path when close reading is requested;
3. summarize title, segment id, available curated links, and key evidence;
4. avoid extending the row beyond its source text without saying so.
