# Ripasso costruttivo — Blocco 2 (A4 L07→L18)

> Blocco: le 12 lezioni A4 sugli editor manuali (Filmora, Premiere, Final Cut, Audacity) e sugli
> strumenti generativi di terzi (avatar, musica). Tutte dichiarate BRONZO nel primo passaggio, con
> la domanda «quale documento cambio?». Qui si ripassano con le quattro domande nuove: AGENTE,
> SKILL/COMANDO, FLUSSO, CODICE — verificando ogni proposta contro `INVENTARIO.md` prima di
> scriverla, e contro i file reali della fabbrica (letti, non presunti) per evitare doppioni.

---

### P-B2-01 · script/codice
- **Lezione:** A4/L11 — «Intelligenza Artificiale con Premiere Pro (SENSEI)»
- **Prova:** `RAPPORTO-GREZZO-L11.md` §2.2 — «quando si cambia il formato della sequenza da
  orizzontale a verticale, il soggetto principale sparisce dall'inquadratura» @06:55-07:05;
  l'effetto "Reframe automatico" lo ricentra da solo, anche in bulk su un'intera sequenza
  @10:18-11:06; uso dichiarato per Shorts/Reels/TikTok, durata target 1 minuto @09:46-09:55.
- **Cosa manca oggi:** la regola già estratta (`A4-L11-01`) dice solo «noi generiamo già nel
  formato di destinazione, il problema non si pone» — vero per UN video generato per UN canale
  verticale. Ma non copre il caso opposto: prendere un video orizzontale già prodotto e ricavarne
  Shorts verticali tenendo il soggetto a centro-inquadratura. Verificato contro `INVENTARIO.md`:
  zero script con `reframe`, `crop`, `repurpos*`, `shorts` nel nome; zero agente che parli di
  "ricavare formati multipli da un video". La fabbrica genera un formato a canale, non riusa un
  video lungo per produrne varianti brevi — è una capacità assente, non uno strumento diverso per
  fare la stessa cosa.
- **Cosa nasce:** `02-AUTOMAZIONI-E-SCRIPTS/reframe_shorts.py` — dato un MP4 orizzontale già
  esportato e i timestamp delle scene (già nel payload Fliki), individua il soggetto per
  fotogramma (face/object detection leggero, es. `mediapipe` o `opencv` Haar/DNN) e produce un
  ritaglio verticale 9:16 centrato sul soggetto via `ffmpeg` (crop filter programmatico), operabile
  da CLI/funzione — mai un editor aperto a mano. Aggancio naturale: dopo `video-producer.md`,
  prima di `metadata-optimizer.md`, per i video scelti come sorgente di Shorts.
- **Perché vale:** oggi un video lungo prodotto finisce in un solo formato. Con questo script un
  video diventa anche 2-4 Shorts derivati, moltiplicando l'output pubblicabile senza rigenerare
  nulla da Fliki (zero costo API aggiuntivo) — è esattamente il tipo di leva che il metodo
  copia-incolla insegnava a fare a mano su materiale ALTRUI; qui la applichiamo a materiale NOSTRO,
  dove non c'è alcun problema di diritti.
- **Binario:** B (nuovo script in 02-AUTOMAZIONI-E-SCRIPTS, wiring nella catena di produzione)
- **Misura:** esiste `reframe_shorts.py` sul disco, e almeno un video pubblicato ha uno Short
  derivato con lo stesso soggetto a centro-inquadratura per tutta la durata.

### P-B2-02 · codice
- **Lezione:** A4/L08 — «Premiere Pro Mega Tutorial Completo» + A4/L18 — «Registrare Voice Over
  con Audacity»
- **Prova:** L08 @44:39-45:06 — musica portata da 0 dB a −25 dB («ancora troppo alta»), chiusa a
  −35 dB. L18 @15:38-16:05 — «l'audio fa la differenza nel caso in cui è scadente», cioè un gate
  difende una soglia misurabile, non un ideale.
- **Cosa manca oggi:** letto `qa-audio-video.md` per intero (non presunto): il criterio
  «Bilanciamento Volumi» è dichiarato inapplicabile a mano (§10, verificato che il payload non ha
  campo musica), ma **tutti gli altri criteri della checklist — nitidezza audio, correttezza
  pronuncia, sincronizzazione sottotitoli — restano verificati ad ORECCHIO**: il playbook dice
  letteralmente «Controlla il video tramite l'anteprima/file finale» (§4.2). Verificato
  nell'inventario: nessuno script misura dB/LUFS/RMS di un MP4 esportato — `quality_gate.py`
  (letto per intero) valuta solo JSON di specifica (`fliki_spec_valid`), mai il file audio/video
  reale. Il numero −35 dB (A4-L08-02) sta scritto in un file di riferimento ma non lo legge nessun
  controllo automatico: è un metro senza righello.
