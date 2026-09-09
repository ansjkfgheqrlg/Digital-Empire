# MT-GHZ6 — S2d - i sei controlli, i sei agenti, lan-gate e il ponte ADR-014

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 9

## Cosa fa

S2d. I sei controlli veri, i sei agenti (`lan-pub-censore`, `lan-str-filtro`,
`lan-prd-collaudatore`, `lan-int-analista`, `lan-prv-modello`, `lan-off-conductor`), piu'
`lan-gate`, piu' il ponte verso gli agenti secondo ADR-014: prompt da standard input,
identificativo esplicito del modello, `total_cost_usd` letto e budget verificato **prima**
della chiamata, `registro-chiamate.jsonl`.

**Invarianti non negoziabili:** `lan-gate` non ha mai `Write`/`Edit` (INV-09); chi produce
un artefatto non lo approva mai (INV-01). `valida_registro.py` verifica entrambi prima di
ogni build.

Dipende da [[MT-4GNU]] (i rossi esistono gia') e da [[MT-3XWC]].

## Gate di chiusura

`lancio crea prova-vuota` seguito da `lancio avanza prova-vuota` si ferma al controllo dell'offerta, esce con codice **1**, scrive il verbale e lascia lo stato dov'era. **Se esce zero, S2 non e' chiuso**, per quanto codice sia stato scritto.

## Output

