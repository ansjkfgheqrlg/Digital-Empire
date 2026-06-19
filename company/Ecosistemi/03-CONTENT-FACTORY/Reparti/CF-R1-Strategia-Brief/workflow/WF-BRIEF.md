---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #CF-R1 #brief #gate-bloccante
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-BRIEF — Da Ordine a Brief Eseguibile

> **ID:** WF-R1-001 · **Owner:** `cf-r1-coord` · **Reparto:** CF-R1 Strategia & Brief
> **Trigger:** ricezione ordine validato da CF-D-DISPATCH in `orders/<id>/order.json`

---

## Scopo

Trasformare ogni ordine validato in un `brief.json` eseguibile depositato in
`orders/<id>/01-brief/`. Il brief è il documento che autorizza la produzione:
senza brief.json con gate PASS, nessun reparto di produzione (R3/R4/R5) può avviare
il lavoro su quell'ordine. Il gate di CF-R1-QA è BLOCCANTE: un brief incompleto
non viene mai inoltrato alla produzione, neanche parzialmente.

**Gate d'uscita:** CF-R1-QA verifica la presenza e validità di tutti i campi
obbligatori (angle, hook_type, struttura_formato, canali, vincoli_brand, word_count
o durata_stimata, icp_ref). PASS = brief.json scritto e produzione autorizzata.
FAIL = rework + motivo strutturato; nessun avanzamento.

**Dry-run:** produce `brief-draft.json` in `orders/<id>/01-brief/` senza aggiornare
`state.json` fase completata e senza assegnare slot di produzione. Zero impatto coda.
Si attiva passando `dry_run: true` nell'ordine.

---

## Attori

| Step | Agente | Funzione |
|---|---|---|
| Coordinamento e supervisione | `cf-r1-coord` | Riceve ordine, sceglie workflow, verifica Mandato, gestisce rework |
| Analisi e contesto | `cf-r1-analyst` | Carica brand_kit + icp; identifica vincoli formato |
| Angoli creativi | `cf-r1-angle` | Produce 3 angle alternativi da libreria + trend |
| Selezione hook | `cf-r1-hook` | Sceglie hook_type da libreria coerente con icp |
| Gate bloccante | `cf-r1-qa` | Verifica tutti i campi obbligatori; PASS o FAIL |

---

## Flusso passo-passo

```
[TRIGGER]
orders/<id>/order.json ricevuto da CF-D-DISPATCH
        │
        ▼
[STEP 1] CF-R1-COORD — verifica pre-workflow
  → brand_kit percorso valido?
  → icp percorso valido?
  → formato riconosciuto?
  → GATE-0 (pre-verifica): se anche 1 campo mancante → BLOCCO + escalation CF-D-DISPATCH
  → Se dry_run: true → modalità dry-run (flag passato a ogni agente)
        │
        ▼
[STEP 2] CF-R1-ANALYST — analisi ordine e caricamento contesto
  → parse order.json
  → carica brand_kit/<slug>.json: voice (tono, esempi, parole_vietate), visual, canali
  → carica brands/<slug>/icp.json: dolori, desideri, obiezioni, awareness_level
  → mappa formato → vincoli tecnici (slide_max, durata, dimensioni, cta_richiesta)
  → produce context.json
  → anomalie? (brand_kit incompleto, icp vuoto) → segnala a CF-R1-COORD; non prosegue
        │
        ▼
[STEP 3] CF-R1-ANGLE — produzione 3 angle alternativi
  → input: context.json
  → interroga cf/patterns per brand_slug: quali formule hanno first_pass_rate alto?
  → recupera trend-attivi da CF-R1-TREND (se presenti)
  → produce angle_A (formula ad alto first-pass), angle_B (registro alternativo),
    angle_C (trend o contro-intuitivo)
  → verifica conformità brand_kit.voice su ogni angle prima dell'output
  → flag angle con dati non verificabili (Mandato Art.2)
        │
        ▼
[STEP 4] CF-R1-HOOK — selezione hook type
  → input: 3 angle + context.json
  → mapping formula_angle × awareness_level × brand.tono → hook_type candidati
  → selezione dalla libreria hook formule (priorità: first-pass storico per brand)
  → produce hook_type + hook_draft (1-2 righe applicato al contesto)
  → verifica assenza parole_vietate nel hook_draft
        │
        ▼
[STEP 5] CF-R1-QA — GATE BLOCCANTE
  → riceve brief_draft completo (angle + hook_type + context)
  → verifica checklist campo per campo:
    [ ] angle: presente e da CF-R1-ANGLE (non inventato)
    [ ] hook_type: presente e in libreria
    [ ] struttura_formato: coerente con formato ordine
    [ ] canali: array non vuoto, coerenti con brand_kit
    [ ] vincoli_brand: oggetto presente (anche se {})
    [ ] word_count o durata_stimata (o slide_count per carosello): numerico o range
    [ ] icp_ref: percorso o slug presente
  → PASS: scrive brief.json in orders/<id>/01-brief/
           aggiorna state.json: {"fase": "01-brief", "stato": "completata",
           "timestamp": "<ISO>", "owner": "cf-r1-coord", "gate_r1_qa": "PASS"}
  → FAIL: lista campi mancanti → CF-R1-COORD → rework agente specifico
           NON scrive nulla su disco
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Pre-verifica | brand_kit + icp + formato presenti nell'ordine | CF-R1-COORD | Avvio workflow |
| G1 — Anomalie contesto | Nessuna anomalia critica in context.json (brand_kit e icp completi) | CF-R1-ANALYST | Step 3 |
| G2 — Conformità Mandato | Nessun angle con claim non verificabile (Mandato Art.2) | CF-R1-COORD | Step 4 |
| G3 — Gate brief (PRINCIPALE) | Tutti i 7 campi obbligatori presenti e validi | CF-R1-QA | Avanzamento a produzione |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "order_id": "CF-2026-0042",
  "committente": "DE-interno",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "icp": "brands/mentalita-brutale/icp.json",
  "formato": "carosello-ig",
  "quantita": 3,
  "deadline": "2026-06-25",
  "budget": {"crediti_engine": 0, "tier_max": "haiku"},
  "note": "angle su errori comuni; CTA: segui per altri errori",
  "dry_run": false
}
```

