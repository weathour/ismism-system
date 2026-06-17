# AGENTS.md

This repository is a standalone ISMISM knowledge-processing project. Work from the current corpus and `knowledge/` contract only.

## Operating priorities

1. Preserve corpus integrity.
2. Preserve row, segment, clean-path, and quote traceability.
3. Preserve the hierarchy and method spine.
4. Extend `knowledge/` in small auditable batches.
5. Verify before claiming completion.

## Truth-source order

1. `目录索引_结构化.csv`
2. `split_md/`
3. `split_md_clean/`
4. `knowledge/manifests/*`
5. `knowledge/segment-cards/*`
6. `knowledge/lexicon/*`
7. `knowledge/position-cards/*`
8. `knowledge/relations/*`
9. `knowledge/w10-absorption/*`
10. `knowledge/themes/*`
11. `knowledge/syntheses/*`
12. `knowledge/qa/*`

## Safe editing rules

- Do not overwrite `split_md/`.
- Do not edit `split_md_clean/` unless the task explicitly targets text cleaning.
- Keep W3 term senses and W5 relation assets in `draft` unless a separate review process promotes them.
- Keep W10 close-reading cards in `pilot-draft`.
- Add no dependency or generated cache to the repository unless the user explicitly asks and the artifact is required by the project contract.

## Current project markers

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Mainline files

1. `PROJECT-SPEC.md`
2. `README.md`
3. `ISMISM-MAINLINE-HANDOFF.md`
4. `knowledge/STATE.md`
5. `knowledge/DIGESTION_PROGRAM.md`
6. `DIRECTORY_MAP.md`
7. `knowledge/references/social-phenomena-diagnostic-protocol.md`
8. `knowledge/w10-absorption/PLAN.md`
9. `knowledge/w10-absorption/index.md`
10. `skills/ismism-knowledge-operator/SKILL.md`

## Active theme surfaces

- `knowledge/themes/aesthetics-media/README.md` — Aesthetics / Art / Media / Image / Narrative.
- `knowledge/themes/ai/README.md` — AI.
- `knowledge/themes/capitalism/README.md` — Capitalism / Political Economy maximum absorption layer.
- `knowledge/themes/chinese-philosophy/README.md` — Chinese Philosophy.
- `knowledge/themes/class-youth-generational-anxiety/README.md` — Class / Youth / Generation / Mobility Anxiety.
- `knowledge/themes/consumption-desire-lifestyle/README.md` — Consumption / Desire / Commodity / Lifestyle.
- `knowledge/themes/education-examination-credentialism/README.md` — Education / Examination / Credentialism.
- `knowledge/themes/family-intimacy-reproduction/README.md` — Family / Intimacy / Marriage / Birth.
- `knowledge/themes/feminism/README.md` — Feminism / Gender / Sexuality.
- `knowledge/themes/governance-law-bureaucracy/README.md` — Governance / Law / Bureaucracy / Order.
- `knowledge/themes/health-body-risk-society/README.md` — Health / Body / Medicine / Risk Society.
- `knowledge/themes/labor-workplace-precarity/README.md` — Labor / Workplace / Precarity.
- `knowledge/themes/media-platform-public-opinion/README.md` — Media / Platform / Public Opinion / Traffic Society.
- `knowledge/themes/psychoanalysis-subjectivity/README.md` — Psychoanalysis / Subjectivity.
- `knowledge/themes/psychological-distress-social-symptom/README.md` — Psychological Distress / Anxiety / Addiction / Social Symptom.
- `knowledge/themes/religion/README.md` — Religion Problem.
- `knowledge/themes/time-death-finitude-life/README.md` — Time-Death-Finitude-Life maximum absorption layer; 时间 / 死亡 / 有限性 / 生命.
- `knowledge/themes/urban-housing-migration-space/README.md` — Urban / Housing / Migration / Space.

## Verification commands

```bash
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
