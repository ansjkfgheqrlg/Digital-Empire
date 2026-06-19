---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R3 #batch #swarm #mesh #budget #parallel #video
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-BATCH-VIDEO — Produzione Batch ≥5 Video (Swarm Mesh)

> **Reparto:** CF-R3 Produzione Video · **Area:** Produzione
> **Dry-run obbligatorio Art.4.3:** CF-SENT-COST approva il TOTALE batch PRIMA di avviare qualsiasi render
> **Regola fallimenti:** 1 video fallito non ferma il batch; 3 video falliti → escalation immediata CF-R3-COORD

---

## Scopo

Produrre ≥5 video in parallelo con swarm mesh, contenendo i costi dentro il budget approvato
per il batch intero. La stima totale pre-render è obbligatoria e viene approvata da CF-SENT-COST
come singola decisione per l'intero batch. Il batch può contenere video UGC, avatar o shortform
nella stessa esecuzione.

---

## Prerequisiti

- `qty ≥ 5` nell'ordine (o mix di ordini aggregati da CF-D-SCHED)
- Brief.json per ogni video del batch già prodotto da CF-R1
- Soul-id per i brand presenti nel batch già verificati da CF-R3-SOUL
- Budget totale batch dichiarato e sufficiente per la stima aggregata

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN batch | CF-R3-QUEUE | N ordini video | `batch-intent.json` (stima totale) | CF-SENT-COST: APPROVATO TOTALE o BLOCCO |
| 1 | Fan-out | CF-R3-COORD | N brief.json | N job indipendenti assegnati | N ≤ cap paralleli da `budget.tier_max` |
| 2 | Worker paralleli | N × CF-R3-IMG + CF-R3-MOTION (UGC) o CF-R3-AVATAR | N brief + soul_id | N × clip/avatar-raw in parallelo | render completato per job |
| 3 | Post-produzione parallela | N × CF-R3-VO + CF-R3-EDIT | N × voiceover + clips | N × video montati | loudness/aspect per ogni video |
| 4 | QA parallelo | N × CF-R3-QA | N × video + brand_kit | N × verdict.json | GATE-FORMATO + GATE-BRAND per ogni video |
| 5 | Merge risultati | CF-R3-COORD | N verdict.json | `batch-report.json` | n_pass + n_fail + crediti_totali |
| 6 | Handoff CF-R6 | CF-R3-COORD | video con verdict PASS | `pronto_per_cf_r6: true` per ogni video PASS | stato aggiornato per ogni video |

---

## Dry-run batch (passo 0 — obbligatorio Art.4.3)

CF-R3-QUEUE aggrega la stima di tutti i job del batch in un singolo `batch-intent.json`:

```json
{
  "order_id": "CF-2026-BATCH-01",
  "tipo_workflow": "WF-BATCH-VIDEO",
  "dry_run": true,
  "n_video": 6,
  "composizione_batch": [
    { "job_id": "job-01", "tipo": "video-ugc", "brand": "mentalita-brutale", "crediti_stimati": 120 },
    { "job_id": "job-02", "tipo": "video-ugc", "brand": "mentalita-brutale", "crediti_stimati": 120 },
    { "job_id": "job-03", "tipo": "video-avatar", "brand": "brand-agency", "crediti_stimati": 50 },
    { "job_id": "job-04", "tipo": "video-avatar", "brand": "brand-agency", "crediti_stimati": 50 },
    { "job_id": "job-05", "tipo": "shortform",   "brand": "mentalita-brutale", "crediti_stimati": 0 },
    { "job_id": "job-06", "tipo": "shortform",   "brand": "brand-agency", "crediti_stimati": 0 }
  ],
  "totale_crediti_stimati": 340,
  "budget_disponibile": 500,
  "cap_paralleli": 3,
  "decisione": "PENDING_APPROVAZIONE_CF-SENT-COST"
}
```

CF-SENT-COST approva (o blocca) l'intero batch in una sola risposta. Non si possono
avviare render parziali senza approvazione del totale.

---

## Regola failover batch

| Scenario | Comportamento |
|---|---|
| 1 job fallisce (render error engine) | Continua il batch; job-fallito → `cf/failures` + rework schedulato post-batch |
| 2 job falliscono | Continua il batch; flag `attenzione_fallimenti` in batch-report.json |
| 3 job falliscono | ESCALATION immediata CF-R3-COORD; non aspettare fine batch; decide se continuare o bloccare |
| 1 job supera il cap crediti individuale | Blocca solo quel job; continua gli altri |
| CF-SENT-COST blocca il totale batch | Nessun render parte; escalation CF-R3-COORD + CF-Director per revisione budget |

