# Video Analysis — max18-v03-belli-token

- **Video ID:** `1Dyld3y-V7Y`
- **Titolo reale (da `ingest.json`):** "Dammi 36 Minuti e Ti Farò Risparmiare MILIONI di Token su Claude"
- **Canale:** Riccardo Belli Contarini
- **Durata reale:** 2161 s = **36:01**
- **Lingua:** italiano
- **Capitoli ufficiali YouTube:** 20 (letti da `ingest.json`, non inventati)
- **Frame densi estratti:** 721 (1 ogni 3,0 s) + `manifest.json`
- **Frame unici sopra soglia (`scenes.md`):** 138
- **Run:** `empire-studio/runs/max18-v03-belli-token`

> **VINCOLO STRUTTURALE DI QUESTA RUN — leggere prima di fidarsi dei frame.**
> Il file `video.mp4` scaricato è **640x360, codec av1** (verificato con `ffprobe`), quindi
> i 721 frame PNG sono **640x360**. Su un video che è per il 70% screen-recording di
> Claude Code, di una lavagna Excalidraw e di terminali, **il testo piccolo a schermo non
> è recuperabile**: verificato con crop + upscale LANCZOS 4x-8x su `frame-005`, `frame-029`,
> `frame-007` — le lettere non ci sono nei pixel, l'upscale non le inventa.
> Conseguenza operativa dichiarata: **i contenuti testuali e i numeri di questo studio
> vengono dalla trascrizione audio (letta al 100%)**, e i frame servono a (a) classificare
> che tipo di schermata è mostrata in ogni scena, (b) leggere il testo grande davvero
> leggibile. Ogni volta che qualcosa è stato letto davvero dal frame è marcato **[LETTO]**;
> ogni inferenza è marcata **➕**. Nessun contenuto di frame è stato descritto senza aprirlo.

---

## Mappa del video

Il video ha una struttura dichiarata dall'autore a 1:24 ("Ho preparato come al solito una
lavagna dove andiamo a coprire punto per punto") e confermata visivamente: c'è **una
lavagna Excalidraw unica** che fa da indice di tutto il video, e ogni tecnica viene prima
letta sulla lavagna e poi dimostrata a schermo dentro Claude Code / l'app desktop.

### La lavagna madre — `frame-002.png` (0:03), ripresa in `frame-029.png` (1:24)

**[LETTO]** Titolo della lavagna: **"RISPARMIA I TOKEN - Tutte le Tattiche"**.

**[LETTO]** Sottotitolo: "Tutto quello che sposta il conto: come funziona, quanto vale,
quanto ci metti" (leggibile nella vista ravvicinata `frame-033.png`).

La lavagna è organizzata in un banner dorato in alto + **4 colonne colorate** + **2 riquadri
larghi in basso**:

| Blocco | Colore | Intestazione | Stato lettura | Corrispondenza audio |
|---|---|---|---|---|
| Banner | oro/crema | "PRIMA DI TOCCARE QUALSIASI COSA, MISURA" | **[LETTO]** su `frame-033` | 1:33 "prima di toccare qualsiasi cosa, gli strumenti di misurazione… sono tre" |
| Col. 1 | verde | "GRATIS, SUBITO" — sottotitolo "valgono più di tutto il resto" | **[LETTO]** su `frame-033` | 4:24 "partiamo con quelle tecniche che si possono utilizzare da subito" |
| Col. 2 | arancio | "UNA VOLTA SOLA" — sottotitolo "installa una volta, paga per sempre" | **[LETTO]** su `frame-033` | 13:30 "quelle tecniche che devi fare una volta" |
| Col. 3 | viola | "IL MODELLO ADATTO" | ➕ forma-parola su `frame-029`, non ravvicinato | 20:22 "andiamo a vedere la questione dei modelli" |
| Col. 4 | rosa/rosso | "NON FARLO" | ➕ forma-parola su `frame-029` | 22:58 "cose da non fare che sembrano furbe ma sono delle cavolate" |
| Basso sx | azzurro | "USA UNA CLI INVECE DI UN MCP" | ➕ forma-parola su `frame-029` | 24:52 "scegliamo delle CLI invece che degli MCP" |
| Basso dx | arancio | "IL GRAFO DEL CODICE" | ➕ forma-parola su `frame-029` | 28:32 "Code Graph e Graphify" |

**Errore mio corretto in corso d'opera, lasciato a verbale:** nella vista d'insieme
(`frame-002`/`frame-029`, board rimpicciolita) avevo letto la colonna 1 come "ADESSO,
SUBITO"; la vista ravvicinata `frame-033.png` mostra che dice **"GRATIS, SUBITO"**. È
esattamente il motivo per cui le righe marcate ➕ sopra restano ➕: la forma-parola a bassa
risoluzione **sbaglia**, anche quando l'audio sembra confermarla.

### Le card della lavagna leggibili davvero — `frame-033.png` (1:36) / `frame-088.png` (4:21)

Quando l'autore zooma sulla lavagna il testo diventa leggibile. **[LETTO]**:

**Banner "PRIMA DI TOCCARE QUALSIASI COSA, MISURA"** — tre voci:
- `/context` — "cosa occupa la finestra adesso"
- `/usage` — "se li hai bruciati, per [quando]" *(coda della riga non nitida)*
- `statusline` — "il contatore sempre a s[chermo]"

**Colonna verde "GRATIS, SUBITO"** (valgono più di tutto il resto):
- Card 1 — titolo "**/clear a ogni cambio di task**", claim in verde acqua "**azzera la
  base**", corpo: "La cronologia [smette] di essere ripo[sta]. Ogni altro filo taglia una
  fetta, questo azzera la torta."
- Card 2 — titolo "**modello ed effort scelti una volta**", claim "**eviti un 10x**", corpo:
  "La roba già pronta è legata al modello, cambiarlo la butta via tutta. Se vuoi il modello
  economico, parti[ci]."

