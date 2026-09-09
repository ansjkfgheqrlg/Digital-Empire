# RIPASSO COSTRUTTIVO — Blocco 3 · Fliki (A4/L19, A4/L20) + A6/L00, A6/L01 + trasversali

> Blocco: 4 lezioni + tutti i documenti trasversali (REPORT-CATEGORIA, APPUNTI-CATEGORIA,
> REPORT-BLOCCO-ULTIME-TRE, VERIFICA-GATE-A4, VERIFICA-PAYLOAD-L20-GATE-A4, CONFLITTI, BASELINE).
> Verificato contro `INVENTARIO.md` prima di ogni proposta. Dove la prova lo richiedeva, ho
> ri-controllato lo stato reale del codice con grep diretto il 2026-09-10 (non fidandomi solo
> delle date dei report letti), per non riproporre un difetto già chiuso nel frattempo.

---

### P-B3-01 · agente
- **Lezione:** A4-metodo-ai-tube/L19 + A4-metodo-ai-tube/L20 (trasversale: `VERIFICA-PAYLOAD-L20-GATE-A4.md`)
- **Prova:** `VERIFICA-PAYLOAD-L20-GATE-A4.md` — «Leggendo lo schema completo per rispondere (tabella
  intera, non i tre campi cercati), il payload reale ha un campo che il nostro codice non manda
  mai: `bgMusicVolume`» e «questa è la novità con più probabilità di avere un endpoint API
  dedicato» (riferito a `generateSfx`, citando `RAPPORTO-GREZZO-L20.md` punto P, min. 44:53-46:04).
  Sullo stesso solco, L19/appunti.md: «Non nomina mai l'API, che pure è una voce del menu che ha
  davanti (`frame-040`)».
- **Cosa manca oggi:** nessun agente della fabbrica ha per compito ricorrente confrontare i campi
  che il nostro payload usa (`fliki_client.py`) con la superficie reale dell'API del fornitore.
  Verificato contro l'inventario: `regolatori/regolatore-configurazione.md` fa l'esatto contrario
  (blocca ogni cambiamento ai valori approvati, «il video era perfetto, non modificare le regole»,
  decisione di Gael 2026-07-31) — è un guardiano dello status quo, non uno scopritore di capacità
  nuove. `supporto/self-improver.md` guarda solo `performance_logs.json` (CTR, retention, views) —
  mai la documentazione del fornitore. La scoperta di `bgMusicVolume` e `generateSfx` è avvenuta
  **una volta sola**, il 2026-09-07, per iniziativa isolata di Emperator fuori da qualunque ruolo
  che lo faccia di mestiere — e infatti è stata trovata per caso, cercando altro.
- **Cosa nasce:** `03-AGENTI-E-RUOLI/regolatori/regolatore-capacita-fliki.md` — nuovo agente L3,
  classe regolatore. A cadenza dichiarata (ogni apertura di gate di categoria, o su comando), legge
  la documentazione API viva del fornitore (`developer.fliki.ai`), la confronta campo per campo con
  `fliki_client.py`, e produce un elenco di leve mai usate — con la stessa disciplina di doppia
  lettura indipendente vista in `VERIFICA-PAYLOAD-L20-GATE-A4.md` («ogni campo... letto due volte,
  con prompt diversi, su pagine diverse»). Non applica nulla di persona: propone, il binario B resta
  al gate di categoria (ADR-029).
- **Perché vale:** chiude un buco strutturale, non un fatto isolato. Senza questo ruolo, una leva
  gratuita come `bgMusicVolume` (musica di sottofondo, oggi assente per scelta mai dichiarata come
  tale — non per limite tecnico) può restare invisibile per mesi, esattamente come è già successo.
- **Binario:** A (nuovo file agente, fuori dal motore)
- **Misura:** il file `03-AGENTI-E-RUOLI/regolatori/regolatore-capacita-fliki.md` esiste sul disco;
  il suo primo output (elenco leve non usate, con data) compare in un file dedicato o in
  `company/Memory`.

---

### P-B3-02 · skill/comando
- **Lezione:** A4-metodo-ai-tube/L20 (trasversale: `VERIFICA-PAYLOAD-L20-GATE-A4.md`, `REPORT-CATEGORIA.md` §6)
- **Prova:** `REPORT-CATEGORIA.md` §6 — «Tre verifiche nuove, assegnate al gate A4 ... tutte contro
  il payload reale» — le tre erano risposte solo da una sessione di ricerca manuale una tantum
  (Emperator, non sentinella), non da un comando ripetibile: «Non richiedono una sentinella sul
  video: sono domande sull'API reale, non sul corso» (`VERIFICA-PAYLOAD-L20-GATE-A4.md`, riga 8).
