# MT-XV6Y — S2a - stato_lancio.py, comando lancio, caricamento e validazione

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 6

## Cosa fa

S2a. `stato_lancio.py` e il comando `lancio`: crea, legge, elenca, con `stato.json` e
lock su file. Piu' il caricamento e la validazione degli artefatti: un artefatto e' valido
solo contro il proprio schema, **ricalcolato**, mai fidandosi di un campo salvato.

`valida_registro.py` deve stare a exit 0 **prima** del build, non dopo.

## Gate di chiusura

`python -m scripts.lancio crea prova-vuota --prodotto Prova` crea lo stato, e `lancio elenco` lo mostra.

## Output

