---
Type: WORKFLOW
Status: Active
Tags: #workflow #infobusiness #validazione #gate #mvp #scoring #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# WF-VALIDAZIONE — Gate d'Ingresso Idea Prodotto

> **ID:** WF-IB-PROD-001 · **Owner:** `IB-PROD-VALID` (sotto `IB-COORD-PRODOTTO`)
> **Reparto:** IB-L2-PROD Produzione Prodotti
> **Trigger:** nuova idea prodotto (da IB-L2-STRA via `HC-STRA-IB-01`, BACKLOG, community, segnale agency)

---

## Scopo

Filtrare le idee prodotto con un gate quantitativo **prima** di impegnare il team in produzione.
Nessun prodotto entra in WF-CORSO o WF-EBOOK senza aver superato questo workflow. L'idea viene
sottoposta a scoring /100 su 5 criteri e, se supera Gate 1 (≥60), a un MVP test reale di 7 giorni
(5 "sì, lo comprerei" da persone ICP). Solo con entrambi i gate PASS si produce un brief validato.

**Regola fondamentale (ADR-003):** questo workflow WRAPPA il kernel esistente di
`Lancio corso skill beast/processo lancio.txt` / Product Creation Lab — non inventa un nuovo motore.
Lo scoring formalizza quel processo; non lo sostituisce.

---

## Attori

| Step | Agente IB-L2-PROD | Agente/Reparto esterno |
|---|---|---|
| Ingresso idea | `IB-PROD-VALID` | IB-L2-STRA (`HC-STRA-IB-01`) / BACKLOG |
| Scoring 5 criteri | `IB-PROD-VALID` | — (skill `customer-research` per ICP) |
| Gate 1 (≥60) | `IB-PROD-VALID` | `IB-PROD-QA` (verifica evidenze, non opinioni) |
| Disegno MVP test | `IB-PROD-VALID` | skill `mvp-validator` (target V2) |
| Esecuzione MVP test | `IB-PROD-VALID` | ICP reale (canale dichiarato) |
| Gate 2 (5 sì) | `IB-PROD-VALID` | `IB-PROD-QA` (verifica risposte reali) |
| Verdetto avvio | `IB-COORD-PRODOTTO` | — |

---

## Flusso passo-passo

```
[TRIGGER]
Idea prodotto arriva:
  HC-STRA-IB-01 {idea, problema, raw_path, icp_ipotetico, posizionamento}
  oppure ripescata da BACKLOG / segnale community / segnale agency
         │
         ▼
[STEP 1] IB-PROD-VALID — intake e completezza brief
  → il brief ha tutti i campi per lo scoring? (problema, raw, ICP, differenziazione, posizionamento)
  → GATE-0: brief completo → prosegui; incompleto → richiesta completamento a IB-L2-STRA
            (non si scora un brief monco — sarebbe un numero inventato)
         │
         ▼
[STEP 2] IB-PROD-VALID — scoring /100 su 5 criteri (idea_scorer.py target V2)
  → (1) problema reale e misurabile           /20
  → (2) materiale raw già disponibile          /20
  → (3) ICP chiaro e raggiungibile             /20
  → (4) differenziazione da offerta esistente  /20
  → (5) allineamento posizionamento DE         /20
  → TOTALE /100 + breakdown per criterio + evidenza per ogni punteggio
         │
         ▼
[STEP 3] GATE 1 — score ≥60?
   ┌─────┴───────────────┐
score ≥60              score <60
   │                      │
   ▼                      ▼
prosegui a MVP        IDEA IN BACKLOG (ADR-005)
                      motivo registrato, mai in produzione
         │
         ▼
[STEP 4] IB-PROD-VALID — disegno MVP test 7gg
  → definisce: domanda, ICP target reale, canale (DM/email/community), soglia = 5 "sì, lo comprerei"
  → NON è un sondaggio di gradimento: è intenzione d'acquisto reale da persone ICP
         │
         ▼
[STEP 5] MVP test in esecuzione (max 7gg)
  → IB-PROD-VALID raccoglie risposte reali; nessuna risposta inventata o stimata
  → IB-PROD-QA verifica che le risposte vengano da persone ICP reali (no amici, no opinioni interne)
         │
         ▼
[STEP 6] GATE 2 — almeno 5 "sì, lo comprerei" reali in 7gg?
   ┌─────┴───────────────┐
≥5 sì                  <5 sì
   │                      │
   ▼                      ▼
[STEP 7a]              [STEP 7b]
brief validato         IDEA IN BACKLOG
→ IB-COORD-PRODOTTO    learning registrato:
  approva avvio        "domanda insufficiente su questo ICP/prezzo"
  produzione           motivo registrato, mai in produzione
   │
   ▼
[STEP 8] IB-COORD-PRODOTTO — routing
  → corso? → input WF-CORSO
  → ebook? → input WF-EBOOK
  → state.json esito: brief_validato + destinazione workflow
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Brief completo | Tutti i campi per lo scoring presenti | IB-PROD-VALID | Scoring |
| G1 — Score ≥60/100 | Somma dei 5 criteri ≥60, ogni punteggio con evidenza | IB-PROD-VALID + IB-PROD-QA | Avvio MVP test |
| G2 — MVP test PASS | ≥5 "sì, lo comprerei" reali da ICP in 7gg | IB-PROD-VALID + IB-PROD-QA | Avvio produzione |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "HC-STRA-IB-01",
  "idea_id": "IDEA-001",
  "titolo": "Corso Skill Beast",
  "problema": "...",
  "raw_path": "Formazzione/Skill Beast/",
  "icp_ipotetico": "...",
  "posizionamento": "..."
}
```

**Output finale (PASS):**
```json
{
  "idea_id": "IDEA-001",
  "score": 78,
  "breakdown": {"problema_reale": 18, "raw_disponibile": 20, "icp_chiaro": 14,
                "differenziazione": 12, "posizionamento_de": 14},
  "gate_1": "PASS",
  "mvp_test": {"si_comprerei": 6, "soglia": 5, "gate_2": "PASS"},
  "esito": "brief_validato",
  "destinazione": "WF-CORSO",
  "namespace": "infobusiness/prod/validazione/state.json"
}
```

**Output finale (FAIL):**
```json
{
  "idea_id": "IDEA-002",
  "score": 52,
  "gate_1": "FAIL",
  "esito": "backlog",
  "motivo_fail": "differenziazione debole vs offerta esistente; raw parziale",
  "namespace": "infobusiness/prod/validazione/state.json"
}
```

---

## State

File: `infobusiness/prod/validazione/state.json`
- Creato all'intake dell'idea.
- Campo `esito` OBBLIGATORIO alla chiusura: "brief_validato" / "backlog".
- Idea in BACKLOG conserva `motivo_fail` per ripescaggio futuro (ADR-005); non eliminata.

---

## Connessioni

- [[ib-prod-valid]] · `agenti/ib-prod-valid.md` — owner del gate d'ingresso
- [[ib-prod-qa]] · `agenti/ib-prod-qa.md` — verifica evidenze e risposte reali (no opinioni)
- [[WF-CORSO]] · `workflow/WF-CORSO.md` — destinazione di un brief validato (corso)
- [[WF-EBOOK]] · `workflow/WF-EBOOK.md` — destinazione di un brief validato (ebook)
- [[REGOLE]] · `regole/REGOLE.md` — R1: nessuna produzione senza WF-VALIDAZIONE PASS
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-PROD WF-VALIDAZIONE`
