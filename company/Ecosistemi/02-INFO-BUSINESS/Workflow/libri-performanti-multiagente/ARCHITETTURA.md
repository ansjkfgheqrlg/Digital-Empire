# Architettura del workflow libri KDP

**Aggiornato: 2026-08-15.** Questo è il documento di riferimento: cosa c'è, come è diviso,
chi fa cosa, e in che ordine. Se qualcosa qui non corrisponde al codice, vince il codice —
e questo file va corretto.

---

## 1. Il principio, in una riga

**Il libro lo scrive Claude in sessione. Il codice non chiama nessun modello: misura,
impagina, conta, valida, impacchetta.**

Perché è così: il progetto ha provato **tre volte** a far scrivere i libri a un programma
(LM Arena via browser ×2, CLI di Claude con Haiku). Tutte e tre le volte è fallito — captcha,
prompt troncati, limite di spesa — e **nessuno dei tre tentativi ha mai prodotto un libro
finito**. L'unico libro completo mai uscito da qui, *The Quiet Hours* (115 pagine reali), è
stato scritto in sessione. Quel codice non è stato cancellato: sta in
`_archivio_automazione_modelli/`, con un LEGGIMI che spiega cosa è successo.

---

## 2. Chi fa cosa

Non ci sono "agenti software" che si parlano fra loro: sarebbe una finzione, e su questo
progetto è già stata costruita una volta (95+ agenti, controllati, trovati a **zero**
automazione reale — sono in `_archivio_blueprint_narrativo/`).

Gli attori veri sono tre, e ogni fase ha **un esecutore** e **un controllore**:

| Attore | Cos'è | Cosa fa |
|---|---|---|
| **Claude** (io) | l'assistente in sessione | ricerca, sceglie gli argomenti, scrive outline, capitoli, prompt copertina, copy |
| **L'attrezzatura** (`engine/`) | codice Python deterministico | misura le nicchie, impagina, conta le pagine vere, valida, impacchetta |
| **Gael** | la persona | genera l'immagine di copertina, carica su KDP |

**I "controllori" sono funzioni Python che bloccano davvero.** Non sono consigli: se un
controllo fallisce, il comando esce con un codice di errore e il libro non passa. È l'unico
tipo di controllo che vale, perché non dipende dal fatto che io mi ricordi una regola.

---

## 3. Il flusso, fase per fase

Sette fasi. La 0 si fa una volta a settimana, le altre una volta per libro.

```
   FASE 0  Magazzino argomenti        (1 volta a settimana → 7 argomenti)
      │
      ▼
   FASE 1  Progetto                   ┐
   FASE 2  Outline                    │
   FASE 3  Prompt copertina           ├─ 1 volta per libro
   FASE 4  Capitoli  ←──── il grosso  │
   FASE 5  Copertina (Gael)           │
   FASE 6  Consegna                   ┘
      │
      ▼
   Pubblicazione (Gael, a mano)
```

---

### FASE 0 — Magazzino argomenti · *settimanale*

Serve a pagare la fase di giudizio **una volta sola** e avere una settimana di libri pronti.
Gael la chiama "flusso atemporale".

| | |
|---|---|
| **Esegue** | Claude: cerca sul web le nicchie che vendono |
| **Controlla** | `magazzino.valida_argomento()` + `story_validator.validate()` |
| **Comando** | `kdp nicchie --keywords "..."` poi `kdp magazzino --aggiungi f.json` |
| **Produce** | `LIBRI/magazzino_argomenti.json` — 7 argomenti |

**Cosa blocca il controllore**, e non è aggirabile:
- un argomento **senza dati Amazon veri** non entra ("mi sembra una buona nicchia" non basta)
- un argomento che **non è una storia** non entra (diari, planner, journal, tracker)
- un **duplicato** non entra due volte

> Provato dal vivo: su 4 argomenti proposti ne sono entrati 2. Respinti un planner e uno
> senza numeri.

---

### FASE 1 — Progetto · *per libro*

| | |
|---|---|
| **Esegue** | `kdp magazzino --prendi` poi `kdp nuovo "<Titolo>" --nicchia "<n>"` |
| **Controlla** | `BookProject.crea()` — rifiuta se il progetto esiste già |
| **Produce** | la cartella `LIBRI/in_lavorazione/<slug>/` |

---

### FASE 2 — Outline · *per libro*

| | |
|---|---|
| **Esegue** | **Claude**: scrive `outline.md` |
| **Controlla** | `kdp.estrai_titolo()` verifica che il titolo sia leggibile |
| **Produce** | `outline.md` |

