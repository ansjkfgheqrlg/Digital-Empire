# IL LIBRO DELL'AGENCY

### Come Digital Empire acquisisce, vende, consegna e scala — e la formazione da cui il metodo nasce

*Documento pubblico ufficiale — Digital Empire, 2026-09-10*

---

## Cos'e' questo documento

Due parti, dichiarate e separate.

**PARTE PRIMA — IL METODO DIGITAL EMPIRE.** Il nostro sistema operativo reale per acquisire,
vendere, consegnare e scalare un'agenzia CRO: reparti, gate, soglie numeriche, script. Non teoria
- il sistema che gira ogni giorno in produzione.

**PARTE SECONDA — LA FORMAZIONE.** La conoscenza esterna da cui quel metodo e' nato, confrontato,
e in alcuni punti confermato. Tre capitoli, organizzati per fase (Acquisizione / Vendita e Prezzo /
Consegna e Scala), ognuno fedele alle fonti originali senza tagli ne' riassunti - ogni citazione
porta la sua fonte esatta (video e minuto, o KA-id dell'atomo di conoscenza).

**Regola di costruzione non negoziabile**: mai riassunti. Dove una fonte insegna qualcosa, quel
qualcosa resta nel libro per intero, con la citazione che lo ancora. Comprimere per brevita' e'
lavoro sbagliato.

## Indice

**Parte Prima — Il Metodo Digital Empire**
- Introduzione
- 1. Acquisizione — chi cerchiamo, e come lo riconosciamo
- 2. Vendita — dalla conversazione al contratto
- 3. Prezzo — il preventivo come lettera di vendita
- 4. Consegna — l'agenzia progettata per essere licenziata
- 5. Scala — reparti, non eroi

**Parte Seconda — La Formazione**
- Capitolo 1 — Acquisizione Clienti (Paolo Trivellato, Giovanni Beggiato)
- Capitolo 2 — Vendita e Prezzo (Will Barron, Giovanni Beggiato)
- Capitolo 3 — Consegna, Servizio e Scala (Giovanni Beggiato x2, Riccardo Belli Contarini)

**Copertura e fonti** (in coda al documento)

---

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

---

# Capitolo 1 — Acquisizione Clienti

## Due strade per lo stesso canale

LinkedIn è, per entrambe le fonti di questo capitolo, il campo di battaglia intero. Ma le due
fonti lo attraversano in direzioni opposte, e la distanza tra loro è il filo conduttore di
tutto quello che segue.

Paolo Trivellato ha portato la sua agenzia a **$1.294.700 di fatturato in un anno, attribuiti
interamente a LinkedIn**, con **31.000 follower**, **$0 spesi in ads** e **zero cold outreach**.
Il suo sistema funziona costruendo un magnete: contenuto che attira solo i decisori giusti,
un profilo che li converte da solo, due meccanismi che trasformano l'attenzione passiva in call
prenotate. Nessuno scrive per primo a nessuno. Sono i prospect a bussare.

Giovanni Beggiato ha costruito **oltre 50.000 follower nell'ultimo anno** e "poco più di
$100.000" di fatturato dichiarato — ma il dato più importante che rivela è un altro: **meno del
5% del fatturato della sua agenzia AI viene dai contenuti**. La fonte reale sono **circa 100 DM
a settimana** (KA-004, KA-005). Il suo sistema funziona al contrario: si scrive per primi, a
freddo, a persone che non hanno mai sentito parlare di te, e si costruisce nel messaggio stesso
— non nel profilo, non nel post — tutta la fiducia necessaria a ottenere una risposta.

Un'agenzia magnete contro un'agenzia che tira frecce. Nessuna delle due nega l'altra: sono
i due estremi misurabili dello stesso canale. Lette insieme, danno una mappa completa di quando
usare l'una e quando l'altra — l'ultima sezione di questo capitolo prova a tracciarla.

Un'ultima cosa prima di entrare nel merito: sono fonti esterne. Quello che segue è ciò che
Trivellato e Beggiato insegnano nei rispettivi video, non ciò che Digital Empire fa. Dove le
fonti stesse confrontano il proprio insegnamento con la pratica di Digital Empire — Trivellato
lo fa esplicitamente segnalando due "pezzi mancanti" nello stack, Beggiato lo fa scoprendo un
framework quasi identico già in uso — quel confronto resta parte del materiale del capitolo,
ma parla delle fonti, non a nome dell'azienda.

---

## Trivellato — la strada organica

### Il sistema a tre componenti che girano insieme

Il walkthrough di Trivellato (18m49s, su una board Miro condivisa) non presenta la crescita
organica come una lista di tattiche isolate, ma come tre pezzi che si alimentano a vicenda:

```
1) CONTENUTO CHE ATTRAE BUYER, NON FOLLOWER
   -> Named Problem Posts (nomini un problema costoso gia' pensato dall'ICP)
   -> Surfaced Problem Posts (fai emergere un problema non ancora nominato,
      tipicamente un mini-audit a 5 passi con metriche di settore)
   -> Gate pre-pubblicazione: "The One-Sentence Post Test"

2) UN PROFILO CHE CONVERTE IL TRAFFICO CHE IL CONTENUTO GENERA
   -> Ricostruito come landing page di vendita, non un CV

3) DUE MECCANISMI CHE TRASFORMANO L'ENGAGEMENT IN CALL PRENOTATE
   -> Meccanismo 1: Lead Magnet Posts (commento + connessione -> risorsa gratuita)
   -> Meccanismo 2: Profile View Outreach (chi visita il profilo = segnale caldo)
```

Se manca uno dei tre pezzi, gli altri due perdono valore: contenuto ottimo con un profilo
rotto disperde traffico che non tornerà; un profilo perfetto senza contenuto non riceve mai
visite; entrambi senza un meccanismo di conversione restano semplice brand awareness, mai
fatturato.

### La metrica che sostituisce il follower count: buyer concentration

Il punto di partenza del sistema è un cambio di metrica. Trivellato lo mette in scena con un
confronto diretto tra due modelli:

```
THE CONSUMER SOCIAL MODEL (sbagliato per B2B)     THE BUYER CONCENTRATION MODEL
─────────────────────────────────────             ──────────────────────────────
200.000 follower, solo il 2% e' ICP reale    vs    31.000 follower, la stragrande
"go big, go broad" — insegue il reach              maggioranza sono decision-maker esatti
addestra l'algoritmo a mostrare il contenuto        ogni conversione e' un contratto
a chi non comprera' mai                             $10K-$100K, non un ebook da $20
```

La frase che riassume il principio compare in un box verde a schermo, a 3:10 nel video:

> **"THE REAL METRIC — You do not need 500,000 followers. You need the right 5,000 — and a
> system that keeps pulling more of them in."**

Il numero che dà corpo alla metrica: **92% di ICP match sui 31.000 follower** dell'autore,
contro un **2%** tipico di un'audience generica da 200.000. Non è la dimensione dell'audience a
determinare il fatturato, è la sua concentrazione di acquirenti reali.

Trivellato dichiara anche, a voce (non mostrato a schermo, quindi con un grado di verifica
inferiore rispetto ai dati grafici): oltre **60 clienti gestiti**, **3-5$ generati per ogni
follower**, un singolo post con appena ~15 like che ha prodotto un cliente da $10-16K, clienti
con appena 200 follower che hanno prenotato **7 call qualificate in pochi giorni**, e una stima
per cui 10.000 follower possono valere **$50K-$100K/mese** come canale marketing per alcuni
operatori.

### Il contenuto: due tipi di post, un solo gate

Il primo componente del sistema si divide in due formati:

- **Named Problem Posts** — si nomina un problema che il pubblico ICP ha già in testa e che gli
  costa denaro. Non si spiega il problema da zero: lo si etichetta, perché il lettore lo
  riconosca immediatamente come proprio.
- **Surfaced Problem Posts** — si fa emergere un problema che il pubblico non ha ancora
  nominato da solo, tipicamente attraverso un mini-audit a 5 passi corredato di metriche di
  settore. Qui il valore del post è la diagnosi stessa.

Prima di pubblicare qualsiasi post di questi due tipi, Trivellato applica un gate esplicito,
"The One-Sentence Post Test":

> "Can a qualified prospect read this and say 'yes — that is exactly my situation'? If not,
> wrong post."

Se un prospect qualificato non può rispondere "sì, è esattamente la mia situazione" dopo aver
letto il post, il post è sbagliato e va riscritto o scartato — non importa quanto sia ben
scritto o quanto engagement potrebbe generare tra un pubblico più ampio.

### Il profilo come sales page

Il secondo componente è, secondo Trivellato, quello che vale più della metà del sistema — e
la citazione che lo sostiene è netta:

> *"Fixing the profile beats improving content. The traffic is already arriving. A broken
> profile just lets it silently evaporate."*

La logica è che il contenuto genera già traffico verso il profilo: se il profilo non converte
quel traffico, il lavoro fatto sul contenuto va sprecato in silenzio, senza nemmeno un segnale
di fallimento visibile. Il profilo va quindi trattato come una landing page di vendita, non
come un curriculum. La tabella integrale che Trivellato usa per illustrare il cambio:

| The Mistake | The Fix |
|---|---|
| Job title used as the headline | Headline: who you help + outcome delivered, nothing else |
| Custom button links to a generic homepage | Custom button: direct link to a booking calendar |
| Featured section left empty | Featured section: case study, video testimonial, methodology breakdown |
| Profile reads like a career history, not a sales page | — |

Trivellato applica il principio su di sé come primo esempio: le prime due parole del suo
stesso headline sono "Agencies and SaaS" — il suo ICP esatto, dichiarato senza ambiguità nella
prima riga che chiunque legge.

### I due meccanismi che chiudono il loop

Contenuto e profilo, da soli, generano solo attenzione passiva. Il terzo componente del
sistema sono due meccanismi espliciti che trasformano quell'attenzione in azione.

**Meccanismo 1 — Lead Magnet Posts.** Il post chiede al lettore un commento più una richiesta
di connessione, in cambio di una risorsa gratuita. Ogni persona che commenta diventa una
connessione di 1° grado, e da quel momento vede tutti i post futuri dell'autore nel proprio
feed. Il risultato dichiarato: **300-1.000 connessioni ICP qualificate per ogni post** di
questo tipo — non follower generici, ma persone che si sono auto-selezionate rispondendo a un
problema specifico nominato nel post.

**Meccanismo 2 — Profile View Outreach.** Chi visita ripetutamente il profilo di qualcuno sta,
secondo Trivellato, facendo una ricerca attiva — è un segnale di interesse che la maggior parte
delle persone lascia cadere. Lo script che propone di usare, riportato "word for word":

> "Noticed you have been checking out my profile — curious what caught your attention?"

Sul tasso di risposta di questo script, il video stesso contiene una discrepanza dichiarata e
non risolta dall'autore: la grafica a schermo mostra **40-50%**, ma la dichiarazione a voce,
poco dopo, corregge a **20-50%**, indicando che il tasso dipende dalla qualità del profilo e
dei contenuti già pubblicati. Trivellato descrive questo secondo meccanismo come "il pezzo che
la maggior parte delle persone lascia scoperto":

> *"A profile visit is not a booked call. [...] without a specific mechanism, it just sits
> there."* [The Gap Most People Leave Open]

### Chiusura della sezione: la scala non è il punto

Trivellato chiude il ragionamento sulla dimensione dell'audience con una frase che smonta
l'obiezione più ovvia — "ma io non ho 31.000 follower":

> *"31,000 followers is almost beside the point — this exact system works at 5,000. Build it
> before the audience feels 'big enough' to bother."*

Il sistema, cioè, non richiede scala per funzionare: richiede che i tre componenti — contenuto
mirato, profilo convertente, meccanismi di conversione — siano tutti presenti. La scala arriva
dopo, come conseguenza del sistema che gira, non come sua precondizione.

**Un limite dichiarato della fonte**: il video non mostra mai uno screenshot di un post reale
pubblicato — i due esempi di Named/Surfaced Problem Post sono raccontati solo a voce, con cifre
esplicitamente definite "mock" dallo stesso Trivellato — e non mostra il profilo LinkedIn reale
dell'autore, né analytics nativi di LinkedIn, né conversazioni DM reali, né alcun CRM. Il
grafico del fatturato annuo non riporta valori mensili leggibili, solo il totale e gli estremi
dell'asse temporale. Il video contiene inoltre un segmento dichiaratamente promozionale
(presentazione del servizio dell'agenzia, minuti 0:34-0:52, e CTA finale nell'ultimo minuto).

---

## Beggiato — la strada attiva

### L'autorità come primo ingrediente, non come vanto

Beggiato apre il suo video (33m20s) dichiarando a voce: *"Ho generato più di 50.000 follower
nell'ultimo anno solo con LinkedIn e poco più di $100.000."* La dichiarazione è seguita
immediatamente da una prova visiva, non solo verbale: uno screenshot reale di LinkedIn
Analytics che mostra **51.747 follower totali** e una crescita di **+4.828,3%** sui 365 giorni
precedenti, con un grafico cumulativo che sale da quasi zero (aprile 2025) a circa 52.000
(aprile 2026).

A questo si aggiunge una prova di ranking esterno: sul sito Favikon, Beggiato risulta **#1
assoluto** nella classifica "Top 200 Creators · IT & Tech · LinkedIn · Luxembourg" (LinkedIn
Score 93,7/100, 51,7K follower LinkedIn più 10,7K YouTube, crescita +6,95%). Nella classifica
generale, tutte le categorie, è **3° assoluto** in Lussemburgo — dietro solo al primo
classificato e al Vice Primo Ministro lussemburghese Xavier Bettel (argento), davanti al Primo
Ministro Luc Frieden.

Il motivo per cui questi numeri aprono il video non è l'autocelebrazione. Subito dopo averli
mostrati, Beggiato rivela che **meno del 5%** del fatturato della sua agenzia AI nell'ultimo
anno è arrivato da post e content creation — la fonte reale del fatturato sono **circa 100 DM a
settimana**. I numeri di apertura, cioè, sono la stessa cosa che il framework richiederà più
avanti a chiunque scriva un cold DM: una "proof che la avete" — l'unica vera moneta verso uno
sconosciuto sono i risultati verificabili, non l'affermazione della propria professionalità.
Beggiato applica su di sé, prima ancora di enunciarlo esplicitamente, il principio che poi
insegna.

### Le cinque caratteristiche di un cold DM

Il cuore del video è un framework scritto per intero su una lavagna Excalidraw, titolo "LE
CARATTERISTICHE DI UN COLD DMs", usato per il resto del video per giudicare con un ✓/✗ tre DM
reali ricevuti dall'autore:

1. **Personalizzato** — non basta inserire un nome nel messaggio: se il destinatario riconosce
   lo schema di un template dietro la variabile (per esempio "Salve {nome}"), il punto viene
   bocciato comunque. L'esempio di personalizzazione vera che Beggiato contrappone al
   placeholder generico: *"Ho visto che hai una bellissima felpa verde nell'ultimo video [...]
   mi è piaciuta molto"* — un dettaglio specifico realmente osservato, non un campo variabile.

2. **Chiarire chi sei e perché devo leggere** — motivato con una prova concreta tratta dal
   proprio calendario: uno screenshot Typeform (oscurato per privacy) con **157 risposte**
   ricevute nel periodo, più altre richieste di consulenza. *"ho ricevuto 157 [...] richieste di
   consulenza [...] e dovete avere un obiettivo quando scrivete un DMS"* — un destinatario con
   un calendario già pieno non ha motivo di leggere un messaggio che non chiarisce
   immediatamente chi scrive e perché.

3. **Dare qualcosa** — introdotto dal concetto scritto in rosso sulla lavagna, **"NESSUNO È
   SPECIALE"**: *"quando entriamo nel mondo dell'imprenditoria [...] dobbiamo un po' ucciderci
   l'ego"*. La propria professionalità, dice Beggiato, *"vale, ma non ha alcun valore quando e
   se non è in target con quello che state vendendo"*: l'unica vera moneta di credibilità verso
   uno sconosciuto sono i case study verificabili, non l'esperienza dichiarata a parole.

4. **Micro commitment** — principio di coerenza comportamentale: *"nel momento in cui noi
   chiediamo e una persona dice già di sì ad un qualcosa, anche se piccolo, è più semplice che
   poi l'altra persona dica di sì [...] alle nostre richieste successive"*.

5. **Poco attrito** — l'azione richiesta al destinatario per ottenere o continuare la
   conversazione deve costare pochissimo. Nel template riscritto più avanti nel video, il
   micro-commitment a basso attrito è un singolo link Google Drive da mandare — *"perché
   l'attrito che ho è registrare il video e poi devo mandartelo"*, cioè l'attrito lo assorbe chi
   scrive il DM, non chi lo riceve.

### Effetto Barnum e Rainbow Ruse

Le due leve psicologiche che permettono di scalare la personalizzazione senza scriverla da
zero per ogni destinatario sono definite per intero sulla lavagna, verbatim:

> **EFFETTO BARNUM: frase "unversali-specifiche" che sembrano personalizzate**
> (refuso a schermo: "unversali" per "universali", riportato così com'è scritto)
> "Questa è la base di ogni oroscopo o lettura della mano. Consiste nel fare affermazioni
> "universali-specifiche": frasi che sembrano personali ma che valgono per chiunque."
> Esempio: "Hai una grande necessità di piacere agli altri, ma tendi a essere molto critico con
> te stesso."

> **RAINBOW RUSE: L'Inganno dell'Arcobaleno**
> "Si attribuisce a una persona un tratto della personalità e il suo esatto opposto nello stesso
> momento."
> Esempio: "Di solito sei una persona socievole e aperta, ma ci sono momenti in cui ti chiudi in
> te stessa e diventi molto riservata."

Beggiato non presenta queste due leve come un inganno puro, ma come un compromesso statistico
che giustifica esplicitamente disegnando un cerchio diviso in una fetta verde larga (la
maggioranza per cui il messaggio generico "funziona" e si sente rispecchiata — associazioni
tipo legami "FAMILIARE" o "EVENTI" di networking) e una fetta rossa sottile (la minoranza che
rifiuta: *"Madonna ma cosa fai? Queste cose qui per me non vanno bene"*). La sua conclusione
numerica esplicita:

> *"però nel 99% dei casi questa frase può essere può essere corretta, no?"*

Lo stesso principio, secondo Beggiato, giustifica più avanti anche una "proof" costruita
artificialmente (vedi lo schema PROOF più sotto): se il contenuto piace al destinatario, questi
non si sofferma a verificarne la provenienza — conta che il lettore si riconosca, non che la
frase sia irripetibile per lui solo.

### I tre DM reali smontati punto per punto

Beggiato applica il framework a cinque punti a tre DM reali che ha ricevuto, riportati per
intero e giudicati uno per uno.

**DM 1 — "Shakeel"** (Full Stack Developer, headline dichiarata "apposta vaga" per dimostrare
che il framework vale per qualsiasi settore), testo integrale:

> "Hi, I'm Shakeel. I spend most of my time working on web products and solving practical
> problems for teams. I'm currently open to new collaborations. Some recent work:
> https://[nome-progetto-oscurato].vercel.app/ Best,"

Verdetto: bocciatura totale, **0/5**.
1. Personalizzato ✗ — *"non c'è nemmeno il mio nome"*.
2. Chiarire chi sei e perché devo leggere ✗ — non chiarito.
3. Dare qualcosa ✗ — *"non ho ricevuto niente, anzi mi stai prendendo qualcosa che è il mio
   tempo"*.
4. Micro commitment ✗.
5. Poco attrito ✗ — *"per avere poco attrito devo avere poco attrito nel [...] ricevere questo
   qualcosa e io non sto ricevendo niente"*.

**DM 2 — "Zeekeo"** (Operations Executive, secondo grado LinkedIn), oggetto "Early-stage growth
question", testo integrale:

> "Hi Giovanni, congrats on getting AI Automation Founders off the ground. Quick one, when
> things get busy, do you find follow-up slips a bit, or have you already got that side
> sorted?"

Verdetto: **1/5**, il migliore dei tre sulla sola personalizzazione ma bocciato sul resto.
1. Personalizzato ✓ — nomina "Giovanni" e la community specifica "AI Automation Founder".
2. Chiarire chi sei e perché devo leggere ✗ — *"non so chi sia"*.
3. Dare qualcosa ✗.
4. Micro commitment ✗.
5. Poco attrito ✗ — *"non ricevo niente"*.

Nota dell'autore su questo DM: è comunque scritto meglio della media, *"probabilmente l'ha
scritto a mano o ha usato qualche automazione decente"* — ma il resto non soddisfa alcun
criterio.

**DM 3 — video editor freelance** (quello scelto per la riscrittura completa più avanti), testo
integrale:

> "Salve Giovanni, mi chiamo [nome oscurato] e sono una video editor freelance. Sto cercando
> collaborazioni con creator YouTube che vogliono migliorare qualità e ritmo dei loro contenuti.
> Offro editing personalizzato che include: • montaggio dinamico • ottimizzazione del ritmo
> narrativo • audio e color correction • testi, grafiche ed effetti (se richiesti) I miei prezzi
> partono da €60 a video, variabili in base a durata e livello di editing. Sono disponibile a
> valutare anche collaborazioni continuative o pacchetti mensili. Se ti interessa, posso
> inviarti alcuni video che ho editato di recente. Grazie per il tuo tempo, [nome oscurato]"

Verdetto: il peggiore dei tre nonostante nomini il destinatario.
1. Personalizzato ✗ — controintuitivo: nomina "Giovanni", ma Beggiato riconosce lo schema di
   un template "Salve {nome}" dietro la variabile e boccia comunque il punto.
2. Chiarire chi sei ✓ parziale (dichiara di essere video editor) / perché devo leggere ✗.
3. Dare qualcosa ✗ — il paragrafo del prezzo viene cerchiato in rosso: *"mi sta chiedendo
   soldi, quindi in questo messaggio [...] sconsiglio vivamente"*.
4. Micro commitment ✗ — *"non mi sta chiedendo niente"*.
5. Poco attrito ✗ — annotazione manoscritta "CTA?": *"qual è la mia call to action? Cioè, devo
   risponderti sì, devo risponderti no, devo premere un..."* — nessuna azione concreta
   richiesta.

### I due template completi riscritti

Il DM 3 (video editor) viene riscritto da zero con variabili dinamiche, *"di modo tale che voi
possiate customizzarlo con AI"*, in una struttura a cinque blocchi: (1) Effetto Barnum di
apertura, (2) Rainbow Ruse sul pain, (3) case study di autorità, (4) offerta gratuita senza
vincoli, (5) micro commitment a bassissimo attrito più firma. Con questo template arriva, per
la prima volta nel video, un DM che supera l'intero framework a cinque punti, tutti ✓.

**Template CON autorità**, riportato parola per parola così come appare assemblato per intero
sul canvas:

> "Ciao {{nome}}, ho visto il tuo ultimo video su {{variabile}}. Finalmente qualcuno che parla
> di AI in modo chiaro e senza fronzoli. Canali come il tuo hanno un contenuto fantastico, ma
> spesso può non arrivare perché spesso il watch time non è dove dovrebbe. Sono Gino, ed ho
> aiutato *PERSONA* ad crescere da 5k subs a 50k subs in 3 mesi, creando video di alta qualità
> che hanno incrementato drasticamente il watch time. Mi farebbe piacere fare l'introduzione del
> tuo prossimo video gratuitamente. Ovviamente, non mi devi nulla e solo se performa secondo le
> tue aspettative, ti chiederò di lavorare assieme. Se ti interessa, tutto quello che mi serve è
> che tu mi mandi un link google drive da cui io posso caricare e scarica il video. Fammi
> sapere, Giovanni."

**Template SENZA autorità**, per il caso di chi non ha ancora un case study reale da citare:
Beggiato riscrive in diretta solo il terzo blocco (il case study), dichiarando esplicitamente
*"non cambierei niente che non fosse questa parte qui"* — tutto il resto resta invariato. Il
blocco 3 sostituito:

> "Sono Gino e sono un video editor specializzato nel creare "hook" ad alto engagement. Questo è
> un video che ho preparato per te: [LINK]"

Template completo risultante, ricostruito unendo i blocchi invariati confermati al nuovo blocco
3, per intero:

> "Ciao {{nome}}, ho visto il tuo ultimo video su {{variabile}}. Finalmente qualcuno che parla
> di AI in modo chiaro e senza fronzoli. Canali come il tuo hanno un contenuto fantastico, ma
> spesso può non arrivare perché spesso il watch time non è dove dovrebbe. Sono Gino e sono un
> video editor specializzato nel creare "hook" ad alto engagement. Questo è un video che ho
> preparato per te: [LINK]. Mi farebbe piacere fare l'introduzione del tuo prossimo video
> gratuitamente. Ovviamente, non mi devi nulla e solo se performa secondo le tue aspettative, ti
> chiederò di lavorare assieme. Se ti interessa, tutto quello che mi serve è che tu mi mandi un
> link google drive da cui io posso caricare e scarica il video. Fammi sapere, Giovanni."

### Lo schema PROOF: "la avete" o "la create"

Subito dopo la riscrittura "senza autorità", Beggiato introduce uno schema ad albero con due
rami — la scritta in blocco **"PROOF"** che si dirama in **"LA AVETE"** e **"LA CREATE"**:

> *"sarà eh rilevante è o la avete e quindi se la avete potete scriverla, se l'avete in settore
> meglio oppure la create."*

Nel mondo del cold DM, secondo Beggiato, l'unica cosa davvero rilevante per chi riceve il
messaggio è la prova (proof) reale: se il mittente la possiede già — un case study vero — la
scrive nel messaggio; se non la possiede, **la costruisce artificialmente** — per esempio un
video dimostrativo generico offerto a chiunque, con un placeholder tipo "[LINK]".

La regola sulla proof costruita: funziona lo stesso, perché se il contenuto o l'hook piacciono
al destinatario, questi non si sofferma a verificare con chi il mittente abbia realmente
lavorato —

> *"quello che succederà sarà che nella testa di questa persona non viene a pensare 'Ah, ok, ma
> con chi ha lavorato? Che cosa?'"*

A riprova, Beggiato racconta un aneddoto personale: dice di aver trovato tutto il proprio team
YouTube (LinkedIn incluso) proprio grazie a persone che gli hanno scritto messaggi generici di
questo tipo — offerte di lavoro gratuito dimostrativo, senza alcun vincolo se il risultato non
fosse piaciuto.

### La sequenza a tre step, corretta dal vivo

L'ultimo pezzo del framework nasce sottolineando la parola "follow-up" nel DM Zeekeo:

> *"i soldi non sono mai nel primo messaggio, neanche con le cold email, ma i soldi vengono
> generalmente nel secondo messaggio"*

Beggiato disegna tre cerchi verdi in sequenza 1→2→3 con i tassi di risposta attesi, e corregge
dal vivo il secondo numero mentre lo scrive: primo messaggio circa **20%**; secondo messaggio
scritto prima come "40%", poi corretto a voce e sulla lavagna a **50%**; terzo messaggio
**30%**:

> *"e sul terzo messaggio, anzi facciamola a 50 perché è estremamente probabile che al terzo vi
> accoltellino, ma è del 30%."*

Tassi finali dichiarati: **20% / 50% / 30%**. La motivazione a insistere fino al terzo
messaggio, invece di fermarsi al primo silenzio:

> *"se voi non fate questa parte qui, state lasciando [...] soldi sul tavolo [...] al primo
> messaggio non vi si risponde nessuno, al secondo, al terzo comincerete a ricevere risposte
> anche positive."*

---

## Le due strade a confronto

Messe una accanto all'altra, le due fonti non raccontano due tecniche in competizione: coprono
i due estremi opposti dello stesso canale, con logiche di fondo diverse ma un nucleo comune.

**Quando ha senso la strada organica di Trivellato.** Quando esiste (o si può costruire) un
posizionamento abbastanza netto da attrarre da solo un pubblico di decisori — la metrica guida
è la buyer concentration, non la dimensione dell'audience. È una strada più lenta a partire (il
contenuto deve accumulare fiducia prima di generare call), ma una volta che il sistema gira,
il costo marginale di ogni nuovo contatto tende a zero: nessun messaggio a freddo, nessun
budget ads. È la strada adatta a chi ha già qualcosa da dire con autorità in un settore
riconoscibile, e preferisce un flusso costante e prevedibile piuttosto che un impulso rapido.

**Quando ha senso la strada attiva di Beggiato.** Quando serve fatturato con un ciclo più
corto, o quando non esiste ancora un'audience organica sufficiente a generare traffico in
entrata. È una strada che richiede volume gestito (100 DM a settimana, nel caso di Beggiato) e
una sequenza disciplinata su tre contatti, ma può iniziare a produrre risposte da subito, senza
aspettare che un profilo o un contenuto accumulino autorità. È la strada adatta a chi ha bisogno
di controllare direttamente chi contattare e quando, invece di aspettare che sia il mercato a
farsi vivo.

**Cosa hanno in comune, nonostante la direzione opposta.** Entrambe le fonti rifiutano
esplicitamente il volume come sostituto della qualità:

- Trivellato lo dice sulla metrica dell'audience — 31.000 follower ben scelti battono 200.000
  generici, e lo stesso sistema "works at 5.000" follower, quindi la scala non è mai la
  precondizione.
- Beggiato lo dice sul singolo messaggio — un DM che nomina il destinatario per nome viene
  comunque bocciato se il lettore riconosce lo schema di un template dietro la variabile; la
  vera personalizzazione è un dettaglio specifico osservato, non un campo compilato.

Entrambe, inoltre, trattano la prova (proof) come merce più preziosa dell'affermazione di
autorità: Trivellato costruisce un profilo che mostra case study e testimonianze prima di
chiedere qualsiasi cosa; Beggiato apre il proprio video con numeri verificabili (screenshot
Analytics, ranking Favikon) prima di insegnare un framework che richiederà la stessa identica
prova a chiunque lo applichi — e quando la prova reale non c'è ancora, entrambe le fonti
accettano di costruirla artificialmente (l'audit-mockup di Trivellato nei Surfaced Problem
Post, il video dimostrativo generico di Beggiato nello schema PROOF) piuttosto che rinunciarvi.

E infine, entrambe rifiutano lo script rigido recitato a memoria: Trivellato chiede che ogni
post superi il test della frase singola ("è esattamente la mia situazione?"), Beggiato chiede
che ogni DM sia giudicato su cinque criteri indipendenti, non su una formula da copiare e
incollare. In entrambi i casi, il sistema scala, ma il giudizio su ogni singolo pezzo resta
manuale.

---

# Capitolo 2 — Vendita e Prezzo

*Nota al lettore: questo capitolo appartiene alla Parte 2 del libro — la formazione esterna da cui
il metodo operativo di Digital Empire (Parte 1) attinge. Tutto ciò che segue è ciò che due fonti
esterne insegnano sulla vendita e sul prezzo, non ciò che Digital Empire fa al proprio interno. Le
due fonti sono un video diagnostico di Will Barron sul sistema di vendita a 5 fasi, e la parte
dedicata al pricing di un tutorial di Giovanni Beggiato (agenzia Gentes AI) su un agente che genera
proposte commerciali. Ogni citazione riporta l'aggancio esatto — timestamp o riferimento al
fotogramma — così come compare nella fonte originale.*

---

## Apertura — perché il fatturato oscilla quando la vendita non è un processo

C'è un'osservazione da cui parte tutto il ragionamento di Will Barron, ed è più una diagnosi
clinica che un consiglio: nella maggior parte dei service business, il **delivery** — il modo in
cui il lavoro viene consegnato al cliente — è un processo documentato e ripetibile. Le **vendite**,
nella stessa identica azienda, restano ad-hoc, e partono sul serio solo quando si è disperati.

Il video costruisce questa tesi con un confronto visivo mostrato a schermo: da un lato la sequenza
del delivery, una fila di scatole collegate da frecce pulite, un processo lineare; dall'altro la
sequenza delle vendite, un percorso spezzato, uno scarabocchio, una scatola rossa che segnala dove
il sistema si rompe *(frame-045, @1:28)*. Il punto non è estetico: **il divario fra i due lati è la
causa del ciclo di boom-and-bust, non la mancanza di tempo.**

La meccanica di quel ciclo, così come viene descritta nel video, è quasi meccanica in senso
letterale: il fatturato scende, scatta la modalità panico, si va a caccia di nuovi clienti, si
torna occupati, si smette di vendere per fare il lavoro appena acquisito — e il ciclo ricomincia da
capo *(transcript, @1:51)*. È lo stesso schema, sempre uguale, che spiega perché un'azienda di
servizi può essere "brillante un mese e morta il successivo": non manca la domanda, manca un
sistema di vendita che giri indipendentemente dallo stato d'animo di chi vende.

La risposta proposta non è un trucco di chiusura o uno script migliore. È una barra a cinque
caselle, costruita progressivamente lungo tutto il video, che compone un intero sistema attorno
alla vendita: **ICP → Meetings → Indoctrinate → Discovery Call → Business Case**. E una frase che
regge da sola la fase più delicata di tutte, la call: *"Questions first, Solutions later"*
*(caption a schermo, frame-484, @16:06)*.

---

## Il sistema a 5 fasi (Will Barron)

### Fase 1 — ICP: il profilo che si ricava da chi hai già vinto

La prima fase non è un esercizio di marketing astratto fatto a tavolino. L'ICP (Ideal Customer
Profile) si ricava dai **clienti già vinti** — non solo settore e dimensione dell'azienda, ma
**dolore specifico** e **trigger**: l'evento preciso che li ha fatti agire *ora*, e non un mese
prima o un mese dopo.

