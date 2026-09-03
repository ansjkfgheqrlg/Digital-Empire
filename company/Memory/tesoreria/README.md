# Tesoreria - i dati veri

Due file ad accodamento, una riga per movimento:

- `entrate.jsonl` - ogni euro che entra o che dovrebbe entrare
- `spese.jsonl` - ogni euro che esce

Si scrivono con `python scripts/tesoreria.py` e si leggono a occhio.
Si possono correggere a mano: sono testo, una riga per movimento.

**Non cancellare righe.** Un movimento sbagliato si corregge
aggiungendone uno di segno opposto con la nota che spiega perche':
la storia dei soldi non si riscrive, si annota.
