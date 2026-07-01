# Supervisor — PreventivoForge

Il **conductor** (`run.py` + agente `agents/conductor/`) è il supervisore del run. Governa la
sequenza, applica i gate, gestisce retry/fallback e budget, e scrive stato+trace.

## Sequenza governata
```
S1 scraping ─▶ S2 parsing ─▶ [GATE A] ─▶ S3 traduci+copy ─▶ [GATE B]
   ─▶ S4 pricing ─▶ [GATE C] ─▶ S5 PDF ─▶ [GATE D] ─▶ consegna
```
- S3 e S5 (+ gate B/C/D) sono di **Half B**: il supervisore li invoca se i moduli esistono,
  altrimenti salta con nota di handoff (non è errore).
- S4 può girare anche senza S3 (prezzo dipende solo da `listing.json` + dealer).

## Responsabilità
1. **Ordine + dipendenze:** nessuno stage parte se il precedente non ha prodotto il suo output.
2. **Gate bloccanti:** un gate rosso ferma la pipeline e riporta il motivo (nessuna consegna parziale).
3. **Retry/fallback:** S1 blocco anti-bot → istruzioni headful/`--manual`; foto → retry con Referer.
4. **Stato/tracciabilità:** `runs/<id>/state.json` (step→status) + `trace.jsonl` (ogni evento).
5. **Budget:** un solo run per volta; nessuna azione esterna oltre lo scraping dell'URL dato.

## Contratto con gli agenti
Ogni agente operativo espone una funzione pura sul `RunContext` (`scrape`, `parse`, `price`,
`translate`, `render`) e non conosce gli altri: comunicano SOLO via file in `runs/<id>/`
(`raw.json` → `listing.json` → `listing_it.json` → `preventivo_*.pdf`).
