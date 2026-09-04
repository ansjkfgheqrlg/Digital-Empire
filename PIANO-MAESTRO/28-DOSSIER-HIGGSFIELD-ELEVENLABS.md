---
Type: SOURCE
Status: Active
Tags: #tool #video #voce #acquisto #higgsfield #elevenlabs #outreach #produzione-contenuti
Created: 2026-09-04
Last updated: 2026-09-04 (revisione 2 — scansione completa del sito)
Autore: Emperator (per Max)
---

# Dossier 28 — Higgsfield ed ElevenLabs: mappa completa e piano d'acquisto

> **Revisione 2.** La prima stesura era superficiale su Higgsfield: avevo letto il listino e
> tre pagine, e da li' avevo concluso che non potesse sostituire Fliki. Max ha detto di entrare
> davvero. Sono entrato: **60 pagine del sito lette con Playwright sul DOM renderizzato**, piu'
> la documentazione API, l'help center, i Termini e la normativa. **Due conclusioni della
> revisione 1 erano sbagliate e qui sono corrette**, segnate con CORREZIONE.

---

## 0. LE CINQUE COSE CHE CONTANO

1. **CORREZIONE — Higgsfield sostituisce Fliki, e meglio.** Esiste un modulo dedicato, **AI Long Video Generator**, che dichiara esplicitamente il nostro caso d'uso: *"Build YouTube and long-form content... faceless channels... tutorials, breakdowns, video essays... full episodes with consistent voice and look."* Script in ingresso, video multi-scena da minuti in uscita, audio nativo incluso, export MP4 in 16:9, 9:16 e 1:1.
2. **Il Text-to-Speech di Higgsfield ha ElevenLabs v3 come modello di default.** Comprando Higgsfield ottieni le voci ElevenLabs dentro i suoi crediti. Questo ridimensiona ElevenLabs a due soli compiti che Higgsfield non copre: l'**agente telefonico** e lo **speech-to-speech sulla tua recitazione**.
3. **CORREZIONE — sui caroselli avevo torto.** Ho guardato le tue slide. Sono un sistema di design coerente, non immagini generate: Nano Banana Pro a 2 crediti ti darebbe la fotografia di una slide, non quella slide. Arena resta il posto giusto per i caroselli; il problema li' e' l'affidabilita' dell'automazione, non la qualita'.
4. **Higgsfield non e' un generatore video: e' un sistema operativo di produzione.** Supercomputer con AI Employees e 30+ connettori, Canvas a nodi, MCP e CLI, API Cloud, plugin per Photoshop, After Effects, Premiere, DaVinci, Figma e Blender. Il valore vero e' li', non nei singoli modelli.
5. **Le chiamate a freddo automatiche in Italia restano bloccate.** Legge 49/2026 e AI Act articolo 50. Questa parte della revisione 1 regge, e il flusso vocale va costruito sul lead caldo.

---

# PARTE A-ZERO — IL CONTO AL VOLUME REALE (revisione 4)

> Le revisioni 1-3 costavano un video singolo (€2,78) e si fermavano li'. Max ha dato il
> volume vero di produzione. Questo e' il conto che conta; tutto il resto del dossier
> resta valido come mappa del prodotto.

## Il volume, dichiarato da Max il 2026-09-04

| Formato | Cadenza | Al mese | Minuti finiti |
|---|---|---|---|
| **Video YouTube 10 min** | 3-2-3-2 alternata, 2 giorni di stop al mese | **70** | 700 |
| **Corti 1-3 min** | 3 al giorno, 6 una volta a settimana | **102** | 204 |
| **Chiamate agente vocale** | 100 al giorno | **3.000** | 6.000 |

Totale: **172 video e 904 minuti di video finito al mese.**

## CORREZIONE 3 — i corti costavano meta'

Nella revisione 3 avevo costato i corti come dodici clip generative a testa. Sbagliato:
Max li ha descritti **senza avatar e senza soggetto**, eleganti, sottotitoli piccoli al
centro, elementi che si spostano, grafica 3D. Quelli **non sono video generati, sono
progetti Vibe Motion** con qualche sfondo. Da 239 a 109 crediti l'uno, ed e' li' che se ne
andava meta' del conto.

## Higgsfield — tre scenari

| Scenario | Cr/video YT | Cr/corto | Crediti/mese | Pacchetti extra | Totale/mese |
|---|---|---|---|---|---|
| Magro — poche clip, molte immagini; corti di sola grafica | 176 | 45 | 16.890 | €365 | **€635** |
| **Medio** — b-roll vero; corti con 4 sfondi in movimento | 349 | 109 | 35.514 | €1.226 | **€1.496** |
| Ricco — aperture Seedance 2.0; corti con 8 clip | 645 | 175 | 63.006 | €2.498 | **€2.768** |

Base Ultra 9.000 (€270 annuale) piu' pacchetti a €0,046 il credito. Tasso di riprova 2×.
Con riprova 1,3× lo scenario medio scende a **€987**.

## ElevenLabs — e la scoperta che vale $510 al mese

Fabbisogno: **204.000 crediti** di voce (i 102 corti) e **6.000 minuti** di chiamate.

| Piano | Canone | Eccedenza chiamate | Totale | Crediti voce bastano? |
|---|---|---|---|---|
| Creator | $22 | $458 | $480 | No — 121k contro 204k |
| **Pro** | **$99** | **$381** | **$480** | **Si' — 600k, concorrenza 20** |
| Scale | $299 | $181 | $480 | Si', ma margine inutile |
| Business | $990 | $0 | $990 | Si', e costa il doppio per nulla |

