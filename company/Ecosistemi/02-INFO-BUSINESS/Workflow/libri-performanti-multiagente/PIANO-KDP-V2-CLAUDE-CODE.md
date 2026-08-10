# PIANO KDP V2 — Libri scritti da Claude Code, copertine da LM Arena

**Creato:** 2026-08-07 · **Owner:** Gael · **Stato:** 🔴 DA INIZIARE
**Sostituisce** la parte "scrittura testo" di [PIANO-KDP-67.md](PIANO-KDP-67.md) (CP4/CP5).
Il resto di quel piano (CP0-CP3, CP6, CP8, CP9, CP11) resta valido e già costruito.

## Decisione presa da Gael (2026-08-07)

> "lascia stare LM arena e il playwright, usa claude code, cambia tutto il workflow,
> lmArena servirà solo per le copertine, e quello funziona già, i libri completi falli
> internamente con claude code, cercando di usare il minor numero di crediti possibili
> durante la scrittura. [...] alla fine del piano il flusso dovrà essere perfettamente
> funzionante e nell'app aureus dovrà esserci nella sezione automazioni [...] anche il
> tasto di avvio di outreach."

**Perché**: due giorni di lavoro reale hanno dimostrato che LM Arena via Playwright non
regge una generazione lunga in serie — il captcha "Security Verification" scatta dopo poche
richieste per sessione, anche con profilo persistente, chat nuove e pause fra gli invii
(tutto verificato dal vivo, vedi cronaca in PIANO-KDP-67.md). Non è aggirabile e non va
aggirato. Le COPERTINE invece funzionano (una sola richiesta per libro, nessun captcha):
quel pezzo resta com'è, già verificato con immagini reali.

