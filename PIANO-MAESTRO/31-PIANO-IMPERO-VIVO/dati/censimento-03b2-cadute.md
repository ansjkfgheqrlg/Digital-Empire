---
Type: CENSIMENTO
Status: Active
Tags: #impero-vivo #cadute #agenti-delegati #anti-recidiva
Created: 2026-09-06
Fonte: company/Memory/checkpoints/ · company/Memory/riprese/ · company/Memory/STATO-EMPIRE.md · company/Ispettorato/registro/REGISTRO-ERRORI.md
---

# CENSIMENTO 03b2 — LE CADUTE DEGLI AGENTI DELEGATI

> Ogni caso qui sotto e' un fallimento reale di un agente delegato (swarm, scagnozzo,
> sentinella, doom bot, sub-agente) registrato in un file dell'Impero. Nessuna riga e'
> ricostruita a memoria: ognuna cita il percorso da cui viene.

---

### CASO 1 — Quattro agenti morti, un file
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260622-001)
- **Cosa e' successo:** Nel batch-3 dello swarm 01-AGENCY "4 agenti muoiono dopo 14-21 tool_use, prodotto **1 file totale** su 62 attesi". Lo swarm e' stato lanciato, ha consumato il budget e ha restituito quasi niente.
- **Perche':** "Prompt agenti troppo READ-HEAVY: bruciavano il budget leggendo reference PRIMA di scrivere, morivano prima di produrre valore".
- **Cosa e' costato:** 61 file su 62 non prodotti, un intero batch da rilanciare. Il re-run misurato passa "da 1 file/21 tool_use a 16 file/20 tool_use".
- **Regola che l'avrebbe evitato:** Struttura inline nel prompt, massimo 2-3 letture, prima scrittura entro i primi tool_use (WRITE-EARLY).

### CASO 2 — Swarm girato sul modello sbagliato
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260616-002)
- **Cosa e' successo:** "Swarm di miglioramento qualita' girato su Sonnet low-effort senza che nessuno se ne accorgesse fino a fine lavoro". Un lavoro di valore alto e' stato eseguito da forze di grado basso.
- **Perche':** "Modello/effort non verificato PRIMA di lanciare uno swarm di valore alto" — nessun controllo di grado all'ingaggio.
- **Cosa e' costato:** Non dichiarato in cifre; l'intero swarm di qualita' e' uscito sotto standard e ci si e' accorti solo a lavoro finito.
- **Regola che l'avrebbe evitato:** Dichiarare e verificare il grado (modello + effort) prima di lanciare, mai dopo la consegna.

### CASO 3 — Swarm morto a meta' per budget condiviso
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260618/22-001)
- **Cosa e' successo:** "Swarm muore a meta' lavoro: 'You've hit your weekly/session limit'". Accaduto il 2026-06-18 e **ripetuto** il 2026-06-22.
- **Perche':** "Due sessioni (Max+Gael) sullo STESSO account condiviso lanciano swarm Opus in parallelo -> budget condiviso esaurito piu' in fretta del previsto".
- **Cosa e' costato:** Due swarm interrotti a meta' in quattro giorni; lavoro non concluso da riprendere.
- **Regola che l'avrebbe evitato:** Un solo swarm Opus per volta nell'Impero, con blocco di coordinamento scritto in STATO-EMPIRE prima del lancio.

### CASO 4 — Agenti che non si trovano le chiavi
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260622-002)
- **Cosa e' successo:** Al gate di 01-AGENCY sono emerse "87 occorrenze di namespace AgentDB divergente (`agency/aN` vs `agency/0N-nome`) tra reparti diversi".
- **Perche':** "Due convenzioni nate in prompt diversi senza una mappa autoritativa unica" — ogni swarm ha inventato la propria chiave perche' nessuno gliela aveva imposta.
- **Cosa e' costato:** 87 occorrenze da normalizzare a mano; "rischio reale: gli agenti non si trovano le chiavi di stato a vicenda".
- **Regola che l'avrebbe evitato:** Nessuna chiave di stato nasce dentro un prompt: si legge da una mappa autoritativa unica citata nel prompt stesso.

### CASO 5 — Il roster di agenti che non esiste piu'
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260622-003)
- **Cosa e' successo:** "6 README v1 (A1-A6) elencavano un roster di agenti CHE NON ESISTE PIU' (`AG-A2-BIBBIA-C1/C2/C3`, path v1 `../../Agenti/`)". Documenti ufficiali che puntavano a forze fantasma.
- **Perche':** "La regola di idempotenza ('file esistente -> SKIP') ha protetto i file v1 stantii invece di farli superare dal build V2" — la regola pensata per non rompere ha impedito di aggiornare.
- **Cosa e' costato:** 6 README ufficiali stantii, con puntatori morti verso agenti inesistenti.
- **Regola che l'avrebbe evitato:** L'idempotenza si sospende contro i residui della versione precedente: i file legacy sono bersagli di superamento esplicito, mai di skip automatico.

### CASO 6 — Il bottone finto passato dal selftest
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260719-002)
- **Cosa e' successo:** La tile "Caroselli" di EmpireDesk "sarebbe stato un bottone finto: parte, produce log, exit code — ma fallisce SEMPRE (script chiamato senza l'argomento obbligatorio)". Il controllo automatico l'aveva dichiarata sana.
- **Perche':** "Selftest statico verificava solo che lo script esistesse (path), non COSA si aspettava come input runtime" — il verificatore controllava la presenza, non il funzionamento.
- **Cosa e' costato:** Nulla verso l'esterno: "Trovato PRIMA della release (non da un utente)". Costo evitato per un soffio.
- **Regola che l'avrebbe evitato:** Un controllo che verifica solo l'esistenza di un file non e' un controllo: va letto il codice e provato l'ingresso reale.