**I piani ElevenAgents sono perfettamente lineari a $0,08 al minuto**: salire di livello non
fa risparmiare un centesimo sulle chiamate, cambia solo i crediti voce e la concorrenza.
Si prende il piu' basso che copra i crediti, ed e' **Pro**. Business costerebbe $510 in piu'
al mese per lo stesso servizio.

A parte: telefonia Italia ~$180, modello LLM ~$7.
**Totale ElevenLabs ~$667 al mese ≈ €617.**

Concorrenza: 100 chiamate al giorno su otto ore sono **meno di una chiamata in parallelo**.
I 20 canali di Pro sono venti volte il necessario.

## Il totale

| | Mese | Anno |
|---|---|---|
| Higgsfield, scenario medio | €1.496 | €17.952 |
| ElevenLabs tutto compreso | €617 | €7.404 |
| **TOTALE** | **€2.113** | **€25.356** |
| Con riprova 1,3× | €1.604 | €19.248 |

## Le due incognite che restano

1. **Il costo in crediti del TTS Higgsfield.** La voce dei 70 video lunghi sono 700 minuti al mese e non e' in nessuno dei due conti. Se resta su Higgsfield costa crediti (prezzo non pubblicato); se va su ElevenLabs sono 0,7M crediti in piu' e serve Scale invece di Pro.
2. **Il costo di un progetto Vibe Motion.** Nel calcolatore vale 40 crediti ed e' una stima di terzi. Con 102 corti al mese, sbagliarla di venti crediti sposta €1.100 all'anno.

## Il vincolo vero sulle chiamate

Non e' tecnico ne' di prezzo: **3.000 chiamate al mese richiedono 3.000 contatti con
consenso tracciabile**. In Preventa il consenso nasce dalla risposta su WhatsApp. La domanda
da rispondere prima di attivare l'agente non e' quanto costa, e' se generiamo cento risposte
al giorno da richiamare.

## Calcolatore

`PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py` — i numeri si rifanno, non si
ricordano. Accetta `--yt-mese`, `--corti-mese`, `--chiamate-giorno`, `--riprova`.

---

# PARTE A — MAPPA COMPLETA DI HIGGSFIELD

Ogni voce qui sotto e' una pagina o un modulo verificato sul sito, non una supposizione.

## A.1 I quattro motori di base

| Modulo | Cosa fa |
|---|---|
| **Image** | Oltre 20 modelli: Soul e Soul 2.0, Nano Banana e Nano Banana Pro, Seedream 5.0, FLUX.2 (Pro, Flex, Max), GPT Image 2, Reve, Wan 2.2, Multi Reference |
| **Video** | Oltre 15 modelli: Seedance 2.0 e 2.5, Kling 3.0 e la famiglia Omni, Sora 2 in quattro varianti, Veo 3.1, Wan 3.0 e Prime, Minimax Hailuo 2.3, Higgsfield DoP, Genjutsu |
| **Audio** | Text to Speech, **Voice Change**, **Translate**. Modello Seed Audio 1.0, fino a 3 voci o audio di riferimento, batch fino a 4. Oltre 70 lingue |
| **Edit** | Inpainting con pennello, rimozione oggetti, rimozione testo e loghi, correzione luce, modifica espressioni facciali mantenendo lo sfondo |

## A.2 Gli studi verticali

- **Cinema Studio 4.0** — produzione cinematografica, oltre 70 preset di camera reali (crash zoom, dolly, crane, FPV, bullet time).
- **Marketing Studio** — sei formati: product shots, UGC video, ads, marketplace, poster, motion graphics. Incolli il link del sito o del social e **il prodotto si carica da solo**, con logo, colori e copy estratti dalla pagina. Oltre 100 avatar disponibili, o generi il tuo con Soul 2.0. Modalita': TV Spot, UGC, Tutorial, Product Review, Unboxing, Virtual Try-On, Hyper Motion. **Ogni layer resta modificabile**: i poster si aprono come file di design, titolo, data e immagine sono livelli separati che riscrivi e poi rigeneri con "Recreate".
- **AI Ad Generator** (agente Hermes) — **incolli una URL, scegli un formato, esce un annuncio finito in 2 minuti.**
- **Lipsync Studio / UGC Factory** — carichi immagine o clip, generi o carichi l'audio, scegli il modello (Infinite Talk, Higgsfield Speak, Veo 3, Kling, Wan 2.5 Speak, Sync Lipsync 3 fino a 4K).
- **Fashion Factory** — servizi fotografici brandizzati: il tuo prodotto piu' un personaggio costante.
- **Photodump Studio** — set di foto in stile "scatto reale", anche da mobile.

## A.3 Il lungometraggio — la parte che avevo saltato

**AI Long Video Generator.** Funzioni dichiarate sulla pagina:

| Funzione | Dettaglio |
|---|---|
| Script to Long Video | Da script o brief a video multi-scena finito |
| Multi-Shot Continuity | Personaggi, ambienti e ritmo coerenti su tutta la durata |
| Storyboard Mode | Ogni inquadratura pianificata prima del render |
| Character Lock | Volto e vestiario costanti tra le scene |
| Scene Extension | Estende le scene senza stacchi, transizioni primo/ultimo fotogramma |
| **Reference System** | **Fino a 12 riferimenti per scena** (Nano Banana Pro fino a 8) |
| Per-Shot Camera Control | Lente, inquadratura e movimento decisi scena per scena |
| **Native Audio** | **Dialoghi, effetti sonori e musica generati insieme al video, sincronizzati in un passaggio** |
| Lip Sync e Dubbing | Oltre 74 lingue, un master per tutti i mercati |
| Durata | Clip fino a 15 secondi, sequenziate in **minuti** |
| Upscale | Fino a 4K |
| Export | MP4 in 9:16, 1:1 e 16:9 |

