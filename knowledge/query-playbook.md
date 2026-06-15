# W8 Query Playbook

- status: draft protocol
- created: 2026-06-09 CST
- scope: standard paths for common ISMISM knowledge queries.

## 1. “What does a term mean here?”

Path:

```text
term-senses.jsonl → core-terms.md → evidence quote in split_md_clean → optional synthesis
```

Example: `星丛` → `term:星丛:s01/s02` → row 229 → `part-3-idealism.md`.

Optional CLI:

```bash
python3 knowledge/scripts/query_term.py 星丛
python3 knowledge/scripts/trace_evidence.py term:星丛:s01
```

## 2. “Which sense of this term is used in this row?”

Path:

```text
row_id → segment card → term-senses filtered by source_segments.row_id → compare definitions
```

Example: row 285 → `学习`, `研究`, `现实理论化`, `可行性`.

## 3. “Where is a doctrine located in the matrix?”

Path:

```text
目录索引_结构化.csv → position card coordinate → segment card → W3 terms
```

Example: `静止的事件主义` → `3-4-2-2.md` → row 263 terms.

Optional CLI:

```bash
python3 knowledge/scripts/query_position.py 3-4-2
python3 knowledge/scripts/query_position.py 后结构主义
```

## 4. “How does one mechanism move into another?”

Path:

```text
relation-assets.jsonl → relation_type → source/target senses → evidence_segment
```

Example: objectification/subjectivization routes → W5 `objectifies` / `subjectivizes` records.

Optional CLI:

```bash
python3 knowledge/scripts/query_relation.py --type objectifies
python3 knowledge/scripts/query_relation.py --relation-id rel:w5b1:001
```

## 5. “What is the difference between two similar terms?”

Path:

```text
term-senses for both terms → forbidden_mix fields → ambiguous-terms.md → evidence rows
```

Example: `星丛` vs `星座`; `site` vs `position`; `数学化` vs `数学知识`.

## 6. “Can I use a synthesis directly?”

Path:

```text
synthesis claim → source tag → W3/W4/W5 record → clean row
```

Rule: synthesis is a map, not a source of independent claims.

## 7. “Is this relation too strong?”

Path:

```text
relation record → applicability_boundary → forbidden_interpretation → W6 evidence-claim-audit.md
```

Rule: do not generalize a relation beyond its row and position boundary.

## 8. “Is this term safe to use in a new synthesis?”

Path:

```text
term-senses → ambiguous-terms.md → concept-drift-report.md → source row
```

Rule: if the term has multiple senses, cite the exact sense ID.

## 9. “How do I answer a field overview question?”

Path:

```text
part-N synthesis → field position card → representative W3 terms → W5 relations
```

Example: field 4 overview → `part-4-praxis.md` → `4.md` → row 285 terms.

## 10. “How do I trace an evidence quote?”

Path:

```text
sense_id or relation_id → evidence row → segments.jsonl clean_md_path → exact substring check
```

Use `validate_w3_term_senses.py` or `validate_w5_relation_assets.py` when possible.

Optional CLI:

```bash
python3 knowledge/scripts/trace_evidence.py term:主体:s01
python3 knowledge/scripts/trace_evidence.py rel:w5b1:001
python3 knowledge/scripts/trace_evidence.py 276
```

## 11. “How do I add a new term sense?”

Path:

```text
candidate term → exact source row quotes → source_segments metadata → draft JSONL record → batch validation → audit note
```

Minimum: 2 exact quotes, valid axis, `forbidden_mix`, status `draft`.

## 12. “How do I resume the project?”

Path:

```text
ISMISM-MAINLINE-HANDOFF.md → knowledge/STATE.md → knowledge/DIGESTION_PROGRAM.md → latest operation-log entry
```

Then run W3/W4/W5 validators before editing.

## 13. “How do I query the AI / VR / 智能 theme?”

Path:

```text
knowledge/themes/ai/ai-row-manifest.jsonl
→ knowledge/themes/ai/ai-evidence-bank.jsonl
→ AI W3 senses / AI W5 relations / W10 AI cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_ai_theme.py AI身体化
python3 knowledge/scripts/query_ai_theme.py 强AI
python3 knowledge/scripts/query_ai_theme.py AI可朽性
python3 knowledge/scripts/query_ai_theme.py --row 360
```

Rule: the AI theme layer is a maximum-absorption index/synthesis surface, not a canonical source above corpus evidence. Treat W3/W5 AI additions as `draft` and W10 AI cards as `pilot-draft`.

## 14. “How do I query the Chinese Philosophy theme?”

Path:

```text
knowledge/themes/chinese-philosophy/chinese-philosophy-row-manifest.jsonl
→ knowledge/themes/chinese-philosophy/chinese-philosophy-evidence-bank.jsonl
→ Chinese W3 senses / Chinese W5 relations / W10 cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_chinese_philosophy_theme.py 实践论 --limit 3
python3 knowledge/scripts/query_chinese_philosophy_theme.py --row 131
python3 knowledge/scripts/query_chinese_philosophy_theme.py --class buddhist-chan-bridge
```

Rule: the Chinese Philosophy theme layer is a maximum-absorption index/synthesis surface, not a neutral encyclopedia or a source above corpus evidence. W3/W5 records remain `draft`; W10 remains `pilot-draft`.

## 15. “How do I query the Religion Problem / 宗教问题 theme?”

Path:

```text
knowledge/themes/religion/religion-row-manifest.jsonl
→ knowledge/themes/religion/religion-evidence-bank.jsonl
→ Religion W3 senses / Religion W5 relations / W10 Religion cards
→ split_md_clean exact quote
```

Examples:

```bash
python3 knowledge/scripts/query_religion_theme.py 宗教 --limit 3
python3 knowledge/scripts/query_religion_theme.py 偶像 --limit 3
python3 knowledge/scripts/query_religion_theme.py --row 45
python3 knowledge/scripts/query_religion_theme.py --class buddhist-liberation-bridge
```

Rule: the Religion Problem layer is a maximum-absorption index/synthesis surface, not a neutral religious-studies encyclopedia or a source above corpus evidence. W3/W5 records remain `draft`; W10 remains `pilot-draft`.
