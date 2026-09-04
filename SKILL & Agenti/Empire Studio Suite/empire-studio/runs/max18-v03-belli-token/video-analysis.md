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

