# RAPPORTO GREZZO — A4/L20 — «Aggiornamento Fliki Luglio 2024»

Fonte: `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/corso-aitubepro/738f5b4b-59d7-48e4-ade5-f9b6c157cabc/parlato.txt`
Letto integralmente, dal minuto 00:00 al minuto 76:00 (1227 righe). Nessun campionamento.

---

## 1. Cos'è la lezione, davvero

È una **live registrata**, non una lezione registrata in studio: apre "Pietro" che introduce "Samuele" ("Samo"/"Sam"), presentato come il responsabile del reparto di video produzione — chiamato in trascrizione "la muccarossa" (**trascrizione incerta @ 01:39**, probabile nome del brand/canale interno). Per il 90% del tempo è **tutorial pratico a schermo condiviso**: Samuele clicca dentro l'editor Fliki e mostra funzione per funzione, partendo da un file vuoto. La parte di "novità di prodotto" vera e propria (funzioni introdotte di recente da Fliki) occupa circa i due terzi centrali (03:38-59:18). Il resto si divide fra: apertura/hype e community-building (00:00-03:38), aneddoti e posizionamento competitivo rispetto a Premiere/Filmora/Adobe e vendita indiretta del corso ("non è scontato che vi aggiorniamo così", 74:47-76:00), e un blocco di Q&A dal vivo (69:52-73:41). Non c'è quasi nulla di teoria astratta: è tutto mostrato dal vivo, con errori e correzioni in diretta (es. 41:38-41:51 lui stesso sbaglia la scena e si corregge).

---

## 2. LE NOVITÀ DI FLIKI, UNA PER UNA

Ordine di apparizione nel video.

**A) Riposizionamento diretto (drag) di qualsiasi oggetto (media, sottotitoli, logo) direttamente sulla scena, con menu laterale di precisione (top/left ecc.)**
Dove: click su un qualsiasi media/testo → appare un menu laterale con frecce di spostamento.
Minuto: 12:37-13:33 ("queste ho un altro delle cose stupende che hanno fatto da poco tempo, cliccando su qualsiasi oggetto media o anche sottotitoli... abbiamo la possibilità di fare questo").
API o solo click: **solo click** nell'editor visuale. Se il payload della nostra fabbrica genera scene via JSON, la posizione finale del layer potrebbe comunque essere un campo esposto — da verificare, non assumere che sia editor-only nel payload.

**B) Background blur + angoli arrotondati per un'immagine/logo inserito come layer**
Dove: click sul logo/immagine inserita → pannello a destra, opzione "background blur" e arrotondamento angoli.
Minuto: 13:33-14:02 ("abbiamo cliccando background blur... ha un vero proprio tondino").
API o solo click: sembra uno stile applicato al layer immagine (blur, border-radius) — potenzialmente un parametro dello stesso oggetto "image layer" nel payload, da verificare.

**C) Segmentazione automatica del testo in scene con abbinamento immagini migliorato**
Dove: incolla di un testo lungo (es. articolo di viaggio) → Fliki lo divide da solo in scene con immagini già assegnate, senza il lavoro manuale di taglio/immagine-per-blocco che si faceva "una volta" (in maniera manuale, descritta come "rozza").
Minuto: 16:44-18:11 ("oggi invece non c'è più la necessità perché grazie all'ultimo upgrade che hanno fatto").
API o solo click: presumibilmente lato generazione contenuto — è compatibile con come già lavora la nostra fabbrica via payload testo→scene, ma va verificato se il "matching immagine automatico migliorato" dipende da un modello lato Fliki invocato anche via API o solo dall'editor web.

