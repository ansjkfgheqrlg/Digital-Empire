# Report di blocco — A4/L09 · L13 · L14 · L16: le quattro lezioni del copia-incolla avanzato

> Report **unico** per quattro lezioni. Il motivo è nel §1: sono quattro lezioni che insegnano a
> lavorare su **materiale di altri**, e per la nostra fabbrica hanno lo stesso identico esito.
> Quattro report separati avrebbero quadruplicato le pagine per ripetere quattro volte la stessa
> conclusione.
>
> Appunti separati per lezione: `L09-18-tecniche-avanzate/`, `L13-final-cut-gratis/`,
> `L14-final-cut-avanzato/`, `L16-ai-musica-separazione/`.
> Rapporti grezzi degli scagnozzi: [`RAPPORTI-GREZZI-L09-L13-L14-L16.md`](RAPPORTI-GREZZI-L09-L13-L14-L16.md).

---

## 1. Cosa insegnano, e perché le ho declassate

| lezione | durata | parole | contenuto |
|---|---|---|---|
| **L09** «18 Tecniche Avanzate del Metodo Copia e Incolla» | ~18 min | 3.167 | manovre in Premiere su clip altrui |
| **L13** «Come avere Final Cut Pro X Gratis per Sempre» | ~8 min | 1.368 | prova ufficiale + aggiramento della licenza |
| **L14** «Final Cut: Metodo Copia & Incolla Avanzato» | ~50 min | 9.013 | il metodo copia-incolla dal vivo, dall'inizio alla fine |
| **L16** «A.I. per canali di Musica: separare voce da audio» | ~7 min | 951 | *source separation* di brani altrui come nicchia |
| | **~83 min** | **14.499** | |

**Profondità dichiarata: BRONZO** (piano §10), stesso criterio già usato per L07/L08/L10. La
categoria A4 è ORO, ma il piano prevede il declassamento **dichiarato** quando la materia non si
trasferisce — e qui non si trasferisce per **due** ragioni strutturali, non per pigrizia:

1. **La nostra fabbrica genera via API e non apre mai un editor video.** Dove si clicca in Premiere
   o in Final Cut non ci riguarderà mai.
2. **E soprattutto: non partiamo mai da materiale altrui.** Tutte e quattro le lezioni hanno lo
   stesso presupposto — c'è un video (o un brano) di qualcun altro, e il lavoro consiste nel
   renderlo utilizzabile. Tolto quel presupposto, non resta procedura.

**Cosa ho fatto lo stesso:** ho fatto leggere **il parlato integrale di tutte e quattro** (14.499
parole), perché dentro un tutorial può nascondersi del metodo — ed è successo, in L14. **Nessun
frame estratto:** le schermate dei pannelli di un editor sono esattamente la parte che non serve.

**Come le ho lette, dichiarato** (dottrina §6.13): tutte e quattro affidate a **scagnozzi** (agenti
sonnet) con mandato preciso — estrarre solo ciò che si trasferisce a una fabbrica che genera via
API, e **dire chiaramente quando non c'è nulla**. Su L09 e L16 il rapporto è tornato con quella
conclusione, e l'ho tenuta. Il lavoro di **lavorazione** (appunti, regole, innesti, arbitrato) è
mio.

## 2. Cosa facciamo oggi

Niente di ciò che queste lezioni insegnano, e il confronto non è nemmeno «loro così, noi cosà».

`fliki_client.py` manda un payload e riceve un MP4: non esiste una timeline, non esistono clip da
capovolgere, non esiste un file altrui da cui partire. Le immagini nascono dal nostro testo, la
voce è sintetica e nostra, la musica — se c'è — è quella che Fliki ci fornisce con la sua licenza
(`A4-L19-01`). **Il problema che queste quattro lezioni risolvono, noi non ce l'abbiamo.**

Sul lato strumenti, il criterio di scelta (`scelta-strumenti.md`) faceva quattro domande —
storico, piano B, costo, comandabilità — e **nessuna sul titolo d'uso**. È il buco che L13 ha reso
visibile.

## 3. Delta

Su 83 minuti, **cinque cose**. Tre sono principi, due sono buchi trovati in casa nostra.

**a) I primi 30 secondi sono ritenzione, non solo clic.** (L14, 09:36 e 11:35)
Il capovolgimento più utile del blocco. La fabbrica cura esplicitamente il **clic** — titolo,
copertina, `title-writer`, `thumbnail-designer` — e non aveva **una riga** su cosa succede nei
primi trenta secondi, che è dove si decide se chi ha cliccato resta. Ora `script-writer.md` §11:
apertura scritta per ultima, promessa specifica, niente preamboli, budget di ~68 parole, e la
misura è la ritenzione ai 30s in YouTube Studio.

**b) Il video deve finire chiedendo qualcosa.** (L14, 45:35 e 50:33)
Nessun documento della fabbrica diceva **come finisce** uno script. Ora `script-writer.md` §12:
una sola CTA, motivata, ruotata dal ventaglio del §10, distinta dall'outro del canale (che invece
è firma stabile).

**c) Il costo vero del metodo: ~1 ora a video, non 5 minuti.** (L14, 25:23)
Vedi §4: è un conflitto interno al corso, ed è il dato che rende finalmente numerica la terza
ragione della porta chiusa del §4 di `monetizzazione-compliance.md`.

**d) Il criterio di scelta degli strumenti non chiedeva la licenza.** (L13)
Buco nostro, trovato guardando la manovra altrui. Ora la **quinta domanda**: *con che titolo lo
stiamo usando?*, con tre risposte ammesse e una vietata.

**e) Un canale di successo non è una prova.** (L16, 03:55)
`niche-scout.md` misurava i numeri di un canale esemplare e **non chiedeva mai su cosa si
reggessero**. Ora §9: due domande obbligatorie — liceità della pratica e riproducibilità da parte
nostra — e l'esempio entra nel dossier come candidato, mai come verdetto.

