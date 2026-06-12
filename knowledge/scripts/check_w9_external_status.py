#!/usr/bin/env python3
"""Read-only W9 external-target status checker.

This script compares the repo-local W9 protocol with the intended external
psychoanalytic-writing-lab target. It never writes outside the repository. Use
--expect-match only when cross-repository W9 completion is being audited.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


W9_REPO_LOCAL = "knowledge/integration/psychoanalytic-writing-lab/ismism-reference-protocol.md"
W9_EXTERNAL = "/home/weathour/文档/psychoanalytic-writing-lab/docs/method/ismism-reference-protocol.md"


def file_info(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "path": str(path),
            "exists": False,
            "size": None,
            "sha256": None,
        }
    data = path.read_bytes()
    return {
        "path": str(path),
        "exists": True,
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check W9 external target status without writing outside repo.")
    parser.add_argument("--repo", default=".", help="ismism-system repository root")
    parser.add_argument("--external", default=W9_EXTERNAL, help="external W9 target path")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--expect-match", action="store_true", help="fail unless external target exactly matches repo-local protocol")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    repo_local = repo / W9_REPO_LOCAL
    external = Path(args.external)

    local_info = file_info(repo_local)
    external_info = file_info(external)
    matches = bool(
        local_info["exists"]
        and external_info["exists"]
        and local_info["sha256"] == external_info["sha256"]
    )
    status = "MATCH" if matches else "MISMATCH"
    if not local_info["exists"]:
        status = "LOCAL_MISSING"
    elif not external_info["exists"]:
        status = "EXTERNAL_MISSING"

    result = {
        "status": status,
        "repo_local": local_info,
        "external": external_info,
        "matches": matches,
        "boundary_note": "read-only check; this script does not write outside ismism-system",
        "next_action_if_mismatch": "Use COPY-INSTRUCTIONS.md only via human action or explicit outside-repo write authorization.",
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(
            "W9 external status: "
            f"status={status}, "
            f"local_sha256={local_info['sha256']}, "
            f"external_sha256={external_info['sha256']}, "
            f"matches={matches}"
        )
        if status != "MATCH":
            print("NOTE: external W9 is not current unless repo-local W9 is explicitly accepted as sufficient.")

    if not local_info["exists"]:
        return 1
    if args.expect_match and not matches:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
