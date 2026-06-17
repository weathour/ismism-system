# Class / Youth / Generation / Mobility Anxiety Maximum Absorption Handoff

- date: 2026-06-16 CST
- status: complete as draft/pilot-draft maximum absorption layer
- theme root: `knowledge/themes/class-youth-generational-anxiety/`

## Resume first

1. `knowledge/themes/class-youth-generational-anxiety/README.md`
2. `knowledge/themes/class-youth-generational-anxiety/class-youth-generational-anxiety-synthesis.md`
3. `knowledge/themes/class-youth-generational-anxiety/mobility-anxiety-class-solidification-synthesis.md`
4. `knowledge/themes/class-youth-generational-anxiety/youth-success-bottom-humiliation-synthesis.md`
5. `knowledge/themes/class-youth-generational-anxiety/class-youth-generational-anxiety-row-manifest.jsonl`
6. `knowledge/themes/class-youth-generational-anxiety/class-youth-generational-anxiety-evidence-bank.jsonl`
7. `knowledge/scripts/validate_class_youth_generational_anxiety_theme.py`
8. `knowledge/scripts/query_class_youth_generational_anxiety_theme.py`

## Completed assets

- Manifest: 120 reviewed rows (91 core / 8 bridge / 21 excluded).
- Evidence bank: 310 exact-normalizable quote records.
- W3: 45 draft senses in `W3-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16`.
- W5: 40 draft relations in `W5-CLASS-YOUTH-GENERATIONAL-ANXIETY-2026-06-16`, covering all 12 relation types.
- W10: 30 Class-youth pilot-draft cards.
- Syntheses: main synthesis plus mobility/class-solidification and youth/success/bottom-humiliation sub-syntheses.
- Query helper and final validator added.

## Validation

```bash
python3 knowledge/scripts/validate_class_youth_generational_anxiety_theme.py --repo . --final
python3 knowledge/scripts/query_class_youth_generational_anxiety_theme.py 阶层 --limit 3
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 924 --require-type-min 2
```

## Boundaries

- Do not edit `split_md/` or `split_md_clean/`.
- W3/W5 remain `draft`.
- W10 remains `pilot-draft`.
- `上升通道`, `阶层固化`, `中产焦虑`, `底层羞辱`, `成功学`, and `青年虚无` are diagnostic labels, not unsupported current-events claims.
- external material remains auxiliary/candidate-only.
