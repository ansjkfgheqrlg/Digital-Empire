# CRITICA-B — dossier 04, 05, 06

Revisione ostile. Riferimenti: `04` = 04-WF-OFFERTA.md · `05` = 05-WF-COPY.md ·
`06` = 06-WF-FUNNEL-E-EDITORIALE.md · `02` = 02-MEMORIA-E-HANDOFF.md (letto come contesto).
Ogni rilievo cita riga esatta.

---

## 1. IL CUORE REGGE? — verdetto sul flusso Offerta

**Verdetto: no. Come è scritto, il flusso produce un prezzo e una data solo nei casi in cui
l'azienda non era bloccata. Nel caso che lo motiva, si ferma un passo prima del gate — e si ferma
in un punto che non ha né scadenza, né promemoria, né sospensione, né metrica che lo registri.**

Il dossier apre dichiarando di aver capito la malattia (`04:16-19`): *«un gate che blocca su una
decisione mancante non produce la decisione: produce un blocco documentato»*. Poi, novanta righe
più in basso, costruisce esattamente quello.

### La simulazione — un umano che segue le fasi alla lettera

**Giorno 0.** Max esegue `/lancio-offerta 2026-10-manuale-claude-code`.
Primo campo dell'input: `certificato_path`. Regola: *«esce 2: non si prezza un prodotto non
certificato»* (`04:85`), ribadita a `04:312`. Il Manuale Claude Code è **finito da marzo** e non è
mai passato dal flusso Prodotto: non ha un certificato. **Il flusso motivante non supera il proprio
gate d'ingresso.** Il reparto costruito per sbloccare il Manuale è, il giorno 1, inaccessibile al
Manuale. Nessuna riga del dossier prevede un percorso per un prodotto già finito (vedi D-B-05).

**Giorno 0-bis, ipotizzando che il certificato esista.** O0 legge la memoria, tutto bene.
Arriva O1 (`04:97`): `ruolo_prodotto` è `non-deciso` — che non è un'ipotesi, è **il caso descritto
dal dossier stesso** in §5 (`04:112-137`) e nell'input a `04:88` (*«è il campo che blocca tutto»*).
Il workflow produce il confronto delle due strade e **si ferma**: `04:117` (*«produce questo, e poi
si ferma»*) e `04:315` (*«è l'unico caso in cui questo workflow si ferma prima ancora di proporre un
numero»*).

**Giorno 3.** Niente. La tabella dell'inerzia (`04:236-241`) conta *«giorni senza firma»*, e la
funzione che la alimenta è `giorni_di_inerzia(lancio_id, oggi) -> int`, documentata come *«da quanto
**la proposta** aspetta»* (`04:296`). La proposta non è mai stata emessa. **L'orologio non parte.**

**Giorno 7.** Nessuna voce `bloccato_da`. **Giorno 14.** Nessuna sospensione. **Giorno 180.**
Il lancio è fermo esattamente come oggi, con in più un file `offerta/01-ruolo.md`.

**E il fallimento è invisibile alla sua stessa misura.** La metrica regina è *«giorni fra
`ISTRUITO` e la firma ≤3, oggi 180»* (`04:323`). Se la firma non arriva mai, la metrica non produce
un numero alto: **non produce nessun numero.** Il modo in cui questo reparto fallisce è
precisamente il modo che il suo cruscotto non sa vedere.

### Perché è un difetto di architettura e non una svista

Il dossier ha già scritto, in due punti diversi, tutto ciò che serve a ripararlo:

- `04:128` — la tabella dichiara che **la strada A è reversibile e la B no**. È un criterio di
  default, non un commento.
- `05:296-297` — *«dove esiste un default ragionevole, si procede e lo si dichiara […] un'attesa
  senza scadenza non è un punto di controllo: è un punto di morte»*.

Il piano possiede la regola e non la applica al proprio punto più fragile. La tabella dei punti
umani con scadenza (`05:286-294`) elenca **sei** decisioni di Max e **non contiene O1**: la scelta
del ruolo del prodotto, cioè il blocco reale, è l'unico punto umano del piano rimasto senza
scadenza e senza comportamento allo scadere.

### Cosa regge davvero

Il tratto **O4 → O5 → O6** (proposta istruita → domanda binaria → data) è progettato bene ed è la
parte migliore dei tre documenti. Il problema è che quel tratto è a valle di un blocco più duro, e
a monte di un gate che non prova ciò che dichiara di provare (D-B-04).

**Riparazione minima che cambia il verdetto:** O1 entra nella tabella dei punti umani con
scadenza **7 giorni** e default **`vendita`**, marcato `scelto_per_silenzio: true` +
`revisione_il`, giustificato dalla reversibilità già dichiarata a `04:128`; `giorni_di_inerzia`
smette di contare dalla proposta e conta **dal primo punto umano aperto del lancio**, qualunque
esso sia.

---

## 2. DIFETTI STRUTTURALI GRAVI

### D-B-01 · Il blocco vero (O1) non ha né scadenza né default
**Dove:** `04:97`, `04:117`, `04:315`, `04:296`; contro `05:286-297`.
**Perché si rompe:** la macchina dell'inerzia (`04:236-241`) è agganciata alla *proposta*, che nel
caso `non-deciso` non nasce. Il ramo più probabile del flusso è l'unico privo di timer.
**Caso concreto:** Manuale Claude Code, `ruolo_prodotto: non-deciso` — descritto dal dossier come
il caso reale. Sei mesi diventano sei mesi con un file in più.
**Riparazione:** O1 diventa punto umano con scadenza 7 gg e default `vendita` (reversibile per
`04:128`), con `ruolo_scelto_per_silenzio` e `revisione_il` nell'output; il gate a `04:226` accetta
il default purché il campo `scelto_per_silenzio` sia presente e datato.

### D-B-02 · Il gate del prezzo prova una stringa, non una firma
**Dove:** `04:228` (*«`firmato_da` contiene un nome di persona»*), `04:230-232`, `04:295`.
**Perché si rompe:** *«nessuna macchina può riempire `firmato_da`»* è un'affermazione morale, non
un controllo. Qualunque agente con accesso in scrittura al file scrive `"Max"` e il gate passa. Non
esiste `canale_firma`, non esiste provenienza, non esiste proprietario di scrittura per campo (il
`02:57` dà un proprietario per *spazio*, non per *campo*).
**Caso concreto:** un conductor in loop di auto-riparazione, incalzato da un gate che blocca,
scrive `firmato_da: "Max"` per sbloccarsi. Il gate certifica una decisione umana mai presa — e il
lancio parte a un prezzo che nessuno ha approvato. È il fallimento peggiore possibile per questo
reparto, peggiore del blocco.
**Riparazione:** `offerta.json` porta `firma: {chi, canale, riferimento, proposta_hash, il}` con
`canale` in una lista chiusa (`comando-utente`, `chat-firmata`, `file-fuori-agenti`);
`gate_offerta.verifica` rifiuta se `canale` non è nella lista o se `proposta_hash` non corrisponde
allo `04-proposta.md` corrente. Gli agenti non hanno permesso su quel sotto-oggetto.

