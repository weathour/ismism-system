#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import time
import hashlib
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "gemma4:latest"
DEFAULT_API = "http://localhost:11434/api/generate"
DEFAULT_TEMPERATURE = 0.0
DEFAULT_REPEAT_PENALTY = 1.15
DEFAULT_NUM_CTX = 8192
PAGE_HEADING_RE = re.compile(r"^## Page \d+\s*$", re.M)

SYSTEM_RULES = """你是中文文本轻清洗器。你的任务是把直播/讲稿转写文本整理成更正常、可读的中文文本。
严格要求：
1. 尽量保留原话，不总结，不改观点，不补充新概念。
2. 修复断裂换行、缺失标点、中英文空格混乱、明显口语转写噪声。
3. 允许删除明显重复的口头卡壳、重复半句、无意义重复词，但不要改变论证结构。
4. 保留原有术语、编号、引用、英文术语。
5. 保留输入中的页标记，形如 `<<<PAGE:1>>>`、`<<<PAGE:2>>>`，顺序不得改变，不得丢失，不得改写。
6. 不要输出解释，不要输出说明，不要新增标题。
7. 不要添加任何新的 Markdown 格式，例如粗体、斜体、列表、引用块或代码块。
8. 只输出清洗后的正文。
"""


def iter_markdown_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if path.is_file():
            yield path


def split_header_and_pages(text: str):
    match = PAGE_HEADING_RE.search(text)
    if not match:
        return text, []
    header = text[: match.start()].rstrip() + "\n\n"
    page_region = text[match.start():]
    parts = re.split(r"(?=^## Page \d+\s*$)", page_region, flags=re.M)
    pages = [p.strip() + "\n" for p in parts if p.strip()]
    return header, pages


def batch_pages(pages, max_chars=4000):
    batches = []
    current = []
    current_len = 0
    for page in pages:
        plen = len(page)
        if current and current_len + plen > max_chars:
            batches.append("\n".join(current).strip() + "\n")
            current = [page]
            current_len = plen
        else:
            current.append(page)
            current_len += plen
    if current:
        batches.append("\n".join(current).strip() + "\n")
    return batches


