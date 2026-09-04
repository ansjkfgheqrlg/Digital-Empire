# Coverage — max18-v03-belli-token (`1Dyld3y-V7Y`)

## Numeri — contati, non stimati

Ogni cifra qui sotto è stata **contata con un comando in questa sessione**, non ricavata a
memoria né copiata da `scenes.md`. Il comando è indicato accanto.

| Grandezza | Valore | Come l'ho contata |
|---|---|---|
| Durata reale | **2161 s = 36:01** | `ingest.json` → `duration_sec` |
| Risoluzione sorgente | **640x360, codec av1** | `ffprobe -show_entries stream=width,height,codec_name video.mp4` |
| Frame PNG in `frames/` | **721** | `ls frames/*.png \| wc -l` (il 722° file è `manifest.json`) |
| Frame unici in `scenes.md` | **138** | righe tabella di `scenes.md` (file di 149 righe, 11 di intestazione) |
| **Frame unici aperti e guardati** | **138 su 138 — 100%** | elenco nominale sotto |
| Frame ingranditi con crop+upscale | **12 frame → 27 ritagli aperti** | elenco nominale sotto |
| `.vtt` grezzo | **7.616 righe** | `wc -l 1Dyld3y-V7Y.it.vtt` |
| `clean_transcript.txt` | **950 righe** | `wc -l clean_transcript.txt` |
| **Trascrizione letta** | **950 su 950 — 100%**, in una sola lettura integrale | riga 1 (`[00:00:01]`) → riga 950 (`[00:35:46]`) |
| Capitoli ufficiali YouTube | **20** | conteggio dell'array `chapters` in `ingest.json` |
| Atomi estratti | **47** | `json.load(atoms.json)` → `len()` |
| Archi fra atomi | **96, 0 rotti, 0 atomi orfani** | script di validazione (sotto) |

## La strategia, e perché è quella proporzionata a QUESTO video

**Strategia adottata: copertura totale dei frame unici (138/138) + trascrizione integrale +
zoom mirato sui 12 frame che contengono numeri, tabelle o codice.**

Non è la strategia di `max17-v16` (talk dal vivo, 20 frame su 858 campionati) né quella di
`max17-v17` (formato misto). È la strategia da screen-recording denso, e i tre motivi sono
verificabili:

1. **Il contenuto NON è nell'audio.** Questo non è un relatore che parla: è uno schermo
   condiviso per ~70% della durata. La lavagna Excalidraw contiene ~24 card con **claim
   numerici che non vengono mai detti a voce** (`-47.000 a sessione`, `-7.160 a sessione`,
   `2.700 token`, `~2.000 token a giro`, `9.800 spesi per risparmiarne 5.700`). Saltare i
   frame qui avrebbe significato perdere metà del video.
2. **Ci sono contenuti che esistono SOLO nel frame.** Verificato: la clausola "scegli tu cosa
   sopravvive, **soprattutto le strade già fallite**" (KA-010) è scritta sulla card del file
   di handoff e **non compare in nessun punto della trascrizione**. Idem per il suggerimento
   `/compact` di Claude nel pannello `/usage` (KA-045), che è la contraddizione più
   interessante del video.
3. **Le schermate tecniche sono la parte riusabile.** L'hook PDF (KA-036) è documentato
   integralmente in un solo frame (`frame-385`) e in nessun punto dell'audio: percorso del
   file, tipo di hook, matcher, comando di estrazione, cartella di cache, condizioni di
   fallback, override manuale. È l'artefatto più direttamente riusabile del video e vive
   interamente a schermo.

**Il video è breve abbastanza da permetterselo**: 36 minuti e 138 frame unici sono un ordine
di grandezza sotto ai 858 frame di `max17-v16`. La copertura totale qui costa poco; là sarebbe
stata sproporzionata. La strategia segue la densità informativa, non l'abitudine.

## Il vincolo che va dichiarato: la sorgente è a 360p

`ffprobe` sul `video.mp4` già scaricato dà **640x360, av1**. Non è un difetto
dell'estrazione dei frame: è la risoluzione del file sorgente, quindi **i 721 PNG non possono
contenere più informazione di così**.

Conseguenze misurate, non supposte:
- Ho provato a recuperare il testo con **crop + upscale LANCZOS 4x-8x** su `frame-005`,
  `frame-029`, `frame-007`. **Non funziona**: le lettere non sono nei pixel e l'upscale non le
  inventa. Verifica salvata come `zoom-005.png`, `z029-col1.png`, `z007-ctx.png` nello
  scratchpad di sessione (non nel repo).
- **Ma la lavagna è leggibile quando è l'autore a zoomare.** Nelle viste ravvicinate
  (`frame-033`, `frame-093`, `frame-271`, `frame-341`, `frame-410`, `frame-462`, `frame-570`,
  `frame-628`, `frame-652`, `frame-667`) il testo delle card si legge per intero a occhio nudo
  o con un 4x. È da lì che vengono tutte le citazioni testuali di `video-analysis.md`.
