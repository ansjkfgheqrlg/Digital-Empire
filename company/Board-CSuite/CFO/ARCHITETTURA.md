---
Type: CONCEPT
Status: Active
Tags: #cfo #architettura #gerarchia #budget-guard #3-tier #cost-ledger
Created: 2026-06-17
Last updated: 2026-06-17
---

# CFO — Architettura Espansa

> Fonte primaria: `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
> Fonte v1: `company/Board-CSuite/CFO.md`
> Connessioni: [[README]] · [[12-DOSSIER-MAXIMILIAN]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]]

---

## 1. Posizione nella gerarchia

```
MAX (founder — umano)
  │
  ├─ MANDATO (LX) ─────────────── Art.4.3: dry-run obbligatorio prima di ogni spesa API
  ├─ MAXIMILIAN ───────────────── Standard di qualità e scala
  │
  └─ CEO / Empire-Conductor (L0)
       │
       └─ CFO ← questa figura (L0 Board C-Suite)
             │
             ├─ cfo-budget-guard   (always-on: blocca PRIMA dello sforo)
             ├─ cfo-cost-sentinel  (alert 80% budget)
             ├─ cfo-spend-approver (ok esplicito spese API)
             ├─ cfo-tier-router    (enforcement 3-tier)
             ├─ cfo-cost-accountant (ledger attribution)
             ├─ cfo-forecast-finance (forecast + runway)
             ├─ cfo-roi-analyst    (ROI per ecosistema)
             ├─ cfo-runway-tracker (ADR-006: budget-guard 20% sessione)
             └─ cfo-memoria        (storico + pattern di spreco)
```

Il CFO presidia il **piano finanziario della holding**: nessun ecosistema spende API senza
passare dal budget guard. Il flusso è sempre: stima → approvazione → esecuzione → attribution.
Mai: esecuzione → riconoscimento a posteriori.

---

## 2. Gerarchia interna del team CFO

```
cfo-conductor (Opus — coordina + riporta al CEO)
  │
  ├── [BLOCCO PRE-SFORO — always-on]
  │     ├── cfo-budget-guard (Sonnet)   ← blocca run oltre il budget dichiarato
  │     └── cfo-cost-sentinel (Haiku)   ← alert proattivo a soglia 80%
  │
  ├── [APPROVAZIONE & ROUTING]
  │     ├── cfo-spend-approver (Sonnet) ← ok esplicito spese API reali
  │     └── cfo-tier-router (Haiku)     ← enforcement 3-tier (modello giusto per task)
  │
  ├── [ATTRIBUTION & LEDGER]
  │     └── cfo-cost-accountant (Haiku) ← ledger per agente/run/commessa
  │
  ├── [ANALISI & FORECAST]
  │     ├── cfo-forecast-finance (Sonnet) ← forecast costi + runway
  │     └── cfo-roi-analyst (Sonnet)      ← ROI per ecosistema
  │
  └── [SESSIONE & MEMORIA]
        ├── cfo-runway-tracker (Haiku)  ← ADR-006: alert quando <20% risorse sessione
        └── cfo-memoria (Haiku)         ← storico costi, pattern di spreco
```

---

## 3. Regola dei 3 Tier (enforcement cfo-tier-router)

Il 3-tier routing è il meccanismo primario di contenimento costi. Il CFO è responsabile
che ogni task dell'intera holding usi il modello minimo sufficiente.

| Tier | Modello | Quando è ammesso | Costo relativo |
|---|---|---|---|
| T0 — WASM | Modello locale / WASM | Classificazione semplice, QA deterministico | Minimo |
| T1 — Haiku | Claude Haiku | Parsing strutturato, alert, classificazione, ledger | Basso |
| T2 — Sonnet | Claude Sonnet | Copy, coding, analisi standard, approvazione spese | Medio |
| T3 — Opus | Claude Opus | Decisioni strategiche, contenuti premium, architettura, conductor | Alto |

**Regola:** il tier T3 richiede giustificazione esplicita. L'uso di Opus per task T1/T2
è un'anomalia tracciata nel ledger e segnalata dal `cfo-tier-router`.

**Metodo di selezione:** Thompson Sampling adattivo (dal v1 `CFO.md`). Il router non assegna
Opus per default — la giustificazione deve essere esplicita e tracciata.

---

## 4. Flusso finanziario standard

```
EVENTO COSTO (qualsiasi run / workflow / agente)
        │
        ▼
[cfo-runway-tracker] — sessione > 80% risorse? Sì → alert al conductor
        │
        ▼
[cfo-budget-guard] — l'ecosistema richiedente ha budget disponibile?
        │  No → BLOCCA (non continua, notifica conductor)
        │  Sì → continua
        ▼