- **Cosa nasce:** `02-AUTOMAZIONI-E-SCRIPTS/audio_level_check.py` — usa `ffmpeg`/`ffprobe`
  (`volumedetect` o `loudnorm` in modalità misura) sul MP4 esportato per calcolare il livello medio
  e di picco della traccia audio, e lo aggancia come nuovo gate `L4_L5b` in `quality_gate.py`:
  fallisce se il livello è fuori da una soglia dichiarata (oggi solo voce: fascia di volume
  "scadente" da definire col primo campione reale; il giorno in cui rientrerà la musica, il tetto è
  −35 dB come da A4-L08-02). Sostituisce il controllo a orecchio del §4.2 di `qa-audio-video.md`
  con un numero riproducibile.
- **Perché vale:** oggi «Nitidezza Audio» è una checkbox spuntata a giudizio umano, per un gate che
  si dichiara bloccante. Uno script che misura il file reale rende il gate verificabile da chiunque
  (anche da un altro agente), non solo da chi lo ascolta quella volta — ed è la stessa mossa che
  L18 chiede: una soglia, non un'impressione.
- **Binario:** B (nuovo script + nuova regola dentro `quality_gate.py`, motore in produzione)
- **Misura:** `audio_level_check.py` esiste, `quality_gate.py` ha il gate `L4_L5b` registrato, e
  almeno un run di produzione mostra un valore numerico di dB nel report QA invece della sola
  checkbox.

### P-B2-03 · agente
- **Lezione:** A4/L15 — «Crea il tuo AVATAR con A.I» (con richiamo a L09, L12, L13, L16)
- **Prova:** L15 @11:36-11:48 — l'avatar legge una finta notizia di lutto su un cantante italiano
  reale, senza una parola su consenso; @09:08-10:52 — personaggio Dragon Ball generato e fatto
  parlare, senza menzione di copyright. Stesso schema d'errore già visto in L09 (manovre di
  camuffamento, catalogo §6), L12 (mito 7 — voce+sottotitoli = originale), L13 (aggiramento
  licenza), L16 (separazione audio di brani altrui).
- **Cosa manca oggi:** letti `regolatore-originalita.md` e `qa-audio-video.md` per intero: il
  primo misura SOLO la somiglianza n-gram fra script e transcript sorgente (per lo script-writer
  attuale, che riscrive da un video base); nessuno dei due — e nessun altro agente in
  `03-AGENTI-E-RUOLI/` — legge il testo dello script cercando **nomi di persone reali**,
  **personaggi protetti**, richieste di separazione audio di brani altrui, o richieste di
  strumenti con licenza aggirata. Le nove porte chiuse che questo blocco ha scritto in
  `monetizzazione-compliance.md` (§5-§9) sono regole **lette da un umano**, mai controllate da un
  gate: se domani uno script-writer (umano o agente) scrivesse «fai leggere questo testo a un
  avatar con la voce di [persona reale]», oggi non lo fermerebbe nessuno strumento, solo la
  memoria di chi rilegge la scheda.
- **Cosa nasce:** `03-AGENTI-E-RUOLI/controllo/compliance-gate.md` — nuovo agente L2 di
  `classe: controllo`, attivato subito dopo `script-writer` e prima di `video-producer` (come
  `regolatore-originalita`, ma su un asse diverso: non originalità, compliance). Playbook: legge lo
  script finale e cerca (a) nomi propri di persone reali con dichiarazioni messe in bocca loro,
  (b) nomi di personaggi/opere protette note, (c) richieste che implicano materiale audio/video di
  terzi (separazione, riuso, camuffamento) — usando come lista di pattern proprio il catalogo delle
  manovre già scritto in `monetizzazione-compliance.md` §5-§9. BLOCCO motivato con la porta chiusa
  esatta citata, non un rifiuto generico.
- **Perché vale:** chiude esattamente il buco che l'ISTRUZIONI di questo studio descrive — 64
  regole su 69 finite in un `.md` che nessuno consulta a runtime. Le nove regole di compliance di
  questo blocco (L09, L12, L13, L15×2, L16×2, L17×2) restano parole scritte finché non c'è un
  agente che le applica prima che il video venga generato, non dopo che qualcuno se n'è accorto.
- **Binario:** A (nuovo file agente in 03-AGENTI-E-RUOLI, nessuna riga del motore toccata per
  attivarlo come agente L2 a prompt; solo se in futuro si vorrà automatizzarne la ricerca pattern
  con codice si passa a B)
