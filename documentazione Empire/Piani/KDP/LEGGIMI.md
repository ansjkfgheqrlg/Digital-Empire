# Piani editoriali KDP — documentazione ufficiale

Qui vive il DOPPIONE ufficiale di ogni piano editoriale libri (ecosistema 02-INFO-BUSINESS).
L'originale vivo, quello che il motore legge e aggiorna, resta in:

`company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/LIBRI/_piani/`

Regola: si COPIA qui, mai si sposta (emperator.md §6.17). Niente PDF: un piano settimanale
e' materiale temporaneo, si tiene in Markdown + JSON.

| Piano | Settimana | Autore piano | Generato | Nicchia di catalogo | Commit |
|---|---|---|---|---|---|
| piano-editoriale-kdp-settimana-2026-08-31 | 31/08 → 06/09/2026 | Gael | 2026-09-02 | witch bookshop cozy fantasy (Maren Ashcroft) | 66389b58 |

Come si genera un piano nuovo: skill `/piano-libri` (dentro il workflow libri-performanti-multiagente),
motore `engine/piano.py`. Il libro del giorno si apre con `/libro-del-giorno`.
