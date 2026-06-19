---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #marketing #analytics #ottimizzazione #tracking #ReasoningBank #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — L2.4 Analytics & Ottimizzazione

> **Standard:** CF-grade (ADR-007) · **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING

---

## 1. Gerarchia interna

```
AN-LEAD (coordinator sonnet)
 ├── AN1 — Tracking Engineer (worker sonnet)
 │    └── coordina con 06-PLATFORM per implementazione eventi
 ├── AN2 — Attribution Analyst (worker sonnet)
 │    └── legge performance per copy_id, canale, campagna
 ├── AN3 — Experiment Designer (worker sonnet)
 │    └── dimensionamento campione, verdetto statistico
 ├── AN4 — Insight Distiller (worker sonnet)
 │    └── scrive patterns in ReasoningBank (namespace memoria)
 ├── AN5 — Funnel Analyst (worker sonnet)
 │    └── drop rate per sezione APSOC → input L2.6 e A8
 └── AN-OBSERVER — Marketing Observability Lead (verifier sonnet)
      └── monitora KPI 04-MARKETING; segnala anomalie; alimenta CMO
```

AN-LEAD riceve task da MKT-Conductor, assegna agli agenti specializzati,
consolida i risultati e risponde del loop di ottimizzazione end-to-end.

---

## 2. Il loop che rende il sistema auto-migliorante (§4b dossier v2)

```
1. RACCOLTA
   AN1/AN2: performance per copy_id (CTR, reply, opt-in, vendite, per canale)
   AN5: drop rate per sezione APSOC (dove abbandona il lettore?)

2. DIAGNOSI
   AN2 + T-REVIEW: quale sezione APSOC sotto-performa?
   hook debole = A · drop a metà = P/S · click senza conversione = O/C

3. DISTILLA
   AN4 → ReasoningBank:
   - fallimento → anti-pattern → marketing/copy/antipatterns/{icp}
   - successo   → pattern vincente → marketing/copy/patterns/{icp}

4. REVISIONE
   COPY-MASTER riapre il copy SOLO sulla sezione diagnosticata
   (regola anti-deriva: no riscrittura totale di copy che performa parzialmente)

5. TEST
   WF-AB-TEST: vecchia variante vs nuova → verdetto con criterio predefinito
   (AN3 verifica dimensione PRIMA del verdetto)

6. CONSOLIDA
   winner → pattern library; wiki/log.md aggiornato; ciclo → 1
```

Questo loop è la colonna vertebrale del reparto. Tutto il lavoro degli agenti
converge qui: tracking (AN1), attribuzione (AN2), esperimento (AN3), distillazione
(AN4), analisi funnel (AN5), osservabilità (AN-OBSERVER).

---

## 3. Namespace memoria (AgentDB)

| Namespace | Contenuto | Owner scrittura | Owner lettura |
|---|---|---|---|
| `marketing/copy/patterns/{icp}` | Pattern copy vincenti per ICP (hook, angoli, CPB che hanno performato — con evidenza) | AN4 | COPY-MASTER (L2.1), A3-A7 |
| `marketing/copy/antipatterns/{icp}` | Cosa non funziona per quell'ICP (da ReasoningBank) | AN4 | COPY-MASTER, A8 |
| `marketing/copy/scores` | Storico score APSOC per copy_id (trend qualità nel tempo) | A8 / COPY-QA-LEAD (L2.1) | AN2 |
| `marketing/ads/experiments` | Matrici test, varianti, campioni, verdetti | AN3 / AD6 (L2.2) | AN-LEAD, AD-LEAD |
| `marketing/avatars/{icp}` | Avatar completi (prodotti da A2/T-AVATAR in L2.1) | A2 (L2.1) | AN4, AN5 |

