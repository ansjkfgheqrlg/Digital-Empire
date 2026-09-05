---
Type: PROJECT
Status: Proposta — l'ADR va registrato PRIMA di creare la cartella
Tags: #lanci #ecosistema-15 #ADR #decisione
Created: 2026-09-05
---

# 10 — LA DECISIONE DA REGISTRARE, E I TRE GIRI

---

# PARTE A — L'ADR PROPOSTO

> ⚠️ **Questo non è l'ultimo passo del piano: è il primo passo della costruzione.**
> Una decisione già in vigore impone che ogni ecosistema dal quattordicesimo in poi richieda una
> decisione registrata **prima** di poter essere inserito, e un controllo di conformità dell'Impero
> lo verifica davvero. Senza, la cartella nasce fuori norma.
>
> **Numero:** l'ultimo ADR registrato è il 021, quindi questo è **ADR-022**.
> Va salvato in `company/Memory/decisions/ADR-022-ecosistema-lanci.md` **solo dopo l'ok di Max**.

## ADR-022 — Nasce l'ecosistema 15-LANCI

**Stato:** proposto · **Data:** 2026-09-05 · **Proponente:** Max (via Emperator) ·
**Esecutore:** Gael · **Decide:** Max

### Contesto — i fatti misurati

| Fatto | Misura |
|---|---|
| Il reparto Lanci esistente | **19 file, 2.377 righe, 0 eseguibili, 0 agenti invocabili, 0 stato scritto** |
| Gli script che dovrebbe avere | **0 su 3**, dichiarati *"pianificati, build in V2"* |
| Le skill utili già installate | **11 su 11** presenti e funzionanti |
| Il Manuale Claude Code | 203 pagine, **"Pronto" dal 07/03/2026** · prezzo *"€ NON LO SO"* · data *"Presto spero"* · ricavo **0** |
| Il blocco dichiarato e mai risolto | dall'**11 giugno 2026** |
| Materiale storico assorbito | **26.300 righe**, 58 framework, 26 soglie numeriche |

**Il problema:** Digital Empire non ha un buco di *capacità* sui lanci. Ha un buco di **decisione
ed esecuzione**. Manca l'organo che mette in fila ciò che esiste e che **istruisce** le due
decisioni che nessun documento obbliga a produrre: un prezzo e una data.

### Decisione

1. **Nasce `company/Ecosistemi/15-LANCI/`.** Il numero è **15**: il 14 è occupato da Tesoreria.
   **Va riservato nel registro dei numeri nello stesso commit che crea la cartella.**
2. **Dodici reparti**, di cui quattro nuovi e otto che avvolgono capacità esistenti — **compreso
   il reparto Vendite & Funnel**, che il primo giro del piano aveva ignorato.
3. **Sette flussi completi**, ognuno con input tipizzato, fasi con l'agente che le esegue, gate con
   criteri numerici, output tipizzato e modi di fallimento.
4. **`IB-L2-LANC` si sposta dentro 15-LANCI**, non si copia e non si riscrive.
5. **Tredici gate bloccanti**, con numerazione unica. Due sono nuovi: quello su prezzo e data, e
   quello che pretende che una pagina misuri per essere considerata online. **Sono precisamente i
   due che avrebbero impedito al Manuale di restare fermo sei mesi.**
6. **La costruzione procede a scaglioni**, e il primo ha come criterio di chiusura **l'uscita
   reale del Manuale Claude Code**. Se non esce, gli altri reparti non si costruiscono — e il
   vincolo è tecnico: il registro rifiuta gli agenti dei reparti non abilitati.
7. **Ogni agente nasce ufficiale**, con il campo degli strumenti che impone meccanicamente le
   regole di comportamento.
8. **Tre condizioni di abbandono scritte prima di cominciare** (dossier 00 §6).

### Le alternative scartate

