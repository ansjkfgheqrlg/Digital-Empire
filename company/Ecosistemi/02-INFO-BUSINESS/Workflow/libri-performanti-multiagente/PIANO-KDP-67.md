# PIANO KDP 67 — Motore Reale Workflow Amazon KDP (Playwright + LM Arena)

**Creato:** 2026-08-05 · **Owner:** Gael · **Stato:** 🔄 IN CORSO — 5/13 checkpoint chiusi
(CP0, CP3, CP6*, CP8*, CP11), bloccato su CP1 in attesa di login manuale di Gael

**Per riprendere dopo spegnimento PC o fine crediti**: dire a Claude *"continua con il piano KDP 67"*.
Claude deve: (1) aprire questo file, (2) leggere quale checkpoint ha ✅/🔄/🔴, (3) riprendere dal
primo non completato, (4) aggiornare questo file dopo ogni checkpoint chiuso (non solo a fine sessione).

---

## 0. Cosa questo piano corregge (riferimento — vedi analisi completa in conversazione 2026-08-05)

Diagnosi confermata sul codice reale, non sui documenti che lo descrivono:

1. Lo zip dice esplicitamente "questo workflow **non** verrà usato su lmarena, dovrà essere usato
   su Claude Code" — l'opposto del requisito reale (autonomo, **zero dipendenza da crediti Claude
   Code**, tutto via Playwright + LM Arena con sessioni salvate).
2. Zero Playwright reale (`real_tool.py` riga 76: chiamata reale ancora in un commento, mai eseguita).
3. Zero righe di codice che parlano con LM Arena in tutto lo zip (971 file) — solo nei `.md`.
4. Zero gestione sessioni (`storage_state`/cookies) — nessun file la implementa.
5. `genera_nuovo_libro.py` non genera nulla: **copia** sempre lo stesso file docx/png template
   rinominandolo (provato con hash/dimensioni byte identiche su 5 "libri" diversi).
6. Nessuno script scrive testo (niente `python-docx` da nessuna parte, niente chiamata LLM nel codice).
   I `.docx` reali presenti nello zip sono stati prodotti a mano in chat, non dalla "pipeline".
7. Storico errori reali (nel loro stesso log): libro troppo corto, impaginazione KDP sbagliata,
   diario invece di storia, conteggio pagine sbagliato due volte — nessuno rilevato dal sistema,
   tutti scoperti da Gael a mano.
8. Struttura output triplicata/quadruplicata (`LIBRI/`, `BIBLIOTECA_LIBRI_GENERATI/`,
   `workflow_execution/`, `AMAZON_KDP_PACKAGE/`) — nessuna fonte unica di verità.
9. Zero integrazione con Aureus/Empire Desk.
10. Riferimento a una "Official Claude Code Managed Agents API" (`managed-agents-2026-04-01`) che
    non risulta esistere nella superficie reale delle API Anthropic — probabile allucinazione da
    verificare, non da usare come fondamento.

---

## 1. Architettura del motore reale (decisioni prese, valgono per tutto il piano)

**Principio guida**: niente narrativa, niente 95 agenti-di-carta. Ogni modulo sotto fa UNA cosa,
è testabile da solo, e non dichiara "fatto" finché non è verificato con un'esecuzione reale
(stesso standard già applicato al fix di `assembly_finale.py` in CP-20260803-006: gira davvero,
o non è finito).

