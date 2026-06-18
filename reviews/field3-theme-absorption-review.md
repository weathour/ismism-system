# Field 3 Theme Absorption Review Evidence

- status: G001 preflight complete
- date: 2026-06-18
- source spec: Autopilot deep-interview Field 3 scope artifact
- approved plan: Autopilot Ralplan Field 3 PRD artifact
- test spec: Autopilot Ralplan Field 3 test-spec artifact
- protocol: skills/ismism-knowledge-operator/references/theme-absorption-protocol.md

## Baseline validation

Command: python3 tools/ismism.py validate core

    {
      "status": "PASS",
      "toc_rows": 363,
      "segments": 363,
      "available_segments": 363,
      "missing_segments": 0,
      "chunks": 1594,
      "segments_with_chunks": 363,
      "missing_segment": null,
      "pdf_slices_dir_exists": false,
      "pdf_slices_file_count": 0,
      "segment_card_files_present": 364
    }
    concept validation: records=1685, terms=1237, quotes=3443, errors=0, warnings=0
    {'status': 'PASS', 'level': 1, 'count': 4, 'cards': [{'path': 'library/positions/1.md', 'length': 873}, {'path': 'library/positions/2.md', 'length': 915}, {'path': 'library/positions/3.md', 'length': 951}, {'path': 'library/positions/4.md', 'length': 947}]}
    relation validation: records=1054, quotes=1091, types=12/12, errors=0, warnings=0
    type_counts={"blocks-transition": 81, "boundary-between": 80, "evidences-claim": 93, "mediates-between": 131, "misrecognizes-as": 71, "objectifies": 81, "overcodes": 74, "represents-position": 74, "route-from-to": 98, "subjectivizes": 69, "tension-between": 92, "transitions-to": 110}
    validate_close_reading: PASS
    {"status": "PASS", "cards": 741, "type_counts": {"close-reading-argument": 287, "close-reading-process": 267, "close-reading-case": 187}, "errors": 0}
    ISMISM product contract validation: status=PASS, dirs=27/27, files=35/35, segments=363, chunks=1594, concepts=1685, relations=1054, close_reading=741, themes=19, residue=0, bytes=731, errors=0
    validate_social_topics: PASS themes=11 rows=1188 evidence=3076 failures=0
    - labor-workplace-precarity: PASS rows=98 evidence=247 quotes=247 errors=0
    - education-examination-credentialism: PASS rows=109 evidence=281 quotes=281 errors=0
    - science-academia-research: PASS rows=79 evidence=225 quotes=225 errors=0
    - family-intimacy-reproduction: PASS rows=86 evidence=240 quotes=240 errors=0
    - consumption-desire-lifestyle: PASS rows=93 evidence=223 quotes=223 errors=0
    - media-platform-public-opinion: PASS rows=119 evidence=267 quotes=267 errors=0
    - governance-law-bureaucracy: PASS rows=124 evidence=307 quotes=307 errors=0
    - class-youth-generational-anxiety: PASS rows=120 evidence=310 quotes=310 errors=0
    - psychological-distress-social-symptom: PASS rows=120 evidence=340 quotes=340 errors=0

## Donor pattern inspection

Inspected donor theme files and tool surfaces:

- library/themes/psychoanalysis-subjectivity/README.md
- library/themes/psychoanalysis-subjectivity/psychoanalysis-subjectivity-row-manifest.jsonl
- library/themes/psychoanalysis-subjectivity/psychoanalysis-subjectivity-evidence-bank.jsonl
- tools/internal/query_psychoanalysis_subjectivity_theme.py
- tools/query/themes/psychoanalysis_subjectivity.py
- tools/validate/themes/psychoanalysis_subjectivity.py
- library/themes/aesthetics-media/README.md
- library/themes/aesthetics-media/aesthetics-media-row-manifest.jsonl
- library/themes/aesthetics-media/aesthetics-media-evidence-bank.jsonl
- tools/internal/query_aesthetics_media_theme.py
- tools/query/themes/aesthetics_media.py
- tools/validate/themes/aesthetics_media.py
- tools/lib/theme_validation.py

Donor validator smokes:
    validate_theme[psychoanalysis-subjectivity]: PASS manifest=120 evidence=387 quotes=387 syntheses=5 errors=0
    validate_theme[aesthetics-media]: PASS manifest=69 evidence=192 quotes=192 syntheses=2 errors=0

Adopted pattern: theme directory with README, row manifest, evidence bank, taxonomy, concept-relation notes, synthesis; internal query helper plus wrapper; specialized validator building on the generic exact-quote validator and adding class/status/taxonomy checks.

## Field 3 source boundary

