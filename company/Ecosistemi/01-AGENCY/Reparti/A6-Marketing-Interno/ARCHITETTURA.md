---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #marketing-interno #proof #case-study #agency #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — A6 Marketing Interno & Proof

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.
> Reparto L2 di 01-AGENCY. Topologia `star`. Standard CF-grade (ADR-007).

---

## 1. Gerarchia interna

```
01-AGENCY (L1) — AG-CONDUCTOR
   └── A6 Marketing Interno & Proof
         │
         AG-A6-COORD (coordinator, sonnet)
         ├── AG-A6-PROOF (worker, haiku)
         │     → raccolta testimonianze/metriche reali a fine 90gg
         │     → "prove non promesse": raccolta attiva, mai presunta
         ├── AG-A6-CASE (worker, sonnet)
         │     → case study APSOC (skill case-study-forge)
         │     → solo numeri reali verificati dal cliente
         ├── AG-A6-UPSELL (worker, sonnet)
         │     → matrice cliente→offerta successiva (skill upsell-mapper)
         │     → attiva SOLO dopo Gate Delivery + NPS ≥8
         ├── AG-A6-INBOUND (worker, sonnet)
         │     → traccia lead da landing/presentazione
         │     → misura tasso conversione; suggerisce ottimizzazioni
         └── AG-A6-QA (verifier, sonnet)
               → Brand Gate: no claim senza proof
               → conformità Mandato Art.1-2 su ogni asset pubblico
```

**Principio di coordinamento:** AG-A6-COORD riceve i segnali (Gate Delivery firmato, 90gg
chiusi, gap vetrina) e orchestra task in parallelo. I task sono a bassa frequenza
(un case study per cliente chiuso, non una pipeline quotidiana). AG-A6-QA è bloccante su
ogni asset pubblico prima della pubblicazione; nessun claim esce senza proof verificata.

---

## 2. Flussi principali

### 2.1 Case study da delivery chiusa (WF-CASE-STUDY)

```
[A4-Delivery: Gate Delivery firmato + 90gg supporto chiusi]
         │
         ▼
AG-A6-COORD — riceve segnale; avvia raccolta
         │
         ▼
AG-A6-PROOF — contatta cliente (messaggio personalizzato, non automatico)
  → raccoglie metriche reali: reply rate, tempo setup, ROI misurato
  → trascrizione/screenshot testimonianza → mai inventare o parafrasare
  → se cliente non fornisce metriche → case study qualitativo (no numeri fabbricati)
         │
         ▼
AG-A6-CASE — scrive case study (skill case-study-forge, struttura APSOC)
  → APRE con problema del cliente → soluzione → risultato con numeri reali
  → ogni claim cita fonte/cliente (con consenso documentato)
         │
         ▼
AG-A6-QA — Brand Gate: solo metriche verificate, no claim inventati; brand voice conforme
  → PASS: richiesta asset a 03-CONTENT-FACTORY (HC-AG-CF-01)
  → FAIL: rework sulla sezione non conforme (mai bypass)
         │
         ▼
Pubblicazione su agency-empire-landing + wiki → munizioni per A2 e A3
```

### 2.2 Manutenzione vetrina (WF-ASSET-VETRINA)

```
AG-A6-COORD — identifica gap (caso studio mancante, social proof da aggiornare)
         │
         ▼
ticket ad AG-A6-CASE (nuovo case study) o a 06-PLATFORM (HC-AG-PL-01) per modifica landing
         │
         ▼
AG-A6-QA — Brand Gate (Sentinel Brand-Voice) su ogni modifica della landing
         │
         ▼
06-PLATFORM — deploy (mai deploy autonomo da A6)
```

### 2.3 Upsell & referral (WF-UPSELL-REFERRAL)

```
A7-Account Mgmt — segnale: 90gg finiti + NPS ≥8
         │
         ▼
AG-A6-UPSELL — mappa prodotto attuale → offerta successiva (skill upsell-mapper)
  → singolo prodotto → Engine Room €8.000 → referral
  → se no upsell: referral ask
         │
         ▼
AG-A3-COORD (Preventivi) — proposta commerciale (mai upsell automatico; via umana/Max)
```

