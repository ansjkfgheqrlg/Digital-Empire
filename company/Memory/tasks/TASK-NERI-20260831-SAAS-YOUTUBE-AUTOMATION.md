# TASK-NERI-20260831 — PACCHETTO SAAS "YOUTUBE AUTOMATION"

> **Destinatario:** NERI · **Ruolo:** Designer & Web (siti, loghi, asset social)
> **Committente:** Maximilian (Max) · **Affiancamento:** Emperator Agent
> **Emessa:** 2026-08-31 · **Stato:** APERTA
> **Governo:** ADR-002 (memory-first) · ADR-005 (i blocchi minori non fermano il lavoro) · ADR-006 (ciclo a 9 passi)

---

## PRIMA DI TUTTO — leggi questa mezza pagina, Neri

Ciao Neri. Sono **Emperator**, l'assistente di Max. Questa task è il tuo lavoro delle
prossime settimane, e la leggiamo insieme.

**Tre cose, e sono le più importanti di tutto il documento.**

**1. Non devi costruire tu i siti a mano.** Li costruisco io. Tu mi dai la direzione (cosa
deve dire la pagina, a chi parla, cosa deve far fare a chi la legge) e io scrivo il codice.
Tu sei il regista, non il muratore.

**2. Il tuo lavoro vero è il CONTESTO.** Il contesto è tutto quello che io devo sapere per
non indovinare: a chi parliamo, cosa vendiamo, che problema risolve, che tono usare, quali
esempi guardare. **Più contesto mi dai, migliore esce il lavoro. Sempre. Senza eccezioni.**

Quando mi darai un ordine con poco contesto io **mi fermo e te lo chiedo**. Non è per farti
perdere tempo: è perché Max non tollera un solo tipo di errore, ed è l'errore di pigrizia —
quando sappiamo cosa servirebbe e non lo facciamo perché è una scocciatura. Non dare il
contesto è esattamente quello. Meglio dieci minuti in più a spiegarmi la cosa, che un sito
rifatto tre volte.

**3. Non devi sapere tutto.** Non devi sapere cos'è una skill, quando serve un workflow,
cosa conviene automatizzare. **Quelle scelte le facciamo insieme:** tu mi dici cosa vuoi
ottenere, io ti dico le opzioni, quale sceglierei e perché. La volta dopo lo saprai fare da
solo. Se ti blocchi, scrivimi. Se ti blocchi due volte sulla stessa cosa, scrivimi lo
stesso: non è una figuraccia, è come si impara.

---

## COS'È IL PRODOTTO — il contesto che ti serve per lavorare

Stiamo costruendo il **primo SaaS di Digital Empire**.

*SaaS* si legge "sass" e vuol dire **software ad abbonamento**: una piattaforma online a cui
il cliente si iscrive e **paga ogni mese** finché la usa. Non la compra una volta: la
affitta. Questo cambia il modo di vendere, e te lo spiego subito perché ti serve per il
design.

**Come si chiama, per ora:** YouTube Automation *(nome definitivo: lo decide Max)*.

**Cosa fa:** è una piattaforma dove dentro c'è **tutto il flusso della YouTube Automation
già montato e collegato**. L'utente entra, e la piattaforma gli fa i video per il suo canale
YouTube dall'inizio alla fine. Non gli dà un pezzo: gli dà la fabbrica intera.

**A chi lo vendiamo:** a chi vuole **guadagnare** con un canale YouTube senza metterci la
faccia e senza montare i video a mano.

**La promessa in una frase:** *non ti diamo un attrezzo, ti diamo la fabbrica già accesa.*

**Perché ti serve saperlo per il design:** su un prodotto ad abbonamento la persona non
compra un oggetto, compra **la fiducia che tra sei mesi funzionerà ancora**. Quindi il sito
deve trasmettere solidità: niente aria da promessa facile, molto "questa cosa è seria e
resta". È il motivo per cui i siti CCM sono il nostro riferimento — pesano.

---

## GLI ARNESI — cosa userai (te li spiego, non li devi cercare)

### La skill dello stile: `empire-premium-style`

Una *skill* è un manuale che io so già a memoria: dentro ci sono le regole esatte per
costruire una cosa. `empire-premium-style` è il manuale del nostro stile: i colori, i
caratteri, la grana sullo sfondo, come sono fatte le schede, i bottoni, le animazioni.

**Cosa vuol dire per te:** non devi decidere tu i colori o i caratteri. Sono già decisi e
sono giusti. Tu decidi **cosa dice la pagina e in che ordine**. Lo stile arriva da solo.

**Come si accende:** io scrivo `/empire-style` seguito dalla cartella. Non lo devi fare tu.

### I riferimenti da guardare — aprili DAVVERO prima di iniziare

Sono i siti già fatti, quelli che Max considera venuti benissimo:

| Dove | Cos'è |
|---|---|
| `Lancio corso skill beast/Leanding Page CCM/ccm-premium` | **Il riferimento principale.** Guarda questo per primo. |
| `Crea siti/Siti CCM/ccm-sale-page-empire` | Com'è fatta una pagina di vendita nostra |
| `Crea siti/Siti CCM/ccm-full-empire` | Sito completo, più sezioni |
| `Crea siti/Siti CCM/ccm-elite-ultimate` | Versione più spinta |
| `Crea siti/Siti CCM/ccm-webinar` | Pagina che porta a un evento |

**Come si guardano** — te lo spiego perché è il tipo di cosa che non è ovvia: chiedimi
*"Emperator, aprimi ccm-premium"* e te lo faccio vedere funzionante nel browser. Non provare
ad aprire i file da solo: sono pezzi di codice, da fuori non si capisce niente. Vederli vivi
ti serve a **rubare la struttura** — quante sezioni, cosa viene prima, dove sta il bottone.

---

## IL LAVORO — 6 blocchi, in quest'ordine

L'ordine non è un capriccio. Ogni blocco usa quello prima.

---

### BLOCCO 0 — MI INSTALLI SUL TUO COMPUTER *(priorità 1 — blocca tutto)*

**Perché è il primo:** senza questo, tutto il resto non può partire, e soprattutto il tuo
lavoro non arriva a Max. Ho controllato: **nel progetto condiviso non è mai entrato niente
di tuo.** Non è un'accusa — è un sintomo, e va risolto oggi.

**Cosa succede:** ti preparo una guida tua, `SETUP-NERI.md`, passo per passo, un'azione per
riga, con scritto **cosa devi vedere sullo schermo** dopo ogni passo per sapere che è andata.

**I 3 dati sono arrivati (Max, 2026-08-31):** Windows · account fornito da Max (ognuno avrà
il suo a breve) · mai installato prima, quindi si parte da zero pulito — la condizione migliore.

**La guida è pronta: `SETUP-NERI.md`**, nella cartella principale del progetto. Otto passi,
scritti per chi non è tecnico, con scritto dopo ognuno cosa devi vedere sullo schermo.

**Il blocco è chiuso quando:** un tuo salvataggio arriva nel progetto e Max lo vede. Non
quando dici "fatto". Quando si vede.

---

### BLOCCO 1 — LA PAGINA DI VENDITA DEL SAAS

**Cos'è:** la pagina principale. Chi ci arriva deve capire cos'è, crederci, e abbonarsi.
È il pezzo che porta i soldi: è il più importante di tutti.

**Cosa mi devi dare** — è questo il tuo lavoro, non il codice:
- **A chi parliamo davvero.** Uno che non sa niente di YouTube? Uno che ha già un canale
  fermo? Uno che ha provato e ha mollato? Cambia ogni singola parola della pagina.
- **Il problema che gli togliamo.** Non "fa i video": *cosa smette di fare la sera alle 23*.
- **Le obiezioni.** Le tre cose che uno pensa prima di non pagare. ("Sarà l'ennesima fuffa",
  "ci vorrà comunque un sacco di tempo", "e se YouTube mi banna?")
- **Le prove.** Numeri veri, risultati veri, schermate vere. **Mai inventate.** Se non ne
  abbiamo ancora si dice a Max e si trova un altro modo — non si finge.
- **Il prezzo e com'è fatto l'abbonamento.** *(lo decide Max)*

**Come lavoriamo:** tu mi dai questa roba anche a voce, disordinata, in note sparse. Io la
ordino, ti faccio vedere la struttura della pagina sezione per sezione, tu correggi, **poi**
costruisco. Non costruisco prima che tu abbia approvato la struttura: rifare una pagina
intera costa dieci volte più che cambiare una riga di scaletta.

---

### BLOCCO 2 — LA RISORSA GRATUITA + LA SUA LANDING PAGE

**I due nomi tecnici, spiegati:**
- **Lead magnet** = la cosa gratis che regali per farti lasciare l'email. "Calamita per
  contatti". La regali perché chi la scarica ti sta già dicendo che il problema ce l'ha.
- **Landing page** = una pagina con **un obiettivo solo**. Qui l'obiettivo è: lasciare
  l'email e scaricare il regalo. Niente menu, niente distrazioni, nessun'altra strada.

**Prima va inventata la risorsa gratuita.** Ti do tre strade, ti dico quale sceglierei e
perché — poi decide Max:

1. **La guida** — "I 7 formati di canale YouTube Automation che stanno monetizzando adesso".
   Facile e veloce da fare. Ma ce ne sono mille in giro: si nota poco.
2. **Il template** — un pacchetto pronto (struttura di canale + copertine + scaletta video).
   Più faticoso da preparare. Ma chi lo scarica lo **usa**, e chi lo usa si affeziona.
3. **Il mini-strumento** — una paginetta dove metti il tuo argomento e ti sputa 10 idee di
   video con i titoli. **La mia scelta.** Costa più delle altre due, ma è l'unica che fa
   assaggiare come lavora la piattaforma: è una fetta gratis della cosa che poi vendiamo.
   Chi assaggia compra molto più di chi legge.

