# Social Topics Route 2 — Platform, Public Affect, Institution, and Class Synthesis

- status: G033 cross-theme synthesis; evidence-routed, not canonical ontology
- route_group: Social Topics Router
- integrates:
  - `library/themes/media-platform-public-opinion/`
  - `library/themes/governance-law-bureaucracy/`
  - `library/themes/class-youth-generational-anxiety/`
- method anchor: `library/protocols/social-phenomena-diagnostic-protocol.md`
- boundary: no current-events commentary, legal advice, policy analysis, or unsupported platform sociology; all use must return to row/quote evidence.

## Core question

How do private suffering, public affect, platform visibility, institutional order, and class anxiety mediate each other?

This phase answers: private suffering becomes public affect when a platform or public discourse carrier makes it visible, countable, narratable, and judgeable; institutions then stabilize, process, discipline, or displace that affect; class and generational positions determine how the same visibility/order is lived as anxiety, humiliation, cynicism, aspiration, or blocked mobility.

```text
private symptom or grievance
→ platform visibility / traffic / public opinion window
→ public affect, fan/idol investment, judgment, cynicism, forgetting
→ rule, bureaucracy, law, order, risk/security procedure
→ class/youth mobility promise or humiliation
→ renewed private suffering or displaced practice
```

This is a social-diagnosis route, not a news-commentary route. It does not say that every online event, institution, or youth anxiety follows this exact sequence; it supplies a row-grounded grammar for checking whether a concrete case does.

## Diagnostic axes

### 1. Platform visibility turns attention into a carrier of public affect

The Media-platform layer shows that public affect is not simply already-present opinion. It is carried by media/platform forms: platform operation, live-stream room, traffic purchase, recommendation, advertising, short video image, public discourse space, fan/idol relation, and network cynicism.

Evidence route:

- main synthesis: `library/themes/media-platform-public-opinion/media-platform-public-opinion-synthesis.md`
- focused synthesis: `library/themes/media-platform-public-opinion/platform-traffic-attention-economy-synthesis.md`
- focused synthesis: `library/themes/media-platform-public-opinion/public-opinion-fandom-network-cynicism-synthesis.md`
- classes: `platform-traffic-attention`, `public-opinion-discourse-space`, `fandom-idol-celebrity`, `network-cynicism-public-judgment`, `algorithm-data-recommendation-bridge`
- concept handles include: `平台社会`, `流量`, `短视频`, `直播平台`, `平台运营`, `广告投放`, `买流量`, `定向强化`, `注意力可用度`, `算法加权`, `推荐系统`, `舆论窗口`, `公众遗忘`, `网络犬儒`

Diagnostic use: for `短视频成瘾`, `直播`, `热搜舆论`, `网红`, `饭圈`, or `舆论审判`, first ask what carrier makes the scene visible and countable. `热搜` and `饭圈` remain downstream diagnostic labels unless exact adjacent evidence supports them.

### 2. Institutions convert affect into procedure, rule, discipline, or risk management

The Governance-law layer shows how public problems can be recoded as procedure, rule, legality, bureaucracy, discipline, command, risk, security, and justice imagination.

Evidence route:

- main synthesis: `library/themes/governance-law-bureaucracy/governance-law-bureaucracy-synthesis.md`
- focused synthesis: `library/themes/governance-law-bureaucracy/law-bureaucracy-rule-fetishism-synthesis.md`
- focused synthesis: `library/themes/governance-law-bureaucracy/discipline-risk-security-governance-synthesis.md`
- classes: `institution-organization-administration`, `governance-control-management`, `discipline-obedience-command`, `rules-order-normativity`, `law-rights-legalism`, `bureaucracy-kafka-judgment`, `risk-security-management`, `justice-legitimacy-state`

Diagnostic use: for `官僚手续`, `法律意识`, `规则拜物`, `治理技术`, or `服从结构`, ask whether institutional form is enabling practice or displacing responsibility into procedure. The layer must not be used for external legal advice or current-event case evaluation.

### 3. Class/youth position decides how visibility and order are lived

The Class-youth layer shows that public affect and institutional order are not received by a neutral public. They are lived through stratification, youth/future promise, credential/labor carriers, success ideology, humiliation, poverty/wealth difference, and blocked mobility.

Evidence route:

- main synthesis: `library/themes/class-youth-generational-anxiety/class-youth-generational-anxiety-synthesis.md`
- focused synthesis: `library/themes/class-youth-generational-anxiety/mobility-anxiety-class-solidification-synthesis.md`
- focused synthesis: `library/themes/class-youth-generational-anxiety/youth-success-bottom-humiliation-synthesis.md`
- classes: `middle-class-anxiety`, `class-solidification-channel-blockage`, `class-stratification-mobility`, `bottom-shame-humiliation`, `poverty-wealth-inequality`, `success-competition-merit`, `youth-generation-future`, `youth-nihilism-cynicism`

Diagnostic use: for `中产焦虑`, `青年虚无`, `底层羞辱`, `阶层固化`, `贫富差异`, or `成功学`, ask how the subject is positioned before it appears in public. Do not upgrade generic `虚无`, `底层`, `地位`, or `上升` wording into a class-youth claim without row-class support.

## Cross-theme mediation map

| Link | Diagnostic movement | Evidence-routed interpretation |
|---|---|---|
| private suffering → platform visibility | symptom becomes shareable scene, traffic, scandal, fan/idol object, or public judgment | The platform does not merely show the problem; it shapes what counts as visible, memorable, valuable, and judgeable. |
| platform visibility → institution | public affect demands order, rule, management, legality, or security | Procedure can stabilize conflict while also displacing responsibility and practice. |
| institution → class/youth anxiety | rule and order distribute recognition, opportunity, shame, and legitimacy unevenly | A procedure can appear neutral while being lived as blocked channel, fragile status, or humiliation. |
| class/youth anxiety → platform affect | blocked future seeks recognition in public discourse, cynicism, celebrity, scandal, or resentment | Visibility can be mistaken for practical transformation. |
| platform → class fantasy | traffic, fan devotion, influencer visibility, and public ranking promise symbolic mobility | Visibility can imitate mobility while leaving structural carriers untouched. |
| governance → platform | order, discipline, and risk management shape what can be said, circulated, forgotten, or judged | Publicness and order mediate each other rather than belonging to separate spheres. |

## Use as a diagnostic sequence

For a concrete Route 2 query:

1. Identify whether the problem starts as platform visibility, institutional procedure, or class/youth anxiety.
2. Open the matching theme query helper and manifest row.
3. Inspect exact quote records and `theme_class`; do not rely on keyword presence alone.
4. Ask which public affect is produced: indignation, fandom, cynicism, forgetting, humiliation, aspiration, fear, obedience.
5. Check whether the institutional carrier enables practice or substitutes procedure/rule/security for transformation.
6. Check whether class/youth position changes the subject's exposure, credibility, shame, or future promise.
7. Use concept/relation only as draft handles and close-reading only as pilot-draft close-reading aids.

## Query routes

```bash
# Media / platform / public opinion
python3 tools/query/themes/media_platform_public_opinion.py 平台 --limit 3
python3 tools/query/themes/media_platform_public_opinion.py 舆论 --limit 3
python3 tools/query/themes/media_platform_public_opinion.py 流量 --limit 3
python3 tools/query/themes/media_platform_public_opinion.py 直播 --limit 3
python3 tools/query/themes/media_platform_public_opinion.py 网红 --limit 3

# Governance / law / bureaucracy / order
python3 tools/query/themes/governance_law_bureaucracy.py 治理 --limit 3
python3 tools/query/themes/governance_law_bureaucracy.py 官僚 --limit 3
python3 tools/query/themes/governance_law_bureaucracy.py 规则拜物 --limit 3
python3 tools/query/themes/governance_law_bureaucracy.py 法律 --limit 3

# Class / youth / generation / mobility anxiety
python3 tools/query/themes/class_youth_generational_anxiety.py 阶层 --limit 3
python3 tools/query/themes/class_youth_generational_anxiety.py 青年 --limit 3
python3 tools/query/themes/class_youth_generational_anxiety.py 中产焦虑 --limit 3
python3 tools/query/themes/class_youth_generational_anxiety.py 青年虚无 --limit 3
python3 tools/query/themes/class_youth_generational_anxiety.py 底层 --limit 3
```

## Boundary and failure modes

- Do not equate visibility with truth, traffic with social value, public anger with practice, rule with justice, legality with legitimacy, or youth anxiety with individual weakness.
- Do not turn this synthesis into platform-opinion commentary, legal commentary, policy advice, or generational moralizing.
- `热搜`, `饭圈`, `短视频成瘾`, `上升通道`, `阶层固化`, `中产焦虑`, `青年虚无`, and `底层羞辱` can be query labels, but claims require row/quote evidence and theme-class support.
- concept/relation remain `draft`; close-reading remains `pilot-draft`.
