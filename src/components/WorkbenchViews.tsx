import { manualSeedPack } from '../data/manualSeed';
import type { AssetStatus, DimensionLens, NodeSeed, RelationAsset, StructuredOutput, ThemeProfile, TrainingCase } from '../types';
import type { MapViewMode, RunSummary, ThreadRecord } from '../appModel';
import { mapViewOptions } from '../appModel';
import { evidenceById, modeLabel, nodeById, unique } from '../workbench';

export function HomeView({
  threadsCount,
  recentRuns,
  currentAssets,
  onOpenThread,
  onGoMap
}: {
  threadsCount: number;
  recentRuns: RunSummary[];
  currentAssets: RelationAsset[];
  onOpenThread: (threadId: string) => void;
  onGoMap: () => void;
}) {
  return (
    <section className="page-section">
      <div className="page-header">
        <div>
          <div className="eyebrow">Workbench Home</div>
          <h2>种子驱动工作台首页</h2>
        </div>
        <button className="ghost-button" onClick={onGoMap}>
          进入地图
        </button>
      </div>
      <div className="stat-grid">
        <MetricCard title="节点骨架" value={`${manualSeedPack.nodes.filter((node) => node.type === 'spine').length} 个二级核心节点`} description="以 16 个二级核心节点 + 方法节点 + 4 大主部组成地图主骨架。" />
        <MetricCard title="关系资产" value={`${currentAssets.length} 个`} description="优先保留 boundary / route / tension / mediation，而不是先堆节点摘要。" />
        <MetricCard title="本地线程" value={`${threadsCount} 条`} description="线程现在是工作台一级对象，可独立切换与回看。" />
      </div>
      <div className="two-col-grid">
        <div className="card inset-card">
          <div className="panel-title">推荐继续点</div>
          <ul className="bullet-list">
            <li>主路线：{currentAssets.find((asset) => asset.id === 'asset-route-1-2-3-4')?.title}</li>
            <li>桥接路线：{currentAssets.find((asset) => asset.id === 'asset-route-2-3-3-1-3-4')?.title}</li>
            <li>实践过渡：{currentAssets.find((asset) => asset.id === 'asset-route-4-1-4-3')?.title}</li>
          </ul>
        </div>
        <div className="card inset-card">
          <div className="panel-title">最近线程活动</div>
          <div className="stack-sm compact-stack">
            {recentRuns.length === 0 ? (
              <div className="muted">先从地图新开一条 orient / diagnose / compare 线程，首页会显示最近运行。</div>
            ) : (
              recentRuns.map((run) => (
                <button key={run.id} className="history-card" onClick={() => onOpenThread(run.threadId)}>
                  <strong>{run.summary}</strong>
                  <div className="muted">{modeLabel[run.mode]} · {run.at} · {run.status}</div>
                </button>
              ))
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

export function MapView({
  mapViewMode,
  onChangeMapView,
  macroGroups,
  selectedNodeId,
  selectedNode,
  selectedNodeAssets,
  currentAssets,
  selectedCompareTargetId,
  selectedCompareTarget,
  suggestedCompareNodeIds,
  selectedNodeEvidenceIds,
  highlightedAssetIds,
  activeThreadLocked,
  dimensionLens,
  learningSignals,
  onFocusNode,
  onSelectCompareTarget,
  onSelectAsset,
  onStartThread,
  onStartCompareThread
}: {
  mapViewMode: MapViewMode;
  onChangeMapView: (mode: MapViewMode) => void;
  macroGroups: { macro: NodeSeed; children: NodeSeed[] }[];
  selectedNodeId: string;
  selectedNode: NodeSeed;
  selectedNodeAssets: RelationAsset[];
  currentAssets: RelationAsset[];
  selectedCompareTargetId?: string;
  selectedCompareTarget?: NodeSeed;
  suggestedCompareNodeIds: string[];
  selectedNodeEvidenceIds: string[];
  highlightedAssetIds: string[];
  activeThreadLocked: boolean;
  dimensionLens: DimensionLens;
  learningSignals: { totalCases: number; draftAssets: number; reviewedAssets: number; recommendedTraining: string[] };
  onFocusNode: (nodeId: string) => void;
  onSelectCompareTarget: (nodeId: string) => void;
  onSelectAsset: (assetId: string) => void;
  onStartThread: (mode: 'orient' | 'diagnose') => void;
  onStartCompareThread: () => void;
}) {
  const selectedThemeProfile = manualSeedPack.themeProfiles[selectedNodeId];

  return (
    <section className="page-section">
      <div className="page-header">
        <div>
          <div className="eyebrow">Map Workspace</div>
          <h2>分层地图主入口</h2>
        </div>
        <div className="stack-row wrap">
          <button className="primary-button" onClick={() => onStartThread('orient')}>
            新开导学线程
          </button>
          <button className="secondary-button" onClick={() => onStartThread('diagnose')}>
            新开诊断线程
          </button>
          <button className="secondary-button" disabled={!selectedCompareTargetId || selectedCompareTargetId === selectedNodeId} onClick={onStartCompareThread}>
            新开比较线程
          </button>
        </div>
      </div>
      <div className="inline-notice">
        当前活跃线程 {activeThreadLocked ? '已锁定 heavy run，但你仍可以从地图新开另一条线程。' : '空闲，可继续新开线程或切回当前线程。'}
      </div>
      <ThemeFocusGallery selectedNodeId={selectedNodeId} onFocusNode={onFocusNode} />
      {selectedThemeProfile && <ThemeProfilePanel profile={selectedThemeProfile} onFocusNode={onFocusNode} />}
      <div className="view-switcher">
        {mapViewOptions.map((view) => (
          <button key={view.id} className={`view-pill ${mapViewMode === view.id ? 'active' : ''}`} onClick={() => onChangeMapView(view.id)}>
            {view.label}
          </button>
        ))}
      </div>
      <DimensionLensPanel node={selectedNode} lens={dimensionLens} />
      {mapViewMode === 'structure' && (
        <>
          <div className="map-grid">
            {macroGroups.map(({ macro, children }) => (
              <div key={macro.id} className={`map-column ${selectedNode.parentId === macro.id || selectedNode.id === macro.id ? 'is-highlighted' : ''}`}>
                <button className="macro-node" onClick={() => onFocusNode(macro.id)}>
                  {macro.shortTitle}
                </button>
                <div className="spine-list">
                  {children.map((node) => {
                    const relatedAssetCount = currentAssets.filter((asset) => asset.nodeIds.includes(node.id)).length;
                    const suggestedCompare = currentAssets.filter((asset) => asset.type === 'boundary' && asset.nodeIds.includes(node.id)).length;
                    return (
                      <button key={node.id} className={`spine-node ${selectedNodeId === node.id ? 'active' : ''}`} onClick={() => onFocusNode(node.id)}>
                        <span>{node.shortTitle}</span>
                        <small>{relatedAssetCount} 资产 / {suggestedCompare} compare 候选</small>
                      </button>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
          <NodeSupportPanels
            selectedNode={selectedNode}
            selectedNodeAssets={selectedNodeAssets}
            highlightedAssetIds={highlightedAssetIds}
            selectedNodeEvidenceIds={selectedNodeEvidenceIds}
            onFocusNode={onFocusNode}
            onSelectAsset={onSelectAsset}
          />
        </>
      )}

      {mapViewMode === 'learning' && (
        <div className="three-col-grid">
          <div className="card inset-card">
            <div className="panel-title">学习信号</div>
            <ul className="bullet-list">
              <li>训练案例：{learningSignals.totalCases}</li>
              <li>draft 资产：{learningSignals.draftAssets}</li>
              <li>reviewed 资产：{learningSignals.reviewedAssets}</li>
            </ul>
          </div>
          <div className="card inset-card">
            <div className="panel-title">推荐补课入口</div>
            <div className="stack-sm compact-stack">
              {learningSignals.recommendedTraining.map((nodeId) => (
                <button key={nodeId} className="ghost-button align-left" onClick={() => onFocusNode(nodeId)}>
                  {nodeById[nodeId]?.shortTitle}
                </button>
              ))}
            </div>
          </div>
          <div className="card inset-card">
            <div className="panel-title">当前节点为什么值得学</div>
            <p>{selectedNode.whyImportant}</p>
            <p className="muted">学习视图强调：先修、混淆、回退与补结构。</p>
          </div>
        </div>
      )}

      {mapViewMode === 'diagnose' && (
        <div className="three-col-grid diagnose-grid">
          <div className="card inset-card">
            <div className="panel-title">当前判定对象</div>
            <h3>{selectedNode.title}</h3>
            <p>{selectedNode.summary}</p>
            <p className="muted">判定视图强调：候选、证据、排除链、不确定性。</p>
          </div>
          <div className="card inset-card">
            <div className="panel-title">候选关系对象</div>
            <div className="stack-sm compact-stack">
              {selectedNodeAssets.length === 0 ? (
                <div className="muted">当前节点还没有足够的 relation-first 资产。</div>
              ) : (
                selectedNodeAssets.map((asset) => (
                  <button key={asset.id} className={`link-card ${highlightedAssetIds.includes(asset.id) ? 'selected' : ''}`} onClick={() => onSelectAsset(asset.id)}>
                    <span>{asset.title}</span>
                    <small>{asset.summary}</small>
                  </button>
                ))
              )}
            </div>
          </div>
          <div className="card inset-card">
            <div className="panel-title">证据节点</div>
            <div className="stack-sm compact-stack">
              {selectedNodeEvidenceIds.slice(0, 6).map((evidenceId) => {
                const evidence = evidenceById[evidenceId];
                if (!evidence) return null;
                return (
                  <div key={evidence.id} className="evidence-card compact-evidence">
                    <strong>{evidence.title}</strong>
                    <small>{evidence.pageLabel}</small>
                    <p>{evidence.summary}</p>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {mapViewMode === 'compare' && (
        <div className="compare-board">
          <div className="card inset-card compare-side">
            <div className="panel-title">对象 A</div>
            <h3>{selectedNode.title}</h3>
            <p>{selectedNode.summary}</p>
          </div>
          <div className="card inset-card compare-middle">
            <div className="panel-title">边界 / 张力 / 中介</div>
            <div className="stack-sm compact-stack">
              {currentAssets
                .filter((asset) => selectedCompareTarget && asset.nodeIds.includes(selectedNode.id) && asset.nodeIds.includes(selectedCompareTarget.id))
                .map((asset) => (
                  <button key={asset.id} className="link-card selected" onClick={() => onSelectAsset(asset.id)}>
                    <span>{asset.title}</span>
                    <small>{asset.summary}</small>
                  </button>
                ))}
            </div>
          </div>
          <div className="card inset-card compare-side">
            <div className="panel-title">对象 B</div>
            {selectedCompareTarget ? (
              <>
                <h3>{selectedCompareTarget.title}</h3>
                <p>{selectedCompareTarget.summary}</p>
              </>
            ) : (
              <p className="muted">先从 compare 候选中选择一个对象。</p>
            )}
          </div>
          <div className="card inset-card compare-candidates">
            <div className="panel-title">推荐 compare 对象</div>
            <div className="stack-sm compact-stack">
              {suggestedCompareNodeIds.map((nodeId) => (
                <button key={nodeId} className={`link-card ${selectedCompareTargetId === nodeId ? 'selected' : ''}`} onClick={() => onSelectCompareTarget(nodeId)}>
                  <span>{nodeById[nodeId].shortTitle}</span>
                  <small>{nodeById[nodeId].summary}</small>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      {mapViewMode === 'scholar' && (
        <div className="three-col-grid">
          <div className="card inset-card">
            <div className="panel-title">待审核资产</div>
            <div className="stack-sm compact-stack">
              {currentAssets
                .filter((asset) => asset.status !== 'canonical' && asset.nodeIds.includes(selectedNode.id))
                .map((asset) => (
                  <button key={asset.id} className={`link-card ${highlightedAssetIds.includes(asset.id) ? 'selected' : ''}`} onClick={() => onSelectAsset(asset.id)}>
                    <span>{asset.title}</span>
                    <span className={`status-chip chip-${asset.status}`}>{asset.status}</span>
                  </button>
                ))}
            </div>
          </div>
          <div className="card inset-card">
            <div className="panel-title">学者视图关注</div>
            <ul className="bullet-list">
              <li>优先看 disputed / draft / reviewed 的边界资产。</li>
              <li>确认哪类对象能进入地图主视图，哪类只留在工作台视图。</li>
              <li>检查 relation-first 资产是否足够支撑 thread / training / review 闭环。</li>
            </ul>
          </div>
          <div className="card inset-card">
            <div className="panel-title">相关证据</div>
            <div className="stack-sm compact-stack">
              {selectedNodeEvidenceIds.slice(0, 4).map((evidenceId) => {
                const evidence = evidenceById[evidenceId];
                if (!evidence) return null;
                return (
                  <div key={evidence.id} className="evidence-card compact-evidence">
                    <strong>{evidence.title}</strong>
                    <p>{evidence.summary}</p>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </section>
  );
}


function ThemeFocusGallery({ selectedNodeId, onFocusNode }: { selectedNodeId: string; onFocusNode: (nodeId: string) => void }) {
  const featuredIds = ['node-1-1', 'node-2-3', 'node-3-4', 'node-4-1'];
  return (
    <div className="theme-gallery">
      {featuredIds.map((id) => {
        const profile = manualSeedPack.themeProfiles[id];
        if (!profile) return null;
        return (
          <button key={id} className={`theme-card ${selectedNodeId === id ? 'selected' : ''}`} onClick={() => onFocusNode(id)}>
            <div className="panel-subtitle">四维专题</div>
            <strong>{nodeById[id].shortTitle}</strong>
            <p>{profile.summary}</p>
          </button>
        );
      })}
    </div>
  );
}

function ThemeProfilePanel({ profile, onFocusNode }: { profile: ThemeProfile; onFocusNode: (nodeId: string) => void }) {
  return (
    <div className="card inset-card theme-profile">
      <div className="panel-title">专题深描卡</div>
      <h3>{profile.title}</h3>
      <p>{profile.summary}</p>
      <p className="muted">{profile.whySelected}</p>
      <div className="dimension-grid">
        <ThemeDimensionCard title="场域论" data={profile.dimensions.field} />
        <ThemeDimensionCard title="本体论" data={profile.dimensions.ontology} />
        <ThemeDimensionCard title="认识论" data={profile.dimensions.epistemology} />
        <ThemeDimensionCard title="目的论" data={profile.dimensions.teleology} />
      </div>
      <div className="three-col-grid">
        <div className="card inset-card">
          <div className="panel-title">高频混淆</div>
          <div className="stack-sm compact-stack">
            {profile.confusionPairIds.map((id) => (
              <button key={id} className="ghost-button align-left" onClick={() => onFocusNode(id)}>
                {nodeById[id]?.shortTitle}
              </button>
            ))}
          </div>
        </div>
        <div className="card inset-card">
          <div className="panel-title">对话追问</div>
          <ul className="bullet-list">
            {profile.dialoguePrompts.map((prompt) => (
              <li key={prompt}>{prompt}</li>
            ))}
          </ul>
        </div>
        <div className="card inset-card">
          <div className="panel-title">证据入口</div>
          <div className="stack-sm compact-stack">
            {profile.evidenceIds.map((id) => {
              const evidence = evidenceById[id];
              if (!evidence) return null;
              return (
                <div key={id} className="evidence-card compact-evidence">
                  <strong>{evidence.title}</strong>
                  <p>{evidence.summary}</p>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

function ThemeDimensionCard({ title, data }: { title: string; data: ThemeProfile['dimensions']['field'] }) {
  return (
    <div className="theme-dimension-card">
      <div className="panel-subtitle">{title}</div>
      <p><strong>命题：</strong>{data.thesis}</p>
      <p><strong>识别：</strong>{data.cue}</p>
      <p><strong>风险：</strong>{data.risk}</p>
    </div>
  );
}

function NodeSupportPanels({
  selectedNode,
  selectedNodeAssets,
  highlightedAssetIds,
  selectedNodeEvidenceIds,
  onFocusNode,
  onSelectAsset
}: {
  selectedNode: NodeSeed;
  selectedNodeAssets: RelationAsset[];
  highlightedAssetIds: string[];
  selectedNodeEvidenceIds: string[];
  onFocusNode: (nodeId: string) => void;
  onSelectAsset: (assetId: string) => void;
}) {
  return (
    <div className="two-col-grid">
      <div className="card inset-card">
        <div className="panel-title">当前节点关系资产</div>
        <div className="stack-sm">
          {selectedNodeAssets.map((asset) => (
            <button key={asset.id} className={`link-card ${highlightedAssetIds.includes(asset.id) ? 'selected' : ''}`} onClick={() => onSelectAsset(asset.id)}>
              <span>{asset.title}</span>
              <span className={`status-chip chip-${asset.status}`}>{asset.status}</span>
            </button>
          ))}
        </div>
      </div>
      <div className="card inset-card">
        <div className="panel-title">推荐跳转与证据</div>
        <div className="stack-sm compact-stack">
          {unique([...selectedNodeAssets.flatMap((asset) => asset.recommendedJumps), selectedNode.id]).slice(0, 4).map((jumpId) => (
            <button key={jumpId} className="ghost-button align-left" onClick={() => onFocusNode(jumpId)}>
              {nodeById[jumpId]?.shortTitle ?? jumpId}
            </button>
          ))}
          {selectedNodeEvidenceIds.slice(0, 3).map((evidenceId) => {
            const evidence = evidenceById[evidenceId];
            if (!evidence) return null;
            return (
              <div key={evidence.id} className="evidence-card compact-evidence">
                <strong>{evidence.title}</strong>
                <small>{evidence.pageLabel}</small>
                <p>{evidence.summary}</p>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

function DimensionLensPanel({ node, lens }: { node: NodeSeed; lens: DimensionLens }) {
  return (
    <div className="card inset-card dimension-panel">
      <div className="panel-title">四维镜 · {node.shortTitle}</div>
      <div className="dimension-grid">
        <DimensionCard title="场域论" body={lens.field} />
        <DimensionCard title="本体论" body={lens.ontology} />
        <DimensionCard title="认识论" body={lens.epistemology} />
        <DimensionCard title="目的论" body={lens.teleology} />
      </div>
      <div className="dimension-emphasis">当前强调：{lens.emphasis}</div>
    </div>
  );
}

function DimensionCard({ title, body }: { title: string; body: string }) {
  return (
    <div className="dimension-card">
      <div className="panel-subtitle">{title}</div>
      <p>{body}</p>
    </div>
  );
}

function ModeTemplate({ mode, currentNode, compareNode }: { mode: 'orient' | 'diagnose' | 'compare'; currentNode: NodeSeed; compareNode?: NodeSeed }) {
  if (mode === 'orient') {
    return (
      <ul className="bullet-list">
        <li>先把 {currentNode.shortTitle} 放回主干或方法轴，避免直接掉入聊天式长解释。</li>
        <li>优先看 route / boundary 资产，而不是先把节点摘要扩写到很长。</li>
        <li>导学页应给出“不推荐先碰什么”和“下一步跳哪里”。</li>
      </ul>
    );
  }

  if (mode === 'diagnose') {
    return (
      <ul className="bullet-list">
        <li>保留至少一个主候选和一个边界/排除理由。</li>
        <li>主结果必须把 evidence pack 和 uncertainty 一并显示。</li>
        <li>如果关系资产还是 draft，结果必须保留 provisional 语义。</li>
      </ul>
    );
  }

  return (
    <ul className="bullet-list">
      <li>当前比较对象：{currentNode.shortTitle}{compareNode ? ` ↔ ${compareNode.shortTitle}` : '（待补）'}。</li>
      <li>比较页优先显示边界卡 / 张力卡，而不是两段摘要并排。</li>
      <li>比较后应能跳回地图并继续高亮相关节点与关系资产。</li>
    </ul>
  );
}

function StructuredOutputView({
  output,
  assets,
  onJump,
  onSelectAsset
}: {
  output: StructuredOutput;
  assets: RelationAsset[];
  onJump: (nodeId: string) => void;
  onSelectAsset: (assetId: string) => void;
}) {
  const renderedAssets = assets.filter((asset) => output.highlightAssetIds.includes(asset.id));
  const compareTarget = output.compareTargetId ? nodeById[output.compareTargetId] : undefined;

  return (
    <div className="output-stack">
      <section className="card inset-card">
        <div className="panel-title">Task Summary</div>
        <p>{output.taskSummary}</p>
      </section>
      <section className="card inset-card">
        <div className="panel-title">Object Summary</div>
        <p>{output.objectSummary}</p>
        {compareTarget && <div className="muted">当前 compare 对照：{compareTarget.shortTitle}</div>}
      </section>
      <section className="card inset-card">
        <div className="panel-title">Primary Output</div>
        <p>{output.primaryOutput}</p>
      </section>
      <section className="three-col-grid">
        <div className="card inset-card">
          <div className="panel-title">Candidate Outputs</div>
          <ul className="bullet-list">
            {output.candidateOutputs.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
        <div className="card inset-card">
          <div className="panel-title">Relation Findings</div>
          <ul className="bullet-list">
            {output.relationFindings.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
        <div className="card inset-card">
          <div className="panel-title">Uncertainty</div>
          <p>{output.uncertainty}</p>
        </div>
      </section>
      <section className="card inset-card">
        <div className="panel-title">Rendered Relation Assets</div>
        <div className="asset-grid">
          {renderedAssets.map((asset) => (
            <button key={asset.id} className="asset-card align-left" onClick={() => onSelectAsset(asset.id)}>
              <div className="asset-header">
                <strong>{asset.title}</strong>
                <span className={`status-chip chip-${asset.status}`}>{asset.status}</span>
              </div>
              <p>{asset.summary}</p>
            </button>
          ))}
        </div>
      </section>
      <section className="card inset-card">
        <div className="panel-title">Recommended Jumps</div>
        <div className="stack-row wrap">
          {output.recommendedJumps.map((nodeId) => (
            <button key={nodeId} className="ghost-button" onClick={() => onJump(nodeId)}>
              {nodeById[nodeId]?.shortTitle ?? nodeId}
            </button>
          ))}
        </div>
      </section>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="metric-row">
      <span className="meta-label">{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function MetricCard({ title, value, description }: { title: string; value: string; description: string }) {
  return (
    <div className="card inset-card">
      <div className="panel-title">{title}</div>
      <div className="metric-card-value">{value}</div>
      <p className="muted">{description}</p>
    </div>
  );
}

export function ThreadView({
  activeThread,
  threadSummaries,
  activeThreadLocked,
  currentAssets,
  onRunActiveThread,
  onCancelActiveThread,
  onDuplicateThread,
  onOpenThread,
  onFocusNode,
  onSelectAsset
}: {
  activeThread: ThreadRecord;
  threadSummaries: ThreadRecord[];
  activeThreadLocked: boolean;
  currentAssets: RelationAsset[];
  onRunActiveThread: () => void;
  onCancelActiveThread: () => void;
  onDuplicateThread: () => void;
  onOpenThread: (threadId: string) => void;
  onFocusNode: (nodeId: string) => void;
  onSelectAsset: (assetId: string) => void;
}) {
  return (
    <section className="page-section">
      <div className="page-header">
        <div>
          <div className="eyebrow">Thread Workspace</div>
          <h2>通用线程工作区</h2>
        </div>
        <div className="stack-row wrap">
          <button className="primary-button" disabled={activeThreadLocked} onClick={onRunActiveThread}>
            在当前线程重跑
          </button>
          <button className="danger-button" disabled={!activeThreadLocked} onClick={onCancelActiveThread}>
            Cancel
          </button>
          <button className="secondary-button" onClick={onDuplicateThread}>
            另开同配置线程
          </button>
        </div>
      </div>
      <div className={`inline-notice ${statusTone(activeThread.status)}`}>
        <strong>{activeThread.status}</strong> · {activeThread.statusMessage}
      </div>
      <div className="thread-context-bar wrap">
        <span>Thread：{activeThread.title}</span>
        <span>Mode：{modeLabel[activeThread.mode]}</span>
        <span>主对象：{nodeById[activeThread.contextNodeId].shortTitle}</span>
        {activeThread.compareTargetId && <span>对照对象：{nodeById[activeThread.compareTargetId]?.shortTitle}</span>}
      </div>
      <div className="three-col-grid">
        <div className="card inset-card">
          <div className="panel-title">活跃线程详情</div>
          <ModeTemplate mode={activeThread.mode} currentNode={nodeById[activeThread.contextNodeId]} compareNode={activeThread.compareTargetId ? nodeById[activeThread.compareTargetId] : undefined} />
        </div>
        <div className="card inset-card">
          <div className="panel-title">线程列表</div>
          <div className="stack-sm compact-stack">
            {threadSummaries.map((thread) => (
              <button key={thread.id} className={`mini-run-card ${thread.id === activeThread.id ? 'selected' : ''}`} onClick={() => onOpenThread(thread.id)}>
                <strong>{thread.title}</strong>
                <small>{thread.updatedAt} · {thread.status}</small>
              </button>
            ))}
          </div>
        </div>
        <div className="card inset-card">
          <div className="panel-title">该线程历史</div>
          <div className="stack-sm compact-stack">
            {activeThread.history.length === 0 ? (
              <div className="muted">当前线程还没有结构化输出。可直接重跑，或从地图新开线程。</div>
            ) : (
              activeThread.history.map((item) => (
                <button key={item.id} className="history-card" onClick={() => { onFocusNode(activeThread.contextNodeId); if (item.highlightAssetIds[0]) onSelectAsset(item.highlightAssetIds[0]); }}>
                  <strong>{modeLabel[item.mode]} · {item.primaryOutput.slice(0, 22)}…</strong>
                  <div className="muted">候选 {item.candidateOutputs.length} · 关系对象 {item.highlightAssetIds.length}</div>
                </button>
              ))
            )}
          </div>
        </div>
      </div>
      {activeThread.history[0] ? (
        <StructuredOutputView output={activeThread.history[0]} assets={currentAssets} onJump={onFocusNode} onSelectAsset={onSelectAsset} />
      ) : (
        <div className="empty-state">
          <p>当前线程还没有结构化输出。你可以在当前线程直接重跑，或从地图新开线程。</p>
        </div>
      )}
    </section>
  );
}

export function TrainingView({
  selectedTrainingCase,
  selectedTrainingCaseId,
  trainingFeedback,
  onSelectCase,
  onAnswer,
  onGoMap
}: {
  selectedTrainingCase: TrainingCase;
  selectedTrainingCaseId: string;
  trainingFeedback: { caseId: string; correct: boolean; explanation: string } | null;
  onSelectCase: (caseId: string) => void;
  onAnswer: (caseItem: TrainingCase, choiceId: string) => void;
  onGoMap: () => void;
}) {
  return (
    <section className="page-section">
      <div className="page-header">
        <div>
          <div className="eyebrow">Training Workspace</div>
          <h2>最小训练闭环</h2>
        </div>
      </div>
      <div className="training-layout">
        <div className="card inset-card">
          <div className="panel-title">题目列表</div>
          {manualSeedPack.trainingCases.map((caseItem) => (
            <button key={caseItem.id} className={`training-item ${selectedTrainingCaseId === caseItem.id ? 'active' : ''}`} onClick={() => onSelectCase(caseItem.id)}>
              <span>{caseItem.title}</span>
              <span className={`status-chip chip-${caseItem.status}`}>{caseItem.status}</span>
            </button>
          ))}
        </div>
        <div className="card inset-card">
          <div className="panel-title">题面</div>
          <h3>{selectedTrainingCase.title}</h3>
          <p>{selectedTrainingCase.prompt}</p>
          <div className="stack-sm">
            {selectedTrainingCase.choices.map((choice) => (
              <button key={choice.id} className="choice-button" onClick={() => onAnswer(selectedTrainingCase, choice.id)}>
                {choice.label}
              </button>
            ))}
          </div>
          {trainingFeedback?.caseId === selectedTrainingCase.id && (
            <div className={`feedback-box ${trainingFeedback.correct ? 'feedback-ok' : 'feedback-warn'}`}>
              <strong>{trainingFeedback.correct ? '回答正确' : '需要补结构'}</strong>
              <p>{trainingFeedback.explanation}</p>
              <button className="ghost-button" onClick={onGoMap}>
                跳回相关结构
              </button>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

export function ReviewView({
  reviewQueue,
  selectedAsset,
  selectedAssetId,
  reviewNotes,
  onSelectAsset,
  onPromoteAsset,
  onEditReviewNote
}: {
  reviewQueue: RelationAsset[];
  selectedAsset: RelationAsset;
  selectedAssetId: string;
  reviewNotes: Record<string, string>;
  onSelectAsset: (assetId: string) => void;
  onPromoteAsset: (assetId: string, status: AssetStatus) => void;
  onEditReviewNote: (assetId: string, value: string) => void;
}) {
  return (
    <section className="page-section">
      <div className="page-header">
        <div>
          <div className="eyebrow">Scholar / Review</div>
          <h2>最小生命周期与审核工作台</h2>
        </div>
      </div>
      <div className="training-layout">
        <div className="card inset-card">
          <div className="panel-title">待处理资产</div>
          {reviewQueue.map((asset) => (
            <button key={asset.id} className={`training-item ${selectedAssetId === asset.id ? 'active' : ''}`} onClick={() => onSelectAsset(asset.id)}>
              <span>{asset.title}</span>
              <span className={`status-chip chip-${asset.status}`}>{asset.status}</span>
            </button>
          ))}
        </div>
        <div className="card inset-card">
          <div className="panel-title">审核动作</div>
          <h3>{selectedAsset.title}</h3>
          <p>{selectedAsset.summary}</p>
          <div className="stack-row wrap">
            <button className="secondary-button" onClick={() => onPromoteAsset(selectedAsset.id, 'reviewed')}>
              标记 reviewed
            </button>
            <button className="primary-button" onClick={() => onPromoteAsset(selectedAsset.id, 'canonical')}>
              升级 canonical
            </button>
            <button className="ghost-button" onClick={() => onPromoteAsset(selectedAsset.id, 'draft')}>
              退回 draft
            </button>
          </div>
          <label className="panel-subtitle" htmlFor="review-note">
            Review note
          </label>
          <textarea id="review-note" className="note-box" value={reviewNotes[selectedAsset.id] ?? ''} onChange={(event) => onEditReviewNote(selectedAsset.id, event.target.value)} />
        </div>
      </div>
    </section>
  );
}

export function ContextRail({
  selectedNode,
  threads,
  activeThreadId,
  onOpenThread
}: {
  selectedNode: NodeSeed;
  threads: ThreadRecord[];
  activeThreadId: string;
  onOpenThread: (threadId: string) => void;
}) {
  return (
    <aside className="context-rail card">
      <div className="panel-title">Context Rail</div>
      <div className="stack-sm">
        <Metric label="种子节点" value={manualSeedPack.nodes.length} />
        <Metric label="关系资产" value={manualSeedPack.relationAssets.length} />
        <Metric label="训练案例" value={manualSeedPack.trainingCases.length} />
      </div>
      <hr />
      <div className="panel-subtitle">当前对象</div>
      <div className="selected-object">
        <strong>{selectedNode.title}</strong>
        <div className={`status-chip chip-${selectedNode.status}`}>{selectedNode.status}</div>
      </div>
      <p className="muted">{selectedNode.summary}</p>
      <div className="panel-subtitle">线程列表</div>
      <div className="stack-sm compact-stack">
        {threads.map((thread) => (
          <button key={thread.id} className={`mini-run-card ${thread.id === activeThreadId ? 'selected' : ''}`} onClick={() => onOpenThread(thread.id)}>
            <strong>{thread.title}</strong>
            <small>{thread.updatedAt} · {thread.status}</small>
          </button>
        ))}
      </div>
      <div className="panel-subtitle">线程纪律</div>
      <ul className="bullet-list">
        <li>锁是线程级的，不是全站级的。</li>
        <li>锁住某条线程时，仍可浏览地图或新开另一条线程。</li>
        <li>结果默认保留候选、证据、关系资产与下一步跳转。</li>
      </ul>
    </aside>
  );
}

export function InsightPanel({
  selectedAsset,
  currentAssets,
  highlightedAssetIds,
  evidenceIds,
  onSelectAsset
}: {
  selectedAsset: RelationAsset;
  currentAssets: RelationAsset[];
  highlightedAssetIds: string[];
  evidenceIds: string[];
  onSelectAsset: (assetId: string) => void;
}) {
  return (
    <aside className="insight-panel card">
      <div className="panel-title">Insight / Evidence Panel</div>
      <h3>{selectedAsset.title}</h3>
      <div className={`status-chip chip-${selectedAsset.status}`}>{selectedAsset.status}</div>
      <p>{selectedAsset.summary}</p>
      <p className="muted">{selectedAsset.whyImportant}</p>
      <div className="panel-subtitle">高亮关系资产</div>
      <div className="stack-sm compact-stack">
        {currentAssets.filter((asset) => highlightedAssetIds.includes(asset.id)).map((asset) => (
          <button key={asset.id} className={`link-card ${selectedAsset.id === asset.id ? 'selected' : ''}`} onClick={() => onSelectAsset(asset.id)}>
            <span>{asset.title}</span>
            <span className={`status-chip chip-${asset.status}`}>{asset.status}</span>
          </button>
        ))}
      </div>
      <div className="panel-subtitle">证据锚点</div>
      <div className="stack-sm">
        {evidenceIds.map((id) => evidenceById[id]).filter(Boolean).map((anchor) => (
          <div key={anchor.id} className="evidence-card">
            <strong>{anchor.title}</strong>
            <div className="muted">{anchor.path}</div>
            <div className="muted">{anchor.pageLabel}</div>
            <p>{anchor.summary}</p>
            <small>锚点摘记：{anchor.excerpt}</small>
          </div>
        ))}
      </div>
    </aside>
  );
}

function statusTone(status: string) {
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
