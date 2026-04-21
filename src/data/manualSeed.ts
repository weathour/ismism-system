import type { DimensionLens, EdgeSeed, EvidenceAnchor, NodeSeed, RelationAsset, ThemeProfile, TrainingCase } from '../types';

export const seedMeta = {
  version: 'manual-v2-spine-boundary-first',
  strategy: 'spine_boundary_first',
  sourcePolicy: 'Hand-curated from split_md_clean/ plus Matrix_Backbone.md and Boundary_Rules.md.',
  notes: [
    'Map skeleton uses the four macro sections + sixteen second-level core nodes.',
    'Method nodes and high-confusion boundary assets are prioritized over breadth-heavy relation generation.',
    'A few reviewed/draft assets are intentionally retained to support the minimum review workflow.'
  ]
};

export const nodes: NodeSeed[] = [
  {
    id: 'macro-1',
    title: '1 实在论',
    shortTitle: '1 实在论',
    type: 'macro',
    status: 'canonical',
    summary: '作为整体场域和融贯秩序的起点区域，承接 1-1 到 1-4 的闭合型现实姿态。',
    whyImportant: '它是后续 2/3/4 跃迁的起点，也提供最典型的“闭合场”误判来源。',
    evidenceIds: ['ev-matrix-backbone'],
    tags: ['macro', 'truth-layer']
  },
  {
    id: 'macro-2',
    title: '2 形而上学',
    shortTitle: '2 形而上学',
    type: 'macro',
    status: 'canonical',
    summary: '围绕场域与存在者整体、在场与不在场、虚无与观看者等问题展开的张力区。',
    whyImportant: '它是从闭合现实到更高阶张力化思维的主过渡层。',
    evidenceIds: ['ev-matrix-backbone'],
    tags: ['macro', 'truth-layer']
  },
  {
    id: 'macro-3',
    title: '3 观念论',
    shortTitle: '3 观念论',
    type: 'macro',
    status: 'canonical',
    summary: '围绕主体、意向性、观念论传统、生存体验与符号结构展开的理论区。',
    whyImportant: '它把认识、主体与符号中介推到核心位置，是后续训练和比较任务的高混淆区。',
    evidenceIds: ['ev-matrix-backbone'],
    tags: ['macro', 'truth-layer']
  },
  {
    id: 'macro-4',
    title: '4 实践',
    shortTitle: '4 实践',
    type: 'macro',
    status: 'canonical',
    summary: '把理论推进到政治、组织、建设、乌托邦试验与实践单元的区域。',
    whyImportant: 'ISMISM 不停留在解释，而要走向诊断、实践与推演，这一层是工作台闭环的落脚点。',
    evidenceIds: ['ev-matrix-backbone', 'ev-practice-unit'],
    tags: ['macro', 'truth-layer', 'practice']
  },
  {
    id: 'method-field',
    title: '场域论',
    shortTitle: '场域论',
    type: 'method',
    status: 'canonical',
    summary: '优先回答“存在在什么背景秩序/展开面中出现”，不直接等同于对象本身。',
    whyImportant: '它是第一层边界测试，直接决定节点判位和地图导航视角。',
    evidenceIds: ['ev-boundary-axis'],
    tags: ['method', 'axis']
  },
  {
    id: 'method-ontology',
    title: '本体论',
    shortTitle: '本体论',
    type: 'method',
    status: 'canonical',
    summary: '优先回答“什么算真正存在、存在如何分项”，区别于背景性场域。',
    whyImportant: '它是大量 confusion pair 的分水岭，尤其在 1-1/1-2 与 2 字头中最常出错。',
    evidenceIds: ['ev-boundary-axis'],
    tags: ['method', 'axis']
  },
  {
    id: 'method-epistemology',
    title: '认识论',
    shortTitle: '认识论',
    type: 'method',
    status: 'canonical',
    summary: '优先回答“主体如何把握、表达、中介和合法化”，不是行动目的本身。',
    whyImportant: '它是现象学、观念论、符号学比较中的关键区分轴。',
    evidenceIds: ['ev-boundary-axis'],
    tags: ['method', 'axis']
  },
  {
    id: 'method-teleology',
    title: '目的论',
    shortTitle: '目的论',
    type: 'method',
    status: 'canonical',
    summary: '优先回答“朝哪里去、为何行动、如何闭合或跃迁”，体现整个体系的行动收束。',
    whyImportant: '训练与实践推演若缺这一轴，会退化成静态概念说明。',
    evidenceIds: ['ev-boundary-axis'],
    tags: ['method', 'axis']
  },
  {
    id: 'method-practice-unit',
    title: '实践单元',
    shortTitle: '实践单元',
    type: 'method',
    status: 'canonical',
    summary: '主体的客体化在实践中显现，实践单元是主体落地与历史撬动的最小工作形态。',
    whyImportant: '它把 4 字头从纯理论讨论推进到可训练、可诊断、可推演的实践面。',
    evidenceIds: ['ev-practice-unit'],
    tags: ['method', 'practice']
  },
  {
    id: 'method-boundary-rules',
    title: '边界规则',
    shortTitle: '边界规则',
    type: 'method',
    status: 'canonical',
    summary: '强调四元轴不能混写，同一个数字在不同轴上也不是同一个意思。',
    whyImportant: '这是 v1 训练、判定、比较与 review 的统一校准器。',
    evidenceIds: ['ev-boundary-axis'],
    tags: ['method', 'boundary']
  },
  {
    id: 'node-1-1',
    title: '1-1 科学实在论',
    shortTitle: '1-1 科学实在论',
    type: 'spine',
    status: 'canonical',
    summary: '把科学秩序及其派生实体当作唯一存在，主体位置被压扁为被装配的物。',
    whyImportant: '它是最常见的现代闭合姿态之一，也是后续边界训练的高频正例。',
    parentId: 'macro-1',
    evidenceIds: ['ev-1-1'],
    tags: ['science', 'closure', 'core']
  },
  {
    id: 'node-1-2',
    title: '1-2 宗教实在论',
    shortTitle: '1-2 宗教实在论',
    type: 'spine',
    status: 'canonical',
    summary: '共享统一宇宙场，但把主宰者与被主宰者、本体与存在者拉成分裂结构。',
    whyImportant: '它与 1-1 共场域但异本体，是最适合做 boundary card 的首批对象。',
    parentId: 'macro-1',
    evidenceIds: ['ev-1-2'],
    tags: ['religion', 'core', 'boundary']
  },
  {
    id: 'node-1-3',
    title: '1-3 庸俗唯我论',
    shortTitle: '1-3 庸俗唯我论',
    type: 'spine',
    status: 'canonical',
    summary: '在四轴矩阵中把主体性剩余中心化，表现为暴力、爱情、排他与唯美等策略。',
    whyImportant: '它是从闭合场进入主体残余处理的关键节点，适合训练“本体 vs 主体化调和”。',
    parentId: 'macro-1',
    evidenceIds: ['ev-1-3'],
    tags: ['subject', 'core']
  },
  {
    id: 'node-1-4',
    title: '1-4 平庸主义',
    shortTitle: '1-4 平庸主义',
    type: 'spine',
    status: 'canonical',
    summary: '维持人间秩序、拒绝本体反思，以安全、服从和明哲保身维持闭合。',
    whyImportant: '它解释“为什么怎么也学不进哲学”的入口，也给导学页提供高价值起点。',
    parentId: 'macro-1',
    evidenceIds: ['ev-1-4'],
    tags: ['ordinary', 'core', 'orient']
  },
  {
    id: 'node-2-1',
    title: '2-1 在场形而上学',
    shortTitle: '2-1 在场形而上学',
    type: 'spine',
    status: 'canonical',
    summary: '围绕在场/presence 建构形而上学，忽视差异、缺席和符号结构的中介。',
    whyImportant: '它为 2-2 与 3-4 的反思提供被批判对象，是高价值比较起点。',
    parentId: 'macro-2',
    evidenceIds: ['ev-2-1'],
    tags: ['presence', 'core', 'boundary']
  },
  {
    id: 'node-2-2',
    title: '2-2 辩证形而上学',
    shortTitle: '2-2 辩证形而上学',
    type: 'spine',
    status: 'canonical',
    summary: '从有名/无名、内外、宇宙/逻格斯等张力出发，把握时间、虚无与否定性的存在。',
    whyImportant: '它是从在场到辩证张力的关键跃迁节点。',
    parentId: 'macro-2',
    evidenceIds: ['ev-2-2'],
    tags: ['dialectic', 'core']
  },
  {
    id: 'node-2-3',
    title: '2-3 我思形而上学',
    shortTitle: '2-3 我思形而上学',
    type: 'spine',
    status: 'canonical',
    summary: '把意识、思维和第一人称距离本体化，使观看者获得正当的抽离位置。',
    whyImportant: '它是现代科学与后续现象学/观念论节点的重要桥梁。',
    parentId: 'macro-2',
    evidenceIds: ['ev-2-3'],
    tags: ['cogito', 'core']
  },
  {
    id: 'node-2-4',
    title: '2-4 反形而上学',
    shortTitle: '2-4 反形而上学',
    type: 'spine',
    status: 'canonical',
    summary: '嘴上拒绝形而上学，却在经验、秩序与政治学上保留暴力背景秩序。',
    whyImportant: '它解释多种“反形而上学却更封闭”的现代陷阱。',
    parentId: 'macro-2',
    evidenceIds: ['ev-2-4'],
    tags: ['anti-metaphysics', 'core']
  },
  {
    id: 'node-3-1',
    title: '3-1 现象学',
    shortTitle: '3-1 现象学',
    type: 'spine',
    status: 'canonical',
    summary: '以意向行为/意向对象二分和悬置技术组织第一人称经验。',
    whyImportant: '它是 3 字头最常见的入口，也最容易与观念论或符号学互相混淆。',
    parentId: 'macro-3',
    evidenceIds: ['ev-3-1'],
    tags: ['phenomenology', 'core', 'boundary']
  },
  {
    id: 'node-3-2',
    title: '3-2 德国观念论',
    shortTitle: '3-2 德国观念论',
    type: 'spine',
    status: 'canonical',
    summary: '围绕命题/设定、康德问题域、费希特/谢林/黑格尔的平行或发展关系组织理论。',
    whyImportant: '它是理解 3-1/3-3/3-4 的中轴，也是比较模式的高价值对象。',
    parentId: 'macro-3',
    evidenceIds: ['ev-3-2'],
    tags: ['idealism', 'core']
  },
  {
    id: 'node-3-3',
    title: '3-3 生存论',
    shortTitle: '3-3 生存论',
    type: 'spine',
    status: 'canonical',
    summary: '聚焦内在实存、代价、命运与主体现身的后观念论冒险。',
    whyImportant: '它与 3-4 一样都反观念论，但一个偏体验/实存，一个偏结构/符号，最适合做 hard confusion case。',
    parentId: 'macro-3',
    evidenceIds: ['ev-3-3'],
    tags: ['existential', 'core', 'hard-case']
  },
  {
    id: 'node-3-4',
    title: '3-4 符号学',
    shortTitle: '3-4 符号学',
    type: 'spine',
    status: 'canonical',
    summary: '强调结构是关系性的，借结构主义运动对现象学的直接表达冲动提出反抗。',
    whyImportant: '它是 map、thread 与 relation asset 渲染的关键理论背景。',
    parentId: 'macro-3',
    evidenceIds: ['ev-3-4'],
    tags: ['semiotics', 'core', 'boundary']
  },
  {
    id: 'node-4-1',
    title: '4-1 政治-经济-意识形态批判',
    shortTitle: '4-1 政治-经济-意识形态批判',
    type: 'spine',
    status: 'canonical',
    summary: '通过历史、人民、理论家三元结构理解政治-经济-意识形态的交叉批判。',
    whyImportant: '它是实践区最适合先做诊断/线程/证据回链的锚点。',
    parentId: 'macro-4',
    evidenceIds: ['ev-4-1'],
    tags: ['practice', 'critique', 'core']
  },
  {
    id: 'node-4-2',
    title: '4-2 现实的正统化',
    shortTitle: '4-2 现实的正统化',
    type: 'spine',
    status: 'canonical',
    summary: '围绕行动者、理论家、人民和历史的配置，为现实合法性与正统性进行辩护。',
    whyImportant: '它与 4-1 共享实践区但方向不同，是第一批 scholar review 的重点边界。',
    parentId: 'macro-4',
    evidenceIds: ['ev-4-2'],
    tags: ['practice', 'orthodoxy', 'boundary']
  },
  {
    id: 'node-4-3',
    title: '4-3 建设理想社会',
    shortTitle: '4-3 建设理想社会',
    type: 'spine',
    status: 'canonical',
    summary: '围绕生存、解放、发展与实现展开建设者视角下的社会主义建设问题。',
    whyImportant: '它为训练和实践投射提供正向建设路径。',
    parentId: 'macro-4',
    evidenceIds: ['ev-4-3'],
    tags: ['practice', 'construction', 'core']
  },
  {
    id: 'node-4-4',
    title: '4-4 不可能的乌托邦',
    shortTitle: '4-4 不可能的乌托邦',
    type: 'spine',
    status: 'canonical',
    summary: '以不可能方案和思想实验探索异化被克服后的新矛盾与新敌托邦。',
    whyImportant: '它提供 project / trace / speculative comparison 的高阶目标区。',
    parentId: 'macro-4',
    evidenceIds: ['ev-4-4'],
    tags: ['practice', 'utopia', 'project']
  }
];

