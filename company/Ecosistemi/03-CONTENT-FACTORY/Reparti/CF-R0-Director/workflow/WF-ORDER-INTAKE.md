---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #ordini #intake #gate #dispatch #cf-r0
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-ORDER-INTAKE — Validazione e Dispatch Ordine

> **ID:** WF-CF-D-001 · **Owner:** `cf-d-lead` · **Reparto:** CF-R0 Director
> **Trigger:** ricezione di un nuovo ordine da un committente
> **Marcatura dossier:** [WRAPPA-ESISTENTE skill `cf-order`] + [TARGET-V2 validazione multi-tenant e capacity check]

---

## Scopo

Trasformare un ordine grezzo da un committente in un ordine validato, con cartella
progetto creata, slot assegnato e area notificata. Il workflow è BLOCCANTE: un ordine
senza `brand_kit` o `icp` validati non entra mai nella coda produttiva — viene rifiutato
con motivo strutturato che consente al committente di correggere e risubmit.

**Gate di uscita:** ordine con brand_kit+icp validi, budget compatibile, cartella
`orders/<id>/` creata, slot assegnato in `cf/orders`, capo area L1 notificato.

---

## Attori

| Step | Agente CF-R0 | Agente/Reparto esterno |
|---|---|---|
| Ricezione ordine | `cf-d-lead` | Committente (01-AGENCY, 02-INFO, 04-MKT, 05-MB, DE-interno) |
| Gate contratto | `cf-d-qa` | — |
| Priorità coda | `cf-d-lead` | — |
| Check capacità | `cf-d-sched` | Capi area L1 (per modello capacità aggiornato) |
| Check budget | `cf-d-budget` | Reparti CF-R1/R3/R4/R5/R6 (per stime engine) |
| Dispatch e struttura | `cf-d-dispatch` | — |
| Notifica committente | `cf-d-status` | Committente |

---

## Flusso passo-passo

```
[TRIGGER]
Ordine grezzo da committente → cf-d-lead
  {order_id, committente, brand_kit, icp, formato, quantita, deadline, budget, note}
        │
        ▼
[STEP 1] cf-d-lead — verifica presenza fields obbligatori (pre-check rapido)
  → tutti i campi di primo livello presenti? (order_id, committente, brand_kit, icp,
    formato, quantita, deadline, budget.crediti_engine, budget.tier_max)
  → GATE-PRE: se manca un campo di primo livello: rifiuto immediato senza passare a cf-d-qa
    (efficienza: non sprecare il gate per un ordine palesemente incompleto)

        │ (GATE-PRE PASS)
        ▼
[STEP 2] cf-d-qa — Order Gate (BLOCCANTE)
  → Verifica brand_kit: file esiste in registry CF-R2? Schema JSON completo? (slug, visual, voice, canali)
  → Verifica icp: file esiste? Campi obbligatori presenti? (dolori, desideri, obiezioni, awareness_level, linguaggio)
  → Verifica formato: nella lista ammessa? (carosello-ig, video-ugc, video-avatar, articolo,
    newsletter, thumbnail, grafica, publish-only)
  → Verifica budget: tier_max valido? (haiku|sonnet|opus); per video: tier_max >= sonnet
  → GATE-QA:
      PASS → output strutturato con campi validati → prosegui a STEP 3
      FAIL → output FAIL con errori per campo → rifiuto al committente tramite cf-d-lead
             STOP WORKFLOW: l'ordine non prosegue; committente deve correggere e risubmit

        │ (GATE-QA PASS)
        ▼
[STEP 3] cf-d-lead — Decisione priorità coda
  → Legge la coda attiva in cf/orders
  → Applica regola precedenza: deadline → revenue impact → interno
  → Assegna priorità_coda (numero intero; 1 = massima priorità)
  → Identifica area di destinazione in base al formato:
      carosello-ig, thumbnail, grafica → CF-R5 (via Pre-Produzione CF-R1)
      video-ugc, video-avatar → CF-R3 (via Pre-Produzione CF-R1)
      articolo, newsletter → CF-R4 (via Pre-Produzione CF-R1)
      publish-only → CF-R7 (area Post-Produzione, salta Pre e Produzione)

        │
        ▼
[STEP 4] cf-d-sched — Capacity check
  → Verifica stato capacità per area/reparto identificato
  → Calcola slot disponibile: primo slot che consente completamento entro deadline - 1gg buffer QA
  → Classifica: verde / giallo / rosso
  → Se rosso: produce opzioni a cf-d-lead (posporre, batch merging, swarm)
  → GATE-CAPACITY:
      verde o giallo: slot assegnato → prosegui a STEP 5
      rosso: cf-d-lead decide; se nessuna opzione accettabile → rifiuto con motivazione

        │ (GATE-CAPACITY risolta)
        ▼
[STEP 5] cf-d-budget — Budget check
  → Raccoglie stime engine da ogni reparto coinvolto (CF-R1, CF-R3/R4/R5, CF-R6)
  → Somma totale crediti stimati
  → Confronto con budget_dichiarato e envelope_globale_cf
  → GATE-BUDGET:
      DENTRO_BUDGET → prosegui a STEP 6
      ALERT_BUDGET → cf-d-lead decide: richiedere approvazione committente o bloccare ordine

        │ (GATE-BUDGET risolto)
        ▼
[STEP 6] cf-d-dispatch — Creazione struttura e dispatch
  → Crea orders/<order_id>/order.json (copia ordine validato)
  → Crea orders/<order_id>/state.json (stato iniziale: dispatchato, area, slot, timestamp)
  → Crea orders/<order_id>/trace.jsonl (prima entry: dispatch con timestamp e rationale)
  → Aggiorna registry cf/orders con record ordine
  → Invia handoff al capo area L1 competente

        │
        ▼
[STEP 7] cf-d-status — Notifica committente
  → Invia milestone "ordine ricevuto e dispatchato" al committente
  → Include: order_id, area di destinazione, slot stimato, deadline confermata

[FINE WORKFLOW]
Gate di uscita verificato: cartella orders/<order_id>/ con 3 file, cf/orders aggiornato,
L1 notificato, committente notificato.
```