**D) "B-roll" — evidenzi una frase narrata e Fliki crea in automatico un media aggiuntivo sincronizzato al secondo esatto della narrazione**
Dove: selezioni il testo nella scena → appare un menu con l'opzione "B-roll". Fliki calcola quanti secondi dura la narrazione di quel pezzo di testo (es. "dura 9 secondi") e crea un media che occupa esattamente quell'intervallo, frazionando automaticamente la scena in più segmenti temporizzati con precisione al secondo (esempi dati dal vivo: "8 secondi... dura 10... 9 secondi... fino 11... 2 secondi di scena... 10 va 12").
Minuto: 19:34-21:04 (spiegazione e demo), poi riapplicato al caso "leoni" 39:42-40:56, e ancora nell'esempio combattimenti gladiatori 41:24-43:36.
**Prerequisito operativo**: prima di usare B-roll bisogna dare "Play" a tutta la scena/timeline per far calcolare a Fliki la durata reale del testo (18:14-19:22: "dovete sempre dare un play generale a tutto in modo che Fliki calcoli il tempo del testo... in secondi generazione").
**Effetto collaterale da conoscere**: il primo media che B-roll inserisce sopra il media originale diventa orfano/inutile, non compare più nella timeline ma pesa comunque in fase di export e va cancellato manualmente (21:16-21:52: "questo media è presente, ma non è presente perché non si vede... provvediamo e lo cancelliamo").
API o solo click: **verosimilmente editor-only**, è un calcolo fatto interattivamente sul testo evidenziato nell'editor. Se il nostro payload costruisce le scene in automatico via API, questa funzione di segmentazione "intelligente" andrebbe verificata come endpoint separato — non darla per scontata come comportamento di default della generazione via API.

**E) Allineamento libero dei sottotitoli (posizionamento ovunque nel frame, non solo alto/centro/basso)**
Dove: click sul testo/sottotitolo → menu laterale di posizionamento con guide a croce per centrare rispetto all'immagine.
Minuto: 24:56-25:31 ("una volta poteva[no] far solo... mettere al centro, spostare più su, spostare più giù... oggi... abbiamo la possibilità di mettere dove vogliamo").
API o solo click: click, editor grafico.

**F) Effetto "Fill" — evidenziazione delle parole in sincrono con la narrazione (stile karaoke, in trasparenza fino a rivelare colore)**
Dove: pannello effetti del testo/sottotitoli.
Minuto: 29:23-30:10.
**Avviso esplicito del relatore**: con alcuni narratori o in alcuni momenti il sincrono si sfasa ("il narratore 3, 4, 5 parole avanti che ancora devono scattare le parole... il narratore avanti, sottotitoli sono indietro, quindi occhio"), definendolo "potrebbe essere la nostra rovina" (29:23-30:10).
API o solo click: effetto visivo dell'editor sottotitoli.

**G) Contorno/Stroke sul testo dei sottotitoli**
Dove: stesso pannello effetti testo.
Minuto: 30:10-31:00 (avviso: se il contorno è troppo marcato "devasta il testo, non è più leggibile").
API o solo click: click.

**H) Strumento di prelievo colore dalla scena ("contagocce" — trascritto "contavoce", trascrizione incerta @ 31:00) per abbinare i colori del testo/logo ai colori presenti nell'immagine**
Minuto: 31:00-31:49 ("è uno strumento davvero finissimo... abbiamo la possibilità di creare un equilibrio tra tutti i colori").
API o solo click: click, strumento grafico.

**I) Effetto "Text Color" — variante di Fill che mostra subito la parola nel colore scelto (senza passaggio di trasparenza)**
Minuto: 31:59-32:25.
API o solo click: click.

**J) Effetti Zoom sulle immagini**
Minuto: 32:25-32:35 (menzione rapida: "gli zoom sono carini se li utilizzate moderatamente").
API o solo click: click.

**K) Animazioni di ingresso/uscita della scena**
Minuto: 32:35-32:50.
API o solo click: click.

**L) Visualizzazione della forma d'onda audio (waveform), riposizionabile in alto/basso**
Minuto: 32:50-33:18.
API o solo click: click.

