# Archivio — scrittura via Claude Code CLI (modello Haiku)

**Stato: NON ancora archiviato.** Questa cartella è preparata, ma
`engine/scrittore_haiku.py` e `tests/test_scrittore.py` sono **ancora al loro posto e
ancora il percorso di scrittura attivo**. Lo spostamento avviene solo dopo che il flusso
via LM Arena avrà prodotto un libro reale completo (vedi "Quando spostare" in fondo).

## Perché verrà archiviato

Decisione di Gael del 2026-08-14: la scrittura dei libri non deve passare da Claude
(né CLI né API). Si torna a LM Arena pilotato con Playwright, con un flusso a 5 fasi —
piano di produzione (sommario capitoli + prompt copertina) → capitoli uno alla volta in
modalità Direct/Max con staging su Google Doc → copertina dal prompt del piano → copy KDP
nella stessa chat dei capitoli.

Il sostituto è `engine/arena_book_writer.py`.

## Cosa NON va perso di questo modulo

`scrittore_haiku.py` non è codice sbagliato: è codice che ha funzionato e ha prodotto
libri reali. Contiene tre cose conquistate con bug veri, già portate nel sostituto — se
un giorno qualcuno tornasse su questo percorso, sono le stesse da riapplicare:

1. **Il wrapper `.cmd` di npm distrugge i prompt multiriga.** Su Windows `claude.CMD` è un
   batch che rilancia con `%*`, e cmd.exe tronca alla PRIMA RIGA qualunque argomento
   contenga un a capo, perdendo anche gli argomenti successivi. Misurato con una sonda su
   argv (stesso prompt di 11 righe): via `.CMD` arrivavano 2 argomenti su 4 e il prompt era
   la sola riga del ruolo; via `.exe` arrivava tutto. Conseguenza doppia e **silenziosa**:
   il modello riceveva un prompt mutilato *e* `--model haiku` non arrivava affatto, quindi
   si pagava il modello di default — l'esatto contrario della scelta economica del
   progetto, con il CLI che rispondeva "successo" a ogni chiamata.
2. **`claude -p` è un AGENTE, non un generatore di testo.** Lanciato con `cwd` dentro il
   repo risaliva l'albero, caricava i `CLAUDE.md` di Digital Empire e leggeva lo stato del
   disco, rispondendo da assistente ("riprendo The Ninth Winter o ne apro uno nuovo?")
   invece di scrivere. Va lanciato da una cartella neutra fuori dall'albero, con
   `--system-prompt` proprio e i tool negati.
3. **Il titolo placeholder.** Un parser rigido su `TITLE:` accettava in silenzio il titolo
   di lavoro quando il modello decorava la riga (`**TITLE:**`), producendo un libro
   chiamato "Untitled Small Town Romance Suspense 202608131759". La tolleranza alla
   decorazione markdown vive ora in `workflow.estrai_titolo`, riusata da
   `arena_book_writer._parse_piano` — resta viva, non si archivia.

Le soglie di validazione (minimo parole per capitolo, capitolo duplicato, numero di
tentativi) sono state riportate nel sostituto, dove la guardia anti-duplicato è la stessa
già presente nel vecchio percorso Arena.

## Quando spostare

Solo dopo che `arena_book_writer.py` avrà completato un libro reale end-to-end (piano →
capitoli → copertina → copy → pacchetto in `LIBRI/libri_pronti/`). Fino ad allora
`scrittore_haiku.py` resta il sistema attivo e intoccabile — ADR-003: il sostituto si
valida in parallelo, non si spegne un sistema che produce prima di avere la prova che il
nuovo funziona.

Da spostare insieme, quel giorno:
- `engine/scrittore_haiku.py`
- `tests/test_scrittore.py` (test specifici della meccanica CLI-Claude: wrapper batch, cwd
  neutra, limite di spesa — perdono significato una volta che la scrittura passa da Arena)

**Non** si spostano i test su `workflow.estrai_titolo`: quella funzione è agnostica su chi
genera il testo e resta in uso.
