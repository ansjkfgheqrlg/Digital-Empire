
[00:00:00] Hei, benvenuto in quello che è il corso
[00:00:02] più completo sugli agenti AI attualmente
[00:00:04] disponibile su YouTube. Io ho una
[00:00:06] community dove insegno agli imprenditori
[00:00:07] e freelancer come implementare agenti AI
[00:00:10] sia sul proprio business sia per
[00:00:12] venderli agli altri. Ed attualmente ho
[00:00:14] anche una mia agenzia AI che lavora con
[00:00:16] aziende da €10.000 al mese fino a 50
[00:00:18] milioni l'anno utilizzando proprio gli
[00:00:20] agenti AI. Non ci sarà bisogno di nessun
[00:00:23] background tecnico o conoscenza
[00:00:25] pregressa di piattaforme per seguire
[00:00:26] questo video, dato che sarà un corso
[00:00:28] generale in modo tale da assicurarsi che
[00:00:31] tutti partiremo dalla stessa conoscenza
[00:00:33] ed arriveremo allo stesso punto. Vi
[00:00:34] faccio ora un overview veloce di quello
[00:00:36] che andremo a coprire, così saprete cosa
[00:00:38] aspettarvi. La prima cosa che faremo
[00:00:40] sarà andare a capire che cos'è un agente
[00:00:42] AI, quindi ci soffermeremo su i pezzi
[00:00:45] che lo costituiscono e andremo a vedere
[00:00:47] poi l'architettura. La seconda cosa che
[00:00:49] faremo sarà andare a costruire un
[00:00:52] semplicissimo agente su N10 per capire
[00:00:55] come i pezzi interagiscono tra di loro e
[00:00:57] vederlo anche a livello pratico. La
[00:01:00] terza sarà capire come questi agenti
[00:01:02] svolgono le tasks. Penso che molti di
[00:01:05] noi abbiano unintuizione su quello che
[00:01:07] succede, ma eh capire che cosa succede
[00:01:10] nel dettaglio è un po' più complicato.
[00:01:12] Poi andremo a vedere i come queste tasks
[00:01:15] avvengono nel dettaglio e utilizzeremo
[00:01:17] antigravity o cloud code, qualsiasi ID
[00:01:19] per farlo. [sbuffare] Andremo poi a
[00:01:21] vedere qual è il loop di ragionamento
[00:01:23] agentico, quello che viene chiamato OTD
[00:01:27] e poi andremo ad analizzarlo in Cloud
[00:01:29] Code per vedere step by step che cosa
[00:01:31] Cloud Code fa nel momento in cui gli
[00:01:32] chiediamo di eseguire una task. Andremo
[00:01:35] poi ad analizzare qual è l'importanza
[00:01:37] dei prompt negli agenti AI e quindi
[00:01:39] questo vuol dire quando utilizzare il
[00:01:41] nostro gemini. Cloud.md o agents.md a
[00:01:45] seconda poi della piattaforma che
[00:01:46] andiamo ad utilizzare.
[00:01:48] Parleremo poi di back prompt
[00:01:51] engineering, quindi in questo caso
[00:01:53] capiremo come riuscire a fare back
[00:01:56] engineering dei nostri prompt
[00:01:57] analizzando due skill. La prima sarà lo
[00:02:00] step back prompting e la seconda skill
[00:02:03] che utilizzeremo sarà il reverse
[00:02:04] prompting. E queste due le utilizzeremo
[00:02:07] sostanzialmente per fare zoom out e
[00:02:09] capire bene o forzare la gente a capire
[00:02:11] qual è la task che vogliamo fare prima
[00:02:13] ancora di andare ad eseguirla. Parleremo
[00:02:15] poi di che cosa sono i prompt contracts,
[00:02:17] che sono una metodologia per assicurarsi
[00:02:20] che i nostri prompt siano sempre molto
[00:02:21] accurati. E alla fine parleremo poi di
[00:02:24] premortem proming, che significa
[00:02:27] assicurarsi di mettere all'inizio del
[00:02:29] progetto tutte le ragioni per cui questo
[00:02:31] progetto potrebbe andare storto, di modo
[00:02:33] tale che l'AI abbia un piano complessivo
[00:02:35] migliore per capire che cosa succede.
[00:02:38] Parleremo poi di self improving prompts,
[00:02:40] in particolare parleremo di quelli che
[00:02:42] vengono definiti adaptive guard rails,
[00:02:44] quindi delle guide che servono ai nostri
[00:02:47] prompt andare nella direzione corretta e
[00:02:49] quindi essere più efficaci e poi ne
[00:02:51] capiremo anche il ciclo iterativo.
[00:02:54] Andremo poi ad analizzare quali sono i
[00:02:56] quattro livelli di specificità del
[00:02:58] prompt e l'influenza che hanno quando
[00:03:00] andate a costruire su piattaforme come
[00:03:02] Codex, Antigravity, Cloud e come si
[00:03:05] comportano. Vedremo poi la definizione
[00:03:07] di agent polling e una skill per farlo.
[00:03:10] Allo stesso modo vedremo quelli che in
[00:03:11] gergo tecnico vengono chiamati agents
[00:03:13] debates, quindi avere più di un agente
[00:03:15] che eh aiuta a rifinire un'idea e quindi
[00:03:19] avremo questi agenti che collaboreranno
[00:03:21] affinché potremo poi avere l'idea
[00:03:23] raffinata alla fine. Parleremo poi di
[00:03:25] che cosa sono i browser SWM, quindi come
[00:03:27] utilizzare più agenti per andare a fare
[00:03:29] diverse sessioni all'interno di
[00:03:31] qualsiasi browser e poi vedremo come si
[00:03:34] fa un full workflow audit e utilizzeremo
[00:03:37] poi una skill per farlo. Detto questo,
[00:03:39] spero siate eccitati tanto quanto me di
[00:03:41] fare questo corso. Cominciamo.
[00:03:42] Cominciamo quindi dalle cose un po' più
[00:03:45] semplici, quindi riprendiamo la canonica
[00:03:47] definizione di che cos'è un agente AI
[00:03:50] prima di andarlo poi a costruire. Nel
[00:03:51] pratico, tutto parte dalla richiesta di
[00:03:55] un utente, quindi l'utente utilizzerà
[00:03:57] una qualche interfaccia di interazione
[00:04:00] con il nostro agente AI. Allora, qui
[00:04:02] abbiamo varie possibilità, no? Abbiamo
[00:04:04] interfacce di tipo chat, quindi
[00:04:06] interfacce di testo, abbiamo interfacce
[00:04:10] eh di tipo vocale, quindi nel momento in
[00:04:13] cui utilizziamo ehm agenti vocali,
[00:04:15] abbiamo un'interfaccia come il microfono
[00:04:17] del telefono o qualsiasi cosa vogliamo
[00:04:20] avere, abbiamo anche possibilità di
[00:04:23] attivare questi ehm agenti AI con
[00:04:27] l'utilizzo di form. Quindi, nel caso in
[00:04:29] cui un ehm cliente compili un form,
[00:04:33] allora attiva l'agente AI e fai queste
[00:04:35] determinate cose. Una volta che questa
[00:04:38] richiesta viene fatta dall'utente, entra
[00:04:41] in quello che noi chiamiamo agente AI. E
[00:04:44] qui allora sappiamo che dentro l'agente
[00:04:48] AI per processare questa richiesta viene
[00:04:52] richiesto in linea generale il fatto che
[00:04:55] ci sia un prompt. Questo è in linea
[00:04:58] generale perché negli agenti più
[00:04:59] semplici, come magari ne vedremo uno
[00:05:02] dopo, eh, o per le cosiddette demo, non
[00:05:05] c'è necessità di avere questo prompt. il
[00:05:07] prompt diventa necessario se e solo se
[00:05:10] cominciamo a avere un un progetto
[00:05:14] abbastanza complesso e lì diventerà la
[00:05:17] cosa invece più importante perché questo
[00:05:20] sarà a livello effettivo l'unica vostra
[00:05:23] proprietà intellettuale mano che il
[00:05:26] mercato delle automazioni e dell'AI
[00:05:29] andrà avanti. Questo perché? perché
[00:05:32] l'automazione di per sé stessa e quindi
[00:05:34] per esempio il template 101 o cose di
[00:05:37] questo tipo non sono cose che hanno
[00:05:39] particolare valore. Quello che avrà
[00:05:41] valore sarà quello che andrete a dare
[00:05:43] voi come istruzione all'agente AI. Ed è
[00:05:46] anche il motivo di questo corso perché
[00:05:48] sarà l'unica skill che non cambierà nel
[00:05:51] momento in cui gli agenti ehm si
[00:05:53] evolveranno, ma rimarrà eh la skill
[00:05:55] necessaria e soprattutto perché, e
[00:05:58] questo ci tengo a stressarlo, il
[00:06:00] l'agente AI viene direzionato dal vostro
[00:06:03] prompt. Che cosa vuol dire? Vuol dire
[00:06:05] che se io sono l'utente e ho come
[00:06:09] obiettivo il fatto di arrivare qui, eh
[00:06:13] se il mio prompt è direzionato nel modo
[00:06:17] corretto, ok? avrò una possibile
[00:06:21] traiettoria di questo tipo, nella quale
[00:06:23] il mio prompt dirà lei hei, vai in
[00:06:26] questa direzione fino a che poi non
[00:06:28] colpisci l'obiettivo. Se invece il mio
[00:06:31] agente è direzionato male, questo
[00:06:33] significa che magari il prompto.
[00:06:36] Abbiamo la possibilità che il prompt
[00:06:38] manchi il nostro obiettivo e poi
[00:06:40] continui all'infinito. Questo perché è
[00:06:43] importante? Beh, perché sapete che
[00:06:45] minore le iterazioni e adesso con la
[00:06:47] scusa dei tagli che magari sta facendo
[00:06:49] antropic che vedremo anche eh Open AI
[00:06:52] farli nel futuro prossimo molto
[00:06:54] probabilmente abbiamo che le due
[00:06:56] variabili che noi abbiamo per decidere
[00:06:58] quanto un eh prompt sia efficace, quindi
[00:07:02] quando un agente stia aiutando il nostro
[00:07:04] business o no, è nell'investimento che
[00:07:06] noi facciamo appunto in dollari che
[00:07:09] rientrano dall'utilizzo di questo ehm
[00:07:12] agente, quindi in time saved o tempo
[00:07:15] salvato, scusatemi, o in fatturato
[00:07:17] aumentato, oppure in token, perché
[00:07:20] questi sono il nostro costo. Quindi,
[00:07:22] ovviamente vogliamo averlo il minore
[00:07:26] possibile, quindi vogliamo avere che la
[00:07:28] gente arriva ad obiettivo nel minor
[00:07:30] tempo possibile. Questo perché un un
[00:07:33] prompt fatto male può permettere al
[00:07:35] vostro agente di non arrivare
[00:07:36] all'obiettivo o mai o magari dopo
[00:07:38] settimane al posto che diciamo dopo
[00:07:41] pochi tentativi. E questo è esattamente
[00:07:43] quello che andremo a fare d'oggi. Un
[00:07:45] altro concetto, dopo avere introdotto il
[00:07:47] nostro prompt e avere detto che questa è
[00:07:50] l'IP, quindi la proprietà intellettuale
[00:07:52] che avremo nel futuro, sappiamo che la
[00:07:55] gente può processare tutte queste
[00:07:57] informazioni perché esistono gli LM.
[00:08:00] Quindi ad ogni agente, come vedremo
[00:08:02] dopo, andremo a collegare un LM, quindi
[00:08:05] c'è CVT, Clod, Gemini o chi per esso, a
[00:08:09] seconda del caso che avremo in esame. Ed
[00:08:12] il motivo per cui lo facciamo è perché
[00:08:14] questi Llm di per se stessi non sono
[00:08:17] super intelligenti, ma possono
[00:08:19] processare bene input testuali. Perché
[00:08:23] dici questo? Allora, perché qui come
[00:08:26] facciamo se l'input non è testuale?
[00:08:28] Quindi, se la richiesta non è testuale,
[00:08:31] abbiamo due modi. Uno è riusciamo a
[00:08:34] trasformare qui in questa, diciamo,
[00:08:37] nuvola, ok, l'input in testo, oppure
[00:08:40] quello che è stato fatto nel corso del
[00:08:42] tempo è dare alla gente la possibilità
[00:08:46] di accedere ai cosiddetti strumenti.
[00:08:49] Quindi gli strumenti sono oltre a quelli
[00:08:51] che noi conosciamo, se avete utilizzato
[00:08:54] anche magari strumenti come cloud code o
[00:08:58] Antigravity o Codex eccetera, abbiamo
[00:09:01] anche la possibilità di avere uno
[00:09:03] strumento che si chiama read, uno
[00:09:05] strumento che si chiama bash e quindi
[00:09:08] sotto al allaagente esistono, diciamo,
[00:09:11] molte cose che sono state concesse,
[00:09:14] diciamo, nell'infrastruttura da parte di
[00:09:16] antropic open AI e via dicendo. che
[00:09:19] permettono alla gente di fare cose,
[00:09:21] quindi permettono alla gente in queste e
[00:09:24] ce ne sono una marea, di processare
[00:09:26] anche input non testuali perché la gente
[00:09:29] di solito o l'LM semplice non ce la fa,
[00:09:32] oppure di accedere ai servizi esterni.
[00:09:35] questi servizi esterni, ovviamente noi
[00:09:37] sappiamo che ci accediamo tramite
[00:09:39] specifiche API, quindi una
[00:09:41] documentazione specifica e noi in cambio
[00:09:44] dell'accesso a questi servizi di terzi
[00:09:47] abbiamo che dobbiamo dare una un piccolo
[00:09:50] riscontro economico, quindi che è il
[00:09:51] motivo per cui noi veniamo abbiamo un
[00:09:55] billing, quindi il nostro ehm il nostro
[00:09:58] la nostro quantitativo di denaro che noi
[00:10:00] spendiamo per qualcosa dipende da il
[00:10:03] numero di token che consumiamo che
[00:10:05] dipende dal numero di chiamate che
[00:10:07] facciamo all'API di un servizio a terzo.
[00:10:09] Quindi ovviamente più chiamiamo un
[00:10:12] servizio terzo, quindi più volte lo
[00:10:13] utilizziamo, peggio è per noi perché
[00:10:15] pagheremo molto di più. Come ultimo
[00:10:18] concetto conclusivo e poi andiamo a
[00:10:20] vederlo nella pratica, abbiamo che la
[00:10:23] gente AI non ricorda le cose che andiamo
[00:10:28] a ehm fare, a meno che non gli diamo la
[00:10:32] possibilità di avere una memoria.
[00:10:34] Allora, noi sappiamo che esistono
[00:10:36] diversi tipi di memorie di cui poi
[00:10:38] andremo a parlare, però per ora è
[00:10:41] necessario sapere che noi dobbiamo
[00:10:43] inserire una memoria all'interno di
[00:10:45] questo agente per permettergli di fare
[00:10:46] determinate cose.
[00:10:49] Una volta discusso questo, quindi,
[00:10:50] andiamo dentro NA10 e vediamo nella
[00:10:52] pratica come possiamo costruirne uno.
[00:10:55] Perfetto, io sono dentro NA10. Ora,
[00:10:57] questo non è un corso eh diciamo su
[00:11:00] NA10, quindi basta semplicemente che voi
[00:11:02] guardiate. Andremo a replicare
[00:11:04] esattamente quello che abbiamo detto ora
[00:11:05] sulla teoria e vi disegnerò i
[00:11:08] parallelismi di modo tale che voi
[00:11:09] possiate collegare le cose. Allora,
[00:11:11] abbiamo detto che inizialmente dobbiamo
[00:11:13] avere questo, quindi un agente AI,
[00:11:15] quindi quello che andremo a fare sarà
[00:11:18] andare a premere AI agent ed importarlo
[00:11:21] dentro al nostro NA10. Come vedete di
[00:11:24] default
[00:11:26] viene concessa un o connessa,
[00:11:28] perdonatemi, un'interfaccia grafica con
[00:11:30] il nostro agente che gli permetterà di
[00:11:33] poter interagire con il nostro
[00:11:35] potenziale utente. Adesso, prima di
[00:11:37] entrare nel pratico, andiamo a
[00:11:39] connettere un LM. In questo caso andremo
[00:11:42] a connettere Open AI e gli dirò le mie
[00:11:46] credenziali che ho già connesso
[00:11:48] ovviamente al mio ehm al mio NA10.
[00:11:52] Quindi adesso abbiamo connesso il nostro
[00:11:54] LLM che, come vedete, è un blocco
[00:11:56] separato, non è è diciamo dentro
[00:11:58] l'agente AI, ma non è una cosa a sante.
[00:12:01] Dobbiamo poi connettergli una memoria di
[00:12:05] modo tale che la gente possa ricordarsi
[00:12:07] quello che facciamo e abbiamo detto che
[00:12:09] in questo caso ehm noi possiamo
[00:12:12] connettere uno strumento. Allora, in
[00:12:15] questo caso andremo a connettere uno
[00:12:16] strumento come Gmail e quindi andatemi a
[00:12:20] eh magari prendere questo strumento qui.
[00:12:25] Tool description fatta automaticamente e
[00:12:27] diciamo che vogliamo mandare una mail a
[00:12:31] Giovanni Beggiato. Allora, gli diremo
[00:12:33] che vogliamo mandare una mail di testo.
[00:12:35] Lasceremo decidere alle AI l'oggetto
[00:12:38] della mail e anche il nostro messaggio.
[00:12:41] Fatemi fare così, giusto per pulirlo.
[00:12:44] [sbuffare]
[00:12:45] E ora quello che abbiamo detto è in
[00:12:47] questo caso eh la richiesta su agenti
[00:12:51] semplici può essere eh quella che la
[00:12:56] gente interpreta per autocrearsi un
[00:12:58] prompt e per cose complicate non è
[00:13:02] richiesto questo, ok? O non è richiesto
[00:13:05] entrare nel dettaglio di un prompt.
[00:13:06] Infatti voi vedete che adesso per essere
[00:13:09] un po' più precisi, il mio prompt viene,
[00:13:14] diciamo, estratto dalla richiesta
[00:13:15] dell'utente, ok? Quindi non è che non
[00:13:18] c'è, è che non è necessario scriverlo a
[00:13:20] mano ed andare a farlo in maniera
[00:13:21] dettagliata per task molto molto
[00:13:23] semplici che sono quelle che noi
[00:13:24] consideriamo le nostre demo. Quindi, in
[00:13:26] questo caso, apriremo la chat e diremo:
[00:13:29] "Hei, per favore, mando un'email a
[00:13:31] Giovanni" eh, salutandolo e capisci tu
[00:13:35] in maniera automatica eh l'oggetto e il
[00:13:38] testo della mail ehm per ehm raggiungere
[00:13:42] il mio gol. Allora, qui io ovviamente
[00:13:46] ora magari mi sposto per farvi vedere
[00:13:48] dove ho messo il prompt. È qua sotto.
[00:13:51] Ok, quindi gli dirò manda. Ora ritorno
[00:13:55] dov'ero e vedete che qui è andato
[00:13:58] direttamente in memoria, poi è andato a
[00:14:00] capire con l'LM che cosa doveva fare e
[00:14:04] dopo è andato qua dentro. Allora, eh
[00:14:07] adesso ehm se il tutto va bene, tiriamo
[00:14:10] su e vediamo la cartella di esecuzione.
[00:14:13] Adesso fatemi vedere se riesco magari
[00:14:15] anche a farvi vedere.
[00:14:18] Ehm,
[00:14:20] eccolo qua
[00:14:22] il nostro messaggio. Allora, perfetto.
[00:14:26] Questo è il messaggio che abbiamo
[00:14:28] ricevuto. Spero spero si veda e ora
[00:14:32] andiamo a vedere in dettaglio com'è
[00:14:33] avvenuta questa esecuzione.
[00:14:35] Inizialmente abbiamo che la gente ha
[00:14:38] interpretato la nostra richiesta, quindi
[00:14:40] la prima cosa che ha fatto è entrare,
[00:14:43] scusate, nella memoria semplice ed è
[00:14:47] andato a capire se effettivamente c'era
[00:14:51] qualcosa in memoria oppure no. Che cosa
[00:14:53] ha trovato? Ha trovato assolutamente
[00:14:55] nulla. Ha trovato un array, quindi la
[00:14:57] memoria vuota. Quindi che cosa ha fatto?
[00:15:00] è andato di nuovo a dal nostro input
[00:15:03] open AI e perché non ha trovato niente
[00:15:05] in memoria e ha processato poi la nostra
[00:15:08] eh richiesta. Infatti c'è scritto
[00:15:10] l'umano
[00:15:12] ha voluto mandare questa mail. Poi una
[00:15:16] volta
[00:15:17] che ha processato il tutto, ora senza
[00:15:20] farvi vedere il resto, dice l'email è
[00:15:23] stata inviata a Giovanni con un saluto.
[00:15:25] Se hai bisogno di ulteriori modifiche o
[00:15:27] inviare un'altra mail, fammi sapere.
[00:15:30] Poi qua vedete che tra questo processo e
[00:15:34] questo abbiamo che il subject è stato
[00:15:37] manipolato dalle Yai e ha capito al volo
[00:15:39] che quello che volevamo avere era un
[00:15:41] saluto. E poi ciao Giovanni, spero tu
[00:15:44] stia bene, ti volevo solo ehm prendermi
[00:15:47] un momento per salutarti, un caro saluto
[00:15:49] e poi il mio nome. Vedete che qui ora
[00:15:53] all'interno della nostra memoria noi
[00:15:55] abbiamo la cosiddetta memory variable e
[00:15:59] quindi se io ora andassi ad interpretare
[00:16:01] o scusate interpellare
[00:16:04] la gente di nuovo mi muovo al volo un
[00:16:07] secondo e gli chiedessi
[00:16:09] "Hei, sapresti dirmi qual è l'ultima eh
[00:16:12] richiesta che ti ho fatto in questa
[00:16:14] chat?"
[00:16:18] Noi ora andremo a vedere che, e ora mi
[00:16:22] riposiziono dov'ero, che l'ultima
[00:16:24] richiesta che mi hai fatto è stata di
[00:16:26] inviare unemail a Giovanni. di nuovo è
[00:16:29] qui, in questo caso è andato dentro alla
[00:16:31] memoria, ha processato, ha trovato la
[00:16:35] cosa, ma come vedete non ha attivato il
[00:16:38] tool di Gmail, quindi l'LM fa eh
[00:16:41] processare in maniera intelligente alla
[00:16:44] gente i le proprie informazioni e gli
[00:16:48] permette poi di usufruire dei tool
[00:16:50] corretti nel momento in cui ne ha
[00:16:52] bisogno. di nuovo, qui abbiamo
[00:16:54] un'infinità di tool, come potete vedere
[00:16:57] abbiamo, scusatemi, abbiamo e fatemelo
[00:17:01] rimuovere al volo, abbiamo ehm in app
[00:17:06] azioni, quindi abbiamo tutti questi,
[00:17:08] quindi vedete che ce ne sono veramente
[00:17:10] un'infinità e starei qui 5 minuti solo
[00:17:12] per scollerli tutti. Bene. Eh, ultima
[00:17:17] cosa, la memoria sarà molto interessante
[00:17:20] per noi. In questo caso abbiamo una
[00:17:22] memoria con una context window length di
[00:17:25] 5, vuol dire teniamo al massimo cinque
[00:17:28] conversazioni. Poi questo è perché
[00:17:30] questo agente di N10 è molto semplice.
[00:17:32] Ora che ci sposteremo sugli IDE, le cose
[00:17:35] un po' si complicano, però le vedremo
[00:17:37] tutte passo passo. Di nuovo, abbiamo
[00:17:39] detto che se invece avessimo un prompt
[00:17:42] complesso, noi potremmo cominciare a
[00:17:44] scrivere qui qualcosa e quindi potremmo
[00:17:48] scrivergli qualcosa. Ehi, nonostante la
[00:17:53] richiesta dell'utente, per favore non
[00:17:56] mandare mai un email.
[00:18:00] Perfetto. Noi ora potremmo chiedergli di
[00:18:04] nuovo, potremmo fare open chat. Ehi, per
[00:18:07] favore, puoi mandare una mail a
[00:18:09] Giovanni?
[00:18:14] Perfetto. [schiarire la voce]
[00:18:16] E ora, come vedete, eh workflow è con
[00:18:19] successo, ma questo strumento non è
[00:18:21] stato mai chiamato, quindi vedete la
[00:18:24] potenza e ora andremo un po' più nel
[00:18:25] dettaglio con gli altri del prompt che
[00:18:28] se prima era capita dal dall'input ora è
[00:18:31] processata dall'agente. Bene, detto
[00:18:34] questo entriamo in cose un po' più
[00:18:36] complesse e andiamo un po' più nel
[00:18:38] dettaglio. Abbiamo ora visto nella
[00:18:40] pratica un piccolo agente semplice, ma
[00:18:43] cerchiamo di capire, di formalizzare
[00:18:45] come questi agenti AI effettivamente
[00:18:48] svolgano task che abbiano qualche
[00:18:51] rientro economico, no, nelle nostre
[00:18:53] quotidianità aziendali o nelle nostre
[00:18:56] task personali. La prima cosa che fa la
[00:18:59] gente, come avete visto, è crearsi o
[00:19:03] assemblare la propria finestra di
[00:19:05] contesto. Ok? Quindi questo è
[00:19:08] esattamente quello che la gente sta
[00:19:09] facendo. E che cosa vuol dire? Vuol dire
[00:19:11] che e noi abbiamo capito dal la prima
[00:19:15] chat dove abbiamo dato semplicemente un
[00:19:16] input alla seconda dove abbiamo messo un
[00:19:19] prompt che è contro, no? Quello che
[00:19:21] abbiamo messo nella chat che la finestra
[00:19:24] di contesto raccoglie che cosa? Prima di
[00:19:28] tutto raccoglie gli obiettivi, quindi
[00:19:30] che cosa sta chiedendo la gente e
[00:19:33] scusate l'utente e in che metodologia.
[00:19:36] poi raccoglie gli strumenti che ha a
[00:19:38] disposizione, quindi nel nostro caso di
[00:19:41] prima un Gmail, però quando entreremo
[00:19:43] negli ID ne avremo molti altri a
[00:19:46] disposizione. Poi raccoglierà eventuali
[00:19:49] esempi. Questi dove sono? Sono
[00:19:51] eventualmente dentro al nostro prompt.
[00:19:54] Poi raccoglie le istruzioni del
[00:19:56] contesto, quindi se qui aveva
[00:19:58] l'obiettivo di mandare unemail, qui le
[00:20:02] istruzioni gli dicono non farlo e poi
[00:20:05] abbiamo visto che raccoglie lo storico
[00:20:07] della conversazione.
[00:20:09] Quando dopo parleremo dei quattro layer
[00:20:12] di principio su come gli agenti
[00:20:14] interagiscono, vediamo che qui abbiamo
[00:20:17] già un primo layer che è che se questa è
[00:20:21] la nostra interfaccia chat, ok? E quindi
[00:20:25] abbiamo un cerchio e qui abbiamo invece
[00:20:28] il nostro prompt, ok? più andiamo verso
[00:20:32] il core di questo di questo centro, di
[00:20:35] questo cerchio, scusate, più il prompt
[00:20:38] diventa forte. Dopo parleremo di quattro
[00:20:41] layer che abbiamo quando andiamo su
[00:20:42] Cloud Code, Codex e tutti quei sistemi
[00:20:45] lì e vi mostrerò a livello pratico di
[00:20:47] nuovo come prompt che confliggono l'uno
[00:20:50] con l'altro si comporteranno.
[00:20:53] La seconda cosa che viene fatta dopo
[00:20:55] avere sistemato la finestra di concetto
[00:20:57] è invocare l'LM. Che cosa vuol dire?
[00:21:00] Vuol dire che in questo caso stiamo
[00:21:02] facendo una chiamata esterna che
[00:21:05] significa che stiamo usufruendo di API
[00:21:09] che tradotto significa che per ogni
[00:21:12] chiamata esterna noi abbiamo un
[00:21:15] investimento, quindi un piccolo
[00:21:17] quantitativo di denaro che noi mandiamo.
[00:21:19] Una volta invocato l'LM che cosa cerca
[00:21:23] di fare l'AI? Cerca di capire se il
[00:21:26] nostro obiettivo è stato raggiunto
[00:21:28] oppure no. se è raggiunto esce
[00:21:30] direttamente dal loop e ci restituisce
[00:21:33] il risultato. Nel nostro caso
[00:21:35] l'obiettivo era non mandare email,
[00:21:38] quindi l'obiettivo è raggiunto e abbiamo
[00:21:40] visto, se torniamo in NA10, che è uscito
[00:21:43] immediatamente
[00:21:45] dal
[00:21:47] loop perché non è andato qua dentro per
[00:21:50] prendere il tool, ma siccome l'obiettivo
[00:21:52] era raggiunto, abbiamo già ricevuto in
[00:21:55] output un item di successo con la
[00:21:58] risposta dell LLM che dice "Ho capito,
[00:22:01] non invierò la tua richiesta".
[00:22:04] Una volta raggiunto questo obiettivo,
[00:22:07] ehm, lo strumento si, o meglio l'agente
[00:22:10] si prepara per l'esecuzione dello
[00:22:12] strumento e questo l'abbiamo visto nel
[00:22:15] workflow precedente. Quindi, se noi
[00:22:17] andiamo in esecuzioni ed andiamo
[00:22:19] nell'agente precedente, o meglio in due
[00:22:22] agenti fa, probabilmente. Esatto. dove
[00:22:25] abbiamo copiato le cose di prima,
[00:22:27] vediamo che la gente si era poi
[00:22:30] preparato per utilizzare il nostro nodo
[00:22:33] Gmail, quindi aveva fatto tutte le sue
[00:22:35] ehm le sue manipolazioni.
[00:22:38] Tornando qui, infatti, vediamo anche che
[00:22:41] dopo il nodo AI è entrato nel nodo Gmail
[00:22:44] e si è preparato ad utilizzarlo. Una
[00:22:46] volta che si è preparato ad utilizzarlo,
[00:22:48] ha invocato lo strumento Gmail, quindi
[00:22:51] prompt a strumento e una volta fatto ha
[00:22:55] fatto che cosa? Siccome è un tool e
[00:22:57] questo tool è esterno, di nuovo ha fatto
[00:23:00] una chiamata API, quindi nuovamente
[00:23:03] abbiamo investito una piccola quantità
[00:23:06] di denaro e eh una volta fatto fa
[00:23:09] l'azione ed aggiorna la finestra di
[00:23:12] contesto. Che cosa vuol dire? Vuol dire
[00:23:14] che tutte le cose che abbiamo discusso
[00:23:16] prima, quindi aggiornerà la memoria e
[00:23:17] farà molte altre cose. Andiamo a vedere
[00:23:20] ora questo come si ripercuote dentro ad
[00:23:23] un eh IDE e quindi andremo ad utilizzare
[00:23:26] poi un qualcosa ora di agentico, quindi
[00:23:29] entreremo dentro cloud code e vedremo
[00:23:31] questo processo in dettaglio, quindi
[00:23:33] andremo a vederlo in maniera pratica,
[00:23:35] quindi andremo a vedere esattamente come
[00:23:37] funziona. Perfetto, sono quindi in
[00:23:39] un'interfaccia vuota e quello che ora
[00:23:41] chiederò sarà: "Hei, per favore, mi
[00:23:43] servirebbe che tu ehm spawnassi cinque
[00:23:47] agenti in parallelo per fare cinque
[00:23:50] ricerche diverse su quale sia il metodo
[00:23:54] migliore per vendere servizi ad aziende
[00:23:57] sopra ai €10.000.
[00:24:00] Allora,
[00:24:04] qui potremmo dire eh quindi analizza
[00:24:07] qualsiasi cosa dal content creation al
[00:24:10] cold email outreach e quindi quello che
[00:24:13] vedremo ora è che comincerà a lanciare i
[00:24:16] cinque agenti in parallelo, ok? Per
[00:24:19] vendita B2B high ticket e quindi
[00:24:22] comincerà a fare cosa? A creare la
[00:24:24] finestra di contesto, quindi strumenti,
[00:24:27] obiettivi, eccetera. Vedete che qui ha
[00:24:29] cominciato a chiamare i vari agenti.
[00:24:33] Ok. E eccoci qui. Cominciamo ad
[00:24:36] utilizzare i primi strumenti di ricerca
[00:24:38] eh personalizzata.
[00:24:40] Ehm vi faccio uno spoiler, è il Cold
[00:24:44] Outreach, però [risate] intanto andiamo
[00:24:47] a vedere che cosa c'è. Content creation
[00:24:49] è sotto i €10.000 come più o meno come
[00:24:51] 8020.
[00:24:53] Allora, poi abbiamo che eh qui andiamo a
[00:24:56] processare le istruzioni e quindi
[00:24:59] andremo, vedete, continueremo ad andare
[00:25:01] sotto abbiamo il secondo web search che
[00:25:04] viene chiamato, il terzo bash command e
[00:25:08] quindi vedete come prima si prepari ad
[00:25:11] utilizzare questi tool e poi li vada ad
[00:25:13] utilizzare. Se poi voi premete avete
[00:25:16] anche la possibilità di vedere dentro al
[00:25:19] tool che cosa sta processando, no?
[00:25:21] Quindi GDPR, called email strategy in
[00:25:23] 2025, legal basis, eccetera, eccetera
[00:25:27] eccetera. Una volta quindi che tutti
[00:25:30] questi strumenti e anche i vari agenti
[00:25:32] no, abbiamo la possibilità di vedere che
[00:25:34] cosa pensano, in questo caso ne abbiamo
[00:25:36] più di uno, abbiamo che alla fine di
[00:25:39] questo processo avremo il nostro output.
[00:25:42] E ora aspetto semplicemente che questa
[00:25:44] ricerca venga completata per
[00:25:45] mostrarvelo. Perfetto. E ora abbiamo il
[00:25:48] risultato. Allora, e questo, attenzione
[00:25:51] perché è super importante, mi dice, ecco
[00:25:54] i risultati delle cinque delle cinque
[00:25:56] ricerche, eh, ti faccio una sintesi per
[00:25:58] canale. Content marketing e thought
[00:26:01] leadership, quindi priorità LinkedIn
[00:26:04] YouTube per revenue immediata, eccetera
[00:26:06] eccetera eccetera.
[00:26:08] cosa si sblocca, il perché e via
[00:26:11] dicendo. E poi mi mette il cold email
[00:26:14] outreach come metodo numero due. Ok?
[00:26:17] Allora, questo capiamo che a livello
[00:26:20] logico è una cosa che non ci aspettiamo
[00:26:23] perché se noi andiamo a guardare non lo
[00:26:25] so, un i deal più grossi che ci siano,
[00:26:28] quindi i cosiddetti merger and
[00:26:31] acquisition, giusto? Questi sono fatti
[00:26:34] generalmente ovviamente tramite network,
[00:26:37] ma sono fatti tramite outbound, quindi
[00:26:41] non ci aspettiamo che un deal da 5
[00:26:44] milioni [risate] avvenga tramite content
[00:26:47] creation, neanche per persone come Alex
[00:26:50] Ormosi o quella gente lì che ha,
[00:26:53] diciamo, capitali anche da investire in
[00:26:55] un team di marketing. Ma perché questo
[00:26:57] succede? Perché questa ricerca è biased
[00:27:01] da Eccolo qui. Eh, il l'arry più alto
[00:27:06] nel breve termine è LinkedIn Social
[00:27:09] Selling, combinato con un workshop
[00:27:11] mensile come meccanismo di conversione.
[00:27:13] Cold, email e referral sono buoniali
[00:27:16] canali paralleli da costruire nel tempo,
[00:27:18] ma LinkedIn è la leva più immediata.
[00:27:20] Ora, se io facessi una ricerca unbiased
[00:27:23] però e quindi ecco qua il prompt,
[00:27:27] ok? Vediamo che il il risultato dei
[00:27:32] cinque agenti ora è il cold email
[00:27:35] outbound, ok? Quindi cold email outbound
[00:27:38] più LinkedIn Outreach come motore di
[00:27:41] ricerca, che è esattamente quello che io
[00:27:43] per esempio insegno in community quando
[00:27:44] dobbiamo o vendere servizi AI o dobbiamo
[00:27:48] ehm incrementare il revenue di
[00:27:50] un'azienda e vogliamo utilizzare AI
[00:27:53] dentro. Quindi questo è senza dubbio la
[00:27:55] nostra stella. Però ora dobbiamo
[00:27:58] chiederci una cosa e cioè ma perché
[00:28:02] questo è successo? Cioè, se noi abbiamo
[00:28:04] dato lo stesso promptan
[00:28:07] perché la il primo prompt esattamente la
[00:28:11] risposta giusta, ma ci ha dato una
[00:28:13] risposta che sembra giusta e se non
[00:28:15] impariamo a controllare i nostri prompt,
[00:28:18] a controllare in generale i nostri
[00:28:19] agenti AI, continueremo a ricevere
[00:28:21] risposte che sembrano giuste, ma non
[00:28:23] hanno alcun poi ritorno economico su
[00:28:26] quello che facciamo, quindi magari ci dà
[00:28:28] una proposta su la eh non so
[00:28:30] l'automazione che vogliamo fare per fare
[00:28:33] automazione di proposte quando li
[00:28:35] mandiamo ad un cliente, cioè dopo finita
[00:28:38] la chiamata noi vogliamo mandare in
[00:28:40] automatico la proposta e cloud code ci
[00:28:42] fa costruire qualcosa. Se non siete
[00:28:44] direzionati ottenete una cosa che sembra
[00:28:47] corretta ma non ha alcun valore
[00:28:48] economico perché perché magari è stato
[00:28:51] biased da cose interne a se stesso.
[00:28:54] Quindi tendono a essere un po' pigri
[00:28:56] questi LLM, per capirci. Tendono a
[00:28:59] prediligere alcune informazioni, se
[00:29:02] queste informazioni sono AI optimized
[00:29:06] per la ricerca. E vi faccio un esempio,
[00:29:09] cioè se io cerco Giovanni Beggiato
[00:29:12] adesso e chiedo chi è, io ho un profilo
[00:29:15] che è estremamente AI optimized, no?
[00:29:18] Perché tutto qui parla solamente, tra
[00:29:20] virgolette di me quando cerco me stesso
[00:29:23] e prima che arrivi qualcuno, ok, non c'è
[00:29:25] nessuno sulla prima pagina di Google.
[00:29:27] Quindi questo per dirvi attenzione
[00:29:30] perché qua sta succedendo qualcosa. E
[00:29:32] che cosa succede? Allora, per fare
[00:29:35] questo andiamo nel nostro Excalidro e
[00:29:37] introduciamo il concetto di loop di
[00:29:40] ragionamento. Allora, il Rop di
[00:29:43] ragionamento agentico funziona e ora
[00:29:46] stiamo andando un layer sotto a tutto
[00:29:48] quello che abbiamo spiegato prima con il
[00:29:51] nostro input utente. Qui prima abbiamo
[00:29:54] detto che entra nell'agente AI, ora
[00:29:56] abbiamo detto, diciamo, viene processato
[00:29:59] dal nostro LLM. Poi l'LM che cosa fa?
[00:30:02] Abbiamo visto qui che la cosa che fa è
[00:30:05] assemblare la finestra di contesto
[00:30:07] iniziale. Ma che cosa vuol dire? Vuol
[00:30:09] dire che qui è dove cominciamo a
[00:30:10] introdurre i primi bias. Quindi, che
[00:30:12] cosa abbiamo? Abbiamo una memoria
[00:30:15] semantica. Che cos'è? È la conoscenza
[00:30:18] dell'utente e dell'ambiente per
[00:30:20] conoscere meglio l'input. Quindi qui è
[00:30:23] dove abbiamo introdotto che cosa? Il
[00:30:26] LinkedIn bias, per esempio. E capite
[00:30:29] bene quanto sbagliato sia. dire ad una
[00:30:33] persona o magari voi volete vendere
[00:30:35] servizi ai o cose di questo tipo,
[00:30:37] content creation nella strada, è folle,
[00:30:40] voi dovete fare outbound perché è
[00:30:42] l'unico modello che si scala sopra i
[00:30:44] €10.000 000 al mese volete crescere
[00:30:45] un'azienda di un certo tipo. Ed è il
[00:30:47] mio, per esempio, eh meccanismo di
[00:30:49] acquisizione dei clienti più grosso e
[00:30:52] anche quello dei clienti con cui lavoro.
[00:30:54] Quindi memoria semantica super
[00:30:57] importante. La seconda cosa che abbiamo
[00:30:59] di cui non molti parlano perché non
[00:31:01] molti conoscono, è memoria episodica.
[00:31:05] Ok? Quindi che cosa vuol dire? sono le
[00:31:07] raccolte di interazioni che vengono
[00:31:09] fatte tra l'AI, l'utente ed i processi
[00:31:14] nel mentre di pensiero. Quindi, che cosa
[00:31:16] vuol dire? Che se qualcosa è successo e
[00:31:19] ora vi darò un promptate
[00:31:21] inserirla questa eh memoria episodica
[00:31:25] che se qualcosa è successo l'AI in
[00:31:27] qualche modo deve ricordarselo, o
[00:31:28] meglio, una buona AI. A questo punto,
[00:31:32] dopo avere fatto questo loop, che è
[00:31:35] quello che noi andremo a definire tra
[00:31:37] poco, dove pianifica, esegue, valuta il
[00:31:41] suo feedback, ok? E poi ripianifica,
[00:31:45] allora a questo punto che cosa farà?
[00:31:47] Riandrà a chiamare questi strumenti, ma
[00:31:50] che sono i nostri tool, sono quelli che
[00:31:52] abbiamo definito prima, come Google,
[00:31:55] come le API del meteo, eccetera. E a
[00:31:57] questo punto introduciamo altri due
[00:31:59] concetti di memoria.
[00:32:01] Il primo è la memoria procedurale,
[00:32:04] quindi conoscenza di cosa si può fare e
[00:32:07] come eseguirlo. E quindi che cosa ci
[00:32:10] viene in mente qui? Se voi avete
[00:32:12] automatizzato un po' dei vostri workflow
[00:32:15] o avete già capito di cosa sto per
[00:32:16] parlare, parliamo delle cosiddette skill
[00:32:20] degli agenti, no? Se non sapete che
[00:32:22] cos'è, andate nel mio canale, ho fatto
[00:32:24] un corso di 40 minuti dove vi spiego in
[00:32:26] dettaglio che cosa sono le skill. E
[00:32:28] questo invece è la memoria di lavoro,
[00:32:31] quindi i vari stati interni da
[00:32:32] mantenere, cose da non modificare e cose
[00:32:35] di questo tipo. Che cosa succede quando
[00:32:38] abbiamo questo loop di ragionamento
[00:32:40] agentico? E ve lo faccio vedere di nuovo
[00:32:41] live e gli chiederò adesso alla al primo
[00:32:45] prompt, quindi quello biased, hei, ho
[00:32:49] una domanda per te. Per caso il tuo
[00:32:51] output è biased fatto che io ho un
[00:32:54] LinkedIn con più di 50.000 persone?
[00:32:57] Per caso se partissi da zero, avresti
[00:33:00] un'altra raccomandazione da darmi?
[00:33:03] Adesso semplicemente per convenienza lo
[00:33:05] teniamo in ehm in bypass permission.
[00:33:09] Eccolo qui. Vedi? Quindi sì,
[00:33:11] assolutamente il mio è biased
[00:33:15] tuo asset esistente. Quindi questo è per
[00:33:18] dirvi se per caso voi non riuscite a
[00:33:21] controllare il promptete in qualche modo
[00:33:23] consapevoli che questo bias esiste,
[00:33:26] state già direzionando il vostro agente
[00:33:28] nella direzione sbagliata. Quindi spero
[00:33:30] che fino ad ora io vi abbia almeno
[00:33:32] convinti che questo è un bias da da
[00:33:36] addressare immediatamente. Ora vediamo
[00:33:38] anche come farlo con un paio di chicche,
[00:33:40] ma eh spero che la prima cosa sia
[00:33:43] arrivata. Quindi, quando fate o
[00:33:46] utilizzate un agente AI per un processo
[00:33:48] che deve portarvi un ritorno economico,
[00:33:50] assicuratevi sempre che nel vostro
[00:33:52] promptate
[00:33:54] eliminato i biasserito
[00:33:58] tutti quei piccoli pezzettini di memoria
[00:34:00] di cui abbiamo appena parlato. Detto
[00:34:02] questo, continuiamo. Tornando quindi a
[00:34:04] noi, se ora dovessimo cominciare a
[00:34:06] descrivere questo loopentico e a capire
[00:34:09] nel dettaglio che cosa vuol dire che la
[00:34:11] gente pianifica, che cosa vuol dire che
[00:34:14] esegue, cosa vuol dire che valuta, che
[00:34:16] feedback, ok? Perché sono le classiche
[00:34:18] cose che vediamo. Entriamo un po' più
[00:34:20] nel dettaglio e allora andiamo a
[00:34:22] vederlo. Questo, come detto, è il nostro
[00:34:25] OTDI che sono i il framework agentico
[00:34:29] tramite il quale la gente opera. E
[00:34:31] questo è per darvi una struttura in modo
[00:34:34] tale che d'ora in avanti voi possiate
[00:34:36] avere consapevolezza di quello che
[00:34:38] succede e poi la vedremo in maniera
[00:34:40] pratica. Per spiegarvelo in maniera
[00:34:42] semplice, cominciamo a partire dal
[00:34:43] pensiero. Allora, la prima cosa che
[00:34:46] facciamo ora è processare tutto il
[00:34:49] contesto. Quindi, cominciamo a
[00:34:52] processare il prompt, quindi tutte le
[00:34:54] istruzioni che gli abbiamo dato,
[00:34:56] processare tutto quello che abbiamo in
[00:34:58] memoria, processare la nostra
[00:35:00] traiettoria, quindi no, il goal che gli
[00:35:02] abbiamo dato e capire dove siamo.
[00:35:05] Abbiamo un ragionamento che si articola
[00:35:09] in una generalmente quando diamo ad un
[00:35:13] un AI un task ed immaginiamo che il task
[00:35:17] sia disegna questo questo rettangolo.
[00:35:20] Lei quello che farà sarà andare a capire
[00:35:23] che ehm abbiamo magari che questo eh
[00:35:27] rettangolo può essere costruito da varie
[00:35:30] forme, ok? e da vari altri rettangoli
[00:35:33] che possono avere questi questi colori.
[00:35:36] Quindi quello che fa è decompone il
[00:35:39] nostro obiettivo in subobiettivi e dopo
[00:35:43] una volta che li ha decomposti quello
[00:35:45] che va a fare è unirli. Quindi
[00:35:48] inizialmente abbiamo che questi quadrati
[00:35:51] sono disposti così. Ok? Adesso
[00:35:53] semplifico il disegno per evitare di
[00:35:57] perdere 4 ore solo perché siamo magari
[00:36:00] non dei disegnatori fortissimi. E dopo
[00:36:03] questi tutti questi vengono in qualche
[00:36:05] modo con il nostro loop, no? vengono
[00:36:08] tutti riorganizzati fino a che non vanno
[00:36:11] a formare esattamente questa forma qui.
[00:36:14] Quindi quello che fa è chain of thoughts
[00:36:17] che quindi è incatena le cose per
[00:36:19] capire, ok, devo fare prima questo, poi
[00:36:21] questo, poi questo, poi questo, dopo
[00:36:22] averli decomposti.
[00:36:25] Perfetto. Poi e tutto questo si basa
[00:36:27] ovviamente su un paradigma che se volete
[00:36:29] andare ad approfondire si chiama React.
[00:36:32] Ok?
[00:36:33] Quindi una volta fatto e quindi una
[00:36:36] volta pensato, la gente agisce, quindi
[00:36:39] vuol dire che comincia a chiamare gli
[00:36:41] strumenti esterni. E qui vi ho fatto un
[00:36:43] esempio che è quello che prima abbiamo
[00:36:45] detto che erano che cosa? Erano le
[00:36:48] Google API, era che cosa? Era per
[00:36:51] esempio il meteo, oppure vi ho detto
[00:36:54] erano i tool esterni, come per esempio
[00:36:58] interni, ok? dispatch, ricerca, code
[00:37:01] interpreter, browser e quindi qui sono
[00:37:04] tutti questi tool qui che ora noi
[00:37:07] andiamo a vedere. Se io tornassi qui,
[00:37:09] vedete, abbiamo bash, abbiamo un sacco
[00:37:13] un sacco di cose diverse, web search e
[00:37:15] cose di questo tipo. Perfetto. L'output
[00:37:18] del tool poi torna, ok? E e rientra come
[00:37:23] output. E a questo punto, se noi abbiamo
[00:37:26] fatto un buon prompt, dobbiamo dare al
[00:37:29] tool la possibilità di riflettere. Cosa
[00:37:33] vuol dire riflettere? Vuol dire
[00:37:35] autovalutare il proprio prompt. E una
[00:37:38] volta che lo abbiamo autovalutato, la
[00:37:41] gente dovrebbe poter ricominciare il
[00:37:44] cerchio di modo tale da ripoter
[00:37:46] osservare quello che ha fatto e
[00:37:48] continuare ad avere che questo loop
[00:37:51] continua all'infinito, diciamo, fino a
[00:37:53] che non ehm abbiamo che cosa? O un goal.
[00:37:59] Quindi a questo punto noi abbiamo che un
[00:38:02] output è done, quindi gli avremo
[00:38:05] definito eh che cosa vuol dire avere
[00:38:08] finito una task, oppure avremo una
[00:38:11] condizione di terminazione, quindi le
[00:38:14] API sono morte, hai speso troppi soldi,
[00:38:17] eh non non convergiamo, eccetera.
[00:38:19] Ovviamente tutto questo verrà inserito
[00:38:21] nella memoria e poi dentro l'ambiente.
[00:38:24] Ehm, per farvi un'idea,
[00:38:28] questo è un loop che se voi lo doveste
[00:38:32] disegnare, ok? Immaginatevi di avere qui
[00:38:36] il vostro prompt
[00:38:39] iniziale,
[00:38:41] poi avete qui l'agente fa qualcosa,
[00:38:46] quindi abbiamo task, ok? Poi qui abbiamo
[00:38:52] il verification loop,
[00:38:56] verifica.
[00:38:58] Qui poi avremo il concetto di feedback,
[00:39:02] ok? Eh, quindi la nostra riflessione che
[00:39:06] poi torna qui. In realtà noi abbiamo che
[00:39:09] dopo il feedback abbiamo che questa cosa
[00:39:12] va in memoria, ok? salva l'errore e una
[00:39:17] volta che la memoria è salvata abbiamo
[00:39:19] questo. Quindi, per capirci, il nostro
[00:39:23] ehm tool più verrà utilizzato, quindi il
[00:39:26] nostro agente, più verrà utilizzato eh a
[00:39:28] all'inizio farà una cosa del genere,
[00:39:31] quindi partirà da qui, farà una cosa del
[00:39:33] genere, poi continuerà a fare un loop
[00:39:35] così e dopo tornerà di qui e dopo
[00:39:38] continuerà a fare un loop così e poi
[00:39:39] tornerà di qui. Perché vi dico questo?
[00:39:41] Perché all'inizio questo feedback del
[00:39:44] salvataggio in memoria e voglio e voglio
[00:39:45] farvelo vedere, è una cosa che ehm
[00:39:48] diciamo farà imparare alla gente
[00:39:51] parecchie cose, ok? E quindi qui è dove
[00:39:54] il vostro agente, adesso fatemi chiudere
[00:39:56] queste qui in modo tale che voi possiate
[00:39:58] vederlo nel migliore dei modi. Vedete
[00:40:00] che io qui poi ho una serie infinita di
[00:40:03] regole che il mio agente ha imparato.
[00:40:06] Ora il promptare questa cosa qui ve lo
[00:40:08] darò perché è esattamente l'argomento
[00:40:10] che ora andiamo a trattare. Quindi ora
[00:40:13] andremo a capire che cosa sono i prompt,
[00:40:16] perché sono importanti e quando
[00:40:18] utilizzare questi markdown file quando
[00:40:20] andiamo a costruire i nostri agenti.
[00:40:21] Bene, per farlo cominciamo da un
[00:40:23] progetto completamente nuovo. Quello che
[00:40:25] vogliamo fare ora è ehm capire come
[00:40:29] questi prompt direzionano i nostri
[00:40:30] agenti, no? Perché abbiamo detto che
[00:40:32] ipotizziamo di sapere già che risposta
[00:40:35] vogliamo, ok? Da un qualcosa, giusto per
[00:40:38] scopi didattici e dopo andremo a vedere
[00:40:40] i guardrail. Voglio farvi vedere come
[00:40:42] questo c'è avviene nella pratica.
[00:40:45] Allora, hei, dimmi un numero da 1 a 100.
[00:40:50] Allora, in questo caso noi abbiamo che
[00:40:53] eh stiamo chiedendo al alla gente di
[00:40:57] darci un numero da 1 a 100. Ipotizziamo
[00:40:59] che la risposta corretta sia sempre, non
[00:41:01] lo so, 27. Ok? Che cosa faremo noi?
[00:41:06] Bene, noi avremo un prompt e la gente
[00:41:09] andrà senza direzione e mi darà un
[00:41:12] numero da 1 a 100. Ok?
[00:41:15] Bene, ora immaginiamo di fare il nostro
[00:41:19] prompto,
[00:41:21] siccome utilizziamo antigravity e nella
[00:41:24] parte qui con Gemini, utilizziamo un
[00:41:26] Gemini. MD, se stessimo utilizzando
[00:41:30] Cloud Code, useremmo un cloud. MD.
[00:41:36] Se invece stessimo utilizzando Codex,
[00:41:39] utilizzeremmo un agentsmd.
[00:41:42] E che cosa sono questi DMD? Beh, non
[00:41:44] sono altro che dei mini prompt inseriamo
[00:41:47] prima della nostra conversazione di modo
[00:41:50] tale da direzionare le AI, ok? E per
[00:41:53] farle imparare che cosa? Tutte le cose
[00:41:55] che abbiamo sbagliato nelle sezioni
[00:41:56] prima. Quindi ora andiamo nel nostro
[00:41:58] gemin e diciamo: "Ehi,
[00:42:02] quando ti chiedo di darmi un numero da 1
[00:42:03] a 100 dammi sempre 42, anzi 27.
[00:42:10] Perfetto. Lo strumento che utilizzo, se
[00:42:12] volete, è Whisperflow e andate sotto e
[00:42:15] hanno cominciato ad introdurre delle
[00:42:16] cose molto come vedete. Bene,
[00:42:19] quindi ora gli chiederò,
[00:42:21] salverò il mio prompt, hei, dammi un
[00:42:24] numero da 1 a 100.
[00:42:29] Ora aspetteremo
[00:42:31] 27. Ehi, dammi un numero da 1 a 100.
[00:42:36] Da uno. Da un a 100.
[00:42:38] &gt;&gt; [risate]
[00:42:39] &gt;&gt; Vediamo se lo capisce. 27. Ok, quindi
[00:42:42] vediamo che ora abbiamo direzionato il
[00:42:45] nostro prompt. Perché questo è
[00:42:47] importante? Beh, non per questo esempio
[00:42:49] sciocco, ma perché ora vi darò questo
[00:42:53] prompt qui che è come noi possiamo
[00:42:56] cominciare a creare i cosiddetti
[00:42:59] adaptive guard rails. Quindi, che cosa
[00:43:01] sono? sono dei promptorano
[00:43:04] da soli piano a mano a mano che noi
[00:43:08] andremo ad utilizzare il nostro agente.
[00:43:11] Quindi che cosa vuol dire? Adesso
[00:43:13] velocemente vi spiego che cos'è. È una
[00:43:15] cosa che ho fatto sulla base di quello
[00:43:16] che ho visto e poi vi dico anche perché
[00:43:19] alcuni altri che trovate in giro non
[00:43:20] funzionano.
[00:43:22] Allora, ti dice ehm eh fai scan a tutte
[00:43:25] le le entry, quindi a tutti i record
[00:43:28] sotto per prima di cominciare a
[00:43:29] qualsiasi task. Quindi questa è una cosa
[00:43:31] che aggiungete al vostro cloud. Mmd.
[00:43:34] Questa è un live correction log, quindi
[00:43:36] è una sessione di correzione live per
[00:43:38] capirci, dove manteniamo tutti gli
[00:43:40] errori. Eh, quando l'errore, lo user ti
[00:43:43] corregge o quando una nuova assunzione
[00:43:46] ehm quando fai un'assunzione sbagliata,
[00:43:48] ehm metti una nuova entrata qua sotto.
[00:43:51] Quindi qui è è il posto in cui
[00:43:52] cominceremo ad avere uno, ad avere due,
[00:43:55] ad avere tre e cose di questo tipo.
[00:43:58] Bene, allora
[00:44:00] che classificazione viene fatta? Allora,
[00:44:03] c'è ci sono persone che tendono a
[00:44:05] classificare questo in 1 modi, quindi
[00:44:08] con label dicendo eh non lo so, eh
[00:44:12] questa è un errore che è stato fatto
[00:44:14] nella chiamata di Cloud Code oppure nel
[00:44:18] eh non lo so, nella pulizia del codice,
[00:44:20] ok? quindi o nella UI dell'interfaccia,
[00:44:23] queste cose non funzionano. Ehm, l'unica
[00:44:26] cosa che vi funziona è una
[00:44:27] categorizzazione in base
[00:44:29] all'attivazione, perché è veramente il
[00:44:31] continuous improvement che la gente
[00:44:33] vuole. Quindi, quando lo facciamo
[00:44:37] abbiamo tre modalità. Abbiamo un always,
[00:44:39] abbiamo un never e abbiamo uno when. Che
[00:44:41] cosa vuol dire? Quindi eh always è un
[00:44:44] comando rinforzante per la gente, quindi
[00:44:46] fai sempre questo quando devi fare
[00:44:49] qualcosa. Never una proibizione, quindi
[00:44:53] non fare mai questo quando chiami
[00:44:57] LinkedIn perché continui a sbagliare e
[00:44:59] continuiamo a perdere tempo. Oppure when
[00:45:02] e quando lavoriamo con qualcosa di
[00:45:04] specifico, quindi when NA10, when Loom,
[00:45:07] when GitHub e cose di questo tipo. Ok?
[00:45:10] Benissimo, ora facciamo un esempio
[00:45:12] sciocco e voglio farvi vedere come
[00:45:14] questo viene aggiornato in maniera live.
[00:45:17] Allora, eh fatemi andare qui, fatemi
[00:45:21] chiudere il disastro che ho appena fatto
[00:45:23] e gli chiederò eh
[00:45:28] per favore, ora ehm generami un numero
[00:45:32] da 1 a 10. 7. Ora una cosa che potrei
[00:45:36] dirgli è: "Ehi, per favore, quando ti
[00:45:39] chiedo di generare un numero da 1 a 10,
[00:45:41] non generai non generare mai un numero
[00:45:45] superiore a 5."
[00:45:54] E ora gli premiamo invio. Quello che il
[00:45:55] nostro agente fa è prioritizing tool
[00:45:58] usage e come vedete abbiamo un entrata
[00:46:01] always. Quindi questo è come andiamo a
[00:46:03] costruirli. Ora, qual è il problema di
[00:46:06] questo? È che quando andiamo giù e
[00:46:08] cominciamo ad avere entrate infinite,
[00:46:11] ok, mettiamone eh che arriviamo a non lo
[00:46:14] so, eh 150 è possibile che un'entrata
[00:46:19] cominci ad essere conflittuale con
[00:46:21] qualcos'altro, no? Eh, a me non è ancora
[00:46:25] successo, però ho introdotto un resolve
[00:46:28] contradictions. È una cosa che ho fatto
[00:46:31] recentemente, dato che sto facendo eh un
[00:46:34] eh un prompt a cui sto lavorando ormai
[00:46:36] da otto quasi settimane per un voice AI.
[00:46:41] Nel caso non lo sappiate, ho un'agenzia
[00:46:43] e una delle cose che facciamo è sono
[00:46:47] voice AI per per B2C. un business
[00:46:50] abbastanza complesso il voice AI. Ecco,
[00:46:52] quindi eh questo è come poi andremo a eh
[00:46:56] fare suppression, quindi un'entrata che
[00:46:59] finisce con super seeds, uccide n entry
[00:47:02] e qui poi potete vederla. [sbuffare] Vi
[00:47:04] lascio questo prompt sotto in
[00:47:07] descrizione, aggiungetevelo ai vostri
[00:47:09] prompt. Eh, risorsa molto e e vi
[00:47:13] permette di migliorare. Che cosa vuol
[00:47:15] dire in termini pratici quello che
[00:47:18] abbiamo appena visto?
[00:47:20] Beh, vuol dire che ipotizziamo di avere
[00:47:23] il nostro asse cartesiano qui e
[00:47:26] ipotizziamo di avere voglia di costruire
[00:47:29] un una non demo, ma un sistema che porti
[00:47:32] effettivamente un risultato economico a
[00:47:33] un qualsiasi tipo di impresa. Che cosa
[00:47:36] vediamo qui? Vediamo che il nostro
[00:47:40] agente con questa tipologia di prompt è
[00:47:42] un agente che migliora nel corso del
[00:47:44] tempo. Se in questo asse mettiamo il
[00:47:46] numero di iterazioni
[00:47:51] che facciamo, che è direttamente
[00:47:52] proporzionale al tempo che spendiamo
[00:47:56] nella sessione. Ok? E se qui invece
[00:48:01] mettiamo il numero di sessioni, quindi
[00:48:03] sostanzialmente è quante volte uso
[00:48:05] l'agente su per quanto tempo lo uso, per
[00:48:08] capirci, possiamo eh vedere magari,
[00:48:10] allora ipotizziamo di avere questa che
[00:48:12] sia un'ora, 2 ore, 3 ore, 4 ore.
[00:48:16] Ipotizziamo, eh, sono conti della serva.
[00:48:19] In rosso avremo che magari inizialmente
[00:48:22] abbiamo che la l'AI fa questo numero di
[00:48:24] errori, poi cominciano a scendere, poi
[00:48:27] siccome continuiamo ad avere sempre più
[00:48:28] sessioni, scendono sempre di più e poi
[00:48:30] magari arriveranno bassi. E invece, e
[00:48:33] quindi questi sono, per farci una
[00:48:36] piccola leggenda, il eh numero di errori
[00:48:42] e invece questo in verde abbiamo che
[00:48:46] queste cominciano invece ad essere il
[00:48:49] nostro numero di regole. Ok? Quindi, per
[00:48:52] capirci, adesso qui e metto regole.
[00:48:58] Man mano a mano che utilizziamo il la
[00:49:01] nostra sessione, il nostro agente
[00:49:03] diventa sempre più intelligente.
[00:49:07] Ok? Quindi questo è il nostro obiettivo
[00:49:13] finale
[00:49:14] e ehm questo è quello che questa
[00:49:17] tipologia di prompte.
[00:49:20] Quindi abbiamo visto che inizialmente
[00:49:22] questo promptare il mio output e poi
[00:49:24] pian pianino se lo controllo in maniera
[00:49:26] corretta possa aspettarmi quello che
[00:49:29] viene definito miglioramento
[00:49:31] incrementale. Quindi, per capire un po'
[00:49:32] meglio e formalizzare quello che abbiamo
[00:49:34] visto, abbiamo visto che il ciclo di
[00:49:36] iterazione, quando parliamo di
[00:49:38] improvement continui, di agenti e quindi
[00:49:41] di quello che abbiamo definito adaptive
[00:49:43] guardra rails, o meglio così è come eh
[00:49:46] li definisco io, ma spero che renda il
[00:49:49] concetto. Abbiamo che inizialmente
[00:49:51] cominciamo la nostra sessione, poi la
[00:49:54] gente andrà ad eseguire un task che
[00:49:57] viene richiesto. A questo punto, se il
[00:49:59] task va bene, non succede niente. Se il
[00:50:01] task non va bene, allora ci sarà un
[00:50:04] errore. La gente commette un errore e
[00:50:07] viene corretto dall'utente dicendo "Ehi,
[00:50:09] per favore, non fare quello". E quello
[00:50:11] che abbiamo visto è che viene scritta
[00:50:14] una regola che andrà ad essere ehm
[00:50:17] salvata nella nostra nella memoria, ok?
[00:50:19] Del nostro cloud.
[00:50:22] Ehm poi una volta fatto l'agente
[00:50:24] continua a lavorare finché la la
[00:50:26] sessione non termina. A questo punto la
[00:50:29] sessione poi ricomincerà, quindi la
[00:50:32] volta due, quello che verrà fatto sarà
[00:50:35] che questa nuova conoscenza viene
[00:50:37] caricata, quindi una volta che
[00:50:39] ricominciamo il nostro cloud, il nostro
[00:50:41] cloudmd non si cancella, no, ma rimarrà
[00:50:45] ehm aggiornato con le cose che abbiamo
[00:50:47] scritto. Il task verrà eseguito, ci
[00:50:51] saranno poi ulteriori connessioni e
[00:50:53] ulteriori regole scritte. Quindi quello
[00:50:55] che sostanzialmente stiamo facendo è
[00:50:58] andare a prendere il nostro piccolo
[00:50:59] cervellino e pian pianino lo facciamo
[00:51:02] diventare sempre più intelligente. Ora
[00:51:06] una domanda che può nascere spontanea è:
[00:51:08] "Hei, ma che differenza c'è tra avere un
[00:51:12] cloud.
[00:51:14] E avere tutte le informazioni messe nel
[00:51:18] prompt? Allora, fatemelo rimuovere e vi
[00:51:21] dirò ora che la differenza è
[00:51:23] sostanzialmente
[00:51:25] nessuna, cioè ogni volta noi potremmo
[00:51:28] letteralmente prendere tutto questo,
[00:51:30] metterlo qua dentro e eh lo
[00:51:33] e noi avremo appunto un prompt che
[00:51:35] funziona. Ovviamente se facessimo
[00:51:37] questo, noi non avremmo modo di avere
[00:51:39] questo eh questa correzione continua,
[00:51:41] quindi questi guardra rails che vengono
[00:51:43] adattati e non avremo modo nemmeno di
[00:51:45] avere questo continuous improvement del
[00:51:47] nostro prompt. che va a poi ehm diciamo
[00:51:51] migliorare il funzionamento complessivo.
[00:51:53] Questo non è l'unico motivo, ma per ora
[00:51:57] eh dato che non abbiamo ancora eh
[00:51:59] diciamo visto i vari tipi di prompt,
[00:52:02] teniamolo qui e adesso andiamo a capire
[00:52:05] invece e ad andare in qualche concetto
[00:52:07] un po' più avanzato. Quindi capiamo come
[00:52:10] dobbiamo promptare ora questi agenti,
[00:52:12] ora che abbiamo capito dove il prompt
[00:52:14] viene salvato e come si può migliorare
[00:52:16] continuamente. Ora, per chiudere questa
[00:52:18] breve base iniziale sulle basi di
[00:52:21] prompting, io vorrei chiedervi una cosa
[00:52:23] e cioè noi abbiamo detto che questo
[00:52:26] serve per controllare, diciamo, il
[00:52:29] nostro promptine
[00:52:33] e questo invece viene chiamato appunto
[00:52:35] il prompt nel gemini. MD. Ora mi chiedo,
[00:52:38] ma se io avessi una cosa del genere e
[00:52:42] quindi il gemini. MD ha quella a mi dice
[00:52:46] che un numero da 1 a 100 eh mi deve dare
[00:52:50] sempre 24 e invece in line dico numero
[00:52:54] da 1 a 100 devi darmi sempre eh 77.
[00:52:59] Ok? Quale dei due vince e perché?
[00:53:03] Ora io lo faccio andare e voglio che voi
[00:53:06] magari mi diciate che cosa ne pensate.
[00:53:10] Perfetto. Allora, ora gli chiederò
[00:53:15] "Hei, potresti per favore darmi un
[00:53:18] numero da 1 a 100?"
[00:53:21] Aspettiamo che ehm
[00:53:25] questo venga cambiato
[00:53:27] e vediamo che cosa succede. Benissimo,
[00:53:33] 77. Quindi abbiamo visto che il prompt
[00:53:36] che vince è questo qui. Che cosa vuol
[00:53:39] dire per noi e quanti prompt esistono?
[00:53:42] Bene, per rispondere in maniera
[00:53:44] abbastanza semplice ho voluto creare
[00:53:46] questa piccola immagine e per farvi dei
[00:53:48] vari livelli, immaginateveli come un
[00:53:51] cerchio concentrico e come una torta. E
[00:53:53] qui vi dico che il più specifico vince
[00:53:57] sempre. Che cosa vuol dire? Più siamo
[00:53:59] vicini al centro, più questo prompt
[00:54:02] andrà ad influire sull'output che voi
[00:54:04] avete rispetto a quello che c'è nel
[00:54:06] gemide. Quindi quanti prompt esistono?
[00:54:09] Beh, ne esistono un po' perché esistono
[00:54:11] i cosiddetti inline prompt che sono
[00:54:14] istruzioni specifiche che noi diamo al
[00:54:16] prompto. Dentro alla mia chat. Esistono
[00:54:20] le skills che sono delle metodologie per
[00:54:23] automatizzare i nostri workflow. E per
[00:54:26] farvi un esempio pratico, questa è una
[00:54:27] skill, no? Quindi noi nel mio social
[00:54:30] media manager abbiamo un sacco di skill,
[00:54:32] abbiamo che questa è come fare
[00:54:33] commitment per esempio a GitHub. E poi
[00:54:36] qui invece abbiamo dei delle linee di
[00:54:39] codice che dicono quando ti dico fai
[00:54:42] commit devi farlo sempre in questo modo.
[00:54:44] Ma poi cosa abbiamo? Abbiamo i nostri
[00:54:47] projectccla.
[00:54:48] Il filino che vi ho fatto vedere, ma poi
[00:54:51] oltre a quelli abbiamo il nostro
[00:54:54] globalc.md.
[00:54:55] Questo, per esempio, l'ho spiegato nel
[00:54:57] corso di Cloud Code che potete trovare
[00:54:58] in community. Ehm, c'ho ci ho speso 4
[00:55:01] ore, porto chiunque da eh novizio a ad
[00:55:04] esperto, ecco, per capirci. Quindi,
[00:55:06] ecco, questo è per dirvi che a seconda
[00:55:08] di dove andiamo a mettere queste regole,
[00:55:11] quindi nei vari DOT MD o nelle varie
[00:55:14] skill eccetera, abbiamo sempre la
[00:55:16] possibilità di eh sbagliare o
[00:55:19] direzionare l'AI, dipende a seconda di
[00:55:21] come lo utilizziamo, nella direzione
[00:55:23] corretta ehm se utilizziamo bene i
[00:55:25] nostri prumt e quindi se capiamo bene
[00:55:27] anche come questi sono organizzati e con
[00:55:30] che eh diciamo grado di ehm accuratezza
[00:55:34] vengono rispettati. e in che ordine.
[00:55:36] Parliamo ora di come riusciamo a
[00:55:38] scrivere prompt in maniera efficace per
[00:55:40] qualsiasi AI agent. Allora, questo è
[00:55:43] perché ne dobbiamo parlare, perché
[00:55:44] vogliamo evitare di aprire Cloud e
[00:55:48] cominciare subito a fare un prompt,
[00:55:52] come sappiamo, il tasso di errore e di
[00:55:55] eh progetti che risultano non riusciti
[00:55:59] se se abbiamo un approccio di questo
[00:56:01] tipo è abbastanza alto. Non so se è mai
[00:56:03] capitato di cominciare a fare qualcosa,
[00:56:05] usare plan mode, avere un
[00:56:07] promptilometrico, implementate, poi vi
[00:56:10] bloccate, eccetera eccetera eccetera.
[00:56:12] Ok? Quindi il nostro obiettivo è evitare
[00:56:14] questo. E per farlo dobbiamo introdurre
[00:56:18] un po' di tecniche di prompting. Allora,
[00:56:19] ve le introduco prima come concetto
[00:56:21] teorico e poi una alla volta andremo ad
[00:56:24] eseguirle in cloud code e vi faccio
[00:56:26] vedere in pratica in che cosa
[00:56:28] consistono. Allora, il primo ehm la
[00:56:31] prima tecnica, diciamo, che fatemela
[00:56:34] chiamare in questo modo che andiamo ad
[00:56:35] utilizzare è il cosiddetto back prompt
[00:56:38] engineering. Che cosa significa?
[00:56:39] significa fare zoom out, diciamo, o dal
[00:56:44] dal progetto, quindi non entrare subito
[00:56:46] a fare prompt, ma cercare di capire ad
[00:56:49] alto livello prima quali sono gli
[00:56:51] obiettivi di progetto e se questo
[00:56:53] progetto è inquadrato nella maniera
[00:56:55] corretta oppure no. Per farlo esistono
[00:56:58] due tecniche e andremo a vederle
[00:57:00] entrambe. La prima è quella chiama che
[00:57:02] viene chiamata stepback prompting e
[00:57:05] questa permette, come detto, di fare un
[00:57:08] cosiddetto passo indietro per
[00:57:11] identificare quali siano i principi alla
[00:57:14] base dell'obiettivo che vogliamo
[00:57:15] raggiungere prima ancora di andarlo a
[00:57:17] raggiungerlo o il reverse prompting, che
[00:57:20] invece è una tecnica che permette di far
[00:57:23] emergere quali sono le assunzioni e ci
[00:57:26] permette di porci delle domande di
[00:57:29] chiarimento prima. di poter iniziare
[00:57:31] questo.
[00:57:33] Che cosa vuol dire? Nello specifico
[00:57:35] cominciamo con lo step back prompting.
[00:57:38] Allora, vediamo come funziona. Allora,
[00:57:41] di qui diamo un compito specifico ad un
[00:57:45] AI. Allora, immaginiamo, allora, qui ho
[00:57:47] fatto c'è un esempio di una qui sequel,
[00:57:49] ma facciamo una cosa un po' più
[00:57:50] comprensibile e quindi per esempio
[00:57:53] ipotizziamo che il nostro processo di
[00:57:56] automazione per mandare email in
[00:57:59] automatico, quindi cold email campaign,
[00:58:02] quella che chiamiamo, ehm, sia si sia
[00:58:06] fallito. Ok? Quello che possiamo dirgli
[00:58:08] è correggi o ottimizza il mio processo.
[00:58:13] Ok? Quello che noi otterremo sarà una
[00:58:16] ottimizzazione di quello che di quello
[00:58:18] che è chiamiamo il sintomo, ma non la
[00:58:20] causa del fallimento. Quello che invece
[00:58:22] permette di fare la skill è quella di
[00:58:25] fare un passo indietro e chiederci qual
[00:58:27] è il principio generale, cioè cosa sono
[00:58:30] le cose che dobbiamo ottimizzare, perché
[00:58:32] dobbiamo ottimizzarle e come dobbiamo
[00:58:33] farle. Allora, per farvi vedere in modo
[00:58:35] pratico come funziona questa cosa qui,
[00:58:37] ehm, adesso io utilizzerò una serie di
[00:58:40] skill, insomma, che mi sono creato, però
[00:58:42] questo è il principio alla base delle
[00:58:43] mie skill, no? E quindi gli dirò adesso
[00:58:47] step
[00:58:49] back prompting e gli chiederò creami un
[00:58:53] bel sito web.
[00:58:56] Allora, questo non vuol dire nulla,
[00:58:59] giusto? Perché cosa vuol dire un bel
[00:59:02] sito web? Ed infatti vediamo che il
[00:59:05] modello, in questo caso il nostro
[00:59:07] agente, quando abbiamo un prompt così
[00:59:10] generico, che cosa farà? Bene, andrà a
[00:59:13] chiarire un po' qual è il principio di
[00:59:15] modo tale che noi possiamo rivederlo.
[00:59:18] Vediamo che dice. Un website è uno
[00:59:21] strumento con un uno scopo ben preciso.
[00:59:26] La domanda che ci dobbiamo fare, quindi,
[00:59:29] non è come dovrebbe essere a livello
[00:59:33] estetico, ma la vera domanda è che cosa
[00:59:38] dovrebbe fare a livello pratico,
[00:59:41] specialmente qual è la azione di
[00:59:44] conversione che un visitor, quindi
[00:59:47] qualcuno che visita il nostro sito
[00:59:49] dovrebbe fare. che cosa vuol dire in
[00:59:51] parole povere, cioè e e qui lo vedete
[00:59:55] sotto, chi terra nel tuo sito serve per
[00:59:59] far comprare traffico cold traffic da
[01:00:02] YouTube, quindi serve per comprare
[01:00:04] persone che arrivano dal traffico
[01:00:06] YouTube perché magari ho lasciato un
[01:00:07] link, oppure serve per avere autorità
[01:00:12] quando magari le tue connessioni
[01:00:14] LinkedIn vanno a vedere il sito e vanno
[01:00:15] a capire chi sei. serve per convertire
[01:00:19] un potenziale cliente a cui hai mandato
[01:00:22] un link per magari entrare in community,
[01:00:25] perché ogni audience ha bisogno di che
[01:00:27] cosa? Di un messaggio diverso. Quindi
[01:00:29] già qui capiamo come stiamo entrando in
[01:00:31] dettaglio della cosa per capire qual è
[01:00:34] lo scopo. Quindi a questo punto ci dice
[01:00:36] ok, capito a chi si rivolge, qual è
[01:00:41] l'azione che dobbiamo fare? Allora, qui
[01:00:43] è
[01:00:44] avere una call, entrare nella community
[01:00:47] avanguardia, fare subscription a
[01:00:49] YouTube, ehm o che cosa poi che entity,
[01:00:54] quindi per quale delle tue aziende in
[01:00:57] questo caso o ehm programmi è il la
[01:01:01] cosa? Cioè è per gente sei, quindi
[01:01:04] l'agenzia, è per Avanguardia Plus,
[01:01:06] quindi la community eh a pagamento
[01:01:10] e perché ovviamente qui ti dice avresti
[01:01:13] offerte diverse. E poi qual è il budget
[01:01:17] che tu hai per la manutenzione di
[01:01:18] questo? Quindi landing page statica
[01:01:22] oppure blog content che ha bisogno di
[01:01:25] continuamente nuovo contenuto
[01:01:27] e eccetera eccetera eccetera. Che cosa
[01:01:30] stiamo evitando? Stiamo evitando di
[01:01:32] costruire un generico sito multipagina e
[01:01:36] e multiportfolio
[01:01:37] con la solita cosa che sembra solo
[01:01:41] professionale ma non converte. Ok?
[01:01:44] Quindi vediamo che questo primo step
[01:01:47] serve proprio a definire quali sono i
[01:01:51] nostri goal nel momento in cui andiamo a
[01:01:54] chiedere qualcosa al nostro agente. Ora
[01:01:57] abbiamo ci chiede, ok, il nostro ICP,
[01:02:01] allora gli diciamo "Ehi, fammi un bel
[01:02:04] sito web per Avanguardia Plus, è la mia
[01:02:07] community a pagamento nella quale
[01:02:09] insegno a imprenditori e freelancer come
[01:02:11] utilizzare le AI e vendere agenti AI
[01:02:13] alle aziende o come implementarli". Ehm,
[01:02:16] deve questo sito deve far sì che le
[01:02:18] persone capiscano la il valore della
[01:02:20] community e che quindi poi acquistino
[01:02:22] magari il mio programma. eh sotto quale
[01:02:24] brand utilizza pure Avanguardia Plus.
[01:02:27] Perfetto. Ora gli diciamo però una volta
[01:02:30] che hai queste informazioni, per favore
[01:02:32] aspetta eh prima di procedere perché
[01:02:35] ovviamente non voglio eh che questo vada
[01:02:37] avanti come prompt e andiamo avanti. Ora
[01:02:39] quello che farà sarà fare una
[01:02:41] ricapitolazione, ecco, dove ci dice ok
[01:02:45] qual è il principio guida. Quindi
[01:02:47] abbiamo capito che il mio beautiful
[01:02:49] website, quindi il mio bellissimo ehm
[01:02:52] sito, non è un sito, ma è una sales
[01:02:56] page, quindi è una cosiddetta landing
[01:02:59] page che ha l'unico scopo di convertire
[01:03:00] e vendere.
[01:03:02] Bene, ora eh ci dice qual è la struttura
[01:03:05] che va utilizzata e quindi come
[01:03:07] ottimizzarla, quindi hero, problema,
[01:03:08] soluzione, cosa ottieni? proof, chi sono
[01:03:11] e pricing. Ora però abbiamo una cosa e
[01:03:15] cioè abbiamo capito qual è il goal, ok,
[01:03:18] di questo agente, però abbiamo ancora
[01:03:21] delle assunzioni che sono state fatte
[01:03:23] perché perché in questo momento noi
[01:03:25] abbiamo detto che il nostro deve essere
[01:03:27] una sales page, però non siamo ancora
[01:03:30] andati nel dettaglio per capire ok, ma
[01:03:33] che cosa vogliamo dentro, come deve
[01:03:34] essere, perché dal mio prompt super
[01:03:36] generico di voglio un bellissimo sito ho
[01:03:38] tolto come una cipolla il primo strato.
[01:03:42] ma ne mancano ancora dentro. Quindi, che
[01:03:45] cosa succederebbe ora? Che io ho dato un
[01:03:47] input, la gente pensa di avere capito,
[01:03:51] però magari non ha capito del tutto, o
[01:03:54] meglio, non gli ho dato le informazioni
[01:03:56] sufficienti per farlo. Quindi eh queste
[01:03:59] informazioni che sono state inventate,
[01:04:02] ok, non sono ancora ben definite, quindi
[01:04:07] che cosa facciamo? Beh, il secondo step
[01:04:09] che facciamo dopo aver definito il
[01:04:11] nostro goal e il nostro obiettivo che
[01:04:14] abbiamo definito facendo un passo
[01:04:15] indietro, ci chiediamo all'AI di
[01:04:18] aiutarci con una serie di domande che ci
[01:04:20] dovrebbero aiutare ad arrivare ad un
[01:04:23] output il più preciso possibile. Quindi,
[01:04:26] che cosa abbiamo? Beh, qui abbiamo
[01:04:29] reverse prompting, che è la skill che ho
[01:04:33] appena fatto su questo output. Ok?
[01:04:38] Che cosa fa Reverse Prompting? Bene,
[01:04:41] prima di procedere con il sito, Reverse
[01:04:43] Prompting, come detto, ci farà cinque
[01:04:46] domande,
[01:04:47] ok? E e ora le vedremo. E quindi questo
[01:04:51] permette di cominciare a togliere il
[01:04:52] secondo output o scusate, il secondo
[01:04:55] layer dalla cipolla che permette di
[01:04:58] prendere un eh diciamo un output e
[01:05:01] andare sempre più nel dettaglio. Allora,
[01:05:04] che cosa ci dice? Beh, e ora vediamo
[01:05:06] quante cose non abbiamo ancora detto.
[01:05:09] Allora, Q1, impatto massimo, dove punta
[01:05:14] la CTA, quindi la nostra call to action,
[01:05:16] quindi i nostri bottoni nel sito, che
[01:05:18] cosa ci stanno facendo? Punta a school
[01:05:21] direttamente o a una call con te? Beh,
[01:05:23] questo capite che è molto importante,
[01:05:25] no? Perché in questo momento noi abbiamo
[01:05:27] fatto un'ipotesi e cioè l'ipotesi che
[01:05:30] abbiamo detto è che eh noi avessimo
[01:05:33] questo bellissimo sito e nel sito quello
[01:05:37] che avevamo fatto l'ipotesi prima era
[01:05:40] che ci fosse questo bottone, ok? Quindi
[01:05:43] bottone e se la gente premeva questo
[01:05:45] bottone poi acquistava,
[01:05:48] però non è detto, giusto? Eh, perché?
[01:05:52] Perché in questo caso potremmo avere che
[01:05:54] se la gente preme il bottone, allora
[01:05:56] magari siccome magari avendo un servizio
[01:05:58] high ticket, eh magari ricevi una call
[01:06:01] diretta, no? E quindi questo è un primo
[01:06:04] layer di complicazione. Non abbiamo
[01:06:05] specificato. Lui avrebbe fatto delle
[01:06:07] ipotesi e queste ipotesi sarebbero state
[01:06:09] sbagliate. Poi hai testimonianze,
[01:06:12] risultati o numeri concreti da usare
[01:06:13] perché lui qui le ha messe. Però le
[01:06:16] abbiamo o non le abbiamo?
[01:06:19] Bene. Che cosa ha fatto? di nuovo ha
[01:06:21] fatto una media perché l'output di un
[01:06:23] agente è una media di quello che
[01:06:26] conosce.
[01:06:27] Perfetto. Poi tre, non abbiamo ancora
[01:06:30] detto, e questa può essere una domanda
[01:06:32] non rilevante per noi se non siamo
[01:06:34] tecnici, ma è un esempio di quante cose
[01:06:36] non abbiamo comunicato. Non abbiamo
[01:06:38] ancora detto qual è lo stack con cui
[01:06:40] deve costruire questo sito e quindi
[01:06:42] vogliamo un HTML o CSS, vogliamo un
[01:06:45] qualcosa di più tecnico, cosa vogliamo?
[01:06:48] Poi parte numero 4, qui noi abbiamo
[01:06:51] fatto pricing CTA finale, ma questa è
[01:06:53] un'assunzione. Se per esempio vendete
[01:06:56] servizi high ticket, ok, soprattutto nel
[01:07:00] B2C, quindi con consumatori, ipotizziamo
[01:07:03] che voi abbiate un coaching program
[01:07:05] avevo io, siccome il mio il mio ticket
[01:07:08] era €6.500 €500 a persona, eh, non non
[01:07:12] esiste persona che senza avere fatto una
[01:07:14] sales call avrebbe mai comprato un
[01:07:16] servizio del genere, no? Quindi in
[01:07:18] questo caso serviva sia avere la sales
[01:07:20] call che non avere il prezzo disponibile
[01:07:23] nel sito. E così tutte le persone che
[01:07:26] fanno servizio ai ticket e tutti i
[01:07:27] business, non troverete mai nessuno con
[01:07:29] un questo costa €50.000 compra perché
[01:07:33] perché se potessero farlo non avrebbero
[01:07:35] le sales call, giusto? L'obiettivo del
[01:07:37] del del rappresentante di vendita o del
[01:07:41] manager di vendita è quello proprio di
[01:07:43] convertire un potenziale cliente in un
[01:07:46] effettivo acquirente. Se la gente fosse
[01:07:48] già convinta basterebbe premere il
[01:07:50] bottone, non servirebbe il
[01:07:51] rappresentante di vendita, no? Quindi
[01:07:54] questo è un altro. Altra cosa che noi
[01:07:57] non abbiamo ancora definito è lo stile,
[01:07:59] che ora diciamo "Ah, sì, cavolo, è vero,
[01:08:01] però nel senso vedete quante cose non
[01:08:03] abbiamo detto" e questo è solo l'inizio,
[01:08:06] giusto?
[01:08:07] Quindi questo è per dirvi, queste sono
[01:08:09] tutte le cose che ehm contano prima di
[01:08:13] poter arrivare a a dire "Ok, eh siamo
[01:08:18] contenti con l'output". Quindi ora gli
[01:08:20] diremo come prima: "Ehi, per favore, eh
[01:08:23] decidi tu, eh perché questa è una demo,
[01:08:26] però ehm aspetta prima di procedere con
[01:08:30] l'esecuzione." Quindi ora quello che noi
[01:08:32] faremo è aspettare. [sbuffare] E allora
[01:08:35] voi in questo momento vi chiederete "Ok,
[01:08:37] perfetto, ora so ehm come fare
[01:08:41] perfettamente un agente perché ho queste
[01:08:44] questi due prompt iniziali e io so cosa
[01:08:48] devo cercare. È così?
[01:08:50] No, perché perché in questo momento noi
[01:08:54] che cosa abbiamo fatto? Noi abbiamo dato
[01:08:56] una serie di ehm di istruzioni, ok?
[01:09:00] Quindi abbiamo dato una [sbuffare] eh
[01:09:03] Ca, abbiamo dato uno stile,
[01:09:06] abbiamo dato i un chiamiamolo elemento
[01:09:11] 3, abbiamo dato un elemento 4, un 5, un
[01:09:14] 6, un 7, abbiamo fatto tutta una serie
[01:09:17] di step infiniti. Ok? Ma la domanda che
[01:09:21] ora ci poniamo è come fa la gente AI a
[01:09:25] capire che quello che ha prodotto,
[01:09:28] immaginiamo di dirgli "Va bene, vai ora
[01:09:31] vai e conquista il mondo e fammi vedere
[01:09:32] il sito". Come fa a capire che quello
[01:09:35] che ha prodotto va bene o no? E cioè
[01:09:38] detto diversamente, quali sono le nostre
[01:09:42] condizioni
[01:09:44] per
[01:09:45] il successo? che detto diversamente è
[01:09:49] come fa la gente a capire di avere
[01:09:51] finito la task e cioè detta diversamente
[01:09:55] qual è la definizione di successo.
[01:09:59] Questa è quella che non abbiamo ancora
[01:10:01] fatto perché perché esempio sciocco, se
[01:10:05] avessimo un sito dove la Heroction,
[01:10:09] quindi la prima parte e poi la parte
[01:10:11] dove eh mettiamo le foto della nostra
[01:10:14] agenzia o del nostro servizio e dopo la
[01:10:16] parte di prezzo, sono tutte collassate
[01:10:18] in una pagina e tutte una sopra l'altra,
[01:10:20] qui non abbiamo ancora detto alla gente
[01:10:22] questo sarebbe un output sbagliato,
[01:10:24] quindi non puoi considerarlo corretto e
[01:10:26] quindi devi continuare a migliorare fino
[01:10:28] a che non mi fai una pagina pulita e
[01:10:32] precisa, no? Quindi ora dobbiamo cercare
[01:10:36] qualcosa che ci aiuti a definire questa.
[01:10:39] Quindi noi dobbiamo cominciare a capire
[01:10:41] qual è la nostra definizione di
[01:10:43] successo. Allora, per farlo introduciamo
[01:10:47] un ulteriore concetto che è un prompt
[01:10:50] contract. Quindi, che cosa vuol dire?
[01:10:53] Allora, noi questo prompt contracts
[01:10:56] possiamo idealmente pensarlo come un
[01:11:00] equivalente, poi non è così perché
[01:11:03] adesso vediamo perché della plan mode
[01:11:06] che abbiamo dentro a cloud. Ok? Però
[01:11:12] qual è il vantaggio di utilizzare questi
[01:11:16] rispetto a una plan mode o meglio questi
[01:11:18] magari dentro ad una plan mode? è che
[01:11:21] ora noi abbiamo ancora un compito vago
[01:11:25] con un perimetro definito. Quindi quello
[01:11:28] che vogliamo introdurre ora è dobbiamo
[01:11:30] chiarire qual è la tipologia di
[01:11:33] obiettivo che noi vogliamo, ok? Quali
[01:11:36] sono i vincoli che noi dobbiamo
[01:11:38] introdurre al nostro sistema, che
[01:11:40] tipologia di formato dobbiamo avere e
[01:11:43] cosa consideriamo come fallimento. E
[01:11:47] quindi cosa vuol dire? che la gente non
[01:11:48] può smettere di lavorare fino a che non
[01:11:50] abbiamo introdotto questo fallimento.
[01:11:53] E allora qui entriamo nei dettagli
[01:11:55] perché un obiettivo deve essere qualcosa
[01:11:58] di misurabile. Quindi, esempio, eh il
[01:12:03] padding o lo spazio bianco che c'è tra
[01:12:06] questo e questo nel mio sito deve essere
[01:12:09] un massimo di 10 pixel, altrimenti non
[01:12:12] sono contento. Oppure quando mando un
[01:12:16] contratto in automatico al mio cliente,
[01:12:19] devo poterglielo mandare senza dover
[01:12:21] toccare niente. Cioè, da quando finisce
[01:12:24] la chiamata con il mio cliente a quando
[01:12:26] gli invio il contratto, io non devo
[01:12:28] premere più nessun bottone. Questo è il
[01:12:30] mio obiettivo.
[01:12:32] Per esempio, la condizione di fallimento
[01:12:34] a quel punto sarebbe mi stai chiedendo
[01:12:37] conferma di qualche informazione oppure
[01:12:40] "Mi stai dicendo o mi stai dando
[01:12:43] consenso per utilizzare, non lo so,
[01:12:46] degli step intermedi. Mi stai facendo
[01:12:48] delle domande perché non hai capito"?
[01:12:50] Ok? Questo è un obiettivo e una eh
[01:12:54] condizione di ehm di fallimento. Poi che
[01:12:57] cosa diciamo? Beh, torniamo nell'esempio
[01:12:59] del contratto, magari sto sviluppando un
[01:13:01] sistema e gli dico che la condizione di
[01:13:05] di vincolo che ha è che io ho un massimo
[01:13:08] budget di, per esempio, €5 quando faccio
[01:13:11] questa tipologia di di sviluppo. E
[01:13:15] quindi anche qui ehm diciamo è un
[01:13:18] vincolo che dobbiamo introdurre perché i
[01:13:20] vincoli permettono al nostro al nostro
[01:13:23] sistema di rimanere dentro ai
[01:13:25] boundaries, no? Quindi ipotizziamo ora
[01:13:27] di avere un un tunnel che rappresentano
[01:13:31] i miei vincoli. Se io ho un prompt che
[01:13:34] ha questa apertura qui, ok? Io ehm
[01:13:38] ovviamente senza vincoli avrei il prompt
[01:13:41] che va dove vuole. Con i vincoli
[01:13:44] sostanzialmente gli sta dicendo, "Guarda
[01:13:46] che l'unica zona in cui ti è concesso
[01:13:48] agire è questa qua dentro
[01:13:51] e il formato, quindi una forma esatta
[01:13:53] dell'output. Quindi esempio di nuovo con
[01:13:55] il contratto al cliente. Voglio che il
[01:13:58] contratto abbia esattamente il mio logo,
[01:14:01] i miei colori, le mie cose e magari il
[01:14:04] fallimento è un logo diverso, un colore
[01:14:06] che non sia in target con quello che
[01:14:08] voglio, eccetera eccetera. Output
[01:14:11] preciso, qualità professionale.
[01:14:14] Bene,
[01:14:15] ora che cosa facciamo? diciamo
[01:14:18] introduciamo una skill e questa è per
[01:14:21] esempio come l'ho fatta io.
[01:14:23] Utilizziamo prompt contracts sull'output
[01:14:27] appena prodotto.
[01:14:31] Che cosa fa questa skill? Adesso andiamo
[01:14:34] a vedere che cosa ci fa. E questo è la
[01:14:37] divisione che farà sempre.
[01:14:39] &gt;&gt; [sbuffare]
[01:14:39] &gt;&gt; Allora, comincerà a creare una ehm un un
[01:14:44] contratto, immaginatevi un contratto che
[01:14:47] firmate col sangue, col vostro AI, e ci
[01:14:50] dice: "Ok, il contratto è c'è una
[01:14:52] singola pagina per Avanguardia Plus che
[01:14:55] porta il visitatore da chi è questo a
[01:14:59] click su CTA e School". Benissimo, deve
[01:15:02] caricare in meno di 2 secondi, essere
[01:15:04] mobile first e avere un flow visivo che
[01:15:07] guida lo scroll senza distrazioni.
[01:15:10] Allora, il file è un singolo HTML+ CSS.
[01:15:14] Perfetto.
[01:15:15] Dark mode palette con scura con ehm un
[01:15:21] accento vivace. Font da Google Font,
[01:15:24] massimo due immagini solo place
[01:15:26] placeholder o icone inline, eh che
[01:15:31] quindi sono le icone che vedete. Niente
[01:15:33] asset esterni da caricare.
[01:15:36] Sezioni obbligate in questo ordine Kiro
[01:15:39] problema soluzione. Cosa ottieni? Proof
[01:15:41] chi sono pricing CTA finale. Vedete
[01:15:45] questo vuol dire se c'è un ordine
[01:15:46] diverso non puoi considerarla come
[01:15:49] finita. CTA punta un URL di school,
[01:15:52] placeholder per ora, testo completamente
[01:15:54] in italiano, pricing visibile con
[01:15:56] breakdown. In questo caso abbiamo fatto
[01:15:58] la cosa della demo, no? Poi formato, un
[01:16:02] certo stile, deve essere responsive,
[01:16:05] deve essere facile quando facciamo
[01:16:07] scrolling al allo scroll, dobbiamo avere
[01:16:10] animazioni leggere, non dobbiamo avere
[01:16:11] file separati e via dicendo.
[01:16:15] Fallimento non è responsive. eh la CTA,
[01:16:18] quindi il nostro pulsante, non è
[01:16:20] visibile. Abbiamo più di un file
[01:16:21] generato al posto che uno solo. Abbiamo
[01:16:24] dipendenze esterne da font che non sono
[01:16:26] Google. Il testo è in inglese o abbiamo
[01:16:28] inglesismi dentro. Manca una delle sette
[01:16:31] sezioni e vedete voi, no? Ora non ve le
[01:16:34] leggo tutte, ma avete capito il
[01:16:35] concetto. Quindi, detto questo, abbiamo
[01:16:41] ora un prompt che è completo, ma è
[01:16:44] completo al 95%.
[01:16:48] Perché noi ora abbiamo una serie di cose
[01:16:52] che ehm il nostro prompt. Ora capite
[01:16:57] bene dal "Voglio un sito bellissimo a
[01:17:00] tutto quello che gli abbiamo detto e
[01:17:02] quanto più completo ora sia il prompt
[01:17:05] che dobbiamo fare." Giusto per capirci,
[01:17:06] dovreste spendere il 90% del tempo a
[01:17:09] fare un bel prompt e dopo il resto ad
[01:17:12] utilizzarlo. Anche se molta gente oggi
[01:17:14] apre Cloud Code e comincia semplicemente
[01:17:16] a premere e dice "Ok, perfetto, so fare
[01:17:19] automazioni". Però manca ancora
[01:17:21] qualcosa. Che cosa manca? che è il
[01:17:24] nostro ultimo tassellino. Manca il
[01:17:27] premortem. Che cos'è? Allora, il
[01:17:29] premortem è: "Immaginatevi di essere ad
[01:17:32] oggi e immaginatevi che abbiamo un
[01:17:35] momento futuro in cui il nostro progetto
[01:17:38] può eventualmente fallire. Ok? Quindi
[01:17:43] ora il
[01:17:45] post mortem, diciamo, quindi una volta
[01:17:48] che il il sito è giù, per esempio, ehm,
[01:17:52] questo sarebbe un disastro, mentre il
[01:17:56] premortem trova gli stessi problemi
[01:17:58] prima che ci costino qualcosa. Vi faccio
[01:18:01] un esempio pratico. Immaginiamo di avere
[01:18:04] un Voice AI agent e l'abbiamo fatto con
[01:18:07] cloud, tutto perfetto. utilizza un
[01:18:09] modello di Open AI per, come diciamo
[01:18:14] lloro,
[01:18:16] ma se Open AI va giù come funziona
[01:18:20] questo agente? La risposta è non
[01:18:22] funziona. E cosa vuol dire? rischiamo di
[01:18:25] perdere un sacco di soldi e denaro e
[01:18:27] anche clienti. Altro esempio, se per
[01:18:30] caso sto mandando un contratto ad un
[01:18:32] cliente e ho che tutto viene fatto con
[01:18:36] cloud, perché tutti i miei progetti sono
[01:18:37] in cloud, cosa succede se cloud va giù?
[01:18:40] L'azienda si blocca. Quindi questo è un
[01:18:42] esempio sciocco per ehm diciamo farvi
[01:18:46] capire che adesso non abbiamo ancora
[01:18:49] introdotto tutte queste cose che sono i
[01:18:51] premortem
[01:18:53] prima che tutto fallisca. Ma voglio che
[01:18:55] concettualmente la pensiate così.
[01:18:57] Immaginatevi di essere un raccoglitore e
[01:19:02] abbiamo un eh una monocultura. Ok? Noi
[01:19:07] per ora abbiamo fatto che cosa? Abbiamo
[01:19:10] preso qua e abbiamo detto, "Guarda,
[01:19:12] questo progetto è fenomenale perché
[01:19:16] abbiamo fatto tutto questo, però quello
[01:19:20] che il prompt è attenzione perché se
[01:19:24] arriva un incendio, ok, e spero vi
[01:19:27] piaccia la mia fiammetta e l'incendio ti
[01:19:30] brucia tutto in un colpo solo, se non
[01:19:33] pianifichi bene il tuo progetto e non
[01:19:35] pianifichi bene la tua azienda e tutte
[01:19:37] queste cose qui.
[01:19:39] Beh, questo può eh spaccare tutto e a
[01:19:42] quel punto sei completamente caput e voi
[01:19:44] sapete che ingeniamo il il modello
[01:19:48] svirgola e mandiamo il
[01:19:51] contratto sbagliato o eh i modelli vanno
[01:19:54] giù, l'azienda si ferma, noi non è che
[01:19:57] stiamo perdendo il non lo so,
[01:19:59] immaginiamo che va giù per l'1% del
[01:20:01] tempo, ok? in una settimana noi 1% di
[01:20:05] down time, quindi con i sistemi non
[01:20:08] funzionano e questa è solo un esempio
[01:20:10] perché è visivamente chiaro, non sempre
[01:20:13] corrisponde all'1% della perdita del
[01:20:15] revenue, ma nel caso in cui voi abbiate
[01:20:17] che il cliente vi arriva proprio in quel
[01:20:19] momento, qui voi avete perso il 100% del
[01:20:22] revenue più, tra l'altro danno
[01:20:24] reputazionale perché vi dicono "Ah,
[01:20:26] Madonna, magari siete proprio voi
[01:20:27] l'agenzia AI, vi dico non funziona
[01:20:29] niente di quello che fai". Ok? Quindi
[01:20:31] quello che dobbiamo fare è capire se c'è
[01:20:34] qualcosa che possiamo fare in anticipo.
[01:20:37] Ok? Bene. Quindi andiamo qui e quindi
[01:20:42] qui possiamo utilizzare di nuovo, io
[01:20:44] sono skill che ho fatto, ma voi potete
[01:20:47] utilizzarle ehm e potete farvele come
[01:20:50] volete. L'importante è che ci siano e
[01:20:52] che voi abbiate questa struttura, ok?
[01:20:55] sull'ultimo output gli diciamo bene,
[01:20:59] fammi un premortem. Io queste le ho
[01:21:01] fatte secondo le mie preferenze, ehm,
[01:21:04] però nel senso voi siete liberissimi di
[01:21:08] andare cercare online, chiedere a Cloud
[01:21:10] di cercare online, fare tutte queste
[01:21:12] cose qui, no? Ehm, però ecco qui il task
[01:21:16] è completato, è considerato un
[01:21:18] fallimento. Ecco le tre cause più cause
[01:21:20] più probabili. copy generica da
[01:21:23] template. Quindi ancora qui non abbiamo
[01:21:26] eh come dire definito tutte queste cose,
[01:21:29] no? Vedete quanta complicazione c'è
[01:21:32] quando facciamo un progetto e quanto
[01:21:34] magari lontani siamo dall'utilizzare
[01:21:37] questi agenti I bene nel caso in cui
[01:21:39] stiamo eh troppo fuori, no? E e premiamo
[01:21:42] i bottoni. Quindi il testo suona come
[01:21:45] ogni altra pagina. Ai imparo ad usare
[01:21:47] l'AI, eh. Quindi il visitatore chiude in
[01:21:50] 2 secondi perché non sente la voce di
[01:21:51] Giovanni. Eh, mitigation, scrivere il
[01:21:54] copy nello stile di Giovanni, diretto,
[01:21:56] zero pratico, eccetera. Bene. Dark mode
[01:22:00] illeggibile, quindi non c'è
[01:22:02] sufficientemente contrasto. Benissimo.
[01:22:04] Poi muro di testo senza respiro visivo.
[01:22:07] Otto sezioni in un singolo file senza
[01:22:10] immagini. Rischio più alto è il numero
[01:22:12] uno. È chiaramente il rischio più alto,
[01:22:14] no, che c'è quando abbiamo il nostro AI
[01:22:15] slop. Quindi, di nuovo, qui non ho dato
[01:22:20] un prompt di qualità all'inizio, però
[01:22:22] vedete che con un piano e che ritengo
[01:22:27] ancora di basso livello, siamo riusciti
[01:22:30] però con quattro prompto.
[01:22:33] sicuramente è molto meglio di prima
[01:22:34] perché perché abbiamo definito un sacco
[01:22:37] di cose e ora semplicemente magari dopo
[01:22:40] che voi vi siete fatti la vostra skill
[01:22:42] andrete ad ehm a a fare questa tipologia
[01:22:46] di processo in scala, vedete come il
[01:22:49] vostro output può migliorare eh molto
[01:22:51] molto velocemente. Qui ovviamente
[01:22:53] abbiamo introdotto delle ulteriori eh
[01:22:56] metodologie di chiamiamolo fallimento e
[01:23:00] eh possiamo aggiornare anche il nostro
[01:23:03] prompt contract. Bene, passiamo quindi
[01:23:05] ora a concetti un po' più complicati che
[01:23:10] ehm voglio spiegarvi bene però quando
[01:23:12] andiamo ad utilizzarli e perché quello
[01:23:13] che voglio introdurvi è l'agent polling.
[01:23:16] Allora, questo è un framework che serve
[01:23:18] nel momento in cui facciamo ehm
[01:23:20] decisioni strategiche o quando stiamo
[01:23:23] facendo ricerche di qualsiasi tipo che
[01:23:26] richiedano ehm il eh l'intervento di più
[01:23:32] di una mente. Ok? mettiamola così. Ehm,
[01:23:35] come funziona? funzione che abbiamo in
[01:23:37] input una domanda, quindi ehm abbiamo
[01:23:41] una ricerca e quello che facciamo è
[01:23:45] spawnare, che significa creare, cinque
[01:23:48] agenti che sono tra di loro
[01:23:51] indipendenti. Questi cinque agenti
[01:23:53] avranno ognuno una prospettiva diversa
[01:23:57] sulla decisione strategica che eh
[01:24:01] dobbiamo andare ad eh ad affrontare. E
[01:24:04] che cosa succede? ognuno di loro avrà
[01:24:08] quindi alla fine, diciamo, della loro eh
[01:24:11] della loro ricerca avrà un piccolo
[01:24:14] filino, ok? nel quale ognuno di loro
[01:24:17] andrà a raccogliere tutte le
[01:24:20] informazioni che hanno trovato. Allora,
[01:24:23] immaginiamo e dopo lo faremo a livello
[01:24:25] pratico, di avere che ehm vogliamo fare
[01:24:29] una ricerca di marketing e vogliamo
[01:24:31] mandare un report a, non lo so, un
[01:24:33] influencer o uno youtuber tipo me su
[01:24:37] come puoi arrivare il più velocemente
[01:24:39] possibile a 100.000 follower quest'anno
[01:24:43] su YouTube. Ok, quindi questa sarà il
[01:24:45] nostro output.
[01:24:47] Quello che vogliamo fare è avere magari
[01:24:50] una un agente che diventa l'agente, non
[01:24:52] lo so, il quello più conservativo,
[01:24:55] l'altro è l'ottimista, l'altro è il
[01:24:56] cinico. Quindi abbiamo delle prospettive
[01:24:59] diverse. Qui a un certo punto, finito
[01:25:02] questo, abbiamo un report che viene
[01:25:05] definito report di consenso nel quale
[01:25:10] sono raccolti tutte le
[01:25:14] opinioni e sono elencate dalla più alla
[01:25:18] meno probabile. Quindi questo è quello
[01:25:20] che stiamo facendo. qual è il concetto
[01:25:23] di di funzionamento di questa di questa
[01:25:27] metodologia di modo tale che voi
[01:25:29] possiate magari anche ricrearvela.
[01:25:33] ipotizziamo di avere un agente.
[01:25:37] Quindi, ho il mio agente numero un. Se
[01:25:41] io guardo il mio agente numero uno, il
[01:25:43] mio agente numero uno mi troverà tre
[01:25:45] risposte. Ok? Allora, io la richiamerò
[01:25:49] la risposta A, la risposta B e la mia
[01:25:52] risposta C. Poi ho la gente 2, poi ho la
[01:25:57] gente 3, poi ho la gente 4 e poi ho la
[01:26:00] gente 5. Allora, 2
[01:26:04] 3
[01:26:06] 4 e 5. Ok. Allora, l'agente 2 magari mi
[01:26:11] trova B, C e D.
[01:26:15] L'agente 3 mi trova A, B ed. L'agente 4
[01:26:22] mi trova B, C e D. E l'agente 5 mi trova
[01:26:27] A, D e F. Quindi, che cosa succede?
[01:26:33] Succede che ora ho c delle delle
[01:26:36] risposte, giusto? e ne ho messi cinque,
[01:26:38] per esempio, solo perché ci viene più
[01:26:40] comodo.
[01:26:43] E ogni risposta ha un ehm coefficiente
[01:26:48] eh o chiamiamolo tale, in realtà ha un
[01:26:50] termine un po' diverso, ma lasciamolo
[01:26:52] coefficiente. Ed è un coefficiente che
[01:26:54] ti dice quante volte una risposta è
[01:26:56] stata presa. Quindi nel caso della a
[01:26:59] abbiamo che tre agenti diversi, anzi
[01:27:01] cinque agenti diversi, su cinque agenti
[01:27:03] questa è stata eh diciamo presa o o
[01:27:06] ripetuta tre volte, quindi la soluzione
[01:27:08] A è la più probabile. La soluzione B
[01:27:12] invece è stata ripetuta quattro volte,
[01:27:14] quindi ora abbiamo un nuovo vincitore.
[01:27:17] La soluzione C è stata ripetuta 1 2 eh
[01:27:21] tre volte.
[01:27:24] La soluzione D è stata ripetuta 1 2 e 3
[01:27:30] volte. La soluzione E, come potete ben
[01:27:33] vedere, e la soluzione F sono state ehm
[01:27:38] ripetute solamente una volta. Allora,
[01:27:42] ora domanda.
[01:27:45] Qual è la soluzione migliore?
[01:27:47] Attenzione, perché?
[01:27:50] Perché saremo tentati di dire la B, ok?
[01:27:54] E la B in una distribuzione,
[01:27:57] ok? Quindi se non voglio fare un corso
[01:28:00] di matematica, ma se questa è la vostra
[01:28:03] eh distribuzione, ok? Il valore più alto
[01:28:07] tende ad essere il più probabile.
[01:28:12] Vuol dire che è il più giusto? Non
[01:28:14] necessariamente perché perché magari
[01:28:17] troviamo che la strategia per crescere
[01:28:21] su YouTube a 100.000 follower quest'anno
[01:28:25] magari è un outlier e ce l'ho qui, no? E
[01:28:30] quindi quello che questa ci permette di
[01:28:32] fare è che ci permette di andare a
[01:28:35] leggere il nostro dov'è report di
[01:28:38] consenso che è questo. Ok, quindi qui
[01:28:41] avremo il nostro report.
[01:28:44] di consenso
[01:28:48] e ci permette
[01:28:50] di andare a capire qual è la migliore la
[01:28:55] migliore soluzione se noi ci mettiamo
[01:28:57] anche il nostro giudizio. Quindi, per
[01:28:59] fare un ulteriore paragone, quello che
[01:29:02] abbiamo fatto è stato dividere il nostro
[01:29:06] il nostro insieme di soluzioni possibili
[01:29:09] in una serie di soluzioni che adesso ne
[01:29:12] farò solo un paio. Abbiamo che magari
[01:29:15] questa occupa 4 su x, facciamo il 30%,
[01:29:19] adesso sarà molto di più, ma lasciamo
[01:29:20] perdere. Poi anche questa invece sono
[01:29:23] tre soluzioni. Poi ho il colore blu che
[01:29:25] sono magari altre tre soluzioni e poi ho
[01:29:28] i due neri che sono magari piccolini,
[01:29:30] no? Quindi ehm scusate, magari questa è
[01:29:32] una soluzione. Quindi, che cosa vuol
[01:29:34] dire? Vuol dire che questi agenti
[01:29:37] permettono, diciamo, in un in un
[01:29:40] intervallo di soluzioni, quindi nel
[01:29:41] nostro cerchio, di identificare quante
[01:29:44] più fette possibili. Questo perché?
[01:29:47] Perché anche se in media magari la gente
[01:29:51] singolo è magari mediamente
[01:29:54] intelligente, ok? Quindi ipotizziamo che
[01:29:57] abbia un Q di 50 e l'uomo migliore al
[01:30:02] mondo ha un Qi di 60, ok? un numero
[01:30:06] sufficientemente alto di persone con un
[01:30:09] QID di 50 pensando ad una stessa cosa,
[01:30:12] eventualmente anche per botta di
[01:30:14] fortuna, arriveranno alla soluzione
[01:30:17] pensata dal QUI di 60, però come ci
[01:30:20] arrivano molto più velocemente perché eh
[01:30:23] continuano a pensare tutti in maniera
[01:30:25] indipendente. Quindi questo permette a
[01:30:28] noi di identificare non solo la
[01:30:29] soluzione più probabile per risolvere il
[01:30:31] nostro problema, ma anche gli outlier.
[01:30:33] Bene, andiamo a vedere come funziona. E
[01:30:36] allora facciamo agent polling
[01:30:41] e gli diciamo:
[01:30:44] "Hei, vorrei capire, dato il mio profilo
[01:30:48] e dato il mio canale YouTube, qual è la
[01:30:50] soluzione migliore che io posso
[01:30:53] implementare quest'anno per raggiungere
[01:30:55] 100.000 ehm subscribers su YouTube. Puoi
[01:31:00] aiutarmi?". Allora, qui mi ha detto che
[01:31:03] in questo caso ha deciso che mi servono
[01:31:06] 10 agenti indipendenti
[01:31:08] per la mia YouTube Strategy, ok? Quindi
[01:31:12] 10 agenti in parallelo con tutti lenti
[01:31:15] diverse. Io per fare questa task sto
[01:31:17] spendendo ora cento,
[01:31:22] quindi analyze following, qualsiasi cosa
[01:31:26] lui voglia. Poi abbiamo quindi il
[01:31:29] neutrale. Poi abbiamo il risk adverse,
[01:31:32] quindi quello che non vuole rischiare,
[01:31:34] abbiamo quello che ha solo orientato ad
[01:31:37] una crescita, no? E se li premiamo
[01:31:39] possiamo anche andare a vedere che cosa
[01:31:42] hanno questi al loro interno, ok? E
[01:31:44] quindi vediamo che la migliore strategia
[01:31:47] per un solo YouTube creator per andare
[01:31:51] da 2700 a eh 10.000. Ok? Allora, qui poi
[01:31:57] vediamo che abbiamo questi agenti e ora
[01:31:59] andranno tutti in parallelo, ognuno da
[01:32:02] un angolo diverso. Ehm, e quindi qui poi
[01:32:06] avremo avremo delle strategie delle
[01:32:09] strategie diverse. Ok, vi faccio vedere
[01:32:11] poi il risultato di tutti questi e
[01:32:14] quindi qui poi avremo non lo so, fai un
[01:32:16] sacco di short più eh collaborazioni
[01:32:19] mensili oppure eh eh la domanda è vuoi
[01:32:25] questo o hai un revenue goal? Quindi,
[01:32:27] per esempio, hai perché 100.000
[01:32:30] subscriber perché quello hai un goal per
[01:32:33] quanto riguarda la crescita economica o
[01:32:35] vuoi semplicemente una base di utenti?
[01:32:39] Poi un agente furbo mi direbbe: "Ok, ma
[01:32:43] vuoi 100.000 subscriber in target o non
[01:32:45] in target?" E quindi poi questo è il
[01:32:48] motivo per cui noi vogliamo avere un
[01:32:51] certo livello di sofisticazione anche a
[01:32:53] livello di pensiero, perché come vedete
[01:32:55] possiamo fare outsourcing del pensiero
[01:32:58] con questi agenti AI, ma non possiamo eh
[01:33:01] a fare outsourcing della nostra
[01:33:02] comprensione, quindi, comunque, il
[01:33:05] nostro input diventa necessario nel
[01:33:07] momento in cui poi andiamo a modellare
[01:33:09] quello che vogliamo essere l'output di
[01:33:10] tutto questo.
[01:33:12] Bene, ora loro staranno facendo un
[01:33:15] report. E una volta che il report è
[01:33:17] fatto, ve lo faccio vedere. E questo è
[01:33:20] il report finito. Quindi qui ci dicono
[01:33:23] che ok, da 100 arrivare a 100.000
[01:33:25] follower è un o subscriber è un
[01:33:28] moonshot. La matematica richiede questi
[01:33:32] follower per settimana che non sembra
[01:33:34] possibile. Abbiamo tre agreement point.
[01:33:37] Allora, interesting split. Qua ci dice
[01:33:40] che l'unico modo che abbiamo o meglio
[01:33:43] quello che hanno, quello che credono, è
[01:33:45] avere un unico video che esploda e
[01:33:48] quello è il modo migliore per arrivare
[01:33:49] ai 100.000 subscribers. se fosse quello
[01:33:53] che ehm volessi fare perché sto cercando
[01:33:56] viralità, potrebbe essere una possibile
[01:34:00] soluzione. Ehm, quindi le l'engineer
[01:34:03] numero 4 dice proof of income video,
[01:34:06] quindi dire "Ok, ho guadagnato x in 30
[01:34:10] giorni utilizzando solo AI agent e poi
[01:34:12] qui avremo ehm il full report, ok? per
[01:34:16] capirci se volessimo premerlo. Bene, ora
[01:34:20] abbiamo una serie di idee e abbiamo
[01:34:22] detto che possiamo metterci il nostro
[01:34:23] pensiero critico, ma se volessimo
[01:34:25] ulteriormente avere un altro un'altra
[01:34:28] campana, cosa potremmo fare? Beh,
[01:34:31] potremmo andare in quelli che vengono
[01:34:32] chiamati agentes.
[01:34:34] Allora, questi debates sono
[01:34:36] sostanzialmente due agenti che
[01:34:38] cominciano a disquisire su una tematica
[01:34:40] con opinioni diverse, ok? Quindi questo
[01:34:42] è l'agente numero uno, questo è l'agente
[01:34:45] numero due, potremmo averne anche molti
[01:34:47] di più, eh, potremmo averne quattro,
[01:34:48] cinque, quello che volete. E ad ogni
[01:34:51] round, come vedete dalle frecce, lo
[01:34:54] scopo è che questi agenti che partono da
[01:34:55] idee completamente diverse, al posto che
[01:34:57] stare orizzontali e quindi non
[01:35:00] convergere mai a quella che è la
[01:35:02] soluzione, chiamiamola migliore,
[01:35:03] eventualmente convergono
[01:35:06] verso una soluzione comune.
[01:35:08] Immaginatevela così. Allora,
[01:35:10] immaginatevi di trovare un pezzo di
[01:35:12] diamante che inizialmente è questo
[01:35:14] cerchio. Poi i due agenti cominciano a
[01:35:17] discutere e cominciano a raffinare
[01:35:19] questo pezzo di diamante, quindi
[01:35:20] comincia a diventare un po' sgrezzato.
[01:35:23] Poi lo raffinano ulteriormente e allora
[01:35:26] cominciamo a vedere la prima forma del
[01:35:28] diamante che magari appare e poi
[01:35:31] continuano a disquisire fino a che poi
[01:35:34] non appare la forma finale del diamante,
[01:35:37] che è quella che noi chiamiamo
[01:35:38] convergenza.
[01:35:40] e che ci dà eh l'idea migliore, ok? o
[01:35:46] meglio, l'idea migliore è l'idea
[01:35:47] raffinata da questi due. Ehm, quindi,
[01:35:51] nel caso in cui volessimo avere anche un
[01:35:54] ulteriore parere nel quale di nuovo ogni
[01:35:57] agente discute ma in maniera separata,
[01:35:59] quindi prima facevano ricerche separate,
[01:36:02] [suono gutturale] ora hanno punti
[01:36:04] diversi su magari la stessa idea per
[01:36:06] smontarla o per raffinarla, potremmo
[01:36:08] utilizzare questo questa tipologia di
[01:36:11] approccio.
[01:36:14] Qual è il il pro e il contro? Che il
[01:36:17] sostenitore, in questo caso sono due,
[01:36:19] troverà ogni idea che o ogni ragione per
[01:36:21] sostenere un'idea, il critico per
[01:36:25] buttarla giù, per capirci. Allora,
[01:36:27] quindi se io andassi qui e gli direi "He
[01:36:31] usa eh agent
[01:36:34] debates
[01:36:36] per capire la migliore".
[01:36:40] Ora lui in automatico andrebbe a capire
[01:36:44] quanti agenti gli servono, ok, per
[01:36:47] produrre queste ehm quindi per per
[01:36:50] riuscire ad arrivare a generazione del
[01:36:53] nostro diamante ed in base a quanti
[01:36:55] agenti gli servono, poi sarà esattamente
[01:36:57] quello che andrà a fare qui quando li
[01:37:00] spawnerà. Quindi in questo caso gli
[01:37:02] servono tre agenti e tre round vuole
[01:37:05] fare. Quindi anche qui è un processo pam
[01:37:09] e eh in questo caso vediamo che sta
[01:37:13] creando, diciamo, una stanza, ok? Quindi
[01:37:16] questi agenti eh dibattono, però
[01:37:19] immaginatevi che questo sia il vostro
[01:37:23] progetto e quello che la skill fa è
[01:37:27] dire, ok, o meglio la mia, poi vedete
[01:37:29] voi come volete farla la vostra, ma è
[01:37:31] dire "Ok, vi lascio questa casetta qui e
[01:37:35] quindi voi andate tutti e tre qua
[01:37:37] dentro. Ehm, qua dentro andate a
[01:37:39] discutere. Una volta che avete il report
[01:37:41] di quello che è l'idea migliore,
[01:37:44] sentitevi pure libero di mandarmelo qui
[01:37:46] e quindi qui nel mio contesto principale
[01:37:49] vedrò qual è l'idea migliore. Quindi,
[01:37:51] come sentite, ora abbiamo
[01:37:54] il dibattito, quindi Volume Machine,
[01:37:57] breakout engineer, collab strategist,
[01:37:59] quindi le tre che andrà a guardare sono
[01:38:02] fare il più volume possibile, il il
[01:38:05] faccio un unico video che esplode o
[01:38:07] cerco collaborazioni.
[01:38:09] Adesso qui avremo che i round vengono
[01:38:12] lanciati. Una volta che questo viene
[01:38:14] lanciato avremo gli agenti che
[01:38:17] rientreranno di nuovo in questo processo
[01:38:19] di continua raffinazione e quindi
[01:38:22] passeremo da questo a questo a questo a
[01:38:26] questo e poi ogni volta arriveremo allo
[01:38:28] stadio finale in cui questo diamante
[01:38:31] viene appunto raffinato.
[01:38:33] Ovviamente avrà avremo che cosa? avremo
[01:38:36] il contesto di quella che sono le
[01:38:38] conversazioni precedenti più avremo
[01:38:40] tutto quanto quello che è stato discusso
[01:38:42] tra i vari agenti. Quindi ogni volta di
[01:38:45] nuovo, come nelle fasi prima, quando
[01:38:47] abbiamo un qualcosa che migliora e se
[01:38:48] migliora in automatico, abbiamo anche la
[01:38:50] possibilità di far migliorare i nostri
[01:38:52] agenti. Quindi nel nel caso in cui
[01:38:54] abbiamo che le prime volte investiamo
[01:38:56] qualche buon token per fargli parlare,
[01:38:58] ma magari gli output non sono adeguati a
[01:39:01] quello che vogliamo, abbiamo avuto 4 5 6
[01:39:04] skill prima, tra cui quella che vi ho
[01:39:05] lasciato anche all'inizio per appendervi
[01:39:08] al a a al prompte.
[01:39:13] Avete poi la possibilità di fare
[01:39:15] continuamente migliorare questi agenti
[01:39:17] qui. Detto questo, ora aspetto che il
[01:39:19] dibattito finisca e vi faccio vedere il
[01:39:21] risultato. Ed eccoci qui. E senza
[01:39:22] leggerlo tutto, ora abbiamo il verdetto
[01:39:24] del dibattito
[01:39:26] con il piano integrato. Ok, quindi
[01:39:30] per ora dicono "Ok, il migliore è ho
[01:39:33] guadagnato X con le AI e
[01:39:36] basta". Eh, il disagreement più
[01:39:39] interessante invece sono le
[01:39:41] microcollaborazioni.
[01:39:42] Il rischio più grande è il buco
[01:39:44] motivazionale del mese du magari eh i
[01:39:47] risultati non arrivano. Quindi eh con
[01:39:51] questa cosa qui lui dice è ragionevole
[01:39:53] pensare che sei tra i 20 e i 40.000
[01:39:55] iscritti entro eh dicembre 2026. Bene,
[01:40:00] andiamo a qualcosa di ancora un po' più
[01:40:02] avanzato e per farlo vado in una nuova
[01:40:05] conversazione, ma ve lo torno qui a
[01:40:07] spiegare prima dal punto di vista
[01:40:08] teorico e questo vi lascerò invece la
[01:40:11] skill perché è abbastanza complesso da
[01:40:13] fare e non è come gli altri. È quello
[01:40:15] che viene chiamato browser Swarm. Che
[01:40:18] cosa significa? Significa che ehm noi
[01:40:22] siamo abituati ad utilizzare gli agenti
[01:40:25] facendo le cosiddette browser
[01:40:27] automation. Che cosa sono? sono il fatto
[01:40:30] che il nostro Cloud Code, per esempio,
[01:40:32] Codex, chiunque di voi vogliate, possa
[01:40:35] eh utilizzare il nostro browser e andare
[01:40:38] a cercare le varie cose.
[01:40:41] Questo questa cosa qui eh permette di
[01:40:46] avere più browser in parallelo che
[01:40:48] facciano la stessa cosa. Allora, ora
[01:40:51] senza stare molto sul teorico, voglio
[01:40:53] farvi vedere l'unica cosa di guadagno
[01:40:57] pratico che avete, se lo fate, ma poi
[01:41:00] voglio farvi vedere un esempio pratico.
[01:41:02] Allora, che cosa succede? Beh, succede
[01:41:04] che quando facciamo un un'automazione,
[01:41:07] ok? Quindi partiamo da qui. Se questo è
[01:41:10] il nostro tempo e eh vediamo che abbiamo
[01:41:16] magari non lo so, 10 minuti, abbiamo 20
[01:41:19] minuti, abbiamo 30 minuti, abbiamo poi
[01:41:22] non lo so 60 minuti. [sbuffare]
[01:41:24] Ipotizziamo che queste siano le task che
[01:41:26] facciamo con un browser, magari sono
[01:41:28] lente. La prima task ci ha messo 10
[01:41:31] minuti a farla, la seconda ce ne ha
[01:41:33] messi altri 10, la terza se ne ha messi
[01:41:35] altri 10. Ok? Quindi noi abbiamo fatto
[01:41:38] un una task, un'altra task e un'altra
[01:41:42] task. Quindi in questo caso abbiamo
[01:41:44] fatto tre task in 30 minuti.
[01:41:48] Quello che questa automazione ci
[01:41:50] permette di fare è di mettere tutto in
[01:41:52] parallelo. Che cosa vuol dire? che noi
[01:41:54] partiamo, abbiamo immediatamente tre
[01:41:57] parallelo che spawnano
[01:42:00] e poi quello che succede è che noi
[01:42:03] quindi avremo che tutte e tre le task
[01:42:06] vengono fatte nello stesso tempo in cui
[01:42:09] ne è fatta una. Quindi per questo
[01:42:11] esempio molto semplice abbiamo abbiamo
[01:42:13] dimezzato il tempo di tre e quindi
[01:42:15] abbiamo avuto un un arrowi in termini di
[01:42:17] tempo che è di tre volte. Ovviamente più
[01:42:20] il processo è lungo, più il processo è
[01:42:21] lento, più questo eh viene viene,
[01:42:25] diciamo, viene amplificato. Immaginatevi
[01:42:27] che questo processo dobbiate farlo
[01:42:29] cinque volte. In questo caso avete 5* 3,
[01:42:33] quindi avete 15 unità di tempo, ok?
[01:42:37] Quindi da 10 minuti, quindi
[01:42:38] sostanzialmente avete 150 minuti se se
[01:42:41] riprendiamo questa equivalenza. E se noi
[01:42:44] riuscissimo a spawnare, ovviamente costa
[01:42:46] dei token, ma a livello logico 15 eh
[01:42:49] agenti in parallelo, avremo un risparmio
[01:42:51] del per 15.
[01:42:53] Andiamo a vedere come funziona. Ehm,
[01:42:55] hei, per favore, ehm, spawna
[01:43:00] tre browser con il nostro Chrome Swarm e
[01:43:05] quello che vorrei che tu facessi è che
[01:43:07] entrassi con tutti e tre nella pagina
[01:43:08] iniziale di Google, poi inserissi tre
[01:43:10] diverse qui, magari una per andare su
[01:43:12] LinkedIn, una su YouTube, una su
[01:43:14] Instagram e poi
[01:43:16] andassi lì.
[01:43:20] Perfetto. Task semplice, potremmo fare
[01:43:22] cose un po' più complesse, come per
[01:43:23] esempio ehm non lo so, trovami 5 barano
[01:43:28] oppure dati questi contatti, entra in
[01:43:33] cinque siti. Oh, ok, dovremmo averli già
[01:43:36] funzionanti.
[01:43:38] Eccoli qui. Adesso pian pianino si
[01:43:41] sistemano, però vedete che li ha
[01:43:43] spawnati. Ora sta facendo le sue cose e
[01:43:46] vedete che ora uno LinkedIn, uno
[01:43:48] Instagram. un YouTube e quindi poi qui
[01:43:50] potremmo fare cose diverse. Altro
[01:43:52] esempio che potrebbe esservi utile è
[01:43:56] avere come ho io una E adesso vi faccio
[01:43:59] vedere un paio di cose super che
[01:44:01] ho fatto. Non entrerò dentro, ma questa
[01:44:03] è la mia skill sign, quindi ci sono
[01:44:05] tutte le mie informazioni, nome,
[01:44:07] cognome, indirizzo, email, eccetera, che
[01:44:11] sono per i form online.
[01:44:14] E perché? perché li utilizzo per o ehm
[01:44:19] fare processo di raccolta di email e
[01:44:22] quindi poi vedete qui che dice che ha
[01:44:24] fatto tutto, quindi o raccolta di email
[01:44:26] su lead o identificazione autenticazione
[01:44:31] in in siti in cui è richiesta
[01:44:33] l'autenticazione umana o selezione
[01:44:35] cookie, come avete visto 2 secondi fa.
[01:44:38] Eh, esistono skill molto più avanzate,
[01:44:41] però ecco, questo è un esempio di come
[01:44:43] potete utilizzare questi con un certo
[01:44:45] ritorno economico. E per esempio
[01:44:47] un'altra cosa che vi consiglio è per
[01:44:49] molti studi medici, eh perché avevo ho
[01:44:53] avevo ho anche quella come nicchia e per
[01:44:56] ricevere l'email del dottore dovete
[01:44:59] entrare dentro, registrarvi, mettere i
[01:45:00] vostri dati e poi vi verrà dato lo
[01:45:03] scraping. Io non sto incitando niente,
[01:45:05] però nel caso aveste un Multia
[01:45:08] Swarm o un browser Swarm, quello che
[01:45:10] potete fare è avere questa questa
[01:45:13] squadra di agenti che va a identificarsi
[01:45:16] come voi e nel caso raccoglierebbe
[01:45:18] unemail. Ovviamente io non lo
[01:45:19] raccomando.
[01:45:21] Ehm, molto bene. [risate]
[01:45:24] Allora, torniamo a noi. E ultima cosa.
[01:45:27] Bene, ipotizziamo di avere fatto un ehm
[01:45:32] progetto perfetto. Ora, come facciamo ad
[01:45:36] assicurarci che facciamo un audit?
[01:45:38] Un audit di progetto viene fatto
[01:45:40] utilizzando tre agenti parallelo.
[01:45:43] Allora, il primo è un eh ispettore del
[01:45:48] codice. Che cosa vuol dire? Che lui avrà
[01:45:52] zero contesto. Ok? Quindi zero contesto.
[01:45:57] Ed il motivo è proprio per quello che è
[01:45:58] successo all'inizio del video, quando un
[01:46:01] agente comincia a lavorare su qualcosa
[01:46:04] diventa abbastanza biased sulle
[01:46:06] informazioni di contorno che ha per
[01:46:08] tutte le varie memorie di cui abbiamo
[01:46:09] discusso. Quindi un'altra cosa che
[01:46:11] dobbiamo fare per assicurarci che non ci
[01:46:12] sia un bias di contesto è ok, ho fatto
[01:46:16] questo progetto, è venuto nel migliore
[01:46:18] dei modi e allora la gente capirà in
[01:46:20] automatico la tex stack che state
[01:46:22] utilizzando e tutte le altre cose.
[01:46:25] Eh, l'altra cosa è un coso, un un agente
[01:46:29] di e quindi questo avrà il codice come
[01:46:32] meccanismo principale di ehm review. Il
[01:46:36] secondo sarà un ispettore
[01:46:38] e quindi questo ha ehm file mancanti eh
[01:46:43] di coerenza e quindi, per esempio, ho
[01:46:47] non ho scritto tutte le regole, quindi
[01:46:49] nel mio eh cloud dot
[01:46:54] MD non sono riuscito a scrivere tutte le
[01:46:57] regole o per favore fammi il l'update di
[01:47:02] tutto quanto e mille altre cose. Oppure
[01:47:05] l'ultimo è quello che riguarda sicurezza
[01:47:09] e vulnerabilità. Quindi il mio codice è
[01:47:12] stato fatto, è scritto perfetto, però
[01:47:14] manca di eh tutti i layer di sicurezza
[01:47:17] che abbiamo. Qui avrete anche un comando
[01:47:21] nel caso foste interessato, foste
[01:47:23] interessati che si chiama/Ssecurity
[01:47:26] Review che vi permette di fare questo.
[01:47:28] Oppure potete usare un un agente
[01:47:30] specializzato.
[01:47:32] Sono tra l'altro i tre agenti di
[01:47:33] Antropic.
[01:47:34] &gt;&gt; Ehm, questo è il mio audit e se non
[01:47:38] sbaglio io utilizzo un agente
[01:47:40] specializzato
[01:47:42] e quindi code, skill, eh broken chain,
[01:47:46] eccetera eccetera eccetera
[01:47:49] e tre agenti in parallelo, come vedete.
[01:47:53] E e Sì, esatto. E e orfan detection. Ce
[01:47:56] ne sono un po' di cose che io controllo,
[01:47:58] però per capirci. Ecco, io giusto perché
[01:48:01] ho fatto un sacco di cose oggi, come
[01:48:04] faccio a fare questo audit?
[01:48:06] Semplicemente io ho fatto la mia skill
[01:48:08] di audit che mi permette di fare questo
[01:48:10] e senza alcun tipo di contesto va e
[01:48:12] analizza tutto quanto. Volevo farvi
[01:48:15] vedere anche che c'è, se non sbaglio, ho
[01:48:19] detto che c'era security audit, eh, ma
[01:48:23] vediamo se
[01:48:27] security review, eccolo qui,
[01:48:28] perdonatemi, è un security review,
[01:48:30] quindi non era il security audit, però
[01:48:32] ecco, questa è l'altra skill che potete
[01:48:34] poi utilizzare. Questa è stata fatta
[01:48:36] perché perché io in questo agente ho
[01:48:38] messo un po' di cose. Ho messo quindi i
[01:48:40] tre che sono un researcher, un reviewer
[01:48:42] e un QA e gli ho messo che deve fare oD
[01:48:47] tutti i file orfani, tutti i file che ci
[01:48:49] sono, non ci sono, codice chain
[01:48:52] integrity, quando il progetto magari sta
[01:48:54] andando nella direzione sbagliata,
[01:48:56] togliermi i rami e pulirmelo. poi, ehm,
[01:49:00] quello che ho detto, regole sul
[01:49:02] freshness, sulle regole, sugli, su
[01:49:05] un'analisi di memoria, quindi ho fatto
[01:49:07] un audit molto approfondito, ok? Potete
[01:49:09] farvelo anche voi in base a quello che
[01:49:11] volete e poi io ho messo anche un QA se
[01:49:13] volete un mezzo consiglio anche per
[01:49:15] tutto quello che riguarda GitHub.
[01:49:16] Quindi, per esempio, io qui ora ho ehm
[01:49:20] 28 cose pending su GitHub, che sono dei
[01:49:23] changes che volevo fare e ehm questi
[01:49:26] changes qui, una volta che la mia skill
[01:49:28] ha finito di rannare, eh poi verranno
[01:49:31] tutti committati, verrà tutto pushato in
[01:49:34] GitHub e quindi poi il mio progetto eh
[01:49:36] rimarrà pulito. Bene. Eh, ovviamente vi
[01:49:39] lascerò anche questa skill di audit
[01:49:40] sotto in modo tale che se poi vogliate
[01:49:42] importarla per inserire all'entate
[01:49:46] farlo in tutta libertà. È stato
[01:49:47] divertentissimo fare questa tipologia di
[01:49:49] video e spero vi sia piaciuto. Se ne
[01:49:51] volete altre fatemi sapere. Ehm,
[01:49:54] utilizzate pure le risorse disponibili,
[01:49:55] le lascerò sotto in un link gratuito. E
[01:49:58] se siete interessati ad un programma
[01:50:00] strutturato per cominciare a vendere
[01:50:02] servizi AI o ad implementare servizi
[01:50:04] nella vostra azienda, vi lascio il primo
[01:50:06] link qua sotto. Detto questo, eh, per
[01:50:09] favore mettete like al video se vi è
[01:50:11] piaciuto, commentate, ditemi qualcosa.
[01:50:14] Aiuta il canale e se non ci siete
[01:50:17] iscrivetevi e ci vediamo alla prossima.
[01:50:19] Tchau.
