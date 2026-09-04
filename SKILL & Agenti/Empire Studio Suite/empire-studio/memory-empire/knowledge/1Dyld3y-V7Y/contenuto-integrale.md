# Contenuto integrale — 1Dyld3y-V7Y

**"Dammi 36 Minuti e Ti Farò Risparmiare MILIONI di Token su Claude"**
Riccardo Belli Contarini (Martes AI) · 36:01 · italiano · 20 capitoli ufficiali
Run: `empire-studio/runs/max18-v03-belli-token` · Ingest 2026-09-04

> Archivio **integrale, non riassunto**: Parte 1 = tutto ciò che è stato letto sulle schermate
> (le cifre della lavagna non vengono mai dette a voce, quindi senza questa parte il video è
> dimezzato); Parte 2 = la trascrizione completa, 950/950 righe.
> Vincolo: sorgente **640x360**; le citazioni testuali vengono solo dalle viste in cui l'autore
> zooma sulla lavagna. Le parti non leggibili sono marcate come tali e non sono state inventate.

---

# PARTE 1 — Tutto ciò che è stato letto a schermo

## 1.1 La lavagna Excalidraw — "RISPARMIA I TOKEN · Tutte le Tattiche"

Sottotitolo: *"Tutto quello che sposta il conto: come funziona, quanto vale, quanto ci metti"*

Struttura: banner dorato + 4 colonne colorate + 4 riquadri larghi in basso.

### Banner — "PRIMA DI TOCCARE QUALSIASI COSA, MISURA"
- `/context` — "cosa occupa la finestra adesso"
- `/usage` — "se li hai bruciati, per [quando]" *(coda non nitida)*
- `statusline` — "il contatore sempre a s[chermo]"

### Colonna verde — "GRATIS, SUBITO" · *valgono più di tutto il resto*

| Titolo card | Claim | Corpo |
|---|---|---|
| `/clear` a ogni cambio di task | azzera la base | "La cronologia smette di essere rispesta. Ogni altro fix taglia una fetta, questo azzera la torta." |
| modello ed effort scelti una volta | eviti un 10x | "La roba già pronta è legata al modello, cambiarlo la butta via tutta. Se vuoi il modello economico, partici." |
| `/rewind`, non `/compact` | non ricostruisci nulla | "Torni a un punto che il modello ha già pronto. È il posto dove quasi tutti usano /compact e sbagliano." |
| un file di handoff, non `/compact` | poche centinaia di token | "Scrivi lo stato e riparti da un prefisso piccolo. E scegli tu cosa sopravvive; soprattutto le strade già fallite." |
| diagramma ASCII prima di costruire | togli il giro | "Il lavoro rifatto non avviene proprio. Nessun compressore può farlo: agiscono su ciò che è già successo." |

### Colonna arancio — "UNA VOLTA SOLA" · *installa una volta, paga per sempre*

| Titolo card | Claim | Corpo |
|---|---|---|
| spegni gli MCP che non usi | **-47.000 a sessione** | "GitHub 26.000, Slack 21.000, caricati prima che tu scriva. /context deve dire 'deferred'." |
| CLAUDE.md come indice | sotto le 200 righe | "Si rilegge a ogni messaggio. Dice DOVE stanno le cose, non le contiene. Regola dai doc Anthropic." |
| un CLAUDE.md per cartella | **-7.160 a sessione** | "Il root si carica SEMPRE, quelli nelle sottocartelle solo se l'agente entra lì dentro." |
| archivia le skill e accorcia le descrizioni | migliaia a sessione | "Skill e descrizioni si caricano ogni volta, anche quelle che non parti mai. Restano installate, smettono di pesare." |
| hook PDF e filtro sull'output | 3-4x sui PDF | "Il Read manda ogni pagina come testo PIÙ immagine. E l'output dei comandi lo tagli una volta, con un filtro che scrive l'agente." |

### Colonna viola — "IL MODELLO GIUSTO" · *la qualità è essa stessa un risparmio*

| Titolo card | Claim | Corpo |
|---|---|---|
| coding e planning veri | resta sul modello di frontiera | "Un risultato da rifare costa più di quello che hai risparmiato scegliendo il modello economico." |
| routine, skill, sub-agenti, `/chrome` | Haiku e Sonnet vanno benissimo | "I job schedulati che sai già riuscire, la navigazione, la manovalanza. Lì il modello grosso non serve." |
| si sceglie per skill e per sub-agente | mai a metà sessione | "Cambiare modello in corsa butta via la roba pronta. Lo passi dentro la skill e la sessione principale non la tocchi." |
| i task schedulati | pagano dieci volte | "Mandano il contesto INTERO a ogni scatto, e sotto la frequenza oraria non trovano mai niente di pronto. Anche alle 3 di notte." |

### Colonna rosa — "NON FARLO" · *sembrano furbe, costano*

| Titolo card | Claim | Corpo |
|---|---|---|
| `/compact` per risparmiare | il messaggio più caro | "Per riassumere rimanda tutto, e poi butta via la roba pronta. Compra continuità, non risparmio." |
| screenshot del testo | 2.700 token | "Per duecento parole. E un'immagine l'agente non la può modificare. Incolla il testo." |
| dare PDF grezzi | paghi due volte | "Il testo della pagina PIÙ l'immagine della stessa pagina. Vedi l'hook nella colonna qui accanto." |
| prompt più corti | lo 0,01% del conto | "Quello che digiti tu è un errore di arrotondamento. I prompt vaghi costano, ma per il lavoro rifatto che innescano." |
| i tool che promettono il 90% | fra zero e negativo | "Li ho provati tutti. Comprimono l'unica parte del conto che non conta, e ti mettono in mezzo uno strato fragile." *(loghi accanto: **Caveman** e **RTK AI**)* |

### Riquadro azzurro — "🔧 UNA CLI INVECE DI UN MCP"
*"il manuale di un MCP entra in contesto anche se quel tool non lo usi"*

| MCP: il manuale entra all'avvio | CLI: zero finché non la chiami |
|---|---|
| GitHub 26.000 · Slack 21.000 | il comando non occupa niente |
| resta lì anche da spento | una riga in CLAUDE.md e sa che esiste |
| l'indice cresce a ogni tool | è un fatto architetturale |

Barra "quanto pesa in contesto, prima che tu scriva": **MCP 26.000** · **CLI ~40 token, e solo
quando serve**.

Nota gialla: *"Il taglio più grosso della lista sta qui, e non è un tool: è scegliere un altro
modo di collegare le cose. Verifica sempre che /context dica 'deferred': vuol dire che i manuali
restano zitti finché non servono."*

### Riquadro arancio — "🔍 IL GRAFO DEL CODICE"
*"CodeGraph e Graphify: due mestieri diversi, e una soglia sotto cui non conviene nessuno"*

| senza grafo cerca a tentoni | con il grafo, una domanda sola |
|---|---|
| apre un file, non è quello | chiede alla mappa dov'è |
| ne apre altri cinque | va dritto al nodo giusto |
| ogni apertura resta in contesto | il file poi lo legge lo stesso |

- **CodeGraph**: "il sensore residente per il CODICE: si indicizza da solo e un watcher lo tiene
  aggiornato."
- **Graphify**: "la torcia per un BRAIN: PDF, immagini, markdown, output Obsidian. Ma il grafo te
  lo costruisce un agente, e lo paghi."
- Nota gialla: *"Sotto i ~500 file non conviene nessuno dei due: il grafo costa più di quello che
  ti fa risparmiare. Non lo dico io: i manutentori di CodeGraph lo scrivono nel loro README, su un
  repo da 102 file il tool consuma più del nativo."*

### Riquadro verde — "⚙️ TRASFORMA IN CODICE"
*"quello che non ha bisogno di un modello non deve pagarlo"*

| lo rifà l'AI, ogni volta | → *lo fai scrivere UNA volta sola* → | lo fa uno script |
|---|---|---|
| paghi token a ogni giro | | zero token, sempre |
| ogni tanto sbaglia | | non sbaglia mai |
| il risultato cambia | | gira uguale ogni volta |
| **~2.000 token a giro** | | **0 token** |

Nota gialla: *"**L'AI serve per il GIUDIZIO. Tutto il resto è esecuzione, e l'esecuzione ripetibile
è codice.** Come si trova cosa trasformare: lancia il prompt di audit e fatti dire quali pezzi del
tuo flusso non hanno bisogno di un modello. Quelli diventano uno script dentro la skill, e da lì in
poi non li paghi mai più. Ogni 'ricordati di' è un candidato hook: è l'unica categoria di consiglio
che sopravvive al fatto che te ne dimentichi."*

### Riquadro viola — "👥 I SUB-AGENTI SPOSTANO [il conto]"
*"non risparmiano: guarda i due conti, non solo quello che vedi tu"*

| quello che vedi tu | il conto vero |
|---|---|
| **tornano 420 token** | il suo system prompt — 2.400 |
| | la sua copia della memoria — 1.400 |
| | i suoi strumenti e permessi — *(cifra non leggibile)* |
| | la lettura vera e propria — 6.000 |
| | → **9.800 spesi per risparmiarne 5.700** |

Nota gialla: *"Usali SOLO per le azioni in bulk: quaranta file, dieci fonti, roba di cui ti serve
solo il verdetto. È la condizione che ribalta il conto."* + *"metti i sub-agenti su Haiku, e non
tocca la cache della sessione principale."*

---

## 1.2 Le animazioni originali

