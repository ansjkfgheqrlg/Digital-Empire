---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #conversion #funnel #cro #marketing #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — L2.6 Conversion Architecture

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.

---

## 1. Gerarchia interna

```
04-MARKETING (L1) — MKT-Conductor
   └── L2.6 Conversion Architecture
         │
         CONV-LEAD (coordinator, opus)
         ├── CA1 Funnel Strategist (worker, opus)
         │     → architettura funnel multi-step
         │     → mapping APSOC per stage (ToFu/MoFu/BoFu)
         ├── CA2 Landing Page Strategist (worker, sonnet)
         │     → struttura landing per stage
         │     → brief tecnico per 06-PLATFORM
         ├── CA3 Micro-Conversion Analyst (worker, sonnet)
         │     → mappa micro-conversioni
         │     → input per AN5 (piano di misurazione)
         ├── CA4 CRO Sprint Lead (worker, sonnet)
         │     → esecuzione sprint CRO
         │     → coordinamento WF-AB-TEST con AN3
         └── CA-QA Conversion QA Verifier (verifier, sonnet)
               → gate APSOC end-to-end su ogni funnel
               → blocca se coerenza non rispettata
```

**Principio di coordinamento:** CONV-LEAD riceve il brief del committente e assegna i task
agli agenti specializzati. CA-QA è bloccante su ogni output prima della consegna. Tutti gli
agenti lavorano sotto il coordinamento di CONV-LEAD; nessun output esce senza passare CA-QA.

---

## 2. Flussi principali (ToFu → MoFu → BoFu)

### 2.1 Funnel design completo

```
[Committente: es. 02-INFO per lancio corso]
         │
         ▼
CONV-LEAD — valida brief; assegna a CA1
         │
         ▼
CA1 Funnel Strategist
  → mappa stage: ToFu (awareness) · MoFu (consideration) · BoFu (conversion)
  → obiettivo APSOC per stage:
     ToFu  = A (Attenzione) → traffico qualificato
     MoFu  = P+S (Problema+Soluzione) → lead nurturati
     BoFu  = O+CTA (Obiezioni+Chiamata) → conversione
  → per ogni stage: URL/punto di contatto · copy richiesto · email richiesta
         │
         ▼
CA2 Landing Page Strategist (per ogni landing nel funnel)
  → struttura: hero → proof → offer → objections → CTA
  → brief tecnico per 06-PLATFORM: sezioni, micro-conversion target, requisiti tecnici
         │
         ▼
Handoff L2.1 — richiesta copy gated per stage
Handoff L2.3 — richiesta sequenze email per stage
         │
         ▼
CA3 Micro-Conversion Analyst
  → mappa: scroll depth atteso · click CTA · opt-in · micro-conversioni per stage
  → invia schema a AN5 per piano di misurazione
         │
         ▼
CA-QA — gate APSOC end-to-end:
  ogni stage ha copy gated? la progressione APSOC è coerente tra stage?
  → PASS: brief tecnico va a 06-PLATFORM; handoff completo
  → FAIL: CONV-LEAD identifica stage mancante → rifacimento stage specifico
```

### 2.2 Sprint CRO (ottimizzazione post-live)

```
AN5 (L2.4) — identifica drop rate per stage/sezione APSOC
         │
         ▼
CONV-LEAD + CA4 — analisi collo di bottiglia
  → drop in hero = A debole → richiesta A3 (Attention Writer)
  → drop a metà = P/S debole → richiesta A4/A5
  → click senza conversione = O/CTA → richiesta A6/A7
         │
         ▼
CA4 — disegna variante (NON scrive il copy: lo chiede a L2.1)
  → brief variante → WF-COPY-* (L2.1)
         │
         ▼
WF-AB-TEST (L2.4/AN3) — dimensionamento test
  → AN3 verifica: dimensione campione raggiunta? → sì: esegui test
  → verdetto con criterio predefinito
         │
         ▼
CA4 — implementazione winner (via 06-PLATFORM per pagine)
  → registra in `marketing/cro/sprints`
```

### 2.3 Audit landing esistente