```
company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/
├── engine/                          # NUOVO — il motore reale, sostituisce le 4 varianti finte
│   ├── config.py                    # trim size, target pagine, keyword niche vietate/richieste,
│   │                                 # URL LM Arena, path sessioni — TUTTO qui, niente path assoluti
│   │                                 # hardcoded /home/user/... (bug ricorrente in ogni zip finora)
│   ├── session_manager.py           # CP1
│   ├── amazon_research.py           # CP2
│   ├── story_validator.py           # CP3
│   ├── lmarena_client.py            # CP4 — wrapper condiviso Playwright per LM Arena (testo+immagini)
│   ├── book_writer.py               # CP5
│   ├── kdp_formatter.py             # CP6
│   ├── cover_generator.py           # CP7
│   ├── book_output_manager.py       # CP8 — riscritto da zero, non più uno stub che copia
│   └── orchestrator.py              # CP9 — unico entrypoint, checkpointing interno per resume
├── sessions/                        # gitignored — storage_state.json Amazon + LM Arena
├── LIBRI/
│   ├── libri_pronti/<Nome-Libro>/   # libro.docx + copertina.png + metadata — creata ad ogni run
│   └── libri_pubblicati/            # spostamento manuale dopo pubblicazione (invariato, era già giusto)
├── _archivio_blueprint_narrativo/   # CP11 — le 4 varianti finte + doc "Managed Agents API" spostate
│                                     # qui, MAI cancellate, chiaramente etichettate come non funzionanti
└── PIANO-KDP-67.md                  # questo file
```

**Perché non 95 agenti**: le fasi concettuali del blueprint (Ricerca → Qualifica → Piano →
Scrittura → Copertina → Pacchetto) sono corrette e restano. Il problema non era la suddivisione
in fasi, era che ogni "agente" era un nome in un documento invece che codice. Ogni fase sopra
= un modulo Python reale con una funzione reale che fa quella cosa, non una gerarchia a 7 livelli
finta.

**Rischi dichiarati fin da ora (non scoperti a metà lavoro)**:
- **Login la primissima volta non può essere 100% automatico**: Amazon e LM Arena hanno
  captcha/2FA — CP1 apre un browser VISIBILE la prima volta, Gael fa login a mano una volta sola,
  la sessione si salva e da lì in poi è automatico. Non è un bug, è l'unico modo onesto.
- **Scraping Amazon e automazione LM Arena possono violare i rispettivi Termini di Servizio.**
  Lo dichiaro qui esplicitamente prima di costruire, non lo scopriamo dopo — è una scelta
  consapevole del progetto, non un dettaglio nascosto.
- **Amazon cambia il DOM spesso**: i selettori CSS in CP2 andranno testati sul sito reale e
  probabilmente ritoccati nel tempo, non è un "una volta e per sempre".
- **Continuità narrativa su 30.000 parole via prompt-per-capitolo** (CP5) richiede iterazione
  reale sui prompt per tenere coerenti personaggi/trama — non garantito perfetto al primo colpo,
  richiede test veri con libri veri, non solo lettura del codice.

---

## 2. Checkpoint (aggiornare lo stato qui dopo ogni chiusura)

Legenda: 🔴 non iniziato · 🔄 in corso · ✅ chiuso e verificato con esecuzione reale

| # | Checkpoint | Stato | Dipende da |
|---|---|---|---|
| CP0 | Setup struttura + config centralizzato + requirements (playwright, python-docx) | ✅ | — |
| CP1 | Session Manager: salva/carica sessione reale Amazon + LM Arena | 🔄 | CP0 |
| CP2 | Amazon Research reale: naviga, cerca keyword, estrae dati libri veri | 🔴 | CP1 |
| CP3 | Story Validator reale: classificatore GO/NO-GO storia vs diario, deterministico | ✅ | CP0 |
| CP4 | LM Arena Client condiviso: invia prompt, aspetta risposta, estrae testo/immagine | 🔴 | CP1 |
| CP5 | Book Writer: loop capitolo-per-capitolo con continuità, produce bozza completa | 🔴 | CP4 |
| CP6 | KDP Formatter: python-docx reale (trim/margini/font/TOC) + validazione pagine in loop | ✅* | CP5 |
| CP7 | Cover Generator: immagine reale unica per libro via LM Arena | 🔴 | CP4 |
| CP8 | Output Manager riscritto: pacchetto reale per libro, no più copia-template | ✅ | CP6, CP7 |
| CP9 | Orchestrator: unico entrypoint, incatena CP2→CP8, checkpoint interni per resume | 🔴 | CP2,3,6,7,8 |
| CP10 | Integrazione Aureus/Empire Desk: tile "Avvia" in sezione automazioni | 🔴 | CP9 |
| CP11 | Pulizia archivio: sposta le 4 varianti finte + doc API inventata in archivio etichettato | ✅ | — |
| CP12 | Test end-to-end reale: 1 run completo, libro diverso da tutti i precedenti, verificato | 🔴 | CP10 |