- **Regola che ho applicato**: una card è citata testualmente solo se letta in una vista
  ravvicinata. Dalle viste d'insieme ho preso solo la struttura (quante colonne, di che
  colore, in che ordine), mai il testo.

**Non ho riscaricato il video a risoluzione maggiore** (il brief lo vietava: l'estrazione è la
parte cara).

### La causa NON è YouTube: è un default della nostra pipeline

Prima ipotesi mia, sbagliata: "yt-dlp non è sul PATH della shell delle sentinelle"
(`timeout 60 yt-dlp -F …` → "No such file or directory"). Vero, ma **non è la causa**.

La causa vera è in casa nostra, `empire-studio/scripts/frame_extractor.py`:

```
riga  42:  def download_video(url, run_dir: Path, height=360):
riga  51:      "format": f"bv*[height<={height}]/b[height<={height}]/worst",
riga 133:      ap.add_argument("--height", type=int, default=360)
riga 155:      print(f"[frame] scarico video a <= {args.height}p ...")
```

**È l'Impero a chiedere esplicitamente ≤360p a yt-dlp**, per default, per ogni video. Il
manifest di `max18-v02` conferma che è la prassi:
`"trace": "… frame_extractor.py --interval 3 --height 360 …"`.

La scelta ha senso per i talk dal vivo (dove il contenuto è nell'audio e 360p basta per
riconoscere una scena) ed è sbagliata per gli screen-recording, dove il contenuto **è** il
testo a schermo. Il flag esiste già: `--height 720`. Nessuno lo usa.

## Tre errori di lettura miei, trovati e corretti in corso d'opera

Li lascio a verbale perché sono la prova che la regola "cita solo dalla vista ravvicinata"
serve davvero. Tutte e tre le prime letture venivano da viste d'insieme, e tutte e tre erano
**sbagliate nonostante l'audio sembrasse confermarle**:

| # | Prima lettura (vista d'insieme) | Lettura corretta (vista ravvicinata) | Dove |
|---|---|---|---|
| 1 | colonna 1 = "ADESSO, SUBITO" | **"GRATIS, SUBITO"** | `frame-029` → `frame-033` |
| 2 | MCP spenti = "-19.000 a sessione" | **"-47.000 a sessione"** (= 26.000 GitHub + 21.000 Slack) | `frame-033` → `frame-271` |
| 3 | colonna 3 = "IL MODELLO ADATTO" | **"IL MODELLO GIUSTO"** | `frame-029` → `frame-410` |

Nei tre casi l'audio diceva rispettivamente "tecniche che si possono utilizzare **da subito**",
"un MCP può occupare anche **26.000** token", "la questione dei **modelli**" — cioè
**l'audio confermava plausibilmente la lettura sbagliata**. È il modo tipico in cui una
sagoma di parola a bassa risoluzione produce una citazione falsa che suona giusta.

## Il controllo sulla cifra "1.500-3.000 token per pagina PDF"

**Appunto ricevuto**: la cifra verrebbe da un riassunto automatico di Google. **Verificato di
persona, non preso per buono. Esito: l'appunto è corretto, e la prova è nel video stesso.**

1. **La cifra è nel video**: `clean_transcript.txt` riga 480, `[00:17:41]` — *"Ogni pagina di un
   documento PDF elaborato con Cloud code consuma tra i 1500 e 3000 token."*
2. **La fonte è visibile a schermo 5 secondi prima**, `frame-353.png` (17:36), letto dopo zoom
   5x su quattro regioni (`z353-query`, `z353-overview`, `z353-dettagli`, `z353-reddit`):
   - query Google: `claude code quanti token consuma per ogni pagina di un pdf`
   - la risposta è un **AI Overview di Google**, con chip di citazione **"GitHub"** sulla frase
     che contiene la cifra
   - le tre voci di dettaglio sono citate a **Reddit · r/ClaudeAI (×2)** e **Medium**
   - i due risultati organici in colonna destra sono **entrambi thread Reddit r/ClaudeAI**
3. **Catena reale**: relatore → AI Overview di Google → GitHub/Reddit/Medium. **Nessun anello
   è documentazione primaria Anthropic.**

**Come è riportata nei deliverable**: sempre come *detta dal relatore* (KA-037, `confidenza:
"detto dal relatore, fonte a monte debole e verificata come tale"`), mai come dato verificato.

**Nota di equità verso l'autore**, che va detta o il rilievo è scorretto: **non nasconde la
fonte**, la tiene a schermo per 12 secondi (`frame-353` → `frame-357`). Quello che non fa è
**dire a voce** che sta citando un riassunto generato da un'AI. È un difetto di etichettatura,
non di occultamento.

