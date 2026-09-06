
[00:00:00] In questo video ti faccio vedere come
[00:00:01] tagliare drasticamente il consumo dei
[00:00:04] token di Cloud Code con 10 mosse. Sono
[00:00:07] gratis, le implementi oggi stesso e la
[00:00:09] prima funziona in 10 secondi. La vediamo
[00:00:12] una per una, passo dopo passo e per
[00:00:14] ognuna voglio farti vedere anche un
[00:00:16] confronto visivo dei token che vai a
[00:00:18] risparmiare e per quale motivo la
[00:00:20] tecnica funziona. E poi c'è la parte che
[00:00:23] nessuno ti dice. Infatti, verso la fine
[00:00:25] di questo video andrò a vedere quali di
[00:00:27] queste strategie portano delle
[00:00:29] conseguenze, perché in alcuni casi
[00:00:31] andare a risparmiare sui token porta una
[00:00:33] ripercussione magari sulla qualità
[00:00:35] dell'output. Stessa storia per i trucchi
[00:00:37] e i tool famosi che ti consigliano in
[00:00:39] giro promettendoti di risparmiare il 90%
[00:00:43] dei tuoi token. Molti sono fuffa e
[00:00:45] alcuni peggiorano solamente la
[00:00:47] situazione. Ti dico anche quali sono e
[00:00:49] il motivo per il quale non funzionano.
[00:00:51] Se è la prima volta che vedi questi
[00:00:52] video, sono un ingegnere informatico e
[00:00:54] gestisco Mart, un'azienda attraverso la
[00:00:57] quale aiutiamo le imprese a scalare
[00:00:58] implementando l'intelligenza artificiale
[00:01:00] all'interno dei loro processi. Partiamo
[00:01:02] con la formazione di tutto il loro team
[00:01:04] su strumenti pratici come Cloud Code,
[00:01:07] Cloud Cowork, Codex per poi diventare il
[00:01:10] loro partner strategico, nel senso che
[00:01:12] andiamo ad analizzare i loro processi
[00:01:13] per poi andare a costruire soluzioni AI
[00:01:16] customizzate in base alle loro esigenze.
[00:01:19] Senza perdere altro tempo direi di
[00:01:20] passare subito al video. Ho preparato
[00:01:22] come al solito, una lavagna dove andiamo
[00:01:24] a coprire punto per punto, comprendendo
[00:01:27] davvero ogni tecnica, che cos'è, come
[00:01:29] funziona e perché funziona. Ma prima di
[00:01:31] toccare qualsiasi cosa, gli strumenti di
[00:01:33] misurazione che sono indispensabili sono
[00:01:36] tre, sono/usage
[00:01:39] e la status line, sono nello specifico
[00:01:41] dentro cloud code e slashcectext
[00:01:44] a vedere la quanta finestra di contesto
[00:01:47] abbiamo occupato. Ogni modello ha la
[00:01:49] finestra di contesto, cioè quanto input
[00:01:51] può prendere dentro, no? Opus nello
[00:01:53] specifico ha un milione di token. Sonet
[00:01:55] se non sbaglio, sta ancora a 200.000.
[00:01:57] Quindi questo è un modo per misurare.
[00:01:59] Una cosa che pochissima gente sa è che
[00:02:01] adesso sono sulla nuova chat, vedete,
[00:02:02] non ho scritto nulla, sto andando giù
[00:02:04] su, non ho scritto nulla, non ho scritto
[00:02:06] nulla e sto già al 6% dello usage. Ho
[00:02:09] già occupato 60.000 token. Questa è una
[00:02:12] cosa che la gente non sa e se vi
[00:02:13] chiederete "Ma come 6% non hai mandato
[00:02:16] neanche un messaggio?" Beh, perché ci
[00:02:18] sono i file di memoria, il system prompt
[00:02:22] che è il cloud. MD, i server MCP.
[00:02:24] Infatti, ogni volta che noi carichiamo
[00:02:26] un server MCP occupa memoria, anche se
[00:02:28] poi non lo usiamo. Abbiamo anche le
[00:02:30] skills, quindi come regola bisogna stare
[00:02:33] fra il 3 e il 6%, io sto proprio al
[00:02:35] limite. Quando fate slash context su una
[00:02:37] nuova conversazione. Molti dei nostri
[00:02:39] clienti quando partono con slashce
[00:02:40] context andiamo a vedere che stanno già
[00:02:42] al 20% e poi si chiedono perché
[00:02:44] consumano i loro token in un batter
[00:02:46] d'occhio. Secondo comando fondamentale è
[00:02:49] slusage. Ci fa vedere a che livello
[00:02:52] siamo dello usage. solo i limiti delle 5
[00:02:55] ore settimanali di Fable, ma ci dice
[00:02:57] anche come stiamo usando i nostri limiti
[00:03:00] e le skill che consumano di più. Io ho
[00:03:03] consumato il 93% oltre il 150.000 token
[00:03:07] nella finestra di contesto e il 30% con
[00:03:10] quattro più sessioni in parallelo. La
[00:03:13] skill che mi consuma più di tutti è la
[00:03:15] mia skill Real Editor. Questo perché io
[00:03:17] ho questo mio profilo Instagram che
[00:03:19] essenzialmente va quasi in autopilota,
[00:03:22] nel senso tutti i reel che vedete qua
[00:03:24] che fanno anche i bei numeri sono tutti
[00:03:26] quanti editati e postati automaticamente
[00:03:28] dalle AE. Io li registro, io faccio la
[00:03:29] ricerca dei contenuti, però queste
[00:03:32] questo edit che state vedendo qua me lo
[00:03:33] fa Cloud. Un'altra cosa molto
[00:03:36] importante, se utilizzate le app di
[00:03:37] Cloud da desktop, basta avanzano questi
[00:03:39] questi comandi qua. Un'altra cosa
[00:03:41] interessante è vedere qui in basso a
[00:03:42] destra abbiamo il la finestra di
[00:03:44] contesto e il limite direttamente qui in
[00:03:46] questo pallino, ma se usate Cloud
[00:03:48] all'interno del terminale, come spesso
[00:03:50] piace fare a me, potete personalizzare
[00:03:52] questa cosa che si chiama status line e
[00:03:55] io ad esempio l'ho personalizzata così,
[00:03:57] cioè qua posso vedere quanto il mio
[00:03:58] contesto occupato, qua posso vedere il
[00:04:01] mio limite della sessione, qua il mio
[00:04:02] limite settimanale. Mi piace vederlo
[00:04:04] così con questi colori. Se volete anche
[00:04:06] voi un setup come questo, basta che fate
[00:04:08] lo screenshot a questo video, questa
[00:04:10] sezione qua di teclada, mi personalizzi
[00:04:12] la status line in modo tale da aver da
[00:04:16] averla così e l'equivalente di quella
[00:04:18] status line è questa cosetta qua
[00:04:19] nell'app. Bene, quindi elevati eh questi
[00:04:22] strumenti di misurazione, partiamo con
[00:04:24] quel con quelle tecniche che si possono
[00:04:27] utilizzare da subito, che sono quelle
[00:04:29] spesso noiose, ma che funzionano meglio.
[00:04:32] Prima di tutto slash clear ad ogni
[00:04:34] cambio di task. Ogni volta che c'è un
[00:04:36] task diverso, che sia una nuova
[00:04:38] funzionalità nell'app, che sia una nuova
[00:04:40] richiesta di cloud che non c'entra con
[00:04:42] quello che abbiamo detto, fate slash
[00:04:44] clear che vi riazzera la cronologia
[00:04:46] nella conversazione. Faccio un esempio,
[00:04:48] mettiamo caso che qua a questa
[00:04:49] conversazione gli dico "Ciao, come
[00:04:51] stai?" Con "Ciao, come stai?" Sono
[00:04:53] arrivato al 15% già della mia finestra
[00:04:57] del contesto. Se faccio slash clear la
[00:05:01] conversazione riparte da zero e come
[00:05:03] vedete se poi digito slash context dopo
[00:05:05] che faccio slash clear si riparte.
[00:05:07] Dovrebbero ripartire da quel 6% là.
[00:05:10] Eccoci qua. Quindi, senza che
[00:05:12] necessariamente dovete aprire una nuova
[00:05:14] chat, qui fate slash clear e si riparte
[00:05:16] per ogni nuovo task noioso, ma funziona.
[00:05:19] Poi modello ed effort scelti una volta
[00:05:23] sola, sola all'inizio della chat. Noi
[00:05:25] all'inizio della chat possiamo decidere
[00:05:27] il modello piuttosto che l'effort.
[00:05:29] Possiamo mettere l'effort basso, medio,
[00:05:32] alto, extra, max, ultra code e questo
[00:05:36] diciamo è se dobbiamo fare del lavoro
[00:05:38] estremamente estremamente potente. Uno
[00:05:40] degli errori più spessi che vedo è che
[00:05:43] nel bel mezzo della conversazione si
[00:05:45] cambia il modello o si cambia l'effort.
[00:05:46] Che succede? è come se andassimo a
[00:05:48] scegliere un nuovo cervello. Per passare
[00:05:51] a un nuovo cervello, quel cervello deve
[00:05:53] avere il contesto di tutta la
[00:05:54] conversazione, no? Quindi dobbiamo
[00:05:56] ripassare tutta quanta la conversazione,
[00:05:57] quello che abbiamo fatto al nuovo
[00:05:59] cervello e questo che vuol dire? Consumo
[00:06:01] di token, quindi scegliere il modello e
[00:06:03] l'effort solo all'inizio della
[00:06:05] conversazione, mi raccomando. Altra cosa
[00:06:09] slashca compact, questa è la cavolata
[00:06:11] più grossa che si legge in giro, cioè
[00:06:14] Compact viene valutato come un ottimo
[00:06:16] strumento di cloud per chi sai
[00:06:18] essenzialmente che cosa fa Compact.
[00:06:19] Quando arriviamo a un certo punto della
[00:06:20] conversazione, mettiamo caso siamo
[00:06:22] arrivati all'80% del contesto, la
[00:06:24] compattiamo, cioè andiamo Cloud si va a
[00:06:26] prendere i punti salienti della
[00:06:28] conversazione così che possiamo
[00:06:29] continuare, così che compattandola
[00:06:32] riusciamo a continuare in quella chat e
[00:06:34] sembra fantastico perché, insomma,
[00:06:36] possiamo continuare su quella stessa
[00:06:37] chat. Spesso Cloud ce lo consiglia anche
[00:06:39] lui, fai compact perché stiamo arrivando
[00:06:41] alla fine del contesto. Compact è una
[00:06:44] cavolata gigantesca, secondo me, per due
[00:06:47] motivi. Spesso non serve fare un
[00:06:49] compact, ma basta fare il rewind. Adesso
[00:06:51] andiamo a vedere che vuol dire. Seconda
[00:06:53] cosa, se lasciamo a Cloud la libertà di
[00:06:56] riassumere la nostra conversazione,
[00:06:59] sceglierà lui cosa riassumere, cosa
[00:07:00] tenere. Quindi la cosa che è decisamente
[00:07:04] migliore è quello di creare un file di
[00:07:05] endoff, si chiama tranquilli, adesso
[00:07:07] andiamo a vedere tutto dove diciamo a
[00:07:08] Cloud questi sono i punti salienti,
[00:07:11] queste sono le cose che voglio portarmi
[00:07:12] nella prossima conversazione perché
[00:07:14] sennò diamo la palla a Cloud, sceglie
[00:07:16] lui cosa mettere, cosa cosa cosa
[00:07:18] riassumere e non lo vogliamo. Mettiamo
[00:07:20] caso che ho questa conversazione dove
[00:07:22] essenzialmente qui dentro quello che ho
[00:07:24] fatto con Cloud è stato aiutarmi alla
[00:07:27] preparazione di questo video. Se fossi
[00:07:28] arrivato, che ne so, a un 50-60% del
[00:07:31] contesto Proip, se arrivi al 40-50%
[00:07:34] del tuo contesto perdi di un sacco la
[00:07:37] qualità. Quindi dopo il 4050%
[00:07:40] cambia chat, se ti serve ancora qualcosa
[00:07:43] creati un file d'andoff. Adesso ti
[00:07:44] faccio vedere come invece di fare
[00:07:46] compact, spesso quello che funziona
[00:07:49] molto meglio è un comando che si chiama
[00:07:51] rewind che ci permette di andare di
[00:07:53] ritornare a un certo punto della
[00:07:54] conversazione senza consumare alcun
[00:07:56] token. Quindi vi faccio vedere come
[00:07:58] funziona. Rewind e mi dice dove puoi
[00:08:01] riavvolgere il nastro. Questo è l'ultimo
[00:08:03] messaggio che gli ho passato. Questo è
[00:08:05] il primo messaggio. Posso riavvolgere il
[00:08:07] nastro a un certo punto della
[00:08:08] conversazione. Quindi, ad esempio, posso
[00:08:10] aggiungerlo qui dove ho detto, "Guarda,
[00:08:12] look del video me lo devi fare più
[00:08:13] forte." Posso cliccare questo, posso
[00:08:16] cliccare un qualsiasi punto della
[00:08:17] conversazione e tornare lì. Ovviamente
[00:08:20] se usi Cloud Code nel terminale o
[00:08:22] all'interno dell'estensione di Visual
[00:08:24] Studio Code è la stessa identica cosa,
[00:08:26] non cambia nulla. Vi faccio vedere.
[00:08:28] rewind e possiamo passare a un qualsiasi
[00:08:31] punto della conversazione, vedete, va a
[00:08:34] riavvolgere il nastro in quel punto là.
[00:08:37] Quindi rewind, non compact. Se proprio
[00:08:41] devi cambiare conversazione e portarti
[00:08:43] dietro delle informazioni senza passare
[00:08:45] la palla a cloud, creati un file di
[00:08:47] handoff. Un file di handoff è un file
[00:08:49] dove diciamo a Cloud ecco a che punto
[00:08:51] siamo arrivati, ecco le problematiche,
[00:08:53] ecco che cosa dobbiamo fare, lo passiamo
[00:08:56] una nuova sessione di Cloud Code così
[00:08:57] lui ha già idea di a che punto siamo
[00:09:00] arrivati. possiamo aprire una nuova
[00:09:02] sessione, quindi ripartendo da zero,
[00:09:03] essenzialmente, senza consumare token, e
[00:09:05] gli passiamo noi eh le informazioni che
[00:09:09] vogliamo avere nella prossima
[00:09:10] conversazione, perché una cosa
[00:09:12] fondamentale da capire è questa
[00:09:14] animazione qui. Cioè, ogni volta che noi
[00:09:16] andiamo a mandare un messaggio, il
[00:09:18] nostro messaggio pensiamo vabbè, ma sono
[00:09:21] pochi token, no? Questo è questo è il
[00:09:23] messaggio singolo che mando, questo è il
[00:09:25] messaggio singolo che mando, no? Questo
[00:09:26] è il singolo messaggio che mando. Il
[00:09:28] problema è che ogni volta che ci
[00:09:29] risponde lui si va a rileggere tutto ciò
[00:09:32] che è successo prima. Quindi, mettiamo
[00:09:34] caso, questo è il secondo messaggio.
[00:09:36] Cloud si va a rileggere quello che ha
[00:09:38] detto prima, in più ci dice ci mette la
[00:09:40] nuova risposta. Poi ci deve essere una
[00:09:42] nuova risposta. Emma si va a leggere
[00:09:44] ogni volta quello che è successo prima,
[00:09:46] quindi ogni volta è come se fosse
[00:09:48] esponenziale. Vedete, ogni nuovo
[00:09:49] messaggio che gli passiamo, lui si va a
[00:09:51] leggere tutto prima, tutta la storia, la
[00:09:54] la conversation history, la cronologia,
[00:09:57] motivo per il quale Rewind è
[00:10:00] estremamente intelligente. Vediamo ora
[00:10:02] come funziona il file di endoff. o gli
[00:10:03] diciamo semplicemente creiamo un file di
[00:10:05] endoff in cui Mirenki le problematiche
[00:10:08] che abbiamo avuto, come le abbiamo
[00:10:10] risolte, concentrati su questo piuttosto
[00:10:12] che quello, piuttosto che io, ad
[00:10:14] esempio, ho creato eh una skill che si
[00:10:16] chiama slash andandof che avrete eh qui
[00:10:19] sotto nel secondo link in descrizione,
[00:10:21] c'è il link a tutti quanti i miei
[00:10:22] template che potete prendere
[00:10:23] tranquillamente, vi potete scaricare
[00:10:24] anche questa skill. Vi faccio vedere. Ho
[00:10:26] riaperto un'altra chat a caso. Se io
[00:10:28] faccio slashendof,
[00:10:30] guardate che cosa mi chiede. Ci fa delle
[00:10:32] domande chiedendo quali sono quelle cose
[00:10:34] che ci vogliamo portare in una prossima
[00:10:36] chat di Cloud Code. Quindi io spesso
[00:10:37] quello che faccio, siccome so che questa
[00:10:39] skill quando la invoco mi chiede quali
[00:10:41] sono le cose che ti vuoi portare, faccio
[00:10:43] nella prossima sezione faccio slash
[00:10:44] andandof, focalizzati sui problemi che
[00:10:46] abbiamo avuto, come li abbiamo risolti
[00:10:48] su questa cosa e su questa cosa e e poi
[00:10:50] mi dà un file che me lo incolle in
[00:10:52] un'altra chat. Comunque
[00:10:54] in questo caso Cloud ci chiede ad
[00:10:55] esempio su cosa ci vogliamo concentrare.
[00:10:57] Mi voglio concentrare su questo, ad
[00:10:59] esempio. Ecco che mi scrive il il mio
[00:11:02] file di endoff. Nel file di handoff mi
[00:11:04] mette sempre l'obiettivo, a che punto
[00:11:07] siamo, cosa abbiamo provato che non ha
[00:11:08] funzionato, i problemi incontrati e come
[00:11:11] li abbiamo risolti, decisioni prese,
[00:11:13] file toccati, dove vogliamo andare.
[00:11:14] Quindi basta copiare questo file qui,
[00:11:17] aprire la nuova sessione e fare
[00:11:19] continuiamo
[00:11:21] quello che stavamo facendo nella scorsa
[00:11:26] sessione.
[00:11:28] Incolliamo e si parte. Questo è molto
[00:11:30] più efficiente di continuare una
[00:11:31] sessione all'infinito proprio per questo
[00:11:33] ragionamento qui, per non parlare della
[00:11:34] qualità in più che andiamo ad ottenere
[00:11:37] facendo un mero compact. Altra cosa
[00:11:40] fondamentale, questo non l'ho visto
[00:11:41] quasi da nessuna parte, farsi fare un
[00:11:44] diagramma ashi, asi, chiamatelo come vi
[00:11:47] pare, prima di costruire qualsiasi cosa
[00:11:49] eh che sia grafico. Mi spiego meglio.
[00:11:51] Quando andiamo a costruire un qualcosa
[00:11:52] di grafico, che sia questa lavagna
[00:11:55] piuttosto che un front-end, spessissimo
[00:11:58] che succede? Vai Clode, voglio costruire
[00:12:00] questo, questo, questo e questo.
[00:12:02] Costruisce tutto quanto. Il risultato
[00:12:04] non ci piace. Cloud cambia questo.
[00:12:06] Cloud, questo mettilo più in alto.
[00:12:08] Cloud, questo mettilo in basso a destra.
[00:12:09] Cloud cambia il font. Soluzione i
[00:12:12] diagrammi
[00:12:14] asci. essenzialmente sono dei diagrammi
[00:12:16] che costano pochissimo a Cloud fare
[00:12:18] perché sono delle lineette, dei trattini
[00:12:20] e con queste lineette, questi trattini
[00:12:23] Cloud ci presenta un po' l'interfaccia
[00:12:25] come verrà fuori, così che prima di
[00:12:27] andare a costruire qualcosa ci facciamo
[00:12:30] prima fare un diagrammino e già dal
[00:12:31] diagrammino capiamo se lo stile ci
[00:12:33] piace. ad esempio una skill che mi
[00:12:35] prepara le lavagne come quella che
[00:12:36] vedevamo prima e questo è un esempio.
[00:12:38] Quando vado a generare la lavagna, ecco
[00:12:40] che mi dà prima la preview della
[00:12:42] lavagna, così che senza che me la va a
[00:12:45] generare sprecando token, gli posso dire
[00:12:47] "No, guarda, questo non mi piace,
[00:12:48] cambia". No, guarda quest'altro, fallo
[00:12:50] così, fallo col là. Ho fatto anche un
[00:12:52] altro esempio, gli ho detto "Guarda,
[00:12:53] voglio che mi crei un e-commerce per i
[00:12:55] miei prodotti shampoo". E
[00:12:58] automaticamente quello che fa è mi fa
[00:12:59] vedere la homepage come la farebbe con
[00:13:01] le immagini, la la hero section. Questo
[00:13:05] qua sono è la nav,
[00:13:08] la scheda prodotto, cosa farebbe? borsa,
[00:13:11] mobile. Quindi prima di andare a
[00:13:13] generare qualsiasi cosa, posso
[00:13:15] automaticamente cambiare le cose qua
[00:13:17] senza sprecare i codici inutilmente.
[00:13:18] Quindi una cosa che vi consiglio di fare
[00:13:20] è che in ogni skill che avete per il
[00:13:22] design metteteci uno step prima che vi
[00:13:24] consente di avere un diagramma Ashi
[00:13:26] prima di generare qualsiasi cosa. Poi
[00:13:29] andiamo a vedere quelle tecniche che
[00:13:30] devi fare una volta e una volta che lo
[00:13:32] fai poi eh sei pronto a procedere. Il
[00:13:36] primo è quello di spegnere gli MCP che
[00:13:38] non utilizzi, proprio perché, come
[00:13:40] vedevamo prima, se fai slash contact
[00:13:41] senza aver neanche mandato un messaggio,
[00:13:43] comunque gli MCP occupano spazio. Per
[00:13:46] farlo è semplicissimo, basta che vai su
[00:13:49] eh fai slp, ti si appaiono tutti gli MCP
[00:13:52] e quelli che non utilizzi li eh li
[00:13:55] elimini. Essenzialmente questo da solo
[00:13:58] ti garantisco che ti salverà un sacco di
[00:14:00] token. Altra cosa, il cloud.md MD come
[00:14:03] indice. Quello che vogliamo, appunto,
[00:14:05] non è un documento, ma trattare questo
[00:14:08] Clode MD come se fosse un indice. Il
[00:14:10] cloud.md, MD, per chi non lo sapesse, è
[00:14:13] un prompt che Clode si va a leggere ad
[00:14:15] ogni messaggio. Anche prima di aver
[00:14:18] mandato qualsiasi altra cosa, come
[00:14:19] avevamo visto prima con slashce context,
[00:14:20] si va a leggere quel prompt si chiama,
[00:14:24] se lo legge ad ogni messaggio per tutta
[00:14:26] la conversazione. Quindi se il nostro
[00:14:27] Cloud MD è gigantesco e per leggerlo si
[00:14:30] consumano 4.000 token, capite bene che
[00:14:32] magari dopo 8 messaggi abbiamo consumato
[00:14:34] 32.000 token così, mentre se fosse
[00:14:36] semplicemente un indice, quindi 450
[00:14:39] token, dopo 8 messaggi stiamo a 3600 di
[00:14:43] token. La regola dal doc di Antropic
[00:14:45] dice di tenere il cloud MD sotto le 200
[00:14:47] righe e trattare semplicemente come un
[00:14:49] indice. Il Clode MD deve dire a Cloud:
[00:14:52] "Ok, questa cartella fa questo, cioè poi
[00:14:53] c'è questa cartella che fa questo,
[00:14:55] eccetera eccetera". Ad esempio, nel mio
[00:14:57] second
[00:15:00] è questo qui. Come vedete non è
[00:15:02] nient'altro che un indice, cioè qua
[00:15:05] andiamo a dirgli, guarda, in questa
[00:15:07] cartella ci sono preferenze stile
[00:15:09] abitudini, qua ci sono strutture,
[00:15:11] organizzazioni infaziendali, eccetera
[00:15:13] eccetera e stiamo sulle 166 righe. Altra
[00:15:17] cosa che forse questa del cloud. MD come
[00:15:19] indice la sapevate, ma questa, ossia
[00:15:22] usare il cloud. MD come cartella non è
[00:15:24] per niente banale, scusate, un Cloud MD
[00:15:27] per ogni cartella. Mi spiego meglio.
[00:15:30] Questo è un è un trucco che viene
[00:15:31] direttamente da Andrew Carpati, uno dei
[00:15:34] membri fondatori di Openi, adesso sta ad
[00:15:36] Antropic, ha inventato tutto il concetto
[00:15:38] di second brain con l' LLM wiki. Una
[00:15:41] cosa che vi consiglio tantissimo di fare
[00:15:45] è avere un cloud.
[00:15:48] Tale che il cloud. MD generale funge da
[00:15:52] indice e poi quando, che ne so, che io
[00:15:54] gli faccio una domanda su Painpoint di
[00:15:57] un mio cliente con il cloud. Sa che deve
[00:16:00] accedere a questa cartella qua, Context,
[00:16:02] e solamente poi quando va a accedere a
[00:16:04] context qui dentro ci sarà un altro
[00:16:08] cloud. MD. Quest'altro Cloud MD va a
[00:16:10] spiegare i vari file che ci sono
[00:16:13] all'interno della mia cartella di
[00:16:14] contesto. Qui poi andiamo a mettere le
[00:16:17] regole eccetera eccetera. Ma in questo
[00:16:19] modo non andiamo a caricare il cloud.d
[00:16:22] generale con tantissime informazioni.
[00:16:24] Mettiamo un clode. MD per ogni cartella.
[00:16:27] Ogni mia cartella ha un cloud. MD. Che
[00:16:28] ne so. Apro risorse. Queste risorse ha
[00:16:32] un clode. MD. Ogni mia cartella ha un
[00:16:35] clode. MD. Non vi spaventate se io
[00:16:37] utilizzo l'estensione di visual Sudo
[00:16:39] Code. Questa è l'excalro che mi ha
[00:16:41] mandato prima anche qui all'interno eh
[00:16:44] dell'Aptic Clode va va alla grande. Poi
[00:16:46] altra cosa, archiva le skill che non
[00:16:48] utilizzi e accorcia e accorcia le
[00:16:50] descrizioni. Come abbiamo visto prima,
[00:16:53] con slash contact si vanno a caricare
[00:16:54] tutte le skill, quindi quelle che non
[00:16:56] usi consumano token, e vai ad accorciare
[00:16:59] le descrizioni. Basta chiederlo a Cloud,
[00:17:01] guarda Cloud, voglio accorciare le
[00:17:04] descrizioni delle main skill per
[00:17:05] sprecare meno token, poi vammi a fare un
[00:17:08] test end to end per vedere che le skill
[00:17:10] funzionano comunque alla grande. Lo puoi
[00:17:12] fare anche volta per volta, questo
[00:17:14] tranquillamente, però questo ehm è una
[00:17:17] cosa che fai una volta
[00:17:20] e eh aiuta tantissimo. Altra cosa,
[00:17:23] diciamo che questa è una cosa di cui
[00:17:25] vado abbastanza fiero, nel senso che una
[00:17:28] cosa che spende tantissimo, che brucia
[00:17:31] tantissimo token, sono i PDF che
[00:17:34] carichiamo a Cloud. Ogni pagina di un
[00:17:36] documento PDF elaborato con Cloud code
[00:17:39] consuma tra i 1500 e 3000 token.
[00:17:41] Immaginatemi un PDF di 100 pagine, 200
[00:17:44] pagine, 1000 pagine. Quindi molto spesso
[00:17:47] a noi serve solamente il contenuto del
[00:17:49] documento. Questo metodo che andremo a
[00:17:51] vedere è ottimo se ci serve il
[00:17:52] contenuto, se ci servono le immagini, i
[00:17:54] grafici è un'altra storia, carichiamo
[00:17:56] solamente quella e basta. Avanza. Ma
[00:17:58] siccome nell'80% dei casi ci serve il
[00:18:00] testo, ho costruito un hook che mi va a
[00:18:03] prendere il PDF e mi estrae il testo.
[00:18:05] Cosa diavolo è un hook? Che cosa ho
[00:18:07] appena detto? Spiego meglio. UNUC è una
[00:18:10] regola deterministica di Cloud che
[00:18:12] possiamo far attivare ogni qualvolta
[00:18:14] succede un determinato evento. Mi spiego
[00:18:16] meglio ancora. Noi possiamo imporre
[00:18:18] delle condizioni deterministiche a un
[00:18:21] if, per capirci. Ogni qual volta succede
[00:18:23] qualcosa. Ogni volta che carico un PDF
[00:18:26] deve succedere questo. Ogni volta che
[00:18:28] crei un file deve succedere quello. Ogni
[00:18:31] volta che faccio una chiamata API deve
[00:18:33] succedere questo. Esempi di UK sono ogni
[00:18:36] volta che creo un file sincronizzami con
[00:18:39] il mio Drive, Google Drive, Gitab, così
[00:18:42] che quel file che mi hai creato sta
[00:18:44] anche nel mio nel mio nel mio Drive, nel
[00:18:46] mio cloud, piuttosto che ogni volta che
[00:18:49] carico un documento vammi a controllare
[00:18:51] se ci sono delle informazioni manevole
[00:18:54] perché magari c'è un prompt injection.
[00:18:56] Quello che ho fatto io, ho creato un
[00:18:57] hook che ogni volta che carico un PDF mi
[00:19:00] va a eseguire uno script, un codice, uno
[00:19:02] script di Python che mi estrae il testo.
[00:19:06] Non si va a leggere ogni pagina perché
[00:19:08] se si andasse a leggere ogni pagina si
[00:19:09] va a estrapolare solamente il testo.
[00:19:11] viene spiegato meglio, cioè c'è questo
[00:19:14] hook che ogni volta che carico un ehm un
[00:19:18] documento, quindi quando Cloud deve fare
[00:19:20] una read, va a eseguire questo script
[00:19:23] PDF read che essenzialmente mi estrae il
[00:19:27] testo e si legge solamente questo testo,
[00:19:29] non il PDF e questo si attiva ogni volta
[00:19:33] che gli carico un PDF. Nel secondo link
[00:19:35] in descrizione, oltre alla skill di
[00:19:37] Handoff, vi lascio anche il prompt che
[00:19:39] potete incollare per costruirvi voi
[00:19:41] stessi questo hook. Vi garantisco che
[00:19:43] questo è veramente una mano dal cielo,
[00:19:45] non sapete quanti token mi ha fatto
[00:19:47] risparmiare. Io ho fatto diversi test,
[00:19:49] se non mi credete fateli anche voi, dove
[00:19:51] essenzialmente ho caricato un PDF da 300
[00:19:53] pagine. Con il Reid ho speso circa
[00:19:57] 500-600.000 token dove il read non è
[00:20:00] nient'altro che ho passato il PDF, Cloud
[00:20:02] se l'è letto tutto. Con il mio hook ho
[00:20:04] eh speso 150.000 token, quindi risparmi
[00:20:07] dalle 3:00 alle 4:00 volte. È tantissima
[00:20:10] roba. Secondo il link in descrizione
[00:20:12] trovi il tra tutte le mie risorse il
[00:20:15] promptarti anche tu questo hook. Copi il
[00:20:17] prompt, te lo passi su Cloud Code, è una
[00:20:19] cavolata. Ok, andiamo poi a vedere la
[00:20:22] questione dei modelli, eh, perché la
[00:20:24] qualità stessa del modello che scegliamo
[00:20:26] è essa essa stessa un risparmio, nel
[00:20:28] senso che quando si fa coding e comunque
[00:20:32] si va a costruire un qualcosa di
[00:20:33] estremamente complesso resta sul modello
[00:20:36] di frontiera. Ho fatto anche un video su
[00:20:38] come utilizzare Cloud Code gratis e la
[00:20:40] cosa che essenzialmente dico anche là è
[00:20:42] se devi fare i task estremamente
[00:20:43] complessi non usare il modello chip, non
[00:20:46] usare un qualcosa che ti può far
[00:20:49] risparmiare un pochettino perché
[00:20:51] probabilmente poi farà un lavoro pessimo
[00:20:53] e poi ci dovrai ripassare sopra, quindi
[00:20:55] fra il tuo tempo perso e e i token che
[00:20:57] dovrei rispreare dopo non ha senso.
[00:20:59] Quindi, se stiamo parlando di coding,
[00:21:01] comunque non troppo complesso, ma fai
[00:21:04] conto che è un software che devi
[00:21:05] costruire per un cliente, un qualcosa da
[00:21:07] portare in produzione, modelli di
[00:21:09] frontiera, quindi che sia Fable, Opus,
[00:21:13] GPT 5.6, Grock 4.6,
[00:21:16] utilizziamo modalità di frontiera.
[00:21:18] Questa è una cosa che non si scappa,
[00:21:20] purtroppo. Se vuoi costruire qualcosa di
[00:21:21] estremamente complesso, resta sul top
[00:21:23] del top. Però quando parliamo di routine
[00:21:27] skill sotto agenti/chrome
[00:21:29] che è essenzialmente Cloud che può
[00:21:31] vedere la nostra schermata e può toccare
[00:21:34] all'interno del nostro internet, IQ e
[00:21:36] Sonet vanno benissimo. Il 99% di skill e
[00:21:40] routine, dove per chi non lo sapesse la
[00:21:42] skill è una procedura standardizzata che
[00:21:44] insegniamo a Cloud, quindi che ne so,
[00:21:46] gli insegniamo, gli possiamo dare una
[00:21:47] skill così che scriverà sempre le mail
[00:21:49] con il nostro stile. Quella è una skill,
[00:21:52] una competenza che insegniamo a Cloud.
[00:21:53] come faremo con un nostro membro del
[00:21:55] team. La routine è una è una skill che
[00:21:58] viene seguita sempre un certo in certa
[00:22:00] ora di un determinato giorno. Per il 90%
[00:22:03] dei casi le skill e le routine va
[00:22:05] benissimo IQ o Sonnet. Stessa cosa per
[00:22:08] Chrome, cioè quando Cloud deve andare a
[00:22:10] toccare il nostro schermo e della nostra
[00:22:13] che ne so del nostro Google Chrome, di
[00:22:14] quello che utilizziamo, Brave, quello
[00:22:16] che sia. IQ Onet vanno alla grande.
[00:22:18] Ovviamente qui ho messo la stessa cosa
[00:22:20] che dicevamo prima, cioè cambiare il
[00:22:22] modello in corsa. spreca un sacco di
[00:22:24] token. Vale lo stesso se stiamo
[00:22:25] utilizzando una skill, se stiamo creando
[00:22:28] più sottoagenti. Stessa cosa. Ultima
[00:22:30] cosa, occhi task schedulati. ti assicuro
[00:22:33] che magari hai tantissime routine delle
[00:22:35] quali ti sei o scordato oppure non sono
[00:22:38] per niente efficienti. Quindi vatti a
[00:22:40] rivedere se puoi efficientarle, se puoi
[00:22:42] usare un modello più economico, perché
[00:22:45] io mi sono reso conto facendo unudit
[00:22:47] completa che avevo tantissimi task
[00:22:49] schedulati che mi consumavano tantissimo
[00:22:51] del del mio usage, del mio utilizzo.
[00:22:54] Quindi sembra una cavolata, ma questo ma
[00:22:56] dargli un'occhiata. cose da non fare che
[00:22:58] sembrano furbe ma sono delle cavolate.
[00:23:01] Slash compact è il messaggio più caro,
[00:23:04] cioè funziona male e ti consumi un sacco
[00:23:07] di token perché per riassumere tutto
[00:23:09] rimanda tutto quanto, poi butta via la
[00:23:11] roba che ti serve, non lo fare. Un'altra
[00:23:15] cosa da non fare, screenshot del testo.
[00:23:18] Se puoi incolla direttamente il testo,
[00:23:20] piuttosto che creati che se passi uno
[00:23:23] screenshot con il testo, allora con uno
[00:23:25] script che non consuma token si può
[00:23:27] prendere il testo. Dare PDF grezzi,
[00:23:30] l'abbiamo già detto, promptio
[00:23:33] perché spesso se diamo prompt corti
[00:23:35] senza dare il giusto contesto, pensiamo
[00:23:37] di salvare eh un pochettino mandando un
[00:23:40] prompto, ma non dando il giusto
[00:23:42] contesto. Clode non farà un buon lavoro,
[00:23:44] ci dobbiamo ripassare sopra, quindi
[00:23:45] andiamo a sprecare token. E occhio ai
[00:23:48] tool là fuori che promettono il 90% di
[00:23:50] risparmio. Li ho provati tutti Cavem RTK
[00:23:55] e veramente non sono nulla di che. Cavem
[00:23:58] ad esempio eh quello che fa è che questo
[00:24:01] è la risposta normale che ti darebbe
[00:24:03] Cloud, no? Ecco, lui ti dà un po' il il
[00:24:07] riassunto, ma spesso salta informazioni.
[00:24:10] Io l'ho testato, non c'è chissà quanto
[00:24:12] risparmi e se risparmi vi assicuro che
[00:24:14] l'esperienza peggiora tantissimo e
[00:24:16] spesso lascia cose fondamentali. Una
[00:24:19] cosa molto più intelligente è cambiare
[00:24:21] l'output style, cioè qua con in output
[00:24:24] style che qua purtroppo si può cambiare
[00:24:27] solamente da terminale, quindi qua sono
[00:24:28] su settings, vado su output style,
[00:24:32] possiamo cambiare. La cosa che ha molto
[00:24:36] più senso è mettere ad esempio conciso,
[00:24:38] cioè ci dà il risultato senza preamboli
[00:24:40] neioghi. non vi scaricate Caveman o RTK,
[00:24:44] la maggior parte di queste cose sono
[00:24:45] inutili, insomma, se volete testatele,
[00:24:47] ma la cosa migliore è scegliere un
[00:24:49] output style. Bene, andiamo a un altro
[00:24:52] punto fondamentale che è quando possiamo
[00:24:55] scegliamo delle Cli invece che degli
[00:24:57] MCP. La Cli è o Command line Interface,
[00:25:00] è essenzialmente, se volessi proprio
[00:25:03] dirlo in maniera brutale, un API, ma per
[00:25:06] i terminali. Allora, se vogliamo
[00:25:07] connettere software 1 a software 2, ci
[00:25:10] serve un ponte. Questo ponte si chiama
[00:25:12] API. Ci sono diversi metodi API, cioè eh
[00:25:15] questi ponti che abbiamo detto possono
[00:25:17] essere, che ne so, se io dal software 1,
[00:25:20] ops, software 1 che può essere eh Gmail
[00:25:23] e l'altro software 2 che può essere il
[00:25:24] nostro gestionale, possiamo avere la
[00:25:26] chiamata API, il metodo API, send email
[00:25:29] che mi manda un email, write draft che
[00:25:32] mi va a creare una bozza, read email,
[00:25:34] quindi abbiamo tantissimi metodi, no? e
[00:25:36] quando più opportuno andiamo a chiamare
[00:25:38] il metodo giusto, no? Cioè se voglio
[00:25:40] mandare unemail allora utilizzo il
[00:25:42] metodo send email. Se voglio leggerla
[00:25:44] allora utilizzo il metodo read email.
[00:25:46] Cosa fanno gli MCP? Si vanno a prendere
[00:25:49] tutti questi metodi e se li vanno a
[00:25:51] raggruppare in questa sorta di
[00:25:53] gigantesco ponte, quindi senza dover
[00:25:56] azzeccare il metodo giusto tramite gli
[00:25:57] MCP. Abbiamo come se fosse un mega
[00:26:00] wrapper, abbiamo tutti quanti i metodi,
[00:26:02] figo, semplifica tantissimo l'utilizzo,
[00:26:04] la la connessione fra i software, ma il
[00:26:06] problema è che quando questi metodi non
[00:26:09] sono tre, ma diventano tantissimi, noi
[00:26:13] magari vogliamo fare solo poche poche
[00:26:15] cose, cioè mandare unemail e leggere
[00:26:18] l'email e scrivere eh le bozze e
[00:26:21] automaticamente, come vedevamo prima, il
[00:26:22] server MCP li include tutti, il che non
[00:26:25] ha senso perché includendoli tutti
[00:26:26] andiamo a ingolfare il contesto con
[00:26:29] metodi che probabilmente non
[00:26:30] utilizzeremo, quindi vogliamo sfruttare
[00:26:33] solamente i metodi che ci servono a noi.
[00:26:35] Mi direte voi, "Ma allora perché i
[00:26:37] server MCP utilizziamo l'PI
[00:26:39] direttamente? Il problema è che le
[00:26:41] chiamate PI nascono per essere lette da
[00:26:42] umani." Questa è una classica risposta
[00:26:45] di una chiamata API. sembra complesso,
[00:26:47] ma è semplicemente ci dice tutte le
[00:26:50] informazioni della risposta perché così
[00:26:51] un umano può andare a leggere tutto
[00:26:53] quanto e capire la risposta che ci ha
[00:26:56] dato il software. Il problema è che
[00:26:58] tutta questa risposta che di solito è
[00:26:59] lunghissima, anche quella va a occupare
[00:27:02] il contesto delle I alla Context Window,
[00:27:04] no? nascono quindi le click command line
[00:27:07] interface dove risolve il problema dell
[00:27:09] MCP, cioè non si va a caricare a priori
[00:27:11] tutto quanto, ma risolve il problema
[00:27:12] dell'epi. La risposta il JSON se no, è
[00:27:14] troppo grossa. Risolvendo questi due
[00:27:16] problemi si utilizzano appunto le Clee,
[00:27:18] il linguaggio che era nato per i
[00:27:20] terminali commandline interface per
[00:27:22] questo. E quindi le CLE sono tanto
[00:27:24] tantissimo più efficiente eh delle API e
[00:27:28] dei e degli MCP, specialmente se
[00:27:31] utilizziamo appunto Cloud, Codex e
[00:27:32] quant'altro. Questo è un po' quello che
[00:27:33] vi dicevo, l'MCP, il manuale entra
[00:27:35] all'avvio, resta lì anche da spento e
[00:27:39] l'indice cresce ad ogni tool, la Cli è
[00:27:41] zero fino a che non la chiami. Il
[00:27:43] comando non occupa nulla. In una riga
[00:27:45] nel clode.md diciamo, guarda, hai
[00:27:46] accesso alla click di Gmail, eh, se ti
[00:27:48] vuoi connettere a Gmail è accesso a
[00:27:50] quello. Quindi, prima che scriviamo
[00:27:53] qualsiasi cosa, un MCP può occupare
[00:27:55] anche 26.000 token. La click solo 40
[00:27:57] token che è nel cloud. MD che si chiama,
[00:28:00] guarda, hai accesso alla click di Gmail.
[00:28:02] Quindi quando puoi usa una e non è un
[00:28:04] MCP. Che diavolo vuol dire? Mettiamo
[00:28:06] caso che ci vogliamo connettere a eh non
[00:28:08] lo so, Supase. Invece che fare Supase
[00:28:12] MCP e che ne so, passare questa questa
[00:28:14] documentazione a Cloud per farlo
[00:28:16] connettere, proviamo a cercare se c'è
[00:28:18] una clip che di solito è molto più
[00:28:20] efficiente o semplicemente a Cloud LC.
[00:28:22] Connettiamoci a questo software, usa una
[00:28:24] clip. Personalmente io come regola
[00:28:26] generale ho nel mio cloud cerca sempre
[00:28:28] se ci sono clipetto ad MCP. Oh, altra
[00:28:30] cosa veramente interessante, gli unici
[00:28:32] due tool che sono veramente tanta tanta
[00:28:35] roba sono Code Graph e grapy. Ho
[00:28:38] preparato una breve animazione che
[00:28:40] spiega il la forza di un grafo, nel
[00:28:43] senso che se noi dobbiamo ricercare una
[00:28:45] determinata informazione, mettiamo che
[00:28:47] l'informazione sia questo tassello qua,
[00:28:49] che cosa fa Cloud? va a ricercare tanti
[00:28:51] file fino a che non lo becca, mentre un
[00:28:53] grafo, siccome sono tutti i puntini
[00:28:55] connessi fra di loro e Clode ha accesso
[00:28:57] a tutti questi puntini, sa esattamente
[00:29:00] dove se lo va a prendere. Questa è un
[00:29:01] po' la differenza. Quindi prima di
[00:29:03] andare a cercare di trovare il punto
[00:29:05] deve leggersi tutti questi altri file,
[00:29:07] mentre con il grafo bom lo becca subito.
[00:29:09] Quindi senza grafo Cloud cerca tentoni
[00:29:13] per i più nerd lì fuori fa tutte quante
[00:29:16] read, fa tutte quante grap si chiamano.
[00:29:18] Apre un file, no, non è quello. Ok, ne
[00:29:20] apro altri cinque. Un riapertura consuma
[00:29:23] token, mentre con il grafo chi è c'è una
[00:29:25] mappa dove essenzialmente va dritto al
[00:29:27] nodo giusto, il file poi lo legge lo
[00:29:30] stesso. Ci sono due tool che si chiamano
[00:29:32] Code Graph e grapify. Per trovarle code
[00:29:35] graph Gab, eccolo qua. Basta che lo
[00:29:39] prendi e te lo installi, gli passi
[00:29:41] questa repositoria al tuo cloud e
[00:29:43] l'altro è grapy.
[00:29:47] Eccolo qua. Anche qua gli passi l'URL e
[00:29:49] te lo fai installare. Qual è la
[00:29:51] differenza? Entrambi trasformano tutti i
[00:29:54] tuoi file in un grafo, in questa mappa
[00:29:56] facilmente accessibile da Clode. Usa
[00:30:00] Code Graph per il codice. Se cioè
[00:30:03] essenzialmente se è una repositoria, se
[00:30:04] stai lavorando un software, un'app molto
[00:30:07] grossa, CODG graph è ottimizzata per il
[00:30:09] codice, anche perché va a trasformare
[00:30:12] del testo in un grafo.
[00:30:15] Rapy è ottimo per un brain, quindi
[00:30:17] quando invece dobbiamo trasformare in un
[00:30:19] grafo PDF, immagini, markdown, output di
[00:30:23] obsidian, riesce a trasformare comunque
[00:30:25] il grafo. Quindi grpify per il codice
[00:30:27] per base di codice, scusami, code graph
[00:30:29] per basi di codice, grapy per un brain.
[00:30:32] Cosa da sapere, sotto i 500 file non
[00:30:34] conviene nessuno dei due, il grafo ti
[00:30:37] costerà più di risparmiare. Quindi sotto
[00:30:39] 500 file eh non conviene crearsi un
[00:30:43] grafo. Altro trucco fondamentale è
[00:30:46] trasforma in codice dove è possibile,
[00:30:48] nel senso che ogni volta che facciamo
[00:30:50] fare qualcosa alle AI, a parte che non è
[00:30:52] deterministico, cioè è le hai, è per
[00:30:55] natura non è deterministica, ma ogni
[00:30:57] volta paghiamo dei token, ogni tanto si
[00:31:00] sbaglia, il risultato può cambiare dove
[00:31:02] puoi se trasformi un qualcosa in uno
[00:31:05] script, il codice spesso ce lo
[00:31:07] scordiamo, uno script di Python, uno
[00:31:09] script di qualsiasi linguaggio esso sia,
[00:31:11] consuma zero token. è velocissimo, non
[00:31:15] sbaglia mai e gira uguale ogni volta e
[00:31:17] quindi consuma zero token. Ovviamente il
[00:31:19] codice, essendo deterministico, non non
[00:31:22] dà un giudizio, non ti dice se un non ti
[00:31:25] riesce a categorizzare se unemail è spam
[00:31:27] o oppure di customer support, però ti
[00:31:31] assicuro che tantissimo che sia una
[00:31:33] skill, che sia un qualcosa che fai
[00:31:36] spesso, se lo riesci a trasformare da AI
[00:31:38] a codice vai a risparmiare tantissimo.
[00:31:41] Pensa che stavo avendo questo discorso
[00:31:43] con il CTO di Clickup, che è uno dei CRM
[00:31:46] più grossi del mondo, valutato a 4
[00:31:48] miliardi. Stavo in Montenegro eh con con
[00:31:51] il mio gruppo, insomma, un gruppo di
[00:31:53] creator, un network internazionale e il
[00:31:55] CTO di Clickup mi ha detto: "Questa è
[00:31:57] proprio la nostra regola aura, cioè
[00:31:58] aurea, cioè quando noi andiamo a
[00:31:59] costruire nuove featureal o qualsiasi
[00:32:02] cosa, andiamo a rivedere il codice, dove
[00:32:05] possiamo cambiare quella chiamata API a
[00:32:08] cloud, openi, quello che è in codice,
[00:32:11] dove possiamo farlo il più possibile
[00:32:13] perché è più veloce, non sbaglia e
[00:32:16] risparmi."
[00:32:17] Quindi lei serve per il giudizio, tutto
[00:32:19] il resto è esecuzione. Esecuzione
[00:32:22] ripetibile è codice. Per farlo basta
[00:32:24] lanciare un audit all'interno del tuo
[00:32:26] brain o all'interno di di della tua app
[00:32:29] o dovunque tu utilizzi le hai. Lanci un
[00:32:31] prompt dove essenzialmente devi fare un
[00:32:33] audit dove gli chiedi quali pezzi del
[00:32:35] tuo flusso non hanno bisogno di un
[00:32:36] modello. Quel diventano uno script,
[00:32:38] magari le skill, no? Spesso non serve
[00:32:41] far lavorare la tua usage cloud, ma
[00:32:42] serve uno script. Poi ogni ricordati di
[00:32:46] è un candidato di Hook, che è quella
[00:32:48] cosa deterministica di cui parlavamo
[00:32:50] prima. Fra l'altro Luke si triggera
[00:32:54] sempre quando gli diciamo che avviene
[00:32:56] sempre un certo evento. Che ne so,
[00:32:58] quando noi carichiamo il PDF
[00:33:00] automaticamente ogni volta succede
[00:33:03] quello script perché è un hook, un
[00:33:04] qualcosa di terministico. Se invece
[00:33:05] scriviamo, banalmente non avessimo fatto
[00:33:07] un hook, ma l'avessimo scritto nel
[00:33:09] cloud. MD può essere che una volta Clude
[00:33:12] non lo esegua perché è un prompt, non è
[00:33:14] deterministico. E l'ultima cosa che ci
[00:33:15] tenemo a dirti sono i sottoagenti.
[00:33:18] Spesso quello che vedi è che ti
[00:33:19] ritornano 420 token, sembra una
[00:33:22] vittoria, ma in realtà il tuo sotto
[00:33:25] agente probabilmente ha un ha un suo
[00:33:27] system prompt, ha la sua copia della
[00:33:29] memoria, cioè dove siamo arrivati con
[00:33:32] Clud a un certo punto della
[00:33:33] conversazione, i suoi strumenti
[00:33:34] permessi, la lettura vera e propria,
[00:33:36] quindi spesso non sono mai così pochi,
[00:33:38] ma spesso magari spendiamo 980 9800
[00:33:42] token per risparmiare i 5700, quindi
[00:33:45] quando utilizzare i sottoagenti
[00:33:47] solamente Per le azioni in bulk devi
[00:33:49] leggere 40 file, devi analizzare 10
[00:33:52] fonti. Eh, in quel caso allora utilizza
[00:33:56] i sottoagenti. Sennò no. Pro tip, i
[00:33:59] sottoagenti IQ vanno una bomba. Quindi
[00:34:02] io spessissimo quando le dico "Creami i
[00:34:03] sottoagenti per farlo", sottoagenti IQU,
[00:34:06] a meno che non devo fare un compito
[00:34:07] molto complesso, però sotto agenti Iu
[00:34:09] fanno veramente una favola. look, quello
[00:34:12] che ti ho detto da PDF a testo,
[00:34:14] ovviamente non è più un vantaggio se i
[00:34:16] tuoi PDF eh sono eh hanno tante
[00:34:19] immagini, schemi grafici che devi
[00:34:21] leggere. In tal caso però basta glielo
[00:34:23] dici, gli carichi il PDF, siccome look
[00:34:25] si triggera ogni volta, dici "Guarda,
[00:34:26] non eseguire quello script là perché
[00:34:28] questa volta devo analizzare i grafici".
[00:34:29] Altra cosa che ti volevo dire è quella
[00:34:31] lì sul grafo, cioè il grafo sotto i 500
[00:34:35] file non ha senso crearli, quindi non
[00:34:37] usare code, graph o grapify. Questo era
[00:34:39] tutto ciò che ti volevo dire,
[00:34:41] essenzialmente quasi tutto ciò che so
[00:34:43] sul risparmio dei token su Cloud Code.
[00:34:46] Va benissimo. Questi concetti si
[00:34:47] applicano anche a Codex, si applicano
[00:34:49] anche a qualsiasi altro codic agent tu
[00:34:51] utilizzi. Quindi se sei un'azienda e
[00:34:53] vuoi implementare l'intelligenza
[00:34:54] artificiale all'interno dei tuoi
[00:34:55] processi a partire dalla formazione del
[00:34:57] tuo team su strumenti pratici come Cloud
[00:35:00] Code, Cloud Cowork, Codex, offriamo fra
[00:35:02] l'altro anche percorsi di coaching sia
[00:35:04] singoli che dopo che facciamo la
[00:35:07] formazione facciamo dei coaching one to
[00:35:09] many a tutto il tuo team per continuare
[00:35:10] a tenerli formati sul lungo periodo.
[00:35:13] piuttosto se vuoi analizzare i tuoi
[00:35:14] processi per capire quali soluzioni hai
[00:35:17] costruire su misura per la tua realtà e
[00:35:19] poi costruire tali soluzioni. Non siamo
[00:35:22] l'azienda di consulenza che ti fa
[00:35:24] l'analisi dei processi e ti dà il deck
[00:35:26] di 200 pagine, ma andiamo ad eseguire e
[00:35:28] a costruire poi queste soluzioni che
[00:35:30] sono estremamente customizzate per la
[00:35:32] tua azienda. Se ti può interessare, come
[00:35:34] al solito, nel primo link in descrizione
[00:35:35] puoi prenotare una chiamata se ci vuoi
[00:35:37] parlare del tuo progetto. Questo è
[00:35:38] tutto. Fatemi sapere qui sotto che ne
[00:35:40] pensate e quali sono quei trick che
[00:35:43] magari non sapevate o che avete
[00:35:45] applicato e che vi hanno salvato
[00:35:46] tantissimi token.
