# MT-04 — S2: stato_lancio.py, avanza, ponte agenti, sei gate, sei agenti

- **Padre:** TASK-LANCI-BUILD-W3
- **Onda:** 3
- **Stato:** APERTA
- **Data:** 2026-09-08
- **Dipende da:** MT-03
- **Scope (percorsi che tocca — controllo di sovrapposizione):**
  - company/Ecosistemi/15-LANCI/

## Cosa fa

S2 (`04-COSTRUZIONE.md` §3, 45-65 ore) — la prima riga di codice di tutto l'ecosistema:

1. `stato_lancio.py` + comando `lancio`: crea/legge/elenca, `stato.json` con lock su file.
2. Caricamento e validazione degli artefatti (un artefatto è valido solo contro il proprio
   schema, ricalcolato).
3. `avanza` — la firma di `01-ARCHITETTURA.md` §2: lock esclusivo, idempotenza, codici
   0/1/2/3, verbali.
4. Il ponte verso gli agenti (ADR-014): prompt da standard input, identificativo esplicito
   del modello, `total_cost_usd` letto e budget verificato **prima** della chiamata,
   `registro-chiamate.jsonl`.
5. I sei gate di questa metà — `GATE-PUB-1`, `GATE-STR-1`, `GATE-PRD-1`, `GATE-INT-1`,
   `GATE-PRV-1`, `GATE-OFF-1` — ognuno col suo test rosso scritto **prima**.
6. I sei agenti — `lan-pub-censore`, `lan-str-filtro`, `lan-prd-collaudatore`,
   `lan-int-analista`, `lan-prv-modello`, `lan-off-conductor`, più `lan-gate`.

## Gate di chiusura

```
python -m scripts.lancio crea prova-vuota --prodotto "Prova"
python -m scripts.lancio avanza prova-vuota
```
Deve bloccarsi al controllo dell'offerta, uscire con codice **1**, scrivere il verbale,
lasciare lo stato dov'era. **Se esce zero, S2 non è chiuso**, per quanto codice sia stato
scritto. Più: `python -m pytest tests/rossi/` — i test rossi dei sei controlli devono
fallire come devono.

## Output

`scripts/lancio.py`, `stato.json`, 6 agenti + `lan-gate`, 6 gate con test rosso verde.