### `frame-006` / `frame-185` — il costo che cresce
> **"Tu scrivi una riga. Lui rilegge tutto. Ogni volta."**
> "I modelli non hanno memoria. A ogni invio il modello si rilegge la conversazione dall'inizio per
> poterti rispondere: il tuo contesto, tutte le sue risposte, ogni file aperto. Tu scrivi sempre la
> stessa quantità. Quello che rilegge lui cresce a ogni turno."

TURNO 2 → messaggio **180 token**, rilegge **360 token**. TURNO 3 → **180** / **540**.
Istogramma a scalini crescenti.

### `frame-283` — il CLAUDE.md
> **"Il CLAUDE.md è un *indice*, non un documento."**
> "Si rilegge **a ogni messaggio**, per tutta la conversazione. Con uno da 4.000 token, ogni
> conversazione parte da 4.000 token indietro. E poi li ripaga."

Confronto: "CLAUDE.md come documento — **4.000 TOKEN**" vs "CLAUDE.md come indice — **450 TOKEN**".
In basso: "6 MESSAGGI" → **24.000**. Piè di pagina: "La regola dai doc di Anthropic: sotto le 200
righe."

### `frame-574` — il grafo
> **"Senza grafo cerca *a tentoni*. E ogni tentativo resta in contesto."**
> "Apre un file, non è quello. Ne apre altri cinque. Ogni apertura entra nel contesto e ci resta,
> anche quella sbagliata. Con un grafo fa una domanda sola."

Contatore CONTESTO sul pannello "Senza grafo": **3480**. Pannello "Con il grafo": grafo esagonale
di nodi, contatore non leggibile. Piè di pagina: "Vale sopra i ~500 file. Sotto, il grafo costa più
di quello che ti risparmia, e lo scrive il manutentore stesso nel README."

---

## 1.3 Il pannello `/usage` (`frame-073`, 3:36) — letto per intero

```
Limite di 5 ore                Si ripristina tra 4 h 46 min          1%
Settimanale · tutti i modelli  Si ripristina mer 18:00              24%
Settimanale · Fable                                                  0%
Questa sessione:  Costo 0,00 USD  ·  Attivo 2s

Cosa sta usando i tuoi limiti?   [24h] [Tutto]
Ultime 24h · misure approssimative e sovrapposte · solo questo computer, escluso claude.ai

  93%  eseguito oltre 150k di contesto
  30%  eseguito mentre 4+ sessioni erano in parallelo

  /reel-editor      Competenza   29%
  /apple-design     Competenza    2%
  /resource-page    Competenza    1%
  /post-all         Competenza    1%
  /repurpose        Competenza    1%

Suggerimento: Le sessioni piu' lunghe sono piu' costose anche con la cache.
Usa /compact a meta' attivita', /clear quando passi a nuove attivita'.
```

**Il suggerimento in fondo raccomanda `/compact`, cioè esattamente il comando che il video
definisce "la cavolata più grossa". L'autore non lo nota e non lo confuta.**

## 1.4 Il selettore modelli (`frame-110`, 5:27)

```
Modelli:   Fable 5 (1)   ·   Opus 5 ✓ (2)   ·   Sonnet 5 (3)   ·   Haiku 4.5 (4)   ·   Altri modelli >
Modalita' rapida: Abilita la modalita' veloce   [on]
Finestra di contesto:  59.5k / 1M  (6%)
Indicatore in basso a destra:  Opus 5 | Extra
```

## 1.5 L'hook PDF (`frame-385`, 19:12) — la schermata più riusabile

```
File:      ~/.claude/hooks/pdf-read-as-text.py
Registrato in ~/.claude/settings.json come PreToolUse, matcher: Read, globale su tutti i progetti

Quando fa Read su un .pdf:
  1. estrae il testo con  pdftotext -layout
  2. lo mette in cache in ~/.claude/pdf-text-cache/<nome>.<hash>.txt
  3. riscrive il file_path verso quel .txt
     -> Claude legge testo, le pagine non entrano in contesto come immagini renderizzate

Test live mostrato:  permissionDecision: allow
                     "PDF -> testo (1 pag, ~1.296 token di immagini risparmiati)"

Si tira indietro da solo:
  - testo estratto sotto 200 caratteri per pagina (scansioni, slide tutte immagini)
  - pdftotext assente o in errore
  -> in quel caso passa il PDF originale

Override quando serve il visivo:  touch ~/.claude/pdf-visual-once
  l'hook consuma la sentinella e lascia passare l'originale UNA volta sola

Limite dichiarato a schermo: sui PDF a piu' colonne, pdftotext appiattisce le colonne
```

## 1.6 La ricerca che è la fonte della cifra sui PDF (`frame-353`, 17:36)

```
Query Google:  claude code quanti token consuma per ogni pagina di un pdf

>> AI Overview (riassunto generato da Google) <<
"In genere, ogni pagina di un documento PDF elaborato da Claude Code consuma
 tra i 1.500 e i 3.000 token."          [chip di citazione: GitHub]

- Elaborazione multimodale: le pagine vengono convertite e analizzate considerando
  sia la parte testuale che quella visiva/strutturale (immagini e layout).
                                        [Reddit · r/ClaudeAI +1]
- Costi extra (Overhead): in Claude Code l'uso del tool di lettura (Read) su file PDF
  aggiunge un carico supplementare che puo' aumentare i token totali rispetto al testo puro.
                                        [Reddit · r/ClaudeAI]   <- freccia verde disegnata a mano
- Consiglio per risparmiare: se il PDF contiene solo testo, convertirlo preventivamente
  in Markdown riduce il consumo (spesso del 50% o piu').
                                        [Medium · Vivek Singh P... +1]

Risultati organici in colonna destra (entrambi Reddit r/ClaudeAI):
  "Sto raggiungendo i limiti di Claude quasi subito. Ormai e' inutile."   5 Jan 2025
  "I tested PDF token usage Claude Code vs Claude.ai"                    25 Jan 2026
```

**Catena della fonte: relatore → AI Overview di Google → GitHub / Reddit / Medium. Nessuna
documentazione primaria Anthropic.**

## 1.7 La regola editoriale dell'autore (`frame-203`, 10:06)

Risposta di Claude, letta per intero mentre l'autore preparava **questo stesso video**:

> "**Saved final v6 intro and distill rule**
> Salvata come definitiva in `script.md`, la v5 archiviata accanto. 238 parole, circa 75 secondi.
> La scelta di 'DRASTICAMENTE' al posto del numero l'ho scritta come regola in `style.md`, perché
> vale oltre questo video: se il corpo è pieno di numeri misurati, l'intro promette con un
> avverbio, non con una cifra. Una cifra in apertura o è gonfiata, e allora contraddice un video
> che smonta chi promette percentuali, oppure è precisa, e allora non è una promessa ma un
> dettaglio che chi guarda non sa ancora dove mettere. L'avverbio tiene alta la promessa, i numeri
> la dimostrano nei capitoli dove si vedono a schermo.
> Buone riprese."

## 1.8 Le due repo dei grafi

**CodeGraph** — `colbymchenry/codegraph`, pubblica, MIT, **68.8k stelle**, 163 watching, 955 commit.
> "Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini,
> Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls,
> 100% local"
> Sezione "4. No more syncing!": "Auto-sync is enabled by default. CodeGraph watches the project
> and updates the graph on every file change… **The index is never stale, and there is nothing to
> re-run.**"
> Disinstallazione: `codegraph uninstall` (`--keep-cli` per tenere solo la CLI).

**Graphify** — Apache-2.0, **#2 Repository Of The Day**, 162 contributors, Python 100%, downloads 5.7K.
> "Type `/graphify` in your AI coding assistant and it maps your entire project (code, docs, PDFs,
> images, videos) into **a knowledge graph you can query instead of grepping** through files."
> - "**Code maps for free, fully local.** Code is parsed with tree-sitter AST: deterministic, no
>   LLM, nothing leaves your machine. (Docs, PDFs, images and video use your assistant's model, or
>   a configured API key, for a semantic pass.)"
> - "**Every edge is explained.** Each connection is tagged `EXTRACTED` (explicit in the source) or
>   `INFERRED` (resolved by graphify), so you can tell what was read directly from what was inferred."
> - "**Not a vector index.** No embeddings, no vector store: a real graph you traverse."
> Install: `uv tool install graphify` → `graphify install`.

## 1.9 Altre schermate lette

- **`frame-020`/`021` — sito Martes AI**: "**€82.271 generati da un agente AI su WhatsApp**" per
  **Bluvacanze**; altri clienti a schermo: Swiss Natural Med, Truck Italia, Turnover, Shape Up,
  Clinica Oculistica Santa Lucia, Fantozzi & Associati.
- **`frame-067` — Instagram dell'autore**: 134 post, 12.5K follower; bio "Aiuto le aziende italiane
  a integrare l'AI nei loro processi / Founder di Martes AI / 22.5K iscritti YouTube";
  `www.martes-ai.com`.
- **`frame-069` — griglia reel**: "15 STRUMENTI AI COMPLETAMENTE [GRATIS]" 725K · "**70x MENO
  TOKEN**" 53.7K · "23.333 PROMPT" · "CLAUDE CODE" · "CLOUDFLARE".
- **`frame-246`/`250`/`252` — Google "diagrammi ascii"**: ASCIIFlow, Diagon
  (`ArthurSonzogni/Diagon`), ascii-diagram (GitHub Topics), "ASCII and Why Developers Should Use
  ASCII Diagrams — The New Stack".
