# SOP — Scrivere e pubblicare un libro KDP

**Procedura operativa standard.** Vale per ogni libro nuovo, sempre uguale. Chi la esegue:
Claude (scrittura) + gli script del motore (tutto il resto) + Gael (copertina e pubblicazione).

**Tempo indicativo per un libro da 120 pagine**: 2-4 ore di lavoro di scrittura, spezzabili
in più sessioni senza perdere niente.

> **Il principio (2026-08-15)**: il libro lo scrive **Claude in sessione**. Il codice non
> chiama nessun modello — impagina, conta le pagine vere, valida, impacchetta. Tre tentativi
> di automatizzare la scrittura sono falliti (LM Arena→captcha ×2, Claude CLI→prompt troncati
> e limite di spesa); l'unico libro completo mai prodotto è nato scrivendolo a mano qui.
> Dettagli in `_archivio_automazione_modelli/LEGGIMI.md`.

---

## Come si avvia

**`/libro`** — la skill fa partire tutta la procedura. In alternativa, a parole: *"scrivi un
libro sulla nicchia X"* oppure *"riprendi il libro <slug>"*.

---

## STEP 0 — Il magazzino argomenti *(una volta a settimana)*

Una ricerca sola produce 7 argomenti pronti, poi ogni libro ne consuma uno senza rifare
l'analisi. Claude cerca sul web le nicchie che vendono, poi **verifica ognuna con numeri
veri** prima di metterla in magazzino.

```
python -m engine.kdp magazzino                     # cosa c'è di pronto
python -m engine.kdp magazzino --aggiungi f.json   # inserisce la ricerca fatta
python -m engine.kdp magazzino --prendi            # il prossimo da scrivere
```

Il codice **rifiuta** argomenti senza dati Amazon e quelli che non sono storie: è voluto.

**Fatto quando**: il magazzino ha argomenti liberi.

---

## STEP 1 — Ricerca nicchia *(automatico)*

```
python -m engine.kdp nicchie --keywords "cozy mystery cats" "small town romance"
```

Restituisce i libri concorrenti reali su Amazon: titoli, autori, prezzi, recensioni.
**Serve a**: capire cosa vende in quella nicchia e con che taglio, non a copiare.

**Fatto quando**: hai una lista di 10-20 concorrenti veri sotto gli occhi.

---

## STEP 2 — Validazione nicchia *(automatico)*

```
# (incluso nel comando sopra: una nicchia che non e' una storia esce con punteggio 0)
```

Blocca diari, planner, journal e affini: non sono storie, vendono male e non è quello che
stiamo costruendo. Se esce **NO-GO, si cambia idea** — non si forza.

**Fatto quando**: esito GO.

---

## STEP 3 — Creazione progetto e outline *(Claude scrive)*

```
python -m engine.kdp nuovo "<Titolo Del Libro>" --nicchia "<nicchia>"
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
- Ogni capitolo **~1650 parole** (24 × 1650 = 39.600 = ~124 pagine reali).
  ⚠️ **Non 1500**: 24 × 1500 = 36.000 parole, che impaginate fanno **112 pagine — sotto il
  minimo di 115**. È l'errore che ha fatto arrivare *The Ninth Winter* a 111 pagine con il
  conteggio parole "in target". La misura vera è **320 parole a pagina**, non 300.
- **Controllare la lunghezza già al primo blocco**, non a fine libro: se i primi 4 capitoli
  stanno a 1.000 parole, il libro chiuderà a ~24.000 e non c'è modo di recuperare senza
  riscriverlo.
- Dopo ogni blocco, aggiornare `riassunti.md` con 2-3 righe per capitolo scritto: è la
  memoria del libro, permette di riprendere in una sessione nuova senza rileggere tutto.
- Prima di scrivere un blocco nuovo, **rileggere `outline.md` + `riassunti.md`**: bastano
  quelli per la continuità.

**Controllo a ogni blocco**:
```
python -m engine.kdp stato <slug>
```
Dice capitoli scritti, parole totali, pagine stimate e qual è il prossimo capitolo.

**Fatto quando**: 24/24 capitoli e parole ≥ 36.800 (= 115 pagine × 320).

---

## STEP 5 — Copertina *(Claude scrive il prompt, Gael genera l'immagine)*

Claude scrive `copertina-prompt.md` nella cartella del libro: un prompt **lungo e completo**,
che descrive **tutta la copertina finita, testo incluso** — non solo lo sfondo. Ci vanno
scena, atmosfera, luce, palette, stile, composizione, resa e nitidezza, **e il titolo scritto
lettera per lettera** con posizione, carattere ed effetti, più il nome dell'autore.

Gael lo usa sul suo modello di immagini e salva il PNG.

**Fatto quando**: c'è un `.png` reale, guardato e giudicato adeguato al genere, col titolo
leggibile anche in miniatura.

---

## STEP 6 — Assemblaggio e controllo *(automatico)*

```
python -m engine.kdp consegna <slug> --cover <percorso-copertina.png>
```

Il codice porta l'immagine a norma KDP (2:3, 1800×2700) **senza riscriverci sopra il titolo**:
l'ha già disegnato il modello seguendo il prompt. Se invece l'immagine arriva senza testo o
col titolo sbagliato, `--scrivi-titolo` lo stampa sopra con un font vero — rete di sicurezza,
non la norma.

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
python -m engine.kdp stato                     # elenco di tutti i libri in lavorazione
python -m engine.kdp stato <slug>     # a che punto è questo
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
