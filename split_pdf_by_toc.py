import argparse
import csv
import re
from pathlib import Path

import fitz


def safe_component(text: str, max_len: int = 48) -> str:
    text = text.strip()
    cleaned = []
    for char in text:
        if char.isalnum() or "\u4e00" <= char <= "\u9fff" or char in ("-", "_", " "):
            cleaned.append(char)
        else:
            cleaned.append("_")
    value = "".join(cleaned)
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    if not value:
        value = "untitled"
    return value[:max_len]


def load_rows(csv_path: Path) -> list[dict]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    for row in rows:
        row["row_id"] = int(row["row_id"])
        row["tree_level"] = int(row["tree_level"])
        row["page_start"] = int(row["page_start"])
        row["next_page_start"] = int(row["next_page_start"]) if row["next_page_start"] else None
    return rows


def build_output_path(output_dir: Path, rows_by_id: dict[int, dict], row: dict) -> Path:
    ancestors = []
    parent_id = int(row["parent_row_id"]) if row["parent_row_id"] else None
    while parent_id:
        parent = rows_by_id[parent_id]
        label = f"{parent['safe_toc_id'] or f'item_{parent['row_id']:04d}'}__{parent['safe_title']}"
        ancestors.append(safe_component(label, 48))
        parent_id = int(parent["parent_row_id"]) if parent["parent_row_id"] else None
    ancestors.reverse()

    current_dir_label = safe_component(
        f"{row['safe_toc_id'] or f'item_{row['row_id']:04d}'}__{row['safe_title']}",
        48,
    )
    item_label = (
        f"{row['row_id']:04d}__"
        f"{row['safe_toc_id'] or 'item'}__"
        f"{row['safe_title']}__"
        f"p{row['page_start']}"
    )
    directory = output_dir.joinpath(*ancestors, current_dir_label)
    return directory / f"{safe_component(item_label, 120)}.pdf"


def split_pdf(
    pdf_path: Path,
    csv_path: Path,
    output_dir: Path,
    page_offset: int,
    limit: int | None,
) -> None:
    rows = load_rows(csv_path)
    rows_by_id = {row["row_id"]: row for row in rows}
    output_dir.mkdir(parents=True, exist_ok=True)

    source = fitz.open(pdf_path)
    total_pages = source.page_count

    if limit is not None:
        rows = rows[:limit]

    for row in rows:
        start_index = row["page_start"] + page_offset - 1
        if start_index < 0 or start_index >= total_pages:
            print(f"skip row {row['row_id']}: start page out of range")
            continue

        if row["next_page_start"] is not None:
            end_index = row["next_page_start"] + page_offset - 1
        else:
            end_index = total_pages - 1

        end_index = min(end_index, total_pages - 1)
        if end_index < start_index:
            print(f"skip row {row['row_id']}: invalid range")
            continue

        target_path = build_output_path(output_dir, rows_by_id, row)
        target_path.parent.mkdir(parents=True, exist_ok=True)

        new_doc = fitz.open()
        new_doc.insert_pdf(source, from_page=start_index, to_page=end_index)
        new_doc.save(target_path)
        new_doc.close()
        print(
            f"row {row['row_id']:04d}: {target_path} "
            f"(book p{row['page_start']} -> p{row['next_page_start'] or 'END'})"
        )

    source.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="按目录 CSV 拆分 PDF。")
    parser.add_argument(
        "--pdf",
        default="主义主义 (未明子) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
        help="源 PDF 路径。",
    )
    parser.add_argument(
        "--csv",
        default="目录索引_结构化.csv",
        help="目录 CSV 路径。",
    )
    parser.add_argument(
        "--output-dir",
        default="split_pdf",
        help="拆分后的 PDF 输出目录。",
    )
    parser.add_argument(
        "--page-offset",
        type=int,
        default=1,
        help="目录页码到 PDF 页索引的偏移量。当前 PDF 默认为 1。",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="仅处理前 N 条，便于测试。",
    )
    args = parser.parse_args()

    split_pdf(
        pdf_path=Path(args.pdf).resolve(),
        csv_path=Path(args.csv).resolve(),
        output_dir=Path(args.output_dir).resolve(),
        page_offset=args.page_offset,
        limit=args.limit,
    )


if __name__ == "__main__":
    main()