**Colonna arancio "UNA VOLTA SOLA"** (installa una volta, paga per sempre):
- Card 1 — titolo "**spegni gli MCP che non usi**", claim "**-19.000 a sessione**", corpo con
  le cifre "26.000" e "20.000" *(il resto della riga non è nitido)*.
- Card 2 — titolo "**CLAUDE.md come indice**", claim "**sotto le 200 righe**", corpo: "[Lo]
  rilegge a ogni messaggio. Da 3.000 [scende] a [poche centinaia]… Regola dai doc Anthropic."

**NON leggibile**: il corpo delle card nelle viste d'insieme `frame-002`/`frame-029`
(verificato a 5x su `z029-col1.png`: si distinguono titolo scuro + sottotitolo verde acqua +
3 righe di corpo, ma non le parole), e le colonne viola/rosa + i due riquadri bassi, su cui
l'autore **non zooma mai** nei 138 frame unici. Il contenuto di quelle sezioni in questo
documento viene **solo dall'audio**, ed è dichiarato come tale.

---

## ⚠️ CONTROLLO SULLA CIFRA "1.500-3.000 TOKEN PER PAGINA PDF" — esito

**Domanda posta**: una sentinella precedente aveva lasciato l'appunto che questa cifra
verrebbe da un riassunto automatico di Google e non da una fonte primaria. Verificato in
prima persona, non preso per buono.

**1. La cifra è davvero nel video — SÌ.** Ancora letterale dalla trascrizione,
`clean_transcript.txt` riga 480, timestamp **[00:17:41]**:

> "Ogni pagina di un documento PDF elaborato con Cloud code consuma **tra i 1500 e 3000
> token**. Immaginatemi un PDF di 100 pagine, 200 pagine, 1000 pagine."