**Quello che NON prendo:** tutte le manovre di editing (zoom, keyframe, LUT, chroma key, MOGRT,
reverse, slow motion), l'aggiramento della licenza, la separazione audio di brani altrui, la
nicchia «canali di musica» così com'è proposta, e i prezzi delle licenze citati.

## 4. Conflitti col nostro modo di fare

**Un conflitto nuovo, e non è fra noi e il corso: è del corso con sé stesso.**

**`C-006` — il tempo che costa il metodo.** L05 lo vende come «~5 minuti a video»; L14 lo mostra
dal vivo e dichiara **~1 ora a video** dopo la pratica [25:23]. **Fattore 12×, stesso corso,
nessuna delle due lezioni segnala l'altra.**

Arbitrato: **vince L14**, per una ragione di metodo prima che di merito — *il costo di un metodo si
prende dalla lezione che lo esegue davanti alla telecamera, non da quella che lo annuncia.* È il
secondo caso di autocontraddizione del corso dopo `C-005` (la freschezza del video sorgente), e i
due insieme dicono qualcosa **sulla fonte**: le lezioni-vetrina e le lezioni-dimostrazione danno
numeri diversi, sistematicamente a favore della vetrina.

Non cambia nessuna nostra decisione (la porta era già chiusa per ragioni di diritto, `C-004`), ma
**arma di un numero** l'argomento più debole di quella porta.

### I miti del camuffamento passano da quattro a sei

I due nuovi vengono entrambi da **L14**, e sono i più istruttivi dei sei:

| # | Il mito | Dove | Perché conta |
|---|---|---|---|
| 5 | «Sono **4 secondi** di video… siamo dentro il fair use, andate super tranquilli» | L14 · 20:51 | È la stessa soglia inesistente del mito 3, **con un numero diverso**: L10 diceva 5 secondi. Che la cifra cambi da una lezione all'altra è la prova che nessuno l'ha letta da nessuna parte |
| 6 | «Il canale che usa quella clip non l'ha creata lui, quindi **il fair use decade**… noi siamo a posto» | L14 · 19:50 | Il più contorto dei sei: confonde **chi può agire** con **se l'uso sia lecito**, e trasforma una **difficoltà di prova** in una **licenza** |

**E accanto ai miti, ora c'è il catalogo delle manovre** (`monetizzazione-compliance.md` §6, da
L09): dodici tecniche con lo scopo reale di ciascuna. Le frasi (§5) sono la giustificazione; le
manovre (§6) sono ciò che quella giustificazione copre. Due di esse — **flip a specchio** e
**distorsione** — non migliorano il video di un fotogramma: esistono solo per ingannare un sistema
di riconoscimento, e sono la dimostrazione più pulita della regola di casa.

**Due porte chiuse nuove**, scritte perché siano già pronte quando qualcuno le proporrà:
- **l'aggiramento di licenza** (L13) → `scelta-strumenti.md`, quinta domanda;
- **la separazione audio di brani altrui** (L16) → `monetizzazione-compliance.md` §7.

## 5. Regole estratte

Nove, in quattro file del registro.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L09-01` | Le manovre di camuffamento sono **elusione**, non lavorazione: catalogo delle dodici | `monetizzazione-compliance.md` | **A** |
| `A4-L13-01` | Uno strumento entra solo per la **porta d'ingresso**: quinta domanda del criterio | `scelta-strumenti.md` | **A** |
| `A4-L14-01` | I primi 30 secondi sono **ritenzione**, non solo CTR | `script-writer.md` | **A** |
| `A4-L14-02` | Il video finisce con **una** CTA, motivata e ruotata | `script-writer.md` | **A** |
| `A4-L14-03` | Nessuna soglia di durata: «4 secondi» *(mito 5)* | `monetizzazione-compliance.md` | **A** |
| `A4-L14-04` | «Il fair use decade perché la clip non è loro» è falso su due piani *(mito 6)* | `monetizzazione-compliance.md` | **A** |
| `A4-L14-05` | Il metodo costa **~1 ora a video**, non 5 minuti | `monetizzazione-compliance.md` | **A** |
| `A4-L16-01` | La **separazione audio** di brani altrui non entra: si separa ciò di cui si hanno i diritti | `monetizzazione-compliance.md` | **A** |
| `A4-L16-02` | Un canale di successo **non è una prova**: liceità e riproducibilità, sempre | `niche-scout.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e nove applicate subito** (binario A). Nessuna riga del motore toccata.
- **Nessuna regola di binario B**: queste lezioni non toccano il motore, perché non toccano nulla
  di ciò che facciamo.
- **Registro dopo il blocco: 47 regole, tutte a norma, 44 applicate**, 3 in attesa del gate A4
  (`A4-L01-03`, `A4-L03-02`, `A4-L04-02` — tutte binario B, tutte sul motore).

**Valore netto del blocco: medio, e concentrato in una lezione sola.** L09 e L16 non portano un
solo metodo (e l'ho scritto senza addolcirlo); L13 non porta nulla di suo ma fa vedere un buco
nostro. **L14 da sola vale il blocco**: due principi di script che la fabbrica non aveva, due miti,
e il numero che smonta la promessa della lezione madre.

**La lezione di metodo, di nuovo:** come per L06-L10, il raccolto migliore non è dentro una lezione
— è **fra le lezioni**. I due miti nuovi valgono perché stanno accanto ai quattro vecchi (e il
quinto contraddice il terzo); il numero di L14 vale perché sta accanto alla promessa di L05.
**Leggere tutto, in ordine, e tenere il registro: è il metodo che produce, non la singola lezione.**
