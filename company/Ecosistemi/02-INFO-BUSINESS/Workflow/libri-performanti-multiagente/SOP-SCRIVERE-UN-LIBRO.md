# SOP — Scrivere e pubblicare un libro KDP

**Procedura operativa standard.** Vale per ogni libro nuovo, sempre uguale. Chi la esegue:
Claude (scrittura) + gli script del motore (tutto il resto) + Gael (pubblicazione finale).

**Tempo indicativo per un libro da 120 pagine**: 2-4 ore di lavoro di scrittura, spezzabili
in più sessioni senza perdere niente.

---

## Come si avvia

Dire a Claude: **"scrivi un libro sulla nicchia <X>"** oppure **"riprendi il libro <slug>"**.
Da lì Claude segue questa procedura senza bisogno di altre istruzioni.

---

## STEP 1 — Ricerca nicchia *(automatico)*

```
python -m engine.amazon_research "cozy mystery cats"
```

Restituisce i libri concorrenti reali su Amazon: titoli, autori, prezzi, recensioni.
**Serve a**: capire cosa vende in quella nicchia e con che taglio, non a copiare.

**Fatto quando**: hai una lista di 10-20 concorrenti veri sotto gli occhi.

---

## STEP 2 — Validazione nicchia *(automatico)*

```
python -m engine.story_validator "<titolo di lavoro>" "<descrizione>"
```

Blocca diari, planner, journal e affini: non sono storie, vendono male e non è quello che
stiamo costruendo. Se esce **NO-GO, si cambia idea** — non si forza.

**Fatto quando**: esito GO.

---

## STEP 3 — Creazione progetto e outline *(Claude scrive)*

```
python -m engine.book_project nuovo "<Titolo Del Libro>" --nicchia "<nicchia>"
```

Crea la cartella del libro. Poi Claude scrive `outline.md` con:

- **Titolo definitivo** — commerciale, chiaro sul genere
- **Personaggi** — protagonista, comprimari, antagonista: nome + ruolo in una riga ciascuno
- **Trama in 3 atti** — impianto, sviluppo/complicazione, risoluzione
- **Scaletta dei 24 capitoli** — una riga per capitolo, cosa succede

L'outline è la mappa: se è solida, i capitoli vengono da sé e restano coerenti.

**Fatto quando**: `outline.md` contiene tutti e quattro i punti sopra.

---

## STEP 4 — Scrittura capitoli *(Claude scrive, a blocchi)*

Un file per capitolo: `capitoli/cap_01.md`, `cap_02.md`, …

**Formato di ogni file**:
```markdown
# Titolo del capitolo

Primo paragrafo.

Secondo paragrafo.
```

**Regole di lavoro**:
- **4-6 capitoli per volta**, non tutti in una botta: la qualità cala e la sessione si
  appesantisce.
- Ogni capitolo **~1500 parole** (24 × 1500 = 36.000 = ~120 pagine).
- Dopo ogni blocco, aggiornare `riassunti.md` con 2-3 righe per capitolo scritto: è la
  memoria del libro, permette di riprendere in una sessione nuova senza rileggere tutto.
- Prima di scrivere un blocco nuovo, **rileggere `outline.md` + `riassunti.md`**: bastano
  quelli per la continuità.

**Controllo a ogni blocco**:
```
python -m engine.book_project stato <slug>
```
Dice capitoli scritti, parole totali, pagine stimate e qual è il prossimo capitolo.

**Fatto quando**: 24/24 capitoli e parole ≥ 34.500.

---

## STEP 5 — Copertina *(automatico, LM Arena)*

```
python -m engine.cover_generator
```

Genera l'immagine dal titolo e dalla trama del libro. Una sola richiesta: qui LM Arena
funziona bene (verificato con immagini reali).

**Fatto quando**: file `.png` reale su disco, > 500 KB, guardato e giudicato adeguato al
genere.

---

## STEP 6 — Assemblaggio e controllo *(automatico)*

```
python -m engine.book_project assembla <slug> --cover <percorso-copertina.png>
```

Produce il `.docx` formattato KDP (6×9", margini specchio, numeri di pagina) e **conta le
pagine vere rileggendo il file salvato**. Se è sotto le 115 pagine **si ferma** e dice
quanti capitoli mancano — non esiste il caso "dichiarato pronto ma corto" (era il bug
ricorrente del vecchio workflow: 120 pagine dichiarate, 21 reali).

**Fatto quando**: pacchetto creato in `LIBRI/libri_pronti/<Titolo>/` con manoscritto +
copertina + metadata.

---

## STEP 7 — Pubblicazione *(manuale, Gael)*

Caricare su KDP il pacchetto pronto. **Questo passo resta manuale di proposito**: il
caricamento su un account editoriale reale è meglio che passi da una persona.

Dopo la pubblicazione, spostare la cartella in `LIBRI/libri_pubblicati/`.

---

## Riprendere un libro interrotto

Niente si perde: i capitoli sono file su disco.

```
python -m engine.book_project stato            # elenco di tutti i libri in lavorazione
python -m engine.book_project stato <slug>     # a che punto è questo
```

Poi si rileggono `outline.md` e `riassunti.md` e si riparte dal capitolo indicato.

---

## Regole non negoziabili

1. **Mai dichiarare finito un libro sotto le 115 pagine reali.** Il controllo è automatico
   e blocca: non aggirarlo con `--forza` se non per ispezionare una bozza.
2. **Mai un capitolo identico o quasi a un altro.** Se succede è un errore di processo, non
   una coincidenza: riscriverlo.
3. **Mai copiare da un concorrente.** La ricerca serve a capire il mercato, non i testi.
4. **La coerenza viene da outline + riassunti**, non dalla memoria della sessione: se non
   sono aggiornati, il libro va in contraddizione al capitolo 12.