export const edges: EdgeSeed[] = [
  ...['1-1', '1-2', '1-3', '1-4'].map((id) => ({
    id: `edge-macro-1-${id}`,
    from: 'macro-1',
    to: `node-${id}`,
    type: 'hierarchy' as const,
    reason: '实在论主部下的二级核心节点。'
  })),
  ...['2-1', '2-2', '2-3', '2-4'].map((id) => ({
    id: `edge-macro-2-${id}`,
    from: 'macro-2',
    to: `node-${id}`,
    type: 'hierarchy' as const,
    reason: '形而上学主部下的二级核心节点。'
  })),
  ...['3-1', '3-2', '3-3', '3-4'].map((id) => ({
    id: `edge-macro-3-${id}`,
    from: 'macro-3',
    to: `node-${id}`,
    type: 'hierarchy' as const,
    reason: '观念论主部下的二级核心节点。'
  })),
  ...['4-1', '4-2', '4-3', '4-4'].map((id) => ({
    id: `edge-macro-4-${id}`,
    from: 'macro-4',
    to: `node-${id}`,
    type: 'hierarchy' as const,
    reason: '实践主部下的二级核心节点。'
  })),
  {
    id: 'edge-field-to-1',
    from: 'method-field',
    to: 'macro-1',
    type: 'method',
    reason: '实在论区提供“整体场域/融贯秩序”的第一批训练样本。'
  },
  {
    id: 'edge-ontology-to-2',
    from: 'method-ontology',
    to: 'macro-2',
    type: 'method',
    reason: '形而上学区集中讨论本体与存在者关系。'
  },
  {
    id: 'edge-epistemology-to-3',
    from: 'method-epistemology',
    to: 'macro-3',
    type: 'method',
    reason: '观念论区集中处理认识、表达和中介问题。'
  },
  {
    id: 'edge-teleology-to-4',
    from: 'method-teleology',
    to: 'macro-4',
    type: 'method',
    reason: '实践区集中处理行动目的、收束与跃迁。'
  },
  {
    id: 'edge-practice-unit-to-4-1',
    from: 'method-practice-unit',
    to: 'node-4-1',
    type: 'method',
    reason: '4-1 提供理论家/人民/历史关系转向实践单元的入口。'
  },
  {
    id: 'edge-boundary-to-methods',
    from: 'method-boundary-rules',
    to: 'method-field',
    type: 'method',
    reason: '边界规则首先服务于四元轴分辨。'
  },
  {
    id: 'edge-route-1-2',
    from: 'macro-1',
    to: 'macro-2',
    type: 'transition',
    reason: '从闭合场与现实姿态跃迁到场域/存在者整体的形而上学张力。'
  },
  {
    id: 'edge-route-2-3',
    from: 'macro-2',
    to: 'macro-3',
    type: 'transition',
    reason: '从本体张力推进到意向性、设定、实存与结构。'
  },
  {
    id: 'edge-route-3-4',
    from: 'macro-3',
    to: 'macro-4',
    type: 'transition',
    reason: '从理论与中介推进到实践、组织与乌托邦试验。'
  },
  {
    id: 'edge-confusion-1-1-1-2',
    from: 'node-1-1',
    to: 'node-1-2',
    type: 'confusion',
    reason: '共享场域一，却在本体组织上分叉。'
  },
  {
    id: 'edge-confusion-3-3-3-4',
    from: 'node-3-3',
    to: 'node-3-4',
    type: 'confusion',
    reason: '同属反观念论高频区，但体验取向与结构取向不同。'
  }
];

