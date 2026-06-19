---
Type: WORKFLOW
Status: Active
Tags: #workflow #tracking #utm #eventi #conversion-api #analytics #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-TRACKING-SETUP — Piano di Tracking Completo

> **ID:** WF-AN-001 · **Owner:** `an-lead` · **Reparto:** L2.4 Analytics & Ottimizzazione
> **Trigger:** avvio di una nuova campagna o funnel prima del lancio

---

## Scopo

Produrre il tracking plan completo per ogni campagna o funnel prima del lancio:
eventi con nome, trigger e valore; parametri UTM; conversion API server-side;
consegna a 06-PLATFORM per implementazione; verifica pre-lancio che nessun evento
sia "fantasma" (definito ma non implementato).

**Gate d'uscita:** AN1 verifica che ogni evento nel piano sia visibile nella piattaforma
di analytics prima del lancio. `eventi_fantasma: 0` è il criterio di PASS.
Un solo evento fantasma blocca il lancio fino alla risoluzione.

---

## Attori

| Step | Agente L2.4 | Agente/Reparto esterno |
|---|---|---|
| Ricezione brief e coordinamento | `an-lead` | MKT-Conductor (se routing centralizzato) |
| Produzione tracking plan | `an1-tracking-engineer` | — |
| Implementazione tecnica | `an1-tracking-engineer` (specifica) | 06-PLATFORM (implementa) |
| Verifica pre-lancio | `an1-tracking-engineer` | — |
| Monitoraggio post-lancio | `an2-attribution-analyst` | — |

---

## Flusso passo-passo

```
[TRIGGER]
Brief campagna/funnel → AN-LEAD
  {campagna_id, canali, obiettivi misurazione, icp, piattaforma analytics}
        │
        ▼
[STEP 1] AN-LEAD — validazione brief
  → obiettivi di misurazione dichiarati? (CTR, opt-in rate, vendite, reply)
  → canali completi? (ogni canale richiede UTM dedicati)
  → icp definito? (necessario per correlare performance con patterns ICP)
  → GATE-1: brief completo → prosegui; incompleto → richiesta al mittente

        │
        ▼
[STEP 2] AN1 — mapping obiettivi → eventi
  → per ogni obiettivo: identifica il momento tecnico esatto
    ("vendite corso" → "checkout completato" → evento snake_case con valore €)
  → per ogni landing: identifica gli eventi di micro-conversione (scroll depth, click CTA)
    sulla base dello schema CA3 (L2.6) se disponibile
  → lista eventi completa: nome, trigger, valore, piattaforma

        │
        ▼
[STEP 3] AN1 — definizione UTM
  → struttura UTM coerente con schema AN2 (no ambiguità attribuzione)
  → utm_campaign: ID campagna univoco
  → utm_content: copy_id per tracciare varianti
  → utm_source/medium: per canale
  → verifica: stesso utm_campaign non usato per campagne distinte in parallelo

        │
        ▼
[STEP 4] AN1 — conversion API (per eventi ad alto valore)
  → identifica eventi da inviare server-side (opt-in, acquisto)
  → verifica PII: dati personali nel payload? → hashing obbligatorio (SHA-256)
  → specifica event_id per deduplicazione (server-side + pixel client-side)
  → GATE-2: privacy check → PII in chiaro nel payload = blocco

        │
        ▼
[STEP 5] AN1 → 06-PLATFORM — consegna tracking plan
  → formato JSON strutturato (tracking_plan_id, lista eventi, UTM schema, conversion API)
  → disponibile per chiarimenti tecnici durante implementazione

        │
        ▼
[STEP 6] AN1 — verifica pre-lancio
  → accede alla piattaforma di analytics (debug mode o test events)
  → verifica: ogni evento della lista è visibile? Trigger corretto? Valore corretto?
  → GATE-3 (bloccante): eventi_fantasma = 0 → PASS, lancio autorizzato
             eventi_fantasma > 0 → blocco lancio + segnalazione a 06-PLATFORM per fix

        │
        ▼
[STEP 7] AN2 — setup attribuzione
  → acquisisce il tracking plan approvato
  → configura il sistema di lettura performance per copy_id (UTM → dashboard)
  → ready per raccolta dati post-lancio nel ciclo WF-OPTIMIZATION-LOOP
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Brief completo | Obiettivi, canali, ICP presenti | AN-LEAD | Avvio workflow |
| G2 — Privacy check | Nessun dato PII in chiaro nel payload conversion API | AN1 | Consegna a 06-PLATFORM |
| G3 — Verifica pre-lancio | `eventi_fantasma = 0` confermato in debug mode | AN1 | Lancio campagna |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "campagna_id": "CAMP-003",
  "tipo": "campagna_ads",
  "canali": ["ads-meta", "landing-page"],
  "obiettivi": ["click ad", "form fill landing", "vendita corso"],
  "icp": "agency-owner-ita",
  "piattaforma_analytics": "GA4 + Meta Pixel",
  "privacy": {"liste_email": false, "checkout_dati_personali": true}
}
```

**Output finale:**
```json
{
  "tracking_plan_id": "TP-003",
  "campagna_id": "CAMP-003",
  "eventi_totali": 5,
  "eventi_fantasma": 0,
  "utm_schema": "utm_campaign=CAMP-003-agency-owner, utm_content=CP-001|CP-002",
  "conversion_api": {
    "eventi_server_side": ["landing_form_submit", "corso_purchase_complete"],
    "pii_minimizzato": true
  },
  "stato_implementazione": "06-PLATFORM verificato — PASS",
  "gate_g3": "PASS",
  "pronto_per_lancio": true
}
```

---

## State

File: `marketing/analytics/tracking/{campagna_id}/state.json`
- Aggiornato ad ogni step del workflow.
- Ripartibile a freddo: AN1 può riprendere dal punto di interruzione.
- Archiviato dopo verifica pre-lancio PASS.

---

## Connessioni

- [[an-lead]] · `agenti/an-lead.md`
- [[an1-tracking-engineer]] · `agenti/an1-tracking-engineer.md`
- [[an2-attribution-analyst]] · `agenti/an2-attribution-analyst.md`
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md` — usa il tracking prodotto qui
- [[06-ECOSISTEMA-PLATFORM]] · implementa il piano tecnico
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
