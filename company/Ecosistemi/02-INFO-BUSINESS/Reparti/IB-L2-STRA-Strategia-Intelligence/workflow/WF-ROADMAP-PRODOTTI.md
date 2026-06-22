---
Type: WORKFLOW
Status: Active
Tags: #workflow #info-business #strategia #roadmap #lanci #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# WF-ROADMAP-PRODOTTI — Roadmap Prodotti 6-12 Mesi

> **ID:** WF-STRA-002 · **Owner:** `IB-COORD-STRATEGIA` + `IB-STRA-ROADMAP`
> **Reparto:** IB-L2-STRA Strategia & Intelligence
> **Cadenza:** trimestrale + aggiornamento dopo ogni lancio
> **Output:** roadmap aggiornata + calendario lanci approvato → guida per tutte e 5 le aree
> **Gate di uscita:** lead time per ogni prodotto + buffer ≥30gg tra lanci consecutivi

---

## Scopo

Mantenere una roadmap prodotti a 6-12 mesi **coerente con la capacità produttiva e i lanci pianificati**.
Non un documento statico: si aggiorna dopo ogni lancio e dopo ogni ciclo intelligence. Sequenzia il
backlog validato in un calendario sostenibile, rispettando le dipendenze prodotto→lancio e il buffer di
recovery tra liste.

**Regola fondamentale:** nessuna roadmap si presenta al Director senza lead time stimato per ogni prodotto
e senza buffer ≥30gg tra lanci consecutivi. Una roadmap che la produzione non può reggere (P4) è peggio di
nessuna roadmap: genera slittamenti silenziosi.

---

## Trigger

- **Programmato:** ciclo trimestrale (revisione completa della roadmap).
- **Post-lancio:** dopo ogni lancio reale — si ricalcola il calendario coi tempi effettivi e si verifica
  che il buffer di recovery della lista sia stato rispettato.
- **Su escalation:** cambio trend dirompente segnalato da WF-PRODUCT-INTELLIGENCE → ri-priorizzazione.

---

## Attori

| Step | Agente IB-L2-STRA | Agente/Reparto esterno |
|---|---|---|
| Import dati | `IB-STRA-ROADMAP` | IB-L2-PROD (catalogo live + lead time), IB-L2-LANC (calendario) |
| Sequenziamento | `IB-STRA-ROADMAP` | — |
| Check ICP | `IB-STRA-ICP` | IB-L2-COMM (segnali community) |
| Allineamento contenuti | `IB-STRA-ROADMAP` | Content Factory (03-CONTENT-FACTORY) |
| Gate prove + buffer | `IB-STRA-QA` | — |
| Approvazione | `IB-COORD-STRATEGIA` | ib-director |
| Handoff lanci | `IB-COORD-STRATEGIA` | IB-L2-LANC |

---

## Flusso passo-passo

