# PARTE PRIMA — IL METODO DIGITAL EMPIRE

## Introduzione

Digital Empire è un'agenzia CRO organizzata come una fabbrica: **sprint produttizzati di 2-4
settimane, pay-on-performance**, con un posizionamento dichiarato fin dal primo contatto —
*"l'agenzia progettata per essere licenziata"*. Non è uno slogan vuoto: è la conseguenza diretta
di come è costruita l'intera macchina di consegna, descritta per intero più avanti in questa
Parte (§4, *Consegna*).

Il metodo che segue non è teoria. È il sistema operativo reale — reparti, gate, script,
soglie numeriche — con cui l'agenzia acquisisce, vende, consegna e scala. Ogni meccanismo
descritto qui sotto vive in un file eseguibile del repository di produzione: non un principio
astratto, ma una skill, uno script o un contratto di handoff che gira ogni giorno.

La Parte Seconda di questo libro (i capitoli che seguono) raccoglie la formazione esterna —
quello che altri hanno insegnato e da cui questo metodo è nato, confrontato e in alcuni punti
confermato. Le due parti restano separate apposta: qui sotto c'è cosa facciamo NOI, con le
nostre soglie e i nostri numeri; nella Parte Seconda, cosa dicono le fonti che abbiamo studiato.

L'agenzia è organizzata in **reparti** con handoff strutturati (oggetti JSON che passano da un
reparto all'altro, es. `HC-A3-A4-contratto`), non in un unico flusso indifferenziato: A1-RICERCA
(chi troviamo), A3-PREVENTIVI (chi paghiamo per il problema che ha), A4-DELIVERY (chi consegniamo
e a chi rendiamo il cliente autonomo). Ogni reparto ha propri **gate** — controlli che bloccano
il passaggio allo step successivo se un requisito non è soddisfatto, non semplici promemoria.

---

## 1. Acquisizione — chi cerchiamo, e come lo riconosciamo

### 1.1 Il principio: concentrazione, non volume

Prima ancora del canale, viene il bersaglio. Il principio guida dell'acquisizione in Digital
Empire non è "più contatti possibile", è **concentrazione di buyer reali** dentro qualunque
lista o pubblico si stia lavorando — un'audience piccola e precisa batte sempre una grande e
generica. La cifra di riferimento adottata in casa (92% di ICP match su un pubblico concentrato
contro 2% su uno generico) viene da una fonte esterna studiata a fondo e riportata per intero
nel Capitolo 1 della Parte Seconda; qui conta la conseguenza operativa: ogni lead che entra in
pipeline passa prima da una **scheda ICP** esplicita, non da un giudizio a occhio.

### 1.2 La scheda ICP

Ogni nicchia lavorata ha una scheda ICP scritta (skill `icp-radar`), aggiornata dopo ogni ciclo
di vittorie/perdite, con questi campi obbligatori:

- **Criteri di qualifica** — `must_have` (dimensione azienda, settore, canale raggiungibile,
  problema evidente), `nice_to_have`, `esclusioni` esplicite (es. aziende con procurement lento).
- **Trigger evento** — l'evento specifico che ha spinto il cliente ad agire *proprio ora* (un
  cliente perso, un obiettivo di fatturato mancato, un concorrente comparso). Non si indovina:
  si ricava chiedendo, per ogni cliente già vinto, "cosa è successo poco prima che ci cercasse?".
  Un ICP senza trigger dice CHI è il cliente ma non QUANDO è comprabile — ed è la differenza fra
  un messaggio che sembra spam e uno che arriva al momento giusto.
- **Scoring matrix** — ogni criterio pesato (es. email valida 30, dimensione in range 25, settore
  in target 25, problema evidente nel testo del sito/profilo 20), soglia di passaggio fissata a
  **70 su 100**: sotto soglia, il lead non entra nemmeno in qualifica.

