---
Type: SOURCE
Status: Active
Tags: #claude-code #token #contesto #claude-md #mcp #cli #hook #sub-agenti #grafo-conoscenza #graphify #codegraph #martes-ai #riccardo-belli #max18
Created: 2026-09-04
Last updated: 2026-09-04
---

# Source: Riccardo Belli Contarini (Martes AI) — Dammi 36 Minuti e Ti Farò Risparmiare MILIONI di Token su Claude

## VERDETTO — leggere questo prima di tutto

**Digital Empire rispetta già le due regole più grosse di questo video, e ne viola una in modo
documentato.** Verificato con grep, non a intuito:

- ✅ **CLAUDE.md come indice, sotto le 200 righe**: il `CLAUDE.md` di radice di DE è di **153
  righe**, e nel repo ci sono **48 file `CLAUDE.md`** — il pattern "uno per cartella" è già
  adottato. Nessuna azione.
- ✅ **Modelli per grado**: la gerarchia delle forze di DE (scagnozzo `haiku` / sentinella
  `sonnet` / doom bot `opus`, `emperator.md:1046-1050`) è già esattamente la regola del video.
  Nessuna azione.
- ❌ **`/compact`**: il video lo definisce "il messaggio più caro" e ci costruisce sopra tre
  tecniche alternative. DE ha scritto **il contrario** in
  `.claude/skills/agente-max/knowledge/K05-context.md:531`: *"tenete Autocompact su on… Potrete
  sempre usare /compact manualmente in aggiunta quando necessario."* E in tutta
  `company/Memory` la parola "compact" ha **0 occorrenze**: non esiste una regola dell'Impero
  su questo. **Serve una decisione di Max**, non una patch di iniziativa.

**Il pezzo più riusabile del video** è l'**hook PDF → testo** (`pdf-read-as-text.py`),
documentato integralmente a schermo: DE non ce l'ha (`pdftotext` = 0 occorrenze) ma ha già lo
slot `PreToolUse` attivo in `.claude/settings.json`, quindi è un'aggiunta, non una costruzione.

**Nessuna patch è stata applicata** — questa run è Fase 1, solo studio.

## Dati Tecnici

- **Video ID:** `1Dyld3y-V7Y` · **Durata:** 36:01 (2161 s) · **Lingua:** IT
- **Canale:** Riccardo Belli Contarini — ingegnere informatico, founder di **Martes AI**
- **Formato:** screen-recording denso (~70%) — lavagna Excalidraw + Claude Code desktop e
  terminale + browser — alternato a talking head e ad animazioni originali
- **Capitoli ufficiali:** 20 · **Frame:** 721 densi @3s → **138 unici** · **Frame letti:
  138/138 — coverage 100%** · NO-FINTO: PASS
- **KA:** 47 atomi con **96 archi tipizzati** (0 rotti, 0 orfani) · 44 osservati, 3 marcati
  come non verificati
- **⚠️ Vincolo della run:** sorgente **640x360 av1** — il testo minuto delle schermate non è
  recuperabile; le citazioni testuali vengono solo dalle viste in cui l'autore zooma. Dettaglio
  e conseguenze in `coverage.md`.
- **Run:** `empire-studio/runs/max18-v03-belli-token` · **Memory Empire:**
  `empire-studio/memory-empire/knowledge/1Dyld3y-V7Y/`

## Il principio unico da cui discende tutto il resto

```
Tu scrivi una riga.  Lui rilegge tutto.  Ogni volta.

TURNO 1   messaggio 180 →  rilegge 180
TURNO 2   messaggio 180 →  rilegge 360
TURNO 3   messaggio 180 →  rilegge 540      il tuo costo è costante,
   ...                                       il suo cresce a ogni turno
```

I modelli non hanno memoria: a ogni invio rileggono la conversazione dall'inizio — il tuo
contesto, tutte le loro risposte, ogni file aperto. Da qui discendono `/clear`, `/rewind`, il
file di handoff, il CLAUDE.md-indice e la regola sui grafi.