("Cloud code" è l'ASR italiano per "Claude Code".)

**2. La fonte a monte è debole — CONFERMATO, e si vede a schermo.** `frame-353.png`
(**17:36**, cioè **5 secondi PRIMA** che la cifra venga pronunciata) mostra il browser
dell'autore su una ricerca Google. **[LETTO]** parola per parola dopo zoom 5x:

- **Query digitata**: `claude code quanti token consuma per ogni pagina di un pdf`
- **Il pannello che risponde è un "AI Overview" di Google** (etichetta e icona letti):
  > "In genere, ogni pagina di un documento PDF elaborato da Claude Code consuma
  > **tra i 1.500 e i 3.000 token**."
- **La citazione attaccata a QUELLA frase è un chip "GitHub"** — non la documentazione
  Anthropic.
- Le tre voci di dettaglio sotto sono citate a: **Reddit · r/ClaudeAI +1** (elaborazione
  multimodale), **Reddit · r/ClaudeAI** (costi extra/overhead del tool Read), **Medium ·
  Vivek Singh P… +1** (convertire in Markdown risparmia "spesso del 50% o più").
- Nella colonna destra i due risultati organici sono **entrambi thread Reddit r/ClaudeAI**:
  "Sto raggiungendo i limiti di Claude quasi subito. Ormai è inutile." (5 Jan 2025) e
  "I tested PDF token usage Claude Code vs Claude.ai" (25 Jan 2026).
- L'autore ha disegnato **una freccia verde a mano** sopra lo screenshot che punta alla voce
  "Costi extra (Overhead)".

**VERDETTO.** La cifra va riportata come **detta dal relatore**, mai come dato verificato.
La catena reale è: *relatore → AI Overview di Google → GitHub/Reddit/Medium*. **Nessun
passaggio della catena è documentazione primaria Anthropic**, e questo non è un sospetto:
è leggibile a schermo nel video stesso.

**Nota di equità verso l'autore** (che va detta, altrimenti il rilievo è scorretto): il
relatore **non nasconde la fonte** — mostra la ricerca a schermo per 12 secondi
(`frame-353` → `frame-357`, 17:36-17:48). Quello che non fa è **dire a voce** che sta
citando un riassunto generato da un'AI: la pronuncia come se fosse un dato di fatto. Il
difetto è di etichettatura, non di occultamento.

**Cosa NON ho verificato e non fingo di aver verificato**: se la cifra sia poi vera. Non ho
misurato il consumo reale di una pagina PDF, e nessuna documentazione Anthropic è stata
aperta in questa sessione per confrontarla. L'unica cosa accertata qui è **la provenienza**.

**Da tenere separato** — le altre cifre sui PDF nel video sono di natura diversa: il test
"PDF da 300 pagine: ~500-600.000 token con Read, 150.000 token con l'hook, quindi 3-4x"
([00:19:53]-[00:20:12]) è dichiarato dall'autore come **misurazione fatta da lui**
("Io ho fatto diversi test, se non mi credete fateli anche voi"), non come citazione. Resta
non verificata da noi, ma è una classe di affermazione diversa dalla prima.

---

## Scena per scena

Legenda: **[LETTO]** = letto davvero sul frame aperto in questa sessione · **[AUDIO]** = viene
dalla trascrizione · **➕** = inferenza mia, non letta né detta.

### S1 · 0:00-1:24 — Apertura e promessa · `frame-001` → `frame-029`

**[AUDIO]** Promessa: "tagliare drasticamente il consumo dei token di Cloud Code con **10
mosse**. Sono gratis, le implementi oggi stesso e la prima funziona in 10 secondi." Annuncia
anche la parte "che nessuno ti dice": quali strategie hanno **conseguenze** sulla qualità, e
quali tool famosi che promettono "il 90% di risparmio" sono "fuffa".

**[LETTO]** `frame-002` (0:03): la lavagna Excalidraw intera, titolo "RISPARMIA I TOKEN -
Tutte le Tattiche". `frame-005`/`frame-006` (0:12/0:15): stacco su un'animazione scura con
testo grande "**Tu scrivi una riga. Lui rilegge tutto. Ogni volta.**" e i numeri **3**, **180**,
**540** (il 540 in rosso).

**[LETTO]** `frame-020`/`frame-021` (0:57/1:00): il sito dell'azienda dell'autore,
**Martes AI**. Case study leggibili a schermo: "**€82.271 generati da un agente AI su
WhatsApp**" per **Bluvacanze**; loghi/nomi clienti **Swiss Natural Med, Truck Italia,
Turnover, Shape Up, Clinica Oculistica Santa Lucia, Fantozzi & Associati**.
*(Nota: l'ASR della trascrizione scrive "gestisco Mart, un'azienda" — il nome corretto,
**Martes AI**, viene dal frame, non dall'audio.)*
Overlay ricorrenti nel video: "Formazione AI", "Analisi dei processi", "Soluzioni custom".

**[LETTO]** `frame-067` (3:18): profilo Instagram dell'autore — **134 post, 12.5K follower**,
bio "Aiuto le aziende italiane a integrare l'AI nei loro processi / Founder di Martes AI /
22.5K iscritti YouTube", link `www.martes-ai.com`. `frame-069`: la griglia dei reel, copertine
leggibili ("15 STRUMENTI AI COMPLETAMENTE [GRATIS]" 725K, "**70x MENO TOKEN**" 53.7K,
"CLAUDE CODE", "23.333 PROMPT"). **[AUDIO]** dichiara che i reel sono editati e postati
automaticamente da Claude tramite una sua skill.

### S2 · 1:24-4:24 — Gli strumenti di misurazione · `frame-029` → `frame-097`

Capitolo ufficiale: "Gli strumenti di misurazione: /context, /usage, status line" (96s).

**[AUDIO]** I tre strumenti: `/context`, `/usage`, la **status line**. Regole dette:
- "Opus nello specifico ha **un milione di token**. Sonnet se non sbaglio sta ancora a
  **200.000**."
- Su una chat **nuova, senza aver scritto nulla**, è già al **6%** dello usage = "**60.000
  token**" occupati da file di memoria + system prompt (CLAUDE.md) + server MCP + skill.
- **"Come regola bisogna stare fra il 3 e il 6%"** su una nuova conversazione. "Molti dei
  nostri clienti quando partono con /context stanno già al **20%**."

**[LETTO]** `frame-110` (5:27) conferma a schermo il dato del 6%: pannello contesto
"**Finestra di contesto — 59.5k / 1M (6%)**". Quindi il "milione di token" e il "6%" non sono
solo detti, si vedono.

**[LETTO]** `frame-073` (3:36) — il pannello `/usage` reale, la schermata più densa di numeri
del video:
- "Limite di 5 ore — Si ripristina tra 4 h 46 min — **1%**"
- "Settimanale · tutti i modelli — Si ripristina mer 18:00 — **24%**"
- "Settimanale · **Fable** — 0%"
- "Questa sessione: Costo **0,00 USD**, Attivo 2s"
- "**93%** eseguito oltre 150k di contesto" · "**30%** eseguito mentre 4+ sessioni erano in
  parallelo"
- Classifica skill per consumo: "**/reel-editor 29%**, /apple-design 2%, /resource-page 1%,
  /post-all 1%, /repurpose 1%"
- Disclaimer a schermo: "Ultime 24h · misure approssimative e sovrapposte · solo questo
  computer, escluso claude.ai"

*(L'ASR scrive "la mia skill Real Editor": il nome vero, letto a schermo, è **`/reel-editor`**.)*

> ⚠️ **Contraddizione visibile a schermo e mai commentata dall'autore.** In fondo allo stesso
> pannello `/usage` di `frame-073` c'è il suggerimento ufficiale di Claude:
> "**Suggerimento: Le sessioni più lunghe sono più costose anche con la cache. Usa /compact a
> metà attività, /clear quando passi a nuove attività.**"
> Cioè: mentre l'autore costruisce la tesi "/compact è la cavolata più grossa", il prodotto
> stesso, nella schermata che lui mostra, consiglia /compact. L'autore non ci passa sopra:
> non lo nota e non lo confuta. È il punto più interessante da tenere per DE.

**[LETTO]** `frame-110` (5:27): il selettore modelli aperto — "**Fable 5 (1), Opus 5 ✓ (2),
Sonnet 5 (3), Haiku 4.5 (4)**, Altri modelli >" + "Modalità rapida: Abilita la modalità
veloce". In basso a destra l'indicatore "**Opus 5 | Extra**" (modello + effort).

### S3 · 4:24-5:22 — `/clear` a ogni cambio di task · `frame-088` → `frame-107`

Capitolo: "clear ad ogni cambio di task" (272s).

**[LETTO]** Card sulla lavagna (`frame-093`, `frame-107`, `frame-122`):
> "**/clear a ogni cambio di task**" — "**azzera la base**" — "La cronologia smette di essere
> rispesta. Ogni altro fix taglia una fetta, questo azzera la torta."

**[AUDIO]** Dimostrazione: dopo un solo "Ciao, come stai?" è al **15%** della finestra; con
`/clear` torna al 6% di partenza. "Senza che necessariamente dovete aprire una nuova chat."

### S4 · 5:22-6:07 — Modello ed effort si scelgono una volta sola · `frame-110` → `frame-126`

Capitolo: "Modello ed effort si scelgono solo all'inizio" (319s).

**[LETTO]** Card: "**modello ed effort scelti una volta**" — "**eviti un 10x**" — "La roba già
pronta è legata al modello, cambiarlo la butta via tutta. Se vuoi il modello economico,
partici."

**[AUDIO]** Livelli di effort elencati a voce: "basso, medio, alto, extra, max, ultra".
Metafora: cambiare modello a metà = "scegliere un nuovo cervello", e quel cervello deve
riprendersi tutta la conversazione da capo.

### S5 · 6:07-7:53 — Perché `/compact` è un errore · `frame-126` → `frame-174`

Capitolo: "Perché /compact è un errore" (367s).

**[LETTO]** Card: "**/rewind, non /compact**" — "**non ricostruisci nulla**" — "Torni a un
punto che il modello ha già pronto. È il posto dove quasi tutti usano /compact e sbagliano."

**[AUDIO]** Due motivi contro `/compact`: (1) spesso basta `rewind`; (2) se lasci a Claude la
libertà di riassumere, "sceglierà lui cosa tenere". Soglia dichiarata: "**se arrivi al 40-50%
del tuo contesto perdi di un sacco la qualità**. Quindi dopo il 40-50% cambia chat."

### S6 · 7:53-11:39 — `rewind` e il file di handoff · `frame-148` → `frame-235`

Capitolo: "rewind e il file di hand-off al posto del compact" (473s).

**[AUDIO]** `rewind` "ci permette di ritornare a un certo punto della conversazione **senza
consumare alcun token**", identico in terminale, app e estensione VS Code. Il **file di
handoff** contiene: obiettivo, a che punto siamo, cosa abbiamo provato che non ha funzionato,
problemi incontrati e come risolti, decisioni prese, file toccati, dove vogliamo andare.
L'autore ha una skill `/handoff` che fa domande prima di scrivere il file; la mette fra le
risorse nel secondo link in descrizione.

**[LETTO]** Card: "**un file di handoff, non /compact**" — "**poche centinaia di token**" —
"Scrivi lo stato e riparti da un prefisso piccolo. E scegli tu cosa sopravvive; soprattutto
le strade già fallite." *(L'ultima clausola — portarsi dietro le strade **fallite** — è sulla
lavagna ma non viene detta a voce: è un contenuto che esiste solo nel frame.)*

**[LETTO]** `frame-185` (9:12) — l'animazione sul costo quadratico, testo integrale:
> "**Tu scrivi una riga. Lui rilegge tutto. Ogni volta.**
> I modelli non hanno memoria. A ogni invio il modello si rilegge la conversazione
> dall'inizio per poterti rispondere: il tuo contesto, tutte le sue risposte, ogni file
> aperto. Tu scrivi sempre la stessa quantità. Quello che rilegge lui cresce a ogni turno."
>
> Pannello destro: "**TURNO 2** · IL TUO MESSAGGIO: **180 token** · QUELLO CHE RILEGGE PER
> RISPONDERTI: **360 token**". In `frame-006` lo stesso pannello è al **turno 3**: **180** /
> **540**. Sotto, un istogramma a scalini che cresce.

➕ **Inferenza**: il modello dell'animazione è "messaggio costante da 180 token, riletto
n volte al turno n" — cioè crescita lineare del costo per turno e quadratica cumulata. Il
video **dice** "è come se fosse esponenziale" ([00:09:48]): a rigore è **quadratico**, non
esponenziale. Segnalo lo scarto perché è una imprecisione di linguaggio del relatore, non un
errore dell'animazione, che invece è corretta.

**[LETTO]** `frame-203` (10:06) — trovata di valore. Sullo schermo c'è la risposta di Claude
all'autore mentre prepara **questo stesso video**, e contiene una regola editoriale che lui si
è fatto scrivere in un `style.md`:
> "Salvata come definitiva in `script.md`, la v5 archiviata accanto. 238 parole, circa 75
> secondi. La scelta di '**DRASTICAMENTE**' al posto del numero l'ho scritta come regola in
> `style.md`, perché vale oltre questo video: **se il corpo è pieno di numeri misurati,
> l'intro promette con un avverbio, non con una cifra**. Una cifra in apertura o è gonfiata,
> e allora contraddice un video che smonta chi promette percentuali, oppure è precisa, e
> allora non è una promessa ma un dettaglio che chi guarda non sa ancora dove mettere.
> L'avverbio tiene alta la promessa, i numeri la dimostrano nei capitoli dove si vedono a
> schermo."

Questo spiega la prima riga del video ("tagliare **drasticamente**") e mostra il metodo di
lavoro dell'autore: le regole di stile vivono in un file, non in testa.

### S7 · 11:39-13:35 — Il diagramma ASCII prima di costruire · `frame-235` → `frame-271`

Capitolo: "Il diagramma ASCII prima di costruire qualsiasi cosa di grafico" (699s).

**[LETTO]** Card: "**diagramma ASCII prima di costruire**" — "**togli il giro**" — "Il lavoro
rifatto non avviene proprio. Nessun compressore può farlo: agiscono su ciò che è già successo."

**[AUDIO]** Il problema: costruisci un front-end, non ti piace, e parte il ciclo "sposta
questo, cambia il font" — ogni giro costa. La soluzione: farsi fare prima un diagramma ASCII
("delle lineette, dei trattini") che costa pochissimo, e correggere lì. Consiglio operativo:
"in ogni skill che avete per il design metteteci uno step prima che vi consente di avere un
diagramma ASCII prima di generare qualsiasi cosa".

**[LETTO]** `frame-246`/`frame-250`/`frame-252` (12:15-12:33): ricerca Google "diagrammi
ascii" — risultati leggibili **ASCIIFlow**, **Diagon** (`ArthurSonzogni/Diagon`),
**ascii-diagram** (GitHub Topics), "ASCII and Why Developers Should Use ASCII Diagrams — The
New Stack".

**[LETTO]** `frame-334` (16:39): esempio reale di diagramma ASCII prodotto da Claude, in una
sessione intitolata "Lavagna Excalidraw plugin Claude Code". Contiene numeri di **un altro**
progetto dell'autore (un test sui plugin): "p = 0.004", "10 task -30% → 86 task -8,5%",
"/clear fra un task e l'altro — nel prompt di sistema **-17,9%**", "CLAUDE.md 500-600 token —
come skill in una cartella **-8,5%**", "la trappola dei test piccoli", "QUELLO CHE BATTE I
PLUGIN, E NON SI INSTALLA".
➕ **Inferenza dichiarata**: questi numeri appartengono a un video/esperimento **diverso** da
quello in esame — la lavagna serve solo da esempio della tecnica ASCII-first. **Non vanno
attribuiti a questo video** e non li ho messi fra gli atomi come misure di questo lavoro.

### S8 · 13:35-14:01 — Spegni gli MCP che non usi · `frame-271` → `frame-283`

Capitolo: "Spegni gli MCP che non usi" (815s).

**[LETTO]** Card (`frame-271`, `frame-280`, `frame-307`), numeri pienamente leggibili:
> "**spegni gli MCP che non usi**" — "**-47.000 a sessione**" — "**GitHub 26.000, Slack
> 21.000**, caricati prima che tu scriva. **/context deve dire 'deferred'**."

**Correzione mia messa a verbale**: nella prima vista più lontana (`frame-033`) avevo letto
"-19.000"; nella vista ravvicinata è **-47.000**, e i due addendi 26.000 + 21.000 tornano.
Secondo errore di lettura a bassa risoluzione corretto in corso d'opera.

### S9 · 14:01-15:17 — Il CLAUDE.md come indice · `frame-283` → `frame-309`

Capitolo: "Il CLAUDE.md trattato come un indice" (841s).

**[LETTO]** `frame-283` (14:06) — animazione dedicata, testo integrale:
> "**Il CLAUDE.md è un *indice*, non un documento.**
> Si rilegge **a ogni messaggio**, per tutta la conversazione. Con uno da **4.000 token**,
> ogni conversazione parte da 4.000 token indietro. E poi li ripaga."
> Confronto a due pannelli: "CLAUDE.md come documento — **4.000 TOKEN**" (barre rosse) vs
> "CLAUDE.md come indice — **450 TOKEN**" (righe verdi sottili). In basso: "6 MESSAGGI" e in
> rosso "**24.000**".
> Nota a piè di pagina: "La regola dai doc di Anthropic: **sotto le 200 righe**."

**[LETTO]** Card: "**CLAUDE.md come indice**" — "**sotto le 200 righe**" — "Si rilegge a ogni
messaggio. **Dice DOVE stanno le cose, non le contiene.** Regola dai doc Anthropic."

**[AUDIO]** Stessa aritmetica con 8 messaggi: 4.000×8 = 32.000 contro 450×8 = 3.600. Il suo
CLAUDE.md del second brain sta "sulle **166 righe**".

> **Nota sulla fonte**: qui l'autore attribuisce esplicitamente la soglia "sotto le 200 righe"
> alla documentazione Anthropic, sia a voce sia sulla lavagna. **Non l'ho verificata** in
> questa sessione (nessun doc Anthropic aperto): la riporto come *attribuzione fatta
> dall'autore*, non come regola confermata. È comunque un'attribuzione **dichiarata**, a
> differenza della cifra sui PDF.

### S10 · 15:17-16:45 — Un CLAUDE.md per ogni cartella · `frame-309` → `frame-337`

Capitolo: "Un CLAUDE.md per ogni cartella" (917s).

**[LETTO]** Card: "**un CLAUDE.md per cartella**" — "**-7.160 a sessione**" — "Il root si
carica **SEMPRE**, quelli nelle sottocartelle **solo se l'agente entra lì dentro**."

**[AUDIO]** L'autore attribuisce il trucco a "**Andrew Carpati** [Andrej Karpathy], uno dei
membri fondatori di OpenAI, adesso sta ad Anthropic, ha inventato tutto il concetto di second
brain con l'LLM wiki".
> ⚠️ **Da trattare con cautela.** Questa attribuzione contiene almeno un errore verificabile
> senza fonti esterne: Karpathy è stato fondatore di OpenAI e poi in Tesla, e alla data di
> questo studio **non risulta a noi che lavori in Anthropic**. Non ho aperto fonti esterne per
> accertarlo in questa sessione, quindi lo segnalo come **affermazione dubbia del relatore, da
> non propagare**, non come falsità accertata.

**[LETTO]** `frame-315` (15:42), `frame-333`, `frame-337`: il second brain dell'autore aperto
in VS Code. Albero leggibile: `.claude`, `notify`, `obsidian`, `superpowers`, `code`,
`Context`, `Daily`, `Departments`, `Intelligence`, `Library`, `Onboarding`, `outputs`,
`Projects`, `reference`, `Resources`, `Team`, `workspaces`, `.claudeignore`, `.env`,
`.gitignore`, `CLAUDE.md`, `index.md`. Nel CLAUDE.md aperto si leggono sezioni "# Organizzazione",
"## Regola", numerate fino a "23." / "24.", e una sezione "# Anti-Pattern".

### S11 · 16:45-17:50 — Archivia le skill, accorcia le descrizioni · `frame-341` → `frame-353`

Capitolo: "Archivia le skill inutilizzate e accorcia le descrizioni" (1005s).

**[LETTO]** Card: "**archivia le skill e accorcia le descrizioni**" — "**migliaia a
sessione**" — "**Skill e descrizioni si caricano ogni volta, anche quelle che non parti mai.**
Restano installate, smettono di pesare."

**[AUDIO]** Come farlo: chiedere a Claude di accorciare le descrizioni delle main skill "poi
vammi a fare un test end to end per vedere che le skill funzionano comunque". "È una cosa che
fai una volta e aiuta tantissimo."

### S12 · 17:50-20:17 — L'hook che estrae il testo dai PDF · `frame-353` → `frame-408`

Capitolo: "L'hook che estrae il testo dai PDF" (1070s).

Per la **cifra 1.500-3.000 token/pagina** vedi la sezione dedicata sopra: detta a
[00:17:41], fonte a schermo = AI Overview di Google.

**[LETTO]** Card: "**hook PDF e filtro sull'output**" — "**3-4x sui PDF**" — "Il Read manda
ogni pagina come testo **PIÙ** immagine. E l'output dei comandi lo tagli una volta, con un
filtro che scrive l'agente."

**[AUDIO]** Definizione di hook data dall'autore: "una **regola deterministica** di Claude che
possiamo far attivare ogni qualvolta succede un determinato evento… un `if`". Esempi citati:
sincronizzare su Drive/GitHub a ogni file creato; controllare i documenti caricati per
**prompt injection**.
Test dichiarato: PDF da **300 pagine** → con `Read` "circa **500-600.000 token**", con l'hook
"**150.000 token**", quindi "risparmi dalle **3 alle 4 volte**".

**[LETTO]** `frame-385` (19:12) — la schermata più utile del video per DE: Claude descrive
l'hook reale dell'autore, e si legge quasi per intero:
> Percorso: **`~/.claude/hooks/pdf-read-as-text.py`**, registrato in `~/.claude/settings.json`
> come **PreToolUse con matcher `Read`**, globale su tutti i progetti.
> Quando fa `Read` su un `.pdf`:
> 1. estrae il testo con **`pdftotext -layout`**;
> 2. lo mette in cache in **`~/.claude/pdf-text-cache/<nome>.<hash>.txt`**;
> 3. **riscrive il `file_path`** verso quel `.txt`, così Claude legge testo e le pagine non
>    entrano in contesto come immagini renderizzate.
> Test live mostrato: `permissionDecision: allow`, messaggio "PDF → testo (1 pag, ~**1.296
> token** di immagini risparmiati)".
> **Quando si tira indietro da solo**: se il testo estratto sta **sotto 200 caratteri per
> pagina** (scansioni, slide tutte immagini), o se `pdftotext` manca/va in errore → passa il
> PDF originale.
> **Override manuale** per quando serve il visivo: `touch ~/.claude/pdf-visual-once`; l'hook
> "consuma la sentinella" e lascia passare l'originale **una volta sola**.
> Limite dichiarato a schermo: sui PDF a più colonne `pdftotext` **appiattisce le colonne**.

**[AUDIO]** Conferma il caso d'uso opposto: se il PDF ha grafici e schemi da guardare, "basta
che glielo dici… non eseguire quello script là perché questa volta devo analizzare i grafici".

### S13 · 20:17-22:27 — Quale modello per quale task · `frame-408` → `frame-451`

Capitolo: "Quale modello scegliere in base al task" (1217s).

**[LETTO]** Intestazione colonna (`frame-410`): "**IL MODELLO GIUSTO**" — "la qualità è essa
stessa un risparmio". *(Terza correzione: dalla vista lontana avevo letto "IL MODELLO ADATTO".)*

**[LETTO]** Le tre card:
- "**coding e planning veri**" — "**resta sul modello di frontiera**" — "Un risultato da
  rifare costa più di quello che hai risparmiato scegliendo il modello economico."
- "**routine, skill, sub-agenti, /chrome**" — "**Haiku e Sonnet vanno benissimo**" — "I job
  schedulati che sai già riuscire, la navigazione, la manovalanza. Lì il modello grosso non
  serve."
- "**si sceglie per skill e per sub-agente**" — "**mai a metà sessione**" — "Cambiare modello
  in corsa butta via la roba pronta. **Lo passi dentro la skill e la sessione principale non
  la tocchi.**"

**[AUDIO]** Modelli di frontiera nominati: "che sia Fable, Opus, GPT 5.6, Grock 4.6". Per
skill e routine: "il **90%** dei casi Haiku o Sonnet va benissimo" (in un altro passaggio dice
"il 99% di skill e routine").
**[LETTO]** `frame-414`: rimanda a un suo altro video, "Claude Code + OmniRoute = AI Gratis e
Illimitata" (23:21).

### S14 · 22:27-23:28 — Hook e task schedulati dimenticati · `frame-447` → `frame-459`

Capitolo: "Controlla hook e task schedulati dimenticati" (1347s).

**[LETTO]** Card: "**i task schedulati**" — "**pagano dieci volte**" — "Mandano il contesto
**INTERO** a ogni scatto, e sotto la frequenza oraria non trovano mai niente di pronto. Anche
alle 3 di notte."

**[AUDIO]** L'autore racconta di aver fatto "un audit completa" e di aver trovato "tantissimi
task schedulati che mi consumavano tantissimo del mio usage".

### S15 · 23:28-24:52 — Cose da non fare · `frame-459` → `frame-498`

Capitoli: "Cose da non fare: screenshot, prompt troppo corti, tool fuffa" (1408s) e "Usa
l'output style invece dei 'compressori' di contesto" (1458s).

**[LETTO]** Intestazione colonna: "**NON FARLO**" — "sembrano furbe, costano". Le cinque card,
lette per intero:

| Card | Claim | Corpo |
|---|---|---|
| **/compact per risparmiare** | **il messaggio più caro** | "Per riassumere rimanda tutto, e poi butta via la roba pronta. Compra continuità, non risparmio." |
| **screenshot del testo** | **2.700 token** | "Per duecento parole. E un'immagine l'agente non la può modificare. Incolla il testo." |
| **dare PDF grezzi** | **paghi due volte** | "Il testo della pagina PIÙ l'immagine della stessa pagina. Vedi l'hook nella colonna qui accanto." |
| **prompt più corti** | **lo 0,01% del conto** | "Quello che digiti tu è un errore di arrotondamento. I prompt vaghi costano, ma per il **lavoro rifatto** che innescano." |
| **i tool che promettono il 90%** | **fra zero e negativo** | "Li ho provati tutti. Comprimono l'unica parte del conto che non conta, e ti mettono in mezzo uno strato fragile." |

**[LETTO]** `frame-477`/`frame-480`: accanto all'ultima card ci sono **due loghi**, il badge
nero "**Caveman**" e uno scudo verde "**RTK AI**". Sono i due tool nominati anche a voce.

**[LETTO]** `frame-481` (24:00) — il README GitHub di **caveman**, aperto dall'autore:
> "why using many token when few do trick / Original skill made agents say less. Caveman 2
> makes them read less too. / **33.2% fewer provider-reported input tokens** in a pinned
> Claude Code benchmark. / Keep your agent. Brain big. Context small."
> Esempio a schermo: "Normal agent — **69 tokens**" vs "Caveman agent — **19 tokens**".
> Badge "Product Hunt" e "Repository Of The Day". Install: `npm install -g @caveman-ai/cli`.

Cioè: la pagina del tool rivendica **-33,2%**; l'autore, avendolo provato, dice "fra zero e
negativo" e "spesso salta informazioni… lascia cose fondamentali". Le due affermazioni sono in
diretto conflitto e **nessuna delle due è verificata da noi**.

**[AUDIO]** L'alternativa proposta al posto dei compressori: cambiare l'**output style**
(Settings → output style → "conciso"), che "ci dà il risultato senza preamboli".

### S16 · 24:52-28:32 — CLI invece di MCP (il taglio più grosso) · `frame-498` → `frame-572`

Capitolo: "CLI invece di MCP" (1492s).

**[LETTO]** `frame-570`/`frame-499`/`frame-551` — il riquadro, letto per intero:
> "🔧 **UNA CLI INVECE DI UN MCP** — il manuale di un MCP entra in contesto anche se quel tool
> non lo usi"
>
> | **MCP: il manuale entra all'avvio** | **CLI: zero finché non la chiami** |
> |---|---|
> | GitHub **26.000** · Slack **21.000** | il comando non occupa niente |
> | resta lì anche da spento | una riga in CLAUDE.md e sa che esiste |
> | l'indice cresce a ogni tool | è un fatto architetturale |
>
> Barra "quanto pesa in contesto, prima che tu scriva": **MCP 26.000** (barra rossa lunga) vs
> **CLI ~40 token, e solo quando serve** (quadratino verde).
>
> Nota finale: "**Il taglio più grosso della lista sta qui, e non è un tool: è scegliere un
> altro modo di collegare le cose.** Verifica sempre che `/context` dica '**deferred**': vuol
> dire che i manuali restano zitti finché non servono."

**[AUDIO]** La spiegazione: una CLI è "un'API ma per i terminali"; l'MCP è "un mega wrapper"
che carica **tutti** i metodi anche se ne usi tre; l'API grezza invece restituisce JSON nati
"per essere letti da umani", lunghissimi, che finiscono anch'essi in contesto. La CLI risolve
entrambi i problemi. Regola personale dell'autore, messa nel suo CLAUDE.md: "**cerca sempre se
c'è una CLI prima di un MCP**".

**[LETTO]** Dimostrazioni a schermo: `frame-535` (26:42) ricerca immagini "api response json"
piena di JSON lunghi + pannello Stack Overflow; `frame-543` (27:06) disegno a mano dei metodi
`send_email` / `write_draft` / `read_email` che puntano a un software "S2"; `frame-566`/`567`
(28:15/28:18) la pagina **Supabase MCP Server** della doc ufficiale, con il suo warning
("Connecting an LLM to your Supabase projects carries security risks") e la ricerca Google
"supabase cli" come alternativa.

### S17 · 28:32-30:43 — CodeGraph e Graphify · `frame-574` → `frame-616`

Capitolo: "CodeGraph e Graphify per i grafi di conoscenza" (1771s).

**[LETTO]** `frame-574` (28:39) — animazione:
> "**Senza grafo cerca *a tentoni*. E ogni tentativo resta in contesto.**
> Apre un file, non è quello. Ne apre altri cinque. **Ogni apertura entra nel contesto e ci
> resta**, anche quella sbagliata. Con un grafo fa una domanda sola."
> Contatore "CONTESTO" sul pannello "Senza grafo": **3480** (in rosso). Pannello "Con il
> grafo": grafo esagonale di nodi, contatore molto più basso *(cifra non leggibile con
> certezza — non la riporto)*.

