# MT-GEKH — S3 - dal prezzo all'apertura: CPY, FNL, EDT, BDG, APE

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 10

## Cosa fa

S3, dal prezzo all'apertura:

- `ART-CPY` + `GATE-CPY-1` + `lan-cpy-conductor`
- `ART-FNL` + `GATE-FNL-1` + `lan-fnl-costruttore` — **inclusa la prova di cassa**
- `ART-EDT` + `GATE-EDT-1` + `lan-edt-pianificatore`
- `ART-BDG` + `GATE-TSR-1` + `GATE-TSR-2` + `lan-tsr-contabile`
- `ART-APE` + `GATE-REG-1` + `lan-reg-calendarista`

`ART-FNL` e' anche il cuore della task 4 della settimana (`TASK-LANCI-FUNNEL-W3`).

## Gate di chiusura

Un lancio di prova arriva a `PRONTO` e **si ferma li'**, perche' `PU-APERTURA` non ha default e non ce l'avra' mai.

## Output

