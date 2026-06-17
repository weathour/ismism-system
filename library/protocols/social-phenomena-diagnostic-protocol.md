# Social Phenomena Diagnostic Protocol

- 中文名：现实社会现象诊断协议
- status: shared method protocol for the Social Phenomena / Everyday Life Problems Theme Package Social Topics Router
- created: 2026-06-16 CST
- scope: use ISMISM corpus evidence to absorb and diagnose concrete social phenomena without turning the repository into current-events commentary.
- applies to: labor/workplace, education/examination, family/intimacy, consumption/desire, media/platform, governance/law, class/youth, psychological distress, urban/housing, health/body themes.

## 0. Purpose

This protocol defines the common method for the next theme package social topics router: **现实社会现象与问题主题证据超阶段**.

The objective is not to add generic sociology, journalism, policy commentary, or external news analysis. The objective is to make the existing ISMISM knowledge layer able to diagnose everyday social phenomena through row/segment/quote-traceable concepts, relations, close readings, and syntheses.

A valid social-phenomenon absorption answers:

1. What concrete phenomenon is being diagnosed?
2. What subject-position does it produce or presuppose?
3. What social mechanism reproduces it?
4. What fantasy, misrecognition, ideology, or symbolic form stabilizes it?
5. What institution, medium, economic relation, family form, spatial form, or bodily regime carries it?
6. What contradiction does the phenomenon expose?
7. What practical opening, refusal, transformation, or diagnostic use follows from the evidence?

## 1. Truth-source discipline

Use repository truth sources in the established priority order:

1. `corpus/registry/toc.csv`
2. `corpus/raw-markdown/` and `corpus/clean-markdown/`
3. `library/manifests/*`
4. `library/segments/*`
5. `library/concepts/*`
6. `library/positions/*`
7. `library/relations/*`
8. `library/audits/*`
9. `library/syntheses/*`
10. `library/close-reading/*`
11. `library/protocols/*` protocols

Hard boundaries:

- Do not edit `corpus/raw-markdown/`.
- Do not edit `corpus/clean-markdown/` unless an explicit text-cleaning task authorizes it.
- Do not restore discarded product prototype/product surfaces.
- Do not use external material as final truth.
- Do not promote concept/relation out of `draft`.
- Do not promote close-reading out of `pilot-draft`.

## 2. Theme directory contract

Each social-phenomenon theme should live under:

```text
library/themes/<theme-slug>/
```

Minimum files:

| File | Function |
|---|---|
| `README.md` | Theme scope, counts, query examples, interpretation rules. |
| `<theme>-row-manifest.jsonl` | Reviewed row list with row id, toc id, path, role, class, and rationale. |
| `<theme>-evidence-bank.jsonl` | Exact clean-text quote records. |
| `<theme>-taxonomy.md` | Controlled classes and row ownership map. |
| `<theme>-concept-relation-batch-notes.md` | concept/relation batch ids, relation boundaries, duplicate-control notes. |
| `<theme>-...-synthesis.md` | Evidence-marker syntheses. |

Companion scripts:

| Script | Function |
|---|---|
| `tools/internal/validate_<theme>_theme.py` | Final validator for manifest/evidence/concept/relation/close-reading/docs markers. |
| `tools/internal/query_<theme>_theme.py` | Query helper for keywords, rows, classes, and evidence ids. |

## 3. Row selection protocol

A row can enter a social-phenomenon manifest only if at least one of the following is true:

1. It directly names or analyzes the phenomenon, for example 劳动, 考试, 婚姻, 消费, 媒介, 法律, 阶级, 焦虑, 城市, 身体.
2. It supplies a mechanism necessary to diagnose the phenomenon, for example 主体化, 客体化, 拜物, 大他者, 符号秩序, 社会再生产, 权力关系.
3. It supplies an institutional, spatial, familial, bodily, technological, or economic carrier of the phenomenon.
4. It provides a strong bridge from an existing maximum-absorption layer, such as Capitalism, Psychoanalysis-Subjectivity, Feminism, Aesthetics-Media, Time-Death, Religion, Chinese Philosophy, or AI.

Manifest row roles:

| role | Meaning |
|---|---|
| `core` | The row directly analyzes the social phenomenon or its main mechanism. |
| `bridge` | The row links the theme to another established theme or matrix movement. |
| `context` | The row provides necessary background or contrast but should not carry major claims alone. |
| `excluded` | Keyword hit or tempting row explicitly rejected; kept to document boundary discipline. |