[cfo-tier-router] — il task usa il tier minimo necessario?
        │  No → declassa al tier corretto prima di procedere
        │  Sì → continua
        ▼
[cfo-spend-approver] — la spesa è sopra soglia (spesa API reale)?
        │  Sì → dry-run + ok esplicito (Mandato Art.4.3)
        │  No → procede senza approvazione esplicita
        ▼
ESECUZIONE DEL RUN
        │
        ▼
[cfo-cost-accountant] — attribution nel ledger (agente / run / ecosistema / commessa)
        │
        ▼
[cfo-cost-sentinel] — budget > 80% dopo attribution? → alert proattivo
        │
        ▼
[cfo-forecast-finance] — aggiorna forecast e runway
[cfo-roi-analyst] — aggiorna ROI ecosistema (se run legato a deliverable misurabile)
```

---

## 5. Flusso report settimanale (WF-COST-REPORT)

```
TRIGGER: schedule settimanale (o su richiesta CEO/Board)
        │
        ▼
[cfo-memoria] — carica storico ledger settimana
        │
        ▼
[cfo-cost-accountant] — aggrega: costi per ecosistema / agente / tier
        │
        ▼
[cfo-forecast-finance] — calcola runway residua + proiezione mese
        │
        ▼
[cfo-roi-analyst] — calcola ROI per ecosistema attivo
        │
        ▼
[cfo-conductor] — sintetizza report Board; identifica anomalie
        │
        ▼
OUTPUT: report settimanale → CEO (HC-CFO-CEO-01) + Board
```

---

## 6. Relazione con il Mandato (Art.4.3)

Il Mandato Articolo 4.3 impone il dry-run obbligatorio prima di ogni spesa API reale.
Il CFO è il custode di questa regola:
- `cfo-budget-guard` la applica in entrata (blocca se non c'è dry-run).
- `cfo-spend-approver` emette l'ok esplicito dopo il dry-run.
- `cfo-cost-accountant` verifica che ogni spesa abbia un approval_id nel ledger.

Nessuna eccezione: non esiste "era urgente" come bypass del dry-run.

---

## 7. Handoff contract con il Board C-Suite

| Contract ID | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-CFO-CEO-01` | CFO → CEO | Alert costi + budget status settimanale | CEO acknowledge + decisione se soglia critica |
| `HC-CFO-COO-01` | CFO → COO | Blocco run (budget esaurito) | COO ferma l'esecuzione e informa l'ecosistema |
| `HC-CFO-CRO-01` | CFO → CRO | Margini commessa + forecast ricavi vs costi | CRO conferma pipeline allineata con forecast |
| `HC-CEO-CFO-01` | CEO → CFO | Richiesta envelope di spesa (budget dichiarato) | CFO valida e risponde go/no-go entro sessione |
| `HC-ECO-CFO-01` | Ecosistema → CFO | Evento costo (ogni spend API) | CFO attribution nel ledger entro fine sessione |

---

## 8. Namespace memoria (AgentDB `board/cfo`)

| Chiave | Tipo | Owner | Chi legge | Cosa contiene |
|---|---|---|---|---|
| `board/cfo/ledger-corrente` | JSON ledger | `cfo-cost-accountant` | tutti gli agenti CFO | Attribution costi sessione corrente |
| `board/cfo/budget-envelope` | JSON | `cfo-budget-guard` | tutti | Budget dichiarato per ecosistema + residuo |
| `board/cfo/tier-stats` | JSON | `cfo-tier-router` | `cfo-conductor`, `cfo-forecast-finance` | Distribuzione tier per tipo di task |
| `board/cfo/approvals-pending` | array JSON | `cfo-spend-approver` | `cfo-conductor` | Spese in attesa di ok esplicito |
| `board/cfo/runway-sessione` | JSON | `cfo-runway-tracker` | `cfo-conductor`, `cfo-budget-guard` | Risorse sessione residue (ADR-006) |
| `board/cfo/cost-alerts` | array JSON | `cfo-cost-sentinel` | `cfo-conductor` | Alert aperti (80% budget, drift) |
| `board/cfo/storico-costi` | JSON archive | `cfo-memoria` | `cfo-forecast-finance`, `cfo-roi-analyst` | Storico ledger + pattern di spreco |

---

## 9. Connessioni

- [[README]] · `README.md`
- [[BP-CFO]] · `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
- [[agenti]] · `agenti/` (10 schede roster)
- [[WF-BUDGET]] · `workflow/WF-BUDGET.md`
- [[WF-COST-REPORT]] · `workflow/WF-COST-REPORT.md`
- [[WF-SPEND-APPROVAL]] · `workflow/WF-SPEND-APPROVAL.md`
- [[STATE]] · `state/README.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
