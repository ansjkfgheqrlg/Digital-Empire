---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R6 #qa #batch #parallelo #first-pass-rate #post-produzione
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-QA-BATCH — QA Parallelo su Batch di ≥5 Pezzi

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Trigger:** batch di ≥5 deliverable pronti in `cf/qa` con stesso `order_id` o stesso `brand`
> **Invariant:** ogni pezzo riceve WF-QA-SINGOLO completo; nessuna abbreviazione per volume

---

## Scopo

Coordinare il QA in parallelo su batch di ≥5 deliverable provenienti dalla stessa commessa
o dallo stesso ciclo produttivo. L'obiettivo è mantenere la stessa qualità di WF-QA-SINGOLO
senza creare un collo di bottiglia sequenziale su grandi volumi. Output: batch-report.json
con first-pass rate, distribuzione FAIL per gate, lista pezzi PASS e lista rework.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Condizione |
|---|---|---|---|---|---|
| 0 | Identificazione batch | CF-R6-COORD | `cf/qa` con ≥5 pezzi pronti | lista batch con metadati per pezzo | n_pezzi ≥ 5; sotto 5 → WF-QA-SINGOLO |
| 1 | Fan-out parallelo | CF-R6-BATCH | lista batch + metadati per pezzo | N istanze WF-QA-SINGOLO avviate | ogni istanza indipendente |
| 2 | Esecuzione parallela | N istanze WF-QA-SINGOLO | deliverable + brand_kit + icp per ciascuno | verdict.json per ogni pezzo | gate sequenziali completi su ogni pezzo |
| 3 | Handoff progressivo PASS | CF-R6-BATCH | verdetto PASS singolo | abilitazione CF-R7 per quel pezzo | non aspetta fine batch; PASS immediato |
| 4 | Merge verdetti | CF-R6-BATCH | tutti i verdict.json del batch | batch-report.json aggregato | al termine di tutte le istanze |
| 5 | Analisi anomalia | CF-R6-BATCH | first-pass rate batch | segnalazione a CF-R6-COORD se < 50% | anomalia batch → CF-R6-LEARN |
| 6 | Gestione rework | CF-R6-REWORK (per ogni FAIL) | specifica per ogni pezzo FAIL | rework indirizzato al reparto corretto | n_rework ≥ 2 su singolo pezzo → escalation |
| 7 | Report finale | CF-R6-COORD | batch-report.json | report a CF-Director + L1-POST | fine ciclo batch |

---

## Invariant batch (non negoziabili)

1. **Nessuna abbreviazione per volume**: ogni pezzo del batch riceve WF-QA-SINGOLO completo
   con tutti e 4 i gate. Non esiste "gate spot" o "campionamento" su batch grandi.
2. **Indipendenza dei job**: il FAIL di un pezzo non ferma il QA degli altri.
   I pezzi sono isolati tra loro.
3. **Handoff progressivo**: i pezzi PASS vengono abilitati per CF-R7 non appena
   il verdetto è disponibile, senza aspettare che tutti i pezzi del batch siano conclusi.
4. **Soglia batch**: WF-QA-BATCH si attiva solo se n ≥ 5. Per n < 5: WF-QA-SINGOLO
   in sequenza gestito direttamente da CF-R6-COORD.
5. **Anomalia batch ≠ rework singolo**: se first-pass rate < 50%, il problema è sistemico
   (non 1 pezzo sbagliato); CF-R6-BATCH segnala a CF-R6-COORD e CF-R6-LEARN per analisi
   del processo produttivo, non solo per rework.

---

## Schema batch-report.json

```json
{
  "batch_id": "BATCH-CF-2026-0070",
  "ts_inizio": "2026-06-23T15:00:00Z",
  "ts_fine": "2026-06-23T15:18:00Z",
  "n_pezzi": 7,
  "n_pass": 5,
  "n_fail": 2,
  "first_pass_rate": 0.71,
  "distribuzione_fail_per_gate": {
    "gate_formato": 0,
    "gate_brand": 1,
    "gate_copy": 1,
    "mandato": 0
  },
  "pezzi_pass": [
    "CF-2026-0070-01", "CF-2026-0070-02", "CF-2026-0070-04",
    "CF-2026-0070-05", "CF-2026-0070-07"
  ],
  "pezzi_fail_rework": [
    {
      "order_id": "CF-2026-0070-03",
      "gate_fallito": "GATE-BRAND",
      "motivo": "font body non conforme: rilevato Roboto, atteso Inter (brand_kit.visual.font.body)",
      "destinatario_rework": "CF-R5 (CF-R5-CANVA)",
      "n_rework": 1
    },
    {
      "order_id": "CF-2026-0070-06",
      "gate_fallito": "GATE-COPY",
      "motivo": "CTA assente nella slide finale",
      "destinatario_rework": "CF-R4 (CF-R4-WRITE)",
      "n_rework": 1
    }
  ],
  "anomalia_batch": false,
  "segnalazione_cf_r6_learn": false
}
```