### D-B-03 · La firma non è legata al contenuto firmato
**Dove:** `04:295` — `firma(lancio_id, chi, valore) -> dict`; output a `04:251-276` senza alcun
riferimento alla proposta.
**Perché si rompe:** la firma è un valore scalare sospeso nel vuoto. Se la proposta viene
rigenerata (perché il gate fallisce su struttura, o perché la ricerca arriva dopo), la firma
precedente resta formalmente valida su un contenuto che non esiste più.
**Caso concreto:** Max firma 47 € su una proposta che diceva «alternativa alta 97 € → scatta il
beta test»; poi O7 costruisce una struttura con bonus che alza il valore, il gate fallisce, si
rifà la proposta con motivazioni diverse — e `firmato_da: "Max", firmato_il: ...` è ancora lì.
**Riparazione:** `firma(lancio_id, chi, valore, proposta_hash)`; `offerta.json` porta
`proposta_hash` + `proposta_path`; ogni rigenerazione della proposta invalida la firma e riapre O5.

### D-B-04 · GATE-OFF-1 è auto-soddisfacibile: la macchina sceglie il numero su cui viene giudicata
**Dove:** `04:104` e `04:227` (valore ≥3× prezzo), prodotto da O7 `lan-off-struttura` (`04:103`),
schema a `04:262-263` (`valore_dichiarato`, `rapporto_valore_prezzo`).
**Perché si rompe:** `valore_dichiarato` non ha nessuna regola di derivazione. L'agente che
costruisce il pacchetto è lo stesso che decide quanto vale, ed è misurato su un rapporto che può
raggiungere aggiungendo un bonus con un prezzo inventato. Il vincolo non seleziona: istruisce a
gonfiare.
**Caso concreto:** prezzo 47 €, servono 141 € di valore: si aggiunge «Bonus: checklist — valore
99 €». Rapporto 4,0. Gate verde. Il numero non significa niente e finirà anche sulla pagina di
vendita, dove la griglia A6 (`05:133`) lo riprende come dato.
**Riparazione:** ogni bonus porta `fonte_valore` in una lista chiusa (`prezzo-listino-proprio`,
`prezzo-mercato-con-url`, `costo-produzione`); un bonus senza fonte vale **0** nel calcolo; il gate
somma solo i valori con fonte. E il rapporto ≥3 (già dichiarato arbitrario a `04:349-351`) diventa
un parametro del listino, non una costante sparsa in due dossier.

