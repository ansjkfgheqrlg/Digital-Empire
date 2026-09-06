# Report — A4/L20 «Aggiornamento Fliki Luglio 2024» (76 minuti)

- **Durata:** 76 min · ~12.000 parole · **la lezione più lunga della categoria A4**
- **Letta:** parlato integrale (1.227 righe, 00:00 → 76:00) da una **sentinella** (agente sonnet),
  2026-09-06, senza campionare. **Zero frame.**
- **Profondità dichiarata: BRONZO — per come è stata letta, non per quanto vale.** È l'unica
  lezione del blocco che meriterebbe ORO: parla dello strumento che usiamo in produzione. **I
  frame sulle tre funzioni candidate all'API restano assegnati al gate A4.**
- **Rapporto grezzo integrale (243 righe):** [`../RAPPORTO-GREZZO-L20.md`](../RAPPORTO-GREZZO-L20.md)

---

## 1. Cosa insegna

Una **live registrata**: il responsabile della produzione video mostra a schermo condiviso, per
settantasei minuti, l'editor Fliki funzione per funzione, partendo da un file vuoto. Poca teoria,
poca vendita, molti errori corretti in diretta. Le novità di prodotto occupano i due terzi centrali
(03:38 → 59:18); in coda un blocco di domande dal vivo che vale quanto la lezione.

**Vale più di qualunque tutorial di editor altrui per una ragione sola: Fliki è il nostro motore.**
Tutto ciò che riguarda Premiere o Final Cut non ci tocca; qui ogni riga può toccare il payload.

## 2. Cosa facciamo oggi

`fliki_client.py:252` costruisce un payload con `voiceId`, `aspectRatio` (fisso `"16:9"`),
`subtitlePresetId` e i visual, e riceve un MP4 esportato. **Nessuna scena si compone a mano,
nessun layer si posiziona, nessuna traccia si aggiunge.** Buona parte di ciò che la lezione mostra
— trascinare media, sfocature, contorni del testo, contagocce, transizioni, opacità — è
**editor-only**: non esiste nel nostro mondo, e va detto per non gonfiare il raccolto.

## 3. Delta

**a) ⭐ La domanda sulla musica ha una risposta, e la risposta è NO.**
Era aperta dal 2026-09-05 (`A4-L04-04`) e sembrava richiedere un ascolto. Non è servito: la
lezione mostra che **in Fliki la musica non è automatica** — è una traccia a sé (`Background
Audio`) da scegliere e poi propagare con `Apply to all scenes`, altrimenti resta perfino solo
sulla prima scena [03:57-05:26, 07:48-08:10]. Messo accanto al fatto che **nel nostro payload non
esiste un campo musica**, non resta una terza possibilità: **i nostri video hanno voce e basta.**
Conseguenza operativa in `qa-audio-video.md` §10: il criterio «Bilanciamento Volumi» non è più
*sospeso*, è **inapplicabile**.

**b) Il volume della musica: tre cifre che non si contraddicono.**
10% era il **default visto a schermo** in L19; qui il relatore dà **15% come massimo** e **5% come
tipico** [07:13-07:48], con la condizione che conta più dei numeri: dipende da traccia, narratore e
volume del narratore. La banda vera è **5-15%**, e la nostra vecchia prescrizione «10-15%» aveva
**il pavimento troppo alto**.

**c) Le pronunce: confermate, e peggio di come credevamo.**
Sapevamo che la mappa vale «per questo video». Ora sappiamo **come si propaga**: solo **duplicando
un file-modello** che le contiene già [40:54-41:24], e correggere sul file di lavoro **non basta**
— va incollata anche sul demo [Q&A, 71:52-73:41]. **La nostra catena non duplica nulla:** crea ogni
video da zero. Quindi nei nostri video una correzione di pronuncia **non si applica mai**, nemmeno
per eredità. La via del testo non è un ripiego: è l'unica.

**d) Un secondo tetto che nessuno conosceva: 50 scene per file** sul piano base [66:59-67:23], con
l'aggiramento mostrato (impacchettare testo in una scena e frazionarlo col B-roll: **40 immagini in
una scena sola**). È un vincolo di forma, non di durata, e vive accanto al plafond di minuti.

