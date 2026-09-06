# ✂ CRITICA 3 — VERITÀ E OMISSIONI

> **Oggetto:** `V1-PIANO-GENERALE.md` (522 righe, letto per intero)
> **Angolo:** la verità delle affermazioni e ciò che manca — numeri, prove, contraddizioni coi censimenti chiusi, omissioni, legge L1/L7
> **Revisore:** indipendente, non l'autore del piano
> **Data:** 2026-09-06
> **Metodo:** ogni rilievo scritto appena formulato (append), ogni rilievo con prova misurata

---

### R-1 — V1 rimanda due volte a un §30 che non esiste  [MEDIO]
- **Tipo:** NUMERO SBAGLIATO (riferimento interno mal citato)
- **Dove:** V1 riga 41 («È dichiarato qui e ripreso in §30») e riga 391 («per il limite di sessione (§30)»)
- **Cosa dice il piano:** che la ripresa dei censimenti incompleti e la caduta del doom bot dell'addestramento sono trattate «in §30».
- **Cosa dice la realtà:** V1 finisce a §27 («Cosa V1 NON copre»). Non esistono §28, §29 né §30 — verificato con `grep -n "^## " V1-PIANO-GENERALE.md`: ultima sezione a riga 507.
- **Perché conta:** in un piano che sarà riletto da forze diverse in sessioni diverse, un puntatore interno rotto manda a cercare una sezione che non c'è. È esattamente la «REGOLA PUNTATORI: MAI STALE» del CLAUDE.md di questo repo.
- **Cosa proporresti:** correggere i due rimandi in «§27» (o nella sezione reale che tratta la ripresa).

### R-2 — La tabella delle fonti è già stantia: 3.078 righe di censimento chiuso che V1 non ha mai letto  [GRAVE]
- **Tipo:** CONTRADDIZIONE COL CENSIMENTO (fonti superate)
- **Dove:** V1 §0.3 (tabella fonti, «5.042 righe») e intestazione («Ogni numero di questo piano viene da lì»)
- **Cosa dice il piano:** `02b` = 208 righe, `04`+`04b` = 196 righe, totale fonti 5.042 righe. Tre censimenti dichiarati incompleti.
- **Cosa dice la realtà:** `wc -l dati/*.md` oggi: `02b` = **619** righe, `04`+`04b` = **694** righe (81+613), e la tabella fonti **non nomina affatto** tre censimenti ora chiusi: `01c-sintesi-organi` (468 righe), `02d-sintesi-collegamenti` (622), `03c-addestramento` (1.064). Totale `dati/` = **8.120 righe**, non 5.042. Cronologia da filesystem: V1 salvato alle 19:23:08 del 6/9; `02b` chiuso 19:38, `01c` 19:40, `03c` 19:40, `04b` 19:47, `02d` 20:01 — **tutti dopo**.
- **Perché conta:** V1 dichiara onestamente il buco in §27, ma resta un piano il cui 38% della base di misura (3.078 righe su 8.120) non è mai entrato nel testo. Ogni sezione che tocca motori, collegamenti, organi e addestramento va riletta contro i censimenti chiusi prima di V2 — e come i rilievi seguenti mostrano, su più punti i censimenti chiusi lo smentiscono frontalmente.
- **Cosa proporresti:** V2 riapre le fonti: aggiorna la tabella §0.3 con i numeri veri e integra riga per riga 01c, 02d, 03c e il 04b completo.

