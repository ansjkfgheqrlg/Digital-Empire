### Il momento in cui si dice il prezzo

C'è un istante, dentro ogni call di vendita, in cui tutto il lavoro fatto prima —
la scoperta, la proposta, la relazione costruita — si gioca su una singola frase: il
prezzo detto ad alta voce. Andrei Pascu, nel video sul preventivo che non vende, lo
chiama letteralmente "regola numero 5" del suo metodo, e la formula che propone è
quasi meccanica nella sua semplicità: dire il totale, IVA inclusa, senza girarci
intorno. [[EBU57iVAutA::KA-15]] Il modo in cui lo descrive è quasi teatrale: "generalmente
preferisco dire il prezzo totale, IVA inclusa — quindi 'il totale da pagare è €250, bam,
press price' — e poi aspetti la sua reazione." Non è un dettaglio di stile. È una
struttura precisa in tre mosse: si dice il numero, si sta zitti, si osserva. Il cliente
resta lì a pensare per qualche secondo e poi fa una domanda — quasi sempre. A quel
punto la regola non è difendersi o giustificare il prezzo sul posto: è tornare sulla
pagina del preventivo che risponde esattamente a quella domanda, rispiegare quella
parte, e poi tornare di nuovo sul prezzo. Avanti e indietro, tra il numero e la
spiegazione, fino a quando i dubbi non sono finiti. Il segnale che funziona, secondo
Pascu, è che quando il cliente accetta non lo argomenta: "quando ti dirà di sì, te lo
dirà e basta — 'sì, sono d'accordo, partiamo'." Il motivo per cui questa sequenza
regge è che separa due cose che i venditori inesperti mischiano sempre: il prezzo e la
spiegazione del prezzo. Chi ha paura di dire il numero, in genere, lo annacqua dentro
un paragrafo pieno di giustificazioni preventive — e così facendo comunica lui per
primo che il prezzo è un problema, prima ancora che il cliente lo pensi. Dirlo secco,
aspettare, e poi rispondere solo alle domande vere, tiene la trattativa ancorata ai
fatti invece che all'ansia di chi vende.

### Quanto misura se il prezzo è quello giusto

C'è un secondo strumento, complementare al primo, e serve a capire — non a sentimento,
ma con un numero — se il prezzo fissato è quello corretto. Si chiama close rate: la
percentuale di lead che, arrivati fino alla sales call, poi pagano davvero. Per un
service business, la regola empirica condivisa nel video di analisi sull'agenzia AI è
che il close rate ideale sta intorno al 30%. [[max17-v17-beggiato-agenzia::KA-008]] Il
ragionamento dietro il numero è più interessante del numero stesso: un close rate sopra
il 30% — per esempio il 60% citato come esempio nel video — non è un segnale di bravura,
è un segnale di prezzo troppo basso. Si chiude quasi tutto? Si sta lasciando margine
sul tavolo, sistematicamente, ogni volta che qualcuno dice sì troppo in fretta. Il
video lo mette in chiaro: "non cadete nell'errore di 'Oh mio Dio, io chiudo tutti',
perché questo vuol dire che ci state rimettendo in termini economici. […] non è una
vanity metric, non è una metrica per dire che siete fenomenali, è una metrica che
indica quanti soldi state lasciando ai vostri clienti e non guadagnando voi." Il caso
opposto è altrettanto informativo: un close rate intorno al 20%, o più basso, dice o
che la vendita è debole o che il prezzo è troppo alto rispetto a quello che il mercato
è disposto a pagare per quel servizio in quel momento. Il video segnala anche che il
30% è specifico ai service business — non è una legge universale: per community o
infoprodotti il benchmark citato è molto più basso, tra il 2 e il 4%, perché lì il
volume di persone che valutano l'offerta è enormemente più alto e il costo per
persona di valutarla è enormemente più basso. Per un'agenzia che fa sprint di CRO o
consulenza, applicare il benchmark sbagliato — misurarsi contro il 2-4% pensando di
essere un infoprodotto, o contro numeri arbitrari senza riferimento — significa non
avere nessun modo oggettivo di sapere se il listino prezzi è calibrato. Il close rate,
tracciato lead per lead, è quel modo: si guarda indietro su un campione di sales call
e si legge il numero, non ci si affida alla sensazione di "sto chiudendo bene" o "sto
chiudendo male".

### Un "sì" via email non è un cliente

C'è un errore specifico, molto comune tra chi comincia, che il video sull'agenzia AI
nomina per nome: trattare un "sì" arrivato via email o in chat come se fosse
equivalente a un cliente pagante. Non lo è. [[max17-v17-beggiato-agenzia::KA-019]] Il
passaggio è netto: "voi avete il primo cliente se solo se un movimento di denaro […]
avviene. Quindi, se questo movimento di denaro non avviene, voi non avete un
cliente." Il motivo per cui questa distinzione conta non è semantico, è operativo:
tra il "sì" detto in una call o scritto in una email e il bonifico che arriva sul
conto, passa del tempo — e in quel tempo il cliente ripensa, sente altre persone,
si fa influenzare, gli arrivano nuove priorità che spostano la sua attenzione altrove.
Ognuna di queste cose può far saltare l'accordo senza che nessuno l'abbia disdetto
formalmente: semplicemente, non arriva mai il pagamento. Chi festeggia al "sì"
anziché al bonifico si costruisce previsioni di fatturato false, pianifica assunzioni
o investimenti su un incasso che ancora non esiste, e scopre il buco solo quando è
già dentro le spese. La disciplina corretta è quella opposta: si considera cliente
solo chi ha pagato, si continua a inseguire chi ha detto sì e non ha ancora pagato, e
si tiene sempre visibile la differenza tra le due categorie — anche quando la somma
delle due farebbe un numero più bello da guardare.

#### Cosa fa Digital Empire su questo punto

L'agente `tesoreria-entrate` (`.claude/agents/tesoreria-entrate.md`) applica esattamente
questa distinzione come regola operativa, non come principio astratto: registra ogni
euro che entra o dovrebbe entrare in quattro stati separati — `previsto` ("ne abbiamo
parlato, forse succede. Non è un soldo"), `fatturato` ("la fattura è partita, il
cliente deve pagare. Non è ancora un soldo"), `incassato` ("i soldi sono sul conto.
Questo è un soldo") e `perso` (non arriverà, ma si registra lo stesso perché "dice
quanto costa non chiudere"). Il file è esplicito sul punto centrale del capitolo: "Un
preventivo mandato e un bonifico arrivato sono due cose diverse. Sommarli è il modo
classico di credersi ricchi mentre il conto è vuoto." L'agente insegue anche due
segnali di allarme concreti a ogni sua attivazione: fatture partite da più di 30
giorni e non incassate, che vanno sollecitate, e "previsti" fermi da più di 60 giorni,
che a quel punto non sono più previsti — sono persi, e vanno registrati come tali
invece di restare a mentire sul futuro dell'azienda. Sul momento specifico del "dire
il prezzo" in call e sulla lettura del close rate come termometro del prezzo, Digital
Empire non ha ancora una skill o un agente dedicato: la sequenza dire-tacere-tornare-
spiegare di Pascu e il benchmark del 30% restano, per ora, conoscenza da applicare a
mano nelle sales call, non ancora codificati in un processo.