Il criterio di verifica che il video propone è severo e misurabile: il prospect deve leggere il
messaggio e pensare *"questo sono io"* entro un secondo. Non "potrebbe interessarmi", non "vediamo
di che si tratta" — un riconoscimento immediato.

Il pezzo più operativo del video è un confronto mostrato a schermo fra due email, l'una accanto
all'altra *(frame-160, @5:18)*, dove l'unica variabile che cambia è la quantità di ICP contenuta
nel testo:

```
GENERICA:  "Aiuto gli imprenditori ad aumentare il fatturato.
            Ha senso fare una call e ti spiego come."

OPERATIVA: "Aiuto titolari di aziende di servizi che fatturano tra $20.000 e $200.000 al mese
            a trovare e chiudere piu' contratti nei prossimi 30 giorni, o ti restituisco i
            soldi. Lo facciamo con un sistema di vendita semplice che elimina le montagne
            russe del fatturato su cui probabilmente sei adesso. Ha senso? Facciamo una call
            veloce e ti spiego come."
```

I sette elementi che la seconda email ha e la prima no sono, uno per uno: segmento ristretto,
fascia di fatturato numerica, risultato con un tempo associato, un meccanismo di de-risking (la
promessa di restituzione), un meccanismo dichiarato (il sistema di vendita), un dolore
riconoscibile (le montagne russe del fatturato), e solo alla fine la stessa identica call to
action della prima. **L'unica cosa che le due email hanno in comune è la richiesta di prenotare
una call.** Tutto il resto — tutto quello che fa la differenza fra un messaggio ignorato e uno che
prenota — è ICP.