**M) Transizioni fra scene (pannello "Transizione" > "Type", es. "flip") + suono opzionale al cambio scena**
Dove: click sul banner "Scena" (non sul singolo media) → pannello Transizione.
Minuto: 48:19-48:52 ("se voi cliccate su... transizione, qui c'è type... facciamo flip"; suono al cambio scena 48:42-48:51, con avviso che "potrebbero infastidire").
API o solo click: click, ma "type" di transizione e "suono" sembrano parametri strutturati (enum) plausibilmente esposti anche via API scene-config — da verificare.

**N) Layer di testo con "Timing" per far comparire/sparire un elemento (es. una cifra) a un secondo preciso**
Dove: "Add Layer" > "Text", poi pannello "Timing" per impostare inizio/fine in secondi.
Minuto: 48:57-51:23 (esempio: far comparire il numero "7" colorato solo tra il secondo 7 e il secondo 9, sincronizzato alla narrazione del numero).
API o solo click: il concetto di "layer con start/end in secondi" è esattamente il tipo di dato che una API di composizione video espone come oggetti di scena — **candidato forte da verificare nel nostro payload**.

**O) Pannello "Timing" generico per spostare a piacimento inizio/fine di un qualsiasi media dentro una scena (indipendente dal calcolo automatico di B-roll)**
Minuto: 42:47-43:36 (regolazione manuale dei secondi di un media "leoni" da 22 a 26), riusato per sincronizzare l'audio generato (vedi punto P) a 46:04-46:56.
API o solo click: come sopra, verosimile campo di scena esposto anche via API.

**P) Generazione di audio/effetti sonori (SFX) da prompt testuale — "Add Layer" > "Audio" > "Generate"**
Dove: aggiungi layer audio (non la traccia musicale di sottofondo) → tab "Generate" → si scrive un prompt testuale (nell'esempio, tradotto in inglese da uno strumento esterno prima di incollarlo: "ruggito leone" → prompt inglese) → Fliki genera l'effetto sonoro, rigenerabile se non soddisfa.
Minuto: 44:53-46:04 ("uno strumento davvero figissimo che hanno fatto... vado sul traduttore perché non lo so come si scrive... faccio Generate").
Poi sincronizzato al secondo esatto della scena con il pannello Timing (46:04-46:56).
API o solo click: **questa è la novità con più probabilità di avere un endpoint API dedicato** (generazione audio da prompt testo è un pattern tipico esposto via API in altri prodotti Fliki-simili) — da verificare con priorità contro la documentazione/endpoint Fliki usati dalla fabbrica.

**Q) Blending/trasparenza fra media impilati (opacità per layer)**
Dove: pannello destro del media selezionato, slider Opacità, con più media sovrapposti (es. Colosseo sopra Fontana di Trevi).
Minuto: 51:35-53:20 ("potete fare l'inserimento di media e operare per trasparenza").
API o solo click: click, ma opacità-per-layer è tipicamente un valore numerico di scena, potenzialmente esposto.

**R) Editor multimediale integrato (taglio, conversione formato, rotazione, velocità) per contenuti importati fino a 30 MB, gratuito e senza consumo di crediti**
Minuto: 54:44-55:29 ("avete la possibilità di inserire dentro un contenuto a 30 megabyte e tagliarlo... ruotare, aumentare o diminuire la velocità... tutti questi sono strumenti gratuiti... non consumano credito"). Il relatore precisa che l'aveva già mostrato "in un'altra lezione" (53:54-54:08) — qui viene solo richiamato, non è la novità di questa L20 nello specifico, ma va comunque registrato perché parla di limiti tecnici (30 MB) e costo zero.
API o solo click: editor manuale nel browser, verosimilmente non parte del payload di generazione via API.

