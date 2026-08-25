---
Type: TOOL
Status: Active
Tags: #kdp #libri #publishing #pipeline #arena #niche-finder
Created: 2026-08-23
Last updated: 2026-08-24
---

# Tool: Pipeline Produzione Libri KDP

## Overview
Motore reale (non simulato) che porta un libro da idea a pacchetto KDP pronto al
caricamento: ricerca nicchia → capitoli scritti in sessione → assemblaggio →
copertina → conteggio pagine verificato sul PDF impaginato. Nato dal fallimento
del vecchio "PIANO KDP 67" (LM Arena bloccato dai captcha sul testo lungo) — il
pezzo mancante non era un generatore automatico di testo, ma il ponte tra
capitoli scritti a mano in sessione e un motore di assemblaggio reale.

## Dettagli

**Percorso**: `engine/book_project.py` (un progetto = una cartella, capitoli come
file) + `SOP-SCRIVERE-UN-LIBRO.md` (7 step) + `niche_finder.py` (ricerca nicchie
Amazon reali: recensioni mediane, concorrenti deboli, prezzo medio, punteggio
motivato).

**Perché non usa LM Arena per il testo**: il captcha di Arena non è aggirabile
oltre il primo messaggio — un libro ne richiede 24+. Le copertine invece restano
su LM Arena (funzionano, nessun blocco lì). Il testo si scrive con Claude in
sessione diretta.

**3 bug reali dello stesso tipo trovati sul primo libro** (numeri dichiarati mai
verificati): copertina quadrata accettata perché si controllava solo il peso del
file (fix: proporzioni + risoluzione + adattamento automatico a 1800×2700); pagine
STIMATE (parole/300) invece che contate — dichiarava 115.5 pagine, il PDF reale ne
aveva 106 (fix: `conta_pagine_pdf()` sul PDF impaginato, quello che impagina KDP,
non una stima); PDF assente dal pacchetto finale (aggiunto).

**Sbloccato da**: cambio di approccio chiesto da Gael — "crea i flussi, dei SOP,
dividi in step" invece di inseguire l'automazione end-to-end del testo.

## Output reali (3 libri, 2026-08-08 → 08-20)
- [[Entity_The_Quiet_Hours_Libro_KDP]] — primo libro, 115 pagine reali + copertina (2026-08-08).
- [[Entity_The_Ninth_Winter_Libro_KDP]] — secondo libro, 34.897 parole/115 pagine (2026-08-17).
- [[Entity_The_Second_Hand_Spellbook_Libro_KDP]] — terzo libro, 38.110 parole/115 pagine,
  prova cronometrata del piano "un libro in mezz'ora" (2026-08-20).

## Evoluzione: tre tentativi di automazione falliti, poi il modello definitivo (2026-08-13→15)
Dopo il primo libro (8/8/2026), il progetto ha provato **tre volte** a far scrivere i libri
da un programma invece che da Claude in sessione — tutti e tre falliti:
1. **Workflow a 4 step su Claude CLI + Haiku** (13-14/08): il CLI risultò uno stub da
   500 byte mai installato davvero; una volta riparato, il wrapper batch `.cmd` di npm
   troncava i prompt multi-riga e faceva sparire silenziosamente `--model haiku` — si
   pagava il modello di default senza che nulla lo segnalasse, causa probabile del limite
   di spesa mensile saltato dopo poche chiamate.
2. **LM Arena via Playwright** (15/08): i log reali delle uniche sessioni in cui questo
   progetto aveva davvero parlato con Arena mostravano il capitolo 1 in captcha
   **4 volte consecutive**, anche col pattern anti-captcha "chat nuova a ogni richiesta"
   già in produzione.
3. **Di nuovo LM Arena**, costruito un secondo giro completo (Fase 0 di misura del profilo
   browser reale) — fermato prima di lanciarlo, rileggendo i log del tentativo precedente.

**Decisione finale di Gael (15/08, verbatim)**: *"quando usi Python ti costringi per forza
ad utilizzare le API e non puoi più utilizzare te stesso... tu devi farlo tu, è un workflow
per te."* Il codice smette di chiamare modelli e diventa **attrezzatura**: misura, impagina,
conta, blocca — non genera mai testo. Le tre automazioni fallite sono state archiviate con
`git mv` in `_archivio_automazione_modelli/` (storia preservata, ADR-003: niente cancellato).
La copertina resta un prompt lunghissimo scritto da Claude e generato da Gael (mai Canva,
correzione esplicita di Gael) — `--scrivi-titolo` disattivato di default per non
sovrascrivere un titolo già disegnato dal modello immagine.

## Due bug di calibrazione scoperti producendo libri veri
- **320 parole/pagina, non 300** (17/08): la regola scritta "~1500 parole/capitolo" produceva
  libri reali sotto le 115 pagine minime KDP (misurato su due libri impaginati veri:
  324 e 320 parole/pagina). Corretto a **~1650 parole/capitolo**, verificando la media dopo
  il primo blocco di 4-6 capitoli, non a fine libro.
