import type { RunStatus, StructuredOutput, ThreadMode } from './types';
import { modeLabel, nodeById } from './workbench';

export const pages = [
  { id: 'home', label: 'Workbench' },
  { id: 'map', label: '地图' },
  { id: 'thread', label: '线程' },
  { id: 'training', label: '训练' },
  { id: 'review', label: 'Scholar / Review' }
] as const;

export type PageId = (typeof pages)[number]['id'];

export type ThreadRecord = {
  id: string;
  title: string;
  mode: ThreadMode;
  status: RunStatus;
  contextNodeId: string;
  compareTargetId?: string;
  statusMessage: string;
  history: StructuredOutput[];
  updatedAt: string;
};

export type RunSummary = {
  id: string;
  threadId: string;
  threadTitle: string;
  mode: ThreadMode;
  contextNodeId: string;
  compareTargetId?: string;
  status: RunStatus;
  summary: string;
  at: string;
};

export type FeedbackState = {
  caseId: string;
  correct: boolean;
  explanation: string;
};

export function createThreadRecord(mode: ThreadMode, contextNodeId: string, compareTargetId?: string): ThreadRecord {
  const contextNode = nodeById[contextNodeId];
  const compareNode = compareTargetId ? nodeById[compareTargetId] : undefined;
  const suffix = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 6)}`;
  return {
    id: `thread-${mode}-${suffix}`,
    title:
      mode === 'compare' && compareNode
        ? `${contextNode.shortTitle} ↔ ${compareNode.shortTitle}`
        : `${modeLabel[mode]} · ${contextNode.shortTitle}`,
    mode,
    status: 'idle',
    contextNodeId,
    compareTargetId,
    statusMessage: '线程空闲，可发起新的 heavy action。',
    history: [],
    updatedAt: new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
  };
}

export const mapViewOptions = [
  { id: 'structure', label: '结构视图' },
  { id: 'learning', label: '学习视图' },
  { id: 'diagnose', label: '判定视图' },
  { id: 'compare', label: '比较视图' },
  { id: 'scholar', label: '学者视图' }
] as const;

export type MapViewMode = (typeof mapViewOptions)[number]['id'];