**Cosa NON ho verificato**: se la cifra sia *vera*. Non ho misurato il consumo reale di una
pagina PDF né aperto documentazione Anthropic. L'unica cosa accertata è la **provenienza**.

**Tenuta separata** una cifra di natura diversa: il test "300 pagine → ~500-600.000 token con
`Read` contro 150.000 con l'hook, 3-4x" ([00:19:53]) è dichiarato dall'autore come
**misurazione propria** ("Io ho fatto diversi test, se non mi credete fateli anche voi"), non
come citazione. Resta non verificata da noi, ma è un'altra classe di affermazione ed è
catalogata a parte (KA-038).

## Altre affermazioni marcate come non verificate

| Atomo | Affermazione | Perché è marcata |
|---|---|---|
| KA-023 | Karpathy "adesso sta ad Anthropic", ha "inventato il concetto di second brain con l'LLM wiki" | Attribuzione che non risulta corretta; **non ho aperto fonti esterne** per accertarlo, quindi è segnata come *dichiarazione dubbia del relatore, da non propagare*, non come falsità accertata |
| KA-021 | "sotto le 200 righe" attribuito ai doc Anthropic | Attribuzione **dichiarata** dall'autore (a voce e sulla lavagna) ma non verificata da me contro la doc |
| KA-032 | Caveman "fra zero e negativo" vs il suo README che rivendica "-33,2%" | Le due affermazioni si contraddicono; **nessuna delle due è stata testata da noi** |
| KA-038 | 3-4x sui PDF | Misurazione dell'autore, non riprodotta |
| KA-031 | Aneddoto del CTO di ClickUp | Seconda mano, nessun documento a schermo lo conferma |

## Cosa NON è leggibile, e non ho finto di leggere

- Il **corpo delle card** nelle viste d'insieme (`frame-002`, `frame-029`, `frame-408`,
  `frame-498`, `frame-504`): si distinguono titolo scuro + claim colorato + 3 righe di corpo,
  non le parole.
- Le colonne **viola** e **rosa** e i due riquadri bassi **nelle sole viste d'insieme**; per
  quelle esistono però viste ravvicinate (`frame-410`, `frame-462`, `frame-570`, `frame-628`),
  quindi il contenuto è comunque letto — solo da un altro frame.
- Nel riquadro dei sub-agenti (`frame-667`), la voce "**i suoi strumenti e permessi — …**": la
  cifra accanto **non è leggibile**. Riportata senza numero, non inventata.
- Nell'animazione del grafo (`frame-574`), il contatore del pannello "Con il grafo": **non
  leggibile**. Ho riportato solo il **3480** del pannello "Senza grafo", che si legge.
- Il menu **output style** citato a voce a 24:19: mostrato ma **non leggibile** a 360p. KA-035
  è marcato `frame: n/a` e `confidenza: osservato (audio) / frame non leggibile`.