- **Misura:** `compliance-gate.md` esiste, è agganciato nello `spawned_by`/`blocca` di
  `script-writer.md`, e almeno un caso di test (uno script con un nome reale inventato) produce un
  BLOCCO motivato con citazione della porta chiusa in `monetizzazione-compliance.md`.

### P-B2-04 · script/codice
- **Lezione:** A4/L12 — «Video Virali con sottotitoli automatici in 2 minuti»
- **Prova:** @07:14-07:35 — il docente seleziona una frase trascritta male («grande affetto dei
  suoi figli») e la corregge a mano, dopo aver ascoltato che la trascrizione automatica di Premiere
  non coincideva col parlato reale.
- **Cosa manca oggi:** la lezione stessa non porta nulla di trasferibile (RAPPORTO-GREZZO-L12.md
  §8: «zero materiale trasferibile»), ma il *problema* che mostra è reale anche per noi, per una
  ragione diversa dalla sua: Fliki genera sottotitoli dal TESTO che gli mandiamo, assumendo che il
  TTS lo legga esattamente come scritto. Letto `qa-audio-video.md` §3: «Correttezza Pronuncia» è
  verificata solo ad ascolto umano, e §8 conferma che gli errori di pronuncia finiscono a mano nel
  lessico solo se qualcuno se ne accorge e se lo scrive. Non esiste, nell'inventario, alcun
  controllo che confronti *cosa dice davvero l'audio generato* con *cosa doveva dire lo script*:
  se il TTS storpia, salta o ripete una parola, i sottotitoli (generati dal testo originale, non
  dall'audio) mentirebbero silenziosamente su ciò che si sente — esattamente lo scarto che L12
  risolve a mano con la trascrizione automatica.
- **Cosa nasce:** `02-AUTOMAZIONI-E-SCRIPTS/verifica_pronuncia.py` — dopo l'export Fliki, esegue
  una trascrizione automatica (ASR locale, es. `faster-whisper`, nessuna dipendenza da un servizio
  a pagamento) sulla traccia audio del MP4 e la confronta (diff a parole) con lo script inviato:
  ogni scarto oltre soglia (parola mancante, sostituita, irriconoscibile) va in un report che
  alimenta direttamente `lessico-pronuncia.md` come proposta pronta da confermare, invece di
  aspettare che un umano se ne accorga ascoltando.
- **Perché vale:** oggi il lessico-pronuncia si riempie solo per gli errori che qualcuno HA
  SENTITO. Uno script che confronta scritto/parlato trova gli errori che nessuno ha ancora sentito,
  prima della pubblicazione — il gate qa-audio-video smette di dipendere dall'orecchio di chi è di
  turno quel giorno.
- **Binario:** B (nuovo script + wiring nel gate `qa-audio-video`/`quality_gate.py`)
- **Misura:** `verifica_pronuncia.py` esiste, e almeno un run produce un diff testo-atteso vs
  testo-riconosciuto con almeno una proposta scritta automaticamente in `lessico-pronuncia.md`.

### P-B2-05 · codice
- **Lezione:** A4/L10 — «Montaggio Video Pro con Premiere Pro»
- **Prova:** @04:01 — «ecco perché vi consiglio di creare un'intro e anche un outro»; @07:27 —
  l'intro allunga il video e lo rende riconoscibile come proprio.
- **Cosa manca oggi:** la regola `A4-L10-01` è già applicata (dichiarazione dell'assenza nella
  spec) e `REPORT-BLOCCO-EDITING.md` §6 registra correttamente che avere o no intro/outro è una
  **decisione di prodotto per Max**, non un parametro — e la mette in `BACKLOG.md`, giustamente,
  senza bloccare nient'altro (ADR-028). Quello che manca non è la decisione: è che oggi, SE Max
  dicesse sì domani, non esiste alcun meccanismo tecnico pronto per eseguirla. Verificato:
  `fliki_client.py:252` (il payload) non ha alcun campo per clip di apertura/chiusura, e
  nell'inventario nessuno script compone/concatena asset video fissi con l'MP4 generato.
- **Cosa nasce:** `02-AUTOMAZIONI-E-SCRIPTS/intro_outro_stitcher.py` — funzione pronta ma NON
  agganciata di default: dati un intro.mp4/outro.mp4 per canale (in una cartella
  `assets/intro-outro/<canale>/`) e l'MP4 di Fliki, concatena via `ffmpeg` (concat demuxer, senza
  ricodifica se i codec combaciano) producendo l'MP4 finale con firma di apertura/chiusura. Resta
  spento finché non arriva la decisione di Max; il giorno in cui arriva, l'esecuzione è immediata
  invece di dover essere scritta da zero sotto pressione.
