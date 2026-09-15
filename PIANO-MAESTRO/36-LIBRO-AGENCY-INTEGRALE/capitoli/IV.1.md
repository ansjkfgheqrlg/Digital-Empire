### La chiamata che decide come andrà tutto il resto

Il primo cliente è pagante da qualche ora, forse da qualche minuto. È il momento in
cui la maggior parte delle agenzie improvvisate smette di essere disciplinata: si
passa subito a "costruire", perché costruire sembra il lavoro vero, e la chiamata
di kickoff sembra solo un rito prima della parte interessante. Il materiale di
formazione sull'agenzia AI analizzato per questo libro tratta il kickoff nel modo
opposto: lo mette come primo passo obbligato, prima di qualsiasi lavoro tecnico, e
gli dedica una struttura precisa in cinque punti fissi — perché ognuno di quei
cinque punti, se saltato, produce un problema specifico più avanti nella delivery,
quasi sempre più costoso da risolvere dopo che da prevenire prima.

### I cinque punti della kickoff call

Il metodo descritto fissa esattamente cinque cose da definire dentro la prima
chiamata col cliente, prima di iniziare qualunque lavoro tecnico, e le presenta
come una sequenza che serve innanzitutto a settare aspettative — perché il cliente
non ha altro modo di sapere se il progetto sta andando bene se non attraverso
quello che gli è stato detto in anticipo. [[max17-v17-beggiato-agenzia::KA-021]] Il
primo punto è la timeline del progetto, costruita applicando la regola
dell'"under promise and overdeliver": si scompone il lavoro in fasi (per esempio,
nel caso di un sistema di acquisizione clienti: creazione dell'account pubblicitario,
setup della piattaforma CRM, costruzione della landing page, automazioni), si stima
quanto ci vuole davvero — poniamo quattro settimane — e poi si comunica al cliente
un tempo più lungo, sei settimane, per assorbire imprevisti come bug, downtime o
dati mancanti dal cliente stesso; quando poi il lavoro viene consegnato in quattro
settimane invece delle sei promesse, l'effetto sulla percezione del cliente è
molto più forte che se si fosse promesso il tempo esatto e lo si fosse rispettato
puntualmente. Il secondo punto è la reperibilità, dichiarata esplicitamente e non
lasciata implicita: giorni, orari, tempo di risposta atteso — "io lavoro da lunedì
a venerdì e sono reperibile [...] dalle 4:00 alle 6:00 del pomeriggio e lì
risponderò entro 5 minuti". Il motivo per cui questo va detto ad alta voce è che,
se non lo si fa, è il cliente a fissare l'aspettativa al posto proprio, quasi
sempre in modo molto più esigente di quanto il fornitore possa reggere: il video
racconta l'esperienza diretta di essere stato contattato nei weekend per mesi
proprio perché questo limite non era mai stato dichiarato. Il terzo punto è la
definizione scritta del successo — cosa vuol dire, esattamente, che il progetto è
finito: un elenco chiuso di deliverable verificabili, non un'idea generica di
"funzionare bene". Serve a prevenire lo scope creep, cioè la deriva per cui il
cliente aggiunge richieste una dopo l'altra ("ah no, ma un'altra cosa", "ah no, ma
io intendevo") senza che nessuna di quelle richieste sia mai stata messa nero su
bianco come fuori perimetro; il racconto personale nel video è diretto — un
progetto di dashboard finito per durare mesi oltre il previsto proprio perché ogni
nuova richiesta veniva accettata con un "sì, sì, sì" invece di essere marcata come
aggiunta al progetto originale. Il quarto punto è registrare il cliente su tutte
le piattaforme necessarie durante la call stessa, non dopo: l'obiettivo è evitare
di restare fermi una settimana perché il cliente da solo non riesce a iscriversi a
un servizio cloud, attivare un abbonamento o generare una chiave API, perdendosi
in un'interfaccia che per lui è sconosciuta e opprimente. Il quinto punto, l'unico
esplicitamente marcato come facoltativo per il primissimo cliente, è tracciare
tutto in uno strumento di project management — ma solo se già disponibile, perché
per un solo cliente attivo non serve nessun sistema di tracciamento formale e
costruirlo comunque è definito nel video stesso un caso di over-engineering su
qualcosa che, a quello stadio, non serve ancora. Il materiale aggiunge un avvertimento
a monte di questi cinque punti: non templetizzare né automatizzare nessuna di
queste comunicazioni prima di averle fatte a mano almeno due o tre volte, perché
senza il feedback reale di un cliente vero non si sa ancora se il template
funziona o se manca qualcosa di essenziale.

