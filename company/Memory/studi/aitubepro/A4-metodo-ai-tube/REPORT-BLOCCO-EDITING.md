# Report di blocco — A4/L07 · L08 · L10: le tre lezioni sugli editor manuali

> Report **unico** per tre lezioni, invece di tre report separati. Il motivo è nel §1: le tre
> lezioni insegnano la stessa cosa (usare un editor video a mano) e per la nostra fabbrica hanno
> lo stesso valore. Tre report avrebbero triplicato le pagine senza aggiungere una riga.
>
> Appunti separati per lezione: `L07-filmora/`, `L08-premiere-mega/`, `L10-montaggio-premiere/`.

---

## 1. Cosa insegnano, e perché le ho declassate

| lezione | durata | parole | contenuto |
|---|---|---|---|
| **L07** «Editing facile con Filmora» | ~43 min | 5.843 | tutorial d'interfaccia di Wondershare Filmora |
| **L08** «Premiere Pro Mega Tutorial Completo» | **54:42** | 9.586 | tutorial d'interfaccia di Adobe Premiere Pro |
| **L10** «Montaggio Video Pro con Premiere Pro» | ~13 min | 2.000 | montaggio manuale applicato al metodo copia-incolla |
| | **~110 min** | **17.429** | |

**Profondità dichiarata: BRONZO** (piano §10, stesso criterio già usato per A5 «Smart Tube»).
La categoria A4 è ORO, ma il piano prevede il declassamento **dichiarato** quando la materia non
si trasferisce — e qui non si trasferisce per una ragione strutturale, non per pigrizia: **la
nostra fabbrica genera via API e non apre mai un editor video**. Dove si clicca in Filmora o in
Premiere non ci riguarderà mai.

**Cosa ho fatto lo stesso:** ho letto **il parlato integrale di tutte e tre** (17.429 parole),
perché dentro un tutorial di software può nascondersi del metodo. **Non ho estratto un solo
frame**: le schermate dei pannelli di un editor sono esattamente la parte che non ci serve.

**Come le ho lette, dichiarato:** L10 l'ho letta io. L07 e L08 — le due più lunghe, 15.400 parole
di interfaccia — le ho affidate a **due scagnozzi** (agenti sonnet) con un mandato preciso:
estrarre solo ciò che si trasferisce a una fabbrica che genera via API, **e dire chiaramente se
non c'è nulla**. Il rapporto su L07 è tornato con quella conclusione, e l'ho tenuta.

## 2. Cosa facciamo oggi

Nulla di ciò che queste lezioni insegnano. `fliki_client.py` manda un payload e riceve un MP4
esportato: non esiste una timeline, non esistono tagli, non esiste un rendering da sorvegliare.
**Il confronto non è "loro fanno così, noi cosà": è che il problema non si pone.**

## 3. Delta

**Il raccolto è piccolo e va detto piccolo.** Su 110 minuti, quattro cose.

**a) Non abbiamo intro né outro.** (L10, 04:01)
I nostri video cominciano e finiscono nudi. Il payload non li prevede, nessun agente li nominava.
Non è grave — è **una cosa che non c'è e che nessun documento diceva**, che è il tipo di scoperta
per cui questo studio esiste. Per ora `video-producer` deve **dichiararlo** nella spec, così è una
scelta e non una dimenticanza.

**b) La sincronia ce l'abbiamo gratis.** (L10, 05:25)
Chi monta su clip altrui insegue un problema che noi non abbiamo: il voiceover nuovo è sempre più
veloce o più lento dell'originale, e va compensato togliendo o aggiungendo clip **a mano, su ogni
video**. Le nostre immagini nascono dal nostro testo: combaciano per costruzione. **Scritto in
`video-producer.md` §10** perché i vantaggi che non si sanno di avere si barattano alla prima
scorciatoia.

**c) Gli elementi ricorrenti vanno ruotati.** (L08, ≈09:35)
Tre o quattro varianti di richiami, stacchi e chiusure, mai le stesse due video di fila. La
ripetizione identica è il segnale più forte che un canale è una catena di montaggio.