### D-B-05 · Il prodotto già finito non ha un percorso
**Dove:** `04:85`, `04:312`, `04:54`.
**Perché si rompe:** il flusso ammette solo prodotti che escono dal flusso Prodotto. Un manuale
pronto da marzo, una landing già online (`06:212`), 25 contenuti già prodotti (`06:248-249`): tutto
l'inventario reale dell'azienda entra dalla porta sbagliata o non entra.
**Caso concreto:** per prezzare il Manuale bisogna prima farlo certificare come se fosse nuovo;
il costo di quel giro non è stimato in nessuno dei tre dossier e sta sul percorso critico del
lancio che il piano esiste per sbloccare.
**Riparazione:** un `certificato_path` può essere emesso in **modalità retroattiva** (checklist
ridotta: bandiere rosse + estrazione degli `output_pratici[]` dall'artefatto finito), con
`modalita: "retroattiva"` scritto nel certificato; il 04 accetta anche solo `architettura_path`
marcando l'offerta `senza-certificato`, com'è già previsto per la ricerca (`04:86`).

### D-B-06 · Le due liste su cui poggia metà dell'automatismo del copy non esistono in forma leggibile
**Dove:** `05:200-209` (definizione della voce eliminatoria D3, dichiarata **auto** a `05:156`),
che poggia su (a) *«output pratici verificabili nell'architettura del prodotto»* e (b) *«prove di
categoria dimostrazione o testimonianza già presenti nelle fondamenta»*.
**Perché si rompe:** l'architettura è un `architettura_path` senza schema (`04:67`); le fondamenta
sono `copy/01-fondamenta.md` (`05:72`) — **markdown**. Da un markdown non si estrae una lista
tipizzata di prove. La correzione di cui il dossier va più fiero è appesa a due strutture dati che
il piano non definisce. Lo stesso vale per A4 (`05:131`), A5 (`05:132`), C1 (`05:147`), E1
(`05:224`), B1/B3 (`05:139`, `05:141`).
**Caso concreto:** chi implementa `lan-cpy-giudice` apre `01-fondamenta.md`, non trova campi, e
chiede al modello di «dedurre le prove». La voce eliminatoria torna a essere un'opinione — cioè
esattamente la cosa che §5.6 dichiara di aver eliminato.
**Riparazione:** `copy/01-prove.json` (`{id, categoria ∈ {dimostrazione, testimonianza, dato,
autorita}, testo, fonte_url, verificabile: bool}`) e `prodotto/architettura.json` con
`output_pratici[] {id, descrizione, verificabile_come}`. Il markdown resta per gli umani; il JSON è
la fonte per il gate.

### D-B-07 · Il giudice del copy può auto-promuoversi: nessuna ancora, nessuna cecità, nessun controllo di concordanza
**Dove:** `05:173-174` (*«la parte giudicata ha ancore di punteggio»* — **nessuna ancora è scritta
nel documento**), `05:251-252` (chi esegue / chi ha il veto).
**Perché si rompe:** 58 punti su 100 sono giudizio (`05:173` dichiara ~42 automatici). Il giudice è
un modello che valuta testi prodotti da modelli dello stesso conductor, conosce la soglia (≥80,
`05:115`) e non ha rubrica. `sentinel-quality` *«riceve i punteggi e ha il potere di veto»*
(`05:252`): su quale base, se non sul numero che riceve? Un veto senza criterio proprio è
ratifica.
**Caso concreto:** un pezzo mediocre esce a 81. Nessuno può dire se 81 è vero: non c'è una seconda
misura, non c'è una banda di indifferenza, non c'è un campione ri-giudicato. Al terzo lancio
tutti i pezzi escono fra 80 e 84 e nessuno sa perché.
**Riparazione:** (a) rubrica con **ancore scritte** per ogni voce giudicata — 0/3/5 con un esempio
reale ciascuna, consegnata col piano, non promessa; (b) il giudice **non riceve la soglia** e non
sa chi ha scritto il pezzo; (c) **banda di indifferenza 76-84** → secondo giudice indipendente o
occhio umano; (d) 10% dei pezzi ri-giudicato alla cieca, con la concordanza scritta in
`memoria/qualita/` come metrica del gate stesso.

### D-B-08 · Nessun gate dei tre dossier ha un ramo di fallimento
**Dove:** `04:104` (GATE-OFF-1), `05:74` (GATE-CPY-1), `06:78` (GATE-FNL-1), `06:279` (GATE-EDT-1).
**Perché si rompe:** tutti dicono *cosa* controllano, nessuno dice **cosa succede quando
falliscono**: a quale fase si torna, quante volte, chi decide che si smette. Un gate senza ramo di
fallimento non è un gate: è un'assertion che fa esplodere il processo.
**Caso concreto:** pagina di vendita a 74 punti. Si riscrive. La valutazione costa 3 ore (`05:74`)
e la scrittura 8-12 (`05:73`). Due giri fanno +25 ore invisibili su una stima di 40-55 (`05:24`) —
e la stima dichiara esplicitamente 15-20 ore di *sola valutazione*, cioè **un solo giro**.
Con oscillazione (il modello riscrive e perde punti altrove) il ciclo non termina.
**Riparazione:** ogni gate dichiara `su_fallimento: {torna_a: <fase>, max_tentativi: N,
oltre_N: <escalation umana con la voce bloccante>}`; la stima delle ore è per giro e il numero di
giri attesi è dichiarato.

### D-B-09 · La prova del tracciamento è un `bool` senza fonte di verità e con un timeout che la falsifica
**Dove:** `06:111` (controllo 4), `06:117-120`, `06:126-127`
(`prova_evento(url, evento, timeout_s=60) -> bool`).
**Perché si rompe:** *«si guarda se l'evento compare»* — **dove?** Sono tre cose diverse e
incompatibili: il datalayer nel browser prova che il sito ha sparato; la richiesta di rete prova
l'invio; l'API del provider prova la ricezione. Solo la terza è ciò che il dossier intende, ed è
quella che **non risponde entro 60 secondi** su gran parte degli strumenti reali (i report standard
di GA4 hanno latenza di ore; solo endpoint di debug/realtime dedicati sono quasi-istantanei, e
richiedono parametri specifici). Un `-> bool` non lascia traccia di cosa è stato osservato.
**Caso concreto:** il gate «che separa questo da una formalità» (`06:117`) restituisce `false` su
un tracciamento perfettamente funzionante, blocca il lancio, e viene derogato la prima volta.
Al secondo lancio nessuno lo esegue più — l'esito che `04:21-22` descrive per i gate derogati.
**Riparazione:** `prova_evento(url, evento, fonte, timeout_s) -> dict` con
`{ricevuto: bool, fonte, id_evento, payload, ricevuto_il, latenza_ms}`; `fonte` in lista chiusa per
strumento, con il suo endpoint di verifica dichiarato e il suo timeout realistico; l'esito si
persiste in `funnel.json` (che oggi porta solo `eventi_verificati: [...]`, `06:175`, cioè un
elenco di nomi senza prova).

### D-B-10 · Il consenso ai cookie è nominato come causa numero uno di fallimento e non entra nel controllo
**Dove:** `06:192` (*«consenso ai cookie che la blocca […] è il caso più frequente»*) vs `06:118`
(la visita di prova, che non dice cosa fa il tester col banner).
**Perché si rompe:** se il tester accetta e l'utente medio rifiuta, il gate è verde e i numeri non
arrivano lo stesso. Il gate valida il caso migliore e certifica il caso peggiore.
**Riparazione:** doppia visita obbligatoria — consenso accettato e consenso rifiutato — con
l'esito atteso dichiarato per ciascuna (es. `pagina_vista` deve arrivare in entrambe se è
anonimizzata; `modulo_inviato` almeno nella prima); entrambi gli esiti in `funnel.json`.

