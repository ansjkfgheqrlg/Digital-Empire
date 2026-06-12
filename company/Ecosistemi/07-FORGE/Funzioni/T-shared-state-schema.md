> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.2 Brain · 06-ECOSISTEMI-CORE.md sez. 07 L4

# T-shared-state-schema — Funzione L4: Schema Stato Condiviso del Team

**Ecosistema:** 07-FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Workflow:** WF-TEAM-NEW

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Definire il **schema dello stato condiviso** di un team: quali informazioni i membri del
team leggono/scrivono nel Brain (AgentDB, namespace per team), con quali chiavi tipate e
con quale semantica. Senza shared_state schema esplicito, i worker lavorano in isolamento
e perdono il contesto tra un passo e l'altro.

---

## Il problema che risolve

In un team multi-agente, ogni worker ha accesso alla stessa "memoria di lavoro" del team.
Senza schema:
- Worker-2 non sa cosa ha prodotto Worker-1
- Il coordinator non ha un unico punto di verità sullo stato del task
- I fallimenti diventano invisibili (nessuno sa cosa è stato completato)

Con shared_state schema: ogni membro sa esattamente cosa leggere e scrivere.

---

## Schema tipo (da adattare per ogni team)

```json
{
  "team_id": "T-nome-team",
  "namespace": "ecosistema/team-id",
  "schema_version": "1.0",
  "chiavi": [
    {
      "chiave": "task_brief",
      "tipo": "string",
      "scritto_da": "coordinator",
      "letto_da": ["worker-1", "worker-2"],
      "descrizione": "descrizione del task principale ricevuto dall'esterno"
    },
    {
      "chiave": "output_worker_1",
      "tipo": "object",
      "scritto_da": "worker-1",
      "letto_da": ["coordinator", "worker-2"],
      "descrizione": "output prodotto da worker-1 (formato: {...})"
    },
    {
      "chiave": "status",
      "tipo": "enum",
      "valori": ["pending", "in_progress", "done", "failed"],
      "scritto_da": "coordinator",
      "letto_da": "tutti",
      "descrizione": "stato corrente del task"
    },
    {
      "chiave": "errori",
      "tipo": "array",
      "scritto_da": ["coordinator", "tutti i worker"],
      "letto_da": ["coordinator", "escalation-target"],
      "descrizione": "log errori accumulati durante il task"
    }
  ]
}
```

---

## Integrazione con il Brain (Backbone)

Lo shared_state vive nel namespace AgentDB del team:
- **Store**: `ruflo memory_store --namespace <eco>/team-id -k <chiave> --value <valore>`
- **Read**: `ruflo memory_search --namespace <eco>/team-id "<chiave>"`
- **Fallback** (senza daemon): mirror in `company/runtime/brain/<eco>/team-id.jsonl`

---

## Regole di design

1. **Una chiave = un dato atomico** — non mescolare dati diversi nella stessa chiave
2. **Scritto_da sempre uno solo** — due worker non scrivono la stessa chiave (race condition)
3. **Chiave `status` sempre presente** — il coordinator deve poter monitorare lo stato
4. **Chiave `errori` sempre presente** — traccia di ogni fallimento per escalation e ReasoningBank

---

## KPI

| Metrica | Target |
|---|---|
| Team senza schema shared_state definito | 0 dopo WF-TEAM-NEW |
| Race condition (due writer sulla stessa chiave) | 0 |
| Task falliti senza voce in `errori` | 0 |
| Namespace non inizializzati per team attivi | 0 |
