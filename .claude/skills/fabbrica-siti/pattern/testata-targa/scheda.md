# testata-targa

**Corsia A** | origine: `armageddon.css:118-181` (Andrei Pascu) | canone: `--u`, `--t-78`, `--orange`

## Quando
Pagine di lancio, landing singole, one-pager. Ovunque **la navigazione sia attrito** e serva un solo
ritorno al brand madre.

## Quando NO
Siti multi-pagina con piu' di due destinazioni reali. Una targa con cinque link non e' piu' una
targa: e' un menu travestito, e li' va usata una navigazione vera.

## Il perche'
Il commento del CSS originale: *"built as a plate between two rules that dissolve into the black, so
it reads as part of the same object rather than a website nav bolted on top."* I due filetti in
dissolvenza sono cio' che la lega alla pagina invece di appoggiarla sopra.

## Le misure
| | |
|---|---|
| larghezza | `var(--u)` |
| padding verticale | `clamp(15px, --u x 0.027, 28px)` |
| filetti | 1px, `linear-gradient` verso `transparent` |
| segno | `clamp(23px, --u x 0.036, 36px)` |
| nome | `clamp(11px, --u x 0.0145, 15px)`, w800, `letter-spacing: 0.26em`, opacita' `--t-78` |
| hover | nome -> arancione; segno -> `scale(1.08)` + glow, `0.35s var(--ease-land)` |

## Cosa cade se sbagli
- **Filetti pieni invece che in dissolvenza** -> la testata diventa un bordo, e la pagina si spezza in due.
- **Piu' di un link** -> vedi "Quando NO".
- **Nome a opacita' 1** -> ruba attenzione all'hero. Sta a `--t-78` perche' e' un'indicazione, non un messaggio.
