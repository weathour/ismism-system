import argparse
from pathlib import Path

from enrich_toc import enrich_csv
from extract_markdown import convert_tree
from generate_toc import parse_markdown, write_csv
from slice_source_pdf import pdf_slices


def ensure_csv(markdown_path: Path, csv_path: Path) -> None:
    records = parse_markdown(markdown_path)
    if not records:
        raise SystemExit(f"未从 {markdown_path} 解析到任何目录项。")
    write_csv(records, csv_path)
    print(f"wrote {len(records)} rows to {csv_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="一键执行目录 CSV 生成、PDF 拆分、Markdown 提取。")
    parser.add_argument(
        "--markdown",
        default="corpus/registry/toc.md",
        help="结构化 Markdown 目录路径。",
    )
    parser.add_argument(
        "--csv",
        default="corpus/registry/toc.csv",
        help="结构化 CSV 输出路径。",
    )
    parser.add_argument(
        "--pdf",
        default="corpus/source/ismism.pdf",
        help="源 PDF 路径。",
    )
    parser.add_argument(
        "--split-dir",
        default="corpus/pdf-slices",
        help="PDF slice output directory.",
    )
    parser.add_argument(
        "--md-dir",
        default="corpus/raw-markdown",
        help="Markdown 输出目录。",
    )
    parser.add_argument(
        "--page-offset",
        type=int,
        default=1,
        help="目录页码到 PDF 页索引的偏移量。",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="仅处理前 N 条，便于测试。",
    )
    args = parser.parse_args()

    markdown_path = Path(args.markdown).resolve()
    csv_path = Path(args.csv).resolve()
    pdf_path = Path(args.pdf).resolve()
    split_dir = Path(args.split_dir).resolve()
    md_dir = Path(args.md_dir).resolve()

    ensure_csv(markdown_path, csv_path)
    pdf_slices(
        pdf_path=pdf_path,
        csv_path=csv_path,
        output_dir=split_dir,
        page_offset=args.page_offset,
        limit=args.limit,
    )
    convert_tree(split_dir, md_dir)
    enrich_csv(csv_path, split_dir, md_dir)


if __name__ == "__main__":
    main()
