# Row 176 Clean Redo Audit

- audited_at: 2026-06-17 12:23 CST
- record_status: canonical
- target: `row_id=176`, `toc_id=2-4-2-4`
- clean_path: `split_md_clean/2_形而上学_古代贵族的精神冒险_背景性的符号秩序与它自己的对立_比下_形而下学_有余_比上_观/2-4_反形而上学_学哲学必须绕开的陷阱_嘴巴上不承认自己是形而上学的形而上学/2-4-2_实证主义_为人性筑起圣坛_科学哲学_社会学创始人孔德的形而上学/2-4-2-4_科学的实证主义_马赫的蛇皮哲学_蕴含着巨大危险_被逻辑实证主义误解_也算是因祸得/0176_2-4-2-4_科学的实证主义_马赫的蛇皮哲学_蕴含着巨大危险_被逻辑实证主义误解_也算是因祸得福_p4607.md`

## Result

PASS.

The old clean file was identical to raw Markdown. It has been replaced with a high-fidelity light-cleaned version.

## Method

1. A local Ollama clean attempt was generated in `/tmp` with `gemma4:latest`.
2. That LLM output was rejected because spot audit found terminology drift, including changes such as `2字头` → `两个字头` and `联结` → `连接`.
3. The accepted clean file was produced by deterministic high-fidelity cleanup:
   - preserve all raw non-empty text lines as substrings;
   - repair obvious hard line-wraps such as split words;
   - normalize trailing whitespace and page structure;
   - preserve terms, numbering, and row identity;
   - keep all `## Page N` headings in original order.

## Evidence

| Check | Result |
|---|---:|
| page headings preserved | 27 / 27 |
| page order equal to raw | true |
| raw non-empty line substrings missing from clean | 0 |
| prior W3 row176 quote still present | true |
| LLM/prompt artifacts present | false |
| clean chars | 12874 |
| clean lines | 88 |
| clean sha256 | `da702727ce9216e78bac041eaa0763f5adad9662435880c05e298f7eb69bd754` |

Critical preserved quote:

- `因为阿芬那留斯那边主体性是一个常项`

## Regenerated artifacts

- `knowledge/manifests/corpus-manifest.json`
- `knowledge/manifests/segments.jsonl`
- `knowledge/manifests/chunks.jsonl`
- `knowledge/manifests/missing-and-anomalies.md`
- `knowledge/segment-cards/0176_2-4-2-4.md`

## Boundary

- `split_md/` raw text was not edited.
- Only row 176 under `split_md_clean/` was edited.
- `split_pdf/` remains absent as a regenerable derived layer.
