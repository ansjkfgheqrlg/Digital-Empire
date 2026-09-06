# Reference — Linee Guida Monetizzazione YouTube & Reused Content

> Conoscenza on-demand per `video-producer`, `script-writer`, `niche-scout`. 
> Obiettivo: Prevenire il rifiuto della monetizzazione da parte del Programma Partner di YouTube (YPP).

---

## 1. Il Rischio: "Contenuti Ripetitivi" e "Contenuti Riutilizzati"
I canali facenti uso di YouTube Automation corrono spesso il rischio di essere demonetizzati o non ammessi al programma YPP con due causali principali:
1. **Reused Content (Contenuti Riutilizzati):** Pubblicare video che riutilizzano materiale altrui senza aggiungervi commento originale, valore educativo significativo o un editing trasformativo profondo.
2. **Repetitive Content (Contenuti Ripetitivi):** Contenuti che sono così simili tra loro che gli spettatori faticano a distinguerli (es. stessi modelli video AI, stock video usati nello stesso ordine, voci sintetiche identiche prive di espressività).

---

## 2. Invarianti di Conformità (Come essere ammessi alla monetizzazione)

Per certificare la conformità del video, applica rigorosamente le seguenti regole in fase di sceneggiatura e produzione:

### A. Sceneggiatura Trasformativa (Per lo `script-writer`)
* **Commento Critico Originale:** Lo script non deve essere una traduzione letterale o un riassunto pigro. Deve includere tesi, analisi, commenti originali e riorganizzare le informazioni con un proprio "punto di vista" (segnalato con il marcatore `➕` per tracciare le espansioni originali).
* **Struttura Narrativa Fluida:** Evitare pattern di testo prefabbricati o introduzioni ripetitive uguali su tutti i video del canale.

### B. Produzione Premium (Per il `video-producer` e `qa-audio-video`)
* **Uso Moderato di Stock Footage:** Non affidarsi esclusivamente a clip di archivio predefinite inserite in modo sequenziale. Sovrapponi elementi grafici, grafici animati, screenshot, estratti di notizie e zoom/pan continui per rendere il montaggio dinamico.
* **Voce Narrante di Alta Qualità:** Scegli le voci più umane ed espressive disponibili su Fliki. Evita voci piatte e metalliche (inserisci pause e modulazioni, vedi [fliki-avanzato.md](fliki-avanzato.md)).
* **Cura Estetica dei Sottotitoli:** Non usare sottotitoli standard noiosi. Devono essere dinamici, colorati ed evidenziare le parole chiave principali.
* **Editing Audio Stratificato:** Usa effetti sonori (SFX) per sottolineare i passaggi chiave e le transizioni. La musica non deve essere una singola traccia ripetuta all'infinito senza pause.

---

## 3. Checklist di Conformità per la Fabbrica
- [ ] Il video aggiunge commento critico o valore educativo rispetto alla fonte originale?
- [ ] Il montaggio include zoom, transizioni curate, SFX e overlay grafici (non solo stock video passivi)?
- [ ] La voce narrante selezionata è tra quelle certificate ad alta espressività e non presente nella blacklist di `learned_rules.json`?
- [ ] Il video si distingue nettamente dagli altri video pubblicati sul canale per stile visivo o focus argomentativo?
- [ ] **Nessun fotogramma proviene dal video sorgente** (§4)?

---

## 4. Il «metodo copia e incolla»: perché è una porta chiusa (A4-L06-02 · 2026-09-05)

Esiste un metodo diffuso — insegnato per intero nel corso AI TUBE PRO (A4/L06) — che consiste nel
**scaricare il video altrui e ripubblicarlo modificato**: si rimuove la traccia audio, si traduce
lo script, si rifà il voiceover, si cambia la musica, **si toglie il logo e si rifanno i testi a
schermo**, si riordinano le clip e se ne sostituiscono alcune con materiale da Envato o Pexels.
La difesa dichiarata è: «così **non incorriamo in strike**».

**La nostra fabbrica non lo fa, e non è una questione di gusto.** Tre ragioni, in ordine di peso:

1. **Quella difesa è contro la macchina, non contro il diritto.** Cambiare audio, ordine e grafica
   serve a non farsi riconoscere dal **Content ID**, che è un sistema di identificazione
   automatica: identifica, non stabilisce chi ha ragione. Un titolare può agire anche su un'opera
   modificata. **Non essere riconosciuti** ed **essere in regola** sono due cose diverse, e il
   metodo le confonde per tutta la lezione.
2. **Il «fair use» viene citato come se fosse una regola di YouTube.** Non lo è: è una dottrina
   del diritto **statunitense**, valutata da un giudice su quattro fattori, caso per caso.
   L'ordinamento italiano non ha un equivalente altrettanto largo. Costruire un modello di
   business su un istituto straniero frainteso è il rischio più grosso dell'intero metodo.
3. **È lavoro manuale, e cancella l'automazione.** Togliere un logo, rifare ogni testo a schermo,
   riordinare le clip e sostituirne alcune sono operazioni da editor video, **una per una, su ogni
   video**. La nostra catena genera via API senza aprire un browser: quel passaggio non solo non
   conviene, **non è eseguibile**.

   **Il costo vero, detto dal corso stesso (A4-L14-05 · 2026-09-06).** La lezione madre A4/L05
   promette un video in **~5 minuti**. Sette lezioni dopo, A4/L14 mostra il metodo dal vivo e
   dichiara: **5-10 minuti per il primo minuto di video, e circa 1 ora a video intero**, *dopo*
   che si è fatta pratica [L14 · 25:23]. È un fattore **12×** fra la promessa e la misura, e le due
   cifre stanno **nello stesso corso**. Chi valuta il metodo sui 5 minuti sta valutando un numero
   che la scuola che lo insegna smentisce da sola. Arbitrato completo:
   `company/Memory/studi/aitubepro/CONFLITTI.md` **C-006**.

**Cosa si prende invece, e non è poco:** l'**idea validata**. Che un format abbia funzionato — in
italiano o in un'altra lingua — è il segnale più economico che esista, e va usato (vedi
`video-analyst.md` §8, col caso misurato Lama Facha / Famiglia Sfortunata). **Si replica l'idea e
la struttura; il materiale visivo si genera o si prende alla fonte.**

**Un limite nostro, dichiarato:** i regolatori vigilano sulla copiatura **solo del testo**
(`regolatori.py`, `N_GRAM = 8`). Sul lato visivo non esiste alcun controllo — semplicemente perché
non riusiamo mai materiale altrui. **È una proprietà del flusso, non un presidio:** se qualcuno
introducesse clip scaricate, nessun regolatore se ne accorgerebbe. Annotato in `BACKLOG.md`.

Arbitrato completo: `company/Memory/studi/aitubepro/CONFLITTI.md` **C-004**.

---

## 5. I sei miti del camuffamento (A4-L06/L07/L08/L10/L14 · aggiornata 2026-09-06)

Studiando le lezioni di AI TUBE PRO sono emerse **sei affermazioni diverse** su come rendere
«proprio» un video altrui. Sono tutte false, e sbagliano **nello stesso punto**: confondono **il non
farsi riconoscere da una macchina** con **l'essere in regola**.

> **Aggiornata il 2026-09-06:** i miti erano quattro, sono diventati **sei**. I due nuovi vengono
> entrambi da **A4/L14**, e sono i più istruttivi dei sei perché mostrano che il ragionamento non
> è nemmeno stabile: la soglia magica cambia numero da una lezione all'altra, e il fair use viene
> invocato e poi dichiarato decaduto **nella stessa lezione**, sempre a favore di chi copia.

Le raccolgo qui perché sono esattamente il tipo di frase che circola, suona tecnica, e viene
ripetuta come acquisita da chi non l'ha mai verificata.

