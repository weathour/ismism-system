# ismism锛氬彲鎵ц钃濆浘

## 1. 鐩爣

`ismism` 涓嶆槸鍗曚竴鎻愮ず璇嶏紝鑰屾槸涓€涓笁灞傜郴缁燂細

1. `Skill Layer`
   - 鍦ㄤ换鎰忔柊瀵硅瘽閲岃Е鍙?   - 鏀寔璇婃柇銆佹煡璇€佹瘮杈冦€佽拷韪€佹洿鏂?2. `Atlas Layer`
   - 鎶?`363` 浠芥枃鏈彁绾负鍙绱㈣妭鐐逛笌鍏崇郴
   - 淇濆瓨绋冲畾瀹氫綅銆佹瀹氫綅銆佸姩鎬佸叧绯讳笌璇佹嵁
3. `Corpus Layer`
   - 淇濆瓨鍘熷瀵艰埅鍜屾媶鍒嗘枃鏈?   - 浣滀负鎵€鏈夌粨璁虹殑璇佹嵁鍚庣

## 2. 椤跺眰鐩綍

```text
_bundle\source
鈹溾攢鈹€ 鐩綍绱㈠紩_缁撴瀯鍖?csv
鈹溾攢鈹€ split_md/
鈹溾攢鈹€ split_pdf/
鈹溾攢鈹€ Zhuyi_Matrix_Engine/
鈹?  鈹溾攢鈹€ Phase0_Corpus/
鈹?  鈹溾攢鈹€ Phase1_Concepts/
鈹?  鈹溾攢鈹€ Phase2_Mechanics/
鈹?  鈹溾攢鈹€ Phase3_Applications/
鈹?  鈹溾攢鈹€ Phase4_Skill_Suite/
鈹?  鈹溾攢鈹€ Static_Atlas/
鈹?  鈹斺攢鈹€ Atlas_DB/
鈹斺攢鈹€ _skill_build/
    鈹斺攢鈹€ ismism/
```

## 3. 鏁版嵁妯″瀷

### 3.1 `Atlas_DB/nodes.jsonl`

姣忚涓€涓妭鐐癸細

```json
{
  "id": "person.kafka",
  "type": "Person",
  "label": "鍗″か鍗?,
  "aliases": ["Kafka", "寮楀叞鑼峰崱澶崱"],
  "canonical_position": "3-3-4-2",
  "coarse_family": "3-3-4",
  "distilled_code": "F3-O3-E4-T2",
  "canonical_label": "铏氭瀯鐨勭敓瀛樿鈫掑幓涓績鍖栫殑绉戝眰涓讳箟",
  "summary": "鎶婄粷瀵硅€呭幓涓讳綋鍖栧苟鎻湶鏃犲ご绉戝眰绉╁簭鐨勬枃瀛︽€х敓瀛樿鑰呫€?,
  "why_assigned": "鎬诲涔犱笌瀛愬瀷鏍囬閮界洿鎺ユ妸鍗″か鍗℃斁鍦?-3-4-2銆?,
  "secondary_positions": ["3-3-4-1"],
  "confidence": "high",
  "status": "stable",
  "evidence_ids": ["ev.kafka.1", "ev.kafka.2"]
}
```

### 3.2 `Atlas_DB/relations.jsonl`

姣忚涓€涓叧绯伙細

```json
{
  "id": "rel.kafka.answers.ivan",
  "source": "person.kafka",
  "relation": "answers",
  "target": "figure.ivan-karamazov",
  "summary": "鍗″か鍗″紡缁撴瀯琚綔鑰呰В閲婁负瀵瑰畻鏁欏ぇ娉曞畼闂鐨勫洖绛斻€?,
  "confidence": "medium",
  "evidence_ids": ["ev.kafka.3"]
}
```

### 3.3 `Atlas_DB/evidence.jsonl`

姣忚涓€涓瘉鎹储寮曪細

```json
{
  "id": "ev.kafka.1",
  "entity_ids": ["person.kafka"],
  "path": "split_md/3_瑙傚康璁篲浣滀负涓€涓幇浠ｄ汉_璇ユ€庢牱鎬濊€冨摬瀛?3-3_澶嶄範璇?0233_3-3_澶嶄範璇綺p6008.md",
  "line": 193,
  "quote": "鍗″か鍗″湪杩欓噷鍒欐槸涓€绉嶅幓涓績鍖栫殑绉戝眰鍒?
}
```

### 3.4 `Atlas_DB/file_distillates.jsonl`

姣忚瀵瑰簲涓€涓簮鏂囦欢鐨勬彁绾崱锛?
- `source_path`
- `toc_id`
- `title`
- `primary_position`
- `atlas_candidates`
- `relation_candidates`
- `summary`
- `confidence`

### 3.5 `Atlas_DB/unresolved_queue.jsonl`

淇濆瓨鏈畾鍨嬪璞★細

- 鍒悕鍐茬獊
- 涓诲畾浣嶅啿绐?- 璇佹嵁涓嶈冻
- 鍏崇郴涓嶆槑纭?
## 4. 鑺傜偣绫诲瀷

- `Person`
- `Text`
- `School`
- `Structure`
- `Mechanism`
- `Phenomenon`
- `PracticeUnit`
- `Problem`
- `Collective`

## 5. 鍏崇郴绫诲瀷

- `belongs_to`
- `represented_by`
- `criticizes`
- `answers`
- `transitions_to`
- `mediates`
- `locks`
- `short_circuits_to`
- `inherits_from`
- `inverts`
- `corresponds_to`
- `contrasts_with`
- `requires_practice_unit`
- `secondary_example_of`

