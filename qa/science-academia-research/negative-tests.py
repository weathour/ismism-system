#!/usr/bin/env python3
from __future__ import annotations
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
THEME = ROOT / "library/themes/science-academia-research"
RESULTS: list[dict] = []


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)


def record(name: str, proc: subprocess.CompletedProcess[str], expect_fail: bool = True) -> None:
    ok = (proc.returncode != 0) if expect_fail else (proc.returncode == 0)
    RESULTS.append(
        {
            "name": name,
            "expected": "fail" if expect_fail else "pass",
            "ok": ok,
            "returncode": proc.returncode,
            "stdout_head": proc.stdout.splitlines()[:8],
            "stderr_head": proc.stderr.splitlines()[:8],
        }
    )
    if not ok:
        raise SystemExit(f"negative test did not behave as expected: {name}")


def record_failure_diagnostics(name: str, proc: subprocess.CompletedProcess[str]) -> None:
    record(name, proc, expect_fail=True)
    visible = proc.stdout + "\n" + proc.stderr
    required = [
        "ERROR: social route helper failed",
        "attempt term=科学主义",
        "attempt term=科学化",
        "attempt term=实证主义",
        "attempt term=自然主义",
        "exit=",
        "stderr=",
    ]
    missing = [needle for needle in required if needle not in visible]
    if missing:
        raise SystemExit(f"negative test missing visible diagnostics for {name}: {missing}")


def mutate_file(path: Path, mutator, cmd: list[str], name: str) -> None:
    original = path.read_text(encoding="utf-8")
    try:
        path.write_text(mutator(original), encoding="utf-8")
        record(name, run(cmd), expect_fail=True)
    finally:
        path.write_text(original, encoding="utf-8")


def main() -> int:
    mutate_file(
        THEME / "science-academia-research-evidence-bank.jsonl",
        lambda s: s.replace('"quote": "', '"quote": "BAD-', 1),
        ["python3", "tools/validate/themes/science_academia_research.py", "--repo", "."],
        "bad exact quote fails theme validator",
    )
    mutate_file(
        THEME / "science-academia-research-taxonomy.md",
        lambda s: s.replace("- rows: row 9,", "- rows: row 2, row 9,", 1),
        ["python3", "tools/validate/themes/science_academia_research.py", "--repo", "."],
        "duplicate taxonomy row fails theme validator",
    )
    def wrong_overlap(s: str) -> str:
        lines=[]
        changed=False
        for line in s.splitlines():
            if not changed and '"row_id": 2,' in line:
                obj=json.loads(line)
                obj["overlap_status"]="not-in-education"
                line=json.dumps(obj, ensure_ascii=False)
                changed=True
            lines.append(line)
        return "\n".join(lines)+"\n"
    mutate_file(
        THEME / "science-academia-research-row-manifest.jsonl",
        wrong_overlap,
        ["python3", "tools/validate/themes/science_academia_research.py", "--repo", "."],
        "wrong Education overlap fails theme validator",
    )
    mutate_file(
        THEME / "scientific-discourse-knowledge-legitimacy-synthesis.md",
        lambda s: s.replace("ev:sar:", "ev-sar:"),
        ["python3", "tools/validate/themes/science_academia_research.py", "--repo", ".", "--final"],
        "missing synthesis marker fails final validator",
    )
    def non_draft_concept(s: str) -> str:
        lines = []
        changed = False
        for line in s.splitlines():
            if not changed and 'concept-SCIENCE-ACADEMIA-RESEARCH-2026-06-17' in line:
                obj = json.loads(line)
                obj["status"] = "accepted"
                line = json.dumps(obj, ensure_ascii=False)
                changed = True
            lines.append(line)
        return "\n".join(lines)+"\n"
    mutate_file(
        ROOT / "library/concepts/term-senses.jsonl",
        non_draft_concept,
        ["python3", "tools/validate/concepts.py", "--repo", ".", "--batch-id", "concept-SCIENCE-ACADEMIA-RESEARCH-2026-06-17"],
        "non-draft concept addition fails concept validator",
    )
    def non_draft_relation(s: str) -> str:
        lines = []
        changed = False
        for line in s.splitlines():
            if not changed and 'relation-SCIENCE-ACADEMIA-RESEARCH-2026-06-17' in line:
                obj = json.loads(line)
                obj["status"] = "accepted"
                line = json.dumps(obj, ensure_ascii=False)
                changed = True
            lines.append(line)
        return "\n".join(lines)+"\n"
    mutate_file(
        ROOT / "library/relations/relation-assets.jsonl",
        non_draft_relation,
        ["python3", "tools/validate/relations.py", "--repo", ".", "--batch-id", "relation-SCIENCE-ACADEMIA-RESEARCH-2026-06-17", "--min-count", "10"],
        "non-draft relation addition fails relation validator",
    )
    wrapper = ROOT / "tools/query/themes/science_academia_research.py"
    backup = wrapper.with_suffix(".py.restore")
    try:
        shutil.move(wrapper, backup)
        record_failure_diagnostics(
            "early social route without stable query helper fails with visible diagnostics",
            run(["python3", "tools/query/social_topics.py", "科学主义", "--limit", "1"]),
        )
    finally:
        if backup.exists():
            shutil.move(backup, wrapper)
    out = ROOT / "qa/science-academia-research/negative-tests-summary.json"
    out.write_text(json.dumps({"status":"PASS", "tests":RESULTS}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status":"PASS", "count":len(RESULTS), "path":str(out.relative_to(ROOT))}, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