- **Cosa manca oggi:** verificato contro `INVENTARIO.md` — nessuna skill in
  `.claude/skills/youtube-automation-factory/` esegue questo confronto. L'unica esecuzione esistita
  finora è un lavoro di ricerca ad-hoc, con metodo scritto solo in un file di verifica, non in un
  comando invocabile di nuovo.
- **Cosa nasce:** `.claude/skills/fliki-capability-audit/SKILL.md` — comando `/fliki-capability-audit`,
  braccio operativo di P-B3-01: legge `fliki_client.py`, elenca i campi payload effettivamente
  costruiti, li confronta con lo schema pubblicato su `developer.fliki.ai` (fetch + lettura doppia
  indipendente, stesso metodo di `VERIFICA-PAYLOAD-L20-GATE-A4.md`), e produce una tabella
  campo-per-campo usato/non-usato con citazione della doc.
- **Perché vale:** rende ripetibile in minuti un lavoro che oggi costa una sessione di ricerca
  dedicata (come è costato il 2026-09-07), e dà al `regolatore-capacita-fliki` (P-B3-01) lo
  strumento per operare senza reinventare il metodo ogni volta che serve.
- **Binario:** A (nuova skill, fuori dal motore — non tocca `02-AUTOMAZIONI-E-SCRIPTS/`)
- **Misura:** file `.claude/skills/fliki-capability-audit/SKILL.md` sul disco, invocabile con
  `/fliki-capability-audit`, con un output verificabile su richiesta.

---