| Alternativa | Perché scartata |
|---|---|
| **Sistemare il reparto dov'è** | resterebbe di secondo livello dentro Info-Business mentre i lanci toccano cinque ecosistemi. E sistemarlo significa comunque scrivere gli eseguibili che non ha: cioè fare questo lavoro, in un posto dove non ci sta |
| **Un orchestratore senza reparti** | un livello di indirizzamento in più su una pila che già non esegue. Non toglie carta: ne aggiunge |
| **Otto reparti invece di dodici** | lascia senza proprietario quattro cose richieste: piano editoriale, controllo delle spese, memoria, indipendenza dei gate. Diventerebbero "compiti in più" di reparti che hanno già il loro mestiere — e i compiti in più non si fanno |
| **Costruire tutto e poi lanciare** | è il modo in cui è nato il reparto attuale. Lo scaglione minimo esiste per rendere questa strada impossibile |
| **Riscrivere le skill dentro l'ecosistema** | viola la regola di avvolgere invece di riscrivere, e crea due proprietari per ogni capacità |

### Conseguenze

**Positive**
- Un prodotto finito non può più restare fermo senza che qualcuno se ne accorga.
- Ogni lancio produce dati confrontabili: il secondo parte più informato del primo.
- Le undici skill installate smettono di essere strumenti sparsi e diventano una catena.

**Negative, dichiarate**
- **~235 file da creare, 139-187 ore-uomo.** A tre ore al giorno sono circa tre mesi.
- **Rischio reale di sovradimensionamento** per un'azienda di tre persone. Lo scaglione minimo è la
  difesa, ma il rischio resta.
- **Il modello di memoria può morire come il precedente.** I presidi lo rendono meno probabile,
  nessuno lo rende impossibile.
- **Sposta un reparto di un altro ecosistema**: serve il consenso del suo proprietario.
- **Il controllo di conformità dell'Impero oggi esce in errore** per due bloccanti estranei ai
  lanci: finché restano, la verifica finale è insoddisfacibile per ragioni non nostre.

### Le tre decisioni umane che questo ADR non prende

1. **Il Manuale è a pagamento o è un regalo?** Le fonti si contraddicono dall'11 giugno.
   **Decide Max** — il dossier 04 mette le due strade con le conseguenze.
2. **Quale standard per i testi.** **Decide il direttore marketing.**
3. **Quale sistema visivo** per le pagine. **Decide la guild Design.**

---

# PARTE B — IL LANCIO PILOTA

## B.1 Perché il pilota è il Manuale e non un lancio ipotetico

Perché è **la prova più dura disponibile**.

Un ecosistema di lanci si può provare con un prodotto nuovo, dove tutto è da fare e ogni reparto ha
lavoro — oppure con un prodotto **finito da mesi e mai uscito**, dove quasi tutti i reparti non
hanno niente da fare e resta esposto **solo il pezzo che manca davvero**.

Il secondo modo è più scomodo e infinitamente più utile: **se l'ecosistema fa uscire il Manuale, ha
dimostrato di saper fare la cosa che l'azienda non sa fare.** Se lo dimostra su un prodotto nuovo,
ha dimostrato di saper fare le cose che l'azienda già faceva.

## B.2 Cosa il Manuale ha già

| Pezzo | Stato |
|---|---|
| Il prodotto | ✅ 203 pagine, "Pronto" dal 07/03/2026 |
| Il regalo per acquisire contatti | ✅ un framework in 12 pagine, pubblicabile |
| La pagina di vendita | ✅ costruita, 299 righe |
| Il sistema visivo | ✅ 54 righe di regole |
| La libreria di componenti | ✅ ~30 sezioni |
| La struttura del funnel | ✅ |
| Il framework dei testi | ✅ |
| Lo script del webinar | ✅ ~40 pagine |
| Le sequenze email | ✅ |
| **Il prezzo** | ❌ |
| **La data** | ❌ |
| **Il lancio** | ❌ mai avvenuto |

**Nove pezzi su undici esistono.** I due che mancano non sono i più difficili: sono i due che
richiedono una firma.