| # | Il mito | Dove | Perché è falso |
|---|---|---|---|
| 1 | «Su YouTube esiste il **fair use**, e ci permette di utilizzare video di altre persone» | L06 · 10:36 | Il *fair use* non è una regola di YouTube: è una dottrina del diritto **statunitense**, valutata **da un giudice** su quattro fattori, caso per caso. L'ordinamento italiano non ha un equivalente altrettanto largo |
| 2 | Filtri, overlay ed effetti rendono il video «**originale e non più riconoscibile**» | L07 · 24:57 e 33:04 | «Non riconoscibile» riguarda l'algoritmo di *matching*. L'opera resta l'opera di un altro: l'irriconoscibilità non crea la titolarità |
| 3 | Si possono usare clip protette «magari di un film, magari di *Narcos*, **che dura non meno di 5 secondi**» | L10 · 09:02 | **Nessuna soglia di durata** rende lecito l'uso di materiale protetto — né 5, né 7, né 30 secondi. La porzione usata è **uno** dei fattori del fair use, non una franchigia. Il Content ID riconosce anche frammenti brevi |
| 4 | Coprire il logo con un rettangolo, ritagliare, zoomare e tradurre il testo «**serve a evitare problemi di copyright**» | L08 · 39:56, 40:37, 48:49 | Il diritto d'autore protegge **il contenuto audiovisivo**, non il logo che ci sta sopra. Coprire il marchio nasconde la provenienza, non trasferisce i diritti |
| 5 | «**Sono 4 secondi di video** che non possono dire nulla perché siamo dentro il fair use, quindi andate super tranquilli» | L14 · 20:51 | **La stessa soglia inesistente del mito 3, con un numero diverso.** L10 diceva 5 secondi, L14 dice 4: due lezioni dello stesso corso danno due franchigie diverse per una franchigia che non esiste. Il fatto che il numero cambi è la prova che nessuno dei due l'ha letto da qualche parte |
| 6 | «Il canale che usa quella clip non è che l'ha creata lui, quindi **il fair use decade**: non possono mai dire con certezza che noi abbiamo copiato» | L14 · 19:50 | **Il più contorto dei sei.** Confonde due domande diverse: *chi può agire* (il titolare del diritto, che resta chi ha creato l'opera, non chi la sta riusando) e *se l'uso sia lecito*. E poi trasforma una **difficoltà di prova** in una **licenza**: «non possono dimostrarlo» non ha mai voluto dire «si può fare» |

**La regola di casa, in una riga:** *se una tecnica serve a non farsi riconoscere, quella tecnica
sta ammettendo che c'è qualcosa da riconoscere.*

**Come si comporta la nostra fabbrica:** non riusa materiale di terzi, quindi nessuno di questi
sei problemi la riguarda. Questa sezione **non serve a difenderci** — serve a **non farci
importare quei miti** da un corso, da un video o da un collaboratore che li dà per buoni. Se
qualcuno propone una di queste sei cose, la risposta è già scritta qui.

---

## 6. Il catalogo delle manovre di camuffamento (A4-L09-01 · 2026-09-06)

I sei miti del §5 sono le **frasi**. Questa è la lista delle **manovre** che quelle frasi
giustificano — dodici, tutte da una sola lezione (A4/L09, «18 Tecniche Avanzate del Metodo Copia
e Incolla»), tutte applicate a una clip scaricata da un video altrui.

Serve per riconoscerle quando arrivano: raramente vengono proposte col loro nome.

| manovra | minuto | a cosa serve davvero |
|---|---|---|
| zoom, ridimensionamento, spostamento, pan+zoom animato | 04:38 – 06:29 | tagliare fuori i dettagli che identificano la fonte |
| color grading, LUT, bianco e nero, virata di tinta | 06:35 – 07:24 | alterare la firma cromatica |
| **flip orizzontale / effetto specchio** | 09:10 – 09:41 | **elusione pura**: nessuna funzione estetica |
| **effetti di distorsione / specularità** | 09:53 – 10:17 | **elusione pura** |
| green screen e chroma key per sostituire lo sfondo | 10:58 – 14:35 | cambiare il contesto della scena |
| overlay di testo (MOGRT) e footage ad alpha channel | 15:34 – 17:57 | coprire, distrarre, «rompere la monotonia» |

**Le due in grassetto sono il caso limite, ed è per questo che questa sezione esiste.** Capovolgere
un'immagine o distorcerla **non migliora il video di un fotogramma**: l'unica cosa che cambia è che
un sistema di *matching* fa più fatica a riconoscerla. Una manovra che non ha nessuno scopo se non
quello di **non farsi riconoscere** dichiara, da sola, che c'è qualcosa da riconoscere.