```
Input: URL landing da auditare + committente
         │
         ▼
CA2 — analisi struttura APSOC (hero/proof/offer/objections/CTA presenti?)
CA3 — analisi micro-conversioni (scroll depth, CTA placement, opt-in)
AN5 (L2.4) — dati performance se disponibili
         │
         ▼
CA-QA — consolida: report diagnostico
  → 3 azioni prioritarie ordinate per impatto stimato
  → salva in `marketing/cro/audits`
```

---

## 3. Confine con 06-PLATFORM — strategia vs implementazione

| Aspetto | L2.6 Conversion Architecture (MARKETING) | 06-PLATFORM |
|---|---|---|
| Struttura della landing | Definisce: sezioni, ordine, obiettivo per sezione, CTA | Implementa: HTML/CSS/JS, CMS, deploy |
| Copy della landing | Richiede a L2.1 (non scrive mai) | Inserisce il copy approvato nel template |
| Velocità / mobile | Specifica i requisiti nel brief tecnico | Garantisce il rispetto tecnico dei requisiti |
| Tracking | CA3 definisce le micro-conversioni da tracciare | AN1 (L2.4) + 06-PLATFORM implementano gli eventi |
| A/B test | CA4 disegna le varianti; AN3 valida il disegno | 06-PLATFORM implementa il test tecnico |
| Modifiche post-audit | CA4 specifica cosa cambiare (architettura) | 06-PLATFORM esegue le modifiche |

**Regola d'oro:** il brief tecnico è il documento di confine. L2.6 lo produce e lo approva.
06-PLATFORM lo riceve e lo implementa. Nessun cambiamento strutturale alla landing avviene
senza brief tecnico approvato da CONV-LEAD.

---

## 4. Namespace memoria — `marketing/cro/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `marketing/cro/sprints` | Sprint CRO: collo di bottiglia, variante, risultato, verdetto | CA4 |
| `marketing/cro/audits` | Audit landing: diagnosi, 3 azioni prioritarie, impatto stimato | CA-QA + AN5 |
| `marketing/cro/funnels` | Architettura funnel per committente: stage map, brief tecnico, stato | CONV-LEAD |

**Regola di integrità:** ogni sprint in `marketing/cro/sprints` deve avere campo `verdetto`
popolato. Uno sprint senza verdetto statisticamente valido non è uno sprint chiuso.

---

## 5. Integrazione con altri namespace e workflow

| Namespace / Sistema | Relazione |
|---|---|
| `marketing/copy/patterns/{icp}` | CA1 legge pattern vincenti prima di disegnare il funnel stage |
| `marketing/avatars/{icp}` | CA1 + CA2 leggono avatar per calibrare la struttura per awareness level |
| `marketing/ads/experiments` | CA4 legge esiti test per evitare di ripetere varianti già testate |
| L2.4 WF-AB-TEST | CA4 invoca il workflow per il disegno statistico dell'esperimento |
| L2.1 WF-COPY-FULL / WF-COPY-SALES-PAGE | CONV-LEAD invoca per ogni stage che richiede copy lungo |
| L2.3 WF-EMAIL-LAUNCH / WF-EMAIL-NURTURE | CONV-LEAD invoca per sequenze email per stage MoFu/BoFu |

---

## 6. State e ripartibilità

Ogni esecuzione di WF-FUNNEL-DESIGN produce un `state.json` in `marketing/cro/funnels/`
con i campi:
- `funnel_id` — identificativo univoco del progetto funnel
- `committente` — ecosistema richiedente
- `stage_map` — ToFu/MoFu/BoFu con obiettivo per stage
- `copy_status` — per ogni stage: richiesto / in produzione / gated
- `brief_tecnico_status` — bozza / approvato / inviato a 06-PLATFORM
- `ca_qa_gate` — pending / PASS / FAIL + motivo
- `last_updated` — timestamp ultimo aggiornamento

Questo permette la **ripartibilità a freddo**: un agente può rientrare nel workflow
dal punto esatto di interruzione senza riestrarre tutto il contesto (test amnesia §6 V2).

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.6 e §4d`
- [[06-ECOSISTEMA-PLATFORM]] · partner di implementazione
- [[L2-4-Analytics]] · AN5 e AN3 sono i partner analitici di questo reparto
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md`
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md`
