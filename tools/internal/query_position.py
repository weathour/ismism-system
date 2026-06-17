#!/usr/bin/env python3
"""Query ISMISM matrix position cards."""
from __future__ import annotations

import argparse
from pathlib import Path
from query_helpers import as_json, front_matter_and_body, repo_root, section_text, truncate


def load_cards(root: Path):
    cards = []
    for path in sorted((root / "library" / "positions").glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = front_matter_and_body(text)
        coord = path.stem
        title = meta.get("title") or ""
        cards.append({"coordinate": coord, "path": path, "meta": meta, "body": body, "text": text, "title": title})
    return cards


def card_to_summary(card, root: Path, include_text: bool = False):
    meta = card["meta"]
    body = card["body"]
    data = {
        "coordinate": card["coordinate"],
        "path": str(card["path"].relative_to(root)),
        "position_id": meta.get("position_id"),
        "level": meta.get("level"),
        "title": meta.get("title"),
        "status": meta.get("status"),
        "source_rows": meta.get("source_rows"),
        "source_segments": meta.get("source_segments"),
        "matrix_axes": section_text(body, "矩阵坐标", max_chars=300),
        "evidence_chain": section_text(body, "证据链", max_chars=500),
        "definition": section_text(body, "位置定义", max_chars=900),
    }
    if include_text:
        data["card_text"] = card["text"]
    return data


def print_markdown(matches, root: Path, args) -> None:
    print(f"# Position query: {args.query}")
    print(f"matches: {len(matches)}")
    for card in matches[: args.limit]:
        data = card_to_summary(card, root, include_text=False)
        print()
        print(f"## {data['coordinate']} — {data.get('title')}")
        print(f"- path: `{data['path']}`")
        print(f"- level/status: {data.get('level')} / {data.get('status')}")
        print(f"- source_rows: {data.get('source_rows')}")
        if data.get("matrix_axes"):
            print("- matrix_axes:")
            for line in data["matrix_axes"].splitlines():
                print(f"  {line}")
        if data.get("evidence_chain"):
            print("- evidence_chain:")
            for line in data["evidence_chain"].splitlines()[:4]:
                print(f"  {line}")
        if data.get("definition"):
            print(f"- definition: {truncate(data['definition'], args.definition_chars)}")
    if len(matches) > args.limit:
        print(f"\n... truncated: showing {args.limit}/{len(matches)} cards")


def main() -> None:
    parser = argparse.ArgumentParser(description="Query position cards by coordinate or title text.")
    parser.add_argument("query", help="coordinate (e.g. 3-4-2) or title/search text")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--contains", action="store_true", help="search full card text, not just exact coordinate/title")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--definition-chars", type=int, default=500)
    parser.add_argument("--show-card", action="store_true", help="include full card text in JSON output")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = repo_root(args.repo)
    cards = load_cards(root)
    q = args.query.lower()
    if args.contains:
        matches = [c for c in cards if q in c["text"].lower() or q in c["coordinate"].lower()]
    else:
        matches = [c for c in cards if c["coordinate"] == args.query or str(c["title"]) == args.query]
        if not matches:
            matches = [c for c in cards if q in str(c["title"]).lower()]
    matches.sort(key=lambda c: (len(c["coordinate"].split("-")), c["coordinate"]))
    if args.json:
        print(as_json([card_to_summary(c, root, include_text=args.show_card) for c in matches[: args.limit]]))
    else:
        print_markdown(matches, root, args)


if __name__ == "__main__":
    main()
