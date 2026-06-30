---
Type: SCRIPTS
Status: Active
Tags: #scripts #content-factory #CF-R8 #apprendimento #pattern-validator #engine-comparator #neural-feeder
Created: 2026-06-30
Last updated: 2026-06-30
---

# Scripts — CF-R8 Apprendimento & Ottimizzazione

> **Reparto:** CF-R8 Apprendimento & Ottimizzazione · **Area:** Post-Produzione
> **Policy:** script deterministici, sola lettura su dati di produzione; dry-run disponibile per ogni script;
> nessuno script modifica asset di produzione o scrive in namespace di altri reparti.

---

## Obiettivo degli script

CF-R8 ha 3 script target che automatizzano le parti computazionalmente intensive dei workflow
di distillazione. Sono deterministici: a parità di input producono sempre lo stesso output.
Tutti operano in sola lettura sulle sorgenti dati (cf/patterns, cf/failures, cf/qa);
solo `neural-feeder` scrive, e scrive esclusivamente in `cf/patterns` per aggiornare i flag
di training.

---

## Script 1: pattern-validator

**Scopo:** Validare automaticamente un batch di pattern candidati contro i criteri Gate-N3,
Gate-FONTE, Gate-CORRELAZIONE e Gate-UNICITA di CF-R8-QA. Automatizza la parte meccanica
della validazione (conteggio, verifica campo, deduplicazione); la valutazione di
Gate-CORRELAZIONE richiede revisione da CF-R8-QA per le formulazioni ambigue.

**Trigger:** chiamato da CF-R8-QA durante WF-PATTERN-DISTILLATION (passo 2).

**Cosa fa:**
- Legge un array di pattern candidati in formato JSON.
- Per Gate-N3: conta `len(pattern.esempi)` per ogni candidato; FAIL se < 3.
- Per Gate-FONTE: verifica presenza di `namespace`, `key`, `ts` in ogni elemento di `esempi[]`.
- Per Gate-CORRELAZIONE: flag automatico su affermazioni con keyword causali ("causa", "porta a",
  "determina"); per le affermazioni flaggate: richiede revisione manuale da CF-R8-QA
  (non FAIL automatico, ma sospensione per revisione).
- Per Gate-UNICITA: query `cf/patterns` con filtro `{tipo, contesto.formato, contesto.brand}`;
  calcola similarità testuale con le entry esistenti (threshold: [DM] — da calibrare);
  segnala potenziali duplicati per revisione.
- Produce `pattern-validation-report.json` con esito per ogni candidato.

**Input:**
```json
{
  "candidati": [
    {
      "pattern_id_proposto": "CAND-R8-HOOK-MB-CAROSELLO-001",
      "tipo": "hook",
      "proposto_da": "CF-R8-HOOK",
      "contesto": {"brand": "mentalita-brutale", "formato": "carosello-ig"},
      "pattern": "Hook interrogativo con dato numerico associato a engagement superiore alla media in 3 casi",
      "esempi": [
        {"order_id": "CF-2026-0041", "namespace": "cf/patterns", "key": "CF-R7-FEEDBACK-2026-06-06", "ts": "2026-06-06T10:00:00Z"},
        {"order_id": "CF-2026-0055", "namespace": "cf/patterns", "key": "CF-R7-FEEDBACK-2026-06-13", "ts": "2026-06-13T10:00:00Z"},
        {"order_id": "CF-2026-0063", "namespace": "cf/patterns", "key": "CF-R7-FEEDBACK-2026-06-20", "ts": "2026-06-20T10:00:00Z"}
      ],
      "n_casi": 3
    }
  ]
}
```

**Output:**
```json
{
  "report_id": "PV-2026-06-30-001",
  "ts": "2026-06-30T09:00:00Z",
  "risultati": [
    {
      "pattern_id_proposto": "CAND-R8-HOOK-MB-CAROSELLO-001",
      "gate_n3": "PASS",
      "gate_fonte": "PASS",
      "gate_correlazione": "PASS — nessuna keyword causale rilevata",
      "gate_unicita": "PASS — nessun duplicato rilevato in cf/patterns",
      "esito_automatico": "PASS — pronto per revisione CF-R8-QA",
      "richiede_revisione_manuale": false
    }
  ],
  "sommario": {"totale": 1, "pass_auto": 1, "fail_auto": 0, "sospesi_per_revisione": 0}
}
```

**Dry-run:** con flag `--dry-run` elenca i pattern candidati e i namespace che verrebbero
interrogati senza eseguire la validazione; utile per verificare che i path siano corretti
prima dell'esecuzione.

---

## Script 2: engine-comparator

**Scopo:** Costruire la matrice `engine × formato × brand` per CF-R8-ENGINE nel ciclo mensile.
Aggrega i verdetti CF-R6 del periodo e produce la matrice con first-pass rate, n_rework medio
e gate breakdown per ogni cella comparabile.

**Trigger:** chiamato da CF-R8-ENGINE durante WF-PATTERN-DISTILLATION (passo 1c).

**Cosa fa:**
- Legge tutti i `orders/<id>/05-qa/verdict.json` del periodo specificato.
- Per ogni ordine: estrae `engine_usato` da `orders/<id>/order.json` (campo `engine_preference`
  o log del CF-R5 nel trace.jsonl).
