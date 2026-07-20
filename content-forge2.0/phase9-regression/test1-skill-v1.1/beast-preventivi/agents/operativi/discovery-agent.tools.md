# Tools

## qualification_scorer

- **Description**: Calcola fit-score 0-1 del prospect basato su 5 fattori (budget, urgency, decision-maker, problem-clarity, history)
- **When to use**: Dopo il blocco budget, prima di scrivere il report finale
- **Input schema**:
```json
{
  "type": "object",
  "properties": {
    "budget_alignment": {"type": "number", "minimum": 0, "maximum": 1},
    "urgency": {"type": "number", "minimum": 0, "maximum": 1},
    "decision_maker_present": {"type": "boolean"},
    "problem_clarity": {"type": "number", "minimum": 0, "maximum": 1},
    "history_with_similar_services": {"type": "boolean"}
  },
  "required": ["budget_alignment", "urgency", "decision_maker_present"]
}
```
- **Output schema**:
```json
{
  "fit_score": "number 0-1",
  "recommendation": "string: 'proceed'|'wait'|'disqualify'",
  "reasoning": "string"
}
```
- **Side effects**: nessuno (calcolo deterministico)
- **Errors possible**: `invalid_input`, `missing_required_field`
- **Example invocation**:
```json
{"budget_alignment": 0.8, "urgency": 0.6, "decision_maker_present": true, "problem_clarity": 0.9}
```

## red_flag_detector

- **Description**: Analizza la risposta del prospect e cerca i 5 segnali non-fit
- **When to use**: Su ogni risposta del prospect, automaticamente
- **Input schema**:
```json
{
  "type": "object",
  "properties": {
    "prospect_response": {"type": "string"},
    "context": {"type": "string", "description": "What question prompted this response"}
  },
  "required": ["prospect_response"]
}
```
- **Output schema**:
```json
{
  "red_flags_detected": ["array of flag names"],
  "severity": "low|medium|high",
  "recommendation": "string"
}
```
- **Errors possible**: `empty_response`
