#!/usr/bin/env python3
"""Build W2 segment cards in bounded batches.

Generate draft segment cards directly from W1 segment manifests + clean markdown.
The cards are designed to be editable by analysts later; therefore this script
produces audit-friendly conservative summaries and explicit uncertainty notes.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K = ROOT / "knowledge"
MANIFESTS = K / "manifests"
SEGMENTS_JSONL = MANIFESTS / "segments.jsonl"
SEGMENT_CARDS = K / "segment-cards"
INDEX_PATH = SEGMENT_CARDS / "index.md"
TEMPLATE = K / "templates" / "segment-card-template.md"
STATE = K / "STATE.md"
LOG = K / "logs" / "operation-log.md"

KEYWORDS = {
    "理论", "主义", "意识形态", "符号", "实践", "主体", "客体", "实体", "历史", "生产",
    "本体", "认识", "方法", "实践主义", "经济", "政治", "伦理", "关系", "精神", "欲望",
    "资本", "阶级", "语言", "辩证", "物质", "知识", "科学", "哲学", "观念", "经验",
    "符号秩序", "场", "真理", "实在", "虚无", "中介", "过渡", "身份", "身体",
    "欲望", "主体化", "客体化", "再生产", "再现", "结构", "文本", "话语"
}

KNOWN_FIGURES = [
    "亚里士多德", "柏拉图", "康德", "马克思", "拉康", "海德格尔", "尼采", "福柯", "德勒兹",
    "德里达", "索绪尔", "叔本华", "黑格尔", "卢梭", "孔德", "斯宾诺莎", "萨特",
]


def read_segments() -> list[dict]:
    records = []
    with SEGMENTS_JSONL.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    records.sort(key=lambda r: int(r["row_id"]))
    return records


def read_template() -> str:
    return TEMPLATE.read_text(encoding="utf-8")


def safe_toc(toc: str) -> str:
    return re.sub(r"[^0-9A-Za-z\-_.]", "_", str(toc))


def card_path(row_id: int, toc_id: str) -> Path:
    return SEGMENT_CARDS / f"{row_id:04d}_{safe_toc(toc_id)}.md"


def collect_existing_cards() -> set[int]:
    rows = set()
    if not SEGMENT_CARDS.exists():
        return rows
    for p in SEGMENT_CARDS.glob("*.md"):
        m = re.match(r"^(\d{4})_", p.name)
        if not m:
            continue
        rows.add(int(m.group(1)))
    return rows


def choose_start_row(rows: list[dict], existing: set[int], start_row: int | None) -> int:
    if start_row is not None:
        return max(1, start_row)
    if not existing:
        return 1
    # start from next missing row after largest processed row
    max_done = max(existing)
    return max_done + 1


def strip_markdown(text: str) -> list[str]:
    lines = text.splitlines()
    out = []
    for line in lines:
        s = line.strip()
        if not s or s.startswith("##"):
            continue
        if s.startswith("- source_pdf") or s.startswith("- page_count"):
            continue
        if s == "---":
            continue
        out.append(s)
    return out


def extract_summary(lines: list[str]) -> str:
    if not lines:
        return "（缺少可提取正文）"
    body = "\n".join(lines)
    # split into sentence-ish chunks
    parts = re.split(r"(?<=[。！？\.!?])", body)
    selected = []
    for p in parts:
        p = p.strip().strip("\n")
        if not p:
            continue
        selected.append(p)
        if sum(len(x) for x in selected) >= 420:
            break
    if not selected:
        return body[:420] + ("..." if len(body) > 420 else "")
    summary = "".join(selected).strip()
    if len(summary) > 800:
        summary = summary[:800] + "..."
    return summary


def extract_lines_excerpt(lines: list[str], max_count=3) -> list[str]:
    out = []
    for i, line in enumerate(lines, start=1):
        if not line or len(line) < 12:
            continue
        t = re.sub(r"\s+", " ", line).strip()
        if t.startswith("##") or t.startswith("- source"):
            continue
        out.append((i, t))
        if len(out) >= max_count:
            break
    return out


def extract_terms(text: str, title: str, path_titles: list[str]) -> list[str]:
    raw_terms = set()
    candidate = re.findall(r"[一-龥]{2,6}|[A-Za-z]{3,}(?:ism|ismism|ism)?", text + " " + title)
    candidate.extend(re.findall(r"[一-龥]{2,8}", " ".join(path_titles)))

    for tok in candidate:
        tok = tok.strip("\u3000 \t")
        if len(tok) < 2:
            continue
        if tok in KEYWORDS or tok.endswith("主义") or tok in {"实在论", "观念论", "形而上学", "形而下学", "实践", "主体", "客体"}:
            raw_terms.add(tok)
    # deterministic top terms by frequency in text
    term_scores = Counter()
    for tok in list(raw_terms):
        if tok in text:
            term_scores[tok] += 2
    if not term_scores:
        for tok in list(KEYWORDS):
            if tok in text:
                term_scores[tok] += 1
    ordered = [t for t, _ in sorted(term_scores.items(), key=lambda kv: (-kv[1], kv[0]))]
    if not ordered:
        ordered = sorted({t for t in raw_terms if len(t) <= 6})[:5]
    return ordered[:12]


def extract_figures(text: str, title: str) -> list[str]:
    found = set()
    s = text + " " + title
    for name in KNOWN_FIGURES:
        if name in s:
            found.add(name)
    # if line explicitly includes "代表人物"
    reps = re.findall(r"代表人物[^，。；;:\n]*", text)
    if reps:
        found.update([r.replace("代表人物", "").strip() for r in reps])
    return sorted(found)[:12]


def position_hints(seg: dict) -> list[str]:
    ma = seg.get("matrix_axes", {})
    hints = []
    for axis in ["field", "ontology", "epistemology", "teleology"]:
        v = ma.get(axis)
        if v is None:
            continue
        hints.append(f"- {axis}: {v}")
    # use title-level relationship
    if ma.get("is_four_axis_position"):
        hints.append("- 该段位于 4 维矩阵中的一级定位节点")
    else:
        hints.append("- 该段为补充/复写/重复位（非标准矩阵位置）")
    return hints


def build_card_content(seg: dict, line_sample: list[tuple[int, str]], summary: str) -> str:
    ts = datetime.now().strftime("%Y-%m-%d")
    template = read_template()

    title = seg.get("title", "")
    row_id = seg["row_id"]
    toc_id = seg["toc_id"]
    segid = seg["segment_id"]
    pa = seg.get("path_titles", [])
    mp = seg.get("page_start")
    me = seg.get("page_end_inferred")
    mclean = seg["source_paths"]["clean_md_relpath"]
    mraw = seg["source_paths"].get("raw_md_relpath", "")
    sha = seg.get("clean_md", {}).get("sha256", "")

    raw_terms = extract_terms(seg.get("clean_md", {}).get("text", "") if isinstance(seg.get("clean_md", {}).get("text", None), str) else Path(ROOT / mclean).read_text(encoding="utf-8", errors="ignore"),
                               title,
                               pa if isinstance(pa, list) else [])

    # Since clean_md.text is not stored in manifest, re-read file directly
    text = Path(ROOT / mclean).read_text(encoding="utf-8", errors="ignore")
    raw_lines = strip_markdown(text)
    summary = summary if summary else extract_summary(raw_lines)
    core_terms = extract_terms(text, title, pa if isinstance(pa, list) else [])
    figures = extract_figures(text, title)

    anchors = []
    for ln_no, ln in line_sample[:3]:
        snippet = ln.strip()
        if len(snippet) > 130:
            snippet = snippet[:127] + "..."
        anchors.append(f"- line {ln_no}: {snippet}")

    card = template
    card = card.replace("segment_id:", f"segment_id: {segid}", 1)
    card = card.replace("toc_id:", f"toc_id: {toc_id}", 1)
    card = card.replace("title:", f"title: {title}", 1)
    card = card.replace("created:", f"created: {ts}", 1)
    card = card.replace("updated:", f"updated: {ts}", 1)
    card = card.replace("source_clean_path:", f"source_clean_path: `{mclean}`", 1)

    card = card.replace("## Metadata\n", "## Metadata\n")
    card = card.replace("- segment_id:", f"- segment_id: {segid}", 1)
    card = card.replace("- row_id:", f"- row_id: {row_id}", 1)
    card = card.replace("- toc_id:", f"- toc_id: {toc_id}", 1)
    card = card.replace("- tree_level:", f"- tree_level: {seg.get('toc_depth', '')}", 1)
    card = card.replace("- parent_toc_id:", f"- parent_toc_id: {seg.get('parent_toc_id', '')}", 1)
    card = card.replace("- path_titles:", f"- path_titles: {pa}", 1)
    card = card.replace("- page_start:", f"- page_start: {mp}", 1)
    card = card.replace("- page_end:", f"- page_end: {me}", 1)
    card = card.replace("- raw_md_path:", f"- raw_md_path: {mraw}", 1)
    card = card.replace("- clean_md_path:", f"- clean_md_path: {mclean}", 1)
    card = card.replace("- clean_sha256:", f"- clean_sha256: {sha}", 1)

    # Replace section placeholders once
    card = card.replace("## Faithful Summary\n\n", f"## Faithful Summary\n\n{summary}\n\n")
    card = card.replace("## Core Terms\n\n", f"## Core Terms\n\n{', '.join(core_terms) if core_terms else '待整理（需人工补全）'}\n\n")

    propositions = []
    if core_terms:
        propositions.append(f"- 核心命题1：围绕“{core_terms[0]}”展开，属于{seg.get('toc_id', '')}条目语境。")
    if len(core_terms) > 1:
        propositions.append(f"- 核心命题2：文本持续追问“{core_terms[1]}”与其边界关系。")
    propositions.append("- 核心命题3：该段属于 ISMISM 结构中的实证/形而上学张力节点，需结合邻接段位交叉校验。")
    card = card.replace("## Key Propositions\n\n", "## Key Propositions\n\n" + "\n".join(propositions) + "\n\n")
    card = card.replace("## Figures / Schools / Isms\n\n", "## Figures / Schools / Isms\n\n" + ("\n".join(f"- {f}" for f in figures) if figures else "- 待识别\n") + "\n")
    card = card.replace("## Evidence Anchors\n\n", "## Evidence Anchors\n\n" + ("\n".join(anchors) if anchors else "- 暂无可提取证据行\n") + "\n")
    card = card.replace("## Position / Relation Hints\n\n", "## Position / Relation Hints\n\n" + "\n".join(position_hints(seg)) + "\n")
    card = card.replace("## Uncertainties\n\n", "## Uncertainties\n\n- 已按 clean 文本抽取生成，需人工核对原文语义与术语边界。\n- 若该段与上下位条目重复，需在 W3 术语义项阶段去重。\n\n")
    card = card.replace("## Audit Notes\n\n", "## Audit Notes\n\n- draft: W2 auto-generated by `build_w2_segment_cards.py`\n- evidence_lines_checked: first non-empty lines only\n")
    card = card.replace("# Segment Card: <title>", f"# Segment Card: {title}")

    return card


def build_index(segments: list[dict], card_rows: set[int], processed_rows: list[int]) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# ISMISM Segment Cards Index\n",
        f"- updated: {ts}\n",
        f"- total_segments: {len(segments)}\n",
        f"- generated_cards: {len(card_rows)}\n",
        "\n",
        "## Cards\n",
        "| row_id | toc_id | title | status | path |",
        "|---|---|---|---|---|",
    ]
    for seg in segments:
        row_id = int(seg["row_id"])
        status = "draft" if row_id in card_rows else "pending"
        p = card_path(row_id, seg["toc_id"])
        rel = f"[{p.name}]({p.as_posix()})" if status == "draft" else "-"
        title = seg["title"].replace("|", "｜")
        lines.append(f"| {row_id} | {seg['toc_id']} | {title} | {status} | {rel} |")

    lines.append("\n")
    if processed_rows:
        lines.append("## Last Batch\n")
        lines.append(f"- processed_rows: {', '.join(map(str, processed_rows))}\n")
    lines.append("\n")
    INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")


def update_state(batch_rows: list[int]) -> None:
    state = STATE.read_text(encoding="utf-8")
    total_segments = 0
    with SEGMENTS_JSONL.open(encoding="utf-8") as f:
        total_segments = sum(1 for line in f if line.strip())

    # update progress counters
    existing = collect_existing_cards()
    count = len(existing)

    # update a few key fields conservatively
    repl = {
        "current_phase": "W2 segment cards in progress",
        "segments card": "",
        "| segment cards |": "| segment cards |",
    }
    lines = state.splitlines()
    out = []
    for ln in lines:
        if ln.startswith("- current_phase:"):
            out.append("- current_phase: W2 segment cards in progress")
            continue
        if ln.startswith("- `segments/*.md" ):
            out.append(ln)
            continue
        out.append(ln)
    # append explicit counters if absent or stale
    if "## Progress Counters" in state:
        out2 = []
        replaced = False
        for ln in out:
            if ln.startswith("| segment cards |"):
                out2.append(f"| segment cards | {count} | {total_segments} | W2 batch progress; latest batch rows: {','.join(map(str,batch_rows)) if batch_rows else 'none'} |")
                replaced = True
            else:
                out2.append(ln)
        out = out2
        if not replaced:
            out.append(f"| segment cards | {count} | {total_segments} | W2 batch progress; latest batch rows: {','.join(map(str,batch_rows)) if batch_rows else 'none'} |")
    else:
        out.append(f"- segment cards: {count}/{total_segments}")

    # update next action block with next row
    next_row = batch_rows[-1] + 1 if batch_rows else (max(existing) + 1 if existing else 1)
    out.append("")
    out.append("## W2 Next Batch")
    out.append(f"- next_row: {next_row}")
    out.append(f"- latest_batch_count: {len(batch_rows)}")
    out.append(f"- processed_cumulative: {count}/{total_segments}")

    STATE.write_text("\n".join(out) + "\n", encoding="utf-8")


def log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.touch(exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S CST")
        f.write(f"\n## {ts} — W2 segment cards batch\n")
        f.write(f"{msg}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-row", type=int, default=None, help="Start from row id (inclusive).")
    parser.add_argument("--batch-size", type=int, default=16, help="How many rows to process this batch.")
    parser.add_argument("--rebuild-index", action="store_true", help="Force rebuild index after batch.")
    args = parser.parse_args()

    segments = read_segments()
    available = [s for s in segments if s.get("text_status") == "available"]

    existing = collect_existing_cards()
    start_row = choose_start_row(available, existing, args.start_row)

    pending = [s for s in available if s["row_id"] >= start_row]
    batch = pending[: args.batch_size]
    if not batch:
        print("No available segments to process.")
        return

    SEGMENT_CARDS.mkdir(parents=True, exist_ok=True)

    processed = []
    for seg in batch:
        row_id = int(seg["row_id"])
        toc_id = seg["toc_id"]
        cp = card_path(row_id, toc_id)

        if cp.exists():
            continue

        clean_rel = seg["source_paths"]["clean_md_relpath"]
        text = (ROOT / clean_rel).read_text(encoding="utf-8", errors="ignore")
        lines = strip_markdown(text)
        summary = extract_summary(lines)

        evidence = extract_lines_excerpt(lines, max_count=3)
        card_md = build_card_content(seg, evidence, summary)
        cp.write_text(card_md, encoding="utf-8")
        processed.append(row_id)
        print(f"wrote: {cp.relative_to(ROOT)}")

    existing_after = collect_existing_cards()
    build_index(available, existing_after, processed)
    update_state(processed)

    # update operation log
    msg = (
        f"Generated W2 batch size={len(processed)} from row {start_row}; "
        f"rows={','.join(map(str, processed)) if processed else 'none'}. "
        "Updated knowledge/segment-cards/index.md and STATE.md."
    )
    log(msg)

    if args.rebuild_index:
        print(f"segment cards total now: {len(existing_after)}")


if __name__ == "__main__":
    main()