**S) Generatore di miniature ("Miniatura"/Thumbnail) integrato in "New File", gratuito, con suggerimenti automatici e watermark opzionale**
Dove: "New File" > "Miniatura". Si scrive un testo (es. "Cosa visitare a Roma in 3 giorni") e Fliki propone layout, sfondo, font, immagini.
Minuto: 56:52-59:18. Include un toggle Watermark con icona "occhio" per mostrare/nascondere (58:36-59:12: "c'è lo più sbarrato... dovete cliccare sull'occhio se volete che si veda").
Formati di esportazione della miniatura: JPEG, PNG, WebP ("Web", trascritto), PDF, formato compatibile con la suite Office — minuto 70:53-71:03.
API o solo click: strumento separato dalla generazione video, tutto a schermo nel browser; **non risulta collegato al flusso di generazione video via API** e comunque, per regola interna, la copertina la fa sempre Max — vedi sezione 7.
Nota sui crediti: passaggio confuso a 57:23-57:34 sul consumo di crediti se si usano immagini AI-generate per la miniatura vs immagini stock già incluse nel piano — **trascrizione incerta @ 57:23-57:34**, non abbastanza chiaro da riportare come regola certa.

**T) Workaround per superare il limite di 50 scene del piano base: impacchettare fino a 1000 (o 10.000, vedi sezione 4) caratteri in un'unica scena e poi frazionarli con B-roll in tanti media dentro la stessa scena, che non contano come scene aggiuntive**
Minuto: 65:24-67:53 (spiegazione tecnica), con chiusura dell'argomento a 66:59-67:23 sul limite di 50 e a 67:29-67:53 sull'esempio pratico.
API o solo click: comportamento dell'editor/contatore-scene interno a Fliki; **da verificare se lo stesso meccanismo di conteggio si applica anche alle chiamate API** (potrebbe essere un comportamento specifico dell'editor web e non del billing lato API).

**U) Voci narratore "ultra-realistiche" con pause di respiro naturali (ultimo upgrade voci)**
Minuto: 68:09-69:03 ("con l'ultima upgrade con le voci ultra-realiste che fanno i respiri... si fermano facendo le pause con i respiri... è veramente difficile che si riesca a percepire che un narratore è un'intelligenza artificiale").
API o solo click: presumibilmente selezione di un narratore/voice-ID di livello superiore — verificabile se il nostro payload seleziona narratori per ID e se questi ID includono la nuova generazione vocale.

**V) Mappa delle pronunce: comportamento "per file", propagabile solo duplicando un file-modello**
Dove: pannello pronunce (raggiunto — **trascrizione incerta @ 34:49** — "andiamo sul mur e andiamo nella parte di mappa delle pronunce", probabile refuso per "menu"), si seleziona il narratore specifico (es. "Enzo", filtrato per genere maschile a 34:56-35:25), si scrive la parola/numero, si ascolta con Play, si dà la spunta.
Minuto: 34:44-38:20 (dimostrazione con il numero "7").
Punto delicato, letto con attenzione perché tocca un fatto noto: a 38:42-39:26 il relatore usa un linguaggio che sembra suggerire una "memoria" del narratore che va oltre il singolo file ("una volta sola... poi c'è la mia memoria, io questo non so neanche quando l'ha appreso, forse in un'evoluzione di Fliki... mantengono tantissima memoria"), ma **lui stesso ammette incertezza** su come funzioni davvero. Poi chiarisce concretamente a 40:54-41:24: "io la mappa delle pronunce non l'ho utilizzata mai, vi ripeto. Quindi può darsi che la tenga solo per questo progetto e non per gli altri, però vi posso dire che io ho utilizzato in passato su diversi progetti e la mantiene, **se voi fate un qualcosa che vi ho detto sempre di fare**, quindi vi fate un'impostazione di un file campione, uno demo, e poi fate duplica. Se voi fate questa cosa qui vedrete che la mappa delle pronunce rimane sempre uguale, quindi la istruzione la mantiene". Infine, nella Q&A finale (71:52-73:41), risponde alla domanda di una studentessa confermando la pratica operativa raccomandata: correggere una pronuncia SUL FILE DI LAVORO **non basta** — bisogna copiare la stessa correzione anche sul file "demo"/modello, altrimenti i prossimi file duplicati non la erediteranno ("vado sulla demo, scrivo sette, poi faccio incolla... così ho aggiornato anche il file demo").
**Lettura netta**: questo **conferma e affina** il fatto noto "la mappa delle pronunce vale per questo video soltanto, non è una configurazione d'account" — la propagazione ad altri video avviene solo tramite duplicazione di un file-modello che già contiene le correzioni, mai in automatico su tutto l'account o su tutti i progetti futuri creati da zero.
API o solo click: tutto editor web; se la nostra fabbrica crea progetti via API senza passare da una "duplicazione" di un file modello Fliki, **la mappa delle pronunce probabilmente non si applica affatto ai video generati via API**, salvo che l'API supporti un parametro pronunce a parte — da verificare con priorità alta.

