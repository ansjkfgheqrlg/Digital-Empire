# Appunti — A6/L03 · «Pubblicazione Video + cosa da fare»

- **Corso:** AI TUBE PRO · **Categoria:** YouTube Viral Mastery · **Ordine:** 3
- **Durata:** 4:04 (243s) · **id:** `0b81b294-a586-493d-bde2-081f9ea84c5b` · parlato **510 parole**
  (126 parole/minuto — sopra soglia 60, trascrizione valida)
- **Materiale:** 122 frame densi (1 ogni 2s) → **30 unici** (-75,4%), campione di 7 guardati
  (ogni pannello nuovo del wizard + le azioni post-pubblicazione, che sono il cuore della
  lezione) · **profondità ORO** (lezione breve ma densa di procedura)
- **Canale mostrato:** "Rai"/"Cronaca Notizie" — stesso video "Tragedia in Rai" già visto in
  `A6-L01` e `A6-L04`

> Lezione breve (4 minuti) ma con **due blocchi che A6-L00 non copre**: le azioni nei minuti
> subito dopo la pubblicazione (like, commento in evidenza, condivisione social) e la
> personalizzazione del canale (trailer, video in primo piano per iscritti/non iscritti). `A6-L00`
> (già chiuso) copriva solo il wizard di caricamento; questa lezione copre il **dopo**.

---

## 00:07 — 00:56 · Ultimo passo del wizard: la miniatura, poi il riepilogo

Il docente ricapitola i passi già coperti nelle lezioni precedenti (titolo, descrizione, hashtag,
playlist, tag, impostazioni) e arriva all'ultimo elemento mancante: la miniatura (00:25-00:38).
`frame-005.png @ 0:08` mostra il tab **Dettagli** del wizard con la descrizione già compilata.
Il docente carica la miniatura personalizzata e conferma (00:38-00:48): *"fate sempre quello che
vi ho detto prima"* — rimando esplicito a `A6-L02` (creazione copertina, fuori perimetro di
questo studio). Verifica monetizzazione: *"non abbiamo problemi nella monetizzazione del video,
idonea da annunci"* (00:48-00:56).

## 00:56 — 01:24 · Elementi video, playlist, visibilità, pubblica

`frame-025.png @ 0:48` — tab **Elementi video**: monetizzazione attiva, tag compilati, sezione
**Playlist** con "2 playlist" già assegnate (coerente con `A6-L01-02`, la regola "almeno due
playlist" raccomandata da YouTube). Il docente nota esplicitamente che la scheda (card) creata è
ancora "vuota" in questo momento (01:03-01:10) — un dettaglio onesto, non nascosto: non tutte le
schede vengono compilate in questa lezione. `frame-037.png @ 1:12` — tab **Visibilità**: opzioni
Privato / Non in elenco / Pubblico / Programmazione. Il docente clicca Pubblica (01:10-01:24).

## 01:24 — 02:52 · Le azioni subito dopo la pubblicazione — il cuore della lezione

Sequenza dichiarata esplicitamente come "le cose fondamentali che dobbiamo fare subito dopo aver
pubblicato un video" (01:17-01:24):

1. **Mettere like al proprio video** (01:24-01:33). `frame-045.png @ 1:28` mostra la pagina
   pubblica del video con l'animazione "like" (pollice rosso) attiva sopra il player — conferma
   visiva dell'azione appena compiuta.
2. **Lasciare un commento in evidenza (pinned)** pensato per generare risposte, non un commento
   generico (01:33-02:23): esempio dal vivo, tono adeguato al contenuto (la notizia è triste) —
   *"scrivi RIP per dare le condoglianze a Roberto Vecchioni"* con emoji 🙏. `frame-080.png @
   2:38` mostra il commento pubblicato e fissato in cima, con le prime metriche del video già
   visibili a fianco (views, engagement). Motivazione esplicita: più risposte nei commenti, più
   YouTube dà risalto al video (02:23-02:29).
3. **Mettere like al primo commento** (proprio) per rinforzarne la visibilità (02:29-02:37).
4. **Condividere il link su Facebook e Twitter** — pagine social del brand, se esistenti
   (02:37-02:52). Motivazione dichiarata: non tanto il traffico diretto, ma **segnalare a
   YouTube che il video viene condiviso esternamente**, un segnale che l'algoritmo pesa
   (02:45-02:52). Il docente rimanda esplicitamente lo scaling di questo passo ("come scalare il
   business") a un video successivo, fuori dal perimetro di questa lezione.

## 02:52 — 04:04 · Personalizzazione del canale: trailer e video in primo piano

Passo dichiarato subito dopo, "una volta ogni tanto" non per ogni video (02:57-03:02): dal
pannello **Personalizza canale**, aggiungere un **trailer del canale** (per chi non è ancora
iscritto) e un **video in primo piano per gli iscritti** — due slot distinti, pubblico diverso
(03:02-03:20). `frame-098.png @ 3:14` mostra il modale "Scegli un video specifico" nel pannello
**Personalizzazione**, con la selezione del video appena pubblicato come candidato. Il docente
nota la differenza prima/dopo: *"prima qui vedete non c'era niente, adesso si aggiorna dopo aver
pubblicato il primo video"* (03:20-03:26) — la sezione "Notizie recenti"/homepage del canale si
popola automaticamente man mano che si pubblica. `frame-106.png @ 3:30` mostra l'esito: la
homepage pubblica del canale "Cronaca Notizie" con banner, pulsante Iscriviti, conteggio iscritti,
e il video appena pubblicato in evidenza.

Chiusura (03:33-04:04): l'obiettivo dichiarato ora è la costanza — pubblicare più video al
giorno — con una nota di posizionamento del corso: *"buona costruzione di asset digitali"*.

## Confronto col nostro codice — il vero delta

- **Il wizard (miniatura, elementi video, playlist, visibilità, pubblica)** è già coperto in
  buona parte da `youtube_uploader_playwright.py` e dalle regole già registrate in `A6-L00` e
  `A6-RC-01`. Nessuna novità di rilievo su questo segmento rispetto a quanto già a registro.
- **Le azioni post-pubblicazione (like, commento in evidenza, condivisione social) non esistono
  da nessuna parte nel codice**: grep mirato su `youtube_uploader_playwright.py` per "pin",
  "like", "commento", "in evidenza" → **zero occorrenze**. Lo script pubblica il video e si
  ferma; non fa mai nulla di quello che il docente definisce "le cose fondamentali da fare
  subito dopo". Questo è un buco **diverso** da `A6-RC-01` (che riguarda i tab del wizard): qui
  il wizard è finito, il video è pubblico, e sono azioni sull'engagement post-pubblicazione.
- **Nessuna condivisione automatica su Facebook/Twitter** collegata alla pubblicazione di un
  video: le uniche occorrenze di "facebook"/"social" nella cartella `02-AUTOMAZIONI-E-SCRIPTS`
  sono in file di pianificazione editoriale (`assemble_piano_editoriale.py`,
  `generate_calendario_md.py`) o in script non-YouTube (`legamidiamore_login.py`), non in un
  passo automatico dopo l'upload.
- **La personalizzazione del canale (trailer, video in primo piano per iscritti/non iscritti)**
  non è trattata da nessuno dei tre agenti di setup canale (`ytl-channel-architect`,
  `ytl-brand-designer`, `ytl-channel-seo`) né aggiornata dopo ogni pubblicazione — oggi è un
  passo "una tantum" implicito, mai un passo ricorrente dichiarato in un playbook.

Non toccato il codice oggi (ADR-029, binario B solo a gate categoria) — regole registrate,
candidate per il gate A6.
