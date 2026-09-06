
[00:00:00] In questo momento alcune aziende pagano
[00:00:02] fino a €10.000 per agenti che possono
[00:00:04] essere costruiti in un solo pomeriggio.
[00:00:06] In questo video costruisco un MVP live
[00:00:09] dall'inizio alla fine con Cloud Code e
[00:00:11] vi lascerò tutti i prompt replicarlo.
[00:00:14] Per costruirlo però non andremo a caso.
[00:00:16] Useremo la teoria di cui Andrei Carpati
[00:00:18] parla quando costruisce con AI,
[00:00:21] costruendo attorno a questo agente una
[00:00:23] piccola company Brain che potremmo
[00:00:25] utilizzare per costruire automazioni
[00:00:27] successive. Se sei nuovo al canale sono
[00:00:28] Joe con la mia agenzia di intelligenza
[00:00:30] artificiale Gente Sei facciamo
[00:00:32] consulenza ad aziende che vanno dai
[00:00:33] €10.000 [musica] al mese fino ai 50
[00:00:35] milioni di euro l'anno ed o poi una
[00:00:37] community privata di imprenditori e
[00:00:38] freelancer che vogliono applicare AI nel
[00:00:40] loro business o rivenderlo ad altri.
[00:00:43] Detto questo, cominciamo. Prima di
[00:00:45] andare a costruire il sistema, fatemi
[00:00:46] spiegare brevemente qual è il pattern
[00:00:49] che è stato descritto da Carpati. Qui
[00:00:52] quando parliamo di carpati parliamo di
[00:00:54] quella che viene definita la nostra LLM
[00:00:57] wiki e non è altro che il cervello di
[00:00:59] Obsidian che vedete spesso in alcuni
[00:01:00] video. Questo ne è un esempio e questo è
[00:01:02] appunto quello che andremo pian pianino
[00:01:05] a costruire e se vedete qui tutte le
[00:01:07] note sono collegate l'una con l'altra e
[00:01:10] abbiamo appunto questo effetto visivo di
[00:01:12] avere questa questa testa o questa brain
[00:01:16] interconnessa. Ora andiamo a vedere come
[00:01:19] funziona quello che Carpati ha poi
[00:01:21] descritto. Allora, il presupposto da cui
[00:01:23] parte è il seguente e cioè le persone
[00:01:26] quando utilizzano lei eh continuano a
[00:01:29] rispiegare tutto in ogni chat, ma
[00:01:32] abbiamo questa nuova metodologia che
[00:01:34] permette in qualche modo all'AI di
[00:01:36] cominciare a creare una propria
[00:01:38] conoscenza in file markdown che poi l'AI
[00:01:42] riesce a mantenere da sola. Quindi che
[00:01:44] cosa vuol dire? Se noi andiamo a
[00:01:45] leggerci il post, che è stato questo,
[00:01:48] sostanzialmente è stato un post iper
[00:01:50] virale in cui, come vedete qua sotto, in
[00:01:53] cui ha dettagliato quello che ora andrò
[00:01:57] a descrivervi.
[00:01:59] Che cosa ci dice? ci dice che questa LLM
[00:02:02] wiki ha tre strati principali o questi
[00:02:05] sono gli elementi costitutivi. Il primo
[00:02:07] sono le cosiddette fonti grezze ed in
[00:02:10] questo caso stiamo parlando di
[00:02:12] trascrizioni, di meeting, magari di
[00:02:15] documenti o email che appunto vengono
[00:02:19] lette e non vengono, diciamo, toccate in
[00:02:22] alcun modo, sono proprio grezze. Il
[00:02:24] secondo elemento costitutivo è una wiki.
[00:02:27] Questo significa che il concetto su cui
[00:02:30] si basa questa infrastruttura è un
[00:02:32] concetto di note atomiche che vuol dire
[00:02:35] delle piccole note che sono collegate e
[00:02:38] che l'EI pian pianino aggiorna per il
[00:02:42] nostro cliente o per la task che stiamo
[00:02:43] facendo. Un esempio è l'AI potrebbe
[00:02:47] cominciare a descrivere che il settore
[00:02:49] del cliente, la logistica per il nostro
[00:02:51] cliente, il budget invece magari è da
[00:02:54] definire, magari non ne abbiamo parlato
[00:02:57] in call e che i next step siano la
[00:03:00] proposta. Ovviamente dopo questa nota ci
[00:03:03] saranno un insieme di altre note che
[00:03:05] sono quelle che vedete qui con i quali
[00:03:07] qui magari abbiamo il transcript della
[00:03:09] chiamata, qui abbiamo invece magari le
[00:03:12] informazioni del cliente e possiamo
[00:03:14] quindi avere che tutte queste piccole
[00:03:16] note sono interconnesse tra loro e la
[00:03:19] parte bella è appunto, come vedete in
[00:03:21] questa immagine che l'AI alla fine può
[00:03:23] navigarle e aggiornarle in completa
[00:03:26] autonomia. La terza parte che andremo a
[00:03:28] vedere sarà lo schema, quindi un insieme
[00:03:31] di regole che ci spiegano come è
[00:03:33] organizzato la la wiki, quindi come
[00:03:36] navigare la wiki e che operazioni l'AI
[00:03:39] può fare. Che operazioni possono fare?
[00:03:41] Sono principalmente tre. La prima è
[00:03:44] un'operazione che definiamo di ingest o
[00:03:46] ingestione, quindi vuol dire che
[00:03:50] qualsiasi materiale nuovo è ingerito
[00:03:53] dall'AI ed è aggiornato grazie all'AI.
[00:03:57] La seconda operazione è l'operazione di
[00:03:59] qui. Cosa vuol dire? che noi possiamo
[00:04:01] fare una domanda a la nostra company
[00:04:04] Brain o alle nostre note e l'AI è in
[00:04:07] grado, tramite questi collegamenti eh di
[00:04:10] eh rispondere e di trovare la risposta
[00:04:12] corretta.
[00:04:14] La terza operazione che fa l'AI è
[00:04:16] un'operazione chiamata di lint. In
[00:04:19] sostanza, significa che l'AI riesce in
[00:04:22] automatico a fare il controllo delle
[00:04:24] contraddizioni, a pulire i dati vecchi e
[00:04:28] a gestire le note orfane. Premessa è,
[00:04:32] questa infrastruttura sarà
[00:04:34] un'infrastruttura che noi utilizzeremo
[00:04:36] ed è molto molto buona per una
[00:04:38] conoscenza di tipo personale. Il eh
[00:04:41] focus di tutto questo è che l'umano si
[00:04:43] mette a curare le fonti e fa le domande.
[00:04:45] Lei fa arresto di nuovo. E questa
[00:04:48] conoscenza qui, anche per questa demo,
[00:04:51] va molto bene se siete un solo founder.
[00:04:54] Nel caso in cui vi interessi qualcosa di
[00:04:55] un po' più strutturato, in community,
[00:04:57] qua dentro abbiamo un corso di company
[00:04:59] Brain nel quale andremo a spiegare che
[00:05:02] cos'è una company Brain, come si
[00:05:03] struttura e come scalare queste company
[00:05:05] brain ad un contesto aziendale. Che cosa
[00:05:07] ci permetterà quindi di fare queste LMW
[00:05:09] e di costruire il nostro company Brain,
[00:05:11] appunto per noi con il business. vi darò
[00:05:13] i prompt di tutto. Questa sarà la
[00:05:16] struttura che andremo ad utilizzare.
[00:05:18] Avremo la nostra company Brain per la
[00:05:20] quale vi darò un mini prompt ora. Avremo
[00:05:22] quindi poi il nostro cloud.md MD che
[00:05:24] rappresenta lo schema, quindi quello che
[00:05:26] vi dicevo prima, una delle tre cose che
[00:05:28] ci permette di capire come navigare
[00:05:30] questa company Brain. Avremmo una prima
[00:05:33] parte di fonti nel quale avremo un primo
[00:05:37] pezzo e quindi saranno le fonti di
[00:05:39] riferimento che utilizzeremo. avremo una
[00:05:41] cartella clienti e poi avremo la skill
[00:05:44] che andremo a fare in questo specifico
[00:05:47] video che è una proposal generation,
[00:05:49] quindi un'automazione dei preventivi e
[00:05:51] utilizzeremo un servizio che si chiama
[00:05:53] pandadoc. Qua dentro poi riusciremo a
[00:05:55] vedere che abbiamo anche i vari file che
[00:05:57] invece sono i le cose generate dall'AI e
[00:06:02] che quindi possono essere i log, quindi
[00:06:04] quello che abbiamo fatto o un index che
[00:06:06] ci racconta com'è fatta la company brain
[00:06:09] e che cosa c'è dentro e via dicendo. E
[00:06:11] l'offerta Dot MD invece sarà quella che
[00:06:13] verrà generata anche grazie a Pandado
[00:06:15] Doc prima di essere trasformata in PDF e
[00:06:17] mandata poi al nostro cliente. Qui
[00:06:20] avremo poi il cosiddetto ingest dal
[00:06:22] vivo, quindi effettivamente metteremo
[00:06:24] dentro un nostro transcript. Questo
[00:06:26] transcript verrà spezzato in queste
[00:06:29] micronote e una volta che sarà spezzato
[00:06:32] noi avremo la possibilità di entrare
[00:06:34] dentro Obsidian, vedere che la nostra
[00:06:36] company Brain comincia a popolarsi e
[00:06:39] l'AI aggiornerà in automatico sia il
[00:06:41] nostro index che il nostro log.
[00:06:43] Tradotto, a noi non serve per il momento
[00:06:45] sapere che cosa sono, sono tutte cose
[00:06:47] che vi darò e le AI le aggiornerà in
[00:06:49] maniera totalmente autonoma. Allora, ora
[00:06:51] per farvi vedere la differenza di che
[00:06:53] cosa vuol dire avere un sistema eh una
[00:06:55] skill all'interno di una company Brain o
[00:06:57] meno, voglio incollare in entrambe lo
[00:07:00] stesso tipologia di transcript e voglio
[00:07:04] farvi vedere qual è la differenza
[00:07:06] qualitativa sui due ehm script, ok? E
[00:07:11] sui due output. Ehi, per favore,
[00:07:13] generami una proposta per questo
[00:07:15] cliente.
[00:07:16] Vedete, qui non c'è niente. Lasciamo a
[00:07:19] Cloud la libertà assoluta di farlo e qui
[00:07:22] gli facciamo la stessa identica cosa. Vi
[00:07:25] faccio vedere a livello di output ora
[00:07:27] che cosa succede quando entrambi i
[00:07:28] sistemi finiscono. E questi sono i due
[00:07:30] risultati. Adesso fatemeli aprire
[00:07:32] velocemente. Il primo è un artifact di
[00:07:35] Cloud. Vedete? Eh, in questo caso sì,
[00:07:37] gente se non c'è il mio logo, non c'è
[00:07:40] niente, è una cosa abbastanza anonima,
[00:07:43] direi quasi AI slop. A questo punto,
[00:07:46] come potete ben vedere, abbiamo questo
[00:07:49] obiettivo, un sistema, quindi senza la
[00:07:52] nostra company Brain, lasciando e una
[00:07:54] skill, lasciando che il tutto sia
[00:07:56] generico, non ha nemmeno il nostro logo.
[00:07:58] Se noi poi invece tornassimo all'interno
[00:08:01] di questa e premessimo qua sotto, quindi
[00:08:05] dove trovarlo, mi aprirebbe Pandado e
[00:08:07] qui ovviamente adesso abbiamo una
[00:08:09] proposta totalmente diversa. Quindi,
[00:08:11] vedete, c'è il mio logo, insomma, di
[00:08:13] Gentes, un sistema di acquisizione per
[00:08:16] il mio cliente. Ehm, vedete qui che
[00:08:19] descrive brevemente la situazione del
[00:08:20] cliente, il sistema che andremo a
[00:08:22] costruire, che sarà appunto un lead
[00:08:24] enrichment, sarà la la call di
[00:08:26] transcript che vedrete dopo che vi darò.
[00:08:28] eh di modo tale che voi potete
[00:08:29] utilizzarla. Vedete che ha fatto le due
[00:08:31] opzioni con le modalità di pagamento che
[00:08:33] ci sono, con il tipo di pagamento, ma
[00:08:35] non solo, abbiamo anche la possibilità
[00:08:38] ora di mandarla in maniera automatica
[00:08:40] avere la firma e anche il pagamento che
[00:08:43] avvengono tramite Pandooc. Quindi
[00:08:46] riuscite bene a capire quale sia la
[00:08:47] differenza a livello qualitativo, sia da
[00:08:50] un punto di vista estetico che da un
[00:08:51] punto di vista funzionale. Cominciamo
[00:08:53] ora a costruire la nostra company Brain
[00:08:55] e qui avrete un notion, ve lo lascio
[00:08:58] sotto, con tutti i prompt che andremo ad
[00:08:59] utilizzare. Quindi la prima cosa che
[00:09:02] facciamo è dare questo prompt che fa
[00:09:04] esattamente quello che abbiamo appena
[00:09:05] descritto per la nostra company Brain.
[00:09:07] Quindi quello che faremo sarà andare a
[00:09:09] copiare questo prompt e poi dovremmo
[00:09:11] andare a scaricarci cloud code. Vedete
[00:09:14] voi dove volete farlo. Potete farlo in
[00:09:16] Antigravity, quindi qui mettete
[00:09:18] Antigravity IDE, potete farvelo dentro
[00:09:21] ad un cloud code, quindi nella desktop
[00:09:25] app. Per il momento lo farò qua dentro,
[00:09:27] ma non cambia assolutamente nulla. Qua
[00:09:30] dentro abbiamo una cartella vuota che
[00:09:32] noi apriremo e vedete qui che è
[00:09:34] completamente vuota. Come facciamo ad
[00:09:36] installarci Cloud Code qua dentro?
[00:09:38] Andiamo in extension e e premiamo Cloud.
[00:09:43] Eh, scusate, Cloud Code. Premeremo qui e
[00:09:46] premeremo installa. Una volta fatto,
[00:09:48] avrete questa rotellina qua in alto a
[00:09:50] destra e potrete arrivare qua dentro.
[00:09:53] Allora, che cosa facciamo? Andiamo qui e
[00:09:56] cominciamo a mettere il primo prompt.
[00:09:59] Questo è un prompt scritto ovviamente
[00:10:02] con una sintassi eh HTML e quello che
[00:10:06] farà questo nostro promptà andare a
[00:10:10] creare questa struttura della company
[00:10:12] brain, appunto, quindi con tutto quello
[00:10:14] che vi abbiamo descritto prima, con il
[00:10:16] cloudd che cosa deve contenere, un
[00:10:18] template, criteri di completamento. E io
[00:10:21] in questo caso gli dico "Ehi, ehm, per
[00:10:24] alcune informazioni che magari non
[00:10:26] conosci metti pure placeholder". Perché
[00:10:30] ehm in questo caso io sto facendo una
[00:10:33] demo per YouTube e puoi riempire le
[00:10:36] informazioni con qualcosa eh di demo. Il
[00:10:39] mio nome è Giovanni, la mia azienda si
[00:10:41] chiama Gente Sei. Il resto inventatelo
[00:10:44] pure e offriamo servizi anche di lead
[00:10:47] generation e faremo un esempio su
[00:10:49] questo. Perfetto. In questo caso voi
[00:10:51] avrete, come avete visto prima, una
[00:10:53] specie di questionario dove vi chiederà
[00:10:55] appunto chi siete, che fate, come
[00:10:57] andate. E in questo caso gli ho
[00:10:58] semplicemente detto "Per favore
[00:11:00] creameli" e poi popolami questa parte
[00:11:02] qui con informazioni demo di modo tale
[00:11:04] che io possa farvi vedere esattamente
[00:11:06] tutto poi la build come funziona. Nel
[00:11:08] mentre che il nostro prompt finisce vi
[00:11:11] spiego brevemente che tipologia di
[00:11:12] flusso andremo a fare. Allora, noi
[00:11:14] vogliamo creare questa company Brain e
[00:11:17] vogliamo che all'interno di questa
[00:11:18] company Brain ci sia una skill che in
[00:11:22] questo caso automatizza i preventivi
[00:11:24] perché ci viene molto più semplice
[00:11:26] farlo, no? Perché a quel punto noi non
[00:11:28] dovremmo continuare a fornire un sacco
[00:11:29] di informazioni sulla nostra azienda
[00:11:31] ogni volta in ogni prompt. Potremmo
[00:11:32] semplicemente dirgli fammi il preventivo
[00:11:34] per quel cliente, in automatico l'EI
[00:11:37] saprà esattamente che informazioni
[00:11:39] prendere e dove prenderle. Quindi a
[00:11:41] livello di business che tipologia di
[00:11:42] flusso abbiamo? Abbiamo innanzitutto una
[00:11:45] fonte. In questo caso noi avremmo una
[00:11:48] trascrizione di una call che entra
[00:11:50] dentro la nostra AI. Avete la
[00:11:52] trascrizione nel Notion, la copieremo,
[00:11:54] ma qui potete decidere, una volta che
[00:11:56] questo Workflow è fatto anche di
[00:11:57] collegarla al vostro eh note Taker come
[00:12:00] FOM o Firefly. Avremo poi il secondo
[00:12:03] step che sarà il cervello, quindi il
[00:12:06] flusso completamente lo disegna Cloud,
[00:12:09] trasforma eh la call che abbiamo fatto
[00:12:12] in varie note e andrà poi a decomporre i
[00:12:14] vari pezzettini fino a quando non capirà
[00:12:17] qual è l'offerta appunto MD che poi
[00:12:20] dovrà utilizzare dentro Pandadoc per il
[00:12:22] sistema. Pandadoc invece produrrà, e ora
[00:12:24] vi faccio vedere che cos'è, un documento
[00:12:26] firmabile, quindi qui Cloud scrive, qui
[00:12:29] avremo la possibilità di fare i sign e
[00:12:32] quindi di pagare e firmare direttamente
[00:12:35] dentro a questo documento che arriverà
[00:12:36] al nostro cliente e eh poi, appunto,
[00:12:40] nella memoria verrà registrato tutto
[00:12:41] come proposta. Nel caso in cui voi non
[00:12:44] lo conosceste, il servizio è questo, si
[00:12:46] chiama Pandadoc. Basta che facciate
[00:12:48] così, vi lascio un link sotto, avete 14
[00:12:51] giorni gratuiti se volete utilizzarlo.
[00:12:53] Questo è il sistema che andremo ad
[00:12:54] utilizzare e se vi interessa capire come
[00:12:57] ho fatto questa tipologia di template
[00:12:59] eccetera, ho fatto un corso abbastanza
[00:13:01] lungo nella parte di introduzione dopo
[00:13:04] il mio corso di 4 ore di cloud per AI e
[00:13:07] qui dentro avrete tutta la parte di come
[00:13:09] fare preventivi automatici e un
[00:13:11] walkthrough di Pandadoc. Appunto, qui ho
[00:13:14] fatto una trentina di minuti in cui ve
[00:13:15] lo spiego in dettaglio. In sostanza
[00:13:17] voglio farvi comunque vedere che cosa
[00:13:19] c'è dentro in questo video e [sbuffare]
[00:13:21] questo è un ottimo sistema perché questo
[00:13:23] è un template che io ho preparato con
[00:13:26] tanto di logo aziendale, proposta di
[00:13:29] collaborazione, servizi che offriamo e
[00:13:31] vedete che qua sotto e dopo che appunto
[00:13:34] questo, vedete è fatto con il mio brand
[00:13:37] setup e il m brand guidelines, vedremo
[00:13:40] che nella call avremo un qualcosa del
[00:13:43] genere, però tutto questo viene popolato
[00:13:45] in automatico con AI e qui abbiamo
[00:13:47] Abbiamo poi la possibilità di avere
[00:13:49] anche la firma digitale. Come vedete in
[00:13:51] questo caso la signer è Marco Rossi.
[00:13:55] Quando gli manderà manderemo il tutto
[00:13:58] Pandadoc in automatico utilizzerà questo
[00:14:01] per far firmare il documento. Qua
[00:14:03] potremmo mettere la data o avviene anche
[00:14:04] in maniera automatica. Quindi tutto
[00:14:06] questo servizio è un servizio che vi
[00:14:07] permette di generare proposte
[00:14:10] automatiche con AI, partendo da template
[00:14:14] del genere e utilizzando le cosiddette
[00:14:16] variabili dinamiche o text fields che
[00:14:19] per farvi vedere come funziona, basta
[00:14:21] che ne trasportate una all'interno qua
[00:14:24] dentro e poi qui potete cominciare a
[00:14:26] scrivere variabili custom o farle
[00:14:27] popolare all'AI. Ok? Quindi questo è
[00:14:29] solo per farvi vedere come funziona. Io
[00:14:31] per questo video ho già preparato il
[00:14:33] template e questo è esattamente quello
[00:14:35] che andremo ad utilizzare e quello che
[00:14:36] vorremmo automatizzare. Per farlo voi
[00:14:39] basta che andiate qua dentro e potete
[00:14:40] cominciare a giocare con le varie
[00:14:42] variabili. Perfetto, quindi in questo
[00:14:44] caso la nostra skill ha finito. Abbiamo
[00:14:46] detto struttura del brain carpati è
[00:14:48] stata fatta, che cosa c'è? vuoto, stato
[00:14:51] grezzo, skills, segnaposto per te, per
[00:14:54] offerta, fonti e via dicendo. Quindi
[00:14:57] adesso apriamo una nuova chat, abbiamo
[00:14:59] fatto tutto quello che volevamo e la
[00:15:01] nostra cartella è stata eh creata e la
[00:15:05] nostra company Brain può cominciare a
[00:15:08] prendere forma. Andiamo poi nel Notion e
[00:15:10] la prima cosa che dobbiamo fare è dirgli
[00:15:12] di generare una skill con Pandadoc. In
[00:15:17] questo caso andremo a copiare il prompt,
[00:15:19] andremo poi qui ad incollarlo e quello
[00:15:22] che gli diremo adesso è per favore
[00:15:25] utilizza eh il Panda Doc in questo URL e
[00:15:29] poi questo template. Allora, qui andremo
[00:15:31] ad incollargli il nostro URL.
[00:15:34] Perfetto. Ed andremo anche ad
[00:15:37] incollargli il nostro screenshot. Eccoci
[00:15:40] qui. Una cosa che manca è ovviamente
[00:15:43] avere le API key a cui potrete
[00:15:45] tranquillamente accedere.
[00:15:47] Quindi eh anche con la cosa gratuita,
[00:15:49] quindi account in basso a sinistra,
[00:15:52] avete poi qui API and integration. Se
[00:15:55] scrollate giù del tutto API and Webox,
[00:16:00] potrete fare open e qui avrete la
[00:16:02] possibilità di copiarvi le API key e poi
[00:16:04] incollarle dentro cloud. In questo caso
[00:16:06] l'ho appena fatto, copiate dentro al
[00:16:08] file.
[00:16:09] E la cosa che possiamo fare ora è dirgli
[00:16:11] bypass permission. Quello che andrà a
[00:16:14] fare ora è creare il nostro la nostra
[00:16:18] skill e poi potremo cominciare a
[00:16:20] provarla. Vi spiego come funziona questa
[00:16:22] integrazione. Quando noi andremo ad
[00:16:24] incollare il transcript che ora avremo
[00:16:28] nel nel nostro notion dentro cloud,
[00:16:32] quello che farà sarà il tutto viene
[00:16:34] spezzato in note, la skill di Pandadoc
[00:16:38] avrà tre strati, avrà un primo script.py
[00:16:40] PY e nel quale appunto crea legge la
[00:16:44] bozza e lo aspetta. Poi andrà a creare
[00:16:47] la proposta. Effettivamente è fatta con
[00:16:49] il nostro template e una volta fatto
[00:16:52] questo è il modo in cui andremo ad
[00:16:54] attivare la skill. Di nuovo, per chi di
[00:16:56] voi non lo sapesse, la skill non è altro
[00:16:57] che un modo di dire a cloud automatizza
[00:17:01] questo workflow perché gli step sono
[00:17:03] sempre quelli e quindi abbiamo
[00:17:05] automatizzato un un piccolo pezzo di
[00:17:07] processo. Perfetto, ora questo è andato
[00:17:10] con successo. Vedete che ha generato i
[00:17:12] miei script per la mia genera proposta e
[00:17:16] abbiamo ora la nostra skill.md con
[00:17:19] all'interno tutto quanto quello che
[00:17:21] serve per generare la proposta su
[00:17:24] Pandooc. Che cosa faremo ora? Andremo a
[00:17:27] prendere il transcript della nostra call
[00:17:29] all'interno del nostro pandadoc e
[00:17:31] vedremo se questo effettivamente
[00:17:33] funziona. Quindi copiamo. Questa è fatta
[00:17:36] una discovery call di Genti per Rossi
[00:17:38] Marketing e adesso andremo semplicemente
[00:17:41] a copiarla, incollarla e diremo qualcosa
[00:17:44] del genere.
[00:17:46] Ehi, ehm, questo è il transcript della
[00:17:49] mia call. Per favore, con la skill
[00:17:53] genera proposta, eh generami una
[00:17:56] proposta che posso mandare a eh il mio
[00:18:00] cliente. Ok, ci dice proposta fatta,
[00:18:03] riepilogo, documento trovato, quindi
[00:18:06] andiamo ad aprirlo. Ed ecco qua quello
[00:18:08] che otteniamo di nuovo con il nostro
[00:18:10] Mario Rossi. Ehm, qui abbiamo la data
[00:18:13] aggiornata, situazione con
[00:18:17] arricchimento, infrastruttura, copi,
[00:18:19] vediamo che il prezziario si è
[00:18:21] sostanzialmente mantenuto. E adesso
[00:18:24] abbiamo questa next step e poi abbiamo
[00:18:27] la firma. Vedete qui è un attimo
[00:18:29] modificata. Ed adesso per vedere che
[00:18:31] effettivamente questo sia quello che
[00:18:32] abbiamo discusso dentro la call, andiamo
[00:18:34] nel nostro cloud fonti. Qui dovremmo
[00:18:37] avere la nostra call messa già nelle
[00:18:40] nelle cose grezze e abbiamo che ci sono
[00:18:45] due modi di pagarlo, stesso identico
[00:18:46] sistema. Il primo è l'opzione standard,
[00:18:49] eh costo certo, setup €1000, una tantum
[00:18:52] che copre l'infrastruttura, estrazione
[00:18:54] leadify, enrichment clod, poi un
[00:18:57] retainer di €500 al mese e il secondo
[00:19:00] l'opzione performance setup ridotto a
[00:19:03] €600 e poi €80 per ogni meeting.
[00:19:07] Allora, qui abbiamo, come vedete, il
[00:19:08] setup una tantum e qui abbiamo retainer
[00:19:11] di 2e mesi, quindi 1000 più i 500 di 2
[00:19:13] mesi e dopo abbiamo invece il setup a
[00:19:15] performance con €80 a meeting. Quindi da
[00:19:17] qui vediamo che il tutto ha funzionato
[00:19:20] nella maniera corretta. Ora che abbiamo
[00:19:22] visto come ehm Ora che abbiamo visto
[00:19:25] come costruire queste offerte, guardiamo
[00:19:27] velocemente quello che molte persone
[00:19:29] sbagliano, ossia come possiamo
[00:19:31] apprezzarle. Allora, le due modalità di
[00:19:35] prezzo che noi abbiamo per cominciare ad
[00:19:37] osservare questa slide sono prezzare su
[00:19:41] quello che è il nostro costo che ci
[00:19:43] serve per produrla oppure prezzarla su
[00:19:47] quello che è il valore che questa
[00:19:49] tipologia di automazione, quindi la
[00:19:51] proposal automation all'interno di una
[00:19:53] company Brain, può generare. Premessa
[00:19:57] importante è questa tipologia audio
[00:19:59] automazione può arrivare ad avere un
[00:20:00] valore sostanzioso perché per esempio un
[00:20:03] one day training di 8 ore su AI può
[00:20:06] arrivare a costare 10-15.000.
[00:20:08] Un'automazione del genere può arrivare a
[00:20:10] costare anche €10.000. Sarà forse la
[00:20:12] prima che vendrete? Assolutamente no.
[00:20:14] Però ora voglio spiegarvi qual è il
[00:20:16] concetto che è teorico che vi permette
[00:20:19] poi di cominciare ad alzare il prezzo e
[00:20:21] adattare anche l'avatar alla vostra
[00:20:23] offerta. Se prezzate queste automazioni
[00:20:25] in base al costo, oggettivamente queste
[00:20:28] automazioni richiedono un costo
[00:20:30] abbastanza basso per farle, perché
[00:20:32] parliamo di un abbonamento molto
[00:20:35] probabilmente da 100 o $200 per cloud e
[00:20:38] poi un'automazione che eh possiamo fare
[00:20:42] con, se non mi sbaglio, $59
[00:20:45] per Panda Doc più un paio di altre cose.
[00:20:47] Quindi il costo è una strategia che vi
[00:20:50] farà perdere e vi farà sempre più
[00:20:52] schiacciare i margini. Se non riuscite a
[00:20:54] posizionare un'offerta di modo tale che
[00:20:56] spiegate al cliente qual è il valore che
[00:20:58] portate. Questa altra metodologia di
[00:21:01] prezzo è una una metodologia che si
[00:21:04] chiama value based pricing e quindi è in
[00:21:08] base al valore che andrete a generare
[00:21:09] per un'azienda. Come facciamo a
[00:21:11] calcolare questo valore? Allora, il
[00:21:13] valore si può vedere come tempo che in
[00:21:17] questo caso l'azienda sta salvando per
[00:21:20] andare a automatizzare il loro processo
[00:21:23] di proposal generation e quindi in
[00:21:25] questo caso è il tempo che una persona
[00:21:30] eh impiega per fare una proposta, quindi
[00:21:33] tempo persona proposta possiamo mettere
[00:21:36] moltiplicato per il numero di eh
[00:21:41] proposte
[00:21:43] al mese. Questo è una proxy. Se volete
[00:21:46] andare nel dettaglio di come farei
[00:21:47] questo preziario, potete andare nella
[00:21:49] mia community, abbiamo un corso
[00:21:50] specifico su come prezzare le offerte e
[00:21:53] come rivenderle, [sbuffare] però questo
[00:21:56] è un primo. Poi il secondo metodo
[00:21:59] aggiuntivo, quindi non è un o, ma è un
[00:22:01] e, è la parte di arroi, ossia
[00:22:06] ipotizziamo che questa persona stia
[00:22:08] salvando un totale di magari un 10 ore
[00:22:13] al mese per fare queste proposte.
[00:22:17] Quanto si traduce questo in valore per
[00:22:20] l'azienda? Quindi questa questa persona
[00:22:24] se facesse queste 10 ore e in queste 10
[00:22:27] ore prendesse magari due clienti, quanto
[00:22:31] questo upside potrebbe portare in
[00:22:34] termini di fatturato? E quindi questo vi
[00:22:36] esce, ma facciamo numeri a casissimo,
[00:22:38] eh, però ipotizziamo che un cliente
[00:22:40] medio per voi sia i 2500, quindi magari
[00:22:43] due clienti e quindi 10 ore vi valgono
[00:22:45] per voi €5000. Questi ovviamente sono al
[00:22:47] mese e quindi vedete come già adesso
[00:22:51] semplicemente facendo vedere quello che
[00:22:54] ehm e qui ovviamente dovremmo
[00:22:56] moltiplicarlo per il valore del tempo
[00:22:58] all'ora per cui paghiamo la persona,
[00:23:01] vedete che già qui abbiamo che questa
[00:23:03] automazione con qualche semplice conto,
[00:23:06] ovviamente molto molto semplificato, ma
[00:23:09] già qui è abbastanza semplice cominciare
[00:23:12] a apprezzare questa automazione con
[00:23:14] €6000 al mese. Ovviamente dovete avere
[00:23:16] un business che ne ha bisogno, dovete
[00:23:17] avere un mercato che ve lo permette,
[00:23:19] dovete avere un avatar che è disposto a
[00:23:20] pagare, quindi [sbuffare] dovete essere
[00:23:22] bravi perché ovviamente c'è modo e modo
[00:23:25] di fare queste tipologie di automazioni
[00:23:26] e poi per scalarle non è poi così
[00:23:29] semplice come farle one shot, però
[00:23:32] vedete che questo è il metodo e quindi
[00:23:34] qui stiamo andando a quanti giorni
[00:23:37] effettivamente salvi rispetto a quanto
[00:23:39] tempo ti ci metterà il sistema per
[00:23:41] generarti tutte le proposte che vuoi. E
[00:23:44] quindi qui vedete che questi sono prezzi
[00:23:47] che potete considerare entry level,
[00:23:49] quindi potete cominciare ad offrire
[00:23:51] questa automazione dopo ovviamente
[00:23:52] averne fatte un po', tra i 1000 e i
[00:23:54] €5000 e poi potete avere un retainer se
[00:23:58] l'azienda ha bisogno che questa
[00:23:59] automazione venga ehm mantenuta.
[00:24:03] esempio, potrebbe essere per persone che
[00:24:05] hanno preventivi molto grossi, magari
[00:24:07] aziende che vendono macchinari pesanti,
[00:24:09] dove hanno allora che magari vendono in
[00:24:12] un mercato inglese, vendono nel mercato
[00:24:14] italiano, vengono nel mercato francese,
[00:24:16] tedesco e quindi queste automazioni
[00:24:19] cominciano a avere lingue diverse, ma
[00:24:21] soprattutto magari a seconda del tipo di
[00:24:23] macchinario devono prendere forme
[00:24:25] diverse. Capite bene che qua ovviamente
[00:24:27] servirà un retainer. Mi raccomando, eh
[00:24:29] l'ultimo eh cosa che ci tengo a
[00:24:31] sottolineare un'altra volta è: prezzate
[00:24:34] in base al valore e non in base alle ore
[00:24:35] che ci mettete a sviluppare perché
[00:24:37] altrimenti i vostri margini andranno giù
[00:24:39] e nessuna azienda di successo prezza mai
[00:24:42] al costo. E quindi eccolo, un agente che
[00:24:45] se implementato nel modo corretto le
[00:24:47] aziende sono disposte a pagare fino a
[00:24:49] migliaia di euro. Costruirlo come MVP,
[00:24:51] come in questo caso è semplice. Se
[00:24:53] volete andare più a fondo e volete avere
[00:24:55] un corso comprensivo di come costruire
[00:24:57] queste cose con Cloud Code, entrate in
[00:24:59] community e troverete tutto lì.