### Prendersi in carico la richiesta prima ancora di chiamare

C'è una tecnica più piccola, pensata per il momento immediatamente precedente al
kickoff — il primo contatto dopo che un lead ha compilato un form — chiamata
"taking in charge": inviare subito un messaggio automatico che comunica la presa
in carico della richiesta, prima ancora della telefonata umana vera e propria.
[[max17-v17-beggiato-agenzia::KA-023]] Il testo tipo è volutamente minimo — "ho
appena ricevuto la tua richiesta, ti chiamo tra pochi minuti da questo numero" —
e il motivo per cui funziona è quasi meccanico: un lead che riceve questo
messaggio riconosce il numero da cui riceverà la chiamata come atteso, non come
sconosciuto, il che aumenta in modo misurabile la probabilità che risponda —
"questo aumenta lo show rate o il pickup rate per quanto riguarda le chiamate" —
risolvendo uno dei problemi più comuni delle chiamate a freddo, cioè il fatto che
un numero non riconosciuto normalmente non genera risposta.

#### Cosa fa Digital Empire su questo punto

Digital Empire ha due skill che coprono la parte di delivery attorno a questo
capitolo, ma nessuna delle due replica ancora, punto per punto, lo script della
kickoff call descritto sopra. La skill `delivery-playbook`
(`.claude/skills/delivery-playbook/SKILL.md`) parte dal contratto firmato
(payload `HC-A3-A4-contratto`) e struttura la consegna dei tre prodotti agency in
sette giorni, ma il suo primo passo è "Pre-giorno-1: verifica ambiente" — un
controllo tecnico (OS, Python, accessi SSH/RDP, credenziali) — non una chiamata
di allineamento sulle aspettative del cliente nel senso descritto in questo
capitolo: non c'è ancora, nel playbook, un punto esplicito su timeline dichiarata
con buffer, reperibilità dichiarata o registrazione del cliente sulle piattaforme
durante una call dedicata. La skill `client-handover`
(`.claude/skills/client-handover/SKILL.md`) copre invece l'altro estremo della
relazione, la fine della delivery: genera il pacchetto che rende il cliente
autonomo (README operativo, runbook giornaliero, FAQ, indice credenziali senza
valori, licenza d'uso, indice dei video di training, checklist di autonomia
firmabile), con la stessa logica di aspettative esplicite e verificabili che il
kickoff applica all'inizio — il gate di consegna richiede che il cliente dimostri
di saper avviare una run da zero, leggere il report, modificare un template,
fermare il sistema in caso di errore e trovare i log, cinque azioni concrete
verificate una per una, non date per scontate. Esiste anche una skill chiamata
`onboarding` (sia in `.claude/skills/onboarding/` di progetto sia nella libreria
globale), ma è costruita per un dominio diverso: ottimizzare l'attivazione di
utenti dentro un prodotto SaaS dopo la registrazione (aha moment, checklist di
attivazione, empty state, tour guidati) — utile per Digital Empire quando vende o
costruisce prodotto software, non per il processo di accoglienza di un cliente
agency descritto in questo capitolo. Il gap è reale: la sequenza dei cinque punti
del kickoff e la tecnica del "taking in charge" restano, per ora, conoscenza da
applicare a mano nella prima chiamata, non ancora un passo scritto dentro
`delivery-playbook`.
