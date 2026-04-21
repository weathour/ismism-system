export type AssetStatus = 'draft' | 'reviewed' | 'canonical';
export type NodeType = 'macro' | 'spine' | 'method';
export type EdgeType = 'hierarchy' | 'method' | 'transition' | 'confusion';
export type RelationAssetType = 'boundary' | 'route' | 'tension' | 'mediation';
export type RunStatus =
  | 'idle'
  | 'preparing'
  | 'generating'
  | 'streaming'
  | 'finalizing'
  | 'done'
  | 'error'
  | 'cancelled';
export type ThreadMode = 'orient' | 'diagnose' | 'compare';
export type TrainingCaseType = 'canonical' | 'confusion' | 'hard' | 'disputed';

export interface NodeSeed {
  id: string;
  title: string;
  shortTitle: string;
  type: NodeType;
  status: AssetStatus;
  summary: string;
  whyImportant: string;
  parentId?: string;
  evidenceIds: string[];
  tags: string[];
}

export interface EdgeSeed {
  id: string;
  from: string;
  to: string;
  type: EdgeType;
  reason: string;
}

export interface EvidenceAnchor {
  id: string;
  title: string;
  path: string;
  pageLabel: string;
  summary: string;
  excerpt: string;
  nodeIds: string[];
}

export interface RelationAsset {
  id: string;
  title: string;
  type: RelationAssetType;
  status: AssetStatus;
  summary: string;
  whyImportant: string;
  nodeIds: string[];
  evidenceIds: string[];
  reviewNote: string;
  recommendedJumps: string[];
}

export interface TrainingCase {
  id: string;
  title: string;
  type: TrainingCaseType;
  status: AssetStatus;
  prompt: string;
  choices: { id: string; label: string; targetNodeId?: string }[];
  correctChoiceId: string;
  explanation: string;
  relatedAssetIds: string[];
  remediationNodeIds: string[];
  evidenceIds: string[];
}

export interface StructuredOutput {
  id: string;
  mode: ThreadMode;
  taskSummary: string;
  objectSummary: string;
  primaryOutput: string;
  candidateOutputs: string[];
  relationFindings: string[];
  evidencePack: string[];
  uncertainty: string;
  recommendedJumps: string[];
  compareTargetId?: string;
  highlightAssetIds: string[];
}

export interface DimensionLens {
  field: string;
  ontology: string;
  epistemology: string;
  teleology: string;
  emphasis: string;
}

export interface ThemeProfileDimension {
  thesis: string;
  cue: string;
  risk: string;
}

export interface ThemeProfile {
  nodeId: string;
  title: string;
  summary: string;
  whySelected: string;
  confusionPairIds: string[];
  evidenceIds: string[];
  dialoguePrompts: string[];
  dimensions: {
    field: ThemeProfileDimension;
    ontology: ThemeProfileDimension;
    epistemology: ThemeProfileDimension;
    teleology: ThemeProfileDimension;
  };
}
