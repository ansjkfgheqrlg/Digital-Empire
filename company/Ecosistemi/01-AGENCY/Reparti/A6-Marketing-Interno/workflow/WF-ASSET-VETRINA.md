---
Type: WORKFLOW
Status: Active
Tags: #workflow #vetrina #landing #presentazione #brand-gate #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-ASSET-VETRINA — Manutenzione Vetrina dell'Agency

> **ID:** WF-A6-002 · **Owner:** `ag-a6-coord`
> **Reparto:** A6 Marketing Interno & Proof
> **Trigger:** gap vetrina identificato (caso studio mancante, social proof obsoleto, calo conversione inbound)

---

## Scopo

Mantenere aggiornati e performanti gli asset di vetrina dell'agency: `agency-empire-landing`
e `presentazione-empire.vercel.app`. Il reparto NON costruisce né deploya le pagine (lo fa
06-PLATFORM): identifica i gap, genera i ticket, fa passare ogni modifica dal Brand Gate, e
coordina il deploy. La presentazione è la CTA standard di ogni canale outreach: deve sempre
riflettere i case study più recenti e verificati.

**Regola fondamentale:** ogni modifica della vetrina passa dal Brand Gate (AG-A6-QA, Sentinel
Brand-Voice) PRIMA del deploy. Il deploy avviene SOLO via 06-PLATFORM. A6 non tocca il codice (R6).

---

## Attori

| Step | Agente A6 | Agente/Reparto esterno |
|---|---|---|
| Identificazione gap | `ag-a6-coord` + `ag-a6-inbound` | — |
| Nuovo case study (se manca) | `ag-a6-case` | (vedi WF-CASE-STUDY) |
| Brief modifica landing | `ag-a6-coord` | — |
| Brand Gate | `ag-a6-qa` | — |
| Implementazione + deploy | — | 06-PLATFORM (HC-AG-PL-01) |
| Verifica post-deploy | `ag-a6-inbound` | — |

---

## Flusso passo-passo

```
[TRIGGER]
Gap vetrina identificato:
  - AG-A6-INBOUND segnala: visitatori settore X senza case study dedicato
  - AG-A6-COORD nota: social proof obsoleto / case study nuovo da inserire
  - build rossa / pagina non aggiornata
         │
         ▼
[STEP 1] AG-A6-COORD — triage del gap
  → tipo di gap: contenuto mancante (case study) o modifica strutturale (sezione/layout)?
  → priorità per impatto qualitativo (da segnale AG-A6-INBOUND; numeri [DM] se non misurati)
  → GATE-1: gap reale e prioritario → prosegui

         │
   ┌─────┴───────────────┐
contenuto mancante     modifica strutturale
   │                       │
   ▼                       ▼
[STEP 2a]               [STEP 2b]
ticket ad AG-A6-CASE    brief modifica landing →
(→ WF-CASE-STUDY per    sezioni da cambiare, obiettivo,
 il case study)          social proof da aggiornare
   │                       │
   └───────────┬───────────┘
               ▼
[STEP 3] AG-A6-QA — Brand Gate sulla modifica
  → il contenuto rispetta "prove non promesse"? (R1)
  → ogni claim ha fonte? consenso cliente per nuovi case study? (R2)
  → brand voice conforme (Sentinel Brand-Voice, Mandato Art.1)?
  → GATE-2: PASS → prosegui; FAIL → rework mirato

         │
         ▼
[STEP 4] 06-PLATFORM (HC-AG-PL-01) — implementazione + deploy
  → riceve il brief approvato; implementa la modifica
  → deploy (A6 non deploya — R6)
  → se build rossa → alert a AG-A6-COORD; gap resta aperto in agency/a6/vetrina

         │
         ▼
[STEP 5] AG-A6-INBOUND — verifica post-deploy
  → la modifica è live e corretta?
  → traccia l'effetto sulla conversione inbound (baseline → nuovo periodo)
  → aggiorna agency/a6/vetrina (gap chiuso) + agency/a6/inbound
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Gap reale | Gap concreto e prioritario (non cosmetico arbitrario) | AG-A6-COORD | Avvio modifica |
| G2 — Brand Gate | Claim con fonte + consenso + brand voice conforme | AG-A6-QA | Deploy via 06-PLATFORM |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "gap_vetrina",
  "tipo_gap": "case_study_mancante | social_proof_obsoleto | sezione_da_aggiornare | build_rossa",
  "asset": "agency-empire-landing | presentazione-empire.vercel.app",
  "fonte_segnale": "AG-A6-INBOUND | AG-A6-COORD",
  "dettaglio": "es. nessun case study e-commerce per visitatori e-commerce"
}
```

**Output finale:**
```json
{
  "gap_id": "GAP-001",
  "tipo_gap": "case_study_mancante",
  "azione": "nuovo case study e-commerce pubblicato + sezione social proof aggiornata",
  "brand_gate": "PASS",
  "deploy": "06-PLATFORM — live",
  "effetto_inbound": "[DM] — misurato da AG-A6-INBOUND nel periodo successivo",
  "namespace": "agency/a6/vetrina/GAP-001"
}
```

---

## State

File: `agency/a6/vetrina/{gap_id}.json`
- Creato allo STEP 1 (gap identificato).
- Campo `brand_gate` OBBLIGATORIO prima del deploy.
- Campo `deploy` tracciato (richiesto / live / build_rossa).
- Build rossa → gap resta `aperto`; alert a HC-AG-PL-01.

---

## Connessioni

- [[ag-a6-coord]] · `agenti/ag-a6-coord.md` — triage e coordinamento gap
- [[ag-a6-inbound]] · `agenti/ag-a6-inbound.md` — fonte dei gap e verifica post-deploy
- [[ag-a6-qa]] · `agenti/ag-a6-qa.md` — Brand Gate prima del deploy
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md` — fornitore dei case study per la vetrina
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6 WF-ASSET-VETRINA`