- **`frame-315`/`333` — second brain dell'autore in VS Code**: `.claude`, `notify`, `obsidian`,
  `superpowers`, `code`, `Context`, `Daily`, `Departments`, `Intelligence`, `Library`,
  `Onboarding`, `outputs`, `Projects`, `reference`, `Resources`, `Team`, `workspaces`,
  `.claudeignore`, `.env`, `.gitignore`, `CLAUDE.md`, `index.md`. Nel CLAUDE.md aperto: sezioni
  "# Organizzazione", "## Regola" numerate fino a 23/24, e "# Anti-Pattern".
- **`frame-481` — README di caveman**: "why using many token when few do trick / Original skill
  made agents say less. Caveman 2 makes them read less too. / **33.2% fewer provider-reported input
  tokens** in a pinned Claude Code benchmark. / Keep your agent. Brain big. Context small."
  Esempio: "Normal agent — 69 tokens" vs "Caveman agent — 19 tokens". `npm install -g @caveman-ai/cli`.
- **`frame-566` — Supabase MCP Server (doc ufficiale)**: warning "Connecting an LLM to your
  Supabase projects carries security risks. Read our security best practices before running the
  MCP server."
- **`frame-334` — diagramma ASCII di esempio**: contiene numeri di un **ALTRO** lavoro dell'autore
  (test sui plugin): `p = 0.004`, `10 task -30% → 86 task -8,5%`, `/clear fra un task e l'altro
  -17,9%`, `CLAUDE.md 500-600 token -8,5%`, "la trappola dei test piccoli", "QUELLO CHE BATTE I
  PLUGIN, E NON SI INSTALLA". **NON sono misure di questo video** e non sono entrate in atoms.json.

---

# PARTE 2 — Trascrizione integrale (950/950 righe, 100%)

