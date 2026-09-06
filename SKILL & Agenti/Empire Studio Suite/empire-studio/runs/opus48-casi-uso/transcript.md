
[00:00:00] In questo video ti mostro sette casi
[00:00:02] d'uso reali di Cloud Opus 4.8, il nuovo
[00:00:05] modello di Antropic che ha un giudizio
[00:00:07] migliore, più autonomia e la possibilità
[00:00:09] di decidere quanto deve sforzarsi.
[00:00:11] Facciamo capire un intero progetto di
[00:00:14] codice che non ha mai avverto. Andiamo a
[00:00:16] caccia di bug che ti bloccano da ore e
[00:00:18] costruiamo una nuova funzione completa
[00:00:20] dall'inizio alla fine con i flussi
[00:00:22] dinamici. Gli diamo impasto tre report
[00:00:24] da confrontare in un colpo solo e gli
[00:00:26] facciamo riscrivere unemail perché suoni
[00:00:28] esattamente come scrivi tu. Infine gli
[00:00:31] lasciamo riordinare e automatizzare i
[00:00:33] tuoi file con cowork e trasformiamo un
[00:00:35] foglio di dati grizzi in una
[00:00:36] presentazione pronta. Sembra pazzesco,
[00:00:38] ma è la realtà, quindi non perdiamo
[00:00:40] tempo e partiamo. Il debutto. Il 28
[00:00:43] maggio 2026 Opus 4.8 è uscito, è
[00:00:46] costruito sulla base del 4.7, ma con un
[00:00:49] giudizio più lucido, maggiore sincerità
[00:00:52] su quanto il lavoro ha davvero portato a
[00:00:54] termine. Questo ricorda un po' la
[00:00:55] versione di GPT 5.5 che è esattamente
[00:00:58] come 5.4 solo più matura, quindi è
[00:01:01] costruito sulle ceneri del precedente.
[00:01:03] Dettaglio molto importante, il prezzo è
[00:01:05] identico al 4.7, 7. Le novità sui costi
[00:01:08] riguarda i limiti di richieste, cioè
[00:01:10] quante chiamate puoi fare in un dato
[00:01:12] intervallo, sono stati alzati per
[00:01:13] reggere il maggior consumo dei livelli
[00:01:15] di sforzo più alti. Attenzione a non
[00:01:17] confonderle con i limiti di sessione, la
[00:01:19] finestra a ore o quelle settimanale,
[00:01:21] quelli restano invariati. C'è poi un
[00:01:22] dato che conta parecchio per chi lavora
[00:01:24] a ritmo. La nuova modalità veloce,
[00:01:26] quella del 4.8, gira a 2,5 volte la
[00:01:30] velocità e costa tre volte meno rispetto
[00:01:32] ai modelli precedenti. Quindi non solo è
[00:01:35] più capace, ma su questo fronte è anche
[00:01:37] più rapido ed economico rispetto a
[00:01:39] prima. Il livello di sforzo e i flussi
[00:01:41] dinamici insieme al modello sono le
[00:01:43] novità maggiori. La prima disponibile
[00:01:44] anche nella versione web e in cork
[00:01:47] lascia decidere quanto impegno vuoi
[00:01:48] dedicare a un compito, cioè quanta
[00:01:50] capacità di ragionamento il modello ci
[00:01:52] mette. La seconda dentro Cloud Code si
[00:01:55] chiama flussi dinamici e serve ad
[00:01:57] affrontare problemi di grande scala. Una
[00:01:59] precisazione importante, sui flussi
[00:02:01] dinamici per ora sono in anteprima,
[00:02:03] quindi research preview e disponibili
[00:02:05] solo su Cloud Code con il piano
[00:02:07] Enterprise o Team o Max. Se hai un piano
[00:02:10] base ancora non ritrovi. Il controllo di
[00:02:12] livello dello sforzo invece è
[00:02:14] disponibile su tutti i piani. In pratica
[00:02:15] scelto il modello parti in automatico a
[00:02:17] livello alto, ma puoi cambiarlo quando
[00:02:19] vuoi. La scala va dal basso a medio,
[00:02:21] alto a molto alto. Troviamo dentro Cloud
[00:02:24] Code Xi che è oltre veramente il
[00:02:26] massimo. Più sali più il modello è
[00:02:28] capace ma consuma molto di più. Più
[00:02:30] scendi più le risposte sono veloci. Lo
[00:02:32] stesso comando è disponibile sia
[00:02:33] nell'app sia da riga di comando. Perché
[00:02:35] i test ufficiali vanno presi con le
[00:02:37] pinze? Ora, come sempre, andiamo a
[00:02:39] guardare i benchmark che sono utili, ma
[00:02:40] vanno sempre presi con le pinze perché
[00:02:42] ogni nuovo modello batte sempre
[00:02:44] praticamente quello precedente, ma ormai
[00:02:46] sappiamo anche che i modelli sono
[00:02:47] ottimizzati per fare meglio sui
[00:02:49] benchmark. Magari la versione 4.8 è
[00:02:51] davvero più forte di Codex con GPT 5.5
[00:02:54] nella programmazione autonoma, ma per il
[00:02:56] tuo flusso specifico un altro strumento
[00:02:57] magari può essere migliore. Quindi, come
[00:02:59] dico sempre, ok benchmark, ma poi testa
[00:03:02] sempre sul campo. Un modello più sincero
[00:03:04] su ciò che fa. Antropic ha dedicato
[00:03:06] un'intera sezione all'interno del suo
[00:03:08] paper di rilascio ed è proprio
[00:03:09] interessante perché è proprio uno dei
[00:03:10] difetti che si notava nella versione
[00:03:12] 4.7. Tutti i modelli vengono addestrati
[00:03:15] a non promettere cose che non possono
[00:03:17] mantenere. Due esempi classici di
[00:03:19] affermazioni da evitare. Esempio numero
[00:03:21] uno, stima dei tempi gonfiati.
[00:03:24] Dichiarare ci vorranno 4 ore e puoi
[00:03:26] finire in 20 minuti. Oppure un altro
[00:03:28] esempio è lavoro dichiarato ma non
[00:03:30] fatto. Dire ho finito, ho caricato tutte
[00:03:32] e 50 le modifiche quando in realtà ne
[00:03:34] sono state caricate solo 15. Se ti è
[00:03:36] capitato di ricevere risposte così, non
[00:03:39] sei il solo. La versione 4.8 è molto più
[00:03:41] affidabile su questo. Il dato concreto
[00:03:43] di Antropic è netto. La 4.8 ha circa
[00:03:46] quattro volte meno probabilità della 4.7
[00:03:49] di lasciare passare un difetto nel
[00:03:52] codice che ha scritto senza
[00:03:53] segnalartelo. Hanno anche test specifici
[00:03:56] per misurare i comportamenti fuori riga,
[00:03:58] come per esempio l'inganno. Qui i tasti
[00:04:00] del 4.8 sono sostanzialmente più bassi
[00:04:03] della 4.7 7 e si avvicinano a quelli di
[00:04:06] Mos, il modello migliore in assoluto che
[00:04:08] ancora non è rilasciato. Mos in arrivo e
[00:04:11] dove trovi già la 4.8. Nel complesso la
[00:04:13] versione di Opus 4.8 viene descritta
[00:04:15] come un passo avanti modesto ma concreto
[00:04:18] rispetto alla 4.7. C'è ancora strada da
[00:04:20] fare? La cosa più intrigante è
[00:04:22] l'annuncio di una futura famiglia di
[00:04:24] modelli più potente di Opus chiamata
[00:04:27] MOS. Per ora la usano poche
[00:04:28] organizzazioni, come sappiamo, per la
[00:04:30] sicurezza informatica, il cosiddetto
[00:04:32] Project Glasswing. Col progetto
[00:04:34] Glasswing l'obiettivo è prima mettere in
[00:04:36] sicurezza tutto il web, quindi tutte
[00:04:38] queste grandi aziende che cosa fanno?
[00:04:40] Prendono e stanno lanciando Mos cercare
[00:04:43] di tappare tutte le falle, così da
[00:04:44] rendersi, diciamo, a prova di bomba e
[00:04:47] poi dopo rilasciare Mitos sul mercato.
[00:04:49] Piccola nota mi sembra che addirittura è
[00:04:51] stata Firefox a dichiarare che in un
[00:04:52] solo mese con l'utilizzo di Vitos hanno
[00:04:54] chiuso più di 140 falle, una cosa del
[00:04:56] genere. Anropic ci dice che punta a
[00:04:58] rilasciare il Mitos disponibile a tutti
[00:05:00] i clienti nelle prossime settimane, ma
[00:05:02] non si sa quando ancora, diciamo, è
[00:05:04] molto generico. Intanto la 4.8 è
[00:05:06] disponibile ovunque, web, terminale,
[00:05:08] estensione nell'editor, la trovi
[00:05:10] direttamente anche nell'app iPhone,
[00:05:12] Android o direttamente su Mac e resta la
[00:05:14] finestra di contesto di 1 milione, cioè
[00:05:15] la quantità di testo che il modello
[00:05:17] riesce a tenere a mente in una sola
[00:05:18] conversazione. Dal menù di scelta puoi
[00:05:21] passare in qualsiasi momento alla 4.8,
[00:05:23] indicata come l'opzione più capace per
[00:05:25] la maggior parte dei lavoratori. I
[00:05:26] difetti della 4.7 secondo gli utenti. La
[00:05:29] 4.7 era uscita appena un mese e mezzo
[00:05:31] prima, il 16 aprile circa, quindi un
[00:05:33] ritmo di rilascio altissimo. Eppure
[00:05:35] parecchio utenti non l'avevano accolta
[00:05:37] benissimo, anzi la trattavano peggio
[00:05:38] della versione 4.6. I problemi più
[00:05:40] citati sembravano un po' pigra, mollava
[00:05:42] il compito troppo presto e per questo
[00:05:44] era nato il comando obiettivo, un
[00:05:46] rimedio per spingere a insistere più a
[00:05:48] lungo verso un traguardo preciso che ora
[00:05:50] è diventato parte integrante del
[00:05:51] modello. Di base è meno pigra e regge
[00:05:54] meglio i lavori lunghi. le si
[00:05:55] rimproverava anche un eccesso di
[00:05:57] rigidità sulle restrizioni di sicurezza
[00:05:59] e un consumo, quindi anche un costo più
[00:06:02] alto. La critica di più divertente è
[00:06:03] stata a un certo punto come compagno di
[00:06:05] ragionamento va benissimo, ma a volte
[00:06:07] risultava brusca o testarda, cioè si
[00:06:09] incaponiva mare su cose su cui credeva
[00:06:10] di avere ragione anche se non aveva
[00:06:12] ragione. Sono difetti che la community
[00:06:13] ha percepito e indovinate un po' in 4.8
[00:06:16] non c'è più, quindi vediamo che Antropic
[00:06:18] è molto recettiva ai feedback che
[00:06:19] riceve. Colpa del modello o di come lo
[00:06:21] usiamo? Qui entriamo in una differenza
[00:06:23] sostanziale. Tra un modello che ha dei
[00:06:25] limiti e un modello usato male c'è
[00:06:26] grande differenza e a volte è sottile e
[00:06:29] altre volte è una muraglia cinese. Non è
[00:06:30] sempre colpa del modello, a volte è una
[00:06:32] questione di metodo e la risposta non è
[00:06:34] la 4.7 non ci riesce aspetto alla 4.8. a
[00:06:37] volte è semplicemente un errore nostro e
[00:06:39] questo è importante dirlo. Detto questo,
[00:06:40] la 4.8 nasce proprio per sistemare quei
[00:06:43] punti: più sincerità e capacità di
[00:06:45] correggersi, più autonomia sui lavori
[00:06:47] lunghi, un tono più caldo e
[00:06:48] collaborativo e una qualità d'uso
[00:06:51] migliore. Usa meglio gli strumenti,
[00:06:52] ragiona meglio, fa domande più sensate,
[00:06:54] spreca meno risorse, tutto in un'ottica
[00:06:57] di ottimizzazione, anche perché sappiamo
[00:06:58] che i limiti di Cloud sono veramente
[00:07:00] stringenti, quindi consumo vola. Lezione
[00:07:02] numero uno, lo sforzo. Per tutto questo
[00:07:04] ho ricavato alcune lezioni. La prima che
[00:07:06] andremo a vedere è per l'appunto lo
[00:07:08] sforzo. È la levola numero uno. Diversi
[00:07:10] difetti di prima, quindi la preghirizia,
[00:07:12] gli eccessi di prudenza, potevano essere
[00:07:13] in realtà un problema di impostazione.
[00:07:16] Se affronti un compito impegnativo con
[00:07:17] il livello su basso medio è normale che
[00:07:19] resti indietro, serve più sforzo. Vale
[00:07:21] anche il contrario. Su un compito banale
[00:07:23] e io stesso ho provato mettere un
[00:07:25] ragionamento altissimo, indovino un po',
[00:07:26] a volte mi ha portato anche all'errore.
[00:07:28] Incredibile, ma vero, perché andavamo a
[00:07:31] overcomplicare il tutto. è lì che pensi,
[00:07:33] ma è facile perché non lo fa? Quando
[00:07:35] molte volte dobbiamo andare veramente a
[00:07:37] selezionare l'impegno giusto, ok? Quindi
[00:07:39] se dobbiamo semplicemente corregger
[00:07:40] unemail, mettere l'impegno altissimo,
[00:07:42] non ha senso. Quindi qui ci vuole un
[00:07:43] equilibrio tra capacità, consumo e
[00:07:45] velocità. Il punto è questo. Se sei fra
[00:07:48] quelli che aprono lo strumento, iniziano
[00:07:49] a scrivere e non toccano mai le
[00:07:51] impostazioni, prova a farlo. La
[00:07:52] differenza tra il 4.8 al minimo e il 4.8
[00:07:55] al massimo è veramente abissale e vale
[00:07:57] la pena testarlo. Lezione due. Digli
[00:07:59] cosa fare, non cosa evitare. Questa
[00:08:01] indicazione è molto interessante perché
[00:08:03] indicare l'obiettivo e non il divieto e
[00:08:06] io ci sono arrivato sfogliando la
[00:08:07] documentazione piena di esempi e di
[00:08:09] prompt fatti da Antropic. quasi nessuno
[00:08:11] elencava il non fare, cosa che prima
[00:08:13] invece veniva consigliato su tutti i
[00:08:15] modelli, cioè dare l'esempio è anche
[00:08:17] l'esempio del non fare assolutamente.
[00:08:19] Questo è stato molto interessante perché
[00:08:21] ci fa capire che dobbiamo far
[00:08:22] concentrare di più il modello su quello
[00:08:23] che noi vogliamo come obiettivo, non
[00:08:25] tanto su quello da evitare. Questo è un
[00:08:27] cambiamento anche nel prompting molto
[00:08:29] importante. Lezione 3, spiega il perché
[00:08:31] di ogni richiesta. Da qui la terza
[00:08:33] lezione, motivare l'istruzione. Ok? Ti
[00:08:35] faccio un esempio, invece del divieto,
[00:08:37] voglio che sembri scritto davvero da me,
[00:08:38] è il mio stile e non uso mai le lineette
[00:08:40] lunghe, quindi rispetta il mio modo di
[00:08:42] scrivere. Formulato così, il modello
[00:08:44] segue più volentieri il tutto nei vari
[00:08:46] confronti. A me piace molto Opus
[00:08:47] rispetto a 5.5. Se non spiego il perché,
[00:08:49] specialmente con questa versione nuova,
[00:08:51] non sempre esegue il tutto. Invece dare
[00:08:53] un perché fa capire di più al modello
[00:08:56] come mai evitarlo, invece le istruzioni
[00:08:58] negative lo portano sulla sulla cattiva
[00:09:00] strada, cosa che prima invece non era
[00:09:02] così. Lezione numero quattro. Prima
[00:09:04] ragiona, poi agisce. Questa lezione è
[00:09:06] fondamentale perché cerca di capire da
[00:09:08] sé domande e approcci migliori per
[00:09:10] quello che deve fare. Cioè prima di del
[00:09:11] legare un pezzo di lavoro a un
[00:09:13] assistente secondario, consultare un
[00:09:15] archivio dati o compiere un'azione, si
[00:09:17] mette a pensare, diciamo che vuoi che
[00:09:19] ragioni su come muoversi. Altre volte
[00:09:21] invece ti serve che raccolga prima le
[00:09:23] informazioni e poi inizi a ragionare.
[00:09:25] Per questo conta sperimentare con le
[00:09:28] istruzioni e con il livello di sforzo,
[00:09:29] soprattutto quando sposti i flussi al
[00:09:31] 4.7 al 4.8. Non darli per scontati,
[00:09:34] tienili d'occhio prima di capire come si
[00:09:36] comporta. Lezione 5. La lunghezza si
[00:09:39] regola da sola. La 4.8 calibra da sé
[00:09:42] quanto scrivere, valuta la complessità
[00:09:44] del compito e adatta le risposte, invece
[00:09:46] di restare su una quantità fissa. In
[00:09:48] pratica, risposte brevi per le richieste
[00:09:50] semplici, più estese per le analisi
[00:09:51] aperte che richiedano un ragionamento.
[00:09:53] Questo è veramente molto interessante. E
[00:09:55] ora andiamo a vedere sette casi d'uso
[00:09:57] pratici per usare Opus 48. andremo a
[00:09:59] vedere i vari casi d'uso sia su cloud da
[00:10:02] web, sia su Cloud Code, sia su cowork.
[00:10:04] Per ciascuno trovi quanto ha senso il
[00:10:06] livello di sforzo consigliato e il
[00:10:08] prompt, mi raccomando, poi dopo testali
[00:10:10] su di te, insomma, adattali. Caso d'uso
[00:10:12] uno, capire un progetto di codice che
[00:10:14] non conosci. Quando entri su una base di
[00:10:16] codice nuovo e devi orientarti, prima di
[00:10:18] metterci mano, ecco che cosa fare.
[00:10:20] Sforzo consigliato alto, digita questo
[00:10:22] prompt, esplora questo progetto e
[00:10:24] spiegami com'è strutturato, quali sono i
[00:10:25] punti di ingresso, come scorrono i dati
[00:10:27] e dove sta la logica principale. Per ora
[00:10:29] non modificare niente prima disegna la
[00:10:31] mappa. Caso d'uso numero due, caccia al
[00:10:34] bug difficile. Quando hai un errore che
[00:10:36] non riesci a chiudere e ci giri intorno
[00:10:38] a un po', qui questo prompt è pazzesco.
[00:10:40] Lo sforzo consigliato è molto alto, è un
[00:10:43] compito che più ragiona meglio è. Quindi
[00:10:46] ho questo errore, incollo il messaggio e
[00:10:47] il codice intorno, trova la causa alla
[00:10:49] rice, spiegami perché succede. Proponimi
[00:10:51] la correzione minima. Prima di toccare
[00:10:53] il codice, dimbi la tua ipotesi, così la
[00:10:55] valuto. Vedrai il risultato è davvero
[00:10:57] pazzesco. Caso d'uso numero tre,
[00:10:59] costruire una funzione completa
[00:11:01] dall'inizio alla fine. Quando il lavoro
[00:11:02] tocca più file e più passaggi è il caso
[00:11:05] ideale per i flussi dinamici. Sforzo
[00:11:07] consigliato massimo o ancora extra.
[00:11:10] Ricorda, i flussi dinamici sono solo per
[00:11:12] i piani massimi, quindi Enterprise, Team
[00:11:14] e Max, altrimenti non ce l'hai. Prompt
[00:11:16] possibile. Implementa, inserisci la
[00:11:18] funzione dall'inizio alla fine,
[00:11:20] pianifica i passaggi, scrivi il codice,
[00:11:22] aggiungi i test e verifica che passino.
[00:11:24] Aggiornami a ogni tappa e fermati se
[00:11:26] trovi una scelta importante da farmi
[00:11:28] decidere. Caso d'uso numero quattro,
[00:11:30] analizzare e confrontare documenti
[00:11:32] lunghi. Questo è perfetto per farlo da
[00:11:34] direttamente da web quando devi leggere
[00:11:36] e mettere a confronto contratti report o
[00:11:37] ricerche. Qui sfrutti davvero la
[00:11:39] finestra da 1 milione di token. Sforzo
[00:11:41] consigliato medio oppure alto. Ti
[00:11:43] incollo tre report, confrontali,
[00:11:44] evidenziali dove si contraddicono e
[00:11:47] fammi una sintesi di una pagina con i
[00:11:49] cinque punti che contano per prendere
[00:11:50] una decisione. Cita per ogni punto da
[00:11:52] quale documento arriva, così siete
[00:11:54] sicuri che tutto è corretto. Caso d'uso
[00:11:56] numero 5: scrivere e rivisionare con la
[00:11:59] tua voce. Anche qui perfetto
[00:12:00] direttamente al web. Quando crei email,
[00:12:02] articoli o post e vuoi che suonino
[00:12:04] esattamente come scriveresti. Ecco che
[00:12:06] cosa fare. Riscrivi questa email così
[00:12:07] che sembri scritta da me. Ton diretto
[00:12:10] frasi brevi. Niente frasi fatte. È per
[00:12:12] un cliente importante, quindi deve
[00:12:14] restare professionale. Te la giro in
[00:12:16] modo che tu capisca lo stile da
[00:12:17] replicare e qui, tra le parentesi quadre
[00:12:19] incollate il testo. Caso d'uso numero 6:
[00:12:22] automatizzare i file su cowork. Quando
[00:12:24] devi mettere ordine, convertire o
[00:12:26] estrarre i dati da file che hai in
[00:12:28] locale, ti conviene utilizzare cowork
[00:12:31] come sforzo medio e andiamo su questo
[00:12:33] prompt. Guarda questa cartella e quindi
[00:12:35] allegategli solo quella cartella, mi
[00:12:37] raccomando. Raggruppa i file per tipo e
[00:12:39] per mese, rinominali con uno schema
[00:12:41] coerente e alla fine fammi un ripilgo di
[00:12:43] cosa hai spostato e perché. Caso d'uso
[00:12:45] numero 7, trasformare i dati grezzi in
[00:12:48] un deliverable pronto. Qui potete
[00:12:50] utilizzare cowork o web. Io di solito
[00:12:52] utilizzo cowork quando da un foglio o da
[00:12:54] appunti, lo utilizzo molto spesso con i
[00:12:56] transcript delle call che faccio e vado
[00:12:58] a inserire un prompto. Sforzo
[00:13:00] consigliato a seconda del livello di
[00:13:01] complessità medio o alto. Da questo
[00:13:03] foglio di vendita crea una presentazione
[00:13:05] di otto slide, numeri chiavi in
[00:13:07] apertura, un grafico per trimestre, una
[00:13:09] slide sui rischi e una con tre
[00:13:11] raccomandazioni concrete. Dimmi prima
[00:13:13] una scaletta, poi la costruisci. Mi
[00:13:15] raccomando, questo è fondamentale perché
[00:13:17] se gli chiedete prima la scaletta,
[00:13:19] verificate se volete le modifiche e poi
[00:13:20] costruisce così vi consuma meno token,
[00:13:23] altrimenti senò poi dovete farglielo
[00:13:24] modificare e vi deve ricostruire tutto a
[00:13:26] capo. Ok? Quindi mi raccomando, molto
[00:13:29] importante. Altro consiglio, testate i
[00:13:31] vari livelli di sforzo e vedrete come
[00:13:32] cambiano le risposte. Opus 4.8 Pro e
[00:13:35] contro. Qui vi voglio dare dei feedback
[00:13:37] super onesti di quello che ho testato
[00:13:39] anch'io sulla versione 4.8 ho amato
[00:13:42] veramente il livello di sforzo perché
[00:13:43] tanti task che facevo già prima riesco a
[00:13:45] farli molto meglio cambiando il livello
[00:13:48] di sforzo. Per esempio, tutta la parte
[00:13:49] di scrittura di contenuti che faccio,
[00:13:51] ragionamenti, flussi, eccetera eccetera,
[00:13:53] con livelli di pensiero più alto e il
[00:13:55] fatto che il modello è molto, diciamo,
[00:13:58] più onesto e anche si impegna molto di
[00:14:00] più, riesca a avere dei risultati
[00:14:02] enormemente migliori. Faccio un esempio,
[00:14:04] io a fine mese faccio sempre un recap di
[00:14:05] tutti i dati di tutte le mie
[00:14:06] piattaforme, Instagram, TikTok, YouTube.
[00:14:08] Questo mese è stato notevolmente
[00:14:10] migliore rispetto ai mesi precedenti
[00:14:12] perché riesco a spingere molto di più.
[00:14:14] Contro che invece ho trovato, a mio
[00:14:15] avviso, è uno la quantità di bug. Ora,
[00:14:17] nel momento in cui sto girando questo
[00:14:19] video, magari è così perché il modello è
[00:14:20] uscito da 3 giorni e quindi per voi
[00:14:22] invece sarà diverso perché come sempre
[00:14:24] quando un modello viene rilasciato ci
[00:14:25] sono un po' di criticità che dopo vanno
[00:14:27] a diminuire. Però questo è quello che ho
[00:14:29] riscontrato io. Secondo, il fatto che
[00:14:31] diventa un pochino più complesso perché
[00:14:33] non tutti riescono effettivamente a
[00:14:35] capire subito il livello di impegno. È
[00:14:37] vero che si può lasciare quello medio e
[00:14:39] quindi si abbastanza sul sicuro, però mi
[00:14:42] sono accorto che veramente per
[00:14:43] determinati task mettere un modello di
[00:14:45] impegno più basso ti porta un risultato
[00:14:47] veramente migliore. Faccio un esempio,
[00:14:49] io faccio sempre il test delle email. Ho
[00:14:50] cercato di eh farmi sistemare alcune
[00:14:53] email n risposta con un modello di
[00:14:55] pensiero molto alto il risultato era
[00:14:57] terribile. Mi impiegava un sacco di
[00:14:58] tempo e il risultato era veramente
[00:15:00] terribile. Viceversa, con un livello di
[00:15:02] impegno più basso, si arrivava subito
[00:15:04] alla versione finale e in maniera
[00:15:05] veramente molto pulita. Quindi questo
[00:15:07] rischia di essere in fase iniziale un
[00:15:08] po' un ostacolo per tutti i vari utenti
[00:15:10] perché ad esempio su GPT già esiste
[00:15:12] questo, però non ci noto tutta questa
[00:15:15] enorme differenza nelle risposte. Sì,
[00:15:17] c'è ma non in maniera esorbitante,
[00:15:20] mentre su Opus c'è un impatto veramente
[00:15:22] notevole. Questo è il mio onesto
[00:15:23] pensiero. Fatemi sapere anche la vostra.
[00:15:25] Mi raccomando, se il video vi è stato
[00:15:26] utile, lascia un bel like per
[00:15:27] supportarmi, iscriviti al canale e come
[00:15:29] sempre buona soluzione a tutti. Yeah.