**[LETTO]** `frame-601`/`frame-628` — il riquadro completo:
> "🔍 **IL GRAFO DEL CODICE** — CodeGraph e Graphify: due mestieri diversi, e una soglia sotto
> cui non conviene nessuno."
> - "**senza grafo cerca a tentoni**": apre un file non è quello / ne apre altri cinque / ogni
>   apertura resta in contesto
> - "**con il grafo, una domanda sola**": chiede alla mappa dov'è / va dritto al nodo giusto /
>   il file poi lo legge lo stesso
> - "**CodeGraph**: il sensore residente per il **CODICE**: si indicizza da solo e un watcher
>   lo tiene aggiornato."
> - "**Graphify**: la torcia per un **BRAIN**: PDF, immagini, markdown, output Obsidian. Ma il
>   grafo te lo costruisce **un agente, e lo paghi**."
> - Riquadro giallo: "**Sotto i ~500 file non conviene nessuno dei due: il grafo costa più di
>   quello che ti fa risparmiare.** Non lo dico io: i manutentori di CodeGraph lo scrivono nel
>   loro README, su un repo da **102 file** il tool consuma più del nativo."

**[LETTO]** Le due repo aperte a schermo:
- `frame-594`/`frame-595`: **`colbymchenry/codegraph`** — "Pre-indexed code knowledge graph,
  auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity,
  Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local". **68.8k
  stelle**, 163 watching, 955 commit, MIT. Sezione "**4. No more syncing!**": "Auto-sync is
  enabled by default… **The index is never stale, and there is nothing to re-run.**" +
  disinstallazione con `codegraph uninstall`.
