#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Callable, cast

ROOT = Path(__file__).resolve().parents[2]


def load_validate_theme() -> Callable[[Path, str], dict]:
    validator = ROOT / "tools/lib/theme_validation.py"
    spec = importlib.util.spec_from_file_location("theme_validation", validator)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load theme validator: {validator}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return cast(Callable[[Path, str], dict], module.validate_theme)


validate_theme = load_validate_theme()

SOCIAL_THEMES = [
    "labor-workplace-precarity",
    "education-examination-credentialism",
    "science-academia-research",
    "family-intimacy-reproduction",
    "consumption-desire-lifestyle",
    "media-platform-public-opinion",
    "governance-law-bureaucracy",
    "class-youth-generational-anxiety",
    "psychological-distress-social-symptom",
    "urban-housing-migration-space",
    "health-body-risk-society",
]

STRICT_FINAL_VALIDATORS = {
    "science-academia-research": ROOT / "tools/validate/themes/science_academia_research.py",
}


def normalize_json(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): normalize_json(v) for k, v in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [normalize_json(v) for v in value]
    return value


def validate_social_theme(repo: Path, slug: str, final: bool) -> dict:
    strict = STRICT_FINAL_VALIDATORS.get(slug)
    if final and strict:
        spec = importlib.util.spec_from_file_location(f"validate_{slug.replace('-', '_')}", strict)
        if spec is None or spec.loader is None:
            return {"status": "FAIL", "theme": slug, "errors": [f"cannot load strict final validator: {strict}"]}
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = normalize_json(module.validate(repo, final=True))
        return cast(dict, result)
    return validate_theme(repo, slug)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate social-topic theme packages")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    results = [validate_social_theme(repo, slug, args.final) for slug in SOCIAL_THEMES]
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
