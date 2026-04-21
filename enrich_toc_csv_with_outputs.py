import argparse
import csv
from pathlib import Path

from split_pdf_by_toc import build_output_path, load_rows


def enrich_csv(csv_path: Path, split_pdf_dir: Path, split_md_dir: Path) -> None:
    rows = load_rows(csv_path)
    rows_by_id = {row["row_id"]: row for row in rows}

    original_rows: list[dict] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        original_rows = list(reader)

    extra_fields = [
        "split_pdf_relpath",
        "split_md_relpath",
        "split_pdf_exists",
        "split_md_exists",
    ]
    for field in extra_fields:
        if field not in fieldnames:
            fieldnames.append(field)

    enriched_rows: list[dict] = []
    for original_row in original_rows:
        row_id = int(original_row["row_id"])
        parsed_row = rows_by_id[row_id]

        pdf_path = build_output_path(split_pdf_dir, rows_by_id, parsed_row)
        md_path = split_md_dir / pdf_path.relative_to(split_pdf_dir).with_suffix(".md")

        original_row["split_pdf_relpath"] = pdf_path.relative_to(csv_path.parent).as_posix()
        original_row["split_md_relpath"] = md_path.relative_to(csv_path.parent).as_posix()
        original_row["split_pdf_exists"] = "1" if pdf_path.exists() else "0"
        original_row["split_md_exists"] = "1" if md_path.exists() else "0"
        enriched_rows.append(original_row)

    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_rows)

    print(f"enriched {len(enriched_rows)} rows in {csv_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="把 split_pdf / split_md 路径回填到结构化 CSV。")
    parser.add_argument(
        "--csv",
        default="目录索引_结构化.csv",
        help="结构化 CSV 路径。",
    )
    parser.add_argument(
        "--split-pdf-dir",
        default="split_pdf",
        help="拆分 PDF 根目录。",
    )
    parser.add_argument(
        "--split-md-dir",
        default="split_md",
        help="Markdown 根目录。",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv).resolve()
    split_pdf_dir = Path(args.split_pdf_dir).resolve()
    split_md_dir = Path(args.split_md_dir).resolve()

    enrich_csv(csv_path, split_pdf_dir, split_md_dir)


if __name__ == "__main__":
    main()
