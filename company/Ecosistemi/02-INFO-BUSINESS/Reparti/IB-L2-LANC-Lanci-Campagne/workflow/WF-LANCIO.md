---
Type: CONCEPT
Status: Active
Tags: #workflow #infobusiness #lanci #lancio #go-nogo #IB-L2-LANC
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-LANCIO — Lancio Completo T-30→T+7

> **Workflow:** WF-LANCIO · **Reparto:** IB-L2-LANC Lanci & Campagne
> **Trigger:** prodotto con gate qualità prodotto PASS + budget approvato da 09-OPERATIONS
> **Output:** lancio chiuso + debrief + coorte in onboarding + metriche nel CATALOGO
> **Gate di uscita:** tutti i gate verdi (APSOC, asset, dry-run, go/no-go) + debrief entro T+7

---

## Trigger

Un prodotto (corso o ebook) ha superato il gate qualità prodotto (WF-CORSO o WF-EBOOK PASS) e
09-OPERATIONS ha pre-approvato un budget. IB-COORD-LANCI riceve il brief lancio e apre il WF.
**Nessun lancio parte senza entrambi i prerequisiti.** Se manca il gate prodotto o il budget,
IB-COORD-LANCI blocca e restituisce al richiedente.

---

## Input JSON

```json
{
  "lancio_id": "lancio-<prodotto>-<YYYYMM>",
  "prodotto": {"id": "corso-X | ebook-Y", "gate_qualita": "PASS", "offer_stack": ["core", "bonus", "garanzia"]},
  "lista": {"size": 1200, "segmenti": ["caldi", "freddi"]},
  "finestra": {"cart_open": "2026-07-15", "cart_close": "2026-07-22"},
  "budget_proposto": {"ads": 1050, "tool": 90, "bonus": 0, "totale": 1140},
  "webinar": true,
  "brand_kit": "DE"
}
```

---

## Pipeline + owner

```
PRE-LANCIO (T-30 → T-1)
[T-30] IB-LANC-PLANNER — calendario completo + dipendenze + owner per task
[T-28] IB-COORD-LANCI — handoff HC-IN-IB-01 → 08-INTELLIGENCE (customer research / angoli)
[T-21] IB-COORD-LANCI — handoff HC-IB-CF-01 → 03-CONTENT-FACTORY (contenuti organici pre-lancio)
[T-14] IB-LANC-COPY-LIAISON — handoff HC-IB-MK-01 → 04-MARKETING (sales page + sequenza pre-lancio)
       GATE 1 — IB-LANC-QA: APSOC ≥80/100 (≥85 sales page) su TUTTO il copy ricevuto
[T-7]  IB-LANC-COPY-LIAISON — tutte le email cart open/close rientrate e validate vs acceptance
[T-3]  IB-LANC-ASSET — checklist 100% (page live, checkout testato, tracking attivo, email caricate)
       GATE 2 — IB-LANC-QA: asset-complete verificato sul campo (no falsi verdi)
[T-1]  IB-LANC-DRY — dry-run completo (simulazione invii + funnel) + stima costi → HC-IB-OPS-01
       GATE 3 — Cost-Sentinel/09-OPERATIONS: stima costi approvata (delta <10%)
[T-0-ε] IB-COORD-LANCI — GO/NO-GO: hive-mind consensus
       VOCI: ib-director + IB-LANC-QA + Quality-Sentinel + Brand-Voice-Sentinel + Cost-Sentinel
       GATE 4 — UN solo NO blocca il lancio. Nessun override.

CART OPEN (T0 → T+4/6)
[T0]    IB-COORD-LANCI — apertura: email 1 + post organico + webinar (se schedulato, WF-WEBINAR)
[T+1..n] sequenza cart open: 1 email = 1 obiezione (pattern APSOC), social proof, FAQ
[ogni 24h] IB-LANC-TRACKER — conversioni per step (opt-in, click, checkout, acquisto)
           → micro-aggiustamenti SOLO copy (non offerta, non prezzo) pre-approvati IB-COORD-LANCI

CART CLOSE (ultime 48h)
[T+close-2] scarcity REALE (deadline/bonus verificabile — mai finta, Mandato Art.2)
            email close ×3 (urgenza, FAQ finale, last call)
[T+close]   chiusura checkout all'ora stabilita (non posticipabile)

POST-LANCIO (T+7)
[T+1]   IB-COORD-LANCI — onboarding acquirenti ≤24h → handoff HC-IB-COMM-01 a IB-L2-COMM
[T+7]   IB-LANC-DEBRIEF — piano vs reale, root cause, ≥3 pattern → ReasoningBank (WF-DEBRIEF-LANCIO)
        IB-COORD-LANCI — report a ib-director; update CATALOGO con metriche reali
```

