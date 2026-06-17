---
Type: CONCEPT
Status: Active
Tags: #coo #skills #tools #ops-dashboard #incident-runbook #handoff-validator
Created: 2026-06-17
Last updated: 2026-06-17
---

# SKILLS — COO (Chief Operating Officer)

> Skill proprie della figura COO. Strumenti specializzati che il team COO usa e che possono
> essere esportati (versione parametrizzata) come prodotti o strumenti interni agli ecosistemi.
> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-COO.md` §Skill proprie

---

## SKILL 1 — `ops-dashboard`

**Scopo:** Produce lo snapshot dello stato operativo della holding in ≤30 secondi di lettura.
È il deliverable primario di WF-OPS-DAILY: un quadro sintetico, leggibile, non ambiguo.

**Input:** output aggregato dei 5 monitor COO (backbone, sync, runtime, sla, cadence).

**Output format:**
```
STATO OPERATIVO — [DATA] [ORA]
═══════════════════════════════════════
BACKBONE:  ● verde  | BUS ok · BRAIN ok · Gov ok · Obs ok · Coord ok · Auth ok
SYNC:      ● verde  | Max↔Gael: ok · 0 conflitti · flag COORD: nessuno
RUNTIME:   ● verde  | 3 run attive · 0 zombie · budget medio 45%
SLA:       ● giallo | 1 a rischio: SLA-AGENCY-CF-001 (33h) · 0 violati
CADENZA:   ● verde  | standup: ok · review settimanale: tra 6gg

STATO GLOBALE: GIALLO

BLOCCHI ATTIVI:
[1] SLA-AGENCY-CF-001 — delivery cliente X scade tra 33h. Owner: coo-sla-tracker. ETA: update da 01-AGENCY.

AZIONI IN CORSO:
[1] coo-sla-tracker notifica 01-AGENCY per status update delivery.

ESCALATION: nessuna.
═══════════════════════════════════════
```

**Quando si usa:** ogni apertura sessione (via WF-OPS-DAILY) + quando il CEO richiede
un aggiornamento istantaneo sullo stato della holding.

**Chi la usa:** coo-conductor (produce), CEO (consuma via HC-COO-CEO-01).

---

## SKILL 2 — `incident-runbook`

**Scopo:** Runbook strutturato per la gestione di un incidente operativo. Guida l'agente
(o il team) passo-passo dalla rilevazione al post-mortem, con domande di triage standardizzate
e template per ogni fase.

**Template triage rapido:**
```
INC-ID: ______________
Timestamp apertura: ______________
Fonte rilevazione: [ ] backbone-health  [ ] runtime-marshal  [ ] sla-tracker  [ ] sync-keeper  [ ] esterno
Descrizione in 1 riga: ______________

TRIAGE:
1. Blocca la produzione? [ ] sì totale  [ ] sì con workaround  [ ] degrada  [ ] no
2. Causa: [ ] ops (zombie/run/cron)  [ ] tecnico Backbone  [ ] esterno (API/token)  [ ] umano
3. Risolvo in autonomia? [ ] sì (stima ETA: ___)  [ ] no → escala a: [ ] CEO  [ ] CFO  [ ] CTO  [ ] umano
4. Impatto SLA cliente? [ ] sì → quale: ___  [ ] no

CONTROMISURA IMMEDIATA:
[ ] kill zombie  [ ] restart run  [ ] re-schedule cron  [ ] alert umano per token  [ ] ticket CTO  [ ] pausa run

POST-MORTEM (dopo risoluzione):
Root cause (5-Why): ______________
Fix applicato: ______________
Prevenzione proposta: ______________
Pattern bank entry: ______________
```

**Quando si usa:** ogni volta che viene aperto un INC, indipendentemente dalla severità.
Il runbook è obbligatorio (vedi REGOLA OPS-01).

**Chi la usa:** coo-incident-handler (primary), coo-conductor (supervisione), qualsiasi
agente del team COO che rileva una prima anomalia.

---

## SKILL 3 — `handoff-validator`

**Scopo:** Valida la conformità strutturale di un contratto HC. Può essere usato in modo
proattivo (prima di attivare un nuovo HC) o in modo retrospettivo (audit HC esistenti).

**Input:** definizione HC (schema + acceptance criteria) + payload campione da validare.

**Checks eseguiti:**
1. **Schema validation** — tutti i campi obbligatori presenti? Tipi corretti?
2. **Acceptance criteria operability** — il criterio è misurabile? Ha un owner? Ha una deadline?
   Criteri vaghi come "il destinatario leggerà" non sono acceptance criteria: sono speranze.
3. **Owner attuale** — il ruolo owner esiste ancora? È il ruolo giusto?
4. **Bidirezionalità** — se il contratto prevede ACK di ricezione, c'è un canale di ritorno?

**Output:**
```json
{
  "hc_id": "HC-COO-CEO-01",
  "valido": true,
  "anomalie": [],
  "raccomandazioni": [
    "Aggiungere campo 'timestamp_invio' al payload per tracciare la latenza di ricezione"
  ]
}
```

**Quando si usa:** (1) prima di registrare un nuovo HC nel registry; (2) durante WF-HANDOFF-AUDIT
per ogni HC campionato; (3) quando un ecosistema propone una modifica a un HC esistente.

**Chi la usa:** coo-handoff-auditor (primary), coo-conductor (su nuovi HC proposti).

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[REGOLE]] · `regole/REGOLE.md`
- [[KPI]] · `kpi/KPI.md`
- [[WF-OPS-DAILY]] · `workflow/WF-OPS-DAILY.md`
- [[WF-INCIDENT]] · `workflow/WF-INCIDENT.md`
- [[WF-HANDOFF-AUDIT]] · `workflow/WF-HANDOFF-AUDIT.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
