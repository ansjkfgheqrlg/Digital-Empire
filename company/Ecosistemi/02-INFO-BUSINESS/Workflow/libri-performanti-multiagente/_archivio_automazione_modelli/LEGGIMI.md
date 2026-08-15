# Archivio — tutta l'automazione che chiamava un modello

**Archiviato il 2026-08-15.** Niente qui dentro è in uso. Il codice attivo è in `engine/` e
**non chiama nessun modello**: il libro lo scrive Claude in sessione, seguendo la skill
`/libro` (`.claude/skills/libro/SKILL.md`) e la `SOP-SCRIVERE-UN-LIBRO.md`.

## Perché

Questo progetto ha provato tre volte a far scrivere i libri a un programma. Tutte e tre le
volte ha fallito, e ogni volta per un motivo diverso ma della stessa famiglia — un pezzo di
codice che parla con un modello dipende da qualcosa che non controlla:

1. **LM Arena via Playwright** (luglio-agosto) — captcha. Non aggirabile e non da aggirare:
   è un controllo pensato apposta per distinguere una persona da un programma. I log reali
   (`sessions/debug_logs/lmarena_*.jsonl`) mostrano il capitolo 1 andato in captcha **4
   volte consecutive**, ogni volta risolto a mano e ripresentatosi — e questo *dopo* aver
   applicato la difesa "chat nuova per ogni richiesta". Perfino le copertine, un solo invio
   a libro, l'hanno incontrato in 2 sessioni su 3.
2. **Claude Code CLI con Haiku** (13 agosto) — due guasti silenziosi in fila. Il wrapper
   `claude.CMD` di npm troncava i prompt multiriga alla prima riga *e* faceva sparire
   `--model haiku`, quindi si pagava il modello di default senza accorgersene. Poi il piano
   ha raggiunto il limite di spesa mensile.
3. **Di nuovo LM Arena** (15 agosto) — fermato prima di rifare la stessa strada, dopo aver
   riletto i log del punto 1.

Decisione di Gael, il 15 agosto: *"l'utilizzo di Arena è praticamente infattibile... anche se
si risolvessero questi problemi ne verrebbero altri"*. E il punto più importante: quando il
codice chiama un modello via API, **non posso più essere io a scrivere**.

## Il precedente che ha convinto tutti

L'unico libro completo che questo progetto abbia mai prodotto — *The Quiet Hours*, 115 pagine
reali contate dal PDF, pacchetto in `LIBRI/libri_pronti/The_Quiet_Hours/` — è nato l'8 agosto
**scrivendolo in sessione**. Il checkpoint di quel giorno lo dice testualmente: *"Il testo
l'ho scritto io in sessione: zero costi esterni"*, e *"il pezzo mancante non era un motore
che chiama un modello ma il PONTE fra i capitoli scritti in sessione e il codice già
costruito"*.

Nessuno dei tre tentativi automatici ha mai prodotto un libro finito.

## Cosa c'è qui dentro

| File | Cosa faceva |
|---|---|
| `lmarena_client.py` | wrapper Playwright su arena.ai: sessione, modalità Direct, invio prompt, gestione captcha |
| `arena_book_writer.py` | piano di produzione, capitoli, copy KDP via Arena |
| `lmarena_captcha_probe.py` | la sonda che doveva misurare quanti invii regge Arena prima del captcha (mai eseguita) |
| `google_doc_staging.py` | staging dei capitoli su Google Doc via Playwright |
| `scrittore_haiku.py` | scrittura via CLI di Claude, modello Haiku |
| `cover_generator.py` | generazione copertina via Arena **+** post-processing Pillow |
| `orchestrator.py` | macchina a fasi con checkpoint/resume, alimentata dalle dependency di cui sopra |
| `workflow.py` | la CLI a step del flusso automatico |
| `test_*.py` | i test di quei moduli |
| `_testo_lmarena/`, `_scrittura_haiku/` | archivi precedenti, confluiti qui |

## Cosa è stato salvato prima di archiviare

Non tutto quel codice era da buttare. Prima dello spostamento sono stati estratti:

- **il post-processing della copertina** → `engine/copertina_kdp.py`. Ritaglio 2:3, upscale a
  1800×2700, scrittura del titolo con Pillow, verifica proporzioni/risoluzione. Non ha mai
  avuto niente a che fare con un modello, ed è esattamente ciò che serve ora per portare a
  norma una copertina generata da Gael. *Era dentro `cover_generator.py`, che importava
  `lmarena_client` a livello di modulo: senza lo split sarebbe diventato non importabile.*
- **i comandi della nicchia persistente** (`nicchia-scegli` / `nicchia-stato` /
  `nicchia-confronta`) → `engine/kdp.py`
- **`estrai_titolo()`** → `engine/kdp.py`
- **~29 test** ancora validi → `tests/test_flusso_manuale.py`

## Se un giorno servisse rileggerlo

Il codice qui dentro **non è eseguibile così com'è**: le costanti che usava
(`LMARENA_SESSION_PATH`, `BRAVE_*`, `GOOGLE_*`) sono state tolte da `engine/config.py`, e
`session_manager.py` non ha più le funzioni di login per Arena e Google. Vive nella storia
git: `git log --follow _archivio_automazione_modelli/<file>.py`.

Tre cose imparate qui che valgono a prescindere dallo strumento, e che sono già state pagate:

1. **Un successo dichiarato non è un successo.** Il CLI rispondeva exit code 0 con prompt
   mutilato e modello sbagliato. Bisogna verificare *cosa è arrivato*, non *se ha risposto*.
2. **Un test che non guarda il prompt non testa la scrittura.** Tutti i test usavano un invio
   finto: verificavano che il file venisse scritto, mai cosa veniva chiesto.
3. **I log valgono più della documentazione, quando divergono.** Una nota diceva che le
   copertine su Arena non davano problemi; i log dicevano il contrario, ed erano lì da giorni.
