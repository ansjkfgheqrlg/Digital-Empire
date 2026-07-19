---
Type: TOOL
Status: Active
Tags: #state #agency #qa #memoria #agentdb #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# state/ — Namespace `agency/a10`

> Memoria del reparto QA. È il punto di **aggregazione più sensibile** dell'ecosistema AGENCY:
> A10 tocca tutte le delivery di tutti i clienti. Per questo la regola R6 (zero PII, zero segreti)
> qui non è una precauzione — è una condizione di esistenza.

---

## 1. Namespace

| Chiave | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a10/reviews/{delivery_id}` | Verdetto unico, verdetti parziali, evidenze, timestamp, `review_index` | AG-A10-COORD |
| `agency/a10/defects/{delivery_id}` | Difetti: categoria, severità, componente, evidenza, stato rework | AG-A10-REVIEW |
| `agency/a10/uat/{delivery_id}` | Sessione UAT: test eseguiti, run autonoma, comprensione verificata | AG-A10-UAT |
| `agency/a10/brand/{delivery_id}` | Brand compliance: campo per campo, output campionati (riferimenti) | AG-A10-BRAND |
| `agency/a10/handover/{delivery_id}` | Checklist completezza pacchetto, voce per voce | AG-A10-HANDOVER |
| `agency/a10/patterns` | Pattern ricorrenti, report mensili, difetti sfuggiti al gate | AG-A10-LEARN |

---

## 2. Schema filesystem

```
agency/a10/
├── reviews/
│   └── {delivery_id}/
│       ├── review.json          — verdetto unico + checks G1..G7 + evidenze
│       ├── assignments.json     — chi ha auditato cosa
│       └── runtime.json         — esito per componente (AG-A10-REVIEW)
├── defects/
│   └── {delivery_id}/
│       └── defects.json         — lista difetti: id, categoria, severita, evidenza, stato_rework
├── uat/
│   └── {delivery_id}/
│       ├── session.json         — test eseguiti, esiti, punti di blocco, durata
│       └── autonomia.json       — run_autonoma (bool) + comprensione_verificata (bool)
├── brand/
│   └── {delivery_id}/
│       ├── checks.json          — campo per campo: atteso_ref vs osservato
│       └── samples.json         — riferimenti (path) agli output campionati
├── handover/
│   └── {delivery_id}/
│       └── checklist.json       — voce per voce: presente / assente / inutilizzabile
└── patterns/
    ├── defects.json             — pattern ricorrenti (≥3 occorrenze o ≥2 clienti)
    ├── escaped.json             — difetti sfuggiti al gate, emersi come ticket 90gg
    └── monthly/{YYYY-MM}.json   — report mensile qualità
```

---

## 3. Schema `review.json`

```json
{
  "delivery_id": "DLV-2026-0042",
  "cliente_ref": "CLI-017",
  "review_index": 1,
  "stato": "chiusa",
  "verdetto": "FAIL",
  "checks": {
    "G1": { "esito": "PASS", "owner": "AG-A10-REVIEW", "evidenza_ref": "runtime.json#c3" },
    "G2": { "esito": "FAIL", "owner": "AG-A10-REVIEW", "evidenza_ref": "runtime.json#c7" },
    "G3": { "esito": "PASS", "owner": "AG-A10-BRAND", "evidenza_ref": "brand/checks.json" },
    "G4": { "esito": "PASS", "owner": "AG-A10-HANDOVER", "evidenza_ref": "handover/checklist.json" },
    "G5": { "esito": "SKIP", "owner": "AG-A10-UAT", "motivo": "R5 — UAT non aperta: G2 rosso" },
    "G6": { "esito": "SKIP", "owner": "AG-A10-UAT", "motivo": "R5" },
    "G7": { "esito": "PASS", "owner": "AG-A10-COORD", "evidenza_ref": "assignments.json" }
  },
  "difetti_ref": ["DEF-0113"],
  "handoff_in": "HC-AG-QC-01",
  "handoff_out": "HC-QC-AG-01",
  "ts_handoff_in": "2026-07-11T09:00:00Z",
  "ts_verdetto": "2026-07-11T15:40:00Z"
}
```

**Campi vietati** (R6): nomi, email, telefoni, firme, credenziali, token, contenuti di output.
Il cliente è `cliente_ref`. Gli output sono `path`, mai contenuto.

---

## 4. Lifecycle di una review

```
aperta        ← HC-AG-QC-01 ricevuto; COORD crea review.json, review_index = N
   │
assegnata     ← REVIEW + BRAND + HANDOVER lanciati in parallelo (assignments.json)
   │
tecnica-ok?   ← G1..G4 raccolti
   │  NO (R5) → uat: SKIP → verdetto FAIL → chiusa
   │  SÌ
uat-aperta    ← AG-A10-UAT facilita la sessione col cliente (G5, G6)
   │
verdetto      ← COORD emette PASS o FAIL (G7 incluso) — binario, con evidenze (R2, R3)
   │
chiusa        ← handoff_out emesso; LEARN distilla i pattern
   │
   └─ FAIL → A4 fa rework → nuovo HC-AG-QC-01 → nuova review con review_index = N+1
             (la review precedente resta immutabile: la storia dei FAIL non si riscrive)
```

**Immutabilità**: una review `chiusa` non si modifica mai. Un rework apre una **nuova** review con
`review_index` incrementato. La % di PASS al primo review (KPI) esiste solo se la storia è intatta.

---

## 5. Accessi

| Chi | `agency/a10/*` | `agency/a4/*` | Repo cliente |
|---|---|---|---|
| Roster A10 | **read + write** | read | **read-only** (esecuzione test, mai modifica — R1) |
| Roster A4 | **nessun accesso in scrittura** (R8) | read + write | read + write |
| AG-DIR | read | read | — |
| 07-FORGE | read su `patterns/` | — | — |

**R8 in forma tecnica**: una scrittura in `agency/a10/*` con `author` fuori dal roster A10 è
**rifiutata** e registrata come incidente di integrità → `HC-QC-DIR-01` ad AG-DIR. Se A4 potesse
scrivere qui, l'indipendenza sarebbe una decorazione.

---

## 6. Ripartibilità a freddo

`review.json` è progettato per il rientro: un agente che riprende una review interrotta legge
`stato` + `checks` e riparte esattamente dal check mancante, senza riesecuzione dei check già
chiusi e senza riestrarre il contesto (test amnesia, §6 V2).

---

## Connessioni

- [[REGOLE]] · `../regole/REGOLE.md` — R6 (no PII) e R8 (indipendenza degli accessi)
- [[ARCHITETTURA]] · `../ARCHITETTURA.md §6` — namespace memoria del reparto
- [[SKILLS]] · `../skills/SKILLS.md` — i contratti JSON che atterrano in queste chiavi
