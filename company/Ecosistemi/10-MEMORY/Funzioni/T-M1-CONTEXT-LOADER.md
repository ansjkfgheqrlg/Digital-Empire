> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 (Reparto M1 — Recall & Pre-Task Gate)

# T-M1-CONTEXT-LOADER — Funzione Context Loader

> Layer funzione condiviso · Livello: L3 · Usato da: ME-A01 context-loader, ME-A02 relevance-scorer
> Ecosistema: `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/10-MEMORY/BACKBONE.md`

---

## Identità funzione

| Campo | Valore |
|---|---|
| Funzione ID | T-M1-CONTEXT-LOADER |
| Capability servite | context-load, recall, relevance-score, pre-task-gate |
| Reparto owner | M1 — Recall & Pre-Task Gate |
| Stato | ATTIVO (pattern #13 memory-first obbligatorio) |
| Tier modello | haiku (lettura file) + sonnet (scoring ambiguo) |
| Trigger | HC-ME-PRE ricevuto dal ME-A00 |

---

## Contratto funzione (non negoziabile)

| Operazione | Input | Output |
|---|---|---|
| `load_context(task)` | `{task_id, ecosistema, keywords[]}` | context-pack JSON |
| `score_relevance(items, task)` | lista CP/ADR/pattern + task | items ordinati per score desc |
| `check_contradictions(task, adrs)` | task proposto + ADR attivi | `{ok: bool, conflitti: []}` |

---

## Flusso operativo (HC-ME-PRE)

```
HC-ME-PRE ricevuto {task_id, ecosistema, descrizione, keywords}
  1. Leggi company/Memory/INDEX.md → lista CP/ADR per ecosistema target
  2. Leggi company/Memory/STATO-EMPIRE.md → lavori in corso, blocchi attivi
  3. Filtra CP per keywords → ultimi N checkpoint pertinenti (N ≤ 10)
  4. Filtra ADR per stato = ATTIVO → solo regole ancora valide
  5. memory_search(AgentDB namespace "memory/", keywords) → pattern rilevanti
  6. score_relevance() → ordina, taglia rumore
  7. check_contradictions() → se conflitto con ADR ATTIVO → STOP + escalation Board
  8. Assembla context-pack → ritorna al team richiedente
```

---

## Struttura context-pack (output)

```json
{
  "task_id": "YYYYMMDD-XXX",
  "generato": "YYYY-MM-DDTHH:MM:SSZ",
  "stato_empire": "stringa RIPRESA DA: attuale",
  "checkpoint_rilevanti": [
    {"cp_id": "CP-YYYYMMDD-NNN", "titolo": "...", "score": 0.92, "path": "..."}
  ],
  "adr_attivi": [
    {"adr_id": "ADR-NNN", "decisione": "...", "conseguenze": "..."}
  ],
  "pattern_agentdb": [
    {"chiave": "...", "contenuto": "...", "score": 0.87}
  ],
  "contraddizioni": [],
  "ok_per_procedere": true
}
```

---

## Regole operative

1. **Gate bloccante**: se `ok_per_procedere = false` → il task NON può partire. Escalation a Board via hive-mind, non decidere unilateralmente.
2. **Max item**: context-pack non supera 10 CP + 5 ADR + 10 pattern (evita context overflow).
3. **Stato sempre dal filesystem**: STATO-EMPIRE.md è letto ogni volta, mai cachato in memoria volatile.
4. **Vietato inferire**: se il campo `ecosistema` manca nel HC-ME-PRE → richiedere al mittente, non assumere.

---

## Connessioni

- `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/10-MEMORY/BACKBONE.md` — namespace AgentDB `memory/`
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A01-context-loader.md` — agente che esegue questa funzione
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A02-relevance-scorer.md` — agente di scoring
- `company/Ecosistemi/10-MEMORY/Workflow/WF-PRETASK.md` — workflow che orchestra questa funzione
- `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` §3, §5

*Fonte: dossier 09 §3 (M1), §5 (WF-PRETASK) · Aggiornato: 2026-06-12*
