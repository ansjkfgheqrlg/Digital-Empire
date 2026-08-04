# Playbook — qa-output-reviewer

## Quando gira
Dopo S5 (render), come ultimo gate. Chiamata: `gate_d(ctx, dealer)`.

## Interpretare i risultati
| Issue | Significato | Chi corregge |
|---|---|---|
| `nessun PDF preventivo_*.pdf` | render non eseguito/fallito | S5 op-pdf-renderer |
| `PDF troppo piccolo` | render vuoto | S5 (content/foto mancanti) |
| `scheda tecnica/descrizione/dotazioni vuota` | content incompleto | S3 op-translator-copy |
| `final_title senza prezzo` | pricing/titolo | S4 op-pricer |
| `N foto mancanti su disco` | download foto fallito | S1 scraper |
| `placeholder Jinja non risolti` | context template incompleto | S5 (template/context) |

## Consegna
Solo se `gate_d` è verde: il PDF `runs/<id>/preventivo_<slug>.pdf` è pronto per il cliente.

## Riferimento verificato
BMW 320d → PDF 63 KB, tutte le sezioni, prezzo in titolo, 0 placeholder → Gate D PASS.
Ispezione visiva confermata (2 pagine, layout pulito).
