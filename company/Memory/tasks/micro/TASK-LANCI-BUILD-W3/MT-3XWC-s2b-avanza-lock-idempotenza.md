# MT-3XWC — S2b - avanza con lock, idempotenza, codici 0/1/2/3, verbali

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 7

## Cosa fa

S2b. `avanza`, cioe' la firma del documento 01 §2: lock esclusivo, idempotenza, codici
d'uscita 0/1/2/3, verbali scritti a ogni passaggio.

Dipende da [[MT-XV6Y]].

## Gate di chiusura

`lancio avanza` e' idempotente (due esecuzioni di fila non cambiano niente la seconda volta) e scrive un verbale a ogni transizione.

## Output

