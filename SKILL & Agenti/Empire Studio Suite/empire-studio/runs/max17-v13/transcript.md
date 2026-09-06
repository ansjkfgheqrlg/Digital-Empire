
[00:00:00] Ed eccoci qua ancora una volta con un
[00:00:02] nuovo termine che sta diventando super
[00:00:04] virale chiamato loop Engineering.
[00:00:09] Ne stanno parlando veramente tutti.
[00:00:11] Siamo passati dal prompt Engineering al
[00:00:15] Context Engineering all'Arnest
[00:00:17] Engineering che è durato veramente poco
[00:00:19] e adesso già siamo entrati in questa
[00:00:21] nuova era dell'Open Engineering. Che
[00:00:23] cos'è? È tutto hype? È marketing? lo
[00:00:27] andremo a scoprire in questo video.
[00:00:29] Questo nuovo, diciamo, paradigma è stato
[00:00:31] lanciato da questi due personaggi qua
[00:00:35] nel mondo Tech e I che sono super
[00:00:37] famosi. Parliamo di Boris Cerni che è il
[00:00:39] creatore di Cloud Code che in una
[00:00:41] recente intervista disse queste parole
[00:00:52] dove dice che non lui non scrive più i
[00:00:54] prompt su Cloud, ma è Cloud che si
[00:00:56] scrive i prompt
[00:00:58] se stessa tramite appunto i loop che
[00:01:00] crea. Il suo compito adesso è creare
[00:01:01] loop. Anche Peter Steinberger la pensa
[00:01:05] allo stesso modo. Lui è il creatore di
[00:01:07] Open Clow, la gente ha generalista più
[00:01:09] famoso al mondo. E con questo post suo
[00:01:11] ex lui dice "Ti ricordo che tu non
[00:01:14] dovresti più fare prompting agent, non
[00:01:18] più anymore, non lo devi fare più. tu
[00:01:20] dovresti fare il design dei loop che
[00:01:23] promptano in automatico al tuo agente.
[00:01:25] Partiamo adesso dal prompt engineering e
[00:01:28] facciamo tutti gli step che ci hanno
[00:01:30] portato al loop engineering, spiegando
[00:01:33] anche perché ci serve questo nuovo modo
[00:01:36] di usare gli agenti AI. Partiamo quindi
[00:01:38] con il prompt engineering che consisteva
[00:01:41] nella scrittura
[00:01:43] del system prompt, quindi tu nel modello
[00:01:47] scrivevi qua un prompt, ok? In modo
[00:01:52] dargli in modo tale da dargli le
[00:01:53] istruzioni. Cosa ci scrivi in questo
[00:01:56] prompt? ci scrivi sei un avvocato,
[00:02:01] sei un eh front-end developer, sei un
[00:02:07] assistente personale per la customer
[00:02:09] care. Una volta settomt,
[00:02:13] ok, che può essere promptimo prompt dove
[00:02:16] gli dai le istruzioni, ad ogni domanda,
[00:02:19] ad ogni question,
[00:02:21] il modello ti risponde
[00:02:24] e la risposta te la dà in base a questo
[00:02:26] prompt che hai settato. E quindi c'era
[00:02:28] tutto questo questo prompt engineering
[00:02:31] di come si scrive il prompt nel modo
[00:02:33] migliore in cui la risposta rispecchia
[00:02:35] le istruzione che gli hai dato e abbiamo
[00:02:37] girato molto su questo setup qua di
[00:02:41] prompt engineering che ancora ad oggi si
[00:02:43] fa. Ad esempio, questo qui è il
[00:02:45] promptable
[00:02:47] 5 che è stato ottenuto tramite prompt
[00:02:50] leaking e vediamo un system prompt
[00:02:54] gigantesco che ti occupa già solo questo
[00:02:56] penso 25.000 token, ci stanno appunto
[00:02:59] istruzioni di cosa deve, cosa non deve
[00:03:01] fare, esempi di risposte giuste,
[00:03:04] risposte sbagliate, vengono descritte un
[00:03:07] sacco di cose, limitazioni, cosa appunto
[00:03:10] non deve fare, snippet di codice, beh,
[00:03:13] per essere arrivati a creare un prompt
[00:03:17] così grande hanno fatto appunto prompt
[00:03:19] engineering e non solo, perché poi sono
[00:03:22] anche loro stessi che eh dichiarano nei
[00:03:25] cookbook qual è il modo migliore di come
[00:03:28] strutturare il prompt determinati
[00:03:30] modelli. Ad esempio, questa è l'anatomia
[00:03:32] di Clode prompt, quindi il task, context
[00:03:35] files, referenze, success brief, roots,
[00:03:38] conversation plan e l'alignement. E fino
[00:03:41] a qui tutto bene, adesso entriamo nel
[00:03:43] Context Engineering. Qua è dove si è
[00:03:46] lavorato per più tempo perché qui entra
[00:03:49] in gioco la finestra di contesto, quindi
[00:03:51] ogni modello ha una finestra che è la
[00:03:54] Context Window che non è altro che la
[00:03:57] memoria che può gestire il modello,
[00:04:00] intesa come quanti token in input può
[00:04:02] leggere. Il prompt di sistema, questo
[00:04:05] qua che noi andiamo a definire
[00:04:06] effettivamente occupa una porzione di
[00:04:09] questo eh context window. Ok? Tutto il
[00:04:13] resto invece sono contesto e
[00:04:15] informazioni che possiamo ancora
[00:04:17] utilizzare. Tipicamente ad oggi i
[00:04:19] modelli di frontiera possono gestire al
[00:04:21] massimo 1 milione di token in input,
[00:04:25] quindi abbiamo tanto margine su cui
[00:04:27] lavorare, ma comunque e andremo sempre
[00:04:30] incontro al problema del riempimento di
[00:04:33] questa finestra di contesto. Comunque
[00:04:35] con il context Engineering, oltre al
[00:04:37] prompt
[00:04:39] gioco è il fatto che il large language
[00:04:42] model, il modello che sta qua, diventa
[00:04:43] un agente e quindi che può fare? Può
[00:04:47] accedere a quelle che sono le cartelle,
[00:04:50] quindi abbiamo i files,
[00:04:52] abbiamo internet, web, scrivo, e abbiamo
[00:04:57] quelle che sono le app.
[00:05:00] E quindi adesso l'agente e cioè il Large
[00:05:03] Language Model che diventa può in
[00:05:05] autonomia
[00:05:06] leggere e scrivere e chiamare delle
[00:05:10] funzioni che gli permettono di
[00:05:11] interagire con il web, con i files e con
[00:05:14] le app con le app con il protocollo MCP,
[00:05:17] ad esempio.
[00:05:20] tutte queste chiamate che vengono fatte
[00:05:22] del tipo "Voglio vedere dentro questa
[00:05:24] cartella che file ci sono" e ottenere la
[00:05:26] risposta vanno a riempire quello che è
[00:05:29] appunto il contesto del modello. Quindi
[00:05:33] la gente inizia per soddisfare le sue
[00:05:36] richieste a chiamare in concatenazione
[00:05:38] tutti questi tool che mano mano vanno a
[00:05:41] riempire il contesto. Quindi vai sul
[00:05:43] web, fammi la ricerca e ti riempie
[00:05:45] contesto. Scrivimi il report sul file
[00:05:49] locale e ti riempie contesto. Vai nel
[00:05:52] mio CRM, quindi usa l'MCP si collega
[00:05:54] all'app e questa finestra qua mano mano
[00:05:57] si va a riempire. Qual è il problema? Il
[00:06:00] problema è che uno
[00:06:02] la finestra ha delle problematiche di
[00:06:05] performance. Questa qui chiama context
[00:06:08] rot
[00:06:11] e dice che all'aumentare
[00:06:13] dei token in input
[00:06:16] degradano appunto le performance,
[00:06:18] soprattutto superate i 200.000 token,
[00:06:21] tipo qua a 200.000 token, le performance
[00:06:25] iniziano a a degradare drasticamente
[00:06:27] perché perché talmente tanto testo,
[00:06:29] talmente tanto tanti token che ha nella
[00:06:31] Context Windows che inizia a confondersi
[00:06:34] e quindi il context engineering
[00:06:37] lavora e si sforza nel cercare di
[00:06:40] mantenere questo contesto qua il più
[00:06:43] compatto possibile, cioè cerca di
[00:06:47] accorciarlo oppure quando si chiamano
[00:06:49] questi tool si cerca di ottenere delle
[00:06:51] risposte più brevi. Il context
[00:06:53] engineering lavora su tutto questo layer
[00:06:55] qua, cioè di aggiungere contesto dai
[00:06:59] file web app con dei tool che può
[00:07:01] chiamare Large Language Model, ma poi
[00:07:02] lavora tantissimo sulla pulizia e
[00:07:05] soprattutto c'è un problema quando noi
[00:07:08] facciamo dei lavori che richiedono tanti
[00:07:11] tool, quindi un lavoro che richiede eh
[00:07:15] un orizzonte temporale lungo, è
[00:07:18] inevitabile che il contesto si va a
[00:07:20] riempire, magari abbiamo bisogno di più
[00:07:22] contesto per lavorare e quindi il
[00:07:24] context engineering che fa? Prova a
[00:07:26] riassumere
[00:07:28] facendo appunto della la cosiddetta
[00:07:30] compaction prova a riassumere il
[00:07:33] contesto per cercare di liberare spazio.
[00:07:36] Quindi questo spazio adesso l'abbiamo
[00:07:37] recuperato per poter continuare a
[00:07:40] lavorare e poi che fa? Rifa nuovamente
[00:07:42] un'altra compaction e ricompatta ancora.
[00:07:45] Tutto questo approccio qua viene poi
[00:07:48] gestito in autonomia appunto dal nuovo
[00:07:51] approccio che è nato che si chiama
[00:07:53] Harness Engineering,
[00:07:57] dove invece di fare il riassunto e poi
[00:08:01] riassunto e poi riassunto che comunque
[00:08:03] perdi un sacco di performance
[00:08:05] tramite la compaction che è descritta
[00:08:07] qua nella documentazione ufficiale di
[00:08:09] Cloud,
[00:08:10] l'Arnest Engineering dice, "Aspetta un
[00:08:12] attimo, perché non facciamo tutta una
[00:08:15] struttura esterna per gestire appunto in
[00:08:19] modo efficace ed efficiente il contesto.
[00:08:22] Quindi l'arness engineering è proprio
[00:08:24] creare un'impalcatura
[00:08:26] qua esterna,
[00:08:28] quindi questo diventa un componente
[00:08:31] unico. Poi si crea un'impalcatura qua
[00:08:33] esterna
[00:08:35] dove effettivamente dato il task si
[00:08:38] strutturano una serie di step e file
[00:08:44] che ogni volta praticamente
[00:08:45] reinizializza il nostro agente e lo fa
[00:08:48] partire dal punto a cui era rimasto.
[00:08:50] Quindi continua lo step 2, poi va lo
[00:08:53] step 3, poi va lo step 4. E tipicamente
[00:08:57] questo approccio qua di Arnness
[00:08:58] Engineering si basa su dei file che
[00:09:01] vengono creati dal nostro agente in
[00:09:03] locale sul nostro IPC, dei file tipici
[00:09:06] MD, quindi markdown file, quindi il
[00:09:09] tipico cloudmd
[00:09:13] o il tipico agents.md, MD, il fatto de
[00:09:18] non lo so, lo storico, quindi il memory
[00:09:21] punmd e tutte le cartelle. Perché questo
[00:09:24] senza dover compattare il contesto ogni
[00:09:28] volta, ok? Quindi quando andiamo a
[00:09:32] saturarlo senza doverlo compattare,
[00:09:34] quello che fa la gente è scrive su dei
[00:09:37] file proprio, scrive su dei file cosa ha
[00:09:40] fatto,
[00:09:41] svuota tutta la memoria
[00:09:44] e si va a leggere il file ogni qualvolta
[00:09:46] che riparte la sessione in modo tale che
[00:09:48] ha memoria in modo persistente sui file.
[00:09:51] E da qui che è nato tutto questa tutta
[00:09:54] questa gestione dei file markdown. Ad
[00:09:56] esempio, andando a vedere OpenClow, che
[00:09:59] la gente è più famoso al mondo, se vai a
[00:10:01] cercare una documentazione come funziona
[00:10:02] la memoria di OpenClow, vedrai che ha un
[00:10:05] file che si chiama memory markdown, che
[00:10:07] è il longterm memory, durable faxs,
[00:10:09] preferences, decisions, poi c'è una
[00:10:12] cartella si chiama memory dove dentro
[00:10:14] crea dei file markdown con anno, mese e
[00:10:16] giorno che non sono altro che tutte le
[00:10:19] chat, tutto tutto quello che fai viene
[00:10:20] scritto proprio su file, quindi non si
[00:10:22] riempie il contesto perché viene
[00:10:24] flashato flusciato. lì poi ha il file
[00:10:28] che si chiama Dreams.md che è opzionale
[00:10:30] che è il Dream Diary. Poi gli puoi
[00:10:33] settare un sacco di altre memorie, ma
[00:10:35] sono tutti file. Si usa il file system
[00:10:39] come estensione della context Windows
[00:10:41] del modello e poi gli si dà al modello
[00:10:43] degli strumenti tipo memory search,
[00:10:46] memory get per poter cercare appunto in
[00:10:49] quei file e leggersi in modo dinamico
[00:10:51] quello che gli serve. Eh, la memory
[00:10:53] search viene fatta sia ehm in modo
[00:10:57] semantico, vedi, using semantic search,
[00:11:00] ma anche facendogli [schiarire la voce]
[00:11:01] leggere direttamente il file che è stato
[00:11:03] scritto sul file system.
[00:11:06] Quindi Harness Engineering è tutta
[00:11:08] questa impalcatura che viene aggiunta
[00:11:10] che struttura il task in sottotask e per
[00:11:13] ogni sottotask abbiamo tutta la finestra
[00:11:17] del contesto del modello che quindi si
[00:11:19] va a riempire, poi termina qui, allora
[00:11:22] si passa allo step 2, questa viene tutta
[00:11:25] svuotata e si passa a lavorare lo step 2
[00:11:29] e ovviamente così via fino al
[00:11:31] raggiungimento dell'obiettivo finale.
[00:11:33] Facciamo dei test così capisci meglio di
[00:11:35] che colore è fatta la Ferrari.
[00:11:37] Questa richiesta qua prevede solamente
[00:11:40] una risposta tramite prompt engineering,
[00:11:43] quindi utilizzeremo la conoscenza del
[00:11:45] modello per ottenere la risposta. Sono
[00:11:48] celebri per il rosso, nello specifico il
[00:11:50] rosso corsa. E ce lo spiega. Quindi in
[00:11:52] questo primo prompt abbiamo
[00:11:54] semplicemente fatto prompt engineering
[00:11:56] chiamando solo il modello e abbiamo
[00:11:58] ottenuto la risposta. Non abbiamo usato
[00:11:59] nessun tool. Mentre adesso se io gli
[00:12:02] chiedo come si chiama l'ultimo modello
[00:12:06] lanciato da Ferrari,
[00:12:09] facendogli questa domanda adesso lui
[00:12:12] utilizzerà degli strumenti, quindi
[00:12:14] lascia che controlli le notizie più
[00:12:16] recenti. Questo qua già è context
[00:12:18] engineering, sta chiamando dei tool per
[00:12:21] prendere contesto informazioni. Quindi
[00:12:23] in questo caso adesso questo è lo step
[00:12:26] uno, lo step 2
[00:12:28] stiamo usando anche tutti quelli che
[00:12:30] sono i tool,
[00:12:33] quindi vediamo che adesso eccolo qua la
[00:12:35] Ferrari elettrica chiamata anche luce,
[00:12:39] molto discussa e qua abbiamo le
[00:12:41] citazioni. Mentre per Arnest Engineering
[00:12:44] io dovrei dirgli clonami il sito della
[00:12:48] Ferrari
[00:12:50] così com'è.
[00:12:52] Con questa richiesta adesso, dato che il
[00:12:55] sito della Ferrari è molto complesso,
[00:12:59] è un sito che non è semplice,
[00:13:02] abbiamo bisogno di tutto quel componente
[00:13:05] per gestire appunto eh lo sviluppo e
[00:13:08] tutte le componenti che deve fare, deve
[00:13:10] copiare dal sito. Quindi adesso entra in
[00:13:13] gioco l'Arnest Engineering, quindi step
[00:13:16] 3 che ci struttura il task in sottotask
[00:13:20] che ovviamente questa richiesta è
[00:13:22] talmente grande che non entrerebbe
[00:13:24] dentro tutto tutto un milione di
[00:13:26] context, quindi va strutturata in
[00:13:28] sottotask e va gestito tutto tramite
[00:13:30] l'Arnest Engineering. E vabbè, poi qua
[00:13:32] parte Nav Baro, gamma di modelli, parte
[00:13:34] a strutturare tutto il sito. E adesso ti
[00:13:36] introduco il loop engineering, tanto
[00:13:39] parlato e discusso in questi ultimi
[00:13:41] tempi. Partiamo dal fatto che di base il
[00:13:44] large language model quando chiama i
[00:13:46] suoi strumenti e riceve le risposte,
[00:13:49] questo qua è già un loop, ok? Perché può
[00:13:52] ciclare sui suoi tool. Questo è un loop.
[00:13:55] Non solo, ma quando poi usiamo l'Arnest
[00:13:57] Engineering, quest'altro pezzo, questo
[00:13:59] qui è un altro loop perché perché
[00:14:02] cicliamo fino a quando tutti i task sono
[00:14:07] stati eh risolti. Ok, quindi questo è un
[00:14:10] loop, questo è un loop e adesso col loop
[00:14:12] engineering che facciamo? Prendiamo
[00:14:13] tutto questo e lo mettiamo dentro un
[00:14:15] altro loop,
[00:14:18] un loop su loop sul loop. Questo è il
[00:14:19] loop engineering e magari starai
[00:14:21] pensando e esagerato, tre loop uno sopra
[00:14:24] l'altro, ma c'abbiamo bisogno realmente
[00:14:27] di tutti questi loop? E in realtà il
[00:14:30] loop engineering ha senso ed è
[00:14:33] estremamente interessante come approccio
[00:14:36] perché fare loop qua sopra evita che tu
[00:14:39] ogni volta devi fare tutte queste
[00:14:41] richieste e ottenere le risposte perché
[00:14:43] è l'agente stesso che si fa le domande e
[00:14:45] le risposte. Cioè tu parti con la la
[00:14:47] prima richiesta, setti il loop e da lì
[00:14:50] in poi il modello cicla e praticamente
[00:14:53] tutto l'arness entra dentro un loop.
[00:14:55] Facciamo subito degli esempi pratici,
[00:14:57] così ti rimane fisso il concetto.
[00:14:59] Allora, esempio, creami una pagina web
[00:15:03] tipo portale dei mondiali con tutte le
[00:15:06] partite e rimaniamo un tema da appunto
[00:15:07] che ci sono i mondiali, parte del tuo
[00:15:10] Gente, Codex, Cloud Code, Antigravity e
[00:15:14] tramite appunto Ernest Engineering con
[00:15:16] tutto l'eSapp,
[00:15:19] ok? e ti crea l'applicazione che è
[00:15:21] questa qua. Ora, ad esempio, possiamo
[00:15:24] fare un loop, quindi possiamo mettere
[00:15:27] l'applicazione in un loop
[00:15:30] dove ad ogni news, a ogni novità che la
[00:15:34] gente ha e pesca va e riscrive tutto il
[00:15:37] codice dell'app, la sistema, la
[00:15:39] migliore, aggiorna il link e fa tutto.
[00:15:41] Quindi, mettendo l'app, stiamo mettendo
[00:15:43] in un loop tutto l'Arnest Engineering e,
[00:15:46] ad esempio, mantenendo così
[00:15:48] l'applicazione sempre aggiornata, senza
[00:15:49] che noi dobbiamo fare questo lavoro.
[00:15:52] Facciamo un altro esempio. Creami un'app
[00:15:55] dove ci sta un assistente i per meeting
[00:15:58] e riunioni in locale, quindi parte
[00:16:01] harness engineering e mi crea la mia
[00:16:03] applicazione.
[00:16:05] L'applicazione, mettiamo caso, l'ho
[00:16:06] fatta open source, sta tutta su Gitab,
[00:16:09] tutta bella, tutta open. Ora, ad
[00:16:11] esempio, io potrei mettere
[00:16:12] l'applicazione tramite loop Engineering,
[00:16:15] dove qualsiasi issue aprono su GitHub,
[00:16:18] cioè qualsiasi problema incontrano
[00:16:20] nell'applicazione,
[00:16:22] parte questo loop dove appunto controlla
[00:16:24] l'errore e scrive di nuovo il codice,
[00:16:27] utilizza i tool e parte di nuovo
[00:16:29] l'arnest engineering che luppa sopra
[00:16:31] questa applicazione per migliorarla.
[00:16:33] senza io dover stare a scrivere il
[00:16:35] promptisolvi
[00:16:36] questo problema, direttamente lui sta
[00:16:38] attivo, controlla quando riceve questo
[00:16:40] trigger del tipo c'è questo errore,
[00:16:43] parte e eh sistema l'applicazione.
[00:16:45] Questo approccio qua di mettere tutto
[00:16:47] dentro loop lo si può utilizzare per
[00:16:49] tantissimi casi d'uso, non solamente
[00:16:51] sulle applicazioni. Ad esempio, Andrew
[00:16:53] Garpati è stato il primo a creare una
[00:16:55] struttura del genere per la ricerca,
[00:16:58] quindi ha chiamato questo progetto Auto
[00:17:00] Resarch e alla fine è un loop
[00:17:03] engineering, cioè ha preso ha creato
[00:17:05] tutto un ARNES, l'ha messo dentro un
[00:17:07] ciclo, dentro un loop e dove
[00:17:09] praticamente fa eh una serie di
[00:17:12] esperimenti sul codice fino al
[00:17:14] raggiungimento di una condizione, fino
[00:17:16] al raggiungimento di un obiettivo.
[00:17:18] Quindi il loop è sistemato in questo
[00:17:20] modo. Lui ha fatto uno script dove ci
[00:17:23] sta il dataset, cioè si preparano i
[00:17:26] dati, uno script dove effettivamente
[00:17:29] si fa il training loop, quindi si fa
[00:17:31] l'addestramento del modello, vengono
[00:17:33] scritti i risultati dentro un file
[00:17:35] markdown e si continua così a ciclare
[00:17:38] fino al raggiungimento di una condizione
[00:17:40] eh finale del tipo voglio che mi
[00:17:42] addestri il modello e che abbia recall
[00:17:44] superiore al 90%. oppure termina eh con
[00:17:48] un un limite massimo di iterazioni o di
[00:17:51] ore che sono passate. Questo, ad
[00:17:53] esempio, è il loop engineering e la cosa
[00:17:55] bella è che sta facendo un loop sopra un
[00:17:57] harness che si porta con sé tutti i
[00:17:59] server MCP, tutte le skills, tutte tutto
[00:18:03] quel contesto e strumenti che può
[00:18:04] continuare ad utilizzare nel ciclo
[00:18:06] successivo. Quindi il loop engineering
[00:18:08] alla fine si basa su questi step.
[00:18:12] Dobbiamo avere un trigger, quindi un
[00:18:14] qualcosa che ci fa avviare il loop.
[00:18:17] Quindi nel caso di questa applicazione
[00:18:19] potrebbero essere le issue su GitHub.
[00:18:22] Nel caso di quest'altra applicazione
[00:18:24] potrebbero essere delle news che ci
[00:18:26] arrivano via mail, news che ci arrivano
[00:18:28] via chiamate PI, news in un qualsiasi
[00:18:31] modo.
[00:18:33] triggerato il loop parte l'excution,
[00:18:35] quindi qua parte l'arrest
[00:18:40] verifica che quella issue è stata
[00:18:42] risolta o che quelle news sono state
[00:18:44] implementate, c'è una parte di verifica
[00:18:46] e poi viene scritto su file cosa è stato
[00:18:49] effettuato, tipo memoria e ci si prepara
[00:18:52] per il loop successivo. loop successivo
[00:18:55] che parte quando vi è un nuovo trigger.
[00:18:57] Trigger che può essere settato
[00:18:59] manualmente del tipo "Oni giorno a
[00:19:00] quest'ora parte" oppure ad evento, cioè
[00:19:03] quando avviene un determinato evento. Il
[00:19:05] loop engineering su Cloud è veramente
[00:19:08] semplice da settare, ci sono due modi e
[00:19:10] ho preparato tutta una lezione dentro la
[00:19:12] mia accademia dove nel dettaglio mostro
[00:19:14] casi d'uso reali di loop engineering e
[00:19:17] soprattutto quando serve utilizzarlo
[00:19:19] quando no. Comunque i comandi sono sloop
[00:19:23] spazio, appunto si mette l'intervallo ed
[00:19:25] il prompt, quindi intervallo, ad
[00:19:27] esempio, ogni mattina alle 9:00 prendimi
[00:19:30] le informazioni da quella parte e
[00:19:33] aggiorna il codice, fa partire test bla
[00:19:35] bla bla, oppure loop ogni settimana
[00:19:38] oppure ogni e si mette il tempo. Mentre
[00:19:41] l'altro modo è slg. E qui possiamo
[00:19:44] mettere, ad esempio, ottimizzami tutto
[00:19:47] il codice della mia pagina web in modo
[00:19:50] tale che si possa aprire in meno di 100
[00:19:52] missecondi
[00:19:54] e poi ci si mette la sbarra dritta. Dopo
[00:19:56] la condizione sbarra dritta fai al
[00:19:59] massimo 100 tentativi
[00:20:02] o fa fai al massimo tentativi per 8 ore
[00:20:05] totali. Perché si mette quest'altra
[00:20:07] condizione? Perché mettiamo il caso che
[00:20:09] eh gli abbiamo chiesto un qualcosa di
[00:20:11] impossibile, magari non si riuscirà mai
[00:20:13] a ottimizzare la pagina web sotto ai 100
[00:20:15] misecondi. Quello che succede è che
[00:20:17] entra in un ciclo infinito e ci fa
[00:20:19] consumare tanti tanti token, quindi gli
[00:20:22] si mette la condizione è sempre un'altra
[00:20:23] condizione di terminazione.
[00:20:26] Il gol deve essere un qualcosa di ehm
[00:20:30] valutabile, ok? Io ad esempio ho detto
[00:20:32] di far caricare la pagina web sotto i
[00:20:34] 100 mseci. è un qualcosa di
[00:20:36] verificabile, cioè le hai parte,
[00:20:39] modifica il codice, poi testa
[00:20:41] effettivamente se se sta sotto i 100
[00:20:43] misecondi, se non sta allora parte con
[00:20:45] l'altro loop. Oppure gli potrei direami
[00:20:51] la migrazione
[00:20:53] di questo servizio in quell'altra parte,
[00:20:56] quindi è verificabile perché una volta
[00:20:58] che ha effettuato tutta la migrazione di
[00:21:01] tutto il pacchetto, allora sa se ha
[00:21:03] terminato o no. Oppure gli potrei dire
[00:21:07] "Effettuami
[00:21:08] gol, fammi il training su questo Large
[00:21:11] Language Model in modo tale che nel
[00:21:13] validation set raggiunga tot% di
[00:21:16] accuratezza". Ok? Poi gli mettiamo
[00:21:19] sempre l'altra condizione, al massimo
[00:21:20] fai 1000 tentativi, però sono condizioni
[00:21:23] verificabili e sulle condizioni ci
[00:21:25] dobbiamo fare molta attenzione. E questi
[00:21:28] sono i cinque livelli di verifica
[00:21:29] specifici per questa parte qua. Abbiamo
[00:21:32] la verifica deterministica del tipo
[00:21:34] realizzami questa applicazione che deve
[00:21:37] compilare senza errori, ok? Non mi deve
[00:21:39] dare errori. Questa è una cosa buleana
[00:21:42] deterministica, true false. Poi abbiamo
[00:21:44] il secondo step, regole vincoli del tipo
[00:21:48] voglio che ci metta sotto 100 misecondi
[00:21:51] o che la cura si sia sopra 90% di
[00:21:53] accuratezza o che eh mi consuma tot RAM
[00:21:59] questo programma o che il testo sia
[00:22:01] lungo al massimo 100 caratteri. Quindi
[00:22:04] sono eh regole e vincoli numerici, non
[00:22:06] buleani. Poi abbiamo la verità terrena
[00:22:10] ritardata. Questo è molto interessante
[00:22:12] perché sono cose verificabili ma che
[00:22:14] Leai non può verificare adesso ad oggi.
[00:22:18] Ad esempio, creami, gli dico slgol,
[00:22:21] creami eh un post eh prendendo le ultime
[00:22:25] news da pubblicare su LinkedIn e che sia
[00:22:29] virale, che sia virale è una condizione
[00:22:32] eh vaga, non è un qualcosa di
[00:22:34] deterministico, non è un qualcosa che ha
[00:22:37] delle regole. Quindi magari lo dovrei
[00:22:38] cambiare e dirgli fammi un post che su
[00:22:40] LinkedIn raggiunga 300 ehm
[00:22:44] reazioni, ok?
[00:22:46] Eh, e continua a migliorarti in modo
[00:22:48] tale che riaggiungo questo obiettivo.
[00:22:50] Quello che fa la gente, crea il post, lo
[00:22:52] carica, ma non ha modo di verificare
[00:22:54] direttamente che ha raggiunto queste 300
[00:22:56] reazioni, perché le reazioni magari
[00:22:58] maturano in 23 giorni e quindi in questo
[00:23:01] caso è perfetto il sloop
[00:23:04] dove gli si spiega qua l'obiettivo di
[00:23:06] ogni giorno allora tot controlla i miei
[00:23:09] ultimi post fatti su LinkedIn e migliora
[00:23:13] il tuo modo di crearmi caroselli in modo
[00:23:15] tale da raggiungere 300 eh reazioni ad
[00:23:19] ogni post.
[00:23:20] E quindi questo è un perfetto loop
[00:23:22] ritardato perché perché il risultato del
[00:23:25] post che fa adesso lo vedrà quando si
[00:23:27] parte partirà magari il loop successivo
[00:23:29] o due loop successivi. Ed è ottimo
[00:23:32] perché il mondo reale molto spesso ha
[00:23:35] dei risultati ritardati. ad esempio, che
[00:23:38] il deploy eh non abbia molti problemi,
[00:23:41] che i clienti siano soddisfatti o che
[00:23:44] l'engagement sia tot o "Otimizzami
[00:23:47] questa campagna pubblicitaria", cioè
[00:23:49] come Gol gli dice di ottimizzare la
[00:23:50] campagna pubblicitaria, ma il risultato
[00:23:52] lo vedremo tra giorni. Quindi risposte
[00:23:54] del mondo reale. Super interessante è il
[00:23:57] punto quattro, cioè usare il Large
[00:23:58] Language Model come giudice. Ad esempio,
[00:24:02] gli dico fammi il refactoring del codice
[00:24:05] eh fino a che sei soddisfatto. Quindi il
[00:24:08] fatto di essere soddisfatto significa
[00:24:10] nella fase qua di gol verifica lei
[00:24:12] stessa che assegna un valore tra 1, tra
[00:24:17] 1 e 20, tra 1 e 100 decide lui, assegna
[00:24:19] un valore e decide lei stessa se è
[00:24:22] arrivata a conclusione oppure no.
[00:24:25] Un caso d'uso interessante di LLM come
[00:24:26] giudice è quando vogliamo clonare, ad
[00:24:28] esempio, delle pagine web, delle app,
[00:24:30] quindi facciamo lo screenshot
[00:24:34] alla pagina web reale, poi gli diamo il
[00:24:38] promptina
[00:24:40] web, come prima detto "Clonami la
[00:24:42] Ferrari e lui ti farà un'app, ok? Che ci
[00:24:45] si avvicina". Però molto spesso quando
[00:24:48] gli dici che creami la pagina web della
[00:24:50] Ferrari non è che te la fa proprio
[00:24:52] uguale. E quindi qui lo mettiamo adesso
[00:24:54] dentro il loop
[00:24:56] dove l'LM fa da giudice e gli dico
[00:25:01] "Ti trovi dentro la codebase di questa
[00:25:03] applicazione qua
[00:25:05] slg
[00:25:08] migliora l'applicazione dal punto di
[00:25:11] vista della UI UX
[00:25:14] in modo tale che sia esattamente uguale
[00:25:17] a questa immagine che ti allego e gli
[00:25:19] alleghi questa immagine qua
[00:25:22] eh
[00:25:24] provaci fino a eh 80 modifiche e di ogni
[00:25:28] modifica fammi vedere il render della
[00:25:31] pagina web che hai che hai modificato. E
[00:25:33] quindi cosa fa? Entra dentro questo loop
[00:25:36] dove modifica la pagina,
[00:25:40] poi si legge di nuovo l'immagine e fa un
[00:25:43] confronto e lei si autogiudica, dice
[00:25:46] "Ok, l'immagine reale con l'immagine
[00:25:49] render della pagina web quanto so
[00:25:51] vicine?"
[00:25:52] dice, "Eh, stanno lontane 030". Ok,
[00:25:55] allora faccio altre modifiche e fa altre
[00:25:57] modifiche, altre modifiche e fa altre
[00:25:59] modifiche. Magari arriva a un punto che
[00:26:00] si autogiudica che sta a 0,90 perché
[00:26:03] vede che praticamente ha sistemato tutto
[00:26:06] leader e bottoni, ha messo gli stessi
[00:26:08] effetti, stesso font, messo esattamente
[00:26:10] le stesse cose. Dice apposta sono
[00:26:12] arrivato ed ho concluso. Il loop
[00:26:15] engineering praticamente evita che te
[00:26:18] devi intervenire ogni volta a scrivere
[00:26:20] prompt migliora questo. No, fai
[00:26:22] quell'altro. No, migliore questo. No,
[00:26:23] fai quell'altro. Gli dici direttamente
[00:26:25] il gol.
[00:26:27] È meglio ovviamente se rientriamo in
[00:26:28] questo caso qua che è verificabile, è in
[00:26:31] autonomia. Anche quest'altro più o meno
[00:26:33] ci sta perché è verificabile con delay.
[00:26:36] Mentre nel caso quattro lo fai valutare
[00:26:38] le hai e nel caso peggiore sei tu che
[00:26:40] fai la valutazione, il checkpoint umano.
[00:26:42] Sei tu che guardi ogni pagina, ogni
[00:26:45] modifica della pagina web e gli dici sì,
[00:26:47] no? o gli dai uno score per fargli
[00:26:49] capire se sta andando bene o male.
[00:26:52] Questo approccio qua funziona molto bene
[00:26:55] a loro due perché perché loro due sono
[00:26:57] degli sviluppatori,
[00:26:59] scrivono codice e quindi senza loro
[00:27:02] dover stare a babysittare quello che fa
[00:27:04] la gente definiscono in modo chiaro un
[00:27:07] loop del tipo fammi refactory di tutto
[00:27:10] questo servizio in modo tale che sia più
[00:27:12] efficiente, che la memoria occupa meno,
[00:27:14] in modo tale che i token vengono ridotti
[00:27:17] del 70% bla bla bla bla bla e gli danno
[00:27:20] un task ben definito e lo lasciano
[00:27:22] andare fino a che non raggiunge
[00:27:24] quell'obiettivo. Quindi funziona molto
[00:27:26] bene a loro perché è verificabile questo
[00:27:28] questo task. Per questo lo dicono. Io
[00:27:31] non scrivo più prompt, faccio solo loop.
[00:27:32] Ma in altri casi questo approccio qua va
[00:27:36] visto nel dettaglio perché appunto ci
[00:27:39] sono cose in cui, ad esempio, non è
[00:27:41] verificabile in automatico, non è
[00:27:43] deterministico e quindi bisogna noi fare
[00:27:46] da giudici o large language model fa da
[00:27:49] giudice oppure bisogna metterci noi
[00:27:51] avere più controllo di quello che sta
[00:27:53] accadendo. Facciamo un test reale di
[00:27:55] loop engineering. Allora, ho fatto
[00:27:57] creare uno script che fa il prodotto fra
[00:28:00] matrici
[00:28:02] e e valuta quanto tempo ci impiega a
[00:28:05] fare questo calcolo, no? Questo è lo
[00:28:07] script base di partenza e adesso
[00:28:09] utilizziamo loop engineering per
[00:28:11] ottimizzare questo prodotto framrice che
[00:28:14] è un problema aperto che tutti stanno
[00:28:16] cercando di ottimizzare.
[00:28:19] Quindi lanciamo il primo esperimento,
[00:28:21] matrix multiply e questi sono i tempi.
[00:28:25] Queste sono le dimensioni delle matrici
[00:28:26] 500* 500, 1000* 1000, 2000* 2000, 3000*
[00:28:29] 3000 e questi sono i tempi 004 018, 0019
[00:28:34] e 0398 secondi. Quindi adesso
[00:28:37] utilizziamo GOL per fare ottimizzazione
[00:28:39] di algoritmi, che è il caso d'uso più
[00:28:43] bello da utilizzare perché vedi proprio
[00:28:45] gli esperimenti, gli step che fa. Quindi
[00:28:48] facciamo slashg
[00:28:50] migliora eh i tempi impiegati per fare
[00:28:56] il prodotto fra matrici
[00:28:59] ehm
[00:29:01] con questo script Python
[00:29:05] ad ogni test che fai e
[00:29:09] scrivilo su di un file mark down e
[00:29:15] scrivendo anche in breve le modifiche
[00:29:19] fatte
[00:29:21] per avere tracciabilità
[00:29:25] virgola. E qua metto fai al massimo 10
[00:29:31] eh tentativi di ottimizzazione,
[00:29:35] quindi adesso gli do 10 step per
[00:29:38] automigliorarsi. E questo adesso è slash
[00:29:40] gol, quindi entra adesso in un loop
[00:29:43] senza che io devo stare tutte le volte
[00:29:45] "No, migliora questo, no, miglioralo
[00:29:47] un'altra volta", no, riportalo come
[00:29:50] prima senza scrivere prompt. Gli ho
[00:29:52] settato un gol, un loop specifico e
[00:29:55] adesso parte.
[00:29:56] Ecco qua che ha fatto tutti e 10 i
[00:29:58] tentativi. Abbiamo qua lo speedup,
[00:30:00] quindi ha raggiunto un'ottimizzazione di
[00:30:02] 320 volte dal punto di vista della
[00:30:05] velocità usando appunto i tensor core.
[00:30:08] Qua su optimization log vediamo tutte le
[00:30:10] modifiche che ho fatto, quindi script
[00:30:13] originale, flot 64 di default, poi
[00:30:17] doppia banda di memoria passato a non
[00:30:19] pai, flot 32 blus con quattro thread e
[00:30:23] cp torchu,
[00:30:26] poi patorch sulla GPU ha iniziato a
[00:30:29] usare CUDA eh, fino ad arrivare a Porch
[00:30:32] GPU flot 16, solo calcolo half precision
[00:30:36] su Tensor Core Max Truput. E qua abbiamo
[00:30:38] la massima eh il massimo risultato.
[00:30:41] Questo è un esempio eh molto semplice,
[00:30:44] però che ti fa capire appunto le
[00:30:46] potenzialità di questo approccio,
[00:30:47] soprattutto nel coding e nelle app, ma
[00:30:49] lo si può utilizzare anche per fargli
[00:30:51] creare modelli 3D,
[00:30:54] post sui social, praticamente qualsiasi
[00:30:56] cosa, perché poi Cloud con i vari server
[00:30:58] MCP lo puoi collegare a tutto e quindi
[00:31:01] puoi utilizzare il loop engineering
[00:31:04] praticamente per qualsiasi cosa. Spero
[00:31:06] che tu abbia compreso, appunto, che
[00:31:08] cos'è il loop engineering e che ti sia
[00:31:10] piaciuto anche tutto l'escursus storico
[00:31:11] fatto delle scelte e di tutti i loop che
[00:31:14] sono stati aggiunti, appunto, in questi
[00:31:17] sistemi. Scrivimi un commento qui sotto
[00:31:19] dicendomi la tua, cosa ne pensi e
[00:31:20] seguimi per rimanere aggiornato sul
[00:31:22] mondo delle ar.