- Costruisce la matrice `{engine, formato, brand}` → `{n_ordini, first_pass_rate, n_rework_medio,
  gate_formato_pass, gate_brand_pass, gate_copy_pass}`.
- Identifica le celle con n_ordini ≥ 3 su almeno 2 engine diversi (celle comparabili).
- Per le celle comparabili: calcola delta first_pass_rate tra i due engine.
- Produce `engine-comparison-matrix.json` con la matrice completa e la lista delle celle
  comparabili con delta calcolato.

**Input:**
```json
{
  "periodo": "2026-06-01/2026-06-30",
  "verdict_base_path": "orders/",
  "formati_inclusi": ["carosello-ig", "video-ugc", "thumbnail", "articolo"]
}
```

**Output:**
```json
{
  "report_id": "EC-2026-06-001",
  "periodo": "2026-06-01/2026-06-30",
  "matrice": [
    {
      "engine": "canva",
      "formato": "carosello-ig",
      "brand": "mentalita-brutale",
      "n_ordini": 5,
      "first_pass_rate": 1.0,
      "n_rework_medio": 0,
      "celle_comparabili_con": [
        {"engine": "puppeteer", "delta_first_pass_rate": 0.67, "n_ordini_peer": 3}
      ]
    }
  ],
  "celle_insufficienti": [
    {"engine": "higgsfield", "formato": "video-ugc", "brand": "brand-education", "n_ordini": 1}
  ],
  "ts": "2026-06-30T10:00:00Z"
}
```

**Dry-run:** con flag `--dry-run` elenca i path dei verdict.json che verrebbero letti senza
aggregare i dati; utile per verificare che tutti i verdetti del periodo siano presenti.

---

## Script 3: neural-feeder

**Scopo:** Alimentare `neural_train` con i pattern validati in `cf/patterns` che non sono
ancora stati processati (`neural_trained: false`). Chiamato da CF-R8-NEURAL su autorizzazione
di CF-R8-COORD.

**Trigger:** chiamato da CF-R8-NEURAL durante WF-IMPROVEMENT-CYCLE (passo 9, asincrono).

**Cosa fa:**
- Legge tutte le entry in `cf/patterns` con `stato: "VALIDATO" | "IMPLEMENTATO"` e
  `neural_trained: false` (o campo assente).
- Per ogni pattern: trasforma in formato compatibile con `neural_train`.
- Chiama `neural_train` con i dati trasformati; gestisce errori per singolo pattern
  senza interrompere il batch.
- Per ogni pattern processato con successo: aggiorna il campo `neural_trained: true`
  e `ts_neural_training` nell'entry di `cf/patterns`.
- Produce `neural-feed-report.json` con elenco processati, errori, timestamp.

**Input:**
```json
{
  "pattern_ids": ["PAT-R8-HOOK-MB-CAROSELLO-001", "PAT-R8-FAILURE-COPY-HOOK-001"],
  "autorizzazione": "CF-R8-COORD",
  "ts_autorizzazione": "2026-06-30T12:00:00Z",
  "batch_max_size": 10
}
```

**Output:**
```json
{
  "sessione_id": "NEURAL-SESS-2026-06-30-001",
  "processati": ["PAT-R8-HOOK-MB-CAROSELLO-001", "PAT-R8-FAILURE-COPY-HOOK-001"],
  "errori": [],
  "n_processati": 2,
  "n_errori": 0,
  "ts_inizio": "2026-06-30T12:05:00Z",
  "ts_fine": "2026-06-30T12:12:00Z",
  "stato": "completato"
}
```

**Dry-run:** con flag `--dry-run` elenca i pattern che verrebbero processati con il loro
formato trasformato senza chiamare `neural_train`; utile per verificare la trasformazione
prima dell'esecuzione reale.

---

## Regole script (non negoziabili)

1. Ogni script produce sempre output JSON strutturato (`pattern-validation-report.json`,
   `engine-comparison-matrix.json`, `neural-feed-report.json`).
2. `pattern-validator` e `engine-comparator` sono sola lettura: non modificano nessun asset
   o namespace di produzione.
3. `neural-feeder` scrive solo in `cf/patterns` (update flag `neural_trained`): non tocca
   nessun altro namespace.
4. In caso di file non leggibile o errore tecnico: output con `"esito": "ERRORE"` e motivo
   strutturato; mai eccezione non gestita che blocca l'intero batch.
5. Dry-run disponibile per ogni script prima dell'esecuzione reale.
6. Nessuno script accetta parametri che abbassino la soglia n ≥ 3: la soglia è hardcoded
   e non configurabile dall'esterno.

---

## Connessioni

- [[cf-r8-qa]] · `agenti/cf-r8-qa.md` — usa pattern-validator nel Gate QA di WF-PATTERN-DISTILLATION
- [[cf-r8-engine]] · `agenti/cf-r8-engine.md` — usa engine-comparator per costruire la matrice mensile
- [[cf-r8-neural]] · `agenti/cf-r8-neural.md` — usa neural-feeder per la sessione di training