**e) Fliki genera effetti sonori da un prompt testuale** (`Add Layer → Audio → Generate`) e li
sincronizza al secondo col pannello `Timing` [44:53-46:56]. È la novità con più probabilità di
esistere anche via API. **Con un vuoto:** delle tracce musicali dice che sono «tutte licenziate»,
**degli SFX generati non dice nulla**.

**f) La difesa dai reclami, nell'ordine sbagliato.** Il corso insegna un **«trafiletto»** da
incollare nella disputa, fornito dalla **community del corso, non da Fliki** [06:20-06:48]. E in
settantasei minuti sullo strumento **non nomina mai il campo `YouTube channel ID(s)`**, che è la
difesa **nativa** per lo stesso problema. Insegnano cosa fare **dopo** il reclamo e ignorano cosa
fare **prima**.

**Quello che NON prendo:** riposizionamento drag, background blur, angoli arrotondati, allineamento
libero dei sottotitoli, effetti Fill/Text Color/Stroke, contagocce, zoom, animazioni di scena,
waveform, transizioni, opacità fra media, editor multimediale (30 MB), generatore di miniature
(**la copertina la fa Max, sempre**). Tutta post-produzione a mano.

## 4. Conflitti col nostro modo di fare

**Nessun conflitto nuovo, ed è di per sé un risultato:** questa lezione **conferma senza smentire**
i tre vincoli che avevamo trovato da altre fonti — 16:9 fisso (**Shorts, TikTok e 9:16 non sono
nominati una sola volta in 76 minuti**), musica non automatica, pronunce legate al file.

Due incoerenze interne al parlato, riportate e non normalizzate: **8 contro 2 minuti** di durata
consigliata [08:59 / 09:17] e **mille contro 10.000 caratteri** per scena [65:29 / 67:41]. Non
sono arbitrati: sono numeri da **misurare**, non da credere.

## 5. Regole estratte

Sei, tutte binario A.

| id | regola in una riga | tocca |
|---|---|---|
| `A4-L20-01` | **I nostri video non hanno musica**: il criterio del gate è *inapplicabile*, non sospeso | `qa-audio-video.md` |
| `A4-L20-02` | Volume musica **5-15%**, tipico in basso, e si regola ascoltando | `fliki-avanzato.md` |
| `A4-L20-03` | Le pronunce si propagano **solo duplicando un file-modello** → da noi mai | `lessico-pronuncia.md` |
| `A4-L20-04` | Secondo tetto del piano base: **50 scene** per file | `fliki-produzione.md` |
| `A4-L20-05` | Fliki **genera SFX da prompt** — e sulla loro licenza non dice nulla | `fliki-avanzato.md` |
| `A4-L20-06` | La difesa dai reclami si gioca **prima** (ID canale), non dopo (trafiletto) | `fliki-produzione.md` |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e sei applicate subito** (binario A). Nessuna riga del motore toccata.
- **Registro: 59 regole, tutte a norma, 56 applicate**, 3 in attesa del gate (tutte binario B).
- **Una verifica del gate A4 si CHIUDE oggi** (`A4-L04-04`, la musica). Ne restano due — il tempo
  per video (`A4-L05-04`) e il campo `YouTube channel ID(s)` da compilare (`A4-L19-01`).
- **Tre verifiche nuove, assegnate al gate A4**, tutte contro il payload reale:
  1. la **generazione SFX** esiste via API?
  2. il **timing per-media in secondi** (layer con inizio/fine, media sovrapposti dentro una scena)
     è supportato dal nostro payload, o siamo a una scena = un media?
  3. il tetto di **50 scene** vale anche per i file creati via API, o è un conteggio dell'editor?

**Valore netto: il più alto del blocco, e il migliore arriva da dove non lo cercavo.** La lezione
prometteva novità di prodotto; la cosa che ha spostato davvero qualcosa è stata **chiudere una
domanda vecchia di due giorni** su una cosa che il gate controllava senza che esistesse.
