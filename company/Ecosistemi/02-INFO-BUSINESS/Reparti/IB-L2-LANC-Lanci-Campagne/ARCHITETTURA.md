---
Type: CONCEPT
Status: Active
Tags: #architettura #infobusiness #lanci #campagne #IB-L2-LANC
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — IB-L2-LANC Lanci & Campagne

> Cartella-workflow CF-grade. Un lancio = un'operazione militare a calendario T-30→T+7.
> Dossier sorgente: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-LANC

---

## Topologia del team

```
                   ┌──────────────────────────────────┐
                   │     IB-COORD-LANCI (Opus)          │
                   │  regista lancio, go/no-go, timeline│
                   └──────────────┬───────────────────-┘
                                  │
     ┌──────────────┬─────────────┼─────────────┬──────────────┐
     │              │             │             │              │
┌────▼─────┐  ┌─────▼──────┐ ┌────▼──────┐ ┌────▼──────┐ ┌─────▼──────┐
│ PLANNER  │  │ COPY-      │ │ ASSET     │ │ WEBINAR   │ │ TRACKER    │
│ (Sonnet) │  │ LIAISON    │ │ (Haiku)   │ │ (Sonnet)  │ │ (Haiku)    │
│ timeline │  │ (Sonnet)   │ │ checklist │ │ script    │ │ conversioni│
└──────────┘  └─────┬──────┘ └───────────┘ └───────────┘ └────────────┘
                    │ handoff HC-IB-MK-01
              ┌─────▼──────┐        ┌─────────────┐       ┌──────────────┐
              │ 04-MARKETING│       │ IB-LANC-DRY │       │ IB-LANC-     │
              │ (copy)      │       │ (Sonnet)    │       │ DEBRIEF      │
              └─────────────┘       │ dry-run T-1 │       │ (Sonnet)     │
                                    └──────┬──────┘       │ post-mortem  │
                                           │              └──────────────┘
                   ┌───────────────────────▼────────────────────────┐
                   │     IB-LANC-QA (Opus) — gate trasversale         │
                   │  copy APSOC ≥80 · asset-complete · dry-run OK    │
                   │  (bloccante su ogni step, mai suggerisce copy)   │
                   └─────────────────────────────────────────────────┘
```

**Topologia:** star da `IB-COORD-LANCI` → specialisti per fase del lancio. La pipeline è
sequenziale sul calendario (PLANNER → COPY-LIAISON → ASSET → DRY → go/no-go → TRACKER →
DEBRIEF), ma i task interni a ogni fase girano in parallelo. `IB-LANC-QA` opera trasversalmente
come gate bloccante su copy, asset e dry-run, indipendente da chi produce.

---

## Livelli gerarchici interni

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `IB-COORD-LANCI` | Opus | Regista lancio, timeline, go/no-go con consensus, report director |
| L1 — QA indipendente | `IB-LANC-QA` | Opus | Gate copy/asset/dry-run; potere di NO; non produce copy |
| L2 — Planner & Liaison | `IB-LANC-PLANNER` · `IB-LANC-COPY-LIAISON` · `IB-LANC-WEBINAR` · `IB-LANC-DRY` · `IB-LANC-DEBRIEF` | Sonnet | Pianificazione, handoff, webinar, dry-run, debrief |
| L3 — Executor | `IB-LANC-ASSET` · `IB-LANC-TRACKER` | Haiku | Checklist asset, monitoraggio conversioni giornaliero |

---

## Flussi principali

### WF-LANCIO (lancio completo T-30→T+7)
```
Trigger: prodotto con gate qualità PASS + budget approvato OPERATIONS
  T-30 IB-LANC-PLANNER: calendario + dipendenze + owner per task
  T-28 handoff HC-IN-IB-01 → 08-INTELLIGENCE (customer research / angoli)
  T-21 handoff HC-IB-CF-01 → 03-CF (contenuti organici pre-lancio)
  T-14 handoff HC-IB-MK-01 → 04-MARKETING (sales page + sequenza)
       GATE IB-LANC-QA: APSOC ≥80 su TUTTO il copy ricevuto
  T-7  IB-LANC-COPY-LIAISON: email cart open/close rientrate e validate
  T-3  IB-LANC-ASSET: checklist 100% (page live, checkout, tracking, email)
  T-1  IB-LANC-DRY: dry-run completo + stima costi → GATE Cost-Sentinel/OPERATIONS
  T-0-ε GO/NO-GO: hive-mind consensus (5 voci). UN NO blocca.
  T0→T+4/6 CART OPEN: IB-LANC-TRACKER conversioni ogni 24h
  ultime 48h CART CLOSE: scarcity REALE, email close ×3
  T+7 POST: onboarding → IB-L2-COMM, IB-LANC-DEBRIEF → ReasoningBank
Output: lancio chiuso + debrief + coorte in onboarding + metriche nel catalogo
Gate di uscita: tutti i gate verdi + debrief scritto entro T+7
```

### WF-WEBINAR (webinar di vendita come asset di lancio)
```
Trigger: lancio con webinar schedulato nel calendario WF-LANCIO
  → IB-LANC-WEBINAR: struttura (apertura storytelling da Webinar/, valore, pitch APSOC, Q&A, CTA)
  GATE IB-LANC-QA: script APSOC + brand voice + zero promesse senza prova
  → coordinamento 03-CF per setup tecnico (video/audio)
  → esecuzione live/registrazione (Max al microfono)
  → replay funnel (link protetto → opt-in → replay → scarcity reale sul replay)
Output: webinar registrato + replay funnel live + metriche registrati/partecipanti
```

