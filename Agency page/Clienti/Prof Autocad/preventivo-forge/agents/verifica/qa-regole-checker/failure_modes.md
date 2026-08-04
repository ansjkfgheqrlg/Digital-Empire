# Failure Modes — qa-regole-checker

| # | Rischio | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Regola dimenticata | difetto passa | il gate scorre R-01…R-14 in modo esaustivo e le logga tutte |
| 2 | Check via stringa fragile | markup cambia → falso FAIL | usa marcatori stabili del template (`logo-only`, `logo-sm`, testi barre) |
| 3 | Report non scritto | manca l'audit | `regole-check.json` salvato sempre (try/except non silenzia il verdetto) |
| 4 | Delega non eseguita | R-09/R-11/R-12 non valutate | invoca `gate_img`/`gate_b`/`gate_c` e riporta le loro issue |
| 5 | Manca `dealer` | non re-renderizza | verifica solo il verificabile; segnala che serve dealer per il check pieno |
| 6 | R-14 auto-referenziale | passa anche con altre rosse | R-14 = AND di tutte le altre (fallisce se una fallisce) |

## Principio
Nessuna regola è "minore". Il gate non decide priorità: se una è rossa, il PDF non esce.