**Regola di casa:** nessuna di queste manovre entra in fabbrica, e nessuna serve — perché la
fabbrica non parte mai da materiale altrui. Se una di esse viene proposta «per sicurezza», la
domanda giusta non è «funziona?» ma **«cosa stiamo cercando di nascondere?»**.

---

## 7. Porta chiusa: la separazione audio di brani altrui (A4-L16-01 · 2026-09-06)

Il corso (A4/L16) propone una nicchia «canali di musica» costruita così: **link YouTube → sito
terzo di download audio → mp3 → AI di *source separation* (lalal.ai) → voce e base separate**, da
ripubblicare. La presenta come «uno dei settori che funziona di più su YouTube se si fa bene,
evitando tutti i problemi di copyright» [03:20], **e poi non spiega alcun meccanismo per evitarli**.

**Non entra in fabbrica.** Due passaggi distinti, entrambi problematici:

1. **Scaricare l'audio da YouTube tramite siti terzi** viola i Termini di servizio della
   piattaforma su cui pubblichiamo. È già sufficiente da solo.
2. **Separare voce e strumentale da una registrazione altrui e riusarle** è **elaborazione non
   autorizzata**: tocca sia il **diritto d'autore sulla composizione** sia i **diritti connessi
   sulla registrazione**. La separazione non crea un'opera nuova — **isola pezzi di quella
   esistente**, e li isola meglio di prima.

**L'argomento portato a sostegno è un canale da 544 video e quasi 1 milione di iscritti** [03:55].
Non prova nulla: è **survivorship bias**. Un canale che non ha *ancora* subito conseguenze non
dimostra che la pratica sia lecita, e non si contano quelli spariti facendo la stessa cosa. Il
principio in forma generale sta in `03-AGENTI-E-RUOLI/operatori/niche-scout.md` §9 (`A4-L16-02`).

**Lo strumento non è il problema: il materiale in ingresso lo è.** La *source separation* resta
legittima e utile su **audio nostro** — una traccia registrata male, una voce coperta dalla musica
[L16 · 06:18]. La linea è semplice e vale per qualunque strumento del genere: **si separa ciò di
cui si hanno i diritti.**

---

## 8. Il volto e la voce: due porte chiuse sul generativo (A4-L15-01/02 · 2026-09-06)

Le sezioni precedenti riguardano il **materiale altrui riusato**. Questa riguarda il **materiale
generato**, ed è lo stesso errore spostato di un passo: là si credeva che modificare un video di
altri creasse un diritto, qui si crede che **generarlo** lo crei. **Generare non è acquisire un
titolo.**

Le due manovre vengono dalla stessa lezione (A4/L15, tutorial di uno strumento di avatar parlanti),
mostrate come normali esercizi tecnici, **senza una sola parola di avvertimento**.

### 8.1 Il volto e la voce di una **persona reale** — mai

Nella lezione, un avatar legge una **finta notizia di lutto** su un cantante italiano **realmente
esistente** [11:36-11:48], e il commento è: «abbiamo dato anche un volto all'intelligenza
artificiale». Niente sul consenso, niente sul diritto all'immagine, niente sul fatto che quella
sia **una notizia falsa** con voce e faccia di una persona viva.

**Regola di casa:** la fabbrica non genera **volto, voce o sembianze riconoscibili di una persona
reale** — nota o sconosciuta, viva o morta — e non le mette in bocca dichiarazioni che non ha
fatto. Non è una questione di diritto d'autore: è **diritto all'immagine e identità personale**, e
non si estingue perché l'immagine è sintetica. Una notizia falsa attribuita a una persona vera è
il caso peggiore, non un caso limite.

L'unica eccezione possibile è **il consenso scritto della persona** — che per una fabbrica che
pubblica automaticamente vuol dire, in pratica: **mai**.

### 8.2 I **personaggi protetti** generati dall'AI restano di chi sono