> **Precisione che il video sbaglia e noi non ereditiamo**: a 9:48 il relatore dice
> "è come se fosse esponenziale". L'animazione che mostra lui stesso descrive una crescita
> **lineare per turno**, quindi **quadratica sul cumulato**. L'animazione è giusta, la parola no.

## Le tecniche, per blocco (dalla lavagna, lette a schermo)

**GRATIS, SUBITO** — "valgono più di tutto il resto"
| Tecnica | Claim sulla lavagna |
|---|---|
| `/clear` a ogni cambio di task | *azzera la base* — "ogni altro fix taglia una fetta, questo azzera la torta" |
| modello ed effort scelti una volta | *eviti un 10x* |
| `/rewind`, non `/compact` | *non ricostruisci nulla* — torni a uno stato già pronto |
| file di handoff, non `/compact` | *poche centinaia di token* |
| diagramma ASCII prima di costruire | *togli il giro* |

**UNA VOLTA SOLA** — "installa una volta, paga per sempre"
| Tecnica | Claim |
|---|---|
| spegni gli MCP che non usi | **-47.000 a sessione** (GitHub 26.000 + Slack 21.000) |
| CLAUDE.md come indice | *sotto le 200 righe* — "dice DOVE stanno le cose, non le contiene" |
| un CLAUDE.md per cartella | **-7.160 a sessione** |
| archivia le skill, accorcia le descrizioni | *migliaia a sessione* |
| hook PDF + filtro sull'output | *3-4x sui PDF* |

**NON FARLO** — "sembrano furbe, costano": `/compact` (*il messaggio più caro*) · screenshot
del testo (*2.700 token* per duecento parole) · PDF grezzi (*paghi due volte*: testo **più**
immagine della stessa pagina) · prompt più corti (*lo 0,01% del conto*) · i tool che
promettono il 90% (*fra zero e negativo*).

## I tre pezzi che valgono più delle liste

### 1. CLI invece di MCP — "il taglio più grosso, e non è un tool"

```
MCP: il manuale entra all'avvio          CLI: zero finché non la chiami
─────────────────────────────            ──────────────────────────────
GitHub 26.000 · Slack 21.000             il comando non occupa niente
resta lì anche da spento                 una riga in CLAUDE.md e sa che esiste
l'indice cresce a ogni tool              è un fatto architetturale

peso in contesto PRIMA che tu scriva:  MCP 26.000  vs  CLI ~40 token
```

Il test di verifica dato dall'autore: **`/context` deve dire "deferred"** — vuol dire che i
manuali restano zitti finché non servono. Perché non usare l'API grezza: le risposte API
nascono per essere lette da umani, quindi sono JSON lunghissimi che finiscono interi in
contesto. La CLI risolve **entrambi** i problemi.

### 2. L'hook PDF → testo (l'artefatto più riusabile del video)

Documentato integralmente in un solo frame, e in nessun punto dell'audio:

```
~/.claude/hooks/pdf-read-as-text.py     registrato in ~/.claude/settings.json
                                        come PreToolUse, matcher: Read, globale

Read su un .pdf  →  1. pdftotext -layout estrae il testo
                    2. cache in ~/.claude/pdf-text-cache/<nome>.<hash>.txt
                    3. riscrive il file_path verso quel .txt
                       → le pagine non entrano come immagini renderizzate

si tira indietro da solo:  testo < 200 caratteri/pagina (scansioni, slide-immagine)
                           oppure pdftotext assente/in errore  → passa il PDF originale
override quando serve il visivo:  touch ~/.claude/pdf-visual-once   (una volta sola)
limite dichiarato:  sui PDF a colonne, pdftotext le appiattisce
```

### 3. Trasforma in codice ciò che è ripetibile

> **"L'AI serve per il GIUDIZIO. Tutto il resto è esecuzione, e l'esecuzione ripetibile è
> codice."**

