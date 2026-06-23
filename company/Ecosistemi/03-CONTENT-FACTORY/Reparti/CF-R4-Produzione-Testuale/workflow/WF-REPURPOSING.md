---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R4 #repurposing #batch #derivati #content-forge #pipeline
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-REPURPOSING — Pipeline Repurposing da Pezzo Madre a N Derivati

> **Reparto:** CF-R4 Produzione Testuale · **Area:** Produzione
> **[TARGET-V2] — skill `content-forge` come motore di derivazione**
> **Invariant:** ogni derivato riceve gate COPY + BRAND indipendente; nessuna abbreviazione per batch

---

## Scopo

Trasformare un pezzo madre (articolo, video trascritto, podcast, pillar page) in N formati
secondari: caption social, thread, email-teaser, slide copy, articolo derivato sintetico.
L'obiettivo è moltiplicare il ROI di ogni pezzo madre riducendo il costo marginale per
contenuto secondario. Ogni derivato è trattato come ordine indipendente: ha il proprio
gate e il proprio record in state.json.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Analisi pezzo madre | CF-R4-REPURP | `asset_madre` (testo/trascrizione) + `brief.json` (formati richiesti) | `02-copy/repurp-map.json` (N derivati, formato, canale, estimate token) | mappa completa prima di avviare derivazioni |
| 1 | Derivazione parallela | CF-R4-REPURP (skill content-forge) | `repurp-map.json` + `brand_kit` | N file `02-copy/derivato-<formato>-<N>.md` | auto-verifica formato per ogni derivato |
| 2 | Caption / hashtag (se social) | CF-R4-CAPTION | derivato social draft + `brand_kit.voice` + canale | `02-copy/derivato-<N>-caption.json` | lunghezza canale rispettata; hashtag ≤30 per IG |
| 3 | GATE-COPY per ogni derivato | CF-R4-QA | ogni `derivato-<N>.md` + brief_derivato + `brand_kit.voice` | `05-qa/gate-copy-derivato-<N>.json` | gate completo indipendente per ogni derivato |
| 4 | GATE-BRAND per ogni derivato | CF-R4-QA | ogni `derivato-<N>.md` + `brand_kit.voice` | `05-qa/gate-brand-derivato-<N>.json` | tone campionato per ogni derivato indipendentemente |
| 5 | Report batch | CF-R4-COORD | tutti i gate completati | `05-qa/repurp-report.json` (N ok / N rework / derivati per pezzo madre) | nessun derivato con FAIL consegnato senza rework completato |
| 6 | Output finale | CF-R4-COORD | derivati con gate PASS | manifest + `02-copy/derivati-final/` | state.json aggiornato per ogni derivato |

---

## Mappa derivati standard

Per ogni pezzo madre, i formati secondari disponibili:

| Formato derivato | Agente | Input richiesto | Canale tipico |
|---|---|---|---|
| Caption IG (breve) | CF-R4-CAPTION | estratto chiave + brand_kit | Instagram |
| Caption LinkedIn (lunga) | CF-R4-CAPTION | estratto + angle B2B | LinkedIn |
| Caption TikTok (hook-only) | CF-R4-CAPTION | hook del pezzo madre | TikTok |
| Thread X / LinkedIn (5-7 punti) | CF-R4-WRITE | struttura del pezzo madre | X / LinkedIn |
| Email teaser (corpo-only, senza APSOC) | CF-R4-WRITE | sintesi 200-300 parole | newsletter |
| Slide copy (3-7 punti, carosello seed) | CF-R4-WRITE | punti chiave estratti | IG carosello (seed per CF-R5) |
| Articolo derivato sintetico (400-600p) | CF-R4-WRITE | riassunto strutturato | blog secondario |
| Script reel 30s | CF-R4-WRITE | hook + punto principale | WF-SCRIPT → CF-R3 |

Il brief.json dell'ordine specifica quali formati derivare. Non tutti i formati sono
richiesti per ogni pezzo madre.

---

## Gate di uscita per ogni derivato (invariant non bypassabile)

Ogni derivato riceve il gate completo in modo indipendente. La logica di batch non
abbrevia i gate: un derivato non può "ereditare" il gate del pezzo madre.

**GATE-COPY per ogni derivato (CF-R4-QA):**
- Hook presente (adattato al formato: prime 2 righe per caption, primo bullet per thread, [HOOK] per script)
- Formato rispettato: lunghezza canale, struttura dichiarata, marcatori presenti
- Zero claim non verificabili nel derivato (anche se presenti con fonte nel pezzo madre)
- Zero parole_vietate dal brand_kit.voice
- Un segnaposto non sostituito nel testo = FAIL su quel campo

**GATE-BRAND per ogni derivato (CF-R4-QA):**
- Tone campionato vs brand_kit.voice.esempi (≥3 campioni per derivati brevi, ≥5 per testi >200p)
- Coerenza tono derivato con tono pezzo madre per lo stesso brand

---

## Regola batch: 1 fallito non ferma il batch; 3 falliti fermano il batch

