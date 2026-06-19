---
Type: STATE
Status: Active
Tags: #state #namespace #registry #cf-r0 #orders #trace #cf-kpi
Created: 2026-06-19
Last updated: 2026-06-19
---

# State e Namespace — CF-R0 Director

> **Reparto:** CF-R0 · **Ecosistema:** 03-CONTENT-FACTORY · **Versione:** v2

---

## 1. Namespace AgentDB del reparto

| Namespace | Contenuto | Owner scrittura | Owner lettura | Agente writer |
|---|---|---|---|---|
| `cf/orders` | Registry globale ordini attivi: id, committente, area, stato, slot, deadline | CF-D-DISPATCH | CF-D-STATUS, CF-D-LEAD, CF-D-SCHED, CF-D-LEARN | CF-D-DISPATCH via WF-ORDER-INTAKE |
| `cf/kpi` | Report KPI settimanali aggregati, pattern confermati, trigger_forge | CF-D-LEARN | CF-D-LEAD, Board | CF-D-LEARN via WF-DIRECTOR-REVIEW |

---

## 2. Struttura cartella per ordine

Ogni ordine validato e dispatchato crea la seguente struttura su disco:

```
orders/
└── <order_id>/
    ├── order.json       — copia immutabile dell'ordine originale validato
    ├── state.json       — stato corrente mutabile (aggiornato ad ogni cambio fase)
    └── trace.jsonl      — log append-only di ogni evento sull'ordine
```

La cartella viene creata da CF-D-DISPATCH. I file `state.json` e `trace.jsonl`
vengono aggiornati dagli agenti dei reparti successivi (L1-PRE, L1-PROD, L1-POST)
man mano che l'ordine avanza attraverso le fasi.

---

## 3. Schema `orders/<id>/order.json`

Copia immutabile dell'ordine come ricevuto e validato. Non viene mai modificata dopo
la creazione. È il riferimento di verità per il contratto originale.

```json
{
  "order_id": "CF-2026-0001",
  "committente": "01-AGENCY",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "icp": "brands/mentalita-brutale/icp.json",
  "formato": "carosello-ig",
  "quantita": 10,
  "deadline": "2026-06-25",
  "budget": {
    "crediti_engine": 120,
    "tier_max": "sonnet"
  },
  "note": "CTA: scopri il programma; canale: IG feed",
  "timestamp_ricezione": "YYYY-MM-DDTHH:MM:SS",
  "qa_gate": "PASS",
  "timestamp_qa": "YYYY-MM-DDTHH:MM:SS"
}
```

---

## 4. Schema `orders/<id>/state.json`

Stato corrente mutabile dell'ordine. Ogni agente che compie un'azione sull'ordine
aggiorna questo file e scrive l'evento corrispondente in trace.jsonl.

```json
{
  "order_id": "CF-2026-0001",
  "stato": "dispatchato | in_brief | brief_completato | in_produzione | produzione_completata | in_qa | qa_completato | consegnato | annullato",
  "fase_corrente": "pre-produzione | produzione | post-produzione | completato",
  "area": "CF-R1 | CF-R3 | CF-R4 | CF-R5 | CF-R6 | CF-R7",
  "priorita": 1,
  "slot_stimato": "YYYY-MM-DD",
  "deadline": "YYYY-MM-DD",
  "committente": "01-AGENCY",
  "budget_consuntivo_crediti": 0,
  "owner_corrente": "L1-PRE | L1-PROD | L1-POST",
  "timestamp_dispatch": "YYYY-MM-DDTHH:MM:SS",
  "timestamp_ultimo_aggiornamento": "YYYY-MM-DDTHH:MM:SS",
  "milestone": {
    "dispatchato": "YYYY-MM-DDTHH:MM:SS",
    "brief_completato": null,
    "produzione_avviata": null,
    "qa_avviato": null,
    "consegnato": null
  }
}
```

I campi `null` vengono popolati a runtime dagli agenti dei reparti successivi.
CF-D-STATUS legge questo file per calcolare le milestone e gli alert.

---

## 5. Schema `orders/<id>/trace.jsonl`

Log append-only: ogni riga è un evento JSON separato da newline. Non si modificano
le righe esistenti — si aggiunge sempre e solo in append. Il trace è la storia
completa di ogni decisione sull'ordine.

**Struttura di ogni entry:**
```json
{"timestamp": "YYYY-MM-DDTHH:MM:SS", "agente": "cf-d-dispatch", "azione": "dispatch", "dettaglio": "area: CF-R1, priorita: 1, rationale: deadline 5gg + committente Agency", "crediti_usati": 0}
{"timestamp": "YYYY-MM-DDTHH:MM:SS", "agente": "cf-r1-coord", "azione": "brief_assegnato", "dettaglio": "brief-analyst: CF-R1-A02", "crediti_usati": 5}
{"timestamp": "YYYY-MM-DDTHH:MM:SS", "agente": "cf-r1-qa", "azione": "brief_approvato", "dettaglio": "gate brief: PASS, tutti i campi obbligatori presenti", "crediti_usati": 2}
```

**Regola integrità:** il campo `crediti_usati` in ogni entry è lo step di accumulo
verso il budget consuntivo. CF-D-BUDGET può sommare tutte le entry per ricavare
il `budget_consuntivo_crediti` reale a consuntivo.

---

## 6. Schema record `cf/orders` (registry globale)

Il registry è l'indice veloce degli ordini attivi. Contiene solo i dati necessari
per la dashboard e lo scheduling — il dettaglio è nei file su disco.

```json
{
  "order_id": "CF-2026-0001",
  "committente": "01-AGENCY",
  "formato": "carosello-ig",
  "area": "CF-R1",
  "stato": "in_brief",
  "priorita": 1,
  "slot_stimato": "2026-06-20",
  "deadline": "2026-06-25",
  "timestamp_dispatch": "YYYY-MM-DDTHH:MM:SS"
}
```

---

## 7. Regole di integrità del namespace

1. **Un ordine non entra nel registry `cf/orders` senza `order.json` + `state.json` + `trace.jsonl`
   su disco.** L'integrità è atomica: o tutte e tre le risorse esistono, o nessuna entra nel registry.
2. **`order.json` è immutabile.** Se il committente vuole modificare un ordine già dispatchato,
   deve aprire un nuovo ordine (con nuovo order_id) e annullare il precedente tramite CF-D-LEAD.
3. **`trace.jsonl` è append-only.** Nessuna riga viene modificata o cancellata. In caso di errore
   in un'azione, si aggiunge una entry di tipo "correzione" con il riferimento alla entry errata.
4. **`state.json` viene aggiornato solo dall'agente owner_corrente dell'ordine in quella fase.**
   Un agente di CF-R5 non aggiorna lo state.json di un ordine che è ancora in CF-R1.
5. **Ordini annullati** — lo stato diventa "annullato" con timestamp e motivo nel trace.jsonl.
   La cartella non viene eliminata: è archivio consultabile per 90 giorni (policy DE).

---

## Connessioni

- [[cf-d-dispatch]] · `agenti/cf-d-dispatch.md` — writer degli state.json e registry cf/orders
- [[cf-d-status]] · `agenti/cf-d-status.md` — reader principale per dashboard e alert
- [[cf-d-budget]] · `agenti/cf-d-budget.md` — legge trace.jsonl per consuntivo crediti
- [[WF-ORDER-INTAKE]] · `workflow/WF-ORDER-INTAKE.md` — workflow che crea la struttura