## B.3 Il criterio con cui si giudica il pilota — e non è il fatturato

| Domanda | Come si risponde | Perché è questa |
|---|---|---|
| Il prodotto è uscito? | c'è un indirizzo pubblico | è la cosa che non è mai successa |
| Sappiamo quanto ha reso? | c'è un numero nel consuntivo, **anche se è zero** | uno zero misurato è un dato; un ricavo ignoto non è niente |
| Sappiamo perché ha reso così? | ogni scarto oltre il 10% ha una causa scritta | senza causa, il prossimo lancio ripete lo stesso |
| Il prossimo parte più avanti? | almeno tre schemi nel banco della memoria | è l'unica cosa che rende il secondo lancio diverso dal primo |
| **I gate hanno bloccato qualcosa?** | almeno un verbale di blocco | **un sistema di controlli che non ha mai bloccato niente non è provato: è solo passato** |

L'ultima riga è la meno intuitiva e la più importante. Se il pilota attraversa tredici gate senza
che nessuno blocchi mai, non abbiamo la prova che funzionino: abbiamo la prova che sono compatibili
con un lancio fatto bene. La differenza si scopre al terzo lancio, quando qualcosa va storto — e
allora è tardi.

## B.4 Cosa può andare storto

| Rischio | Probabilità | Cosa si fa |
|---|---|---|
| **Max non firma il prezzo** | alta — non è stato firmato in sei mesi | il sistema si ferma e lo dichiara. **Non propone un prezzo di ripiego**: un prezzo scelto da una macchina per sbloccare un gate è peggio di un lancio rinviato |
| La contraddizione sul ruolo resta aperta | alta | il gate la nomina come motivo del blocco: non si decide il prezzo di una cosa che non si sa se è in vendita |
| La pagina esistente non traccia niente | media | è ciò che il gate deve scoprire. Se succede, il gate ha già ripagato la costruzione |
| Il lancio incassa poco | media | **non è un fallimento**. Il pilota fallisce se non sappiamo quanto ha incassato |
| Gael costruisce il minimo e si ferma lì | media | sarebbe comunque un guadagno netto rispetto a oggi. Va detto adesso, non scoperto dopo |

---

# PARTE C — I TRE GIRI, E COSA È CAMBIATO

> Il metodo dell'Impero impone che un lavoro grosso si batta da solo prima di essere costruito.
> Qui i giri sono stati tre, e ognuno ha battuto il precedente su punti che si possono nominare.
> **Questa sezione esiste perché, se un giorno una scelta sembrerà strana, qui c'è scritto contro
> cosa è stata presa.**

## C.1 Il primo giro

Otto documenti, 3.761 righe: gerarchia a sei livelli, dodici reparti, sette flussi, 41 agenti,
calendario di costruzione, decisione da registrare, lancio pilota.

## C.2 La critica — tre revisori indipendenti, più l'autocritica

| Chi | Cosa ha prodotto |
|---|---|
| **Autocritica** | 12 crepe, 5 gravi |
| **Revisore dell'architettura** | 891 righe, **50 rilievi**, 16 verifiche eseguite nel codice |
| **Revisore dei flussi** | 398 righe, **56 rilievi** |
| **Verifica delle citazioni** | tutte le citazioni di esistenza controllate una per una sul disco |

**Nessuna delle tre revisioni è stata scritta da chi aveva scritto il piano.** È la stessa regola
che il piano impone a sé stesso: chi produce non approva.

## C.3 I dieci difetti gravi trovati, e cosa è cambiato