Rules:

- Do not include every keyword hit.
- Prefer rows with exact quotes that contain an interpretable mechanism, not only a term occurrence.
- For high-density themes such as governance/law/order, choose functionally relevant rows, not all state/order/law mentions.
- Keep excluded rows when they prevent future false positives.

## 4. Evidence bank protocol

Every evidence record must include enough information to recover the quote:

- evidence id with theme prefix,
- row id,
- toc id when available,
- clean source path,
- quote text,
- quote role or diagnostic function,
- theme class.

The quote must be an exact substring of the declared `corpus/clean-markdown/` file after the validator's established whitespace normalization.

Evidence roles should be diagnostic, not merely topical. Suggested roles:

| evidence role | Use |
|---|---|
| `phenomenon-name` | Names the concrete social phenomenon. |
| `subject-position` | Shows the subject-position produced by the phenomenon. |
| `mechanism` | Shows the social, symbolic, economic, institutional, or psychic mechanism. |
| `fantasy-misrecognition` | Shows the illusion, fantasy, fetish, ideology, or misrecognition stabilizing it. |
| `institution-carrier` | Shows school, work, family, law, platform, city, medicine, market, etc. as carrier. |
| `contradiction` | Shows conflict, failure, impossibility, suffering, blockage, or symptomatic tension. |
| `practice-opening` | Shows possible refusal, transformation, practice, reorganization, or diagnostic use. |
| `cross-theme-bridge` | Links to an existing maximum-absorption layer. |
| `boundary-exclusion` | Explains why a tempting keyword hit is not a core theme row. |

## 5. Diagnostic grammar

Every synthesis and close-reading card should prefer the following grammar:

```text
Phenomenon → Subject-position → Mechanism → Fantasy/misrecognition → Carrier → Contradiction → Practical opening
```

### 5.1 Phenomenon

The phenomenon must be named concretely enough that a future query can hit it: 内卷, 考公热, 婚恋市场, 打工人, 短视频成瘾, 住房焦虑, 医疗焦虑, 青年虚无, etc.

### 5.2 Subject-position

Ask: what kind of subject does this phenomenon require or produce?

Examples:

- self-optimizing worker,
- credential-seeking student,
- marriage-market participant,
- consumer of identity,
- platform-visible performer,
- institution-facing petitioner,
- anxious youth,
- pathologized patient,
- urban renter/migrant.

### 5.3 Social mechanism

Ask: by what mechanism is the phenomenon reproduced?

Possible mechanism families:

- capital accumulation and production relation,
- social reproduction,
- credential sorting,
- symbolic order and big Other,
- commodity fetishism,
- platform attention capture,
- bureaucratic procedure,
- class distinction,
- medicalization,
- spatial exclusion,
- time/death/finitude pressure.

### 5.4 Fantasy / misrecognition / ideology

Ask: what false immediacy lets the phenomenon appear natural, personal, deserved, inevitable, or enjoyable?

Examples:

- effort mythology,
- meritocracy,
- romance destiny,
- consumer identity,
- platform visibility as existence,
- rule as justice,
- health as moral success,
- city success narrative,
- success/failure individualization.

### 5.5 Carrier

Ask: where is the mechanism materially or symbolically carried?

Carrier types:

- workplace,
- school/exam system,
- family/marriage market,
- commodity/market,
- platform/media,
- legal-bureaucratic procedure,
- class/generation relation,
- clinic/health regime,
- housing/city/space,
- body/affect/time.

### 5.6 Contradiction

Ask: where does the phenomenon fail, hurt, contradict itself, produce symptoms, or require repression?

### 5.7 Practical opening

A practical opening is not a slogan. It must be grounded in evidence and can be modest:

- naming the mechanism,
- refusing a false alternative,
- tracing a fantasy to its carrier,
- separating personal suffering from privatized blame,
- finding a collective or structural dimension,
- locating an institutional contradiction,
- preserving a row/quote path for scholar-in-the-loop refinement.

## 6. concept term-sense protocol

concept additions for social-phenomenon themes must remain `draft`.

Add a new concept sense only when one of these is true:

1. The term is new to the lexicon.
2. Existing term senses do not capture the social-phenomenon function.
3. The theme needs a narrower operational sense for diagnosis, for example `内卷`, `学历崇拜`, `平台可见性`, `住房焦虑`.
4. A cross-theme term needs a function-specific social diagnosis variant, for example `商品拜物` in consumption, `社会再生产` in family, `症状` in psychological distress.

Duplicate-control rules:

- Search existing `library/concepts/term-senses.jsonl` before appending.
- Prefer extending with a precise new sense over creating near-synonym terms.
- Each sense must include evidence quotes recoverable from declared source rows.
- Batch ids should be theme-specific and date-stamped, for example `concept-LABOR-WORKPLACE-PRECARITY-2026-06-16` or execution date.

## 7. relation relation protocol

relation additions must remain `draft` and use existing relation type discipline.

A relation is valid only if it connects evidence-backed terms, claims, mechanisms, rows, or positions. It should explain movement, mediation, blockage, misrecognition, objectification, subjectivation, transition, boundary, route, or tension.

Strong social-phenomenon relation patterns:

| Pattern | Example function |
|---|---|
| phenomenon `mediates-between` subject-position and institution | Exam mediates student subject and credential order. |
| fantasy `misrecognizes-as` natural fact | Meritocracy misrecognizes class sorting as personal ability. |
| platform `overcodes` public affect | Traffic logic overcodes attention as social truth. |
| labor regime `subjectivizes` worker | Performance discipline subjectivizes self-exploitation. |
| commodity `objectifies` desire | Lifestyle goods objectify identity desire. |
| law/procedure `blocks-transition` practice | Bureaucratic form blocks lived contradiction from becoming transformation. |
| family form `reproduces` social relation | Family and birth pressure reproduce gender/class obligations; use available relation type closest to this if no explicit reproduces type exists. |

If no existing relation relation type fits, do not invent a type casually. Use the nearest existing relation type and explain the choice in batch notes.

## 8. close-reading close-reading protocol

close-reading additions remain `pilot-draft`.

A social-phenomenon close-reading card should do one of three things:

| card type | Social-phenomenon use |
|---|---|
| argument card | reconstructs an argument diagnosing a social mechanism. |
| process card | tracks how a phenomenon is produced or transformed. |
| case card | analyzes a concrete case, figure, metaphor, or everyday scene. |

Each close-reading card should include the diagnostic grammar where possible and cite exact row evidence. Avoid writing cards that merely summarize a row without social diagnostic function.

## 9. Synthesis protocol

Theme syntheses should be evidence-marker documents, not essays detached from the corpus.

Each synthesis should include:

1. scope and boundary,
2. main diagnostic claims,
3. evidence-marker references,
4. concept/relation/close-reading links,
5. cross-theme bridges,
6. excluded or weak areas,
7. query routes.

Required cross-theme bridge discipline:

- Labor must bridge to Capitalism and Time-Death only when work/time/finitude evidence supports it.
- Education must bridge to subject formation, knowledge, and governance only with evidence.
- Family must bridge to Feminism and Social Reproduction with evidence.
- Consumption must bridge to Capitalism, Psychoanalysis, and Aesthetics-Media with evidence.
- Media-platform must bridge to Aesthetics-Media and Psychoanalysis with evidence.
- Governance-law must bridge to symbolic order and institutional practice with evidence.
- Class-youth must bridge to labor, education, family, and consumption with evidence.
- Psychological distress must bridge to Psychoanalysis but avoid reducing all distress to private psychology.
- Urban-housing must bridge to space, class, governance, and desire with evidence.
- Health-body must bridge to body, death, governance, risk, and care with evidence.

## 10. Query helper protocol

Each query helper should support at least:

- keyword query,
- row query,
- class query,
- evidence display,
- limit parameter.

Theme README query examples should include both Chinese phenomenon keywords and class/row examples.

The final social topics router query layer should test at least 30 prompts, including:

```text
内卷, 打工人, 加班, 绩效, 失业焦虑, 考公热, 考研, 学历崇拜, 鸡娃, 专家崇拜,
婚恋市场, 彩礼, 生育焦虑, 父母控制, 消费主义, 情绪消费, 奢侈品, 短视频成瘾,
直播, 热搜舆论, 网红, 官僚手续, 法律意识, 中产焦虑, 青年虚无, 躺平,
抑郁焦虑, 住房焦虑, 城市漂泊, 医疗焦虑
```