---

## 3. Impostazioni, pannelli e parametri nominati (nome esatto come detto, valore, minuto)

- **Background Audio** (traccia audio di sottofondo, sezione dedicata separata da Voiceover/Media) — 03:57-05:26
- **Volume** (percentuale, sulla traccia audio) — massimo normale 15, valore "gradevole" 5 — 07:13-07:48
- **Apply to all scenes / "applica a tutte le scene"** (va rifatto ad ogni modifica, altrimenti resta solo sulla Scena 1) — 07:48-08:10, ripetuto più volte
- **Speed** (velocità narratore) — default mostrato 100, range utile "85 circa... a 100", esempio applicato 90 — 08:21-09:31
- **Watermark** (Add Layer > immagine) — 11:19-16:01
- **Background blur** (sul logo/immagine) — 13:33-14:02
- **Opacità/Opacity** — 14:02-14:29 (proporzioni), 15:29-15:37 (uso come filigrana, valore "5 barra di 10%" — **trascrizione incerta**)
- **B-roll** — 19:34-21:52, 39:42-43:36, 65:24-67:53
- **Timing** (pannello secondi inizio/fine) — 42:47-43:36, 46:04-46:56, 49:00-51:23
- **Add Layer** (con sotto-tipi: immagine, Audio, Text) — 11:19, 44:16-44:39, 48:57
- **Generate** (generazione audio/SFX da prompt testo) — 44:53-46:04
- **Fill** (effetto sottotitoli sincronizzati, stile karaoke in trasparenza) — 29:23-30:10
- **Text Color** (effetto sottotitoli, colore diretto) — 31:59-32:25
- **Stroke/contorno** — 30:10-31:00
- Strumento colore/eyedropper (nome storpiato "contavoce" — **trascrizione incerta @ 31:00**) — 31:00-31:49
- **Zoom** (effetto immagine) — 32:25-32:35
- **Animazione** (ingresso/uscita scena) — 32:35-32:50
- **Transizione > Type** (es. "flip") + suono al cambio scena — 48:19-48:52
- **Allineamento testo** (sinistra/centro/destra + posizionamento libero drag) — 24:56-25:31
- **Font size** — range consigliato "tra 50 e 60" — 27:01-27:22
- **Font weight**: grassetto, corsivo, normale, light, extra bold — 27:41-28:19
- **New File**: opzioni incluse Blank (16:9) e **Miniatura** (Thumbnail) — 03:38-03:50, 56:52-56:58
- **My Library** / **Stock library** (fonti media) — 23:12-23:24, 60:28-60:33
- **Mappa delle pronunce** (per narratore, es. Enzo/Elsa) — 34:44-41:24, 71:52-73:41
- **Voci ultra-realistiche** (con pause di respiro) — 68:09-69:03
- Formati export miniatura: **JPEG, PNG, WebP ("Web"), PDF, formato Office-compatibile** — 70:53-71:03
- Traduzione: **non trattata come funzione Fliki di doppiaggio/traduzione video**; unico uso della parola "traduttore" è manuale ed esterno, per tradurre un prompt in inglese prima di incollarlo nel tool Generate audio — 44:53-45:14
- Avatar, cloni vocali: **non menzionati in nessun punto della lezione**

---

## 4. Numeri