| # | Il difetto | La correzione |
|---|---|---|
| 1 | **La squadra minima non poteva produrre prezzo e data.** Nessuno dei nove agenti sapeva scrivere né la ricerca, né il certificato, né il file dell'offerta — che per esplicita ammissione del piano spetta a un agente non incluso. Il lancio si sarebbe fermato al secondo stato **per sempre** | undici agenti su sei reparti, più una **modalità pilota** con attestazione firmata e debito scritto |
| 2 | **Il flusso del funnel non aveva fasi né agenti**: dodici sezioni e nessuno che le eseguisse. Il pre-mortem numero uno, commesso dal piano stesso | nove fasi con l'agente che le esegue, output tipizzato, handoff, fallimenti |
| 3 | **Due gate sul budget non potevano fallire**: uno divideva per una grandezza che nessun campo permetteva di calcolare, l'altro confrontava numeri scritti dalla stessa persona | date e profili di spesa nelle voci; approvazione da chi non ha scritto il budget |
| 4 | **La griglia dei testi dichiarava sessanta punti automatici e ne aveva undici**, e bocciava per costruzione otto pezzi su quattordici | tre griglie per classe di pezzo, quarantadue punti automatici veri, e le voci ambigue rese meccaniche |
| 5 | **Nessun comando dell'Impero può verificare che un agente sia ufficiale** — provato nel codice | l'ecosistema si porta il proprio verificatore |
| 6 | **Vietare il campo degli strumenti** toglieva l'unico modo di impedire a un controllore di riscrivere ciò che giudica | si usa, con un profilo per ruolo |
| 7 | **`SOSPESO` non aveva uscita**, e ci si arrivava automaticamente | stato di partenza, data di revisione e comando di uscita, tutti obbligatori |
| 8 | **Il calendario era incompatibile coi flussi**: un giorno a lavori che ne dichiarano quattro, zero margine per rifacimenti previsti | 38 giorni con 12 di margine dichiarato |
| 9 | **Duplicazione dell'esistente**: un reparto Vendite & Funnel con tre workflow e sei agenti, una sentinella della qualità, una dei costi e uno script di tesoreria — tutti già esistenti, tutti ignorati | avvolti, con il percorso dichiarato |
| 10 | **Una citazione falsa**: il piano diceva che certi componenti accettavano parametri. **Non ne accettano**, e appartengono a un altro prodotto | corretta, con la parametrizzazione trasformata in una fase con le sue ore |

## C.4 Le sei cose che la critica ha confermato buone

Un revisore che boccia tutto è inutile quanto uno che approva tutto. Queste sono passate:

| Cosa | Perché regge |
|---|---|
| **Il campo `misurato`** su ogni record | traduce in dati la legge di verità: un dato assunto non può essere prova |
| **Il gate che ricalcola dai file** invece di leggere i riepiloghi | è la difesa diretta contro un difetto documentato tre volte in questo repo |
| **La scala osservazione → indizio → regola, col declassamento** | una memoria che sale soltanto è una superstizione con la data |
| **Il ribaltamento fra Regia e Memoria** | nessuno dei due scrive da solo la storia di com'è andata |
| **La verifica a campione sulle fonti** | contare quindici frasi si falsifica; aprirne cinque a caso e cercarci dentro la frase, no |
| **Il criterio "un sistema di gate che non ha mai bloccato non è provato"** | è controintuitivo ed è vero |

## C.5 Cosa resta aperto, dichiarato

| Cosa | Stato |
|---|---|
| Il ruolo del Manuale (in vendita o regalo) | **decide Max** — senza, il primo lancio non parte |
| Lo standard dei testi | decide il direttore marketing |
| Il sistema visivo | decide la guild Design |
| I due bloccanti di conformità dell'Impero | **non riguardano i lanci**, ma rendono insoddisfacibile la verifica finale |
| Le pagine del Manuale (203) e del regalo (12) | **non verificate**: i PDF non erano leggibili con gli strumenti disponibili |
| I benchmark del funnel | **provvisori**: vengono da un altro mercato. Il primo lancio produce i veri |
| Le stime di costo | **non misurate**: nessun lancio è mai stato eseguito |

**Sette cose aperte, tutte scritte.** Un piano che non dichiara cosa non sa è un piano che chiede
fiducia invece di darne le ragioni.