## 6. Skill 鎵ц妯″紡

### `diagnose`

- 杈撳叆涓€涓璞?- 杈撳嚭 `F-O-E-T` 璇婃柇鎶ュ憡

### `lookup`

- 浼樺厛鏌?`Atlas_DB`
- 鍛戒腑鍚庤緭鍑洪潤鎬佸崱涓庤瘉鎹?
### `compare`

- 姣旇緝涓や釜鎴栧涓璞?- 杈撳嚭鍏卞悓鐐广€佸樊寮備綅銆佸姩鎬佸垎鍙?
### `trace`

- 杩借釜涓€涓璞′笌鍏朵粬鑺傜偣鐨勫叧绯婚摼

### `update`

- 褰?Atlas 涓嶅瓨鍦ㄧǔ瀹氭潯鐩椂
- 鍩轰簬璇枡鍒嗘瀽浜у嚭鍊欓€?- 鍐欏洖 `nodes / relations / evidence / unresolved`

### `build`

- 闈㈠悜鎵归噺鏋勫缓
- 涓哄皻鏈彁绾殑婧愭枃浠剁敓鎴?`file_distillates`

## 7. 杩愯浼樺厛绾?
浠讳綍鏂拌姹傞兘鎸変互涓嬮『搴忔墽琛岋細

1. 鏌?`Atlas_DB/nodes.jsonl`
2. 鏌?`Atlas_DB/relations.jsonl`
3. 鏌?`Atlas_DB/file_distillates.jsonl`
4. 鍥炶 `Phase1-4` 瑙勫垯鏂囦欢
5. 蹇呰鏃跺洖 `鐩綍绱㈠紩_缁撴瀯鍖?csv`
6. 鏈€鍚庡洖 `split_md/`

## 8. 鑷垜瀹屽杽鏈哄埗

### 鍘熷垯

- 鏂板垎鏋愪笉鑳界洿鎺ヨ鐩栨棫缁撹
- 蹇呴』淇濈暀锛?  - 鏃х粨璁?  - 鏂扮粨璁?  - 璇佹嵁
  - 鍙樻洿鐞嗙敱

### 鍏蜂綋娴佺▼

1. 鏂板璇濆懡涓湭鐭ュ璞?2. 鎶€鑳藉厛鍋氱幇鍦鸿瘖鏂?3. 鑻ヨ揪鍒扳€滅ǔ瀹氳В閲娾€濋槇鍊硷細
   - 鍐欏叆 `nodes.jsonl`
   - 鍐欏叆 `evidence.jsonl`
   - 濡傚瓨鍦ㄥ姩鎬佸叧绯伙紝鍐欏叆 `relations.jsonl`
4. 鑻ヨВ閲婂皻涓嶇ǔ锛?   - 鍐欏叆 `unresolved_queue.jsonl`
5. 鑻ユ柊缁撹涓庢棫缁撹鍐茬獊锛?   - 鍐欏叆 `changes.jsonl`

## 9. 鏋勫缓娴佹按绾?
### Stage 1锛氱珷鑺傛彁绾?
- 涓烘瘡涓?`split_md` 鏂囦欢鐢熸垚锛?  - `primary_position`
  - `summary`
  - `atlas_candidates`
  - `relation_candidates`

### Stage 2锛氳妭鐐瑰綊骞?
- 鍘婚噸鍒悕
- 鍚堝苟閲嶅鑺傜偣
- 鏍囪涓诲畾浣嶄笌娆″畾浣?
### Stage 3锛氬叧绯荤患鍚?
- 姹囨€昏法鏂囦欢鍏崇郴
- 鐢熸垚鍏ㄥ眬杈归泦

### Stage 4锛氬彂甯?Atlas

- 杈撳嚭绋冲畾鑺傜偣琛?- 杈撳嚭绋冲畾鍏崇郴琛?- 杈撳嚭璇佹嵁绱㈠紩
- 杈撳嚭鏈喅闃熷垪

## 10. 褰撳墠钀藉湴浼樺厛绾?
### 绗竴浼樺厛

- 寤虹珛绋冲畾 Skill
- 寤虹珛 Atlas 鏁版嵁妯″瀷
- 寤虹珛鏌ヨ涓庢洿鏂拌剼鏈?
### 绗簩浼樺厛

- 鎶婇珮浠峰€间汉鐗┿€佹枃鏈€佹祦娲惧仛鎴愮涓€鎵圭ǔ瀹氳妭鐐?- 浼樺厛瑕嗙洊锛?  - 鍗″か鍗?  - 闄€鎬濆Ε鑰跺か鏂熀
  - 鍔犵吉
  - 鍗氬皵璧柉
  - 灏奸噰
  - 娴峰痉鏍煎皵
  - 钀ㄧ壒
  - 椹厠鎬?
### 绗笁浼樺厛

- 瀵?`363` 浠芥枃浠惰繘琛屽垎鎵?`file_distillates` 鐢熶骇

## 11. 瀹屾垚鏍囧織

浠ヤ笅鏉′欢婊¤冻鏃讹紝`ismism` 鎵嶇畻杩涘叆鍙暱鏈熶娇鐢ㄧ姸鎬侊細

- Skill 宸插畨瑁呭埌鍏ㄥ眬 `skills`
- Skill 鑳藉湪鏂板璇濅腑鐙珛瑙﹀彂
- Atlas 鍙煡璇?- Atlas 鍙閲忔洿鏂?- 鑷冲皯瀛樺湪涓€鎵圭ǔ瀹氳妭鐐瑰拰鍏崇郴
- 鑳藉鏈煡瀵硅薄杩涜璇婃柇骞跺啓鍥炴彁绾眰