### Dettaglio per checkpoint (definizione di "fatto")

**CP0 — Setup**
- Cartelle `engine/`, `sessions/` (in `.gitignore`), `LIBRI/` create
- `config.py` con TUTTI i parametri centralizzati (niente path assoluti `/home/user/...`)
- `requirements.txt`: `playwright`, `python-docx`, più eventuale `pillow` per validazione immagini
- Fatto = `pip install -r requirements.txt && playwright install` gira senza errori

**CP1 — Session Manager**
- Prima esecuzione: apre browser visibile, Gael fa login manuale su Amazon e su LM Arena,
  script salva `sessions/amazon_state.json` e `sessions/lmarena_state.json` via
  `context.storage_state(path=...)`
- Esecuzioni successive: carica lo state salvato, browser headless, nessun login richiesto
- Fatto = seconda esecuzione dimostrata SENZA prompt di login, sessione riconosciuta come valida

**CP2 — Amazon Research reale**
- Naviga `amazon.com/s?k=<keyword>` con sessione salvata
- Estrae almeno: titolo, autore, categoria/BSR se visibile, prezzo, rating — da libri VERI,
  screenshot o dump HTML come prova
- Gestione retry/backoff su blocco o captcha (dichiarare fallimento onestamente, non inventare dati)
- Fatto = una ricerca reale su una keyword vera produce una lista di libri veri con URL verificabili

**CP3 — Story Validator**
- Funzione pura, deterministica, senza LLM: prende titolo+descrizione, ritorna GO/NO-GO +
  motivazione, basata su keyword vietate (diario, questionario, tracker, journal, planner...)
  vs keyword richieste (mystery, romance, thriller, memoir, ecc.) — lista in `config.py`
- Fatto = test con almeno 5 titoli reali (3 devono passare, 2 devono essere respinti) verificati a mano

**CP4 — LM Arena Client**
- Apre LM Arena con sessione salvata, seleziona un modello specifico (non modalità "battaglia"
  anonima — serve un output verificabile e ripetibile)
- Invia un prompt, aspetta il completamento reale della generazione (non un timeout fisso),
  estrae il testo di risposta
- Stessa logica per un modello immagine: invia prompt, aspetta, scarica il file immagine reale
- Fatto = un prompt di test reale produce testo reale ripetibile, un prompt immagine produce un
  file .png reale scaricato su disco

**CP5 — Book Writer**
- Genera outline (titolo, personaggi, trama in 3 atti) via CP4
- Loop capitolo per capitolo: ogni prompt include riassunto capitoli precedenti per continuità
- Fatto = un libro completo di bozza (tutti i capitoli) generato end-to-end, letto per intero e
  verificato a mano che non ci siano incongruenze palesi di trama/personaggi

**CP6 — KDP Formatter**
- `python-docx`: trim 6x9, margini secondo tabella KDP, font, Heading 1 stile, TOC, numeri
  pagina, section break — applicati via codice, non descritti in un markdown
- Conta parole/pagine REALI dopo assemblaggio; se sotto target, torna a CP5 per capitoli
  aggiuntivi invece di dichiarare falso successo (questo è l'errore che si è ripetuto 2 volte
  nello zip originale — qui deve essere impossibile per costruzione)
- Fatto = un .docx reale con conteggio pagine verificato via `python-docx` stampato a schermo,
  dentro il range dichiarato

**CP7 — Cover Generator**
- Prompt di copertina generato dai dettagli reali del libro (titolo, genere, elementi trama),
  non un prompt fisso copiato da un altro libro