**d) Un numero per la musica: −35 dB.** (L08, 44:39)
Non applicabile oggi (nel nostro payload la musica non c'è), ma **è il metro che servirà** quando
al gate A4 accerteremo se i nostri video ne hanno una. Il dato utile non è il numero in sé: è che
**−25 dB era ancora troppo alto**, cioè che l'errore tipico è lasciarla molto più alta del dovuto.

**Quello che NON prendo:** tutto il resto. Tagli, transizioni, fotogrammi chiave, MOGRT, proxy,
Adobe Media Encoder, scorciatoie da tastiera, prezzi di licenze del 2023.

## 4. Conflitti col nostro modo di fare

**Nessun conflitto nuovo** — ma il **pattern più importante trovato finora nello studio**, e non
viene da una lezione sola: viene dall'averne lette quattro di fila.

### I quattro miti del camuffamento

Quattro lezioni consecutive contengono **quattro affermazioni diverse** su come rendere «proprio»
un video altrui. Sono tutte false, e sbagliano **nello stesso punto**.

| # | Il mito | Dove |
|---|---|---|
| 1 | Il **fair use** è una regola di YouTube che «ci permette di usare video di altre persone» | L06 · 10:36 |
| 2 | Filtri ed effetti rendono il video «**originale e non più riconoscibile**» | L07 · 24:57, 33:04 |
| 3 | Le clip protette si possono usare «**non meno di 5 secondi**» | L10 · 09:02 |
| 4 | Coprire il logo, ritagliare e tradurre il testo «**serve a evitare problemi di copyright**» | L08 · 39:56, 40:37, 48:49 |

**L'errore comune:** confondono **il non farsi riconoscere da una macchina** con **l'essere in
regola**. Il Content ID identifica; non stabilisce chi ha ragione.

Raccolti con la confutazione di ciascuno in `references/monetizzazione-compliance.md` **§5**, con
la regola di casa in una riga: *se una tecnica serve a non farsi riconoscere, quella tecnica sta
ammettendo che c'è qualcosa da riconoscere.*

**Perché è la scoperta più utile del blocco:** non ci difende (non riusiamo materiale altrui, il
problema non ci tocca). Serve a **non farci importare quei miti** — da un corso, da un video, da
un collaboratore che li dà per buoni. Se qualcuno propone una di quelle quattro cose, la risposta
è già scritta.

## 5. Regole estratte

Sette, in tre file del registro.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L07-01` | Filtri ed effetti non creano titolarità: irriconoscibile ≠ originale *(mito 2)* | `monetizzazione-compliance.md` | **A** |
| `A4-L08-01` | Gli elementi ricorrenti si tengono in un ventaglio piccolo e si **ruotano** | `script-writer.md` | **A** |
| `A4-L08-02` | La musica sta sotto la voce, e molto più sotto di quanto sembri: **−35 dB** | `qa-audio-video.md` | **A** |
| `A4-L08-03` | Coprire il logo non trasferisce i diritti *(mito 4)* | `monetizzazione-compliance.md` | **A** |
| `A4-L10-01` | Un canale ha **intro e outro** propri — noi non li abbiamo | `video-producer.md` | **A** |
| `A4-L10-02` | **Nessuna soglia di durata** rende lecita una clip protetta *(mito 3)* | `monetizzazione-compliance.md` | **A** |
| `A4-L10-03` | La **sincronia** voce/immagini è gratis nel nostro flusso, e va saputo | `video-producer.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e sette applicate subito** (binario A). Nessuna riga del motore toccata, test 11/11 verdi.
- **Nessuna regola di binario B**: queste lezioni non toccano il motore, perché non toccano nulla
  di ciò che facciamo.
- **`A4-L10-01` (intro e outro) apre una domanda vera**, non una toppa: se il canale debba avere
  una firma è una **decisione di prodotto**, non un parametro. Per ora `video-producer` deve
  dichiarare l'assenza in ogni spec; la decisione va portata a Max. Annotato in `BACKLOG.md`.

**Valore netto del blocco: basso in assoluto, ma non nullo — e la parte migliore non è nelle
lezioni, è nel confronto fra le lezioni.** Le tre prese una per una valgono poco e l'ho scritto
senza addolcirlo (L07 non porta **nulla**). Ma lette in fila con L06 hanno fatto emergere i
quattro miti, che nessuna delle quattro lezioni avrebbe mostrato da sola. **È il primo raccolto
dello studio che nasce dal metodo — leggere tutto, in ordine — e non dal contenuto.**
