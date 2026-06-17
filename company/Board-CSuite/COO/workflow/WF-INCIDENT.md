---
Type: CONCEPT
Status: Active
Tags: #workflow #coo #incident #runbook #postmortem #recovery
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-INCIDENT — Gestione Incidente Operativo

> **ID workflow:** WF-COO-02 · **Owner:** coo-incident-handler (coordinato da coo-conductor)
> **Trigger:** anomalia rilevata da qualsiasi monitor COO con severità ≥ media
> **Durata attesa:** triage ≤5min · contromisura ≤15min · risoluzione variabile · post-mortem ≤30min
> **Blueprint di riferimento:** `company/Board-CSuite/_BLUEPRINT/BP-COO.md`

---

## Scopo

Garantire che ogni incidente operativo venga gestito con un processo strutturato e tracciato:
dalla rilevazione al post-mortem, senza saltare passi. L'obiettivo è duplice: (1) risolvere
l'incidente nel minor tempo possibile (minimizzare MTTR), e (2) imparare da ogni incidente
per prevenire la ricorrenza (pattern bank + ottimizzazione). Un incidente gestito male lascia
la holding vulnerabile alla stessa anomalia la settimana dopo.

---

## Agenti coinvolti

| Agente | Ruolo nel workflow | Fase |
|---|---|---|
| `coo-conductor` | riceve la segnalazione, coordina il workflow, decide le escalation | tutto |
| `coo-incident-handler` | apre INC, triage, contromisura, monitoring, post-mortem | tutto |
| `coo-backbone-health` | check isolato sul componente impattato (se Backbone) | fase 1-2 |
| `coo-runtime-marshal` | esecuzione kill zombie / restart run (se runtime) | fase 2-3 |
| `coo-sla-tracker` | verifica impatto SLA dell'incidente | fase 1-3 |
| `coo-memoria` | carica pattern noti + archivia post-mortem | fase 1 e 5 |
| `coo-process-optimizer` | riceve il post-mortem per analisi pattern | fase 5 |

---

## Flusso passo-passo

### Fase 1 — Rilevazione e Apertura INC (≤2 minuti)
**Owner:** `coo-incident-handler` + `coo-conductor`

**Trigger possibili:**
- Monitor COO (backbone-health, runtime-marshal, sla-tracker, sync-keeper) segnala anomalia.
- Segnalazione diretta da Max/Gael (anomalia rilevata esternamente al sistema).
- Alert da 09-OPERATIONS (run fallita, budget superato).

**Azioni:**
1. `coo-incident-handler` apre INC con ID univoco `INC-YYYYMMDD-NNN`.
2. Carica da `coo-memoria` i pattern noti: questo tipo di anomalia è già stato visto?
   Se sì → pattern noto, applica il fix già documentato (fast-track, salta fase 2-3).
3. Classifica la severità: critica (blocca produzione esterna) / alta (blocca produzione interna)
   / media (degrada ma non ferma) / bassa (monitorare, non critica).
4. Identifica il componente primario impattato e l'owner della risoluzione.

**Output — INC aperto:**
```json
{
  "inc_id": "INC-20260617-003",
  "timestamp_apertura": "2026-06-17T10:30:00Z",
  "severita": "alta",
  "fonte_rilevazione": "coo-runtime-marshal",
  "descrizione": "3 agenti zombie in swarm outreach-factory, timeout 2x (60min vs 30min attesi)",
  "componente_impattato": "swarm outreach-factory (01-AGENCY)",
  "pattern_noto": "zombie-api-auth-loop",
  "owner_risoluzione": "coo-runtime-marshal (kill) + rinnovo token FB (umano: Gael/Max)",
  "impatto_sla": "nessun SLA cliente immediato — ritardo outreach giornaliero"
}
```

---

### Fase 2 — Triage (≤5 minuti)
**Owner:** `coo-incident-handler` + `coo-conductor`

**Domande di triage (in ordine):**
1. **Blocca la produzione?** Sì critico / sì ma workaround disponibile / degrada / no.
2. **Causa interna o esterna?** Ops (nostro) / Tecnica Backbone (CTO) / Esterna (API terza parte).
3. **Risolvibile in autonomia?** Sì (ops kill/restart/re-run) / No (escalation CEO/CFO/CTO/umano).
4. **Impatto SLA cliente?** Sì → coo-sla-tracker verifica e aggiorna `sla-status`.

**Matrice di triage:**

| Causa | Autonomia | Azione |
|---|---|---|
| Zombie / run fallita (ops) | Sì | kill + restart + monitor. No escalation. |
| Token/credenziale scaduta | No (umano) | Alert a Max/Gael per rinnovo. INC rimane aperto. |
| Backbone degradato (tecnico) | No (CTO) | Ticket CTO + metti in attesa le run dipendenti. |
| SLA cliente violato | No (CEO/CRO) | Alert CEO + CRO. Comunicazione cliente se necessario. |
| Budget superato | No (CFO) | Alert CFO via coo-conductor. Pausa run. |