- `frame-598`/`frame-599`: **Graphify** — "**#2 Repository Of The Day**", Apache-2.0, **162
  contributors**, Python 100%, "Downloads 5.7K". Testo: "Type `/graphify` in your AI coding
  assistant and it maps your entire project (code, docs, PDFs, images, videos) into **a
  knowledge graph you can query instead of grepping** through files." Tre punti: "**Code maps
  for free, fully local**" (tree-sitter AST, deterministico, nessun LLM, niente esce dalla
  macchina — mentre "Docs, PDFs, images and video use your assistant's model, or a configured
  API key, for a semantic pass"); "**Every edge is explained**" (ogni arco è taggato
  `EXTRACTED` o `INFERRED`); "**Not a vector index**" (nessun embedding, grafo vero da
  attraversare). Install: `uv tool install graphify` → `graphify install`.

### S18 · 30:43-33:14 — Trasforma in codice ciò che è ripetibile · `frame-616` → `frame-666`

Capitolo: "Trasforma in codice ciò che è ripetibile" (1843s).

**[LETTO]** `frame-634`/`frame-652` — il riquadro:
> "⚙️ **TRASFORMA IN CODICE** — quello che non ha bisogno di un modello non deve pagarlo"
>
> | **lo rifà l'AI, ogni volta** | → *lo fai scrivere UNA volta sola* → | **lo fa uno script** |
> |---|---|---|
> | paghi token a ogni giro | | zero token, sempre |
> | ogni tanto sbaglia | | non sbaglia mai |
> | il risultato cambia | | gira uguale ogni volta |
> | **~2.000 token a giro** | | **0 token** |
>
> Riquadro giallo: "**L'AI serve per il GIUDIZIO. Tutto il resto è esecuzione, e l'esecuzione
> ripetibile è codice.**
> Come si trova cosa trasformare: lancia il prompt di audit e fatti dire quali pezzi del tuo
> flusso non hanno bisogno di un modello. Quelli diventano uno script dentro la skill, e da lì
> in poi non li paghi mai più. **Ogni 'ricordati di' è un candidato hook: è l'unica categoria
> di consiglio che sopravvive al fatto che te ne dimentichi.**"