Il video mostra anche, come controesempio esplicito, l'errore opposto: una card rossa a schermo con
la frase *"We work with anyone who needs what we do"* *(frame-108, @3:34)*, presentata non come un
consiglio ma come **l'errore capitale** di questa fase — l'ICP che non esclude nessuno è, di fatto,
l'assenza di un ICP.

Nell'esempio mostrato, la fascia di fatturato dell'ICP è **$20.000–$200.000 al mese**. Sopra i
**$5.000–10.000 di ticket**, il video è netto su un punto: l'outreach di massa — quello che chiama
"AI slop" — smette di funzionare. A quella soglia di prezzo serve precisione, non volume.

### Fase 2 — Meetings: un solo KPI per touchpoint

La seconda fase è il processo di lead-gen, e deve essere **ripetibile**, non un'iniziativa
sporadica lanciata quando il fatturato crolla. La formula che il video usa per descriverla è
**Right Person + Right Timing + Right Message** — la persona giusta (definita dall'ICP della Fase
1), il momento giusto (il trigger, sempre dalla Fase 1), il messaggio giusto (la lettera operativa
vista sopra).

Il vincolo di misurazione è altrettanto netto: **un solo KPI per ogni touchpoint di outreach**, ed
è il meeting prenotato — mai il pitch. Il messaggio di prospezione non deve vendere nulla, deve
soltanto portare la persona giusta a mettere una data in calendario.

