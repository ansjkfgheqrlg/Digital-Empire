# Architettura del workflow libri KDP

**Aggiornato: 2026-08-23.** Questo è il documento di riferimento del **codice**: cosa c'è,
come è diviso, chi controlla cosa. La **procedura** (come si scrive un libro) sta in un solo
posto, [`.claude/skills/libro/SKILL.md`](.claude/skills/libro/SKILL.md), e qui non viene
ripetuta: era ripetuta in tre file e i tre file si erano messi a dire numeri diversi.

Se qualcosa qui non corrisponde al codice, **vince il codice** — e questo file va corretto.

---

## 1. Il principio, in una riga

**Il libro lo scrive Claude in sessione. Il codice non chiama nessun modello: misura,
impagina, conta, valida, impacchetta.**

Perché è così: il progetto ha provato **tre volte** a far scrivere i libri a un programma
(LM Arena via browser ×2, CLI di Claude con Haiku). Tutte e tre le volte è fallito — captcha,
prompt troncati, limite di spesa — e **nessuno dei tre tentativi ha mai prodotto un libro
finito**. I libri completi usciti da qui sono stati scritti in sessione. Quel codice non è
stato cancellato: sta in `_archivio_automazione_modelli/`, con un LEGGIMI.

---

## 2. Chi fa cosa

Non ci sono "agenti software" che si parlano fra loro: sarebbe una finzione, e su questo
progetto è già stata costruita una volta (95+ agenti, controllati, trovati a **zero**
automazione reale — sono in `_archivio_blueprint_narrativo/`).

Gli attori veri sono tre, e ogni fase ha **un esecutore** e **un controllore**:

| Attore | Cos'è | Cosa fa |
|---|---|---|
| **Claude** | l'assistente in sessione | ricerca, sceglie gli argomenti, scrive outline, capitoli, prompt copertina, copy |
| **L'attrezzatura** (`engine/`) | codice Python deterministico | misura le nicchie, impagina, conta le pagine vere, valida, impacchetta |
| **Gael** | la persona | genera l'immagine di copertina, carica su KDP |

**I "controllori" sono funzioni Python che bloccano davvero.** Non sono consigli: se un
controllo fallisce, il comando esce con un codice di errore e il libro non passa. È l'unico
tipo di controllo che vale, perché non dipende dal fatto che chi scrive si ricordi la regola.