**Output finale (PASS):**
```json
{
  "order_id": "CF-2026-0042",
  "brief_path": "orders/CF-2026-0042/01-brief/brief.json",
  "angle": "errore-costoso: I 3 errori che bloccano la crescita",
  "hook_type": "affermazione-diretta",
  "hook_draft": "Stai perdendo clienti ogni giorno. Non per mancanza di impegno — per questi 3 errori che non vedi.",
  "struttura_formato": "slide-deck",
  "canali": ["instagram"],
  "vincoli_brand": {
    "parole_vietate": ["forse", "quasi"],
    "palette": "dark",
    "cta_richiesta": "segui per altri errori"
  },
  "slide_count": "8-10",
  "icp_ref": "brands/mentalita-brutale/icp.json",
  "gate_r1_qa": "PASS",
  "n_rework": 0,
  "lead_time_min": 18
}
```

**Output dry-run:**
```json
{
  "order_id": "CF-2026-0042",
  "modalita": "dry-run",
  "brief_draft_path": "orders/CF-2026-0042/01-brief/brief-draft.json",
  "gate_r1_qa": "PASS (simulato)",
  "state_aggiornato": false,
  "slot_produzione_assegnati": false
}
```

---

## Gestione rework

Quando CF-R1-QA emette FAIL:
1. CF-R1-COORD riceve la lista campi mancanti.
2. Identifica quale agente è responsabile del campo mancante:
   - angle mancante → CF-R1-ANGLE rielabora.
   - hook_type fuori libreria → CF-R1-HOOK selezione alternativa.
   - vincoli_brand mancanti → CF-R1-ANALYST verifica context.json.
   - word_count/slide_count mancanti → CF-R1-ANALYST verifica vincoli formato.
3. Agente specifico rielabora solo il campo mancante (non tutta la pipeline).
4. Brief_draft aggiornato torna a CF-R1-QA per secondo tentativo.
5. Secondo FAIL → escalation a L1-PRE; terzo tentativo non parte senza autorizzazione.

---

## State

File: `orders/<id>/state.json`
```json
{
  "order_id": "CF-2026-0042",
  "fasi": {
    "01-brief": {
      "stato": "completata",
      "timestamp": "2026-06-19T10:52:00Z",
      "owner": "cf-r1-coord",
      "gate_r1_qa": "PASS",
      "n_rework": 0,
      "brief_path": "orders/CF-2026-0042/01-brief/brief.json"
    }
  }
}
```

---

## Connessioni

- [[cf-r1-coord]] · `agenti/cf-r1-coord.md`
- [[cf-r1-analyst]] · `agenti/cf-r1-analyst.md`
- [[cf-r1-angle]] · `agenti/cf-r1-angle.md`
- [[cf-r1-hook]] · `agenti/cf-r1-hook.md`
- [[cf-r1-qa]] · `agenti/cf-r1-qa.md`
- [[WF-CALENDAR]] · `workflow/WF-CALENDAR.md` — usa brief.json per popolare i slot
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