- La didascalia sotto la lavagna in `frame-652` ("Le mosse che contano di più non hanno un
  numero: cambiano la base su cui tutte le altre sono una…") è **tagliata dall'inquadratura**:
  riportata troncata, non completata a fantasia.

## Una trappola evitata, documentata perché si ripresenterà

`frame-334` (16:39) mostra un diagramma ASCII pieno di numeri appetitosi: `p = 0.004`,
`10 task -30% → 86 task -8,5%`, `/clear fra un task e l'altro -17,9%`, `CLAUDE.md 500-600
token -8,5%`. Sembrano misurazioni di **questo** video. Non lo sono: la sessione si chiama
"Lavagna Excalidraw plugin Claude Code" e i contenuti parlano di test su plugin e della
"trappola dei test piccoli", cioè di un **altro** lavoro dell'autore, usato qui solo come
esempio della tecnica ASCII-first. **Quei numeri non sono entrati in `atoms.json`** e sono
segnalati come estranei in `video-analysis.md`. Un ingest distratto li avrebbe attribuiti a
questo video con tanto di timestamp, e sarebbero sembrati verificati.

## Correzioni fatte all'ASR (dal frame, non a intuito)

| Trascrizione | Corretto | Fonte della correzione |
|---|---|---|
| "gestisco Mart, un'azienda" | **Martes AI** | `frame-020` (sito), `frame-067` (bio IG) |
| "la mia skill Real Editor" | **`/reel-editor`** | `frame-073` (pannello `/usage`) |
| "Cloud Code" / "Clode MD" | Claude Code / CLAUDE.md | ASR sistematico, corretto ovunque |

## Metodo di lavoro (per chi ripete la run)

- **Trascrizione**: `clean_transcript.txt` (950 righe, già deduplicato da una sessione
  precedente a partire dalle 7.616 righe del `.vtt`) letto **per intero in un solo passaggio**
  prima di aprire un solo frame. Ordine voluto: conoscere la struttura prima di guardare, per
  sapere cosa cercare nei frame.
- **Frame**: `scenes.md` usato come mappa, aperti **a batch di 5-6** (vincolo duro: con più
  immagini per richiesta vengono scartate in silenzio). 23 batch, 138 frame.
- **Zoom**: 12 frame ingranditi con uno script PIL locale (crop della regione + resize LANCZOS
  4x-8x), 27 ritagli aperti. I ritagli stanno nello **scratchpad di sessione**, non nel repo.
- **Ancora letterale per ogni atomo**: ogni voce di `atoms.json` ha un campo `ancora` con la
  frase esatta da cui nasce, verificata contro il transcript o contro il frame **prima** del
  salvataggio.
- **Consigli**: ogni affermazione sulla codebase DE è stata verificata con `Grep`/`Read`
  **prima** di essere scritta (elenco dei comandi nella pagina wiki). Nessuna patch applicata:
  Fase 1 = solo studio.

## Validazione di `atoms.json`

```
ATOMI: 47
ID duplicati: nessuno
ARCHI: 96
archi rotti: nessuno
atomi senza archi: nessuno
atomi senza ancora: nessuno
tipi: regola 15, numero 12, metodo 10, architettura 4, affermazione 3, strumento 2, entita 1
confidenza: osservato 44, + 3 marcati esplicitamente come non verificati
atomi solo-audio (frame n/a): KA-023, KA-035
```

**Sugli archi** — l'Impero aveva notato che i suoi atomi non hanno relazioni. Qui ogni atomo
porta un campo `relazioni` con archi tipizzati (`discende-da`, `quantifica`, `sostituisce`,
`contraddice`, `corregge`, `motiva`, `specializza`, `istanza-di`, `generalizza`, …).
**Scelta di compatibilità**: il file resta un **array piatto** come in
`max17-v01-artem/atoms.json`, e le relazioni sono un campo **dentro** ogni atomo. Un lettore
del vecchio schema ignora il campo in più e continua a funzionare; un lettore nuovo ottiene il
grafo. Nessun wrapper attorno all'array, che avrebbe rotto tutti i lettori esistenti.

I 96 archi sono stati validati a macchina (ogni `verso` punta a un `id` esistente): 0 rotti,
0 orfani. **Errore mio corretto qui**: nella prima stesura 14 archi puntavano a ID sbagliati —
avevo scritto relazioni verso atomi "DE" (`applicabile-a-DE`, `gia-in-DE`) che non esistono,
perché le osservazioni sulla codebase di Digital Empire **non sono atomi di questo video** e
stanno nella sezione Consigli della wiki. Rimossi o ripuntati, e la validazione è stata
rieseguita.

## Riepilogo finale

- **Frame unici guardati: 138/138 — 100%.** Nessun frame descritto senza essere stato aperto.
- **Trascrizione: 950/950 righe — 100%.**
- **Atomi: 47, con 96 archi validati.** 44 osservati, 3 marcati esplicitamente come non
  verificati.
- **Vincolo dichiarato**: sorgente 360p, testo minuto non recuperabile; citazioni testuali
  prese solo dalle viste ravvicinate.
- **Controllo sulla cifra dei token: fatto, appunto confermato, prova nel frame stesso.**
- **3 errori di lettura miei trovati e corretti**, lasciati a verbale con il meccanismo che li
  ha prodotti.

## Cosa resta aperto

1. **La sorgente a 360p — causa individuata, fix a una riga.**
   `empire-studio/scripts/frame_extractor.py:133` ha `--height` con `default=360`, e la riga 51
   lo passa a yt-dlp come `bv*[height<=360]`. Non è un limite di YouTube: **è l'Impero che
   chiede il formato peggiore**. Proposta (non applicata, Fase 1): far scegliere l'altezza in
   base al **tipo** di video invece che a un default fisso — 360 per i talk dal vivo, **720 per
   gli screen-recording**, che è il caso in cui il contenuto è il testo a schermo. Costa più
   banda e frame più pesanti, quindi è una decisione di costo, non una svista da correggere di
   nascosto. Finché resta com'è, **ogni futuro video-tutorial su Claude Code sarà studiabile
   solo dall'audio**, e questo studio ne è la dimostrazione.
   *(Secondario e separato: `yt-dlp` non è sul PATH della shell in cui girano le sentinelle —
   verificato in questa sessione. Non è la causa del 360p, ma impedisce a una sentinella di
   ri-scaricare alcunché di propria iniziativa.)*
2. **La cifra 1.500-3.000 token/pagina non è stata falsificata, solo tracciata.** Se serve
   davvero, va misurata in casa: `Read` su un PDF di N pagine e confronto del contatore.
3. **Nessuna patch applicata** (Fase 1 = studio). I consigli grep-verificati sono nella pagina
   wiki e aspettano una decisione.
