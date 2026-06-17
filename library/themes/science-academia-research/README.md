# Science / Academia / Research / Knowledge Production

- status: validated theme layer with manifest, evidence bank, taxonomy, draft concept/relation coverage, close-reading coverage, syntheses, query helper, and social-route integration.
- Chinese name: 科学话语—学术共同体—科研主体化
- provenance: corpus-backed curation; external material, if any, is candidate-only and cannot ground claims.
- validator: `python3 tools/validate/themes/science_academia_research.py --repo .`

## Scope

This theme organizes corpus-backed evidence about scientific discourse, academic community, research evaluation, expert/STEM subjectivation, scientism/naturalism/positivism, and critical counter-academic practice. It is not a generic STEM guide and does not make current real-world university or policy claims.

## Boundary against Education

`education-examination-credentialism` owns schooling, exams, credentials, classroom discipline, and student sorting. Shared rows appear here only when their science-academia function is distinct: knowledge legitimacy, scientific/academic institutionality, research evaluation, or scientific ideology. Every manifest row carries `overlap_status`, `education_theme_class`, `science_claim_function`, and `evidence_reuse_policy`.

## Validated foundation counts

- manifest rows: 79
- evidence records: 225
- usable core/bridge rows: 78
- core status counts: {'core': 58, 'bridge': 20, 'context': 1}
- overlap counts: {'science-core-distinct-function': 38, 'not-in-education': 33, 'education-core-science-bridge': 8}
- taxonomy class counts: {'research-evaluation-paper-metrics': 6, 'scientific-discourse-reality-definition': 18, 'expert-stem-subjectivation': 12, 'scientific-knowledge-sociology-paradigm': 3, 'academic-institution-community': 5, 'scientism-naturalism-positivism': 26, 'academic-practice-critical-counter-community': 4, 'technology-industry-science-bridge': 5}

## Files

- `science-academia-research-row-manifest.jsonl`
- `science-academia-research-evidence-bank.jsonl`
- `science-academia-research-taxonomy.md`
- `science-academia-research-go-no-go.md`

## Query examples

```bash
python3 tools/query/themes/science_academia_research.py 科学主义 --limit 3
python3 tools/query/themes/science_academia_research.py 科研评价 --limit 3
python3 tools/query/themes/science_academia_research.py 学术共同体 --limit 3
python3 tools/query/themes/science_academia_research.py 科学话语 --limit 3
python3 tools/query/themes/science_academia_research.py 专家权威 --limit 3
python3 tools/query/themes/science_academia_research.py 论文指标 --limit 3
```

## Synthesis files

- `scientific-discourse-knowledge-legitimacy-synthesis.md`
- `academic-community-research-subjectivation-synthesis.md`
- `positivism-naturalism-scientism-ideology-synthesis.md`
- `critical-academic-counter-community-synthesis.md`
