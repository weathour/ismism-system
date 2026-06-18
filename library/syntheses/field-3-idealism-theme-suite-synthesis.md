# Field 3 / 观念论 theme suite synthesis

- status: evidence-linked suite synthesis
- date: 2026-06-18
- source boundary: `corpus/registry/toc.csv` rows 187-275
- theme packages: `phenomenology`, `german-idealism-dialectics`, `existentialism-ethics-meaning`, `semiotics-language-hermeneutics`

This synthesis is a navigation layer over four validator-backed theme packages. It is not an external history of phenomenology, German idealism, existentialism, semiotics, or hermeneutics. All claims below should be checked through the row manifests and evidence banks of the four packages.

## Suite boundary

Field 3 is organized around row 187 as the overview context and four internal sections:

- rows 188-209: 3-1 现象学, absorbed by `library/themes/phenomenology/`.
- rows 210-231: 3-2 德国观念论, absorbed by `library/themes/german-idealism-dialectics/`.
- rows 232-253: 3-3 生存论, absorbed by `library/themes/existentialism-ethics-meaning/`.
- rows 254-275: 3-4 符号学, absorbed by `library/themes/semiotics-language-hermeneutics/`.

Each package currently contains 36 reviewed rows and 58 exact quote records: 22 own-section core rows, row 187 as context, 10 Field 3 bridge rows, and 3 excluded/noise controls.

## Four-package route

### 1. Phenomenology

`phenomenology` asks how ISMISM treats phenomenology as a method problem: intentionality, reduction, lifeworld, intersubjectivity, body, worldly experience, and ontological phenomenology. Core evidence starts in rows 188-209, with evidence ids such as `ev:phenomenology:0188:01`, `ev:phenomenology:0190:01`, `ev:phenomenology:0200:01`, and `ev:phenomenology:0208:01`.

### 2. German idealism and dialectics

`german-idealism-dialectics` asks how ISMISM organizes Kant, Fichte, Schelling, Hegel, freedom, system, absolute spirit, and dialectical negation. Core evidence starts in rows 210-231, with evidence ids such as `ev:german-idealism:0210:01`, `ev:german-idealism:0212:01`, `ev:german-idealism:0217:01`, `ev:german-idealism:0227:01`.

### 3. Existentialism, ethics, and meaning

`existentialism-ethics-meaning` asks how ISMISM treats existentialism and 生存论 as a problem of existence, authenticity, freedom, choice, ethics, nihilism, and meaning. Core evidence starts in rows 232-253, with evidence ids such as `ev:existentialism:0232:01`, `ev:existentialism:0234:01`, `ev:existentialism:0239:01`, `ev:existentialism:0249:01`.

### 4. Semiotics, language, and hermeneutics

`semiotics-language-hermeneutics` asks how ISMISM treats sign systems, structuralism, post-structuralism, discourse, text, difference, language, and interpretation. Core evidence starts in rows 254-275, with evidence ids such as `ev:semiotics:0254:01`, `ev:semiotics:0256:01`, `ev:semiotics:0266:01`, `ev:semiotics:0271:01`.

## Bridge rules

- A bridge row does not transfer primary ownership away from its own Field 3 section.
- Bridge claims must cite the relevant package evidence id and should stay narrower than the quote.
- The suite does not change `tools/query/social_topics.py`; these are direct theme routes, not social-topic routes.
- Concept, relation, and close-reading additions are deferred in this pass. The packages are queryable and validator-backed without promoting new W3/W5/W10 records.

## Query entry points

```bash
python3 tools/query/themes/phenomenology.py 现象学 --limit 3
python3 tools/query/themes/german_idealism_dialectics.py 辩证法 --limit 3
python3 tools/query/themes/existentialism_ethics_meaning.py 生存论 --limit 3
python3 tools/query/themes/semiotics_language_hermeneutics.py 符号学 --limit 3
```

## Validation entry points

```bash
python3 tools/validate/themes/phenomenology.py --repo . --final
python3 tools/validate/themes/german_idealism_dialectics.py --repo . --final
python3 tools/validate/themes/existentialism_ethics_meaning.py --repo . --final
python3 tools/validate/themes/semiotics_language_hermeneutics.py --repo . --final
```
