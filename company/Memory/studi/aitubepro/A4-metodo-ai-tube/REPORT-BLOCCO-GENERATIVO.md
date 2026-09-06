# Report di blocco — A4/L15 · L17: gli strumenti generativi di terzi (avatar e musica)

> Report **unico** per due lezioni. Il motivo è nel §1: mostrano due strumenti diversi (un
> generatore di **avatar parlanti**, un generatore di **musica**) e per la nostra fabbrica pongono
> **lo stesso identico problema**, due volte. Due report separati avrebbero detto la stessa cosa a
> pagine alterne.
>
> Appunti per lezione: `L15-avatar-ai/`, `L17-musica-generata/`.
> Rapporti grezzi delle sentinelle: [`RAPPORTO-GREZZO-L15.md`](RAPPORTO-GREZZO-L15.md) ·
> [`RAPPORTO-GREZZO-L17.md`](RAPPORTO-GREZZO-L17.md).
> La terza lezione letta lo stesso giorno, **L20**, ha un report suo: è sul nostro strumento di
> produzione e non appartiene a questo blocco.

---

## 1. Cosa insegnano, e perché stanno insieme

| lezione | durata | strumento | cosa mostra |
|---|---|---|---|
| **L15** «Crea il tuo AVATAR con A.I» | ~14 min | avatar parlanti (verosimilmente **D-ID Studio**) | 17 passaggi per far parlare un volto |
| **L17** «Componi Musica Originale Con AI» | ~14 min | **AIVA** | 26 passaggi per generare una traccia |
| | **~28 min** | | |

**Profondità dichiarata: BRONZO** (piano §10). Lette dal parlato integrale, **zero frame**, da due
**sentinelle** (agenti sonnet) con mandato esplicito di dire «nulla» dove non c'era nulla — e su
entrambe l'hanno detto, per la parte operativa.

**Stanno insieme perché pongono lo stesso problema due volte, su due assi:**
- **l'asse tecnico** — sono strumenti che vivono solo dentro un browser;
- **l'asse dei diritti** — riguardano cosa hai davvero il diritto di fare con ciò che generi.

## 2. Cosa facciamo oggi

Non usiamo né avatar né musica. La fabbrica manda un payload a Fliki e riceve un MP4: nessuna
interfaccia, nessun volto, e — accertato lo stesso giorno — **nessuna musica** (`qa-audio-video.md`
§10). Quindi nessuna delle due lezioni descrive un pezzo di catena da confrontare: descrivono
**due tentazioni**, e il valore sta nell'averle esaminate prima che qualcuno le proponga.

## 3. Delta

**a) Una famiglia intera di strumenti non passa la domanda 4.**
Ventisei passaggi in L17, diciassette in L15: **quarantatré click, zero endpoint**. In
ventotto minuti di dimostrazione non compare mai una chiave, un payload, un formato di richiesta.
Non è un difetto degli strumenti — sono fatti per un umano davanti a uno schermo. È che per noi
**uno strumento migliore ma solo a click è uno strumento peggiore**: il suo costo vero non è
l'abbonamento, è il tempo umano che reintroduce su ogni video. Ora `scelta-strumenti.md` porta i
due casi accanto, e la domanda da fare per prima: **quale di questi si comanda da programma?**

**b) La musica ha finalmente tre vie, e una è chiusa.**
Era la domanda con cui L17 è stata mandata a leggere, dopo che L16 aveva proposto la via sporca.
La risposta c'è, e sta ora in `monetizzazione-compliance.md` §9: **(1)** la musica di Fliki, coperta
dalla sua licenza — è quella che abbiamo già in casa, ed è ciò che il campo `YouTube channel ID(s)`
difende; **(2)** musica generata, **percorribile solo se il piano pagato dichiara i diritti** e
senza brani altrui come riferimento; **(3)** voce e base separate da brani altrui, **chiusa**.

**c) Il dettaglio che nessuno dice sulla musica generata: i diritti dipendono dal piano.**
Parole della lezione: col **gratuito** «non abbiamo i diritti» [08:50]; con lo **Standard** si
monetizza «solamente su YouTube, Twitch, TikTok e Instagram» e non si rivende [08:57, 09:49]; solo
col **Pro** «siamo noi i proprietari» [09:16]. È il tipo di dettaglio che chi genera musica «gratis
per il canale» non sa di dover conoscere.