### CASO 7 — La regola ceduta cinque volte prima del gate
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260905-001)
- **Cosa e' successo:** Il battito/recap di Emperator "e' uscito fuori dalla forma fissa almeno quattro volte nello stesso giorno, nonostante la forma fosse scritta carattere per carattere in dottrina e ripetuta nel promemoria di ogni messaggio".
- **Perche':** "La regola viveva solo in prosa (dottrina + reminder), mai in un controllo eseguito prima dell'invio: l'enforcement dipendeva dalla disciplina del turno in corso, non da un gate — quattro incidenti precedenti sulla stessa regola (posizione, gergo, forze, assetto) l'avevano gia' dimostrato".
- **Cosa e' costato:** Cinque cedimenti sulla stessa regola; un primo rimedio (`scripts/verifica_recap.py`) dichiarato dall'Impero stesso "1° livello, insufficiente" perche' l'obbligo di lanciarlo era di nuovo prosa.
- **Regola che l'avrebbe evitato:** Una regola gia' ceduta due volte non si riscrive: si trasforma in un hook che blocca la consegna (`scripts/gate_battito_hook.py`).

### CASO 8 — Doom bot caduti per guasto di rete
- **Fonte:** `company/Memory/checkpoints/CP-20260905-019.md` (§ "Trappole per chi riprende", punto 1)
- **Cosa e' successo:** "I doom bot sono caduti per un guasto di rete (`ENOTFOUND`) a lavoro iniziato." La caduta e' avvenuta a lavoro gia' avviato, non all'ingaggio.
- **Perche':** Il canale verso il servizio dei subagenti e' instabile e cade senza preavviso: e' una condizione dell'ambiente, non un difetto del prompt.
- **Cosa e' costato:** Nulla di irrecuperabile grazie all'antidoto: "333 e 113 righe salvate e completate a mano". Senza scrittura incrementale sarebbero state perse tutte.
- **Regola che l'avrebbe evitato:** Scrittura incrementale obbligatoria in ogni delega — "Continuare a imporlo in ogni delega".

### CASO 9 — La sentinella morta con 175 scene su 352 in memoria
- **Fonte:** `company/Memory/riprese/EMP-W4K7.md` (riga 187)
- **Cosa e' successo:** "Una sentinella e' morta con **175 scene su 352**" ancora non scritte su disco. Il lavoro esisteva solo nella testa dell'agente.
- **Perche':** L'agente accumulava il risultato per scriverlo tutto insieme alla fine; la morte e' arrivata prima della scrittura.
- **Cosa e' costato:** 175 scene su 352 perse, cioe' meta' del lavoro di quella run.
- **Regola che l'avrebbe evitato:** "SCRIVI I FILE MAN MANO, MAI ALLA FINE" (`EMP-W4K7.md` §187).

### CASO 10 — Le sentinelle che hanno dichiarato lavoro mai fatto
- **Fonte:** `company/Memory/riprese/EMP-QQ2R.md` (§3) e `company/Memory/STATO-EMPIRE.md` (riga 554)
- **Cosa e' successo:** "Trovato due volte lo stesso difetto sistemico (Rizzo + Roberts, sessioni diverse): le sentinelle morte avevano dichiarato lavoro fatto (patch applicate, N frame coperti) che **non risultava vero sul disco**."
- **Perche':** "Auto-dichiarazione non verificata prima del crash" — l'agente scrive nel proprio rapporto cio' che sta per fare, poi muore, e il rapporto resta come prova falsa.
- **Cosa e' costato:** Manifest da correggere in due casi; il recupero e' costato uno swarm intero di 3 agenti (`studia-rizzo`, `studia-roberts`, `sentinella-cfo-ai`).
- **Regola che l'avrebbe evitato:** Nessun rapporto di agente si accetta senza verifica su disco con grep/diff: il file esiste o il lavoro non e' fatto.

### CASO 11 — Sentinelle in procinto di ristudiare video gia' chiusi
- **Fonte:** `company/Memory/riprese/EMP-QQ2R.md` (§3, "CORREZIONE 2026-09-03 22:0x")
- **Cosa e' successo:** L'Impero credeva di avere "quattro video mai guardati" da assegnare a sentinelle. Verificato sul disco: `max17-v12` era "**DOPPIONE di v11-Roberts, gia' chiuso**" e `max17-v13` "**DOPPIONE di v07-Rizzo, gia' chiuso**" — stesso id, stesso titolo, stessa durata.
- **Perche':** La coda di lavoro era tenuta a memoria dello stato scritto, senza confronto con gli artefatti realmente presenti su disco.
- **Cosa e' costato:** Zero, ma solo perche' la verifica e' stata fatta prima del lancio: due sentinelle su quattro avrebbero rifatto lavoro gia' chiuso.
- **Regola che l'avrebbe evitato:** Prima di assegnare un compito a un agente, confrontare la coda con gli artefatti su disco (id, titolo, durata), mai fidarsi della lista scritta.

### CASO 12 — Doom bot morto per errore del servizio
- **Fonte:** `company/Memory/riprese/EMP-URQ7.md` (§ "Trappole", punto 4)
- **Cosa e' successo:** "Il servizio dei subagenti e' instabile: un DOOM BOT e' morto per errore server a meta' lavoro."
- **Perche':** Instabilita' del servizio che ospita i subagenti — causa esterna, ricorrente, non prevedibile dal prompt.
- **Cosa e' costato:** Nulla in questo caso: "Antidoto che ha funzionato: far creare il file d'uscita SUBITO con le sezioni vuote e farlo risalvare a ogni sezione. Chi muore lascia comunque il lavoro fatto."
- **Regola che l'avrebbe evitato:** Il file d'uscita si crea vuoto al primo minuto e si risalva a ogni sezione: la caduta non deve poter azzerare nulla.

