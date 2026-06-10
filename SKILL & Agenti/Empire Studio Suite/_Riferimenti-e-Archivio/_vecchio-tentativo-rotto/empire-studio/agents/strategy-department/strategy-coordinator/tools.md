# Strategy Coordinator — Tools

## Tool Principali
1. **ReadStrategyRegistry** — Legge STRATEGY-REGISTRY.md e strategie specifiche.
2. **ConsultSpecialist** — Chiama Department Strategist o Content-Type Strategist per input complesso.
3. **CreateStrategyManifest** — Genera il manifest JSON + markdown.
4. **WriteToMemory** — Usa Memory Management (checkpoint + decision) per registrare la scelta.
5. **HandoffToConductor** — Passa il manifest.

## Schema Strategy Manifest (esempio)
```json
{
  "run_id": "...",
  "selected_strategies": {
    "department": "YouTube Department Strategy v1.0",
    "content_type": "Design System Content Strategy v1.1",
    "wiki_implementation": "Visual-Heavy Reference"
  },
  "rules": ["frame ogni capitolo", "descrizioni visive dettagliate >50 parole"],
  "rationale": "Input è video lungo YouTube su design system",
  "trace": "CP-XXX, decision da Coordinator"
}
```

## Script di Supporto
- `scripts/generate_manifest.py` (da creare nello step 4)

**Trace**: Tools per applicare strategie specifiche come richiesto.