export const evidenceAnchors: EvidenceAnchor[] = [
  {
    id: 'ev-matrix-backbone',
    title: '矩阵骨架：16 个二级核心节点',
    path: 'Zhuyi_Matrix_Engine/Phase0_Corpus/Matrix_Backbone.md',
    pageLabel: 'Section 3',
    summary: '明确列出 1/2/3/4 各自的四个二级核心节点，构成第一批地图骨架。',
    excerpt: '16 个二级核心节点',
    nodeIds: ['macro-1', 'macro-2', 'macro-3', 'macro-4']
  },
  {
    id: 'ev-boundary-axis',
    title: '四元轴边界规则',
    path: 'Zhuyi_Matrix_Engine/Phase1_Concepts/Boundary_Rules.md',
    pageLabel: 'Sections 1-4',
    summary: '规定场域/本体/认识/目的四轴不能混写，是 v1 训练与判定的统一边界。',
    excerpt: '四元轴不能混写',
    nodeIds: ['method-field', 'method-ontology', 'method-epistemology', 'method-teleology', 'method-boundary-rules']
  },
  {
    id: 'ev-practice-unit',
    title: '实践单元作为主体的落地形态',
    path: 'split_md_clean/4_实践/0276_4_实践_p7184.md',
    pageLabel: 'Pages 9-12',
    summary: '实践单元被明确为主体的客体化和历史撬动的最小工作形态。',
    excerpt: '实践的单元是一个主体',
    nodeIds: ['macro-4', 'method-practice-unit']
  },
  {
    id: 'ev-1-1',
    title: '1-1 科学实在论：秩序等于实体',
    path: 'split_md_clean/1_实在论/1-1_科学实在论/0002_1-1_科学实在论_p27.md',
    pageLabel: 'Pages 1-3',
    summary: '把科学秩序派生的实体当作唯一存在，主体被物神化并缺席。',
    excerpt: '秩序等于实体',
    nodeIds: ['node-1-1']
  },
  {
    id: 'ev-1-2',
    title: '1-2 宗教实在论：主宰与众生对立',
    path: 'split_md_clean/1_实在论/1-2_宗教实在论/0024_1-2_宗教实在论_p527.md',
    pageLabel: 'Pages 1-3',
    summary: '共享统一 cosmos，但主宰/众生、太一/杂多在本体层面保持分裂。',
    excerpt: '太一和杂多之间的对立',
    nodeIds: ['node-1-2']
  },
  {
    id: 'ev-1-3',
    title: '1-3 庸俗唯我论：主体性剩余中心化',
    path: 'split_md_clean/1_实在论/1-3_庸俗唯我论_复习课/0046_1-3_庸俗唯我论_复习课_p1069.md',
    pageLabel: 'Pages 1-6',
    summary: '四轴矩阵在此转向主体性剩余的四种中心化策略。',
    excerpt: '面对主体性的剩余',
    nodeIds: ['node-1-3']
  },
  {
    id: 'ev-1-4',
    title: '1-4 平庸主义：拒绝本体反思',
    path: 'split_md_clean/1_实在论/1-4_平庸主义_你为什么怎么也学不进哲学_前反思者中的拒绝反思者_你为什么如此平庸/0067_1-4_平庸主义_你为什么怎么也学不进哲学_前反思者中的拒绝反思者_你为什么如此平庸_p1674.md',
    pageLabel: 'Pages 1-3',
    summary: '通过“关我鸟事”的态度保持人间秩序与刻意平庸。',
    excerpt: '关我鸟事',
    nodeIds: ['node-1-4']
  },
  {
    id: 'ev-2-1',
    title: '2-1 在场形而上学：presence 与差异',
    path: 'split_md_clean/2_形而上学_古代贵族的精神冒险_背景性的符号秩序与它自己的对立_比下_形而下学_有余_比上_观/2-1_在场形而上学_宰制西方精神数千年的形而上学范式/0097_2-1_在场形而上学_宰制西方精神数千年的形而上学范式_p2415.md',
    pageLabel: 'Pages 1-6',
    summary: '以在场为本体支点，被差异、缺席和符号关系问题击穿。',
    excerpt: 'presence 在场',
    nodeIds: ['node-2-1']
  },
  {
    id: 'ev-2-2',
    title: '2-2 辩证形而上学：有名/无名、宇宙/逻格斯',
    path: 'split_md_clean/2_形而上学_古代贵族的精神冒险_背景性的符号秩序与它自己的对立_比下_形而下学_有余_比上_观/2-2_辩证形而上学_把握时间_把握虚无_把握否定性的存在/0118_2-2_辩证形而上学_把握时间_把握虚无_把握否定性的存在_p3136.md',
    pageLabel: 'Pages 1-3',
    summary: '通过有名/无名和宇宙/逻格斯等辩证张力进入否定性存在。',
    excerpt: '无名天地之始',
    nodeIds: ['node-2-2']
  },
  {
    id: 'ev-2-3',
    title: '2-3 我思形而上学：观看者本体化',
    path: 'split_md_clean/2_形而上学_古代贵族的精神冒险_背景性的符号秩序与它自己的对立_比下_形而下学_有余_比上_观/2-3_我思形而上学_笛卡尔的梦魇_斯宾诺莎的宁静_科学的摇篮_形而上学的坟墓/0144_2-3_我思形而上学_笛卡尔的梦魇_斯宾诺莎的宁静_科学的摇篮_形而上学的坟墓_p3909.md',
    pageLabel: 'Pages 1-5',
    summary: '让“我思/意识/距离”获得本体论地位，为现代科学和现象学提供桥。',
    excerpt: '我思这个东西',
    nodeIds: ['node-2-3']
  },
  {
    id: 'ev-2-4',
    title: '2-4 反形而上学：经验主义的暴力背景秩序',
    path: 'split_md_clean/2_形而上学_古代贵族的精神冒险_背景性的符号秩序与它自己的对立_比下_形而下学_有余_比上_观/2-4_反形而上学_学哲学必须绕开的陷阱_嘴巴上不承认自己是形而上学的形而上学/0166_2-4_反形而上学_学哲学必须绕开的陷阱_嘴巴上不承认自己是形而上学的形而上学_p4339.md',
    pageLabel: 'Pages 1-5',
    summary: '拒斥形而上学，却在经验与政治上保留一个难以言说的暴力背景秩序。',
    excerpt: '嘴巴上不承认自己是形而上学',
    nodeIds: ['node-2-4']
  },
  {
    id: 'ev-3-1',
    title: '3-1 现象学：意向行为 / 意向对象',
    path: 'split_md_clean/3_观念论_作为一个现代人_该怎样思考哲学/3-1_现象学_胡塞尔和他的事业_拥趸_敌人/0188_3-1_现象学_胡塞尔和他的事业_拥趸_敌人_p4987.md',
    pageLabel: 'Pages 1-5',
    summary: '通过悬置、意向行为和意向对象二分组织经验。',
    excerpt: '意向行为和意向对象',
    nodeIds: ['node-3-1']
  },
  {
    id: 'ev-3-2',
    title: '3-2 德国观念论：设定 / 命题 / 问题域',
    path: 'split_md_clean/3_观念论_作为一个现代人_该怎样思考哲学/3-2_德国观念论_人类哲学史最精华的部分/0210_3-2_德国观念论_人类哲学史最精华的部分_p5482.md',
    pageLabel: 'Pages 1-3',
    summary: '围绕 Kant 发出的难题与 Fichte/Schelling/Hegel 的设定运动组织德国观念论。',
    excerpt: 'setzung 设置',
    nodeIds: ['node-3-2']
  },
  {
    id: 'ev-3-3',
    title: '3-3 生存论：内在实存与代价',
    path: 'split_md_clean/3_观念论_作为一个现代人_该怎样思考哲学/3-3_生存论_Existentialism_温和布尔乔亚的激进反观念论/0232_3-3_生存论_Existentialism_温和布尔乔亚的激进反观念论_p5984.md',
    pageLabel: 'Pages 1-3',
    summary: '从内在实存、命运与真理代价切入后观念论冒险。',
    excerpt: '主体性是一个实存',
    nodeIds: ['node-3-3']
  },
  {
    id: 'ev-3-4',
    title: '3-4 符号学：结构是关系性的',
    path: 'split_md_clean/3_观念论_作为一个现代人_该怎样思考哲学/3-4_符号学/0254_3-4_符号学_p6567.md',
    pageLabel: 'Pages 1-4',
    summary: '以结构主义运动反击现象学的直接表达，强调结构与关系网络。',
    excerpt: '结构永远是关系性的',
    nodeIds: ['node-3-4']
  },
  {
    id: 'ev-4-1',
    title: '4-1 政治-经济-意识形态批判：历史 / 人民 / 理论家',
    path: 'split_md_clean/4_实践/4-1_政治-经济-意识形态批判/0277_4-1_政治-经济-意识形态批判_p7198.md',
    pageLabel: 'Pages 1-6',
    summary: '把政治、经济、意识形态与历史/人民/理论家三元结构交叉起来。',
    excerpt: '历史→理论家，普罗大众',
    nodeIds: ['node-4-1']
  },
  {
    id: 'ev-4-2',
    title: '4-2 现实的正统化：行动者与合法性',
    path: 'split_md_clean/4_实践/4-2_现实的正统化/0299_4-2_现实的正统化_p7647.md',
    pageLabel: 'Pages 1-4',
    summary: '围绕行动者、理论家和历史必然性的宣称组织现实合法性。',
    excerpt: '真正的现实的正统化',
    nodeIds: ['node-4-2']
  },
  {
    id: 'ev-4-3',
    title: '4-3 建设理想社会：生存、解放、发展、实现',
    path: 'split_md_clean/4_实践/4-3_建设理想社会/0321_4-3_建设理想社会_p8077.md',
    pageLabel: 'Pages 1-4',
    summary: '把建设理想社会拆成生存、解放、发展与实现等建设环节。',
    excerpt: 'first of all you have to survive',
    nodeIds: ['node-4-3']
  },
  {
    id: 'ev-4-4',
    title: '4-4 不可能的乌托邦：本体论实验',
    path: 'split_md_clean/4_实践/4-4_不可能的乌托邦/0342_4-4_不可能的乌托邦_p8560.md',
    pageLabel: 'Pages 1-6',
    summary: '以乌托邦方案和 VR 式实验想象异化克服后的新矛盾。',
    excerpt: '本体论实验',
    nodeIds: ['node-4-4']
  }
];