- **Perché vale:** separa la decisione (che aspetta legittimamente Max, ADR-028) dal lavoro
  preparatorio (che non deve aspettare nessuno): quando la decisione arriva, il costo di attivarla
  scende da "scrivere uno script" a "attivare un flag".
- **Binario:** B (nuovo script in 02-AUTOMAZIONI-E-SCRIPTS; resta inattivo finché non collegato)
- **Misura:** `intro_outro_stitcher.py` esiste sul disco e supera un test locale con due file MP4
  di prova concatenati correttamente, anche se non ancora richiamato in produzione.

### P-B2-06 · flusso
- **Lezione:** A4/L14 — «Final Cut: Metodo Copia & Incolla Avanzato»
- **Prova:** @09:36 e @11:35 — «è fondamentale cambiare tutte le clip dei primi 30 secondi… il tuo
  obiettivo non è solo farlo cliccare, ma fargli vedere l'intero video» → principio già applicato
  in `script-writer.md` §11 (apertura come leva di ritenzione, non solo CTR).
- **Cosa manca oggi:** letto `channel-performance-analyst.md` per intero: l'agente dichiara
  esplicitamente, come regola di failure-mode, che «CTR, retention e ricavi richiedono YouTube
  Studio, che è privato» e nei log li lascia sempre `null` — l'unica fonte usata è
  `youtube_hunter_playwright.py`, scraping pubblico che vede solo views ed età. Risultato: la
  regola appena scritta in `script-writer.md` §11 (l'apertura si misura sulla ritenzione ai 30s)
  **non può mai essere verificata con un dato reale**, perché nessuno strumento della fabbrica
  legge la retention curve — che YouTube espone via **YouTube Analytics API**, autenticata via
  OAuth sul canale proprietario (non serve scraping, il canale è nostro). Non è un limite fisico:
  è un flusso mai costruito.
- **Cosa nasce:** ridisegno del flusso di `channel-performance-analyst`: un nuovo script
  `02-AUTOMAZIONI-E-SCRIPTS/youtube_analytics_client.py` che si autentica via OAuth sul canale di
  proprietà e scarica `audienceWatchRatio`/retention curve per video pubblicato, con il punto ai
  30 secondi isolato come campo dedicato. `channel-performance-analyst.md` smette di scrivere
  `null` su retention per i canali dove l'OAuth è configurato, e correlato allo stile di apertura
  (domanda/affermazione, presenza promessa specifica) per dire, con dati reali, se la regola L14
  funziona per noi o va corretta.
- **Perché vale:** oggi applichiamo una regola di ritenzione presa da un tutorial di editing e non
  abbiamo modo di sapere se, sul nostro canale, funziona. Senza questo flusso la regola resta un
  atto di fede citato da una fonte esterna; con questo flusso diventa una regola che il canale
  stesso può confermare o smentire.
- **Binario:** B (nuovo script nel motore + modifica del playbook di un agente esistente)
- **Misura:** `youtube_analytics_client.py` esiste, e almeno un report di
  `channel-performance-analyst` mostra un valore di retention reale (non `null`) accanto allo stile
  di apertura del video corrispondente.

### L07 — nessuna proposta aggiuntiva
Riletta integralmente (appunti + regola `A4-L07-01`). È la lezione più povera del blocco: tutorial
puro d'interfaccia Filmora, un solo mito già estratto e applicato. Anche applicando le quattro
domande nuove non emerge nessun problema che la fabbrica non affronti già altrove (color/effetti
manuali non hanno equivalente via API da colmare): dichiarata a vuoto, onestamente.

### L09, L13, L16, L17 — coperte dalle proposte sopra, nessuna proposta autonoma aggiuntiva
Il contenuto operativo di queste quattro lezioni (catalogo manovre L09, aggiramento licenza L13,
separazione audio L16, licenza musica AI L17) è già la materia prima di **P-B2-03** (il catalogo
delle porte chiuse che il compliance-gate deve saper riconoscere). Non emerge, rileggendole con le
quattro domande nuove, alcun bisogno DISTINTO da quello già coperto — proporre un secondo agente/
script per ciascuna sarebbe frammentare la stessa esigenza (far rispettare le porte chiuse) in più
pezzi invece che in uno.

## FINITO — 6 proposte, lezioni ripassate: L07, L08, L09, L10, L11, L12, L13, L14, L15, L16, L17, L18
