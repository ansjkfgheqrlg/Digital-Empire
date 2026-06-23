---
Type: KPI
Status: Active
Tags: #kpi #content-factory #CF-R6 #qa #gate #first-pass-rate #post-produzione
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — CF-R6 QA & Gate

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Owner:** CF-R6-COORD · **Reporting:** L1-POST + CF-Director (report mensile)
> **[DM]** = Da Misurare: baseline non ancora disponibile; rilevare le prime 4 settimane.

---

## KPI primari (da monitorare ogni ciclo)

| KPI | Definizione | Owner | Come si misura | Baseline |
|---|---|---|---|---|
| **First-pass rate per formato** | % deliverable che superano tutti e 4 i gate al primo giro, per formato (carosello-ig, video-reel, thumbnail, testo) | CF-R6-COORD | n. PASS al primo giro / n. totale QA nel periodo, per ogni formato | [DM] |
| **GATE-FORMATO pass rate** | % pezzi con GATE-FORMATO PASS al primo giro | CF-R6-FORMAT | n. FORMAT PASS / n. totale nel periodo | [DM] |
| **GATE-BRAND pass rate** | % pezzi con GATE-BRAND PASS al primo giro (su pezzi che hanno già superato FORMAT) | CF-R6-BRAND | n. BRAND PASS / n. che hanno superato FORMAT nel periodo | [DM] |
| **GATE-COPY pass rate** | % pezzi con GATE-COPY PASS al primo giro (su pezzi che hanno già superato BRAND) | CF-R6-COPY | n. COPY PASS / n. che hanno superato BRAND nel periodo | [DM] |
| **N. rework per ciclo** | Numero totale di cicli rework aperti nel periodo (ogni FAIL che genera specifica rework) | CF-R6-REWORK | conta `rework_aperto` in trace.jsonl per periodo | [DM] |
| **Latenza QA per pezzo** | Tempo medio dal prelievo del deliverable da `cf/qa` all'emissione del verdetto | CF-R6-COORD | media (ts_verdetto - ts_prelievo) per tutti i deliverable del periodo | [DM] |

---

## KPI secondari (monitorare per trend mensile)

| KPI | Definizione | Owner | Come si misura | Note |
|---|---|---|---|---|
| **N. escalation (n_rework ≥ 2)** | Pezzi che non superano il QA nemmeno dopo il primo rework | CF-R6-COORD | conta escalation L1-POST nel periodo; segnale di problema produttivo | Monitorare ↓ |
| **First-pass rate batch** | First-pass rate calcolato per batch ≥5, separato dal singolo | CF-R6-BATCH | n. PASS batch / n. totale batch nel periodo | [DM] |
| **Anomalie batch (first-pass rate < 50%)** | Batch con più di metà dei pezzi che falliscono il QA | CF-R6-BATCH | n. batch con anomalia / n. totale batch nel periodo | Deve tendere a 0 |
| **Pattern confermati per mese** | Pattern di FAIL con n ≥ 3 occorrenze identificati nel periodo | CF-R6-LEARN | da report mensile WF-QUALITY-AUDIT | [DM] |
| **Pattern risolti per trimestre** | Pattern in `cf/failures` che non si ripresentano da ≥3 mesi | CF-R6-LEARN | da revisione `cf/failures` trimestrale | [DM] |

---

## Come leggere i KPI (guida interpretazione)

**First-pass rate per formato:**
- Prima delle prime 4 settimane: rilevare la baseline senza giudizio.
- Dopo baseline: un calo del first-pass rate su un formato specifico è il primo segnale
  di un problema nel reparto produttore corrispondente (non in CF-R6).
- Gate con pass rate basso = gate che identifica più problemi; è un segnale di valore,
  non di errore del gate.

**GATE-FORMATO vs GATE-BRAND vs GATE-COPY:**
- I 3 pass rate separati permettono di identificare quale dimensione della qualità è più
  carente nel processo produttivo: tecnica (FORMAT), identità (BRAND), o struttura persuasiva (COPY).
- Un FORMAT pass rate basso indica problemi nel processo di render/esport (CF-R5-RENDER, CF-R3-EDIT).
- Un BRAND pass rate basso indica drift dal brand_kit (CF-R2 deve aggiornare o CF-R5 deve
  controllare di più).
- Un COPY pass rate basso indica problemi nel brief (CF-R1) o nel processo di scrittura (CF-R4).

**N. rework per ciclo:**
- Un rework non è un fallimento del reparto QA: è il sistema che funziona (intercetta
  prima della pubblicazione). Un numero alto è però un segnale di costo operativo elevato.
- Se n_rework cresce mese su mese → CF-R6-LEARN verifica se è un pattern confermato.

**Latenza QA per pezzo:**
- Dipende dal volume e dal tipo di formato (i video richiedono analisi tecnica più lunga).
- Obiettivo: latenza che non crea collo di bottiglia nella pipeline CF-DE.
- Se la latenza cresce → valutare se il fan-out batch è appropriato o se servono più
  istanze CF-R6 (richiesta a 07-FORGE).

---

## Reporting

| Cadenza | Report | Destinatario | Formato |
|---|---|---|---|
| Ogni ciclo | KPI primari per ciclo | L1-POST | entry in `cf/qa` con flag "kpi_ciclo" |
| Mensile | Audit completo WF-QUALITY-AUDIT | CF-Director + 07-FORGE | `cf/failures/audits/audit-YYYY-MM.json` |
| Trimestrale | Pattern risolti + trend KPI | CF-Director | sezione del report mensile di fine trimestre |

---

## Connessioni

- [[cf-r6-coord]] · `agenti/cf-r6-coord.md` — produce e consolida i KPI ogni ciclo
- [[WF-QUALITY-AUDIT]] · `workflow/WF-QUALITY-AUDIT.md` — workflow che usa i KPI per il report mensile
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §CF-R6 KPI — definizione originale nel dossier
