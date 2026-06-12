> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 AGENT-WORKS · L3 WF-TEAM-NEW

# WF-TEAM-NEW — Workflow L3: Creazione Team Canonico L3/L4

**Ecosistema:** 07-FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Forgiare un **team multi-agente canonico** (schema CF: coordinator + workers, I/O espliciti,
acceptance criteria, escalation, shared_state) per una funzionalità L3 o L4 di qualsiasi
ecosistema. Il team è l'unità operativa fondamentale di EMPIRE OS — ogni funzionalità ha
il suo team, nessuna funzionalità è coperta da un agente solitario senza escalation.

---

## Trigger di attivazione

- Un ecosistema dichiara un workflow L3 o funzione L4 senza team assegnato
- OPERATIONS segnala che un processo eseguito manualmente supera la soglia di ripetizione
- FORGE F4 (roadmap): forgiatura team reale (es. T-thumbnail per MULTI-BUSINESS/YT)
- WF-ECOSYSTEM-NEW richiede i team L4 dell'ecosistema nuovo

---

## Schema canonico del team (pattern #1 — non negoziabile)

```
Team <nome> (L3/L4)
├── coordinator         — riceve il task, pianifica, divide, aggrega output, gestisce fallimenti
├── worker-1            — esegue sottocompito specifico
├── worker-2            — esegue sottocompito specifico
├── ...                 — N workers in base alla complessità
└── (opzionale) reviewer — verifica output workers prima di consegnare al coordinator
```

---

## Fasi del workflow

| Fase | Attore | Output | Gate |
|---|---|---|---|
| **T-org-design** | `frg-org-designer` | org chart team: ruoli, responsabilità, confini | ruoli non sovrapposti, ogni worker ha una sola responsabilità |
| **T-handoff-contracts** | `frg-org-designer` + `frg-spec-writer` | handoff contract tra coordinator/workers e verso l'esterno | schema HC-v1 rispettato (acceptance_criteria misurabili) |
| **T-shared-state-schema** | `frg-org-designer` | schema shared_state: cosa il team condivide in memoria | namespace AgentDB dichiarato, chiavi tipate |
| **Spawn agenti** | `frg-spec-writer` + WF-AGENT-NEW | ogni membro del team creato come agente (7-file) | smoke test verde per ogni membro |
| **Integration test** | `frg-eval-runner` | test end-to-end: task reale attraversa l'intero team | output conforme all'acceptance criteria del team |
| **Registrazione** | `frg-hr-registrar` | tutti i membri nel registro-agenti.yaml; team in ECOSISTEMA.md | G-REGISTRY team completo |

---

## Schema handoff contract del team (obbligatorio)

```json
{
  "team_id": "T-nome-team",
  "ecosistema": "XX-ECO",
  "coordinator": "agente-id-coordinator",
  "workers": ["agente-id-1", "agente-id-2"],
  "input_trigger": "cosa attiva il team",
  "acceptance_criteria": ["criterio 1 misurabile", "criterio 2 misurabile"],
  "escalation": "a chi va il task se fallisce dopo N tentativi",
  "shared_state_namespace": "namespace/team-id"
}
```

---

## Funzioni L4 operative in questo workflow

- `T-org-design` (`Funzioni/T-org-design.md`) — disegno org chart
- `T-handoff-contracts` (`Funzioni/T-handoff-contracts.md`) — contratti di handoff
- `T-shared-state-schema` (`Funzioni/T-shared-state-schema.md`) — schema stato condiviso

---

## KPI

| Metrica | Target |
|---|---|
| Team con integration test verde al primo ciclo | ≥ 75% |
| Team senza escalation protocol definito | 0 |
| Tempo org-design → team operativo | ≤ 5 giorni |
| Team senza acceptance criteria misurabili | 0 |