**Il tuo compito qui:** guardare le tre, dirmi quale ti convince e **perché**. Sbagliare non
è un problema: ragionare ad alta voce è esattamente l'esercizio.

---

### BLOCCO 3 — IL LOGO

**Cosa serve:** un logo per la piattaforma, che stia bene sia sul sito sia piccolo sulla
foto profilo dei social.

**Come ci arriviamo insieme:**
1. Mi dici **che sensazione** deve dare (tecnico? potente? amichevole? affilato?). Non serve
   che dici come si disegna: serve che dici cosa deve far sentire.
2. Ti preparo io **le indicazioni precise** da dare al generatore di immagini — quelle che
   chiamiamo *prompt*, cioè la descrizione scritta con cui si ordina un'immagine. Sono un
   mestiere a parte: te li scrivo io e ti spiego perché ogni pezzo sta lì.
3. Le guardiamo, scegliamo, sistemiamo.

**Serve in tutte queste misure** — te le scrivo perché è la cosa che ci si dimentica sempre
e poi tocca rifare tutto: versione grande, versione piccola per la foto profilo, versione
chiara e versione scura, e la sola icona senza scritta.

---

### BLOCCO 4 — GLI ASSET SOCIAL

*Asset* vuol dire semplicemente **i pezzi grafici pronti da usare**.

Servono: immagine di copertina dei profili, foto profilo, 2-3 sfondi per le storie, e i
modelli per gli annunci. Tutto con i colori e i caratteri della skill — **la stessa faccia
del sito**, non un mondo a parte. Se il social è bello ma diverso, la gente non collega le
due cose e la fiducia si spezza.

---

### BLOCCO 5 — I CAROSELLI DI ESEMPIO

*Carosello* = quel post fatto di più immagini che si scorrono di lato.

Ne servono **2-3 completi** come esempio, per far vedere che aria tira.

**Buona notizia, e la sai solo se te la dico io:** i caroselli qui **non si fanno a mano.**
Esiste già una fabbrica che funziona — un comando, gli dai l'argomento, e sputa fuori le
immagini pronte con i nostri colori. È stata costruita e collaudata il 27 agosto. Tu mi dai
gli argomenti, io la accendo.

**Questo è il tipo di cosa che ti volevo far vedere:** prima di fare a mano una cosa
ripetitiva, chiedimi sempre *"Emperator, esiste già qualcosa che lo fa?"*. Nove volte su
dieci esiste, e ti risparmia una giornata.

---

## COME SI SCRIVE UN ORDINE BUONO — il tuo esercizio vero

Questa è la parte che ti farà crescere più di tutte, Neri. Leggila due volte.

**Ordine scarso** *(mi fermo e ti chiedo il contesto):*
> "Fammi la landing page del SaaS"

Non posso: non so a chi parla, cosa regala, che tono, quale riferimento guardare. Se
provassi a indovinare uscirebbe una pagina generica — e una pagina generica non vende
niente. Ti farei perdere due giorni per farti risparmiare dieci minuti.

**Ordine buono** *(parto subito):*
> "Landing page per la risorsa gratuita del SaaS YouTube Automation.
> Parla a chi ha già provato ad aprire un canale e ha mollato dopo tre video.
> Regala il mini-strumento che sputa 10 idee di video.
> Voglio la stessa aria di ccm-premium, ma più corta: si legge in trenta secondi.
> Obiettivo unico: lasciare l'email. Niente menu, niente altri bottoni."

Vedi la differenza? Nel secondo caso non ho **niente** da indovinare.

**Lo schema, tienilo a portata di mano:**
1. **Che cosa** ti serve (pagina, logo, carosello)
2. **Per chi** è — la persona vera, con la sua situazione
3. **Cosa deve fare** chi la vede — una cosa sola
4. **Quale riferimento** guardare
5. **Cosa NON deve esserci**

Il punto 5 lo saltano tutti ed è spesso il più utile.

---

## COSA DEVE ANCORA DECIDERE MAX

*(nessuna di queste ferma il lavoro — ADR-005: si va avanti e si riempie dopo)*

- [ ] Nome definitivo della piattaforma
- [ ] Prezzo e forma dell'abbonamento
- [ ] Quale risorsa gratuita fra le tre del Blocco 2
- [ ] I 3 dati per l'installazione (Blocco 0)
- [ ] Dove vivranno i siti — cartella e indirizzo online

---

## COME SI CHIUDE OGNI BLOCCO

Un blocco è finito quando **si vede**, non quando si dice.

1. La cosa esiste davvero e si apre.
2. L'abbiamo guardata insieme.
3. Max l'ha approvata.
4. È salvata nel progetto condiviso — **quello lo faccio io**, non è un tuo pensiero.

*"L'ho fatto" non chiude niente. "Guardalo" chiude tutto.*

---

**Emperator Agent** — assistente personale di Maximilian.
Neri: per qualunque cosa, anche una domanda che ti sembra stupida, scrivimi. Le domande
stupide non esistono; esiste solo il non chiedere, e quello si paga sempre.
