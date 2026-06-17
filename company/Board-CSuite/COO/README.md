---
Type: ENTITY
Status: Active
Tags: #board #csuite #coo #operations #backbone #runtime #monitor
Created: 2026-06-17
Last updated: 2026-06-17
---

# COO — Chief Operating Officer — Architettura della Figura

> **Livello:** L0 — Board/C-Suite · **ID registro:** COO-001
> **Namespace AgentDB:** `board/coo` · **Tier modello:** Opus (conductor) / Sonnet (monitor/fix) / Haiku (tracking/patrol)
> **Riporta a:** CEO (Empire-Conductor) · **Review:** MAXIMILIAN (passo 5-bis su decisioni operative strutturali)
> **Blueprint di riferimento:** `company/Board-CSuite/_BLUEPRINT/BP-COO.md`

---

## Missione

Il COO è il **responsabile operativo della holding**: fa girare la macchina ogni giorno. Presidia
la salute del Backbone (BUS/BRAIN), la sincronizzazione Max↔Gael, il runtime degli swarm/cron
via ecosistema 09-OPERATIONS, il rispetto degli SLA per ecosistema, la gestione degli incidenti
e il ritmo operativo (cadenza, standup, review). **NON decide cosa produrre** (quello è CEO/CRO):
il COO decide **come gira la macchina** e risolve ogni blocco che rallenta la produzione.

Missione in una frase: *"Faccio girare la macchina mentre il CEO pensa alla strategia — e se
la macchina si rompe, sono io che la riparo prima che Max se ne accorga."*

---

## Forma: Cartella-Workflow (CF-grade)

Le operations della holding non sono un ruolo singolo: sono un **sistema di monitoraggio always-on**
con un team di 10 agenti specializzati. Ogni agente ha un ruolo preciso: monitor, ottimizzatori,
auditor, cadence keeper, memoria. Il peso della figura è PESANTE per la natura del monitoraggio
(sempre attivo), ma media per il singolo intervento (la maggior parte dei check è automatica).

---

## Struttura interna

```
COO/
├── README.md                      ← questo file (architettura, mappa)
├── ARCHITETTURA.md                ← gerarchia interna, flussi, relazioni con backbone/09-OPERATIONS
├── agenti/                        ← 10 schede agente CF-grade
│   ├── coo-conductor.md           ← coordina le operations, riporta al CEO (Opus)
│   ├── coo-backbone-health.md     ← monitor BUS/BRAIN/handoff always-on (Sonnet)
│   ├── coo-sync-keeper.md         ← sync repo Max↔Gael, anti-collisione (Sonnet)
│   ├── coo-runtime-marshal.md     ← orchestra swarm/cron via 09-OPERATIONS (Sonnet)
│   ├── coo-sla-tracker.md         ← SLA per ecosistema, ritardi (Haiku)
│   ├── coo-incident-handler.md    ← gestisce run fallite, daemon zombie, escalation (Sonnet)
│   ├── coo-process-optimizer.md   ← rimuove colli di bottiglia ricorrenti (Sonnet)
│   ├── coo-handoff-auditor.md     ← verifica contratti HC tra ecosistemi (Haiku)
│   ├── coo-cadence-keeper.md      ← ritmi operativi, standup, review settimanali (Haiku)
│   └── coo-memoria.md             ← storico incidenti, pattern operativi (Haiku)
├── workflow/                      ← 3 workflow CF-grade
│   ├── WF-OPS-DAILY.md            ← health check backbone + run + sync → report CEO in 30s
│   ├── WF-INCIDENT.md             ← rilevazione → triage → fix → post-mortem
│   └── WF-HANDOFF-AUDIT.md        ← campionamento contratti HC, segnala rotture
├── principi/
│   └── PRINCIPI.md                ← come ragiona la figura COO
├── regole/
│   └── REGOLE.md                  ← limiti non negoziabili del dominio operations
├── skills/
│   └── SKILLS.md                  ← ops-dashboard, incident-runbook, handoff-validator
├── scripts/
│   └── README.md                  ← script ops (health-check, sync-guard, cron-runner)
├── kpi/
│   └── KPI.md                     ← KPI presidiati con logica di misura
└── state/
    └── README.md                  ← schema stato, namespace memoria board/coo
```

---

## Come governa

**Tre modalità operative:**

1. **Daily Health** — ogni sessione: backbone check + runtime status + sync conflict → report stato
   al CEO via `HC-COO-CEO-01` (verde/giallo/rosso + lista blocchi + azioni in corso).
2. **Incident Response** — incidente rilevato (run fallita, daemon zombie, sync conflict, SLA breach)
   → triage → contromisura → post-mortem → pattern in memoria per prevenire la ricorrenza.
3. **Handoff Audit** — campionamento periodico dei contratti HC tra ecosistemi: validazione
   struttura, verifica esito, segnalazione rotture al conductor + proposta di fix.

**Regola universale:** ogni incidente aperto deve avere owner, stato corrente e ETA fix
documentati in `state/README.md`. "Incidente non documentato = incidente non gestito."

---

## Relazioni esterne

| Con | Quando | Tipo relazione |
|---|---|---|
| CEO (Empire-Conductor) | ogni sessione via HC-COO-CEO-01 | Report stato → riceve direttive |
| CFO | alert run costosa / overrun budget | Escalation costo → CFO decide envelope |
| CTO | anomalia tecnica Backbone (non ops) | Escalation tecnica → CTO risolve |
| 09-OPERATIONS | ogni esecuzione swarm/cron | Runtime reale (COO orchestra, 09 esegue) |
| 10-MEMORY | load stato prima / write checkpoint dopo | Sempre, ogni sessione |
| Tutti gli ecosistemi | ricezione stato run/HC in ingresso | Monitoraggio passivo + alert attivo |

---

## Handoff contract con il Board C-Suite

| Contract ID | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-COO-CEO-01` | COO → CEO | report stato (verde/giallo/rosso) + blocchi + azioni | CEO legge in apertura sessione Board |
| `HC-COO-CFO-01` | COO → CFO | eventi run con costo anomalo + alert budget | CFO aggiorna cost-sentinel |
| `HC-CEO-COO-01` | CEO → COO | direttiva operativa + acceptance criteria | COO conferma ricevuta + assegna owner operativo |
| `HC-CTO-COO-01` | CTO → COO | segnalazione salute tecnica componenti Backbone | COO integra in health-check giornaliero |

---

## Connessioni

- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[COO-v1]] · `company/Board-CSuite/COO.md`
- [[CEO-Empire-Conductor]] · `company/Board-CSuite/CEO-Empire-Conductor/README.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
- [[14-DOSSIER-ARCHITETTURA]] · `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md`
