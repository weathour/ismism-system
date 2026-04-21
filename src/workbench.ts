import { manualSeedPack } from './data/manualSeed';
import type { NodeSeed, RelationAsset, StructuredOutput, ThreadMode } from './types';

export const activeRunStatuses = ['preparing', 'generating', 'streaming', 'finalizing'] as const;

export const modeLabel: Record<ThreadMode, string> = {
  orient: '导学',
  diagnose: '诊断',
  compare: '比较'
};

export const nodeById = Object.fromEntries(manualSeedPack.nodes.map((node) => [node.id, node]));
export const evidenceById = Object.fromEntries(manualSeedPack.evidenceAnchors.map((item) => [item.id, item]));
export const trainingById = Object.fromEntries(manualSeedPack.trainingCases.map((item) => [item.id, item]));
export const dimensionLenses = manualSeedPack.dimensionLenses;
export const themeProfiles = manualSeedPack.themeProfiles;

export function unique<T>(items: T[]) {
  return [...new Set(items)];
}

export function getRelatedAssets(nodeId: string, assets: RelationAsset[]) {
  return assets.filter((asset) => asset.nodeIds.includes(nodeId));
}

export function getSuggestedCompareNodeIds(nodeId: string, assets: RelationAsset[]) {
  const fromEdges = manualSeedPack.edges
    .filter((edge) => edge.type === 'confusion' && (edge.from === nodeId || edge.to === nodeId))
    .map((edge) => (edge.from === nodeId ? edge.to : edge.from));
  const fromAssets = assets
    .filter((asset) => asset.type === 'boundary' && asset.nodeIds.includes(nodeId))
    .flatMap((asset) => asset.nodeIds.filter((id) => id !== nodeId));
  return unique([...fromEdges, ...fromAssets]).filter((id) => Boolean(nodeById[id]));
}

export function buildStructuredOutput(
  mode: ThreadMode,
  node: NodeSeed,
  currentAssets: RelationAsset[],
  compareTarget?: NodeSeed
): StructuredOutput {
  const relatedAssets = currentAssets.filter((asset) => asset.nodeIds.includes(node.id));
  const compareAssets = compareTarget
    ? currentAssets.filter((asset) => asset.nodeIds.includes(node.id) && asset.nodeIds.includes(compareTarget.id))
    : [];
  const activeAssets = (mode === 'compare' ? compareAssets : relatedAssets).slice(0, 4);
  const evidenceIds = unique([
    ...node.evidenceIds,
    ...(compareTarget?.evidenceIds ?? []),
    ...activeAssets.flatMap((asset) => asset.evidenceIds)
  ]).filter(Boolean);
  const recommendedJumps = unique([
    node.id,
    ...(compareTarget ? [compareTarget.id] : []),
    ...activeAssets.flatMap((asset) => asset.recommendedJumps)
  ]).slice(0, 6);

  const compareSummary = compareTarget
    ? `对照对象为 ${compareTarget.shortTitle}，当前优先看两者的边界资产与排除理由。`
    : '当前尚未挂第二对象，因此比较会退回到边界卡推荐。';

  return {
    id: `${mode}-${node.id}-${Date.now()}`,
    mode,
    taskSummary:
      mode === 'orient'
        ? `从 ${node.shortTitle} 进入结构导学，优先建立它与方法轴、高混淆边界和主路线的关系。`
        : mode === 'diagnose'
          ? `围绕 ${node.shortTitle} 生成 provisional diagnosis，并把 relation-first 资产拉进线程主视图。`
          : `围绕 ${node.shortTitle}${compareTarget ? ` ↔ ${compareTarget.shortTitle}` : ''} 组织比较，突出边界、张力与推荐跳转。`,
    objectSummary:
      mode === 'compare' && compareTarget
        ? `${node.summary}；${compareTarget.summary}`
        : `${node.summary} ${compareTarget ? compareSummary : ''}`,
    primaryOutput:
      mode === 'orient'
        ? `当前建议先把 ${node.shortTitle} 放回 ${node.parentId ? nodeById[node.parentId]?.shortTitle ?? '主干' : '方法骨架'}，再沿 boundary / route 资产进入高混淆区。`
        : mode === 'diagnose'
          ? `${node.shortTitle} 当前可作为主候选，但必须保留 relation-first 证据、排除链与不确定性。`
          : compareTarget
            ? `当前比较不做“两段摘要并排”，而是优先读取 ${activeAssets[0]?.title ?? '边界卡'} 来解释 ${node.shortTitle} 与 ${compareTarget.shortTitle} 的决定性分野。`
            : compareSummary,
    candidateOutputs:
      mode === 'compare'
        ? activeAssets.length > 0
          ? activeAssets.map((asset) => `边界/张力候选：${asset.title}`)
          : ['候选 1：先补一个 compare 对象', '候选 2：先回 boundary rules 重新定轴']
        : activeAssets.length > 0
          ? activeAssets.map((asset) => `候选关系对象：${asset.title}`)
          : ['候选 1：回到方法轴确认当前讨论的是哪一轴', '候选 2：回到主干看它在 1/2/3/4 中的位置'],
    relationFindings:
      activeAssets.length > 0
        ? activeAssets.map((asset) => `${asset.type.toUpperCase()} · ${asset.summary}`)
        : ['当前节点的下一步价值不在扩写摘要，而在继续补 relation-first 资产。'],
    evidencePack: evidenceIds,
    uncertainty:
      activeAssets.some((asset) => asset.status === 'draft')
        ? '当前结果含 draft 级关系资产，只能作为探索性判断，不能冒充最终定论。'
        : '当前结果以 canonical/reviewed 资产为主，但仍保持 provisional 语义。',
    recommendedJumps,
    compareTargetId: compareTarget?.id,
    highlightAssetIds: activeAssets.map((asset) => asset.id)
  };
}

export function getDimensionLens(nodeId: string) {
  return dimensionLenses[nodeId] ?? dimensionLenses[nodeById[nodeId]?.parentId ?? ''] ?? dimensionLenses['macro-3'];
}

export function getThemeProfile(nodeId: string) {
  return themeProfiles[nodeId];
}