**Il test del riconoscimento in un secondo.** Una scheda ICP è scritta bene se, leggendo il
messaggio che ne deriva, il prospect pensa "questo sono io" entro un secondo. Il modo con cui lo
si verifica in casa è scrivere due versioni dello stesso messaggio e confrontarle: una versione
generica ("aiutiamo le aziende ad aumentare il fatturato" — tenere aperte tutte le opzioni
equivale in pratica a non parlare a nessuno) contro una versione operativa che nomina segmento,
fascia numerica precisa, risultato con un tempo dato, meccanismo e dolore riconoscibile. Se non
si riesce a scrivere la seconda versione, mancano quasi sempre due soli campi nella scheda:
`trigger_evento` o `dolore_specifico`. Si riempiono prima di passare la scheda al reparto
ricerca, mai dopo.

### 1.3 I canali

L'acquisizione lavora su più canali in parallelo, ognuno con un motore proprio:

- **Cold email** — sequenze di 3-5 messaggi, gap crescenti fra un invio e l'altro, ogni email
  autosufficiente (il destinatario potrebbe non aver letto le precedenti), un solo invito
  all'azione a bassa frizione per email. Principio guida: il lettore deve vedere la propria
  situazione riflessa, mai la nostra — "tu/il tuo" domina su "io/noi". La sequenza intera non
  supera 1-2 mesi: oltre quella finestra il tasso di risposta crolla e diventa rumore.
