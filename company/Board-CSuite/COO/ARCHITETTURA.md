---
Type: CONCEPT
Status: Active
Tags: #coo #architettura #gerarchia #backbone #runtime #operations #sync
Created: 2026-06-17
Last updated: 2026-06-17
---

# COO — Architettura Espansa

> Fonte primaria: `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
> Fonte v1: `company/Board-CSuite/COO.md`
> Connessioni: [[12-DOSSIER-MAXIMILIAN]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]] · [[14-DOSSIER-ARCHITETTURA]]

---

## 1. Posizione nella gerarchia

```
MAX (founder — umano)
  │
  ├─ MANDATO (LX) ─────────── Cosa è lecito (regole non negoziabili)
  ├─ MAXIMILIAN ───────────── Cosa è all'altezza (standard e visione)
  │
  └─ CEO / Empire-Conductor   (L0 Board C-Suite — superiore diretto del COO)
       │
       └─ COO   ← questa figura (L0 Board C-Suite — operations)
            │
            ├─ 09-OPERATIONS (ecosistema — runtime reale: swarm, cron, budget-guard)
            ├─ Corporate Backbone (BUS / BRAIN / Governance / Identity-HR / Observability / Coordination)
            └─ Sync GitHub Max↔Gael (hook sistema, ADR-004)
```

Il COO non si trova sopra il Mandato né sopra MAXIMILIAN. La sua autorità è operativa:
gestisce il "come gira" (mai il "cosa fare"). Ogni decisione cross-ecosistema di portata
strategica deve passare dal CEO prima del dispatch.

---

## 2. Gerarchia interna del team COO

```
coo-conductor (Opus — coordinatore delle operations)
  │
  ├── [MONITOR ALWAYS-ON]
  │     ├── coo-backbone-health (Sonnet) ← BUS/BRAIN/handoff/Observability
  │     └── coo-sync-keeper (Sonnet)     ← sync Max↔Gael, anti-collisione
  │
  ├── [RUNTIME & SLA]
  │     ├── coo-runtime-marshal (Sonnet) ← swarm/cron via 09-OPERATIONS
  │     └── coo-sla-tracker (Haiku)      ← SLA per ecosistema, ritardi
  │
  ├── [INCIDENT & FIX]
  │     ├── coo-incident-handler (Sonnet)    ← run fallite, daemon zombie, escalation
  │     └── coo-process-optimizer (Sonnet)   ← rimuove colli di bottiglia ricorrenti
  │
  ├── [AUDIT & CADENCE]
  │     ├── coo-handoff-auditor (Haiku)  ← contratti HC tra ecosistemi
  │     └── coo-cadence-keeper (Haiku)   ← ritmi, standup, review settimanali
  │
  └── [MEMORIA]
        └── coo-memoria (Haiku) ← storico incidenti, pattern operativi
```

Il `coo-conductor` è l'unico agente che parla direttamente con il CEO (via HC-COO-CEO-01)
e con il CFO (via HC-COO-CFO-01). Gli altri 9 agenti operano all'interno del team COO
o verso gli ecosistemi su delega esplicita del conductor.

---

## 3. Flusso operativo giornaliero (WF-OPS-DAILY)

```
[Apertura sessione]
        │
        ▼
[coo-memoria] — carica STATO-EMPIRE + lista incidenti aperti + pattern noti
        │
        ▼
[coo-backbone-health] — verifica BUS / BRAIN / Governance / Observability / Coordination
[coo-sync-keeper]     ─┐ in parallelo
[coo-sla-tracker]     ─┘
        │
        ▼
[coo-conductor] — aggrega stato: tutto verde? → report CEO. Giallo/Rosso?
        │ Giallo/Rosso
        ▼
[coo-incident-handler] — triage: risolvo qui o escalo a CEO/CFO/CTO?
        │
        ▼
[coo-runtime-marshal] — verifica run schedulate, swarm in corso, cron attivi
        │
        ▼
[coo-conductor] — compila report stato in 30s → invia HC-COO-CEO-01
        │
        ▼
[coo-memoria] — checkpoint: stato del giorno, blocchi aperti, azioni avviate
        │
        ▼
