# Appunti — A6/L04 · «Come aumentare il CTR vertiginosamente»

- **Corso:** AI TUBE PRO · **Categoria:** YouTube Viral Mastery · **Ordine:** 4
- **Durata:** 21:12 (1272s) · **id:** `bd269e1e-eff1-4e33-b519-0f0de2984bd9` · parlato **2.993 parole**
  (141 parole/minuto — sopra soglia 60, trascrizione valida)
- **Materiale:** 636 frame densi (1 ogni 2s) → **54 unici** (-91,5%), campione di 12 guardati
  (i cambi di schermata con dati numerici reali; i "presidio" — 30s statici sullo stesso pannello
  Analytics mentre il docente parla sopra — non aggiungono cifre nuove, dichiarato non nascosto)
  · **profondità ORO**
- **Canale mostrato:** "Rai" (nicchia notizie/gossip), lanciato ~un mese prima della
  registrazione, dati da YouTube Studio reale

> **Il raccolto migliore, di nuovo, è nel confronto col nostro codice**: il docente dimostra per
> 21 minuti un metodo che dipende per intero da dati che il nostro `channel-performance-analyst`
> dichiara esplicitamente **impossibili da ottenere** (`ctr: None`, `retention_rate: None`,
> `apex7_orchestrator.py:1680-1684`) perché letti da fetch pubblico, non da YouTube Studio. Ma lo
> stesso repository ha **già** uno script che fa login persistente su `studio.youtube.com`
> (`youtube_uploader_playwright.py`) — la porta per prendere questi dati **esiste già aperta**,
> solo per la pubblicazione, mai per la lettura Analytics.

---

## 00:06 — 00:54 · Perché il CTR conta: la definizione e il primo caso reale

Apertura diretta (00:06): CTR = "click true rate" (mistrascritto per "click-through rate"),
dichiarato **il dato più importante insieme al watch time** per far diventare un video virale
(00:16-00:22). Il docente dichiara di aver aspettato **due giorni** prima di girare il video, per
avere dati reali da mostrare (00:22-00:31).

Primo caso: il primo video pubblicato sul canale, nei primi due giorni **26 visualizzazioni**,
**3,3% CTR**, durata media di visualizzazione **49 secondi** (00:36-00:50) —
`frame-028.png @ 0:54` conferma a schermo: "26 visualizzazioni", tempo di visualizzazione "0,4"
(ore), 0,02€ di entrate, grafico "Momenti chiave per la fidelizzazione del pubblico" con
"0:54 durata visualizzazione media" e **57,6% percentuale visualizzata** (video di 1:35).

## 00:54 — 02:46 · Da dove arriva il pubblico, e la tab "Copertura"

Il pubblico arriva principalmente da **ricerca di YouTube** e **video consigliati**
(01:16-01:30); obiettivo dichiarato: far arrivare le visualizzazioni da video consigliati, non
solo dalla ricerca — perché più alto il CTR, più YouTube spinge nei consigliati (01:51-02:02).