export const relationAssets: RelationAsset[] = [
  {
    id: 'asset-boundary-axis-field-vs-ontology',
    title: 'Boundary Card：场域论 vs 本体论',
    type: 'boundary',
    status: 'canonical',
    summary: '场域论问背景秩序，本体论问何为存在；共享数字或对象并不表示同一轴。',
    whyImportant: '这是 v1 最重要的第一道混淆边界。',
    nodeIds: ['method-field', 'method-ontology', 'node-1-1', 'node-1-2'],
    evidenceIds: ['ev-boundary-axis', 'ev-1-1', 'ev-1-2'],
    reviewNote: '可直接进入地图工作台和训练工作流。',
    recommendedJumps: ['node-1-1', 'node-1-2']
  },
  {
    id: 'asset-boundary-axis-ontology-vs-epistemology',
    title: 'Boundary Card：本体论 vs 认识论',
    type: 'boundary',
    status: 'canonical',
    summary: '本体论处理存在构成，认识论处理把握、中介和表达。',
    whyImportant: '这是 2-3、3-1、3-2 高频混淆的底层规则。',
    nodeIds: ['method-ontology', 'method-epistemology', 'node-2-3', 'node-3-1', 'node-3-2'],
    evidenceIds: ['ev-boundary-axis', 'ev-2-3', 'ev-3-1', 'ev-3-2'],
    reviewNote: '为 compare 模式保留。',
    recommendedJumps: ['node-2-3', 'node-3-1', 'node-3-2']
  },
  {
    id: 'asset-boundary-axis-epistemology-vs-teleology',
    title: 'Boundary Card：认识论 vs 目的论',
    type: 'boundary',
    status: 'canonical',
    summary: '认识论是如何把握与表达，目的论是朝哪里去与为何行动。',
    whyImportant: '它保证 thread 输出不会把解释误当行动导向。',
    nodeIds: ['method-epistemology', 'method-teleology', 'node-4-3'],
    evidenceIds: ['ev-boundary-axis', 'ev-4-3'],
    reviewNote: '为 training 回跳准备。',
    recommendedJumps: ['node-4-3']
  },
  {
    id: 'asset-boundary-1-1-vs-1-2',
    title: 'Boundary Card：1-1 vs 1-2',
    type: 'boundary',
    status: 'reviewed',
    summary: '两者都处于统一宇宙/场域，但 1-1 倾向秩序=实体，1-2 倾向主宰者/被主宰者分裂。',
    whyImportant: '是第一批 confusion 训练的最优样本。',
    nodeIds: ['node-1-1', 'node-1-2'],
    evidenceIds: ['ev-1-1', 'ev-1-2', 'ev-boundary-axis'],
    reviewNote: '已完成首轮人工筛读，可进入地图次级视图与训练。',
    recommendedJumps: ['method-field', 'method-ontology', 'node-1-1', 'node-1-2']
  },
  {
    id: 'asset-boundary-2-1-vs-2-2',
    title: 'Boundary Card：2-1 vs 2-2',
    type: 'boundary',
    status: 'reviewed',
    summary: '2-1 以在场为锚，2-2 以有名/无名与否定性张力推进。',
    whyImportant: '说明“形而上学内部也有跃迁”，不是一个扁平类目。',
    nodeIds: ['node-2-1', 'node-2-2'],
    evidenceIds: ['ev-2-1', 'ev-2-2'],
    reviewNote: '适合 compare 与 diagnose 的双候选输出。',
    recommendedJumps: ['node-2-1', 'node-2-2', 'node-2-3']
  },
  {
    id: 'asset-boundary-3-1-vs-3-2',
    title: 'Boundary Card：3-1 vs 3-2',
    type: 'boundary',
    status: 'reviewed',
    summary: '3-1 重在意向性与经验组织，3-2 重在设定、命题与观念论问题域。',
    whyImportant: '是 3 字头最频繁的“看起来都很理论”误判点。',
    nodeIds: ['node-3-1', 'node-3-2'],
    evidenceIds: ['ev-3-1', 'ev-3-2'],
    reviewNote: '可直接作为训练回跳卡使用。',
    recommendedJumps: ['node-3-1', 'node-3-2', 'method-epistemology']
  },
  {
    id: 'asset-boundary-3-3-vs-3-4',
    title: 'Boundary Card：3-3 vs 3-4',
    type: 'boundary',
    status: 'draft',
    summary: '3-3 走内在实存与代价，3-4 走符号结构与关系网络。二者都反观念论，但并不等价。',
    whyImportant: '是首批 hard case，既适合 compare 也适合 review。',
    nodeIds: ['node-3-3', 'node-3-4'],
    evidenceIds: ['ev-3-3', 'ev-3-4'],
    reviewNote: '故意保留为 draft，供 Scholar/Review 页完成升格。',
    recommendedJumps: ['node-3-3', 'node-3-4']
  },
  {
    id: 'asset-boundary-4-1-vs-4-2',
    title: 'Boundary Card：4-1 vs 4-2',
    type: 'boundary',
    status: 'reviewed',
    summary: '4-1 聚焦政治-经济-意识形态批判，4-2 聚焦现实合法性与正统化配置。',
    whyImportant: '这是实践区第一个值得进入 review 的核心边界。',
    nodeIds: ['node-4-1', 'node-4-2'],
    evidenceIds: ['ev-4-1', 'ev-4-2'],
    reviewNote: '当前可作为 reviewed 支撑材料。',
    recommendedJumps: ['node-4-1', 'node-4-2', 'method-practice-unit']
  },
  {
    id: 'asset-route-1-2-3-4',
    title: 'Route Card：1 → 2 → 3 → 4 主线跃迁',
    type: 'route',
    status: 'canonical',
    summary: '从闭合现实姿态，经过形而上学张力和主体/符号中介，最终进入实践。',
    whyImportant: '这是首页推荐路径和地图主路线的种子。',
    nodeIds: ['macro-1', 'macro-2', 'macro-3', 'macro-4'],
    evidenceIds: ['ev-matrix-backbone'],
    reviewNote: '作为 v1 首页与地图主入口的默认路线。',
    recommendedJumps: ['macro-1', 'macro-2', 'macro-3', 'macro-4']
  },
  {
    id: 'asset-route-3-4-to-4-1',
    title: 'Route Card：3-4 符号学 → 4-1 批判实践',
    type: 'route',
    status: 'draft',
    summary: '从符号结构和关系网络，推进到政治-经济-意识形态批判。',
    whyImportant: '说明 relation-first 资产如何把理论区接到实践区。',
    nodeIds: ['node-3-4', 'node-4-1'],
    evidenceIds: ['ev-3-4', 'ev-4-1'],
    reviewNote: '先作为 draft 进入 Scholar 工作流。',
    recommendedJumps: ['node-3-4', 'node-4-1']
  },
  {
    id: 'asset-tension-presence-absence',
    title: 'Tension Card：在场 vs 不在场/差异',
    type: 'tension',
    status: 'reviewed',
    summary: '以 presence 为锚的形而上学与以差异/缺席拆解同一性的结构张力。',
    whyImportant: '为 diagnose 和 compare 模式提供标准关系对象。',
    nodeIds: ['node-2-1', 'node-3-4'],
    evidenceIds: ['ev-2-1', 'ev-3-4'],
    reviewNote: '可直接进入结构化输出渲染器。',
    recommendedJumps: ['node-2-1', 'node-3-4']
  },
  {
    id: 'asset-tension-history-people-theorist',
    title: 'Tension Card：历史 / 人民 / 理论家',
    type: 'tension',
    status: 'reviewed',
    summary: '4-1 中历史、人民、理论家并不只是并列项，而是围绕中介与实践权的张力结构。',
    whyImportant: '这是实践区 relation-first 输出的核心样本。',
    nodeIds: ['node-4-1', 'method-practice-unit'],
    evidenceIds: ['ev-4-1', 'ev-practice-unit'],
    reviewNote: '已适合 thread 渲染，但仍保留 scholar 争论空间。',
    recommendedJumps: ['node-4-1', 'method-practice-unit']
  },
  {
    id: 'asset-mediation-practice-unit',
    title: 'Mediation Card：理论 → 实践单元',
    type: 'mediation',
    status: 'draft',
    summary: '实践单元把历史、人民和理论家等对象关系中介到真正的主体客体化。',
    whyImportant: '这是 4 字头工作台不退化成抽象聊天的关键关系对象。',
    nodeIds: ['method-practice-unit', 'node-4-1', 'node-4-3'],
    evidenceIds: ['ev-practice-unit', 'ev-4-1', 'ev-4-3'],
    reviewNote: '需要后续 scholar note 确认“实践单元”的展示话术。',
    recommendedJumps: ['method-practice-unit', 'node-4-1', 'node-4-3']
  },
  {
    id: 'asset-boundary-2-3-vs-3-1',
    title: 'Boundary Card：2-3 vs 3-1',
    type: 'boundary',
    status: 'reviewed',
    summary: '2-3 先把观看者/我思本体化，3-1 则以意向性二分组织经验；两者都强调主体，但切入层级不同。',
    whyImportant: '它能把 2 字头通向 3 字头的桥梁做实，适合 compare 模式。',
    nodeIds: ['node-2-3', 'node-3-1'],
    evidenceIds: ['ev-2-3', 'ev-3-1', 'ev-boundary-axis'],
    reviewNote: '作为第二批 reviewed 边界资产进入地图和线程。',
    recommendedJumps: ['node-2-3', 'node-3-1', 'node-3-2']
  },
  {
    id: 'asset-boundary-4-3-vs-4-4',
    title: 'Boundary Card：4-3 vs 4-4',
    type: 'boundary',
    status: 'draft',
    summary: '4-3 处理建设与实现，4-4 处理不可能乌托邦与思想实验；两者都面向未来，但一个偏建设，一个偏实验。',
    whyImportant: '它为实践区提供第二个高价值 hard boundary。',
    nodeIds: ['node-4-3', 'node-4-4'],
    evidenceIds: ['ev-4-3', 'ev-4-4'],
    reviewNote: '先以 draft 进入 scholar/review 工作流。',
    recommendedJumps: ['node-4-3', 'node-4-4', 'method-teleology']
  },
  {
    id: 'asset-route-2-3-3-1-3-4',
    title: 'Route Card：2-3 → 3-1 → 3-4',
    type: 'route',
    status: 'reviewed',
    summary: '从我思形而上学的观看者位置，进入现象学的意向性组织，再被符号学的结构关系反击。',
    whyImportant: '这是第二批最适合演示 compare/trace 共用线程模板的路线。',
    nodeIds: ['node-2-3', 'node-3-1', 'node-3-4'],
    evidenceIds: ['ev-2-3', 'ev-3-1', 'ev-3-4'],
    reviewNote: '适合在首页和 thread workspace 做推荐路线。',
    recommendedJumps: ['node-2-3', 'node-3-1', 'node-3-4']
  },
  {
    id: 'asset-route-4-1-4-3',
    title: 'Route Card：4-1 批判 → 4-3 建设',
    type: 'route',
    status: 'reviewed',
    summary: '从政治-经济-意识形态批判推进到建设理想社会，避免停在纯批判姿态。',
    whyImportant: '它把 thread 与 training 从批判导向建设路径。',
    nodeIds: ['node-4-1', 'node-4-3', 'method-practice-unit'],
    evidenceIds: ['ev-4-1', 'ev-4-3', 'ev-practice-unit'],
    reviewNote: '进入 reviewed 后可直接做 recommended jump。',
    recommendedJumps: ['node-4-1', 'node-4-3', 'method-practice-unit']
  },
  {
    id: 'asset-tension-theory-practice',
    title: 'Tension Card：理论姿态 vs 实践单元',
    type: 'tension',
    status: 'reviewed',
    summary: '理论活动若不被实践单元中介，会停留在抽象解释；一旦进入实践，又会遭遇牺牲、建设与合法性问题。',
    whyImportant: '这是 3 字头向 4 字头过渡时最需要可视化的张力。',
    nodeIds: ['node-3-2', 'node-4-1', 'method-practice-unit'],
    evidenceIds: ['ev-3-2', 'ev-4-1', 'ev-practice-unit'],
    reviewNote: '第二批 tension 样本，用于 thread 的 relation-first 渲染。',
    recommendedJumps: ['node-3-2', 'node-4-1', 'method-practice-unit']
  }
];

