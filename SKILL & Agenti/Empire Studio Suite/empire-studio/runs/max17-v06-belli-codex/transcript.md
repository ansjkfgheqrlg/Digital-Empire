
[00:00:00] Tutti là fuori si chiedono se è meglio
[00:00:02] Cloud Code o Codex e secondo me è la
[00:00:05] domanda sbagliata. La vera domanda è:
[00:00:07] come posso ottenere il massimo da
[00:00:09] entrambi? Anche perché se volessimo
[00:00:11] davvero eleggere un vincitore, ogni
[00:00:13] volta che esce un nuovo modello
[00:00:14] cambierebbe la classifica e
[00:00:16] ricomincerebbe la guerra. Quindi in
[00:00:17] questo video voglio farti vedere come
[00:00:19] farli lavorare insieme. Ti mostro dove
[00:00:21] vince uno e dove vince l'altro, i
[00:00:23] comandi che servono davvero e poi voglio
[00:00:26] farti vedere un caso d'uso pratico per
[00:00:28] farti vedere io come li utilizzo
[00:00:29] insieme. Se è la prima volta che vedi
[00:00:31] questi video, sono un ingegnere
[00:00:32] informatico e gestisco Mart, un'azienda
[00:00:35] attraverso la quale aiutiamo le imprese
[00:00:36] a scalare implementando l'intelligenza
[00:00:38] artificiale all'interno dei loro
[00:00:40] processi. Partiamo dalla formazione del
[00:00:42] loro personale, dei loro key user, su
[00:00:44] strumenti pratici come Cloud Code, Cloud
[00:00:46] Cowork e poi andiamo a costruire
[00:00:48] soluzioni di intelligenza artificiale
[00:00:50] customizzate sulle esigenze
[00:00:51] dell'azienda. Ci poniamo infatti come un
[00:00:54] partner AI a 360°. Abbiamo lavorato
[00:00:57] ormai con più di 65 aziende, portato in
[00:00:59] produzione più di 75 soluzioni di
[00:01:01] intelligenza artificiale. E tutto questo
[00:01:02] per dirti che io e anche il mio team
[00:01:04] utilizziamo ogni giorno strumenti come
[00:01:06] Cloud Code e Codex. E questo è
[00:01:09] esattamente il metodo che stiamo
[00:01:10] utilizzando per sfruttare il meglio di
[00:01:12] [musica] entrambi. Senza perdere altro
[00:01:14] tempo passiamo subito al video. Come al
[00:01:16] solito ho preparato prima una lavagna
[00:01:17] per capire meglio quello di cui andremo
[00:01:19] a parlare, dove vince uno, dove vince
[00:01:21] l'altro e qual è il metodo che
[00:01:22] utilizzeremo in questo video. Cloud Code
[00:01:24] contro Codex. Cloud Code è fortissimo su
[00:01:27] tutta la parte di copywriting, design e
[00:01:29] gusto estetico. È molto forte a
[00:01:31] pianificare, avere una visione
[00:01:32] complessiva del progetto, anche quando
[00:01:34] magari non abbiamo un'idea chiara.
[00:01:36] scrive tanto codice e in fretta. Codex è
[00:01:38] un pochettino più lento secondo la mia
[00:01:39] esperienza personale e ha tutto
[00:01:41] l'ecosistema di skills, plugins, MCP,
[00:01:43] hook che a parer mio è superiore
[00:01:45] rispetto a quello di Codex. Codex, le
[00:01:47] sue forze che esegue alla lettera. Se
[00:01:50] gli dici di fare 1 2 3 4 e 5, farà 1 2 3
[00:01:53] 4 5, mentre Cloud Code ci prova a
[00:01:55] mettere sempre un po' del della sua
[00:01:57] idea, della sua iniziativa. Motivo per
[00:02:00] il quale Codex sta iniziando a spopolare
[00:02:02] anche su eh developer anche più esperti,
[00:02:05] developer senior, riesce a trovare più
[00:02:07] edge case, cioè quei casi specifici,
[00:02:09] magari quel pulsantino in alto a destra
[00:02:12] che fa crashare tutta l'applicazione.
[00:02:14] Per ogni cosa che fa riesce a vedere e a
[00:02:16] trovare delle conseguenze di secondo e
[00:02:18] terzo ordine e come dicevo prima è
[00:02:20] efficiente sulle modifiche mirate e la
[00:02:22] cosa più importante è che non è
[00:02:24] innamorato del codice come invece
[00:02:25] secondo me lo è Cloud. Infatti Cloud
[00:02:28] come debolezza è che si entusiasma, cioè
[00:02:30] ti dice fatto ma magari non ha neanche
[00:02:32] provato o testato end to end
[00:02:34] l'applicazione. Salta gli edge case, ti
[00:02:36] dà sempre ragione e si scrive testa da
[00:02:38] solo. Le debolezze di Codex invece sono
[00:02:40] che sul copia e sul design secondo me
[00:02:42] non ci siamo. vuoi le istruzioni più
[00:02:44] precise, secondo me Codex lo si sfrutta
[00:02:46] al meglio quando gli diamo istruzioni
[00:02:48] veramente precise. Motivo per il quale
[00:02:50] anche molti dei nostri ingegneri interni
[00:02:52] che non vi codano le cose, ma seguono
[00:02:54] determinati criteri e sanno esattamente
[00:02:56] cosa vogliono fare, stanno iniziando a
[00:02:58] preferire Codex. È un po' più lento a
[00:03:01] parer mio e un'altra cosa che in realtà
[00:03:04] qua non è inserito sono anche i limiti
[00:03:05] di utilizzi. Codex eh secondo la mia
[00:03:08] esperienza, sta marciando tantissimo su
[00:03:10] questa cosa e i limiti di Codex si
[00:03:12] sprecano molto più lentamente rispetto a
[00:03:15] quelli di Cloud Code. Il concetto che
[00:03:16] seguiremo oggi è che chi costruisce è
[00:03:18] diverso da colui che giudica e vogliamo
[00:03:20] sfruttare la caratteristica di Codex,
[00:03:22] ossia che non è innamorato del nostro
[00:03:23] codice. Che vuol dire? Questa è la
[00:03:25] metodologia principale, poi ovviamente
[00:03:26] ci sono altri comandi che possiamo
[00:03:27] eseguire. Il piano lo vogliamo far fare
[00:03:29] a cloud. Questo piano vogliamo che venga
[00:03:32] contestato da Codex. Il piano versione 2
[00:03:35] fatto da Codex va passato, va lo andiamo
[00:03:37] a revisionare sia a noi, ricordiamoci,
[00:03:39] non vogliamo affidarci completamente
[00:03:41] alle AI ed essere dei pipecoders
[00:03:43] seriali, ma l'obiettivo è sempre,
[00:03:46] sperabilmente capire quello che sta
[00:03:48] succedendo, sennò arriviamo a un punto
[00:03:49] dove quello che abbiamo costruito
[00:03:51] diventa un mostro incontrollabile.
[00:03:53] Questo piano poi viene ripassato a Cloud
[00:03:56] e continuiamo questo ciclo fino a che
[00:03:58] Codex non ha più niente da ridire. Tutto
[00:04:00] questo video si basa su questa
[00:04:02] repositoria di Gitab fatta ufficialmente
[00:04:04] da OpenI ed è il Codex Plugin.
[00:04:07] Essenzialmente ci permette di utilizzare
[00:04:08] Codex all'interno di Cloud Code. Infatti
[00:04:11] andremo a installare questo plugin qui e
[00:04:14] questi sono i cinque comandi
[00:04:16] fondamentali, quelli che useremo più di
[00:04:17] tutti. Primo comando/review.
[00:04:20] Tranquilli, dopo andiamo a installare
[00:04:21] questo plugin e andiamo a vedere come
[00:04:22] utilizzare questi comandi.
[00:04:23] Essenzialmente slreview ci va a fare una
[00:04:26] review dell'applicazione di quello che
[00:04:28] stiamo costruendo. Non accetta testo
[00:04:30] libero, quindi non gli possiamo dire
[00:04:31] nello specifico guarda questo bug,
[00:04:33] guarda questo piano che mi ha fatto
[00:04:35] Cloud, non lo puoi indirizzare su un
[00:04:37] punto preciso, quindi è ottimo quando
[00:04:38] vuoi fare magari una review generale
[00:04:40] della tua app, non il mio comando
[00:04:41] preferito. di default va a vedere tutte
[00:04:43] quelle modifiche non committate perché
[00:04:46] ovviamente se noi stiamo costruendo
[00:04:47] un'applicazione, un'automazione, una
[00:04:49] qualsiasi cosa su Cloud Code e siamo
[00:04:51] connessi a GitHub, che per chi non lo
[00:04:52] sapesse GitHub è come se fosse un Google
[00:04:54] Drive per il codice, tutte le ultime
[00:04:55] modifiche che non abbiamo pushato, che
[00:04:57] non abbiamo mandato sul nostro Drive,
[00:04:59] sul nostro Gitab, che di solito sono le
[00:05:01] feature alle quali stiamo lavorando in
[00:05:02] quel momento lì, lui va a vedere quelle
[00:05:05] modifiche là, quindi tutto ciò che non
[00:05:07] abbiamo commentato su BTAB/Adversarial
[00:05:10] review, lo stesso, ma lo puoi puntare
[00:05:12] addosso a qualcosa, quindi gli puoi dire
[00:05:14] cosa contestare, lui attacca quella
[00:05:16] scelta lì. Questo è esattamente quello
[00:05:18] che utilizzeremo per attuare questo
[00:05:19] meccanismo qua. Quindi gli possiamo
[00:05:21] passare il piano che ci ha generato
[00:05:23] Cloud. Ad esempio, quando sei bloccato
[00:05:25] perché c'è un determinato problema che
[00:05:27] magari Clode non sa risolvere. Slash
[00:05:29] rescue. È quello che fa essenzialmente
[00:05:31] prende il problema e lo prova a
[00:05:32] risolvere. Lui indaga, prova una
[00:05:34] correzione e prova a sbloccare il punto
[00:05:36] dove eravamo fermi. Questo anche è un
[00:05:38] comando fantastico. Quante volte
[00:05:41] utilizziamo Cloud e per qualche motivo
[00:05:42] magari si impappina nel senso che non
[00:05:45] riesce proprio a risolvere una certa
[00:05:47] cosa. Beh, in questo caso/codextrfer
[00:05:50] prende la conversazione che abbiamo in
[00:05:51] corso con Cloud e la porta dentro Codex
[00:05:53] continuando da dove eravamo. Questo è
[00:05:56] davvero davvero utilissimo. E questi
[00:05:59] sono i due comandi che andremo a vedere,
[00:06:00] cioè che ogni volta che noi lanciamo uno
[00:06:02] di questi comandi parte una una sorta di
[00:06:06] lavoro in background, che ne so, la
[00:06:08] review del codice, questaversarial
[00:06:10] review e con status possiamo vedere se
[00:06:13] Codex ha finito o meno e in tal caso se
[00:06:15] ha finito darci dei risultati, ma
[00:06:17] tranquilli, dopo andiamo a vedere tutto
[00:06:19] quanto. i due modi per usarli in
[00:06:21] pratica. Questa è la parte fondamentale
[00:06:23] perché è esattamente come utilizzo io
[00:06:25] personalmente Codex e come lo stiamo
[00:06:27] utilizzando anche interamente
[00:06:28] all'interno di Marttees. Quindi se non
[00:06:30] capite questa parte tutto il resto del
[00:06:31] video non avrà alcun senso. I due modi
[00:06:34] migliori sono uno far controllare
[00:06:36] un'applicazione prima di mandarla online
[00:06:38] e due, il piano prima di scrivere una
[00:06:40] riga. Allora, quando l'applicazione è
[00:06:42] pronta noi pensiamo di volerla mandare
[00:06:43] online. Quindi quello che possiamo fare
[00:06:45] è prima fare una review della nostra
[00:06:47] applicazione. Noi andiamo a revisionare
[00:06:49] la review. ricordiamoci quando vogliamo
[00:06:51] essere dei Vibe coders. Sono arrivato al
[00:06:53] punto e avevo questa conversazione con
[00:06:56] alcuni dei nostri ingegneri dove
[00:06:58] essenzialmente quello che vado a fare
[00:06:59] quando costruisco applicazioni, agenti,
[00:07:01] automazioni, quello che è la parte
[00:07:03] umana, secondo me inizia a diventare
[00:07:04] fondamentale solamente nella parte di
[00:07:06] revisione e il controllo dei piani
[00:07:08] dell'intelligenza artificiale. Poi per
[00:07:10] le altre cose Leai sta iniziando a
[00:07:12] raggiungere un livello eccezionale,
[00:07:15] quindi questa è fondamentale. Noi
[00:07:17] andiamo a rivedere, a revisionare la
[00:07:19] review e poi possiamo mandare online.
[00:07:21] Secondo pattern, facciamo il piano con
[00:07:24] Fable 5, un po' quello di cui parlavo
[00:07:26] nello scorso video, quello dove dicevo
[00:07:28] come usare Fable 5, come lo utilizzo io
[00:07:29] personalmente. Facciamo slashcodex
[00:07:32] adversarial review sul piano, quindi
[00:07:34] ricordiamoci che addversario a review
[00:07:37] fa un controllo generale. Adversale a
[00:07:39] review su una cosa specifica. Andiamo a
[00:07:40] controllare il piano, le critiche ci
[00:07:43] tornano a Cloud. Abbiamo un piano
[00:07:44] versione 2. Ritorniamo fino a che non ha
[00:07:47] più obiezioni. C'è l'umano qua dentro
[00:07:49] che va a rivisionare i controlli di
[00:07:51] Codex. Solo ora poi quando diamo l'ok e
[00:07:54] anche quando Cloud non ha nulla da
[00:07:55] ridire, mandiamo live dove per mandarlo
[00:07:58] live vuol dire che si inizia veramente a
[00:08:00] scrivere il codice e in quel caso la
[00:08:01] palla ripassa a Cloud Code e la palla
[00:08:04] può ripassare a Codex quando abbiamo un
[00:08:08] bug, quando Clode si impappina e non
[00:08:10] sappiamo più e non riesce più a
[00:08:11] risolvere un problema per qualche
[00:08:12] motivo. spesso succede quando magari
[00:08:14] arriviamo occupiamo tantissimo contesto
[00:08:16] oppure siamo arrivati quasi al limite di
[00:08:18] utilizzo di cloud oppure quando gli
[00:08:20] vogliamo far fare la review del lavoro
[00:08:22] che stiamo facendo attualmente. Molto
[00:08:25] bene, passiamo subito a installare
[00:08:26] questo plugin. Dovete cercare
[00:08:28] essenzialmente Codex Plugin, vi apparirà
[00:08:33] sulla prima la prima repo di Gitab,
[00:08:35] questa ufficiale di Openi e dobbiamo
[00:08:37] rannare questi comandi. Se siete proprio
[00:08:39] pigri e potete passare questa cloud code
[00:08:41] e farlo fare a lui. mi trovo all'interno
[00:08:43] di Visual Studio Code, quindi
[00:08:45] prerequisiti dobbiamo avere Visual
[00:08:47] Studio Code e Cloud Code. Quindi, se non
[00:08:50] ce l'avete, cercate su Visual Studio
[00:08:51] Code download e Cloud Code download,
[00:08:53] però insomma se state vedendo questo
[00:08:54] video immagino abbiate entrambi. Siamo
[00:08:57] all'interno di Cloud Code. Clicchiamo
[00:08:58] qui in alto terminale, nuovo terminale.
[00:09:01] Qui ingrandisco un pochettino e mi metto
[00:09:04] questo sopra. Seguiamo questi comandi
[00:09:06] qua. Prima di tutto dobbiamo lanciare
[00:09:09] Cloud e lanciamo questo qua slplugin.
[00:09:13] Abbiamo aggiunto il nostro plugin.
[00:09:16] Dovrebbe averlo già installato.
[00:09:18] Ah no, aggiunto il plugin, ma adesso lo
[00:09:20] dobbiamo installare questo. Metto
[00:09:21] install for you. Torno indietro,
[00:09:23] ricarichiamo i plugin. E adesso in
[00:09:25] teoria se faccio slugins
[00:09:29] dovremmo vedere questo qua di codex.
[00:09:32] Codex.
[00:09:33] Ups, ancora non c'è. Proviamo a fare
[00:09:36] slit
[00:09:38] di ricarico cloud. Non ho fatto
[00:09:39] nient'altro che chiudere un terminale,
[00:09:41] riaprire un terminale con exit e lancio
[00:09:44] slcecodex setup. Eccolo qua. Ecco qua,
[00:09:47] sta facendo il setup di Codex, quindi in
[00:09:50] teoria adesso dovremmo fare l'accesso al
[00:09:52] nostro account di Openi, quindi cosa che
[00:09:55] poi accendernerò meglio prima, ma
[00:09:56] essenzialmente eh come lo sfrutto io
[00:09:58] questo abbinamento? Il consiglio che do
[00:10:00] sempre è di avere il piano max di Cloud
[00:10:03] Code, se lo usate veramente noi lo
[00:10:05] usiamo per lavoro, ad esempio, quindi
[00:10:07] abbiamo il piano max e di sfruttare eh
[00:10:10] Codex con questo plugin. Quindi in
[00:10:12] realtà basta semplicemente il piano da
[00:10:13] €100, $100, il piano da $20. Molti di
[00:10:16] voi che state guardando questo video,
[00:10:17] forse avete solamente quello da $100, ma
[00:10:20] solamente con un'aggiunta di $20 e Openi
[00:10:22] non mi sta pagando per dire queste cose,
[00:10:24] ovviamente la qualità aumenterà
[00:10:26] esponenzialmente, fidatevi di me. Adesso
[00:10:28] andiamo a provare determinate cose, ma
[00:10:29] poi lo proverete e sarà veramente, vi
[00:10:31] assicuro, un'altra cosa la qualità del
[00:10:33] lavoro che tirerete fuori. Qua diciamo
[00:10:36] di installare Codex. Bene, ha finito di
[00:10:38] installarsi, quindi adesso dobbiamo fare
[00:10:40] il login. Dobbiamo fare punto
[00:10:42] esclamativo codex login. Eccolo qua.
[00:10:45] Ottimo, ho fatto il login con il mio
[00:10:47] account di CGPT e quindi siamo pronti.
[00:10:50] Molto bene. Adesso io ho due
[00:10:52] applicazioni e prima di mandarle online
[00:10:54] voglio far fare una review a Codex. Solo
[00:10:57] che in questo caso non è che ci sto
[00:10:58] lavorando adesso al codice, quindi non
[00:11:01] utilizzerò Slashcodex Review, ma
[00:11:03] utilizzerò Rescue perché ricordiamoci
[00:11:05] che Review va a vedere quelle modifiche
[00:11:08] che non sono committate su Gitab, quindi
[00:11:10] mi risponderebbe "Guarda, non c'è nulla
[00:11:12] da vedere perché tutte le modifiche sono
[00:11:14] già commentate e ho già finito la mia
[00:11:16] applicazione". Quindi importantissimo,
[00:11:18] perché questa è la differenza che tutti
[00:11:20] sbagliano. Tutti i video online che ho
[00:11:22] visto sbagliano questa differenza qui è
[00:11:24] che se voglio far vedere l'applicazione
[00:11:26] che è già finita, allora dobbiamo fare
[00:11:28] slashcodex rescue. Voglio analizzare due
[00:11:31] repositori prima di mandarle online. Il
[00:11:33] primo tool è uno di cui vado veramente
[00:11:35] veramente fiero. Non l'ho costruito io
[00:11:37] personalmente, l'ha costruito il nostro
[00:11:39] CTO. Essenzialmente abbiamo ricreato
[00:11:42] completamente many chat. nello specifico
[00:11:45] io noi facciamo tanti video dove scrivo
[00:11:47] "Commenta X e ti mando Y in privato"
[00:11:50] specialmente su Instagram e pagavamo
[00:11:52] Many chat-80 al mese per fare questo
[00:11:54] giochetto. Non solo, ma poi le API di
[00:11:56] Many ci stavano strette, quindi abbiamo
[00:11:59] detto "Ma sai che c'è? Ricostruiamoci
[00:12:01] Many" e questo essenzialmente è many
[00:12:03] ricreato. Qui ci sono tutti quanti le
[00:12:07] animazioni. Ad esempio, questo è il mio
[00:12:08] ultimo reil. commenta repo e ti mando
[00:12:11] tutte questi questi dettagli qua. Questi
[00:12:14] sono tutti i reil, ci sono due anche
[00:12:17] schedulati, cosa che non si può fare ad
[00:12:19] esempio col main chat, creare
[00:12:20] un'automazione
[00:12:22] per un rel schedulato. Qui ci sono le
[00:12:23] impostazioni e quant'altro. Insomma, un
[00:12:25] un'applicazione di cui vado super super
[00:12:27] fiero. Il nostro CTO ha fatto un lavoro
[00:12:29] pazzesco. Ma detto ciò, prima di
[00:12:31] mandarla live, perché magari questa
[00:12:32] potrebbe essere interessante per alcuni
[00:12:34] dei nostri clienti, voglio farla
[00:12:36] revisionare da Codex. Altra cosa, quindi
[00:12:38] questa è un'applicazione proprio che
[00:12:39] andrà in produzione, c'è questo form
[00:12:42] interattivo che può sembrare molto
[00:12:43] semplice, ma in realtà è abbastanza
[00:12:44] complesso. A parte che ci sono a
[00:12:46] animazioni grafiche, è il form delle
[00:12:49] nostre candidature. Abbiamo ricreato
[00:12:51] essenzialmente type form anche per qua,
[00:12:52] anche qua perché non ci va di pagarlo,
[00:12:54] ce lo ricostruiamo in house e questo è
[00:12:56] il form che facciamo compilare alle
[00:12:57] persone che vorranno lavorare con noi.
[00:12:59] Infatti, piccola parentesi, stiamo
[00:13:01] assumendo questi ruoli qua, stiamo
[00:13:04] cercando questi ruoli qua. Quindi,
[00:13:07] piccola parentesi, se ti può interessare
[00:13:09] uno di questi ruoli o se conosci una
[00:13:11] persona che può essere interessate, vai
[00:13:13] su candidature.com.mmartessai.com.
[00:13:15] Comunque lo lascio anche in descrizione.
[00:13:17] Chiusa parentesi. Questo può sembrare un
[00:13:19] form molto semplice, ma in realtà è
[00:13:21] interattivo, è piuttosto complesso.
[00:13:22] Cioè, se io clicco formatore,
[00:13:25] gli do un nome, gli do unemail a caso e
[00:13:29] gli do un numero di telefono,
[00:13:32] ehm mi andrà a fare delle domande dopo
[00:13:36] queste qua generali, delle domande
[00:13:39] specifiche se ho scelto ovviamente il la
[00:13:42] se ho scelto formatore piuttosto che se
[00:13:43] ho scelto sviluppatore e quant'altro.
[00:13:45] come ti piacerebbe collaborare con noi,
[00:13:47] da quanto conosci Cloud Code, perché è
[00:13:49] lo strumento che con cui lavoriamo
[00:13:51] durante le formazioni
[00:13:53] e e insomma qua. Quindi può sembrare un
[00:13:56] form veramente stupido, ma non è per
[00:13:58] niente banale e ovviamente prima di
[00:13:59] mandarla in produzione voglio farmi la
[00:14:02] revisione da Codex. Bene, come fare?
[00:14:04] Allora, qua prima di tutto mi faccio
[00:14:06] slash clear, poi non ho aperto nessun
[00:14:09] progetto qui, ok? Quindi devo aprire una
[00:14:11] cartella. Apro prima di tutto Myly, che
[00:14:13] è quel codice essenzialmente, cioè
[00:14:15] quella quell'applicazione che funge da
[00:14:17] Man chat. Ecco qui, ad esempio, ho
[00:14:19] aperto M reply. Quindi la prima cosa che
[00:14:22] faccio è mi apro un terminale
[00:14:26] e mi digito clod.
[00:14:29] Quindi quello che voglio fare è
[00:14:30] revisionare la mia app. Quindi faccio
[00:14:33] slcecodex
[00:14:35] rescue e se io faccio questo vediamo che
[00:14:39] ci sono determinati parametri che
[00:14:41] possiamo riempire. Se andiamo sulla
[00:14:43] documentazione di Gitab essenzialmente
[00:14:45] ci dice che supporta tutti questi
[00:14:47] parametri qua, dove per farla breve,
[00:14:49] sinceramente io quello che faccio è
[00:14:51] semplicemente background, cioè lo eseguo
[00:14:54] in background in modo tale che io posso
[00:14:56] continuare a fare un altro lavoro.
[00:14:58] Quindi che cosa succederà? È come se
[00:15:00] spawnasse una un agente in parallelo di
[00:15:02] Codex che va a fare la revisione
[00:15:03] dell'app, motivo per il quale poi dopo
[00:15:05] potremmo fare status per vedere se la
[00:15:07] gente ha finito. Quindi rescue meno men
[00:15:10] background. Ho scritto poi questo prompt
[00:15:12] codex e rescue meno meno background. Fai
[00:15:14] un audit completo di questa app. È molto
[00:15:16] utento e costodisce gli account
[00:15:18] Instagram dei clienti. Cioè ovviamente
[00:15:19] se lo passa un cliente dovrà fare il
[00:15:21] login con il suo account Instagram.
[00:15:23] Concentrati su potenziali falle. Siccome
[00:15:24] voglio lanciarla in Prod. Ad esempio, se
[00:15:26] un utente può vedere e toccare i dati di
[00:15:27] un altro, come sono protetti gli accessi
[00:15:29] di Instagram, cosa può far partire un DM
[00:15:32] sbagliato doppio, eccetera eccetera.
[00:15:34] Mando dunque questo pronto. Ecco qua che
[00:15:37] ci dice che sta passando la richiesta ad
[00:15:39] un sotto di codex e adesso è partito in
[00:15:43] background, siccome abbiamo messo sl
[00:15:46] background, quindi teoricamente adesso
[00:15:47] ne potremmo fare altro nel frattempo. E
[00:15:50] ricordiamoci che tutti i nostri
[00:15:52] sottoagenti li possiamo vedere. Qua
[00:15:54] metto un pochettino più grande. Qua
[00:15:56] abbiamo main che essenzialmente è dove
[00:16:00] questo il prompt che mandiamo lo
[00:16:02] manderemo all'agente.
[00:16:04] Ricordiamoci che adesso noi siamo su
[00:16:06] main, cioè la richiesta che andremo a
[00:16:08] fare adesso andrà all'agente principale.
[00:16:11] Poi adesso insomma tutti quei puntini
[00:16:12] stanno a significare sotto agenti. In
[00:16:15] questo caso non c'è più perché molto
[00:16:16] probabilmente ha finito. Comunque per
[00:16:18] controllare lo status basta fare questo.
[00:16:21] questo comando qui per controllare
[00:16:23] effettivamente a che punto sta
[00:16:24] quell'agente. Quindi vedete che adesso
[00:16:26] quello che ci va a dire è che lo status
[00:16:29] di questo agente è che è running, quindi
[00:16:32] sta ancora rannando e possiamo vedere
[00:16:34] volta per volta che cosa sta
[00:16:36] controllando. Ho rannato un'ultima volta
[00:16:39] lo status e adesso mi dice completo.
[00:16:41] Quindi come faccio a vedere eh il
[00:16:43] risultato? mi basta fare slashcodex
[00:16:46] result e l'ID dell'agente. Quindi,
[00:16:48] comunque, me lo consigliava anche qui.
[00:16:50] Ed ecco qua, sommare esecutivo. Ha
[00:16:52] identificato zero fa le critiche certe,
[00:16:55] due falle alte, due falle medie e due
[00:16:57] falle basse. Ok? Considerate che Cloud
[00:16:59] Code mi aveva detto che questa
[00:17:00] applicazione era pronta per essere
[00:17:02] mandata in produzione, quindi uno dei
[00:17:04] problemi era che l'autenticazione mail e
[00:17:06] password non aveva una verifica delle
[00:17:08] mail. Ah, ok. Un attaccante può
[00:17:11] registrare preventivamente l'indirizzo
[00:17:12] email della vittima usando una password
[00:17:14] sotto il proprio controllo. Impedisce
[00:17:16] alla vittima di registrarsi normalmente
[00:17:18] con quell'email. Se l'attaccante ottiene
[00:17:20] un URL token di invito destinato alla
[00:17:22] vittima, può attaccarlo usando l'account
[00:17:23] preregistrato. Wow! Ok, questo che
[00:17:26] impatto ha? Accesso a workspace della
[00:17:28] vittima, inclusi conversazioni
[00:17:29] Instagram, automovazioni, questo eh
[00:17:32] capisco perché dice che adesso che è una
[00:17:34] falla alta. Come dice di fixare, rendere
[00:17:37] obbligatoria la verifica email prima di
[00:17:39] considerare utilizzabile un account
[00:17:41] email password. Rifiare l'accettazione
[00:17:43] degli inviti se l'email della sessione
[00:17:44] non è verificata. Quindi, ok, mi dice
[00:17:46] tutta quest'altra cosa. Alta DM
[00:17:48] duplicati per assenza di claim atomico
[00:17:49] prima dell'invio. Che vuol dire? Ok,
[00:17:52] questa è un pochettino più tecnica, però
[00:17:53] comunque potrebbe portare eh DM
[00:17:57] duplicati allo stesso utente, risposte
[00:17:58] pubbliche duplicate, doppio consumo del
[00:18:01] budget meta. Ok, questa tanta roba. C'è
[00:18:04] un endp il quale mandiamo il messaggio
[00:18:06] diretto, il messaggio di Instagram
[00:18:08] diretto. Ricordiamoci che questo è è un
[00:18:10] è una replica di Many chat dove andiamo
[00:18:12] a mandare la risorsa su Instagram al
[00:18:15] all'utente. Questa funzione qua quello
[00:18:17] che fa è che va a mandare il messaggio
[00:18:20] la risorsa su Instagram. non controlla
[00:18:23] l'ID del recipiente, il messaggio.
[00:18:25] Questo vuol dire che un admin, una
[00:18:27] sessione rubata, anche un client u
[00:18:29] difettoso può chiamare ripetutamente
[00:18:31] l'end point e inviare tantissimi
[00:18:33] messaggi contro i limiti mantenuti.
[00:18:34] Impatto spam, quindi un attaccante
[00:18:36] potrebbe entrare all'interno del di un
[00:18:38] cliente e spammare le persone a cui
[00:18:40] mandare le risorse in DM, per cui
[00:18:42] insomma problemi di rate limiting. E ci
[00:18:44] sono altre, ad esempio, questo che
[00:18:46] potrebbe esserci un abuso del dominio di
[00:18:48] Mariply per fishing e danno
[00:18:50] reputazionale. Ok. Qua c'è tanta tanta
[00:18:52] roba, quindi capite bene che queste sono
[00:18:55] tutte falle che Cloud Code non mi aveva
[00:18:56] trovato. Ora apro una nuova finestra
[00:18:59] perché voglio farmi controllare il form
[00:19:01] interattivo, quello delle candidature.
[00:19:03] Ok, ho aperto questo form che ovviamente
[00:19:05] c'è molta molta meno roba. Mi creo anche
[00:19:08] qua un altro terminale e stessa storia.
[00:19:11] Prima vado su Cloud e ho preparato
[00:19:14] questo promptare un audit completo
[00:19:16] dell'app e essenzialmente ci sono alcune
[00:19:19] potenziali file, nel senso le persone
[00:19:21] mandano il CV come allegato e tutto
[00:19:23] finisce su Air Table che è il nostro
[00:19:24] CRM. Ad esempio, se cosa può essere
[00:19:27] caricato e chi può leggere quei file, se
[00:19:30] qualcuno può chiamare l'end point e
[00:19:31] mandare centinaia di candidature in un
[00:19:33] minuto, come sono trattati i dati
[00:19:34] personali dei candidati, insomma anche
[00:19:36] qua vogliamo andare a scovare potenziali
[00:19:40] falle come abbiamo fatto in precedenza,
[00:19:42] quindi anche qua sappiamo ormai che cosa
[00:19:45] sta succedendo.
[00:19:47] Abbiamo l'agente dall'altra parte che è
[00:19:50] stato mandato, l'agente di Codex e
[00:19:53] quindi aspettiamo che finisca il lavoro
[00:19:55] per noi. Come al solito ci passa anche
[00:19:57] il task, quindi dovrebbe essere questo
[00:20:00] l'ID o ci passa proprio qua il comando,
[00:20:02] quindi basta copiarci il nostro comando
[00:20:04] per controllare ogni volta a che punto
[00:20:07] siamo. E ci dice che l'audit è ancora in
[00:20:09] corso. Codex ha appena finito di mappare
[00:20:11] la struttura dell'app, lo stato di git,
[00:20:13] quindi sta iniziando a leggere i file.
[00:20:14] Perfetto. Volevo dirvi una cosa molto
[00:20:16] interessante, cioè se noi facciamo
[00:20:18] slodex
[00:20:20] rescue, oltre a background che abbiamo
[00:20:22] già visto, c'è sia l'effort che possiamo
[00:20:26] mettere, quindi minimal, low, medium,
[00:20:28] high, x high e anche il modello. Quindi,
[00:20:31] ad esempio, guardate qua, noi potremmo
[00:20:33] mettere modello, il nome del modello. Ad
[00:20:35] esempio, attualmente nel momento in cui
[00:20:37] sto registrando questo video, il miglior
[00:20:38] modello è 5.6 Sol. Potremmo prendere
[00:20:40] quello e mettere una determinata effort.
[00:20:42] Quindi, se vogliamo andare ancora ancora
[00:20:44] più pesanti, basta fare meno meno model.
[00:20:47] Eh, GPT 5.6
[00:20:50] Sol, dovrebbe essere così la sintassi,
[00:20:52] sì. GPT numero trattino, ok? con anche
[00:20:56] l'effort, quindi effort e potremmo
[00:21:00] mettere Xi, ad esempio, insomma, se
[00:21:02] vogliamo fare un qualcosa di andarci giù
[00:21:05] pesante. Ha finito l'audit, quindi per
[00:21:08] darvi il risultato vi basta mandare
[00:21:11] Codex Result con l'ID del nostro agente
[00:21:14] e ci dice nessun finding critico, però
[00:21:16] c'è un problema alto, anzi più problemi
[00:21:19] alti. Ok, andiamola a revisionare prima
[00:21:21] di mandare tutto quanto in production. E
[00:21:24] ripeto, anche qui, prima di mandare le
[00:21:26] cose in produzione, avevo fatto fare una
[00:21:28] review a Cloud Code, mi aveva detto
[00:21:29] "Vai, vai tranquillo" e meno male che ho
[00:21:31] chiamato Codex. Guardate che cosa
[00:21:34] abbiamo visto, cioè punto numero uno,
[00:21:36] end point pubblico prima di protezione
[00:21:37] antiabuso. Anche qua quindi problemi di
[00:21:40] rate limit, nel senso che un bot manda
[00:21:42] 200.000 candidature, no? Quindi
[00:21:44] consumando quote di cloudfare e di air
[00:21:47] table. Tutto questo è ostato su
[00:21:49] Cloudfare questo codice upload
[00:21:51] completamente lato server, cioè
[00:21:53] chiamando direttamente l'end point si
[00:21:55] possono caricare eseguibili archivi
[00:21:57] HTML, malware o file molto più grandi.
[00:21:59] Beh, questo non è per niente banale.
[00:22:02] Nessun limite server side al limite
[00:22:05] della dimensione dei payload, cioè ci
[00:22:07] possono mandare un documento gigantesco
[00:22:09] e altre problematiche, quindi medie,
[00:22:13] errori di air table, possibili cose,
[00:22:15] insomma qua abbiamo trovato un bel po'
[00:22:17] di roba. Meno male che ho rannato questa
[00:22:18] cosa prima di mandarlo live, quindi
[00:22:20] quello che farò adesso è ottimo. Voglio
[00:22:24] che fixiamo tutti questi problemi.
[00:22:27] Ovviamente prima leggiamo tutti quanti,
[00:22:29] ad esempio alcune cose prima che mi
[00:22:30] aveva detto di Myply. eh un fix non lo
[00:22:34] andrò a fare che è quello del doppio DM,
[00:22:36] perché in pratica che succede? Quando
[00:22:39] mandiamo una risorsa una persona, se
[00:22:40] clicca il pulsante gli arriva una
[00:22:42] risorsa, se uno clicca due volte il
[00:22:44] pulsante gli arriva due volte la
[00:22:45] risorsa. Ma sti cavoli, cioè magari una
[00:22:47] persona non per qualche modo vuole avere
[00:22:49] un'altra volta la risorsa, quindi non è
[00:22:51] un qualcosa che implementerò.
[00:22:53] Questo sta questo sta un po' a provare
[00:22:55] quello che dicevo prima. Non vogliamo
[00:22:56] fare i Vibe coders, ma tutte queste cose
[00:22:58] che ci dice Cloud ha senso dargli una
[00:23:01] letta prima poi di attuare tutti questi
[00:23:03] cambiamenti. Dunque, abbiamo visto
[00:23:05] questo. Prima di mandarlo online andiamo
[00:23:07] a vedere quest'altro, cioè il piano
[00:23:09] prima di scrivere una riga di codice. Ho
[00:23:11] questo piano che mi sono fatto scrivere,
[00:23:13] posso farvi vedere la preview un
[00:23:15] pochettino fatta meglio, [sbuffare]
[00:23:17] che quello che voglio fare è replicare
[00:23:19] Bitly, che essenzialmente è un software
[00:23:21] che ti permette di abbreviare i tuoi
[00:23:23] link quando, che ne so, un link è
[00:23:26] gigantesco perché dentro dobbiamo
[00:23:27] mettere i parametri di tracciamento, è
[00:23:29] bruttino da vedere. Quindi volevo creare
[00:23:30] una piattaforma tipo Bitly che ti
[00:23:32] accorcia quel link, ma comunque ti
[00:23:34] traccia i click, che ne so, banalmente
[00:23:36] se una persona sotto un mio video eh
[00:23:39] prenota una determinata call, voglio
[00:23:41] vedere le statistiche da quali video
[00:23:43] magari portano più clienti, no? E quindi
[00:23:46] questo è il motivo per il quale il
[00:23:47] tracciamento è così importante e volevo
[00:23:49] ricreare Bitlin senza doverlo pagare
[00:23:51] perché secondo me è una cavolata
[00:23:52] ricrearlo e mi sono fatto fare questo
[00:23:54] piano. Ora questo piano è estremamente
[00:23:56] semplice. Idealmente anche per una
[00:23:58] piattaforma più complesso quello che
[00:24:00] vogliamo fare è farci fare il piano da
[00:24:02] Fable 5, quindi qui terminale abbiamo
[00:24:06] questo piano qui clod. Idealmente io
[00:24:09] quello che faccio all'inizio di ogni
[00:24:10] progetto è vado a fare slashmodel e me
[00:24:14] lo vado a mettere su Fable per crearmi
[00:24:16] il piano. Ora in questo caso resto su
[00:24:18] Opus perché il piano l'ho già creato e
[00:24:20] quindi quando vado a sviluppare io uso
[00:24:22] Opus, non uso Fable ovviamente. E quello
[00:24:24] che voglio fare quindi è questo. Codex
[00:24:26] Adversarial Review in background
[00:24:29] contesta questo piano. Voglio creare un
[00:24:30] socia di Bitly e ovviamente gli voglio
[00:24:32] passare il piano. Quindi faccio
[00:24:34] chiocciola. chi@ciola ci può ci può
[00:24:37] permettere di taggare i file. Vedete,
[00:24:39] abbiamo diversi file e li passo plan.
[00:24:43] che è il nome di questo file. Questo è
[00:24:45] un modo per passare i file. Oppure
[00:24:47] un'altra cosa che si potrebbe fare è
[00:24:48] semplicemente fare tasto destro, copia
[00:24:51] il percorso e glielo passiamo così,
[00:24:53] insomma, così lo capisce in entrambi i
[00:24:56] modi. Ma lanciamo nel frattempo questa
[00:24:59] revisione del piano e mentre Cloud
[00:25:01] finisce di resolding, abbiamo lanciato
[00:25:04] la review nel background, ormai sappiamo
[00:25:06] come funziona. Ecco qua, dopo un po' ha
[00:25:08] finito di revisionare tutto il piano e
[00:25:09] va a trovare essenzialmente una serie di
[00:25:11] cose, cioè l'autenticazione è descritta,
[00:25:14] ma il piano non richiede get, stats e
[00:25:16] delete vincono ogni query. Quindi ora io
[00:25:19] quello che faccio prima di tutto gli
[00:25:20] diamo una riletta al piano, poi quello
[00:25:22] che facciamo è slashmodel e ci andiamo a
[00:25:26] scegliere e a Fable gli dico controlla
[00:25:29] queste obiezioni che ha fatto Codex al
[00:25:34] nostro piano plan MD per ricreare Bitly.
[00:25:40] Mandiamo Fable e quindi Fable va a
[00:25:43] vedere le obiezioni che ha fatto eh
[00:25:45] Codex, nel senso questa fondata, questa
[00:25:49] fondata, questo fondata, ma gonfiata, il
[00:25:51] fix è banale, questo fondata, eh delle
[00:25:54] P, ordine di implementazione respingo in
[00:25:56] gran parte. Quindi in questo caso, ad
[00:25:58] esempio, me lo vado a leggere un attimo
[00:25:59] meglio. Costruire un API di post
[00:26:01] dellautenticazione è normale sviluppo.
[00:26:04] Ok, vero. Il rischio reale che Codex
[00:26:06] descrive record senza owner è già
[00:26:08] coperto fixando il punto unico. In
[00:26:10] sintesi, quattro obzioni su cinque hanno
[00:26:12] un nucleo valido. In questo caso sono
[00:26:14] d'accordo, quindi le dico bene, applica
[00:26:18] tali correzioni Fable. Quindi adesso mi
[00:26:20] andrà a fixare il piano. E qual è il
[00:26:23] prossimo step? SLAmel. Cambio modello,
[00:26:26] vado su Opus, continuo lo sviluppo con
[00:26:29] Opus fino ad arrivare a un punto dove
[00:26:32] posso andare in produzione. Prima di
[00:26:34] andare in produzione mi faccio sia una
[00:26:37] review con Cloud, spessissimo io mi vado
[00:26:39] a fare una security review/security
[00:26:42] review, eccola qua. Che mi vado a fare
[00:26:45] un controllo con Codex. Altra cosa
[00:26:48] importantissima, altro comando che a me
[00:26:49] piace tantissimo è questo qua,
[00:26:52] transfer, cioè quando Cloud proprio non
[00:26:55] riesce a aggiustare qualcosa, proprio si
[00:26:58] impappina, allora trasferisco la
[00:27:01] conversazione da quel punto lì a Codex
[00:27:03] per provarla a fare aggiustare a lui.
[00:27:06] Oppure un'altra cosa è nel frattempo che
[00:27:09] sto costruendo le cose vado a fare
[00:27:11] slccex review. Ricordiamoci che review
[00:27:14] va a controllare tutto ciò che non è
[00:27:15] stato committato su Gitab, quindi quindi
[00:27:17] mentre sto costruendo la mia
[00:27:19] applicazione, se voglio dare una passata
[00:27:21] a Codex, allora posso fare anche la
[00:27:24] review. Però se vi devo dire la verità,
[00:27:25] io quello che utilizzo di più di tutti è
[00:27:28] questo per fare le audit, questo per i
[00:27:31] piani, fondamentale questo, ma anche
[00:27:34] questo qui dell'Audit, avete visto? E
[00:27:36] questo quando Cloud proprio si
[00:27:37] impappina. Questi sono i miei tre
[00:27:39] comandi preferiti. Questi, vabbè, sono
[00:27:40] di contorno per vedere Codex a che punto
[00:27:42] sta. Applicate tutti i fix al piano.
[00:27:44] Quindi adesso il piano è molto più
[00:27:46] completo. Passiamo quindi alla domanda
[00:27:48] che sicuramente ti starei facendo. Ma
[00:27:50] quindi fammi capire, tutto bellissimo,
[00:27:52] eh, ma io dovrei pagare $200 per Cloud e
[00:27:54] $200 magari anche per Codex, no? a meno
[00:27:57] che non sei un ingegnere full time che
[00:28:00] fa solamente questo e dalla mattina alla
[00:28:03] sera deve shippare software per i propri
[00:28:05] clienti. La cosa che io consiglio è
[00:28:08] questa coppia qua, cioè la il piano da
[00:28:11] $100 di Cloud Max e il piano da $20 di
[00:28:15] Codex, nel senso, abbiamo Cloud che
[00:28:17] scrive e Codex che controlla.
[00:28:19] Attualmente agosto 2026 questa credo sia
[00:28:23] la coppia migliore. Potrebbe cambiare
[00:28:25] perché ovviamente ad esempio Codex ha
[00:28:27] iniziato ad alzare i propri limiti di
[00:28:29] utilizzi, adesso i limiti di utilizzi di
[00:28:32] Codex si sforano molto più
[00:28:33] difficilmente. Cloud adesso staremo a
[00:28:35] vedere se effettivamente anche lui
[00:28:37] alzerà i limiti di utilizzo. Io credo di
[00:28:39] sì. Quindi ad oggi questa è la combo
[00:28:42] migliore a parer mio e con $120 al mese,
[00:28:45] quindi $20 in più, non il doppio,
[00:28:47] abbiamo una qualità molto molto più
[00:28:50] alta. Immaginatevi se io mandavo quelle
[00:28:52] applicazioni in produzione e vi assicuro
[00:28:54] che anche solamente la revisione del
[00:28:56] plan inizialmente vi salverà tantissimo
[00:28:59] tantissimo lavoro poi quando eh starete
[00:29:01] nel mezzo della costruzione della vostra
[00:29:03] applicazione. E se comunque siete ancora
[00:29:05] scettici, ripeto, non c'è GPT non mi sta
[00:29:07] pagando per questo, però capisco che
[00:29:09] ovviamente è non è una spesa di €5.
[00:29:13] Quello che vi consiglio di fare è
[00:29:15] utilizzate il piano gratuito di CG GPT
[00:29:17] per testare questa roba. Considerate
[00:29:19] che, ripeto, ancora ad oggi Codex è
[00:29:22] disponibile sul piano gratis di CG GPT,
[00:29:25] [musica] quindi Codex è incluso sia in
[00:29:27] free che Go Plus Pro Business
[00:29:29] Enterprise. Quindi testate questa combo
[00:29:32] con il vostro piano di cloud.
[00:29:34] Ricordiamoci che Cloud Code sta minimo
[00:29:36] c'è il devi avere il piano pro di $20,
[00:29:39] quindi volendo puoi testare questa combo
[00:29:41] anche solamente con il tuo piano free di
[00:29:44] [musica] CG GPT. Testalo, vedi se noti
[00:29:46] dei miglioramenti. Ripeto, c'ha GPT va
[00:29:49] Codex va a revisionare il piano o va a
[00:29:52] trovare determinate falle, vedi
[00:29:53] passandolo una o due volte se la qualità
[00:29:56] migliora e se effettivamente vedi un
[00:29:58] netto miglioramento, allora secondo me
[00:30:00] ha estremamente senso utilizzare
[00:30:03] entrambi. Questa è la mia opinione.
[00:30:05] Bene, questo era tutto ciò che avevo da
[00:30:07] dirti. Se sei un'azienda e vuoi
[00:30:09] implementare l'intelligenza artificiale
[00:30:10] all'interno della tua realtà, a partire
[00:30:12] dalla formazione del tuo team su
[00:30:17] Cork, offriamo sia percorsi di coaching
[00:30:20] one toone e one to many many, ma anche
[00:30:22] formazione aziendale proprio in loco,
[00:30:24] fino ad analizzare poi i tuoi processi
[00:30:26] per capire quali soluzioni di
[00:30:28] intelligenza artificiale costruire
[00:30:30] customizzate per la tua azienda e per la
[00:30:32] tua realtà. Se la cosa ti interessa,
[00:30:35] come al solito, nel primo link qui sotto
[00:30:37] in descrizione puoi prenotare una
[00:30:39] chiamata con noi per parlare insieme del
[00:30:41] tuo progetto. Questo è tutto. Fatemi
[00:30:42] sapere qui sotto cosa ne pensate di
[00:30:44] questa combo.