---

## Cap paralleli (da `budget.tier_max`)

| Tier max ordine | Cap job paralleli |
|---|---|
| haiku | 5 |
| sonnet | 3 |
| opus | 2 (alta qualità, meno volume) |

Il cap evita saturazione dell'account API e costi non previsti per burst di chiamate simultanee.

---

## Batch report (output passo 5)

```json
{
  "batch_id": "CF-2026-BATCH-01",
  "n_video_richiesti": 6,
  "n_video_completati": 5,
  "n_video_falliti": 1,
  "fallimenti": [
    { "job_id": "job-03", "motivo": "HeyGen API timeout dopo 2 tentativi", "stato": "schedulato_rework" }
  ],
  "crediti_stimati_totale": 340,
  "crediti_consumati_totale": 318,
  "video_pronti_cf_r6": ["job-01","job-02","job-04","job-05","job-06"],
  "first_pass_rate_gate_interno": 0.80,
  "note": "job-03 HeyGen in rework; resto batch consegnato a CF-R6"
}
```

---

## State machine (state.json batch)

```json
{
  "batch_id": "CF-2026-BATCH-01",
  "workflow": "WF-BATCH-VIDEO",
  "stato_batch": "completato_con_fallimenti",
  "fasi": {
    "00-dry-run":   { "stato": "completato", "risultato": "APPROVATO 340/500 crediti" },
    "01-fan-out":   { "stato": "completato", "n_job": 6, "cap_paralleli": 3 },
    "02-render":    { "stato": "completato", "n_completati": 5, "n_falliti": 1 },
    "03-post":      { "stato": "completato", "n_montati": 5 },
    "04-qa":        { "stato": "completato", "n_pass": 4, "n_fail": 1 },
    "05-merge":     { "stato": "completato", "batch_report_path": "orders/batch-01/batch-report.json" },
    "06-handoff":   { "stato": "completato", "n_consegnati_cf_r6": 4 }
  },
  "escalation_attiva": false
}
```

---

## Esempio operativo

**Batch:** 6 video (2 UGC mentalita-brutale + 2 avatar brand-agency + 2 shortform) · budget: 500 crediti

**Passo 0:** batch-intent.json → totale stimato 340/500. CF-SENT-COST: APPROVATO.

**Passo 1:** CF-R3-COORD fan-out 6 job. Cap paralleli: 3 (tier_max sonnet).
Primo slot: job-01 (UGC Higgsfield) + job-03 (avatar HeyGen) + job-05 (shortform ffmpeg).

**Passo 2-3:** Job-01 e job-02 (UGC): CF-R3-IMG + CF-R3-MOTION → CF-R3-EDIT. ✓ Completati.
Job-03 (avatar): CF-R3-AVATAR → HeyGen timeout dopo 2 tentativi → FAIL. Logato `cf/failures`.
Job-04 (avatar): stesso brand e avatar → fallisce (stesso timeout HeyGen). n_falliti = 2.
Job-05 e job-06 (shortform): CF-R3-EDIT ffmpeg → 0 crediti → completati.

n_falliti = 2 (sotto soglia escalation 3). Batch continua.

**Passo 4:** QA interno su 4 video completati: 4 PASS (job-01, 02, 05, 06).

**Passo 5:** batch-report.json → 4 video pronti CF-R6; 2 (job-03, 04) in rework schedulato.

**Passo 6:** CF-R3-COORD passa 4 video a CF-R6. Crediti consumati: 240/340 stimati (HeyGen non consumato).

---

## Connessioni

- [[cf-r3-coord]] · `agenti/cf-r3-coord.md` — orchestra fan-out e merge
- [[cf-r3-queue]] · `agenti/cf-r3-queue.md` — dry-run batch e approvazione CF-SENT-COST
- [[WF-VIDEO-UGC]] · `workflow/WF-VIDEO-UGC.md` — pipeline UGC per ogni job UGC nel batch
- [[WF-VIDEO-AVATAR]] · `workflow/WF-VIDEO-AVATAR.md` — pipeline avatar per ogni job avatar nel batch
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 CF-R3 WF-BATCH-VIDEO + §4 topologia swarm R3