[coo-cadence-keeper] — verifica: oggi è giorno di standup/review? Triggera se sì
```

---

## 4. Relazione con 09-OPERATIONS (runtime reale)

Il COO **orchestra**, il ecosistema 09-OPERATIONS **esegue**. Il confine è netto:

| COO decide | 09-OPERATIONS esegue |
|---|---|
| Quali swarm attivare | Lancia gli agenti del swarm |
| Quale cron schedulate oggi | Esegue il cron alla scadenza |
| Budget-guard trigger | Applica il blocco/alert al runtime |
| Priority queue ordine | Esegue nella sequenza indicata |

Il COO non scrive script di esecuzione: delega via contratto HC a 09-OPERATIONS.
Se 09-OPERATIONS non risponde o la run fallisce, il COO registra un incidente e
avvia WF-INCIDENT.

---

## 5. Relazione con il Backbone

Il Backbone è l'infrastruttura trasversale della holding. Il COO la monitora ma non la governa
(quella è competenza del CTO). Il COO ha accesso read-only ai canali di stato del Backbone:

| Componente Backbone | Cosa monitora il COO | Soglia alert |
|---|---|---|
| BUS (message bus) | handoff queue backlog, messaggi in dead-letter | >5 messaggi in DLQ |
| BRAIN (AgentDB) | availability, latenza query | indisponibile >2min |
| Governance | gate attivi, ADR in pending | gate bloccato >1h senza risposta |
| Observability | log anomali, error rate | error rate >5% in 15min |
| Coordination | lock contesi, stallo raft | stallo >30min |
| Identity-HR | token scaduti, credenziali mancanti | token scaduto non rinnovato |

Quando il COO rileva anomalia Backbone → contatta CTO (non tenta fix autonomo su infrastruttura).

---

## 6. Relazione con il Sync Max↔Gael (ADR-004)

Il `coo-sync-keeper` supervisiona il sistema di sincronizzazione GitHub tra Max e Gael.
Verifica: nessun file in conflitto non risolto, nessuna collisione su aree critiche
(Memory/, PIANO-MAESTRO/, cartelle C-Suite in costruzione attiva). Il flag di blocco
`⚠️ COORDINAMENTO` in STATO-EMPIRE è sempre obbedito prima di entrare in un'area condivisa.

---

## 7. Namespace memoria (AgentDB `board/coo`)

| Chiave | Cosa contiene | Owner |
|---|---|---|
| `board/coo/stato-operativo` | snapshot stato giornaliero (verde/giallo/rosso + blocchi) | coo-conductor |
| `board/coo/incidenti-aperti` | lista incidenti aperti con owner + ETA fix | coo-incident-handler |
| `board/coo/incidenti-storico` | archivio post-mortem + pattern ricorrenti | coo-memoria |
| `board/coo/sla-status` | SLA per ecosistema, last-check, trend | coo-sla-tracker |
| `board/coo/sync-status` | ultimo check sync Max↔Gael, conflitti rilevati | coo-sync-keeper |
| `board/coo/hc-audit-log` | log audit contratti HC campionati | coo-handoff-auditor |
| `board/coo/run-schedule` | cron attivi, swarm pianificati, prossime run | coo-runtime-marshal |

---

## 8. Escalation ladder

```
EVENTO OPERATIVO
      │
      ▼
coo-conductor (gestisce in autonomia se risolvibile in <15min)
      │ Non risolvibile
      ▼
CEO → se impatta decisione cross-ecosistema o strategica
CFO → se impatta budget (costo run anomalo, overrun)
CTO → se l'anomalia è in Backbone (infrastruttura tecnica)
MAX → se CEO/CFO/CTO non sono sufficienti (caso raro, documentato)
```

---

## Connessioni

- [[README]] · `company/Board-CSuite/COO/README.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[COO-v1]] · `company/Board-CSuite/COO.md`
- [[CEO-Empire-Conductor/ARCHITETTURA]] · `company/Board-CSuite/CEO-Empire-Conductor/ARCHITETTURA.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[ADR-004]] · `company/Memory/decisions/` (sync Max↔Gael)
- [[ADR-006]] · `company/Memory/decisions/` (ciclo a 9 passi)