- **Canali diretti automatizzati** (WhatsApp e simili) — invio automatico ma a **ritmo umano**
  (decine di secondi fra un messaggio e l'altro, mai a raffica), **cap giornaliero** esplicito
  per account, arresto automatico ai primi segnali di blocco della piattaforma. Il principio non
  negoziabile è lo stesso dell'email: personalizzazione reale legata al problema del
  destinatario, non un campo variabile compilato a macchina.
- **LinkedIn** (organico e diretto) — trattato per intero nel Capitolo 1 della Parte Seconda,
  dove le due strade opposte (contenuto vs messaggio diretto) sono confrontate fonte per fonte.

### 1.4 Cosa NON facciamo

Nessun invio di massa senza scheda ICP a monte. Nessuna personalizzazione che si riduce a un
nome compilato in automatico: la regola di casa è che un lead riconosce lo schema di un template
anche quando il proprio nome è presente — la vera personalizzazione richiede un dettaglio
specifico e verificabile, non solo una variabile sostituita.

---

## 2. Vendita — dalla conversazione al contratto

### 2.1 La postura: diagnosi, non pitch

Il principio che apre ogni call di vendita in Digital Empire è netto: **chi vende è un dottore,
non un venditore**. Un dottore non entra nella stanza dicendo "compri questa medicina": fa
domande sui sintomi, diagnostica il problema vero, spiega la causa al paziente, e solo allora
propone la cura. Quando i primi tre passi sono fatti bene, il paziente **vuole** la cura al
quarto passo — non serve convincerlo.

La misura con cui questo principio si controlla, call dopo call, è la **regola del rapporto
parola**: chi vende deve parlare al massimo il 30% del tempo, il prospect il restante 70%. Chi
parla di più sta vendendo (tasso di chiusura osservato 8-12%); chi ascolta di più sta
diagnosticando (tasso di chiusura osservato 30-45%, 3-5 volte meglio). Dopo ogni call, si stima
onestamente questa percentuale — è una metrica di processo tanto quanto il fatturato lo è di
risultato.

Sette principi non negoziabili governano ogni call: (1) la call è una diagnosi, mai un pitch —
non si apre mai parlando di sé o dell'agenzia; (2) il valore precede sempre la vendita — il
prospect deve sentirsi in debito prima che l'agenzia venga anche solo nominata; (3) si ascolta il
70%, si parla il 30%, e dopo ogni domanda cala il silenzio per lasciare elaborare la risposta;
(4) mai tattiche manipolative — niente urgenza falsa, niente scarsità inventata; (5) un no si
rispetta sempre, con grazia — un no ben gestito produce referral futuri e lascia la porta aperta;
(6) il rapporto viene prima della vendita — è meglio perdere una vendita che la reputazione;
(7) se il prospect non è quello giusto, si declina — dire no al cliente sbagliato protegge il
brand.

### 2.2 La struttura della discovery

La fase di scoperta segue una sequenza fissa a quattro tempi: **rapporto** (2-3 minuti, script
diversi a seconda della provenienza del lead — da contenuto, da referral, da outreach diretto,
il più delicato dei tre), **le domande di scoperta** (15-20 minuti, dodici domande organizzate
in quattro blocchi — situazione attuale, il problema, il desiderio, qualificazione silenziosa),
**diagnosi live** (5-7 minuti — si riformula il problema reale, se ne identifica la causa, si
costruisce il collegamento emotivo) e **valore gratuito** (8-10 minuti — tre consigli
strutturati e applicabili subito, indipendentemente dal fatto che il prospect firmi o meno). Solo
dopo questi quattro tempi si passa alla proposta economica.

### 2.3 Quando la call è lo step giusto

La discovery call non è sempre il passo corretto nel percorso di un lead: è il terzo gradino di
un percorso a tre step (con varianti più leggere prima di arrivarci), e diventa la scelta giusta
quando il valore del contratto è alto — la soglia di mercato osservata e adottata in casa è
**3.000 €**. Sotto quella cifra un percorso self-service può chiudere da solo, senza consumare
uno slot di call; sopra, la call strutturata è lo step che chiude davvero.

Ogni call produce un **brief strutturato** (non appunti sparsi): problema in termini del
cliente, livello di consapevolezza (consapevole/non consapevole), dolore quantificato se
disponibile, stack tecnico attuale, vincoli d'ambiente, segnali di budget, competitor
menzionati, e due campi che bloccano la fase successiva se mancanti — il **trigger evento**
(perché proprio ora) e il **prossimo passo con data e ora precise già in calendario**. Senza
quest'ultimo, la regola di casa è netta: la discovery call non è stata completata, qualunque
buona impressione abbia lasciato — un "ti faccio sapere" senza data è la causa più comune di
trattative che muoiono da sole dopo una call andata bene.

---

## 3. Prezzo — il preventivo come lettera di vendita

### 3.1 Il principio cardine

Un preventivo di Digital Empire non è una lista prezzi: è un documento che dimostra di aver
capito il problema del cliente meglio di chiunque altro glielo abbia proposto. Tutto ruota
intorno al problema — il documento non dice "ecco cosa facciamo", dice "ecco come risolviamo
il tuo problema specifico e cosa otterrai".

Conseguenza diretta: **il prezzo non si dà mai prima della discovery**. Non esiste un listino
pubblico da citare a chi chiede "quanto costa" prima ancora di aver parlato del problema.

### 3.2 La struttura in otto sezioni

Ogni preventivo segue una struttura fissa: copertina, introduzione/perché noi, il problema del
cliente riformulato (la prova di aver ascoltato davvero), i risultati attesi in termini di
outcome misurabili — mai elenchi di feature —, i deliverable esatti, l'investimento (**sempre
tre opzioni, mai un listino a voce singola**), la call to action con una scadenza, i termini
contrattuali essenziali.

Regole di prezzo non negoziabili: tre opzioni sempre (essenziale / professionale / full
service), un margine di sicurezza del 10% applicato prima di scrivere il numero mentale, numeri
tondi (2.000 €, non 1.980 €), **nessuno sconto** — se il cliente chiede di meno, si riduce lo
scope, non il prezzo. Alla presentazione, il documento si condivide sempre a schermo in call,
mai per email senza commento: dopo aver detto il prezzo, cala il silenzio — non ci si giustifica
prima che sia il cliente a chiederlo.

---

## 4. Consegna — l'agenzia progettata per essere licenziata

### 4.1 I tre prodotti a prezzo fisso

