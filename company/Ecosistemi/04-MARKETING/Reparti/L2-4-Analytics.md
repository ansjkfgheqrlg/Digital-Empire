> Fonte: PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md sez. 2 (L2.4 — ANALYTICS & OTTIMIZZAZIONE)

# L2.4 — ANALYTICS & OTTIMIZZAZIONE

> Reparto L2 · Ecosistema: 04-MARKETING
> Ecosistema: `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/04-MARKETING/BACKBONE.md`

---

## Missione

Misurare l'effetto di ogni copy/campagna e chiudere il cerchio: **i dati diventano pattern (reasoningbank) e i pattern diventano revisioni di copy**. È il reparto che rende il sistema auto-migliorante (pattern #5 del Piano Maestro).

Regola anti-deriva: **nessuna revisione di copy basata su opinioni** — solo su dati del loop o su score A8. "Prove non promesse" vale anche internamente.

---

## Struttura interna

| Livello | ID | Contenuto |
|---|---|---|
| Workflow L3 | WF-TRACKING-SETUP | Tracking plan, UTM, eventi, conversion API (skill analytics) |
| Workflow L3 | WF-OPTIMIZATION-LOOP | Loop data-driven: performance → diagnosi → reasoningbank → revisione |
| Workflow L3 | WF-AB-TEST | Disegno ed esecuzione esperimenti (skill ab-testing) |
| Funzione L4 | T-ATTRIBUTION | Attribuzione per canale/campagna/copy |
| Funzione L4 | T-REPORT | Report periodici per committente (skill market-report / market-report-pdf) |
| Funzione L4 | T-INSIGHT-DISTILLER | Distilla i risultati in pattern per ICP → namespace memoria + wiki |

---

## Agenti L5

| Codice | Agente | Ruolo | Stato |
|---|---|---|---|
| AN1 | Tracking Engineer | Tracking plan, UTM, eventi (con 06-PLATFORM) | NUOVO |
| AN2 | Attribution Analyst | Attribuzione e lettura performance per copy/canale | NUOVO |
| AN3 | Experiment Designer | Ipotesi, varianti, dimensionamento test | NUOVO |
| AN4 | Insight Distiller | Performance → pattern reasoningbank + wiki | NUOVO |

---

## Loop ottimizzazione data-driven (§4d — il cerchio che si chiude)

```
1. RACCOLTA    AN1/AN2: performance per copy_id (CTR, reply, opt-in, vendite, per canale)
2. DIAGNOSI    AN2 + T-REVIEW: sezione APSOC sotto-performa?
               (hook debole = A, drop a metà = P/S, click senza conv. = O/C)
3. DISTILLA    AN4 → reasoningbank-*:
               - fallimento → anti-pattern ("ICP dentisti: hook su fatturato = ignorato")
               - successo  → pattern vincente → memory_store in marketing/copy/patterns/{icp}
4. REVISIONE   copy-master riapre il copy SOLO sulla sezione diagnosticata
               (mai riscrittura totale di un copy che performa parzialmente)
5. TEST        WF-AB-TEST: vecchia vs nuova variante → verdetto con criterio predefinito
6. CONSOLIDA   winner → pattern library; wiki/log.md aggiornato; neural_train periodico
   └──────────────────────► torna a 1 (loop continuo)
```

**Regola AN3:** sotto soglia minima di dati il verdetto è "inconclusivo", mai forzato. I pattern si consolidano solo con evidenza ripetuta.

---

## Namespace memoria (AgentDB/HNSW — convenzione `marketing/...`)

| Namespace | Contenuto |
|---|---|
| `marketing/copy/patterns/{icp}` | Pattern copy vincenti per ICP (hook, angoli, CPB che hanno performato) |
| `marketing/copy/antipatterns/{icp}` | Cosa NON funziona per quell'ICP (da reasoningbank) |
| `marketing/copy/scores` | Storico score A8 per copy_id (trend qualità) |
| `marketing/ads/experiments` | Matrici test, varianti, verdetti |
| `marketing/handoffs/log` | Registro richieste/risposte cross-ecosistema |

---

## KPI principali

| KPI | Definizione |
|---|---|
| Esperimenti chiusi con verdetto / mese | Velocità di apprendimento del loop §4d |
| Pattern ICP consolidati | Conteggio record validati in `marketing/copy/patterns/*` |
| Costo per run | Cost-attribution per agente (Cost-Sentinel) |

**Nota baseline:** nessuna baseline storica esiste alla fase M1. Si stabilisce in M1-M2. Nessun numero inventato.

---

## Connessioni

- `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md` — ecosistema padre
- `company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting.md` — destinatario pattern vincenti
- `company/Backbone/Observability/README.md` — infrastruttura KPI dashboard
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-AN4-insight-distiller.md`
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` §2 (L2.4), §4d, §7 (namespace Ruflo)

*Fonte: dossier 04 §2 (L2.4), §4d, §7 · Aggiornato: 2026-06-12*