Per vedere questo dato si va sul tab **Copertura**: `frame-087.png @ 2:52` mostra lo stesso
pannello di `frame-028` (tab "Panoramica" ancora attivo nello screenshot, il cambio di tab è
nell'azione successiva non catturata in questo campione) — 26 visualizzazioni, 0,4h, confermando
i numeri del minuto precedente. Il parlato aggiunge (02:17-02:40): copertina apparsa **642 volte**,
CTR 3,3%, 53% dei click da video consigliati, 34% da ricerca YouTube, resto da funzioni di
navigazione — **solo parlato**, non ripreso in un frame dedicato nel campione.

## 02:46 — 05:47 · Caso comparativo: canale lanciato il mese prima, come esplode

Cambio di scena (03:00): il docente apre un secondo canale — già monetizzato all'apertura — per
mostrare la crescita "tipo" nei primi 10-11 giorni. `frame-108.png @ 3:34` mostra la tab
**Pubblico › Video che fanno crescere il tuo pubblico** — non il primo minuto del canale (il
frame cade più avanti nel racconto di quanto suggerisca il timestamp del parlato, il video salta
schermate durante il parlato continuo).

Narrazione (03:45-05:41): primo video **44 visualizzazioni**, poi le view si sommano giorno su
giorno (un video pubblicato oggi continua a fare view nei giorni successivi, sommandosi ai nuovi)
finché un video "esplode": **50.000 visualizzazioni** in un giorno dopo 6 giorni dal lancio,
poi 29.000, poi 42.000. Target dichiarato per restare "in media" una volta scalato: 400-500k,
100-150k views/giorno, equivalenti a **100-300€/giorno** a seconda della nicchia (05:04-05:17).
Costanza di pubblicazione è premiata da YouTube: i contenuti vecchi continuano a fare view mentre
i nuovi ne aprono altre (05:17-05:41).

## 05:47 — 08:23 · La tab Contenuti: impressioni, CTR giorno per giorno, e la regola "più view → CTR più basso"

Per il CTR si va sul tab **Contenuti**. `frame-202.png @ 6:42` mostra a schermo, periodo 01-11 mar
2023: **271.070 visualizzazioni**, **2,1 Mln impressioni**, **11,9% percentuale di clic delle
impressioni**, durata media 2:01 — il grafico giornaliero oscilla tra ~9% e 15,6%.
`frame-217.png @ 7:12` isola il picco: **lunedì 6 mar 2023 → 15,6%** (il giorno del contenuto
virale citato dal parlato @ 06:49-07:04). `frame-247.png @ 8:12` isola un altro giorno:
**venerdì 10 mar 2023 → 12,6%**.

Regola dichiarata a voce (06:08-06:19): **più visualizzazioni fa un video, più il CTR scende in
percentuale** — non perché il video peggiora, ma perché YouTube lo spinge a un pubblico più ampio
e meno mirato. **Confermato dallo schermo**, non solo dal parlato: `frame-262.png @ 8:42`, stesso
canale su **90 giorni**: 2,1 Mln views (stesso numero assoluto dell'11-giorni sopra, ma ora
sommato su periodo più lungo), **25,5 Mln impressioni**, CTR sceso a **7,2%**, durata media
3:18 — la crescita del volume diluisce la percentuale, esattamente come dichiarato a voce.

## 08:23 — 10:01 · La soglia: minimo 8% di CTR, sopra 10-12% "copertine da replicare"

Regola numerica esplicita (07:18-08:10): il CTR "per essere in media, per andare bene" deve
essere **almeno l'8%**; sotto (2-6%) vuol dire che copertine e titoli non funzionano, ma **non si
può giudicare dal primo video**: servono almeno 10-20-30 video pubblicati prima di trarre
conclusioni (07:41-07:56). Copertine con CTR **12-15%** sono "quelle giuste, da replicare"
(08:10-08:23). Nota di calibrazione (09:04-09:32): su **milioni** di visualizzazioni un CTR del
5,5-7% "va comunque bene" — la soglia dell'8% si applica a canali/video con **pochi** dati, non
a chi ha già scala.

## 10:01 — 11:44 · Il video virale singolo: CTR, copertura, pubblico

`frame-307.png @ 10:12` — pannello **Panoramica** del singolo video pubblicato il 15 mar 2023,
snapshot al 24 apr: **392.643 visualizzazioni**, **35.969,0 ore** di tempo di visualizzazione,
**+3.891 iscritti**, **963,70$** di entrate stimate, sorgenti di traffico: **49,9% funzioni di
navigazione**, **45,4% video consigliati**, 1,8% ricerca YouTube. `frame-322.png @ 10:42` — tab
**Copertura** dello stesso video: **6,1 Mln impressioni**, **5,4% CTR**, 392.643 views, **307.865
spettatori unici**; il grafico mostra il CTR stabilizzarsi intorno al 5,1% a 39 giorni dalla
pubblicazione — coerente col parlato (10:54-11:01: "quando ho pubblicato il video era già 9,4%",
poi si stabilizza). `frame-354.png @ 11:42` — tab **Pubblico**: **98,5%** del watch time viene da
**non iscritti**, solo 1,5% da iscritti; genere **61,5% donne, 38,5% uomini**; nuovi spettatori
4.677 contro 2.175 di ritorno.

## 11:44 — 13:12 · La sezione più operativa: "cosa guarda il nostro pubblico"

Passo dichiarato come "un'altra cosa fantastica" (12:05-12:44): dentro **Pubblico › Panoramica**,
scorrendo in basso, YouTube mostra direttamente **quali canali e quali video guarda il nostro
pubblico** — fonte diretta di nuove idee, sia per nuovi canali sia per nuovi video nella stessa
nicchia (12:44-13:04). Non catturato in un frame dedicato nel campione (schermata sotto il fold,
il docente scorre mentre parla); **solo parlato**, rischio annotato più alto.

## 13:12 — 21:12 · Le sei regole operative per il CTR (sintesi finale del docente)

Dichiarate esplicitamente come "scrivetevi bene questa informazione" (13:24):

1. **Primo minuto = il migliore**, mai un'intro del canale nei primi 60s — l'intro fa perdere
   pubblico, la gente vuole "il sodo" (13:30-14:07).
2. **Ripeti la keyword più volte all'inizio** e crea un gancio: dire cosa si scoprirà durante il
   video (14:17-14:26).
3. **Call to action nei primi minuti**: chiedere commenti mirati (non generici) — "se sei
   d'accordo commenta X" — perché i commenti pesano più dei like per l'algoritmo, ma vanno
   comunque chiesti anche i like come segnale di interazione (14:32-15:19).
4. **Copiare (non clonare) le copertine dei competitor che funzionano**, e una volta trovato un
   format che converte, **non stravolgerlo** — piccoli aggiustamenti (sfondo, dettagli), mai
   cambio radicale, per restare riconoscibili (15:28-16:20).
5. **La copertina non deve dare la soluzione**: deve creare una domanda nella mente di chi guarda
   (esempio "chi è morto", "quale programma è stato sospeso") — mai rivelare tutto, il video deve
   promettere la risposta (16:20-16:55, 18:20-18:33).
6. **Titoli e copertine "forti" ma non clickbait**: la differenza dichiarata è che il clickbait
   promette e non mantiene — chi clicca e non trova la risposta promessa smette di seguire il
   canale, e c'è rischio di demonetizzazione (19:24-20:03).

`frame-634.png` @ 21:06 e i due frame successivi sono la transizione grafica di chiusura (cerchio
viola animato), non contenuto informativo — coerenti con la chiusura standard del format.

## Confronto col nostro codice — il vero delta

Verificato leggendo il codice, non assunto dal nome dei file:

- `YOUTUBE-AUTOMATION-FACTORY/03-AGENTI-E-RUOLI/operatori/channel-performance-analyst.md` §2
  dichiara esplicitamente: *"CTR, retention e ricavi richiedono YouTube Studio, che è privato.
  Dal fetch pubblico si ricavano solo views ed età. Nei log quei campi sono `null`, e `null` è la
  risposta giusta"*.
- `apex7_orchestrator.py:1678-1685` conferma nel codice: ogni log di performance scrive
  `"ctr": None, "retention_rate": None` con un commento esplicito che dice perché ("richiedono
  YouTube Studio, non ottenibile da fetch pubblico").
- `self_improve.py` ha **già la logica pronta** per usare il CTR — righe 68 (`ctr = float(...)`),
  109-111 (soglia 4,0% = tag da scartare), 130-132 (soglia 7,0% = tag da rinforzare) — soglie
  scelte in modo indipendente ma **quasi identiche** a quelle insegnate a voce dal corso (8% =
  in media, sotto 4-6% = problema). Il motore di apprendimento è costruito e non riceve mai dati
  reali perché la fonte a monte è sempre `null`.
- `meta_agent.py:48-70` ricalibra `success_rate` di una strategia se `avg_ctr > 7.5` — stessa
  storia: soglia pronta, input sempre vuoto in produzione.
- `youtube_uploader_playwright.py` **dimostra che il login persistente su `studio.youtube.com`
  già funziona** (righe 186, 192, 260-307): apre `studio.youtube.com`, verifica se la sessione è
  loggata, usa un profilo Chrome persistente. È la stessa identica porta d'accesso che servirebbe
  per leggere Analytics — oggi usata solo per il wizard di pubblicazione, mai per leggere i tab
  Panoramica/Copertura/Pubblico che il docente usa per l'intera lezione.
- Nessuno script nella cartella `02-AUTOMAZIONI-E-SCRIPTS` legge mai
  `studio.youtube.com/video/<id>/analytics/tab-*` (grep mirato: zero occorrenze di `/analytics/`
  come path Studio, a parte `/monetization/ads` in `youtube_uploader_playwright.py:233`).

Non toccato il codice oggi (ADR-029, binario B solo a gate categoria) — regola registrata,
candidato forte per il gate A6: è il pezzo che chiuderebbe A4-RC-15/il buco già a registro.
