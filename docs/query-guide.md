# Query Guide

## Social topic router

```bash
python3 tools/query/social_topics.py 内卷 --limit 3
```

## Concept query

```bash
python3 tools/query/concept.py 主体
```

## Relation query

```bash
python3 tools/query/relation.py 主体 --limit 3
```

## Position query

```bash
python3 tools/query/position.py 3-4-2
```

## Trace query

```bash
python3 tools/query/trace.py 176 --limit 5
```

## Theme query example

```bash
python3 tools/query/themes/health_body_risk_society.py 身体 --limit 3
python3 tools/query/themes/time_death_finitude_life.py 死亡 --limit 3
```
