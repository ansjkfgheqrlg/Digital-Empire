# Handoff Rules

> Matrice dei passaggi tra agenti. Ogni handoff usa il `communication_protocol.md` envelope.

| # | From | To | What (payload) | When (trigger) | Format | Validation |
|---|------|-----|----------------|----------------|--------|-----------|
| 1 | user | coordinator | task description | user submits | free-text | non vuoto, ≤1000 char |
| 2 | coordinator | technique-selector | parsed task + complexity hint | dopo turn 1 coordinator | JSON envelope | `task_id`, `parsed_intent` non null |
| 3 | technique-selector | coordinator | techniques + reasoning | dopo analisi | JSON envelope | array `techniques` non vuoto, ogni item con `name`+`reason` |
| 4 | coordinator | prompt-composer | techniques + constraints + examples count | dopo turn 3 | JSON envelope | `techniques` array, `constraints` object |
| 5 | prompt-composer | coordinator | prompt draft | composition done | JSON envelope | `prompt_text` non vuoto, ≤1500 parole |
| 6 | prompt-composer | coordinator | clarification request | composer ha dubbio | JSON envelope (type=clarify) | `question` non vuoto |
| 7 | coordinator | technique-selector | re-route on clarify | dopo type=clarify | JSON envelope (type=re-eval) | reference all'original task_id |
| 8 | coordinator | eval-designer | prompt + task type | dopo prompt draft OK | JSON envelope | `prompt_text` + `task_type` |
| 9 | eval-designer | coordinator | 3-5 test cases | tests designed | JSON envelope | `test_cases` array, ognuno con `input`+`expected_behavior` |
| 10 | coordinator | user | final bundle (prompt + reasoning + tests) | tutti i workers done | markdown | TOC + 3 sezioni canoniche |

## Validation rules

```python
# Validator pseudocode
def validate_handoff(envelope: dict, from_agent: str, to_agent: str) -> list[str]:
    errors = []
    if envelope.get("from_agent") != from_agent: errors.append("from_agent mismatch")
    if envelope.get("to_agent") != to_agent: errors.append("to_agent mismatch")
    if not envelope.get("task_id"): errors.append("missing task_id")
    if not envelope.get("trace_id"): errors.append("missing trace_id")
    # Per-rule validation per payload (vedi tabella sopra)
    ...
    return errors
```

## Timeout

- Per ogni handoff: 60s default
- Coordinator può estendere a 120s per task multi-paragrafo
- Se timeout → retry 1x, poi escalation umana
