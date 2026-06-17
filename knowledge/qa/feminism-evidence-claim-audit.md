# Feminism Evidence-Claim Audit

- status: PASS
- date: 2026-06-16 CST
- method: spot-check evidence marker chains plus validator-wide exact-substring checks.

## Marker-chain spot checks

- false feminism / female essence: `ev:feminism:0090:01` -> `term:女性本质:s07` -> `rel:feminism:001` -> `w10:arg:0090:feminism-false-feminism-female-essence`.
- misogyny / patriarchal fantasy: `ev:feminism:0061:01` -> `term:厌女症:s07` -> `w10:arg:0061:feminism-misogyny-patriarchal-fantasy`.
- sexual liberation / erotic economy: `ev:feminism:0085:01` -> `term:性解放:s07` -> `rel:feminism:011` -> `w10:proc:0085:feminism-sexual-liberation-erotic-economy`.
- love / marriage / intimacy: `ev:feminism:0055:01` and `ev:feminism:0184:02` -> `term:爱情意识形态:s07` / `term:婚姻:s07` -> `w10:arg:0055:feminism-love-romance-marriage` / `w10:arg:0184:feminism-love-romance-marriage`.
- women/children/economic liberation: `ev:feminism:0330:01` -> `term:妇女解放:s07` -> `rel:feminism:027` -> `w10:case:0330:feminism-women-children-liberation`.
- family/social reproduction: `ev:feminism:0322:01`, `ev:feminism:0323:01`, `ev:feminism:0295:02` -> `term:社会再生产:s07` / `term:经济生活组织:s07`.

## Validator-backed claims

`python3 knowledge/scripts/validate_feminism_theme.py --repo . --final` checks:

1. manifest row/segment/toc/clean-path consistency;
2. all 309 evidence-bank quotes as exact substrings of declared clean files;
3. W3 batch count/status/evidence exactness;
4. W5 batch count/status/type/evidence exactness;
5. W10 feminism card count/status/evidence exactness;
6. synthesis evidence marker validity;
7. navigation/state markers;
8. protected-corpus sha checks;
9. append-only batch boundaries against `HEAD`.

Latest result: PASS in `.omx/tmp/feminism_full_validation_final.log`.
