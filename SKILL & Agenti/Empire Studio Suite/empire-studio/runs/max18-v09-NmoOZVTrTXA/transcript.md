
[00:00:00] Ciao, e benvenuto al corso completo su agenti vocali con Cloud God per Business.
[00:00:04] In questo corso ti mostro esattamente come costruire agenti vocali da zero,
[00:00:08] come integrarli in processi aziendali e qual è il ritorno concreto per le aziende che li adattano
[00:00:12] e per voi che magari andrete a venderli.
[00:00:14] Lavoro su questi progetti ogni giorno con consulenze per aziende sopra i 50 milioni,
[00:00:18] li implemento in piccole medi imprese con la mia agenzia e li insegno nel mio coaching program.
[00:00:23] Quindi tutto quello che andremo a vedere sono cose che effettivamente implemento ed utilizzo.
[00:00:27] Detto questo, cominciamo.
[00:00:28] Questo è quello che andremo a vedere oggi.
[00:00:30] Allora, innanzitutto partiremo dai concetti base,
[00:00:33] quindi prima di costruire agenti vocali in Cloud Code,
[00:00:36] capiremo che cosa è un agenti vocale,
[00:00:38] poi andremo a costruirlo su Cloud Code
[00:00:40] e poi parleremo di quali sono le offerte che ad oggi stanno andando
[00:00:43] e quale sia un ROI per un'azienda
[00:00:46] o i relativi ritorni sugli investimenti
[00:00:48] qualunque sia il tipo di agenti che andate poi a creare.
[00:00:51] Allora, partiremo quindi dalla prima definizione
[00:00:54] di che cos'è un agenti vocale,
[00:00:56] andremo a vedere qual è l'anatomia,
[00:00:57] quali sono i componenti, come funziona, parleremo poi di quale è la struttura di un system
[00:01:02] prompt corretto o le best practices, vedremo poi quali sono i quattro modi di inserire
[00:01:09] una knowledge base all'interno del nostro agente vocale, capiremo poi quale è la migliore
[00:01:13] tra quelle che andremo ad utilizzare, vedremo poi i cinque tipi di tool che possono essere
[00:01:19] integrati con una gente, capiremo come è possibile customizzare o quindi apportare
[00:01:24] delle modifiche che noi vogliamo personalizzare un qualsiasi gente vocale e infine parleremo
[00:01:29] di latency tuning e cioè qualsiasi cosa vi ha a che fare con i e quindi le stesse cose che
[00:01:34] sto implementando anch'io nelle aziende dei piccole dimensioni o per chiunque voglio venire
[00:01:38] poi a lavorare con me. Queste sono anche le stesse offerte che le persone dentro al mio
[00:01:42] coaching program oggi stanno utilizzando quindi saranno delle soluzioni che potranno
[00:01:47] essere applicate istantanevamente. Allora, prima di cominciare con la parte pratica,
[00:01:51] due parole solo sulle due piattaforme che io oggi considero quando si parla di
[00:01:56] voice agent e due parole anche magari su quale usare a seconda dell'azienda che
[00:02:01] avete se siete un imprenditore o con cui diciamo andrete a lavorare se siete una
[00:02:06] persona che vuole vendere servizi ai. Queste sono le stesse anche che poi una
[00:02:10] persona diciamo può andare ad utilizzare quando fa development senza
[00:02:14] andare in cose molto più complicate come non lo so AWS o cose di questo tipo.
[00:02:19] Allora, le due piattaforme sono WAPI e RETELL, ok?
[00:02:23] Quindi queste sono le due GO TO PLATFORMS.
[00:02:26] Allora, diciamo che, per tenerle molto più semplice, RETELL è molto più beginner-friendly,
[00:02:34] specialmente per il fatto che, come vedete, se io premo, è una UI, quindi un'interfaccia visiva, molto più pulita, vedete?
[00:02:42] Ho già le funzioni, qualsiasi cosa, queste cose vogliono dire, lo vedremo dopo,
[00:02:47] vedete che ce l'ho già tutte belle in ordine, tutte belle pronte e quindi è molto, diciamo,
[00:02:54] bella anche dal punto di vista visivo. Questo ha un'implicazione e cioè, nonostante sia
[00:02:59] molto bella dal punto di vista visivo, a livello tecnico hai un po' meno controllo, diciamo,
[00:03:04] quindi quando farete cose super complesse, per questo corso va benissimo quasi così
[00:03:08] cosa, anche se implementato un servizio in azienda va benissimo retail, è perfetto,
[00:03:14] sono mille casistiche con retail che funzionano alla grandissima. Il prompt, quindi le istruzioni
[00:03:19] saranno gran parte di dove farete la differenza, poi andremo a vedere perché. Diciamo solo che
[00:03:24] a livello tecnico, soprattutto per quanto riguarda la parte di latenza, quindi questo
[00:03:28] valore qui, piccolino, no? Quindi diciamo il tempo che un agente ci mette a rispondervi,
[00:03:36] quindi non lo so, immaginatevi di essere al telefono. Ciao, come stai? Io sto
[00:03:40] bene tu, tutti quei secondi lì si chiamano la tensa, ok? Diciamo che è un po' meno
[00:03:45] controllabile da ritel, vapi permette di fare qualcosa di un po' più sofisticato, ecco.
[00:03:50] Per lo scopo del corso non ci saranno grosse differenze, quindi utilizzate quella che voi
[00:03:56] volete.
[00:03:57] Allora, partiamo dal principio, che cos'è un'agente vocale e qual'è l'anatomia
[00:04:02] di un'agente vocale? Anatomia, sostanzialmente, intendo come è fatto, no? Allora, in
[00:04:07] parole molto semplici, abbiamo un utente che parla, giusto? Poi dentro alla gente succede
[00:04:14] qualcosa, tale per cui poi abbiamo una risposta da parte del modello. Allora, che cos'è questo
[00:04:22] qualcosa? Allora, queste sono delle parti che vengono chiamate, allora STT, giusto? Questa
[00:04:32] viene chiamata tts e questa come voi già sapete viene chiamato lm allora stt vuol dire speech
[00:04:42] to text cioè sostanzialmente è un pezzo di modello che traduce sostanzialmente il parlato
[00:04:50] in testo questo perché perché come sapete le ai tende a capire meglio quello che viene
[00:04:55] definito testo in particolare tende a capire meglio quello che noi poi vedremo
[00:05:00] i nostri prompt che viene definito markdown, quindi il testo con dei simboletti che sostanzialmente
[00:05:05] permettono alle AI di capire un po' meglio ok qual è la gerarchia del testo e in che
[00:05:10] ordine procedere perché magari un pezzo di testo è più importante di qualcos'altro.
[00:05:14] Allora, detto questo quindi sappiamo il motivo per cui abbiamo la prima parte, che
[00:05:19] è questo appunto speech to text, poi qua dentro, quindi sostanzialmente dentro al
[00:05:24] nostro LLM, l'AI sta cercando di capire cosa l'utente dica, quindi cosa vuol dire il testo
[00:05:30] in ingresso, capire che task deve fare sulla base del testo in ingresso, che altrimenti non
[00:05:35] è che un piccolo prompt che abbiamo dato, e poi passeremo alla parte finale in cui l'LLM
[00:05:40] ha capito e allora genera un output e questo output di nuovo è informato di testo, giusto?
[00:05:47] Una classica chat con cloud dove semplicemente vediamo che l'output è sempre in una
[00:05:52] chatbot. Allora, una volta che questo succede, passiamo alla parte tts, quindi text to speech,
[00:06:00] in cui ci sono delle cose dentro a questi modelli che permettono di trasformare il testo in
[00:06:06] qualcosa di udibile. Motivo per cui poi noi, alla fine di questo percorso, andiamo a
[00:06:11] sentire che le AI ci risponde sostanzialmente, ok? Quindi questo in maniera molto semplificata
[00:06:19] è il processo. Ora, qualcuno si potrà chiedere, benissimo,
[00:06:23] dato che questo processo è relativamente semplice, chi decide che questa cosa funzioni
[00:06:29] o osmetta di funzionare quando questo processo parte? Bene, introduciamo un concetto che
[00:06:34] si chiama End Pointing, che è questo qui, che è diverso dall'End Point, l'End Point
[00:06:41] è un URL, quindi sostanzialmente una cosa tipo questa, Excalidro.com che è l'app
[00:06:47] che utilizzo, mentre l'endpointing ci sostanzialmente permette di capire quando questo processo inizio
[00:06:56] finisce presumerebbe.
[00:06:57] Quindi l'endpointing sarà, e lo vedremo poi, quello che andrà a decidere, l'utente ha smesso
[00:07:02] di parlare o l'utente sta parlando.
[00:07:05] In base alle interazioni che l'endpointing avrà con noi, abbiamo la possibilità di stoppare
[00:07:13] nostro agente AI, nel momento in cui parliamo, è sempre regolato da questo end-pointing qui,
[00:07:18] ok?
[00:07:19] Questo è molto importante.
[00:07:20] Bene, allora detto questo andiamo a vedere i nostri agenti vocali e cominciamo a partire
[00:07:25] con magari, non lo so, Riley sono quelli preinseriti e andiamo a vedere le cose che abbiamo appena
[00:07:33] discusso.
[00:07:34] Allora, zoomo e vedete che la prima cosa che andiamo a vedere è l'LLM, giusto?
[00:07:40] quindi abbiamo già detto ok questa parte qui è quella che noi abbiamo definito lm quindi
[00:07:46] il nostro modello quello che permette di capire insomma che cosa andiamo a fare, poi qui abbiamo
[00:07:50] la possibilità di selezionare questi modelli quindi avete openai, azier, entropic, bedrock
[00:07:57] e cose di questo tipo no?
[00:07:59] quindi poi a seconda poi del provider che andrete ad utilizzare ci sono mille cose
[00:08:05] sono diverse qui, starei qui 70 anni, però avete il provider, poi avrete i modelli e il
[00:08:12] modello è sostanzialmente, diciamo, il pezzettino di provider che voi andrete ad utilizzare per
[00:08:18] fare tutto questo processo di trascrizione e poi di processo delle informazioni, no?
[00:08:26] Allora, quale modello dovreste scegliere? Beh, allora, qui non c'è una metodologia,
[00:08:32] diciamo omni comprensiva che dica questo è il migliore o quello è il migliore se qualcuno
[00:08:36] ve lo dice no. Allora, che cosa andremo a considerare? Bene, allora noi andremo a considerare due
[00:08:44] cose, allora e vedete che Vapi vi aiuta anche e vi dice che le due cose che andete a considerare
[00:08:50] sono costo e latenza. Una terza che metterei è importanza della task, ok? Quindi per
[00:08:57] esempio, se noi decidessimo di usare OpenAI, allora avremmo che questo modello ha una latenza
[00:09:05] o scusatemi di 600 o 400 e un costo di 0.09 dollari, giusto? Quindi capiamo che se facciamo anche
[00:09:15] senza saperne molto, no? 1.670, 2.400, 3.90, 5.10, capiamo che uno dei modelli veloci,
[00:09:24] quindi questo speedometer in inglese è la cosa del cruscotto dell'auto, permette di
[00:09:32] capire quanto tempo ci mette a risponderci, quindi 400 mili secondi o 390 mili secondi
[00:09:38] qua un secondo e 45, capite quanto lento sia questo modello. Qui capite però che anche
[00:09:46] il costo in questo caso è molto più basso di questo, diciamo di questo, che è folle,
[00:09:54] però questo permette di fare cose in real time. Quindi vedete che abbiamo poi a seconda
[00:09:58] della tipologia del caso, abbiamo mille modelli insomma che possiamo utilizzare e qui decideremo
[00:10:06] in base a ok è una cosa real time, non è una cosa real time o possiamo aspettare
[00:10:11] magari qualche secondo in più perché la task poi non è così importante. Un esempio,
[00:10:15] se io so che se i miei fornitori sanno che alle 9 di mattina li chiamo per raccogliere
[00:10:19] dei dati, non sarà importante avere un AI che, non lo so, faccia tuttori al time, no?
[00:10:26] Perché anche se ci mettono un secondo in più, sì, va bene, un po' un disagio, ma niente
[00:10:29] di che. Se invece ho un'interfaccia con un utente per fare uno split to lead o cose
[00:10:34] di questo tipo, allora come ci è diventato complesso, no? Bisogna avere un qualcosa
[00:10:37] di molto performante, altrimenti il lead se ne va.
[00:10:40] Quindi avete la possibilità di scegliere insomma quello che volete.
[00:10:44] Allora, per questo esempio, ma giusto perché così faremo un modello GPT 4.1, no, non ci sono
[00:10:51] grossi motivazioni, però voglio solo farvi vedere una cosa che ora lo pubblico, ok,
[00:10:57] skip and publish, e vedete che prima avevamo una latenza che era 1.220, e ora è ancora
[00:11:03] 1.220, ora se io vado a metterci un modello, invece, super ciccione e faccio skip and
[00:11:09] publish, quello che succede è che poi la nostra latenza andrà ad essere impattata e lo vedete
[00:11:15] qui, adesso pian piano si aggionerà anche, ma vedete che la latenza è 1.670, quindi
[00:11:20] il modello sostanzialmente ci sta dicendo che è peggiorato e tra un po' insomma lo
[00:11:25] vedremo, lo vedremo anche al riflesso qui. Allora, poi abbiamo detto quindi il modello
[00:11:32] è questo, quindi l'LLM, poi abbiamo la cosa numero 2 che è il transcriber, quindi trascriviamo,
[00:11:40] quindi giusto, quindi facciamo lo speech to text e dopo abbiamo il voice, voice configuration
[00:11:47] facciamo text to speech. Quindi la motivazione per cui siamo partiti è che abbiamo esattamente
[00:11:53] poi tutte le cose che abbiamo appena detto sarà ora molto più semplice capire che
[00:11:57] cosa vediamo, no? Perfetto. Ora abbiamo, e poi vi spiegherò cosa sono i tool, abbiamo
[00:12:03] questa parte qui che è la parte di analisi compliance, vi dicendo, per normative analisi
[00:12:09] dei dati, e vi dicendo. Allora, detto questo, prima di passare ai tool, abbiamo visto che
[00:12:16] c'è qualcosa qui. Abbiamo detto che questa è la cosa più importante ed è un prompt,
[00:12:20] giusto? Se non imprimiamola i, è il system prompt che può essere utilizzato per configurare
[00:12:26] contesto, ruolo, personalità, istruzioni e via dicendo.
[00:12:29] Allora, come vedete, questo, come già detto, è Markdown, quindi sostanzialmente è un testo
[00:12:36] strutturato per quelli di voi che sono nuovi, lo faccio vedere al volo.
[00:12:40] Sostanzialmente Markdown è una cosa dove se io scrivo tre o quattro volte ciao, ed
[00:12:46] è un esempio che ho fatto anche in uno dei video scorsi, se io metto un asterischetto
[00:12:52] vedete che ho una certa tipologia di formatazione, se ne metto 2 ne ho un'altra diversa, se
[00:12:57] ne metto 4 vedete che ho una cosa diversa ancora, ora vedete che è grigio e addirittura se
[00:13:02] metto gli asterischi faccio grassetto, quindi sostanzialmente quello che questo linguaggio,
[00:13:09] questi simboli stanno dicendo non è altro che, guarda che questo è un titolo in
[00:13:13] grassetto, questo invece è un, come si chiama, un grassetto di un elenco puntato
[00:13:21] qualunque, no? Quindi, se io ora facessi una cosa così, vedete che adesso lui mi diventerà,
[00:13:28] insomma, adesso questo può diventerà grassetto, eccetera, eccetera, eccetera. Ok? Perfetto.
[00:13:34] Allora, quale è la struttura di un buon system prompt? Allora, abbiamo otto componenti,
[00:13:43] se non sbaglio, anzi, nove, perché ho messo anche gli esempi. Allora, innanzitutto
[00:13:49] dobbiamo dargli una certa identità, giusto? E una personalità a questo agente. Quindi
[00:13:55] vi diremo, hey, non sei una persona reale, se è una persona reale, scusate, non sei
[00:13:59] un AI. Lavori da 8 anni, sei una persona cordiale, suoni come un collega e via dicendo, quindi
[00:14:05] hai un suono familiare e via dicendo. Poi, secondo, sarà lo stile di parlata. Una
[00:14:12] cosa che mi piace molto sono frasi corte, parole naturali, evita di andare in, non
[00:14:17] lo so, frasi corte, seguiti da un mappazzone, quindi una cosa tipo molto AI, non è per
[00:14:22] questo, ma è per quello. Allora, cose di questo tipo e poi di numeri per esteso, quindi
[00:14:29] non 23, non è 2-3, giusto? Ma cose di questo tipo, poi una volta che abbiamo inserito
[00:14:38] lo stile di parlata, abbiamo regole di iterazione, quindi fai una domanda per
[00:14:44] volta, perché? Perché magari vogliamo raccogliere dei dati, quindi una domanda la volta è una
[00:14:49] buona prassi, io generalmente cerco di tenere anche le domande corte, massimo due opzioni
[00:14:56] e via dicendo. Poi, azioni concrete, quindi dettaglio che cosa mi aspetto che la gente
[00:15:04] faccia in maniera abbastanza pulita, quindi prima di tutto saluta, poi questi d'intelesi
[00:15:11] si chiama Gathering the Intent of the Call, quindi capisci perché stanno chiamando, per
[00:15:15] esempio noi faremo una gente per una clinica dentale che è una delle verticali, l'ambito
[00:15:21] medico è una delle verticali che abbiamo dentro la mia azienda per esempio e in questo
[00:15:27] caso è ok, perché l'intento è importante, immaginate che un paziente arrivi e vi dica
[00:15:33] devo fare una pulizia dentale o ho un'urgenza perché mi sta sanguinando la gengiva
[00:15:38] devo parlare con una persona. Queste sono cose che, per esempio, faccio nelle cliniche, capite
[00:15:44] bene che, diciamo, l'urgenza e l'intento della chiamata è molto importante, quindi
[00:15:49] questo è il motivo per cui io generalmente tendo di farlo relativamente presto. Poi raccogli
[00:15:56] le info, conferma, oppure, quindi in realtà c'è un po' un'articolazione, quindi
[00:16:00] e fa il reroute, quindi magari se è urgente fa scala a una gente, insomma mille cose,
[00:16:06] no? Poi qui gli do poi le informazioni aziendali nostre, quindi non lo so, orari, zone, orario
[00:16:17] attuale, super importante, altrimenti la gente non capisce spe' rerout,
[00:16:21] co' collegato al contesto di prima avremmo un qualcosa dentro il prompt che ci permette di rilevare l'urgenza
[00:16:27] quindi come la rilevate l'urgenza? Beh, è difficile chiedere ad un agente, ehi, capisci
[00:16:32] se la persona sta male. No, gli date parole chiave, quindi non lo so, sanguinante o svenuto
[00:16:41] o dolore e cose di questo tipo, ovviamente chiariamoci, soprattutto in un mito mericano
[00:16:48] tutti male, e quindi ecco cose di questo tipo e dopo dipende questo in questo caso da che
[00:16:55] cosa andate a fare, poi ho messo dei profili della persona chiamante, quindi capire che tipologia
[00:17:02] di persona è, perché anche sulla base di quello ovviamente vogliamo un grado di cura
[00:17:09] diverso, ma anche un grado di affidabilità dell'informazione diversa, e benissimo, poi
[00:17:18] abbiamo tool, guardrail e tutte cose di questo tipo, quindi per esempio una cosa
[00:17:24] che trovo molto utile o che meglio ho preso diciamo un cefone con il primo agente che
[00:17:30] ho fatto nove mesi fa era non ho detto non inventare cose e allora mi sono accorto al
[00:17:37] volo che una delle prime cose che la gente ha fatto era stato inventarsi un prezzo per
[00:17:40] una cosa che non aveva. Ecco quindi questi sono i tool ai guardrail che ora mettiamo.
[00:17:44] Questo diventa importante per esempio in una delle consulenze che sto facendo
[00:17:48] in un'azienda che fa più di 50 milioni abbiamo questa tipologia di cose, i guardrail
[00:17:53] sono fondamentali, no? Bene, e poi come gestire gli errori, quindi chiedere di ripetere e cose
[00:18:00] di questo tipo. Bene, ora, detto questo mappazzone, come facciamo nella pratica questa tipologia
[00:18:08] di prompt? Beh, qui è dove vi ho preparato un po' di cose, un po' di prompt che possiamo
[00:18:13] utilizzare, quindi andate in community, sezione classi, adesso vedrò se rimpiazzare magari
[00:18:18] questo corso completo o se potete trovarlo nel template youtube però qui
[00:18:22] sostanzialmente avrete poi una voce qua sotto cloud code probabilmente con il nome
[00:18:28] del corso e vi lascio il riferimento ad un notion che ora vado ad aprire e
[00:18:33] comunque ve lo lascerò anche gratuito per tutti quelli di voi che non hanno alcune
[00:18:37] intenzioni di entrare in community e qui cominciate a trovare le cose allora
[00:18:41] questo è una linea guida che io vi ho scritto in cui vi ho messo
[00:18:47] sostanzialmente un 80-20 di quello che metterai o potete utilizzarla per il vostro agente ok?
[00:18:54] quindi questa è la linea guida in markdown che avete, quindi quella che potete utilizzare con
[00:19:00] orario attuale e cose di questo tipo questa è quella che ora vorrei utilizzare con voi quindi
[00:19:04] prompt per vapi l'abbiamo preso, l'ho semplicemente popolato, di modo tale che anche voi
[00:19:09] possiate vedere come è un prompt popolato oltre che le linee guida generali quindi vado
[00:19:15] qua dentro, copio, cancello e incollo. Allora ovviamente non lo leggerò tutto ma volevo farvi
[00:19:21] vedere velocemente che cosa abbiamo. Identità Marco il receptionist della Giovanni Beggiato
[00:19:27] clinica dentale, parli come una persona reale, calme, cordiale, stile, frasi corte, scrivi
[00:19:33] i numeri, quello che vi ho detto prima, linee guida, una domanda per risposta, massimo
[00:19:37] 15 parole, non ripetere mai informazioni già date, se presenti i rari disponibili
[00:19:41] massimo due opzioni alla volta, quindi questo è perché quando qualcuno vi chiede ok, quando
[00:19:46] hai appuntamento, se è una gente vi fa il ma pazzone di da qui al 2000 e mai e quindi
[00:19:52] uno alla volta, benissimo, poi saluta il paziente calorosamente, ascolta se serve un appuntamento,
[00:19:58] offre massimo due fasce orari, rileggi e conferma, quindi questo è importante, poi il contesto
[00:20:05] Qui vi ho lasciato appunto qualcosa di generale, telefono e via dicendo, era attuale, rilevamento
[00:20:12] d'urgenza, quindi queste sono cose che ho messo per darvi un esempio, quindi dello raccuto,
[00:20:16] dentro rotto, con fiore, trauma caduta, eccetera, eccetera, eccetera.
[00:20:20] E poi qui avete un esempio di strumenti e di tool di cui ora vi parlo, ma questo
[00:20:28] sostanzialmente è un ottimo prompt iniziale.
[00:20:31] Poi, come facciamo a verificare che questo funzioni?
[00:20:36] Allora, facciamo publish, skip and publish, ora una volta messo il prompt, abbiamo un paio
[00:20:45] di cose da sistemare, allora, innanzitutto, abbiamo che ancora il transcriber che dicevamo
[00:20:51] prima in inglese, quindi ora che capiamo perché lo sistemiamo, andiamo in 11labs
[00:20:56] e lo mettiamo in italiano, quindi vogliamo qua sotto, perfetto, e ora andiamo a selezionarci
[00:21:04] la nostra voce, metteremo 11 labs e poi, non lo so, dovrebbe esserci un qualcosa tipo
[00:21:11] un mario rossi giovane se non mi ricordo male, anzi giovanni rossi giovane, perfetto,
[00:21:19] E ora possiamo fare pubblica, perfetto, e ora vedremo una cosa, e che, e cioè che
[00:21:29] l'assistente ancora ci risponderà in inglese.
[00:21:32] Proviamo.
[00:21:33] Ciao, vorrei prenotare un appuntamento per le 10 di
[00:21:53] domani mattina. Certo, capito, come si chiama. Ok, lasciamo
[00:22:01] perdere allora il fatto di che cosa abbia trascritto, che quello ne parleremo dopo di
[00:22:06] come trovare un buon transcriber e via dicendo, ma vedete che la prima risposta inglese è
[00:22:10] la seconda risposta italiana che era l'unica cosa che mi interessava. Perché? Perché
[00:22:14] ora introduciamo questo e cioè la parte che ho saltato prima volontariamente,
[00:22:20] ovviamente ho anche preso un modello stupido, quindi giusto per capirci.
[00:22:24] Allora, questo dice che l'assistente parla per primo, quindi ci dice qualcosa, no?
[00:22:30] E al posto avremo queste possibilità qui, ma insomma, vogliamo che l'assistente ci parli
[00:22:35] perché altrimenti non avremo modo di capire che la gente ha preso la chiamata.
[00:22:40] Ma questo è il primo messaggio che abbiamo, quindi avremo quello che c'ha detto prima,
[00:22:46] Quindi ciao, sono Giovanni, mi piace YouTube, insegno AI e la applico alle PMI italiane
[00:23:03] ed estere.
[00:23:04] Ora, pubblico, skip and publish e ora parliamo e sentiamo il primo messaggio.
[00:23:13] Ciao, sono Giovanni, mi piace YouTube, insegno AI e l'applico alle PMI italiane ed estere.
[00:23:23] Perfetto, quindi noi abbiamo capito che ora il sistema funziona e quindi ora abbiamo portato
[00:23:31] tutto il nostro sistema a parlare in italiano.
[00:23:34] Grandissima cosa, questa è la Milestone numero uno, ok?
[00:23:39] Quindi abbiamo fatto questo, abbiamo introdotto che cos'è un system prompt e ora cominciamo
[00:23:46] ad andare in cose un pochino più articolate e cominciamo a parlare di tool.
[00:23:52] Allora, i tool sono delle cose che permettono al vostro agente di andare a fare qualcos'altro
[00:23:59] e perché lo dico?
[00:24:00] Allora, perfetto, qui ho già solo messo ciao come posso aiutarti, allora al posto
[00:24:04] che parlarci, voglio andare in una chat. Ciao, come posso aiutarti? Voglio prenotare
[00:24:10] un appuntamento per domani alle 10. Allora, ora vediamo che cosa succede, no? Quindi
[00:24:15] il nostro agente poi, certo, mi dice il suo nome per favore, io gli risponderò a Giovanni
[00:24:20] e di cominciare a dare un po' di informazioni, quindi denti, pulizia, denti, lui mi risponderà
[00:24:28] a qualcos'altro, ho capito, controllo se abbiamo un posto per domani alle 10 un
[00:24:31] un attimo. Ora vedete però, ed è una cosa molto importante, e cioè la gente ora ci
[00:24:37] sta dicendo che lui sta controllando se domani alle 10 ha un appuntamento. E questo però
[00:24:43] non può farlo, perché al momento noi non gli abbiamo dato nessun modo di accedere ad
[00:24:49] un'agenda, controllare il CRM, vedere cose, ok? La gente ad ora può solo cattare
[00:24:57] o parlare. Quindi questo è importante perché? Beh, perché capiamo che a questo punto il
[00:25:02] nostro agente rimarrà bloccato perché non ha un modo di vedere se abbiamo spazi o no.
[00:25:09] Quindi l'utilità dei tool è perché adesso bellissimo abbiamo un'agente che ancora parla
[00:25:15] malissimo e ciatta ancora peggio, ma non abbiamo modo di fargli fare nulla, quindi
[00:25:20] questo agente è tutt'ora al momento non troppo utile, soprattutto per un'azienda.
[00:25:25] Allora, quindi, che tipologie di strumenti esistono?
[00:25:31] Allora, abbiamo quattro tipologie di strumenti, non è importante sapere, diciamo, le tipologie,
[00:25:38] è più importante perché a nessun reparto amministrativo importerà come si chiama
[00:25:44] la tipologia di strumenti che voi usiate e nemmeno a voi, a voi però interessa avere
[00:25:48] una idea di come ragionare per sistemi.
[00:25:52] Allora, questi tool sono i tool di default, quindi quelli che sono preinstallati, immaginatevi
[00:25:58] il nostro Riley ora avremo la connessione con, non lo so, Google Sheet, ok, roba preinstallata
[00:26:05] da Vapi.
[00:26:06] Poi, custom tool, cioè sono delle cose fatte custom appositamente per noi, quindi i nostri
[00:26:14] webbook o i nostri sistemi, magari accesso ad una cosa che noi vogliamo.
[00:26:19] Eh, snippet di codice, quindi sostanzialmente come si differenziano gli snippet di codice
[00:26:26] o i code tools dai custom tools, la differenza è dove vivono, i custom tools sono cose che
[00:26:33] si connettono al vostro database, quindi immaginate che avete una cosa vostra in azienda,
[00:26:38] fatta solo per voi il vostro processo, la vostra CRM, quello che è che avete fatto
[00:26:44] voi, bene la importate, i code tool vivono dentro vapi, quindi il codice avviene
[00:26:49] dentro VAPI e dopo avete le integrazioni classiche, quindi non lo so, Mac.com, G.H.L e
[00:26:55] via dicendo ok? Dove andiamo a trovarle? Bene, allora adesso vediamo l'interfaccia
[00:27:00] VAPI, quindi qui abbiamo questa, vediamo se volete, perfetto, sì avete questo simboletto
[00:27:07] qui che è il simboletto tool. Allora, qui forse avrete solo questo, ma sostanzialmente
[00:27:16] come li create, premete qui. E allora qui cominciamo a vedere, allora custom tool sono
[00:27:21] delle funzioni particolari, poi avete query che vi permettono di cercare cose dentro di
[00:27:28] database, quindi non lo so, avete una con una knowledge aziendale che volete mettere dentro
[00:27:33] un pdf con le vostre FAQs perché magari il chatbot è un chatbot per rispondere all'FAQ,
[00:27:40] qui la inserirete, avete funzioni prefatte come vi dicevamo prima, quelle di default,
[00:27:46] quindi finire, iniziare una chiamata, trasferirla e via dicendo, poi avrete integrazioni e
[00:27:54] quindi avete poi i vostri mcp, il vostro Slack e via così.
[00:27:59] Quindi questo è solo perché, perché ora avete più o meno un'idea di quello che succede
[00:28:03] quando e di che tipologia di tool esistono. Come ne creiamo o uno? Beh andiamo in
[00:28:09] create tool, qui ne selezioniamo uno, per esempio, facciamo ne uno o l'altro al volo che poi
[00:28:14] utilizziamo, che è query, ok? Allora, noi avremo questo tool qui e qui metteremo, diciamo,
[00:28:23] F Knowledge, conoscenza aziendale e qui metteremo file che serve per capire quali sono le cose
[00:28:41] che la clinica dentale belgiato fa. Perfetto, benissimo. E poi qui al momento stiamo solo
[00:28:49] creando il tool, ora dobbiamo inserire la knowledge qua dentro. Quindi per questo facciamo
[00:28:55] add knowledge base, new knowledge base, di nuovo, gli andiamo a copiare questa cosa qui,
[00:29:05] e qui lo chiameremo beggiato clinica dentale, perfetto, e poi che modello utilizziamo,
[00:29:15] gemini flash fa benissimo, file, adesso noi qui vediamo che non abbiamo modo di selezionare
[00:29:23] niente, soprattutto se ancora non le avrete inserite, giusto?
[00:29:27] Quindi dovremmo, e questo è la prima cosa che vediamo, dovremmo avere un modo di inserire
[00:29:31] qualcosa, questo file era già presente ma diciamo non conta e quindi al momento
[00:29:35] la cosa buona che possiamo fare è salvare il nostro tool, quindi il nostro tool aziendale
[00:29:41] e nel mentre andiamo ad inserire questi file.
[00:29:45] Allora per farlo andiamo qua dentro, quindi questo simboletto qui, premiamo file e qui potremmo
[00:29:52] inserirli quindi upload a file, andremo nel desktop e ho Giovanni Beggiato Knowledge Base,
[00:30:02] altro non è, vediamo se riesco a farvelo vedere al volo, che un file che vi lascio sempre
[00:30:07] in community dove sostanzialmente, anzi fatemelo aprire velocemente, ma altro non ho fatto
[00:30:13] che creare la mia clinica dentale e gli ho messo dentro un po' di informazioni stino prezzi,
[00:30:19] FAQ e cose di questo tipo, no? Cose molto banali, niente di che.
[00:30:24] Allora, andiamo a vedere qualcosa che poi potremmo chiedere al nostro agente, quindi
[00:30:29] fate la prima visita gratuita, sì, la prima visita di valutazione è sempre gratuita
[00:30:34] e dura circa 30 minuti. In me di quesame una situazione è necessario
[00:30:37] il formulo preventivo, ok? Quindi questa è la risposta che ci vogliamo o ci
[00:30:41] ci aspettiamo di ottenere. Ora, torniamo nei nostri tool, torniamo nel nostro query
[00:30:46] tool, che si è sminchietti, quindi fatemi al volo ricompilarlo velocemente, perfetto,
[00:30:53] siamo tornati a noi e ora faremo file e vedremo che Giovanni Beggiato Knowledge è stato inserito.
[00:31:01] Quindi ora potremmo premere salva, perfetto, salvato, ed una volta salvato, ora
[00:31:09] questa knowledge base l'abbiamo messa qua dentro, ok? Quindi è dentro al nostro agente.
[00:31:16] Ora, non è ancora collegata al nostro agente, perché per farlo possiamo andare in Reilly,
[00:31:23] giusto? E possiamo andare qua sotto in File e poi premeremo Giovanni Beggiato Knowledge
[00:31:32] base pdf vedremo pubblica salta e pubblica e ora semplicemente andremo di nuovo in chat
[00:31:40] parlare con nostra gente e gli chiederemo fate la fate la prima visita gratuita in video
[00:31:50] e quello che ci aspettiamo è certo la prima visita è quanto dura la prima visita e cosa
[00:31:56] succede dura circa mezz'ora controllo competto e vuoi prenotare ok perfetto allora abbiamo
[00:32:08] avuto quello che volevamo, ora però che cosa è successo? Beh, io ho detto che abbiamo
[00:32:13] aggiunto una Knowledge Base, ma perché la inseriamo qua nei file? Perché non possiamo
[00:32:19] metterla nel prompt? E quali sono le possibilità che noi abbiamo di inserire questa Knowledge
[00:32:25] Base? Beh, allora, quindi come inseriamo una Knowledge Base ed implicazioni? Allora,
[00:32:38] Vediamo che cosa succede al nostro agente, perché questo è una delle cose più importanti che un sacco di persone sbagliano.
[00:32:45] Allora, vediamo la prima cosa.
[00:32:48] Allora, punto numero uno, e lo metto in nero, nel prompt.
[00:32:56] Giusto?
[00:32:57] Quindi, noi otterremo lo stesso risultato senza fare tutto questo casino enorme.
[00:33:02] Se io andassi qua dentro e cominciassi a prendere, adesso vediamo se riesco a farlo
[00:33:08] continuous scroll, magari lo prendo così, perdonatemi continuous scroll, vado qui e nella
[00:33:17] pagina ora tiriamo già tutto, allora perfetto, fino a qui copiamo e se io andassi qua sotto
[00:33:30] e gli dicessi knowledge, base, giusto?
[00:33:36] e poi gli la incollassi
[00:33:38] ora ho incollato tutto questo cazzilliardo di informazioni che voi vedete
[00:33:43] servizio offerti, orari e vedete che da qua ci siamo, ok?
[00:33:47] pubblicchiamolo così e vediamo che cosa succede
[00:33:52] perfetto, chat, eh allora gli chiediamo, fate la prima visita gratuita?
[00:34:00] certo, la prima visita è gratuita
[00:34:02] Quindi sappiamo che fa la prima visita gratuita e la vede.
[00:34:05] Bene, quindi questa è la metodologia numero uno.
[00:34:08] Ora, cancello tutto, la rimuovo da lì, da dove l'ho appena messa.
[00:34:15] E ovviamente qui non c'è più, quindi cancelliamo anche questo.
[00:34:19] La seconda modalità che abbiamo è la inseriamo cramite file.
[00:34:25] Quindi sostanzialmente è questo.
[00:34:27] Noi non serve che la riproviamo adesso,
[00:34:30] ma andremo ad aggiungerla al nostro metodologia inserimento tramite file, giusto?
[00:34:40] E questa è la metodologia che abbiamo scelto di utilizzare per questo caso.
[00:34:46] Di nuovo potremmo parlarci, ora vediamo l'impatto.
[00:34:51] La terza metodologia è utilizzando i tool, quindi ora vi ho tra virgolette ingannati
[00:34:58] perché la verità è che se io volessi ora tolgo il file che è quello che abbiamo appena
[00:35:05] fatto giusto che è appena messo dentro perché non l'ho pubblicato e quello che farei è
[00:35:10] tool seleziona tool e io vado qui e dico knowledge base clinica corretto e se io ora
[00:35:18] premessi publish e ora ve lo faccio vedere perché quello di prima era in realtà il file
[00:35:25] Se io vado qui, hey, fate la prima visita gratuita, questa è una esclamazione, più che
[00:35:31] una domanda.
[00:35:32] Certo, la prima visita è gratuita, perfetto.
[00:35:35] E quindi questa è la terza metodologia, la quarta è di dimenticare tutto una funzione
[00:35:44] custom.
[00:35:45] Di cui non parlo, ma questo sostanzialmente è quando le cose cominciano a diventare
[00:35:49] interessanti perché andiamo nel dettaglio di come funzionano, scriviamo cose custom
[00:35:56] per le aziende, andiamo in, non lo so, ad efficientare anche SuperBase e via dicendo.
[00:36:03] Allora, andiamo quindi a vedere, l'abbiamo detto, tramite Tool e Funzioni Custom, queste
[00:36:12] sono le quattro modalità.
[00:36:15] Ora, noi rimuoviamo questa e vediamo quali sono gli impatti.
[00:36:19] Allora, per fare questo, disegniamo.
[00:36:22] Allora, disegniamo un grafico, il primo grafico che voglio disegnarvi è questo, quindi performance,
[00:36:32] giusto? Quindi qui avremo una P e questo sarà i tokens che andiamo a consumare e noi sappiamo
[00:36:40] già che il grafico avrà più o meno un andamento di questo tipo, ok? Indiciamo spesso e la
[00:36:47] La seconda cosa che vogliamo andare a disegnare è il nostro prompt. Ok? Il nostro prompt
[00:36:53] di sistema. Quindi questa è la nostra conversazione. Ok? Perdonatemi, lo rifaccio al volo, che
[00:36:59] così non si chiude, siamo a posto. Allora, se io mettessi il nostro file dentro al prompt,
[00:37:10] quindi casistica numero uno, torno nella gente, abbiamo detto cancello tutto, lo
[00:37:16] in collo qua sotto, ok, o qua dentro. Che cosa sto facendo? Beh, allora diciamo che
[00:37:22] la mia conversazione parte con un malloppo di cose che sono inserite tutte dentro al prompt,
[00:37:32] no? Quindi immaginiamo che la persona sia solo interessata, ad esempio, sciocco a capire
[00:37:39] come si chiama la clinica dentale, questa informazione è già qua dentro. Quindi non
[00:37:45] non avrebbe bisogno di prendere tutto il resto del mio prompt e quindi tutto il resto delle
[00:37:50] informazioni su visite gratuite, preziari e cose di questo tipo. Quindi in questo caso
[00:37:58] avremmo che la parte blu rimangono un po' di informazioni che non ci servono, quindi
[00:38:02] sono un po' di informazioni che sono inserite all'interno del prompt iniziale, quindi
[00:38:07] consumeranno un po' i nostri token, quindi, adesso vi faccio vedere cosa vuol dire, poi
[00:38:12] la gente ci dirà ciao come stai ma questo ciao come stai o come posso aiutarti diciamo
[00:38:17] c'è attaccato anche tutto questo malloppo ok quindi questi token consumati non sono solo
[00:38:24] questi ma sono anche tutti quelli che sono stati attaccati qua dentro che sono tutti quelli
[00:38:30] che sono qua dentro ok quindi inserirlo dentro al prompt ha questo effetto e poi
[00:38:35] noi continuiamo a interagire e lui poi richiamerà le informazioni iniziali solamente
[00:38:40] se, diciamo, ne avrà bisogno. Però, insomma, ha tutto questo contesto. Che cosa vuol dire?
[00:38:47] Beh, vuol dire che immaginiamo che il prompt sia grosso, ora facciamo casi estremi perché
[00:38:51] ci capiamo meglio. Se noi sappiamo che l'ottimale è qui, ok, è questo. Ovviamente, questo
[00:38:58] è un prompt, è una cosa ridicola. Sapiate che formazione aziendale, insomma, 11 pagine
[00:39:03] vuol dire che è un'azienda di mezzo dipendente, ma di solito sono SOP da 300, 400 pagine
[00:39:08] con migliaia e migliaia e migliaia di token, quindi ecco, questo è per dire non sono sempre
[00:39:15] così poche. Quindi se quello è l'ottimale, noi adesso abbiamo il nostro blue e potremmo
[00:39:21] avere il caso in cui il nostro primo prompt sia proprio qua nell'intorno della perfezione
[00:39:29] del contesto e quindi capite che con due tre conversazioni con la gente, se non
[00:39:34] facciamo one shot, stiamo già ascendendo qui e stiamo avendo un'agente che già comincia
[00:39:40] a peggiorare le proprie condizioni. Però, diciamo, questo è buono perché, a seconda
[00:39:45] di dove è l'ottimale, potremmo essere in questo intervallo qui e quindi potremmo avere
[00:39:50] più di qualche conversazione con la gente prima di cominciare a scendere come performance.
[00:39:54] Ok? Quindi, questo capiamo che diciamo non è ottimale, però non è un disastro.
[00:40:00] Cosa vuol dire avere inserimento tramite file e lo faremo in rosso?
[00:40:12] Beh, inserimento tramite file è il peggiore che voi potiate fare, quindi se lo mettete
[00:40:19] qua dentro dovrebbero lasciarvi a casa subito e voi non capite sostanzialmente
[00:40:25] Allora, che cosa vuol dire? Vuol dire che, per pulire il disegno, immaginiamo allora
[00:40:33] di avere e fatemi vedere se riesco a farlo. Immaginiamo, torniamo, che la nostra prima
[00:40:37] conversazione, quindi questa verde è sempre la solita, no? Quindi è il ciao come posso
[00:40:44] aiutarti, magari fatemelo fare qui, ok? Quindi questa era l'equivalente della
[00:40:48] prima conversazione, abbiamo detto prima che la prima conversazione aveva non
[00:40:52] solo il mallopetto blu, ma aveva anche tutti i token consumati dal prompt iniziale che è
[00:40:59] questa cosa blu.
[00:41:00] Allora, qui invece abbiamo i file, quindi cosa vuol dire?
[00:41:04] Vuol dire che la prima conversazione avrà quello verde più tutte le info del rosso
[00:41:11] e il rosso è sostanzialmente avere il blu, abbiamo detto, perché sono tutte le info
[00:41:16] che sono qua dentro, quindi il primo prompt ha ciao come posso aiutarti,
[00:41:21] tutti questi token consumati. Voi rispondete come si chiama la clinica e avete magari che
[00:41:27] la clinica di nuovo è Giovanni Beggiato clinica dentale, non mi ricordo cosa abbiamo detto,
[00:41:32] ok, clinica dentale. Bene, la seconda risposta, quindi come si chiama la clinica, Giovanni Beggiato
[00:41:39] clinica dentale, ancora tiene di nuovo un'altra volta ricarica tutti i dati perché
[00:41:47] che averlo qua significa che lo stiamo continuando a ricaricare ogni volta. Quindi capite che
[00:41:54] ogni conversazione sta ricaricando tutte le effe i cui aziendali, quindi sostanzialmente,
[00:42:01] ed è un errore che fanno in un sacco, voi alla prima o alla seconda conversazione siete
[00:42:06] già qua ed è il motivo per cui le aziende perdono un sacco di soldi per cui oggi
[00:42:10] voi sei ai, non è che sia un fenomeno, ma... o beh, ecco, questo è uno dei motivi
[00:42:15] più grossi. Bene, se invece andiamo con i tool... Ok, quindi, scusate, questo mi sembra
[00:42:24] chiaro, voi andrete in questa zona estremamente veloce, ok? Quindi lo ho disegnato in rosso
[00:42:30] a posta. Bene, adesso cosa succede con i tool? Quindi, questi arancio? Beh, allora pulisco
[00:42:38] il disegno un'altra volta. Allora, questo lo rimuoviamo, questo lo rimuoviamo, questo
[00:42:44] lo rimuoviamo, abbiamo fatto il nostro esempio e adesso ve lo rimetto qui al volo dove abbiamo
[00:42:49] le conversazioni e sappiamo che avere i file significa avere sto maloppone che ce lo riattacchiamo
[00:42:56] ogni volta? Ora capiamo i tool che cosa succede. Allora, con i tool è una conoscenza che
[00:43:02] chiamiamo onDemand. Che cosa vuol dire? Che non viene chiamata sempre, viene chiamata
[00:43:06] solo quando ne abbiamo bisogno. Quindi, nel pratico.
[00:43:09] Ciao, come posso aiutarti? Consumerà solo questi token.
[00:43:13] Come si chiama la clinica dentale? Beh, la clinica dentale è già nel prompte iniziale,
[00:43:20] quindi la mia conoscenza, le mie FQ, non vengono ancora chiamate. Quindi solo questi
[00:43:25] token. Poi, ah ok, fate la prima visita gratuita, allora chiamo la parte di, diciamo, FQ
[00:43:36] che mi serve. Super importante, perché con i tool partiamo da qui. Siamo già nella parte
[00:43:43] diciamo ottimale di performance e quindi diciamo, ovviamente, è magari giusto per avere una
[00:43:49] compliance del disegno, ok, lo disegno così, poi non è mai così, ma, insomma, ecco, siamo
[00:43:54] in questo intervallo qui. Quindi va sempre messo con i tool. Poi, in la realtà dei fatti
[00:44:01] è che con la Custom Function questa cosa qui diventa ancora migliore, ma lì poi si apre
[00:44:08] un universo, perché posso non solo chiamare la FAQ solamente quando voglio, ma posso addirittura
[00:44:17] chiamarne solo un pezzo, perché magari ho messo dei metadatta e quindi diventa estremamente
[00:44:22] complesso, non voglio parlarne perché diventerebbe lunghissimo, però mi basta farvi capire
[00:44:28] che tra queste tre metodologie, se partite per i vostri primi progetti, qui è dove andiamo,
[00:44:33] no? Ok, benissimo. Quindi tramite tool è la nostra soluzione. Quindi spero che questo
[00:44:40] tra l'altro sia una cosa che sia utile per voi perché non tanti ad oggi la sanno. Allora
[00:44:46] passiamo adesso a parlare dell'ultimo concetto che è sostanzialmente la latenza, prima
[00:44:50] poi di entrare nel pratico e magari andare in cloud code e cominciare a fare questo
[00:44:55] un sistema end-to-end. E questo è solo perché ora abbiamo tutte le informazioni che vogliamo
[00:45:00] per anche interagire con Cloud Code, capire, vedere dopo cosa succede, capire perché le
[00:45:05] cose vanno bene, vanno male e vi è dicendo. Allora, la latenza abbiamo detto essere la
[00:45:10] differenza, diciamo, di tempo tra quando la gente parla e quando noi parliamo e
[00:45:16] viceversa. È l'intervallo di silenzio, chiamiamolo così, ok, per capirci. Bene.
[00:45:22] Ora, come facciamo a controllarlo e quali sono le variabili che usiamo?
[00:45:28] Bene, allora questo è importante perché di nuovo varia molto in base allo use case
[00:45:33] aziendale, non faccio un corso giganorme per parlare di tutto, a vedete tra l'altro
[00:45:39] ora si è allineata la latenza e capite perché era così lento, per il modello che
[00:45:43] abbiamo scelto, ma come la controlliamo?
[00:45:48] abbiamo tre modi di controllarla e allora fatemi andare velocemente qui perché questo ce lo rende
[00:45:56] molto più semplice. Allora noi sappiamo che sia qui, giusto? Che qui? Che qui? Che cosa abbiamo?
[00:46:06] Abbiamo un modello che viene utilizzato in una piattaforma di terzi. Quindi non lo so,
[00:46:12] LLM, Anthropic, qui abbiamo visto varie cose, adesso c'era Deepgram, ci sono tutti questi
[00:46:18] transcriber, 11labs, Gladia, Google, ci sono un sacco di cose, no?
[00:46:25] Allora, per farve la semplice, questi modelli qui sono quelli che vanno ad impattare la vostra
[00:46:30] latenza.
[00:46:31] Quindi sostanzialmente che cosa succede?
[00:46:33] Che per migliorare la vostra latenza potete scegliere una combinazione di modelli,
[00:46:39] nuovo non c'è un o solo questo o solo quello, ma una combinazione di modelli che non vi
[00:46:44] assassinino, diciamo, il progetto, ma che possano migliorarlo, perché come vedete, allora
[00:46:54] siamo a due e mezzo, ovviamente ora ci metterà magari un cazzeliardo di tempo ad aggiornarsi,
[00:47:00] ma ah no ok, ma siamo già scesi di più di un secondo e mezzo solo con un modello,
[00:47:05] Quindi capite che se noi riusciamo ad avere un buon prompt iniziale, dove se il prompt
[00:47:12] è buono il modello può essere un po' più scarso, perché comunque tutto è gestito in
[00:47:17] maniera ottimale dal prompt, lì è dove facciamo agenti di successo ed è lì dove oggi si
[00:47:25] fa molta fatica perché, non so dei modelli costano, ma perché la qualità dei prompt
[00:47:30] medie è molto bassa ok quindi detto questo come facciamo beh allora abbiamo alcune cose un
[00:47:39] po più visibili quindi queste semplicemente vediamo l'impatto di questo su quell'altro
[00:47:46] via dicendo altre cose invece lo abbiamo ad andare proprio dentro a piattaforme come
[00:47:50] 11 labs capire quali sono le voci quali sono queste quali sono i transcriber che cosa impattano
[00:47:58] quali costi ci sono e via dicendo. Quindi, sostanzialmente quello che vi dico è vi rimando
[00:48:03] alla documentazione ufficiale dei vari pezzi e però la latenza viene controllata in questo
[00:48:10] modo. Oltretutto, dentro VAPI avete anche la possibilità dentro Ad Advanced, ed è una
[00:48:17] cosa che anche qui non troppe persone sanno perché ci giocano magari poco con questi
[00:48:21] strumenti, di controllare la latenza anche tramite cursori, quindi, movendoli, diciamo,
[00:48:28] ok, quindi questo è quanto un assistente aspetta prima di cominciare a parlare. Allora, questo
[00:48:35] potete, come vedete, regolarvelo e questo ovviamente andrà ad impattare sulla latenza,
[00:48:39] quindi non è solo una questione di modelli, ma è anche una questione di impostazione.
[00:48:43] Di nuovo, non c'è una latenza perfetta, non sempre la menor latenza è la migliore
[00:48:48] dell'universo, ci sono le varie casistiche aziendali, allora se fate un new receptionist, se fate
[00:48:53] uno speed to lead, se fate un qualcosa che invece deve raccogliere un sacco di informazioni
[00:48:58] per varie case aziendali e via dicendo. Endpointing, sapete che cos'è ora, sapete
[00:49:05] quale scegliere, sapete che è quello che vi permette di iniziare la conversazione
[00:49:08] no, poi avete quanto si aspetta quando c'è una punteggiatura, quindi punto
[00:49:15] di domanda, punto esclamativo o niente, che è questa parte qui e on number seconds quindi
[00:49:23] sostanzialmente è il minimo numero di secondi che devi aspettare prima che si cominci diciamo
[00:49:28] il processo di trascrizione, quindi sostanzialmente stiamo controllando anche questo endpointing
[00:49:34] qui che era quello che vi dicevo che è quello che diciamo triggera tutto il processo.
[00:49:39] Quindi questo è per dirvi avete un sacco di opzioni, avete anche stop speaking quanto aspettiamo,
[00:49:46] quindi magari per zero due secondi è il tempo che l'utente deve parlare prima che la gente
[00:49:54] si fermi, quindi per esempio se lui sta parlando io parlo a voi per più di zero due secondi
[00:49:59] lui si fermerà e aspetterà e poi ricomincerà e quindi avete sotto tutta la parte di impostazioni
[00:50:05] così e come andiamo a controllare poi la latenza nel pratico. Ora, noi abbiamo appena visto tutta
[00:50:13] la grossa base di agenti vocali e questo perché solamente perché prima di cominciare a costruirli
[00:50:19] nel pratico abbiamo diciamo livellato il terreno per tutti, di modo tale che abbiamo un'infarinatura
[00:50:26] di base di quali sono che cosa sono gli agenti vocali, quali siano i problemi che
[00:50:33] queste gentili vocali hanno e come in linea di massima possiamo controllarli.
[00:50:37] Adesso, quello che faremo è andare ad utilizzare Cloud Code per costruire questi, perché?
[00:50:44] Perché beh, capite che per ora abbiamo fatto un processo estremamente manuale, cioè abbiamo
[00:50:49] ehm preso, non lo so, vari receptionist, abbiamo messo dei prompt noi, abbiamo cominciato
[00:50:55] a prendere delle impostazioni eccetera, ma idealmente vorremmo un modello che in
[00:51:00] qualche modo ci aiuta.
[00:51:01] In maniera adizionale poi, questa cosa qui per ora vive nel nostro computer, cioè vive
[00:51:06] letteralmente dentro VAPI, non l'abbiamo ancora pubblicata, non la possiamo dare a nessuno
[00:51:12] questo voice agent diciamo è ancora qui, quindi diciamo l'utilità per il momento
[00:51:17] siamo noi che parliamo con questo agente, ma non è una cosa che poi possiamo andare
[00:51:21] a dire hey azienda top, tieni questo è il voice agent che dovrei andare a fare,
[00:51:26] ok?
[00:51:27] Allora, questo per dirvi che noi ora usi, utilizzeremo delle piattaforme, allora premetto
[00:51:35] che tutto può essere fatto con Cloud Code senza andare ad utilizzare Na10, che io invece
[00:51:43] ora utilizzerò come sponda perché, perché vi permette di controllare i system prompt,
[00:51:48] sarà più semplice una volta che entriamo dentro e vedremo quello che andiamo a costruire.
[00:51:52] Però, questo è per dirvi, generalmente il mio flusso è prendo, comincio con Cloud Code,
[00:52:01] uso N8n perché mi viene un po' meglio modellare la gente, capire i vari system prompt, dei
[00:52:07] vari agenti, perché ora ne costruiremo uno ma avremo più flussi e allora lo vedremo
[00:52:11] con una cosa un po' complessa, faremo nei high receptionist, e una volta che tutti
[00:52:16] i flussi funzionano, allora chiedo di ricostruire tutto con Cloud Code, ma allora ho già
[00:52:21] ha controllato magari la tensa varia, il prompt, come risponde, se tutti i flow individuali
[00:52:27] funzionano e quindi a quel punto Cloud deve semplicemente ricostruire e poi possiamo pubblicare
[00:52:32] in Vercel queste cose, quindi poi sono accessibili come qualsiasi altra cosa. Vercel, per chi
[00:52:38] non lo conosce, questa piattaforma qui dove sostanzialmente mettiamo le cose live
[00:52:43] e per farvi un esempio queste sono magari alcuni progettini che ho fatto, questa
[00:52:49] era un lead magnet che ho fatto per calcolare l'arro AI degli agenti AI dove se uno preme
[00:52:56] lo mandavo agli imprenditori e questo è sostanzialmente quando possono salvare, ovviamente
[00:53:01] ci sono dei conti sotto fatti in un certo modo, ma ok questo è live, quindi come vedete
[00:53:06] non è più nel mio computer e se volete entrare tra l'altro potete entrarci e ha
[00:53:11] questo URL qui, quindi poi lo vedrete insomma, ok? Quindi poi per metterlo live lo avremo
[00:53:16] Detto questo quindi cominciamo ad entrare nelle varie piattaforme.
[00:53:19] Allora per quelli che di voi sono nuovi velocemente anti-gravity è l'interfaccia che utilizziamo quindi l'IDI e sostanzialmente potete scaricarlo per Mac
[00:53:31] e per quanto riguarda invece Cloud una sola cosa avete da considerare e cioè noi useremo ora Cloud Code ma mentre anti-gravity avrete diciamo un intervallo per
[00:53:45] giocare con il modello gratuitamente con i modelli dentro anti-gravity in maniera gratuita, dentro
[00:53:50] cloud questo risulta un po' più difficile ora nel mentre che si carica perché non tutte
[00:53:56] le tier permettono di avere cloud code ma anzi sfortunatamente al momento abbiamo solo
[00:54:01] che la cloud la tier pro e la tier max sono quelle che vi permettono di utilizzarlo e quindi
[00:54:09] questo è una sfortuna nel senso che poi io lo utilizzo, ma se non pagate l'abbonamento
[00:54:15] questa cosa qui vi potrebbe non potete utilizzarla. Allora, detto questo quindi andiamo dentro
[00:54:22] Antigravity e tutti i progetti dentro Antigravity questa sarà l'interfaccia che vi accoglio
[00:54:27] quando lo scaricate e vivono dentro una cartella. Quindi la prima cosa che andiamo a fare
[00:54:31] è aprire una cartella dentro nostro desktop e lo chiameremo voiceaicorsocompleto youtube.
[00:54:41] Allora, ora vediamo che qui non abbiamo sostanzialmente nulla, come facciamo a scaricarci
[00:54:47] Cloud Code. Comunque, se non sapete che cosa è questa interfaccia, vi rimando velocemente
[00:54:54] alla mia community, classi, avete un corso di quattro ore qua dentro, avete due corsi
[00:55:00] da 3 ore e mezza qua dentro, uno per agenti AI, uno per SAS, questo è 3 ore 26, quindi
[00:55:09] vi rimando lì, ora procediamo in maniera abbastanza più veloce, quindi come scarichiamo
[00:55:15] cloud code, estensioni, scriviamo cloud code, e qui poi semplicemente andremo a scaricarcela
[00:55:22] quindi ora questo rumore è perché sta facendo l'update e quindi una volta che l'ha fatto poi
[00:55:27] continuiamo perfetto abbiamo ristartato tutto quindi estensioni cloud code ora per utilizzarlo
[00:55:34] avrete questa iconcina qui quindi basta che la premiate oppure se avete un Mac è command shift
[00:55:41] ed esc la shortcut che potete utilizzare e ora sostanzialmente cominciamo con l'impostare
[00:55:49] il progetto. Allora, prima cosa è la piattaforma che
[00:55:54] noi andiamo ad utilizzare come vi ho detto per cominciare a costruire i workflow sarà
[00:55:59] na10. Quindi qui premiamo semplicemente na10 login, entriamo qua dentro, facciamo sign-in,
[00:56:07] voi vi registrerete, farete tutte le vostre cose splendide e qui ovviamente troverete
[00:56:13] questa interfaccia che vi accoglie e sostanzialmente questa è l'interfaccia che andremo ad
[00:56:17] utilizzare quindi poi qua dentro troverete delle mini cosine che vi permettono e questo sarà
[00:56:22] sostantemente l'workflow o uno dei workflow che andremo a fare ovviamente li faremo molto più
[00:56:26] complessi ora questo lo archivio al volo di modo tale che partiamo con la stessa interfaccia a
[00:56:33] tutti quanti e partiamo tutti da zero bene allora brevemente questi template che potrete
[00:56:39] utilizzare qua fate semplicemente crea workflow e questa e ce metto 30 secondi ora è semplicemente
[00:56:46] un'interfaccia nella quale poi noi vedremo apparire dei moduli, quindi quelli che sono
[00:56:50] chiamati drag and drop, perché li potete semplicemente trascinare e rilasciare, però, diciamo, non
[00:56:57] sarà questo la sede in cui vi spiego Nei Ten, vi farò un corso magari molto breve
[00:57:03] per capire quali sono le cose di Nei Ten che dovete sapere oggi, che ci sono piattaforme
[00:57:08] come Cloud Code, perché alcune cose ancora saranno, diciamo, fate meglio su questa
[00:57:14] tipologia di piattaforma rispetto che Claude. Allora, ora che abbiamo livellato il terreno
[00:57:19] che cosa dobbiamo fare? Beh, Claude nativamente non sa come utilizzare
[00:57:25] N8n e questo è molto importante perché nessuno strumento ha la capacità di capire questo
[00:57:34] N8n come funziona se non gli diamo che cosa. Un manuale di istruzioni, quindi il nostro
[00:57:40] manuale di istruzioni sarà un md file, quindi qui avremo il nostro file.md che dovrà far
[00:57:50] capire al nostro, diciamo, cloud code come funziona na10. Quindi, immaginiamo di avere
[00:57:57] questo file qui, ok? Bene. Ora, il nostro obiettivo però, qual è? È quello di disegnare
[00:58:07] anche questi workflow, questi agenti su VAPI, giusto? Avremmo lo stesso problema allora
[00:58:12] perché qui avremmo che nessuno nativamente sa come VAPI funziona e quindi avremo anche
[00:58:21] bisogno di fare questa cosa qui, quindi questo file qui ci servirà per spiegare come Netn
[00:58:27] funziona, questo ci servirà per spiegare come funziona VAPI, ma allora capite che
[00:58:32] allora noi non abbiamo ancora capito però come costruire questo voice agent, quindi
[00:58:37] avremo un voiceagent.md che ci spiegherà, che saranno una serie di nuovo distruzioni
[00:58:46] in lingua naturale, che ci spiegheranno come funziona creare un'agente AI.
[00:58:53] E una volta che voi saprete questo, di nuovo vi rimando al corso di Cloud nella community
[00:58:58] nel caso vogliate vederlo, sapete che avremo bisogno di un Cloud.md che sono le istruzioni
[00:59:03] generali di progetto.
[00:59:05] Quindi, quando Cloud farà qualcosa, andrà per primo a leggersi questo file, questo file
[00:59:11] farà capire a Cloud che cosa c'è dentro al progetto, questo file poi andrà a rimandare
[00:59:17] Cloud a questa cosa qui, giusto che gli dirà come creare dei voice agents, e allora
[00:59:24] poi il flusso si spezzerà in due parti, una parte che andrà, e lo faremo passo passo
[00:59:29] è a creare questo file dottem e diciamo in a 10 e creare i workflow e una parte separata
[00:59:36] che invece andrà a creare questo qua dentro dentro vapi ok questo è il metodo più efficace
[00:59:42] che all' momento ho visto che vuol dire spezziamo tutto di modo tale che abbiamo delle
[00:59:47] guide molto precise per tutto quanto perfetto quindi ora pian pianino andremo a crearle
[00:59:53] quindi fatemi cancellare questi, anzi fatemi lasciare, allora come facciamo tutta questa
[01:00:00] documentazione, allora perché questo è diciamo la cosa importante, beh dobbiamo cominciare
[01:00:05] a fare questa documentazione per NA10, allora per NA10 dobbiamo inserirli che cosa, beh
[01:00:12] dobbiamo inserirli due cose, giusto prima dobbiamo inserirli un MCP e dobbiamo inserirli
[01:00:18] e poi le skills, anzi forse in questo ordine, ok? Quindi skills, vediamo se voi vedete
[01:00:25] queste cose velocemente, sì, benissimo, fatemi zoomare, bene. E poi qui dovremmo dargli
[01:00:31] un mini prompt che ci permette di capire che cos'è che stiamo andando a fare. Allora,
[01:00:37] dove andiamo a trovare queste? Beh, fortunatamente esiste una repo fenomenale che è shout out
[01:00:44] a lui non fatemi pronunciare il nome ma sostanzialmente questa è la repo delle skill ok quindi andremo
[01:00:52] a copiarla troverete tutto sotto vi lascio i link vi ricendo e poi se io qui alla fine
[01:00:59] al posto che premere skill metto mcp e di nuovo voi dovreste vederlo sì perfetto allora
[01:01:07] vado nella seconda parte della repositori e quindi abbiamo che, diciamo, la nostra repo
[01:01:15] è questa per l'MCP. E questo perché? Perché l'MCP dà accesso a i vari strumenti di
[01:01:22] Anethen. Le skill dicono a Cloud come deve usare questi strumenti. Quindi immaginatevi
[01:01:28] che io dica ok, questa è la cosa per il T e invece questo è il mouse, all'MCP
[01:01:36] è, tenete, la skill ti dicono ok, se vuoi bere il tè devi fare questo movimento, se
[01:01:42] vuoi usare il mouse devi fare questo movimento qui, ok? Quindi questo è quello che gli stiamo
[01:01:47] dicendo. Il prompt ci dice che cosa fare con queste due informazioni. Allora, diremo
[01:01:53] qualcosa del genere, allora. Hey, vorrei che tu mi aiutassi a creare un system prompt
[01:02:01] nel mio file che ho già nominato na10.md e sostanzialmente questo system prompt deve
[01:02:10] aiutarti a capire come generare workflow tramite na10. Per farlo ti ho messo a disposizione
[01:02:20] due repositori, una si chiama skills e una si chiama mcp, le trovi sopra e sostanzialmente
[01:02:26] vorrei che tu mi aiutassi a generare questo system prompt in modo tale che fosse chiaro
[01:02:32] che quando ti chiedo di generare un workflow, voglio che tu faccia riferimento alle informazioni
[01:02:39] contenute qua dentro. Per favore, nel momento in cui poi vai a copiarti le informazioni,
[01:02:44] assicurati di clonare le repository anche all'interno del nostro, o di importarle
[01:02:50] nel nostro workspace o nel nostro progetto, perché questo sostanzialmente ci permetterà
[01:02:54] di avere tutte le informazioni contenute in un'unica source of truth.
[01:02:59] Benissimo, quindi ora gli diamo bypass permissions qua, perché non è una cosa diciamo molto
[01:03:07] complessa, non richiede thinking, quindi sostanzialmente quello che facciamo ora
[01:03:12] è premere in bio. Allora, questo è estremamente importante,
[01:03:16] lo ripeto, il motivo per cui lo stiamo facendo è perché stiamo dando a cloud
[01:03:22] le one file che rappresenta come utilizzare gli strumenti e come utilizzare na10. Quindi
[01:03:32] qui noi abbiamo ancora detto che per il nostro voice agent quello è il workflow. Qui gli
[01:03:38] stiamo dicendo in maniera generale, hey, il workflow si fa con questi strumenti, quindi
[01:03:45] quando ti chiedo file un workflow dovresti fare riferimento a questo e a questo. Ok,
[01:03:50] quindi questo è quello che stiamo facendo ora. Quindi il primo dei nostri prompt sarà
[01:03:55] l'anitn.md. Ora, una volta che questo prompt ha finito, la prima cosa che faremo come sempre
[01:04:01] sarà andare ad assicurarci che tutto funzioni per il meglio. Quindi la prima verifica
[01:04:06] che faremo è ok. Detto che ho importato queste informazioni, ora se io chiedessi
[01:04:11] a Cloud di farmi un workflow, può Cloud farmi effettivamente il workflow che ho
[01:04:17] chiesto, si o no, e poi verificheremo. La risposta si suppone, sarà sì, però insomma
[01:04:23] andremo a verificarla insieme. Perfetto, sembra essere andato, quindi vediamo che cosa c'è
[01:04:27] scritto ad alto livello, eh? Ok, workflow generation, fonti di riferimento, ok, quindi file chiave
[01:04:34] da consultare, architettura, i 5 partner architetturali, va bene, e quindi abbiamo
[01:04:42] perfetto. Allora, vedo subito che... e questo è una cosa che vi condivido dall'esperienza.
[01:04:52] Allora, il file Figo ha importato tutte le informazioni, manca una cosa molto importante,
[01:04:59] e cioè, qui abbiamo i 5 pattern che ci dicono che è come fare una architettura, no?
[01:05:05] scopri dei nodi, creazione workflow, validazione, attivazione. Però non vedo che abbia dettagliato
[01:05:15] in maniera sufficientemente chiara il fatto che bisogna utilizzare MCP e skill. Quindi
[01:05:23] ora io vi faccio un po' di iterazioni, me le salvo perché magari vado avanti in
[01:05:30] dietro 3-4 minuti e poi vi lascio un prompt sotto che magari è fatto un po' meglio.
[01:05:36] Allora, questo è il prompt nuovo, quindi, giusto per farvi vedere, ho messo un processo
[01:05:42] a 6 step, mi piace molto di più e gli ho messo che step 1 è clarify and plan, quindi
[01:05:52] ok, abbiamo tenuto le stesse cose di prima, no, ho solo fatto qualche modifichina.
[01:05:56] La parte 2 è ricercare i nodi, la parte 3 è scrivere espressioni e codice, la parte
[01:06:05] 4 è costruire, la parte 5 è validare e la parte 6 è attivare e confermare.
[01:06:11] Diciamo ho aggiunto un layer perché mi piaceva un po' di più e gli ho dettagliato anche come
[01:06:17] fare magari i modifichi incrementali e cose di questo tipo.
[01:06:21] È semplicemente un processo iterativo dove ho semplicemente parlato un po'
[01:06:24] con l'LLM, gli dito guarda ok, alcune cose non mi piacciono, altre mi piacciono di più,
[01:06:29] credo tu non riuscivi a risolvere eventuali problemi se qualcosa si apparisse, eccetera.
[01:06:34] Questo prompt, gratuito sotto, prendetelo e è il definitivo, cioè non è che c'è
[01:06:40] di più, quindi avete il prompt per utilizzare na10 sempre, quindi se lo vorrete è sotto.
[01:06:47] Ok, quindi detto questo, vorrei testare ora na10 e vorrei vedere se riesco a fare
[01:06:54] qualcosa di sensato quindi per farlo deve andare ovviamente in modalità plan perché
[01:06:59] richiede un certo tipo di effort allora possiamo chiedergli qualcosa del tipo hey vorrei ora
[01:07:05] creare due workflow su n8n uno è un agente ai che deve sostanzialmente confermare la
[01:07:15] disponibilità del dei miei slot a calendario quindi sostanzialmente è un agente ai che
[01:07:23] un modello come per esempio Google Anthropi Code OpenAI scegliene uno che più ti piace
[01:07:30] e Qtel utilizzerà come mente e poi avrà un tool che è un nodo in Google Calendar che poi io
[01:07:40] connetterò e sostanzialmente questo deve essere, deve interagire con la gente AI di modo tale che
[01:07:46] si capisca vicendevolmente quando ho uno slot libero no usa pure ora quindi una variabile
[01:07:53] le dinamiche NOW per capire che giorno è oggi e assicurati di usare variabili dinamiche anche
[01:08:01] dentro al node in NETAN. La seconda cosa che vorrei invece è un workflow che permetta di
[01:08:10] capire se un appuntamento è pernotato oppure no. Quindi anche qui vorrei un agent AI collegato
[01:08:17] a google maps che invece permetta di capire ok l'appuntamento è stato prenotato oppure
[01:08:24] c'è qualcosa che è andato storto perfetto noi lo lasceremo in plan mod e gli diremo
[01:08:31] solo magari per farlo ovviamente riferisci ti al file chiamato n8n.md lo dico piano
[01:08:40] perché di solito mi viene eccolo qua appunto allora ora però prima di premere in video
[01:08:46] e sbagliare, perché ancora non abbiamo avuto tutti i dati, che cosa ci manca?
[01:08:51] Beh, ci mancano due cose, uno dobbiamo dirgli ok a che URL devi fare riferimento e due dobbiamo
[01:08:58] dirgli ok ma quali sono poi le credenziali di accesso che tu hai, quindi questo sostanzialmente
[01:09:05] significa che dobbiamo dargli ancora lo URL e le API chi, per farlo quindi dobbiamo
[01:09:10] entrare dentro N8n ora e fatemi muovere un secondo il mio bel faccione di modo
[01:09:17] tale che poi voi possiate vedere tutto. Quindi ora cosa facciamo? Settings, N8n API,
[01:09:25] crea API Key e mettiamo YouTube, Italia Voice Agent. Magari mettete No Expiration
[01:09:38] date, questo è quello che vi consiglio, andiamo in cloud e gli mettiamo che le apik sono queste
[01:09:45] e ora prendiamo l'url che è sostanzialmente tutto quello che c'è prima di settings. Ok,
[01:09:52] quindi questo. Quindi lo prendiamo, non dovevo tagliarlo senza dubbio, e poi andiamo a fare
[01:09:59] plan e ora possiamo far partire il tutto perché gli abbiamo dato ovviamente tutte le
[01:10:04] credenziali. Giusto, una cortezza, ma giusto così. Guarda, prima di partire assicurati anche
[01:10:12] che le mie chiavi siano dentro ad un file .imv, te l'ho già creato, può inserirle lì dentro.
[01:10:24] In nuovo, questo che cosa vuol dire? Può dire che vi rimando al corso di Cloud in
[01:10:31] in community ma sostanzialmente abbiamo delle API key che sono contenute dentro a un file
[01:10:38] che è questo .env, una convenzione di software developer dove sostanzialmente evita che le
[01:10:46] nostre chiavi di accesso vengano pubblicate al pubblico e quindi come in questo caso,
[01:10:51] se voi avete le mie API key o io mi dimenticassi dopo io di cancellarle, voi potresti usare
[01:10:56] il mio account e quindi utilizzare il mio abbonamento per fare questo.
[01:11:01] letteralmente come se io vi stessi dando le chiavi di casa o come se avessi nel mio computer
[01:11:06] un post-it con scritto il mio username, questa è mia password e questa, vuoi potreste entrare
[01:11:10] e fare un po' quello che lasciamolo così, potete fare tante cose, potete fare, ma non
[01:11:18] entrate in casa mia, grazie. Bene, io torno a posto con il faccione e dopo con calma
[01:11:23] aspettiamo che tutto questo vada a buon fine e una volta fatto vi farò vedere
[01:11:29] il piano e poi vedremo se effettivamente questo ha funzionato perché che cosa dovremmo aspettarci
[01:11:35] che qui adesso nella nostra pagina che è vuota sostanzialmente dovremmo avere questi nuovi
[01:11:42] agenti demo che vengono pubblicati e noi potremmo accedervi e vedere se appunto funziona
[01:11:48] oppure no. Ok, ora cosa importante dobbiamo riattivare Cloud Code perché per accedere
[01:11:54] al mcp insomma che è quello che ora si sta scaricando bisogna riattivarlo quindi ora
[01:12:00] prima di farlo gli dico ok per favore assicurati di salvare il tutto in una memoria di modo
[01:12:07] tale che appena riapro io posso semplicemente dire ok continua e tu capisci immediatamente
[01:12:12] da dove devi ripartire perfetto allora una volta che questo è fatto sostanzialmente
[01:12:19] allora noi possiamo cominciare a chiudere cloud code riaprirlo e poi vediamo insomma
[01:12:25] che cosa succede. Perfetto quindi ora ok continua, lo abbiamo riavviato quindi ora
[01:12:31] dovrebbe andare, vediamo se tutto funziona come deve e dopo vediamo solo il risultato finale.
[01:12:37] Ora questo solo per farvi vedere che sta ancora andando, ma qui mi dice creati e se
[01:12:43] io infatti vado in Anetern abbiamo che il primo è stato creato e il secondo è stato
[01:12:51] creato anche, con la differenza che per quello che controlla la disponibilità a calendario
[01:13:00] abbiamo ovviamente una memoria, quindi stiamo già andando nella direzione giusta. Ora cosa
[01:13:05] ci dice? Questo è stato creato, che cosa devi fare, variabili dinamiche, via dicendo,
[01:13:12] ora debbi solo connettere le credenziali, no? Quindi ora lui avrà utilizzato qualche
[01:13:16] sistema, gemina e via dicendo e quindi sostanzialmente ora il processo che ci serve fare è, oltre
[01:13:24] che controllare brevemente queste variabili per essere sicuri che lo vogliamo, ma andare
[01:13:29] qua dentro, creare nuove credenziali e via dicendo cose che per il momento non sono ad
[01:13:35] estremo valore aggiunto perché poi lo faremo nel workflow finale, quindi per ora volevo
[01:13:40] solo che voi vedeste che insomma queste cose funzionano, riesce a creare workflow corretti
[01:13:46] e poi riesce anche a fare lo step di verifica. La cosa che ci rimarrà da fare a noi all'affine
[01:13:51] sarà semplicemente quella di integrare appunto le credenziali, quindi setup credentials
[01:13:56] se vi ho dicendo. Ok, quindi questo è stato fatto per validare che su Na10 riusciamo
[01:14:03] ad interagire utilizzando cloud code. Perché? Perché questo ci permetterà di
[01:14:08] evitare che tutto quanto venga fatto manualmente tramite noi, no? Perché noi qui avremo dovuto
[01:14:14] fare chat trigger, poi con l'intercione AI e gente vi è dicendo. Una sola cosa volevo
[01:14:18] farvi notare, e cioè perché stiamo facendo in anitend? Perché qui quando avremmo workflow
[01:14:25] più complessi, quindi dopo, avremmo la possibilità di vedere se c'è qualcosa che
[01:14:32] non va guardando il prompt, quindi se per caso io non volevo la ISO ma avevo una
[01:14:37] necessitare di avere una formatazione diversa di data, è una cosa che posso fare già da qui,
[01:14:41] no? Magari dicendogli un qualcosa tipo format e allora qui posso magari fare, non lo so,
[01:14:48] day, month, year, ok? Magari se ho un CRM con questa data e via dicendo cosa che è estremamente più
[01:15:00] semplice da fare se io utilizzo questo tipo di interfaccia, quindi lo leggo, vedo e, insomma,
[01:15:11] capisco quello che faccio, e invece che utilizzare Cloud Code. Io ora non so come mai sono nel
[01:15:17] futuro con i mesi, ma ok, questo è pubblicato a novembre 2026, non a marzo. Ora possiamo
[01:15:29] tornare a noi e cosa dobbiamo fare bene. Abbiamo fatto il nostro NA10, ora dobbiamo fare la
[01:15:36] stessa cosa per VAPI, perché la cosa numero 2 che vogliamo fare ora è semplicemente quella
[01:15:42] di capire se ora possiamo fare la stessa cosa con VAPI, quindi scrivere ad NA10,
[01:15:48] hey, voglio, un AI agent che parli in italiano, e NA10 in automatico mi fa questo, mi
[01:15:55] mette 11 labs e tutte queste cose qui. Perché? Perché come abbiamo detto prima se poi ora
[01:16:00] che sappiamo cosa è la latency e via dicendo possiamo avere un po' uno sparring partner
[01:16:05] quindi qualcuno che viene utilizzato magari in sport come la box come il tennis e via dicendo
[01:16:11] con cui continuare a fare questo back and forth per capire ok stiamo facendo le cose
[01:16:16] giuste la gente non va qual è il motivo mi puoi dare qualche indicazione in più
[01:16:20] e cose di questo tipo, ok? Quindi ora facciamo il nostro vapi.md e per fare questo andiamo
[01:16:28] quindi di nuovo in cloud code e capiamo quali sono ora gli step che servono per il nostro
[01:16:35] vapi. Allora io farò una cosa come clear conversation perché voglio avere la conversazione
[01:16:41] pulita, quindi niente più token usage che vi ho dicendo e ora semplicemente procedo
[01:16:46] in questo modo. Allora io comincio come sempre a far partire il mio prompt perché utilizzerò
[01:16:52] di nuovo il mio whisper flow e gli dirò qualcosa del genere. Allora mi servirebbe che mi aiutassi
[01:17:02] ora a popolare il mio vapi.md. Fatemi solo vedere che l'abbia preso bene. Ecco
[01:17:09] l'ho lì. Già, sapevo io. Ok. E per farlo ti fornirò tutta la documentazione di Vapi.
[01:17:20] Mi servirebbe che quello che tu facessi è prendere la documentazione che avrai in generale
[01:17:31] in ingresso e facessi le seguenti cose. Allora, perfetto. Adesso prima di continuare
[01:17:41] facciamo lì questo, quindi documentazione vapi, fetto introduction e ora in linea generale
[01:17:54] volevo vedere se gliela togliamo non credo succede da grandi robe, ok sì questa è la core
[01:18:00] poi abbiamo gli API reference che gli possiamo dare solo per fargli diciamo la vita più
[01:18:06] semplice no?
[01:18:07] potrebbe farlo lui, ma documentazione vapi per api reference, perfetto e poi documentazione
[01:18:25] vapi per mcp se necessaria ok e ora dovremmo avere tutto, non dovrebbe esserci più nulla
[01:18:37] riguardo, quindi perfetto. Allora, che cosa vogliamo che faccia? Uno, leggi attentamente
[01:18:45] la documentazione di VAPI, soprattutto quella in ingresso, per capire che cosa c'è al
[01:18:52] suo interno. Due, salva le informazioni che ritieni importanti per riuscire a creare
[01:19:01] agenti su WAPI nel file WAPI.md, pre, struttura il file WAPI.md, di modo tale che quando un
[01:19:13] utente ti chiede di creare un file, tu sappia esattamente cosa cercare e in che sezione
[01:19:22] della documentazione, di modo tale che tu possa andare a colpo sicuro, e quattro vorrei
[01:19:27] che per creare un prompt di una gente tu non utilizzassi un prompt fa da te, ma che utilizzassi
[01:19:35] il prompt che ti fornisco sotto, di modo tale che continuiamo ad avere una struttura di un
[01:19:41] certo tipo. Perfetto, ora gli mettremo il prompt, ma prima di metterglielo, prompt di
[01:19:48] riferimento, prima di metterglielo gli diciamo questo di nuovo, in Synthesis questo
[01:19:54] documento vapi.md deve essere un documento di riferimento, ogni volta che l'utente ti chiede
[01:20:01] di costruire un'agente vocale, entri dentro, capisci cosa devi fare e se devi creare un
[01:20:07] prompt, utilizzi il prompt di riferimento, come base per fare un prompt elevato a qualità.
[01:20:13] Perfetto, e ora che ci chiediamo qual è il prompt di riferimento, e qualcuno di
[01:20:16] voi l'ha già capito, quindi torniamo su Notion ed è esattamente il primo prompt
[01:20:21] che abbiamo fatto, quindi ora andiamo qua sotto, glielo incolliamo e ora faremo un
[01:20:28] bel plan mode, perché anche questo non è esattamente semplicissimo come tipologia di
[01:20:34] richiesta e quindi poi precederemo con invio. Allora io ora vorrei solo fare una cosa
[01:20:42] perché mi sta cominciando a dare fastidio, perdonatemi. Allora questo sarà così,
[01:20:48] lo faremo così e poi gli dirò solo una cosa perfetto e gli dirò hey per favore ora
[01:20:59] rinomina il documento naten.md in naten.md e aggiorna qualsiasi tipologia di documentazione
[01:21:09] ci faccia riferimento. Perfetto in… adesso gli dirò… solo perché è una cosa abbastanza
[01:21:18] sciocca, non necessaria, ma solo perché generalmente questi file.md sono scritti in caps e questa
[01:21:25] cosa l'avevo scritta all'inizio per farvelo vedere, ma adesso volevo solo rinominarlo
[01:21:29] di modo tale che insomma fossimo compliant con le convenzioni da software developer.
[01:21:37] solo perché se qualcuno lo prende poi non capisce
[01:21:40] magari voi ci state lavorando o qualcun altro dentro del progetto e non capisce che cosa siano questi file.md
[01:21:46] però insomma questo è fatto benissimo abbiamo riaggiornato tutto e ora
[01:21:52] siamo a posto, Claude dovrebbe essere ancora vuoto perché non gli ho ancora chiesto di fare niente
[01:21:57] perfetto questo pianifica e quindi ora una volta finito
[01:22:01] andremo a vedere insomma che cosa esce nella documentazione vapi e poi da lì
[01:22:06] continueremo a procedere fino a che poi non dovremmo finalmente fare il nostro ultimo
[01:22:11] cal voice agent .md che è sostanzialmente quello che ci permetterà poi di fare questi
[01:22:15] workflow complessivi. Perfetto, quindi qui abbiamo il piano, questo va benissimo, quindi
[01:22:23] come documento di riferimento abbiamo un contesto, struttura del vappi .md, abbiamo
[01:22:28] un overview, quick reference, assistenti, voice providers, transcriber, tool, telefono
[01:22:34] e, bene, squads, server URL, webhook, mcp, quindi abbiamo tutto quello che ci serve.
[01:22:40] Quindi non semplicemente.
[01:22:41] Primerò accetta e poi bypass permissions e, ehm, benissimo, poi il resto verrà fatto.
[01:22:49] Eh, ah, piccola variazione, l'ho chiamato vapi.md.
[01:22:57] Perfetto, e ora aspettiamo, quindi ora il nostro vapi.md è pronto
[01:23:03] e al volo abbiamo manuale operativo vocale, ogni volta che viene chiamato, cos'è, come funziona
[01:23:11] e ora abbiamo vedete endpoint, assistente, configurazione moduli, voice providers, quindi adesso sa qualcosa in più di noi
[01:23:21] sicuramente molte più cose
[01:23:23] e ora vedete che ha impostazioni chiave, quindi ora comincia ad avere tutti i dettagli del caso, perfetto
[01:23:30] quindi ora che cosa ci rimane da provare che tutto funzioni quindi gli chiederemo
[01:23:37] qualcosa del genere hey per favore potresti crearmi un'agente vocale su vapi che parli
[01:23:44] in italiano e si chiami agente vocale prova lingua italiana se puoi quindi transcriber
[01:23:53] italiano una voce italiana magari da 11 labs o qualcosa del genere dimmi se hai
[01:24:00] bisogno dell'apik di levenlabs per accederci o se puoi farlo direttamente da vapi e una
[01:24:06] volta che hai fatto questo io andrò a controllare dentro la piattaforma vapi che tutto funzioni.
[01:24:12] Mi raccomando non fare alcun tipo di workflow, quello lo chiederò a parte e fai sempre riferimento
[01:24:20] al file e ora gli diremo vapi.md pianifico e ora di nuovo vedremo il piano, ci assicureremo
[01:24:34] questa cosa è una cosa importante, ci assicureremo ora che nel piano ci sia effettivamente scritto
[01:24:41] che non deve fare il workflow perché molto spesso quello che succede è che noi gli
[01:24:45] lo diciamo poi nel piano ci è scritto file workflow tutto esplode e noi comincieremo
[01:24:49] e continueremo sempre ad utilizzare questo approccio quindi prima disegneremo
[01:24:53] cosa su VAPI, quando siamo soddisfatti allora lo faremo su NITEN e poi ci sarà il progetto finale.
[01:24:59] Per creare la gente vocale su VAPI mi serve la tua API key di VAPI, non ne ho trovata una nel
[01:25:06] file, puoi fornirmela bene. Quindi ora faremo login alla piattaforma, allora suppongo che
[01:25:14] che siano qua dentro, credo sia una public key, quella di cui abbiamo bisogno, quindi
[01:25:21] add key, voice agent youtube italia, perfetto, select all, voice agent youtube italia, perfetto
[01:25:41] e qui gli diamo accesso a tutto o a niente, ma quasi quasi gli diamo accesso a niente
[01:25:48] gli diciamo che faccia quello che vuole, quindi create public token, quindi incolla la kp allora,
[01:25:59] quindi vapi public API key e ora gli diremo anche questo, quindi anzi YouTube Italia 2
[01:26:21] e ora gli diremo questo, quindi WAPI, WAPI, Private API. Chi? Perfetto, ora rimetto il
[01:26:40] mio faccione apposto e ora valutiamo che tutto sia andando per il meglio, quindi
[01:26:46] contesto, passi, recupera, verificare la creazione, file di riferimento, verifica,
[01:26:53] perfetto, qua non vedo in workflow, quindi ora bypass permission e dovremmo
[01:27:00] esserci. Perfetto, allora, agente creato con successo e proviamo con questo,
[01:27:06] nome, l'emvoice, allora questa avrà come voce SARA, multilingual, deepgram,
[01:27:14] lingua italiana, primo messaggio, ciao, sono la gente vocale, come posso aiutarti?
[01:27:19] Allora, quello che faremo ora sarà andare qui in vapi, dentro nostri
[01:27:23] assistenti abbiamo agente vocale, prova, quindi ora sappiamo che funziona, le
[01:27:29] itensi sappiamo che è meglio buttarsi giù da un ponte, perfetto, ciao, sono la
[01:27:34] gente vocale e ora qui abbiamo un sacco di cosine.
[01:27:41] Allora, ovviamente non gli abbiamo dato alcun contesto, quindi non ci saranno file, configurazione
[01:27:46] 11labs, ce l'abbiamo, voce perfetto.
[01:27:49] Adesso, giusto per sentire, deepgram italiano, giusto per sentire, ora vediamo che cosa
[01:27:57] succede se, anzi se ci risponde in italiano… Ciao, sono la gente vocale di prova, come
[01:28:09] posso aiutarti? Ciao, vorrei prenotare un appuntamento.
[01:28:15] certo perché giorno e ora vorresti prenotare per domani alle 4 capito domani alle 4 per
[01:28:26] quale servizio vuoi prenotare l'appuntamento va bene ok allora suona un po' robotica ora
[01:28:33] possiamo provare a fare una cosa di questo tipo giusto per sport hey mi piace ho un
[01:28:42] problema la latenza è tipo due secondi quindi è lentissimo abbiamo un modo per
[01:28:49] migliorare questo. Mi piacerebbe essere un po' interativo con la gente e fare in modo
[01:28:54] tale che magari riesca ad avere una conversazione che è più simile a quella di un umano. Oltretutto,
[01:29:02] mi sembra che sia un po' robotica la voce, quindi abbiamo qualche modo per migliorarla
[01:29:08] o per far sì che tutto questo sembri un po' meno AI. E vediamo ora cosa succede sulla
[01:29:16] basso del feedback che gli abbiamo dato. Perfetto, aggiornato, ecco cos'ho cambiato,
[01:29:21] LLM prima dopo, ne sposta un momento più rapida, modello voce, siamo a flash, stability,
[01:29:31] similar boost e proviamo. Va bene, se io vado ora nella gente vocale, vedo che il mio cosa
[01:29:39] succede, non so perché ci sia questa scritta davanti, ok, che il mio agente vocale
[01:29:44] prova ora una latenza di 6,65. Ovviamente avrà sicuramente degli impatti, no? Però
[01:29:50] vediamo, ed è quello che volevo dirgli, prima era un costo di 2 centesimi, ora l'ha anche
[01:29:54] ridotto, come ora diventi molto più semplice migliorare le cose se capiamo che cos'è
[01:30:00] che stiamo facendo, cioè noi qui dobbiamo cominciare a pensare che con Cloud Code l'importante
[01:30:04] riuscire a pensare per sistemi, capire quali sono i building blocks che lo fanno
[01:30:10] E poi possiamo essere un po' più targeted e quindi andare direttamente a colpire la cosa
[01:30:15] che ci serve, no?
[01:30:16] Quindi quello che vogliamo fare è letteralmente anche capire come piattaforme, come Nathan,
[01:30:21] come Vapi, e via dicendo, solo perché migliorerà la capacità che abbiamo poi di interagire
[01:30:26] con Cloud e di ottenere poi quello che vogliamo.
[01:30:28] Ora proviamo a vedere cosa succede.
[01:30:31] Se noi cominciamo ad iniziare una conversazione e vediamo appunto che cosa succede e
[01:30:35] la qualità.
[01:30:36] Ciao, solo la gente vocale di prova, come posso aiutarti?
[01:30:40] Ciao, vorrei prenotare un appuntamento per domani.
[01:30:44] Certo, a che ora vorresti prenotare l'appuntamento per domani?
[01:30:48] No bene, abbiamo visto sostanzialmente che sia un attimo di tutta la latenza, ma possiamo
[01:30:53] molto migliorare per quanto riguarda il suono e quello semplicemente viene con voce più
[01:31:02] costose e con punteggiatura dentro alle risposte delle AI, quindi abbiamo dei modi anche un
[01:31:09] po' subdoli, anzi scusate, di modificarla, però non è il momento giusto per farlo, questo
[01:31:18] ci serve solo per capire ok, tutto quello che stiamo facendo abbiamo messo i vari blocchi
[01:31:24] che funzionano e ora quello che ci rimane da fare è pulire la nostra conversazione
[01:31:29] vedere ora come creare il nostro voiceagent.md. Allora, per farlo, possiamo utilizzare un prompt
[01:31:38] di questo tipo. Allora, ho scritto qualcosa del genere. Allora,
[01:31:43] A Cloud crea un file chiamato voiceagent.md, anzi qui potrei dirgli addirittura, l'ho
[01:31:50] già creato, quindi per favore semplicemente scrivici dentro. Questo file è la tua
[01:31:59] guida di riferimento per costruire un voice agent, segui sempre gli step in questo ordine.
[01:32:05] Leggi la richiesta dell'utente, apri vapi.md e carica la documentazione necessaria.
[01:32:09] Poi, usa l'esempio di prompt dentro vapi per creare il prompt della gente, configura la gente
[01:32:15] quindi modello, voce, lm, qualsiasi altra cosa richiesta dell'utente, se l'utente fornisce
[01:32:20] un workflow da costruire apri a naten.md, usa le competenze per crearlo, una volta
[01:32:25] creato il workflow, recupera il webbook URL dal nodo trigger e poi crea un tool
[01:32:30] dentro la gente vocale che punta quel webbook per finire collega il tool alla
[01:32:34] gente. Questo è importante perché ogni volta che faremo un nodo o qualcosa
[01:32:40] in NETN, avremo un URL, quindi un indirizzo a cui poi dovremmo riferirci,
[01:32:47] quindi il motivo per cui glielo chiediamo è perché interagiremo e
[01:32:51] manderemo dati, quindi noi parleremo alla gente, la gente li terrà dentro, magari li porterà
[01:32:57] in un CRM o cose di questo tipo, tramite N8N, quindi questo ci servirà e lo useremo. Perfetto,
[01:33:04] quindi ora faremo plan mod e poi semplicemente aspettiamo e vi faccio vedere il risultato
[01:33:10] qua dentro del voice agent. Perfetto, ora ha finito e quindi questo è il file di riferimento
[01:33:16] principale, quindi workflow, set step, analizza, crea la gente, configura la gente, insomma
[01:33:22] tutto quello di cui abbiamo parlato con i riferimenti.
[01:33:26] Ora quindi l'ultima cosa che ci rimane da fare è quella di andare a crearci il nostro
[01:33:31] famigerato cloud.md, quindi perché? Perché come sapete, quando io entro in una chat
[01:33:37] qualunque e chiedo un qualcosa a cloud, la prima cosa che cloud fa, e fatemi cambiare
[01:33:43] magari colore è andare dentro il cloud.md, dal cloud.md cercherà di capire quali sono le
[01:33:49] impostazioni corrette e quindi poi farà probabilmente questo e dopo una volta fatto quello capirà
[01:33:55] che deve andare qui e dopo una volta fatto questo capirà che deve andare qui. Il cloud.md
[01:34:00] è un qualcosa che il cloud leggerà ad ogni initializzazione quindi bisogna crearla
[01:34:08] e perché sarà il nostro file di riferimento principale.
[01:34:10] Allora, detto questo, per farlo c'è una cosa molto molto carina, quindi ve lo faccio
[01:34:15] vedere al volo, o facciamo un mega prompt o facciamo slash init e quindi questo sostanzialmente
[01:34:23] permetterà di crearci in automatico il nostro file che si chiama appunto cloud.md e insomma
[01:34:29] lo vedremo adesso al volo perché è sostanzialmente il file di inizializzazione del progetto,
[01:34:38] quindi man mano che ci mettiamo queste cose dentro e la gente andrà poi a capire che
[01:34:44] appunto questo è quello che deve fare e quindi poi creerà il nostro cloud.md ok perfetto
[01:34:50] infatti qui ora lo vedete e lui ci dice now let me create cloud.md for this project
[01:34:56] root quindi semplicemente con quello siamo riusciti a crearlo perfetto ora ci dice
[01:35:02] creato e se noi andiamo abbiamo il what, how e why e oltretutto ci ha creato un altro
[01:35:08] paio di di cosi interessanti, git ignore, ma giusto per farvi capire, questo è un file
[01:35:13] di guida per cloud code, creo voice agent, quindi costruisco usando vapi più na10 o tutta
[01:35:23] la documentazione in italiano e cose di questo tipo, quindi adesso questo è in inglese
[01:35:28] ovviamente con il comando slash init potrei tradurlo in italiano, però questo è quello
[01:35:34] che ti dice.
[01:35:35] Ora, lo lascio così perché stiamo facendo per educational purposes, però questo è un
[01:35:42] comando molto facile che vi salva un po' di mal di testa perché semplicemente è fatto
[01:35:48] sulle best practices.
[01:35:49] Perfetto.
[01:35:50] Quindi, detto questo, possiamo procedere con la creazione del nostro gente end-to-end
[01:35:55] E quindi ora possiamo dargli un mega prompt che ci aiute insomma a procedere quindi a
[01:36:00] creare questo questo grosso voice agent che poi andremo a testare e quindi caleremo nel
[01:36:05] pratico.
[01:36:06] Hey Cloud sto cercando di costruire un AI receptionist e sostanzialmente quello che
[01:36:13] voglio fare è creare un agente che possa ricevere le chiamate da parte dell'utente
[01:36:22] e possa interagire con l'utente.
[01:36:24] cose che questi high receptionist può fare sono prenotare gli appuntamenti, cancellare
[01:36:33] gli appuntamenti, rischidulare gli appuntamenti nel caso in cui fossero stati già presentati
[01:36:41] precedentemente e per farlo la gente dovrà raccogliere alcune informazioni come per
[01:36:47] ad esempio un nome, un connome, anzi, scusami, un nome, un email e un... e basta così.
[01:37:03] Vorrei che queste inf... anzi, e quindi nome, email e ragione del contatto. Poi, vorrei
[01:37:11] che queste informazioni venissero poi collegati con un CRM. Questo CRM per scopi educativi
[01:37:21] sarà un Google Sheet che dovrà avere obbligatoriamente la stessa nomenclatura dei campi che utilizziamo
[01:37:34] dentro VAPI. Assicurati anche poi ovviamente che dentro al CRM venga anche contenuta la data,
[01:37:41] perché appunto non vorrei mai che poi nel CRM non ci sia la data dell'appuntamento e assicurati
[01:37:48] che il formato di questa data sia compatibile con quelli che sono contenuti all'interno di
[01:37:54] Google Sheet e anche che in i ten gli confermi. E quindi una volta pensato a questo vorrei
[01:38:02] vorrei che tu ragionassi per sistemi, quindi non vorrei che tu facessi un mischiotto di
[01:38:11] tutto, ma vorrei che tu sostanzialmente dividessi questi workflow con una task ben specifica
[01:38:17] perché come sai lei ha il lavoro bene con task lineari, quindi uno è per il booking,
[01:38:23] uno è per la cancellation, uno è per il rescheduling, per esempio, e vorrei poi anche che ci fosse
[01:38:34] un quarto workflow, magari per delle FAQ aziendali, perché vorrei anche fare in modo che io possa
[01:38:45] inserire al tuo interno una file che lo utilizzeremo come knowledge base. Ovviamente questi quattro
[01:38:53] workflow dovranno essere fatti nelle ten e dovranno essere sì fatti nel migliore dei modi
[01:38:59] e dovranno funzionare tutti. Per quanto riguarda la zona geografica oggi è il 24 di marzo
[01:39:12] 2026 quindi assicurati di avere questo dato al tuo interno. Per quanto riguarda le date, ti ho dato
[01:39:19] questo dato solo perché tu possa avere un aggancio ma dovresti a livello teorico utilizzare variabili
[01:39:24] dinamiche dentro VAPI e di modo tale che tu possa anche averle dentro NITN. Tutto dovrebbe
[01:39:31] essere interattivo, non dovresti avere niente di hard coded, se non ovviamente i dati all'interno
[01:39:36] di un CRM. Vorrei che una volta fatto questo tu avessi un processo di verifica e di test
[01:39:44] iterativo continuo, di modo tale che tu non debba richiedere il mio intervento affinché
[01:39:49] questo venga fatto e vorrei che tu utilizzassi la funzione chat che c'è interna a VAPI tramite
[01:39:57] API dove puoi sostanzialmente continuare ad interagire a parlare in autonomia tu con
[01:40:02] gente vocale, di modo tale che io possa avere un prodotto finito alla fine. Allora, vorrei
[01:40:09] che procedessimo un'ultima informazione è la gente dovrebbe interagire con me in italiano,
[01:40:19] tutte le conversazioni verranno fatte in italiano, quindi mi aspetto che tu stia efficientando
[01:40:23] tutto sia a livello di transcriber, che a livello di voice, che a livello di LLM per
[01:40:30] far sì che anche i vari prompt sia in italiano e per far sì che tutto sia il più efficiente
[01:40:35] possibile.
[01:40:36] Come mi piacerebbe procedere per questo piano è nel seguente modo, vorrei che cominciassimo
[01:40:44] prima con guardare questo voice agent partissimo da cloud.md, poi a livello teorico dovremmo
[01:40:55] procedere con creare la gente in VAPI e con successivamente creare il tutto in N8N, utilizzando
[01:41:02] skill ed mcp. Hai tutta la documentazione all'interno, ora io aggiungerò il file come conoscenza
[01:41:11] che è il database con le informazioni azientali. Perfetto? E ora gli darò quindi questo
[01:41:19] file qui, gli lo metterò dentro, lo chiameremo conoscenza.pdf così per sport, perfetto, conoscenza.pdf
[01:41:30] che è da dovesi informazioni aziendali, assicurati di capire dal file di conoscenza.pdf di che
[01:41:39] tipologia di agente si tratta, assicurate di capire la clinica, assicurate di capire
[01:41:44] tutti i servizi, orari e via dicendo. Per favore, un'ulteriore cosa è, siccome so che
[01:41:53] per avere un prompt scritto in modo efficace per non impattare le performance mi servirebbe
[01:42:00] avere la knowledge base, quindi conoscenza attaccata come tool, per favore fa sì
[01:42:09] che tu utilizzi il tool, conoscenza.pdf, che io caricherò dentro ora a WAPI, quindi
[01:42:18] lo troverai all'interno, e fa sì appunto che questa conoscenza venga appunto pescata
[01:42:24] come tool. Anzi, anche il CRM dovresti, quindi il Google Sheet, dovresti collegarmelo
[01:42:31] come tool. Facciamo che, invece che farlo io, fai entrambi queste cose tu, io ora
[01:42:38] ti do semplicemente l'accesso ad un Google Sheet che è completamente vuoto, di modo
[01:42:44] tale che tu possa poi agire in autonomia e evitare di chiedermi informazioni. Perfetto,
[01:42:53] ora gli faccio, vabbè adesso ve lo mostro in questo schermo ma sostanzialmente ho
[01:42:59] fatto questo file vuoto, quindi gli mettiamo Google Sheet, so che perché questo funzioni
[01:43:11] che affinché tu possa connetterti, devo condividere questo file con qualcosa, quindi assicurati
[01:43:20] di farlo solo nel momento in cui questo serve. Ok? Quindi possiamo partire con il prompt
[01:43:27] che ti ho dato. Va bene, allora un prompt giganorme, sono tipo 8 minuti di brainstorming.
[01:43:34] Questo perché? Perché a livello teorico voglio essere il più dettagliato possibile
[01:43:40] con questo prompt perché diciamo che se io ora dovesse dirvi ok, preferite dare l'informazione
[01:43:49] e spiegarle bene ad un impiegato o a un sistema una volta sola e metterci dieci minuti oppure
[01:43:56] metterci sei ore e spiegargli alle ventisette volte, beh, io preferisco fare tutto il lavoro
[01:44:02] upfront, quindi essere quanto più dettagliato possibile all'inizio, dare quante più indicazioni
[01:44:07] possibile e poi eventualmente solamente verso la fine andare poi a toccare tutto il resto.
[01:44:12] Bene, ora quindi aspettiamo che il nostro sistema con calma pianifichi e poi procederemo con il resto.
[01:44:20] Perfetto, quindi siamo arrivati ora al piano finale che rivediamo velocemente assieme,
[01:44:28] quindi AI Receptionist per la clinica dentale, come costruire un AI Receptionist,
[01:44:34] cheat d'appuntamenti, ok, ci ha dato un bel po' di cose, vabbè ha fatto un minisiarem,
[01:44:42] ok, anche eccessivo per quanto mi riguarda. Prompt VAPI, perfetto, segue il nostro prompt
[01:44:49] standard, configurazione, workflow NA10, perfetto, abbiamo i tool, bene, check availability,
[01:45:01] appointment, canso, reschedule, search, non vedo end call, ok, quindi non vedo la capacità
[01:45:10] di chiudere, lo farà all'utente ma sarebbe carino, vabbè dai non complichiamolo troppo,
[01:45:15] però ecco, una cosa che non vedo è la capacità da parte della gente di chiudere la chiamata,
[01:45:22] quindi dovrei dirgli ok aggiungi end call ma poi c'è già messo tipo sei anni e quattro
[01:45:27] l'une a fare questa roba qui quindi ok ordine di esecuzione vapi google auth quindi dovremmo
[01:45:34] configurarla perché non l'ho ancora fatto con la scienza sequenza di implementazione salvare
[01:45:40] le chiavi di vapi lì dentro ok setup di google perfetto ci siamo fase test set testing
[01:45:50] autonomo vipi chat api file critici ci siamo ci siamo e ora caffè allora
[01:46:10] perfetto lui sta facendo dopo aver fatto questo caziliardo di cose mi dice di
[01:46:15] andare su neiten aprire uno dei quattro workflow appena creati e clicca su un
[01:46:23] un nodo e poi fare il collegamento alle credenziali. Perfetto, quindi ora noi andiamo qui, N8N, vediamo
[01:46:32] dove stiamo andando. Ah, ok, allora aspetta che archivio al volo questi che così li
[01:46:38] teniamo sotto occhio, uno dei quattro a caso, quindi facciamo Book Appointment. Allora
[01:46:47] faremo sign-in with Google, perché questo abbiamo un OAuth authentication, quindi andrà
[01:46:53] via veloci veloci. Perfetto, quindi ora facciamo il nostro login. Queste sono le mie
[01:47:00] dummy emails, quindi spammatemi. Ok, collegato e ora... Ok, perfetto, quindi ora fatto
[01:47:13] credenziale creata e fatto, adesso vediamo se la presa, ma mi ha detto uno solo quindi
[01:47:22] suppongo che ora è tutto perfetto, ora devo preparare, prima verifico che le credenziali
[01:47:30] funzionino, quindi perfetto, ha visto che il resto dovrebbe andare, perfetto, quindi
[01:47:43] credo che ora tutto sia andato, tutto va da bene come dovrebbe andare, ok sì
[01:47:49] si confermo o update all for any 10 workflows, l'ha visto e quindi sta facendo l'update.
[01:47:56] Perfetto, ora sembra aver finito, quindi il riepilogo e i high receptionist Sara, prompt
[01:48:04] Sara fatto ed è qua dentro, ok, ok, perfetto, flusso, domande, va bene, poi
[01:48:19] VAPI ASSISTANT, quindi ora abbiamo su VAPI LOGIN, anzi fatemi vedere se riesco ad accederci
[01:48:28] al volo così, abbiamo perfetto SARA RECEPTIONIST CLINICA BEGGIATO con il nostro PROMPT, una
[01:48:38] latenza di un cazziliardo di universi però a un buon costo, poi knowledge base caricato
[01:48:46] come tool, allora verifichiamolo, non è in files, perfetto, non è dentro al prompt,
[01:48:58] nella knowledge tool, search knowledge base, quindi nei tool, ora search knowledge base,
[01:49:09] cerchi informazioni, c'erano che nell'identale usano questo tool per rispondere a domande
[01:49:12] servizi, protocolli, FAQ, perfetto, quindi ha caricato conoscenza pdf, che è questo, ottimo.
[01:49:20] Poi c'è che availability, calcola slot, perfetto, scrive nel data sheet, vediamo se il Google
[01:49:29] sheet ha le robe giuste, quindi nome, email, telefono, perfetto, non l'ha messo, quindi
[01:49:36] fatto che provi anche a vuoto, stato, confermato e message action. Ok, questa non ha un'azione
[01:49:46] perché è un cancellato, ottimo, perfetto, data, ok. E dopo cosa ci dice? Segna come
[01:50:01] cancellato, Google Sheets IRM e 5 tool VAPI. Perfetto. Quindi abbiamo tutto, ora N8N, YouTube
[01:50:12] A. Ora no, vediamo che tutto vada. Ok. Perfetto. Cancel appointment. Ok. Perché non gli ho
[01:50:26] ho detto di andare con agenti AI, quindi lui ha fatto con formule molto interessante e codice
[01:50:37] di modo tale che sia più semplice e quindi lascia fare il direzionamento a VAPI.
[01:50:43] Va bene, vediamo comunque che tutti questi workflow avremmo dovuto farli da soli in autonomia
[01:50:48] cosa che sarebbe stata folle e quindi, e quindi, ecco sono tutti pubblicati anche
[01:50:54] quindi sono live, abbiamo i webbook live e questo era quello che vedevamo, no, quindi
[01:50:58] qui abbiamo il webbook in ingresso, il URL e dopo abbiamo le varie cose qui.
[01:51:03] Allora, testiamolo, sapete ora la latency, non perdo un millenio a farlo, se questo
[01:51:10] funziona vi lascio sotto tutto quanto tutti prompt, tutti workflow in A10, avrete una
[01:51:15] cartella credo con tutto, per i miei membri della community vabbè, vi lascio con il
[01:51:21] la nostra classe, vi lascio un altro po' di materiale, per tutti gli altri invece vi lascio
[01:51:25] una cartella o un Google Form, qualcosa.
[01:51:28] Vediamo.
[01:51:29] Allora, voglio capire però, allora, deve prenotarmi l'appuntamento e vorrei però capire
[01:51:34] magari che tipologia di servizio andare a chiedergli.
[01:51:38] Allora, perfetto, allora, vogliamo testare innanzitutto che non possiamo prenotare
[01:51:47] dopo le otto.
[01:51:48] Cominciamo con questo.
[01:51:49] Faccio così solo perché è molto più veloce. Vorrei prenotare, vorrei prenotare un appuntamento
[01:51:57] alle 8 di domani, 8 di sera. Allora Giovanni Beggiato, Esbian Camento, Gio Beggiato at gmail.com,
[01:52:28] vediamo che cosa succede ora grazie domani alle 20 non siamo aperti, perfetto. Ha un'altra
[01:52:35] preferenza per una fascia oraria. Ho detto, non mi ricordo più cosa ho detto, credo
[01:52:42] di aver detto sbiancamento, ok, perfetto. Allora, sbiancamento in studio. Ma prima di
[01:52:50] dirti la fascia oraria mi dici quanto costa sta cosa? Vabbiamo con un prompt a caso proprio
[01:52:59] come la gente... in modo preciso per sapere e fare una visita gratuita, vuole fissarla?
[01:53:05] no vorrei capire il costo di uno sbiancamento ok allora non capiamo innanzitutto il costo
[01:53:20] dello sbiancamento cosa molto importante quindi questa è una cosa che non riusciamo
[01:53:25] a vedere perfetto poi vediamo se possiamo capire come paghiamo posso pagare in contanti
[01:53:40] Allora, qui fino al limite legale, fino al limite legale, ok, quindi capisco che sta
[01:53:50] avendo problemi nella visualizzazione di tabelle, questo è quello che ho capito, fammi
[01:53:56] vedere questo, allora chiediamo che tipologie di dottori ci sono in studio, cioè come
[01:54:02] si chiamano, allora se la teoria è confermata dovremmo avere qualche problema a vedere
[01:54:08] questi. Ora valuteremo se questo è vero oppure non è vero. Beggiato per Odontoiatria,
[01:54:16] Generale, Marta Silvestri per Orto Donzia ed Estetica dentale e Dottor Luca. Ok. Allora,
[01:54:26] forse, allora gli abbiamo detto non quotare mai al telefono senza visita. Allora tutto
[01:54:37] funziona fenomenale! Già one shot! Cazzo che figo! Che figo! Ok, perfetto, funziona
[01:54:47] molto meglio di quello che credevo! Ok, vediamo... Allora, vediamo se ho un dolore acuto cosa
[01:55:01] succede. Io ho un dolore acuto però sei sicuro che non posso fare niente a riguardo. Vediamo
[01:55:10] se devo per forza fare la visita gratuita. Devo per forza fare la visita gratuita anche
[01:55:16] se sto male e sto per morire? O mi puoi dare un preventivo?
[01:55:20] Oh, facciamo stress test per vedere cosa succede.
[01:55:25] Tipologia di problema? Allora Giovanni e poi la tipologia di problema è il problema è
[01:55:36] sangue che non si ferma. Non ci sono slot per domani, la passo subito alla segreteria
[01:55:49] per trovare una soluzione immediata. Perfetto, quindi abbiamo rerouting, corretto.
[01:55:55] è corretto che domani in uno slot a calendario perché il mio calendario è fottuto. Perfetto.
[01:56:01] Allora, ora vediamo se riesce a capire che mercoledì ha uno spazio alle 5 e se volessi
[01:56:13] avere uno spazio mercoledì c'è qualcosa dopo un mezzo giorno come disponibilità.
[01:56:18] Allora, mercoledì, vediamo orari di apertura, haa, spettacolo, ottimo, e sabato mattina
[01:56:44] ore dieci, vedete comunque come una conversazione può facilmente deteriorare.
[01:56:53] Ok, questo è falso invece, non ci sono slot disponibili perché io li ho, quindi fa
[01:56:59] fatica a vedere gli slot disponibili. Questo perché può succedere? Beh, perché innanzitutto
[01:57:06] dovrei vedere di avere accesso ad un calendario. Cosa che io qua non vedo per esempio. Quindi
[01:57:14] ora diamo il feedback a Claude. Funziona tutto, ma non abbiamo accesso al calendario.
[01:57:21] Vediamo così. No, va bene, voglio cancellare l'appuntamento. Vediamo che cosa succede
[01:57:30] nel nostro… Quello appena discusso trova le cose dentro alla chat, vediamo che succede.
[01:57:39] Non ho trattato l'accontamento? No, apposto, grazie. Anzi, frenotami al primo buco disponibile.
[01:57:50] Ogni giorno va bene e qualsiasi era riva bene, dimmi solo quando. Perfetto. Allora,
[01:58:07] torniamo a Claude e lo sistemiamo. Hey Claude, allora vedo che la gente è fatto, la Knowledge
[01:58:15] Base c'è, ma ho dato un occhio a i tuoi check availability book appointment, cancel appointment
[01:58:23] e tutte quelle cose lì. Allora io non credo che tu abbia oggi accesso ad un Google Calendar
[01:58:29] per poter verificare la disponibilità. Il motivo in cui te lo dico è perché la
[01:58:36] la gente non riesce a prenatare uno slot mai e a continuadarmi errori dentro al tool.
[01:58:44] Tipesto ti incollo anche l'errore che il tool mi sta dando, di modo tale che tu possa magari
[01:58:53] fare debugging.
[01:58:54] Per favore entra nella conversazione, cerca nei logs che cosa sta succedendo e cerca
[01:59:00] di risolverlo.
[01:59:01] Devi assicurarti che io abbia la possibilità di aver accesso ad un Google Calendar.
[01:59:05] Per favore è sempre collegato alla stessa e mail e quello che vorrei che tu facessi
[01:59:12] è fai tutte le verifiche del caso, quindi prima di confermarmelo devi avere un check
[01:59:21] di availability, book appointment, cancel appointment e rescaggio e io devo
[01:59:27] vederli anche a calendario, cosa che oggi i tuoi cosi di test non li ho visti.
[01:59:33] Quindi per favore fallo e una volta fatto tutto conferma, andiamo in plan mode e poi vediamo
[01:59:44] che cosa succede.
[01:59:45] Ok, perfetto, è già capito il problema, i tu non rispondono correttamente a Vapi e
[01:59:50] manca l'integrazione con Google Calendar, analizzo la situazione e ora riparte con il nostro
[01:59:55] ciclo.
[01:59:56] Bene, quindi ora sostanzialmente io continuerò a farlo adesso finché tutto non si sistema
[02:00:00] ma abbiamo capito che sostanzialmente adesso è solo una questione di abbiamo impostato
[02:00:05] a grandi linee la testa, quindi come impostare questa tipologia di sistemi. Ora andremo semplicemente
[02:00:13] a callarle nel pratico, quindi continueremo fino a che non abbiamo fatto come si chiama
[02:00:17] fine tuning della nostra soluzione con le necessità aziendali. Vedete, ora come vedete
[02:00:23] C'è che avrebbe le abilititi fallisce monte probabilmente dato da questo.
[02:00:27] L'utente vuole Google Calendar per la disponibilità, non solo Google Sheets, questo è importante.
[02:00:34] E esistono già tu il Google Calendar Legacy in Vapi che non sono collegati, verifico lo
[02:00:41] stato attuale e lo faccio.
[02:00:43] Quindi ora sta verificando lo stato dei logs, ora mi ha fatto un bel piano quindi suppongo
[02:00:48] abbia trovato il problema o presunto tale.
[02:00:50] quando va picchiamo al webo che inviede dati informato diverso da quello che il nostro
[02:00:55] codenode si aspetta tu con l'argument and define devo vedere che dati
[02:01:00] di vapi effettivamente invia e quindi poi fa tutto le sue cosine quindi ora procediamo
[02:01:06] aspettiamo e una volta fatto vediamo il risultato fetto allora
[02:01:11] ora vediamo dovrebbe
[02:01:14] funzionare
[02:01:16] anche sul mio calendar. Allora andiamo su Vapi, gli facciamo Assistant, Sara e gli diciamo
[02:01:26] Hey mi chiamo Giovanni, la mia mail è gino at gmail.com. Vorrei prenotare un appuntamento
[02:01:39] per domani mattina alle 10 e la ragione della mia visita è un dolore acuto, anzi è un
[02:01:51] igiene dentale, anzi alle 10 non posso perché ora che ho un appuntamento e quindi vediamo
[02:02:03] Send, vediamo che succede, si, in generale, perfetto, un attimo che controllò disponibilità
[02:02:15] per venere di mattina, ora a livello teorico dovremmo avere un tool response, va bene,
[02:02:24] 27, perfetto, l'ingegnere disponibile alle 8.30 oppure alle 9, Giovanni prene di o disponibile
[02:02:33] alle 8.30 oppure alle 9, quale preferisce specia alle 10, non si può. Mi dispiace ma le 10
[02:02:43] non c'è disponibilità, fammi controllare, c'è le susponga perché ragioni quindi alle 8.30 perfetto,
[02:02:51] Ricapitolando, venerdì, 27 marzo, confermo, yes, va bene, vediamo ora che cosa succede,
[02:03:10] prenotato a bisogno d'altro, allora Giovanni Gino 27, confermato, perfetto, ora andiamo
[02:03:21] vedere se è nel calendario e vediamo che alle 8.30 ce l'abbiamo a calendario il venerdì
[02:03:28] allora vediamo se riusciamo a fare un'oravo del genere ok e gli diciamo sempre qui chat
[02:03:38] ei ciao queste sono le mie informazioni vorrei cancellare l'appuntamento perfetto
[02:03:51] vediamo se riusciamo a cancellarlo e vediamo cosa succede anche al CRM perché non abbiamo
[02:03:58] Dattograndi risposte allora appuntamento cancellato diamo ok serve altro no grazie grazie buona giornata te ora controlliamo
[02:04:11] E perfetto dirai che ci siamo qui è rimosso non c'è più e quindi fatto il workflow funziona ok ora vorrei controllare solo
[02:04:22] Uno dei log DNA 10 per capire se abbiamo fatto un buon lavoro vediamo buco appointment
[02:04:26] Vediamo Execution Logs, vediamo se c'abbiamo qualcosa e ora sono le 8 di sera, perfetto
[02:04:37] e ora vediamo l'appuntamento è prenotato, Anon confirmed, Peggiato LinkedIn, True e
[02:04:50] e dovrebbe essere alle 8.30 UTC, perfetto, è l'appuntamento corretto e ora possiamo
[02:04:57] vederlo anche in JSON, quindi ottimo. Abbiamo che le nostre cose sono state fatte come si
[02:05:04] deve e che tutto è stato prenotato, giusto? Quindi ora, qui abbiamo fatto la verifica
[02:05:10] del duplicato che non c'è, perfetto, ottimo. Quindi ora tutto questo funziona, abbiamo
[02:05:18] fatto un AI receptionist, possiamo anche giocare a rischedulare o a fare altro, o c'è
[02:05:25] che availability e basta. Direi che ora, beh, abbiamo detto per la latenza, possiamo
[02:05:32] andare a modificarla con i parametri che abbiamo, interagiamo con Cloud Code fino a quando
[02:05:36] non gli diciamo, hey, per favore modificare la latenza, fai la voce in italiano, fai
[02:05:40] questo, fai quello, e quindi sostanzialmente ora, il prossimo passo che ci rimane
[02:05:45] è andare a vedere quali sono le soluzioni che effettivamente vengono lasciate nel mercato.
[02:05:50] Quindi ora che ci siamo assicurati che tutto funzioni andiamo a vedere quali sono le varie
[02:05:53] soluzioni che possiamo fare per le aziende e oggi più o meno che livello di income hanno,
[02:05:58] che cosa potete aspettarvi e cose di questo tipo.
[02:06:01] Allora partiamo con AI Receptionist. Allora la difficoltà di questa soluzione è sostanzialmente
[02:06:08] media, media facile, e anche il costo di sviluppo è basso, ma che per cui l'abbiamo fatto adesso,
[02:06:17] qualche centinaio di euro no? Cioè abbiamo 30 euro mi pare di Anethen, 30 euro di Cloud
[02:06:23] Code se vogliamo andare proprio nella low tier, un 10 euro o 20 o 30 non mi ricordo
[02:06:30] di ClickUp se volessimo un CRM di un certo tipo e poi sostanzialmente questa è la vostra
[02:06:35] soluzione, giusto? Qualche costo per l'API qua e lì però. Generalmente un
[02:06:41] introito buono diciamo per queste cose qui, soprattutto considerando valore SAS è
[02:06:46] tra i 20 e i 120, per fare i conti cosiddetti della serva se abbiamo 20.000
[02:06:52] euro al mese e abbiamo un retener medio che generalmente è basso,
[02:06:57] pesterobe, no? È 100, 200 euro proprio quelli molto chip sono qui, generalmente per il mass
[02:07:06] market, abbiamo che ci servono sostanzialmente un ottantino, un centinaio di clienti. Sconsiglio
[02:07:14] di andare diciamo così bassi perché generalmente, sì, da indice che il servizio non è molto
[02:07:23] buono, ma da anche indice che generalmente meno si spende, più i clienti diventano difficili,
[02:07:29] scusate meno i clienti pagano, più diventano difficili, queste per esperienza perché hanno
[02:07:34] più aspettative, chiedono in borso più spesso, invece diciamo se ci posizioniamo un segmento
[02:07:40] un po' più premium, generalmente diventano clienti un po' più semplici.
[02:07:43] Ok, poi abbiamo, ed è il motivo per cui l'abbiamo costruita, no? Quindi questo
[02:07:50] è quello che potete aspettarvi. Se poi ovviamente lo fate con nicchie specifiche, quindi ovviamente
[02:07:55] sono più complesse perché c'è la norma, però immaginatevi, non lo so, insurance o
[02:07:59] cose di questo tipo, allora l'eachern è molto più basso, l'it-ticket è molto più
[02:08:04] alto e quindi ovviamente tutto poi cambia, ovviamente ascono il settore, però questa
[02:08:09] è una buona media, diciamo, ho fatto una cosa media non specifica al farmaceutico
[02:08:14] che ne so, ok? Poi, customer support per i commerce, generalmente avete un ticket un
[02:08:20] po' più elevato per questi, ma perché è più monetizzabile anche per un e-commerce,
[02:08:28] questa tipologia di cosa è molto più utile, no? E spesso avete anche la possibilità di
[02:08:35] fare il recupero ordini, quindi riuscite anche a monetizzare questa cosa qui con il
[02:08:40] in receptionist diventa un po' più difficile collegare la monetizzazione con il recupero
[02:08:46] cliente, anche se questa è una soluzione che per esempio io sto offrendo e va molto bene.
[02:08:51] Non sono ancora a SAS perché non mi interessa fare SAS ancora, sono ancora in studio del
[02:08:59] mercato però, insomma, vanno bene come soluzioni.
[02:09:01] L'Hydreat activation, super sexy, molto molto fica, generalmente difficile a far la voce,
[02:09:09] un'altra metodologia, email, messaggi, cose di questo tipo. Anche questo, questo è solo
[02:09:17] difficile da fare in maniera che i lead si riattivino per farvi capire sono i messaggi
[02:09:22] che ricevete dalle palestre, che vi dicono, ah, scontone! E questa invece ha un enorme
[02:09:28] potenziale perché generalmente sono prezzate sul revenue che viene fatto o recuperato,
[02:09:34] quindi è sempre una cosa dove se il vostro cliente pagando vi diciamo guadagna, poi guadagnate
[02:09:41] su guadagnato, quindi è un win per tutti. E dopo ok, questa è in assoluto la più difficile
[02:09:47] che è le AI recruitment che quindi sono, cominciamo a fare processi di un certo tipo
[02:09:51] no? Quindi e con recruitment poi potete vedere quello che volete, quindi che sia
[02:09:56] link di outreach, che sia outbound, ora non potevo metterle tutte, ma capite
[02:10:01] bene i modelli vari, diciamo che queste sono le più complesse e con giustamente anche ritorne
[02:10:08] sull'investimento maggiori, perché per esempio Outbound potrete guadagnare su percentuale
[02:10:13] di un cliente chiuso, percentuale di un candidato preso e cose di questo tipo.
[02:10:17] Per farla più semplice e perché voi abbiate magari un'idea di 80-20 di azienda più
[02:10:22] semplice, se questa è la nostra azienda, quindi... e potrezziamoli avere questo...
[02:10:27] anzi facciamo in blu questa è la nostra azienda ok è così in questo caso mi va anche bene che
[02:10:34] sia colorato allora tutte le soluzioni che vanno verso l'esterno quindi che contattano
[02:10:40] persone che non hanno a che fare con l'azienda quindi quello che chiamiamo generalmente outbound
[02:10:45] sono le soluzioni dove ci sono i dindini più alti no quindi contattare clienti contattare
[02:10:53] candidati, trovare, non lo so, l'oro, non lo so. E quindi tutte queste soluzioni di outbound
[02:11:02] sono quelle dove ci sono i soldi più grandi ma sono estremamente difficili da fare. Poi,
[02:11:09] invece, ora queste, diciamo, le soluzioni qua dentro, quindi interne ad un processo
[02:11:16] aziendale se questa ovviamente è la vostra azienda. Questa tipologia di soluzioni sono quelle che,
[02:11:23] diciamo, rientrano un po' nel dimenticatoio perché, perché tipo sono gli FAQ, cioè sì,
[02:11:30] va bene, è figo, però diciamo non abbiamo grossi impatti a livello economico. Per quanto riguarda
[02:11:35] invece le soluzioni borderline, che quindi sono quelle dove un lead vi conosce già per qualche
[02:11:41] che ragione, no? E quindi abbiamo questo flusso qui, quindi un cliente che chiama dal dentista,
[02:11:46] sono soluzioni relativamente semplici dove questa volta vi faccio mezza S di Superman con
[02:11:51] una stanghetta sola e questa ve la tratteggio perché non ce l'avete, però sono soluzioni
[02:11:56] che comunque possono andare bene ma diciamo dove l'introito è meno rilevante. Quindi
[02:12:02] questa è generalmente come mi piace immaginarmi le aziende, quindi le cose dentro, le
[02:12:07] cose nel bordo, le cose fuori, questo vale un po' per tutto. Quindi, motivo per cui in
[02:12:12] un'azienda normale piaccia o meno, escludiamo i tech che sono sempre ben pagati, ma i commerciali
[02:12:18] sono quelli che prendono più soldi. Perché? Perché siamo sempre in outbound. Generalmente
[02:12:25] poi il marketing è un'altra funzione ben pagata, però è una funzione che considero
[02:12:29] border. Ops, che è dove vero io, diciamo piange, è il motivo anche per cui ho
[02:12:34] fatto career shift un paio di volte. Detto questo quindi spero che il corso vi sia piaciuto,
[02:12:40] se siete proprietari di una piccola media impresa e volete soluzioni di questo tipo
[02:12:44] ho lasciato il link sotto quindi potete scriverlo e contattarmi, il team poi vi risponderà
[02:12:48] e vi farà sapere non appena possibile se c'è un fit, se invece siete un 9 to 5er e avete
[02:12:54] voglia di cominciare a vendere questa tipologia di soluzioni, vi lascio anche per voi
[02:12:57] il secondo link qua sotto che è il link al mio coaching program dove vi aiuto a
[02:13:01] partire con la vostra AI Agents in i prossimi 90 giorni.
[02:13:04] Detto questo, è stato fighissimo fare il corso, fatemi sapere cosa ne pensate nei commenti.
[02:13:09] Un saluto.