**Higgsfield Popcorn** e' il generatore di storyboard: fino a 8 scene coerenti da un unico flusso,
con riferimento immagine opzionale e prompt per scena.

**Non c'e' un generatore di sottotitoli nativo** (la pagina `/subtitles` e' un 404). I sottotitoli
restano lavoro nostro — cosa che gia' facciamo.

## A.4 Identita' e personaggi

- **Soul 2.0** — fotorealismo editoriale a **0,12 crediti a immagine**, il modello piu' economico dell'intero listino.
- **Soul ID** — definisci un personaggio da una reference e resta identico attraverso luci, angoli e stile. E' il market leader dichiarato sulla consistenza.
- **Character training** — carichi foto da piu' angolazioni e addestri il tuo personaggio, poi lo riusi su immagini e video.
- **AI Influencer Studio** — un personaggio digitale costante per TikTok, Reels e Shorts, senza mai stare davanti a una camera.

## A.4-BIS Vibe Motion — il motion design (la macchina dei corti)

Pagina `/ai-motion-design`. Motore **da testo ad animazione**: non genera pixel, **costruisce
la logica dell'animazione**, e l'uscita e' un **asset strutturato e modificabile**, non un
video piatto. E' esattamente cio' che serve ai 102 corti al mese.

Flusso in cinque passi:
1. Descrivi l'idea in chat, il motore interpreta l'intento.
2. Carichi i tuoi asset — **loghi, SVG, immagini, footage**.
3. Applichi un **Motion Preset** dalla libreria invece di curare l'easing a mano.
4. **Modifichi il codice, non i pixel**, dall'inspector visuale.
5. Render fino a 4K.

Controlli, uno per uno:
- **Colore**: si inseriscono i codici **HEX o RGB esatti** per fondi, tracciati e font. Il nostro `#fb4604` entra alla lettera, non "piu' o meno arancione". E' la prima volta che un tool generativo rispetta le Brand Guidelines alla virgola.
- **Posizione del testo**: elementi trascinabili, e **safe zone delle piattaforme** perche' i sottotitoli non finiscano sotto i bottoni dell'interfaccia. Esattamente i sottotitoli piccoli al centro chiesti da Max.
- **Movimento**: durata, ritardo e **curve di easing** su cursori.
- **Tipografia**: font nostri, crenatura e interlinea, ridimensionamento senza perdita.

Categorie native: **Infografiche, Presentazioni, Kinematic Captions**.

Costo: a generazione, e **le iterazioni bruciano in fretta**. Da fonte terza, ~150 crediti
valgono 3-10 progetti completi, quindi 15-50 crediti l'uno. **E' una stima, non un dato
ufficiale**: nel calcolatore vale 40 ed e' da tarare sul campo.

## A.4-TER Canvas — l'officina (da sapere a memoria, ordine di Max)

- **Come si costruisce**: Canvas → nuova lavagna → nodo Text Prompt → collegalo a un nodo di generazione → scegli il modello → collega l'uscita al passo successivo. Ogni modello Higgsfield e' un nodo, audio compreso.
- **Le reference si comportano in modo diverso, ed e' il dettaglio che fa sbagliare tutti**: i nodi **Seedance** lavorano con le immagini collegate **solo se il prompt dichiara il ruolo** di quell'immagine; i nodi **Kling** trattano l'immagine collegata come **primo fotogramma**, e per usarla come personaggio serve il tag `@nome-elemento`.
- **Crediti**: costruire e collegare i nodi e' **gratis**. Si paga solo quando un nodo genera, alla stessa tariffa che quel modello ha altrove. Quindi **si progetta l'intera pipeline a costo zero**.
- **Parallelo**: piu' modelli affiancati sullo stesso grafo, output confrontabili a fianco. Su Ultra sono 8 job video insieme — e' cosi' che si abbatte il tasso di riprova, scegliendo fra quattro varianti invece di rigenerare quattro volte la stessa.
- **Template**: un intero flusso si salva come template riutilizzabile fra campagne.
- **Squadra**: si condivide con un link, si lavora in contemporanea, ogni versione resta.

## A.5 Editing avanzato

- **Higgsfield Layers** — **trasforma un'immagine piatta in livelli modificabili**: relight, inpaint, decomposizione in livelli, **modifica del testo**, effetti. Ogni elemento torna modificabile dopo la generazione.
- **Genjutsu** — prende un video esistente e ne ricasta il movimento con i tuoi personaggi, luoghi o prodotti, oppure scambia singoli elementi lasciando il resto.
- **Mixed Media** — scene complete da 10 secondi, dichiarate "100 volte piu' veloci del montaggio manuale".
- **Face Swap e Character Swap** — 2 crediti a immagine.

## A.6 Automazione — il livello che vale davvero

**Supercomputer.** Non e' un generatore, e' un agente che gira tutta la piattaforma da una chat:

- **AI Employees** — dipendenti AI specializzati con skill preinstallate: Cartoon Animator (24 skill), Motion Designer (43 skill), Podcast Producer (4 skill), Product Photographer (24 skill). Puoi crearne di tuoi.
- **Orchestrator** — sceglie il modello migliore per il compito, dichiarato piu' economico e piu' veloce.
- **Modelli di ragionamento selezionabili**: Claude Opus 4.6 per campagne complesse, Claude Sonnet 4.6 come default, Gemini 3.1 Pro, Grok 4.3.
- **Oltre 30 connettori**: Slack, Google Drive, Notion. Legge i brief dai documenti e pubblica gli asset finiti nei canali.
- **Workflow ricorrenti programmabili** e progetti multipli in parallelo sui piani alti.
- Mostra il costo in crediti **prima** di eseguire e chiede approvazione.
- Costo indicativo: un flusso a due passaggi circa 90 crediti (circa €3,50 su Plus), una produzione completa circa 200 crediti (circa €8).

**Canvas** — editor a nodi: prompt, immagini e modelli video collegati in una pipeline unica.
Piu' modelli nello stesso grafo, output instradati tra loro, collaborazione dal vivo sullo stesso
canvas via link. I flussi si salvano come **template riutilizzabili tra campagne**.

**MCP e CLI** — server MCP ufficiale, installazione su Claude Code:

```
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Autenticazione OAuth dal browser, nessuna chiave. Da li' genero io, direttamente da qui.
Limiti: immagini fino a 4K, video fino a 15 secondi, **nessun unlimited** e **nessun tetto di
spesa nativo**.

**API Cloud** (cloud.higgsfield.ai) — Bearer token, asincrona con webhook, SDK Python e
TypeScript, modalita' Text-to-Video, Image-to-Video e Soul Mode. **Gli output restano
scaricabili solo 7 giorni**: vanno portati subito in casa.

## A.7 Integrazioni nei programmi che gia' usiamo

Plugin nativi per **Photoshop, After Effects, Premiere Pro, DaVinci Resolve, Figma, Blender**.
Il Supercomputer gira **dentro i plugin**. Installer nativo per Windows e macOS.
Nota per la domanda che hai fatto sui siti: **il plugin Figma** e' la porta d'ingresso per il
lavoro di design, e c'e' un modulo **Games** che costruisce esperienze interattive da un prompt
con **deploy incluso**. Non e' un costruttore di siti, ma sul comparto visivo dei nostri siti
incide eccome.

## A.8 Contorno

Higgsfield Collab (progetti condivisi, chat in contesto, chiamate), Team Plan, Enterprise,
Academy, Originals (serie prodotte in casa), Contests con un **film festival da 1 milione di
dollari** attivo ora, Viral Presets, Assist.

---

# PARTE B — LISTINO E CREDITI

## B.1 Piani (verificati sul sito, in EURO, IVA esclusa)

Promo attiva: **30% sull'annuale**.

| Piano | Mensile | Annuale | Crediti/mese | Costo per credito | Job paralleli |
|---|---|---|---|---|---|
| Free | €0 | — | limitato | — | 1 video / 1 img |
| Starter | €19 | €19 (nessuno sconto) | 270 | €0,070 | 2 video / 4 img |
| **Plus** | €59 | **€47** (risparmi €144/anno) | **1.200** | €0,039 | 6 video / 8 img |
| Ultra | €129 | €99 (risparmi €360/anno) | 3.000 (scalabile 6.000 e 9.000) | €0,033 | 8 video / 8 img |

Crediti extra: circa 20 per dollaro (**$0,05**), quindi **piu' cari dell'abbonamento**; da fonte
terza scadono dopo 90 giorni.
**Starter non accede a Seedance 2.0 e 2.5**: il piano minimo utile e' Plus.

## B.2 Costo per generazione (estratto dal comparatore)

**Video** — Kling 3.0 720p 7 cr/5s · **Kling 3.0 1080p 8 cr/5s** · Kling 3.0 4K 30 cr/5s ·
Kling Omni 3 Image Reference 1080p 7 cr/5s · Seedance 1.5 1080p 7 cr/5s ·
Seedance 2.0 1080p 45 cr/5s · Seedance 2.0 4K 110 cr/5s · Veo 3.1 Fast 1080p 11 cr/4s ·
Veo 3.1 1080p 29 cr/4s · Sora 2 720p 10 cr/4s · Sora 2 Pro 1080p 50 cr/4s ·
Wan 3.0 1080p 27,5 cr/5s · Minimax Hailuo 2.3 1080p 10 cr/6s

**Immagini** — **Soul 2.0 0,12 cr** · Soul 0,25 cr · Reve 0,25 cr · Wan 2.2 0,5 cr ·
Nano Banana / Seedream / GPT Image / FLUX.2 Pro 1 cr · **Nano Banana Pro 2 cr** ·
Nano Banana Pro 4K 4 cr · Multi Reference 1,5 cr · Face/Character Swap 2 cr

**Lipsync** — Kling Speak 720p 2 cr/2s · Wan 2.5 Speak 720p 12 cr/5s ·
Higgsfield Speak 2.0 720p 14 cr/5s · Infinite Talk 720p 12 cr/2s · Sync Lipsync 3 4K 18 cr/2s

**Audio** — **il costo in crediti del Text-to-Speech non e' pubblicato sulla pagina prezzi.**
E' la sola voce che non sono riuscito a verificare da fuori: si legge in-app al primo utilizzo,
ed e' la prima cosa che misuro il giorno 1.

## B.3 Unlimited — come funziona davvero

- Modelli unlimited per piano: Starter 3, Plus 7, Ultra 7 (con i modelli di punta migliori).
- Finestre: la maggior parte 365 giorni, i modelli di punta appena usciti (Kling 3.0, Nano Banana 2, Nano Banana Pro) **7 giorni**.
- Starter **non** ha unlimited su Kling 3.0, Nano Banana 2 e Nano Banana Pro.
- Coda rilassata: 1 immagine, 1 video e 1 audio alla volta, velocita' ridotta nelle ore di punta. I crediti vanno sempre in coda prioritaria.
- **Esiste solo su higgsfield.ai**: niente unlimited su MCP, CLI, Canvas o Supercomputer.
- **I Termini vietano l'automazione sull'unlimited**: possono limitare, sospendere o rallentare l'uso automatizzato. L'unlimited e' per uso personale umano.

**Regola operativa:** unlimited a mano, in sprint. Automazione via MCP e API, a crediti.

---

# PARTE C — CORREZIONE 1: HIGGSFIELD SOSTITUISCE FLIKI

Nella revisione 1 avevo scritto che il tetto di 15 secondi per clip rendeva impraticabile un
video da 10 minuti. Il conto era giusto **solo se il video e' tutto video**. Tu hai detto che un
video si riempie di immagini piu' qualche clip, con voce e sottotitoli. E' esattamente cosi' che
lavora il nostro canale, ed e' esattamente cio' per cui il Long Video Generator e' costruito.

**Il conto vero, per un video YouTube da 10 minuti, su piano Plus:**

| Componente | Quantita' | Modello | Crediti |
|---|---|---|---|
| Clip video di stacco | 8 da 5s | Kling 3.0 1080p | 64 |
| Immagini di riempimento | 60 | Soul 2.0 | 7,2 |
| Voce narrante | 10 minuti | Seed Audio / ElevenLabs v3 | da misurare |
| **Totale visivo** | | | **~71 crediti = €2,78** |

**Con 1.200 crediti al mese fai circa 16 video da 10 minuti**, e ti resta margine. Contro i 21
fallimenti dell'ultimo lotto, non e' un miglioramento: e' un altro mestiere.

**Ma il gate resta da riparare lo stesso.** Nei log ci sono 21 fallimenti identici, e non vengono
da Fliki: vengono da `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/quality_gate.py:93`
(sezioni HOOK, CORPO, CTA mancanti). Lo scrittore produce un formato, il gate ne pretende un
altro. Se migriamo su Higgsfield senza sistemarlo, ci portiamo dietro il blocco.

---

# PARTE D — CORREZIONE 2: I CAROSELLI RESTANO SU ARENA

Ho guardato le slide in `Lancio corso skill beast/Page/caroselli - Agency`. Il metro non e'
un'opinione, e' quello che c'e' dentro: tag pre-headline in pillola con icona, grana su fondo
nero, arancione usato solo come accento sotto il 10%, grotesque bold accoppiato al corsivo serif
per l'enfasi, card argento in gradiente per il blocco soluzione, numerazione 2/8, firma in basso
a destra. **E' un sistema di design coerente tra slide diverse**, allineato alle Brand Guidelines
CCM.

Il mio errore e' stato confrontare sul prezzo quando l'asse vero e' un altro. Nano Banana Pro a
2 crediti genera **la fotografia di una slide**; quello che hai in mano tu e' un layout. E lo hai
ottenuto gratis, con il metodo giusto: prompt lunghi e reference allegate — i nomi dei file lo
dicono, `Max_a_I'm_attaching_refere`.

**Quindi:** i caroselli restano su Arena. Il problema li' non e' la qualita', e' che
l'automazione si rompe — captcha, modale Terms of Use, bottoni che cambiano, sessioni che
scadono. In `caroselli - agency` ci sono oltre 40 script di debug e 60 screenshot che lo
raccontano. **Quello va riparato, non sostituito.**

Una cosa di Higgsfield pero' entra bene anche qui, e non c'entra con il generare da zero:
**Layers**. Prende un'immagine piatta e la scompone in livelli modificabili, testo compreso.
Vuol dire prendere una slide gia' perfetta fatta in Arena e **rigenerarne solo il testo** per le
altre slide, invece di ritirare i dadi su tutto il layout. E' il caso d'uso da provare, e costa
pochi crediti.

---

# PARTE E — ELEVENLABS: COSA RESTA DAVVERO

Scoperta che cambia la valutazione: **il Text-to-Speech di Higgsfield usa ElevenLabs v3 come
modello di default**, insieme a MiniMax, Seed Speech e Vibe Voice. Comprando Higgsfield le voci
ElevenLabs le hai gia' dentro, pagate in crediti Higgsfield.

**Cosa Higgsfield NON copre e ElevenLabs si':**

| Bisogno | Chi lo copre |
|---|---|
| Voce per i video | **Higgsfield** (ElevenLabs v3 incluso) |
| Doppiaggio e traduzione video | **Higgsfield** (74+ lingue, nativo) |
| Clonazione voce base | **Higgsfield** (da campione breve) |
| **Speech-to-speech sulla tua recitazione** | **ElevenLabs** — 1.000 crediti/minuto, modello `eleven_multilingual_sts_v2`, 29 lingue, max 5 minuti per file |
| **Clonazione professionale certificata** | **ElevenLabs** (da piano Creator) |
| **Agente telefonico** | **ElevenLabs** — Higgsfield non ha niente del genere |
| API voce dentro i nostri sistemi | **ElevenLabs** |

## Listino ElevenLabs (verificato, USD, annuale = 2 mesi gratis)

| Piano | Mensile | Crediti/mese | Minuti TTS | Clonazione | Concorrenza |
|---|---|---|---|---|---|
| Free | $0 | 10.000 | ~10 | Instant (2) | 2 |
| Starter | $6 | 30.000 | ~30 | Instant (2) | 3 |
| **Creator** | **$22** (1° mese $11) | **121.000** | ~121 | **Professional (1)** | 5 |
| Pro | $99 | 600.000 | ~600 | Professional (1) | 10 |
| Scale | $299 | 1.800.000 | ~1.800 | Professional (3) | 15 |
| Business | $990 | 6.000.000 | ~6.000 | Professional (10) | 25 |

Consumi: TTS 1 credito per carattere (circa 1.000 caratteri al minuto) · **Voice Changer 1.000
crediti/minuto** · Speech to Text 330/min · Musica 900/min · Effetti 200 a generazione ·
Doppiaggio 2.000-10.000/min. La licenza commerciale parte da Starter.

## ElevenAgents (chiamate)

| Piano | Minuti inclusi | Concorrenti | Minuto extra |
|---|---|---|---|
| Free | 15 | 4 | $0,080 |
| Starter $6 | 75 | 6 | $0,080 |
| **Creator $22** | **275** | **10** | $0,080 |
| Pro $99 | 1.238 | 20 | $0,080 |
| Scale $299 | 3.738 | 30 | $0,080 |

LLM e telefonia a parte, a costo. Chiamata da 2 minuti: circa **€0,21** tutto compreso.
500 chiamate al mese richiedono Pro: circa **€120 al mese**, cioe' €0,24 a chiamata, contro
circa €2.000 di un teleoperatore.

**Startup Grant ElevenLabs:** 12 mesi gratis piu' 33 milioni di caratteri per startup che
integrano gli agenti conversazionali in un prodotto. Digital Empire e' candidabile.

---

# PARTE F — IL VINCOLO LEGALE SULLE CHIAMATE (invariato)

1. **Legge 49/2026, in vigore dal 19 giugno 2026** — modifica l'articolo 51 del Codice del Consumo, **opt-in obbligatorio**: chiamata commerciale solo con consenso preventivo, esplicito e tracciabile. Nasce sul settore energia, le fonti divergono sulla trasversalita': **va verificato con un legale prima di costruire**.
2. **Registro Pubblico delle Opposizioni** — copre anche le utenze aziendali, e vale sia per l'operatore umano sia per le chiamate automatiche.
3. Il **68% dei numeri "aziendali"** nelle liste e' intestato a persone fisiche: GDPR pieno.
4. **AI Act articolo 50, operativo dal 2 agosto 2026** — obbligo di dichiarare, **dentro la conversazione e al primo contatto**, che si sta parlando con un'AI e per conto di chi. La privacy policy non basta.
5. **Sanzioni fino a €20 milioni o il 4% del fatturato**, responsabilita' **in solido** tra mandante e contact center.

**Il flusso che si puo' fare, ed e' migliore:** in Preventa la catena di consenso esiste gia'
(WhatsApp, il concessionario risponde). L'agente entra li': richiamo del lead caldo entro 5
minuti, qualifica in entrata, conferma appuntamenti, riattivazione dormienti, post-vendita.
Con dichiarazione AI nei primi 3 secondi e opt-out immediato, e' in regola — e converte piu' del
freddo.

---

# PARTE F-BIS — IL MESE DI PROVA (decisione di Max, 2026-09-05)

> Max: *"faremo un acquisto di prova solamente per un mese, un acquisto minimo indispensabile
> per poter fare tutte le prove possibili — però considera che le prime prove saranno scarti
> perche' sbaglieremo qualcosa."*
>
> Questa parte viene **prima** di tutto il resto del piano. Nessun impegno annuale finche' le
> prove non hanno risposto.

## La regola che rende valida la prova

**MENSILE, mai annuale.** L'annuale sconta il 30% ma blocca dodici mesi: su un mese di prova
annullerebbe il senso stesso della prova. **Si perde lo sconto, e va bene: e' il prezzo
dell'opzione di dire di no.** Promozioni come quella vengono rimesse ogni due mesi.

Seconda regola: **i crediti dell'abbonamento non si riportano al mese dopo**. Quello che non
si spende entro il mese e' perso, quindi le prove vanno fatte tutte, non "quando c'e' tempo".

## Cosa comprare per la prova

| Tool | Piano | Prezzo | Cosa sblocca |
|---|---|---|---|
| **Higgsfield** | **Ultra 3.000, MENSILE** | **€129** | Tutti i modelli, 8 job paralleli, Supercomputer, Canvas, Vibe Motion, e i **7 giorni di Kling 3.0 e Nano Banana Pro unlimited** |
| **ElevenLabs** | **Creator, MENSILE** | **$11** (primo mese al 50%) | Professional Voice Cloning, licenza commerciale, 121.000 crediti (~121 min), **275 minuti di chiamate** |

**Totale del mese di prova: circa €139.**

### Perche' Ultra e non Plus, sulla prova
Plus mensile costa €59 e da' 1.200 crediti. Le prove ne chiedono ~2.640, quindi servirebbero
1.440 crediti a pacchetto: €66. Totale **€125** — praticamente identico a Ultra (**€129**), ma
con 6 job paralleli invece di 8, senza Nano Banana Pro unlimited e senza un solo credito di
margine per gli scarti. **A parita' di spesa si prende quello che non finisce a meta' prova.**

## Il bilancio della prova, con lo scarto dentro

Tasso di scarto **3×** sulle prime prove (contro 2× a regime): la prima volta si sbaglia il
prompt, la reference, il formato. E' messo nel conto, non sperato via.

| # | Prova | Composizione | Crediti |
|---|---|---|---|
| 1 | **Video YouTube** — prima un segmento da 2 min provato 3 volte per trovare la formula, poi un video intero da 10 min | 3 × (4 clip Kling ×3 + 25 img Soul) + 1 × (20 clip ×2 + 120 img) | **664** |
| 2 | **Corti Vibe Motion** — 3 corti diversi, 3 iterazioni ciascuno, sfondi condivisi | 9 progetti Vibe Motion + 8 clip ×3 | **552** |
| 3 | **Misura del TTS Higgsfield** — 5 campioni di lunghezza nota (30s, 1, 2, 5, 10 min) per ricavare la tariffa | incognita, budget | **150** |
| 4 | **Canvas** — costruzione gratis, 3 esecuzioni del template YouTube | 3 × 110 | **330** |
| 5 | **Layers su una slide Arena** — 10 tentativi di rigenerazione del solo testo | incognita, budget | **80** |
| 6 | **Avatar UGC** — 300 volti Soul 2.0, training del personaggio, 1 video da 30s | 36 + 120 + 6 lipsync ×3 | **372** |
| 7 | **Promo prodotto 30s** — Manuale Claude Code | 6 clip Kling ×3 | **144** |
| 8 | **Confronto modelli premium** sulla stessa scena | Seedance 2.0 ×2, Veo 3.1 ×2, Sora 2 Pro ×2 | **248** |
| 9 | **MCP da Claude Code** — 10 generazioni miste guidate da me | | **100** |
| | **Somma** | | **2.640** |
| | **Margine imprevisti 25%** | | **660** |
| | **TOTALE** | | **~3.300** |

**Ultra da' 3.000 crediti, quindi si e' 300 sotto — ma solo sulla carta:** i 7 giorni di
**Kling 3.0 unlimited** coprono a mano tutte le clip Kling delle prove 1, 2, 7 e in parte 4,
che valgono circa **900 crediti**. Facendo quelle nella finestra unlimited, i 3.000 bastano con
margine reale. **La finestra unlimited va usata per prima, non per ultima.**

## Le nove risposte che la prova deve portare a casa

| Prova | La domanda | Come si decide |
|---|---|---|
| 1 | Il Long Video Generator batte quello che usciva da Fliki? | Confronto diretto con un video gia' pubblicato, a parita' di script |
| 2 | Vibe Motion regge il livello di editing che hai in testa? | Sottotitoli al centro, elementi in movimento, `#fb4604` esatto — pubblicabile o no |
| 3 | **Quanto costa un minuto di TTS in crediti?** | E' l'incognita che decide se i 700 minuti dei video lunghi restano su Higgsfield o vanno su ElevenLabs, cioe' Pro contro Scale |
| 4 | Il costo scende alla seconda e terza esecuzione di un template? | Se non scende, l'architettura a template non paga e va ripensata |
| 5 | Layers tiene il layout rigenerando solo il testo? | Se si', i caroselli Arena diventano riusabili |
| 6 | L'avatar e' indistinguibile? | Se non lo e', il formato UGC si accantona e basta |
| 7 | Il promo e' pubblicabile senza scuse? | Metro binario |
| 8 | Quale modello premium vale il suo prezzo? | Seedance 2.0 costa 5,6 volte Kling 3.0: deve valerlo |
| 9 | L'MCP regge un flusso vero da qui? | Se si', l'automazione parte; se no, resta lavoro a mano |

**Il numero 3 e' il piu' importante.** Senza quello nessun conto di questo dossier e' chiuso.

## Regole di condotta durante la prova

1. **Tetto di spesa scritto nel codice:** nessuna generazione sopra 50 crediti senza via libera esplicito di Max. L'MCP non ha un tetto nativo.
2. **Registro delle prove**: ogni generazione annotata con modello, crediti spesi, esito. Senza registro il mese di prova non produce numeri, produce impressioni.
3. **La finestra unlimited per prima**, a mano, mai con script (i Termini lo vietano).
4. **Disdetta prima del rinnovo** se due prove su tre falliscono. La data del rinnovo va segnata sul calendario il giorno stesso dell'acquisto.
5. **Le prove 3 e 5 sono misure, non giudizi**: vanno fatte anche se l'esito estetico e' brutto, perche' servono i numeri.

## Cosa NON si compra nel mese di prova
- Nessun impegno annuale, su nessuno dei due.
- Nessun piano Team o Scale di Higgsfield.
- Nessun pacchetto di crediti extra prima di aver esaurito i 3.000 e la finestra unlimited.
- ElevenLabs Pro o Scale: Creator basta per provare, e i 275 minuti di chiamata coprono il test dell'agente su venti lead molte volte.

---

# PARTE G — COSA COMPRARE (a regime, dopo la prova)

## Mese di taratura (il primo)

| Tool | Piano | Prezzo | Perche' questo |
|---|---|---|---|
| **Higgsfield** | **Ultra 3.000** | €99/mese annuale | Non si parte dal tetto: il primo mese serve a MISURARE le due incognite, non a produrre a regime |
| **ElevenLabs** | **Pro** | $99/mese + eccedenza | I piani chiamate sono lineari a $0,08/min: Pro basta e Business costerebbe $510 in piu' per nulla |

## A regime, scenario medio

| Tool | Piano | Costo/mese |
|---|---|---|
| Higgsfield | Ultra 9.000 (€270) + ~26.500 crediti a pacchetto | €1.496 |
| ElevenLabs | Pro + eccedenza + telefonia + LLM | €617 |
| **Totale** | | **€2.113** (€25.356/anno) |

Con il tasso di riprova portato a 1,3×: **€1.604 al mese**, cioe' €19.248 l'anno.
**Seimila euro all'anno stanno nella qualita' dei nostri prompt**, non nel piano scelto.

## Cosa NON comprare
- **Higgsfield Team o Scale**: sono i crediti **piu' cari** del listino (€0,065 e €0,060) perche' il prezzo e' per posto con minimo cinque. Comprano posti, coda prioritaria, controllo di spesa, SSO e manleva — non crediti convenienti.
- **ElevenLabs Business ($990)**: $510 al mese in piu' per lo stesso identico servizio.
- **ElevenLabs Scale ($299)**: stesso totale di Pro, ma margine di crediti che non useremo — a meno che la voce dei video lunghi non finisca su ElevenLabs (incognita 1).
- **Higgsfield Starter e Plus**: sotto il fabbisogno di un fattore dieci.

## Le tre mosse a costo zero, prima di pagare
1. **Startup Grant ElevenLabs** — 33 milioni di caratteri contro un consumo di 204.000 al mese: vale oltre dieci anni di voce dei corti. Mezz'ora di lavoro.
2. **Trattativa Enterprise Higgsfield** — a 35.000 crediti al mese siamo un conto da commerciale: sconti a volume per modello e soprattutto **crediti che si riportano al mese dopo**, che con una cadenza 3-2-3-2 e due giorni di stop conta davvero. Richiede settimane, va aperta ora.
3. **Riparare `quality_gate.py:93`** — a tre video al giorno quel gate ferma settanta produzioni al mese.

---

# PARTE H — IL PIANO

## Fase 0 — A costo zero, oggi
- [ ] Riparare `quality_gate.py:93`: 21 fallimenti aspettano questo, non un abbonamento.
- [ ] Candidatura Startup Grant ElevenLabs.
- [ ] Scrivere i 3 test di accettazione, pronti a partire il minuto dopo l'acquisto.

## Fase 1 — Acquisto e collegamento (giorno 1)
- [ ] Higgsfield Plus, ElevenLabs Creator.
- [ ] `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`
- [ ] **Misurare il costo in crediti del Text-to-Speech**: e' l'unico numero che non ho potuto verificare da fuori.
- [ ] Chiave ElevenLabs in `.env`, mai nel repository.
- [ ] Tetto di spesa nel codice: mai sopra 50 crediti senza via libera di Max.

## Fase 2 — Le quattro prove dei 30 giorni
1. **Video YouTube completo** con Long Video Generator, modello misto immagini piu' clip, voce inclusa. Metro: batte quello che usciva da Fliki?
2. **Promo prodotto da 30 secondi** per il Manuale Claude Code, Kling 3.0 1080p. Metro: pubblicabile senza scuse?
3. **Layers su una slide Arena**: rigenerare solo il testo tenendo il layout. Metro: il layout sopravvive?
4. **Voce**: uno script inciso da te, ripassato in Speech-to-Speech ElevenLabs contro il TTS Higgsfield. Metro: quale delle due usiamo davvero?

## Fase 3 — Sprint unlimited (giorni 1-7 di ogni mese)
Kling 3.0 e Nano Banana 2 unlimited, **a mano, mai con script**. Si produce il girato del mese
a costo zero e i 1.200 crediti restano per i modelli premium.

## Fase 4 — Costruzione (settimane 2-6)
- [ ] Skill `video-youtube-higgsfield`: script, storyboard, Long Video Generator, voce, sottotitoli nostri, VIDEO-PRONTI.
- [ ] Template Canvas "Promo Digital Empire" e Soul ID del personaggio di brand.
- [ ] Supercomputer collegato a Google Drive e Notion, con workflow ricorrenti.
- [ ] **Riparazione del ramo Arena** per i caroselli: e' li' che si vince, non su Nano Banana Pro.
- [ ] Valutare il plugin Figma sul comparto visivo dei siti.

## Fase 5 — Agente vocale (settimane 4-8)
- [ ] **Parere legale prima di tutto** su Legge 49/2026 e perimetro B2B.
- [ ] Agente "richiamo lead caldo" su Preventa, dichiarazione AI nei primi 3 secondi, opt-out immediato, registro consensi tracciabile.
- [ ] Test su 20 lead, poi si decide.

---

## Connessioni
- [[Tool_Higgsfield_ElevenLabs]]
- [[Digital_Empire_YouTube_Automation_Factory]]
- [[Preventa_Outreach_Automation]]
- [[Concept_CCM_Brand_Guidelines]]
- `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md`
- `PIANO-MAESTRO/21-ARENA-PROMPTS-MASTER-PACK.md`

## Metodo e fonti
60 pagine di higgsfield.ai lette con Playwright sul DOM renderizzato il 2026-09-04 (le pagine
sono SPA: il fetch semplice le vede vuote e restituisce dati di terze parti, spesso sbagliati),
piu' docs.higgsfield.ai, l'help center, i Termini d'uso, elevenlabs.io/pricing,
elevenlabs.io/pricing/agents e la documentazione Voice Changer.
Normativa: Garante Privacy, Legge 49/2026, AI Act articolo 50 con le linee guida della
Commissione Europea operative dal 2026-08-02.
Numeri non verificabili dall'esterno e dichiarati tali: costo in crediti del Text-to-Speech
Higgsfield, quota crediti del piano Free.
