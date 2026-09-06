
[00:00:00] Ho costruito un bot che fa trading di
[00:00:02] Bitcoin con Cloudcode ed in questo video
[00:00:03] lo andremo a ricostruire insieme. Però
[00:00:06] questo video non è un video su come si
[00:00:08] diventa ricchi facendo trading di
[00:00:10] Bitcoin, non sarei qui, eh, però è
[00:00:13] piuttosto un video su come possiamo
[00:00:16] utilizzare l'AI per affrontare qualsiasi
[00:00:19] problema concreto. Quindi andremo a
[00:00:20] vedere qual è un framework che possiamo
[00:00:23] utilizzare per affrontare questo
[00:00:24] problema e come possiamo farci guidare
[00:00:26] da questi strumenti nel caso in cui noi
[00:00:29] non siamo degli esperti nel settore.
[00:00:31] Questo video si dividerà in tre parti
[00:00:33] principali. Andremo inizialmente a
[00:00:36] comprendere il problema che dobbiamo
[00:00:38] analizzare, quindi che cosa vuol dire
[00:00:40] fare un trading bot di Bitcoin, cioè
[00:00:43] quali sono i problemi che andiamo a
[00:00:46] risolvere, quali sono le parti
[00:00:47] costitutive. Andremo poi a definire come
[00:00:50] facciamo un design del sistema ed alla
[00:00:53] fine procederemo all'implementazione. E
[00:00:55] se per caso siete nuovi al canale, sono
[00:00:57] Jo, ho una mia azienda di intelligenza
[00:00:58] artificiale con la quale facciamo
[00:01:00] consulenza business che vanno dai
[00:01:01] €10.000 al mese fino ai 50 milioni di
[00:01:04] euro all'anno ed ho una community
[00:01:06] privata nella quale insegno a freelancer
[00:01:08] ed imprenditori come applicare l'AI in
[00:01:10] qualsiasi business e come vendere questi
[00:01:12] servizi. Detto questo, cominciamo.
[00:01:14] Partiamo innanzitutto dalla comprensione
[00:01:17] del problema. Allora, che cosa vuol dire
[00:01:19] avere un bot che fa trading di Bitcoin?
[00:01:23] Significa che innanzitutto dovremmo
[00:01:25] avere un layer di fondamenta. Nel nostro
[00:01:28] caso useremo Binance. Non ho alcuna
[00:01:30] associazione, non c'è uno sponsored
[00:01:31] link, faccio il video solo perché
[00:01:33] qualcuno di voi me l'ha chiesto. E
[00:01:35] quindi dovremmo avere una piattaforma
[00:01:38] tramite la quale noi andremmo a fare
[00:01:41] trading di queste cose e dopo dovremmo
[00:01:44] avere una connessione API a questa
[00:01:46] piattaforma. Questo è importante perché
[00:01:48] non la la piattaforma di per sé sì è il
[00:01:51] layer principale, ma se non possiamo
[00:01:53] connetterci con API e quindi con queste
[00:01:55] chiavi che permettono a Cloud di
[00:01:57] accedere a o a Codex di accedere in
[00:02:00] maniera automatica, noi non possiamo
[00:02:03] fare questa cosa qui. Quindi questo qui
[00:02:05] sarà lo step uno che sarà il
[00:02:08] prerequisito ci servirà per poter poi
[00:02:10] procedere alla formulazione del resto
[00:02:12] del sistema. Sempre rimanendo ad alto
[00:02:13] livello perché non siamo ancora nella
[00:02:15] fase architetturale, capiamo che il
[00:02:18] nostro bot deve avere delle
[00:02:21] caratteristiche e di nuovo sono
[00:02:23] caratteristiche ad alto livello. Deve
[00:02:25] saper leggere i dati. Quindi, siccome
[00:02:28] noi stiamo facendo trading giornaliero,
[00:02:31] che cosa vuol dire? Vuol dire che il
[00:02:33] nostro bot avrà la possibilità di vedere
[00:02:36] le cosiddette candele, ok? Quindi quando
[00:02:39] il valore in borsa, diciamo, di queste
[00:02:43] asset va su e giù e quindi dovrà
[00:02:46] raccogliere le cosiddette candele in
[00:02:47] tempo reale. Sostanzialmente l'analisi
[00:02:49] dei dati. Il secondo è che dovrà esserci
[00:02:53] una decisione e gestione del rischio.
[00:02:56] Che cosa vuol dire questa cosa qui? Vuol
[00:02:59] dire che ci serve in sostanza una
[00:03:01] logica, ok? Non abbiamo ancora definito
[00:03:04] che tipologia di logica stiamo andando
[00:03:07] ad utilizzare qua dentro, ma
[00:03:08] sostanzialmente questo vuol dire che
[00:03:10] dobbiamo dare al nostro bot un cervello.
[00:03:14] Perché dire a Claud e per favore vai e
[00:03:17] conquista il mondo non è sufficiente per
[00:03:20] Claud
[00:03:22] conquistare questo mondo, cioè con il
[00:03:24] carro armato, con le spade o con le
[00:03:26] pistole d'acqua. Quindi dobbiamo
[00:03:29] definire quella che è la strategia e ci
[00:03:31] tengo a specificare che questo sarà il
[00:03:35] core della vostra proprietà
[00:03:37] intellettuale. Che cosa vuol dire? Vuol
[00:03:39] dire che tutti dopo questo video
[00:03:41] realisticamente sapranno fare un bot con
[00:03:44] Cloud Code. Non tanti sapranno qual è la
[00:03:47] miglior strategia per fare trading,
[00:03:50] quindi la gran parte della vostra
[00:03:52] ricerca dovrebbe essere nel decidere
[00:03:54] qual è la strategia migliore prima
[00:03:57] ancora di capire come costruire il
[00:03:59] sistema. Ok? E questo vale sempre per
[00:04:02] qualsiasi tipologia di sistema.
[00:04:05] Poi ovviamente dovremmo avere la
[00:04:06] possibilità di fare, quindi dovremmo
[00:04:09] piazzare gli ordini per capirci. Per
[00:04:11] quanto riguarda poi il layer 1 è il
[00:04:13] layer di monitoraggo. E perché vi ho
[00:04:15] fatto una scala, diciamo, di importanza
[00:04:18] in questo modo? Beh, perché quando
[00:04:21] affrontate qualsiasi tipo di problema,
[00:04:24] quello che dovete fare è sempre
[00:04:26] procedere in questa direzione, cioè
[00:04:28] andare a pensare a come faccio
[00:04:31] monitoraggio alert prima ancora di aver
[00:04:33] capito se il sistema può essere
[00:04:35] costruito e quindi se c'è una chess API
[00:04:37] o quale sia la logica con cui andremo a
[00:04:40] costruire questo sistema non è la cosa
[00:04:43] corretta. Ok? Quindi partiamo sempre da
[00:04:45] possiamo farlo, dopo andiamo al ok, cosa
[00:04:48] facciamo e dopo è come lo monitoriamo.
[00:04:50] Ora però noi potremmo chiederci una
[00:04:52] cosa, voi potreste dirmi: "Hey Jo, però
[00:04:53] non è sempre chiaro qual è il problema
[00:04:55] che sto affrontando, non ho sempre
[00:04:57] chiaro quali sono i building blocks e
[00:04:59] non ho sempre chiaro come farlo." Bene,
[00:05:00] per risolvere questo problema vi
[00:05:02] consiglio sempre di utilizzare uno
[00:05:03] strumento come cloud. Ora vi faccio
[00:05:05] vedere un paio di skill che io ho
[00:05:07] costruito per i membri della mia
[00:05:08] community, però vorrei darvi il
[00:05:10] framework di modo tale che voi possiate
[00:05:12] ricostruire qualsiasi skill nello stesso
[00:05:15] identico modo. Allora, come vedete io
[00:05:17] qui a prompt a parte ho detto che cosa?
[00:05:21] Ehi, sto cercando di costruire un
[00:05:24] trading bot per un video di YouTube.
[00:05:26] Dovrebbe analizzare Bitcoin, le candele
[00:05:29] di Bitcoin e capire qual è la miglior
[00:05:32] strategia. Eh, vorrei disegnare un
[00:05:34] diagramma che mi permetta di mostrare le
[00:05:37] varie skill. Eh, e il target di questo
[00:05:41] diagramma è non technical people, quindi
[00:05:44] persone che non sanno di cose tecniche,
[00:05:47] quindi entrepreneurs e quindi
[00:05:48] imprenditori, scusate, e altri che non
[00:05:51] capiscono molto riguardo alla finanza.
[00:05:54] Eh, e tra questi, tra l'altro, ci sono
[00:05:56] io. Io non sono un esperto di finanza,
[00:05:58] no? Quindi il target con cui lo dico è
[00:06:00] perché devo dare al bot un diciamo un
[00:06:04] riferimento su ok, se faccio questo ti
[00:06:07] mostro una mega cosa con tutte le le
[00:06:10] diciamo KPI finanziari eccetera o stiamo
[00:06:13] cercando di stare ad alto livello e
[00:06:15] costruire un sistema. E quindi con
[00:06:18] questo gli ho detto ehm ti darò un
[00:06:22] esempio perché tu possa andare nella
[00:06:25] direzione corretta. Eh, se ti dico ehm
[00:06:28] tu di costruire un Trading bot, eh tu
[00:06:31] dovresti includere più parti, come per
[00:06:33] esempio le connessioni IPI, una
[00:06:35] piattaforma, la strategia bot strategy
[00:06:38] ander
[00:06:42] e il layer, chiamiamolo 2, sono stati
[00:06:44] rispettati. Poi il bot ha potuto
[00:06:48] generarmi questa immagine di modo tale
[00:06:50] che lui ha potuto darmi anche, come
[00:06:53] vedete voi, un'interpretazione, ma
[00:06:55] vedete che questo può essere fatto. Ehm,
[00:06:58] come potete farlo? Beh, semplicemente
[00:07:00] questa è una skill nella quale io ho
[00:07:03] detto al bot, "Hei, quando ti do un
[00:07:05] richiesta per farmi un diagramma", stai
[00:07:08] ad alto livello, cerca di decomporre il
[00:07:10] task in micro sezioni e dopo
[00:07:14] disegnamelo. Questo è quello che c'è
[00:07:15] dentro la mia skill e potete
[00:07:17] semplicemente replicarla anche voi. Fate
[00:07:20] poi la le immagini con quello che
[00:07:23] preferite. Avete 1000 opportunità, avete
[00:07:26] Miro, avete un'immagine con, non lo so,
[00:07:30] Gemini, avete Flowchart, avete mille e
[00:07:33] mille cose e ora ve ne farò vedere anche
[00:07:35] un'altra. Quindi questo è il primo modo
[00:07:38] e tra l'altro io faccio anche sessioni
[00:07:40] di brainstorming, magari prima di
[00:07:41] capirlo. Quindi questo è come noi
[00:07:43] andiamo ad affrontare il problema. La
[00:07:45] parte numero due è fare il design del
[00:07:49] sistema. Allora, da dove si parte però
[00:07:51] per fare il design del sistema? Si parte
[00:07:54] dal blocco che io considero il blocco
[00:07:56] core. Quindi, partiamo sempre da la
[00:08:00] nostra strategia. E come possiamo andare
[00:08:03] allora a fare la strategia? Beh, io
[00:08:05] l'avevo già fatta. Vi faccio vedere
[00:08:07] brevemente il prompt, poi vi dico che
[00:08:08] cosa è successo e poi questa è la
[00:08:09] strategia. Io non me ne intendo di
[00:08:12] trading, quindi partiamo da quel
[00:08:14] concetto lì. E quindi quello che abbiamo
[00:08:16] detto è sto costruendo un bot su Cloud
[00:08:19] Code che dovrebbe fare trading di
[00:08:21] Bitcoin su base giornaliera. Ehm quello
[00:08:25] che vorrei è un bot che guarda le
[00:08:29] candele nell'app di Binance. Ho bisogno
[00:08:31] del tuo aiuto con cose seguenti. Allora,
[00:08:35] la prima cosa è che devi avere una
[00:08:37] strategia che io posso utilizzare per
[00:08:40] creare questo bot con successo. Per
[00:08:43] favore, abbi contezza che questa è una
[00:08:46] demo e quindi voglio fare la run nella
[00:08:50] sandbox con soldi finti perché Binance
[00:08:53] dà l'opportunità, però è importante non
[00:08:55] cambia nulla dal metterlo al vero al no
[00:08:58] e e quindi ehm vedrete qui. Quindi no
[00:09:01] harm o financial advice verranno dati in
[00:09:04] questo video, però voglio che il bot sia
[00:09:07] completamente funzionante e non biased,
[00:09:09] quindi non con un'architettura più
[00:09:11] semplice o che non funziona solo perché
[00:09:13] è una demo. Qual è il motivo? Che io non
[00:09:16] posso su YouTube fare una cosa del
[00:09:17] genere e [risate] quindi devo farla per
[00:09:19] forza come demo e dire che queste non
[00:09:22] sono financial advices. Allora, detto
[00:09:26] questo,
[00:09:27] che cosa andiamo a fare? Allora, noi
[00:09:30] andiamo ad utilizzare quello che io
[00:09:31] chiamo agent polling. È semplicemente
[00:09:33] una mia skill e vi dico come potete
[00:09:35] farla adesso, nella quale dentro la
[00:09:37] skill ho detto quando ti do un qualsiasi
[00:09:41] task, per favore crea X agenti ognuno
[00:09:46] dei quali ha un punto di vista diverso.
[00:09:48] Ok? Questo è quello che c'è dentro la
[00:09:49] skill. E quindi, come vedete qui abbiamo
[00:09:52] che il primo agente fa i ricerca i trend
[00:09:55] following, l'altro mi fa eh la media più
[00:10:00] momentum strategies, qualsiasi cosa
[00:10:02] questo voglio dire. L'altra mi fa
[00:10:04] research advanced più strategie composte
[00:10:07] e quindi poi vediamo che questi agenti
[00:10:09] vanno tutti in autonomia, no? e vediamo
[00:10:13] come funzionano questi agenti.
[00:10:14] Ovviamente, dato che la mia skill fa
[00:10:16] questo, saranno 10 diversi per ogni
[00:10:19] tipologia di tas che io gli do. Se gli
[00:10:21] dicevo fammi le 10 ehm agenti che
[00:10:24] trovano, non so, la miglior ricetta
[00:10:26] sulla pasta, avrebbero fatto eh diciamo
[00:10:29] qualcosa di diverso. E questa è la
[00:10:31] strategia che viene utilizzata. Ok?
[00:10:35] Questo perché? Perché voglio tornare qui
[00:10:36] e voglio dirvi che gran parte,
[00:10:38] ovviamente non mi sono soffermato perché
[00:10:41] questo di nuovo non è financial advice,
[00:10:43] ma è come dovreste approcciare un un
[00:10:45] qualsiasi problema, perché ho
[00:10:47] identificato immediatamente che il core
[00:10:48] del problema è questo, cioè la
[00:10:52] probabilità di successo o meno del mio
[00:10:54] bot dipende da questa gestione del
[00:10:56] rischio. Quindi la probabilità che voi
[00:10:58] facciate un sistema che fa marketing
[00:11:01] campaign corrette è magari basato su
[00:11:05] quanto bene il vostro sistema identifica
[00:11:07] gli outlier e quindi gran parte del
[00:11:09] vostro sistema o del vostro development
[00:11:12] dovrebbe andare in questa direzione.
[00:11:14] oppure facciamo email copy per email
[00:11:18] marketing, gran parte della
[00:11:21] del successo del vostro sistema dipende
[00:11:23] da quanto buona è la copia e quindi
[00:11:25] dovreste andare dentro a questa
[00:11:27] tipologia di sistema. Ipotizziamo che
[00:11:29] andiamo a fare una proposal generation,
[00:11:31] quindi che mandiamo proposte automatiche
[00:11:33] ai nostri clienti. Gran parte del
[00:11:35] successo del sistema viene da quanto
[00:11:37] bene analizziamo i transcript e da
[00:11:38] quanto questi possono essere convertiti
[00:11:41] in pain per il nostro cliente, da quanto
[00:11:43] il nostro template converte. Quindi gran
[00:11:45] parte del focus dovrebbe essere messo
[00:11:47] qui. Quindi vediamo che ogni problema ha
[00:11:50] sempre questo layer che noi qui
[00:11:52] chiamiamo strategia nel quale dobbiamo
[00:11:54] concentrarci.
[00:11:56] Allora, una volta definita questa,
[00:11:58] quello che faccio è questa cosa ad alto
[00:12:02] livello, quindi la copio, mettiamo in
[00:12:05] bypass permission e gli diciamo qualcosa
[00:12:07] del genere. Ehi, sto costruendo un Botsu
[00:12:09] Finance che fa trading di Bitcoin su
[00:12:12] base giornaliera. Ora, vorrei darti due
[00:12:15] cose in input. Una è la strategia che ho
[00:12:19] fatto separatamente e ora ti incollo, e
[00:12:21] l'altra è l'architettura ad alto
[00:12:23] livello. Vorrei che tu ora mi disegnassi
[00:12:27] un flowchart
[00:12:30] io possa ehm visualizzare l'architettura
[00:12:33] di sistema. Eh per utilizzare il
[00:12:36] flowchart puoi pure utilizzare la mia
[00:12:38] skill di Excalidro.
[00:12:41] Allora, ora vi spiego anche che cosa fa
[00:12:42] la skill e poi lo vedremo. Allora,
[00:12:45] strategia
[00:12:47] strategia e qui la incolleremo
[00:12:50] e poi mettiamo e e questa è una cosa che
[00:12:54] faremo così ad alto livello quello che
[00:12:57] noi vogliamo dentro al nostro sistema.
[00:13:00] Ok? Quindi ora quello che stiamo facendo
[00:13:02] è cominciare a dare contesto di quello
[00:13:05] che facciamo al sistema. per favore
[00:13:09] assicurati che sia chiaro dove inizia e
[00:13:11] dove finisce il workflow, di modo tale
[00:13:12] che io possa visualizzarlo.
[00:13:15] Ora,
[00:13:16] che cosa fa eh la mia skill Excalidro?
[00:13:21] Di nuovo, potete farla come volete.
[00:13:23] Questa è semplicemente un mental model
[00:13:26] mio per affrontare questi sistemi e il
[00:13:29] motivo è che a me piace vedere in
[00:13:32] maniera visiva le architetture solo
[00:13:34] perché mi permette più o meno di capire
[00:13:37] se tutti i pezzi vanno dove devono
[00:13:41] oppure se c'è qualcosa di, chiamiamolo
[00:13:44] drasticamente sbagliato. Vi faccio un
[00:13:46] esempio. Se io dicessi: "Ehi, fammi una
[00:13:50] ricerca degli outlier per il mio canale
[00:13:53] YouTube e vedo che però
[00:13:55] nell'architettura il sistema o o meglio
[00:13:58] in questa architettura ipotetica non va
[00:14:00] a prendere gli Outlier dal New Excel, ma
[00:14:02] va a prenderli magari da qualche altra
[00:14:04] parte, beh, questo sicuramente non è
[00:14:07] quello che voglio."
[00:14:08] Quindi quello che dobbiamo fare è
[00:14:10] visualizzare questa architettura ora con
[00:14:12] i vari pezzi dell'AI, quindi con i vari
[00:14:14] pezzettini dentro che ci permette di
[00:14:16] capire ok come faccio. Allora, andiamo,
[00:14:21] ci dice che è dentro la mia cartella
[00:14:22] temporaneo ehm e dentro al Daily di
[00:14:26] Excalidro. Eccolo qui,
[00:14:28] dailyotexcalidro.com.
[00:14:31] Quindi copierò questo e adesso andrò qui
[00:14:34] nel mio design di sistema e lo
[00:14:36] incollerò. Allora, dove comincia? Dal
[00:14:38] verde, andiamo a vedere che cosa
[00:14:39] succede.
[00:14:41] Perfetto, mi dice questa è la nostra
[00:14:45] partenza, quindi aspettiamo una candela.
[00:14:47] Cosa facciamo? andiamo a prendere dentro
[00:14:50] a ehm i dati dentro al nostro Binance,
[00:14:55] quindi troviamo le candele, poi andiamo
[00:14:58] tutto su e cominciamo a calcolare i
[00:15:01] nostri indicatori. Di nuovo, noi non
[00:15:03] sappiamo niente a questo punto di
[00:15:04] indicatori, però ipotizziamo che la
[00:15:06] nostra strategia l'abbiamo raffinata,
[00:15:08] abbiamo contattato gli esperti, abbiamo
[00:15:10] capito qual è la migliore, quindi noi
[00:15:12] ora possiamo fare il nostro bot. Piccola
[00:15:14] interruzione, solo per dirti che se sei
[00:15:16] un imprenditore che vuole applicare l'AI
[00:15:18] nel proprio business o sei una persona
[00:15:20] che vuole cominciare a vendere servizi
[00:15:22] AI alle aziende, ho lasciato il primo
[00:15:24] link qua sotto che è la mia community
[00:15:26] privata in cui vi aiuto in prima
[00:15:27] persona. Detto questo, torniamo al
[00:15:29] video. Allora, una volta che abbiamo
[00:15:30] calcolato i nostri indicatori,
[00:15:33] abbiamo il cosiddetta la parte di
[00:15:36] collezione di questi indicatori, quindi
[00:15:37] la logica aggregherà tutto in qualche
[00:15:39] modo. E ora ci chiediamo se questo è
[00:15:43] sopra a 25, che sarà molto probabilmente
[00:15:46] il nostro eh livello di thold sopra il
[00:15:50] quale magari compriamo o sotto vendiamo.
[00:15:53] Ok? Quindi questo vediamolo come abbiamo
[00:15:56] fatto questo threshold e poi quindi qui
[00:15:58] cominciamo a vedere il routing. Ok?
[00:16:00] Quindi bullish sì. Eh allora apri una
[00:16:04] posizione di long eh e oppure beish,
[00:16:07] quindi no. E allora magari vuol dire
[00:16:10] hold, quindi non prendere niente. Io
[00:16:12] vedete perché uso Excalidro, perché
[00:16:14] questo mi permette anche di modificare,
[00:16:16] quindi nel senso se dovessi dire ad un
[00:16:18] cliente "Ehi ehm ti faccio un disegno al
[00:16:21] volo" eccetera, vedete che comunque
[00:16:22] questi sono comunque disegni che
[00:16:25] rimangono qualitativamente importanti e
[00:16:28] sembra che, insomma, voi abbiate speso
[00:16:30] una grande quantitativo di tempo per
[00:16:32] fare queste cose manualmente. Allora,
[00:16:34] vedete quindi che questa è la fase di
[00:16:36] validazione dell'architettura e questo è
[00:16:38] quello che vogliamo fare, no? Perché noi
[00:16:40] vogliamo assicurarci che la nostra
[00:16:42] architettura sia corretta. Quindi questo
[00:16:45] è la maniera visiva in cui possiamo
[00:16:47] vedere l'architettura. Bene, ora una
[00:16:50] volta fatto questo, possiamo quindi
[00:16:53] andare dentro al nostro sistema e ora
[00:16:56] possiamo pianificarlo. Perfetto.
[00:16:57] Sintetizzami tutto in un prompt e
[00:17:00] includi anche tutta la strategia che ti
[00:17:02] ho incollato di modo tale che io possa
[00:17:04] andare ora in una nuova sessione di
[00:17:06] cloud code e incollargliela in plan mode
[00:17:09] ed assicurarmi che cloud poi vada a eh
[00:17:12] implementare il mio sistema. Perfetto.
[00:17:15] Quindi quello che faremo ora è aspettare
[00:17:17] insomma che questo finisca. Ottimo.
[00:17:19] Sembra che abbia finito, quindi ora
[00:17:21] prendiamo,
[00:17:23] incolliamo
[00:17:25] e gli diamo questo. E ora possiamo eh
[00:17:29] semplicemente Oh, prompt contract
[00:17:31] suggested. Non c'è niente qua sotto. Ah,
[00:17:34] vedi che non me l'ha copiato bene.
[00:17:37] Ok.
[00:17:38] e poi incolliamo
[00:17:41] bypass permission e potremmo partire.
[00:17:43] Prima di farlo però, ovviamente, che
[00:17:45] cosa vogliamo fare? Senza impazzirci,
[00:17:48] ehm, e per questo lo rimettiamo in in
[00:17:51] plan mode, mettiamo credenziali
[00:17:55] Binance. Adesso infatti che cosa
[00:17:57] dobbiamo farlo?
[00:17:59] API link per vedere candele. Mancano due
[00:18:04] cose importanti e mancano le due cose
[00:18:05] importanti dell'inizio. Quindi come
[00:18:08] facciamo ad autenticarci nella
[00:18:10] piattaforma Binance e quindi da qui poi
[00:18:14] vedremo come come si fa e dove andiamo a
[00:18:17] prendere i dati delle candele. Bene,
[00:18:19] abbiamo che se io andassi a premere
[00:18:20] Binance Login avrei
[00:18:24] questo. Non so. Adesso vediamo se
[00:18:28] possiamo farlo senza verificarci.
[00:18:32] Ah, API management sotto la sezione
[00:18:34] account e qui abbiamo create API system
[00:18:39] generated e quindi label API
[00:18:43] YouTube bot. Security verification
[00:18:46] requirements. You need to complete. Ok,
[00:18:50] va bene. Ora mi autenticherò. Perfetto.
[00:18:54] Dopo 6 anni, 4 mesi e due lune abbiamo
[00:18:58] questo. Quindi abbiamo API key. Adesso
[00:19:02] gli metteremo
[00:19:04] secret key. Perfetto, quindi ora le
[00:19:08] abbiamo inserite all'interno e ci manca
[00:19:12] che cosa? ci manca il link per vedere le
[00:19:14] candele. Allora, per fare questo potete
[00:19:16] o chiedere a Cloud di andare e ed
[00:19:18] esplorare l'universo, oppure potete
[00:19:20] andare in questo link qui ehm che è la
[00:19:23] parte di developerinance.com
[00:19:26] e qui avrete la possibilità di esplorare
[00:19:28] candele. Come l'ho trovata? Ovviamente
[00:19:31] l'ho trovata utilizzando Cloud e
[00:19:32] chiedendogli "Ehi ehm dove potrei andare
[00:19:35] a cercarle?"
[00:19:36] per favore, eh ricordati che eh questa
[00:19:40] eh questo bot vorrei farlo funzionare
[00:19:43] nel utilizzando soldi falsi e quindi in
[00:19:49] sandbox. Ora dovremmo esserci e quindi
[00:19:53] la cosa che possiamo fare è ora premere
[00:19:55] plan mode e aspettare che tutto questo
[00:19:58] venga implementato. Ehm, detto questo,
[00:20:00] io ora aspetterò che il tutto venga
[00:20:04] implementato e poi vi faccio vedere eh
[00:20:07] come funziona. Perfetto, ora ha
[00:20:09] funzionato e questo è il bot che mi ha
[00:20:11] creato. Però ora gli ho chiesto un altro
[00:20:13] paio di cose e gli ho chiesto di mettere
[00:20:16] il bot perché fino ad ora che cosa
[00:20:19] abbiamo fatto? Abbiamo semplicemente
[00:20:21] creato la nostra infrastruttura e quindi
[00:20:23] questo vuol dire che siamo alla parte di
[00:20:25] implementazione. Però una volta finita
[00:20:27] l'implementazione e quindi il nostro bot
[00:20:29] che sia stato creato, abbiamo la parte
[00:20:32] di go live. Allora, per farlo e ora vi
[00:20:35] mostro il prompt che ho utilizzato, è
[00:20:39] ok, che cosa vuol dire mettere il bot,
[00:20:42] che dovrei vedere le trades nel mio
[00:20:44] Binance account, che dovrei avere
[00:20:46] deployed it already, ehm avrei dovuto
[00:20:48] fare un sacco di cose, no? Quindi devo
[00:20:50] vedere il bot che effettivamente faccia
[00:20:53] trading. Questo perché vogliamo fare un
[00:20:55] qualcosa che sia eh finalizzato, no?
[00:20:58] Quindi un readymade product che voi
[00:21:00] potete poi utilizzare nel caso in cui
[00:21:02] vogliate uscire dalla sandbox. E qui gli
[00:21:04] ho messo eh sempre ovviamente con soldi
[00:21:06] finti. Quindi quello che sta facendo ora
[00:21:08] è arrivare qua e volevo fare questo
[00:21:10] passaggio con voi e quindi ho ho premuto
[00:21:12] questo qua. Avevo il mio login con
[00:21:15] GitHub, è proprio sotto a queste API qui
[00:21:19] che abbiamo utilizzato. Una volta preso
[00:21:21] facciamo generate questo
[00:21:25] e quindi qui faremo la generate. Quello
[00:21:28] che ci metteremo è copied new API and
[00:21:31] secret key. Quindi qui avremo la nostra
[00:21:34] API key e la nostra secret key. una
[00:21:36] volta che l'abbiamo generata, quindi
[00:21:39] YouTube
[00:21:41] bot
[00:21:43] e quindi unique name containing between
[00:21:45] one and 20 letters, number, dashes or
[00:21:48] undersores. Perfetto. Generate. E ora
[00:21:52] possiamo dirgli tornando su cloud,
[00:21:55] quindi API,
[00:21:58] e poi gli possiamo dire secret key. Ok,
[00:22:03] gli avevo chiesto di fare tutto da solo,
[00:22:05] però poi ho deciso di farlo con voi.
[00:22:09] Perfetto, quindi fatemi pulire.
[00:22:13] E ora noi una volta fatto premeremo
[00:22:15] bypass permission e continueremo
[00:22:17] l'implementazione. E questo è quindi il
[00:22:20] nostro bot che ha fatto adesso, come
[00:22:23] vedete, nell'arco di qualche minuto,
[00:22:25] perché gli ho chiesto di simularle, eh
[00:22:27] cinque o sei transazioni.
[00:22:30] E qui abbiamo la possibilità di fare
[00:22:31] refresh dashboard. Come eh vedete,
[00:22:34] questa è una dashboard fatta in local
[00:22:36] hostilate
[00:22:40] il testnet di Binance, questo non ha una
[00:22:43] dashboard visiva, ma se invece poi voi
[00:22:45] andrete ad utilizzare la dashboard di
[00:22:48] Binance con soldi veri, allora potrete
[00:22:50] entrare nell'interfaccia principale e
[00:22:52] vedere proprio le vostre trade, come se
[00:22:54] stesse facendo trading voi in prima
[00:22:57] persona. Spero quindi che il video vi
[00:22:58] sia stato utile, non tanto per capire
[00:23:00] qual è il miglior modo di costruire un
[00:23:02] bot di trading, ma quanto per capire
[00:23:04] come potete affrontare qualsiasi
[00:23:06] problema con l'AI e quindi innanzitutto
[00:23:09] chiarificando il problema che andrete a
[00:23:11] fare, zoomando indietro, avendo una
[00:23:12] visione di alto livello, poi andando
[00:23:14] dentro e definendo più o meno una
[00:23:16] struttura architetturale e solo a quel
[00:23:18] punto procedere con l'implementazione.
[00:23:20] Questi tre step però non sono
[00:23:22] sufficienti se non sapete come scrivere
[00:23:24] prompticaci con cloud e per farlo ho
[00:23:27] fatto un corso completo che vi lascio
[00:23:29] qua sopra nel quale vi porto da beginner
[00:23:32] a completi esperti in come scrivere
[00:23:34] prompt di successo con Cloud Code e con
[00:23:36] Codex. Yeah.