```
[TRIGGER]
Ciclo trimestrale OPPURE lancio appena concluso OPPURE escalation trend
         │
         ▼
[STEP 1] IB-STRA-ROADMAP — import
  → catalogo prodotti live (da IB-L2-PROD)
  → backlog validato: idee score ≥60 in stato "validato" (da backlog/idee.json)
  → capacità area prodotto: lead time per tipo prodotto (da IB-L2-PROD, dato reale — no stima di comodo)
  → calendario lanci pianificati (da IB-L2-LANC)
  → GATE-1: ogni prodotto candidato ha un lead time? mancante → richiesta a IB-L2-PROD, non si inventa

         │
         ▼
[STEP 2] IB-STRA-ROADMAP — sequenziamento
  → ordina i prodotti per dipendenze (prodotto → lancio → eventuale cross-sell)
  → applica buffer ≥30gg tra lanci consecutivi (la lista recovery deve riprendersi)
  → allinea con Content Factory: ogni lancio ha finestra contenuti organici a supporto
  → produce roadmap candidata con date di lancio pianificate

         │
         ▼
[STEP 3] IB-STRA-ICP — check copertura pain
  → input: roadmap candidata + ICP corrente
  → i prodotti pianificati coprono ancora i pain point ICP attuali? (l'ICP è vivo — P5)
  → GATE-2: copertura PASS → prosegui; pain scoperto critico → segnala a ROADMAP per ri-sequenziamento

         │
         ▼
[STEP 4] IB-STRA-QA — GATE "prove + sostenibilità"
  → ogni prodotto ha lead time stimato (reale, da PROD)? nessun lead time inventato?
  → ogni coppia di lanci consecutivi ha gap ≥30gg?
  → le idee in roadmap hanno score ≥60 + fonti (eredità WF-PRODUCT-INTELLIGENCE)?
  → PASS → procede a [5] · FAIL → torna a IB-STRA-ROADMAP col difetto specifico

         │
         ▼
[STEP 5] IB-COORD-STRATEGIA — proposta a Director
  → sintetizza la roadmap in one-pager (sequenza, razionale, buffer, dipendenze, rischi)
  → presenta a ib-director
  → GATE-3: approvazione Director → store in roadmap/roadmap_corrente.md; versione precedente in archivio

         │
   ┌─────┴──────────┐
APPROVATA        RIMANDATA
   │                 │
   ▼                 ▼
[STEP 6a]        [STEP 6b]
Store roadmap     Note di rimando registrate:
roadmap_corrente  "conflitto capacità / priorità
+ archivia        da rinegoziare". Ritorno a [2]
precedente        con vincoli aggiornati.
   │
   ▼
[STEP 7] IB-COORD-STRATEGIA → IB-L2-LANC
  → handoff HC-STRA-LANC-01: roadmap lanci approvata (sequenza, buffer ≥30gg, dipendenze)
  → la roadmap guida il calendario lanci di tutte e 5 le aree
         │
         ▼
Dopo ogni lancio reale → re-trigger post-lancio:
  → confronta date pianificate vs effettive
  → aggiorna KPI "% prodotti a roadmap nei tempi"
  → deriva tracciata in roadmap_archivio/
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Lead time presente | Ogni prodotto candidato ha lead time reale da IB-L2-PROD | IB-STRA-ROADMAP | Sequenziamento |
| G2 — Copertura ICP | I prodotti pianificati coprono i pain ICP attuali | IB-STRA-ICP | Gate QA |
| G3 — Prove + buffer ≥30gg | Lead time reale per prodotto + nessun gap <30gg + score ≥60 con fonti | IB-STRA-QA | Proposta a Director |
| G4 — Approvazione Director | Roadmap approvata da ib-director | ib-director | Store + handoff lanci |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "ciclo_trimestrale | post_lancio | escalation_trend",
  "periodo": "2026Q3",
  "catalogo_live": ["prodotto_id", "..."],
  "backlog_validato": "infobusiness/strategia/backlog/idee.json (stato=validato, score>=60)",
  "capacita_prod": {"mini-corso": "lead_time_gg da IB-L2-PROD", "ebook": "lead_time_gg"},
  "calendario_lanci": "da IB-L2-LANC",
  "buffer_min_gg": 30
}
```