### D-B-11 · Nessun artefatto è versionato: un cambio a monte non invalida niente a valle
**Dove:** `05:40-43` (le fondamenta partono senza prezzo), `06:60-64` (precondizioni),
`06:212` (la landing esistente *«si verifica e si collega, non si rifà»*), `04:327` (metrica
«prezzi rivisti dopo l'apertura: 0»).
**Perché si rompe:** il piano gestisce l'ordine *giusto* e assume che nulla cambi. Ma il proprio
design **prevede** che le fondamenta nascano prima del prezzo: quindi il caso «il prezzo arriva
dopo, ed è 27 invece di 47» non è un'eccezione, è il flusso normale. Nessun artefatto porta la
versione dell'offerta o delle fondamenta da cui deriva; nessuna regola dice cosa si rigenera.
**Caso concreto:** Max firma «no, preferisco 27» (`04:169` prevede questa risposta). La pagina di
vendita è già scritta con l'ancoraggio su 47, la cassa è già configurata, le email di recupero
citano il prezzo. Nessun processo se ne accorge.
**Riparazione:** ogni file derivato porta `offerta_versione` e `fondamenta_versione` (hash);
un cambio di hash marca automaticamente i derivati `da_rigenerare` con `motivo`, e il gate a valle
rifiuta un artefatto con hash disallineato. È lo stesso meccanismo di `contraddice` già accettato
in `02:103`.

### D-B-12 · Idempotenza e concorrenza: assenti in tutti e tre i dossier
**Dove:** `04:309` (`/lancio-offerta`, `--firma`), `05:75-79` (cinque fasi C3a-e in parallelo che
scrivono tutte in `copy/`), `06:75` (F4 parallelo, una per pagina), `02:57` (un solo proprietario
di scrittura per spazio).
**Perché si rompe:** non è scritto cosa succede se un comando gira due volte; se `firma()` può
essere chiamata due volte con valori diversi; chi scrive `copy/manifest.json` mentre cinque agenti
producono file; cosa succede se due lanci sono aperti insieme (`proponi_data` consulta «impegni»
a `04:294`, una lista di cui nessuno dichiara l'origine).
**Caso concreto:** C3d (28 email) e C3e (annunci) finiscono a distanza di secondi; entrambi
aggiornano il manifest; l'ultimo vince e metà dei pezzi sparisce dall'handoff verso il funnel.
**Riparazione:** ogni fase scrive **solo** file con nome deterministico di sua proprietà; il
manifest è **generato** da una scansione, mai scritto in concorrenza (regola già adottata per
l'indice della memoria a `02:178`); ogni comando è idempotente per chiave `(lancio_id, fase)` e
rifiuta la riesecuzione su una fase chiusa salvo `--rifai <motivo>` che scrive un record.

### D-B-13 · `copy/manifest.json` è l'artefatto più importante del dossier 05 e non ha schema
**Dove:** `05:81` (output di C5), `06:43` (`copy_manifest: "string"` — solo un percorso),
`02:248` (criterio d'accettazione CPY→FNL: *«ogni pezzo ha superato il gate della sua classe»*).
**Perché si rompe:** il funnel deve verificare un criterio che il manifest non gli permette di
verificare. L'handoff è formalmente accettabile e sostanzialmente cieco.
**Riparazione:** schema `pezzi[] {id, tipo, classe ∈ {madre, breve, micro}, path, punteggio,
denominatore, soglia, esito, verbale_path, fondamenta_versione, offerta_versione}` + `stato`
complessivo. Senza questo, `06` non può implementare la propria precondizione a `06:60`.

### D-B-14 · La ripresa dopo una sospensione non è governata: niente scade, niente si rigenera
**Dove:** `04:241` (a 14 giorni il lancio va in `SOSPESO` *«con data di revisione»*), `04:223`
(il gate vuole una data **futura**), `02:63` (l'intelligence scade in 3-12 mesi).
**Perché si rompe:** al riavvio dopo tre mesi il gate fallisce correttamente sulla data — e poi?
Nessuna regola dice cosa resta valido: il prezzo (i concorrenti sono cambiati), la ricerca
(scaduta per `02:63`), il copy che nomina «14 ottobre» in decine di punti, il piano editoriale
che ha `data` assoluta in ogni riga (`06:300`).
**Caso concreto:** si sposta la data, si rifirma, e restano in circolazione 28 email che citano
una data morta. Nessun gate le intercetta: hanno già il loro verbale.
**Riparazione:** classi di decadenza dichiarate per artefatto (`prezzo: 90 gg`, `ricerca: 180 gg`,
`data: sempre`, `copy con blocco ::data: rigenerazione parziale`); `offerta.json` porta
`valido_fino`; la ripresa è una procedura nominata con il suo elenco di rigenerazioni obbligate.

### D-B-15 · Lo spostamento automatico della data invalida per silenzio una firma umana
**Dove:** `05:289` e `05:293` (*«si ferma e si sposta la data»* come comportamento allo scadere di
due punti umani) vs `04:102` (la data è firmata) e `04:228` (la firma è condizione di gate).
**Perché si rompe:** la data è di proprietà di `LAN-OFF` (`02:65`) e porta una firma umana.
Un timeout di un *altro* reparto la modifica senza nuova firma. Il sistema che ha eretto la firma
a principio la aggira nel documento successivo.
**Riparazione:** lo scorrimento non è automatico: riapre O6 e produce una nuova proposta di data
nella stessa forma binaria; il lancio resta in `data-da-riconfermare` finché non è firmata. E il
calendario a valle usa **offset** (`T-16`), non date assolute, così solo l'ancora si rifirma.

### D-B-16 · Il piano editoriale ha tre rappresentazioni dello stesso istante e nessuna fonte di verità
**Dove:** `06:300` — `"giorno": 12, "data": "2026-10-14", "fase": "T-16"`.
**Perché si rompe:** denormalizzazione pura. Al primo spostamento di data le tre divergono, e
nessuna riga dice quale comanda.
**Riparazione:** `fase` (offset dall'apertura) è la fonte; `giorno` e `data` sono **derivate** e
non si scrivono nel file.

### D-B-17 · L'ottimizzatore in-lancio non può decidere nulla, e il dossier lo dimostra da solo
**Dove:** `06:79` (F7 «continuo», con un agente dedicato), `06:156-160` (300 visitatori per
versione per una differenza grande), `06:162-165` (*«con il traffico di un lancio piccolo si vedono
solo le differenze grandi»*), contro un carrello di 5 giorni (`04:188`).
**Perché si rompe:** in cinque giorni su un pubblico piccolo non si raggiungono i volumi per una
sola decisione. `lan-fnl-ottimizzatore` è un agente il cui output, per costruzione, è sempre
«non si sa ancora» (`06:196` lo prescrive esplicitamente).
**Riparazione:** spezzare F7: **F7a — presidio in-lancio** (nessun test: solo allarmi su rotture
tecniche — pagina giù, evento sparito, cassa in errore) e **F7b — apprendimento fra un lancio e
l'altro**, dove il traffico si accumula e i 300 hanno senso. Le soglie verde/giallo/rosso
(`06:133-139`) sono materiale da **debrief**, non da giorno 2.

### D-B-18 · La pubblicazione irreversibile viene prima della prova che la cassa funziona
**Dove:** `06:76` (F5 pubblicazione, *«è irreversibile»*), `06:115` (controllo 8, transazione reale,
dentro GATE-FNL-1 che sta **dopo** F5-F6), e `06:62` che chiede la stessa transazione come
**precondizione d'ingresso** al flusso.
**Perché si rompe:** o è duplicata, o sono due cose diverse e non è dichiarato quali. In ogni caso
l'ordine mette una prova bloccante dopo un passo dichiarato irreversibile.
**Riparazione:** due controlli distinti — **8a** in staging, blocca F5; **8b** in produzione,
blocca l'apertura della vendita (`06:194`). E `funnel.json` (`06:178`) porta entrambe.

### D-B-19 · Le copertine sono il punto umano più frequente del piano e non compaiono in nessuna tabella dei punti umani
**Dove:** `06:339-340` (*«le copertine le fa una persona […] il piano editoriale prepara titolo e
indicazioni, apre la cartella, e si ferma»*) contro `05:286-294` (i sei punti umani con scadenza).
**Perché si rompe:** un piano editoriale reale in questa azienda arriva a decine di righe. Ogni
riga con `formato: video-*` contiene un punto umano senza scadenza, senza escalation, e sulla
**stessa persona** che deve firmare il prezzo, approvare la promessa e dare il via libera a T-1.
La capacità umana totale non è mai sommata in nessuno dei tre dossier.
**Caso concreto:** metrica «contenuti prodotti che vengono pubblicati: 100%» (`06:347`) — che il
dossier chiama la propria ragione d'esistere (`06:352`) — è irraggiungibile per un collo di
bottiglia che il dossier stesso dichiara e non governa.
**Riparazione:** la copertina è una riga della tabella dei punti umani, con scadenza 48 h e
comportamento allo scadere dichiarato (pubblicazione con copertina provvisoria + `da_rifare`,
oppure slittamento della riga con ricalcolo delle quote); e il gate editoriale (`06:324-331`)
somma le ore-persona richieste dal piano e le confronta con una capacità dichiarata.

### D-B-20 · Una regola dichiarata «cambiata» non esiste nel documento
**Dove:** `05:339` — *«l'anti-plagio passa a dieci parole, con soglia a due sequenze»*, nella
tabella dei cambiamenti. **Nel corpo del dossier non esiste nessuna voce anti-plagio**: non è nella
griglia madre (`05:124-171`), non è nelle tre classi (`05:113-117`), non è una fase (`05:69-81`).
**Perché si rompe:** chi costruisce legge la tabella finale come specifica e cerca invano cosa
implementare. È la stessa specie di difetto che i dossier dichiarano di aver corretto nel piano
precedente (`05:305`, `06:217`): un contratto dichiarato che non esiste.
**Riparazione:** o la voce entra nella griglia con punti, classe e metodo (n-grammi di 10 parole,
≥2 sequenze contro quale corpus?), o la riga esce dalla tabella dei cambiamenti.

### D-B-21 · Nessuno esegue le fasi «continue»: non esiste uno scheduler
**Dove:** `04:55` (il workflow *«si propone da solo»* quando un lancio entra in `ISTRUITO`),
`04:236-241` (la scala dell'inerzia a 3/7/14 giorni), `06:79` (F7 «continuo»), `06:281` (E5,
*«ogni giorno controlla»*, ore: «automatico»).
**Perché si rompe:** ogni riga presuppone un processo che gira senza che nessuno lo invochi.
In nessuno dei tre dossier è nominato un demone, un cron, un hook o un event bus, né chi lo accende
e chi lo sorveglia. È lo stesso difetto che `02:42-44` dichiara di aver corretto per la memoria
(*«non nominava chi invoca quegli script»*) — corretto lì, ripetuto qui.
**Riparazione:** un unico `battito` giornaliero dichiarato (chi lo lancia, cosa esegue in quale
ordine, dove scrive l'esito), e ogni riga «continuo/automatico» dei tre dossier diventa una voce di
quel battito con il suo script e il suo output.

### D-B-22 · Due dossier portano lo stesso numero, e un agente ha due nomi
**Dove:** `05:8` (`# 06 — WF-CPY`) in un file chiamato `05-WF-COPY.md`, e `06:8`
(`# 06 — WF-FNL`); `05:74`/`05:80` usano `lan-cpy-giudice`, `05:244` scrive `lan-copy-giudice`.
Inoltre `04` non ha frontmatter (comincia a `04:1` con l'H1) mentre `05:1-6` e `06:1-6` ce l'hanno.
**Perché si rompe:** è esattamente il difetto che `06:30-32` dichiara letale (*«un reparto con due
nomi riceve passaggi di consegne che nessuno raccoglie»*), commesso dai documenti che lo dichiarano.
E il dossier «cuore» è l'unico invisibile a qualunque indicizzazione per frontmatter.
**Riparazione:** rinumerare l'H1 del 05, unificare `lan-cpy-giudice`, aggiungere il frontmatter al 04.

---

## 3. BUCHI — cose che il piano NON dice e che servono per costruire

### B-B-01 · Diciassette file dichiarati, tre schemi consegnati
I tre dossier nominano come output: `offerta/00-precedenti.json`, `offerta/01-ruolo.md`,
`offerta/02-livello.json`, `offerta/03-mercato.json`, `offerta/04-proposta.md`,
`offerta/05-firma.json`, `offerta/07-struttura.json` (`04:96-105`), `copy/00-intake.json`,
`copy/01-obiezioni.json`, `copy/gate/10-punteggio.json`, `copy/70-coerenza.json`,
`copy/manifest.json` (`05:71-81`), `funnel/00-intake.json`, `funnel/01-topologia.json`,
`funnel/02-tracciamento.json`, `funnel/07-test.json` (`06:71-79`),
`editoriale/00-riusabili.json`, `editoriale/pubblicazioni.json`, `editoriale/evergreen.json`
(`06:276-282`). **Schemi effettivamente scritti: tre** — `offerta.json` (`04:251-276`),
`funnel.json` (`06:169-181`), la riga del piano editoriale (`06:299-315`). Tutto il resto è un
nome di file. Un nome di file non è un contratto: due agenti che lo leggono lo interpretano
diversamente, e il gate non può verificare niente.

### B-B-02 · Il listino a livelli e la «regola dei passaggi» sono il cuore del prezzo e non sono mai definiti
`livello: "0-4"` compare nell'input (`04:71`), la fase O2 «determina il livello e verifica la
regola dei passaggi» (`04:98`), l'input dice che senza catalogo *«la regola dei passaggi non può
essere verificata»* (`04:87`). **Le fasce dei cinque livelli sono citate una sola volta e solo per
il livello 1** (`04:149`, «7-47 €»). Cosa sia la regola dei passaggi non è scritto in nessun punto
dei tre dossier. `colloca_listino` (`04:291`) è quindi non implementabile.

### B-B-03 · `ricerca.json` non ha schema, e tre voci della griglia dipendono dai suoi campi
B1 «≥10 frasi della ricerca usate» (`05:139`), B2 «5 dolori» (`05:140`), B3 «≥3 buchi dei
concorrenti» (`05:141`), più E1 che conta «un elemento dichiarato assente nei concorrenti»
(`05:220-224`). Il criterio d'accettazione esiste (`02:245`: 15/5/3/3) ma non i **campi**. Senza
`frasi[] {testo, fonte}`, `dolori[] {id, testo}`, `concorrenti[] {nome, prezzo, fonte}`,
`buchi[] {id, testo}` nessuna di quelle voci è calcolabile — e sono 20 punti su 100 dichiarati in
parte «auto».

### B-B-04 · Nessun costo, in un'azienda che ha un CFO e un Cost Sentinel
Quattordici pezzi, un giudice LLM su ognuno, rifacimenti, cinque fasi parallele, un giudizio da
2-3 ore a pezzo (`05:26-29`): nessuno dei tre dossier dichiara un costo in token o in euro per
passata, né una soglia oltre la quale si chiede l'autorizzazione. È la voce che decide se il
sistema è sostenibile al terzo lancio.

### B-B-05 · Nessun permesso di scrittura per campo
`firmato_da` (`04:274`), `stato` (`06:312`), `url_pubblicato` (`06:314`) sono i tre campi che
provano rispettivamente una decisione umana, un avanzamento e una pubblicazione. `02:57` assegna un
proprietario per **spazio di memoria**, non per campo di artefatto. Chiunque scriva nel workflow
può scriverli.

### B-B-06 · «Giorni chiave coperti: 100%» senza definire i giorni chiave
`06:329`. Non è scritto quali siano (apertura? chiusura? metà carrello? ultime 24 h?), quindi il
gate editoriale ha un controllo su cinque non implementabile.

### B-B-07 · Nessuna sintassi, nessun parser, nessun fallback per i blocchi marcati
`05:107` fa nascere l'intera automazione (da 11 a ~42 punti) da `::claim`, `::prova`, `::beneficio`,
`::azione`, `::variante`. Non è definita la sintassi (inline? blocco? con attributi?), non esiste un
linter, e soprattutto **non è scritto cosa succede a un pezzo senza marcature**: bocciato per forma,
o giudicato a occhio? Se è bocciato, il gate boccia per un difetto di formato, non di contenuto —
e i modelli dimenticano le marcature con regolarità.

### B-B-08 · Il modello di similarità non ha un posto dove vivere
`paraphrase-multilingual-MiniLM-L12-v2` (`05:186`) va installato, pinnato per versione, eseguito da
qualche parte, e produce risultati diversi fra versioni. Nessuna riga dice dove gira, quanto pesa,
cosa succede senza rete, e chi verifica che la tabella di taratura promessa (`05:188`) sia ancora
verde dopo un aggiornamento.

### B-B-09 · Nessun meccanismo aggiorna le soglie dichiarate provvisorie
Il rapporto valore/prezzo ≥3 (`04:349-351`) e le sei soglie verde/giallo/rosso (`06:141-144`) sono
dichiarate provvisorie con l'impegno che *«il primo lancio ha il compito di produrre il numero
vero»*. **Nessuna fase produce quel numero, nessun file lo ospita, nessun gate lo legge.** Il
meccanismo per farlo esiste già altrove (`pattern.py conferma`, `02:307`) e non è agganciato.

### B-B-10 · Nessun rollback
F5 è dichiarata irreversibile (`06:76`) e questo è tutto ciò che si dice. Se una pagina pubblicata
è sbagliata — prezzo vecchio, promessa non approvata, cassa rotta — non esiste una procedura per
toglierla, né uno stato per «online ma da non promuovere».

### B-B-11 · La lista degli impegni che governa la scelta della data non ha origine
`proponi_data(oggi, giorni_preparazione, impegni)` (`04:294`) e i «conflitti controllati»
(`04:197-199`). Chi popola `impegni`? Non esiste un calendario condiviso dichiarato nei tre
dossier. E `giorni_preparazione` è un parametro il cui valore (30, `04:195`) non ha derivazione.

### B-B-12 · Nessuna gestione di rimborsi e garanzia
L'offerta emette `garanzia: {giorni: 14, condizioni}` (`04:266`). Nessun flusso registra un rimborso,
e la metrica economica del lancio (che vive in un altro dossier) userà ricavi lordi. Con garanzia a
14 giorni e carrello a 5, il numero vero si conosce **19 giorni dopo la chiusura**: nessuna riga lo
dice, e il debrief rischia di certificare un risultato che non è ancora accaduto.

---

## 4. AMBIGUITA' E CONTRADDIZIONI INTERNE

1. **Procedere senza ricerca condanna il copy, e nessuno dei due dossier lo dice.**
   `04:86` permette di prezzare *«senza mercato davanti»*. Ma la griglia madre assegna 20 punti al
   blocco B, tutti derivati dalla ricerca (`05:139-141`), più E1 (`05:220-224`) che ne dipende in
   parte. Un lancio che procede cieco parte con un tetto di ~75-80 punti su una soglia di 80
   (`05:115`): **la pagina di vendita non può passare il proprio gate.** Le due deroghe sono
   coerenti ciascuna con sé e incompatibili fra loro.

2. **La stessa regola vive in due gate, con due proprietari.**
   Valore ≥3× prezzo: `04:104` e `04:227` (GATE-OFF-1) e `05:133` (A6, griglia copy). Se la soglia
   cambia — ed è dichiarata provvisoria a `04:349` — cambia in un posto solo, e i due gate
   divergono in silenzio.

3. **Tre unità di misura per il tempo, in tre dossier dello stesso ecosistema.**
   `04:40`: «3-5 ore di lavoro **della macchina**». `05:24`: «40-55 **ore-uomo**». `06:28`: «30-45
   **ore-uomo**». Non è dichiarato chi siano gli «uomini» quando il lavoro lo fanno agenti, né come
   si sommano con i «trentasette giorni» del calendario citato a `05:281`. Nessuna di queste stime
   è confrontabile con la capacità dichiarata da un altro ecosistema (`02:263`).

4. **La data si può spostare per silenzio, ma è firmata.** Vedi D-B-15: `05:289`/`05:293` contro
   `04:102` e `04:228`.

5. **La transazione di prova è precondizione o controllo di gate?** `06:62` la mette fra le
   precondizioni d'ingresso al flusso; `06:115` la mette come controllo 8 del gate finale. Sono
   due transazioni o una sola contata due volte? Nessuna riga lo dice.

6. **La pagina di vendita si riscrive o si riusa?** `06:212`: *«la landing già costruita si
   verifica e si collega, non si rifà»*. `06:95`: la pagina di vendita *«riceve i testi da
   LAN-CPY»*. `05:73`: C2 la scrive da zero in 8-12 ore. Per il Manuale — che una landing ce l'ha —
   i tre passaggi prescrivono tre comportamenti diversi, e F0 (`06:71`) «decide quali si riusano»
   senza un criterio scritto.

7. **Due organi di gate diversi, nessuna regola su quale si usa quando.** `05:74` fa eseguire il
   gate del copy a `lan-cpy-giudice` + `sentinel-quality`; `06:279` fa eseguire il gate editoriale
   a `lan-qlt-gate`; `04:104` usa `lan-qlt-gate` per l'offerta ma `06:78` usa
   `lan-fnl-verificatore` per il funnel. Quattro gate, tre esecutori diversi, nessun criterio.

8. **La classe più numerosa è la meno definita.** «Micro: cinque voci, binaria, tutte e cinque
   superate» (`05:117`). Nella griglia madre quelle stesse voci sono punteggi su scala (`05:128`,
   `05:130`); qui diventano pass/fail senza soglia e senza rubrica. Sono 28 email più gli annunci
   (`05:78-79`): **la maggioranza assoluta dei pezzi passa dal criterio meno specificato.**

9. **«Una pagina che non produce un numero non è online»** (`06:26`) è contraddetta dal proprio
   gate: il controllo 4 prova **un** evento in **una** visita (`06:111`), cioè un istante. Non
   esiste monitoraggio continuo (F7 è un ottimizzatore, non una sentinella): il giorno dopo un
   deploy o un cambio di banner l'evento sparisce e nessuno se ne accorge.

10. **L'orologio dell'inerzia misura solo il tratto finale.** `04:215` dice «dopo 7 giorni», la
    tabella `04:236-241` dettaglia 0-2/3/7/14, ma `04:296` definisce il conteggio come «da quanto
    **la proposta** aspetta». Tutto ciò che accade prima di O4 è fuori misura — cioè il blocco vero.

11. **Il gate del webinar non esiste nella griglia.** `05:272-273`: *«il gate lo verifica — se il
    titolo non è riconducibile alla promessa, il webinar non passa»*. «Riconducibile» non è
    definito, non è una voce della griglia madre (che si applica al webinar per `05:115`), non ha
    punti e non ha esecutore. È un gate nominato e inesistente.

12. **«Il flusso non resta fermo ad aspettare la ratifica»** (`06:239`) rinvia lo standard visivo a
    un organo esterno senza scadenza e senza default — la definizione di «punto di morte» data a
    `05:297`. E non è scritto cosa si rifà se la guild decide il contrario di ciò con cui si è
    costruito.

---

## 5. DOVE IL PIANO E' PROSA INVECE CHE ARCHITETTURA

**1. La proposta di prezzo è un mockup ASCII, non un contratto dati** (`04:143-170`).
`istruisci(lancio_id) -> str` (`04:293`) è dichiarata *«la funzione più importante del reparto»* e
ritorna **una stringa opaca**: non è testabile se non facendola leggere a una persona. Riparazione:
`istruisci` ritorna `{proposta: {valore, ragioni[]}, alternative: [{valore, guadagni[], perdite[]}],
non_so[], vincoli_applicati[]}`; il testo è un renderer separato. Il contenuto diventa verificabile,
la forma resta identica.

**2. `proponi_data` non ha regole.** `04:191-195` elenca quattro ragioni in prosa (martedì e
mercoledì, cinque giorni, domenica sera, trenta giorni a ritroso). Nessuna è un parametro, nessuna
ha una fonte, il 30 non ha derivazione. La funzione (`04:294`) non può che riprodurre queste frasi
come stringhe.

**3. Le «ancore di punteggio» sono promesse e mai consegnate** (`05:173-174`). Zero ancore nel
documento. Senza, 58 punti su 100 non sono riproducibili fra due esecuzioni dello stesso giudice.

**4. La tabella di taratura è un impegno futuro** (`05:188`): *«il piano consegna una tabella di
taratura con dieci coppie»*. Il piano dichiara che consegnerà il criterio invece di darlo, e non
stima le ore per produrlo. Stessa specie: le tre griglie per classe (`05:113-117`) descrivono la
regola del denominatore variabile senza mai elencare **quali voci non si applicano a quale classe**
— cioè senza la sola cosa che serve per calcolare il denominatore.

**5. Il ciclo di ottimizzazione è un blocco di cinque parole** (`06:148-154`) mentre il suo output
`funnel/07-test.json` (`06:79`) non ha schema. Un test ha ipotesi, variante, metrica, volume
richiesto, volume raggiunto, esito, data: nessuno di questi campi è dichiarato.

**6. Il piano di tracciamento (F2) produce `funnel/02-tracciamento.json`** (`06:73`) — l'artefatto
da cui dipende il controllo più importante del gate — e non ha né schema né esempio: non è scritto
cosa sia un «evento» (nome, parametri, dove si dichiara), quindi il controllo 4 non ha un contratto
con cui confrontarsi.

**7. «Il verificatore non è il costruttore»** (`06:83`) è enunciata come regola forte, ma
`lan-fnl-verificatore` esegue F2 (`06:73`) — cioè **scrive il piano di tracciamento** — e poi
verifica il tracciamento a GATE-FNL-1 (`06:78`). Chi definisce il criterio e poi lo verifica non è
indipendente: la regola è dichiarata e violata nella stessa tabella.

**8. Le tre quote editoriali (70/20/10, `06:287-290`)** hanno tolleranza ±10 punti nel gate
(`06:330`) e nessuna definizione di come si classifica un pezzo nei tre tipi. Chi decide che un
video è «richiamo» e non «spostamento»? Non scritto: il gate misura una proporzione fra etichette
che nessuno sa assegnare in modo riproducibile.

**9. «Si propone da solo» (`04:55`), «continuo» (`06:79`), «automatico» (`06:281`)**: tre
comportamenti attivi senza un esecutore. Vedi D-B-21.

**10. «Il reparto Vendite & Funnel lo avvolge: i suoi workflow diventano il contenuto delle fasi F1
e F7, le sue schede agente diventano la specifica dei nostri quattro agenti»** (`06:207`).
È la frase che sembra decidere e non decide: non dice **quali** dei tre workflow finiscono in F1 e
quali in F7, né quale delle sei schede diventa quale dei quattro agenti. Sei a quattro non è una
mappatura ovvia: due schede restano fuori, o due agenti ne ereditano due. Il lavoro di
riconciliazione è tutto da fare e non è stimato.

## 6. CIO' CHE INVECE E' SOLIDO — non toccarlo

**S-01 · Il principio di `04:26-28`** — *«un gate posto su una decisione umana deve arrivare con la
decisione già istruita; "decidi" delega la fatica, "confermi questo?" toglie fatica»*. È la pagina
migliore dei tre documenti e va promossa a regola di ecosistema, applicabile ovunque ci sia un
punto umano. Il resto della critica non è contro questo principio: è contro il fatto che il piano
non lo applica a se stesso.

**S-02 · La forma della proposta** (`04:145-179`): numero già dato, due alternative **con la
conseguenza accanto**, blocco `NON SO` esplicito, domanda binaria con la via d'uscita
`[no, preferisco ___]`. Va tenuta parola per parola come contratto di presentazione — solo
tipizzata sotto (§5.1 della critica), non riscritta.

**S-03 · La reversibilità come criterio di scelta** (`04:128`, riga «Reversibile?»). È
l'informazione che quasi sempre manca quando una decisione si impantana, ed è giusto averla messa
in tabella. Va usata anche come **regola di default automatico**, non solo come argomento.

**S-04 · `alternative_scartate` e `non_misurato` persistiti nell'output** (`04:269-273`), con la
motivazione di `04:279-281` (*«al terzo lancio permette di vedere se si è sempre scelto troppo
basso»*). Raro, corretto, a costo zero. Da estendere agli altri reparti.

**S-05 · Il controllo «valore evasivo»** (`04:220-228`): la lista `"da definire" / "non lo so" /
"tbd" / "presto" / "prossimamente" / ""` è concreta, implementabile in un'ora e cattura un
fallimento reale. `valori_evasivi(offerta) -> list[str]` (`04:302`) è una delle poche firme
davvero costruibili così com'è.

**S-06 · Sganciare le fondamenta dal prezzo** (`05:33-46`). È la correzione più intelligente dei
tre dossier: aver visto che bloccare la promessa dietro il prezzo riproduce il blocco che
l'ecosistema esiste per sciogliere. Il guadagno dichiarato a `05:45-46` è reale.

**S-07 · Il denominatore variabile per classe di pezzo** (`05:113-120`), con la motivazione
*«darle zero su quella voce è punirla per aver fatto bene il suo mestiere»*. Corretto. Manca solo
l'elenco delle voci per classe (§5.4 della critica), non l'idea.

**S-08 · Legare le varianti al traffico disponibile** (`05:229-240`) e la sua coerenza esplicita
col dossier del funnel. Aver ucciso 196 varianti inutili è una decisione giusta e ben motivata.

**S-09 · L'autocritica verificata sul codice** (`05:301-320`, `06:214-227`): aver misurato che i
cinque componenti non hanno parametri e aver dichiarato che il piano stesso aveva scritto un
contratto inesistente è il comportamento più sano dei tre documenti. Va tenuto come metodo:
**ogni riuso dichiarato va verificato prima di essere scritto**.

**S-10 · La prova di pubblicazione è l'indirizzo, non il codice di uscita** (`06:255-259`,
`06:270`), nata da un fatto reale (uno strumento che stampa «SIMULATA» ed esce zero). È il criterio
giusto, verificabile, e va copiato ovunque un'automazione dichiari un successo.

**S-11 · Due pagine d'ingresso separate per traffico organico e a pagamento** (`06:52-56`). La
motivazione è tecnicamente corretta: mescolarli rende ogni numero successivo una divisione fra
grandezze scollegate. Da tenere.

**S-12 · «Le pagine non necessarie si dichiarano, non si omettono»** (`06:100-102`) e
`pagine_non_previste` nell'output (`06:179`). Piccolo, giusto, elimina una classe intera di
ambiguità.

**S-13 · L'intuizione dei controlli 4 e 8** (`06:111`, `06:115`): pretendere che l'evento **arrivi**
e che qualcuno **paghi davvero** è ciò che separa un gate da una formalità. L'intuizione è
corretta; è la specifica della prova a essere insufficiente (D-B-09, D-B-18). Non buttare i
controlli: completarli.

**S-14 · La distinzione fabbrica/committente** (`06:335-336`): *«il reparto Editoriale ordina e
verifica, non produce»*, con la ragione (nascerebbe una seconda fabbrica di contenuti). Confine
giusto, e coerente col resto dell'Impero.

---

## 7. LE 5 COSE PIU' IMPORTANTI DA CAMBIARE

### 1. Mettere una scadenza e un default sul blocco vero — O1, non O5
`04:97`, `04:117`, `04:315`. Oggi il flusso ha un timer sulla firma del prezzo e **nessun timer sul
punto in cui il caso reale si ferma**: la scelta del ruolo del prodotto. Il default esiste già nel
testo (`04:128`: A è reversibile, B no) e la regola per scriverlo pure (`05:296-297`). Finché O1
resta senza scadenza, il dossier 04 documenta il blocco invece di scioglierlo, e la sua metrica
regina (`04:323`) non registra nemmeno il fallimento. **È il difetto che rende falso il titolo del
documento.**

### 2. Rendere la firma provabile e legata al contenuto firmato
`04:228`, `04:230-232`, `04:295`. Un gate che accetta la stringa `"Max"` in `firmato_da` non
distingue una decisione umana da un agente che si sblocca da solo — ed è il fallimento peggiore
possibile per questo reparto, peggiore dei sei mesi di silenzio. Servono `canale_firma` in lista
chiusa, `proposta_hash`, e il divieto di scrittura per gli agenti su quel sotto-oggetto. Senza
questo, tutto l'impianto «la macchina istruisce, l'umano firma» è indimostrabile a posteriori.

### 3. Dare a ogni gate un ramo di fallimento e a ogni artefatto una versione
`04:104`, `05:74`, `06:78`, `06:279` (nessun `su_fallimento`); `05:40-43`, `06:212`, `04:327`
(nessuna invalidazione a valle). Il piano è scritto per l'ordine perfetto e per il primo tentativo
riuscito. Nella realtà il prezzo arriva dopo le fondamenta **per progetto**, Max risponde
«preferisco 27», un pezzo esce a 74 e la landing esiste già. Servono `su_fallimento {torna_a,
max_tentativi, oltre_N}` su ogni gate e `offerta_versione`/`fondamenta_versione` su ogni derivato,
con marcatura automatica `da_rigenerare` al cambio di hash.

### 4. Consegnare le due liste e le ancore, o la griglia del copy non è costruibile
`05:200-209` + `05:156` (la voce eliminatoria «auto» che poggia su due liste inesistenti);
`05:173-174` (ancore promesse, zero scritte); `05:188` (tabella di taratura rinviata);
`05:113-117` (tre classi senza l'elenco delle voci per classe). Sono quattro dipendenze mancanti
sotto lo stesso gate. Finché non esistono `01-prove.json` e `architettura.json` con
`output_pratici[]`, la parte «automatica» della griglia resta un giudizio con un numero attaccato —
la cosa che il dossier dichiara di aver eliminato a `05:94-96`.

### 5. Specificare la prova del tracciamento (fonte, payload, consenso) invece di un `bool` a 60 secondi
`06:111`, `06:117-120`, `06:126-127`, `06:192`. Il controllo che il dossier chiama *«ciò che separa
questo gate da una formalità»* oggi non è implementabile: non dice dove si legge l'evento, e con
un timeout di 60 secondi produce falsi negativi sistematici sugli strumenti reali. Un gate che
boccia a caso viene derogato al primo lancio, e un gate derogato una volta smette di esistere
(`04:21-22`). Serve `prova_evento(url, evento, fonte, timeout_s) -> dict` con payload e
`ricevuto_il`, la fonte di verità dichiarata per strumento, e la **doppia visita** con consenso
accettato e rifiutato.

---

*Menzioni d'onore, fuori classifica ma da non perdere:* le copertine come punto umano di massa mai
contato (D-B-19, `06:339-340` contro `05:286-294`); l'assenza di uno scheduler per tutto ciò che è
dichiarato «continuo» (D-B-21); e i due dossier che portano entrambi il numero 06 nell'H1
(`05:8`, `06:8`).