### Fase 3 — Indoctrinate: il tratto fra "ha prenotato" e "è in call"

Questa è la fase meno visibile delle cinque, e probabilmente la più trascurata in generale in chi
vende servizi: il tratto di tempo fra il momento in cui il prospect prenota e il momento in cui si
presenta effettivamente in call. Il video la definisce composta da tre elementi — un'email di
conferma, una landing page con un video, un audit — più una FAQ che **pre-gestisce le obiezioni**
prima ancora che vengano sollevate a voce.

La metrica proposta per questa fase non è un tasso di apertura o di click: è **quante obiezioni
ricorrenti non escono più durante la call**. Se il prospect arriva già informato su prezzo,
processo e aspettative, la call può concentrarsi sulla diagnosi, non sulla gestione di dubbi che
un contenuto scritto avrebbe già risolto in anticipo.

Un dettaglio della fonte merita una nota a parte, perché tocca un punto di dottrina più ampio nella
letteratura di vendita: la FAQ pre-call mostrata a schermo pubblica il prezzo della mentorship
dell'autore — **$8.000 USD** — come filtro di qualificazione che protegge il calendario da prospect
che non possono permetterselo. Questa è una posizione in tensione con una regola molto diffusa
altrove nella formazione alla vendita, secondo cui il prezzo va sempre presentato **dopo** aver
stabilito il valore, mai prima e mai da solo. Le due scuole di pensiero non si conciliano per
decreto, e questa fonte non prova di dover essere l'ultima parola: resta una tensione aperta,
utile da conoscere prima di copiare la tattica senza contesto.

### Fase 4 — Discovery Call: "Questions first, Solutions later"

Qui il video usa un'analogia semplice ma efficace: la call va condotta come farebbe un dottore, non
un venditore. Un dottore non prescrive una cura prima di aver fatto domande, ascoltato i sintomi e
capito la causa. *"Questions first, Solutions later"* è la sintesi di questo principio, mostrata a
schermo come caption fissa nel momento in cui il video entra nel dettaglio della call
*(frame-484, @16:06)*.

I sei passaggi che compongono la discovery call sono narrati (senza supporto grafico) fra 16:41 e
19:57 del video, e vanno eseguiti in quest'ordine:

1. **Pain** — cosa succede se il problema non viene risolto, e chi altro ne è colpito oltre al
   prospect: la sua famiglia, il suo team.
2. **Trigger** — l'evento specifico che ha portato il prospect a prenotare proprio ora: un cliente
   perso, un obiettivo mancato, un concorrente comparso all'improvviso.
3. **Future Reality** — il servizio venduto viene incorniciato come un "Reality Bridge", un ponte
   fra la realtà dolorosa di oggi e la realtà desiderata di domani. Questo passaggio è pensato per
   coprire due tipi di prospect insieme: chi sta fuggendo da un dolore e chi sta inseguendo un
   miglioramento — l'upside.
4. **ROI** — numeri messi sul tavolo, anche grezzi, ma **presto**. Non serve precisione in questa
   fase; serve dimostrare concretamente che il problema può pesare meno di quanto pesi oggi.
5. **Budget** — chiesto **solo dopo** aver mostrato il ROI, mai prima. A quel punto, secondo il
   video, la domanda "passa veloce": *"never as stressful as what most business owners think it's
   going to be before they start doing this routinely"* *(transcript, @19:24)*.
6. **Next Step** — una data e un'ora precise, bloccate nei calendari di **entrambe** le parti,
   prima di chiudere la chiamata. Il video è categorico su questo punto: senza quell'appuntamento
   fissato in entrambi i calendari, *"la discovery call non è stata completata"*
   *(transcript, @19:41)*.

Il valore di questa sequenza non sta in un singolo passaggio, ma nell'ordine: il dolore e il
trigger emergono prima che si parli di soluzioni, il ROI viene stabilito prima che si parli di
budget, e il budget viene chiesto solo quando il prospect ha già davanti a sé una ragione numerica
per considerarlo accettabile.

### Fase 5 — Business Case: l'ostacolo logico, non emotivo

L'ultima fase entra in gioco quando chi ha partecipato alla call non è l'unica persona che deve
dare l'approvazione finale — un socio, un capo, un coniuge che non era presente. Il Business Case è
il documento che rimuove l'ostacolo **logico** a quella decisione, non quello emotivo: quello
emotivo si gestisce in call, quello logico si gestisce per iscritto, in modo che possa circolare
senza l'autore del pitch a spiegarlo.

La struttura del documento segue un ordine preciso, e il video è esplicito sul fatto che **non va
mai invertito**:

1. La situazione del prospect raccontata **nelle sue stesse parole**, trascritte dalla call
   registrata. Il meccanismo psicologico dietro questa scelta è il bias di coerenza cognitiva: le
   persone tendono a restare coerenti con ciò che hanno già detto ad alta voce, quindi rileggere le
   proprie parole rafforza — non introduce — la decisione.
2. L'upside finanziario, il ROI.
3. Solo alla fine, la soluzione — incorniciata con tre parole precise: *"Fast, Easy, Cost
   effective"* *(frame-687, @22:52)*.

Il video attribuisce a questo solo documento un uplift di conversione del **+10-20%**. È bene
segnalarlo per quello che è: un claim dell'autore, detto a voce, senza campione né metodologia
mostrati a schermo — un'ipotesi da testare sul proprio processo, non un benchmark verificato.

---

## Il prezzo (Giovanni Beggiato — solo la parte pricing)

La seconda fonte di questo capitolo nasce in un contesto diverso: un tutorial in cui l'autore
costruisce dal vivo un agente che, partendo dalla trascrizione di una discovery call, genera una
proposta commerciale firmabile e la registra in un archivio dell'agenzia. Il caso d'uso tecnico non
è l'oggetto di questo capitolo — qui interessa solo **come quella fonte tratta il prezzo**: da dove
viene un numero, e perché deve vivere in un solo posto.

### La regola del prezzo unico