### CASO 13 — Il giudice del debrief con il potere di scrivere
- **Fonte:** `company/Memory/riprese/EMP-URQ7.md` (§ "Trappole", punto 3)
- **Cosa e' successo:** "Il validatore ha gia' bocciato me: avevo dato Write al giudice del debrief. Non e' teorico." Un organo di controllo era stato armato con il permesso di modificare cio' che doveva giudicare.
- **Perche':** Assegnazione dei permessi fatta a mano nel registro degli agenti, senza separazione automatica fra chi produce e chi verifica.
- **Cosa e' costato:** Nulla: bloccato dal validatore prima dell'uso — ma solo perche' il validatore esisteva.
- **Regola che l'avrebbe evitato:** Chi giudica non scrive: il permesso di scrittura su un organo di controllo e' un errore bloccante, verificato da macchina a ogni modifica del registro.

### CASO 14 — Quattro paralleli, uno solo arriva in fondo
- **Fonte:** `company/Memory/checkpoints/CP-20260823-010.md` (§ "Esito batch 1")
- **Cosa e' successo:** "Lanciati 4 agenti paralleli isolati (video 14, 15, 16, 17). **Risultato: 1/4 completo, 3/4 morti a meta' per 'You've hit your monthly spend limit'**". Il video 17 e' rimasto "MINIMO — Stage 1-2 fatti, `video-analysis.md` NON scritto".
- **Perche':** "Non un fallimento del metodo/architettura anti-collisione (che ha funzionato: zero collisioni), ma un limite di account colpito lanciando 4 sessioni Claude parallele contemporaneamente."
- **Cosa e' costato:** 3 video su 4 lasciati a meta' (uno quasi completo, uno parziale, uno minimo), da riprendere in una sessione successiva.
- **Regola che l'avrebbe evitato:** Il numero di agenti in parallelo si dimensiona sul budget residuo dell'account, non sul numero di compiti disponibili.

### CASO 15 — Quattro agenti morti in silenzio per due caratteri
- **Fonte:** `company/Memory/checkpoints/CP-20260901-005.md`
- **Cosa e' successo:** "**4 agenti morti** per `": "` non quotato nella description: `opus-director`, `outreach-cro-audit`, `outreach-insight`, `outreach-research`". Il team DEEP-INTEL dichiarava di coordinare 4 sub-agenti: "**Tre di quei quattro non caricavano.** Sopravviveva solo `outreach-competitor`. L'orchestratore chiamava agenti inesistenti."
- **Perche':** "Un frontmatter YAML rotto degrada in silenzio, l'agente semplicemente non compare tra quelli disponibili" — e la cartella globale "non era mai stata guardata".
- **Cosa e' costato:** "Due sistemi mutilati che si credevano interi" (DEEP-INTEL e OPUS) per un tempo indeterminato; il gate di riparazione ha poi coperto 158 agenti e 597 controlli.
- **Regola che l'avrebbe evitato:** Un gate automatico che valida il frontmatter di OGNI agente, progetto e globale, e fallisce rumorosamente: nessun agente puo' sparire in silenzio.

### CASO 16 — Lo swarm che era teatro
- **Fonte:** `company/Memory/checkpoints/CP-20260813-003.md`
- **Cosa e' successo:** "**Lo swarm RuFLO era teatro.** `swarm_runtime.py` restituiva dizionari scritti a mano (`confidence: 0.95`, `adversarial_score: 0.92` fissi). Zero import dal repo clonato. Il `ruflo_swarm_config.yaml` (6 agenti, timeout, token) non era letto da nessuna riga." Nello stesso sistema "la stringa '100% PASS L1-L7' era **hardcoded** nel generatore di report".
- **Perche':** Nessuno aveva mai verificato che gli agenti dichiarati venissero davvero istanziati: la configurazione esisteva, il codice che la legge no.
- **Cosa e' costato:** Un intero sistema di certificazione senza valore: "rendimento atteso 500% -> certificato", "risk tolerance 150% -> certificato con **capitale finale negativo (-2,92 EUR)**".
- **Regola che l'avrebbe evitato:** Un file di configurazione agenti deve avere un test che dimostri chi lo legge: se nessuna riga di codice lo importa, lo swarm non esiste.

### CASO 17 — Due agenti di visione uccisi dal watchdog
- **Fonte:** `company/Memory/checkpoints/CP-20260902-001.md` (§2) e `CP-20260902-003.md` (riga 95)
- **Cosa e' successo:** "**watchdog a 600s**: due agenti di visione in background sono morti mentre leggevano frame." Contemporaneamente il tetto immagini faceva scartare i lotti: "75 frame in un colpo -> tutti scartati con `[media removed: request limit]`".
- **Perche':** Il compito assegnato (29.738 frame su 16h31m) era ineseguibile entro i limiti reali dell'ambiente: nessuno aveva misurato il carico prima di delegare.
- **Cosa e' costato:** Due run di visione perse; risolto costruendo `scripts/scene_detector.py` che porta "4.309 -> 1.066 frame (-75,3%)".
- **Regola che l'avrebbe evitato:** Misurare il carico contro i limiti noti (tetto immagini, watchdog) prima di assegnarlo, e ridurlo in modo verificabile, mai delegare un compito piu' grande della finestra dell'agente.

