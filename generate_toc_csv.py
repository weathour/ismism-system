import argparse
import csv
import re
from pathlib import Path


NUMBERED_PATTERN = re.compile(
    r"^(?P<indent>\s*)-\s+`\[(?P<toc_id>[^\]]+)\]`\s+(?P<title>.+?)（p\.(?P<page>\d+)）\s*$"
)
PLAIN_PATTERN = re.compile(
    r"^(?P<indent>\s*)-\s+(?P<title>.+?)（p\.(?P<page>\d+)）\s*$"
)


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


def parse_markdown(markdown_path: Path) -> list[dict]:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    records: list[dict] = []
    stack: dict[int, dict] = {}

    for line_number, line in enumerate(lines, start=1):
        match = NUMBERED_PATTERN.match(line)
        toc_id = ""
        if match:
            title = match.group("title").strip()
            page = int(match.group("page"))
            toc_id = match.group("toc_id").strip()
            indent = len(match.group("indent"))
        else:
            match = PLAIN_PATTERN.match(line)
            if not match:
                continue
            title = match.group("title").strip()
            page = int(match.group("page"))
            indent = len(match.group("indent"))

        tree_level = indent // 2 + 1
        toc_depth = len(toc_id.split("-")) if toc_id else 0

        parent = stack.get(tree_level - 1)
        parent_row_id = parent["row_id"] if parent else ""
        parent_toc_id = parent["toc_id"] if parent else ""
        parent_path_titles = parent["path_titles"].split(" / ") if parent else []
        parent_path_ids = parent["path_ids"].split(" / ") if parent and parent["path_ids"] else []

        path_titles = parent_path_titles + [title]
        path_ids = parent_path_ids + ([toc_id] if toc_id else [])

        row_id = len(records) + 1
        record = {
            "row_id": row_id,
            "tree_level": tree_level,
            "toc_id": toc_id,
            "toc_depth": toc_depth,
            "title": title,
            "page_start": page,
            "parent_row_id": parent_row_id,
            "parent_toc_id": parent_toc_id,
            "path_titles": " / ".join(path_titles),
            "path_ids": " / ".join(path_ids),
            "safe_title": safe_component(title, 72),
            "safe_toc_id": safe_component(toc_id, 32) if toc_id else "",
            "line_number": line_number,
        }
        record["file_stub"] = (
            f"{row_id:04d}__"
            f"{record['safe_toc_id'] or 'item'}__"
            f"{record['safe_title']}__p{page}"
        )
        records.append(record)
        stack[tree_level] = record

        for key in list(stack.keys()):
            if key > tree_level:
                del stack[key]

    for index, record in enumerate(records):
        next_record = records[index + 1] if index + 1 < len(records) else None
        record["next_page_start"] = next_record["page_start"] if next_record else ""

    return records


def write_csv(records: list[dict], output_path: Path) -> None:
    fieldnames = [
        "row_id",
        "tree_level",
        "toc_id",
        "toc_depth",
        "title",
        "page_start",
        "next_page_start",
        "parent_row_id",
        "parent_toc_id",
        "path_titles",
        "path_ids",
        "safe_title",
        "safe_toc_id",
        "file_stub",
        "line_number",
    ]
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="从结构化 Markdown 目录生成 CSV。")
    parser.add_argument(
        "--input",
        default="目录索引_结构化.md",
        help="输入 Markdown 文件路径。",
    )
    parser.add_argument(
        "--output",
        default="目录索引_结构化.csv",
        help="输出 CSV 文件路径。",
    )
    args = parser.parse_args()

    markdown_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()

    records = parse_markdown(markdown_path)
    if not records:
        raise SystemExit(f"未从 {markdown_path} 解析到任何目录项。")

    write_csv(records, output_path)
    print(f"wrote {len(records)} rows to {output_path}")


if __name__ == "__main__":
    main()