**[AUDIO]** Aneddoto: l'autore riporta una conversazione col **CTO di ClickUp** ("uno dei CRM
più grossi del mondo, valutato a 4 miliardi"), incontrato in Montenegro con un network di
creator, che gli avrebbe detto: "questa è proprio la nostra regola aurea… quando andiamo a
costruire nuove feature andiamo a rivedere il codice, dove possiamo cambiare quella chiamata
API a Claude/OpenAI in codice, il più possibile, perché è più veloce, non sbaglia e risparmi".
➕ Riportato come **aneddoto di seconda mano non verificabile**: nessun documento a schermo lo
conferma.

**[LETTO]** Sotto la lavagna, in `frame-652`, una didascalia: "**Le mosse che contano di più
non hanno un numero: cambiano la base su cui tutte le altre sono una...**" *(la riga è tagliata
dall'inquadratura, non la completo).*

### S19 · 33:14-34:40 — I sotto-agenti · `frame-666` → `frame-696`

Capitolo: "Sottoagenti: quando usarli e i sottoagenti Haiku" (1994s).

**[LETTO]** `frame-667`/`frame-670`/`frame-685` — il riquadro, il conto completo:
> "👥 **I SUB-AGENTI SPOSTANO [il conto]** — non risparmiano: guarda i **due** conti, non solo
> quello che vedi tu"
>
> | quello che vedi tu | **il conto vero** |
> |---|---|
> | **tornano 420 token** | il suo system prompt — **2.400** |
> | | la sua copia della memoria — **1.400** |
> | | i suoi strumenti e permessi — *(cifra non leggibile)* |
> | | la lettura vera e propria — **6.000** |
> | | → **9.800 spesi per risparmiarne 5.700** |
>
> Riquadro giallo: "**Usali SOLO per le azioni in bulk: quaranta file, dieci fonti, roba di
> cui ti serve solo il verdetto. È la condizione che ribalta il conto.**"
> E in coda: "**metti i sub-agenti su Haiku**, e non tocca la cache della sessione principale."