export const trainingCases: TrainingCase[] = [
  {
    id: 'case-axis-field-vs-ontology',
    title: 'Case：这是场域判断还是本体判断？',
    type: 'canonical',
    status: 'canonical',
    prompt: '如果一句话在讨论“存在在什么背景秩序/展开面中出现”，你应先判向哪一轴？',
    choices: [
      { id: 'field', label: '场域论', targetNodeId: 'method-field' },
      { id: 'ontology', label: '本体论', targetNodeId: 'method-ontology' },
      { id: 'epistemology', label: '认识论', targetNodeId: 'method-epistemology' }
    ],
    correctChoiceId: 'field',
    explanation: '场域论优先处理背景秩序；本体论则在此背景中讨论什么算存在。',
    relatedAssetIds: ['asset-boundary-axis-field-vs-ontology'],
    remediationNodeIds: ['method-field', 'method-ontology'],
    evidenceIds: ['ev-boundary-axis']
  },
  {
    id: 'case-1-1-vs-1-2',
    title: 'Confusion：1-1 还是 1-2？',
    type: 'confusion',
    status: 'canonical',
    prompt: '若一段材料既承认统一宇宙场，又把主宰者与众生拉成对立，它更接近哪个节点？',
    choices: [
      { id: '1-1', label: '1-1 科学实在论', targetNodeId: 'node-1-1' },
      { id: '1-2', label: '1-2 宗教实在论', targetNodeId: 'node-1-2' },
      { id: '1-4', label: '1-4 平庸主义', targetNodeId: 'node-1-4' }
    ],
    correctChoiceId: '1-2',
    explanation: '关键不在统一场，而在本体层是否出现主宰/被主宰的分裂。',
    relatedAssetIds: ['asset-boundary-1-1-vs-1-2'],
    remediationNodeIds: ['node-1-1', 'node-1-2', 'method-ontology'],
    evidenceIds: ['ev-1-1', 'ev-1-2']
  },
  {
    id: 'case-3-1-vs-3-2',
    title: 'Confusion：3-1 还是 3-2？',
    type: 'confusion',
    status: 'reviewed',
    prompt: '若一段话在强调悬置、意向行为/意向对象与经验组织，它更接近哪一节点？',
    choices: [
      { id: '3-1', label: '3-1 现象学', targetNodeId: 'node-3-1' },
      { id: '3-2', label: '3-2 德国观念论', targetNodeId: 'node-3-2' },
      { id: '3-4', label: '3-4 符号学', targetNodeId: 'node-3-4' }
    ],
    correctChoiceId: '3-1',
    explanation: '悬置与意向性是 3-1 的核心线索，不应被“都很理论”所误导。',
    relatedAssetIds: ['asset-boundary-3-1-vs-3-2'],
    remediationNodeIds: ['node-3-1', 'node-3-2'],
    evidenceIds: ['ev-3-1', 'ev-3-2']
  },
  {
    id: 'case-3-3-vs-3-4',
    title: 'Hard Case：3-3 还是 3-4？',
    type: 'hard',
    status: 'draft',
    prompt: '如果材料强调“内在实存、代价、命运、被烧掉的精神”，它更偏向 3-3 还是 3-4？',
    choices: [
      { id: '3-3', label: '3-3 生存论', targetNodeId: 'node-3-3' },
      { id: '3-4', label: '3-4 符号学', targetNodeId: 'node-3-4' }
    ],
    correctChoiceId: '3-3',
    explanation: '3-3 聚焦内在实存与代价；3-4 则优先关注结构与关系网络。',
    relatedAssetIds: ['asset-boundary-3-3-vs-3-4'],
    remediationNodeIds: ['node-3-3', 'node-3-4'],
    evidenceIds: ['ev-3-3', 'ev-3-4']
  },
  {
    id: 'case-4-1-vs-4-2',
    title: 'Disputed：4-1 还是 4-2？',
    type: 'disputed',
    status: 'reviewed',
    prompt: '若材料围绕历史、人民、理论家三元结构组织批判，它更应先落在 4-1 还是 4-2？',
    choices: [
      { id: '4-1', label: '4-1 政治-经济-意识形态批判', targetNodeId: 'node-4-1' },
      { id: '4-2', label: '4-2 现实的正统化', targetNodeId: 'node-4-2' }
    ],
    correctChoiceId: '4-1',
    explanation: '4-1 以批判性三元结构为主；4-2 则更多转向现实合法性的配置与正统化。',
    relatedAssetIds: ['asset-boundary-4-1-vs-4-2', 'asset-tension-history-people-theorist'],
    remediationNodeIds: ['node-4-1', 'node-4-2', 'method-practice-unit'],
    evidenceIds: ['ev-4-1', 'ev-4-2']
  },
  {
    id: 'case-2-3-vs-3-1',
    title: 'Confusion：2-3 还是 3-1？',
    type: 'confusion',
    status: 'reviewed',
    prompt: '若材料在强调“观看者/我思的距离被本体化”，它更偏向 2-3 还是 3-1？',
    choices: [
      { id: '2-3', label: '2-3 我思形而上学', targetNodeId: 'node-2-3' },
      { id: '3-1', label: '3-1 现象学', targetNodeId: 'node-3-1' }
    ],
    correctChoiceId: '2-3',
    explanation: '2-3 强调观看者距离本体化；3-1 强调意向性与悬置组织经验。',
    relatedAssetIds: ['asset-boundary-2-3-vs-3-1'],
    remediationNodeIds: ['node-2-3', 'node-3-1'],
    evidenceIds: ['ev-2-3', 'ev-3-1']
  },
  {
    id: 'case-4-3-vs-4-4',
    title: 'Hard Case：4-3 还是 4-4？',
    type: 'hard',
    status: 'draft',
    prompt: '若材料围绕乌托邦方案、VR 式思想实验与不可能性展开，它更接近 4-3 还是 4-4？',
    choices: [
      { id: '4-3', label: '4-3 建设理想社会', targetNodeId: 'node-4-3' },
      { id: '4-4', label: '4-4 不可能的乌托邦', targetNodeId: 'node-4-4' }
    ],
    correctChoiceId: '4-4',
    explanation: '4-3 面向现实建设过程；4-4 明确以不可能方案和思想实验推进。',
    relatedAssetIds: ['asset-boundary-4-3-vs-4-4'],
    remediationNodeIds: ['node-4-3', 'node-4-4'],
    evidenceIds: ['ev-4-3', 'ev-4-4']
  },
  {
    id: 'case-route-3-4-to-4-1',
    title: 'Canonical Route：从符号结构走向批判实践',
    type: 'canonical',
    status: 'reviewed',
    prompt: '若你要从 3-4 符号学继续推进到实践区，第一条更合适的推荐路线是什么？',
    choices: [
      { id: 'route-3-4-4-1', label: '进入 4-1 政治-经济-意识形态批判', targetNodeId: 'node-4-1' },
      { id: 'route-3-4-1-4', label: '回退到 1-4 平庸主义', targetNodeId: 'node-1-4' },
      { id: 'route-3-4-2-1', label: '停留在 2-1 在场形而上学', targetNodeId: 'node-2-1' }
    ],
    correctChoiceId: 'route-3-4-4-1',
    explanation: '3-4 的关系结构最适合先进入 4-1 的批判实践，而不是回到闭合区。',
    relatedAssetIds: ['asset-route-3-4-to-4-1', 'asset-tension-theory-practice'],
    remediationNodeIds: ['node-3-4', 'node-4-1', 'method-practice-unit'],
    evidenceIds: ['ev-3-4', 'ev-4-1']
  }
];