Deve contenere tutti e quattro: **titolo definitivo**, **personaggi** (nome, età, ruolo, cosa
vuole), **trama in 3 atti**, **scaletta dei 24 capitoli** (una riga ciascuno).

> Se l'outline è vago, il libro va in contraddizione al capitolo 12. È già successo.

---

### FASE 3 — Prompt copertina · *per libro*

| | |
|---|---|
| **Esegue** | **Claude**: scrive `copertina-prompt.md` |
| **Controlla** | Gael, guardando l'immagine che ne esce |
| **Produce** | `copertina-prompt.md` |

Il prompt descrive **tutta la copertina finita, testo incluso** — non solo lo sfondo:
formato 2:3, scena e soggetto, atmosfera e luce, palette, stile e nitidezza, composizione
(dove resta spazio per il titolo), **il titolo lettera per lettera** con carattere, posizione
ed effetti, il nome dell'autore, e cosa NON deve esserci.

---

### FASE 4 — Capitoli · *per libro, è il grosso del lavoro*

| | |
|---|---|
| **Esegue** | **Claude**: scrive `capitoli/cap_NN.md`, 4-6 per volta |
| **Controlla** | `kdp stato <slug>` — capitoli, parole, pagine stimate |
| **Produce** | 24 file di capitolo + `riassunti.md` aggiornato |

**Regole di lavoro:**
- **4-6 capitoli per volta**, mai tutti insieme: la qualità cala
- **~1650 parole a capitolo** (24 × 1650 = 39.600 = ~124 pagine reali). **Non 1500**:
  36.000 parole impaginate fanno 112 pagine, sotto il minimo di 115 — vedi la nota sulle
  320 parole/pagina più sotto
- **la lunghezza si controlla al primo blocco**, non a fine libro
- **dopo ogni blocco** aggiorno `riassunti.md` (2-3 righe per capitolo)
- **prima di ogni blocco** rileggo `outline.md` + `riassunti.md`

> **La coerenza viene dai file, non dalla memoria della sessione.** Se `riassunti.md` non è
> aggiornato, il capitolo 9 non sa cosa è successo nei primi 8 — e nessun controllo
> automatico se ne accorge.

---

### FASE 5 — Copertina · *Gael*

| | |
|---|---|
| **Esegue** | **Gael**: usa il prompt della Fase 3 sul suo modello di immagini |
| **Controlla** | `copertina_kdp.verifica_copertina_kdp()` — proporzioni e risoluzione |
| **Produce** | un file `.png` |

Il codice poi lo porta a norma KDP: ritaglio 2:3, upscale a 1800×2700 (6×9in @300dpi).

> **Il titolo NON viene riscritto sopra**: l'ha già disegnato il modello seguendo il prompt.
> Riscriverlo lo farebbe comparire due volte. Se invece l'immagine arriva senza testo o col
> titolo sbagliato, `--scrivi-titolo` lo stampa con un font vero — è la rete di sicurezza,
> non la norma.

---

### FASE 6 — Consegna · *automatico*

| | |
|---|---|
| **Esegue** | `kdp consegna <slug>` — con `--cover <png>` fa anche il pacchetto |
| **Controlla** | 6 controllori in fila (sotto) |
| **Produce** | **sempre** il `.docx` e il **PDF** nella cartella del libro; con la copertina anche `LIBRI/libri_pronti/<Titolo>/` |

> **Il PDF si fa sempre, anche senza copertina** (2026-08-17). Non è comodità: è l'unico
> posto dove si vede il numero di pagine vero. Aspettare la copertina per scoprirlo
> significa scoprirlo troppo tardi.

**I sei controllori, in ordine.** I primi tre **bloccano**, gli altri segnalano:

| # | Controllore | Cosa verifica | Blocca? |
|---|---|---|---|
| 1 | `BookProject.stato()` | tutti i capitoli ci sono | **sì** |
| 2 | `kdp_formatter.count_words_and_pages()` | parole entro il target | **sì** |
| 3 | `book_output_manager.conta_pagine_pdf()` | **pagine vere lette dal PDF** ≥ 115 | **sì** |
| 4 | `validators.valida_copertina_testo()` | il titolo è leggibile (OCR) | **sì** |
| 5 | `validators.valida_lineette()` | **nessuna lineetta lunga `—` `–` `--`** | **sì** |
| 6 | `validators.valida_numerazione_pagine()` | numeri sempre in alto o sempre in basso | no, segnala |
| 7 | `validators.valida_sillabazione_pdf()` | parole spezzate a fine riga | no, segnala |