`~2.000 token a giro` (lo rifà l'AI, ogni tanto sbaglia, il risultato cambia) contro `0 token`
(uno script: non sbaglia mai, gira uguale ogni volta), pagando la scrittura **una volta sola**.
Come trovare cosa trasformare: lanciare un prompt di audit che chieda *quali pezzi del flusso
non hanno bisogno di un modello*. E l'euristica che vale da sola:

> **"Ogni 'ricordati di' è un candidato hook: è l'unica categoria di consiglio che sopravvive
> al fatto che te ne dimentichi."**

## ⚠️ La cifra sui PDF — controllo fatto, esito negativo sulla fonte

Il video afferma a **[17:41]**: *"Ogni pagina di un documento PDF elaborato con Claude Code
consuma tra i 1.500 e 3.000 token."*

**Cinque secondi prima, a schermo, si vede da dove viene** (`frame-353.png`, letto dopo zoom
5x): una ricerca Google `claude code quanti token consuma per ogni pagina di un pdf` a cui
risponde un **AI Overview di Google**, con il chip di citazione **"GitHub"** attaccato alla
frase che contiene la cifra, e le voci di dettaglio citate a **Reddit · r/ClaudeAI** (×2) e
**Medium**. I due risultati organici in colonna sono anch'essi thread Reddit.

**Catena reale: relatore → AI Overview di Google → GitHub/Reddit/Medium. Nessun anello è
documentazione primaria Anthropic.** La cifra va usata solo come *detta dal relatore*.

**Equità verso l'autore**: non nasconde la fonte, la tiene a schermo 12 secondi. Quello che non
fa è **dire a voce** che sta citando un riassunto generato da un'AI. Difetto di etichettatura,
non di occultamento.

**Da tenere separata** la cifra "300 pagine → 500-600k token con `Read` contro 150k con
l'hook, 3-4x": quella è dichiarata come **misurazione propria** dell'autore, non come
citazione. Non verificata da noi, ma è un'altra classe di affermazione.

## La contraddizione più interessante — e l'autore non la vede

Nel pannello `/usage` che il relatore mostra a **3:36** per dimostrare le sue tesi, in fondo,
**Claude Code stesso consiglia**:

> "Le sessioni più lunghe sono più costose anche con la cache. **Usa `/compact` a metà
> attività**, `/clear` quando passi a nuove attività."

Cioè: mentre costruisce la tesi "`/compact` è la cavolata più grossa", il prodotto raccomanda
`/compact` nella schermata che lui stesso proietta. **Non lo nota e non lo confuta.** Per DE
questo è il punto decisivo: il conflitto non è "un YouTuber contro l'Impero", è **il relatore
contro il vendor**, e va risolto misurando, non scegliendo un'autorità.

## Altre affermazioni da NON propagare

| Affermazione | Perché |
|---|---|
| Karpathy "adesso sta ad Anthropic", ha "inventato il second brain con l'LLM wiki" | Attribuzione che non risulta corretta; non verificata contro fonti esterne. Il pattern "un CLAUDE.md per cartella" resta valido a prescindere da chi l'ha inventato |
| "sotto le 200 righe" = regola dei doc Anthropic | Attribuzione **dichiarata** dall'autore ma non verificata da noi |
| Caveman "fra zero e negativo" | Il README di Caveman, mostrato nello stesso video, rivendica **-33,2%**. Le due affermazioni si contraddicono e **nessuna è stata testata da noi** |
| Aneddoto del CTO di ClickUp | Seconda mano, nessun documento a conferma |

## Consigli — tutti verificati con grep/read prima di essere scritti

> Nessuno di questi è stato applicato. Fase 1 = solo studio. I comandi di verifica sono
> indicati perché chiunque possa rifarli.

**C1 — `/compact`: DE ha una raccomandazione opposta, scritta, e nessuna regola.**
`.claude/skills/agente-max/knowledge/K05-context.md:531` dice di tenere Autocompact **on** e di
usare `/compact` manualmente. In `company/Memory` "compact" ha **0 occorrenze**. Il video
sostiene l'esatto contrario e propone due sostituti (`/rewind`, file di handoff). Non è una
patch da fare di iniziativa: **è una domanda per Max**, e la risposta va scritta come ADR
perché oggi l'Impero non ha una posizione.
*Verifica: `Grep "compact" company/Memory` → 0 file; `Grep -i "rewind" .claude` → solo materiale
didattico in `agente-max/knowledge/` e codice di libreria ruflo, mai una regola operativa.*

**C2 — `scripts/peso_skill.py` misura il costo sbagliato (il gap più preciso trovato).**
Lo script pesa il **corpo** di ogni `SKILL.md` (righe, byte, gettoni stimati, soglia 150 righe)
— cioè il costo che si paga **quando la skill si attiva**. Ma la card del video dice:
*"Skill e descrizioni si caricano ogni volta, anche quelle che non parti mai"*: il costo
sempre-acceso è la **`description` del frontmatter di ogni skill installata**, moltiplicata per
tutte le skill, a ogni sessione. `peso_skill.py` **non la misura**: la stringa `description`
ha **0 occorrenze** nel file. Lo script dichiara "115 delle 170 skill superano le 150 righe" —
un numero sul costo di attivazione, mentre la voce che pesa a ogni avvio non è mai stata
contata. *Estensione suggerita, non applicata: aggiungere una seconda colonna che sommi i
gettoni delle sole `description`, che è il conto che si paga sempre.*
*Verifica: `Grep -i "description:" scripts/peso_skill.py` → No matches.*

**C3 — Hook PDF assente, ma l'infrastruttura c'è già.**
`pdftotext` ha **0 occorrenze** in `scripts/`, `.claude/agents/`, `.claude/skills/empire-studio/`
e `company/`. Però `.claude/settings.json` dichiara già i blocchi hook `SessionStart`, `Stop`,
**`PreToolUse`**, `UserPromptSubmit`: lo slot esatto che serve è attivo. Per un Impero che
ingerisce PDF di continuo (KDP, manuali, preventivi, materiale corsi) è l'aggiunta col rapporto
valore/sforzo migliore del video. **Non applicata**: tocca la configurazione globale e va
decisa, non infilata di nascosto.

**C4 — Caveman: distinguo onesto, non un "togliamolo".**
DE ha il plugin caveman estratto in `SKILL & Agenti/caveman-extracted/caveman-main/` e
`emperator.md:1098` raccomanda `caveman:cavecrew-investigator` come subagent di sola lettura.
**Il video non boccia quello**: boccia il *Caveman Proxy*, cioè il compressore di contesto. Sono
due prodotti diversi dello stesso repo. Quello che resta vero anche per noi è C2: le ~7 skill
`caveman:*` installate pagano la propria `description` a ogni sessione, che le si usi o no.
Decisione da prendere con il conto di C2 in mano, non prima.

**C5 — Conferme, che valgono quanto i gap.**
`CLAUDE.md` di radice = **153 righe** (regola "<200" già rispettata); **48 `CLAUDE.md`** nel
repo (pattern per-cartella già adottato); root `.mcp.json` dichiara **1 solo server** con
`autoStart: false` (DE è già sobria dove il video vede il buco più grosso); la gerarchia
haiku/sonnet/opus di [[Emperator_Gerarchia_Forze]] coincide con la regola sui modelli. Su
`graphify`: la soglia del video ("sotto i ~500 file il grafo costa più di quello che
risparmia") **non tocca DE**, che conta **166.534 file** — l'uso di `graphify-out/` prescritto
in `CLAUDE.md` è ampiamente giustificato.
*Verifiche: `wc -l CLAUDE.md`; `find . -name CLAUDE.md | wc -l`; `find . -type f | wc -l`.*

**C6 — Il consiglio più trasferibile non è tecnico.**
"Ogni 'ricordati di' è un candidato hook" è il criterio che separa una regola che
sopravvive da una che si dimentica. Molte regole di DE oggi vivono come prosa in `CLAUDE.md` e
in `emperator.md` — cioè come **prompt**, che il modello può non eseguire. Il video dice
esattamente questo: *"se l'avessimo scritto nel CLAUDE.md può essere che una volta Claude non
lo esegua, perché è un prompt, non è deterministico."* L'Impero ha già hook attivi: la domanda
aperta è **quali regole scritte a parole meritano di diventare deterministiche**.

## Key Quotes

> "Il taglio più grosso della lista sta qui, e non è un tool: è scegliere un altro modo di
> collegare le cose." *(CLI invece di MCP)*

> "L'AI serve per il GIUDIZIO. Tutto il resto è esecuzione, e l'esecuzione ripetibile è codice."

> "Ogni 'ricordati di' è un candidato hook: è l'unica categoria di consiglio che sopravvive al
> fatto che te ne dimentichi."

> "Quello che digiti tu è un errore di arrotondamento. I prompt vaghi costano, ma per il lavoro
> rifatto che innescano." *(perché accorciare i prompt è inutile)*

> "Il lavoro rifatto non avviene proprio. Nessun compressore può farlo: agiscono su ciò che è
> già successo."

> "Se il corpo è pieno di numeri misurati, l'intro promette con un avverbio, non con una cifra."
> *(regola editoriale che l'autore si è fatto scrivere in un `style.md`, letta a schermo mentre
> preparava questo stesso video)*

## Nota di trasparenza — limiti della fonte

Un solo autore, nessun dato di terze parti verificabile, e i numeri della lavagna
(`-47.000`, `-7.160`, `2.700`, `9.800/5.700`) sono **tutti dichiarazioni dell'autore**: nessuno
è accompagnato da una misurazione riproducibile mostrata a schermo. Vanno usati come **ordini di
grandezza per decidere le priorità**, mai citati come dati. La cifra sui PDF è l'unica di cui
abbiamo tracciato la provenienza, ed è risultata debole. Il video promette "10 mosse" ma non
numera mai nulla: le tecniche distinte sono più di dieci.

## Connessioni

- [[Source_Riccardo_Belli_Claude_Codex_Setup]] — stesso autore (Martes AI), batch precedente
  `max17`. Là il verdetto era "il setup non serve a DE, salvo il principio cross-model"; qui è
  l'opposto: DE è già conforme sulle regole grosse, e il valore sta in **un hook** e in **una
  contraddizione da risolvere**. Due video dello stesso autore, due esiti opposti: utile come
  prova che il verdetto si decide sulla codebase, non sulla reputazione della fonte.
- [[Source_Giovanni_Beggiato_Company_Brain_Karpathy]] — l'altra fonte DE che attribuisce a
  Karpathy l'architettura del company brain. Questo video ripete l'attribuzione **aggiungendo
  un errore** ("adesso sta ad Anthropic"): le due pagine vanno lette insieme, perché DE ha ora
  due fonti indipendenti sullo stesso pattern e una sola delle due sbaglia i fatti sull'autore.
- [[Source_Jay_E_Agentic_OS_Claude5]] — da cui viene la soglia delle **150 righe** codificata in
  `scripts/peso_skill.py` (lo script lo dichiara esplicitamente: "non è uno standard ufficiale
  Anthropic"). Questo video porta la soglia **200 righe** attribuita ai doc Anthropic e, più
  importante, sposta il conto dal corpo della skill alla sua `description` — vedi C2.
- [[Emperator_Gerarchia_Forze]] — scagnozzo `haiku` / sentinella `sonnet` / doom bot `opus`: la
  regola del video sui modelli ("routine, skill, sub-agenti → Haiku e Sonnet vanno benissimo";
  "metti i sub-agenti su Haiku") è già la dottrina dell'Impero. Il video aggiunge il **conto
  vero** di un sub-agente (9.800 spesi per risparmiarne 5.700) e la condizione che lo ribalta:
  solo azioni in bulk.
- [[Tool_Memory_Wiki_Bridge]] — il ponte per cui questa ingestione è una pagina wiki invece di
  restare in `memory-empire/knowledge/`.
