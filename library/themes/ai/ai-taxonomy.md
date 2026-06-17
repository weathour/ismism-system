# AI Theme Taxonomy

- status: pilot-draft
- layer: `library/themes/ai/` theme index/synthesis surface, not canonical corpus truth
- evidence: every node links to manifest row ids and representative evidence-bank ids
- validator: `python3 tools/validate/themes/ai.py --repo . --final` checks taxonomy row/class consistency

## Controlled theme classes
- `ai-theory-prehistory`
- `ai-vr-utopia`
- `ai-deanthropocentrization`
- `ai-body-memory-language`
- `ai-social-ethical-system`
- `ai-analogy`
- `peripheral-technical`
- `noise-review`

## T1. 认知主义 / 功能主义 / 强弱AI 前史

- theme_class: `ai-theory-prehistory`
- rows: row 13, row 14, row 15, row 16, row 17, row 18
- evidence_bank: `ev:ai:0013:01`, `ev:ai:0014:01`, `ev:ai:0015:01`, `ev:ai:0016:01`, `ev:ai:0017:01`, `ev:ai:0018:01`
- function: AI 在第一场域被作为认知主义与功能主义的研究目标、模型对象、工程对象或框架问题出现。

## T2. 弱VR / 不可能乌托邦

- theme_class: `ai-vr-utopia`
- rows: row 342, row 343, row 344, row 345, row 346, row 347, row 348
- evidence_bank: `ev:ai:0342:01`, `ev:ai:0343:01`, `ev:ai:0344:01`, `ev:ai:0345:01`, `ev:ai:0346:01`, `ev:ai:0347:01`
- function: 4-4 把 VR/AI 设为实践边界中的乌托邦式装置，而不是现实工程承诺。

## T3. 去人类中心化 / 永生 / 死亡 / 身体化转入

- theme_class: `ai-deanthropocentrization`
- rows: row 349, row 350, row 351, row 352, row 353
- evidence_bank: `ev:ai:0349:01`, `ev:ai:0350:01`, `ev:ai:0351:01`, `ev:ai:0352:01`, `ev:ai:0353:01`
- function: AI/VR 让人类中心组的永生、死亡、衰老、身体化问题被重新布置。

## T4. AI 身体 / 记忆 / 语言 / 秘密 / 再生

- theme_class: `ai-body-memory-language`
- rows: row 354, row 355, row 356, row 357, row 358, row 359, row 361, row 362, row 363
- evidence_bank: `ev:ai:0354:01`, `ev:ai:0355:01`, `ev:ai:0356:01`, `ev:ai:0357:01`, `ev:ai:0358:01`, `ev:ai:0359:01`
- function: AI 的主体性问题转入物质载体、身体、爱欲同化、秘密关系、语音、间隙、可朽性和再生。

## T5. AI 教育 / 筛选 / 社会机制

- theme_class: `ai-social-ethical-system`
- rows: row 360
- evidence_bank: `ev:ai:0360:01`
- function: AI 被放入训练、筛选、去AI化、自我认知和制度化教育机制中。

## T6. AI 类比与哲学比较

- theme_class: `ai-analogy`
- rows: row 8, row 36, row 53, row 121, row 227, row 263
- evidence_bank: `ev:ai:0008:01`, `ev:ai:0036:01`, `ev:ai:0053:01`, `ev:ai:0121:01`, `ev:ai:0227:01`, `ev:ai:0263:01`
- function: 分散行中的 AI/人工智能命中主要作为哲学类比、前史桥接或局部比较。

## T7. 外围技术命中

- theme_class: `peripheral-technical`
- rows: row 19, row 47, row 48, row 56, row 106, row 107, row 116, row 159, row 167, row 168, row 178, row 185, row 186, row 187, row 193, row 195, row 205, row 206, row 218, row 219, row 268, row 283, row 296, row 325, row 331
- evidence_bank: `ev:ai:0019:01`, `ev:ai:0047:01`, `ev:ai:0048:01`, `ev:ai:0056:01`, `ev:ai:0106:01`, `ev:ai:0107:01`
- function: 智能、算法、机器人、VR 等弱/外围技术命中保留为 context evidence，不直接转化为核心AI doctrine。

## T8. noise-review / false-positive audit

- theme_class: `noise-review`
- rows: row 5
- evidence_bank: `ev:ai:0005:01`
- function: 极弱或游戏化关键词命中只保留为审计线索，避免误升为 AI 主题 claim。

## Boundary rule
本 taxonomy 只提供 AI 主题检索轴；主要 claim 必须回链到 `ai-evidence-bank.jsonl`、concept/relation draft assets 或 close-reading pilot cards。
