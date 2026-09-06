# Report di blocco — A4/L11 · L12 · L18: le tre che erano date per perse

> Report **unico** per le tre lezioni rimaste bloccate due giorni in `1-fallito` con la diagnosi
> sbagliata «HTTP 403, gettone scaduto». Stanno insieme per come sono arrivate, non per il tema:
> sono l'ultimo terzo della categoria A4, quello che nessuno avrebbe letto se non si fosse
> riaperta l'ingestione.
>
> Appunti per lezione: `L11-premiere-sensei/`, `L12-sottotitoli-automatici/`,
> `L18-voice-over-audacity/`. Rapporti grezzi: `RAPPORTO-GREZZO-L11.md`, `-L12.md`, `-L18.md`.

---

## 1. Cosa insegnano, e perché le ho declassate

| lezione | durata misurata | contenuto |
|---|---|---|
| **L11** «Intelligenza Artificiale con Premiere Pro (SENSEI)» | **22:37** | quattro funzioni AI dentro un editor |
| **L12** «Video Virali con sottotitoli automatici in 2 minuti» | **9:00** | trascrizione automatica di Premiere |
| **L18** «Registrare Voice Over con Audacity» | **16:37** | registrare la propria voce col microfono |
| | **~48 min** | |

**Profondità dichiarata: BRONZO** (piano §10). Lette dal parlato integrale da tre **sentinelle**
in parallelo, **zero frame**: sono tre tutorial d'interfaccia, e le schermate dei pannelli sono
esattamente la parte che non serve.

**Perché erano bloccate, e cosa è costato scoprirlo.** Il 2026-09-05 erano finite in `1-fallito`
e la causa era stata scritta a memoria: «403, gettone scaduto». **Era falso.** Il gettone era
valido: **mancavano le intestazioni** verso il CDN, che rifiuta chi non si presenta come il
lettore della pagina. Due guasti in fila — `ffprobe` non misurava i flussi e faceva rinunciare la
scelta, `yt-dlp` prendeva 403 sul manifesto — entrambi riparati il 2026-09-06. Le tre lezioni sono
arrivate a casa **con le durate esatte** (1357/1357, 540/540, 997/997).

> **La lezione di metodo, che vale più delle tre lezioni:** *un messaggio d'errore copiato in una
> nota non è una diagnosi. E una diagnosi non verificata invecchia peggio di nessuna diagnosi* —
> perché nessuno riapre un caso che sembra già spiegato.

## 2. Cosa facciamo oggi

Niente di ciò che insegnano. Non apriamo un editor (L11, L12), non registriamo voce umana (L18).
I nostri sottotitoli sono un `subtitlePresetId` più `highlightSubtitles`, la voce è sintetica con
`voice_id` fisso per canale, il formato è dichiarato dal canale.

## 3. Delta

Su 48 minuti, **tre cose**. Va detto piccolo perché è piccolo.

**a) Un vantaggio nostro, finalmente scritto** (L11, 06:55-11:06). Il **riquadro automatico** di
Premiere esiste perché, quando una sequenza orizzontale diventa verticale, il soggetto esce
dall'inquadratura e va inseguito clip per clip. **Noi generiamo già nel formato di destinazione**,
quindi il problema non si pone. È il terzo vantaggio strutturale emerso dallo studio — dopo la
sincronia gratis e le immagini che nascono dal nostro testo — e come gli altri due valeva la pena
scriverlo prima che qualcuno lo barattasse. Ora in `video-producer.md` §12.

**b) Il settimo mito del camuffamento** (L12, 08:36). «*Basterà incollare la voce, o artificiale o
la vostra, per creare video con sottotitoli, **così che diventano video originali, unici** e che
possono senza alcun problema diventare virali.*» È il più insidioso dei sette perché **il lavoro
fatto è vero**: voce nuova e sottotitoli costano tempo. Ma sono uno **strato sopra**; l'opera
sotto resta di chi è, e il lavoro vero su materiale altrui produce un'**opera derivata**, non un
titolo.

**c) La misura di un gate** (L18, 15:38). «*Non è tanto il fatto di massimizzare la qualità
dell'audio… l'audio fa la differenza nel caso in cui è **scadente**.*» Un gate difende una
**soglia**, non un ideale — ed è arrivata proprio al gate che per mesi ha bocciato video sul
volume di una musica che non esiste. Ora in `qa-audio-video.md` §11.

**Quello che NON prendo:** correzione colore automatica, remix della traccia musicale (risolve un
problema che non abbiamo: musica non ne abbiamo), rilevamento dei tagli di scena (presuppone di
partire da un video altrui: è il metodo copia-incolla con un nome tecnico), tutta la registrazione
con microfono, tutto Audacity, i prezzi dei microfoni.

## 4. Conflitti col nostro modo di fare

**Nessun arbitrato nuovo.** Ma due osservazioni che rafforzano quelli aperti:

**La stessa persona reale, due volte.** A **L12, 01:36** compare l'immagine di **Roberto
Vecchioni** come materiale di montaggio; è la stessa persona a cui **L15, 11:36** fa annunciare
una finta notizia di lutto con un avatar. Due lezioni diverse, la stessa persona vera, e in
nessuna delle due la parola «copyright» o «consenso» viene pronunciata. Non è un incidente: è un
modo di lavorare, e per questo `monetizzazione-compliance.md` §8.1 lo registra come **pattern**.

**Il quarto scarto fra promessa e dettaglio.** Il titolo di L12 dice «in **2 minuti**»; dentro, a
06:01, il docente dice «in **2-3 minuti**». È minuscolo — e va nella stessa identica direzione dei
tre arbitrati già aperti (C-005 freschezza, C-006 tempo per video, C-007 licenza della musica):
**il numero mostrato in vetrina è sempre il più favorevole.** Quattro casi non si commentano più
uno per uno: si registra la regola generale, che è già in C-007.

**E un'assenza da segnare:** in L11 e L18 non c'è **una sola** affermazione su copyright, fair use
o monetizzazione. Prima volta nel blocco. Non è un merito: non parlano di diritti perché non
parlano di nulla che li tocchi.

## 5. Regole estratte

Tre, tutte in un file (`L11_L12_L18_ultime.py`).

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L11-01` | Il formato si **genera**, non si ritaglia: la destinazione si dichiara prima | `video-producer.md` | **A** |
| `A4-L12-01` | Voce nuova + sottotitoli **non** rendono proprio il video di un altro *(mito 7)* | `monetizzazione-compliance.md` | **A** |
| `A4-L18-01` | Un gate audio difende una **soglia**, non un ideale | `qa-audio-video.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e tre applicate subito** (binario A). Nessuna riga del motore toccata da queste tre.
- **Registro dopo il blocco: 62 regole, tutte a norma, 62 applicate, 0 in attesa.**
- Con queste tre, **la categoria A4 è completa: 21 lezioni su 21**.

**Valore netto: basso, e onestamente basso.** Quarantotto minuti per tre regole, di cui due
piccole. Ma il blocco vale per una ragione che non sta nelle lezioni: **erano date per perse**, e
la ragione per cui lo erano era una diagnosi sbagliata scritta di fretta. Se non le avessimo
riaperte, avremmo chiuso la categoria al 85,7% dicendoci che il resto era irrecuperabile — e ci
saremmo persi il settimo mito, che è il più diffuso di tutti.
