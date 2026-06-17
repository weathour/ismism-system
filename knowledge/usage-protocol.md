# ISMISM Usage Protocol

Use this repository as a corpus-grounded diagnostic and theory-training knowledge layer. Every answer should preserve row, segment, clean-path, quote, term, relation, and card traceability when making substantive claims.

## Truth path

1. Resolve the row or theme through `目录索引_结构化.csv`, `knowledge/manifests/segments.jsonl`, or a theme row manifest.
2. Read the relevant `split_md_clean/` file or exact evidence-bank quote.
3. Use W3/W4/W5/W10 assets as interpretive supports, not replacements for text evidence.
4. When answering practical or social diagnosis questions, route through the relevant theme README and `knowledge/references/social-phenomena-diagnostic-protocol.md`.

## Guardrails

- W3/W5 assets are draft.
- W10 cards are pilot-draft.
- Do not turn diagnostic labels into clinical, legal, policy, financial, or current-events advice.
- Do not overwrite corpus files during interpretation tasks.
- Do not add generated caches or local session state to the project.

## Validation before publication

```bash
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