def ollama_generate(
    api_url: str,
    model: str,
    prompt: str,
    temperature: float = DEFAULT_TEMPERATURE,
    repeat_penalty: float = DEFAULT_REPEAT_PENALTY,
    num_ctx: int = DEFAULT_NUM_CTX,
    timeout: int = 180,
):
    options = {
        "temperature": temperature,
    }
    if repeat_penalty is not None:
        options["repeat_penalty"] = repeat_penalty
    if num_ctx is not None:
        options["num_ctx"] = num_ctx
    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": options,
        }
    ).encode("utf-8")
    req = urllib.request.Request(api_url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("response", "")


def clean_batch(
    api_url: str,
    model: str,
    batch_text: str,
    timeout: int,
    temperature: float,
    repeat_penalty: float,
    num_ctx: int,
):
    prompt = SYSTEM_RULES + "\n待清洗 Markdown：\n" + batch_text
    return (
        ollama_generate(
            api_url=api_url,
            model=model,
            prompt=prompt,
            temperature=temperature,
            repeat_penalty=repeat_penalty,
            num_ctx=num_ctx,
            timeout=timeout,
        ).strip()
        + "\n"
    )


def normalize_whitespace(text: str):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def validate_page_headings(original_pages, cleaned_text):
    orig_heads = PAGE_HEADING_RE.findall("\n".join(original_pages))
    new_heads = PAGE_HEADING_RE.findall(cleaned_text)
    return orig_heads == new_heads


def convert_headings_to_markers(text: str):
    return re.sub(r"^## Page (\d+)\s*$", lambda m: f"<<<PAGE:{m.group(1)}>>>", text, flags=re.M)


def restore_markers_to_headings(text: str):
    return re.sub(r"^<<<PAGE:(\d+)>>>\s*$", lambda m: f"## Page {m.group(1)}", text, flags=re.M)


def validate_markers(page_numbers, cleaned_text):
    markers = re.findall(r"^<<<PAGE:(\d+)>>>\s*$", cleaned_text, flags=re.M)
    return markers == page_numbers


def process_file(
    path: Path,
    input_root: Path,
    output_root: Path,
    api_url: str,
    model: str,
    overwrite: bool,
    timeout: int,
    max_batch_chars: int,
    temperature: float,
    repeat_penalty: float,
    num_ctx: int,
):
    rel = path.relative_to(input_root)
    out_path = output_root / rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not overwrite:
        return {
            "source": str(path),
            "output": str(out_path),
            "status": "skipped_exists",
        }

    text = normalize_whitespace(path.read_text(encoding="utf-8"))
    header, pages = split_header_and_pages(text)
    original_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()

    if not pages:
        out_path.write_text(text, encoding="utf-8")
        return {
            "source": str(path),
            "output": str(out_path),
            "status": "copied_no_pages",
            "page_count": 0,
            "source_sha256": original_hash,
        }

    cleaned_batches = []
    used_fallback = False
    batch_count = 0

    for batch in batch_pages(pages, max_chars=max_batch_chars):
        batch_count += 1
        page_numbers = re.findall(r"^## Page (\d+)\s*$", batch, flags=re.M)
        batch_for_llm = convert_headings_to_markers(batch)
        cleaned = clean_batch(
            api_url,
            model,
            batch_for_llm,
            timeout=timeout,
            temperature=temperature,
            repeat_penalty=repeat_penalty,
            num_ctx=num_ctx,
        )
        if not validate_markers(page_numbers, cleaned):
            used_fallback = True
            fallback_parts = []
            for page in re.split(r"(?=^## Page \d+\s*$)", batch, flags=re.M):
                if not page.strip():
                    continue
                page_for_llm = convert_headings_to_markers(page.strip() + "\n")
                page_numbers_single = re.findall(r"^## Page (\d+)\s*$", page, flags=re.M)
                page_cleaned = (
                    clean_batch(
                        api_url,
                        model,
                        page_for_llm,
                        timeout=timeout,
                        temperature=temperature,
                        repeat_penalty=repeat_penalty,
                        num_ctx=num_ctx,
                    ).strip()
                    + "\n"
                )
                if not validate_markers(page_numbers_single, page_cleaned):
                    page_cleaned = page_for_llm
                fallback_parts.append(restore_markers_to_headings(page_cleaned).strip())
            cleaned = "\n\n".join(fallback_parts).strip() + "\n"
        else:
            cleaned = restore_markers_to_headings(cleaned)
        cleaned_batches.append(cleaned.strip())

    cleaned_text = header + "\n\n".join(cleaned_batches).strip() + "\n"
    cleaned_text = normalize_whitespace(cleaned_text)
    cleaned_hash = hashlib.sha256(cleaned_text.encode("utf-8")).hexdigest()
    out_path.write_text(cleaned_text, encoding="utf-8")

    return {
        "source": str(path),
        "output": str(out_path),
        "status": "cleaned",
        "page_count": len(pages),
        "batch_count": batch_count,
        "used_fallback": used_fallback,
        "source_chars": len(text),
        "cleaned_chars": len(cleaned_text),
        "char_ratio": round(len(cleaned_text) / max(len(text), 1), 4),
        "source_sha256": original_hash,
        "cleaned_sha256": cleaned_hash,
    }


def main():
    ap = argparse.ArgumentParser(description="Clean split markdown lecture files with local Ollama.")
    ap.add_argument("--input-root", default="split_md")
    ap.add_argument("--output-root", default="split_md_clean")
    ap.add_argument("--subdir", default=None, help="Optional subdir under input root, e.g. 1_实在论")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--api-url", default=DEFAULT_API)
    ap.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    ap.add_argument("--repeat-penalty", type=float, default=DEFAULT_REPEAT_PENALTY)
    ap.add_argument("--num-ctx", type=int, default=DEFAULT_NUM_CTX)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--max-batch-chars", type=int, default=4000)
    ap.add_argument("--report-path", default=None)
    args = ap.parse_args()

    input_root = Path(args.input_root).resolve()
    if args.subdir:
        input_root = (input_root / args.subdir).resolve()
    output_root = Path(args.output_root).resolve()
    if args.subdir:
        output_root = (output_root / args.subdir)
    output_root.mkdir(parents=True, exist_ok=True)

    if not input_root.exists():
        print(f"Input root not found: {input_root}", file=sys.stderr)
        sys.exit(2)

    report_path = Path(args.report_path).resolve() if args.report_path else output_root / "_cleanup_report.jsonl"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    results = []
    started = time.time()
    run_started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(started))
    run_id = f"{int(started)}-{os.getpid()}"
    with report_path.open("a", encoding="utf-8") as rf:
        for idx, path in enumerate(iter_markdown_files(input_root), start=1):
            try:
                result = process_file(
                    path=path,
                    input_root=input_root,
                    output_root=output_root,
                    api_url=args.api_url,
                    model=args.model,
                    overwrite=args.overwrite,
                    timeout=args.timeout,
                    max_batch_chars=args.max_batch_chars,
                    temperature=args.temperature,
                    repeat_penalty=args.repeat_penalty,
                    num_ctx=args.num_ctx,
                )
            except Exception as e:
                result = {
                    "source": str(path),
                    "status": "error",
                    "error": str(e),
                }
            result["index"] = idx
            result["run_id"] = run_id
            result["run_started_at"] = run_started_at
            rf.write(json.dumps(result, ensure_ascii=False) + "\n")
            rf.flush()
            results.append(result)
            print(json.dumps(result, ensure_ascii=False), flush=True)

    cleaned = [r for r in results if r.get("status") == "cleaned"]
    errors = [r for r in results if r.get("status") == "error"]
    skipped = [r for r in results if r.get("status") == "skipped_exists"]
    copied = [r for r in results if r.get("status") == "copied_no_pages"]
    elapsed = round(time.time() - started, 2)
    summary = {
        "input_root": str(input_root),
        "output_root": str(output_root),
        "report_path": str(report_path),
        "model": args.model,
        "temperature": args.temperature,
        "repeat_penalty": args.repeat_penalty,
        "num_ctx": args.num_ctx,
        "total": len(results),
        "cleaned": len(cleaned),
        "errors": len(errors),
        "skipped_exists": len(skipped),
        "copied_no_pages": len(copied),
        "elapsed_seconds": elapsed,
    }
    print("SUMMARY=" + json.dumps(summary, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