In analogia con WF-BATCH-VIDEO di CF-R3:
- 1-2 derivati con FAIL ricevono rework; gli altri proseguono verso la consegna.
- 3 derivati con FAIL → segnale sistemico (brief inadeguato? pezzo madre non derivabile?
  brand_kit non allineato?) → CF-R4-COORD segnala a L1-PROD; il batch si sospende fino
  alla diagnosi.

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0104",
  "workflow": "WF-REPURPOSING",
  "brand": "brand-agency",
  "asset_madre": "orders/CF-2026-0101/02-copy/articolo-final.md",
  "avviato_il": "2026-06-23T12:00:00Z",
  "derivati": {
    "derivato-01-caption-ig": {
      "formato": "caption-ig",
      "stato": "completato",
      "gate_copy": "PASS",
      "gate_brand": "PASS",
      "path": "02-copy/derivati-final/derivato-01-caption-ig.md"
    },
    "derivato-02-caption-linkedin": {
      "formato": "caption-linkedin",
      "stato": "completato",
      "gate_copy": "PASS",
      "gate_brand": "PASS",
      "path": "02-copy/derivati-final/derivato-02-caption-linkedin.md"
    },
    "derivato-03-thread": {
      "formato": "thread-5p",
      "stato": "in_rework",
      "gate_copy": "FAIL",
      "gate_copy_motivo": "hook assente: primo bullet è contesto storico, non hook; n_rework: 1",
      "gate_brand": null,
      "path": null
    },
    "derivato-04-email-teaser": {
      "formato": "email-teaser",
      "stato": "completato",
      "gate_copy": "PASS",
      "gate_brand": "PASS",
      "path": "02-copy/derivati-final/derivato-04-email-teaser.md"
    }
  },
  "batch_summary": {
    "n_derivati_richiesti": 4,
    "n_pass": 3,
    "n_in_rework": 1,
    "n_fail_bloccante": 0
  },
  "stato_finale": "in_completamento"
}
```

---

## Report batch finale (repurp-report.json)

```json
{
  "order_id": "CF-2026-0104",
  "brand": "brand-agency",
  "asset_madre": "articolo-final.md (CF-2026-0101)",
  "n_derivati_richiesti": 4,
  "n_derivati_consegnati": 3,
  "n_in_rework": 1,
  "first_pass_rate_batch": 0.75,
  "derivati_per_pezzo_madre": 4,
  "rework_dettaglio": [
    { "derivato": "derivato-03-thread", "gate_fail": "GATE-COPY", "motivo": "hook assente", "n_rework": 1, "stato": "in_rework" }
  ],
  "costo_stimato_token": "[DM]",
  "lead_time_min": 38
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0104 · brand: brand-agency · pezzo madre: articolo "Il Gap che Svuota il Budget"
· formati richiesti: caption IG, caption LinkedIn, thread 5 punti, email teaser

**Passo 0 (mappa):** CF-R4-REPURP analizza il pezzo madre → mappa 4 derivati con stima token per ognuno.

**Passo 1 (derivazione parallela):** CF-R4-REPURP avvia 4 derivazioni via skill content-forge:
- caption-ig: "La motivazione non converte. L'architettura sì." + hook narrativo 80 parole.
- caption-linkedin: variante B2B 200 parole con angle "budget marketing sprecato".
- thread: 5 punti estratti dalle sezioni H2 con hook nel primo tweet.
- email-teaser: 280 parole del corpo senza blocco CTA (quello è MARKETING).

**Passo 2 (caption):** CF-R4-CAPTION aggiunge hashtag a caption-ig (12 hashtag) e caption-linkedin (6 hashtag).

**Passo 3 (GATE-COPY per ognuno):**
- caption-ig: PASS (hook presente, lunghezza ≤2200 char IG)
- caption-linkedin: PASS
- thread: FAIL (primo bullet è contesto storico "Nel 2024 le aziende hanno speso..." → hook mancante)
- email-teaser: PASS

**Passo 4 (GATE-BRAND):** 3 derivati PASS. Thread: gate sospeso fino a rework GATE-COPY.

**Passo 5 (report):** 3/4 PASS al primo giro. Thread in rework. Batch non sospeso (1 FAIL < 3).

**Passo 6 (output):** 3 derivati consegnati. Thread in rework; riassegnato a CF-R4-WRITE per correzione hook.

---

## Connessioni

- [[cf-r4-coord]] · `agenti/cf-r4-coord.md` — orchestra il batch e gestisce le sospensioni
- [[cf-r4-repurp]] · `agenti/cf-r4-repurp.md` — derivazione con skill content-forge
- [[cf-r4-caption]] · `agenti/cf-r4-caption.md` — caption e hashtag per derivati social
- [[cf-r4-write]] · `agenti/cf-r4-write.md` — derivati testuali (thread, email teaser, slide copy)
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — gate indipendente per ogni derivato
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 WF-REPURPOSING e §8 KPI "derivati per pezzo madre"