export const dimensionLenses: Record<string, DimensionLens> = {
  'macro-1': {
    field: '把世界先理解为一个融贯的整体场，是 1 字头的共同起点。',
    ontology: '本体处理仍相对闭合，容易把秩序与对象当作已经给定。',
    epistemology: '认识更多是从既成秩序出发，不急于拆开中介。',
    teleology: '目的往往偏向闭合、自保或自我中心化。',
    emphasis: '适合作为“为什么会卡在闭合场” 的总入口。'
  },
  'macro-2': {
    field: '不再满足于整体场，而是追问场与存在者整体如何张力化。',
    ontology: '本体问题成为主角，presence、虚无、我思都在争夺支点。',
    epistemology: '观看、命名、差异和否定性逐步被带进来。',
    teleology: '目的仍偏理论收束，但已为 3 字头让路。',
    emphasis: '适合作为“从闭合现实进入形而上学张力”的过渡层。'
  },
  'macro-3': {
    field: '场不再只是背景，而是被主体、意向性与符号结构共同塑形。',
    ontology: '本体问题转向主体、观念、实存与结构的不同站位。',
    epistemology: '认识与表达成为中心战场，是 map 的四维核心区。',
    teleology: '目的开始从理论姿态逼近实践姿态。',
    emphasis: '适合作为 compare / confusion 的高密度区域。'
  },
  'macro-4': {
    field: '场域进入历史、人民、组织与实践单元。',
    ontology: '本体不再只是说清楚是什么，而要承担建设、正统化与实验。',
    epistemology: '理论家、行动者、建设者等中介位置被重新配置。',
    teleology: '目的论显性化，直接指向批判、建设与乌托邦试验。',
    emphasis: '适合作为 thread 输出走向实践与 project 的落点。'
  },
  'node-1-1': {
    field: '默认存在一个稳定、均匀、科学可描述的秩序场。',
    ontology: '秩序与实体趋于同一，只有科学秩序派生的实体才算硬存在。',
    epistemology: '主体退居观看与服从规则的位置。',
    teleology: '收束到对既有秩序的接受与再生产。',
    emphasis: '最适合作为“现代闭合姿态”的标准样本。'
  },
  'node-1-2': {
    field: '同样承认统一宇宙场，但它是被主宰的 cosmos。',
    ontology: '太一/杂多、主宰/众生的分裂取代秩序=实体。',
    epistemology: '认识更多体现虔诚和超越性服膺。',
    teleology: '导向拯救、服从或追求超越秩序。',
    emphasis: '最适合与 1-1 做 boundary compare。'
  },
  'node-1-4': {
    field: '场缩成“人间秩序”，不再愿意继续上探。',
    ontology: '本体问题被一句“关我鸟事”主动切掉。',
    epistemology: '认识停在常识、自保与明哲保身。',
    teleology: '目的论变成安全、稳定和不冒险。',
    emphasis: '非常适合作为导学入口和初学者纠偏节点。'
  },
  'node-2-1': {
    field: '场表现为在场/缺席尚未被充分展开的表征空间。',
    ontology: 'presence 是支点，事物在场即被当作本体核心。',
    epistemology: '直接表征倾向强，还没充分意识到差异网络。',
    teleology: '目的仍是稳住形而上学大厦，而不是拆开它。',
    emphasis: '适合作为“为什么会被 3-4 反击”的前站。'
  },
  'node-2-3': {
    field: '场允许主体/世界拉开距离。',
    ontology: '我思和观看者位置被本体化。',
    epistemology: '观看、悬空、抽离成了合法姿态。',
    teleology: '为现代科学和后续现象学提供稳定起跳点。',
    emphasis: '非常适合与 3-1 现象学做 compare。'
  },
  'node-3-1': {
    field: '不预设背景场为白嫖真相，而从经验组织本身进入。',
    ontology: '本体不是先被定死，而是在意向性组织中被显现。',
    epistemology: '意向行为 / 意向对象是核心二分。',
    teleology: '目的先是严格描述与组织经验，而非直接行动。',
    emphasis: '适合作为四维镜里“认识论最强”的节点。'
  },
  'node-3-3': {
    field: '场被压缩为主体的内在实存和命运处境。',
    ontology: '实存和代价成为本体站位。',
    epistemology: '认识带有痛感、冒险和被烧掉的代价。',
    teleology: '逼向决断、命运承担和存在姿态。',
    emphasis: '适合作为 hard confusion 与 3-4 对照。'
  },
  'node-3-4': {
    field: '场本身就是关系网络和结构。',
    ontology: '本体让位于结构、差异和符号位置关系。',
    epistemology: '认识必须经过符号中介，反对直接表征。',
    teleology: '目的不是停在说明，而是为批判和路线选择约束上下文。',
    emphasis: '适合作为 map 的四维结构视图核心节点。'
  },
  'node-4-1': {
    field: '场进入历史、人民和理论家交错的实践区。',
    ontology: '批判性结构比静态存在判断更重要。',
    epistemology: '理论家位置与人民/历史的中介关系成为核心。',
    teleology: '目的指向政治-经济-意识形态批判。',
    emphasis: '适合作为从理论进入实践的第一落点。'
  },
  'node-4-3': {
    field: '场落到国家、组织、人民生存与发展。',
    ontology: '建设过程本身承担现实存在方式。',
    epistemology: '建设者如何组织、领导和共同建造成为关键。',
    teleology: '生存、解放、发展、实现直接进入目的链。',
    emphasis: '适合作为 teleology 强显节点。'
  },
  'node-4-4': {
    field: '场被推入实验性的未来条件和思想实验环境。',
    ontology: '本体论模型被当作可试验、可失败的方案。',
    epistemology: '认识必须面对不可能性、VR 条件与新异化。',
    teleology: '目的论最强，直接指向方案、敌托邦与未来后果。',
    emphasis: '适合作为 project / scholar 视图的高阶节点。'
  }
};

