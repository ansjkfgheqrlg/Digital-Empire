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

