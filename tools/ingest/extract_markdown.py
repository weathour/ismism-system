import argparse
from pathlib import Path

import fitz


def extract_page_markdown(page: fitz.Page) -> str:
    try:
        text = page.get_text("markdown")
        if text and text.strip():
            return text
    except Exception:
        pass
    text = page.get_text("text")
    return text or ""


def convert_one_pdf(pdf_path: Path, output_path: Path) -> None:
    doc = fitz.open(pdf_path)
    chunks: list[str] = []
    chunks.append(f"# {pdf_path.stem}")
    chunks.append("")
    chunks.append(f"- source_pdf: `{pdf_path.name}`")
    chunks.append(f"- page_count: {doc.page_count}")
    chunks.append("")

    for index, page in enumerate(doc, start=1):
        chunks.append("---")
        chunks.append("")
        chunks.append(f"## Page {index}")
        chunks.append("")
        page_text = extract_page_markdown(page).strip()
        chunks.append(page_text if page_text else "[[EMPTY_PAGE]]")
        chunks.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(chunks), encoding="utf-8")
    doc.close()
    print(f"wrote {output_path}")


def convert_tree(input_dir: Path, output_dir: Path) -> None:
    pdf_files = sorted(input_dir.rglob("*.pdf"))
    if not pdf_files:
        raise SystemExit(f"未在 {input_dir} 下找到任何 PDF。")

    for pdf_path in pdf_files:
        relative = pdf_path.relative_to(input_dir)
        output_path = output_dir / relative.with_suffix(".md")
        convert_one_pdf(pdf_path, output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="将拆分后的 PDF 批量提取为 Markdown。")
    parser.add_argument(
        "--input-dir",
        default="corpus/pdf-slices",
        help="拆分后的 PDF 根目录。",
    )
    parser.add_argument(
        "--output-dir",
        default="corpus/raw-markdown",
        help="提取后的 Markdown 根目录。",
    )
    args = parser.parse_args()

    convert_tree(Path(args.input_dir).resolve(), Path(args.output_dir).resolve())


if __name__ == "__main__":
    main()
