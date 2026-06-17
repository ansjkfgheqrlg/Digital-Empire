---
Type: CONCEPT
Status: Active
Tags: #coo #state #agentdb #namespace #memoria #schema
Created: 2026-06-17
Last updated: 2026-06-17
---

# STATE — COO (Chief Operating Officer)

> Schema dello stato operativo del team COO nel namespace AgentDB `board/coo`.
> Questa pagina documenta cosa viene persistito, dove, da chi, e con quale struttura.
> È il "contratto di stato" del team COO: chi legge qui sa dove trovare ogni informazione.

---

## Namespace AgentDB

**Root namespace:** `board/coo`
**Accesso:** read da tutti gli agenti COO + CEO; write solo dagli agenti COO designati.

---

## Chiavi di stato

### `board/coo/stato-operativo`
**Owner write:** `coo-conductor`
**Frequenza aggiornamento:** ogni sessione (post WF-OPS-DAILY)
**Struttura:**
```json
{
  "timestamp_ultimo_check": "2026-06-17T09:00:00Z",
  "stato_globale": "verde | giallo | rosso",
  "semaforo_dettaglio": {
    "backbone": "verde | giallo | rosso",
    "sync": "ok | conflitto | degradato",
    "runtime": "verde | giallo | rosso",
    "sla": "verde | giallo | rosso",
    "cadenza": "ok | saltata | in-ritardo"
  },
  "blocchi_attivi": [
    {
      "id": "INC-20260617-001",
      "tipo": "sla_a_rischio | zombie | backbone | sync | cron_mancato",
      "descrizione": "...",
      "owner": "...",
      "eta_fix": "...",
      "escalation_attiva": false
    }
  ],
  "report_ceo_inviato": true,
  "ultima_sessione_chiusa": "2026-06-16T23:14:00Z"
}
```

---

### `board/coo/incidenti-aperti`
**Owner write:** `coo-incident-handler`
**Frequenza aggiornamento:** ogni apertura/aggiornamento/chiusura INC
**Struttura (lista di INC aperti):**
```json
[
  {
    "inc_id": "INC-20260617-001",
    "stato": "in-corso | in-attesa-umano | in-attesa-cto | in-attesa-cfo",
    "severita": "critica | alta | media | bassa",
    "apertura": "2026-06-17T09:45:00Z",
    "descrizione": "...",
    "owner": "...",
    "eta_fix": "...",
    "escalation": {"attiva": false, "destinatario": null}
  }
]
```

---

### `board/coo/incidenti-storico`
**Owner write:** `coo-memoria`
**Frequenza aggiornamento:** quando un INC viene chiuso (post-mortem archiviato)
**Struttura (append-only — lista di post-mortem):**
```json
[
  {
    "inc_id": "INC-20260601-001",
    "chiuso": "2026-06-01T11:30:00Z",
    "durata_min": 45,
    "severita": "alta",
    "root_cause": "...",
    "fix_applicato": "...",
    "prevenzione": "...",
    "pattern_bank_entry": "swarm-exit-code-1-token-limit",
    "ecosistema_impattato": "Content-Factory"
  }
]
```

---

### `board/coo/sla-status`
**Owner write:** `coo-sla-tracker`
**Frequenza aggiornamento:** ogni daily check + ogni aggiornamento SLA
**Struttura:**
```json
{
  "ultima_verifica": "2026-06-17T09:15:00Z",
  "sla_registry": [
    {
      "id": "SLA-AGENCY-CF-001",
      "ecosistema": "01-AGENCY",
      "commitment": "...",
      "deadline": "2026-06-18T18:00:00Z",
      "stato": "ok | a-rischio | violato",
      "owner": "...",
      "ultima_verifica": "2026-06-17T09:15:00Z"
    }
  ],
  "trend": {
    "01-AGENCY": {"ritardi_30gg": 1},
    "03-CONTENT": {"ritardi_30gg": 2}
  }
}
```

---

### `board/coo/sync-status`
**Owner write:** `coo-sync-keeper`
**Frequenza aggiornamento:** ogni sync check
**Struttura:**
```json
{
  "ultima_verifica": "2026-06-17T09:05:00Z",
  "sync_ok": true,
  "ultima_run_sync": "2026-06-17T08:47:00Z",
  "conflitti_attivi": [],
  "flag_coordinamento": {
    "attivo": false,
    "area": null,
    "owner": null,
    "motivo": null
  },
  "zone_calde_status": {}
}
```

---

### `board/coo/hc-audit-log`
**Owner write:** `coo-handoff-auditor` + `coo-memoria`
**Frequenza aggiornamento:** ogni sessione WF-HANDOFF-AUDIT
**Struttura (append-only — lista audit session):**
```json
[
  {
    "data_audit": "2026-06-17",
    "hc_auditati": ["HC-CEO-COO-01", "HC-COO-CEO-01"],
    "hc_rotti": [],
    "hc_degradati": ["HC-COO-CEO-01"],
    "azioni_avviate": ["..."],
    "prossima_revisione": "2026-07-01"
  }
]
```

---

### `board/coo/run-schedule`
**Owner write:** `coo-runtime-marshal`
**Frequenza aggiornamento:** ogni update della priority queue + ogni completamento run
**Struttura:**
```json
{
  "data_riferimento": "2026-06-17",
  "priority_queue": [
    {
      "run_id": "RUN-CF-001",
      "tipo": "swarm | cron",
      "priorita": "alta | media | bassa",
      "orario_avvio": "09:00",
      "stato": "running | completed | failed | scheduled | zombie",
      "token_usati": 1200,
      "envelope": 5000
    }
  ],
  "run_completate_oggi": 2,
  "run_fallite_oggi": 0
}
```

---

## Sync con Memory centrale

Il namespace `board/coo` è persistito in AgentDB (BRAIN). Ogni sessione chiusa, `coo-memoria`
esporta il checkpoint in `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md` seguendo il template
in `company/Memory/templates/`.

**Cosa finisce nel checkpoint:**
- Stato operativo della sessione (semaforo + blocchi)
- INC aperti/chiusi nella sessione
- SLA aggiornati
- Cadenza: standup completata? Review? Milestone segnalate?

**Cosa resta solo in AgentDB:**
- Storico completo incidenti (solo summary nel checkpoint)
- Log HC audit completo (solo anomalie nel checkpoint)
- Priority queue run (solo stato finale nel checkpoint)

---

## Connessioni

- [[coo-conductor]] · `agenti/coo-conductor.md`
- [[coo-memoria]] · `agenti/coo-memoria.md`
- [[KPI]] · `kpi/KPI.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[INDEX-MEMORY]] · `company/Memory/INDEX.md`
- [[STATO-EMPIRE]] · `company/Memory/STATO-EMPIRE.md`
- [[ADR-002]] · `company/Memory/decisions/` (MEMORY-FIRST)