---

### Fase 3 — Contromisura Immediata (≤15 minuti)
**Owner:** `coo-runtime-marshal` (per ops) o owner designato al triage

**Contromisure operative standard:**
- **Zombie:** kill agente + verifica che non abbia lock tenuti aperti + restart.
- **Run fallita:** analisi exit code + re-run con parametri corretti (log verboso per debug).
- **Cron mancato:** verifica causa (BRAIN down? cron configurato male?) + re-schedule manuale.
- **Token scaduto:** mette in attesa tutte le run che dipendono dal token. Alert umano.
- **DLQ overflow nel BUS:** drain messaggi stantii + verifica causa della dead-letterizzazione.

**Gate di efficacia:** dopo la contromisura immediata, il monitor corrispondente viene
rilanciato. Se lo stato torna verde → contromisura efficace, si va alla fase 5 (post-mortem).
Se lo stato rimane rosso/giallo → si valuta escalation o contromisura alternativa.

---

### Fase 4 — Escalation (solo se necessario)
**Owner:** `coo-conductor`

L'escalation viene attivata quando la contromisura immediata non è sufficiente o quando
la causa richiede una decisione fuori dal perimetro COO.

**Ladder di escalation:**
```
Causa tecnica Backbone       → CTO (immediato)
Costo run anomalo            → CFO (immediato)
SLA cliente violato          → CEO + CRO (immediato)
Decisione cross-ecosistema   → CEO (immediato)
Credenziale/token rinnovare  → Gael o Max (umano) via nota in STATO-EMPIRE
```

**Formato notifica escalation (INC summary):**
- INC-ID, severità, descrizione in 2 righe, impatto, azione richiesta dal destinatario.
- Non si trasferisce responsabilità senza trasferire il contesto.

---

### Fase 5 — Post-Mortem e Chiusura INC (≤30 minuti dopo risoluzione)
**Owner:** `coo-incident-handler` → archiviazione in `coo-memoria`

**Struttura post-mortem (obbligatoria per ogni INC, anche minori):**
1. **Timeline:** da rilevazione a chiusura, ogni azione con timestamp.
2. **Root cause (5-Why):** non fermarsi al sintomo — trovare la causa strutturale.
3. **Fix applicato:** cosa ha risolto l'incidente (temporaneo o definitivo?).
4. **Prevenzione proposta:** cosa impedisce la ricorrenza? Chi deve implementarla?
5. **Pattern bank entry:** etichetta per il pattern bank di coo-memoria.

**Gate di chiusura INC:**
- [ ] Root cause identificata (anche "sconosciuta" è un valore valido — ma giustificata).
- [ ] Fix documentato.
- [ ] Prevenzione proposta (anche "nessuna — evento eccezionale non ripetibile" se appropriato).
- [ ] Archiviato in `coo-memoria` → pattern bank aggiornato.
- [ ] Notifica chiusura a CEO se l'INC era stato escalato.
- [ ] `coo-process-optimizer` notificato se il pattern è ricorrente (≥2 occorrenze).

---

## State del workflow

| Campo | Valore atteso |
|---|---|
| `inc_id` | `INC-YYYYMMDD-NNN` |
| `fase_corrente` | `1-rilevazione | 2-triage | 3-contromisura | 4-escalation | 5-postmortem | chiuso` |
| `severita` | `critica | alta | media | bassa` |
| `contromisura_applicata` | `descrizione o null` |
| `escalation_attiva` | `{destinatario, motivo} o null` |
| `stato` | `aperto | in-corso | in-attesa-umano | in-attesa-cto | risolto | chiuso` |

---

## KPI del workflow

| Metrica | Target |
|---|---|
| MTTR (Mean Time to Recovery) | [DM] — baseline da stabilire nelle prime 4 settimane |
| % INC con post-mortem completo | 100% |
| % INC con pattern_bank_entry | 100% |
| % INC ricorrenti (pattern già visto) | Obiettivo: trend decrescente nel tempo [DM] |

---

## Connessioni

- [[coo-conductor]] · `agenti/coo-conductor.md`
- [[coo-incident-handler]] · `agenti/coo-incident-handler.md`
- [[coo-backbone-health]] · `agenti/coo-backbone-health.md`
- [[coo-runtime-marshal]] · `agenti/coo-runtime-marshal.md`
- [[coo-sla-tracker]] · `agenti/coo-sla-tracker.md`
- [[coo-memoria]] · `agenti/coo-memoria.md`
- [[coo-process-optimizer]] · `agenti/coo-process-optimizer.md`
- [[WF-OPS-DAILY]] · `workflow/WF-OPS-DAILY.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
