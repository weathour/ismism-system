import { useEffect, useMemo, useRef, useState } from 'react';
import { manualSeedPack } from './data/manualSeed';
import type { AssetStatus, RelationAsset, RunStatus } from './types';
import { activeRunStatuses, buildStructuredOutput, evidenceById, getDimensionLens, getRelatedAssets, getSuggestedCompareNodeIds, modeLabel, nodeById, unique } from './workbench';
import { createThreadRecord, pages, type FeedbackState, type MapViewMode, type PageId, type RunSummary, type ThreadRecord } from './appModel';
import { ContextRail, HomeView, InsightPanel, MapView, ReviewView, ThreadView, TrainingView } from './components/WorkbenchViews';

const initialThreadId = 'thread-orient-3-1';

function statusTone(status: RunStatus) {
  switch (status) {
    case 'done':
      return 'tone-done';
    case 'error':
      return 'tone-error';
    case 'cancelled':
      return 'tone-cancelled';
    default:
      return 'tone-running';
  }
}

function App() {
  const [page, setPage] = useState<PageId>('home');
  const [selectedNodeId, setSelectedNodeId] = useState<string>('node-3-1');
  const [selectedAssetId, setSelectedAssetId] = useState<string>('asset-boundary-3-1-vs-3-2');
  const [compareTargetId, setCompareTargetId] = useState<string>('node-3-2');
  const [assetStatusMap, setAssetStatusMap] = useState<Record<string, AssetStatus>>(
    Object.fromEntries(manualSeedPack.relationAssets.map((asset) => [asset.id, asset.status]))
  );
  const [reviewNotes, setReviewNotes] = useState<Record<string, string>>(
    Object.fromEntries(manualSeedPack.relationAssets.map((asset) => [asset.id, asset.reviewNote]))
  );
  const [threads, setThreads] = useState<ThreadRecord[]>([
    {
      ...createThreadRecord('orient', 'node-3-1', 'node-3-2'),
      id: initialThreadId,
      title: '导学 · 3-1 现象学',
      statusMessage: '初始线程已建立，可从地图继续推进。'
    }
  ]);
  const [activeThreadId, setActiveThreadId] = useState<string>(initialThreadId);
  const [recentRuns, setRecentRuns] = useState<RunSummary[]>([]);
  const [selectedTrainingCaseId, setSelectedTrainingCaseId] = useState<string>('case-2-3-vs-3-1');
  const [mapViewMode, setMapViewMode] = useState<MapViewMode>('structure');
  const [trainingFeedback, setTrainingFeedback] = useState<FeedbackState | null>(null);
  const timersRef = useRef<Record<string, number[]>>({});

  const currentAssets = useMemo(
    () => manualSeedPack.relationAssets.map((asset) => ({ ...asset, status: assetStatusMap[asset.id] })),
    [assetStatusMap]
  );

  const activeThread = threads.find((thread) => thread.id === activeThreadId) ?? threads[0];
  const activeThreadLocked = activeRunStatuses.includes(activeThread.status as (typeof activeRunStatuses)[number]);
  const selectedNode = nodeById[selectedNodeId];
  const selectedCompareTarget = nodeById[compareTargetId];
  const selectedAsset = currentAssets.find((asset) => asset.id === selectedAssetId) ?? currentAssets[0];
  const selectedTrainingCase = manualSeedPack.trainingCases.find((item) => item.id === selectedTrainingCaseId) ?? manualSeedPack.trainingCases[0];
  const reviewQueue = currentAssets.filter((asset) => asset.status !== 'canonical');
  const selectedNodeAssets = getRelatedAssets(selectedNodeId, currentAssets);
  const suggestedCompareNodeIds = useMemo(() => getSuggestedCompareNodeIds(selectedNodeId, currentAssets), [selectedNodeId, currentAssets]);
  const selectedNodeEvidenceIds = unique([
    ...selectedNode.evidenceIds,
    ...selectedNodeAssets.flatMap((asset) => asset.evidenceIds)
  ]);
  const highlightedAssetIds = activeThread.history[0]?.highlightAssetIds ?? [selectedAsset.id];
  const dimensionLens = getDimensionLens(selectedNodeId);
  const evidenceForSelection = unique([
    ...selectedNodeEvidenceIds,
    ...selectedAsset.evidenceIds,
    ...(activeThread.history[0]?.evidencePack ?? [])
  ]).filter((id) => Boolean(evidenceById[id]));

  useEffect(() => {
    return () => {
      Object.values(timersRef.current).flat().forEach((timer) => window.clearTimeout(timer));
    };
  }, []);

  useEffect(() => {
    if (!selectedCompareTarget || selectedCompareTarget.id === selectedNodeId) {
      const firstSuggestion = suggestedCompareNodeIds[0];
      if (firstSuggestion && firstSuggestion !== selectedNodeId) {
        setCompareTargetId(firstSuggestion);
      }
    }
  }, [selectedCompareTarget, selectedNodeId, suggestedCompareNodeIds]);

  const macroGroups = useMemo(
    () =>
      manualSeedPack.nodes
        .filter((node) => node.type === 'macro')
        .map((macro) => ({
          macro,
          children: manualSeedPack.nodes.filter((node) => node.parentId === macro.id)
        })),
    []
  );

  const threadSummaries = threads.slice().sort((a, b) => b.updatedAt.localeCompare(a.updatedAt));

  function clearThreadTimers(threadId: string) {
    const timers = timersRef.current[threadId] ?? [];
    timers.forEach((timer) => window.clearTimeout(timer));
    timersRef.current[threadId] = [];
  }

  function replaceThread(threadId: string, updater: (thread: ThreadRecord) => ThreadRecord) {
    setThreads((current) => current.map((thread) => (thread.id === threadId ? updater(thread) : thread)));
  }

  function focusNode(nodeId: string) {
    setSelectedNodeId(nodeId);
    const firstRelatedAsset = currentAssets.find((asset) => asset.nodeIds.includes(nodeId));
    if (firstRelatedAsset) setSelectedAssetId(firstRelatedAsset.id);
  }

  function openThread(threadId: string) {
    const thread = threads.find((item) => item.id === threadId);
    if (!thread) return;
    setActiveThreadId(thread.id);
    focusNode(thread.contextNodeId);
    if (thread.compareTargetId) setCompareTargetId(thread.compareTargetId);
    if (thread.history[0]?.highlightAssetIds[0]) setSelectedAssetId(thread.history[0].highlightAssetIds[0]);
    setPage('thread');
  }

  function createThread(mode: 'orient' | 'diagnose' | 'compare', contextNodeId = selectedNodeId, nextCompareTargetId?: string) {
    const compareId = mode === 'compare' ? nextCompareTargetId ?? compareTargetId : undefined;
    const thread = createThreadRecord(mode, contextNodeId, compareId);
    setThreads((current) => [thread, ...current]);
    setActiveThreadId(thread.id);
    setPage('thread');
    focusNode(contextNodeId);
    if (compareId) setCompareTargetId(compareId);
    return thread.id;
  }

  function registerRun(thread: ThreadRecord, status: RunStatus) {
    const summary = thread.title;
    setRecentRuns((current) => [
      {
        id: `${thread.id}-${Date.now()}`,
        threadId: thread.id,
        threadTitle: thread.title,
        mode: thread.mode,
        contextNodeId: thread.contextNodeId,
        compareTargetId: thread.compareTargetId,
        status,
        summary,
        at: new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
      },
      ...current
    ].slice(0, 8));
  }

  function startThreadRun(threadId: string) {
    const thread = threads.find((item) => item.id === threadId);
    if (!thread) return;
    if (activeRunStatuses.includes(thread.status as (typeof activeRunStatuses)[number])) return;

    const node = nodeById[thread.contextNodeId];
    const compareNode = thread.compareTargetId ? nodeById[thread.compareTargetId] : undefined;
    clearThreadTimers(threadId);
    replaceThread(threadId, (current) => ({
      ...current,
      status: 'preparing',
      statusMessage: `${modeLabel[current.mode]} run 已提交，正在准备结构上下文、关系资产与证据锚点。`,
      updatedAt: new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
    }));

    const phasePlan: [RunStatus, string, number][] = [
      ['generating', '正在根据手工 seed 组织 heavy run，地图浏览与证据查看仍然开放。', 700],
      ['streaming', '正在输出“候选 + 证据 + 下一步”；该线程的新 heavy action 仍然锁定。', 1500],
      ['finalizing', '正在把结构化输出写回线程历史，并同步高亮相关关系资产。', 2400]
    ];

    timersRef.current[threadId] = phasePlan.map(([status, message, delay]) =>
      window.setTimeout(() => {
        replaceThread(threadId, (current) => ({
          ...current,
          status,
          statusMessage: message,
          updatedAt: new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
        }));
      }, delay)
    );

    const finishTimer = window.setTimeout(() => {
      const output = buildStructuredOutput(thread.mode, node, currentAssets, compareNode);
      replaceThread(threadId, (current) => ({
        ...current,
        status: 'done',
        statusMessage: '本轮 heavy run 已完成；该线程重新开放新的 heavy action。',
        history: [output, ...current.history],
        updatedAt: new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
      }));
      registerRun(thread, 'done');
      setActiveThreadId(threadId);
      setPage('thread');
      if (output.highlightAssetIds[0]) setSelectedAssetId(output.highlightAssetIds[0]);
    }, 3400);
    timersRef.current[threadId].push(finishTimer);
  }

  function spawnThreadAndRun(mode: 'orient' | 'diagnose' | 'compare', contextNodeId = selectedNodeId, nextCompareTargetId?: string) {
    const threadId = createThread(mode, contextNodeId, nextCompareTargetId);
    window.setTimeout(() => startThreadRun(threadId), 0);
  }

  function cancelActiveThreadRun() {
    clearThreadTimers(activeThread.id);
    replaceThread(activeThread.id, (current) => ({
      ...current,
      status: 'cancelled',
      statusMessage: '本轮已取消。未完成内容不会冒充最终结果；可 retry 或另开线程继续。',
      updatedAt: new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
    }));
    registerRun(activeThread, 'cancelled');
  }

  function answerTraining(choiceId: string) {
    const isCorrect = selectedTrainingCase.correctChoiceId === choiceId;
    setTrainingFeedback({
      caseId: selectedTrainingCase.id,
      correct: isCorrect,
      explanation: `${isCorrect ? '回答正确。' : '回答偏离。'} ${selectedTrainingCase.explanation}`
    });
    const remediationTarget = (isCorrect ? selectedTrainingCase.choices.find((choice) => choice.id === choiceId)?.targetNodeId : selectedTrainingCase.remediationNodeIds[0]) ?? selectedTrainingCase.remediationNodeIds[0];
    if (remediationTarget) {
      focusNode(remediationTarget);
      setPage('map');
    }
  }

  return (
    <div className="app-shell">
      <header className="top-bar">
        <div>
          <div className="eyebrow">ISMISM scoped v1 / MVP</div>
          <h1>理论工作台</h1>
        </div>
        <div className="top-meta">
          <div>
            <span className="meta-label">当前页</span>
            <strong>{pages.find((entry) => entry.id === page)?.label}</strong>
          </div>
          <div>
            <span className="meta-label">活跃线程</span>
            <strong>{activeThread.title}</strong>
          </div>
          <div>
            <span className="meta-label">Run 状态</span>
            <strong className={`status-pill ${statusTone(activeThread.status)}`}>{activeThread.status}</strong>
          </div>
        </div>
      </header>

      <aside className="primary-rail card">
        <div className="rail-title">Primary Rail</div>
        {pages.map((entry) => (
          <button key={entry.id} className={`rail-button ${page === entry.id ? 'active' : ''}`} onClick={() => setPage(entry.id)}>
            {entry.label}
          </button>
        ))}
      </aside>

      <ContextRail selectedNode={selectedNode} threads={threadSummaries} activeThreadId={activeThread.id} onOpenThread={openThread} />

      <main className="main-canvas card">
        {page === 'home' && (
          <HomeView threadsCount={threads.length} recentRuns={recentRuns} currentAssets={currentAssets} onOpenThread={openThread} onGoMap={() => setPage('map')} />
        )}
        {page === 'map' && (
          <MapView
            mapViewMode={mapViewMode}
            onChangeMapView={setMapViewMode}
            macroGroups={macroGroups}
            selectedNodeId={selectedNodeId}
            selectedNode={selectedNode}
            selectedNodeAssets={selectedNodeAssets}
            currentAssets={currentAssets}
            selectedCompareTargetId={compareTargetId}
            selectedCompareTarget={selectedCompareTarget}
            suggestedCompareNodeIds={suggestedCompareNodeIds}
            selectedNodeEvidenceIds={selectedNodeEvidenceIds}
            highlightedAssetIds={highlightedAssetIds}
            activeThreadLocked={activeThreadLocked}
            dimensionLens={dimensionLens}
            learningSignals={{
              totalCases: manualSeedPack.trainingCases.length,
              draftAssets: currentAssets.filter((asset) => asset.status === 'draft').length,
              reviewedAssets: currentAssets.filter((asset) => asset.status === 'reviewed').length,
              recommendedTraining: unique([selectedNodeId, ...selectedNodeAssets.flatMap((asset) => asset.recommendedJumps)]).slice(0, 4)
            }}
            onFocusNode={focusNode}
            onSelectCompareTarget={setCompareTargetId}
            onSelectAsset={setSelectedAssetId}
            onStartThread={(mode) => spawnThreadAndRun(mode)}
            onStartCompareThread={() => spawnThreadAndRun('compare', selectedNodeId, compareTargetId)}
          />
        )}
        {page === 'thread' && (
          <ThreadView
            activeThread={activeThread}
            threadSummaries={threadSummaries}
            activeThreadLocked={activeThreadLocked}
            currentAssets={currentAssets}
            onRunActiveThread={() => startThreadRun(activeThread.id)}
            onCancelActiveThread={cancelActiveThreadRun}
            onDuplicateThread={() => spawnThreadAndRun(activeThread.mode, activeThread.contextNodeId, activeThread.compareTargetId)}
            onOpenThread={openThread}
            onFocusNode={focusNode}
            onSelectAsset={setSelectedAssetId}
          />
        )}
        {page === 'training' && (
          <TrainingView
            selectedTrainingCase={selectedTrainingCase}
            selectedTrainingCaseId={selectedTrainingCaseId}
            trainingFeedback={trainingFeedback}
            onSelectCase={(caseId: string) => {
              setSelectedTrainingCaseId(caseId);
              setTrainingFeedback(null);
            }}
            onAnswer={(_caseItem, choiceId: string) => answerTraining(choiceId)}
            onGoMap={() => setPage('map')}
          />
        )}
        {page === 'review' && (
          <ReviewView
            reviewQueue={reviewQueue}
            selectedAsset={selectedAsset}
            selectedAssetId={selectedAssetId}
            reviewNotes={reviewNotes}
            onSelectAsset={setSelectedAssetId}
            onPromoteAsset={(assetId: string, status: AssetStatus) => setAssetStatusMap((current) => ({ ...current, [assetId]: status }))}
            onEditReviewNote={(assetId: string, value: string) => setReviewNotes((current) => ({ ...current, [assetId]: value }))}
          />
        )}
      </main>

      <InsightPanel selectedAsset={selectedAsset} currentAssets={currentAssets} highlightedAssetIds={highlightedAssetIds} evidenceIds={evidenceForSelection} onSelectAsset={setSelectedAssetId} />

      <footer className="run-dock card">
        <div>
          <div className="panel-title">Run Dock</div>
          <div className="muted">{activeThread.statusMessage}</div>
        </div>
        <div className="dock-meta wrap">
          <span className={`status-pill ${statusTone(activeThread.status)}`}>{activeThread.status}</span>
          <span>{activeThreadLocked ? '当前活跃线程已锁定新的 heavy action' : '当前活跃线程可接受新的 heavy action'}</span>
        </div>
      </footer>
    </div>
  );
}

export default App;