- **Il rapporto parole/pagina dipende dallo stile** (20/08, terzo libro): anche 320 può
  sforare — la regola finale è generare il PDF reale prima della consegna per tarare il
  rapporto vero di quel libro specifico, non fidarsi ciecamente della stima.

## Regola "niente lineette lunghe" (18/08, Gael)
Le lineette `—`/`–`/`--` sono la firma più riconoscibile della scrittura automatica.
`valida_lineette()` è ora un controllo **bloccante**: guarda solo la narrazione (esclude
trattini di parole composte inglesi e lineette nel discorso diretto per parole tagliate a
metà). Applicata a mano su 193 righe dei primi due libri.

## Piano "un libro in mezz'ora" (19-20/08)
6 checkpoint su 7 verificati con misure reali prima della prova cronometrata: bersaglio
pagine al centro della finestra (non al minimo), `gate_blocco.py` (0,06s, nessun PDF/OCR)
lanciabile dopo ogni gruppo di capitoli, riassunti a formato fisso con lista "fili aperti",
copertina consegnata in Fase 3. La prova reale (CP-7, terzo libro) ha impiegato 48 minuti
non 30 — vedi [[Entity_The_Second_Hand_Spellbook_Libro_KDP]] per il dettaglio del perché.

## Come Impatta DE
Sblocca l'ecosistema Publishing (KDP) come revenue stream ripetibile: tre libri prodotti
con la stessa pipeline, ogni bug di calibrazione trovato su un libro si applica
automaticamente al successivo (320 parole/pagina, niente lineette, gate di blocco veloce).

## 2026-08-25 — Il ciclo si chiude end-to-end (TASK-KDP-W1)

Fino a oggi la pipeline produceva un libro, ma i **tre output non arrivavano mai insieme**:
il manoscritto stava in `libri_pronti/`, il prompt della copertina restava in
`in_lavorazione/` e non entrava mai nel pacchetto, e il copy Amazon non aveva **nessun
comando** che lo scrivesse. `salva_copy()` esisteva dal 2026-08-15 ma nel flusso vivo non lo
chiamava nessuno: nei primi tre libri il copy è stato messo **a mano dentro `progetto.json`**,
senza validazione al momento della scrittura. È così che sono passate le lineette lunghe nelle
descrizioni di due libri **già consegnati**.

Tre buchi chiusi e due comandi nuovi:
- `kdp copy <slug> --file copy.json` — valida **prima** di salvare (campi obbligatori +
  `valida_copy_kdp`), e se sbaglia non scrive niente. Il difetto si ferma dove nasce.
- **La cartella finale nasce anche senza il .png**: prima `create_book_package` alzava
  `FileNotFoundError` e senza copertina non esisteva alcun pacchetto. Ora il libro non è
  comunque pubblicabile, ma lo dice `validazione.json` con un bloccante esplicito
  "Copertina assente", invece di sparire in silenzio.
- `COPERTINA-PROMPT.md` entra **sempre** nel pacchetto.
- `kdp pacchetto <slug>` — verificatore: **COMPLETO** (tre artefatti, exit 0) contro
  **CARICABILE SU KDP** (c'è anche l'immagine).

Prova reale: **"The Winter Term"** (dark academia mystery), 24/24 capitoli, 39.668 parole,
**116 pagine reali sul PDF**, 43,2 minuti. 135 test verdi (erano 127).

Due conferme di calibrazione: il gate di blocco ha bocciato **2 volte su 7** per capitoli
scritti corti (1.440 e 1.467 parole contro il bersaglio 1.600), e la stima a 320 parole/pagina
ha sbagliato di nuovo (120,9 stimate contro **113 reali** alla prima consegna). Solo il PDF conta.

## Connessioni
- [[Entity_The_Quiet_Hours_Libro_KDP]]
- [[Entity_The_Ninth_Winter_Libro_KDP]]
- [[Entity_The_Second_Hand_Spellbook_Libro_KDP]]
- [[projects/Piano_Maestro_EMPIRE_OS]]
- [[Reparto_Produzione_Digital_Empire]]

## Status
- First added: 2026-08-23 (backfill del buco wiki 06→22 agosto, lavoro reale del 2026-08-05/08)
- Aggiornato: 2026-08-24 (backfill storico esteso 06-08/2026, permesso esplicito Max) —
  evoluzione del modello di scrittura (3 tentativi automazione falliti → Claude in sessione),
  libro 2 e 3, calibrazione 320 parole/pagina, regola niente lineette, piano "mezz'ora"
- Confidence: Alta — verificato con esecuzione reale, checkpoint CP-20260805-001,
  CP-20260806-004, CP-20260808-002, CP-20260814-001, CP-20260814-002, CP-20260815-002,
  CP-20260817-001, CP-20260817-002, CP-20260818-002, CP-20260819-002, CP-20260819-003,
  CP-20260820-001