> **E un controllo che non è potuto girare non è un controllo passato** (2026-08-23). Se
> manca lo strumento (Word per il PDF, Tesseract per l'OCR), l'esito finisce in
> `verifiche_non_eseguite` dentro `validazione.json`, non fra gli avvisi. Prima un
> pacchetto poteva uscire `pubblicabile: true` con **zero** dei tre controlli pesanti
> eseguiti, e dal verdetto non si vedeva.

---

## 3. Il flusso, fase per fase

Otto fasi. La 0 si fa una volta a settimana, le altre una volta per libro.

```
   FASE 0  Magazzino argomenti        (1 volta a settimana → 7 argomenti)
      │
      ▼
   FASE 1  Progetto                   ┐
   FASE 2  Outline                    │
   FASE 3  Prompt copertina           │
   FASE 4  Capitoli  ←──── il grosso  ├─ 1 volta per libro
   FASE 5  Copertina (Gael)           │
   FASE 6  Consegna                   │
   FASE 7  Pubblicato (dopo KDP)      ┘
```

| Fase | Esegue | Controlla, e blocca | Comando |
|---|---|---|---|
| 0 | Claude cerca le nicchie | `magazzino.valida_argomento` + `story_validator` | `kdp nicchie`, `kdp magazzino --aggiungi` |
| 1 | il codice crea la cartella | `BookProject.crea` (progetto già esistente) + **disciplina di nicchia** | `kdp nuovo` |
| 2 | **Claude** scrive `outline.md` | `kdp.estrai_titolo` (titolo leggibile) | — |
| 3 | **Claude** scrive `copertina-prompt.md` | Gael, guardando l'immagine | — |
| 4 | **Claude** scrive i capitoli | **`gate_blocco.controlla`** dopo ogni blocco | `kdp blocco <slug>` |
| 5 | **Gael** genera il PNG | `copertina_kdp.verifica_copertina_kdp` | — |
| 6 | il codice impagina e impacchetta | **10 controllori** (sotto) | `kdp consegna <slug> --cover` |
| 7 | il codice archivia | `pubblicazione` rifiuta un libro non pubblicabile | `kdp pubblicato <slug> --asin` |

### FASE 1 — la disciplina di nicchia *(2026-08-23)*

`kdp nuovo` **rifiuta** un libro in una nicchia diversa da quella attiva del catalogo, a meno
di `--motivo "<perché>"`, che resta scritto nel progetto.

Serviva: `nicchia_attiva.py` esisteva da 12 giorni, 251 righe con storico e soglia di cambio,
e i primi tre libri sono usciti in **tre nicchie diverse, nessuna delle quali era quella
attiva**. Il controllo c'era e nessun percorso di codice lo interrogava. Su KDP quello che
vende il primo libro è il secondo libro dello stesso autore nella stessa nicchia.

### FASE 4 — il gate rapido

`kdp blocco <slug>` gira in **meno di un secondo** (niente PDF, niente OCR) e guarda: dove
atterra il libro a questo ritmo, lineette, capitoli troncati, riassunti aggiornati, fili
aperti da troppo, **capitoli che si ripetono**. Trovare "sto scrivendo corto" al capitolo 8
costa 8 capitoli; al capitolo 24 ne costa 24.

### FASE 6 — i dieci controllori della consegna

I bloccanti sono in `book_project.GRAVITA_ESITI`, che è una **tabella**, non un confronto fra
stringhe: prima la gravità dipendeva da come era scritta l'etichetta del controllo.

| # | Controllore | Cosa verifica | Blocca? |
|---|---|---|---|
| 1 | `BookProject.stato()` | tutti i capitoli ci sono | **sì** |
| 2 | `kdp_formatter.count_words_and_pages()` | parole entro il target (**paratesto escluso**) | **sì** |
| 3 | `book_output_manager.conta_pagine_pdf()` | **pagine vere dal PDF** ≥ 115 — e `None` blocca | **sì** |
| 4 | `validators.valida_copertina_testo()` | il titolo è leggibile (OCR) | **sì** |
| 5 | `validators.valida_lineette()` | nessuna lineetta lunga nella narrazione | **sì** |
| 6 | `validators.valida_troncamento()` | nessun capitolo interrotto a metà frase | **sì** |
| 7 | `validators.valida_ripetizioni()` | **nessun capitolo quasi identico a un altro** | **sì** |
| 8 | `validators.valida_copy_kdp()` | **niente lineette e limiti KDP nel copy** | **sì** |
| 9 | `BookProject._controlla_epub()` | l'EPUB contiene lo stesso libro del .docx | **sì** |
| 10 | `validators.valida_prezzo()` | il prezzo sta vicino alla media misurata | no, segnala |
| + | `valida_numerazione_pagine`, `valida_sillabazione_pdf`, `valida_trattini` | rifiniture sul PDF e sul testo | no, segnalano |

> **Il 3 esiste per un bug ripetuto due volte**: il vecchio workflow dichiarava "120 pagine"
> e il PDF ne aveva 21. Ora le pagine si contano rileggendo il PDF impaginato. **E dal
> 2026-08-23 `None` blocca**: la condizione era `if pagine_reali and pagine_reali < minimo`,
> quindi un PDF non prodotto faceva sparire il controllo e il libro usciva pubblicabile
> senza che nessuno avesse contato una pagina.
>
> **Il 7 esiste** perché "mai un capitolo identico o quasi a un altro" era l'unica delle sei
> regole non negoziabili senza nessuna funzione che la facesse rispettare. Le soglie sono
> misurate sui 72 capitoli veri: massimo legittimo 2,7%, un capitolo ricopiato a metà dà
> 98,8%, si blocca al 15%.
>
> **L'8 esiste** perché la regola sulle lineette girava solo sui capitoli, e nei pacchetti
> già consegnati c'erano **3 lineette nella descrizione di The Ninth Winter e 2 in quella di
> The Quiet Hours** — cioè nel testo che il compratore legge prima di comprare.

Il verdetto finale sta in `validazione.json` (`pubblicabile`, `pagine_reali`, `bloccanti`,
`verifiche_non_eseguite`, `avvisi`) e in `REPORT.md`.

### FASE 7 — pubblicato

`kdp pubblicato <slug> --asin B0…` copia i sorgenti dentro il pacchetto, **li verifica byte
per byte**, sposta il pacchetto in `libri_pubblicati/`, scrive `pubblicazione.json` con
ASIN e prezzo, registra il libro sulla nicchia, chiude l'argomento in magazzino e solo allora
cancella la cartella di lavorazione.

Serviva: "sposta la cartella a mano quando pubblichi" era scritto in tre documenti ed è
l'unico passo del flusso **mai eseguito** dopo tre libri finiti — con 23 MB di doppioni e
nessuna traccia dell'ASIN.

---

## 4. Cosa produce un libro finito

```
LIBRI/libri_pronti/<Titolo>/
├── <Titolo>.docx           manoscritto KDP 6×9, margini specchio, numeri di pagina
├── <Titolo>.pdf            quello che si legge e da cui si contano le pagine vere
├── <Titolo>.epub           l'ebook (copertina alleggerita: su Kindle si paga a MB)
├── Cover_<Titolo>.png      copertina 1800×2700 a norma
├── KDP_METADATA.txt        titolo, descrizione, keyword, BISAC, bio, prezzo + media nicchia
├── ISPIRAZIONE.json/.txt   da dove nasce il libro, coi numeri veri della nicchia
├── REPORT.md               cosa è stato verificato
└── validazione.json        il verdetto, e su quale numero di pagine è stato dato
```

Dentro il libro ci sono anche le pagine che non sono il romanzo (`engine/paratesto.py`):
**copyright** davanti, **richiesta di recensione**, **"Also by"** e **bio** in fondo. Non
contano nel conteggio parole — hanno uno stile dedicato proprio per poterle escludere.

---

## 5. `engine/` — 21 moduli, nessuno chiama un modello

**Il punto d'ingresso**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `kdp.py` | 558 | **La CLI.** Tutti i comandi passano da qui |

**Il libro**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `book_project.py` | 744 | Un progetto = una cartella. Stato, assemblaggio, orchestrazione dei controlli |
| `kdp_formatter.py` | 280 | Il `.docx` KDP: 6×9in, margini specchio, numeri di pagina, paratesto |
| `epub.py` | 280 | L'**ebook**. Solo `zipfile`: nessuna dipendenza esterna |
| `paratesto.py` | 155 | Copyright, richiesta di recensione, "Also by", bio |
| `book_output_manager.py` | 243 | Pacchetto finale, PDF, **conta le pagine vere** |
| `book_report.py` | 151 | Scrive `REPORT.md` |
| `pubblicazione.py` | 209 | Archivia un libro pubblicato, con ASIN, e toglie i doppioni |

**I controlli**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `validators.py` | 623 | Lineette, troncamento, **ripetizioni**, **copy KDP**, **prezzo**, sillabazione, numerazione, OCR copertina |
| `gate_blocco.py` | 176 | Il gate rapido di fase 4, sotto il secondo |
| `report_validazione.py` | 95 | Un verdetto solo, con la quarta categoria: **non verificato** |
| `story_validator.py` | 90 | GO/NO-GO: è una storia o è un diario? Solo keyword |

**La ricerca** *(gli unici che aprono un browser — su Amazon, per misurare)*

| Modulo | Righe | Cosa fa |
|---|---|---|
| `niche_finder.py` | 217 | Punteggio 0-100 di una nicchia da dati Amazon veri |
| `amazon_research.py` | 159 | Legge i risultati reali di Amazon. Se fallisce ritorna vuoto, **mai dati inventati** |
| `session_manager.py` | 187 | La sessione Amazon salvata |
| `nicchia_attiva.py` | 251 | La nicchia del catalogo: si sceglie **una volta**, si cambia solo con margine |
| `magazzino.py` | 179 | Gli argomenti pronti (Fase 0) |
| `ispirazione.py` | 185 | La scheda "da dove nasce questo libro", coi numeri della nicchia |

**Contorno**

| Modulo | Righe | Cosa fa |
|---|---|---|
| `copertina_kdp.py` | 216 | Porta a norma KDP il PNG di Gael. Solo Pillow |
| `metriche.py` | 132 | Quanto è costato davvero fare il libro: tempo, bocciature, riconsegne |
| `config.py` | 142 | Costanti: trim 6×9, margini, target pagine, keyword GO/NO-GO |

### Come dipendono l'uno dall'altro

```
kdp.py ──┬─→ magazzino ──→ story_validator
         ├─→ nicchia_attiva ──→ niche_finder ──→ amazon_research ──→ session_manager
         ├─→ copertina_kdp
         ├─→ metriche
         ├─→ pubblicazione ──→ book_project, magazzino, nicchia_attiva
         └─→ book_project ──┬─→ kdp_formatter ──→ paratesto
                            ├─→ epub
                            ├─→ book_output_manager
                            ├─→ validators
                            ├─→ report_validazione
                            ├─→ ispirazione
                            └─→ book_report
                    tutti ──→ config
```

Nessuna freccia esce verso un modello: `grep -rn "lmarena\|openai\|anthropic" engine/` non
trova niente di operativo. **È la prova che il principio è nel codice**, non solo dichiarato.

---

## 6. Dipendenze

`requirements.txt` elenca **tutto** quello che il codice importa (fino al 2026-08-23 ne
dichiarava 3 su 6, e su una macchina pulita `python -m engine.kdp stato` moriva subito).

Due programmi che pip **non** installa:

| | Serve a | Se manca |
|---|---|---|
| **Microsoft Word** | `docx2pdf` → il PDF | niente PDF ⇒ niente pagine vere ⇒ **la consegna blocca** |
| **Tesseract OCR** | `pytesseract` → titolo in copertina | il controllo finisce in `verifiche_non_eseguite`, non blocca |

---

## 7. Test

```
python -m pytest tests/ -q        # 127 test, ~4 secondi
```

Nessuno apre un browser, chiama un modello o pretende Word. Quasi ogni test riproduce un
errore realmente avvenuto qui.

---

## 8. Stato attuale *(2026-08-23)*

| Libro | Stato |
|---|---|
| `the-quiet-hours` | ✅ pacchetto completo, 118 pagine reali, PUBBLICABILE |
| `the-ninth-winter` | ✅ pacchetto completo, 119 pagine reali, PUBBLICABILE |
| `the-second-hand-spellbook` | ✅ pacchetto completo, 118 pagine reali, PUBBLICABILE |

Tutti e tre con `.docx` + PDF + **EPUB** + copertina a norma + copy pulito.
**Nessuno è ancora su KDP**: `libri_pubblicati/` è vuoto, e finché resta vuoto il collo di
bottiglia non è la produzione.

**Magazzino**: 3 argomenti, 2 liberi (dark academia mystery, cozy mystery bakery).
**Nicchia del catalogo**: `small town romance suspense` — **e nessuno dei tre libri è in
quella nicchia**. Da rivedere: o si cambia la nicchia attiva con `nicchia-confronta
--applica`, o i prossimi libri si scrivono lì dentro. Da oggi `kdp nuovo` non lascia più
divergere in silenzio.
