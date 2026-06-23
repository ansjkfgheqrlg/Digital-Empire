---
Type: SCRIPTS
Status: Active
Tags: #scripts #content-factory #CF-R6 #qa #automatizzazione #format-gate #batch
Created: 2026-06-23
Last updated: 2026-06-23
---

# Scripts — CF-R6 QA & Gate

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Policy:** script deterministici, zero side effect su asset; dry-run disponibile per ogni script

---

## Obiettivo degli script

CF-R6 ha 3 script target che automatizzano le parti computazionali dei gate di qualità.
Sono deterministici: a parità di input producono sempre lo stesso output. Non modificano
asset; producono solo report JSON e aggiornano state.json. Il GATE-FORMATO è automatizzabile
al 100% tramite questi script.

---

## Script 1: format-gate-runner

**Scopo:** Eseguire GATE-FORMATO automaticamente su un singolo deliverable o su una lista.

**Trigger:** chiamato da CF-R6-FORMAT durante WF-QA-SINGOLO.

**Cosa fa:**
- Legge metadati del file (dimensioni, peso, codec via analisi tecnica del file).
- Per video: verifica loudness LUFS, durata, aspect ratio.
- Per immagini: verifica dimensioni in pixel, peso in MB per file.
- Verifica struttura (n. slide per carosello, presenza heading per testo strutturato).
- Produce `gate_formato_result.json` con esito PASS/FAIL per ogni criterio verificato.

**Input:**
```json
{
  "deliverable_path": "orders/CF-2026-0061/04-render/PNG/carosello-001/",
  "formato": "carosello-ig",
  "specifiche": { "dimensioni": "1080x1350", "n_slide_max": 8, "peso_max_mb": 8 }
}
```

**Output:**
```json
{
  "formato": "carosello-ig",
  "esito": "PASS",
  "dettaglio": {
    "dimensioni_conformi": true,
    "n_slide": 8,
    "peso_max_mb": 6.2,
    "codec": "N/A",
    "loudness": "N/A"
  }
}
```

**Dry-run:** con flag `--dry-run` elenca i file che verrebbero analizzati senza eseguire
l'analisi; utile per verificare il path prima dell'esecuzione.

---

## Script 2: brand-sampler

**Scopo:** Campionare palette colori e font da un deliverable visual e confrontarli
con il brand_kit. Supporta CF-R6-BRAND nel GATE-BRAND.

**Trigger:** chiamato da CF-R6-BRAND durante WF-QA-SINGOLO dopo FORMAT PASS.

**Cosa fa:**
- Per PNG/immagini: campiona 5 punti dal deliverable; estrae colori HEX dominanti.
- Confronta i colori campionati vs `brand_kit.visual.palette` con tolleranza ±5% su HEX.
- Identifica i font riconoscibili nelle headline e nel body (dove possibile via analisi
  metadati del file o campionamento visivo).
- Produce `brand_sample_result.json` con lista colori campionati, confronto vs brand_kit,
  font identificati.

**Input:**
```json
{
  "deliverable_path": "orders/CF-2026-0061/04-render/PNG/carosello-001/slide-001.png",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json"
}
```

**Output:**
```json
{
  "brand": "mentalita-brutale",
  "colori_campionati": ["#1a1a1a", "#ff4444", "#ffffff"],
  "palette_brand_kit": { "primary": "#1a1a1a", "accent": "#ff4444", "bg": "#0d0d0d" },
  "conformita_palette": "CONFORME — primary e accent riconoscibili",
  "font_identificati": ["Anton (headline)", "Inter (body)"],
  "conformita_font": "CONFORME"
}
```

**Dry-run:** con flag `--dry-run` mostra i 5 punti di campionamento senza confronto
con brand_kit; utile per verificare la rappresentatività del campionamento.

---

## Script 3: batch-qa-aggregator

**Scopo:** Aggregare tutti i verdict.json di un batch in un report batch compatto.
Calcola first-pass rate, distribuzione FAIL per gate, lista rework necessari.

**Trigger:** chiamato da CF-R6-BATCH al termine di tutte le istanze WF-QA-SINGOLO di un batch.

**Cosa fa:**
- Legge tutti i `orders/<id>/05-qa/verdict.json` del batch forniti in input.
- Aggrega: conteggio PASS/FAIL, distribuzione per gate, lista pezzi in rework con motivo.
- Calcola first-pass rate = n_PASS / n_totale.
- Segnala anomalia se first-pass rate < 50%.
- Produce `batch-report.json` nella directory del batch.

**Input:**
```json
{
  "batch_id": "BATCH-CF-2026-0070",
  "verdict_paths": [
    "orders/CF-2026-0070-01/05-qa/verdict.json",
    "orders/CF-2026-0070-02/05-qa/verdict.json"
  ]
}
```

**Output:** `batch-report.json` (schema completo in `workflow/WF-QA-BATCH.md §Schema batch-report.json`)

**Dry-run:** con flag `--dry-run` verifica che tutti i path verdict.json esistano e siano
leggibili senza aggregare i dati; utile per verificare la completezza del batch prima
dell'aggregazione.

---

## Regole script (non negoziabili)

1. Ogni script produce sempre output JSON strutturato in `gate_*_result.json` o `batch-report.json`.
2. Nessuno script modifica un asset; producono solo file di report.
3. Dry-run disponibile per ogni script prima dell'esecuzione reale.
4. In caso di file non leggibile: output con `"esito": "ERRORE"` e motivo; mai eccezione non gestita.

---

## Connessioni

- [[cf-r6-format]] · `agenti/cf-r6-format.md` — usa format-gate-runner
- [[cf-r6-brand]] · `agenti/cf-r6-brand.md` — usa brand-sampler
- [[cf-r6-batch]] · `agenti/cf-r6-batch.md` — usa batch-qa-aggregator
