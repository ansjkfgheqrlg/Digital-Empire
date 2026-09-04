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