- corpus/registry/toc.csv rows 187-275 define Field 3 / 观念论, total 89 rows.
- row 187 is the Field 3 overview context row.
- rows 188-209: 3-1 现象学.
- rows 210-231: 3-2 德国观念论.
- rows 232-253: 3-3 生存论.
- rows 254-275: 3-4 符号学.

## Per-theme scope charters

### phenomenology — 现象学

- central question: ISMISM 如何把胡塞尔及其后继的现象学拆成意向性、还原、生活世界、主体间性、身体/现世和存在论化的哲学方法问题？
- own row range: 188-209 (22 rows)
- Field 3 bridge hits outside own range: 65 rows
- context rows: 1 (row 187)
- inclusion keywords: 现象学，胡塞尔，先验，意向性，意向对象，意向行为，本质还原，先验还原，悬置，生活世界，主体间性，舍勒，梅洛，身体，感知，现世，海德格尔
- downstream diagnostic labels / theme classes: phenomenology-overview-review, transcendental-intentionality-reduction, eidetic-factual-phenomenology, lifeworld-intersubjectivity, worldly-ontological-phenomenology, phenomenology-bridge, excluded-keyword-only
- explicit exclusions and negative controls: 泛泛出现主体、经验、意识或海德格尔，但不承担现象学方法/还原/意向性/生活世界功能的行。
- bridge rules: rows outside the own range can be bridge only when quoted evidence shows the theme function; otherwise keep as excluded/noise-review or leave out of the mature package.
- social-route decision: direct-theme only in this run; do not add social-topic routing unless later QA proves a user-facing diagnostic route is needed.
- expected files: library/themes/{slug}/README.md; {slug}-row-manifest.jsonl; {slug}-evidence-bank.jsonl; {slug}-taxonomy.md; {slug}-concept-relation-notes.md; {slug}-synthesis.md; tools/internal/query_phenomenology_theme.py; tools/query/themes/phenomenology.py; tools/validate/themes/phenomenology.py
- validator command: python3 tools/validate/themes/phenomenology.py --repo . --final
- downgrade/defer decision: mature-package path approved for this run because the own section supplies 22 corpus rows and row-specific evidence is available; concept/relation/close-reading batches remain deferrable.
- top candidate rows by keyword density:
  - row 188 3-1 现象学——胡塞尔和他的事业、拥趸、敌人: 现象学×58, 先验×58, 胡塞尔×52, 意向性×29, 意向行为×18
  - row 194 3-1-1-4 准先验辩证主义——大二时期的德里达如何挽救胡塞尔先验现象学的遗产: 先验×84, 现象学×80, 胡塞尔×39, 意向性×24, 身体×14
  - row 190 3-1-1 先验现象学——胡塞尔的先验哲学计划: 先验×87, 现象学×66, 胡塞尔×53, 身体×11, 先验还原×6
  - row 207 3-1-4-2 性化的现象学——爱抚的哲学：不正经的萨特 VS 正经的胡塞尔，做那事时总要看和摸的深层机制: 身体×131, 现象学×36, 先验×16, 胡塞尔×14, 意向性×14
  - row 193 3-1-1-3 反思性的主体主义——胡塞尔现象学之枢纽，以及为什么胡塞尔的现象学不是一种庸俗的唯我论: 身体×114, 先验×35, 胡塞尔×32, 现象学×20, 意向性×18
  - row 208 3-1-4-3 存在论的现象学——最丰富的现象学：梅洛-庞蒂的格式塔-行动-身体-知觉-他者-视角-语言-世界-场-存在论现象学: 现象学×72, 梅洛×41, 身体×32, 先验×30, 胡塞尔×14
  - row 200 3-1-3 生活世界现象学——用主体间性取代主体性: 先验×36, 身体×34, 主体间性×29, 现象学×21, 胡塞尔×11
  - row 195 3-1-2 实事现象学——令现象学从哲学史走入历史，屈居二号人物的天才，舍勒: 现象学×73, 舍勒×42, 胡塞尔×15, 先验×15, 本质还原×8

### german-idealism-dialectics — 德国观念论—辩证法