| Dato | Valore | Minuto |
|---|---|---|
| Formato del progetto vuoto (New File > Blank) | 16:9 | 03:45-03:50 |
| Volume musica di sottofondo — massimo normalmente applicato | 15% | 07:13-07:25 |
| Volume musica di sottofondo — valore "gradevole" tipico | 5% | 07:39-07:48 |
| Velocità narratore — range utilizzabile | 85 - 100 | 08:38-08:49 |
| Velocità narratore — valore applicato nell'esempio | 90 | 09:21-09:31 |
| Durata contenuto consigliata per generare più ads | "sopra gli 8 minuti" | 08:59-09:17 |
| Stesso concetto ripetuto pochi secondi dopo (incoerente col precedente) | "sopra gli 2 minuti" — **trascrizione incerta @ 09:17-09:21**, probabile errore di trascrizione/lapsus del relatore | 09:17-09:21 |
| Opacità watermark usato come filigrana anti-copia | "5 barra di 10%" — **trascrizione incerta**, valore non chiaro (forse 5/10 = 50%, forse 5%) | 15:29-15:37 |
| Durata del video-demo dopo il primo giro di B-roll (3 scene, Roma) | 1 minuto e 20 secondi | 19:22-19:31 |
| Font size sottotitoli — range consigliato | 50 - 60 | 27:01-27:22 |
| Limite upload editor multimediale (taglio/conversione, gratuito) | 30 MB | 55:08-55:11 |
| Stima soggettiva del relatore sul peso della miniatura nel successo di un video (claim, non parametro Fliki) | "quasi il 90%" | 57:59-58:09 |
| Limite scene sul piano base di Fliki | 50 scene | 66:59-67:23 |
| Capacità caratteri in un'unica scena (prima citazione) | "mille caratteri" | 65:29-65:38 |
| Capacità caratteri in un'unica scena (seconda citazione, incoerente con la prima) | "10.000" | 67:41 |
| Scene aggiuntive nell'esempio del workaround anti-limite | 40 scene con 40 immagini | 67:41-67:48 |
| Durata lezione autodichiarata dal relatore | "un'ora e 10" | 69:44-69:52 |
| Timestamp finale della registrazione | 76:00 | 76:00 |

Nota: le due incoerenze numeriche (8 vs 2 minuti; 1.000 vs 10.000 caratteri) sono nel parlato originale del relatore o nella trascrizione automatica — non sono state normalizzate, sono riportate entrambe come sentite.

---

## 5. Formati e Shorts

**Nessuna menzione di formato verticale, 9:16, Shorts o TikTok in tutti i 76 minuti della lezione.** L'unico riferimento ad aspect ratio è il "16:9" del file vuoto di default a 03:45-03:50, mai messo in discussione o alternativo in nessun altro punto. Gli unici altri "formati" citati riguardano l'esportazione della **miniatura** (immagine di copertina, non il video): JPEG, PNG, WebP, PDF, formato Office-compatibile, a 70:53-71:03 — e questi non sono formati video, sono formati immagine per il file scaricabile della thumbnail. Conclusione: questa lezione **conferma** il vincolo noto (16:9 fisso, nessuna capacità Shorts) senza fornire alcun elemento nuovo o contrario.

---

## 6. Musica

