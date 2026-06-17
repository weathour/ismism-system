#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from theme_validation import validate_theme

SOCIAL_THEMES = [
    "labor-workplace-precarity",
    "education-examination-credentialism",
    "family-intimacy-reproduction",
    "consumption-desire-lifestyle",
    "media-platform-public-opinion",
    "governance-law-bureaucracy",
    "class-youth-generational-anxiety",
    "psychological-distress-social-symptom",
    "urban-housing-migration-space",
    "health-body-risk-society",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate social-topic theme packages")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    results = [validate_theme(repo, slug) for slug in SOCIAL_THEMES]
    failures = [r for r in results if r["status"] != "PASS"]
    summary = {
        "status": "PASS" if not failures else "FAIL",
        "themes": len(results),
        "total_manifest_rows": sum(int(r.get("manifest_rows", 0)) for r in results),
        "total_evidence_records": sum(int(r.get("evidence_records", 0)) for r in results),
        "failures": failures,
        "results": results,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"validate_social_topics: {summary['status']} themes={summary['themes']} rows={summary['total_manifest_rows']} evidence={summary['total_evidence_records']} failures={len(failures)}")
        for r in results:
            print(f"- {r['theme']}: {r['status']} rows={r.get('manifest_rows')} evidence={r.get('evidence_records')} quotes={r.get('exact_quotes_checked')} errors={len(r.get('errors', []))}")
            for err in r.get('errors', [])[:5]:
                print(f"  ERROR {err}")
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