- Fatto = copertina generata per un secondo libro diverso dal primo, dimensione file DIVERSA
  (prova che non è una copia — replica del test byte-per-byte fatto nell'analisi)

**CP8 — Output Manager**
- Riceve i path REALI del docx e della copertina appena generati (non un path template fisso)
- Crea `LIBRI/libri_pronti/<Nome-Libro>/` con dentro libro + copertina + metadata KDP
- Fatto = due run consecutivi con niche diverse producono due cartelle con contenuto DIVERSO
  (di nuovo, verifica dimensione file — stesso test dell'analisi, ma questa volta deve fallire
  nel senso buono: i file NON devono essere identici)

**CP9 — Orchestrator**
- Incatena CP2→CP8 in un solo comando
- Salva un checkpoint interno dopo ogni fase (es. `sessions/run_<timestamp>/checkpoint.json`) così
  se crolla a metà (es. Playwright si blocca, LM Arena non risponde) si può riprendere dalla fase
  giusta invece di ripartire da zero
- Fatto = un run interrotto a metà a mano (kill del processo) e rilanciato riprende dalla fase
  giusta, non da capo

**CP10 — Integrazione Aureus/Empire Desk**
- Nuovo modulo `EmpireDesk/modules/libri_kdp.py` (separato dal modulo `libri.py` esistente, che
  resta com'è per il blueprint vecchio — non lo tocchiamo, è un'altra cosa)
- Tile reale (`kind="py"`) nella sezione automazioni, un solo bottone "Avvia" che lancia
  `engine/orchestrator.py`
- Fatto = lanciata dall'app stessa (stesso test già fatto per la tile "Libri Performanti":
  `/api/launch` reale, non da riga di comando), log visibile in tempo reale, exit code 0

**CP11 — Pulizia archivio**
- `workflow_architecture/`, `official_claude_architecture/`, `architettura_sincrona/`,
  `architettura_completa_7_livelli/` spostate in `_archivio_blueprint_narrativo/` con un
  README che spiega perché sono lì (blueprint narrativo, non funzionante, sostituito da `engine/`)
- Stralciato/segnalato il riferimento alla "Managed Agents API" inventata ovunque compaia
- Fatto = nessun file attivo del motore reale referenzia più le cartelle archiviate

**CP12 — Test end-to-end reale**
- Un run completo, dall'avvio della tile Aureus fino al libro pronto in `LIBRI/libri_pronti/`
- Verifiche esplicite da fare e riportare: conteggio pagine reale, copertina diversa dalle
  precedenti (dimensione file + controllo visivo), classificazione story-vs-diario corretta,
  nessuna dipendenza da crediti Claude Code durante il run (nessuna chiamata Anthropic nel log)
- Fatto = report finale con tutte le verifiche sopra, non una dichiarazione di successo senza prove

---

### Note di avanzamento (aggiornate ad ogni sessione)

**2026-08-05**: CP0 chiuso e verificato (pip install ok, playwright+chromium già presenti sul
PC, python-docx e Pillow installati, cartelle create, `config.py` con path tutti relativi
verificato con import reale). CP1: `engine/session_manager.py` scritto e verificato in modalità
`--check` (rileva correttamente 0/2 sessioni presenti) — **la parte di login vera richiede
Gael fisicamente al PC** (2FA/captcha, non automatizzabile da Claude): serve lanciare
`python -m engine.session_manager` dalla cartella `libri-performanti-multiagente/`, si aprono
2 finestre browser (Amazon poi LM Arena), fare login in ognuna, premere INVIO nel terminale
dopo ogni login. Finché non è fatto, CP1 resta 🔄.

Per non restare fermi in attesa del login, completati anche i checkpoint che NON dipendono da
sessioni live:
- **CP3 chiuso**: `engine/story_validator.py`, self-test 5/5 titoli reali corretti. Durante il
  test trovato e corretto un bug reale: "journal" da solo non era nella lista keyword vietate
  (solo frasi composte tipo "guided journal"), un titolo tipo "Guided Anxiety Journal" passava
  per il percorso "ambiguo" invece che per un vero match — aggiunta la keyword bare, ritestato.