### R-3 — V1 dice «il doom bot dell'addestramento non è mai partito»: invece ha consegnato 1.064 righe  [GRAVE]
- **Tipo:** CONTRADDIZIONE COL CENSIMENTO
- **Dove:** V1 §20 («Il dettaglio pieno con le tre varianti (scagnozzo / sentinella / doom bot) è rimandato a V2: il doom bot che doveva progettarlo non è mai partito per il limite di sessione») e §27.4
- **Cosa dice il piano:** modulo d'ingaggio e addestramento «abbozzati, non progettati», materiale inesistente.
- **Cosa dice la realtà:** `dati/censimento-03c-addestramento.md` esiste, **1.064 righe**, chiuso alle 19:40 del 6/9 (17 minuti dopo V1). Il `00-LEGGIMI.md` §4 lo registra come «✅ 19 fonti · minimo comune 10 righe · modulo d'ingaggio in 3 varianti · costo 180-550 token per forza».
- **Perché conta:** V1 rimanda a V2 la progettazione di una cosa **già progettata su disco**. Chi eseguisse V1 alla lettera rifarebbe da zero un lavoro consegnato — lo stesso identico errore della «cartella vuota» che vuota non era (L7, e la ragione d'essere della legge L1).
- **Cosa proporresti:** V2 assorbe §19-20 direttamente da 03c, citandolo, senza rifare niente.

### R-4 — V1 propone di costruire il punto d'ingresso: l'involucro esiste già, in doppia copia  [FATALE]
- **Tipo:** CONTRADDIZIONE COL CENSIMENTO
- **Dove:** V1 §14 («Ogni ecosistema deve avere un comando che parte, chiama il motore vero dov'è») e E5 («un comando per ecosistema che chiama il motore vero», 25-35 h)
- **Cosa dice il piano:** i punti d'ingresso vanno creati. Il nome «EmpireDesk» e il meccanismo `register(sub)` non compaiono in nessuna riga di V1 (`grep -in "empiredesk\|register(sub"` → 0 risultati).
- **Cosa dice la realtà:** `censimento-04b-motori.md` §4 e §12: `empire/` (14.628 righe, VIVO) è costruito apposta per ricevere motori come plugin — «un motore che espone `register(sub)` diventa un sottocomando `python -m empire <x>` senza toccare una riga di `cli.py`» — ed `EmpireDesk/` (VIVO, scritto oggi, `state/taskboard.json` 2026-09-06) già lancia come subprocess 4 motori su 25: `produci_video_completo.py`, `run.py` di Preventa, `gestione-licenze.py`, più `metrics.py` che però conta i caroselli dalla cartella sbagliata (04b riga 407). Conclusione testuale del censimento (righe 610): «Il patrimonio dell'Impero non è privo di un guscio: ne ha due, già costruiti e vivi.»
- **Perché conta:** E5 prezza 25-35 ore per costruire ciò che in larga parte è da *agganciare*, non da costruire. Peggio: due gusci nuovi (i «punti d'ingresso per ecosistema» di V1) accanto ai due esistenti sarebbe la quarta ripetizione del difetto che il censimento chiama «costruzione ripetuta» — cinque APEX-7, due workshop estate, tre cartelle caroselli.
- **Cosa proporresti:** V2 riscrive §14/E5 come «aggancio dei motori a `empire/` (`register(sub)`) e a EmpireDesk», con la riparazione di `metrics.py` come primo gate.

### R-5 — Il motore più prezioso dell'Impero non è nel piano: la fabbrica libri, orfana, con numero sbagliato  [FATALE]
- **Tipo:** OMISSIONE + NUMERO SBAGLIATO
- **Dove:** V1 §1 (un inciso: «più il solo workflow libri dentro 02-INFO-BUSINESS») e E8 («I 4 libri KDP pubblicati (`libri_pubblicati/` contiene solo `.gitkeep`)»)
- **Cosa dice il piano:** i libri sono un item dell'ultimo scaglione operativo (E8, dopo NEXUS, esecutori e ondate agenti), e sono «4».
- **Cosa dice la realtà:** su disco (`ls LIBRI/libri_pronti/`) i libri finiti sono **6**: tre del 2026-09-02, due del 2026-09-04, uno del 2026-09-06 — quattro dei sei esistevano già da giorni quando V1 è stato scritto. E `censimento-04b` §17: il motore (`libri-performanti-multiagente`, **9.737 righe**, `python -m engine.kdp auto`, gate che riscrive i blocchi bocciati, unico motore che dichiara il costo unitario misurato) è **orfano di ogni registro**: `grep "libri" company/REGISTRO-IMPRESA.md` → 0 righe, mentre `skills-map.yaml` censisce al suo posto due gusci morti (`Workflow-libri/` fermo da 169 giorni, `KDP - prodottti digitali/` da 151).
- **Perché conta:** V1 §21.3 proclama «Prima ciò che porta denaro» — e l'unico motore che produce un bene vendibile ogni giorno sta nell'ultimo scaglione, senza nome, senza la sua anomalia di registro (che viola L6 oggi, non domani), e con il conteggio dei prodotti sbagliato per difetto. Il piano ripete qui, in piccolo, l'errore che dichiara di voler impedire: parlare di un asset senza averlo aperto.
- **Cosa proporresti:** la riga di registro per `libri-performanti-multiagente` e la pubblicazione dei 6 (non 4) libri salgono accanto a E0 fra le cose che portano denaro subito.

### R-6 — I numeri dei collegamenti ora esistono e V1 non li ha: 328 progettati, 21 con contratto, 0 fra ecosistemi  [GRAVE]
- **Tipo:** CONTRADDIZIONE COL CENSIMENTO (lacuna dichiarata, ora colmata e mai integrata)
- **Dove:** V1 §27.1 («Non so ancora quanti collegamenti l'Impero abbia progettato, né quali ecosistemi siano isolati») e §12 (NEXUS motivato senza la mappa)
- **Cosa dice il piano:** la mappa dei passaggi non c'è; NEXUS è progettato «al buio» su questa parte.
- **Cosa dice la realtà:** `censimento-02d` (622 righe, chiuso alle 20:01): **328 passaggi progettati** (57 INTRA, 262 INTER, 9 misti), **21 con contratto** (6,4%), **4 percorsi una volta sola** (a vuoto, dry-run, 87 giorni fa), **0 INTER su 271 mai avvenuti**. E i fatti che cambiano l'architettura di V1: l'Impero ha **10 schemi di comunicazione**, non i soli 3 formati traccia di §10; `11-APEX-7` è isolato del tutto e il suo Event Bus «non ha un campo dove scrivere il destinatario» (B.3) — HC-v2 non può agganciarlo così com'è; 29-LANCI ha i passaggi meglio scritti e `IN = 0`; i 4 ecosistemi Core hanno divieti assoluti («nessuno può aggirarli») e 0 handoff ricevuti.
- **Perché conta:** N1/N2 di NEXUS (§12) e la scelta della fetta verticale (E3) sono decisioni di instradamento prese senza la matrice che ora esiste. La Sintesi C di 02d ordina i 10 collegamenti da accendere con criterio esplicito (incasso, sblocco a valle, motore da entrambe le parti): V2 non può ignorarla.
- **Cosa proporresti:** V2 assorbe la Sintesi B/C di 02d come base di N1 e riverifica E3 contro il punto C.1 (catena AGENCY) e C.2 (ULTIMO METRO, coda già piena).

### R-7 — HC-v2 dimentica il campo che la legge della MEMORY dichiara obbligatorio: il CP-id  [GRAVE]
- **Tipo:** OMISSIONE (dentro la specifica più citata del piano)
- **Dove:** V1 §9 (la tabella dei «dieci campi che mancano» a HC-v2)
- **Cosa dice il piano:** elenca 10 campi mancanti (`_instance_id`, `created_at`, `status`, `queue`, `scope`, `brand_kit`/`icp`, `note_correttive`, `retry`, firma, criterio a macchina). Nessun campo `cp_id`.
- **Cosa dice la realtà:** `censimento-02d` D.5, citando `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:180-182`: *«un handoff senza CP-id è invalido per contratto»* — regola attiva, che oggi invalida tutti i 328 passaggi, compresi i 4 attraversati l'11 giugno (il campo `cp_id` non esiste in `trace.jsonl`, verificato aprendo il file).
- **Perché conta:** V1 costruisce HC-v2 proprio per rendere i passaggi validi e instradabili, e produce uno schema che nascerebbe **già invalido** per una legge scritta dell'Impero. È il tipo esatto di collisione fra regole che V1 altrove rimprovera (due gate con verdetti opposti).
- **Cosa proporresti:** aggiungere `cp_id` all'elenco §9, oppure dichiarare esplicitamente un ADR che modifica la regola della MEMORY. Mai in silenzio.

### R-8 — La Tesoreria «è una riga», ma la riga più economica il piano non la vede: il campo `costi` dei 303 checkpoint  [MEDIO]
- **Tipo:** OMISSIONE
- **Dove:** V1 §23 («serve il primo movimento registrato. Va agganciato a N4») e E4 (il ledger dentro NEXUS, 25-40 h)
- **Cosa dice il piano:** l'aggancio della Tesoreria passa da N4, cioè da un pezzo di NEXUS ancora da costruire.
- **Cosa dice la realtà:** `censimento-02d` C.4: il contratto `HC-ME-POST` dichiara già il campo `costi` (`09-ECOSISTEMA-MEMORY.md:45`), il flusso checkpoint gira già **303 volte** con enforcement cablato, e il campo **non è mai stato compilato**. Stima del censimento: rendere `costi` obbligatorio in `scripts/checkpoint.py` è «un'ora di lavoro, e da quel giorno ogni task chiuso lascia un numero». Nessun NEXUS richiesto.
- **Perché conta:** V1 fa dipendere la prima misura di denaro da E4 (decine di ore, più un ADR); esiste una via già asfaltata che parte oggi. Un piano che dichiara «prima ciò che non costa e sblocca molto» (§21.1) doveva vederla.
- **Cosa proporresti:** spostare «campo `costi` obbligatorio in `checkpoint.py`» dentro E0/E1, come alimentatore della Tesoreria in attesa di N4.

### R-9 — Il magazzino pieno non esiste nel piano: 25 pezzi finiti (23 caricabili OGGI) e nessuno scaglione li pubblica  [FATALE]
- **Tipo:** OMISSIONE
- **Dove:** assente da tutto il piano — `grep -in "ultimo metro|25 pezzi|mai pubblicat|B-043|ADR-016" V1-PIANO-GENERALE.md` → **0 risultati**
- **Cosa dice il piano:** «Prima ciò che porta denaro. L'azienda oggi non può incassare un euro» (§21.3, riga 403). Poi l'unico atto di denaro in tutto il piano: «**2 Payment Link Stripe**» in E0 (riga 410). Nessuno scaglione da E0 a E9 pubblica o vende alcunché.
- **Cosa dice la realtà:** ADR-016 ULTIMO METRO, misurato da `scripts/ultimo_metro.py` e registrato in `company/Memory/STATO-EMPIRE.md` (righe 9341-9343): **«25 pezzi finiti mai usciti, 2.137 MB, il più vecchio fermo da 135 giorni, 23 caricabili subito»**. E la stessa pagina di STATO-EMPIRE elenca fra le tre decisioni che aspettano Max: «I 23 pezzi caricabili oggi — servono gli accessi ai negozi: nessuno può farlo al posto di Max». Intanto `company/Memory/tesoreria/entrate.jsonl` = **0 byte** (dal 3 settembre).
- **Perché conta:** un Payment Link incassa solo se qualcosa è in vendita. Il piano costruisce la *capacità* di incassare (E0) e il *registro* dell'incasso (N4), ma **salta l'atto che sta in mezzo: mettere fuori la merce già prodotta e pagata**. La via più corta al primo euro — caricare 23 pezzi finiti — non richiede NEXUS, non richiede contratti C4, richiede gli accessi ai negozi: è per definizione materia di E0 («le mani di Max, nessuno le fa al posto suo»), e in E0 non c'è. Il principio §21.3 resta un principio: **nessun gate del piano, da E0 a E9, è espresso in euro o in pezzi pubblicati.** Un piano per «rendere viva» un'azienda che misura tutto (tracce, percentuali, exit code) tranne il denaro ripete esattamente B-043 — «la ragione per cui nessuno si era accorto che il magazzino era pieno e le vendite zero».
- **Cosa proporresti:** dentro E0, dopo i Payment Link: «pubblicazione dei 23 pezzi caricabili (accessi = mani di Max)»; e un gate di piano in denaro: «entro la chiusura di E3, `entrate.jsonl` > 0 byte».
### R-10 — 130-190 ore di lavoro e nessun nome accanto: Gael e Neri non esistono in V1  [GRAVE]
- **Tipo:** OMISSIONE
- **Dove:** tutta la Parte V (§21-23) e la Parte IV (§16-20)
- **Cosa dice il piano:** un solo scaglione ha un esecutore: E0, «LE MANI DI MAX (45 minuti, nessuno le fa al posto suo)». Per E1-E9 — la somma dichiarata fa **127-194 ore** — nessun assegnatario. EMPERATOR compare solo come autore (riga 3) e come chi «ordina» in E3/E5 (righe 431, 444): ordina, non esegue.
- **Cosa dice la realtà:** l'azienda ha **tre teste umane**: `grep -cin "gael" V1` → **0**, `grep -cin "neri" V1` → **0**. Eppure l'Impero assegna già il lavoro per nome: esiste `PIANO-MAESTRO/25-GAEL-TASK-BOARD-OPERATIVO.md`, EMPIRE DESK è spartito Max A1-A4 / Gael B0-B4 (dossier 17 §5) ed è dichiarato «lavoro #1», e Neri è operativo su tutto Outreach dal 23 agosto. V1 non dice se questi impegni si fermano, proseguono in parallelo, o assorbono gli scaglioni.
- **Perché conta:** un piano senza nomi è un piano che esegue «qualcuno», e «qualcuno» è il soggetto che in questa azienda ha già prodotto l'Osservabilità: un README senza un padrone. Peggio: V1 ridefinisce le priorità dell'Impero **senza riconciliarsi col lavoro già assegnato** — se Gael sta su EMPIRE DESK «lavoro #1» e V1 non lo nomina, il giorno che V1 parte esistono due «lavori #1» e nessun documento dice quale vince. È lo stesso tipo di collisione fra piani che V1 §5 pretende di regolare per B0..B8 e per il Dossier 30 — ma per le persone non lo fa.
- **Cosa proporresti:** una colonna «Chi» nella tabella degli scaglioni (Max / Gael / Neri / EMPERATOR+forze), più una riga in §5 che dica cosa succede a EMPIRE DESK e alla task board di Gael mentre V1 gira.
### R-11 — Nessuna misura fra un gate e l'altro: il piano si accorge del ritardo solo a scaglione finito  [GRAVE]
- **Tipo:** OMISSIONE
- **Dove:** assente da tutto il piano — i sei «Gate:» di §22 (righe 411-444) sono tutti di **fine scaglione**; `grep -in "giorn|quotidian|cadenz|scadenz|settiman"` su V1 non trova una sola riga di cadenza o data
- **Cosa dice il piano:** ore per scaglione (4-6, 6-10, 12-18, 25-40, 25-35, 30-45, 25-40) e un gate al termine di ognuno. Fra l'inizio e il gate: niente.
- **Cosa dice la realtà:** E4 da solo vale 25-40 ore — a ritmo reale, **settimane di calendario** — e il rischio numero uno dichiarato dal piano stesso (§24 R1: caduta di sessione, «nove episodi in tre mesi, e stanotte il decimo») colpisce *dentro* gli scaglioni, non ai gate. Gli strumenti per una misura giornaliera **esistono già e sono rilanciabili a costo zero**: `empire controllo` (il 2/6→5/6 di E0), `forge scan` (la % OPERATIVO di E2), `trace stato` (E3), `scripts/ultimo_metro.py`. V1 li usa tutti — ma solo come traguardo, mai come termometro.
- **Perché conta:** su 130-190 ore senza misura intermedia, uno scaglione che deraglia si scopre deragliato a lavoro speso — che è esattamente la definizione che V1 §18 dà del costo della caduta in produzione («il lavoro perso è lavoro che ha già speso»). Il piano applica la lezione della scrittura incrementale ai *file* dei doom bot e non la applica a *se stesso*: V1 non ha l'equivalente del proprio «file d'uscita risalvato a ogni sezione».
- **Cosa proporresti:** un cruscotto giornaliero di 4 numeri già calcolabili (`controllo` x/6 · OPERATIVO % · tracce · byte di `entrate.jsonl`), scritto in coda a STATO-EMPIRE a ogni giornata di lavoro sul piano, con la regola: due giornate senza avanzamento del numero dello scaglione aperto = fermarsi e dichiararlo.
### R-12 — Il piano non sa perdere: nessun criterio di abbandono, e nessun piano B se Max dice no a NEXUS  [GRAVE]
- **Tipo:** OMISSIONE
- **Dove:** §24 (rischi), §25.1 (la decisione su NEXUS), §26 (l'obiezione più forte)
- **Cosa dice il piano:** cinque rischi, ognuno con mitigazione — mai con un piano B. L'unico criterio di fallimento di tutto V1 è per NEXUS (§26: «se quei tre fatti non accadono, NEXUS è fallito e va detto») — ma **senza un termine**: non dice *entro quando* devono accadere, e l'obiezione che cita («lo saprai fra tre mesi») resta senza risposta sul tempo. Per E1, E2, E3, E5-E9: nessun criterio di fallimento, nessuna alternativa.
- **Cosa dice la realtà:** la catena delle dipendenze ha un punto di rottura singolo dichiarato ma non gestito. §25.1: NEXUS «richiede un ADR. Senza, l'ecosistema non può essere creato» — e lì il testo finisce. E4 sono i cinque organi di NEXUS; E5 dipende da N1 («i registri diventano tabella di instradamento (N1)», riga 443); E6 dice «se N4 è fatto, qui si aggancia». **Se Max risponde no, o non risponde, il 60% delle ore del piano (E4+E5+E6) non ha una forma alternativa scritta** — eppure quattro dei cinque organi (emettitore, ledger, code, guardiano) potrebbero vivere come infrastruttura dentro `empire/` anche senza il sedicesimo ecosistema, e V1 non lo dice mai.
- **Perché conta:** quest'Impero ha già pagato il rinvio mascherato: l'orchestrazione ha **due motori canonici in conflitto da 8 giorni** (B-047) proprio perché nessun documento aveva un criterio del tipo «se entro X non è deciso, si fa Y». Un piano che sa solo vincere trasforma ogni intoppo in stallo — e lo stallo, qui, non è teorico: è la voce più anziana del backlog.
- **Cosa proporresti:** tre righe in §24: (a) ogni scaglione ha un tetto di ore = stima alta × 1,5, sforato il quale ci si ferma e si riporta; (b) i gate di NEXUS hanno una data; (c) se l'ADR su NEXUS non arriva entro E3 chiuso, N3+N4 nascono come moduli di `empire/` — stessa sostanza, nessun ecosistema nuovo.
### R-13 — Le sessioni parallele valgono una riga di tabella, mentre un SYNC-CONFLICT.txt vivo sta alla radice del repo  [GRAVE]
- **Tipo:** OMISSIONE
- **Dove:** V1 §24 R4 (l'unica riga: «Le sessioni parallele collidono → blocco ⚠️ COORDINAMENTO prima di ogni scaglione + numeri coniati dallo script»)
- **Cosa dice il piano:** la mitigazione è tutta lì: un blocco di coordinamento per scaglione e i numeri di checkpoint coniati dallo script. Nessuno scaglione dichiara *quali percorsi tocca*, e nessun passo del piano dice di bonificare i conflitti pendenti prima di partire.
- **Cosa dice la realtà:** alla radice del repo c'è **`SYNC-CONFLICT.txt`, 511 byte, ore 21:25 di oggi 6/9** — un commit bloccato dal pre-commit, con l'istruzione finale «Poi cancella questo file» non ancora eseguita. Le collisioni di numerazione sono già **4 in 13 giorni** (lo dice V1 stesso, riga 312) *nonostante* la regola dello script esistesse — cioè la mitigazione proposta da R4 è in parte una regola **già vigente e già ceduta**. E la granularità del rischio non è lo scaglione: E2 riscrive **174 file** e E1 tocca **36 coppie di duplicati** — se l'altra sessione (Gael, o un daemon di sync: i commit «sync(Max): aggiornamento automatico» partono da soli) tocca una di quelle cartelle a metà corsa, il rebase avviene su file riscritti in massa.
- **Perché conta:** un blocco «prima di ogni scaglione» protegge i confini, non le 25-40 ore che stanno in mezzo (stesso difetto di R-11, ma sul git). Il piano conosce la regola giusta per le proprie forze — «due forze che scrivono lo stesso oggetto» è nell'elenco degli hook di §15 — e non applica la stessa regola alle **due sessioni umane** che sono, a oggi, le uniche forze che scrivono davvero.
- **Cosa proporresti:** ogni scaglione dichiara i suoi percorsi in scrittura nel blocco COORDINAMENTO (E2: `company/**`; E1: le 36 coppie, elencate); un passo zero in E1: «radice pulita — nessun SYNC-CONFLICT.txt, nessun rebase pendente»; e il daemon di sync sospeso durante E1-E2.
### R-14 — Il ponte di §13 scarta senza dirlo: 162 esecutori reali su 164 non hanno una scheda, e la pipeline parte solo dalle schede  [FATALE]
- **Tipo:** VIOLAZIONE DI LEGGE (L1, per omissione)
- **Dove:** V1 §13 (il ponte schede→esecutori) e §22 E5/E7
- **Cosa dice il piano:** «La soluzione non è scegliere una delle due popolazioni e buttare l'altra — sarebbe contro L1. È **generare** l'esecutore dalla scheda, tenendo la scheda come fonte di verità» (righe 272-274). Lo schema a riga 277 ha una sola freccia: `company/**/agente.md ──generazione──▶ .claude/agents/<nome>.md`.
- **Cosa dice la realtà:** gli esecutori invocabili sono **164** (contati ora: 129 in `.claude/agents/` + 35 in `~/.claude/agents/` — i numeri di V1 §4.2 tornano) e l'intersezione con le 439 schede è di **2 nomi**. Dunque **162 esecutori — la popolazione che gira davvero, gli unici agenti vivi dell'Impero — non hanno scheda sorgente**. E il piano non gliela costruisce mai: E2 e E7 lavorano solo schede (174 + 204 = 378 riscritture, tutte dentro `company/`), E5 genera direttori e MAXIMILIAN *dalle schede*. Nessuno scaglione contiene il passo inverso: «per ogni esecutore senza scheda, la scheda si genera dall'esecutore».
- **Perché conta:** dichiarare le schede «fonte di verità» quando il 99% degli esecutori una scheda non ce l'ha significa che, a regime, il registro N1 instraderà verso ciò che è *descritto* e ignorerà ciò che *funziona* — l'apex-orchestrator, i formazione-*, gli outreach-*, i 129 nomi che rispondono davvero al comando resteranno fuori dalla Tabella di Instradamento, cioè scartati dall'ordine nuovo esattamente «per omissione». È la stessa dinamica della copia FORGE «10 su 10, perfetta — invisibile allo strumento» (V1 §4.4): il piano l'ha appena denunciata, e §13 la riproduce in grande.
- **Cosa proporresti:** la freccia inversa in §13 — un'ondata E5-bis «adozione»: per ognuno dei 162 esecutori orfani si genera la scheda `company/` dall'esecutore (fonte di verità: chi gira), poi la coppia entra in N1 come tutte le altre.
