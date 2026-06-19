---
Type: SCRIPTS
Status: Active
Tags: #scripts #tracking #ab-test #pattern #analytics #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# Script Target V2 — L2.4 Analytics & Ottimizzazione

> **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING · **Versione:** v2
> Tre script deterministici da forgiare via 07-FORGE come automazioni del reparto.

---

## Script 1 — `tracking-validator`

**Scopo:** Verifica che un tracking plan sia privo di "eventi fantasma" prima del lancio.
Legge il file `tracking_plan.json` e verifica che ogni evento abbia:
- `nome` presente e in formato snake_case
- `trigger` presente e non vuoto
- `valore` presente e non vuoto

**Output:** `{valid: true/false, eventi_fantasma: [...], eventi_ok: n}`
**Owner:** AN1
**Quando:** Step 6 di WF-TRACKING-SETUP (pre-lancio)
**Input:** `tracking_plan.json` (path)
**Output file:** `tracking_validation_report_{campagna_id}.json`

**Comportamento deterministico:** non modifica il tracking plan, non lancia nulla.
Solo legge e valida. Exit code 0 = zero eventi fantasma (PASS); exit code 1 = fantasmi rilevati (blocco).

---

## Script 2 — `experiment-sizer`

**Scopo:** Calcola la dimensione minima del campione per un esperimento A/B dato
il tasso base, la differenza attesa, la confidenza e il power statistico.

**Formula:** test a due proporzioni con test z bilaterale
**Input:**
- `tasso_base` (float, es. 0.025 per CTR 2.5%)
- `differenza_attesa` (float relativa, es. 0.30 per +30%)
- `confidenza` (default 0.90)
- `power` (default 0.80)
- `n_varianti` (int, default 2)
- `traffico_giornaliero` (int, per stima giorni)

**Output:** `{campione_per_variante: int, giorni_stimati: float, fattibile_in: str}`
**Owner:** AN3
**Quando:** Step 2 di WF-AB-TEST (prima del lancio)
**Output file:** `experiment_size_{test_id}.json`

**Comportamento deterministico:** solo calcolo matematico, nessuna dipendenza esterna.
Risultato riproducibile con gli stessi parametri. Aggiunge avviso se il traffico stimato
non raggiunge il campione entro 30 giorni.

---

## Script 3 — `pattern-writer`

**Scopo:** Scrive un pattern o antipattern strutturato nel namespace memoria
`marketing/copy/patterns/{icp}` o `marketing/copy/antipatterns/{icp}` dopo
la verifica della regola anti-rumore (≥2 run indipendenti).

**Input:**
- `tipo` ("pattern" | "antipattern")
- `icp` (string)
- `formato` ("ad" | "email" | "sales-page" | "social")
- `sezione_apsoc` ("A" | "P" | "S" | "O" | "CTA")
- `testo_pattern` (string)
- `evidenza` (object: `n_run`, `copy_ids`, `metrica`)
- `data_consolidamento` (YYYY-MM-DD)

**Validazione pre-scrittura:**
- `n_run` ≥ 2? Se no → exit code 1 con messaggio "regola anti-rumore non soddisfatta"
- Tutti i campi obbligatori presenti? Se no → exit code 1 con lista campi mancanti
- Pattern già esistente per stesso `{icp, formato, sezione_apsoc}`? → aggiorna n_run
  anziché duplicare

**Output:** conferma scrittura nel namespace + log entry per `wiki/log.md`
**Owner:** AN4
**Quando:** Passo 3 di WF-OPTIMIZATION-LOOP (distillazione)
**Output file:** `pattern_write_log_{data}.json`

---

## Note implementazione

I tre script sono da forgiare via 07-FORGE come script Python (3.x) standalone.
Nessuna dipendenza esterna oltre alla libreria standard + `scipy.stats` per
`experiment-sizer`. Tutti deterministici: stesso input → stesso output.
Logging strutturato (JSON) per ogni run per tracciabilità nel ciclo di ottimizzazione.

---

## Connessioni

- [[WF-TRACKING-SETUP]] · `workflow/WF-TRACKING-SETUP.md` — usa `tracking-validator`
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md` — usa `experiment-sizer`
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md` — usa `pattern-writer`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
