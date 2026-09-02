---
name: libro-del-giorno
description: Apre e avvia il libro di OGGI leggendolo dal piano editoriale della settimana - nicchia, titolo, premessa e angolo sono gia' decisi, il comando non chiede niente. Rispetta la Regola 6: se c'e' un libro aperto e incompleto si finisce quello. Usa questa skill quando Gael dice "/libro-del-giorno", "il libro di oggi", "cosa scrivo oggi", "apri il libro", o all'inizio di ogni giornata di produzione. NON usarla per generare il piano - quello e' /piano-libri.
---

# /libro-del-giorno — Un comando, e parte

```bash
cd "company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente"
python -m engine.kdp libro-del-giorno            # il libro di oggi
python -m engine.kdp libro-del-giorno --giorno 4 # forza un giorno del piano
```

Non chiede niente perché **tutto è già stato deciso** dal piano: nicchia (con i numeri
misurati), titolo, autore, premessa, angolo differenziante, struttura.

## Cosa fa, in ordine

1. Legge `LIBRI/_piani/piano_<lunedì della settimana corrente>.json`
2. Calcola **che giorno è oggi** dentro quella settimana (lunedì = 1)
3. Prende la riga di quel giorno
4. **Controlla se c'è un libro aperto e incompleto** → se c'è, si finisce QUELLO
5. Crea il progetto con i parametri della riga (`kdp nuovo` sotto il cofano)
6. Scrive premessa, angolo e numeri **dentro `progetto.json`**: chi riprende fra tre giorni
   trova tutto lì e non deve tornare al piano

Poi si scrive, a blocchi, col gate dopo ognuno:
```bash
python -m engine.kdp blocco <slug>     # dopo OGNI blocco di capitoli
```
oppure si lascia fare tutto al flusso automatico:
```bash
python -m engine.kdp auto --slug <slug>
```

## Le due regole non negoziabili

**REGOLA 6 — si finisce quello che è aperto.** Se esiste un libro incompleto, il comando lo
riprende e **rifiuta** di aprirne un altro, dicendo quale e perché. È così che si accumulano
quattro libri a metà: aprendone uno nuovo ogni volta che il precedente si fa noioso. Per
abbandonarne uno davvero, va detto esplicitamente e va cancellata la sua cartella.

**NON IMPROVVISA MAI.** Se il piano della settimana non esiste, il comando si ferma e dice di
lanciare `/piano-libri`. Non sceglie un libro a caso: un comando che inventa quando gli manca
l'input è esattamente il modo in cui è nato **B-018** — quattro libri, quattro nicchie, tre
nomi d'autore, e la pagina "Also by" vuota su tutti e quattro.

## Se si ferma

| Messaggio | Cosa fare |
|---|---|
| *nessun piano per la settimana* | `/piano-libri` |
| *c'è un libro aperto e incompleto* | finisci quello: `kdp blocco <slug>` o `kdp auto --slug <slug>` |
| *il piano non ha una riga per il giorno N* | il piano ha meno righe dei giorni: rigenera o usa `--giorno` |
| *il progetto esiste già* | il libro di oggi è già stato aperto: riprendilo |

## Cosa NON fa

- Non genera il piano (è `/piano-libri`).
- Non genera l'immagine di copertina e **non carica su KDP**: sono i due passi umani. Il primo
  perché serve un generatore di immagini, il secondo perché è irreversibile verso l'esterno.
- Non decide nicchia o autore: arrivano dal piano, che li prende dalla decisione di catalogo.

## Connessioni

- Genera il piano: `/piano-libri`
- Scrive i capitoli: `/libro` (skill già esistente) oppure `kdp auto`
- Motore: `engine/libro_del_giorno.py`
- Regole complete: `SOP-SCRIVERE-UN-LIBRO.md`