**[AUDIO]** Conferma: "spesso magari spendiamo 9800 token per risparmiare i 5700"; "**pro tip,
i sottoagenti Haiku vanno una bomba**"; usarli "solo per le azioni in bulk: devi leggere 40
file, devi analizzare 10 fonti".

### S20 · 34:40-36:01 — Chiusura e pitch · `frame-696` → `frame-721`

**[AUDIO]** Ricapitolazione: "quasi tutto ciò che so sul risparmio dei token su Cloud Code…
questi concetti si applicano anche a Codex, si applicano anche a qualsiasi altro coding agent".
Poi il pitch di Martes AI: formazione del team su Claude Code / Claude Cowork / Codex, coaching
one-to-many, analisi dei processi e costruzione di soluzioni su misura. Frase di
posizionamento: "**Non siamo l'azienda di consulenza che ti fa l'analisi dei processi e ti dà
il deck di 200 pagine, ma andiamo ad eseguire e a costruire.**"

**[LETTO]** `frame-700`/`frame-701`/`frame-702`: spezzoni video di aule di formazione reali
(slide proiettata leggibile: "MCP (o Connettori) — 2.6 MCP sono ponti fra AI e software"),
sempre con l'overlay "Formazione AI". `frame-717` e `frame-721` (35:48 e 36:00) sono **neri**:
il video finisce in dissolvenza.

**Chiusura mancante rispetto alla promessa**: il video apre annunciando "**10 mosse**". Sulla
lavagna e nel parlato le tecniche distinte sono **più di 10** (ne ho contate 14 di risparmio +
5 anti-pattern). Nessuna numerazione "1 di 10, 2 di 10…" compare mai, né a voce né a schermo.
➕ Segnalato come scarto fra promessa e struttura, non come errore di contenuto.