**Nota onesta**: questo ROVESCIA il vincolo fondante del piano originale ("zero dipendenza
da crediti Claude Code"). È una scelta consapevole di Gael dopo aver visto i fatti, non una
dimenticanza — va scritta qui perché chi legge il piano vecchio non si confonda.

---

## ⚠️ PREREQUISITO BLOCCANTE (da risolvere in CP0, prima di tutto il resto)

Verificato il 2026-08-07 su questo PC:
- `claude` **NON è invocabile da riga di comando** (non nel PATH, nessun `claude.exe`/
  `claude.cmd` trovato in LOCALAPPDATA/APPDATA/.claude) — Claude Code gira come
  app/estensione, non come CLI installato.
- `ANTHROPIC_API_KEY` **non presente** fra le variabili d'ambiente.
- SDK Python `anthropic` v0.118.0 **già installato**.

Uno script Python non può quindi "chiamare Claude Code" così com'è. Le strade reali sono
due e **la scelta spetta a Gael** (CP0), perché hanno implicazioni di costo diverse:

| Via | Come funziona | Costo | Automazione |
|---|---|---|---|
| **A. Claude Code CLI headless** | installare il CLI (`npm i -g @anthropic-ai/claude-code`), lo script lancia `claude -p "<prompt>"` | consuma i **crediti del piano** Claude Code già pagato | totale, nessun intervento |
| **B. SDK Anthropic + API key** | creare una API key su console.anthropic.com, lo script usa il pacchetto `anthropic` già installato | **a consumo separato** (~pochi € a libro con Haiku/Sonnet) | totale, nessun intervento |

Entrambe soddisfano "il minor numero di crediti possibile" se si usa un modello economico
per la prosa (Haiku) tenendo i modelli grossi solo per l'outline.

---

## Checkpoint

Legenda: 🔴 non iniziato · 🔄 in corso · ✅ chiuso e verificato con esecuzione reale

> **AGGIORNAMENTO 2026-08-10** — V0-V3 sono stati **superati da una scelta diversa di
> Gael**: *"devi creare i flussi, cioè dei SOP per scrivere i libri, devi dividere tutto in
> step"*. Niente canale API e niente `claude_writer`: i capitoli li scrive Claude in
> sessione e li salva come file, `engine/book_project.py` fa da ponte verso il motore già
> costruito. Zero costi esterni, zero captcha. Il primo libro è stato prodotto così.

| # | Checkpoint | Stato | Dipende da |
|---|---|---|---|
| V0 | ~~Scelta canale API~~ → **superato**: si scrive in sessione, nessun canale esterno | ⬛ | — |
| V1 | ~~`claude_writer.py`~~ → **sostituito** da `book_project.py` (progetto = cartella, capitoli = file) + `SOP-SCRIVERE-UN-LIBRO.md` | ✅ | — |
| V2 | ~~`book_writer.py` su API~~ → **superato**: il testo si scrive in sessione seguendo la SOP | ⬛ | — |
| V3 | ~~Ottimizzazione crediti~~ → **non applicabile**: nessun consumo esterno per il testo | ⬛ | — |
| V4 | Copertina isolata: se fallisce, il libro si produce comunque e la copertina è segnalata mancante | ✅ | — |
| V5 | Flusso completo in `book_project.assembla`: capitoli → .docx → PDF → copertina → pacchetto + report | ✅ | V1, V4 |
| V6 | **Test end-to-end reale**: "The Quiet Hours", 115 pagine REALI contate sul PDF, copertina col titolo, pacchetto completo | ✅ | V5 |
| V6b | Report di consegna + validatori (trattini, numerazione, sillabazione, titolo copertina via OCR) — richiesta 2026-08-10 | ✅ | V6 |
| V7 | Tile "Libri KDP" in Aureus/EmpireDesk, sezione automazioni, con bottone Avvia funzionante | 🔴 | V6 |
| V8 | Tile "Outreach" nella stessa sezione automazioni (richiesta esplicita di Gael) | 🔴 | — |
| V9 | Pulizia: codice LM Arena per il testo archiviato (non cancellato), PIANO-KDP-67 aggiornato con rimando a questo piano | 🔴 | V5 |
| V10 | Comando unico da riga di comando per l'intero flusso (dal piano del 2026-08-10, RF-05) | 🔴 | V5 |

### Definizione di "fatto" per ciascuno

**V0 — Canale** · Gael sceglie A o B. Fatto = una chiamata reale che ritorna testo vero,
stampata a schermo, con il costo/crediti della chiamata annotato.

**V1 — `claude_writer.py`** · Funzione unica `generate_text(prompt, max_words, model)` che
ritorna testo reale. Retry su risposta troncata/vuota (stessa logica già scritta e testata
in `book_writer`). Fatto = self-test che genera 3 testi diversi e verifica che siano
davvero diversi fra loro (il test che avrebbe intercettato subito il bug dei capitoli
duplicati di ieri).

**V2 — `book_writer.py` su Claude** · Stessa interfaccia pubblica di oggi
(`generate_outline`, `write_chapters`) così `orchestrator` non cambia. Le guardie già
scritte restano tutte (anti-duplicato, outline completa, retry). Fatto = outline + 3
capitoli brevi reali, verificati diversi e coerenti fra loro.

**V3 — Costo** · Misurare token/crediti di un libro intero. Fatto = numero reale scritto
qui nel piano, con la scelta del modello motivata dai numeri, non a sensazione.

**V4 — Copertina isolata** · La copertina resta su LM Arena (funziona, verificato con
immagini reali). Fatto = se LM Arena fallisce, il run produce comunque il .docx e segnala
la copertina mancante invece di buttare via tutto il libro.

**V5 — Orchestrator** · Fatto = un run reale arriva fino al pacchetto in
`LIBRI/libri_pronti/`, e un run interrotto a metà riprende dalla fase giusta (il
meccanismo di checkpoint/resume esiste già ed è verificato).

**V6 — End-to-end** · Fatto = report con: pagine reali contate dal .docx, copertina
allegata, verifica a mano che la trama sia coerente, tempo e costo del run.

**V7 — Tile Libri in Aureus** · Modulo in `EmpireDesk/modules/`, tile con bottone Avvia.
Fatto = lanciato dall'app, log visibile, exit code 0 (stesso standard già usato per le
tile esistenti).

**V8 — Tile Outreach in Aureus** · Fatto = come V7, per il workflow outreach già esistente.

**V9 — Pulizia** · Fatto = nessun modulo attivo importa più LM Arena per il testo; il
codice vecchio è in archivio con un README che spiega perché.

---

## Cosa NON cambia (già costruito e verificato, non toccare)

- `amazon_research.py` (CP2) — ricerca competitor reale, 16 risultati verificati
- `story_validator.py` (CP3) — classificatore storia vs diario, 5/5 corretti
- `kdp_formatter.py` (CP6) — .docx reale con trim/margini/numeri pagina
- `book_output_manager.py` (CP8) — pacchetto per libro, test anti-copia superato
- `orchestrator.py` (CP9) — checkpoint/resume verificato 4/4
- `cover_generator.py` + `lmarena_client.py` **per le sole immagini** — copertina reale
  generata e verificata visivamente

## RIPRESA DA

**V0**: Gael sceglie fra CLI headless (crediti del piano già pagato) e SDK+API key
(consumo separato). Senza questa scelta niente altro può partire, perché oggi lo script
non ha alcun modo di chiamare Claude.
