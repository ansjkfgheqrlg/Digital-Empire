# CRITICA-A — dossier 01, 02, 03

> STATO: completo. 30 difetti strutturali · 30 buchi · 24 contraddizioni · 22 punti di prosa · 16 punti solidi.
> Citazioni nella forma `dossier:riga` — `01` = 01-GERARCHIA-E-REPARTI.md, `02` = 02-MEMORIA-E-HANDOFF.md, `03` = 03-WF-PRODOTTO.md.
> Nessun file del repository è stato modificato.

## 1. DIFETTI STRUTTURALI GRAVI

Convenzione di citazione: `01:riga`, `02:riga`, `03:riga`.

---

### D-A-01 · Cinque gate su sette sono eseguiti dallo stesso agente che ha prodotto ciò che il gate giudica
**Dove:** `03:166` (la regola: «chi produce non approva — ogni gate è eseguito da un agente diverso da chi ha prodotto l'output»), poi `03:134`+`03:173` (N1 e GP-1 = `lan-prod-intake`), `03:135`+`03:174` (N2 e GP-2 = `lan-prod-verificatore-ricerca`), `03:138`+`03:176` (N5 e GP-4 = `lan-prod-collaudatore`), `03:141`+`03:178` (N8 e GP-6 = `lan-prod-certificatore`). Contraddice anche `01:30` («il livello L5 non risponde a L3») e tutta la tabella `01:100-111`.

**Perché si rompe:** il gate non è un controllo indipendente ma una seconda lettura dello stesso agente sul proprio verbale. Un difetto sistematico dell'agente produttore è invisibile al gate per costruzione, perché il gate è quell'agente.

**Il caso concreto:** `lan-prod-collaudatore` esegue N5 e scrive `05-collaudo.json`; GP-4 legge `05-collaudo.json` ed è eseguito da `lan-prod-collaudatore`. Se il collaudatore non riconosce come «link» un href dentro un PDF, RF5 esce a zero e GP-4 conferma lo zero. Il prodotto passa con 40 link morti e nessun verbale lo dice. È esattamente il guasto che `03:235` dichiara di voler intercettare.

**Riparazione:** una tabella `artefatto → produttore → esecutore-del-gate` in cui `esecutore ≠ produttore` è un vincolo verificato da `registro.py` prima che `avanza` esegua. In WF-PRD: GP-1, GP-2, GP-4, GP-6 passano a `lan-qlt-gate` (l'agente L5 già previsto in `01:407`), i `lan-prod-*` restano solo produttori. GP-3 e GP-5 sono già corretti e non si toccano.

---

### D-A-02 · Le sigle di reparto del dossier 03 non esistono nei dodici reparti del dossier 01
**Dove:** `01:120-133` definisce `LAN-STR/INT/PRD/OFF/CPY/FNL/TRF/EDT/TSR/REG/QLT/MEM`. Il dossier 03 usa `LAN-PRODOTTO` (`03:56`), `LAN-STRATEGIA` (`03:69`), `LAN-PRICING` (`03:92`, `03:156`, `03:160`, `03:226`), `LAN-COPY` (`03:225`), `LAN-SITI` (`03:227`), `LAN-ESECUZIONE` (`03:228`, `03:317`). Sei sigle, zero corrispondenze letterali.

**Perché si rompe:** `LAN-SITI` e `LAN-ESECUZIONE` non hanno nemmeno un candidato univoco (Funnel? Regia? entrambi?). Il costruttore deve inventare la mappa, e chi la inventa diversamente crea un secondo albero di cartelle.

**Il caso concreto:** `handoff.emetti(da="LAN-PRODOTTO", a="LAN-SITI", ...)` (`02:314`) — nessuno dei due valori appartiene all'enum dei dodici spazi di memoria (`02:60-73`), quindi `scrivi()` rifiuta per proprietario non corrispondente (`02:295`) e il passaggio previsto da `03:227` non è emettibile. Il primo handoff in uscita del primo workflow non parte.

**Riparazione:** tabella di equivalenza in testa al dossier 03, poi rinomina meccanica su una sola nomenclatura (quella dei dodici); `registro.py` rifiuta qualunque sigla fuori dall'enum.

---

### D-A-03 · GP-0…GP-6 e GATE-PRD-1/2/3: la correzione dichiarata non è stata applicata al corpo
**Dove:** `03:16-17` dichiara che «le sigle `GP-*` sono sostituite dalla numerazione unica `GATE-PRD-1/2/3`». Poi `03:170-178` usa sette gate `GP-0`…`GP-6`, e lo schema del certificato `03:195-202` li usa come chiavi JSON. `01:104`, `01:261` e `01:416` usano `GATE-PRD-1/2/3`.

**Perché si rompe:** sette gate non entrano in tre nomi, e la mappa non esiste. Nessun costruttore può sapere quale gate è quale.

**Il caso concreto:** la modalità pilota (`01:416`) ammette l'attestazione firmata per «`GATE-INT-1` e `GATE-PRD-1/2/3`». Non è determinabile se copra GP-4 (i sei red flag) e GP-5 (il beta test) — cioè le uniche due che costano settimane. Il primo lancio reale si ferma su una domanda di nomenclatura, e chiunque risponda ha ragione.

**Riparazione:** scegliere. O sette gate `GATE-PRD-0…6`, o tre gate con i GP declassati a sotto-controlli elencati dentro ciascuno. In entrambi i casi le chiavi del certificato (`03:195-202`) usano i nomi finali, e `01:416` nomina i gate esatti coperti dall'attestazione.

---

### D-A-04 · `lancio.py avanza` — la spina dorsale del sistema — non ha una riga di specifica
**Dove:** `01:33-35` («i gate non sono un reparto da chiamare: sono dentro `lancio avanza`»), `01:358` (compare come `prossimo_passo`), `01:469` («17 file .py»). Confronto: `02:295-317` dà firme complete a `memoria.py`, `pattern.py`, `handoff.py`; `03:252-288` a cinque script di prodotto.

**Perché si rompe:** l'oggetto su cui poggia l'intera tesi del piano — il controllo non è saltabile perché vive dentro l'avanzamento — non ha firma, exit code, lock, politica di idempotenza, invocatore né cadenza.

**Il caso concreto:** Max e Gael lanciano `avanza` sullo stesso `lancio_id` a un minuto di distanza. Due esecuzioni degli stessi gate, due verbali con lo stesso nome file, `stato.json` riscritto due volte da due processi. Oppure il caso opposto e più probabile: nessuno lo digita per tre giorni e il lancio è fermo senza che niente lo segnali, perché non esiste nessun processo che accorga della non-invocazione.

**Riparazione:** specificare `avanza(lancio_id: str, *, solo_gate: str | None = None, dry_run: bool = False) -> int` con lock esclusivo sul file di stato, exit code secondo la convenzione `03:247-249`, verbale idempotente per chiave `(gate, tentativo_n)`, e la dichiarazione esplicita di chi lo invoca e quando (a mano, a ogni chiusura di fase, o via hook).

---

### D-A-05 · La memoria come condizione di chiusura manda in stallo lo scaglione minimo
**Dove:** `02:47` («alla chiusura di ogni fase scrive **il conductor del reparto**, come ultimo atto della fase»), `02:32-34` («una fase non si chiude se non ha scritto il suo record»), `01:396-407` (gli undici agenti minimi).

**Perché si rompe:** fra gli undici c'è un solo conductor, `lan-off-conductor`. Strategia, Intelligence, Prodotto, Funnel e Regia non ne hanno. Se il record di fase lo scrive il conductor e il conductor non esiste, il record non si scrive e la fase non si chiude.

**Il caso concreto:** il lancio pilota entra in `IDEA`, `lan-str-filtro` risponde alle cinque domande, GATE-STR-1 chiede il record di fase di `LAN-STR`; nessuno lo scrive perché LAN-STR non ha conductor. Il primo lancio non supera la prima fase, e la causa è una regola introdotta come la correzione principale del piano.

**Riparazione:** definire «chi chiude la fase» come **funzione** e non come carica: è l'agente che esegue l'ultima attività della fase, chiunque sia. In alternativa aggiungere i cinque conductor mancanti allo scaglione minimo — ma allora il minimo non è undici.

---

### D-A-06 · Il gate della memoria verifica l'esistenza del record, non il suo contenuto
**Dove:** `01:167-169`, `02:32-34`, `02:299` (`verifica_fase(lancio_id, fase) -> bool` — «il record della fase esiste?»).

**Perché si rompe:** un booleano di esistenza si soddisfa con qualunque cosa. Il presidio duro che è la tesi centrale di due dossier è più debole del presidio morbido che sostituisce, perché quello almeno chiedeva un contenuto.

**Il caso concreto:** `{"id":"MEM-LAN-CPY-20261011-4","tipo":"esito","titolo":"fase chiusa","corpo":"ok","fonti":[],"numeri":{},"misurato":false}`. Passa. La fase chiude. Fra sei mesi la memoria contiene undici righe «ok» e il piano dichiarerà di aver risolto il problema del reparto precedente.

**Riparazione:** `verifica_fase(...) -> tuple[bool, list[str]]` con controlli minimi per tipo: `corpo` sopra una lunghezza dichiarata, `fonti` non vuoto per i tipi `misura` ed `esito`, `numeri` non vuoto per `misura`, e il record deve citare il percorso dell'artefatto prodotto dalla fase (che il gate verifica esistente su disco).

---

### D-A-07 · La fase zero si autoconvalida, e la prova che cita non esiste nello schema
**Dove:** `02:148-153` (il gate verifica la consultazione, «e la prova è il campo `letto_il` dei record restituiti» da `pattern.py cerca`), `02:296` (`leggi` incrementa `letto_volte`), `02:116-127` (lo schema `PAT-*` **non ha** né `letto_il` né `letto_volte`).

**Perché si rompe:** doppio guasto. Primo: il comando mostrato a `02:148` interroga i pattern, e lo schema dei pattern non possiede il campo indicato come prova — la prova non è scrivibile. Secondo: se lo fosse, l'atto stesso di verificare incrementerebbe il contatore, quindi il gate produrrebbe la propria prova.

**Il caso concreto:** un agente esegue `pattern.py cerca --reparto LAN-OFF --contesto "x"`, ignora i risultati, e il gate della prima fase passa. In più il contatore così gonfiato è lo stesso che alimenta l'indice di salute della memoria (`02:178`), quindi la macchina di verifica falsifica la propria metrica.

**Riparazione:** la prova è un **record di consultazione** scritto dal chiamante: la query eseguita, i `pattern_id` restituiti, e per ciascuno con forza ≥ `indizio` la dichiarazione «applicato» o «scartato perché…». Il gate verifica che nessun indizio applicabile sia rimasto senza risposta. E `leggi` non incrementa: l'incremento è un atto separato ed esplicito.

---

### D-A-08 · L'handoff scaduto diventa un blocco permanente: rientra l'abbandono silenzioso che §4.3 dichiara di aver chiuso
**Dove:** `02:236-238` («un passaggio scaduto diventa un blocco: compare in `bloccato_da` e la fase dipendente non parte»), `01:353-357` (`handoff_pendenti` nello stato), `01:304` (il trigger di SOSPESO è «decisione mancante alla scadenza, o conflitto non risolto»).

**Perché si rompe:** `bloccato_da` è un campo, non uno stato. Un handoff scaduto non rientra in nessun trigger di SOSPESO, non ha timer, non ha escalation. Il lancio resta in `IN_PRODUZIONE` con un campo valorizzato che nessun processo osserva.

**Il caso concreto:** `HO-20261011-3` scade il 13 ottobre (`01:355`). Il 14 la fase FNL non parte. Lo stato dice `IN_PRODUZIONE`. Nessuno apre `stato.json`. Il 28 ottobre si scopre che il calendario è saltato — che è **letteralmente** il sintomo descritto a `02:228` come il difetto già corretto.

**Riparazione:** scadenza dell'handoff = transizione automatica a `SOSPESO` con `stato_di_partenza`, `bloccato_da = "HO-…"` e `come_si_esce` = comando di riemissione. Oppure escalation a L2 a scadenza + 24 h. In ogni caso una **transizione**, non un campo.

---

### D-A-09 · SOSPESO restituisce a uno stato già bloccato: la sospensione non ferma gli orologi
**Dove:** `01:284`, `01:309-337` (il rientro allo `stato_di_partenza`), `02:236` (48 ore di validità di ogni handoff).

**Perché si rompe:** la durata della sospensione non è limitata (fino a 90 giorni, `01:306`), la validità degli handoff sì (48 ore). Al rientro tutti i pendenti sono scaduti.

**Il caso concreto:** lancio sospeso il 20/09 per firma del prezzo mancante (`01:320-327`), riattivato il 15/10. `stato_di_partenza = ISTRUITO`, si rientra — e ogni handoff pendente è scaduto da 23 giorni, quindi `bloccato_da` si rivalorizza subito. L'uscita da SOSPESO esiste sulla carta e restituisce a un blocco. La correzione fiore all'occhiello del dossier 01 non funziona per la sua stessa causa di ingresso più frequente.

**Riparazione:** entrare in SOSPESO congela `scade_il` di tutti i pendenti (si salva il residuo, non la data assoluta); l'uscita li riemette con nuova scadenza e lascia un record di riemissione in `memoria/regia/`.

---

### D-A-10 · 48 ore fisse, senza calendario lavorativo, in un'azienda di due persone
**Dove:** `02:236` («48 ore dall'emissione, salvo diversa indicazione del calendario»); esempio coerente a `01:355` (11 → 13 ottobre).

**Perché si rompe:** la scadenza è in ore solari e il lavoro è in giorni lavorativi. Nessun calendario di festività o di giorni non lavorati è definito da nessuna parte, e `calendario.md` è un file di prosa (`01:131`).

**Il caso concreto:** handoff emesso venerdì alle 18:00 scade domenica alle 18:00. Lunedì mattina il lancio è bloccato senza che sia successo niente. Con un handoff a settimana emesso di venerdì, succede al primo lancio.

**Riparazione:** `scade_il` calcolato in giorni lavorativi da un file `calendario-lavorativo.json` dichiarato, oppure derivato dalla data della fase dipendente nel calendario del lancio. Mai una costante.

---

### D-A-11 · GP-5 e la soglia €97: il gate si spegne cambiando un numero deciso da chi ha fretta
**Dove:** `03:139` (beta obbligatorio ≥ €97), `03:112` (se `offerta_path` è null si assume il caso peggiore), `03:156` («se LAN-PRICING nel frattempo fissa un prezzo < €97, il gate si rilegge e **il beta decade**»), `03:177` (AUTO-PASS sotto soglia).

**Perché si rompe:** il prezzo lo fissa lo stesso perimetro umano che vuole aprire la vendita (decisione 1 delle nove, `01:65`). Il piano prevede **esplicitamente** il decadimento del controllo al ribasso del prezzo, e non prevede niente al rialzo dopo la certificazione.

**Il caso concreto:** prezzo fissato a 89 € per chiudere il pilota → GP-5 AUTO-PASS → certificato emesso senza beta. Due settimane dopo, prima dell'apertura, il prezzo sale a 197 €. Nessuna regola riapre GP-5. Un prodotto da 197 € esce con zero beta tester e un certificato formalmente valido.

**Riparazione:** il certificato porta `prezzo_massimo_certificato`; `GATE-OFF-1` e `GATE-REG-1` bloccano se il prezzo dell'offerta lo supera, e la sola uscita è riaprire GP-5. Per il primo lancio, AUTO-PASS vietato.

---

### D-A-12 · Il prodotto pilota riceve due prescrizioni opposte dai due dossier
**Dove:** `01:416-436` (modalità pilota: attestazione firmata, con il testo esplicito «I sei controlli non sono stati eseguiti») contro `03:145` («il percorso E salta la PRODUZIONE, non salta MAI la CERTIFICAZIONE») e `03:155` (E3 = collaudo integrale, «ogni link delle 203 pagine testato in incognito»).

**Perché si rompe:** stesso prodotto, stesso primo lancio, due regole incompatibili scritte lo stesso giorno. Il dossier 01 permette di attestare via i sei red flag; il dossier 03 fonda l'intera esistenza del percorso E sul non poterli attestare.

**Il caso concreto:** Max firma l'attestazione di `01:423`. Il collaudatore, che segue il dossier 03, blocca comunque su RF5. Chi ha ragione non è deducibile dai documenti, quindi decide chi urla di più — che è il modo in cui i gate muoiono.

**Riparazione:** decidere e scriverlo in un punto solo. Proposta motivata: l'attestazione copre `GATE-INT-1` (la ricerca a monte di un prodotto già scritto) e **mai** RF5/RF2/RF1, perché sono automatici e costano minuti, non giorni. Ciò che si attesta deve essere solo ciò che è costoso *e* umano.

---

### D-A-13 · Le durate del percorso E si contraddicono tre volte e sono impossibili con il beta obbligatorio
**Dove:** `03:18` («il percorso per prodotti già esistenti è **20-30 ore**»), `03:57` («Percorso E: **3-5 giorni lavorativi**»), `03:308` (target «≤5 giorni lavorativi»), contro la somma delle fasi `03:152-157`: E1 2-4 h + E2 0,5-1 g + E3 0,5-1 g + **E4 5-7 g** + E5 0,5 g.

**Perché si rompe:** `03:156` rende il beta **obbligatorio** per il Manuale (prezzo ignoto → caso peggiore). E4 da solo eccede l'intera durata dichiarata.

**Il caso concreto:** il minimo reale per il prodotto di copertina è ~7-9 giorni lavorativi. Il numero di copertina (3-5) è falso per il caso di copertina, e diventa il target di §12 su cui il workflow verrà giudicato fallito al primo giro.

**Riparazione:** due durate dichiarate e separate — «percorso E senza beta» e «percorso E con beta» — e il target di `03:308` riferito a quella applicabile al caso concreto.

---

### D-A-14 · La soglia sulle URL: la correzione annunciata non è nel corpo, e restano tre criteri diversi sullo stesso file
**Dove:** `03:20` («il criterio *100% delle fonti raggiungibili* è allineato a ≥90%») contro `03:135` («verifica che il **100%** delle URL risponda») e `03:174` («100% URL con HTTP 200/301»); e `02:245`, dove lo stesso artefatto passa con «15/5/3/3, ogni frase con fonte» e nessun controllo di raggiungibilità; e `01:103`, dove il criterio di `GATE-INT-1` non è dato affatto.

**Perché si rompe:** il dossier dichiara in testa di aver risolto un conflitto di soglie che «mandava il primo lancio in stallo fra due reparti», e lascia nel corpo la soglia vecchia, due volte. Un changelog che asserisce correzioni non applicate è peggio dell'assenza di changelog, perché induce il revisore a non verificare.

**Il caso concreto:** 17 fonti, 1 sito dietro Cloudflare che risponde 403 a un client non-browser. `03:174` boccia (100% richiesto, e comunque accetta solo 200/301: un 302 basta a fallire). `03:20` passerebbe (16/17 = 94%). Il verbale dirà una cosa o l'altra secondo quale riga ha letto chi ha scritto il codice.

**Riparazione:** una sola definizione, in un file di criterio posseduto da `LAN-QLT` (`01:144`) e letto sia da `GATE-INT-1` sia da GP-2; stati accettati 200/301/302/307/308; e la soglia dichiarata una volta.

---

### D-A-15 · `ricerca.json` è validato due volte, da due reparti, con criteri diversi e senza precedenza
**Dove:** `01:103` (`ricerca.json` → prodotto da LAN-INT, validato da `GATE-INT-1`), `03:135`+`03:174` (GP-2 lo rivalida dentro WF-PRD e può respingerlo «al WF Intelligence»), `01:144` («la Qualità possiede i criteri»).

**Perché si rompe:** due gate sullo stesso artefatto, criteri diversi (D-A-14), nessuna regola di precedenza, e un terzo soggetto che dovrebbe possedere entrambi i criteri contraddittori.

**Il caso concreto:** `ricerca.json` passa `GATE-INT-1` e viene respinto da GP-2. Di chi è la fase bloccata? La macchina a stati (`01:295`) mette GATE-INT-1 e GATE-PRD-* nella **stessa** transizione VALUTATO → ISTRUITO, mentre `03:70` dice che WF-PRD parte solo per ordine umano esplicito, dopo. I due dossier ordinano gli stessi controlli in modo incompatibile.

**Riparazione:** un solo gate sull'artefatto (`GATE-INT-1`), con il criterio più severo dei due. PRD riceve e si fida del verbale; se trova un difetto apre un **rifiuto di handoff** (`02:272-285`), che è il meccanismo già progettato per questo, non un secondo gate.

---

### D-A-16 · Gli identificativi collidono: contatore giornaliero senza allocatore
**Dove:** `01:205` e `02:79` (`MEM-<REPARTO>-<AAAAMMGG>-<n>`), `02:191` (`HO-<AAAAMMGG>-<n>`), `02:118` (`PAT-<AAAAMMGG>-<n>`), contro la regola `02:100` («un identificativo non si riassegna mai»).

**Perché si rompe:** `<n>` è un progressivo giornaliero e nessuno ne è l'allocatore. Non c'è lock, non c'è contatore atomico, e l'identificativo dell'handoff non contiene nemmeno il `lancio_id` (che pure è un campo del record).

**Il caso concreto:** due lanci in corso — previsti esplicitamente da `01:54` — e sei agenti di `LAN-CPY` (`01:126`) che chiudono lo stesso pomeriggio. Due di loro leggono la cartella, contano 2 record, scrivono entrambi `MEM-LAN-CPY-20261011-3`. Il secondo sovrascrive il primo: la regola più solenne della memoria è violata dal formato dell'identificativo che la enuncia.

**Riparazione:** identificativo `<prefisso>-<AAAAMMGG>-<lancio_id>-<progressivo allocato sotto lock>` oppure UUIDv7; l'allocazione vive solo dentro `memoria.py` / `handoff.py`, mai nel chiamante.

---

### D-A-17 · La proprietà di scrittura è dichiarata dal chiamante: la garanzia confronta un valore con se stesso
**Dove:** `02:295` (`scrivi(reparto: str, ...)` — «rifiuta se il proprietario non corrisponde al reparto»), contro `02:57` («un solo proprietario di scrittura per spazio: quando due processi scrivono nello stesso posto, prima o poi uno mente»).

**Perché si rompe:** `reparto` è un parametro passato dall'agente. La funzione verifica che la stringa dichiarata corrisponda alla cartella dedotta dalla stringa dichiarata.

**Il caso concreto:** un agente di Copy passa `reparto="LAN-QLT"` e scrive un verbale in `memoria/qualita/`. La verifica passa. Lo spazio dei verdetti — quello che `01:195` vuole contenere «ogni verdetto, inclusi tutti i blocchi» — è scrivibile da chiunque.

**Riparazione:** il reparto si ricava dall'identità dell'agente chiamante tramite il registro (`01:482`), non dal parametro; il parametro, se resta, serve solo a fallire quando diverge dall'identità ricavata.

---

### D-A-18 · `criterio_accettazione` è prosa italiana e `accetta()` dichiara di verificarla
**Dove:** `02:198-203` (lista di frasi: «almeno 15 frasi, ognuna con fonte verificabile»…), `02:315` (`accetta(handoff_id, chi) -> dict` — «verifica il criterio prima di accettare»).

**Perché si rompe:** nessuna funzione valuta una frase in italiano. O il criterio diventa un predicato, o `accetta()` è un timbro con una firma che promette il contrario.

**Il caso concreto:** il destinatario chiama `accetta("HO-20261005-1", "lan-cpy-conductor")`. La funzione non può fare altro che ritornare accettato. Tutta la macchina degli handoff — il secondo dei due «sistemi nervosi» del dossier 02 — non ha un solo controllo eseguibile.

**Riparazione:** `criterio_accettazione` come lista di predicati tipizzati `{id, check, campo, operatore, valore}` più un registro che mappa `check` a callable; la frase italiana resta come `descrizione` per gli umani. È la riparazione a più alto rendimento del piano perché sblocca tutti gli undici criteri di `02:243-254` in un colpo.

---

### D-A-19 · `LAN-TRF` non ha gate né riga nella tabella dei controlli: l'unico reparto che spende non è controllato
**Dove:** `01:100-111` (la tabella «chi produce ≠ chi approva» elenca dieci righe: mancano `LAN-TRF` e `LAN-QLT`), `01:128` (LAN-TRF produce `traffico.json`), `01:26` (tredici gate — nessuno è `GATE-TRF-*`).

**Perché si rompe:** il reparto che compra traffico produce un artefatto che nessun gate valida e nessuna riga assegna a un validatore. L'unica soglia che tocca quel denaro è il veto di L1 finanza (`01:50`), che è fuori dal flusso di avanzamento e quindi, per la logica del piano stesso (`01:33-35`), saltabile.

**Il caso concreto:** `traffico.json` dichiara un costo per acquisizione di 3,20 €. Il consuntivo di `LAN-TSR` dice 11 €. Nessun gate confronta i due numeri, nessuno possiede la divergenza, e il debrief la scoprirà a lancio chiuso.

**Riparazione:** `GATE-TRF-1` (ogni campagna ha un identificativo tracciabile; la spesa dichiarata coincide con quella consuntivata entro una tolleranza dichiarata) e la riga mancante in `01:100-111`.

---

### D-A-20 · Lo scaglione minimo non può eseguire l'unico workflow specificato — e usa contro se stesso il metodo con cui ha bocciato il precedente
**Dove:** `01:396-407` (gli undici) contro `03:133-141` e `03:152-157` (le fasi di WF-PRD).

**Perché si rompe:** mancano `lan-prod-intake` (N0, GP-0, GP-1), `lan-prod-verificatore-ricerca` (N2, GP-2), `lan-prod-certificatore` (N8/E5, GP-6) e `lan-prod-inventariante` (E1 — obbligatorio proprio nel percorso del pilota). In più la giustificazione dell'agente #4 (`01:400`: «`lan-prd-collaudatore` — senza, `certificato-prodotto.json` non esiste») è **falsa**: il certificato lo emette `lan-prod-certificatore` (`03:141`, `03:178`).

**Il caso concreto:** identico a quello che `01:386-392` usa per demolire lo scaglione precedente. Con gli undici, il pilota entra in WF-PRD e non ha nessuno che validi l'input, nessuno che censisca i 203 fogli, nessuno che emetta il certificato. Il dossier applica un metodo di verifica alla versione precedente e non lo riapplica alla propria.

**Riparazione:** derivare lo scaglione minimo dai workflow invece di elencarlo a mano — uno script che legge i `WF-*.md`, estrae ogni agente citato in colonna «Agente» e stampa l'insieme. Il minimo è quell'insieme, per costruzione, e si aggiorna da solo.

---

### D-A-21 · Il debito della modalità pilota non ha rappresentazione né esattore
**Dove:** `01:424` (`"debito": "collaudo integrale entro il primo lancio successivo"`), `01:432` («genera un debito scritto che compare nello stato dei lanci successivi»), contro `01:341-361` (lo schema del file di stato **non ha** un campo per i debiti) e l'assenza di qualunque gate che lo legga.

**Perché si rompe:** il meccanismo che rende l'eccezione «progettata invece che improvvisata» (`01:435`) è promesso e non rappresentato. È, esattamente, un presidio morbido — la categoria che il piano condanna a `01:174-176`.

**Il caso concreto:** lancio 2 parte, nessuno ricorda il debito, `GATE-PRD-*` gira in modalità normale su un prodotto diverso, e il collaudo integrale del Manuale non avviene mai. L'attestazione «vale una volta sola» ha funzionato; il debito no.

**Riparazione:** campo `debiti: [{gate, lancio_origine, scadenza, saldato_da}]` nel file di stato dell'ecosistema; `GATE-STR-1` del lancio successivo blocca l'ingresso se esiste un debito scaduto e non saldato.

---

### D-A-22 · La coerenza specifica ↔ agente è verificata solo per esistenza, e non è collegata a niente
**Dove:** `01:481-482` («ogni agente esiste due volte… `registro.py` verifica che nessuna delle due esista senza l'altra»).

**Perché si rompe:** due file possono esistere entrambi e dire cose opposte. E non è detto cosa fa `registro.py` quando trova un disallineamento, né chi lo invoca, né se il suo esito blocca qualcosa.

**Il caso concreto:** la specifica in `Reparti/LAN-PRD/agenti/lan-prod-collaudatore.md` dice che esegue N5 e **non** GP-4; il file in `.claude/agents/` dice che esegue entrambi. Il registro è verde. Il difetto D-A-01 sopravvive alla verifica progettata per trovarlo.

**Riparazione:** un blocco contratto (nome, missione, input, output, gate presidiati) presente identico nei due file, confrontato per hash; l'esito verde di `registro.py` è una **precondizione di `avanza`**, non un controllo facoltativo.

---

### D-A-23 · La produzione parallela scrive tutta dentro un unico file indice
**Dove:** `03:137` («i moduli si producono in parallelo, 1 istanza agente per modulo») con output `prodotto/04-produzione.json` unico («indice: modulo → file → stato»).

**Perché si rompe:** N scrittori concorrenti su un solo JSON senza lock né strategia di fusione. L'ultimo che scrive vince e perde gli altri.

**Il caso concreto:** cinque agenti chiudono a due secondi l'uno dall'altro; l'indice finale elenca due moduli su cinque. GP-6 ricalcola dai file (`03:178`), trova la divergenza, blocca, e apre una voce in `REGISTRO-ERRORI` per un difetto di concorrenza attribuito al prodotto. Il miglior meccanismo del piano viene consumato a diagnosticare un baco che il piano stesso ha introdotto.

**Riparazione:** uno stato per modulo (`prodotto/contenuti/M0n/stato.json`, scritto solo dal proprio agente) e `04-produzione.json` **generato** per aggregazione, mai scritto in concorrenza. È lo stesso principio dell'indice generato della memoria (`01:247`), non applicato qui.

---

### D-A-24 · `misurato` è un booleano autodichiarato che governa l'ammissibilità della prova, e nessuno lo consuma
**Dove:** `02:108` («`misurato: false` ⇒ nessun gate può usare quel record come prova»), `01:226`.

**Perché si rompe:** lo scrive lo stesso reparto che vuole usare il record come prova, senza definizione di cosa significhi «misurato». E nessun gate descritto nei tre dossier legge mai un record di memoria come prova: il campo non ha consumatori.

**Il caso concreto:** `LAN-TRF` scrive un record con `misurato: true` e `numeri: {"cpa": "3.20"}` senza allegare la fonte. Formalmente ammissibile. In pratica: nessun gate lo legge, quindi il campo è inerte in entrambe le direzioni.

**Riparazione:** `misurato` derivato e non dichiarato — vero solo se `numeri` non è vuoto **e** `fonti` contiene almeno un percorso esistente su disco o una URL con esito di verifica registrato. E almeno un gate che lo consuma davvero, altrimenti si toglie il campo.

---

### D-A-25 · `scaduto_il: null` di default rende inerte tutto l'impianto anti-marciume
**Dove:** `02:93` (default `null`), `02:175` e `01:244` (la potatura archivia i record «scaduti **e** mai letti»), `01:186` («12 mesi») contro `02:63` («3-12 mesi per tipo», tipi mai enumerati).

**Perché si rompe:** nessuno assegna `scaduto_il`, e la potatura richiede la congiunzione. Se `scaduto_il` è sempre null, la potatura non tocca mai nulla e l'indice non migliora mai.

**Il caso concreto:** dopo tre lanci, `memoria/intelligence/` contiene 140 record con `scaduto_il: null`, di cui 130 mai letti. La potatura ne archivia zero. La sentinella del 40% suona, non blocca nulla (D-A-26), e la memoria continua a crescere.

**Riparazione:** `scaduto_il` calcolato **alla scrittura** da una tabella `tipo → durata` dichiarata una volta sola per entrambi i dossier, con i tipi enumerati; nessun record può nascere senza.

---

### D-A-26 · La soglia del 40% di mai-letti è vera dal primo giorno, non ha conseguenza, ed è il presidio morbido che il piano condanna
**Dove:** `01:247`, `02:178-182` («sopra il 40% di mai-letti **la sentinella lo segnala**»), contro `01:174-176` («i presidi morbidi sono tutti saltabili senza che succeda niente»).

**Perché si rompe:** al lancio 1 la memoria è al 100% di mai-letti per costruzione — nessuno ha ancora avuto occasione di leggere ciò che si sta scrivendo adesso. La sentinella suona dal primo giorno e non smette. E «segnala» non è una conseguenza: nessun blocco, nessun destinatario, nessuna azione dovuta. La motivazione di `02:180-182` («una memoria letta al 60% è viva») è una spiegazione, non una fonte.

**Il caso concreto:** l'allarme fisso viene ignorato entro due settimane — che è il modo documentato in cui muore ogni allarme — e diventa rumore permanente nel cruscotto.

**Riparazione:** misurare solo i record con più di 30 giorni; la conseguenza è un blocco reale — l'apertura del lancio successivo non passa `GATE-STR-1` finché il capo reparto non ha chiuso le voci mai lette (leggendole o archiviandole con ragione scritta).

---

### D-A-27 · Sospensioni impossibili non sono vietate, e manca il ritorno da una vendita rotta in corsa
**Dove:** `01:284` («da qualunque stato → SOSPESO»), `01:301-302` (APERTO e CHIUSO sono stati come gli altri).

**Perché si rompe:** un lancio `APERTO` è una pagina viva che incassa. «Sospendere» non ha nessun effetto sul mondo esterno: la pagina resta su e i pagamenti passano. E non esiste `APERTO → IN_PRODUZIONE`: l'unico presidio sul tracciamento e sul pagamento (`01:301`) agisce **prima** dell'apertura, mai durante.

**Il caso concreto:** giorno 2 di vendita, il webhook di pagamento smette di consegnare gli accessi. Il piano non ha uno stato per «vendita fermata»: si può solo andare in SOSPESO, che non spegne il carrello, e tornare in APERTO, che non prova che il guasto sia risolto.

**Riparazione:** SOSPESO vietato da APERTO e da CHIUSO; nuovo stato `APERTO_FERMATO` con l'azione esterna dichiarata (chi spegne il carrello, con quale comando) e ritorno ad APERTO solo con una nuova prova di pagamento registrata.

---

### D-A-28 · `IN_PRODUZIONE ↔ DATATO` può ciclare all'infinito e ignora che la data è già pubblica
**Dove:** `01:297-298` (la transizione di rientro per budget saltato, `GATE-TSR-2`).

**Perché si rompe:** nessun contatore di rientri, nessuna uscita verso SOSPESO o ABORTITO allo sforamento ripetuto, e nessuna regola su cosa succede quando la data — che è ciò che `DATATO` significa — è già stata comunicata al pubblico. Rientrare in DATATO non annulla una promessa fatta fuori.

**Il caso concreto:** budget saltato tre volte in due settimane. Il lancio oscilla fra due stati, il calendario è pubblico, e la decisione 8 delle nove («annullare o rinviare tocca promesse già fatte al pubblico», `01:72`) non viene mai innescata perché la macchina considera il rientro una transizione automatica.

**Riparazione:** massimo due rientri, poi SOSPESO con revisione; e un campo `data_comunicata: bool` che, se vero, rende ogni rientro una decisione umana esplicita, non una transizione di gate.

---

### D-A-29 · `PRONTO → IN_PRODUZIONE` non ha un gate che possa attivarla
**Dove:** `01:300` («un gate rifiuta dopo la sincronizzazione», autorizzato da «il gate che rifiuta»).

**Perché si rompe:** nessun gate è definito per girare nello stato `PRONTO`. `GATE-REG-1` presidia l'**ingresso** in PRONTO (`01:299`). Quindi la transizione ha una condizione, un autorizzatore generico e nessun soggetto che possa innescarla.

**Il caso concreto:** un lancio entra in PRONTO il lunedì e apre il venerdì. Giovedì la pagina di checkout si rompe. Nessun gate è schedulato per accorgersene, quindi la transizione di ritorno progettata per questo caso non si attiva mai.

**Riparazione:** dichiarare quali gate rigirano in PRONTO e con quale cadenza (tipicamente `GATE-FNL-1` e `GATE-TSR-2` come ricontrollo pre-apertura, a T-24h), e chi li invoca.

---

### D-A-30 · L'exit code 3 non ha un posto nella macchina a stati
**Dove:** `03:248-249` («**3** = errore d'ambiente (rete, filesystem) — riprovabile»), contro `01:288-307` (nessuna transizione copre un tentativo fallito per cause ambientali) e `01:304` (SOSPESO si innesca su decisione mancante o conflitto, né l'uno né l'altro).

**Perché si rompe:** «riprovabile» non dice quante volte, con quale attesa, chi riprova, e a che punto un errore d'ambiente ripetuto smette di essere ambiente e diventa un difetto da registrare.

**Il caso concreto:** `verifica_url` (`03:263`) gira mentre la rete è giù. Exit 3. Il lancio resta dov'è, senza verbale (perché non è un BLOCK), senza traccia, senza blocco. Il giorno dopo nessuno sa che il tentativo c'è stato.

**Riparazione:** politica di ritentativo dichiarata (n tentativi, backoff, finestra); esaurita, un blocco con causa `ambiente` che compare in `bloccato_da` e porta il proprio `come_si_esce`, come già fa SOSPESO (`01:326`).

## 2. BUCHI — cose che il piano NON dice e che servono per costruire

Ognuna di queste il costruttore dovrebbe inventarsela da solo. Ogni invenzione è una divergenza fra due costruttori.

**B-A-01 · Le cinque domande di `GATE-STR-1`.** `01:292` e `02:245` le rendono il criterio della prima transizione del sistema. Non sono scritte in nessuno dei tre dossier. Il primo gate del primo lancio non è implementabile.

**B-A-02 · Le dieci voci di `GATE-REG-1`.** `01:299` («le dieci voci vere insieme», e «una sola voce falsa» blocca). L'elenco non esiste. È il gate che precede l'apertura della vendita.

**B-A-03 · Nove schemi JSON su dieci.** `01:470` promette una cartella `schemi/` con «gli schemi JSON, uno per artefatto». Ne viene consegnato **uno**: `certificato-prodotto.json` (`03:184-207`). Mancano `decisione.json`, `ricerca.json`, `offerta.json`, `funnel.json`, `traffico.json`, `piano-editoriale.json`, `budget.json`, `03-architettura.json`, il manifesto di `copy/`, e il file di stato dell'ecosistema (quello del singolo lancio esiste come esempio, `01:341-361`, non come schema).

**B-A-04 · Lo schema del verbale di gate.** È l'oggetto più citato dei tre dossier (`01:110`, `01:132`, `02:207`, `03:168`, `03:172-178`) ed è **precondizione** dell'emissione di ogni handoff (`02:314`). Non ha campi, non ha convenzione di nome file, e non è detto se ne esista uno per gate o uno per tentativo — il che decide se un secondo tentativo sovrascrive la prova del primo.

**B-A-05 · La mappa artefatto → gate → percorso del verbale.** `emetti(da, a, artefatto, lancio_id)` (`02:314`) deve rifiutare se manca il verbale del gate, ma la firma non ha un parametro gate e nessuna tabella lega `ricerca.json` a `GATE-INT-1` a `gate/GATE-INT-1-verbale.json`. La funzione non ha modo di trovare ciò che deve verificare.

**B-A-06 · Le quattro sentinelle.** Citate tre volte (`01:26`, `01:59`, `01:132`) e mai nominate. `01:59` dice che bloccano «ciò che la sua soglia dichiara bloccante»: in tre dossier esiste **una** soglia di sentinella (il 40% di mai-letti) e non blocca niente.

**B-A-07 · Il criterio di otto gate su tredici.** Hanno criterio utilizzabile solo `GATE-PRD-*` (via i GP di `03:170-178`) e parzialmente `GATE-INT-1`. `GATE-CPY-1`, `GATE-FNL-1`, `GATE-EDT-1`, `GATE-TSR-1`, `GATE-TSR-2`, `GATE-STR-1`, `GATE-OFF-1`, `GATE-REG-1`, `GATE-MEM-1` hanno una frase o niente.

**B-A-08 · Chi invoca `avanza`, quando, con quale cadenza.** Se è manuale, il sistema si ferma nel momento esatto in cui nessuno lo digita — e non esiste niente che si accorga della non-invocazione. Se è automatico, non è dichiarato nessun processo che lo esegua.

**B-A-09 · La concorrenza fra lanci.** `01:54` assegna a L1 il potere di dare «priorità fra lanci concorrenti», quindi due lanci insieme sono previsti. Poi: nessun lock, nessuna coda, nessuna regola su risorse condivise (gli stessi agenti, la stessa memoria, lo stesso Max). E `01:52` blocca il «lancio che sfora la capacità dichiarata» senza dire dove la capacità è dichiarata né in che unità.

**B-A-10 · L'identità degli agenti e la firma umana.** Chi è «il chiamante» per `scrivi()` (`02:295`)? Cosa impedisce a un agente di scrivere `"firma_umana": "Max"` (`03:201`) o `"attestato_da": "Max"` (`01:422`)? Le nove decisioni non delegabili (`01:63-73`) sono protette da stringhe in un JSON.

**B-A-11 · Versione, backup e ricostruzione del file di stato.** `01:341-361` è il file più critico del sistema e l'unico schema senza `versione_schema` — mentre l'handoff ce l'ha (`02:191`) con la motivazione esplicita a `02:218`. Nessun journal, nessuna copia, nessuna procedura se si corrompe.

**B-A-12 · L'invalidazione a valle di un artefatto modificato.** Il beta (`03:139`) impone fix che toccano i moduli; `03-architettura.json` è già stato consegnato a LAN-COPY come materia prima dei bullet (`03:225`) e a LAN-PRICING (`03:226`). Nessun versioning dell'artefatto, nessuna notifica, nessuna regola che invalidi il copy costruito su una trasformazione poi cambiata.

**B-A-13 · Il costo di esecuzione.** Un ecosistema con 45 agenti (somma di `01:122-133`) non ha una stima di token o euro per lancio, né un tetto, benché esista un veto finanziario con soglia (`01:50`) e l'azienda operi con una regola di dry-run. Il budget del sistema non è nel `budget.json` del lancio (che è il budget del **lancio**, `01:143`).

**B-A-14 · Il tempo umano per lancio.** Sei decisioni su Max (`01:78`) + approvazione moduli a N3 (`03:136`) + reclutamento beta (`03:139`) + firma ≥€97 (`03:141`) + le due firme di `01:106` e `01:110` + le eventuali deroghe. Nessun conteggio dei punti di contatto né del ritardo atteso — che è la variabile che decide se il sistema gira o vive in SOSPESO.

**B-A-15 · La tassonomia degli eventi di tracciamento.** «Ogni pagina risponde **e registra l'evento**» (`02:249`), «pagina che non traccia» (`01:51`, `01:301`). Quali eventi, con quali proprietà, verificati come (browser headless? log di server? interrogazione dell'analytics?). È la condizione di due blocchi diversi e non ha definizione.

**B-A-16 · Cosa prova un pagamento.** `01:301` blocca l'apertura su «pagamento non provato». Una transazione reale poi rimborsata? Con quale carta? Fatta da chi? Registrata dove? È l'ultimo controllo prima dei soldi veri e non ha procedura.

**B-A-17 · Il formato del calendario.** `calendario.md` è l'unico artefatto in markdown (`01:131`) e da esso dipendono tre meccanismi automatici: la finestra di correzione dopo un rifiuto (`02:280`), la scadenza degli handoff (`02:236`, «salvo diversa indicazione del calendario») e la data entro cui serve una decisione (`01:85`). Tre automatismi appesi a un file di prosa.

**B-A-18 · Dove vivono i conflitti.** `01:85` scrive `conflitti/CONF-<data>-<n>.md`. La cartella `conflitti/` non compare nella struttura dei file (`01:459-473`).

**B-A-19 · Dove vivono i verbali e gli handoff.** `02:207` cita `gate/GATE-INT-1-verbale.json`; la cartella `gate/` non compare né in `01:459-473` né nell'elenco dei file prodotti (`03:209-219`). Gli handoff sono un campo di stato (`01:353`) **e** un file con schema (`02:189-211`): non è detto se siano lo stesso oggetto, e il file non ha percorso.

**B-A-20 · Sei script su diciassette.** `01:469` dichiara «17 file .py». Dai tre dossier se ne nominano undici (`lancio.py`, `stato_lancio.py`, `memoria.py`, `pattern.py`, `handoff.py`, `registro.py`, `prodotto_intake.py`, `verifica_ricerca.py`, `gate_architettura.py`, `collaudo_red_flag.py`, `certifica_prodotto.py`). Gli altri sei non esistono nemmeno come nome.

**B-A-21 · Il formato dei file di criterio della Qualità.** `01:144`: LAN-QLT «scrive i file di criterio e le griglie di punteggio, e li mantiene». Nessun formato, nessun percorso, nessun meccanismo che leghi quel file al codice del gate. Se il criterio vive in un `.md` e il gate lo riscrive in Python, i due si separano al primo cambio e nessuno se ne accorge.

**B-A-22 · Come nasce un lancio.** Non esiste il comando di inizializzazione, non è detto chi assegna il `lancio_id`, né qual è il formato canonico (`01:343` usa `2026-10-manuale-claude-code`, `03:41` lascia `<lancio_id>` libero, `01:471` la cartella `<AAAA-MM>-<prodotto>`).

**B-A-23 · Chi produce `input-prodotto.json`.** `03:75` è il file che avvia tutto WF-PRD e non ha un produttore dichiarato. Lo scrive Max a mano? Lo genera `lancio.py`? Lo compone LAN-STR? L'unico input del workflow è orfano.

**B-A-24 · Il piano di migrazione dell'esistente.** `01:131` dice che `IB-L2-LANC` «si sposta»; `03:59-63` dice che le dieci schede di `IB-L2-PROD` vengono «ufficializzate». Nessuna procedura, nessun elenco di riferimenti da aggiornare, nessuna regola sui puntatori che restano indietro — in un progetto che ha una regola esplicita contro i puntatori stale, e che a `03:36-38` ne dichiara uno rotto e lo rimanda altrove.

**B-A-25 · Il formato e il runner dei test.** `01:473`: «ogni gate ha un caso che FALLISCE». È l'unica riga di ingegneria del software in tre dossier, e non ha formato, né runner, né una regola che imponga il test **prima** dell'attivazione del gate.

**B-A-26 · Il ripristino dello stato.** GP-6 ricalcola dai file invece che dai JSON dichiarati (`03:178`) — l'idea migliore del piano — e non viene estesa al file di stato del lancio, dove servirebbe di più. Se `stato.json` diverge dal disco, non c'è procedura.

**B-A-27 · Cosa rende valida una conferma MVP.** `03:134`: «≥5 conferme MVP **nominali** (non "5 persone": 5 identificativi)». Non è detto cosa sia un identificativo valido, né come si verifica che quella persona esista e abbia detto quella frase. È l'unico criterio del piano che riguarda persone reali, e ha zero verifiche — mentre una URL ne ha tre (`03:174`).

**B-A-28 · La ritenzione dei dati dei beta tester.** `03:139` raccoglie nomi e feedback di persone reali. Dove vivono, per quanto, e se finiscono in `memoria/prodotto/` che ha ritenzione «permanente» (`01:187`). Non una riga.

**B-A-29 · Lo stato di un artefatto rifiutato.** `02:272-285` descrive bene la procedura di rifiuto ma non dice se l'artefatto rifiutato resta al suo posto sul disco. Se resta, un terzo reparto lo legge comunque, perché niente lo marca come non accettato.

**B-A-30 · Il collegamento fra la sospensione e chi la deve vedere.** `01:87`: «il file esiste, quindi la Direzione lo vede. Niente notifiche da costruire». Vedere un file richiede che qualcuno apra la cartella. Non è dichiarato nessun cruscotto, nessuna riga di apertura sessione, nessun comando `lancio.py stato` — cioè il modo in cui una persona scopre che c'è qualcosa da guardare.

## 3. AMBIGUITA' E CONTRADDIZIONI INTERNE

**C-A-01 · Chi esegue un gate: tre risposte incompatibili.** Dentro `avanza`, cioè codice (`01:33-35`). L'agente `lan-qlt-gate`, «il motore che fa funzionare tutti i gate» (`01:407`). Gli agenti di reparto, nominativamente (`03:172-178`). Le tre implicano tre architetture diverse, e la scelta cambia tutto il resto.

**C-A-02 · «L5 non risponde a L3» contro i gate eseguiti dagli agenti L4 del reparto controllato.** `01:30` contro `03:172-178`. La prima delle «due regole che rendono la gerarchia vera» è violata dall'unico workflow scritto per intero.

**C-A-03 · «Chi produce non approva» contro cinque autoapprovazioni su sette.** `01:98-114` e `03:166` contro `03:134/173`, `135/174`, `138/176`, `141/178`. La regola e la sua violazione distano dieci righe.

**C-A-04 · Ritenzione dell'intelligence: due valori.** `01:186` «12 mesi, poi riverifica» contro `02:63` «3-12 mesi per tipo». Stessa tabella, due dossier, e i «tipi» non sono enumerati da nessuna parte.

**C-A-05 · Le URL: tre soglie.** `03:20` (≥90%) contro `03:135` e `03:174` (100%, e solo 200/301) contro `02:245` (nessun controllo di raggiungibilità). Il dossier dichiara in testa di aver risolto proprio questo conflitto.

**C-A-06 · La numerazione dei gate.** `01:493` rivendica «una sola numerazione dei gate, col reparto nel nome» come correzione ottenuta; `03:170-178` e `03:195-202` usano `GP-*` ovunque, comprese le chiavi del JSON di output.

**C-A-07 · Le durate del percorso E: quattro numeri.** `03:18` (20-30 ore) · `03:57` (3-5 giorni) · `03:308` (≤5 giorni) · la somma delle fasi `03:152-157` (≥7 giorni col beta, che per il pilota è obbligatorio per `03:156`).

**C-A-08 · Le sigle di reparto.** I dodici di `01:120-133` contro `LAN-PRODOTTO`/`LAN-STRATEGIA`/`LAN-PRICING`/`LAN-COPY`/`LAN-SITI`/`LAN-ESECUZIONE` del dossier 03.

**C-A-09 · Il nome di un agente, e la sua funzione.** `lan-prd-collaudatore` (`01:400`) contro `lan-prod-collaudatore` (`03:138`): due file diversi in `.claude/agents/`. E la giustificazione di `01:400` («senza, `certificato-prodotto.json` non esiste») è smentita da `03:141`: il certificato lo emette il certificatore.

**C-A-10 · `ARCHIVIATO` è terminale e non terminale.** `01:374-380` lo elenca fra «gli stati terminali»; `01:294` gli dà la transizione di ritorno `ARCHIVIATO → IDEA`.

**C-A-11 · Il pilota: attestare o certificare.** `01:416-436` ammette l'attestazione con la frase «I sei controlli non sono stati eseguiti»; `03:145` e `03:155` fanno del collaudo integrale la ragione stessa di esistere del percorso E. Stesso prodotto, stesso lancio, due regole opposte.

**C-A-12 · Il denaro sale e non scende, ma se divergono ha ragione chi sta sopra.** `01:143`: «ogni euro nasce nel lancio e **sale** in Tesoreria; non scende mai» e insieme «se un euro compare in tutti e due i posti con valori diversi, **ha ragione la Tesoreria**». Se il flusso è unidirezionale la divergenza è impossibile per costruzione; se è possibile, esiste una seconda fonte (l'estratto conto) che il piano non dichiara mai. Il confine è scritto bene e non regge alla prima lettura.

**C-A-13 · «Si ferma con tutto pronto» oppure «va in SOSPESO».** `01:75-76` («il sistema le prepara fino all'ultimo centimetro e si ferma con tutto pronto e una riga che dice cosa manca») contro `01:92-94` (la regola del silenzio: «la fase non parte e il lancio va in SOSPESO»). Fermarsi pronti e sospendere un lancio non sono la stessa cosa, e la seconda costa dieci volte di più. Quando manca la firma del prezzo si applica quale delle due?

**C-A-14 · Il «no» non viaggia.** `02:245` fissa il criterio di accettazione di `decisione.json` a «verdetto positivo»; `01:293` prevede la transizione `VALUTATO → ARCHIVIATO` con verdetto negativo. Un `decisione.json` negativo è un artefatto legittimo che nessun handoff può trasportare: la matrice non prevede il rifiuto come contenuto, solo come esito.

**C-A-15 · I conti degli agenti non tornano.** `01:25` dichiara L4 = 30 agenti operativi; la somma della colonna «Agenti» di `01:122-133` fa 45. Anche togliendo gli 11 capi reparto restano 34. E i capi sono 11 per 12 reparti, giustificato solo per LAN-MEM (`01:158`).

**C-A-16 · Diciassette script, undici nomi.** `01:469` contro l'elenco ricavabile dai tre dossier.

**C-A-17 · Carta di progetto o installazione.** `03:42` («nessuna cartella viene creata da questo documento: è carta di progetto») contro `03:246`, che dà il percorso Windows assoluto della cartella `scripts/`. Il dossier oscilla fra specifica e installazione senza dichiarare quale sta facendo.

**C-A-18 · Un riferimento dichiarato rotto e rimandato a una sezione che non esiste.** `03:36-38` segnala che `26-ECOSISTEMA-LANCI.md` scrive «14-LANCI» invece di 15 e rimanda «→ SEGNALAZIONI». Nel dossier non c'è nessuna sezione SEGNALAZIONI.

**C-A-19 · Tre decisioni portanti sono cambiali su dossier non forniti.** `03:12-13` (la griglia di punteggio del copy → dossier 05), `03:17` (la numerazione unica dei gate → dossier 00 §5.2), `03:20` (la soglia delle fonti → dossier 07 §B.3); e `01:80` (il reparto Offerta che istruisce → dossier 05). Il dossier 03 si presenta come completo e non è costruibile da solo.

**C-A-20 · Una terzietà spostata di soggetto.** `03:173` giustifica GP-1 così: «il brief l'ha prodotto Strategia/Prodotto a monte, quindi qui è terza parte». Ma la fase N1 che valuta il brief è eseguita dallo stesso `lan-prod-intake` che esegue GP-1 (`03:134`). La terzietà riguarda il brief, non il controllo: la frase legittima un'autoapprovazione spostando l'attenzione sull'oggetto sbagliato.

**C-A-21 · I verdetti «si subiscono», ma si possono bocciare tre volte.** `02:254` («i verdetti non si accettano: si subiscono», criterio «—») contro `03:175` («max 2 giri, poi escalation a Max») e `03:241` («stesso gate bocciato 2 volte → al terzo il workflow si ferma e segnala **un problema di monte, non di valle**»). La seconda ammette che il gate possa avere torto; la prima esclude che si possa dirlo. Nessun raccordo.

**C-A-22 · Due formati per la stessa cosa.** `01:75-76` vuole «una riga che dice cosa manca»; `01:326` e `01:334` vogliono «un comando eseguibile, non una descrizione». Il secondo è giusto: il primo va allineato, non lasciato lì a fare da scusa.

**C-A-23 · La memoria come condizione, ma dopo o prima del gate?** `01:167-169` e `02:32-34` dicono che il gate della fase verifica il record; `02:53` dice che «il gate della fase **successiva**» lo verifica. Sono due momenti diversi con due conseguenze diverse: nel primo caso la fase non chiude, nel secondo chiude e la successiva non apre — e la differenza determina in quale stato si ferma il lancio.

**C-A-24 · Chi possiede il criterio.** `01:144` («la Qualità possiede i criteri, non l'esecuzione») contro `03:170-178`, dove i criteri di sette gate sono definiti dentro il dossier di un altro reparto, e contro `02:198-203`, dove il criterio di accettazione è scritto dentro l'handoff dal **mittente** (`emesso_da`, `02:208`). Tre proprietari per lo stesso oggetto.

## 4. DOVE IL PIANO E' PROSA INVECE CHE ARCHITETTURA

Criterio applicato: se non c'è uno schema dati, una firma di funzione o un numero verificabile, non è una decisione presa — è una decisione descritta.

**P-A-01 · «Produce `decisione.json`», ripetuto in tre dossier, zero campi.** `01:103`, `01:122`, `02:245`, `03:69`, `03:121`. È l'artefatto che apre la macchina a stati e il piano non ne nomina un solo campo, nemmeno `verdetto` — che compare solo dentro un'espressione di confronto (`03:121`).

**P-A-02 · `GATE-OFF-1`: «prezzo e data presenti e non evasivi».** `01:296`, `02:247`. «Non evasivo» non è un predicato. È il gate per cui, testualmente, «l'ecosistema esiste» (`01:433`), ed è il meno specificato del piano. *Predicato minimo:* `prezzo_centesimi` intero > 0, `valuta` dichiarata, `data_apertura` ISO futura di almeno N giorni, entrambi con un record di memoria di tipo `decisione` in `memoria/offerta/` che ne contenga la ragione, più la firma. Con questo, `"97-197 da decidere"` fallisce; con la formulazione attuale passa.

**P-A-03 · `GATE-REG-1`: «le dieci voci vere insieme».** `01:299`. Dieci voci non elencate, con «una sola voce falsa» come condizione di blocco.

**P-A-04 · `GATE-STR-1`: «le cinque domande hanno risposta scritta».** `01:292`. E «risposta scritta» è verificabile solo come non-vuoto: cinque campi con «sì» passano.

**P-A-05 · `GATE-EDT-1`: «nessuna riga incompleta».** `02:250`. Quali righe, quali campi, completo rispetto a cosa.

**P-A-06 · `GATE-TSR-1`: «pareggio calcolato».** `02:251`. Nessuna formula, nessuna assunzione di conversione dichiarata, nessun proprietario di quelle assunzioni. Un pareggio calcolato con un tasso di conversione inventato passa esattamente come uno calcolato bene, e il piano non ha modo di distinguerli — mentre `03:203` inventa il campo giusto (`non_misurato`) e non lo usa qui.

**P-A-07 · `GATE-TSR-2`: «il budget è saltato».** `01:298`. Nessuna soglia — mentre il veto di L1 finanza sullo stesso evento ne ha una precisa (`01:50`, «spesa oltre il tetto +10%»). Due meccanismi sullo stesso fatto, uno con numero e uno senza, e nessuna relazione dichiarata fra i due.

**P-A-08 · `GATE-CPY-1`: «ogni pezzo ha superato il gate della sua classe».** `02:248`. Le classi non sono enumerate e la griglia è rimandata al dossier 05 (`03:12-13`). Sei agenti di copy (`01:126`) lavorano contro un criterio che non esiste in nessuno dei tre documenti.

**P-A-09 · `GATE-MEM-1`: «debrief con ≥3 schemi e cause scritte».** `01:303`, e lo stesso criterio come handoff a `02:253`. Tre pattern di forza `osservazione` si scrivono in dieci minuti, e il gate conta la quantità di un output prodotto da chi il gate controlla (`LAN-MEM`). L'unico gate dello stato finale è un contatore autoalimentato.

**P-A-10 · `criterio_accettazione` come lista di frasi, con una funzione che promette di verificarle.** `02:198-203` più `02:315`. È l'esempio più puro della sezione: c'è la firma, c'è il tipo di ritorno, e il contenuto su cui opera è italiano.

**P-A-11 · «Il reparto Offerta istruisce la decisione fino a renderla una conferma».** `01:79-80`, `01:125`, `01:494`. È la correzione che il dossier 01 presenta come principale, ripetuta tre volte, e non ha: un artefatto del dossier di istruzione, una struttura, o un criterio che dica quando una decisione **è** istruita. Resta una frase, e le sei decisioni su Max restano dove erano.

**P-A-12 · «I reparti si abilitano a condizione tecnica».** `01:491`. Riga di changelog senza corpo: la condizione tecnica non è scritta da nessuna parte del dossier.

**P-A-13 · Dodici spazi di memoria e un solo schema di record generico.** `01:183-196`, `02:60-73`, `02:77-95`. La colonna «Contiene» è descritta a parole («costo per canale, creatività»; «strutture, numeri per pagina») e non esiste tipizzazione per spazio. Cosa distingue un record di `memoria/traffico/` da uno di `memoria/copy/` oltre alla cartella in cui sta? Niente — quindi la memoria è dodici cartelle con lo stesso oggetto dentro, e la ricerca per contesto (`02:148`) non ha niente su cui filtrare oltre al testo libero di `titolo` e `corpo`.

**P-A-14 · RF3, RF4, RF6: opinioni registrate come misure.** `03:176` («semi-automatici con giudizio registrato per item») e `03:280` (`registra_giudizio(red_flag, item, esito: bool, nota) -> None`). Nessuna rubrica, nessun campione minimo dichiarato, nessun secondo giudice, nessun criterio di disaccordo. RF4 in particolare — «si capisce senza riavvolgere?» — è un giudizio soggettivo che entra nel certificato come un booleano accanto a RF5, che è una misura vera. Il certificato (`03:199`) li presenta come un vettore omogeneo `[0,0,0,0,0,0]`: tre misure e tre opinioni indistinguibili.

**P-A-15 · La copertura E2 ≥80%.** `03:154`. «Capitoli mappati a una trasformazione» — mappati da chi (l'architetto, cioè chi ha interesse a passare), con quale prova, e la soglia è dichiarata «proposta nuova» senza base. `copertura_capitoli(...) -> float` (`03:271`) calcola una frazione su un giudizio.

**P-A-16 · Le metriche del §12.** `03:307-315`. «≥70% passa GP-4 al primo collaudo» e «≤5 giorni» sono target su una popolazione di **un** prodotto: non misurabili per anni. Refund, completion e testimonial sono attribuiti a WF-PRD (`03:317-319`) mentre nulla nel workflow li raccoglie, e il reparto incaricato di raccoglierli — `LAN-ESECUZIONE` — non esiste fra i dodici.

**P-A-17 · «Sopra il 40% la sentinella lo segnala».** `01:247`, `02:178`. Segnala a chi, con che mezzo, e con quale conseguenza. Una soglia senza effetto è una frase con un numero dentro.

**P-A-18 · La firma umana come stringa in un JSON.** `03:201` (`"firma_umana": "Max | Gael | null"`), `01:422` (`"attestato_da": "Max"`), `01:106` e `01:110` («+ firma umana»). Le nove decisioni che il piano dichiara non delegabili (`01:63-73`) sono, tecnicamente, la cosa più facile da falsificare di tutto il sistema: un agente che scrive `"Max"` in un campo.

**P-A-19 · `03-architettura.json` è l'artefatto più riusato del piano e non ha schema.** Citato a `03:136`, `154`, `225`, `226`, `270`, `286`. Alimenta i bullet della sales page, il pricing, due gate e il ricalcolo del certificato. `valida_moduli(architettura: dict)` (`03:270`) opera su un `dict` di forma ignota.

**P-A-20 · L'escalation ha tempi e nessun meccanismo.** `01:85-96` fissa T+0, T+2h, T+1g, T+2g, e a `01:87` dichiara: «il file esiste, quindi la Direzione lo vede. **Niente notifiche da costruire**». Il piano scambia la persistenza per la consegna. Un file in una cartella non è un messaggio ricevuto, e la scala dei tempi — che è la parte buona — non ha niente che la faccia scattare.

**P-A-21 · «Il criterio si allinea», «il gate si rilegge», «il beta decade».** `03:20`, `03:156`. Tre verbi riflessivi al posto di tre meccanismi: chi riallinea, cosa rilegge il gate e quando, quale processo fa decadere il beta e come lo registra.

**P-A-22 · La potatura archivia «i record scaduti **e** mai letti».** `01:244`, `02:175`. Con `scaduto_il: null` di default (`02:93`) e `letto_volte` incrementato da qualunque lettura (`02:296`), la congiunzione è quasi sempre falsa. La firma esiste (`potatura(alla_data: str) -> list[str]`, `02:298`) e la politica che dovrebbe eseguire no.

## 5. CIO' CHE INVECE E' SOLIDO — non toccarlo

**S-A-01 · Il ricalcolo dai file, mai dai JSON di stato.** `03:178` (GP-6), `03:235`, `03:286-287` (`ricalcola_gate`, `confronta_stati`). È l'idea migliore dei tre dossier: nasce da un guasto reale e documentato (l'agente che stampa «successo (SIMULATA)» ed esce 0), è implementabile così com'è, e ogni divergenza ha già la sua destinazione (`REGISTRO-ERRORI`). Non toccare, ed **estendere** al file di stato del lancio, che oggi non ha nessuna ricostruzione indipendente.

**S-A-02 · `SOSPESO` che porta con sé il proprio antidoto.** `01:319-334`: `stato_di_partenza`, `revisione_il` mai vuoto, e `come_si_esce` come **comando eseguibile**. L'idea che uno stato di attesa debba contenere l'istruzione per uscirne è rara e giusta. Va completata (congelare gli orologi degli handoff, D-A-09) e replicata su ogni altro blocco del sistema — a partire da `bloccato_da`, che oggi non ce l'ha.

**S-A-03 · L'escalation che muore contro un gate.** `01:88-89`: «se una delle due posizioni viola un gate esistente, non è un conflitto: vince il gate». Uccide metà dei conflitti senza riunioni e senza gerarchia. Tenere parola per parola.

**S-A-04 · Il declassamento dei pattern e `si_applica_quando`.** `01:238`, `02:136`, `02:139-141`. Una memoria che può solo salire è una superstizione con la data — la frase è giusta e il meccanismo di discesa (smentito due volte, scende di grado) è concreto e implementabile. E `si_applica_quando` è il campo che impedisce a una regola di essere applicata dove non vale.

**S-A-05 · `non_misurato` nel certificato.** `03:203`: «ogni dato assente dichiarato, mai stimato». Va copiato in **tutti** gli altri artefatti — a cominciare da `budget.json`, dove il pareggio calcolato su assunzioni inventate è il rischio principale (P-A-06).

**S-A-06 · La convenzione degli exit code.** `03:247-249` (0 PASS · 1 BLOCK con verbale · 2 input non valido con **zero file scritti** · 3 ambiente) e `03:240`. È corretta, discrimina i casi giusti, e va estesa a `lancio.py` (D-A-04) e al codice della memoria.

**S-A-07 · RF1, RF2, RF5 e le loro firme.** `03:176` e `03:277-279`: file di output pratico esistente e >0 byte, gemello `-ESEMPIO` per ogni template, ogni link testato in incognito con esito registrato per link. Sono tre test veri, con tre funzioni implementabili senza inventare nulla. Sono anche la prova che il piano **sa** scrivere un criterio quando vuole — il che rende la prosa del resto una scelta, non un limite.

**S-A-08 · Il percorso E e la distinzione «pronto dichiarato» / «pronto certificato».** `03:143-148`. È la frase più utile dei tre dossier, e il principio «salta la produzione, non salta MAI la certificazione» è la regola giusta per un'azienda che ha 25 pezzi finiti e mai usciti. Difendere questa contro l'attestazione del pilota (D-A-12), non il contrario.

**S-A-09 · La Regia produce, la Memoria giudica, e nessuno dei due scrive da solo la storia.** `01:111-114` e `01:146-156`. È l'applicazione più pulita della regola «chi produce non approva» in tutto il piano — ironicamente l'unico punto in cui viene davvero rispettata — ed è motivata bene: il debrief orienta tutti i lanci successivi, quindi è il punto in cui l'autoassoluzione fa più danno.

**S-A-10 · Il formato della tabella §1.6.** `01:100-111`: output · chi lo produce · chi lo valida · da chi dipende. È la forma giusta e va usata come **indice generale** del sistema: se un artefatto non ha una riga lì, non esiste. Va solo completata (mancano `LAN-TRF` e `LAN-QLT`, D-A-19) e resa eseguibile da `registro.py`.

**S-A-11 · `accettato: null` come stato iniziale, e la scadenza come campo.** `02:220`, `02:222`, `02:236`. «Il silenzio non vale come accettazione» è corretto e il difetto non è il principio ma la sua meccanica (D-A-08, D-A-10).

**S-A-12 · Le nove decisioni non delegabili, con la motivazione per ciascuna.** `01:63-73`. È una buona carta costituzionale e la colonna «perché non è delegabile» rende ogni voce difendibile. Il problema è l'attuazione (P-A-18), non l'elenco: non ridiscuterlo, proteggerlo tecnicamente.

**S-A-13 · «Un agente scritto solo in `Reparti/*/agenti/` è una specifica, non un agente».** `01:476-482`, ripetuto a `03:61` («10 schede, 2.703 righe, zero agenti invocabili»). Diagnosi esatta di un guasto reale e verificato. La coppia obbligatoria è la risposta giusta; va solo resa sostanziale (D-A-22).

**S-A-14 · L'input tipizzato di WF-PRD.** `03:100-113`: colonna «Obbligatorio», colonna «Se manca», distinzione fra `STOP exit 2` (non parte niente) e `BLOCK exit 1` (parte e si ferma al gate), e la regola del caso peggiore quando `offerta_path` è null (`03:112`, «Mai il contrario»). È l'unico blocco dei tre dossier che un costruttore può implementare senza inventare una riga. È il modello a cui riportare tutti gli altri artefatti.

**S-A-15 · Il formato «cosa è cambiato / contro quale obiezione».** `01:486-503`, `02:321-331`. Tenere il formato: obbliga a dichiarare il motivo di ogni scelta e rende il documento verificabile. Ma va aggiunta la regola che manca: **una riga di changelog vale solo se la correzione è nel corpo** — oggi almeno due non lo sono (C-A-05, C-A-06), e un changelog che asserisce il falso disarma il revisore successivo.

**S-A-16 · Il rifiuto di handoff con criterio citato obbligatorio.** `02:272-285`: un rifiuto senza criterio citato è nullo; l'artefatto torna al mittente e il destinatario **non** lo aggiusta; al secondo rifiuto sale, al terzo diventa conflitto; tre rifiuti della stessa specie obbligano a rivedere il criterio, non chi lo esegue. È la procedura meglio scritta dei tre dossier — le manca solo il criterio eseguibile su cui operare (D-A-18).

## 6. LE 5 COSE PIU' IMPORTANTI DA CAMBIARE

1. **Togliere l'esecuzione dei gate a chi produce l'artefatto**: in WF-PRD cinque gate su sette sono eseguiti dallo stesso agente che ha prodotto ciò che giudicano (`03:134/173`, `135/174`, `138/176`, `141/178`), violando la regola scritta dieci righe sopra (`03:166`) e la prima legge della gerarchia (`01:30`).
2. **Scrivere `lancio.py avanza`** — firma, exit code, lock, idempotenza, chi lo invoca e quando: è la spina dove «vivono i gate» (`01:33-35`) ed è l'unico script del piano senza una riga di specifica, mentre tre script minori ce l'hanno completa.
3. **Unificare nomenclatura e mappa dei gate fra i tre dossier** (`LAN-PRICING`/`LAN-SITI`/`LAN-ESECUZIONE` contro i dodici reparti di `01:120-133`; `GP-0…GP-6` contro `GATE-PRD-1/2/3`; `lan-prd-` contro `lan-prod-`): oggi il dossier 03 non è installabile sopra il dossier 01.
4. **Sostituire i criteri di prosa con predicati eseguibili e consegnare i nove schemi JSON mancanti**, a partire da `decisione.json` e `offerta.json`: oggi le cinque domande, le dieci voci, «prezzo non evasivo» e `criterio_accettazione` come lista di frasi che `accetta()` dichiara di verificare (`02:198-203`, `02:315`) rendono la maggioranza dei gate non implementabile o non fallibile.
5. **Derivare lo scaglione minimo dai workflow invece di elencarlo a mano**: gli undici (`01:396-407`) non hanno gli agenti di N0/N2/N8/E1 e lasciano cinque reparti senza conductor, cioè senza chi scrive il record che la memoria pretende per chiudere una fase (`02:47` + `02:32`) — il primo lancio si blocca alla prima fase, per una regola introdotta come la correzione principale del piano.