Dentro l'architettura mostrata nel video, i prezzi dell'agenzia risiedono in un unico file,
`offerta/offerta.md`, e da nessun'altra parte. La regola, recuperata parola per parola dal prompt
mostrato a schermo e confermata dall'output generato *(frame-005, frame-204, frame-296)*, è
tagliente:

> *"I prezzi vivono SOLO in `offerta/offerta.md`. Mai inventare un numero, mai copiarli altrove."*

Il senso pratico di questa regola emerge da una dimostrazione fianco a fianco mostrata nel video:
due agenti, stessa trascrizione di call, stessa richiesta — uno che lavora senza accesso a
quell'archivio, uno che ci lavora dentro.

**Senza il file dei prezzi**, l'agente produce un documento e poi chiede all'umano di confermare
due scelte che ha inventato lui stesso:

> *"Performance evidenziata come la sua preferenza in call, ma ho messo la stima trimestrale a
> ~3.000 € [...] se preferisci non mostrare quel totale stimato, lo tolgo."*

**Con il file dei prezzi**, lo stesso agente produce il documento e lo chiude con cinque controlli
verificati contro un file che esiste davvero, non contro un'ipotesi:

> *"Copertina con logo, 'Preparata per Marco Rossi – Rossi Marketing', data 23 luglio 2026 ✓ · Pag.
> 'La tua situazione oggi' — 3 paragrafi presi dalla call ✓ · Prezzi identici a
> `offerta/offerta.md`: Standard 2.000 € (1.000 setup + 500/mese × 2), Performance 600 € setup +
> 80 €/meeting ✓ · Nessuna delle due opzioni pre-evidenziata ✓ · Pagina Firma pulita, campi
> firma/data ✓ · Note registrate."*

La differenza fra i due output non è una questione di forma o di eleganza del documento. È una
questione di **verificabilità**: uno dei due agenti chiede fiducia su un numero che ha inventato,
l'altro dichiara un controllo superato contro una fonte che chiunque può riaprire e rileggere. Per
un documento che finisce nelle mani di un cliente con una firma sotto, questa differenza non è un
dettaglio tecnico — è l'intera posta in gioco.

### Value-based pricing: lo stesso agente, due prezzi diversi

Il principio centrale di questa parte del video è enunciato senza giri di parole: lo stesso
identico agente costruito nel tutorial può valere **3.000 €** per un'azienda e **15.000 €** per
un'altra — *"stesso agente, valore diverso"*. Il costo di produzione reale, per contro, è quasi
irrisorio: circa **$100-200 al mese** di utilizzo Claude più circa **$59** di PandaDoc. Da qui la
conclusione dell'autore, netta: *"il costo è una strategia che vi farà perdere e vi farà sempre più
schiacciare i margini"* — prezzare sul costo di produzione, invece che sul valore generato per il
cliente, è la via più diretta per erodere i propri margini nel tempo.

Il video propone **due metodi per arrivare a un numero**, e li presenta esplicitamente come
**additivi, non alternativi** — *"non è un o, ma è un e"*:

```
METODO 1 — IL TEMPO (proxy, dichiarata tale)
  VALORE → VBP → TEMPO → (tempo persona per proposta) × (n° proposte al mese)

METODO 2 — IL ROI
  10 ore/mese liberate
    → in quelle 10 ore la persona prende 2 clienti
    → cliente medio 2.500 €
    → 2 × 2.500 = 5.000 €/mese di upside
    (+ il valore orario di chi paghi)
    ⇒ automazione prezzabile intorno ai 6.000 €/mese
```

Il primo metodo è dichiarato esplicitamente come una **proxy** — un'approssimazione del valore
reale, calcolata moltiplicando il tempo che una persona impiegherebbe per fare a mano ciò che
l'automazione fa, per la frequenza con cui quel lavoro si ripete ogni mese. Il secondo metodo va
oltre il tempo risparmiato e stima l'effetto a valle: cosa succede nelle ore che quel tempo libera,
in termini di nuovi clienti chiusi e fatturato aggiuntivo generato.

Prima di applicare uno qualunque dei due metodi, il video pone **tre condizioni** come prerequisito,
non come dettaglio a margine: *"dovete avere un business che ne ha bisogno, dovete avere un mercato
che ve lo permette, dovete avere un avatar che è disposto a pagare"*. Senza queste tre condizioni
verificate, nessun calcolo di ROI o di tempo salvato produce un prezzo sostenibile — produce solo
un numero sulla carta.

### La struttura entry level e il criterio del retainer

Per chi comincia, la struttura di prezzo suggerita nel video prevede un **setup una tantum** fra
**1.000 e 5.000 €**, più un **retainer mensile** fra **500 e 2.000 €** — entrambi marcati
esplicitamente sulla slide come *"range indicativi"*, e accompagnati a voce da una precisazione
importante: *"dopo ovviamente averne fatte un po'"*, cioè dopo aver già consegnato un certo numero
di progetti, non come punto di partenza assoluto per chi non ha ancora referenze.

Il punto più utile di questa sezione, però, non è la fascia di prezzo in sé — è il **criterio** con
cui decidere se applicare un retainer oppure no, offerto come alternativa a una scelta ideologica:
il retainer si giustifica **quando l'automazione deve cambiare forma nel tempo**, non semplicemente
perché "il ricorrente è meglio dell'una tantum". L'esempio portato nel video è concreto: aziende che
vendono macchinari pesanti su mercati diversi — inglese, italiano, francese, tedesco — dove la
proposta commerciale deve uscire in lingue diverse e prendere forme diverse a seconda del
macchinario specifico venduto. È quel bisogno di manutenzione continua, non la preferenza per un
flusso di cassa prevedibile, a rendere il retainer la scelta corretta.

Un'ultima osservazione, ripresa più volte nel video: il beneficio che si vende al cliente non è
"un'automazione" — è la trasformazione concreta che quell'automazione produce nel suo lavoro
quotidiano. La frase usata come esempio, pronta per essere messa in un'offerta commerciale, è
*"3 GIORNI → 1 ORA"*, seguita a voce da: *"la proposta pronta appena arriva il lead, la rivedi e
premi invia"*.

### I numeri verificati e i claim con riserva

Il listino dell'esempio dimostrativo — **2.000 €** per il pacchetto Standard (1.000 € di setup più
500 €/mese per due mesi) e **600 € + 80 €/meeting** per il pacchetto Performance, con condizioni di
pagamento 50-50 — compare identico su tre fonti indipendenti mostrate nel video: il transcript della
call fittizia, il controllo eseguito dall'agente contro `offerta.md`, e il PDF finale generato. È
uno dei pochi numeri di questa fonte verificabile su più fonti concordanti dentro lo stesso video.

Altri numeri citati nel video vanno presi con la riserva che l'autore stesso vi allega: la cifra di
**€10.000** indicata come prezzo tipico per un'automazione di questo genere arriva accompagnata
dalla domanda retorica *"sarà forse la prima che venderete? Assolutamente no"* — un modo esplicito
per dire che quella cifra è un traguardo, non un punto di partenza.

---

## Chiusura — dove le due fonti si incastrano

Messe una accanto all'altra, queste due fonti non parlano dello stesso momento del processo di
vendita, ma di due momenti che si toccano esattamente in un punto.

La discovery call di Barron è il momento in cui i dati grezzi vengono raccolti: il dolore del
prospect, il trigger che lo ha fatto muovere, un primo numero di ROI messo sul tavolo "anche
grezzo", e infine un budget discusso solo dopo che quel numero ha reso il problema tangibile. Tutto
questo materiale — le parole esatte del prospect, la stima di impatto, l'ordine di grandezza del
problema — è esattamente l'input grezzo che il metodo di pricing di Beggiato trasforma in un
numero preciso: la proxy del tempo persona moltiplicata per la frequenza, o la stima del ROI a
valle in termini di nuovi clienti e fatturato aggiuntivo.

C'è anche una seconda cosa che le due fonti condividono, più sottile della prima: un'ossessione
comune per la **verificabilità** del prezzo, anche se la esprimono in forme opposte. Barron
pubblica il proprio prezzo apertamente in una FAQ pre-call, rendendolo un filtro dichiarato prima
ancora che la conversazione cominci. Beggiato, all'estremo opposto, tiene il prezzo nascosto fino
alla fine della call ma lo àncora a un unico file che qualunque agente — o qualunque persona — può
riaprire e ricontrollare, invece di lasciarlo alla memoria o all'improvvisazione di chi scrive la
proposta in quel momento. Sono due filosofie diverse su **quando** mostrare il prezzo, ma
condividono lo stesso principio di fondo su **come** quel prezzo deve poter essere verificato — da
chi lo riceve, nel caso di Barron; da chi lo genera, nel caso di Beggiato.

La frase che riassume meglio questo punto d'incontro non appartiene a nessuna delle due fonti presa
da sola, ma nasce leggendole insieme: un processo di vendita che non lascia scritto da dove viene
un numero — né il dolore che lo giustifica, né il file che lo contiene — chiede fiducia. Un processo
che lo lascia scritto, dichiara un controllo superato contro una fonte. La seconda cosa è quella che
regge, oltre la singola trattativa, quando a controllare il numero non è più la stessa persona che
lo ha proposto.

---

# Capitolo 3 — Consegna, Servizio e Scala

