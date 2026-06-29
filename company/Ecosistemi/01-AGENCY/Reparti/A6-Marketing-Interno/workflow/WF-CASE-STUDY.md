---
Type: WORKFLOW
Status: Active
Tags: #workflow #case-study #proof #apsoc #brand-gate #prove-non-promesse #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-CASE-STUDY — Da Delivery Chiusa a Case Study Verificato

> **ID:** WF-A6-001 · **Owner:** `ag-a6-coord` + `ag-a6-case`
> **Reparto:** A6 Marketing Interno & Proof
> **Trigger:** Gate Delivery firmato (A4) + 90gg supporto chiusi

---

## Scopo

Trasformare ogni delivery chiusa in un case study APSOC pubblicato con metriche REALI del
cliente. È il workflow cuore del reparto: applica il Mandato Art.2 ("prove non promesse")
end-to-end — la raccolta del proof è attiva, ogni numero cita la fonte, il Brand Gate blocca
qualsiasi claim non verificato. L'output diventa munizione per A2 (outreach) e A3 (preventivi).

**Regola fondamentale:** nessun numero entra nel case study senza fonte verificata dal cliente
o dal report A4. Se il cliente non fornisce metriche → case study qualitativo (descrittivo,
senza numeri), mai fabbricato. [DM] dove il dato non esiste.

---

## Attori

| Step | Agente A6 | Agente/Reparto esterno |
|---|---|---|
| Segnale delivery | `ag-a6-coord` | A4-Delivery (Gate firmato) |
| Raccolta proof | `ag-a6-proof` | Cliente (testimonianza + consenso) |
| Scrittura case study | `ag-a6-case` (skill `case-study-forge`) | — |
| Brand Gate | `ag-a6-qa` | — |
| Asset grafici | `ag-a6-coord` (brief) | 03-CONTENT-FACTORY (HC-AG-CF-01) |
| Pubblicazione | `ag-a6-coord` | 06-PLATFORM (HC-AG-PL-01) |
| Munizioni | `ag-a6-coord` | A2-Acquisizione + A3-Preventivi |

---

## Flusso passo-passo

```
[TRIGGER]
A4-Delivery → Gate Delivery firmato + 90gg supporto chiusi
  {cliente, servizio_erogato, kpi_delivery (agency/kpi), consenso_richiesto}
         │
         ▼
[STEP 1] AG-A6-COORD — pre-screening
  → verifica: 90gg chiusi? consenso del cliente richiesto/in corso?
  → memory_search("agency/a6/proof") — testimonianza già raccolta? evita doppia richiesta
  → GATE-1: trigger valido (90gg + delivery firmata) → prosegui; altrimenti attende

         │
         ▼
[STEP 2] AG-A6-PROOF — raccolta proof ATTIVA
  → legge agency/kpi (dati già documentati da A4) per ridurre il carico sul cliente
  → contatta il cliente (messaggio personalizzato, NON automatico):
    metriche reali (reply rate, tempo setup, ROI, conversione) + testimonianza + consenso
  → ogni metrica con campo `fonte`; numero senza fonte → NON registrato come verificato
  → casi:
    - cliente fornisce numeri → proof_status: metriche_verificate
    - cliente fornisce solo testimonianza → proof_status: qualitativo
    - cliente non risponde (2 follow-up, poi stop) → proof_status: cliente_silente → CHIUSURA
  → GATE-2: proof disponibile (verificato o qualitativo) → prosegui; cliente_silente → chiude WF

         │
         ▼
[STEP 3] AG-A6-CASE — scrittura case study (skill case-study-forge)
  → struttura APSOC, il caso APRE con il PROBLEMA del cliente (R5 — P prima di S):
    A — contesto e settore del cliente
    P — il problema reale prima dell'intervento
    S — cosa ha fatto Digital Empire (il servizio erogato)
    O — obiezioni del cliente gestite nel percorso
    C — risultato con metriche REALI, ogni numero cita fonte inline
    CTA — invito coerente (call / preventivo)
  → se proof_status qualitativo → C descrive il risultato senza numeri (mai fabbricati)
  → produce brief asset per 03-CONTENT-FACTORY (2-3 numeri chiave da visualizzare)

         │
         ▼
[STEP 4] AG-A6-QA — Brand Gate (BLOCCANTE)
  → ogni claim numerico ha fonte in agency/a6/proof? (R1)
  → consenso del cliente documentato? (R2) — altrimenti anonimizza o blocca
  → brand voice conforme (Mandato Art.1)? nessuna promessa, solo proof (Art.2)?
  → P precede S? (R5)
  → GATE-3: PASS → prosegui; FAIL → rework MIRATO sulla sezione indicata (mai "rifai tutto")

         │
   ┌─────┴──────────┐
  PASS            FAIL
   │                 │
   ▼                 ▼
[STEP 5]        rework AG-A6-CASE sulla sezione FAIL → ri-gate (torna a STEP 4)
Handoff asset
HC-AG-CF-01 →
03-CONTENT-FACTORY produce carosello/reel social proof dal brief
         │
         ▼
[STEP 6] AG-A6-COORD — pubblicazione
  → HC-AG-PL-01 → 06-PLATFORM pubblica il case study su agency-empire-landing
  → aggiorna wiki + namespace agency/a6/case-studies/{case_id} (stato: pubblicato)
  → NESSUN deploy autonomo da A6 (R6)

         │
         ▼
[STEP 7] AG-A6-COORD — munizioni
  → notifica A2-Acquisizione: case study pronto come ancora per outreach
  → notifica A3-Preventivi: metriche reali come prova nei preventivi
  → AG-A6-INBOUND traccia la performance inbound del nuovo case study
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Trigger valido | Gate Delivery firmato + 90gg chiusi | AG-A6-COORD | Avvio raccolta proof |
| G2 — Proof disponibile | Metriche verificate O testimonianza qualitativa | AG-A6-PROOF | Scrittura case study |
| G3 — Brand Gate | Claim con fonte + consenso + brand voice + P prima di S | AG-A6-QA | Pubblicazione |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "gate_delivery_firmato",
  "cliente": "CLIENTE-X",
  "servizio_erogato": "CRO sprint 4 settimane + 90gg supporto",
  "kpi_delivery_ref": "agency/kpi/CLIENTE-X",
  "consenso_pubblicazione": "richiesto"
}
```