**Schema minimo per pattern (`marketing/copy/patterns/{icp}`):**
```json
{
  "icp": "freelance-digitale-ita",
  "formato": "ad | sales-page | email | social",
  "sezione_apsoc": "A | P | S | O | CTA",
  "pattern": "testo del pattern rilevato",
  "evidenza": {
    "n_run": 3,
    "copy_ids": ["CP-001", "CP-002", "CP-003"],
    "metrica": "CTR medio 4.2% su 3 campagne"
  },
  "data_consolidamento": "YYYY-MM-DD"
}
```

**Regola anti-rumore (non negoziabile):** un pattern si scrive nel namespace solo se
la stessa osservazione si ripete su almeno 2 run indipendenti con la stessa ICP.
Un singolo risultato eccezionale va in state come "segnale da monitorare", non come pattern.

---

## 4. Coordinamento con 06-PLATFORM (tracking tecnico)

L2.4 possiede il **piano di tracking** (cosa misurare, come nominare gli eventi, UTM, conversion API).
06-PLATFORM possiede l'**implementazione tecnica** (pixel, tag manager, server-side events).

Flusso standard:
```
AN1 → produce tracking plan (WF-TRACKING-SETUP)
     → consegna a 06-PLATFORM come specifica tecnica
06-PLATFORM → implementa
     → AN1 verifica: ogni evento fantasma = blocco prima del lancio
```

Ogni evento nel tracking plan ha tre campi obbligatori:
- `nome` (snake_case, univoco nel progetto)
- `trigger` (quando si attiva: "click su CTA finale", "scroll >70%", ecc.)
- `valore` (cosa misura: "valore conversion, €", "categoria evento GA4", ecc.)

Se un evento non ha tutti e tre i campi → evento fantasma → blocco AN1.

---

## 5. Integrazione con la ReasoningBank (Ruflo / AgentDB)

Il reparto usa tre tool Ruflo per il loop di apprendimento:

| Tool | Quando | Chi |
|---|---|---|
| `memory_search("marketing/copy/patterns/{icp}")` | Prima di ogni nuovo copy | COPY-MASTER (L2.1) su output AN4 |
| `memory_store` (namespace patterns/antipatterns) | Dopo ogni ciclo WF-OPTIMIZATION-LOOP | AN4 |
| `neural_train` | Periodicamente (batch di pattern consolidati) | AN-LEAD (pianifica scheduling con 09-OPERATIONS) |

---

## 6. Regola anti-deriva (copia da §4b dossier v2)

**Nessuna revisione di copy basata su opinioni**: solo su dati del loop o su score A8.
"Prove non promesse" vale anche internamente (Art.2.2 Mandato).

COPY-MASTER riapre il copy **solo sulla sezione diagnosticata da AN2/AN5**.
Non si riscrive mai un copy che performa parzialmente bene su più sezioni:
si interviene chirurgicamente sulla sezione debole.

---

## 7. Confini espliciti

| L2.4 FA | L2.4 NON FA |
|---|---|
| Produce tracking plan (AN1) | Implementa il tracking su server/piattaforma (→ 06-PLATFORM) |
| Attribuisce performance per copy_id (AN2) | Scrive il copy (→ L2.1) |
| Dimensiona e disegna esperimenti (AN3) | Lancia campagne (→ L2.2 AD3) |
| Distilla pattern in ReasoningBank (AN4) | Progetta funnel (→ L2.6) |
| Analizza drop rate per sezione APSOC (AN5) | Forza verdetti senza soglia statistica |
| Monitora KPI dell'ecosistema 04-MARKETING (AN-OBSERVER) | Modifica copy senza dossier diagnostico da AN2/AN5 |

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
- [[L2-1-Copywriting]] · destinatario pattern + fornitore copy_id
- [[L2-6-Conversion-Architecture]] · CA3 → AN5 schema micro-conversioni; AN5 → CA4 drop rate
- [[06-ECOSISTEMA-PLATFORM]] · AN1 → 06-PLATFORM tracking plan; 06-PLATFORM → AN1 verifica
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md` — colonna vertebrale
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md` — passo 5 del loop
