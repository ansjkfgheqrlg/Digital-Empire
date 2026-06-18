---
Type: WORKFLOW
Status: Active
Tags: #workflow #funnel #design #apsoc #conversion #marketing #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-FUNNEL-DESIGN — Design Funnel Completo

> **ID:** WF-CA-001 · **Owner:** `conv-lead` · **Reparto:** L2.6 Conversion Architecture
> **Trigger:** richiesta funnel completo da committente (02-INFO, 01-AGENCY, 04-MKT, 05-MB)

---

## Scopo

Trasformare il brief di un committente in un'architettura funnel completa e operativa:
stage map ToFu→MoFu→BoFu con obiettivo APSOC per stage, copy gated per ogni stage
(richiesto a L2.1), sequenze email per ogni stage (richieste a L2.3), brief tecnico
landing approvato per 06-PLATFORM. Il funnel esce solo dopo gate CA-QA verde su
coerenza APSOC end-to-end.

---

## Attori

| Step | Agente L2.6 | Agente/Reparto esterno |
|---|---|---|
| Ricezione e validazione | `conv-lead` | MKT-Conductor (se routing centralizzato) |
| Stage map | `ca1-funnel-strategist` | — |
| Struttura landing | `ca2-landing-page-strategist` | — |
| Micro-conversioni | `ca3-micro-conversion-analyst` | AN5 (L2.4) |
| Copy per stage | `conv-lead` (richiesta) | COPY-MASTER / A8 (L2.1) |
| Email per stage | `conv-lead` (richiesta) | EMAIL-LEAD / E1 (L2.3) |
| Gate finale | `ca-qa-conversion-verifier` | — |
| Implementazione | `conv-lead` (brief) | 06-PLATFORM (costruisce le pagine) |

---

## Flusso passo-passo

```
[TRIGGER]
Brief committente → CONV-LEAD
  {committente, prodotto, obiettivo, icp, awareness_level, canali, deadline}
         │
         ▼
[STEP 1] CONV-LEAD — validazione brief
  → campi obbligatori presenti?
  → ICP in namespace marketing/avatars/? Se assente → richiesta T-AVATAR prima di procedere
  → awareness_level dichiarato? Se assente → CONV-LEAD deduce e dichiara nel payload
  → GATE-1: brief completo → prosegui; incompleto → richiesta al committente

         │
         ▼
[STEP 2] CA1 — stage map
  → memory_search("marketing/cro/funnels") — funnel simile precedente?
  → progetta: ToFu / MoFu / BoFu con obiettivo APSOC per stage
  → per ogni stage: canale, punto di contatto, brief copy, brief email, segnalazione landing
  → verifica coerenza interna (P prima di S — Art.4.2 Mandato)
  → consegna stage map a CONV-LEAD

         │
         ▼
[STEP 3] CA2 — struttura landing (per ogni stage con landing)
  → per ogni landing: struttura sezioni (hero→proof→offer→objections→CTA)
  → brief copy per sezione (→ L2.1)
  → brief tecnico per 06-PLATFORM (sezioni, performance target, eventi tracking, message-match)
  → consegna a CONV-LEAD

         │
         ▼
[STEP 4] CA3 — schema micro-conversioni
  → per ogni stage/landing: mappa percorso comportamentale (eventi → diagnosi drop pre-mappate)
  → consegna schema ad AN5 (L2.4) per piano di misurazione
  → consegna copia a CONV-LEAD

         │
         ▼   ← PARALLELO (step 5a e 5b si eseguono in parallelo)
[STEP 5a] CONV-LEAD → L2.1 — richiesta copy per ogni stage
  → contratto: {formato, awareness_level, icp, obiettivo, deadline}
  → L2.1 esegue WF-COPY-FULL / WF-COPY-SALES-PAGE / WF-COPY-SOCIAL / WF-COPY-AD
  → copy gated (G1 ≥80, ≥85 per sales page) torna a CONV-LEAD

[STEP 5b] CONV-LEAD → L2.3 — richiesta email per stage MoFu/BoFu
  → contratto: {tipo sequenza, obiettivo stage, icp, n_email, deadline}
  → L2.3 esegue WF-EMAIL-NURTURE / WF-EMAIL-LAUNCH
  → sequenze gated tornano a CONV-LEAD
         │
         ▼
[STEP 6] CA-QA — gate APSOC end-to-end
  → verifica: progressione APSOC completa su tutti gli stage?
  → verifica: P prima di S rispettato?
  → verifica: copy gated per ogni stage (score corretto)?
  → verifica: brief tecnico completo per ogni landing?
  → verifica: schema micro-conversioni presente per ogni stage?
  → verifica: email gated per ogni stage che le richiede?
  → GATE-2: PASS → prosegui; FAIL → diagnosi → CONV-LEAD → rework stage specifico → re-gate

         │
         ▼
[STEP 7] Consegna al committente + handoff 06-PLATFORM
  → package: mappa funnel + copy gated per stage + sequenze email + brief tecnici landing
  → brief tecnici → 06-PLATFORM per costruzione pagine
  → state.json aggiornato in marketing/cro/funnels/{funnel_id}
  → memory_store del funnel completato
  → entry wiki/log.md
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Brief completo | Tutti i campi obbligatori presenti; ICP in namespace o T-AVATAR eseguito | CONV-LEAD | Avvio workflow |
| G2 — Copy gated | Score G1 ≥80 standard / ≥85 sales page per ogni stage | A8 + COPY-QA-LEAD (L2.1) | Consegna al committente |
| G3 — CA-QA APSOC end-to-end | Tutti i check CA-QA PASS | CA-QA | Qualsiasi output del reparto |
| G4 — Brief tecnico completo | Sezioni + performance + tracking + message-match dichiarati | CA2 | Handoff a 06-PLATFORM |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "committente": "02-INFO",
  "prodotto": "Corso Freelance Autonomo — €297",
  "obiettivo_funnel": "acquisto",
  "icp": "freelance-digitale-ita",
  "awareness_level": "problem-aware",
  "canali_traffico": ["organic-ig", "ads-meta"],
  "deadline": "2026-07-15"
}
```

**Output finale:**
```json
{
  "funnel_id": "FUNNEL-001",
  "committente": "02-INFO",
  "stage_map": "→ vedere marketing/cro/funnels/FUNNEL-001/stage-map.json",
  "copy_per_stage": {
    "ToFu": "gated, score 82",
    "MoFu": "gated, score 83",
    "BoFu": "gated, score 86"
  },
  "email_per_stage": {
    "MoFu": "nurture 5 email, gated",
    "BoFu": "lancio 7 email, gated"
  },
  "brief_tecnici": {
    "LP-MOFU-001": "approvato → 06-PLATFORM",
    "LP-BOFU-001": "approvato → 06-PLATFORM"
  },
  "micro_conversion_schema": "consegnato ad AN5",
  "ca_qa_gate": "PASS",
  "stato": "handoff_completo"
}
```

---

## State

File: `marketing/cro/funnels/{funnel_id}/state.json`
- Aggiornato ad ogni step del workflow.
- Permette la ripartibilità a freddo: un agente può riprendere dal punto di interruzione.
- Archiviato in `marketing/cro/funnels/` dopo consegna completa.

---

## Connessioni

- [[conv-lead]] · `agenti/conv-lead.md`
- [[ca1-funnel-strategist]] · `agenti/ca1-funnel-strategist.md`
- [[ca2-landing-page-strategist]] · `agenti/ca2-landing-page-strategist.md`
- [[ca-qa-conversion-verifier]] · `agenti/ca-qa-conversion-verifier.md`
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md` — ottimizzazione post-live
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §4d`
