# Routing — PreventivoForge

Chi gestisce cosa, e dove si escala.

| Stage | Agente operativo | Script | Regola | Gate dopo | Verificatore | Owner |
|---|---|---|---|---|---|---|
| S1 scraping | `op-scraper` | `scraper.py` | R1 | A | `qa-extraction-verifier` | Max / Gael* |
| S2 parsing | `op-parser` | `parser.py` | R2 | A | `qa-extraction-verifier` | Max / Gael* |
| S3 traduci+copy | `op-translator-copy` | `translate_copy.py` | R3 | B | `qa-translation-verifier` | Gael |
| S4 pricing | `op-pricer` | `pricer.py` | R4 | C | `qa-price-verifier` | Max / Gael* |
| S5 PDF | `op-pdf-renderer` | `render_pdf.py` | R5 | D | `qa-output-reviewer` | Gael |

\* Script operativo = Max (Half A); il **verificatore** del gate = Gael (Half B).

## Escalation
- **Gate rosso 1ª volta** → il conductor riprova lo stage secondo la sua regola (retry/fallback).
- **Gate rosso 2ª volta** → STOP: il conductor riporta il problema (nessuna consegna). Umano decide.
- **S1 bloccato (anti-bot)** → route alternativa: modo `--manual` (HTML+foto locali).
- **Errore config dealer** → fallback default `.env`, warning nel report.

## Multi-tenant
Il dealer è scelto da `--dealer <id>` (default `prof-autocad`); `dealers.load_dealer()` risolve
prezzo/logo/contatti. Aggiungere un dealer = nuova cartella in `concessionarie/`, nessun cambio codice.