---

## Gate BLOCCANTE: ordine senza brand_kit o icp

La regola è assoluta e non ha eccezioni:

- `brand_kit` mancante → FAIL CF-D-QA → rifiuto ordine
- `brand_kit` presente ma brand non nel registry CF-R2 → FAIL CF-D-QA → rifiuto con istruzione onboarding
- `icp` mancante → FAIL CF-D-QA → rifiuto ordine
- `brand_kit` e `icp` presenti ma non correlati allo stesso slug → FAIL CF-D-QA

Non esiste una procedura di "ordine provvisorio senza brand_kit": sarebbe una violazione del
pattern 11 del Piano Maestro. Il committente deve completare l'onboarding brand in CF-R2 prima
di emettere ordini di produzione.

---

## Input / Output del workflow

**Input (ordine grezzo):**
```json
{
  "order_id": "CF-2026-0001",
  "committente": "01-AGENCY",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "icp": "brands/mentalita-brutale/icp.json",
  "formato": "carosello-ig",
  "quantita": 10,
  "deadline": "2026-06-25",
  "budget": {"crediti_engine": 120, "tier_max": "sonnet"},
  "note": "CTA: scopri il programma; canale: IG feed"
}
```

**Output (dispatch completato):**
```json
{
  "order_id": "CF-2026-0001",
  "workflow": "WF-ORDER-INTAKE",
  "esito": "PASS",
  "gate_qa": "PASS",
  "gate_capacity": "verde — slot 2026-06-20",
  "gate_budget": "DENTRO_BUDGET (105/120 crediti stimati)",
  "dispatch": "completato",
  "path_ordine": "orders/CF-2026-0001/",
  "priorita_coda": 1,
  "area": "pre-produzione → CF-R1",
  "slot": "2026-06-20",
  "deadline_confermata": "2026-06-25",
  "committente_notificato": true,
  "timestamp_completamento": "YYYY-MM-DDTHH:MM:SS"
}
```

**Output (rifiuto ordine):**
```json
{
  "order_id": "CF-2026-0001",
  "workflow": "WF-ORDER-INTAKE",
  "esito": "FAIL",
  "step_fallito": "GATE-QA",
  "motivo": "brand_kit non trovato nel registry CF-R2",
  "errori": [
    {
      "campo": "brand_kit",
      "valore_ricevuto": "brands/nuovo-brand/brand-kit.json",
      "problema": "file non trovato — brand non onboardato in CF-R2",
      "azione_richiesta": "completare WF-BRAND-ONBOARDING in CF-R2 prima di risubmit"
    }
  ],
  "dispatch": "non_eseguito",
  "risubmit": "possibile dopo risoluzione errori"
}
```

---

## Skill wrappata

Questo workflow wrappa la skill `cf-order` esistente per la fase di intake e creazione
cartella ordine. La skill non viene riscritta (ADR-003). Il wrapper aggiunge:
- Validazione multi-tenant (verifica brand_kit+icp nel registry CF-R2, non hardcoded)
- Capacity check via CF-D-SCHED (assente nella skill v1)
- Budget check via CF-D-BUDGET (assente nella skill v1)
- Trace.jsonl (struttura di tracciabilità aggiunta in v2)

---

## Connessioni

- [[cf-d-lead]] · `agenti/cf-d-lead.md` — orchestra il workflow
- [[cf-d-qa]] · `agenti/cf-d-qa.md` — step 2, gate BLOCCANTE
- [[cf-d-sched]] · `agenti/cf-d-sched.md` — step 4, capacity check
- [[cf-d-budget]] · `agenti/cf-d-budget.md` — step 5, budget check
- [[cf-d-dispatch]] · `agenti/cf-d-dispatch.md` — step 6, creazione struttura
- [[scripts/README]] · `scripts/README.md` — skill cf-order wrappata da questo workflow