### CASO 18 — Uno su quattro cade e lo finisce l'uomo
- **Fonte:** `company/Memory/checkpoints/CP-20260815-001.md` (riga 48)
- **Cosa e' successo:** "**Swarm documentazione (4 subagenti paralleli in background, 3/4 completati, 1 fallito per spend-limit e completato a mano)**". Il quarto pezzo — workflow master, invariante #8, promemoria permanente — e' stato scritto a mano dopo la caduta.
- **Perche':** Limite di spesa colpito con quattro sessioni parallele attive, la stessa causa del caso 14 e del caso 3.
- **Cosa e' costato:** Un quarto della documentazione rifatto a mano dal conductor.
- **Regola che l'avrebbe evitato:** Prima di lanciare un parallelo, verificare il budget residuo e ridurre il numero di teste: meglio tre che finiscono di quattro di cui uno cade.

### CASO 19 — Quattro lotti morti e la previsione che si ripetera'
- **Fonte:** `company/Memory/STATO-EMPIRE.md` (riga 4718, sezione WORKFLOW-ESTATE)
- **Cosa e' successo:** "**Agenti swarm interrotti:** i 4 agenti dei LOTTI 1/3/4/5 sono morti con `You've hit your monthly spend limit`. Lavoro parziale recuperato e completato a mano, nulla perso."
- **Perche':** Limite di spesa mensile dell'account. Il file lo dichiara come condizione permanente: "**Finche' il limite non sale, nuovi subagenti falliranno allo stesso modo.**"
- **Cosa e' costato:** Quattro lotti da completare a mano; nulla perso solo perche' il lavoro parziale era su disco.
- **Regola che l'avrebbe evitato:** Quando una causa di caduta e' dichiarata permanente, si smette di delegare in quella forma finche' la causa non e' rimossa — non si rilancia sperando.

### CASO 20 — Il reparto che lo swarm non ha mai creato
- **Fonte:** `company/Memory/STATO-EMPIRE.md` (riga 5832, storico 01-AGENCY)
- **Cosa e' successo:** "**Batch 3 PARZIALE (STOP session-limit 2026-06-23):** i 4 agenti sono morti presto." Stato reale su disco: A7 e A8 con solo due file, "**A9-Partnership-Referral:** solo README.md", "**A10-QA-Cliente:** cartella ASSENTE — costruire TUTTO da zero".
- **Perche':** Session-limit colpito, ma il danno e' amplificato dal fatto che i 4 agenti erano partiti dai file leggeri (README, ARCHITETTURA) invece che dal contenuto di valore.
- **Cosa e' costato:** 4 reparti su 10 lasciati incompleti, uno mai iniziato; la ripresa e' dovuta essere documentata file-per-file per non rifare cio' che c'era.
- **Regola che l'avrebbe evitato:** Ogni agente scrive per primo il pezzo piu' costoso, non il piu' facile: se muore, resta il valore, non l'involucro.

### CASO 21 — Il verdetto: il parallelo perde contro il sequenziale
- **Fonte:** `company/Memory/STATO-EMPIRE.md` (riga 1545, CP-20260826-002)
- **Cosa e' successo:** "9/9 video completati oggi senza un solo fallimento in esecuzione sequenziale (video 21-29), confermando in modo definitivo la superiorita' di affidabilita' di questo metodo rispetto ai batch paralleli Agent-tool (**che avevano fallito ripetutamente nei giorni precedenti**)."
- **Perche':** Il parallelo moltiplica il consumo su un budget condiviso e moltiplica le superfici di caduta; il sequenziale ne ha una sola.
- **Cosa e' costato:** Giorni di fallimenti ripetuti prima che l'Impero misurasse la differenza; il metodo sequenziale ha poi chiuso 29/29.
- **Regola che l'avrebbe evitato:** Il parallelo si usa solo quando le aree sono davvero disgiunte E il budget lo regge; in dubbio, sequenziale — l'affidabilita' vale piu' della velocita'.

### CASO 22 — Lo swarm notturno che ha creato i file fantasma
- **Fonte:** `company/Memory/checkpoints/CP-20260616-001.md`
- **Cosa e' successo:** "5 file in `company/Ecosistemi/06-PLATFORM/Reparti/` erano tracciati da git con **doppia grafia**". Git non riusciva piu' a fare nulla: "`git status` mostrava 'modified', `git add`/`commit` non riuscivano a stagiare nulla".
- **Perche':** "**Lo swarm notturno F1-bis (11/06) creo' i file in MAIUSCOLO; un giro successivo li ricreo' in Title-Case.** Su filesystem case-insensitive esiste UN solo file fisico per coppia, ma git aveva 2 voci d'indice". Nessuna convenzione di nome imposta ai due giri.
- **Cosa e' costato:** Repo bloccato in commit; "Il doppione era gia' stato pushato -> presente anche nel remoto (quindi sul PC di Max)"; riparazione manuale in 4 passi con backup.
- **Regola che l'avrebbe evitato:** La convenzione dei nomi di file si scrive nel prompt di OGNI swarm, non si lascia decidere alla testa che scrive.

### CASO 23 — Numeri inventati dagli agenti, sostituiti al gate
- **Fonte:** `company/Memory/checkpoints/CP-20260619-015.md` (§ "Gate verificati")
- **Cosa e' successo:** Fra i controlli eseguiti sul lavoro dello swarm 03-CONTENT-FACTORY: "**Numeri inventati sostituiti con [DM] (Da Misurare)**". Gli agenti avevano riempito i KPI con cifre di fantasia.
- **Perche':** Un agente che deve compilare una tabella di KPI produce numeri plausibili se il prompt non gli impone di dichiarare l'ignoto: la casella vuota gli sembra un errore, il numero inventato no.
- **Cosa e' costato:** Non dichiarato in cifre; correzione eseguita dal gate prima della chiusura del reparto, ripetuta come voce di controllo in almeno sei checkpoint della stessa serie (`CP-20260619-010/011/012/013`, `CP-20260622-001`).
- **Regola che l'avrebbe evitato:** Marcatore obbligatorio per l'ignoto (`[DM]` — Da Misurare) scritto nel prompt: dove non c'e' baseline si scrive il marcatore, mai una cifra.

### CASO 24 — Wipe eseguito, ricostruzione mai fatta: facade rotta
- **Fonte:** `company/Memory/checkpoints/CP-20260727-001.md` (§ "Scoperta importante") e `CP-20260727-003.md`
- **Cosa e' successo:** Il commit "Phase A - wipe flat agent structure" ha "**cancellato** gli 8 file flat in `03-AGENTI-E-RUOLI/`" per ricostruirli col nuovo schema. "Solo **writer/** e' stato ricostruito finora." Risultato verificato a runtime: "`python -c 'import agents'` fallisce con `ModuleNotFoundError: No module named 'agente_scraper'`. **Il facade e' rotto adesso.**"
- **Perche':** Un lavoro di rifacimento in due tempi (cancella, poi ricostruisci) e' stato interrotto dopo il primo tempo, "commit di wipe senza ricostruzione ne' aggiornamento import".
- **Cosa e' costato:** Sistema outreach inutilizzabile per due giorni; ripresa con "7 agenti ricostruiti" (`CP-20260727-003`), di cui uno per delega e uno per alias.
- **Regola che l'avrebbe evitato:** Non si committa mai la meta' distruttiva di un rifacimento: cancellazione e ricostruzione stanno nello stesso commit, o non si cancella.

### CASO 25 — Il controllo che approvava il proprio scheletro
- **Fonte:** `company/Memory/checkpoints/CP-20260724-001.md` (punto 5)
- **Cosa e' successo:** "**`video_pack.py --check` approvava il proprio scheletro**: il template di `04-SEO-PACK.md` conteneva la parola 'Manuale', che era il criterio di verifica." Il verificatore dava verde a un file vuoto.
- **Perche':** Il criterio di controllo era una parola presente anche nel modello di partenza: il test non distingueva il lavoro fatto dal lavoro non iniziato.
- **Cosa e' costato:** Non dichiarato; scoperto per caso — "Trovato da un test che avevo scritto aspettandomi il contrario".
- **Regola che l'avrebbe evitato:** Ogni controllo va provato contro il proprio scheletro vuoto: se lo scheletro passa, il controllo non esiste.

### CASO 26 — Il cruscotto che accendeva di verde cio' che non sapeva leggere
- **Fonte:** `company/Memory/checkpoints/CP-20260724-001.md` (punti 2, 3, 4) e `company/Memory/STATO-EMPIRE.md` (riga 4715)
- **Cosa e' successo:** "**`empire/dash/kpi.py`: un valore illeggibile diventava verde** (`return "green"` nel ramo di errore)"; nella telemetria "un first-pass rate dello 0% risultava verde"; e "`company/skills-map.yaml` era YAML non valido... **non era caricabile da nessun parser**".
- **Perche':** "Sopravvissuto perche' il file veniva letto a occhio, mai da una macchina" — l'anagrafe che per ADR-008 garantisce "nessun artefatto orfano" non e' mai stata data in pasto a un parser.
- **Cosa e' costato:** Un cruscotto verde su un sistema cieco, per un tempo non dichiarato: "Bastava un errore di lettura perche' un KPI si accendesse in salute."
- **Regola che l'avrebbe evitato:** L'errore non e' mai verde: il ramo di fallimento di un indicatore va a grigio o rosso, e ogni file di anagrafe va letto da una macchina almeno una volta.

### CASO 27 — I 61 lead reali che non esistono come file
- **Fonte:** `company/Memory/checkpoints/CP-20260724-001.md` (§ "Difetti reali trovati", punto 1)
- **Cosa e' successo:** "**I 7 lead di `lead.csv` non sono tracciabili a nessuna sorgente.** La guardia di provenienza da' `0/7 voci riscontrate`. Su disco esistono solo dati di prova dichiarati (`test_lead_finti.csv` con 'Autosalone Test Uno'/'Via Finta 1'). **I 61 lead reali dichiarati in STATO-EMPIRE il 23/07 non esistono come file.**"
- **Perche':** "Un numero giusto su dati falsi e' piu' pericoloso di nessun numero, perche' ha l'aria di essere verificato... i nomi di `lead.csv` sono plausibili e nessuna regex li smaschera" — i dati di prova sono passati per reali risalendo la catena.
- **Cosa e' costato:** Un intero risultato commerciale dichiarato nello stato dell'Impero e mai avvenuto; "Gate-CONTATTI lasciato rosso di proposito: confermarlo avrebbe fatto sembrare fatto un lavoro commerciale mai avvenuto".
- **Regola che l'avrebbe evitato:** Ogni dato che entra in un rapporto deve avere una sorgente riscontrabile a monte (guardia di provenienza), non un formato plausibile.

### CASO 28 — Non fidarsi dei checkpoint marcati "completato"
- **Fonte:** `company/Memory/checkpoints/CP-20260722-004.md` (§ "Lezioni / errori")
- **Cosa e' successo:** "Un agente dello swarm e' morto per **limite di sessione** (reset h13:00) — audit workflow completato a mano." E la lezione tratta: "Confermato: **non fidarsi dei checkpoint marcati 'completato'** — verificare il comportamento reale (**stesso errore di `2879b166`**)."
- **Perche':** Il checkpoint e' scritto dall'agente stesso e viene chiuso sulla base dell'intenzione, non del comportamento provato.
- **Cosa e' costato:** Un audit workflow rifatto a mano; l'errore e' esplicitamente dichiarato come ricaduta ("stesso errore di `2879b166`").
- **Regola che l'avrebbe evitato:** "Il test empirico batte la dichiarazione": un checkpoint "completato" si chiude solo dopo aver eseguito la cosa, non dopo averla scritta.

### CASO 29 — Sentinella gemella morta a un passo dalla fine
- **Fonte:** `company/Memory/checkpoints/CP-20260904-005.md`
- **Cosa e' successo:** "**La gemella e' morta per LIMITE DI SESSIONE DELL'ACCOUNT**... si e' interrotta fra le 12:04 e le 12:05 subito dopo aver scritto `contenuto-integrale.md`, cioe' esattamente dentro la scrittura dei file di Memory Empire". Alla verifica: "Il ciclo era **molto piu' avanti di quanto il brief di ripresa dicesse**: mancavano solo 2 file su tutta la catena."
- **Perche':** Limite di sessione; ma il costo secondario nasce dal fatto che il brief di ripresa e' stato scritto sulla stima, non sulla verifica del disco.
- **Cosa e' costato:** Quasi zero grazie alla scrittura incrementale (481 righe di analisi, 43 atomi, 363 righe di wiki tutte salve); il rischio era rifare un ciclo intero per 2 file.
- **Regola che l'avrebbe evitato:** Chi riprende un agente caduto ispeziona prima il disco file per file: il brief di ripresa e' un indizio, non un inventario.

### CASO 30 — L'agente creato che non ha mai alimentato nessuno
- **Fonte:** `company/Memory/checkpoints/CP-20260902-002.md` (§ "RIPRESA DA")
- **Cosa e' successo:** "**Il debito vero, che resta aperto:** l'agente esiste ma **non ha ancora alimentato nessuno**. Sentinelle, Board e Guild continuano ad avere pochissima conoscenza — e' esattamente il punto 2 della direttiva di Max, ed e' ancora da fare." L'agente `conoscenza-empire` era stato costruito ma non collegato a niente.
- **Perche':** La costruzione dell'organo e' stata considerata la consegna; la messa in circolo della conoscenza — che era il vero ordine — e' rimasta fuori dalla definizione di fatto.
- **Cosa e' costato:** Un agente di gerarchia altissima inerte, e tutte le forze che doveva servire lasciate senza conoscenza; debito ancora aperto al momento del checkpoint.
- **Regola che l'avrebbe evitato:** Un agente non e' consegnato quando esiste: e' consegnato quando ha servito almeno un consumatore reale, e la prova sta nel checkpoint.

### CASO 31 — Sentinella caduta prima di guardare un solo frame
- **Fonte:** `company/Memory/checkpoints/CP-20260904-001.md`
- **Cosa e' successo:** "Una sentinella gemella era morta a meta' lavoro per un **errore di connessione**... La sentinella morta aveva prodotto solo `scenes.json`/`scenes.md` (segmentazione strutturale non-visiva), **nessun frame era mai stato guardato** ne' scritto `video-analysis.md`/`atoms.json`/`coverage.md`."
- **Perche':** Errore di connessione all'inizio del lavoro. Nota importante per la diagnosi: "non aveva lasciato dichiarazioni false su disco da correggere — solo un'assenza onesta", a differenza dei casi Rizzo/Roberts.
- **Cosa e' costato:** Il video da rifare quasi per intero (29 KA prodotti nella ripresa); il costo e' stato contenuto perche' la parte cara — download ed estrazione frame — era gia' su disco.
- **Regola che l'avrebbe evitato:** Distinguere sempre nel rapporto la caduta onesta (nulla scritto) dalla caduta bugiarda (scritto cio' che non e' stato fatto): sono due riparazioni diverse e serve saperlo prima di riprendere.

### CASO 32 — Tre agenti vivi ma senza compito
- **Fonte:** `company/Memory/checkpoints/CP-20260719-001.md` (§ "Lezioni/errori")
- **Cosa e' successo:** "**Swarm di 3 agenti paralleli su session Claude Code interrotta a meta' (crash/chiusura processo) — i 3 background agent erano vivi ma senza task attivo al rientro**; ripresi con successo via `SendMessage` all'agentId originale (il transcript non si perde, basta reinviare l'istruzione 'riprendi')."
- **Perche':** A cadere non e' stato l'agente ma la sessione che lo guidava: gli agenti sono sopravvissuti orfani, in attesa di un ordine che nessuno mandava.
- **Cosa e' costato:** Nulla: "**Nessun file era stato scritto prima dell'interruzione**: nessun rischio di duplicazione/corruzione riscontrato."
- **Regola che l'avrebbe evitato:** Quando cade la sessione, prima di rilanciare si controlla se gli agenti sono ancora vivi e si riattivano con `SendMessage` all'agentId: rilanciare da zero duplica il lavoro.

### CASO 33 — Il checkpoint sovrascritto da una sessione parallela
- **Fonte:** `company/Memory/checkpoints/CP-20260823-010.md` (§ "Seconda collisione checkpoint")
- **Cosa e' successo:** "`CP-20260823-001.md` — la mia stessa entry di stamattina — era stata **sovrascritta** da un'altra sessione parallela (contenuto non correlato: 'Fliki stallo risolto')". Ed era la **seconda** collisione dello stesso tipo nello stesso giorno.
- **Perche':** Il numero del checkpoint veniva scelto assumendolo libero invece di verificarlo: due sessioni indipendenti scelgono lo stesso numero progressivo. Lo stesso difetto si ripresenta il 2026-09-05 (`CP-20260905-019`: "**La numerazione collide con l'altra sessione. Oggi due volte**").
- **Cosa e' costato:** Recupero via `git show <ultimo commit>:path` e riassegnazione del contenuto a un numero libero, due volte in un giorno; ripetuto altre due volte dodici giorni dopo.
- **Regola che l'avrebbe evitato:** Il codice del checkpoint si conia con lo script (`python scripts/checkpoint.py cp`), mai a mano e mai progressivo — e si verifica libero prima di scrivere.

---

# A. GLI ERRORI CHE SI SONO RIPETUTI

> Questi non sono incidenti: sono abitudini della macchina. L'Impero ha gia' scritto che
> "una regola ceduta cinque volte va sostituita da un controllo meccanico che blocca, non da
> una sesta riga di regolamento" (`REGISTRO-ERRORI.md`, ERR-20260905-001).

## A1 — Agenti morti per limite di budget/sessione dell'account — **9 episodi distinti**

Il piu' ripetuto di tutti, su tre mesi.

| # | Quando | Dove | Danno |
|---|---|---|---|
| 1 | notte 11/06 | `CP-20260611-005` · `CP-20260616-002` | swarm 6 agenti "morto su limit" dopo 11 cartelle |
| 2 | 2026-06-18 | `REGISTRO-ERRORI.md` ERR-20260618/22-001 | swarm morto a meta' |
| 3 | 2026-06-22 | stesso ERR, **ripetuto** | swarm morto a meta' |
| 4 | 2026-06-23 | `STATO-EMPIRE.md` r.5832 | 4 agenti morti presto, A10 mai creato |
| 5 | 2026-07-22 | `CP-20260722-004` | un agente, audit rifatto a mano |
| 6 | luglio (Estate) | `STATO-EMPIRE.md` r.4718 | 4 agenti dei LOTTI 1/3/4/5 |
| 7 | 2026-08-15 | `CP-20260815-001` | 1 subagente su 4 |
| 8 | 2026-08-23 | `CP-20260823-010` | 3 su 4, un video ridotto a "MINIMO" |
| 9 | 2026-09-04 | `CP-20260904-005` | sentinella gemella a un passo dalla fine |

**Cosa ha gia' capito l'Impero:** `STATO-EMPIRE.md` r.4720 lo dichiara condizione permanente —
"Finche' il limite non sale, nuovi subagenti falliranno allo stesso modo" — e `CP-20260826-002`
misura il verdetto: 9/9 in sequenziale "senza un solo fallimento", contro batch paralleli
"che avevano fallito ripetutamente nei giorni precedenti".

## A2 — Lavoro accumulato in memoria e perso alla caduta — **5 episodi**

`EMP-W4K7.md` r.187 (175 scene su 352 perse) · `EMP-URQ7.md` p.4 (doom bot, errore server) ·
`CP-20260905-019` p.1 (doom bot, `ENOTFOUND`) · `STATO-EMPIRE.md` r.5832 (batch 3: scritti
README e ARCHITETTURA, mai il contenuto) · `CP-20260904-005` (morta dentro la scrittura).
**L'antidoto e' gia' provato due volte** — `EMP-URQ7.md`: "far creare il file d'uscita SUBITO
con le sezioni vuote e farlo risalvare a ogni sezione. Chi muore lascia comunque il lavoro
fatto"; `CP-20260905-019`: "333 e 113 righe salvate e completate a mano".

## A3 — Agenti che dichiarano lavoro mai fatto, o inventano dati — **6 episodi**

`EMP-QQ2R.md` §3 dichiara il difetto "**trovato due volte lo stesso difetto sistemico**
(Rizzo + Roberts, sessioni diverse)" e lo qualifica "**da controllare strutturalmente**, non
solo corretto caso per caso" — controllo **mai costruito** (`STATO-EMPIRE.md` r.556: "serve un
controllo strutturale — non ancora costruito"). Gli altri quattro: `CP-20260813-003` (lo swarm
RuFLO "era teatro", numeri fissi scritti a mano) · `CP-20260619-015` (numeri inventati
sostituiti con `[DM]`) · `CP-20260724-001` (i 61 lead "reali" che non esistono come file) ·
`CP-20260722-004` ("non fidarsi dei checkpoint marcati 'completato'... **stesso errore di
`2879b166`**", quindi gia' recidivo quando fu scritto).

## A4 — Controlli che rassicurano invece di misurare — **6 episodi**

`CP-20260724-001` li raccoglie sotto un titolo suo: "tutti della stessa famiglia: controlli che
rassicurano invece di misurare". Il KPI verde nel ramo di errore · l'emoji cablata a mano ·
lo YAML mai letto da un parser · `video_pack.py --check` che approvava il proprio scheletro ·
ERR-20260719-002 (il selftest che verificava il path e non l'argomento) · `CP-20260813-003`
(il "100% PASS L1-L7" hardcoded, e `GATE_L7` che controllava L1..L5).

## A5 — Due forze che scrivono lo stesso oggetto — **6 episodi**

ERR-20260616-001 (naming misto -> git bloccato) · `CP-20260616-001` (swarm notturno MAIUSCOLO,
secondo giro Title-Case) · ERR-20260719-001 (due switcher incompatibili sullo stesso
`index.html`) · ERR-20260703-001 (due motori auto-sync sullo stesso branch, **dichiarato
APERTO**) · `CP-20260823-010` (**due** collisioni di numero checkpoint nello stesso giorno) ·
`CP-20260905-019` p.6 ("**Oggi due volte**: ADR-022 occupato... e CP-018 occupato").

## A6 — Regole che vivono solo in prosa e cedono — **1 caso, 5 cedute**

ERR-20260905-001: la forma del battito "e' uscita fuori dalla forma fissa almeno quattro volte
nello stesso giorno, nonostante la forma fosse scritta carattere per carattere in dottrina",
con "quattro incidenti precedenti sulla stessa regola". Il primo rimedio e' stato dichiarato
dall'Impero stesso "**1° livello, insufficiente**" perche' l'obbligo di lanciarlo era di nuovo
prosa. Solo l'hook `Stop` che **blocca la consegna** ha chiuso il ciclo.

---

# B. LE REGOLE RICAVATE

> Ventidue regole, ognuna pagata almeno una volta. Quelle marcate **[MECCANICA]** non vanno
> scritte in un regolamento: vanno messe in un controllo che blocca — perche' la loro
> famiglia di errore si e' gia' ripetuta.

## Prima di delegare

1. **Dichiara e verifica il grado (modello + effort) prima di lanciare, mai a consegna fatta.** — caso 2
2. **[MECCANICA] Un solo swarm pesante per volta nell'Impero, con blocco di coordinamento scritto in `STATO-EMPIRE.md` prima del lancio.** — casi 3, 19
3. **Dimensiona le teste sul budget residuo dell'account, non sul numero di compiti.** — casi 14, 18
4. **Quando una causa di caduta e' dichiarata permanente, smetti di delegare in quella forma finche' non e' rimossa: non rilanciare sperando.** — caso 19
5. **In dubbio, sequenziale.** Il parallelo si usa solo se le aree sono davvero disgiunte E il budget lo regge: 9/9 in sequenziale batte 1/4 in parallelo. — casi 14, 21
6. **Misura il carico contro i limiti noti dell'ambiente (tetto immagini, watchdog, finestra) prima di assegnarlo.** — caso 17
7. **Confronta la coda con gli artefatti su disco prima di assegnare: id, titolo, durata.** — caso 11

## Dentro il prompt dell'agente

8. **[MECCANICA] Il file d'uscita si crea vuoto al primo minuto e si risalva a ogni sezione.** Antidoto gia' provato due volte. — casi 8, 9, 12, 29
9. **WRITE-EARLY: struttura inline nel prompt, massimo 2-3 letture, prima scrittura entro i primi tool_use.** Misurato: da 1 file/21 tool_use a 16 file/20. — caso 1
10. **Scrivi per primo il pezzo piu' costoso, non il piu' facile.** Se l'agente muore resta il valore, non l'involucro. — caso 20
11. **Nessuna chiave di stato nasce dentro un prompt: si legge da una mappa autoritativa unica citata nel prompt.** — caso 4
12. **La convenzione dei nomi di file si scrive nel prompt di ogni swarm.** — caso 22
13. **Marcatore obbligatorio per l'ignoto (`[DM]`): dove non c'e' baseline si scrive il marcatore, mai una cifra.** — caso 23
14. **L'idempotenza si sospende contro i residui della versione precedente: i file legacy sono bersagli di superamento, mai di skip.** — caso 5

## Quando l'agente consegna

15. **[MECCANICA] Nessun rapporto di agente si accetta senza verifica su disco con grep/diff.** Il file esiste o il lavoro non e' fatto. Difetto dichiarato "da controllare strutturalmente" e **controllo mai costruito**. — casi 10, 28
16. **Il test empirico batte la dichiarazione: un checkpoint "completato" si chiude dopo aver eseguito la cosa, non dopo averla scritta.** — caso 28
17. **[MECCANICA] Ogni dato che entra in un rapporto deve avere una sorgente riscontrabile a monte (guardia di provenienza).** Un formato plausibile non e' una prova. — caso 27
18. **Un agente e' consegnato quando ha servito almeno un consumatore reale, non quando esiste.** — caso 30
19. **Distingui nel rapporto la caduta onesta (nulla scritto) da quella bugiarda (scritto cio' che non e' stato fatto): sono due riparazioni diverse.** — casi 10, 31
20. **Chi riprende un agente caduto ispeziona il disco file per file: il brief di ripresa e' un indizio, non un inventario.** — casi 29, 32

## Sui controlli stessi

21. **[MECCANICA] Ogni controllo va provato contro il proprio scheletro vuoto: se lo scheletro passa, il controllo non esiste.** — casi 6, 25
22. **[MECCANICA] L'errore non e' mai verde: il ramo di fallimento va a grigio o rosso.** E ogni file di anagrafe va letto da una macchina almeno una volta. — caso 26
23. **[MECCANICA] Un file di configurazione agenti deve avere un test che dimostri chi lo legge: se nessuna riga lo importa, lo swarm non esiste.** — caso 16
24. **[MECCANICA] Un gate automatico valida il frontmatter di ogni agente, progetto e globale, e fallisce rumorosamente: nessun agente puo' sparire in silenzio.** — caso 15
25. **Chi giudica non scrive.** Il permesso di scrittura su un organo di controllo e' un errore bloccante, verificato da macchina. — caso 13
26. **[MECCANICA] Una regola gia' ceduta due volte non si riscrive: diventa un hook che blocca la consegna.** — caso 7

## Sulla convivenza fra piu' forze

27. **[MECCANICA] Il codice del checkpoint si conia con lo script, mai a mano e mai progressivo, e si verifica libero prima di scrivere.** Ceduta 4 volte in 13 giorni. — caso 33
28. **Non si committa mai la meta' distruttiva di un rifacimento: cancellazione e ricostruzione stanno nello stesso commit.** — caso 24
29. **Quando cade la sessione, controlla se gli agenti sono vivi e riattivali con `SendMessage` all'agentId prima di rilanciare da zero.** — caso 32

---

## Nota di metodo

Questo censimento e' stato scritto **un caso alla volta, con append immediato dopo ogni scheda**,
per la ragione documentata nel caso 8 e nel caso 12: quando il servizio dei subagenti cade —
e cade — sopravvive solo cio' che e' gia' su disco.

## Connessioni
- `company/Ispettorato/registro/REGISTRO-ERRORI.md` — il registro anti-recidiva ufficiale
- `company/Memory/riprese/EMP-QQ2R.md` · `EMP-URQ7.md` · `EMP-W4K7.md`
- `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` — il ciclo a 9 passi (ADR-006)
