# Playbook — qa-regole-checker

## Quando gira
Dopo S5 (render) e dopo `qa-immagini`. Chiamata: `gate_regole(ctx, dealer)`.
Wiring in `run.py` = Max (Gate R + Gate IMG dopo S5, HANDOFF-GAEL-2 TASK 4).

## Come leggere `regole-check.json`
Ogni voce `R-xx` ha `pass` (bool) + `note`. Le regole FAIL sono la lista dei difetti da correggere.

| Regola rossa | Dove si corregge |
|---|---|
| R-01 / R-10 (logo pages) | `templates/preventivo.html` (pagine `logo-only`) |
| R-02 (logo header) | template (`logo-sm`) |
| R-03 (dati azienda) | config `concessionarie/<id>/config.json` (`legal`+`contacts`) |
| R-05 (scheda) | `render_pdf._specs_novacar` + template |
| R-08 (prezzo) | `render_pdf._price_novacar` + template |
| R-09 (immagini) | `render_pdf` (photo_pages, contain) |
| R-11 (tedesco) | `translate_copy` + glossario |
| R-12 (prezzo) | pricing (Max) / estrazione |

## Riferimento verificato
Fixture BMW + dealer novacar → R-01…R-14 tutte PASS, `regole-check.json` scritto.