**Output finale (metriche verificate):**
```json
{
  "case_id": "CASE-001",
  "cliente": "CLIENTE-X",
  "proof_status": "metriche_verificate",
  "metriche": [
    {"nome": "conversione checkout", "valore": "+38%", "fonte": "report A4 + dashboard cliente + conferma scritta"}
  ],
  "brand_gate": "PASS",
  "asset_status": "consegnato",
  "stato_finale": "pubblicato",
  "munizioni_a": ["A2-Acquisizione", "A3-Preventivi"],
  "namespace": "agency/a6/case-studies/CASE-001"
}
```

**Output finale (cliente silente):**
```json
{
  "case_id": "CASE-002",
  "cliente": "CLIENTE-Y",
  "proof_status": "cliente_silente",
  "motivo": "nessuna risposta dopo 2 follow-up a 7gg",
  "stato_finale": "chiuso_senza_pubblicazione",
  "nota": "nessuna pressione; rapporto preservato (P4)",
  "namespace": "agency/a6/case-studies/CASE-002"
}
```

---

## Esempio CF-grade end-to-end

**Scenario reale (struttura, numeri [DM] finché prima delivery chiusa):** cliente e-commerce,
sprint CRO di 4 settimane chiuso, 90gg supporto terminati, consenso confermato.

1. **G1:** A4 firma il Gate; 90gg chiusi. Trigger valido.
2. **Proof:** A4 ha documentato in `agency/kpi` il dato di conversione checkout. AG-A6-PROOF
   contatta il cliente → conferma il numero sul proprio dashboard + testimonianza + consenso.
   `proof_status: metriche_verificate`, fonte = "report A4 + dashboard cliente + conferma scritta".
3. **Case study:** AG-A6-CASE apre con il problema ("checkout che perdeva utenti"), non con noi.
   C: conversione checkout migliorata, valore reale citato con fonte. Brief carosello a CF.
4. **G3 Brand Gate:** ogni numero ha fonte? sì. Consenso? sì. P prima di S? sì. → PASS.
5. **Asset:** 03-CONTENT-FACTORY produce il carosello social proof dal brief.
6. **Pubblicazione:** 06-PLATFORM pubblica su agency-empire-landing.
7. **Munizioni:** A2 usa il case study come ancora; A3 lo cita nei preventivi e-commerce.

> Nota Mandato Art.2: in questo dossier i valori numerici concreti restano [DM] finché non
> esiste una delivery reale chiusa con metriche verificate dal cliente. Il workflow è pronto;
> i numeri si popolano al primo case study reale.

---

## State

File: `agency/a6/case-studies/{case_id}/state.json`
- Creato allo STEP 1 (pre-screening valido).
- Campo `brand_gate` OBBLIGATORIO: `pending` → `PASS`/`FAIL`.
- Campo `proof_status` OBBLIGATORIO: ogni case study dichiara se è verificato, qualitativo o silente.
- Case study `pubblicato` senza `brand_gate: PASS` = anomalia di integrità (vedi `state/README.md`).

---

## Connessioni

- [[ag-a6-proof]] · `agenti/ag-a6-proof.md` — raccolta proof attiva
- [[ag-a6-case]] · `agenti/ag-a6-case.md` — scrittura APSOC con `case-study-forge`
- [[ag-a6-qa]] · `agenti/ag-a6-qa.md` — Brand Gate bloccante
- [[WF-ASSET-VETRINA]] · `workflow/WF-ASSET-VETRINA.md` — pubblicazione su landing
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6 WF-CASE-STUDY`