> Il controllo 5 è una regola di Gael (2026-08-18): le lineette lunghe sono la firma più
> riconoscibile della scrittura automatica, e su Amazon "sembra scritto dall'AI" è la
> recensione che affonda un titolo. Si tolgono **riscrivendo la frase**, non scambiando il
> segno. I trattini delle parole composte (`twenty-nine`, `hand-lettered`) **restano**: in
> inglese sono ortografia, e li tratta il controllo 7, che segnala e non blocca.

> Il controllo 3 esiste per un bug reale ripetuto due volte: il vecchio workflow dichiarava
> "120 pagine" e il PDF ne aveva 21. Ora le pagine si **contano rileggendo il PDF impaginato**,
> quello che vedrà KDP.
>
> **E il controllo 2 non sostituisce il 3.** La stima parole→pagine è tarata su
> `WORDS_PER_PAGE_ESTIMATE`, che valeva 300 ed era sbagliato: misurato su due libri veri
> impaginati, il rapporto è **320** (*The Quiet Hours* 324, *The Ninth Winter* 320). A 300 la
> stima gonfiava le pagine del 6% — nella direzione pericolosa. *The Ninth Winter* è passato
> dal controllo 2 con 34.897 parole ("116,3 pagine") ed è arrivato al PDF con **111 pagine
> reali**. Costante corretta a 320 il 2026-08-17; il minimo parole è ora 36.800.

Il verdetto finale sta in `validazione.json` (`pubblicabile: true/false`) e in `REPORT.md`.

---

## 4. La struttura dei file

### Radice

| File / cartella | Cos'è |
|---|---|
| `ARCHITETTURA.md` | **questo file** |
| `SOP-SCRIVERE-UN-LIBRO.md` | la procedura in 7 step, per una persona |
| `.claude/skills/libro/SKILL.md` | la stessa procedura, che eseguo io con `/libro` |
| `engine/` | l'attrezzatura Python |
| `tests/` | 38 test, nessuno apre un browser o chiama un modello |
| `LIBRI/` | i libri e lo stato |
| `sessions/` | sessione Amazon salvata (gitignored) |
| `_archivio_automazione_modelli/` | i 3 tentativi falliti di automazione + LEGGIMI |
| `_archivio_blueprint_narrativo/` | l'architettura a 95+ agenti finti, archiviata |
| `PIANO-KDP-67.md`, `PIANO-KDP-V2-CLAUDE-CODE.md` | cronaca storica dei piani precedenti |

### `engine/` — 16 moduli, nessuno chiama un modello

**Il punto d'ingresso**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `kdp.py` | 407 | **La CLI che uso io.** Tutti i comandi passano da qui |

**Il libro**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `book_project.py` | 476 | Un progetto = una cartella. Stato, assemblaggio, orchestrazione dei controlli |
| `kdp_formatter.py` | 215 | Costruisce il `.docx` KDP: 6×9in, margini specchio, numeri di pagina |
| `book_output_manager.py` | 211 | Pacchetto finale, PDF, **conta le pagine vere** |
| `book_report.py` | 151 | Scrive `REPORT.md` |

**I controlli**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `validators.py` | 260 | Trattini, sillabazione nel PDF, numerazione, titolo in copertina (OCR) |
| `report_validazione.py` | 69 | Raccoglie gli esiti e dà **un** verdetto: pubblicabile sì/no |
| `story_validator.py` | 90 | GO/NO-GO: è una storia o è un diario? Nessun modello, solo keyword |

**La ricerca** *(gli unici che aprono un browser — su Amazon, per misurare)*

| Modulo | Righe | Cosa fa |
|---|---|---|
| `niche_finder.py` | 217 | Punteggio 0-100 di una nicchia da dati Amazon veri |
| `amazon_research.py` | 159 | Legge i risultati reali di Amazon. Se fallisce ritorna vuoto, **mai dati inventati** |
| `session_manager.py` | 187 | La sessione Amazon salvata |
| `nicchia_attiva.py` | 251 | La nicchia del catalogo: si sceglie **una volta**, si cambia solo con margine |
| `magazzino.py` | 179 | Gli argomenti pronti (Fase 0) |

**La copertina e la configurazione**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `copertina_kdp.py` | 216 | Porta a norma KDP il PNG che genera Gael. Solo Pillow, nessun browser |
| `config.py` | 126 | Costanti: trim 6×9, margini, target pagine, keyword GO/NO-GO |