### WF-DEBRIEF-LANCIO (apprendimento strutturato)
```
Trigger: cart close completato (entro T+7)
  → IB-LANC-DEBRIEF: piano vs reale (ogni KPI), root cause scarti ≥10%,
    pattern da replicare/evitare, raccomandazione skill/agente da aggiornare
  → distillato in infobusiness/reasoningbank (≥3 pattern, zero numeri approssimati)
  → update CATALOGO con metriche reali del prodotto
Gate di uscita: debrief scritto entro T+7 + ≥3 pattern validati
```

### WF-FOLLOWUP-COPY (libreria evergreen)
```
Trigger: WF-DEBRIEF-LANCIO completato
  → IB-LANC-DEBRIEF: top 3 email per conversione + top 3 hook
  → IB-LANC-COPY-LIAISON: handoff a Area Vendite (libreria evergreen) + segnalazione 04-MARKETING
Gate di uscita: solo copy con metriche reali documentate entra nella libreria
```

---

## Flussi con ecosistemi esterni

### IB-L2-LANC → 04-MARKETING (HC-IB-MK-01)
```
IB-LANC-COPY-LIAISON compone il brief lancio → 04-MARKETING produce copy.
Payload: {lancio_id, tipo, prodotto, icp, offer_stack, deadline, acceptance_criteria, brand_kit}
Rientro: ogni asset validato da IB-LANC-COPY-LIAISON vs acceptance; gate APSOC da IB-LANC-QA.
Se APSOC <80 → rework, non si pubblica.
```

### IB-L2-LANC → 09-OPERATIONS (stima costi dry-run)
```
IB-LANC-DRY produce stima costi a T-1 → Cost-Sentinel/OPERATIONS approva.
Payload: {lancio_id, costo_ads_stimato, costo_tool, costo_bonus, totale, margine_atteso}
Gate: budget approvato prima del go/no-go. Delta reale vs stima target <10%.
```

### IB-L2-LANC → IB-L2-COMM (onboarding acquirenti)
```
A cart close, IB-COORD-LANCI passa la coorte acquirenti a IB-L2-COMM.
Payload: {lancio_id, n_acquirenti, lista_acquirenti, prodotto, data_accesso}
SLA: onboarding ≤24h dall'acquisto (WF-ONBOARDING-STUDENTE).
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-IN-IB-01` | IB-L2-LANC → 08-INT | brief customer research + ICP | angoli/language map con fonte, consegna entro T-21 |
| `HC-IB-CF-01` | IB-L2-LANC → 03-CF | brief contenuti organici pre-lancio | brief per pezzo con ICP, format, deadline |
| `HC-IB-MK-01` | IB-L2-LANC → 04-MK | brief lancio (offer, icp, deadline, acceptance) | copy rientrato con APSOC ≥80 (≥85 sales page) |
| `HC-IB-OPS-01` | IB-L2-LANC → 09-OPS | stima costi dry-run | budget approvato da Cost-Sentinel prima del go |
| `HC-IB-COMM-01` | IB-L2-LANC → IB-L2-COMM | coorte acquirenti | lista completa, onboarding ≤24h |

---

## Namespace memoria

```
infobusiness/lanci/
├── <lancio-id>/
│   ├── state.json            → ogni step: status, gate, timestamp, errori
│   ├── calendario.md         → timeline T-30→T+7 con owner e dipendenze (PLANNER)
│   ├── handoff/              → payload e rientri HC-IB-MK-01, HC-IN-IB-01, HC-IB-CF-01
│   ├── copy-approvati/       → copy con APSOC ≥80 validato (COPY-LIAISON + QA)
│   ├── asset-checklist.md    → checklist asset 100% (ASSET)
│   ├── dry-run.md            → simulazione + stima costi T-1 (DRY)
│   ├── go-nogo.md            → verbale consensus go/no-go
│   ├── tracking/             → conversioni per step, report giornalieri (TRACKER)
│   └── debrief.md            → post-mortem: piano vs reale, root cause (DEBRIEF)
├── webinar/
│   └── state.json            → stato webinar + replay funnel
├── libreria-evergreen/       → top copy/hook con metriche reali (WF-FOLLOWUP-COPY)
└── reasoningbank/            → pattern distillati per lancio (namespace infobusiness/reasoningbank)
```

---

## Skill del reparto

| Skill | File | Funzione |
|---|---|---|
| `launch-runbook` (P0, nuova) | `skills/SKILLS.md` | Calendario T-30→T+7 deterministico + checklist gate per step |
| `launch` (esistente) | mapping skill holding | Ausiliaria: playbook lancio per COORD e PLANNER |
| `market-launch` (esistente) | mapping skill holding | Ausiliaria: orchestrazione lancio lato MK per COPY-LIAISON |
| `emails` (esistente) | mapping skill holding | Ausiliaria: supervisione sequenze cart open/close |
| `cro-copy-architect` (esistente) | mapping skill holding | Riferimento APSOC per il gate IB-LANC-QA (audit) |

---

## Connessioni

- [[README]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/README.md`
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-LANC
- [[WF-LANCIO]] · `workflow/WF-LANCIO.md`
- [[WF-WEBINAR]] · `workflow/WF-WEBINAR.md`
- [[WF-DEBRIEF-LANCIO]] · `workflow/WF-DEBRIEF-LANCIO.md`
- [[WF-FOLLOWUP-COPY]] · `workflow/WF-FOLLOWUP-COPY.md`
- [[IB-LAUNCH-coordinator]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-LAUNCH-coordinator.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — scarcity reale)
