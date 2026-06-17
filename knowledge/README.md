# Knowledge Layer

Current latest checkpoint — Health / Body / Medicine / Risk Society maximum absorption.
Current global counts are 1676 W3 senses / 1228 terms; 6/363 rows remain W1/W2-only; 277 rows now have W3+W5+W10 overlap.

Global current counts: 1676 W3 draft senses / 1228 terms; 1044 W5 draft relations; 741 W10 pilot-draft cards.
Current validator markers: 1676 senses / 1228 terms; 1044 relations / 12 types; 741 cards / 3 card types; 277 rows now have W3+W5+W10 overlap; W5 validator uses `--min-count 1044`.

## Folders

- `manifests/` — W1 corpus manifest, segments, chunks, and anomaly report.
- `segment-cards/` — W2 row-level cards.
- `lexicon/` — W3 draft term senses and term indexes.
- `position-cards/` — W4 matrix position cards.
- `relations/` — W5 relation assets.
- `w10-absorption/` — W10 pilot-draft close-reading cards.
- `themes/` — maximum-absorption theme layers.
- `syntheses/` — cross-row and cross-theme syntheses.
- `qa/` — validation, audit, review, and absorption evidence.
- `scripts/` — validators, query helpers, and build tools.
- `references/` — protocols and stable method references.
- `templates/` — generation templates.

## Theme surfaces

- `themes/aesthetics-media/README.md` — Aesthetics / Art / Media.
- `themes/ai/README.md` — AI.
- `themes/capitalism/README.md` — Capitalism / Political Economy.
- `themes/chinese-philosophy/README.md` — Chinese Philosophy.
- `themes/class-youth-generational-anxiety/README.md` — Class / Youth / Generation / Mobility Anxiety.
- `themes/consumption-desire-lifestyle/README.md` — Consumption / Desire / Commodity / Lifestyle.
- `themes/education-examination-credentialism/README.md` — Education / Examination / Credentialism.
- `themes/family-intimacy-reproduction/README.md` — Family / Intimacy / Marriage / Birth.
- `themes/feminism/README.md` — Feminism / Gender / Sexuality.
- `themes/governance-law-bureaucracy/README.md` — Governance / Law / Bureaucracy / Order.
- `themes/health-body-risk-society/README.md` — Health / Body / Medicine / Risk Society.
- `themes/labor-workplace-precarity/README.md` — Labor / Workplace / Precarity.
- `themes/media-platform-public-opinion/README.md` — Media / Platform / Public Opinion / Traffic Society.
- `themes/psychoanalysis-subjectivity/README.md` — Psychoanalysis / Subjectivity.
- `themes/psychological-distress-social-symptom/README.md` — Psychological Distress / Anxiety / Addiction / Social Symptom.
- `themes/religion/README.md` — Religion Problem.
- `themes/time-death-finitude-life/README.md` — Time-Death-Finitude-Life.
- `themes/urban-housing-migration-space/README.md` — Urban / Housing / Migration / Space.

## Validators

```bash
python3 knowledge/scripts/validate_w1_manifests.py
python3 knowledge/scripts/validate_w3_term_senses.py --repo .
python3 knowledge/scripts/validate_w4_position_cards.py
python3 knowledge/scripts/validate_w5_relation_assets.py --repo . --min-count 1044 --require-type-min 2
python3 knowledge/scripts/validate_w10_absorption.py --repo .
python3 knowledge/scripts/validate_knowledge_contract.py --repo .
python3 knowledge/scripts/validate_social_phenomena_superphase.py --repo . --final
```
