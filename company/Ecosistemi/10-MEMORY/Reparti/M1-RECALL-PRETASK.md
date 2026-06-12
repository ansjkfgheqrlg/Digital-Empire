> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 M1

# L2 — M1 · RECALL & PRE-TASK GATE (Il Reparto Più Critico di MEMORY)

**Ecosistema:** 10-MEMORY · **Direttore:** ME-Conductor
**Workflow L3:** T-M1.1 Context Loader · T-M1.2 Relevance Scorer
**Connessione:** [[../ECOSISTEMA.md]] · [[../BACKBONE.md]]

## Missione

Nessun task parte "al buio". M1 garantisce che ogni team della holding, prima di
iniziare qualsiasi lavoro non banale, riceva un **context-pack**: lo stato corrente
dell'azienda, i checkpoint rilevanti, le decisioni ADR attive, i pattern AgentDB.
È il gate che rende il memory-first (pattern #13) non una regola scritta ma
un meccanismo bloccante.

## Il Context-Pack

Il context-pack è l'output standard di M1. Contiene:

```yaml
context_pack:
  stato_empire: "snippet da STATO-EMPIRE.md (fase corrente, blocchi, prossime azioni)"
  checkpoint_rilevanti:
    - "CP-20260611-003 — Backbone F2 completato"
  adr_attivi:
    - "ADR-002 memory-first: PRIMA di ogni task interroga MEMORY"
    - "ADR-003 wrap-mai-riscrittura: non toccare script attivi"
  pattern_agentdb:
    - "p-001: daemon Ruflo va giù su Windows — usa bootstrap auto-riparante"
  contraddizioni_rilevate: []
  segnalazione: null
```

Se `contraddizioni_rilevate` non è vuoto → task BLOCCATO, escalation al Board.

## Come si attiva

**Handoff HC-ME-PRE (inbound, bloccante):**
```json
{
  "task_id": "T-YYYYMMDD-NNN",
  "ecosistema": "01-AGENCY",
  "descrizione": "preparare preventivo cliente X",
  "keywords": ["preventivo", "agency", "cliente"]
}
```

**Risposta (sincrona, il task attende questa risposta prima di partire):**
```json
{
  "task_id": "T-YYYYMMDD-NNN",
  "context_pack": { "..." },
  "autorizzato": true,
  "note_bloccanti": []
}
```

## Funzioni L4

| Team L4 | Funzione | Descrizione |
|---|---|---|
| T-M1.1 Context Loader | carica INDEX + STATO + CP/ADR pertinenti + `memory_search` | seleziona i contenuti da includere nel pack |
| T-M1.2 Relevance Scorer | ordina per rilevanza, taglia rumore, segnala contraddizioni | filtra perché il pack sia leggibile (<30s) |

## KPI

| Metrica | Target |
|---|---|
| Task non banali preceduti da context-pack | ≥ 95% |
| Tempo di produzione context-pack | ≤ 30s |
| Contraddizioni ADR rilevate prima del task | 100% |
| Task bloccati per contraddizione ADR | immediati (0 bypass) |

## Escalation / Failure handling

- M1 non risponde entro 30s → il task si ferma in attesa; non parte mai senza contesto.
- Contraddizione rilevata con ADR attivo → task BLOCCATO + escalation Board. L'agente
  richiedente riceve il motivo del blocco e il riferimento all'ADR.