**Output finale (approvata):**
```json
{
  "workflow": "WF-ROADMAP-PRODOTTI",
  "roadmap_id": "ROADMAP-2026Q3",
  "orizzonte_mesi": 12,
  "prodotti": [
    {"prodotto": "Mini-corso consulenti", "idea_id": "IDEA-012", "lead_time_gg": 21,
     "data_lancio_pianificata": "2026-09-01", "buffer_da_precedente_gg": 35, "icp_fit": "PASS"}
  ],
  "buffer_min_rispettato": true,
  "qa_gate": "PASS",
  "approvato_da_director": true,
  "handoff": "HC-STRA-LANC-01 → IB-L2-LANC",
  "namespace": "infobusiness/strategia/roadmap/roadmap_corrente.md",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

**Output (rimandata):**
```json
{
  "workflow": "WF-ROADMAP-PRODOTTI",
  "roadmap_id": "ROADMAP-2026Q3",
  "qa_gate": "FAIL",
  "motivo": "2 lanci con gap 18gg (<30gg); lead time 'ebook avanzato' assente da IB-L2-PROD",
  "approvato_da_director": false,
  "azione": "ritorno a STEP 2 — ri-sequenziamento con buffer + richiesta lead time a PROD"
}
```

---

## Handoff

| Contract | Da → A | Payload | Quando |
|---|---|---|---|
| `HC-STRA-LANC-01` | IB-COORD-STRATEGIA → IB-L2-LANC | roadmap lanci approvata (sequenza, buffer ≥30gg, dipendenze) | step [7], se approvata |
| `HC-COMM-STRA-01` | IB-L2-COMM → IB-STRA-ICP | segnali community per check copertura pain | step [3] |

**Acceptance HC-STRA-LANC-01:** lead time per prodotto + buffer ≥30gg tra lanci consecutivi + QA PASS +
approvazione Director. Senza tutti e quattro, l'handoff non parte (R6).

---

## State

File: `infobusiness/strategia/roadmap/roadmap_corrente.md` (+ front-matter di stato).
- Creato/aggiornato allo store dopo approvazione Director.
- Campi `lead_time_gg` e `buffer_da_precedente_gg` OBBLIGATORI per ogni prodotto.
- Versione precedente sempre spostata in `roadmap/roadmap_archivio/` (tracciamento deriva).
- Roadmap con `approvato_da_director: true` e buffer <30gg = anomalia di integrità (vedi `state/README.md`).

---

## Dry-run

**Scenario:** revisione trimestrale Q3 2026. Backlog ha IDEA-012 (score 82) validata + 2 idee 60-70.

1. **[1] ROADMAP** importa: 3 prodotti live, IDEA-012 validata, lead time mini-corso 21gg (da PROD),
   calendario lanci IB-L2-LANC. Lead time "ebook avanzato" mancante → richiesto a PROD, non inventato.
2. **[2] ROADMAP** sequenzia: IDEA-012 lancio 1-set, prodotto B lancio 5-ott (buffer 35gg). Allinea
   Content Factory: finestra contenuti -14gg per ogni lancio.
3. **[3] ICP** verifica: IDEA-012 copre pain "automazione delivery consulenti" → ancora caldo (47 domande
   community) → copertura PASS.
4. **[4] QA** controlla: lead time presente per tutti, buffer 35gg ≥30, IDEA-012 score 82 con fonti → **PASS**.
   (Una bozza con gap 18gg tra due lanci sarebbe stata FAIL e rispedita a STEP 2.)
5. **[5] COORD** one-pager a ib-director → approvata → store in `roadmap_corrente.md`, versione Q2 in archivio.
6. **[7]** HC-STRA-LANC-01 a IB-L2-LANC. Dopo il lancio 1-set: re-trigger post-lancio, data effettiva
   confrontata → KPI "% nei tempi" aggiornato. Log in wiki.

**Esito dry-run:** roadmap approvata, buffer rispettato, 1 lead time correttamente richiesto a PROD invece
che inventato. Gate funzionante.

---

## Connessioni

- [[ib-stra-roadmap-builder]] · `agenti/ib-stra-roadmap-builder.md`
- [[ib-stra-icp-profiler]] · `agenti/ib-stra-icp-profiler.md`
- [[ib-stra-qa-verificatore-strategia]] · `agenti/ib-stra-qa-verificatore-strategia.md`
- [[ib-coord-strategia]] · `agenti/ib-coord-strategia.md`
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md` — fornisce il backlog validato
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-STRA WF-ROADMAP-PRODOTTI`