- **Provenienza**: dalla libreria interna di Fliki ("libreria di Fliki"), tracce descritte come "tutte gratuite" — 05:58-06:11.
- **Diritti**: il relatore dichiara che le tracce sono "tutte licenziate" — 06:06-06:20 ("ma soprattutto sono tutte licenziate, diciamo così").
- **Claim sui reclami copyright**: "Se dovesse arrivarci una segnalazione di violazione di copyright da parte di YouTube, noi abbiamo una frase, un trafiletto che andiamo a incollare nella disputa e YouTube risolve subito la questione, perché ci sono queste tracce che sono già state licenziate" — 06:20-06:39. Punto importante: questo "trafiletto" (testo di disputa) **non è generato da Fliki**, è un template fornito a parte dal team/community del corso ("se avete bisogno, scrivete la [community?] e vi comunichiamo il trafiletto" — 06:39-06:48, **trascrizione incerta** sulla parola esatta). Quindi: Fliki fornisce le tracce licenziate, ma la gestione della disputa di copyright è un processo umano/di supporto esterno a Fliki.
- **Regolazione volume**: percentuale, con valori dati a voce — massimo normalmente applicato 15%, valore "gradevole" tipico 5% (07:13-07:48). Questo **differisce** dal riferimento noto interno di 10% — da riconciliare, non è detto che siano la stessa cosa (potrebbe dipendere dal tipo di narratore/traccia, come precisato dallo stesso relatore a 07:25-07:39: "ci devono essere le condizioni... in base alla tipologia di traccia, in base alla tipologia di narratore, in base al volume del narratore").
- **Coerenza tono/contenuto**: enfasi forte sul dover scegliere una traccia coerente col tono del video (niente musica pop su una favola della buonanotte) — 04:18-04:46.
- **Applicazione**: ogni modifica al volume/traccia va propagata con "Apply to all scenes", altrimenti resta solo sulla prima scena — 07:48-08:10.
- **Campo "YouTube channel ID(s)" nel profilo**: **non menzionato in nessun punto** di questa lezione.
- **SFX generati via AI (Generate)**: il relatore genera un effetto sonoro ("ruggito di leone") da prompt testuale (44:53-46:04) — su questo audio generato **non viene fatta alcuna dichiarazione su licenza o diritti**, a differenza delle tracce musicali di libreria. È un vuoto esplicito della lezione, da segnalare: non sappiamo, da questa fonte, se gli SFX generati via AI abbiano lo stesso trattamento "licenziato" delle tracce musicali pre-esistenti.
- **Minuti/piano come plafond mensile negoziabile**: non trattato in questa lezione.

---

## 7. Cosa è TRASFERIBILE alla nostra fabbrica

Elenco onesto — molte cose viste sono editor-only e non toccano un payload API.

**Da verificare con priorità (impatto diretto plausibile sul payload/API):**
1. **Generazione audio/SFX da prompt testuale** (punto P, 44:53-46:04) — se Fliki espone questo come endpoint API, potrebbe arricchire i nostri video con effetti sonori generati, non solo narrazione+musica. Verificare documentazione API Fliki.
2. **Timing per-media in secondi** (punti N/O, 42:47-51:23) — se il nostro payload costruisce già le scene con start/end in secondi, verificare se supportiamo lo stesso livello di granularità (media multipli sovrapposti in punti temporali precisi dentro la stessa scena) o se ci limitiamo a una scena = un media.
3. **Mappa delle pronunce legata al file, propagabile solo via duplicazione di un template** (punto V) — impatto diretto sulla domanda "come garantiamo pronunce corrette in produzione via API". Se generiamo ogni video da zero via chiamata API (senza duplicare un progetto Fliki esistente), è probabile che **nessuna correzione di pronuncia venga mai applicata automaticamente** ai nostri video. Da verificare se l'API espone un parametro pronunce indipendente dal progetto-modello.
4. **Volume musica di sottofondo: valori 15% max / 5% tipico citati qui**, diversi dal riferimento interno noto di 10% — riconciliare quale valore usiamo davvero nel payload e perché.
5. **Musica di sottofondo non è automatica**: va aggiunta esplicitamente come traccia dedicata (Background Audio, sezione separata dalla scena) — 03:57-05:26. Questo è rilevante per la domanda aperta "non sappiamo se i nostri video contengano musica di sottofondo": secondo questa lezione, nell'editor Fliki la musica **non c'è di default**, va scelta e applicata a parte con "Apply to all scenes". Se il nostro payload API non imposta esplicitamente un parametro audio/musica di sottofondo, è ragionevole assumere che i nostri video generati via API **non abbiano musica**, salvo prova contraria nel payload stesso.
6. **Limite di 50 scene sul piano base** (punto T, 66:59-67:23) — se siamo su un piano base o abbiamo dubbi sul piano attuale, verificare se questo limite si applica anche alla generazione via API o solo all'editor web, prima di scalare i volumi di produzione.