### Come dipendono l'uno dall'altro

```
kdp.py ──┬─→ magazzino ──→ story_validator
         ├─→ nicchia_attiva ──→ niche_finder ──→ amazon_research ──→ session_manager
         ├─→ copertina_kdp                                    └──→ story_validator
         └─→ book_project ──┬─→ kdp_formatter
                            ├─→ book_output_manager
                            ├─→ validators
                            ├─→ report_validazione
                            └─→ book_report

                    tutti ──→ config
```

Nessuna freccia esce verso un modello. **È la prova che il principio è nel codice**, non solo
dichiarato: `grep -rn "lmarena\|api\|openai" engine/` non trova niente di operativo.

### `LIBRI/` — dove vivono i libri

```
LIBRI/
├── magazzino_argomenti.json     gli argomenti pronti (Fase 0)
├── nicchia_attiva.json          la nicchia del catalogo + storico
├── in_lavorazione/<slug>/       un libro in scrittura
│   ├── progetto.json            titolo, autore, nicchia, capitoli, parole target
│   ├── outline.md               la mappa (Fase 2)
│   ├── copertina-prompt.md      il prompt per Gael (Fase 3)
│   ├── capitoli/cap_NN.md       un file per capitolo (Fase 4)
│   └── riassunti.md             la memoria del libro
├── libri_pronti/<Titolo>/       il pacchetto finito
│   ├── <Titolo>.docx            manoscritto KDP
│   ├── <Titolo>.pdf             quello che si legge e si controlla
│   ├── Cover_<Titolo>.png       copertina a norma
│   ├── KDP_METADATA.txt         titolo, descrizione, keyword, categorie
│   ├── REPORT.md                cosa è stato verificato
│   └── validazione.json         il verdetto
└── libri_pubblicati/            ci si sposta a mano dopo il caricamento
```

---

## 5. Tutti i comandi

```bash
# FASE 0 — magazzino
python -m engine.kdp nicchie --keywords "cozy mystery cats" "small town romance"
python -m engine.kdp magazzino                        # cosa c'è di pronto
python -m engine.kdp magazzino --aggiungi f.json      # inserisce la ricerca
python -m engine.kdp magazzino --prendi               # il prossimo da scrivere

# nicchia del catalogo
python -m engine.kdp nicchia-stato
python -m engine.kdp nicchia-confronta --keywords "..." [--applica]

# FASI 1-4 — il libro
python -m engine.kdp nuovo "<Titolo>" --nicchia "<nicchia>"
python -m engine.kdp stato [slug]

# FASE 6 — consegna
python -m engine.kdp consegna <slug> --cover <png> [--scrivi-titolo] [--forza]
```

**Exit code**, uguali per tutti i comandi: `0` ok · `1` non pubblicabile · `2` parametri
sbagliati · `3` errore di sistema.

---

## 6. Le regole non negoziabili

1. **Mai dichiarare finito un libro sotto le 115 pagine reali.** Il controllo blocca da solo.
   `--forza` serve per ispezionare una bozza, **mai** per consegnare.
2. **Mai un capitolo identico o quasi a un altro.** Se succede è un errore di processo.
3. **Mai copiare da un concorrente.** La ricerca serve a capire il mercato, non i testi.
4. **La coerenza viene da `outline.md` + `riassunti.md`**, non dalla memoria della sessione.
5. **Il codice non chiama modelli.** Se una modifica lo reintroduce, è un passo indietro
   verso tre fallimenti già pagati.
6. **Un libro incompleto si finisce prima di aprirne un altro.** Un catalogo si costruisce
   con libri finiti, non con bozze.

---

## 7. Stato attuale

| Libro | Stato |
|---|---|
| `the-quiet-hours` | ✅ finito, 24/24 capitoli, 37.297 parole — pacchetto in `libri_pronti/` |
| `the-ninth-winter` | ⚠️ **8/24 capitoli**, 8.395 parole (~1.040 a capitolo, sotto il target di 1.500). `riassunti.md` **mai aggiornato** |

**Nicchia del catalogo**: `small town romance suspense` — 77.4/100, sana.
**Magazzino**: vuoto, va riempito.

> Su `the-ninth-winter`: prima di scrivere il capitolo 9 vanno **ricostruiti i riassunti**
> rileggendo i capitoli esistenti. E i capitoli sono corti: se il conto finale resta sotto le
> 115 pagine servono capitoli più lunghi o più capitoli — lo dice `kdp stato`.