Nella stessa lezione si genera un ritratto con prompt «qualcosa che ha a che fare con **Dragon
Ball**… e **Goku**» e lo si fa parlare [09:08 → 10:52]. Dragon Ball è di **Toei Animation / Bird
Studio**. Nessuna parola sul diritto d'autore.

**Regola di casa:** che l'immagine esca da un modello generativo **non cambia di chi è il
personaggio**. Un modello addestrato su opere protette può restituirne di riconoscibili: la
riconoscibilità è il problema, non lo strumento. Non generiamo, non pubblichiamo e non mettiamo in
miniatura personaggi, mascotte, loghi o stili identificabili di terzi.

**Il metro pratico, in una riga:** *se un umano guardando l'immagine sa dire di chi è il personaggio
o chi è la persona, allora quel diritto è di qualcun altro — e l'ha generato una macchina non
cambia una virgola.*

---

## 9. Da dove può venire la musica dei nostri video (A4-L17-01/02 · 2026-09-06)

**Domanda ancora aperta, e va detto per prima:** non sappiamo se i video che produciamo abbiano una
musica di sottofondo. La verifica è assegnata al gate della categoria A4 (`A4-L04-04`), e finché
non è fatta, il criterio «Bilanciamento Volumi» di `qa-audio-video` resta sospeso.

Quando la domanda avrà una risposta, le vie sono **tre**, e **una è chiusa**.

| via | stato | perché |
|---|---|---|
| **1. La musica che Fliki ci fornisce** | ✅ **è quella che abbiamo già in casa** | coperta dalla licenza della piattaforma; è esattamente ciò che il campo `YouTube channel ID(s)` del profilo Fliki serve a difendere in caso di reclamo (§ `fliki-produzione.md`, `A4-L19-01`) |
| **2. Musica generata da uno strumento AI** | ⚠️ **percorribile, ma a condizioni** | vedi sotto |
| **3. Voce e base separate da brani altrui** | ❌ **porta chiusa** | §7: elaborazione non autorizzata di una registrazione esistente |

### La via 2, e le sue due condizioni

A4/L17 mostra **AIVA**, generatore di musica da AI, e ha il merito di dire una cosa che quasi
nessuno dice: **i diritti sulla musica generata dipendono dal piano che paghi.** Parole della
lezione:

- piano **gratuito**: «ci permette di creare la musica **così per gioco**… perché **non abbiamo i
  diritti**» [08:50]
- piano **Standard**: «diritti di monetizzare, ma **solamente su YouTube, Twitch, TikTok e
  Instagram**», e «non possiamo rivendere all'esterno» [08:57, 09:49]
- piano **Pro**: «siamo noi i proprietari» [09:16]

**Condizione 1 — il titolo si verifica sui termini del fornitore, mai su una lezione.** La stessa
lezione, in apertura, aveva promesso che «saremo noi i proprietari» e che si può monetizzare
«anche su piattaforme esterne» [00:46-01:03] — cosa vera **solo per il piano più alto**, come lei
stessa spiega otto minuti dopo. Se una promessa e la sua smentita stanno nello stesso video, la
fonte non è il posto dove si legge una licenza: si legge sul contratto del fornitore, prima di
pubblicare (arbitrato `CONFLITTI.md` **C-007**).

**Condizione 2 — nessun brano altrui come riferimento di stile.** Nella dimostrazione, il docente
carica nella sezione `Influencers` «una canzone abbastanza conosciuta e abbastanza famosa» per
farsi generare qualcosa di simile [11:03-11:23], **senza una parola** sul fatto che la licenza lo
copra o meno, né sul rischio che il risultato somigli troppo all'originale. **È lo stesso schema
del §7:** lo strumento è pulito, **il materiale in ingresso no**. Da noi si genera **da zero**:
genere, umore, durata. Nessun file di riferimento che non sia nostro.

**E una cosa che la licenza non copre, da tenere separata.** In tutta la lezione **Content ID non
è mai nominato**. Un contratto col fornitore dice cosa hai il diritto di fare; **non impedisce a
un sistema automatico di segnalarti**. Sono due piani distinti, e servono entrambi: il titolo
d'uso, e la difesa in piattaforma quando arriva un reclamo.