- central question: ISMISM 如何把康德、费希特、谢林、黑格尔和否定辩证法组织为现代主体、自由、体系与否定运动的问题？
- own row range: 210-231 (22 rows)
- Field 3 bridge hits outside own range: 66 rows
- context rows: 1 (row 187)
- inclusion keywords: 德国观念论，观念论，康德，费希特，谢林，黑格尔，辩证法，否定辩证法，批判哲学，知识学，自由，精神，绝对，自我，实践理性
- downstream diagnostic labels / theme classes: idealism-overview-review, critical-philosophy-limits, science-of-knowledge-self-positing, system-freedom-schelling, dialectic-negativity-hegel, idealism-dialectics-bridge, excluded-keyword-only
- explicit exclusions and negative controls: 泛泛出现自由、主体、精神、否定或德国人名，但不承担观念论体系、批判哲学、知识学或辩证法功能的行。
- bridge rules: rows outside the own range can be bridge only when quoted evidence shows the theme function; otherwise keep as excluded/noise-review or leave out of the mature package.
- social-route decision: direct-theme only in this run; do not add social-topic routing unless later QA proves a user-facing diagnostic route is needed.
- expected files: library/themes/{slug}/README.md; {slug}-row-manifest.jsonl; {slug}-evidence-bank.jsonl; {slug}-taxonomy.md; {slug}-concept-relation-notes.md; {slug}-synthesis.md; tools/internal/query_german_idealism_dialectics_theme.py; tools/query/themes/german_idealism_dialectics.py; tools/validate/themes/german_idealism_dialectics.py
- validator command: python3 tools/validate/themes/german_idealism_dialectics.py --repo . --final
- downgrade/defer decision: mature-package path approved for this run because the own section supplies 22 corpus rows and row-specific evidence is available; concept/relation/close-reading batches remain deferrable.
- top candidate rows by keyword density:
  - row 218 3-2-2-1 理智直观主义——从先验主体性退回绝对整体主义，晚年费希特，怂了: 绝对×166, 自我×64, 费希特×63, 谢林×26, 黑格尔×17
  - row 211 3-2 复习课: 观念论×87, 谢林×47, 绝对×47, 费希特×29, 康德×25
  - row 240 3-3-2-1 安放了的实存主义（Positioned Existentialism）——克尔凯廓尔的三个阶段与两种辩证法: 自我×82, 自由×52, 绝对×52, 辩证法×32, 观念论×18
  - row 217 3-2-2 知识学——“我在故我在！”，辩证法、现象学和存在主义的三重先驱：费希特: 自我×66, 费希特×64, 知识学×47, 自由×20, 绝对×20
  - row 227 3-2-4 辩证法——黑格尔：走向绝对精神的历史走向: 精神×99, 绝对×69, 黑格尔×24, 辩证法×19, 自我×12
  - row 219 3-2-2-2 先验观念论——不用再读康德了，读了谢林 25 岁写的这本书，直接上手观念论和辩证法吧: 自我×56, 谢林×49, 观念论×21, 绝对×21, 辩证法×15
  - row 236 3-3-1-2 人道主义的存在主义（Humanistic Existentialism）——萨特存在主义的基本结构: 自由×66, 自我×35, 绝对×33, 辩证法×27, 黑格尔×17
  - row 222 3-2-3 体系自由主义——德国观念论的首个高峰，谢林思想的转折点：绝对者内在的不一致性: 绝对×65, 自由×57, 谢林×41, 黑格尔×9, 观念论×5

### existentialism-ethics-meaning — 生存论—伦理—意义

- central question: ISMISM 如何把生存论、存在主义、虚无、自由、选择、伦理、本真和意义问题纳入现代反观念论与主体实践的诊断？
- own row range: 232-253 (22 rows)
- Field 3 bridge hits outside own range: 66 rows
- context rows: 1 (row 187)
- inclusion keywords: 生存论，存在主义，存在，海德格尔，克尔凯郭尔，尼采，萨特，本真，虚无，意义，自由，伦理，选择，责任，死亡，生存
- downstream diagnostic labels / theme classes: existentialism-overview-review, being-existence-ism, authentic-existence-choice, identity-existential-ethics, fictional-existence-meaning, existentialism-bridge, excluded-keyword-only
- explicit exclusions and negative controls: 泛泛出现存在、自由、死亡、伦理或意义，但不承担生存论/存在主义问题结构的行。
- bridge rules: rows outside the own range can be bridge only when quoted evidence shows the theme function; otherwise keep as excluded/noise-review or leave out of the mature package.
- social-route decision: direct-theme only in this run; do not add social-topic routing unless later QA proves a user-facing diagnostic route is needed.
- expected files: library/themes/{slug}/README.md; {slug}-row-manifest.jsonl; {slug}-evidence-bank.jsonl; {slug}-taxonomy.md; {slug}-concept-relation-notes.md; {slug}-synthesis.md; tools/internal/query_existentialism_ethics_meaning_theme.py; tools/query/themes/existentialism_ethics_meaning.py; tools/validate/themes/existentialism_ethics_meaning.py
- validator command: python3 tools/validate/themes/existentialism_ethics_meaning.py --repo . --final
- downgrade/defer decision: mature-package path approved for this run because the own section supplies 22 corpus rows and row-specific evidence is available; concept/relation/close-reading batches remain deferrable.
- top candidate rows by keyword density:
  - row 236 3-3-1-2 人道主义的存在主义（Humanistic Existentialism）——萨特存在主义的基本结构: 存在×191, 自由×66, 萨特×64, 虚无×37, 存在主义×23
  - row 235 3-3-1-1 分环节的生存论的存在论（Existential Ontology of Moments）——海德格尔《存在与时间》中的领会与筹划: 存在×168, 生存×42, 海德格尔×38, 生存论×23, 本真×16
  - row 240 3-3-2-1 安放了的实存主义（Positioned Existentialism）——克尔凯廓尔的三个阶段与两种辩证法: 伦理×83, 存在×56, 自由×52, 生存×48, 意义×19
  - row 206 3-1-4-1 追问的现象学——比《存在与时间》更真诚的早期海德格尔是怎样的？: 存在×177, 海德格尔×43, 意义×22, 本真×9, 萨特×8
  - row 243 3-3-2-4 超验-生存论: 生存×115, 自由×33, 生存论×28, 存在×25, 尼采×10
  - row 246 3-3-3-2 直接生存论: 尼采×61, 虚无×43, 生存×43, 海德格尔×23, 存在×17
  - row 225 3-2-3-3 生存论的存在主义（Existential Seynism）——与晚期谢林心心相印的晚期海德格尔: 存在×112, 海德格尔×53, 虚无×15, 生存×11, 存在主义×8
  - row 238 3-3-1-4 前本体论——《从本有而来》的海德格尔《对于哲学的贡献》：不是新探索，而是成为新的世界体系构建之前的史前史: 存在×80, 海德格尔×37, 生存×33, 自由×21, 生存论×18