*Nota per il lettore: questo capitolo fa parte della Parte 2 del libro — la formazione esterna
da cui il metodo di Digital Empire nasce. Tutto ciò che segue riporta cosa insegnano tre fonti
esterne (due video di Giovanni Beggiato, fondatore dell'agenzia Gentes AI, e un video di
Riccardo Belli Contarini, fondatore dell'agenzia Martes AI), non cosa fa Digital Empire. Dove le
fonti stesse confrontano il proprio insegnamento con pratiche di agenzia già diffuse, lo si segnala
restando chiaro che il confronto appartiene alla fonte, non a una dichiarazione aziendale.*

## 3.1 Tre fonti, tre livelli dello stesso problema

Il Capitolo 1 e il Capitolo 2 di questa Parte hanno coperto come un'agenzia trova un cliente. Ma
un lead che paga non è ancora un cliente servito bene, ed è qui che la maggior parte delle agenzie
— comprese quelle AI-native, dove il ciclo di vendita può essere rapidissimo — comincia a
scricchiolare. Una delle fonti di questo capitolo lo dice con una frase che vale come cerniera fra
i due momenti:

> "Voi avete un cliente se solo se c'è stato un movimento di denaro." [apertura sezione
> fulfillment, Giovanni Beggiato, *Come Avviare Un'Agenzia AI da 10.000€/Mese*, video ID
> `rvpRQD43wdY`]

Prima di quel movimento di denaro, tutto è acquisizione. Dopo, comincia un problema diverso: come
si consegna lo stesso livello di qualità al cliente numero 50 che si è promesso al cliente numero
1, senza che il fondatore diventi il collo di bottiglia di ogni progetto. La stessa fonte
riassume lo scheletro operativo di un'agenzia in **7 fasi** — Lead Generation → Sales Funnel →
Sales Call → Onboarding → CRM Management → Delivery/Fulfillment → Upselling — e in **3 pilastri**
che reggono l'intera struttura: **Promozione** (acquisizione, coperta nei capitoli precedenti),
**Prodotto** (la consegna vera e propria) e **Daily Ops** (la gestione quotidiana che tiene tutto
in piedi). Il punto sottolineato dalla fonte è che la competenza sui *processi* — non sugli
strumenti, che cambiano ogni pochi mesi — è ciò che sopravvive.

Questo capitolo copre la fase Prodotto/Delivery da tre angolazioni diverse, offerte da tre fonti
distinte:

1. **Prezzo e processo** (Giovanni Beggiato, *Come Avviare Un'Agenzia AI da 10.000€/Mese*,
   `rvpRQD43wdY`, 4h17m00s) — come si prezza un servizio AI, e come si struttura il flusso di
   consegna dal kickoff alla chiusura del progetto, fino a quando e come assumere.
2. **Il servizio reso scalabile** (Giovanni Beggiato, *Ho creato un intero team di marketing AI
   con Claude Code in 20 minuti*, `yJOCyyP77bA`, 19m54s) — un esempio concreto e mostrato dal vivo
   di cosa significa "scalare la consegna senza scalare le ore umane": un team di 6 agenti AI
   specialisti che produce in 20 minuti un audit di marketing completo, deliverable incluso.
3. **Il controllo indipendente della qualità** (Riccardo Belli Contarini, *Claude Code + Codex: Il
   Setup di cui NESSUNO Parla*, `T7PPX5M6Puo`, 30m52s) — perché un lavoro dichiarato "pronto" da
   chi lo ha costruito può non esserlo affatto, e cosa succede quando lo si fa controllare da
   qualcuno — o qualcosa — che non condivide gli stessi punti ciechi.

Tre livelli dello stesso problema: **quanto** far pagare, **come** consegnarlo in modo ripetibile,
**chi** verifica che sia davvero pronto prima che il cliente lo veda.

---

## 3.2 Prezzo e pacchetti

### La matrice DIY / DWY / DFY × Tempo / Unità / Risultato

Beggiato presenta — e la disegna dal vivo, verificata a schermo in `frame-0451.png` — una matrice
3×3 che incrocia **come** il cliente riceve il servizio con **su cosa** viene prezzato:

| | Tempo | Unità | Risultato |
|---|---|---|---|
| **Do It Yourself (DIY)** | il cliente compra tempo del tuo prodotto/strumento | il cliente compra un pacchetto di unità da usare da solo | il cliente paga per un risultato che raggiunge da solo con il tuo strumento |
| **Done With You (DWY)** | consulenza a ore/sessioni | pacchetti di unità con supporto | risultato garantito con coaching incluso |
| **Done For You (DFY)** | retainer a tempo (ore/mese dell'agenzia) | **"vendo N automazioni a X€"** | risultato garantito, l'agenzia fa tutto |

Le soluzioni AI, nota la fonte, si collocano quasi sempre nel quadrante **DFY-Unità**: vendere un
numero definito di automazioni a un prezzo fisso. È il quadrante più scalabile della matrice
perché è l'unico **disaccoppiato dal tempo dell'operatore** — un'automazione consegnata al
cliente 1 non costa più ore all'agenzia del cliente 50, mentre ogni altro quadrante lega il
fatturato a un tempo umano che non si moltiplica.

Sopra questa matrice, la fonte sovrappone **tre modelli contrattuali**, che possono convivere
sullo stesso cliente:

- **Pay in full** — pagamento anticipato dell'intero progetto.
- **Pay on performance** — il cliente paga solo, ad esempio, l'ad-spend; l'agenzia rischia sul
  resto del compenso, scommettendo sulla propria capacità di generare risultato.
- **Retainer misto** — una quota fissa mensile più una componente variabile.

### Perché il quadrante DFY-Unità funziona: la "released capacity"

Un elemento centrale per capire *perché* un cliente paga per un'automazione — e quindi perché il
prezzo del quadrante DFY-Unità regge — è il concetto di **released capacity** (capacità
produttiva liberata), che la fonte pone al centro dell'intera proposta di valore dell'agenzia AI:
non si vende un software, si vende tempo umano restituito all'azienda. L'esempio numerico dato:

```
100 dipendenti × 5 ore risparmiate/settimana = 500 ore/settimana
500 ore × €10/ora                            = €5.000/settimana di "released capacity"
```

La fonte è esplicita su un punto che rischia di perdersi in qualsiasi rielaborazione superficiale
di questo materiale: quelle non sono ore diventate automaticamente soldi in tasca
all'imprenditore — sono soldi **potenzialmente** cash, che si materializzano solo se qualcuno
decide cosa fare con le 500 ore liberate. Da qui il salto di ruolo che la fonte attribuisce
all'agenzia AI matura: da fornitore di uno strumento a **partner di change management**. Se
l'agenzia non aiuta il cliente a decidere cosa fare col tempo liberato, il valore percepito
dell'automazione resta basso, quanto sia tecnicamente elegante lo strumento.

### La golden rule del close rate: 30%

Il criterio con cui la fonte suggerisce di sapere se il prezzo fissato è quello giusto non è un
calcolo sui costi, ma una lettura a posteriori del comportamento dei lead in sales call. Il testo
esatto, verificato sulla trascrizione grezza del video (con correzione di una lettura precedente
che schiacciava le tre soglie in una sola):

> "se il vostro close rate e' piu' alto quindi ipotizziamo che il vostro close rate sia del 60%
> significa che il vostro prezzo e' troppo basso rispetto all'offerta se invece ipotizziamo questo
> sia del 20% vuol dire che o siete delle scarpe a vendere o che il prezzo e' troppo alto [...]
> golden rule per service business dovreste essere sul 30%" [sezione pricing, `rvpRQD43wdY`]

Le tre soglie:

| Close rate | Lettura secondo la fonte |
|---|---|
| **60%** | prezzo **troppo basso** rispetto all'offerta |
| **30%** | **golden rule** per un service business — l'equilibrio giusto |
| **20%** | prezzo troppo alto **oppure** "siete delle scarpe a vendere" |

La fonte precisa anche che questo benchmark non è universale: per un modello a **community**, il
close rate atteso e considerato sano è del **2-4%**, non del 30% — la logica di un servizio
one-to-one (dove ogni lead in call viene qualificato a fondo prima di arrivarci) non si applica a
un'offerta aperta a un pubblico ampio.

### Le sei metodologie di acquisizione — solo il ranking

Il dettaglio operativo delle sei metodologie di acquisizione clienti indicate da questa stessa
fonte — Warm Network, Upwork, Strategie Cold, Ads, Fiverr, Social Media Posting — è trattato per
intero nel Capitolo 1 di questa Parte. Qui interessa solo la loro collocazione nella scala di
difficoltà crescente su cui la fonte le ordina (elenco confermato a schermo in `frame-0631.png`,
1:24:00 del video):

1. Warm Network (rubrica personale)
2. Upwork (bootstrap)
3. Strategie Cold (email, DM, call)
4. Ads (solo su contenuto organico già validato)
5. Fiverr (inbound, richiede brand già riconosciuto)
6. Social Media Posting / Organico (curva lenta, nessun plateau precoce)

Il motivo per cui questo ranking appartiene anche al capitolo sulla consegna, e non solo a quello
sull'acquisizione, è che il pricing e il canale di acquisizione **non sono indipendenti**: un
canale che porta lead poco qualificati (es. Ads su contenuto non testato) può far scendere il
close rate sotto il 20% anche con un prezzo corretto, mentre un canale che porta lead già caldi
(Warm Network) può reggere un prezzo più alto con lo stesso close rate — la matrice di pricing
va sempre letta insieme al canale che ha generato quel lead specifico.

---

## 3.3 Fulfillment: dal kickoff alla consegna ripetibile

### Il flowchart Whimsical

La fonte mostra a schermo (verificato in `frame-1401.png` e `frame-1440.png`, URL
`whimsical.com/beggiato-media/how-to-service-your-first-automation-client-in-2026-...`) un
flowchart di fulfillment completo, costruito su Whimsical, che copre l'intero ciclo da "hai già
fatto questo progetto prima?" fino a "test end-to-end + rafforza i casi limite". È il documento
di processo che trasforma la consegna da artigianale (ogni progetto reinventato da zero) a
ripetibile (ogni progetto segue lo stesso schema, con varianti sui dettagli).

### I cinque punti obbligatori della kickoff call

Il nodo più densamente istruttivo del flowchart è la kickoff call, per cui la fonte elenca cinque
elementi che devono essere coperti **sempre**, senza eccezioni:

1. **Timeline con under-promise-and-overdeliver** — la data comunicata al cliente è
   deliberatamente più larga di quella realisticamente attesa internamente, per lasciare margine
   e consegnare in anticipo invece che in ritardo.
2. **Reperibilità esplicita** — si dichiara al cliente quando e come l'agenzia è raggiungibile,
   invece di lasciarlo intuire o scoprire per tentativi.
3. **Definizione scritta del successo** — cosa significa "progetto completato" viene messo per
   iscritto prima di iniziare, proprio per prevenire lo **scope creep**: senza una definizione
   scritta, ogni richiesta successiva del cliente rischia di essere trattata come "compresa" nel
   progetto originale, anche quando non lo è.
4. **Registrazione delle piattaforme in call** — le credenziali e gli accessi necessari vengono
   raccolti mentre si è in videochiamata con il cliente, non rincorsi via email nei giorni
   successivi.
5. **Tracciamento (opzionale)** — un sistema di monitoraggio dello stato di avanzamento, quando
   il progetto lo richiede.

### La policy delle credenziali: sempre del cliente

Un punto di processo dichiarato esplicitamente dalla fonte, e non negoziabile nel suo racconto:
**le credenziali di ogni piattaforma usata nel progetto sono sempre intestate al cliente**, mai
all'agenzia. La ragione dichiarata è evitare il **vendor lock-in**: se l'agenzia possiede gli
account su cui gira l'automazione del cliente, il cliente non può mai davvero lasciare l'agenzia
senza perdere il proprio sistema — una dipendenza che nel racconto della fonte è vista come un
rischio reputazionale e commerciale, non come una leva di ritenzione legittima.

### GoHighLevel come esempio di piattaforma di servizio

Per rendere concreto cosa significhi "fulfillment" in pratica, la fonte fa una demo dal vivo di
**GoHighLevel**, un CRM all-in-one per agenzie, sul dominio reale `gentes.ai` (dashboard
verificata a schermo in `frame-1511.png`). I dati confermati a schermo:

- Costo: **~97$/mese**
- **3 sub-account** inclusi nel piano base
- Programma di affiliazione: fino al **50% ricorrente**

La distinzione tecnica che la fonte segnala come chiave per **templetizzare** un funnel — cioè
costruirlo una volta e rivenderlo a più clienti senza ricostruirlo da zero — è quella fra:

- **custom values**: legate al sub-account/cliente (es. il nome della città in cui opera quel
  cliente specifico)
- **custom fields**: legate al singolo lead (es. la fonte di provenienza, il consenso dato)

La demo copre anche il funnel builder, la pipeline "Opportunities", il calendario, e i workflow di
automazione — mostrando in particolare la tecnica del **"taking in charge"**: un messaggio
automatico di presa in carico inviato al lead prima ancora che un umano lo richiami, con
l'obiettivo dichiarato di alzare il pickup-rate della chiamata umana successiva. La demo si
chiude su Meta Ads Manager, con una campagna reale in bozza — budget **€20,00**, verificato a
schermo, non un dato sintetico di esempio come altre schermate del video.

### Hiring & Scaling: quando e chi assumere

L'ultima sezione della fonte riguarda il momento in cui un'agenzia smette di essere un solo
fondatore e comincia ad assumere. La regola centrale: si assume **a capacità**, non per avere più
tempo libero, e **per bisogno**, non per crescita — soprattutto nella fase iniziale. Prerequisito
esplicito prima di qualunque assunzione: le **SOP** (procedure operative standard) devono essere
già documentate, altrimenti si assume qualcuno senza dargli un processo da seguire.

Il primo ruolo da assumere, secondo la fonte, non è il commerciale ma il **CTO** — la logica è che
un CTO libera l'imprenditore dal lavoro tecnico per concentrarlo sulle vendite, che restano
l'unica leva capace di far crescere il fatturato in prima persona. Un grafico disegnato a mano
durante il video (`frame-1875.png`) mostra il salario dell'imprenditore **scendere
temporaneamente** subito dopo l'assunzione del CTO, prima di risalire quando il fatturato comincia
a scalare grazie al tempo liberato — un costo iniziale dichiarato esplicitamente, non nascosto.

La fonte chiude l'intero video con una nota che ridimensiona l'ambizione stessa del percorso
appena descritto:

> "Voi letteralmente imparate a gestire un business... l'agenzia AI sarà probabilmente l'ultimo
> business che farete? Assolutamente no." [chiusura, sezione hiring & scaling, `rvpRQD43wdY`]

L'agenzia AI, nella lettura della fonte, è quasi sempre uno **step intermedio** verso business più
scalabili — SaaS, community, prodotto digitale — non il punto di arrivo.

---

## 3.4 Il servizio come prodotto: un team di agenti scala la consegna

Se la sezione precedente descrive il *processo* di fulfillment, questa sezione ne mostra
un'applicazione concreta e filmata dal vivo: come lo stesso autore, nella sua agenzia Gentes AI,
ha trasformato un servizio che normalmente richiederebbe ore di lavoro umano — un audit di
marketing completo per una PMI — in un output di 20 minuti prodotto da un team di agenti Claude
Code.

### Il sistema: 6 specialisti + 1 orchestratore

Da un singolo URL e un solo prompt in linguaggio naturale ("attiva il mio marketing team su
questo URL"), il sistema attiva sei agenti specialisti in parallelo più un orchestratore:

```
01 STRATEGA            -> vota Messaggio e Crescita: "prova dei 5 secondi",
                           fonti di traffico (Search/Instagram/LinkedIn/YouTube)
02 ANALISTA CONCORRENZA -> vota Concorrenza: recensioni vs concorrenti reali
                           (P.IVA -> Registro Imprese -> ATECO -> concorrenti)
03 SPECIALISTA SEO      -> vota Trovabilità: titoli pagina, posizione SERP
04 COPYWRITER           -> senza voto, dimostra: 3 testi più deboli, prima/dopo
05 ESPERTO CONVERSIONI  -> vota Conversione: percorso cliente click-per-click
06 MEDIA BUYER          -> senza voto, verdetto: ads di oggi sono soldi buttati?
```

L'architettura sul filesystem è organizzata in una cartella con 11 skill (una per ogni
deliverable — `marketing-ads`, `marketing-seo`, `marketing-funnel`, ecc.) e una sottocartella
`squadra/` con i file `.md` di ogni agente reale (frontmatter `name/description/tools` più il
corpo delle istruzioni). L'autore descrive il pattern con una frase che riassume bene l'approccio:
*"ho creato un sacco di skill e poi ho fatto qui una mini squadra."*

### La regola di squadra: tre righe

Tre regole, esplicitamente dichiarate a schermo in un banner ("OGNI VOTO HA DIETRO UNO
SPECIALISTA"), governano ogni output del team:

```
1. Ogni voto cita il sito
2. Mai numeri inventati
3. Difetti provati nel browser vero
```

> "Ogni voto cita il sito, mai numeri inventati, difetti provati nel browser vero." [banner di
> squadra, `yJOCyyP77bA`]

### Il pattern riusabile: verifica dal vivo contro il fetch statico

L'elemento più interessante, dal punto di vista del *processo* di controllo qualità, è che il
sistema non si accontenta dei dati raccolti da una lettura statica del sito (fetch), ma esegue un
passaggio di verifica in un browser realmente renderizzato (Chrome via MCP) prima di dichiarare
qualunque difetto. Il video mostra cinque casi in cui questo passaggio **cambia il risultato**:

| Claim dal fetch statico | Verifica nel browser renderizzato |
|---|---|
| "hreflang assenti" | **SMENTITO**: it/en/x-default presenti nel DOM |
| "categorie non tradotte" | **SMENTITO**: tradotte via JS, invisibili al fetch |
| "spedizioni solo Italia" | **SMENTITO**: "SHIPMENTS IN ITALY AND EU" nel checkout |
| zero widget recensioni | **CONFERMATO** dal vivo (home/collezione/2 schede) |
| telefono non cliccabile | **CONFERMATO** dal vivo |

Il test è stato eseguito interamente: click, aggiunta al carrello, checkout raggiunto e abbandonato
prima del pagamento — sull'e-commerce reale del cliente usato come caso nel video. Il risultato
pratico di questa verifica non è cosmetico: il voto sulla Conversione è stato **ricalcolato
dentro lo stesso deliverable**, da 6.0 a 6.5, dopo che il passaggio dal vivo ha scoperto elementi
che il fetch statico non poteva vedere — ritiro in negozio, checkout ospite con pagamento express,
opzione "richiedi la taglia".

### La regola "mai concorrenti inventati"

La seconda regola riusabile riguarda la ricerca competitor, e segue una catena di verifica
tracciabile:

```
URL cliente -> scraping P.IVA -> Registro Imprese -> codice ATECO
            -> concorrenti REALI nella stessa nicchia/città (mai inventati)
            -> confronto recensioni (numero E contenuto, non solo stelle)
```

Applicata al caso reale mostrato nel video, questa catena ha prodotto **6 concorrenti reali con
fonte citata** (Google Places + ricerca web), incluso un concorrente — Musto Calzature —
sconosciuto persino all'autore del video, che commenta:

> "Onestamente non ho idea di chi siano, ma a quanto pare va meglio di noi su quasi tutto." [sul
> concorrente Musto Calzature, `yJOCyyP77bA`]

Questo dettaglio ha valore probatorio nel racconto della fonte: dimostra che il sistema non si è
limitato a confermare ciò che l'operatore umano già sapeva, ma ha trovato qualcosa che l'operatore
stesso non conosceva.

### L'output: un deliverable doppio, pronto per il cliente

Il processo produce due artefatti distinti:

- **HTML aggregato** (`TUTTI-I-DELIVERABLE.html`, uso interno) — 8 tab: Pagella, Mappa
  Opportunità, Campagne Ads, Funnel, Piano SEO, Sequenza Email, Calendario Social, Piano 90
  giorni.
- **PDF cliente** (`REPORT-CLIENTE.pdf`) — cover con voto complessivo (5.6/10), radar chart a 5
  assi contro il concorrente principale, confronto testa a testa con 4 concorrenti, matrice di
  priorità 2×2, e una pagina finale dedicata a "Il primo passo": una sola azione da fare per
  prima, non una lista indistinta di raccomandazioni.

### I numeri del caso mostrato

- Tempo totale dal link incollato al piano completo: **20 minuti**
- Voto finale del caso (calzature): **5.6/10** — scomposto in Messaggio 6.0, Trovabilità 5.0,
  Conversione 6.5, Concorrenza **3.5 (rosso)**, Crescita 7.0
- 6 concorrenti reali con fonte: Turci (4.9/1176 recensioni), Velasca (4.8/542), Musto (4.8/406),
  GHIGO (4.4/476), Walter (4.6/299), Pepperina (4.8/187)
- Volumi di ricerca mensili non intercettati dal cliente, trovati dal piano SEO: sneakers donna
  90.500, ballerine donna 60.500, sandali donna 40.500
- Budget ads raccomandato nel piano: **1.200 €/mese** (40 €/giorno)

Due frasi dell'autore riassumono l'intento dietro il sistema, al di là del singolo caso mostrato:

> "Basta incollare il sito di una piccola impresa e in un paio di minuti sei agenti restituiscono
> un'analisi completa." [`yJOCyyP77bA`]

> "Il nostro obiettivo non è mai fare one shot, ma è avvicinarci quanto più possibile ad un output
> di qualità." [`yJOCyyP77bA`]

Questa seconda frase è importante da leggere insieme alla Sezione 3.5: la fonte stessa dichiara
che il processo normale prevede iterazioni, non un colpo unico — un'ammissione che rende ancora
più rilevante la domanda del prossimo blocco, cioè chi controlla che l'output di un run "pulito"
come quello mostrato nel video sia davvero pronto per il cliente.

---

## 3.5 Chi giudica il lavoro non è chi lo fa

### Il principio cardine

La terza fonte di questo capitolo parte da un problema diverso, ma collegato: anche un team ben
costruito — umano o di agenti — può dichiarare pronto un lavoro che non lo è, semplicemente
perché chi ha costruito e chi ha verificato condividono lo stesso punto di vista. La fonte lo
scrive a lavagna, in maiuscolo, come principio cardine dell'intero video:

```
CHI COSTRUISCE ≠ CHI GIUDICA
```

Il meccanismo mostrato: il piano (o il codice) lo scrive Claude, un secondo modello di famiglia
diversa lo contesta con una revisione avversariale, Claude produce una versione 2, il ciclo si
ripete finché il secondo modello non ha più obiezioni — sempre con una revisione umana nel mezzo,
non come sostituto di essa:

> "non vogliamo essere pipecoder seriali... altrimenti quello che abbiamo costruito diventa un
> mostro incontrollabile." [`T7PPX5M6Puo`]

### Lo strumento mostrato: il plugin Codex dentro Claude Code

La fonte dimostra il principio con un plugin ufficiale OpenAI ("Codex Plugin") installato dentro
Claude Code, che espone cinque comandi:

| Comando | Cosa fa | Flag |
|---|---|---|
| `/codex:review` | Legge solo le modifiche non committate su Git, non indirizzabile | — |
| `/codex:adversarial-review` | Come review, ma puntabile su un target (codice o piano) | `--background` |
| `/codex:rescue` | Indaga/corregge un'app o un bug, anche già committata | `--background` `--wait` `--resume` `--fresh` `--model` `--effort` |
| `/codex:transfer` | Porta la conversazione Claude Code dentro Codex, continuando da dove si era | — |
| `/codex:status` / `/codex:result` | Stato dei job in background / report completo a fine job | richiede ID task |

Due pattern d'uso emergono dal video:

- **Pattern 1** — l'app è pronta → `/codex:review` (o `/codex:rescue` se già committata) → un
  umano revisiona i finding → Claude sistema → si va online.
- **Pattern 2** — il piano è scritto con Claude → `/codex:adversarial-review` sul piano → le
  critiche tornano a Claude → piano v2 → il ciclo continua fino a convergenza → **solo allora** si
  comincia a scrivere codice.

### I tre casi reali

Il cuore probatorio della fonte sono tre casi reali dell'agenzia dell'autore (Martes AI, 65+
aziende clienti e 75+ soluzioni AI in produzione al momento del video), in cui Claude Code aveva
già dato un giudizio positivo — sul codice o sul piano — prima che Codex trovasse il problema:

| Caso | Cosa aveva già dichiarato Claude | Cosa ha trovato Codex |
|---|---|---|
| **MaReply** (clone ManyChat, gestisce account Instagram di clienti) | "pronta per essere mandata in produzione" | **2 falle Alte**: autenticazione via email/password senza verifica email (account dirottabile tramite invito); DM duplicati per assenza di un claim atomico (spam, doppio consumo di budget Meta, rischio phishing) |
| **Form candidature** (Cloudflare + Airtable, dati personali di candidati) | nessun audit di sicurezza eseguito prima | **4 finding Alti** (endpoint pubblico senza rate limiting/CAPTCHA, upload completamente fidato lato server, nessun limite alla dimensione dei campi, librerie di terze parti senza SRI/CSP) più 10 medi e 1 informativo |
| **Piano clone Bitly** (Cloudflare Workers + D1, prima ancora di scrivere codice) | piano scritto e presentato come pronto per lo sviluppo | **1 critical** (le API di statistiche/cancellazione non verificano la proprietà del link: chiunque può cancellare link altrui) più **2 high** (redirect 301 cachato che rompe il tracciamento dopo una cancellazione; contatore gonfiato da eventi duplicati) |

Sul caso Bitly, in particolare, Claude — ri-interrogato dopo le obiezioni di Codex — riconosce di
aver ripetuto un errore già noto nella storia di quel prodotto: aveva proposto un redirect
**301** (permanente, cachato indefinitamente dai browser), lo stesso errore che **Bitly stesso
aveva corretto passando a 302 nel 2016**. Riconosce inoltre la fondatezza della maggioranza delle
obiezioni ricevute:

> "4 obiezioni su 5 hanno un nucleo valido." [Claude, ri-interrogato sulle obiezioni Codex al
> piano Bitly, `T7PPX5M6Puo`]

E sul caso MaReply, l'autore commenta con una frase che riassume il rischio concreto di fidarsi di
un solo giudice:

> "Considerate che Claude Code mi aveva detto che questa applicazione era pronta per essere
> mandata in produzione... meno male che ho chiamato Codex." [`T7PPX5M6Puo`]

### Il costo del secondo giudice

La fonte affronta anche la domanda più ovvia — quanto costa aggiungere un secondo modello che
legge tutto ma scrive raramente:

- Solo Claude ($200/mese): "nessuno che lo controlla"
- Solo Codex ($200/mese): "nessuno che serve bene"
- Combo consigliata: Claude Max $100 + Codex/ChatGPT Plus $20 = **$120/mese**
- Alternativa gratuita per testare: piano ChatGPT Free (Codex incluso, con limiti stretti)
- Requisito minimo lato Claude per la combo: piano Pro $20/mese

> "Venti dollari in più. Non il doppio. Perché qui Codex legge e critica, e scrive quasi mai.
> L'auditor costa molto meno che generare." [lavagna finale sui costi, `T7PPX5M6Puo`]

### Il limite dichiarato dalla fonte stessa

La fonte non presenta questo pattern come una legge universale, e lo dichiara esplicitamente:
tre casi aneddotici di una sola agenzia, nessun benchmark quantitativo aggregato su un campione
più ampio, nessun tasso di falsi positivi misurato. `/codex:review` non viene mai eseguito dal
vivo nel video (solo `rescue` e `adversarial-review`), e non viene mostrata alcuna gestione del
disaccordo oltre il caso Bitly (dove 4 obiezioni su 5 vengono accettate) — resta aperta la domanda
di cosa succeda se i due modelli restano in disaccordo per più cicli consecutivi. La dimostrazione
è inoltre limitata a un solo ambiente (Mac + VS Code).

Un'ultima nota di raffronto, che la fonte stessa registra: un'agenzia che ha già un passaggio di
revisione indipendente nel proprio ciclo di lavoro — un secondo controllo dopo chi produce, prima
che il lavoro raggiunga il cliente — non è per questo esente dal problema dimostrato nei tre casi,
se quel secondo controllo gira sulla **stessa famiglia di modello** di chi ha prodotto il lavoro.
Il principio dimostrato non riguarda "quale IA scrive meglio", ma il fatto che un giudice della
stessa famiglia tende a condividere i punti ciechi dell'autore — a prescindere dal tier o dal
livello di reasoning usato per il controllo.

---

## 3.6 Chiusura: tre livelli dello stesso problema

Le tre fonti di questo capitolo, lette insieme, coprono tre domande che un'agenzia deve rispondere
in sequenza dopo aver chiuso un cliente, e che restano valide indipendentemente da quanto lavoro
venga effettivamente svolto da agenti AI invece che da persone:

- **Quanto far pagare, e su cosa** — la matrice DIY/DWY/DFY × Tempo/Unità/Risultato e la golden
  rule del 30% danno un modo per capire se il prezzo fissato è quello giusto, guardando al
  comportamento reale dei lead invece che a un numero scelto a tavolino.
- **Come consegnarlo in modo ripetibile** — il flowchart di fulfillment, i cinque punti
  obbligatori della kickoff call, la policy sulle credenziali e la regola di assunzione
  "CTO prima del commerciale" trasformano la consegna da un'esperienza diversa per ogni cliente a
  un processo che regge la scala. Il team di 6 agenti marketing mostra concretamente cosa
  significa "scalare la consegna senza scalare le ore umane": lo stesso output di qualità in 20
  minuti invece che in giorni, con regole esplicite ("mai numeri inventati", "mai concorrenti
  inventati", "difetti provati nel browser vero") che sostituiscono la supervisione umana
  costante con vincoli scritti nel sistema stesso.
- **Chi verifica che sia davvero pronto** — il principio "chi costruisce non è chi giudica"
  chiude il cerchio: un processo di consegna ripetibile e un prezzo corretto non bastano se
  l'ultimo controllo di qualità condivide gli stessi punti ciechi di chi ha prodotto il lavoro.
  Nei tre casi mostrati dalla fonte, un secondo giudice di famiglia diversa ha trovato falle di
  gravità alta o critica su lavoro già dichiarato pronto — non una volta, ma tre su tre.

Nessuna delle tre fonti, presa da sola, risolve il problema della scala. Un prezzo corretto senza
un processo di consegna ripetibile produce un'agenzia che vende bene ma consegna in modo
inconsistente. Un processo di consegna ripetibile senza un controllo qualità indipendente produce
un'agenzia efficiente che consegna comunque, di tanto in tanto, un lavoro difettoso dichiarato
pronto. E un controllo qualità indipendente, da solo, non genera né il prezzo né il processo su
cui esercitarsi. È la combinazione delle tre leve — prezzo, processo, controllo — a rendere
un'agenzia capace di crescere senza rompersi, coerentemente con la nota di chiusura della prima
fonte di questo capitolo: l'agenzia AI, quasi sempre, non è il punto di arrivo ma lo step che
insegna a costruire ogni pezzo di questo sistema.

---

## Copertura e fonti

Questo libro chiude la missione `EMP-W4K7` di Empire Studio (checkpoint `CP-20260909-2CWF` e
successivi). Conteggio fatto sul disco, non dichiarato a memoria:

- **73 pagine wiki fonte** esistono in `second-brain-vault/wiki/sources/` al momento della
  stesura. Di queste, **11** portano un tag esplicito riconducibile ad agenzia/acquisizione
  clienti/vendita/prezzo.
- **7 delle 11** sono entrate in questo libro, per intero o nella parte pertinente: Paolo
  Trivellato (LinkedIn organico), Giovanni Beggiato x3 (LinkedIn cold DM, guida agenzia
  completa, team marketing AI, e la sola sezione pricing del video Company Brain/Karpathy),
  Will Barron (sistema di vendita), Riccardo Belli Contarini (cross-model review).
- **4 restano fuori perimetro**, dichiarato: tre pagine di Andrei Pascu (copywriting freelance,
  parte dello studio competitor separato, non del nostro metodo agenzia) e una di MiK Cosentino
  (infobusiness/personal brand a mastermind, modello diverso da un'agenzia di servizi).
- La **Parte Prima** attinge da 9 skill di produzione reali di Digital Empire: `agency-scalping`,
  `icp-radar`, `cold-email`, `avvia-outreach-preventa`, `cro-call`, `beast-preventivi`,
  `discovery-call-brief`, `delivery-playbook`, `client-handover`.

**Cosa NON contiene questo documento, per scelta**: nomi di clienti reali di Digital Empire,
credenziali o valori di configurazione, numeri di fatturato interni non gia' pubblici altrove,
riferimenti a codici ADR o a strumenti di controllo interni per numero/nome. E' un documento
pubblico: descrive il metodo, non espone l'azienda.

---

*Il Libro dell'Agency — Digital Empire, 2026-09-10. Fonte di verita': questo file
(`PIANO-MAESTRO/34-LIBRO-AGENCY.md`). Edizione PDF: `PIANO-MAESTRO/34-LIBRO-AGENCY.pdf`,
generata da `PIANO-MAESTRO/scripts/build_libro_agency_pdf.py`. Doppione in
`documentazione Empire/Piani/Agency/`.*
