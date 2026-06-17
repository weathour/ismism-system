# W1 Recovery Audit — Row 176 & Split Layer Reconstitution

- audited_at: 2026-05-08 18:08 CST
- record_status: canonical
- repository: `/home/weathour/文档/ismism-system`
- related_object: `knowledge/manifests/segments.jsonl`
- objective: 完成 W1 对 row 176 的文本缺失恢复并复核 363/363 可追溯性

## Audit Result

- PASS

| Item | Expectation | Result |
|---|---|---|
| TOC rows | `目录索引_结构化.csv` 共 363 行 | 363 |
| segment records | 形成 363 条 `segments.jsonl` 记录 | 363 |
| text availability | 363 条均为 `text_status=available` | 363 |
| row 176 | `toc_id=2-4-2-4` 可追溯、文本可用 | 通过 |
| chunk coverage | chunks 覆盖全部 available segments | 覆盖 363 |
| `split_md` 实体文件 | 与 TOC 同量 | 363 |
| `split_md_clean` 实体文件 | 与 TOC 同量 | 363 |
| `split_pdf/` | 可选派生层：2026-06-17 cleanup 后不再保留 PDF 分片 | 0 |

## Notes

- `row 176 / 2-4-2-4` 通过页面重建补齐 raw 文本；最初以拷贝方式补齐 clean 文本。
- 2026-06-17 后续修复：row 176 clean 已重做为高保真轻清洗版；页标记顺序保持 1–27，既有 row176 W3 quote 仍逐字命中。
- `chunks.jsonl` 已重新生成并与所有可用 segments 一一对应。
- `knowledge/manifests/missing-and-anomalies.md` 已更新为“无 raw/clean 缺失，`split_pdf/`缺席但可再生”。