## 11. Validator protocol

Each theme validator should check at minimum:

1. manifest exists and has no duplicate row ids unless explicitly allowed by class design,
2. evidence bank exists and all quotes recover from declared clean files,
3. theme classes are controlled,
4. concept batch exists and all records are `draft`,
5. relation batch exists and all records are `draft`,
6. close-reading theme cards exist and remain `pilot-draft`,
7. README, synthesis, status note, query helper, and navigation markers are present,
8. global current counts and relation min-count are not stale,
9. protected corpus directories have no diff.

Social Topics Router final validator should additionally check:

- all ten theme folders exist,
- all ten theme validators pass or are invokable,
- social diagnosis protocol is referenced by every social theme README,
- final query smoke tests cover at least 30 concrete prompts,
- existing maximum-absorption theme validators still pass,
- concept/relation/close-reading/master validators pass.

## 12. Theme-specific scope notes

### 12.1 Labor / Workplace / Precarity / Involution

Core functions: work discipline, performance, alienation, self-exploitation, platform/precarious labor, career anxiety, unemployment, production relation.

Avoid: treating every `生产` mention as workplace evidence.

### 12.2 Education / Examination / Credentialism / Knowledge Discipline

Core functions: exam society, credential sorting, expert authority, school discipline, academic hierarchy, knowledge commodity or knowledge as class filter.

Avoid: treating every `知识` or `理论` mention as education evidence.

### 12.3 Family / Intimacy / Marriage / Birth / Social Reproduction

Core functions: marriage market, romance ideology, parental obligation, birth pressure, gendered household labor, family as social reproduction mechanism.

Avoid: reducing all intimacy to feminism unless the evidence supports the gender/social-reproduction function.

### 12.4 Consumption / Desire / Commodity / Lifestyle

Core functions: commodity fetishism, identity consumption, emotional consumption, lifestyle display, market enjoyment, self-branding.

Avoid: treating all desire as consumption; preserve psychoanalytic distinction where relevant.

### 12.5 Media / Platform / Public Opinion / Traffic Society

Core functions: attention capture, platform visibility, public affect, hot search logic, short video/livestream scenes, network cynicism, image-mediated social truth.

Avoid: treating all image/cinema material as platform society; use Aesthetics-Media bridge only when the public/platform function is present.

### 12.6 Governance / Law / Bureaucracy / Order

Core functions: legal consciousness, bureaucratic procedure, rule fetishism, administrative order, risk management, institutional helplessness, obedience structure.

Avoid: absorbing every state/law/order mention; this theme must focus on everyday institutional experience and social order mechanisms.

### 12.7 Class / Youth / Generation / Mobility Anxiety

Core functions: class position, blocked mobility, youth disillusionment, middle-class anxiety, bottom-layer shame, success mythology, intergenerational pressure.

Avoid: classifying every `人民` or `大众` hit as class-youth.

### 12.8 Psychological Distress / Anxiety / Addiction / Social Symptom

Core functions: anxiety, depression, burnout, nihilism, addiction, therapeutic industry, privatization of social contradiction into personal failure.

Avoid: psychologizing social contradiction; link symptom to mechanism.

### 12.9 Urban / Housing / Migration / Space

Core functions: rent, housing price, city drift, urban-rural split, hukou when present, public space, spatial class division, migration.

Avoid: treating every spatial metaphor as urban/housing evidence.

### 12.10 Health / Body / Medicine / Risk Society

Core functions: illness anxiety, medicalization, health moralism, body governance, epidemic memory when present, disease stigma, risk consciousness, care and finitude.

Avoid: treating every body/death mention as health/medicine; preserve Time-Death boundary.

## 13. Completion standard for the social topics router

The social topics router is complete when a future user can ask a concrete social question and the repository can return a traceable answer with:

- relevant rows,
- exact quotes,
- concept draft concepts,
- relation draft relations,
- close-reading pilot-draft close readings,
- one or more theme syntheses,
- one or more cross-theme routes,
- and a clear boundary between evidence and inference.

The final state must pass all theme validators, global concept/relation/close-reading validators, foundation validators, existing theme validators, master validator, query smoke tests, `git diff --check`, and protected corpus diff check.