**Quasi certamente editor-only, bassa priorità di verifica:**
- Riposizionamento drag di media/testo (A), background blur/angoli (B), allineamento libero sottotitoli (E), effetti Fill/Text Color/Stroke (F/G/I), color picker (H), zoom (J), animazioni scena (K), waveform (L), transizioni fra scene (M), opacità/blending fra media (Q) — tutte interazioni visuali dell'editor, pensate per chi monta a mano dentro Fliki, non per una pipeline API. Se il nostro output finale API è già un MP4 renderizzato, queste sono rifiniture che l'API probabilmente non espone affatto (sono post-produzione manuale, non parametri di generazione).
- Editor multimediale integrato per taglio/conversione (R, limite 30 MB) — utile solo se noi montiamo manualmente dentro Fliki, non per la fabbrica automatica.
- Generatore di miniature (S) — **esplicitamente fuori perimetro per regola interna** (la copertina la fa sempre Max, mai la macchina). Non ha senso valutarlo come sostituto del nostro processo attuale a meno che quella regola cambi.
- Voci ultra-realistiche (U) — utile solo per sapere se il narratore che scegliamo nel payload (per voice-ID) appartiene già a questa generazione più naturale; non è una funzione da "attivare", è una qualità del modello vocale sottostante.

---

## 8. Affermazioni da segnare

- **Copyright/dispute music**: *"Se dovesse arrivarci una segnalazione di violazione di copyright da parte di YouTube, noi abbiamo una frase, un trafiletto che andiamo a incollare nella disputa e YouTube risolve subito la questione, perché ci sono queste tracce che sono già state licenziate."* — 06:20-06:39
- **Zero crediti (promessa in apertura, riferita più avanti agli strumenti gratuiti mostrati)**: *"Ci sarà una novità davvero carina che hanno trovato da pochissimo e che mette in modo di [...] spreca[re] zero crediti"* — 03:08-03:18 (**trascrizione incerta** sulla parte centrale della frase)
- **Contenuti duplicati/originalità impossibile da violare**: *"Se ipotizziamo 100 persone [...] che in questo momento stanno lavorando su un video sul Roma, con lo stesso [contenuto], è quasi impossibile che il contenuto sarà uguale per tutte e cento le persone [...] e matematicamente impossibile che [siano identici] con condizioni del genere."* — 47:02-48:00 circa (numerazione minuti approssimata sul blocco di risposta alla domanda in chat)
- **Peso della miniatura sul successo del video**: *"Sappiamo che la miniatura ha un peso davvero troppo importante per un contenuto che va su YouTube, e non vi dico che 90% ma davvero poco ci manca."* — 57:59-58:09
- **Voci indistinguibili dall'umano**: *"È veramente difficile che si riesca a percepire che un narratore è un'intelligenza artificiale."* — 68:56-69:03
- **Promessa di ricezione email della registrazione**: *"Vi arriverà sicuro al cento per cento."* — 74:47-75:05 (promessa organizzativa del corso, non di Fliki)
- **Editor gratuito, nessun consumo credito**: *"Tutti questi sono strumenti gratuiti che mette a disposizione Fliki, e che non consumano credito."* — riferito all'editor multimediale (taglio/conversione), 55:22-55:29

---

## 9. Verdetto in una riga

Lezione-aggiornamento di luglio 2024, quasi tutta tutorial pratico sull'editor Fliki (poco vendita, poca teoria): conferma senza smentite i tre vincoli noti (16:9 fisso/niente Shorts, musica non automatica ma da aggiungere a mano, pronunce legate al singolo file/propagate solo via duplicazione di un template), aggiorna il riferimento sul volume musica (15% max / 5% tipico, non 10%) e introduce almeno tre funzioni — B-roll a tempo automatico, generazione SFX da prompt testuale, timing per-media in secondi — che vanno verificate una per una contro il payload API della fabbrica prima di assumere che valgano anche lì.
