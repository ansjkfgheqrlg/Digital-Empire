# Evals — qa-output-reviewer

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 happy path | run completo | `(True, [])` |
| E2 no PDF | render non eseguito | `(False, ["nessun PDF ..."])` |
| E3 PDF minuscolo | file < 20 KB | `(False, ["PDF troppo piccolo ..."])` |
| E4 content vuoto | equipment_it vuoto | `(False, ["dotazioni ... vuote"])` |
| E5 titolo senza prezzo | final_title senza € | `(False, ["final_title senza prezzo"])` |
| E6 foto mancante | local_path senza file | `(False, ["N foto mancanti ..."])` |
| E7 placeholder | context incompleto (con dealer) | `(False, ["placeholder Jinja non risolti"])` |

## Metriche
- **Difetti visibili che passano** = 0 (obiettivo).
- **Copertura sezioni** = 100% delle 9 sezioni previste.

## Comando di verifica
`gate_d(ctx, dealer)` → `(True, [])`. Verificato su BMW 320d + ispezione visiva del PDF.