### semiotics-language-hermeneutics — 符号学—语言—解释学

- central question: ISMISM 如何把符号学、结构主义、后结构主义、差异辩证法与解释学组织为语言、文本、话语、意义生成与理解条件的问题？
- own row range: 254-275 (22 rows)
- Field 3 bridge hits outside own range: 66 rows
- context rows: 1 (row 187)
- inclusion keywords: 符号学，符号，结构主义，后结构主义，解释学，能指，所指，话语，文本，语言，差异，语言游戏，德里达，福柯，拉康，伽达默尔
- downstream diagnostic labels / theme classes: semiotics-overview-review, structuralist-sign-system, poststructuralist-discourse-text, dialectics-of-difference, hermeneutics-understanding, semiotics-language-bridge, excluded-keyword-only
- explicit exclusions and negative controls: 泛泛出现语言、文本、意义、差异或符号，但不承担符号系统/结构主义/解释学功能的行。
- bridge rules: rows outside the own range can be bridge only when quoted evidence shows the theme function; otherwise keep as excluded/noise-review or leave out of the mature package.
- social-route decision: direct-theme only in this run; do not add social-topic routing unless later QA proves a user-facing diagnostic route is needed.
- expected files: library/themes/{slug}/README.md; {slug}-row-manifest.jsonl; {slug}-evidence-bank.jsonl; {slug}-taxonomy.md; {slug}-concept-relation-notes.md; {slug}-synthesis.md; tools/internal/query_semiotics_language_hermeneutics_theme.py; tools/query/themes/semiotics_language_hermeneutics.py; tools/validate/themes/semiotics_language_hermeneutics.py
- validator command: python3 tools/validate/themes/semiotics_language_hermeneutics.py --repo . --final
- downgrade/defer decision: mature-package path approved for this run because the own section supplies 22 corpus rows and row-specific evidence is available; concept/relation/close-reading batches remain deferrable.
- top candidate rows by keyword density:
  - row 266 3-4-3 差异的辩证法: 差异×95, 符号×91, 德里达×61, 符号学×26, 能指×21
  - row 255 3-4 复习课: 符号×94, 结构主义×49, 话语×43, 差异×37, 拉康×33
  - row 256 3-4-1 结构主义: 符号×82, 能指×65, 差异×58, 语言×49, 所指×38
  - row 254 3-4 符号学: 符号×115, 符号学×71, 语言×66, 结构主义×30, 能指×17
  - row 257 3-4-1-1 结构人本主义: 能指×84, 符号×58, 语言×43, 所指×32, 差异×25
  - row 258 3-4-1-2 隐喻的象征主义: 符号×68, 拉康×48, 能指×41, 符号学×30, 结构主义×19
  - row 262 3-4-2-1 无意识的主体主义: 能指×115, 拉康×42, 符号×31, 符号学×13, 结构主义×11
  - row 259 3-4-1-3 分类性的叙事学: 结构主义×60, 符号×39, 文本×35, 能指×24, 符号学×12

## G001 acceptance result

- donor inspection recorded: yes
- baseline validation recorded: yes
- four per-theme scope charters recorded: yes
- downgrade decisions recorded: yes, all four continue as mature packages
- protected corpus edit boundary: no raw/clean corpus edits made in G001