La consegna in Digital Empire non è un progetto su misura ogni volta: sono **tre prodotti
produttizzati**, ognuno con un runbook giorno per giorno e un tetto di **sette giorni** dal
momento in cui l'ambiente del cliente è verificato conforme:

| Prodotto | Prezzo | Cosa consegna |
|---|---|---|
| Outreach Factory | 4.000 € | pipeline di acquisizione automatizzata installata sul server del cliente |
| Content Factory | 3.500 € | motore di produzione contenuti parametrizzato sul brand del cliente |
| Second Brain | 2.500 € | vault/workspace di conoscenza strutturato, personalizzato per la nicchia |

Il countdown dei sette giorni non parte all'atto della firma: parte quando l'ambiente del
cliente supera una verifica di conformità esplicita (sistema operativo, accessi, credenziali,
dipendenze installabili). Se l'ambiente non è conforme, la consegna si ferma prima ancora di
iniziare e il blocco viene documentato e comunicato — non si prosegue "a vista".

### 4.2 Il Gate Delivery

Nessuna consegna si dichiara chiusa senza che **ogni** voce di questa checklist sia verificata:
il sistema funziona sul server del cliente (non solo in locale, dentro l'agenzia); è stata
eseguita una run di test reale, non simulata; il training è stato erogato con materiale
consegnato; il pacchetto di handover è completo; la UAT (User Acceptance Test) è **firmata** dal
cliente; il cliente ha dimostrato autonomia operativa durante la sessione di verifica; non resta
nessuna dipendenza residua dall'agenzia.

L'ultimo giorno del runbook, in tutti e tre i prodotti, è identico nella sostanza: **è il
cliente, non l'agenzia, a eseguire la run finale da solo** — è quella la prova reale che il Gate
Delivery può considerarsi superato.

### 4.3 Il pacchetto di autonomia

Il pacchetto di handover è, letteralmente, la prova tangibile del posizionamento dell'agenzia.
Contiene una guida operativa passo-passo, un runbook per i controlli quotidiani, le domande
frequenti raccolte durante il training, un indice delle credenziali usate (**mai i valori
reali** — solo nomi e scopo di ogni variabile, i valori restano nell'ambiente del cliente), una
licenza d'uso che chiarisce che il codice/configurazione è di proprietà del cliente, un indice
dei video di training registrati in sessione, e una checklist di autonomia a cinque punti,
firmabile: il cliente sa avviare il sistema da zero, sa leggere l'esito di una run, sa
aggiungere o modificare un template, sa fermare il sistema in caso di errore, sa dove trovare e
come interpretare i log.

Dopo la consegna, un periodo di supporto di **90 giorni** resta attivo come rete di sicurezza —
ma il sistema, dal settimo giorno, è già nelle mani del cliente.

---

## 5. Scala — reparti, non eroi

La struttura che rende ripetibile tutto quanto sopra non è una singola persona che fa tutto: è
un'organizzazione a **reparti** con confini netti e **handoff strutturati** fra l'uno e l'altro
— oggetti dati (non conversazioni informali) che passano da un reparto al successivo, ognuno con
i propri campi obbligatori. Un reparto di ricerca (che trova e qualifica i lead secondo la
scheda ICP), un reparto preventivi (che trasforma un brief di discovery in un'offerta), un
reparto delivery (che esegue il runbook di sette giorni e produce l'autonomia del cliente) — e
un reparto tesoreria, separato da tutti, che conta cosa entra e cosa esce senza mai stimare un
numero che non può verificare sul disco.

Ogni passaggio fra reparti è un potenziale punto di rottura silenziosa (un dato che si perde,
un'assunzione mai verificata) — per questo ogni handoff porta con sé i campi che il reparto
successivo userà per decidere, non solo un riassunto discorsivo. È lo stesso principio, applicato
all'organizzazione invece che a un singolo documento, che governa il preventivo (mai dare un
numero senza i dati della discovery) e la consegna (mai dichiarare fatto senza la UAT firmata):
**nessun passaggio si dà per scontato, ognuno si verifica**.