---

## Gate

| # | Gate | Owner | Criterio | Se FAIL |
|---|---|---|---|---|
| 1 | Copy APSOC | IB-LANC-QA | ≥80/100 (≥85 sales page) su ogni elemento scritto | rework 04-MARKETING, non si pubblica |
| 2 | Asset-complete | IB-LANC-QA | checklist 100% verificata sul campo | IB-LANC-ASSET completa, no go |
| 3 | Dry-run + costi | Cost-Sentinel/09-OPS | simulazione PASS + budget approvato (delta <10%) | rinegoziare budget o ridurre scope |
| 4 | Go/no-go | hive-mind consensus | 5 voci, un NO blocca | lancio bloccato, escalation ib-director |

---

## Output JSON

```json
{
  "lancio_id": "lancio-X-202607",
  "stato": "chiuso",
  "gate": {"apsoc": "PASS", "asset": "PASS", "dry_run": "PASS", "go_nogo": "GO"},
  "risultati": {"opt_in": 380, "checkout_avviati": 71, "acquisti": 34, "conversione_lista_%": 3.4, "aov": 211},
  "delta_budget_%": -3.0,
  "coorte_a_comm": true,
  "debrief_path": "infobusiness/lanci/lancio-X-202607/debrief.md",
  "catalogo_aggiornato": true
}
```

---

## Handoff

| Quando | Da → A | Contract | Payload |
|---|---|---|---|
| T-28 | IB-L2-LANC → 08-INT | HC-IN-IB-01 | brief customer research + ICP |
| T-21 | IB-L2-LANC → 03-CF | HC-IB-CF-01 | brief contenuti organici pre-lancio |
| T-14 | IB-L2-LANC → 04-MK | HC-IB-MK-01 | brief lancio + acceptance criteria |
| T-1 | IB-L2-LANC → 09-OPS | HC-IB-OPS-01 | stima costi dry-run |
| T+1 | IB-L2-LANC → IB-L2-COMM | HC-IB-COMM-01 | coorte acquirenti (onboarding ≤24h) |

---

## Dry-run (obbligatorio a T-1)

IB-LANC-DRY esegue: (1) simulazione invii di tutta la sequenza (destinatari, date, link, tracking),
(2) percorso funnel end-to-end (opt-in → sales page → checkout → grazie; + replay se webinar),
(3) stima costi (ads + tool + bonus) e margine atteso. Esito PASS richiesto per tenere il go/no-go.
**Senza dry-run PASS, il go/no-go non si tiene.** È il penultimo cancello prima del lancio.

---

## Esempio operativo

**Scenario:** lancio del corso "Vendi la Skill" su lista 1.200, finestra 7 giorni, con webinar.

- T-30: PLANNER produce il calendario; critical path = HC-IB-MK-01 → gate APSOC → asset → dry-run.
- T-14: COPY-LIAISON invia il brief; sales page rientra a 78/100 APSOC → GATE 1 FAIL → rework
  (manca gestione obiezione prezzo) → ri-audit a 86/100 → PASS.
- T-3: ASSET trova cart_close_3 non caricata → BLOCCATO → 04-MK carica → re-check verde.
- T-1: DRY simula tutto, stima costi €1.140 (delta -3% sul budget) → Cost-Sentinel approva.
- T-0-ε: go/no-go, 5 voci → GO.
- Cart open: TRACKER segnala checkout-to-purchase sotto target a T+2 → IB-COORD-LANCI autorizza
  anticipo email obiezione prezzo (solo copy) → recupero 6 vendite.
- T+7: DEBRIEF → 34 acquisti (piano 40), 3 pattern in ReasoningBank, CATALOGO aggiornato.

---

## Connessioni

- [[IB-COORD-LANCI]] · `agenti/IB-COORD-LANCI.md`
- [[IB-LANC-QA]] · `agenti/IB-LANC-QA.md`
- [[IB-LANC-DRY]] · `agenti/IB-LANC-DRY.md`
- [[WF-WEBINAR]] · `workflow/WF-WEBINAR.md`
- [[WF-DEBRIEF-LANCIO]] · `workflow/WF-DEBRIEF-LANCIO.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — scarcity reale)