---

## Gestione anomalia batch

Se `first_pass_rate < 0.50` (meno del 50% dei pezzi supera il QA al primo giro):

1. CF-R6-BATCH segnala a CF-R6-COORD con flag `anomalia_batch: true`.
2. CF-R6-COORD notifica CF-R6-LEARN con dossier batch (quale gate ha prodotto i FAIL,
   quale brand/formato, quale reparto produttore).
3. CF-R6-COORD valuta con L1-POST se bloccare il reparto produttore per revisione
   del processo produttivo (non solo rework pezzo per pezzo).
4. CF-R6-LEARN registra l'anomalia in `cf/failures` come potenziale pattern
   (anche se < 3 occorrenze: le anomalie batch sono segnali più forti dei singoli FAIL).

---

## State machine batch

```json
{
  "batch_id": "BATCH-CF-2026-0070",
  "stato_batch": "in_corso",
  "pezzi": {
    "CF-2026-0070-01": { "stato": "PASS", "ts": "2026-06-23T15:04:00Z", "cf_r7_abilitato": true },
    "CF-2026-0070-02": { "stato": "PASS", "ts": "2026-06-23T15:06:00Z", "cf_r7_abilitato": true },
    "CF-2026-0070-03": { "stato": "in_rework", "gate_fallito": "GATE-BRAND", "n_rework": 1 },
    "CF-2026-0070-04": { "stato": "PASS", "ts": "2026-06-23T15:08:00Z", "cf_r7_abilitato": true },
    "CF-2026-0070-05": { "stato": "in_corso", "ts": null },
    "CF-2026-0070-06": { "stato": "in_rework", "gate_fallito": "GATE-COPY", "n_rework": 1 },
    "CF-2026-0070-07": { "stato": "in_corso", "ts": null }
  }
}
```

---

## Esempio operativo end-to-end

**Batch:** BATCH-CF-2026-0070 · 7 caroselli mentalita-brutale · ciclo settimanale

**Passo 0:** CF-R6-COORD identifica 7 pezzi pronti in `cf/qa` con `pronto_per_cf_r6: true`.
Attiva WF-QA-BATCH.

**Passo 1:** CF-R6-BATCH avvia 7 istanze WF-QA-SINGOLO in parallelo.

**Passo 2:** Le 7 istanze eseguono i 4 gate sequenziali ciascuna in modo indipendente.
Tempo: 18 minuti per completare tutte le istanze.

**Passo 3 (progressivo):** CF-2026-0070-01 PASS a 14:34 → CF-R7 abilitato subito.
CF-2026-0070-02 PASS a 14:36 → CF-R7 abilitato. (e così via per 01, 02, 04, 05, 07)

**Passo 4 — merge:** Tutti i verdetti raccolti.
PASS: 5 pezzi. FAIL: 2 pezzi.

**Passo 5:** First-pass rate = 71%. Anomalia batch: NO (71% > 50%).

**Passo 6:** CF-R6-REWORK gestisce i 2 pezzi FAIL con specifiche strutturate.
CF-2026-0070-03 → CF-R5 per fix font. CF-2026-0070-06 → CF-R4 per aggiungere CTA.

**Passo 7:** batch-report.json consegnato a CF-R6-COORD → L1-POST + CF-Director.

---

## Connessioni

- [[cf-r6-batch]] · `agenti/cf-r6-batch.md` — agente che orchestra il fan-out e il merge
- [[WF-QA-SINGOLO]] · `workflow/WF-QA-SINGOLO.md` — workflow istanziato N volte in parallelo
- [[cf-r6-rework]] · `agenti/cf-r6-rework.md` — gestisce ogni pezzo FAIL del batch
- [[cf-r6-learn]] · `agenti/cf-r6-learn.md` — riceve anomalie batch per analisi pattern