[00:00:01] In questo video ti faccio vedere come
[00:00:04] tagliare drasticamente il consumo dei
[00:00:07] token di Cloud Code con 10 mosse. Sono
[00:00:09] gratis, le implementi oggi stesso e la
[00:00:12] prima funziona in 10 secondi. La vediamo
[00:00:14] una per una, passo dopo passo e per
[00:00:16] ognuna voglio farti vedere anche un
[00:00:18] confronto visivo dei token che vai a
[00:00:20] risparmiare e per quale motivo la
[00:00:23] tecnica funziona. E poi c'è la parte che
[00:00:25] nessuno ti dice. Infatti, verso la fine
[00:00:27] di questo video andrò a vedere quali di
[00:00:29] queste strategie portano delle
[00:00:31] conseguenze, perché in alcuni casi
[00:00:33] andare a risparmiare sui token porta una
[00:00:35] ripercussione magari sulla qualità
[00:00:37] dell'output. Stessa storia per i trucchi
[00:00:39] e i tool famosi che ti consigliano in
[00:00:43] giro promettendoti di risparmiare il 90%
[00:00:45] dei tuoi token. Molti sono fuffa e
[00:00:47] alcuni peggiorano solamente la
[00:00:49] situazione. Ti dico anche quali sono e
[00:00:51] il motivo per il quale non funzionano.
[00:00:52] Se è la prima volta che vedi questi
[00:00:54] video, sono un ingegnere informatico e
[00:00:57] gestisco Mart, un'azienda attraverso la
[00:00:58] quale aiutiamo le imprese a scalare
[00:01:00] implementando l'intelligenza artificiale
[00:01:02] all'interno dei loro processi. Partiamo
[00:01:04] con la formazione di tutto il loro team
[00:01:07] su strumenti pratici come Cloud Code,
[00:01:10] Cloud Cowork, Codex per poi diventare il
[00:01:12] loro partner strategico, nel senso che
[00:01:13] andiamo ad analizzare i loro processi
[00:01:16] per poi andare a costruire soluzioni AI
[00:01:19] customizzate in base alle loro esigenze.
[00:01:20] Senza perdere altro tempo direi di
[00:01:22] passare subito al video. Ho preparato
[00:01:24] come al solito, una lavagna dove andiamo
[00:01:27] a coprire punto per punto, comprendendo
[00:01:29] davvero ogni tecnica, che cos'è, come
[00:01:31] funziona e perché funziona. Ma prima di
[00:01:33] toccare qualsiasi cosa, gli strumenti di
[00:01:36] misurazione che sono indispensabili sono
[00:01:39] tre, sono/usage
[00:01:41] e la status line, sono nello specifico
[00:01:44] dentro cloud code e slashcectext
[00:01:47] a vedere la quanta finestra di contesto
[00:01:49] abbiamo occupato. Ogni modello ha la
[00:01:51] finestra di contesto, cioè quanto input
[00:01:53] può prendere dentro, no? Opus nello
[00:01:55] specifico ha un milione di token. Sonet
[00:01:57] se non sbaglio, sta ancora a 200.000.
[00:01:59] Quindi questo è un modo per misurare.
[00:02:01] Una cosa che pochissima gente sa è che
[00:02:02] adesso sono sulla nuova chat, vedete,
[00:02:04] non ho scritto nulla, sto andando giù
[00:02:06] su, non ho scritto nulla, non ho scritto
[00:02:09] nulla e sto già al 6% dello usage. Ho
[00:02:12] già occupato 60.000 token. Questa è una
[00:02:13] cosa che la gente non sa e se vi
[00:02:16] chiederete "Ma come 6% non hai mandato
[00:02:18] neanche un messaggio?" Beh, perché ci
[00:02:22] sono i file di memoria, il system prompt
[00:02:24] che è il cloud. MD, i server MCP.
[00:02:26] Infatti, ogni volta che noi carichiamo
[00:02:28] un server MCP occupa memoria, anche se
[00:02:30] poi non lo usiamo. Abbiamo anche le
[00:02:33] skills, quindi come regola bisogna stare
[00:02:35] fra il 3 e il 6%, io sto proprio al
[00:02:37] limite. Quando fate slash context su una
[00:02:39] nuova conversazione. Molti dei nostri
[00:02:40] clienti quando partono con slashce
[00:02:42] context andiamo a vedere che stanno già
[00:02:44] al 20% e poi si chiedono perché
[00:02:46] consumano i loro token in un batter
[00:02:49] d'occhio. Secondo comando fondamentale è
[00:02:52] slusage. Ci fa vedere a che livello
[00:02:55] siamo dello usage. solo i limiti delle 5
[00:02:57] ore settimanali di Fable, ma ci dice
[00:03:00] anche come stiamo usando i nostri limiti
[00:03:03] e le skill che consumano di più. Io ho
[00:03:07] consumato il 93% oltre il 150.000 token
[00:03:10] nella finestra di contesto e il 30% con
[00:03:13] quattro più sessioni in parallelo. La
[00:03:15] skill che mi consuma più di tutti è la
[00:03:17] mia skill Real Editor. Questo perché io
[00:03:19] ho questo mio profilo Instagram che
[00:03:22] essenzialmente va quasi in autopilota,
[00:03:24] nel senso tutti i reel che vedete qua
[00:03:25] che fanno anche i bei numeri sono tutti
[00:03:28] quanti editati e postati automaticamente
[00:03:29] dalle AE. Io li registro, io faccio la
[00:03:32] ricerca dei contenuti, però queste
[00:03:33] questo edit che state vedendo qua me lo
[00:03:36] fa Cloud. Un'altra cosa molto
[00:03:37] importante, se utilizzate le app di
[00:03:39] Cloud da desktop, basta avanzano questi
[00:03:41] questi comandi qua. Un'altra cosa
[00:03:42] interessante è vedere qui in basso a
[00:03:44] destra abbiamo il la finestra di
[00:03:46] contesto e il limite direttamente qui in
[00:03:48] questo pallino, ma se usate Cloud
[00:03:50] all'interno del terminale, come spesso
[00:03:52] piace fare a me, potete personalizzare
[00:03:55] questa cosa che si chiama status line e
[00:03:57] io ad esempio l'ho personalizzata così,
[00:03:58] cioè qua posso vedere quanto il mio
[00:04:01] contesto occupato, qua posso vedere il
[00:04:02] mio limite della sessione, qua il mio
[00:04:04] limite settimanale. Mi piace vederlo
[00:04:06] così con questi colori. Se volete anche
[00:04:08] voi un setup come questo, basta che fate
[00:04:10] lo screenshot a questo video, questa
[00:04:12] sezione qua di teclada, mi personalizzi
[00:04:16] la status line in modo tale da aver da
[00:04:18] averla così e l'equivalente di quella
[00:04:19] status line è questa cosetta qua
[00:04:22] nell'app. Bene, quindi elevati eh questi
[00:04:24] strumenti di misurazione, partiamo con
[00:04:27] quel con quelle tecniche che si possono
[00:04:29] utilizzare da subito, che sono quelle
[00:04:32] spesso noiose, ma che funzionano meglio.
[00:04:34] Prima di tutto slash clear ad ogni
[00:04:36] cambio di task. Ogni volta che c'è un
[00:04:38] task diverso, che sia una nuova
[00:04:40] funzionalità nell'app, che sia una nuova
[00:04:42] richiesta di cloud che non c'entra con
[00:04:44] quello che abbiamo detto, fate slash
[00:04:46] clear che vi riazzera la cronologia
[00:04:48] nella conversazione. Faccio un esempio,
[00:04:49] mettiamo caso che qua a questa
[00:04:51] conversazione gli dico "Ciao, come
[00:04:53] stai?" Con "Ciao, come stai?" Sono
[00:04:57] arrivato al 15% già della mia finestra
[00:05:01] del contesto. Se faccio slash clear la
[00:05:03] conversazione riparte da zero e come
[00:05:05] vedete se poi digito slash context dopo
[00:05:07] che faccio slash clear si riparte.
[00:05:10] Dovrebbero ripartire da quel 6% là.
[00:05:12] Eccoci qua. Quindi, senza che
[00:05:14] necessariamente dovete aprire una nuova
[00:05:16] chat, qui fate slash clear e si riparte
[00:05:19] per ogni nuovo task noioso, ma funziona.
[00:05:22] Poi modello ed effort scelti una volta
[00:05:25] sola, sola all'inizio della chat. Noi
[00:05:27] all'inizio della chat possiamo decidere
[00:05:29] il modello piuttosto che l'effort.
[00:05:32] Possiamo mettere l'effort basso, medio,
[00:05:36] alto, extra, max, ultra code e questo
[00:05:38] diciamo è se dobbiamo fare del lavoro
[00:05:40] estremamente estremamente potente. Uno
[00:05:43] degli errori più spessi che vedo è che
[00:05:45] nel bel mezzo della conversazione si
[00:05:46] cambia il modello o si cambia l'effort.
[00:05:48] Che succede? è come se andassimo a
[00:05:51] scegliere un nuovo cervello. Per passare
[00:05:53] a un nuovo cervello, quel cervello deve
[00:05:54] avere il contesto di tutta la
[00:05:56] conversazione, no? Quindi dobbiamo
[00:05:57] ripassare tutta quanta la conversazione,
[00:05:59] quello che abbiamo fatto al nuovo
[00:06:01] cervello e questo che vuol dire? Consumo
[00:06:03] di token, quindi scegliere il modello e
[00:06:05] l'effort solo all'inizio della
[00:06:09] conversazione, mi raccomando. Altra cosa
[00:06:11] slashca compact, questa è la cavolata
[00:06:14] più grossa che si legge in giro, cioè
[00:06:16] Compact viene valutato come un ottimo
[00:06:18] strumento di cloud per chi sai
[00:06:19] essenzialmente che cosa fa Compact.
[00:06:20] Quando arriviamo a un certo punto della
[00:06:22] conversazione, mettiamo caso siamo
[00:06:24] arrivati all'80% del contesto, la
[00:06:26] compattiamo, cioè andiamo Cloud si va a
[00:06:28] prendere i punti salienti della
[00:06:29] conversazione così che possiamo
[00:06:32] continuare, così che compattandola
[00:06:34] riusciamo a continuare in quella chat e
[00:06:36] sembra fantastico perché, insomma,
[00:06:37] possiamo continuare su quella stessa
[00:06:39] chat. Spesso Cloud ce lo consiglia anche
[00:06:41] lui, fai compact perché stiamo arrivando
[00:06:44] alla fine del contesto. Compact è una
[00:06:46] cavolata gigantesca, secondo me, per due
[00:06:49] motivi. Spesso non serve fare un
[00:06:51] compact, ma basta fare il rewind. Adesso
[00:06:53] andiamo a vedere che vuol dire. Seconda
[00:06:56] cosa, se lasciamo a Cloud la libertà di
[00:06:58] riassumere la nostra conversazione,
[00:07:00] sceglierà lui cosa riassumere, cosa
[00:07:04] tenere. Quindi la cosa che è decisamente
[00:07:05] migliore è quello di creare un file di
[00:07:07] endoff, si chiama tranquilli, adesso
[00:07:08] andiamo a vedere tutto dove diciamo a
[00:07:11] Cloud questi sono i punti salienti,
[00:07:12] queste sono le cose che voglio portarmi
[00:07:14] nella prossima conversazione perché
[00:07:16] sennò diamo la palla a Cloud, sceglie
[00:07:18] lui cosa mettere, cosa cosa cosa
[00:07:20] riassumere e non lo vogliamo. Mettiamo
[00:07:22] caso che ho questa conversazione dove
[00:07:24] essenzialmente qui dentro quello che ho
[00:07:26] fatto con Cloud è stato aiutarmi alla
[00:07:28] preparazione di questo video. Se fossi
[00:07:31] arrivato, che ne so, a un 50-60% del
[00:07:34] contesto Proip, se arrivi al 40-50%
[00:07:37] del tuo contesto perdi di un sacco la
[00:07:40] qualità. Quindi dopo il 4050%
[00:07:42] cambia chat, se ti serve ancora qualcosa
[00:07:44] creati un file d'andoff. Adesso ti
[00:07:46] faccio vedere come invece di fare
[00:07:49] compact, spesso quello che funziona
[00:07:51] molto meglio è un comando che si chiama
[00:07:53] rewind che ci permette di andare di
[00:07:54] ritornare a un certo punto della
[00:07:56] conversazione senza consumare alcun
[00:07:58] token. Quindi vi faccio vedere come
[00:08:01] funziona. Rewind e mi dice dove puoi
[00:08:03] riavvolgere il nastro. Questo è l'ultimo
[00:08:05] messaggio che gli ho passato. Questo è
[00:08:07] il primo messaggio. Posso riavvolgere il
[00:08:08] nastro a un certo punto della
[00:08:10] conversazione. Quindi, ad esempio, posso
[00:08:12] aggiungerlo qui dove ho detto, "Guarda,
[00:08:13] look del video me lo devi fare più
[00:08:16] forte." Posso cliccare questo, posso
[00:08:17] cliccare un qualsiasi punto della
[00:08:20] conversazione e tornare lì. Ovviamente
[00:08:22] se usi Cloud Code nel terminale o
[00:08:24] all'interno dell'estensione di Visual
[00:08:26] Studio Code è la stessa identica cosa,
[00:08:28] non cambia nulla. Vi faccio vedere.
[00:08:31] rewind e possiamo passare a un qualsiasi
[00:08:34] punto della conversazione, vedete, va a
[00:08:37] riavvolgere il nastro in quel punto là.
[00:08:41] Quindi rewind, non compact. Se proprio
[00:08:43] devi cambiare conversazione e portarti
[00:08:45] dietro delle informazioni senza passare
[00:08:47] la palla a cloud, creati un file di
[00:08:49] handoff. Un file di handoff è un file
[00:08:51] dove diciamo a Cloud ecco a che punto
[00:08:53] siamo arrivati, ecco le problematiche,
[00:08:56] ecco che cosa dobbiamo fare, lo passiamo
[00:08:57] una nuova sessione di Cloud Code così
[00:09:00] lui ha già idea di a che punto siamo
[00:09:02] arrivati. possiamo aprire una nuova
[00:09:03] sessione, quindi ripartendo da zero,
[00:09:05] essenzialmente, senza consumare token, e
[00:09:09] gli passiamo noi eh le informazioni che
[00:09:10] vogliamo avere nella prossima
[00:09:12] conversazione, perché una cosa
[00:09:14] fondamentale da capire è questa
[00:09:16] animazione qui. Cioè, ogni volta che noi
[00:09:18] andiamo a mandare un messaggio, il
[00:09:21] nostro messaggio pensiamo vabbè, ma sono
[00:09:23] pochi token, no? Questo è questo è il
[00:09:25] messaggio singolo che mando, questo è il
[00:09:26] messaggio singolo che mando, no? Questo
[00:09:28] è il singolo messaggio che mando. Il
[00:09:29] problema è che ogni volta che ci
[00:09:32] risponde lui si va a rileggere tutto ciò
[00:09:34] che è successo prima. Quindi, mettiamo
[00:09:36] caso, questo è il secondo messaggio.
[00:09:38] Cloud si va a rileggere quello che ha
[00:09:40] detto prima, in più ci dice ci mette la
[00:09:42] nuova risposta. Poi ci deve essere una
[00:09:44] nuova risposta. Emma si va a leggere
[00:09:46] ogni volta quello che è successo prima,
[00:09:48] quindi ogni volta è come se fosse
[00:09:49] esponenziale. Vedete, ogni nuovo
[00:09:51] messaggio che gli passiamo, lui si va a
[00:09:54] leggere tutto prima, tutta la storia, la
[00:09:57] la conversation history, la cronologia,
[00:10:00] motivo per il quale Rewind è
[00:10:02] estremamente intelligente. Vediamo ora
[00:10:03] come funziona il file di endoff. o gli
[00:10:05] diciamo semplicemente creiamo un file di
[00:10:08] endoff in cui Mirenki le problematiche
[00:10:09] che abbiamo avuto, come le abbiamo
[00:10:12] risolte, concentrati su questo piuttosto
[00:10:14] che quello, piuttosto che io, ad
[00:10:16] esempio, ho creato eh una skill che si
[00:10:19] chiama slash andandof che avrete eh qui
[00:10:21] sotto nel secondo link in descrizione,
[00:10:22] c'è il link a tutti quanti i miei
[00:10:23] template che potete prendere
[00:10:24] tranquillamente, vi potete scaricare
[00:10:26] anche questa skill. Vi faccio vedere. Ho
[00:10:28] riaperto un'altra chat a caso. Se io
[00:10:30] faccio slashendof,
[00:10:32] guardate che cosa mi chiede. Ci fa delle
[00:10:34] domande chiedendo quali sono quelle cose
[00:10:36] che ci vogliamo portare in una prossima
[00:10:37] chat di Cloud Code. Quindi io spesso
[00:10:39] quello che faccio, siccome so che questa
[00:10:41] skill quando la invoco mi chiede quali
[00:10:42] sono le cose che ti vuoi portare, faccio
[00:10:44] nella prossima sezione faccio slash
[00:10:46] andandof, focalizzati sui problemi che
[00:10:48] abbiamo avuto, come li abbiamo risolti
[00:10:50] su questa cosa e su questa cosa e e poi
[00:10:52] mi dà un file che me lo incolle in
[00:10:54] un'altra chat. Comunque
[00:10:55] in questo caso Cloud ci chiede ad
[00:10:57] esempio su cosa ci vogliamo concentrare.
[00:10:59] Mi voglio concentrare su questo, ad
[00:11:02] esempio. Ecco che mi scrive il il mio
[00:11:04] file di endoff. Nel file di handoff mi
[00:11:07] mette sempre l'obiettivo, a che punto
[00:11:08] siamo, cosa abbiamo provato che non ha
[00:11:11] funzionato, i problemi incontrati e come
[00:11:13] li abbiamo risolti, decisioni prese,
[00:11:14] file toccati, dove vogliamo andare.
[00:11:17] Quindi basta copiare questo file qui,
[00:11:19] aprire la nuova sessione e fare
[00:11:19] continuiamo
[00:11:25] quello che stavamo facendo nella scorsa
[00:11:26] sessione.
[00:11:30] Incolliamo e si parte. Questo è molto
[00:11:31] più efficiente di continuare una
[00:11:33] sessione all'infinito proprio per questo
[00:11:34] ragionamento qui, per non parlare della
[00:11:37] qualità in più che andiamo ad ottenere
[00:11:40] facendo un mero compact. Altra cosa
[00:11:41] fondamentale, questo non l'ho visto
[00:11:44] quasi da nessuna parte, farsi fare un
[00:11:47] diagramma ashi, asi, chiamatelo come vi
[00:11:49] pare, prima di costruire qualsiasi cosa
[00:11:51] eh che sia grafico. Mi spiego meglio.
[00:11:52] Quando andiamo a costruire un qualcosa
[00:11:55] di grafico, che sia questa lavagna
[00:11:58] piuttosto che un front-end, spessissimo
[00:12:00] che succede? Vai Clode, voglio costruire
[00:12:02] questo, questo, questo e questo.
[00:12:04] Costruisce tutto quanto. Il risultato
[00:12:06] non ci piace. Cloud cambia questo.
[00:12:08] Cloud, questo mettilo più in alto.
[00:12:09] Cloud, questo mettilo in basso a destra.
[00:12:12] Cloud cambia il font. Soluzione i
[00:12:12] diagrammi
[00:12:16] asci. essenzialmente sono dei diagrammi
[00:12:18] che costano pochissimo a Cloud fare
[00:12:20] perché sono delle lineette, dei trattini
[00:12:23] e con queste lineette, questi trattini
[00:12:25] Cloud ci presenta un po' l'interfaccia
[00:12:27] come verrà fuori, così che prima di
[00:12:30] andare a costruire qualcosa ci facciamo
[00:12:31] prima fare un diagrammino e già dal
[00:12:33] diagrammino capiamo se lo stile ci
[00:12:35] piace. ad esempio una skill che mi
[00:12:36] prepara le lavagne come quella che
[00:12:38] vedevamo prima e questo è un esempio.
[00:12:40] Quando vado a generare la lavagna, ecco
[00:12:42] che mi dà prima la preview della
[00:12:45] lavagna, così che senza che me la va a
[00:12:47] generare sprecando token, gli posso dire
[00:12:48] "No, guarda, questo non mi piace,
[00:12:50] cambia". No, guarda quest'altro, fallo
[00:12:52] così, fallo col là. Ho fatto anche un
[00:12:53] altro esempio, gli ho detto "Guarda,
[00:12:55] voglio che mi crei un e-commerce per i
[00:12:57] miei prodotti shampoo". E
[00:12:59] automaticamente quello che fa è mi fa
[00:13:01] vedere la homepage come la farebbe con
[00:13:05] le immagini, la la hero section. Questo
[00:13:08] qua sono è la nav,
[00:13:11] la scheda prodotto, cosa farebbe? borsa,
[00:13:13] mobile. Quindi prima di andare a
[00:13:15] generare qualsiasi cosa, posso
[00:13:17] automaticamente cambiare le cose qua
[00:13:18] senza sprecare i codici inutilmente.
[00:13:20] Quindi una cosa che vi consiglio di fare
[00:13:22] è che in ogni skill che avete per il
[00:13:24] design metteteci uno step prima che vi
[00:13:26] consente di avere un diagramma Ashi
[00:13:29] prima di generare qualsiasi cosa. Poi
[00:13:30] andiamo a vedere quelle tecniche che
[00:13:32] devi fare una volta e una volta che lo
[00:13:36] fai poi eh sei pronto a procedere. Il
[00:13:38] primo è quello di spegnere gli MCP che
[00:13:39] non utilizzi, proprio perché, come
[00:13:41] vedevamo prima, se fai slash contact
[00:13:43] senza aver neanche mandato un messaggio,
[00:13:46] comunque gli MCP occupano spazio. Per
[00:13:49] farlo è semplicissimo, basta che vai su
[00:13:52] eh fai slp, ti si appaiono tutti gli MCP
[00:13:55] e quelli che non utilizzi li eh li
[00:13:58] elimini. Essenzialmente questo da solo
[00:14:00] ti garantisco che ti salverà un sacco di
[00:14:03] token. Altra cosa, il cloud.md MD come
[00:14:05] indice. Quello che vogliamo, appunto,
[00:14:08] non è un documento, ma trattare questo
[00:14:10] Clode MD come se fosse un indice. Il
[00:14:12] cloud.md, MD, per chi non lo sapesse, è
[00:14:15] un prompt che Clode si va a leggere ad
[00:14:18] ogni messaggio. Anche prima di aver
[00:14:19] mandato qualsiasi altra cosa, come
[00:14:20] avevamo visto prima con slashce context,
[00:14:24] si va a leggere quel prompt si chiama,
[00:14:26] se lo legge ad ogni messaggio per tutta
[00:14:27] la conversazione. Quindi se il nostro
[00:14:30] Cloud MD è gigantesco e per leggerlo si
[00:14:32] consumano 4.000 token, capite bene che
[00:14:34] magari dopo 8 messaggi abbiamo consumato
[00:14:36] 32.000 token così, mentre se fosse
[00:14:39] semplicemente un indice, quindi 450
[00:14:43] token, dopo 8 messaggi stiamo a 3600 di
[00:14:45] token. La regola dal doc di Antropic
[00:14:47] dice di tenere il cloud MD sotto le 200
[00:14:49] righe e trattare semplicemente come un
[00:14:52] indice. Il Clode MD deve dire a Cloud:
[00:14:53] "Ok, questa cartella fa questo, cioè poi
[00:14:55] c'è questa cartella che fa questo,
[00:14:57] eccetera eccetera". Ad esempio, nel mio
[00:14:57] second
[00:15:02] è questo qui. Come vedete non è
[00:15:05] nient'altro che un indice, cioè qua
[00:15:07] andiamo a dirgli, guarda, in questa
[00:15:09] cartella ci sono preferenze stile
[00:15:11] abitudini, qua ci sono strutture,
[00:15:13] organizzazioni infaziendali, eccetera
[00:15:17] eccetera e stiamo sulle 166 righe. Altra
[00:15:19] cosa che forse questa del cloud. MD come
[00:15:22] indice la sapevate, ma questa, ossia
[00:15:24] usare il cloud. MD come cartella non è
[00:15:27] per niente banale, scusate, un Cloud MD
[00:15:30] per ogni cartella. Mi spiego meglio.
[00:15:31] Questo è un è un trucco che viene
[00:15:34] direttamente da Andrew Carpati, uno dei
[00:15:35] membri fondatori di Openi, adesso sta ad
[00:15:38] Antropic, ha inventato tutto il concetto
[00:15:41] di second brain con l' LLM wiki. Una
[00:15:45] cosa che vi consiglio tantissimo di fare
[00:15:52] Tale che il cloud. MD generale funge da
[00:15:54] indice e poi quando, che ne so, che io
[00:15:57] gli faccio una domanda su Painpoint di
[00:16:00] un mio cliente con il cloud. Sa che deve
[00:16:02] accedere a questa cartella qua, Context,
[00:16:04] e solamente poi quando va a accedere a
[00:16:08] context qui dentro ci sarà un altro
[00:16:10] cloud. MD. Quest'altro Cloud MD va a
[00:16:13] spiegare i vari file che ci sono
[00:16:14] all'interno della mia cartella di
[00:16:16] contesto. Qui poi andiamo a mettere le
[00:16:19] regole eccetera eccetera. Ma in questo
[00:16:22] modo non andiamo a caricare il cloud.d
[00:16:24] generale con tantissime informazioni.
[00:16:27] Mettiamo un clode. MD per ogni cartella.
[00:16:28] Ogni mia cartella ha un cloud. MD. Che
[00:16:32] ne so. Apro risorse. Queste risorse ha
[00:16:35] un clode. MD. Ogni mia cartella ha un
[00:16:37] clode. MD. Non vi spaventate se io
[00:16:39] utilizzo l'estensione di visual Sudo
[00:16:41] Code. Questa è l'excalro che mi ha
[00:16:44] mandato prima anche qui all'interno eh
[00:16:46] dell'Aptic Clode va va alla grande. Poi
[00:16:48] altra cosa, archiva le skill che non
[00:16:50] utilizzi e accorcia e accorcia le
[00:16:53] descrizioni. Come abbiamo visto prima,
[00:16:54] con slash contact si vanno a caricare
[00:16:56] tutte le skill, quindi quelle che non
[00:16:58] usi consumano token, e vai ad accorciare
[00:17:01] le descrizioni. Basta chiederlo a Cloud,
[00:17:04] guarda Cloud, voglio accorciare le
[00:17:05] descrizioni delle main skill per
[00:17:08] sprecare meno token, poi vammi a fare un
[00:17:10] test end to end per vedere che le skill
[00:17:12] funzionano comunque alla grande. Lo puoi
[00:17:14] fare anche volta per volta, questo
[00:17:17] tranquillamente, però questo ehm è una
[00:17:20] cosa che fai una volta
[00:17:23] e eh aiuta tantissimo. Altra cosa,
[00:17:25] diciamo che questa è una cosa di cui
[00:17:28] vado abbastanza fiero, nel senso che una
[00:17:31] cosa che spende tantissimo, che brucia
[00:17:34] tantissimo token, sono i PDF che
[00:17:36] carichiamo a Cloud. Ogni pagina di un
[00:17:39] documento PDF elaborato con Cloud code
[00:17:41] consuma tra i 1500 e 3000 token.
[00:17:44] Immaginatemi un PDF di 100 pagine, 200
[00:17:47] pagine, 1000 pagine. Quindi molto spesso
[00:17:49] a noi serve solamente il contenuto del
[00:17:51] documento. Questo metodo che andremo a
[00:17:52] vedere è ottimo se ci serve il
[00:17:54] contenuto, se ci servono le immagini, i
[00:17:56] grafici è un'altra storia, carichiamo
[00:17:58] solamente quella e basta. Avanza. Ma
[00:18:00] siccome nell'80% dei casi ci serve il
[00:18:03] testo, ho costruito un hook che mi va a
[00:18:05] prendere il PDF e mi estrae il testo.
[00:18:07] Cosa diavolo è un hook? Che cosa ho
[00:18:10] appena detto? Spiego meglio. UNUC è una
[00:18:12] regola deterministica di Cloud che
[00:18:14] possiamo far attivare ogni qualvolta
[00:18:16] succede un determinato evento. Mi spiego
[00:18:18] meglio ancora. Noi possiamo imporre
[00:18:21] delle condizioni deterministiche a un
[00:18:23] if, per capirci. Ogni qual volta succede
[00:18:26] qualcosa. Ogni volta che carico un PDF
[00:18:28] deve succedere questo. Ogni volta che
[00:18:31] crei un file deve succedere quello. Ogni
[00:18:33] volta che faccio una chiamata API deve
[00:18:36] succedere questo. Esempi di UK sono ogni
[00:18:39] volta che creo un file sincronizzami con
[00:18:42] il mio Drive, Google Drive, Gitab, così
[00:18:44] che quel file che mi hai creato sta
[00:18:46] anche nel mio nel mio nel mio Drive, nel
[00:18:49] mio cloud, piuttosto che ogni volta che
[00:18:51] carico un documento vammi a controllare
[00:18:54] se ci sono delle informazioni manevole
[00:18:56] perché magari c'è un prompt injection.
[00:18:57] Quello che ho fatto io, ho creato un
[00:19:00] hook che ogni volta che carico un PDF mi
[00:19:02] va a eseguire uno script, un codice, uno
[00:19:06] script di Python che mi estrae il testo.
[00:19:08] Non si va a leggere ogni pagina perché
[00:19:09] se si andasse a leggere ogni pagina si
[00:19:11] va a estrapolare solamente il testo.
[00:19:14] viene spiegato meglio, cioè c'è questo
[00:19:18] hook che ogni volta che carico un ehm un
[00:19:20] documento, quindi quando Cloud deve fare
[00:19:23] una read, va a eseguire questo script
[00:19:27] PDF read che essenzialmente mi estrae il
[00:19:29] testo e si legge solamente questo testo,
[00:19:33] non il PDF e questo si attiva ogni volta
[00:19:35] che gli carico un PDF. Nel secondo link
[00:19:37] in descrizione, oltre alla skill di
[00:19:39] Handoff, vi lascio anche il prompt che
[00:19:41] potete incollare per costruirvi voi
[00:19:43] stessi questo hook. Vi garantisco che
[00:19:45] questo è veramente una mano dal cielo,
[00:19:47] non sapete quanti token mi ha fatto
[00:19:49] risparmiare. Io ho fatto diversi test,
[00:19:51] se non mi credete fateli anche voi, dove
[00:19:53] essenzialmente ho caricato un PDF da 300
[00:19:57] pagine. Con il Reid ho speso circa
[00:20:00] 500-600.000 token dove il read non è
[00:20:02] nient'altro che ho passato il PDF, Cloud
[00:20:04] se l'è letto tutto. Con il mio hook ho
[00:20:07] eh speso 150.000 token, quindi risparmi
[00:20:10] dalle 3:00 alle 4:00 volte. È tantissima
[00:20:12] roba. Secondo il link in descrizione
[00:20:15] trovi il tra tutte le mie risorse il
[00:20:17] promptarti anche tu questo hook. Copi il
[00:20:19] prompt, te lo passi su Cloud Code, è una
[00:20:22] cavolata. Ok, andiamo poi a vedere la
[00:20:24] questione dei modelli, eh, perché la
[00:20:26] qualità stessa del modello che scegliamo
[00:20:28] è essa essa stessa un risparmio, nel
[00:20:32] senso che quando si fa coding e comunque
[00:20:33] si va a costruire un qualcosa di
[00:20:36] estremamente complesso resta sul modello
[00:20:38] di frontiera. Ho fatto anche un video su
[00:20:40] come utilizzare Cloud Code gratis e la
[00:20:42] cosa che essenzialmente dico anche là è
[00:20:43] se devi fare i task estremamente
[00:20:46] complessi non usare il modello chip, non
[00:20:49] usare un qualcosa che ti può far
[00:20:51] risparmiare un pochettino perché
[00:20:53] probabilmente poi farà un lavoro pessimo
[00:20:54] e poi ci dovrai ripassare sopra, quindi
[00:20:57] fra il tuo tempo perso e e i token che
[00:20:59] dovrei rispreare dopo non ha senso.
[00:21:01] Quindi, se stiamo parlando di coding,
[00:21:04] comunque non troppo complesso, ma fai
[00:21:05] conto che è un software che devi
[00:21:07] costruire per un cliente, un qualcosa da
[00:21:09] portare in produzione, modelli di
[00:21:12] frontiera, quindi che sia Fable, Opus,
[00:21:16] GPT 5.6, Grock 4.6,
[00:21:18] utilizziamo modalità di frontiera.
[00:21:20] Questa è una cosa che non si scappa,
[00:21:21] purtroppo. Se vuoi costruire qualcosa di
[00:21:23] estremamente complesso, resta sul top
[00:21:26] del top. Però quando parliamo di routine
[00:21:29] skill sotto agenti/chrome
[00:21:31] che è essenzialmente Cloud che può
[00:21:34] vedere la nostra schermata e può toccare
[00:21:36] all'interno del nostro internet, IQ e
[00:21:40] Sonet vanno benissimo. Il 99% di skill e
[00:21:42] routine, dove per chi non lo sapesse la
[00:21:44] skill è una procedura standardizzata che
[00:21:46] insegniamo a Cloud, quindi che ne so,
[00:21:47] gli insegniamo, gli possiamo dare una
[00:21:49] skill così che scriverà sempre le mail
[00:21:52] con il nostro stile. Quella è una skill,
[00:21:53] una competenza che insegniamo a Cloud.
[00:21:55] come faremo con un nostro membro del
[00:21:58] team. La routine è una è una skill che
[00:22:00] viene seguita sempre un certo in certa
[00:22:03] ora di un determinato giorno. Per il 90%
[00:22:05] dei casi le skill e le routine va
[00:22:08] benissimo IQ o Sonnet. Stessa cosa per
[00:22:10] Chrome, cioè quando Cloud deve andare a
[00:22:13] toccare il nostro schermo e della nostra
[00:22:14] che ne so del nostro Google Chrome, di
[00:22:16] quello che utilizziamo, Brave, quello
[00:22:18] che sia. IQ Onet vanno alla grande.
[00:22:20] Ovviamente qui ho messo la stessa cosa
[00:22:22] che dicevamo prima, cioè cambiare il
[00:22:24] modello in corsa. spreca un sacco di
[00:22:25] token. Vale lo stesso se stiamo
[00:22:28] utilizzando una skill, se stiamo creando
[00:22:30] più sottoagenti. Stessa cosa. Ultima
[00:22:33] cosa, occhi task schedulati. ti assicuro
[00:22:35] che magari hai tantissime routine delle
[00:22:38] quali ti sei o scordato oppure non sono
[00:22:40] per niente efficienti. Quindi vatti a
[00:22:42] rivedere se puoi efficientarle, se puoi
[00:22:45] usare un modello più economico, perché
[00:22:47] io mi sono reso conto facendo unudit
[00:22:49] completa che avevo tantissimi task
[00:22:51] schedulati che mi consumavano tantissimo
[00:22:54] del del mio usage, del mio utilizzo.
[00:22:56] Quindi sembra una cavolata, ma questo ma
[00:22:58] dargli un'occhiata. cose da non fare che
[00:23:01] sembrano furbe ma sono delle cavolate.
[00:23:04] Slash compact è il messaggio più caro,
[00:23:06] cioè funziona male e ti consumi un sacco
[00:23:09] di token perché per riassumere tutto
[00:23:11] rimanda tutto quanto, poi butta via la
[00:23:15] roba che ti serve, non lo fare. Un'altra
[00:23:18] cosa da non fare, screenshot del testo.
[00:23:20] Se puoi incolla direttamente il testo,
[00:23:22] piuttosto che creati che se passi uno
[00:23:25] screenshot con il testo, allora con uno
[00:23:27] script che non consuma token si può
[00:23:30] prendere il testo. Dare PDF grezzi,
[00:23:33] l'abbiamo già detto, promptio
[00:23:35] perché spesso se diamo prompt corti
[00:23:37] senza dare il giusto contesto, pensiamo
[00:23:40] di salvare eh un pochettino mandando un
[00:23:42] prompto, ma non dando il giusto
[00:23:44] contesto. Clode non farà un buon lavoro,
[00:23:45] ci dobbiamo ripassare sopra, quindi
[00:23:48] andiamo a sprecare token. E occhio ai
[00:23:50] tool là fuori che promettono il 90% di
[00:23:55] risparmio. Li ho provati tutti Cavem RTK
[00:23:58] e veramente non sono nulla di che. Cavem
[00:24:01] ad esempio eh quello che fa è che questo
[00:24:03] è la risposta normale che ti darebbe
[00:24:07] Cloud, no? Ecco, lui ti dà un po' il il
[00:24:10] riassunto, ma spesso salta informazioni.
[00:24:12] Io l'ho testato, non c'è chissà quanto
[00:24:14] risparmi e se risparmi vi assicuro che
[00:24:16] l'esperienza peggiora tantissimo e
[00:24:19] spesso lascia cose fondamentali. Una
[00:24:21] cosa molto più intelligente è cambiare
[00:24:24] l'output style, cioè qua con in output
[00:24:26] style che qua purtroppo si può cambiare
[00:24:28] solamente da terminale, quindi qua sono
[00:24:32] su settings, vado su output style,
[00:24:35] possiamo cambiare. La cosa che ha molto
[00:24:38] più senso è mettere ad esempio conciso,
[00:24:40] cioè ci dà il risultato senza preamboli
[00:24:44] neioghi. non vi scaricate Caveman o RTK,
[00:24:45] la maggior parte di queste cose sono
[00:24:47] inutili, insomma, se volete testatele,
[00:24:49] ma la cosa migliore è scegliere un
[00:24:52] output style. Bene, andiamo a un altro
[00:24:54] punto fondamentale che è quando possiamo
[00:24:57] scegliamo delle Cli invece che degli
[00:25:00] MCP. La Cli è o Command line Interface,
[00:25:03] è essenzialmente, se volessi proprio
[00:25:06] dirlo in maniera brutale, un API, ma per
[00:25:07] i terminali. Allora, se vogliamo
[00:25:09] connettere software 1 a software 2, ci
[00:25:11] serve un ponte. Questo ponte si chiama
[00:25:15] API. Ci sono diversi metodi API, cioè eh
[00:25:17] questi ponti che abbiamo detto possono
[00:25:19] essere, che ne so, se io dal software 1,
[00:25:23] ops, software 1 che può essere eh Gmail
[00:25:24] e l'altro software 2 che può essere il
[00:25:26] nostro gestionale, possiamo avere la
[00:25:29] chiamata API, il metodo API, send email
[00:25:32] che mi manda un email, write draft che
[00:25:34] mi va a creare una bozza, read email,
[00:25:36] quindi abbiamo tantissimi metodi, no? e
[00:25:38] quando più opportuno andiamo a chiamare
[00:25:40] il metodo giusto, no? Cioè se voglio
[00:25:42] mandare unemail allora utilizzo il
[00:25:44] metodo send email. Se voglio leggerla
[00:25:46] allora utilizzo il metodo read email.
[00:25:49] Cosa fanno gli MCP? Si vanno a prendere
[00:25:50] tutti questi metodi e se li vanno a
[00:25:53] raggruppare in questa sorta di
[00:25:56] gigantesco ponte, quindi senza dover
[00:25:57] azzeccare il metodo giusto tramite gli
[00:25:59] MCP. Abbiamo come se fosse un mega
[00:26:02] wrapper, abbiamo tutti quanti i metodi,
[00:26:04] figo, semplifica tantissimo l'utilizzo,
[00:26:06] la la connessione fra i software, ma il
[00:26:09] problema è che quando questi metodi non
[00:26:13] sono tre, ma diventano tantissimi, noi
[00:26:15] magari vogliamo fare solo poche poche
[00:26:18] cose, cioè mandare unemail e leggere
[00:26:20] l'email e scrivere eh le bozze e
[00:26:22] automaticamente, come vedevamo prima, il
[00:26:24] server MCP li include tutti, il che non
[00:26:26] ha senso perché includendoli tutti
[00:26:29] andiamo a ingolfare il contesto con
[00:26:30] metodi che probabilmente non
[00:26:33] utilizzeremo, quindi vogliamo sfruttare
[00:26:35] solamente i metodi che ci servono a noi.
[00:26:37] Mi direte voi, "Ma allora perché i
[00:26:39] server MCP utilizziamo l'PI
[00:26:40] direttamente? Il problema è che le
[00:26:42] chiamate PI nascono per essere lette da
[00:26:45] umani." Questa è una classica risposta
[00:26:47] di una chiamata API. sembra complesso,
[00:26:50] ma è semplicemente ci dice tutte le
[00:26:51] informazioni della risposta perché così
[00:26:53] un umano può andare a leggere tutto
[00:26:56] quanto e capire la risposta che ci ha
[00:26:58] dato il software. Il problema è che
[00:26:59] tutta questa risposta che di solito è
[00:27:02] lunghissima, anche quella va a occupare
[00:27:04] il contesto delle I alla Context Window,
[00:27:06] no? nascono quindi le click command line
[00:27:09] interface dove risolve il problema dell
[00:27:11] MCP, cioè non si va a caricare a priori
[00:27:12] tutto quanto, ma risolve il problema
[00:27:14] dell'epi. La risposta il JSON se no, è
[00:27:16] troppo grossa. Risolvendo questi due
[00:27:18] problemi si utilizzano appunto le Clee,
[00:27:20] il linguaggio che era nato per i
[00:27:22] terminali commandline interface per
[00:27:24] questo. E quindi le CLE sono tanto
[00:27:28] tantissimo più efficiente eh delle API e
[00:27:31] dei e degli MCP, specialmente se
[00:27:32] utilizziamo appunto Cloud, Codex e
[00:27:33] quant'altro. Questo è un po' quello che
[00:27:35] vi dicevo, l'MCP, il manuale entra
[00:27:39] all'avvio, resta lì anche da spento e
[00:27:41] l'indice cresce ad ogni tool, la Cli è
[00:27:43] zero fino a che non la chiami. Il
[00:27:45] comando non occupa nulla. In una riga
[00:27:46] nel clode.md diciamo, guarda, hai
[00:27:48] accesso alla click di Gmail, eh, se ti
[00:27:50] vuoi connettere a Gmail è accesso a
[00:27:53] quello. Quindi, prima che scriviamo
[00:27:55] qualsiasi cosa, un MCP può occupare
[00:27:57] anche 26.000 token. La click solo 40
[00:28:00] token che è nel cloud. MD che si chiama,
[00:28:01] guarda, hai accesso alla click di Gmail.
[00:28:04] Quindi quando puoi usa una e non è un
[00:28:06] MCP. Che diavolo vuol dire? Mettiamo
[00:28:08] caso che ci vogliamo connettere a eh non
[00:28:12] lo so, Supase. Invece che fare Supase
[00:28:14] MCP e che ne so, passare questa questa
[00:28:16] documentazione a Cloud per farlo
[00:28:18] connettere, proviamo a cercare se c'è
[00:28:20] una clip che di solito è molto più
[00:28:22] efficiente o semplicemente a Cloud LC.
[00:28:24] Connettiamoci a questo software, usa una
[00:28:25] clip. Personalmente io come regola
[00:28:28] generale ho nel mio cloud cerca sempre
[00:28:30] se ci sono clipetto ad MCP. Oh, altra
[00:28:32] cosa veramente interessante, gli unici
[00:28:35] due tool che sono veramente tanta tanta
[00:28:38] roba sono Code Graph e grapy. Ho
[00:28:40] preparato una breve animazione che
[00:28:43] spiega il la forza di un grafo, nel
[00:28:45] senso che se noi dobbiamo ricercare una
[00:28:47] determinata informazione, mettiamo che
[00:28:49] l'informazione sia questo tassello qua,
[00:28:51] che cosa fa Cloud? va a ricercare tanti
[00:28:53] file fino a che non lo becca, mentre un
[00:28:55] grafo, siccome sono tutti i puntini
[00:28:57] connessi fra di loro e Clode ha accesso
[00:29:00] a tutti questi puntini, sa esattamente
[00:29:01] dove se lo va a prendere. Questa è un
[00:29:03] po' la differenza. Quindi prima di
[00:29:05] andare a cercare di trovare il punto
[00:29:07] deve leggersi tutti questi altri file,
[00:29:09] mentre con il grafo bom lo becca subito.
[00:29:13] Quindi senza grafo Cloud cerca tentoni
[00:29:16] per i più nerd lì fuori fa tutte quante
[00:29:18] read, fa tutte quante grap si chiamano.
[00:29:20] Apre un file, no, non è quello. Ok, ne
[00:29:23] apro altri cinque. Un riapertura consuma
[00:29:25] token, mentre con il grafo chi è c'è una
[00:29:27] mappa dove essenzialmente va dritto al
[00:29:30] nodo giusto, il file poi lo legge lo
[00:29:32] stesso. Ci sono due tool che si chiamano
[00:29:35] Code Graph e grapify. Per trovarle code
[00:29:39] graph Gab, eccolo qua. Basta che lo
[00:29:41] prendi e te lo installi, gli passi
[00:29:43] questa repositoria al tuo cloud e
[00:29:47] l'altro è grapy.
[00:29:49] Eccolo qua. Anche qua gli passi l'URL e
[00:29:51] te lo fai installare. Qual è la
[00:29:54] differenza? Entrambi trasformano tutti i
[00:29:56] tuoi file in un grafo, in questa mappa
[00:30:00] facilmente accessibile da Clode. Usa
[00:30:03] Code Graph per il codice. Se cioè
[00:30:04] essenzialmente se è una repositoria, se
[00:30:07] stai lavorando un software, un'app molto
[00:30:09] grossa, CODG graph è ottimizzata per il
[00:30:12] codice, anche perché va a trasformare
[00:30:15] del testo in un grafo.
[00:30:17] Rapy è ottimo per un brain, quindi
[00:30:19] quando invece dobbiamo trasformare in un
[00:30:23] grafo PDF, immagini, markdown, output di
[00:30:25] obsidian, riesce a trasformare comunque
[00:30:27] il grafo. Quindi grpify per il codice
[00:30:29] per base di codice, scusami, code graph
[00:30:32] per basi di codice, grapy per un brain.
[00:30:34] Cosa da sapere, sotto i 500 file non
[00:30:37] conviene nessuno dei due, il grafo ti
[00:30:39] costerà più di risparmiare. Quindi sotto
[00:30:43] 500 file eh non conviene crearsi un
[00:30:46] grafo. Altro trucco fondamentale è
[00:30:48] trasforma in codice dove è possibile,
[00:30:50] nel senso che ogni volta che facciamo
[00:30:52] fare qualcosa alle AI, a parte che non è
[00:30:55] deterministico, cioè è le hai, è per
[00:30:57] natura non è deterministica, ma ogni
[00:31:00] volta paghiamo dei token, ogni tanto si
[00:31:02] sbaglia, il risultato può cambiare dove
[00:31:05] puoi se trasformi un qualcosa in uno
[00:31:07] script, il codice spesso ce lo
[00:31:09] scordiamo, uno script di Python, uno
[00:31:11] script di qualsiasi linguaggio esso sia,
[00:31:14] consuma zero token. è velocissimo, non
[00:31:17] sbaglia mai e gira uguale ogni volta e
[00:31:19] quindi consuma zero token. Ovviamente il
[00:31:22] codice, essendo deterministico, non non
[00:31:25] dà un giudizio, non ti dice se un non ti
[00:31:27] riesce a categorizzare se unemail è spam
[00:31:31] o oppure di customer support, però ti
[00:31:33] assicuro che tantissimo che sia una
[00:31:36] skill, che sia un qualcosa che fai
[00:31:38] spesso, se lo riesci a trasformare da AI
[00:31:41] a codice vai a risparmiare tantissimo.
[00:31:43] Pensa che stavo avendo questo discorso
[00:31:46] con il CTO di Clickup, che è uno dei CRM
[00:31:48] più grossi del mondo, valutato a 4
[00:31:51] miliardi. Stavo in Montenegro eh con con
[00:31:53] il mio gruppo, insomma, un gruppo di
[00:31:55] creator, un network internazionale e il
[00:31:56] CTO di Clickup mi ha detto: "Questa è
[00:31:58] proprio la nostra regola aura, cioè
[00:31:59] aurea, cioè quando noi andiamo a
[00:32:02] costruire nuove featureal o qualsiasi
[00:32:05] cosa, andiamo a rivedere il codice, dove
[00:32:08] possiamo cambiare quella chiamata API a
[00:32:11] cloud, openi, quello che è in codice,
[00:32:13] dove possiamo farlo il più possibile
[00:32:16] perché è più veloce, non sbaglia e
[00:32:16] risparmi."
[00:32:19] Quindi lei serve per il giudizio, tutto
[00:32:21] il resto è esecuzione. Esecuzione
[00:32:24] ripetibile è codice. Per farlo basta
[00:32:26] lanciare un audit all'interno del tuo
[00:32:29] brain o all'interno di di della tua app
[00:32:31] o dovunque tu utilizzi le hai. Lanci un
[00:32:33] prompt dove essenzialmente devi fare un
[00:32:35] audit dove gli chiedi quali pezzi del
[00:32:36] tuo flusso non hanno bisogno di un
[00:32:38] modello. Quel diventano uno script,
[00:32:41] magari le skill, no? Spesso non serve
[00:32:42] far lavorare la tua usage cloud, ma
[00:32:46] serve uno script. Poi ogni ricordati di
[00:32:48] è un candidato di Hook, che è quella
[00:32:50] cosa deterministica di cui parlavamo
[00:32:54] prima. Fra l'altro Luke si triggera
[00:32:56] sempre quando gli diciamo che avviene
[00:32:58] sempre un certo evento. Che ne so,
[00:33:00] quando noi carichiamo il PDF
[00:33:03] automaticamente ogni volta succede
[00:33:04] quello script perché è un hook, un
[00:33:05] qualcosa di terministico. Se invece
[00:33:07] scriviamo, banalmente non avessimo fatto
[00:33:09] un hook, ma l'avessimo scritto nel
[00:33:12] cloud. MD può essere che una volta Clude
[00:33:14] non lo esegua perché è un prompt, non è
[00:33:15] deterministico. E l'ultima cosa che ci
[00:33:18] tenemo a dirti sono i sottoagenti.
[00:33:19] Spesso quello che vedi è che ti
[00:33:22] ritornano 420 token, sembra una
[00:33:25] vittoria, ma in realtà il tuo sotto
[00:33:27] agente probabilmente ha un ha un suo
[00:33:29] system prompt, ha la sua copia della
[00:33:32] memoria, cioè dove siamo arrivati con
[00:33:33] Clud a un certo punto della
[00:33:34] conversazione, i suoi strumenti
[00:33:35] permessi, la lettura vera e propria,
[00:33:38] quindi spesso non sono mai così pochi,
[00:33:42] ma spesso magari spendiamo 980 9800
[00:33:45] token per risparmiare i 5700, quindi
[00:33:47] quando utilizzare i sottoagenti
[00:33:49] solamente Per le azioni in bulk devi
[00:33:52] leggere 40 file, devi analizzare 10
[00:33:56] fonti. Eh, in quel caso allora utilizza
[00:33:59] i sottoagenti. Sennò no. Pro tip, i
[00:34:02] sottoagenti IQ vanno una bomba. Quindi
[00:34:03] io spessissimo quando le dico "Creami i
[00:34:06] sottoagenti per farlo", sottoagenti IQU,
[00:34:07] a meno che non devo fare un compito
[00:34:09] molto complesso, però sotto agenti Iu
[00:34:12] fanno veramente una favola. look, quello
[00:34:14] che ti ho detto da PDF a testo,
[00:34:16] ovviamente non è più un vantaggio se i
[00:34:19] tuoi PDF eh sono eh hanno tante
[00:34:21] immagini, schemi grafici che devi
[00:34:23] leggere. In tal caso però basta glielo
[00:34:25] dici, gli carichi il PDF, siccome look
[00:34:26] si triggera ogni volta, dici "Guarda,
[00:34:28] non eseguire quello script là perché
[00:34:29] questa volta devo analizzare i grafici".
[00:34:30] Altra cosa che ti volevo dire è quella
[00:34:35] lì sul grafo, cioè il grafo sotto i 500
[00:34:37] file non ha senso crearli, quindi non
[00:34:39] usare code, graph o grapify. Questo era
[00:34:41] tutto ciò che ti volevo dire,
[00:34:43] essenzialmente quasi tutto ciò che so
[00:34:46] sul risparmio dei token su Cloud Code.
[00:34:47] Va benissimo. Questi concetti si
[00:34:49] applicano anche a Codex, si applicano
[00:34:51] anche a qualsiasi altro codic agent tu
[00:34:53] utilizzi. Quindi se sei un'azienda e
[00:34:54] vuoi implementare l'intelligenza
[00:34:55] artificiale all'interno dei tuoi
[00:34:57] processi a partire dalla formazione del
[00:35:00] tuo team su strumenti pratici come Cloud
[00:35:02] Code, Cloud Cowork, Codex, offriamo fra
[00:35:04] l'altro anche percorsi di coaching sia
[00:35:07] singoli che dopo che facciamo la
[00:35:08] formazione facciamo dei coaching one to
[00:35:10] many a tutto il tuo team per continuare
[00:35:13] a tenerli formati sul lungo periodo.
[00:35:14] piuttosto se vuoi analizzare i tuoi
[00:35:17] processi per capire quali soluzioni hai
[00:35:19] costruire su misura per la tua realtà e
[00:35:22] poi costruire tali soluzioni. Non siamo
[00:35:24] l'azienda di consulenza che ti fa
[00:35:26] l'analisi dei processi e ti dà il deck
[00:35:28] di 200 pagine, ma andiamo ad eseguire e
[00:35:30] a costruire poi queste soluzioni che
[00:35:32] sono estremamente customizzate per la
[00:35:34] tua azienda. Se ti può interessare, come
[00:35:35] al solito, nel primo link in descrizione
[00:35:37] puoi prenotare una chiamata se ci vuoi
[00:35:38] parlare del tuo progetto. Questo è
[00:35:40] tutto. Fatemi sapere qui sotto che ne
[00:35:43] pensate e quali sono quei trick che
[00:35:45] magari non sapevate o che avete
[00:35:46] applicato e che vi hanno salvato