---

## 3. Confine con altri reparti/ecosistemi

| Aspetto | A6 Marketing Interno (AGENCY) | Chi possiede l'altro lato |
|---|---|---|
| Metriche reali del cliente | Raccoglie e verifica (AG-A6-PROOF) | A4-Delivery produce i dati nella delivery |
| Asset grafici/video del case study | Brief + claim verificati | 03-CONTENT-FACTORY produce (HC-AG-CF-01) |
| Landing & presentazione (codice/deploy) | Brief gap + strategia vetrina | 06-PLATFORM implementa e deploya (HC-AG-PL-01) |
| Copy sales page maggiore | Testimonianze come input | 04-MARKETING / A5-Copywriting-Interno |
| Proposta upsell/preventivo | Mappa opportunità (segnala, non decide) | A3-Preventivi + Max (via umana) |

**Regola d'oro:** A6 produce munizioni e brief; non scrive il copy lungo (A5/04) né costruisce
o deploya pagine (06-PLATFORM). Il confine è netto: A6 possiede la PROVA, non l'implementazione.

---

## 4. Namespace memoria — `agency/a6/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a6/case-studies` | Case study per cliente chiuso: problema, soluzione, metriche verificate, stato gate | AG-A6-CASE |
| `agency/a6/proof` | Testimonianze + metriche raccolte per cliente: fonte, consenso, valore | AG-A6-PROOF |
| `agency/a6/vetrina` | Stato landing/presentazione: gap aperti, ticket 06-PLATFORM, deploy | AG-A6-COORD |
| `agency/a6/upsell` | Proposte upsell/referral: prodotto attuale, next, segnale NPS, esito | AG-A6-UPSELL |
| `agency/a6/inbound` | Lead da inbound: fonte (landing/presentazione), conversione, ottimizzazioni | AG-A6-INBOUND |

**Regola di integrità:** ogni case study in `agency/a6/case-studies` con metriche numeriche deve
avere campo `fonte` e `consenso_cliente` popolati. Un claim numerico senza fonte verificata non
può esistere in namespace (Mandato Art.2 — prove non promesse).

---

## 5. Integrazione con altri namespace e workflow

| Namespace / Sistema | Relazione |
|---|---|
| `agency/clients` | AG-A6-PROOF legge lo storico cliente prima di contattarlo per la testimonianza |
| `agency/kpi` | Metriche reali della delivery (A4) → input per case study verificato |
| A4-Delivery (Gate Delivery) | Trigger di WF-CASE-STUDY: segnale "Gate firmato" + metriche reali |
| A2-Acquisizione | Consumatore: case study come munizioni per outreach |
| 03-CONTENT-FACTORY (HC-AG-CF-01) | Produce asset grafici/video da brief A6 |
| 06-PLATFORM (HC-AG-PL-01) | Implementa e deploya modifiche landing/presentazione |

---

## 6. State e ripartibilità

Ogni esecuzione di WF-CASE-STUDY produce uno `state.json` in `agency/a6/case-studies/`
con i campi:
- `case_id` — identificativo univoco del case study
- `cliente` — tenant/cliente (con consenso alla pubblicazione)
- `proof_status` — raccolta / metriche_verificate / qualitativo / cliente_silente
- `metriche` — lista metriche reali con `fonte` e `valore`
- `brand_gate` — pending / PASS / FAIL + motivo
- `asset_status` — richiesto_CF / consegnato / pubblicato
- `last_updated` — timestamp ultimo aggiornamento

Questo permette la **ripartibilità a freddo**: un agente può rientrare nel workflow dal punto
esatto di interruzione senza riestrarre tutto il contesto (test amnesia V2).

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6`
- [[L2-6-Conversion-Architecture]] · reparto CF-grade di riferimento (04-MARKETING)
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md`
- [[WF-ASSET-VETRINA]] · `workflow/WF-ASSET-VETRINA.md`
