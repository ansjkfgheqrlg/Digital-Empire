# Schermate guardate — A4/L01

112 schermate estratte (1 ogni 4 s). Il rilevatore ne ha dichiarate **34 diverse** (−69,6%,
soglia 6.0). **Ne ho guardate 20**: le 11 che portano informazione fra le 34 dichiarate, più
**9 prese a campione fuori elenco** — e quelle 9 hanno scoperto un difetto del rilevatore
(sotto).

Questa è una lezione **operativa**: il valore sta nei passaggi mostrati, non nel parlato. La
trascrizione dice «vado su Down Sub» ma non dice com'è fatta la pagina, quali formati offre, né
che esiste una sezione di traduzione automatica. Quella roba sta **solo** a schermo.

| # | schermata | minuto | perché l'ho guardata | cosa ci ho trovato |
|---|---|---|---|---|
| 1 | `frame-003.png` | 0:08 | apertura | Home YouTube: si parte dal consumo, non da uno strumento |
| 2 | `frame-015.png` | 0:56 | «apriamo il piano editoriale» | Foglio Google vuoto con **la fascia di colonne colorate**: URL originale · COPY base · HASHTAG · COPERTINA · PROGRAMMAZIONE · NOTE |
| 3 | `frame-023.png` | 1:28 | il criterio di scelta del video | Ricerca «canale gossip» con **la barra laterale di vidIQ aperta** (Search Volume, Top channels, Related Queries): è lì che si legge il VPH storpiato dalla trascrizione in «buppi haca» |
| 4 | `frame-024.png` | 1:32 | identificare la sorgente | Pagina del canale **Canale Gossip** — è il canale da cui si copia |
| 5 | `frame-027.png` | 1:44 | vedere il catalogo sorgente | Griglia video: miniature tutte dello stesso stampo, testo giallo maiuscolo su fondo rosso |
| 6 | `frame-033.png` | 2:08 | idem, a schermo pieno | Conferma: **format visivo unico e ripetuto** su tutto il canale |
| 7 | `frame-041.png` | 2:40 | ritorno al piano | Foglio ancora vuoto: il lavoro inizia adesso |
| 8 | `frame-043.png` | 2:48 | come si registra la sorgente | **Link YouTube incollato nella prima colonna**, con l'anteprima della miniatura |
| 9 | `frame-048.png` | 3:08 | il primo strumento | `downsub.com`: barra + `DOWNLOAD`, e la dichiarazione dei formati **SRT, TXT, VTT** e delle piattaforme supportate (YouTube, VIU, Viki, Vlive) |
| 10 | `frame-051.png` | 3:20 | l'esito | Sottotitoli pronti: `Italian (auto-generated)` + sezione **Bilingual / Auto-translate from** |
| 11 | `frame-054.png` | 3:32 | conferma dell'esito | Stessa pagina, stato invariato: **nessuna informazione nuova** — scritto, non nascosto |
| 12 | `frame-056.png` | 3:40 | la leva della lingua | L'elenco lingue per esteso: decine di lingue tradotte in automatico dallo stesso video |
| 13 | `frame-065.png` | 4:16 | il secondo video | Torna sul canale sorgente per il secondo pezzo |
| 14 | `frame-067.png` | 4:24 | ripetizione | DownSub sul secondo link: **la procedura è identica, quindi è automatizzabile** |
| 15 | `frame-074.png` | 4:52 | il piano si riempie | Due righe con i due link + la colonna PROGRAMMAZIONE compilata («20 aprile») |
| 16 | `frame-083.png` | 5:28 | la seconda fonte | Muro dei cookie del **Corriere**: sta uscendo da YouTube per andare su una testata |
| 17 | `frame-085.png` | 5:36 | il contenuto della seconda fonte | Articolo **Corriere del Mezzogiorno** su Federico Salvatore: nomi, date, dichiarazioni della moglie — **materiale che nel transcript del video non c'è** |
| 18 | `frame-087.png` | 5:44 | dove finisce quel link | Il link dell'articolo **incollato nella colonna NOTE** del piano editoriale |
| 19 | `frame-102.png` | 6:44 | la via di riserva | **SaveSubs**: stessa meccanica di DownSub, formati SRT/VTT/TXT, riquadro «Traduci sottotitoli», e anche `SCARICA VIDEO` |
| 20 | `frame-105.png` | 7:00 | il prodotto finale | Il `.txt` aperto in Blocco note: **testo continuo senza timestamp**, pronto per essere riscritto |

## Il difetto scoperto guardando fuori elenco

Il rilevatore di scene dichiara che da **05:44 a 07:20 (96 secondi) lo schermo non cambia**.
È falso. In quella finestra ho trovato, campionando a mano:

| schermata | minuto | cosa c'era davvero |
|---|---|---|
| `frame-094.png` | 6:12 | pagina Google mentre digita «download…» |
| `frame-096.png` | 6:20 | risultati di ricerca «downloader subtitles youtube» — **i cinque siti alternativi** |
| `frame-100.png` | 6:36 | il piano editoriale con la colonna NOTE riempita |
| `frame-102.png` | 6:44 | **SaveSubs**, il secondo strumento della lezione |
| `frame-105.png` | 7:00 | il `.txt` finale aperto in Blocco note |

**Causa:** `scene_detector.py` confronta miniature in scala di grigio. Pagine web a fondo bianco
— Google, un foglio di calcolo, il Blocco note — hanno una luminosità media quasi identica: la
differenza resta sotto la soglia 6.0 anche quando la pagina è **un sito completamente diverso**.
Su uno screen-recording di tutorial, che è esattamente il materiale di questo corso, il
rilevatore salta i passaggi che contano.

Se mi fossi fidato dell'elenco, avrei chiuso questa lezione **senza il secondo strumento e senza
il prodotto finale**: quasi due minuti di lezione operativa, persi in silenzio.

**Copertura dichiarata:** parlato 1.050/1.050 parole (100%, letto per intero prima di aprire un
solo frame) · schermo **20 schermate su 112**, scelte fra le 34 dichiarate uniche più 9 campioni
fuori elenco. Le restanti sono ripetizioni delle venti qui sopra.

## Il difetto è stato riparato lo stesso giorno

`scene_detector.py` ha ora un **presidio a tempo** (`--max-gap`, default 30 s): oltre N secondi
dall'ultima schermata guardata se ne tiene una comunque, marcata `presidio`, anche se sotto
soglia. Non cura la cecità della metrica — le mette un tetto.

Rilanciato su questa lezione con `--max-gap 24`: **43 schermate invece di 34**, di cui **9 tenute
dal presidio**, e la finestra cieca di 96 secondi ora ha tre occhi dentro (`frame-093` @6:08,
`frame-099` @6:32, `frame-105` @6:56).

Il numero che condanna la metrica: fra `frame-087` (foglio di calcolo) e `frame-093` (pagina
Google) il rilevatore misura **delta 2.0** su una soglia di 6.0. Due siti completamente diversi,
per la miniatura in scala di grigi sono quasi la stessa immagine.

**Resta un limite dichiarato:** SaveSubs a 6:44 cade ancora fra due presidi. Il presidio riduce
la finestra cieca da 96 a 24 secondi, non la azzera. Chi studia una lezione operativa deve
comunque campionare a mano dentro le finestre lunghe — è così che questo difetto è saltato fuori.