**d) Due porte chiuse sul generativo, dalla condotta mostrata in L15.**
La lezione fabbrica un **deepfake di un cantante italiano reale** che annuncia una finta notizia di
lutto [11:36-11:48], e fa parlare un personaggio **Dragon Ball** [09:08 → 10:52]. In entrambi i
casi, **nessuna parola di avvertimento**: sono presentati come esercizi tecnici. Ora
`monetizzazione-compliance.md` §8: mai volto, voce o sembianze di **persone reali**; mai
**personaggi protetti**, per quanto generati.

**e) Un vuoto che vale come un'affermazione: Content ID non è mai nominato.** In nessuna delle due
lezioni. Un contratto col fornitore dice cosa **hai il diritto** di fare; **non impedisce a un
sistema automatico di segnalarti**. Sono due piani distinti, e servono entrambi.

**Quello che NON prendo:** l'intera parte operativa di entrambe. Menu, upload, preset, note
musicali, editor interni, prezzi come istruzione (restano solo come metro di mercato).

## 4. Conflitti col nostro modo di fare

**Un arbitrato nuovo, e ancora una volta il corso litiga con sé stesso: `C-007`.**

L17 apre promettendo che si può «monetizzare questa musica **come se l'avessimo creata totalmente
noi**… anche su piattaforme esterne, perché **saremo noi i proprietari**» [00:46-01:03]. Otto
minuti dopo spiega che col gratuito **non hai diritti**, con lo Standard **solo quattro
piattaforme**, e la proprietà piena è **solo del Pro**. In mezzo, su una traccia creata col piano
**free**: «la posso rivendere e la posso utilizzare su YouTube» [08:24] — cioè esattamente ciò che
il free non consente.

**Terza autocontraddizione dello studio** (dopo C-005 sulla freschezza e C-006 sul tempo per
video), e **la prima interna a una lezione sola**. Tre casi non sono più un incidente: sono un dato
sulla fonte. La regola che ne esce vale ben oltre questo corso: ***l'apertura dice quello che
vende, il dettaglio dice quello che sa. Sul denaro, sui diritti e sul tempo si prende il dettaglio
— e quando c'è di mezzo una licenza, non si prende né l'uno né l'altro: si leggono i termini del
fornitore.***

### Perché queste due lezioni contano più di quanto sembri

I **sei miti del camuffamento** (§5) nascevano tutti dallo stesso errore: *modificare abbastanza un
video altrui crea un diritto*. Qui l'errore è **lo stesso, spostato di un passo**: *generare crea
un diritto*. Non lo crea. Genera un volto che è di qualcun altro, un personaggio che è di qualcun
altro, o una traccia i cui diritti dipendono da quanto stai pagando.

**È la stessa scuola di pensiero con uno strumento nuovo**, e per questo la contromisura è la
stessa: scriverla prima che serva.

## 5. Regole estratte

Sei, in due file del registro.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L15-01` | Mai volto, voce o sembianze di **persone reali**, né dichiarazioni mai fatte | `monetizzazione-compliance.md` | **A** |
| `A4-L15-02` | I **personaggi protetti** generati restano di chi sono: il metro è la riconoscibilità | `monetizzazione-compliance.md` | **A** |
| `A4-L15-03` | Gli **avatar parlanti** si comandano solo a click: non entrano in catena | `scelta-strumenti.md` | **A** |
| `A4-L17-01` | La musica ha **tre vie**, una chiusa; il titolo si legge sui **termini del fornitore** | `monetizzazione-compliance.md` | **A** |
| `A4-L17-02` | Nessun **brano altrui come riferimento di stile** in uno strumento generativo | `monetizzazione-compliance.md` | **A** |
| `A4-L17-03` | Prima domanda per una capacità nuova: **quale si comanda da programma?** | `scelta-strumenti.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e sei applicate subito** (binario A). Nessuna riga del motore toccata, test 11/11 verdi.
- **Nessuna regola di binario B:** queste lezioni non toccano il motore, perché descrivono
  strumenti che il motore non usa.
- **Una domanda resta aperta e non la nascondo:** se un giorno vorremo musica, **la via 2 va
  istruita davvero** — quale strumento, quale piano, e i termini letti sul contratto del fornitore.
  Oggi non serve: non abbiamo musica, e la via 1 (Fliki) è già in casa.

**Valore netto: medio, tutto in prevenzione.** Ventotto minuti che non insegnano un passaggio
utilizzabile, e che lasciano **quattro divieti scritti prima che servissero** e **una risposta** a
una domanda che ci portavamo dietro da due lezioni. In un archivio non varrebbero nulla; in un
registro di regole valgono, perché il giorno che qualcuno proporrà un avatar o una musica «presa
da lì», **la risposta è già scritta e non va improvvisata**.