- **CP6 chiuso\***: `engine/kdp_formatter.py` — trim/margini specchio reali (XML diretto,
  `mirrorMargins` verificato), font/heading/section-break per capitolo, campo numero pagina
  reale (XML `PAGE` field, verificato presente). Self-test con 2 casi (uno sotto target, uno
  dentro target): **replica esatta del bug che si è ripetuto 2 volte nello zip originale**
  (dichiarare 120 pagine quando in realtà erano 21) — qui il conteggio è sempre fatto rileggendo
  il file appena salvato, mai fidandosi della costruzione in memoria. `*` = **TOC automatico
  (campo Word) non ancora implementato**, rimandato — margini/font/numeri pagina sì, indice sommario no.
- **CP8 chiuso\***: `engine/book_output_manager.py` — riscritto da zero. Self-test: 2 libri con
  manoscritto/copertina diversi producono cartelle con file di dimensione DIVERSA (stesso test
  forense usato nell'audit per smascherare il bug copia-template — qui il bug NON si riproduce).
  Errore esplicito (`FileNotFoundError`) se manoscritto/copertina non esistono, mai un fallback
  silenzioso a un template. `*` = testato con file finti (dummy), non ancora con output reale
  di CP5/CP7 (che non esistono finché CP1 non sblocca).
- **CP11 chiuso**: le 4 varianti finte + i loro generatori + la documentazione con il
  riferimento alla API inventata spostate in `_archivio_blueprint_narrativo/` (con README che
  spiega perché), non cancellate. Trovato e corretto un effetto collaterale reale: il modulo
  Aureus `EmpireDesk/modules/libri.py` (dal task precedente, CP-20260803-006) referenziava il
  vecchio path di `architettura_completa_7_livelli/` — rotto dallo spostamento (selftest
  EmpireDesk sceso a 17/21), corretto aggiornando il path all'archivio, riverificato con
  selftest reale (tornato a includere `libri`/`module:libri` = OK). I 2 fallimenti residui nel
  selftest (`preventivi`, `licenze` — cartella `Clienti/Prof Autocad/preventivo-forge` mancante)
  sono pre-esistenti, non causati da questa sessione, fuori perimetro di questo piano — non toccati.

**Decisioni prese senza risposta esplicita di Gael (default del piano applicati, da rivedere
se serve)**: sessioni salvate dentro il repo in `sessions/` (già coperta da `**/sessions/` in
`.gitignore`, mai finiranno su GitHub); modello LM Arena testo/immagine non ancora scelto —
deciso di rimandare la scelta al momento del primo login reale (CP1/CP4) guardando la UI
effettiva invece di indovinare un nome adesso; rischio ToS Amazon/LM Arena: proseguo,
considerato confermato implicitamente dal "puoi iniziare" di Gael in risposta diretta alla
domanda; varianti finte: verranno archiviate (non cancellate) in CP11.

## 3. Decisioni aperte per Gael (da confermare prima o durante CP0/CP1)

1. **Quale modello su LM Arena** per il testo (es. un modello specifico in "Direct Chat", non
   "Battle" anonimo) e quale per le immagini? Serve un nome preciso per CP4.
2. **Dove vivono le sessioni salvate** — vanno bene dentro il repo in `sessions/` (gitignored,
   quindi mai su GitHub) o preferisci un percorso fuori dal repo (es. `%APPDATA%`)?
3. **Rischio ToS Amazon/LM Arena** (vedi §1) — confermi di voler procedere consapevole del rischio?
4. **Le 4 varianti finte**: archiviare (default di questo piano) o cancellare del tutto?

Se non rispondi prima, procedo con i default indicati e li segnalo nel checkpoint corrispondente.

---

## RIPRESA DA

Piano appena creato, **nessun checkpoint iniziato**. Prossimo passo: CP0, dopo conferma di Gael
per iniziare la correzione (questo piano è stato consegnato PRIMA di iniziare, come richiesto).
