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

## Stato

**Chiusa il 2026-09-10.** `scripts/stato_lancio.py` + `scripts/lancio.py` in `company/Ecosistemi/15-LANCI/02-AUTOMAZIONI-E-SCRIPTS/`. **17 prove verdi**.

La condizione di sblocco del piano, eseguita alla lettera:

```
python -m scripts.lancio crea prova-vuota --prodotto "Prova"   -> exit 0
python -m scripts.lancio elenco                                -> exit 0
python -m scripts.lancio valida manuale-claude-code            -> exit 0, 3 su 3 validi
python -m scripts.lancio avanza manuale-claude-code            -> exit 2, dice che e' MT-3XWC
```

Coperti: creazione idempotente (creare due volte non sovrascrive), lock esclusivo su file con dentro chi lo tiene, validazione **ricalcolata** contro lo schema (un artefatto che si dichiara valido fallisce lo stesso), le proposte non contano come artefatti, verbale a ogni evento, codici 0/1/2/3.

**Non copre `avanza` e i gate**: sono [[MT-3XWC]] e [[MT-GHZ6]], e il comando lo dice invece di fingere di eseguirli.