export const themeProfiles: Record<string, ThemeProfile> = {
  'node-1-1': {
    nodeId: 'node-1-1',
    title: '专题深描：1-1 科学实在论',
    summary: '把世界压成一个可计算、可装配、可重复验证的秩序场，是现代闭合姿态的最强样本。',
    whySelected: '它是 1 字头里最稳定、最现代、也最容易被误以为“天然正确”的起点。',
    confusionPairIds: ['node-1-2', 'node-2-3'],
    evidenceIds: ['ev-1-1', 'ev-boundary-axis'],
    dialoguePrompts: [
      '如果主体只是观看者，那谁来承担断裂与症状？',
      '当秩序与实体被压成同一种东西时，还剩多少真正的反思空间？'
    ],
    dimensions: {
      field: {
        thesis: '世界先被当成一个均匀、融贯、可测量的整体场。',
        cue: '出现“统一宇宙/规则场/一切可被科学描述”时，优先往 1-1 看。',
        risk: '容易把闭合秩序误当成唯一现实，而看不到症状与裂缝。'
      },
      ontology: {
        thesis: '秩序派生实体，实体只是在科学秩序中被装配出来的对象。',
        cue: '当秩序=实体、物理规律=物理实体时，这是 1-1 的强信号。',
        risk: '把人和主体也压扁成物，最后只剩被定价、被装配的对象。'
      },
      epistemology: {
        thesis: '观看者不需要深度反思，只要站在规则一侧接受和运算即可。',
        cue: '说话方式若偏“按规则推导、按结构服从”，认识论通常很薄。',
        risk: '会把无意识的知识生产直接误当成“我已经理解”。'
      },
      teleology: {
        thesis: '最终指向稳定再生产，而不是穿透闭合场。',
        cue: '如果结论总落回“继续按此运转”，就是 1-1 的典型收束。',
        risk: '会压制实践冲动，让系统只能复制自己。'
      }
    }
  },
  'node-2-3': {
    nodeId: 'node-2-3',
    title: '专题深描：2-3 我思形而上学',
    summary: '把观看者与意识的距离本体化，是从形而上学走向现代科学和现象学的重要桥。',
    whySelected: '它最适合说明 2 字头如何把“观看/抽离”正当化，并直接牵出 3-1。',
    confusionPairIds: ['node-3-1', 'node-2-2'],
    evidenceIds: ['ev-2-3', 'ev-boundary-axis'],
    dialoguePrompts: [
      '“我思”的距离为什么不是单纯的心理感受，而是一个本体位置？',
      '2-3 和 3-1 都重视主体，为什么不能混写？'
    ],
    dimensions: {
      field: {
        thesis: '场允许主体与世界拉开距离，观看成为合法动作。',
        cue: '只要出现“我可以抽离出来看”，就要警惕 2-3 的支点。',
        risk: '容易把抽离误当成天然中立，从而掩盖它的本体论前提。'
      },
      ontology: {
        thesis: '意识和观看者位置本身被抬升为本体论的一极。',
        cue: '当“我思/意识/距离”本身被说成真实存在的支点时，就是 2-3。',
        risk: '会假装自己只是在认识，其实已经偷偷改写了存在结构。'
      },
      epistemology: {
        thesis: '认识的优势在于拉开距离、冷静观察、正当悬置。',
        cue: '如果认识姿态强调“先退一步再看”，这是 2-3 的核心风格。',
        risk: '容易被误认成现象学，但它比现象学更先把观看者本体化。'
      },
      teleology: {
        thesis: '目的不是立即实践，而是先稳住一个观看与说明的阿基米德点。',
        cue: '最后落回“先站住这个点”，而不是“先行动”，就是 2-3。',
        risk: '会把行动无限延后，让世界只剩解释。'
      }
    }
  },
  'node-3-4': {
    nodeId: 'node-3-4',
    title: '专题深描：3-4 符号学',
    summary: '它不是又一套节点摘要理论，而是把结构、差异和关系网络本身推成主角。',
    whySelected: '这个项目的大地图如果不把 3-4 做深，很容易退回普通目录导航。',
    confusionPairIds: ['node-3-3', 'node-2-1'],
    evidenceIds: ['ev-3-4', 'ev-2-1'],
    dialoguePrompts: [
      '为什么 3-4 最适合作为地图系统的内部真相层约束器？',
      '它如何反击“语言就是把意义直接说出来”这种直觉？'
    ],
    dimensions: {
      field: {
        thesis: '场本身就是关系网络，而不是预先给好的白底背景。',
        cue: '凡是开始谈结构、位置、组合与网络关系，就在靠近 3-4。',
        risk: '若只把它做成结构术语展示，就会失去其动态性。'
      },
      ontology: {
        thesis: '本体不再优先属于单个对象，而要在结构位置和差异关系中显现。',
        cue: '对象如果必须通过“它不是什么”才站住，就要看 3-4。',
        risk: '容易被误听成“没有对象了”，其实只是对象不再先于结构。'
      },
      epistemology: {
        thesis: '认识必须经过符号中介，直接表征是不可信的。',
        cue: '任何“我说出来就等于抓住意义”的直觉，都可以用 3-4 反击。',
        risk: '如果前端只剩聊天而没有地图约束，3-4 的优势会直接丢失。'
      },
      teleology: {
        thesis: '目的不是停在解释结构，而是用结构约束比较、跳转和批判路径。',
        cue: '一旦开始问“下一步为什么跳这里”，就进入 3-4 的工作方式。',
        risk: '如果没有 route / boundary / tension 的对象化，3-4 会被削成概念介绍。'
      }
    }
  },
  'node-4-1': {
    nodeId: 'node-4-1',
    title: '专题深描：4-1 政治-经济-意识形态批判',
    summary: '这是把理论区真正推向实践区的第一落点：不是只说结构，而是开始组织历史、人民和理论家的交错关系。',
    whySelected: '它最适合说明这个系统为什么不能停在哲学说明，而必须走向诊断与实践推演。',
    confusionPairIds: ['node-4-2', 'node-4-3'],
    evidenceIds: ['ev-4-1', 'ev-practice-unit'],
    dialoguePrompts: [
      '4-1 为什么是从理论进入实践的第一步，而不是最终步骤？',
      '历史、人民、理论家为什么不是简单并列，而是张力结构？'
    ],
    dimensions: {
      field: {
        thesis: '场被重新写成历史、人民、理论家和批判现场。',
        cue: '如果一个对象已经进入社会结构、历史动力与人民位置，就不能再停在 3 字头。',
        risk: '容易把复杂现场重新压成单条历史必然性叙事。'
      },
      ontology: {
        thesis: '本体不再只是“什么存在”，而是哪些结构性力量在共同起作用。',
        cue: '当政治、经济、意识形态不是分科而是交叉结构时，就是 4-1。',
        risk: '若把它做成纯抽象批判，会失去实践落地。'
      },
      epistemology: {
        thesis: '理论家位置必须重新被审问：谁在命名、谁在中介、谁在说人民。',
        cue: '只要开始追问理论家和人民的关系，4-1 就进入核心。',
        risk: '会滑回理论家自我封闭，把人民重新当成被说明对象。'
      },
      teleology: {
        thesis: '目的不是解释社会，而是把批判推进到实践单元和建设方向。',
        cue: '若一轮对话最后只能停在“我懂了”，那还没有真正进入 4-1。',
        risk: '若没有通向 4-3 / 实践单元的跳转，就会重新退回纯理论姿态。'
      }
    }
  }
};

export const manualSeedPack = {
  meta: seedMeta,
  nodes,
  edges,
  evidenceAnchors,
  relationAssets,
  trainingCases,
  dimensionLenses,
  themeProfiles
};