### P-B3-03 · flusso
- **Lezione:** A6-viral-mastery/L00-caricamento-video + A6-viral-mastery/L01-seo-manuale
- **Prova:** L00/appunti.md — «tre elementi video mai automatizzati: sottotitoli nativi, schermata
  finale, schede — verificati assenti in entrambe le lingue, non per una singola stringa mancata»;
  L00/report.md — «Nessuno dei tre è nel nostro uploader (grep vuoto su "scheda", "schermata
  final", "sottotitol" in `youtube_uploader_playwright.py`)». L01/appunti.md, 13:18-13:23:
  «"inserire il video in almeno due playlist, è consigliato da parte di YouTube"... non una
  raccomandazione mia, è YouTube stesso a consigliarlo secondo il docente», con prova a schermo
  `frame-407.png @ 13:32` (due playlist selezionate nel wizard). **Riverificato io stesso oggi
  (2026-09-10)** con grep diretto su `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py`:
  zero occorrenze di "playlist", "scheda", "card", "endscreen", "schermata final", "subtitle",
  "caption" — il gap è ancora aperto, identico a come l'ha trovato la lezione.
- **Cosa manca oggi:** `youtube_uploader_playwright.py` copre il wizard fino al tab
  Dettagli/Visibilità e Controlli, e si ferma in stato Bozza (coerente con L00, min. 11:31). L'intero
  tab «Elementi video» (sottotitoli nativi CC, schermata finale, schede) e l'assegnazione a
  playlist **non vengono mai toccati** — non parzialmente, per intero.
- **Cosa nasce:** una tappa esplicita nuova nel flusso di pubblicazione — non un ritocco, un passo
  che oggi non esiste in nessuna forma — dentro `youtube_uploader_playwright.py`: dopo il
  caricamento e prima della chiusura in Bozza, apre il tab Elementi video e (a) attiva i
  sottotitoli nativi via riconoscimento automatico (un click, L00 min. 09:00: «faccio fine, e in
  automatico youtube adesso trascrive tutto»), (b) assegna il video ad **almeno due playlist**,
  creandole se non esistono (come mostra il wizard, L01 frame-407), (c) valuta schermata finale e
  schede come leve separate, da prioritizzare coi dati CTR/community già raccolti da
  `performance-auditor` (indicazione già presente in `A6-L00-01`, non riscritta qui).
- **Perché vale:** oggi ogni video pubblica e guadagna comunque, ma perde due leve gratuite dette
  esplicitamente **da YouTube stesso** secondo il corso: la playlist (watch-time di sessione,
  premiato nell'algoritmo) e i sottotitoli nativi (indicizzazione — vedi anche P-B3-04, che dipende
  da questo passo per essere vero e non solo corretto).
- **Binario:** B (tocca `youtube_uploader_playwright.py` in `02-AUTOMAZIONI-E-SCRIPTS/`, motore in
  produzione — ADR-003/ADR-029) — nasce qui, si applica solo al gate di categoria A6.
- **Misura:** `youtube_uploader_playwright.py` contiene una funzione dedicata (es.
  `_gestisci_step_elementi_video`) sul modello di `_gestisci_step_monetization` già esistente; un
  video pubblicato dopo l'applicazione ha almeno 2 playlist verificabili da YouTube Studio e una
  traccia CC nativa attiva.

---

### P-B3-04 · funzione
- **Lezione:** A6-viral-mastery/L01-seo-manuale
- **Prova:** L01/appunti.md — «`apex7_orchestrator.py:1515` lo scrive `True` **incondizionatamente**,
  a fianco di `"thumbnail": not skip_thumbnail` (quello sì condizionale, quindi reale) — nessun
  controllo se una traccia sottotitoli nativa esista davvero. **Il nostro gate SEO assegna sempre 15
  punti su 100 per un elemento che non abbiamo mai creato.**» — e `seo_score.py:30`, commento
  sorgente citato: `"subtitles": 15, # presenti = indicizzati da YouTube`. **Riverificato oggi
  (2026-09-10)** con grep diretto: `apex7_orchestrator.py` riga 1515 scrive ancora `"subtitles": True`
  fisso, nessuna condizione — il difetto è ancora aperto, non applicato nel frattempo.
- **Cosa manca oggi:** una funzione che determini lo stato reale dei sottotitoli nativi invece di
  dichiararlo sempre vero. Oggi non esiste alcun controllo — né in `apex7_orchestrator.py` né
  altrove nella fabbrica — che verifichi se una traccia CC nativa sia stata effettivamente creata
  prima di assegnare il punteggio.
- **Cosa nasce:** una funzione `subtitles_native_creati(...)` in `apex7_orchestrator.py`, sullo
  stesso schema già in uso per `"thumbnail": not skip_thumbnail` — restituisce `True` **solo** se lo
  step di creazione sottotitoli nativi (P-B3-03) è stato eseguito con successo per quel video.
  Finché P-B3-03 non è applicato, la funzione deve restituire **sempre `False`**, non `True`:
  l'onestà del punteggio viene prima della comodità di non toccare il numero.
- **Perché vale:** chiude un difetto reale e già misurato dalla lezione, non ipotetico — «un video
  borderline a 55-69 "onesti" oggi passa lo stesso, gonfiato dai 15 punti falsi» (L01/report.md).
  Senza P-B3-03 la correzione onesta abbassa il punteggio medio dei video già prodotti, ma lo rende
  vero — ed è la stessa logica già accettata per il criterio musica in `qa-audio-video.md` §10
  (inapplicabile dichiarato, non taciuto).
- **Binario:** B (tocca `apex7_orchestrator.py` e la lettura che ne fa `seo_score.py`) — candidato
  al gate A6, condizionato all'applicazione di P-B3-03.
- **Misura:** grep su `apex7_orchestrator.py` non trova più `"subtitles": True` incondizionato; un
  video senza sottotitoli nativi riceve 0/15 su quella voce del punteggio SEO, uno con sottotitoli
  reali riceve 15/15.

---

### Nota d'onestà su D-1 e D-2 (`BASELINE.md`)

Il mandato del blocco chiede di verificare se la chiusura di D-1/D-2 richieda solo un numero o un
pezzo di fabbrica mancante. Le quattro lezioni di questo blocco **non toccano il tema**: L19/L20
sono un approfondimento sull'editor Fliki (voce, musica, pronunce, tetti di scena), non sulla
durata ottimale di pubblicazione; L00/L01 sono sul wizard di caricamento e sulla SEO, non sulla
durata dello script. **D-1** (soglie di durata contraddittorie) resta assegnato, come già scritto in
`BASELINE.md`, alla lezione del corso che tratta esplicitamente «quanti video pubblicare, quanto
devono durare» — non in questo blocco. **D-2** (`verifica_qualita()` mai invocata) non richiede né
un numero né un pezzo di fabbrica mancante: la funzione esiste già, va solo collegata alla catena di
produzione — ma collegarla oggi, con le soglie di D-1 ancora contraddittorie, bloccherebbe ogni
produzione (lo dice `BASELINE.md` stessa). Non scrivo una proposta finta per riempire la casella:
qui non c'è nulla di nuovo da estrarre su D-1/D-2 da questo materiale.

---

## FINITO — 4 proposte, lezioni ripassate: A4/L19-perfezionare-fliki, A4/L20-aggiornamento-fliki, A6/L00-caricamento-video, A6/L01-seo-manuale (+ REPORT-CATEGORIA.md, APPUNTI-CATEGORIA.md, REPORT-BLOCCO-ULTIME-TRE.md, VERIFICA-GATE-A4.md, VERIFICA-PAYLOAD-L20-GATE-A4.md, CONFLITTI.md, BASELINE.md)
