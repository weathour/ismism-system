# Media / Platform / Public Opinion / Traffic Society Evidence Package

- 中文名：媒介—平台—舆论—流量社会证据包
- status: G016 closed Media / Platform / Public Opinion / Traffic Society theme package layer
- date: 2026-06-16 CST
- protocol: `library/protocols/social-phenomena-diagnostic-protocol.md`
- manifest: `media-platform-public-opinion-row-manifest.jsonl` (119 reviewed rows)
- evidence bank: `media-platform-public-opinion-evidence-bank.jsonl` (267 exact-normalizable quote records)
- taxonomy: `media-platform-public-opinion-taxonomy.md`
- concept batch: `concept-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16` (45 draft senses)
- relation batch: `relation-MEDIA-PLATFORM-PUBLIC-OPINION-2026-06-16` (40 draft relations)
- close-reading batch: 30 Media-platform pilot-draft cards
- concept/relation notes: `media-platform-public-opinion-concept-relation-batch-notes.md`
- validator: `python3 tools/validate/themes/media_platform_public_opinion.py --repo . --final`
- query helper: `python3 tools/query/themes/media_platform_public_opinion.py 平台 --limit 3`
- syntheses: `media-platform-public-opinion-synthesis.md`, `platform-traffic-attention-economy-synthesis.md`, `public-opinion-fandom-network-cynicism-synthesis.md`

This is not a neutral media-studies encyclopedia and not current-events commentary. It absorbs how ISMISM internally makes media, platform operations, public opinion, traffic, short video/live-stream examples, influencer/fan-idol formations, attention/data capture, public judgment, and network cynicism usable for social diagnosis.

## Scope markers

媒介 / 媒体 / 传媒 / 传播 / 平台 / 舆论 / 流量 / 短视频 / 直播 / 热搜 / 网红 / 饭圈 / 注意力经济 / 舆论审判 / 网络犬儒 / 粉丝 / 偶像 / 算法 / 数据 / 推荐 / 公共话语。

Boundary note: the current corpus has no direct exact `热搜` or `饭圈` hits. G014 therefore treats these as downstream diagnostic labels only; exact row evidence is concentrated in adjacent terms such as `平台`, `舆论`, `流量`, `短视频`, `直播`, `网红`, `粉丝`, `偶像`, `注意力`, `算法`, `数据`, `推荐`, `媒介`, `媒体`, `传媒`, `传播`, `公共话语`, and `犬儒`.

## Counts

| Item | Count |
|---|---:|
| reviewed manifest rows | 119 |
| evidence quotes | 267 |
| core rows | 46 |
| bridge rows | 63 |
| context rows | 0 |
| excluded rows | 10 |

## Theme classes

- `attention-algorithm-data-capture` — 24 rows
- `cynicism-spectacle-affect-network` — 6 rows
- `discourse-narrative-network-mediatization` — 18 rows
- `excluded-keyword-only` — 10 rows
- `fandom-idol-influencer-economy` — 11 rows
- `governance-platform-public-order-bridge` — 11 rows
- `media-communication-propaganda` — 18 rows
- `platform-traffic-behavior-engineering` — 12 rows
- `public-opinion-judgment-public-sphere` — 9 rows

## Interpretation rules

1. Start from the manifest, then inspect the evidence bank.
2. Use the shared diagnostic grammar: phenomenon → subject-position → mechanism → fantasy/misrecognition → carrier → contradiction → practical opening.
3. Do not treat every `网络`, `文本`, `话语`, `直播`, `饭`, or `数据` hit as media-platform evidence; use `core_status`, `theme_class`, and exact quotes.
4. G014 is evidence-only. concept/relation records must be added only in G015 and remain `draft`; close-reading cards must remain `pilot-draft`.
5. Cross-theme bridges to Aesthetics-Media, AI, Psychoanalysis-Subjectivity, Consumption, Governance, and Class require row-level quote support.
