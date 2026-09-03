# Video Analysis — "Ho creato un CFO AI che controlla l'azienda H24 con Claude"

- **ID YouTube:** sno_IcNbYFM
- **Titolo:** Ho creato un CFO AI che controlla l'azienda H24 con Claude
- **Canale/Autore:** Giovanni Beggiato — si presenta a voce come "Joe", agenzia di intelligenza artificiale "Gente Sei" ("Genti Sei"/nome udito foneticamente, consulenza ad aziende da 10.000€/mese a 50 milioni €/anno, community privata su Skool "Avanguardia Plus")
- **URL:** https://www.youtube.com/watch?v=sno_IcNbYFM
- **Durata:** 2092s = 34m52s
- **Lingua:** italiano
- **Ingested:** 2026-09-03T13:27:23
- **Frame densi estratti:** 523 (1 ogni 4.0s) — **Frame unici (scene reali):** 226 (soglia 3.0, riduzione 56,8%)
- **Frame guardati davvero da me: 82/226 unici (36,3%), 82/523 totali (15,7%)** — vedi `coverage.md` per l'elenco esatto e l'onestà sul resto

## Capitoli ufficiali (da `ingest.json`)

| Start | Titolo |
|---|---|
| 0:00 | Introduzione |
| 1:16 | Demo del report finale dell'AI CFO |
| 3:15 | Connessione a QuickBooks via API |
| 7:21 | Creazione del modello dati Python |
| 10:42 | Collegamento QuickBooks e download dati |
| 15:56 | Integrazione parametri esterni (sconti, budget, fidi) |
| 20:14 | Costruzione del motore di calcolo deterministico |
| 24:32 | Logica degli alert e segnali di rischio |
| 27:34 | Import delle skill (Analista Finanziario + AI CFO) |
| 30:29 | Creazione della dashboard e prompt anti-allucinazione |
| 32:12 | Risultato finale e considerazioni conclusive |

---

## LA TESI DEL VIDEO

Detto a voce nei primi 30 secondi (0:00–0:30): quasi tutte le aziende hanno già i dati per tenere sotto controllo le finanze (gestionale acceso, aggiornato ogni giorno), ma manca chi li **interpreti** per la direzione. Beggiato costruisce un "AI CFO" che tiene sotto controllo l'azienda "24/7" (pronunciato "247" — refuso di trascrizione per "24/7"): analizza conto economico, chi deve pagare, margine, ciclo di cassa, scostamento dal budget "senza che nessuno lo noti", e trasforma tutto in un report con azioni per la leadership già ordinate per priorità.

**Impianto architetturale dichiarato e poi effettivamente costruito, in 3 fasi nettamente separate** (ripetuto più volte nel video come principio, non solo come sequenza di comandi):
1. **Estrazione** — solo dati grezzi da QuickBooks su disco, nessun calcolo.
2. **Calcolo deterministico** — un motore Python (non l'AI) fa tutte le somme, divisioni, punteggi.
3. **Interpretazione** — solo qui, dopo che i numeri esistono già e sono fissi, un agente AI (skill "ai-cfo") li legge e li trasforma in un report per la direzione, verificato da uno script anti-invenzione che blocca la consegna se un numero nella dashboard non risale a un dato calcolato davvero.

Frase riassuntiva pronunciata due volte con parole quasi identiche (2:59 e 32:35 circa): *"Il codice fa i conti, l'AI li interpreta"* — e la ragione dichiarata non è di stile ma di **token e di determinismo**: il codice non consuma token per fare aritmetica, e un'operazione di codice dà sempre lo stesso risultato mentre un LLM "indovina" il token successivo con una probabilità di sbagliare diversa da zero.

---

## PARTE 1 — INTRODUZIONE E DEMO DEL REPORT FINALE (0:00–3:15)

Talking-head diretto in camera (frame-001, frame-002, frame-005…frame-019: sequenza fitta di stacchi typografici kinetici — testo animato bianco/nero su schermo, non slide statiche) che elenca a voce, sezione per sezione, cosa conterrà il report finale: CFO Alert, Executive Summary, overview KPI, insight sul margine, breakdown per servizio, insight sui crediti, azioni raccomandate.

A **1:16 (frame-020)** il video mostra per la prima volta lo **schermo reale**: un file HTML aperto in Chrome via `file:///Users/giovannibeggiato/Desktop/AI%20CFO%20YouTube/output/cfo-review-2026-08-22.html`. Titolo pagina: **"CFO Review"** — sottotitolo **"Vento Logistica S.r.l. — Verona — dati al 22 agosto 2026"**, header a destra **"Fonte: Command Center, QuickBooks Online · Periodo di confronto: 12 mesi mobili · valuta EUR"**.

**Sezione 1 — CFO ALERT** (5 alert, ognuno con badge di gravità CRITICO/ALTO/MEDIO, valore misurato, soglia superata, impatto in euro, azione consigliata):
- **CRITICO** — "I clienti pagano a 93 giorni in media, erano 76 un anno fa. I 18 giorni oltre la soglia di 75 valgono 211.635 euro fermi nei crediti" → *chiamare i dieci clienti con lo scaduto più alto entro questa settimana.*
- **CRITICO** — "Esposizione di 132.727 euro su NordEst Commerce, contro una soglia di 60.000: sono 19 fatture aperte, di cui 43.863 già scadute" → *acconto sulle prossime consegne e fornitura ferma finché non rientra.*
- **ALTO** — "Il 31% dei crediti è già scaduto: 328.028 euro su 1.074.203 aperti, contro un limite del 25%" → *giro di telefonate sui primi dieci per importo entro dieci giorni.*
- **ALTO** — "Altre due esposizioni sopra soglia: ValDistribuzione a 80.984 euro e GardaMetal a 61.136" → *stesso trattamento, ma dopo NordEst.*
- **MEDIO** — "NordEst Commerce vale il 12% del fatturato. Non è ancora un rischio di sopravvivenza, ma la sua perdita toglierebbe 229.353 euro di margine" → *contratto pluriennale e tre clienti nuovi da settori diversi.*

**Sezione 2 — EXECUTIVE SUMMARY**: "Il fatturato dei dodici mesi è 4.198.187 euro, in crescita del 17,4%, e l'EBITDA sale del 41,3% a 442.393 euro: la crescita è reale e la cassa regge, con 205.053 euro disponibili pari a 3,9 mesi di costi fissi. Ma il margine mensile si è rotto a gennaio: era 26,84% a dicembre, è sceso a 20,61% a gennaio e da allora non è più tornato sopra il 25%, chiudendo l'ultimo mese pieno al 22,68%. La media dei dodici mesi, 25,53%, non lo mostra perché contiene ancora il buon secondo semestre 2025. Il divario fra quel 22,68% e la media vale 119.648 euro l'anno. Nello stesso periodo i giorni di incasso sono passati da 76,5 a 93,4, immobilizzando altri 123.070 euro." Chiusa da una frase in corsivo: *"Non è un problema commerciale: vendiamo di più, al prezzo sbagliato, e incassiamo più tardi."* Sotto, tre card **MOSSA 1 / MOSSA 2 / MOSSA 3** con raccomandazioni operative concrete (rivedere il prezzo sui tre servizi che pesano il margine 67%; recuperare lo scaduto e fermare l'allungamento; rientrare sull'esposizione dei tre clienti maggiori).

Beggiato scorre poi a voce (senza più zoom leggibile in questo primo passaggio, ripreso per intero più avanti nel "Risultato finale") KPI overview (ricavi, margine lordo, EBITDA, giorni di incasso, crediti scaduti, copertura costi fissi), il grafico del margine mensile, il breakdown per servizio, lo scadenziario crediti e le azioni raccomandate — cioè l'intero report che il video costruirà da zero nei successivi 29 minuti.

➕ Osservazione mia (non dichiarata a voce): confrontando frame-020 con il **risultato finale** mostrato a fine video (frame-484/488/490, ~32:04–32:36) i numeri sono **identici, cifra per cifra** (93 giorni, NordEst 132.727, 31% crediti, 4.198.187 di fatturato, EBITDA 41,3%/442.393€…). Non è quindi un mockup/demo diverso mostrato all'inizio per hype: è **lo stesso identico file HTML finale**, mostrato in anteprima all'inizio del video e poi ri-mostrato per intero alla fine dopo averlo effettivamente ricostruito in diretta.

---

## PARTE 2 — CONNESSIONE A QUICKBOOKS VIA API (3:15–7:21)

Beggiato apre QuickBooks Online **Sandbox** (dati sintetici, non un'azienda vera) per mostrare da dove arrivano i dati grezzi (frame-050, frame-051, frame-067, frame-070, frame-072, frame-074): PNL (profit & loss), spese pagate/da pagare, sezione Accounting, Receipts, transazioni bancarie, poi Sales → "Get Paid" con le fatture clienti (importo dovuto, importo mandato, data di scadenza attesa, stato attività). Dichiara esplicitamente: *"Questa diventa la nostra source of truth, la nostra fonte di verità. Qualsiasi cosa noi andremo a fare con Cloud dovrà fare in modo che i dati di Cloud rispecchino esattamente questi."*

**Registrazione app QuickBooks (frame-077, frame-083, frame-088)**: apre `developer.intuit.com/dashboard`, entra in "My Apps Dashboard", crea una nuova app (nome tipo "accounting"), seleziona i permessi (Accounting + una seconda voce), preme Confirm — ottiene **Client ID e Client Secret**. Passo tecnico dichiarato come "molto importante": prendere il **redirect URI** dalla sezione Settings dell'app e impostarlo a `http://localhost:8000/callback`, altrimenti "QuickBook non risponde" — senza questo l'OAuth non torna mai al programma locale.

**Ambiente di lavoro (frame-092, frame-096)**: non è la CLI "Claude Code" da terminale ma la **app desktop Claude** (interfaccia scura), con una tab **"Code"** dedicata al coding agentico dentro un progetto locale ("AI CFO YouTube"). La home mostra le statistiche personali di utilizzo di Beggiato: **700 sessioni, 98.076 messaggi, 64,2M token totali, 41 giorni attivi, streak corrente 6 giorni, streak più lungo 24 giorni, ora di picco 9:00, modello preferito "Opus 5"**. Dentro la tab Code, la sessione si chiama "Ciao", con un menu Artifacts/Files/iOS Simulator/Open in/Rename/Transcript view/Fork/Archive/Delete e un selettore di modello in basso a destra ("Sonnet 5 High" in alcuni punti del video, "Opus 5 High" in altri — Beggiato cambia modello manualmente più volte, dicendo esplicitamente a un certo punto "ora metto Opus al volo" prima di un prompt più impegnativo).

Crea nel progetto un file `.env` con `QBO_CLIENT_ID` e `QBO_CLIENT_SECRET`, incollando le credenziali ottenute da Intuit.

Prima di generare codice, spiega perché serve uno "strato intermedio": *"I dati finanziari arriveranno da fonti diverse nel tempo. Oggi un gestionale via API, domani un export in foglio di calcolo, dopodomani un altro gestionale. Le metriche e i prompt devono cambiare quando cambia la fonte. Serve quindi uno strato intermedio che tutte le fonti attraversano e da cui esce sempre la stessa forma."* (3:34 circa) — è la logica dichiarata dietro il modello dati che segue.

---

## PARTE 3 — CREAZIONE DEL MODELLO DATI PYTHON (7:21–10:42)

Tutti i prompt del video sono **precompilati in un documento Notion pubblico** ("AI CFO — tutti i prompt", condiviso in descrizione) e incollati uno per uno nella chat Claude — mai scritti a mano davanti alla telecamera.

**Prompt 1** (visibile per intero in frame-109/111/115, Notion): richiede di costruire, in Python, "il modello dati di un sistema di analisi finanziaria... usando la libreria standard" (nessuna dipendenza esterna). Contesto dichiarato nel prompt: i dati finanziari arriveranno da fonti diverse nel tempo, serve uno strato intermedio comune. Il prompt chiede: quattro tipi/dataclass "non negotiable" (voce = stringa, descrizione, importo = float — sempre nello stesso formato per evitare date lette come testo o numeri sballati), funzioni di collegamento, e due funzioni obbligatorie che devono restituire la contabilità: **carica da CSV** e **carica da QuickBooks**.

Claude produce il modello (frame-121, frame-128, frame-131 — pannello di file Code con lo script generato) e chiede se implementare subito anche "carica da CSV": Beggiato risponde di no per ora e torna al Notion per il prompt successivo.

---

## PARTE 4 — COLLEGAMENTO QUICKBOOKS E DOWNLOAD DATI (10:42–15:56)

**Prompt 2 — "Collegare QuickBooks e scaricare i dati"** (frame-141, frame-151, frame-157, frame-162, frame-165, letto scorrendo il Notion): descrive tre parti — (a) autenticazione OAuth 2.0, (b) una classe client Python per le chiamate API, (c) la parte più sottolineata a voce: **estrazione pura, senza calcoli**. Frase chiave detta a voce e confermata nel prompt: *"Al momento non vogliamo ancora fare dei conti perché vogliamo tenere le due fasi abbastanza distinte, altrimenti rischiamo di andare a far allucinare il nostro modello."*

Motivazione tecnica esplicita per salvare il dato grezzo su disco invece di ricalcolare sempre dall'API: *"Avere il dato grezzo sul disco permette di rifare i conti senza chiamare le API... se un numero non torna, apri il file grezzo."* — un'ottimizzazione dichiarata di **token e costo**, generalizzata a regola: *"Per la piccola-media impresa i dati non sono poi così tanti da non poter essere contenuti dentro al PC"* (a differenza di aziende con "software SQL" e volumi enormi, dove servirebbe tutto in cloud).

Cosa viene estratto: piano dei conti, clienti, fornitori, articoli, fatture di vendita, incassi.

Una volta generato il codice, tre comandi vanno lanciati dal terminale integrato nell'app Claude (icona apposita, mostrata a schermo dopo un tentativo mancato — "no, un secondo solo che lo faccio vedere"): (1) apre il consenso OAuth nel browser e salva il token, (2) verifica stampando il nome dell'azienda collegata, (3) scarica i file grezzi. Eseguiti in sequenza: "tutto collegato", poi "tutto a posto" col nome azienda confermato, poi "estrazione completata".

---

## PARTE 5 — INTEGRAZIONE PARAMETRI ESTERNI (15:56–20:14)

Chapter marker a schermo. Spiegato (frame-183, frame-193, frame-201, frame-209, frame-217, frame-221 — sezione Notion "5 input che il gestionale non ha") che alcuni dati finanziari rilevanti **non esistono in QuickBooks** e vanno aggiunti a mano in file separati: sconto contrattuale concesso a uno specifico cliente (è nel contratto, non nel gestionale), margine di listino per servizio, budget dell'anno redatto dalla leadership in un foglio a parte, fido bancario concesso per cliente (sta nella lettera della banca).

Dichiarazione di postura dell'autore su AI e lavoro (17:53 circa): *"Non stiamo parlando di rimuovere persone o rimuovere i CFO, stiamo parlando di strumenti che, se vengono utilizzati correttamente, possono aumentare drasticamente l'impatto che un determinato CFO... può avere all'interno della nostra azienda."*

Prompt di importazione parametri incollato in chat; Claude fa domande di chiarimento a voce/testo (es. "senza questo margine i margini per servizio escono tutti uguali. Come procediamo? te li do per servizio, unico margine per tutti, lascia vuoto" — Beggiato risponde di darli per i principali) — scambio a botta e risposta, non un prompt unico eseguito ciecamente. Risultato dichiarato: "i primi 10 valgono il 47% del fatturato" e il sistema comincia a "elaborare qualche pattern all'interno del DB".

---

## PARTE 6 — COSTRUZIONE DEL MOTORE DI CALCOLO DETERMINISTICO (20:14–24:32)

**Prompt 3 — "Il motore delle metriche"** (frame-229, frame-241, frame-245, frame-249, frame-255, letto dal Notion): prompt lungo che elenca le funzioni richieste — conto economico, conto economico per periodo, scadenziario/documenti scaduti, punteggio di rischio clienti, redditività per servizio, e altre voci elencate a schermo (non tutte lette per intero da me, vedi coverage.md).

Spiegazione centrale del video (21:01–22:17, ripetuta poco dopo con lo stesso concetto): *"Noi vogliamo che sia il codice a calcolare le cose... perché sono formule matematiche, ma [anche] perché passiamo da quella che viene definita stocasticità a quello che viene definito determinismo... Questa probabilità di sbagliare va a zero se abbiamo il codice, perché il codice fa esattamente sempre la stessa operazione."* Il prompt include esplicitamente un vincolo di **riproducibilità bit-per-bit**: "a parità di dati due esecuzioni devono eseguire un output identico riga per riga, dove ordini per punteggio aggiungi un criterio di parità (nome, ecc.)".

**Il test del determinismo trova un bug reale** (frame-343, sezione "Il test di determinismo ha trovato un bug reale" nel doc Notion, non solo dichiarato a voce): confrontando 12 mesi di budget contro 8 mesi di consuntivo usciva uno scostamento del **−40,8%**, "un risultato che non era un risultato, era un calendario" — bug corretto usando solo i mesi in comune fra budget e consuntivo (nuovo scostamento: **−86.334€, −3,2%**). Tabella mostrata: budget anno intero 4.431.983, budget periodo confrontabile (8 mesi) 2.711.483, consuntivo periodo 2.625.149. Seconda correzione, stessa famiglia di bug: agosto 2026 tagliato al giorno 20, quindi il budget deve coprire il mese pieno mentre il consuntivo copre venti giorni — introdotti i flag `mese_parziale` e `consuntivo_al`. Terza correzione, minore: una percentuale sul fatturato veniva arrotondata due volte in punti diversi del codice, con risultati leggermente diversi nella stessa riga — corretta arrotondando una volta sola. Determinismo confermato con la **stessa impronta SHA-256 su tutte e 13 le funzioni**, prima e dopo le modifiche.

Frame-353 aggiunge due decisioni di progetto dichiarate esplicitamente nel documento (non a voce): il punteggio di rischio è **parziale e lo dichiara** (il fido non è compilato, quindi la componente esposizione — 30 punti su 100 — non è calcolabile; il punteggio si normalizza sul massimo effettivamente calcolabile invece di far sembrare tutti a basso rischio); le percentuali di recupero attese sono scritte in una variabile `RECUPERO_ATTESO` "in cima al modulo, non dentro le formule" con la motivazione esplicita: *"Un numero scritto dentro una formula diventa invisibile: chi legge il risultato non ha modo di sapere che una parte di quel risultato è una scelta e non una misura."* Limite dichiarato: `redditivita_servizi()` restituisce margini fra 25,2% e 26,0% su tutti e otto i servizi perché, senza margini di listino per servizio, il ricarico viene distribuito in proporzione ai ricavi — il codice stesso porta un commento "NON DICE" a chiarirlo.

---

## PARTE 7 — LOGICA DEGLI ALERT E SEGNALI DI RISCHIO (24:32–27:34)

A voce (24:32 circa): *"Non abbiamo ancora insegnato al nostro futuro CFO come gestire alert e segnali."* Beggiato generalizza: le soglie di rischio dipendono dal settore — un'azienda di lusso dovrebbe avere un target di profitto di almeno il 30%, un'azienda di trasporto (quella usata nel video) ha margini più bassi per via dei costi operativi, una farmacia pura sta fra il 5-10% ma con reparto cosmesi può arrivare al 25-30%. Ogni azienda deve quindi definire le proprie soglie.

**Prompt 4 — "Allerte e Command Center"** (frame-364, frame-415/419, Notion): "Cosa fai: insegni al motore quando un numero è un problema, e impacchetti tutte le tabelle in un file solo che l'agente leggerà." "Perché: un alert senza soglia scritta non è un alert, è un'opinione. Qui le soglie diventano un elenco visibile che chiunque può discutere. È anche il confine del sistema: da questo punto in poi non si calcola più niente, si interpreta soltanto." Chiede di aggiungere al motore la funzione `alert(contabilita)` e scrivere `costruisci_command_center.py`, che impacchetta tutto per l'agente.

**PARTE A del prompt — motore di allerta.** Regola di fondo: "Un alert senza soglia esplicita non è un alert, è un'opinione. Metti tutte le soglie in un dizionario in cima al modulo, con un commento per ognuna." Soglie dichiarate (lette per intero, frame-415):

| Soglia | Valore |
|---|---|
| concentrazione su singolo cliente | 20% (attenzione già dal 10%) |
| esposizione su singolo cliente | 60.000 EUR |
| quota di crediti già scaduti | 25% |
| crediti oltre 90 giorni | 12% del totale |
| giorni medi di incasso | 75 |
| ciclo di cassa | 60 giorni |
| calo del margine lordo anno su anno | 1,5 punti |
| EBITDA minimo | 6% dei ricavi |
| copertura dei costi fissi | 3 mesi |
| scostamento dal budget | 10% |

Ogni alert deve avere **sei campi obbligatori**: gravità (critico/alto/medio), titolo (una frase che si legge da sola), valore (il numero misurato, col confronto), soglia (il limite superato), impatto (cosa significa in euro o in giorni, quantificato), azione (cosa si fa, in modo verificabile). Elenco degli alert da implementare, letto parzialmente: margine lordo in calo oltre soglia (quantifica in euro i punti persi), EBITDA sotto soglia minima (quantifica in euro l'allungamento), giorni medi di incasso sopra soglia, ciclo di cassa sopra soglia, copertura dei costi fissi sotto tre mesi, flusso di cassa negativo mentre l'utile è positivo ("la firma inconfondibile del circolante che si mangia l'utile"), quota di crediti scaduti sopra soglia (e altri non letti per intero).

Beggiato, dopo aver visto la prima bozza di output, segnala una "tensione" al modello (frame-399): aveva scritto per `metriche.py` "nessun aggettivo, nessuna raccomandazione" ma ora `azione` dice cose come "vanno chiamati i dieci clienti con lo scaduto più alto entro questa settimana" — chiede se questo sia un'eccezione accettabile o un errore di coerenza; il modello aggiorna la docstring del modulo per dichiarare esplicitamente che un alert scatta solo quando un numero misurato supera una soglia scritta, e che il testo dell'alert è la soglia "vestita" col numero — non un'opinione libera.

---

## PARTE 8 — IMPORT DELLE SKILL: ANALISTA FINANZIARIO + AI CFO (27:34–30:29)

Chapter marker "5. Creazione Ag[ente]" (frame-419). **FASE 3. L'agente** (frame-360, Notion): *"Il motore adesso produce numeri. Manca chi li legge, e servono due teste diverse, non una."*

Due skill **già pronte**, scaricabili dalla community privata **Avanguardia Plus** su Skool (`skool.com/avanguardia-plus`, lezione "AI CFO") — non costruite da zero nel video, ma scaricate come `.zip` e installate:

- **`analista-finanziario`** — "estrae da QuickBooks, normalizza e calcola. Produce le dodici tabelle del Command Center e si ferma lì. Nessun aggettivo, nessuna raccomandazione: 'i giorni per farsi pagare sono 93' è il suo lavoro, 'i giorni per farsi pagare sono preoccupanti' no."
- **`ai-cfo`** — "non tocca mai i conti. Da' per fatta l'analisi e comincia dopo: legge le dodici tabelle, decide qual è la cosa più importante, la traduce in impatto sulla cassa o sul margine, e la trasforma in azioni con un responsabile e una data. Consegna sempre e solo una dashboard HTML." Frase evidenziata nel doc: *"La linea fra le due è il punto di tutto il sistema. Se una sconfina, o i numeri diventano opinioni, o le opinioni diventano numeri."*

Ogni skill porta anche **sette documenti di riferimento** che le fanno ragionare: come ragiona un CFO (con esempi), i quadri di analisi, il glossario delle metriche, la specifica della dashboard, le formule con i loro limiti, il modello dati, le trappole note di QuickBooks, più il modello HTML della dashboard.

**Installazione mostrata dal vivo** (frame-392, frame-445, frame-447): in chat, "Hey, all'interno del mio desktop ci sono delle skill.zip che mi piacerebbe che tu importassi all'interno di questo progetto. Sono una lista finanziaria e un AI CFO. Dimmi una volta che lo hai fatto." Claude cerca sul Desktop, trova `skill-ai-cfo.zip`, elenca il contenuto **prima di estrarlo** (dichiarando esplicitamente il motivo: "sono istruzioni che finirebbero nel mio contesto, quindi le guardo prima di installarle"), verifica che siano "legittime e coerenti col sistema", le installa come skill di progetto: **10 file in tutto dentro `.claude/skills/`** — struttura confermata aprendo l'albero file: `ai-cfo/{assets/, references/, SKILL.md}` e `analista-finanziario/{references/, SKILL.md}`.

Contenuto del `SKILL.md` di `ai-cfo` letto per intero a schermo (frame-447): **Name: ai-cfo. Description:** "Direttore finanziario che legge analisi già fatte e le trasforma in decisioni. Usa ogni volta che arrivano risultati finanziari da interpretare: KPI, conto economico, margini, scadenziario clienti o fornitori, punteggio di rischio, previsione incassi, ciclo del circolante, budget contro consuntivo, alert, pacchetti di reporting direzionale o export di dashboard. Si attiva anche a frasi come 'cosa vuol dire questo per l'azienda', 'guarda questi numeri da CFO', 'cosa devo fare', 'com'è andato il mese'. **NON** fa contabilità, non registra documenti, non riconcilia, non ricalcola: presuppone che l'analisi sia già stata fatta..." (testo tagliato dallo scroll).

Claude stesso segnala una discrepanza prima di procedere (frame-461, "Però non combaciano con quello che c'è"): le skill descrivono percorsi di progetto diversi da quelli reali (`labs/ai-cfo/engine/...` nelle skill contro `analisi/` + `costruisci_command_center.py` nella radice del progetto reale), e citano due script che nel progetto **non esistono ancora**: `verifica_dati.py` (dichiarato dalla skill come "passo 4 della procedura": controlla le coerenze contabili e blocca la consegna se un test fallisce) e `pubblica_su_sheets.py` (con un suo file `dati/parametri/fogli_google.json`). Beggiato chiede esplicitamente di allineare le skill al codice reale scrivendo `verifica_dati.py` prima di proseguire — un dettaglio di attrito reale fra skill "generiche" scaricate e un progetto specifico, non nascosto nel montaggio.

---

## PARTE 9 — CREAZIONE DASHBOARD E PROMPT ANTI-ALLUCINAZIONE (30:29–32:12)

**Prompt 5 — "La dashboard"** (frame-364): "Cosa fai: produci la pagina che finisce davanti alla direzione, un file HTML solo, che si apre anche senza rete." "Perché: chi dirige la legge nei primi trenta secondi oppure non la legge. Quindi la difficoltà non è metterci dentro tutto: è togliere tutto quello che non porta a una decisione. Metà di questo prompt dice cosa NON mettere." Output dichiarato: salva in `output/cfo-review-AAAA-MM-GG.html` e apri.

**Prompt 6 — "Il controllo antinvenzione"** (frame-482): dichiarato a voce come "il prompt più importante di tutti" — *"è quello che ti permette di mettere la dashboard davanti a qualcuno senza doverla accompagnare con dei distinguo."* Chiede di scrivere `verifica_dashboard.py`, che controlla che ogni numero scritto nella dashboard esista davvero nei dati, e insegna a risalire a un numero quando c'è un dubbio.

**PARTE A del prompt — il cancello automatico**, 6 passi dichiarati per intero: (1) estrai ogni numero dal testo dell'HTML, ignorando CSS, SVG e attributi (quelli sono coordinate e larghezze, non dati); (2) costruisci l'insieme dei valori noti scavando ricorsivamente in `command_center.json` a qualunque profondità; (3) espandi l'insieme con le combinazioni elementari che un CFO fa a mente (il valore × 100 e /100 per le percentuali, il valore assoluto, arrotondamenti, migliaia, giorni × fatturato giornaliero, punti percentuali × ricavi, differenze e somme fra coppie di KPI); (4) ignora i numeri che compaiono per forza e non sono dati (anni, giorni del mese, percentuali di sezione, numeri delle barre); (5) confronta con tolleranza relativa dello 0,6%; (6) elenca quello che non trova — vanno guardati a mano, uno per uno, e o si giustificano o si correggono. **Esce con codice 1 se resta anche un solo numero senza origine** — cioè blocca la pipeline, non solo segnala.

Motivazione esplicita del doppio cancello (codice deterministico + questo controllo separato, 31:41 circa a voce): *"Perché dobbiamo mettere un altro cancello di verifica? Perché c'è l'interpretazione del dato. Non vogliamo che nella parte in cui ci siamo distaccati dal codice deterministico allora abbiamo cominciato poi ad introdurre degli errori."*

---

## PARTE 10 — RISULTATO FINALE (32:12–34:52)

Il file HTML finale (`.../AI CFO YouTube/output/cfo-review-2026-08-22.html`) si apre nel browser e viene scorso per intero — **è lo stesso identico contenuto mostrato in anteprima a 1:16** (stessi numeri, stesse cifre: 93 giorni, NordEst 132.727€, 31% crediti scaduti, fatturato 4.198.187€, EBITDA 41,3%/442.393€), confermando che la demo iniziale era il vero output finale, non un mockup.

Sezioni aggiuntive lette per intero in questo secondo passaggio, non descritte a voce nel dettaglio nella demo iniziale:

**Margine per linea di servizio** (frame-484, frame-488 — tabella completa, 8 righe): Trasporto nazionale 2.014.763€/25,9% quota/25,18% margine; Groupage nazionale 1.695.771€/21,8%/25,32%; Trasporto internazionale UE 1.535.869€/19,8%/25,17%; Deposito e magazzino 871.923€/11,2%/25,64%; Handling, picking, imballo 633.863€/8,2%/25,33%; Pratiche doganali 499.293€/6,4%/25,99%; Distribuzione last mile 336.964€/4,3%/25,22%; Consulenza logistica 187.290€/2,4%/25,44%. Nota nella pagina stessa (coerente col limite dichiarato al Prompt 3): *"Attenzione: questi margini per servizio sono tutti fra 25,17% e 25,99% perché il costo del venduto è ripartito in proporzione ai ricavi. Finché i margini di listino non sono dichiarati, questa colonna non distingue un servizio dall'altro e non va usata per decidere."*

**Sezione margine** (frame-513): "4 — MARGINE, Il margine si è rotto a gennaio, e la media annuale lo nasconde" — grafico mensile del margine lordo con marcatore "rottura · gennaio", media pre-rottura **26,7%** vs media post-rottura **22,8%**.

**Sezione crediti** (frame-509): "5 — CREDITI, Un milione fuori, un terzo già in ritardo" — scadenziario crediti (1.074.203€ aperti totali) a barre per fascia di ritardo (a scadere, 1-30gg, 31-60gg, 61-90gg, 91-180gg, oltre 180gg) e tabella "DA CHIAMARE PER PRIMI" con 6 clienti nominati, residuo e giorni di ritardo (dati sintetici della sandbox: TartaroComponenti 11.708€/625gg "ferma dal 2024, qui si decide se svalutare"; CastelDesign 8.400€/494gg; BentivoglioOfficine 8.871€/311gg; un cliente a 16.809€/49gg "importo più alto della lista, ritardo ancora recuperabile"; NordEst Commerce 13.782€/68gg "il cliente più grande, la telefonata la fa la direzione"; GardaTrade 4.101€/441gg "importo piccolo ma vecchissimo: chiudere la posizione").

**Chiusura del video** (talking-head, frame-509→523): Beggiato riassume che ora si ha "il vostro primo AI CFO che potrà essere a supporto delle funzioni di finance e rimpiazzare tutta quella parte di estrazione del dato che è abbastanza macchinosa e noiosa", ribadisce che la parte di analisi va sempre supervisionata da un umano che prende la decisione finale ("parliamo qui di AI enhancement e non di rimpiazzare lavori vari"), e chiude con invito a iscriversi al canale.

---

## CIÒ CHE IL VIDEO NON MOSTRA / NON HO POTUTO VERIFICARE

- **Il codice sorgente completo** di `metriche.py`, `costruisci_command_center.py`, `verifica_dashboard.py` — visti solo a schermo negli editor durante la generazione, mai aperti riga per riga con zoom dedicato in questa analisi (diversamente da rizzo/roberts, qui non è stato fatto un ritaglio ad alto ingrandimento del codice, solo dei documenti Notion che erano già a font grande).
- **Il contenuto completo dei sette "documenti di riferimento"** citati per ogni skill (come ragiona un CFO, quadri di analisi, glossario metriche, ecc.) — solo il nome e la funzione sono dichiarati nel Notion, mai aperti singolarmente a schermo.
- **Nessun costo dichiarato** per l'abbonamento QuickBooks, per la app Claude (Claude Pro/Max), o per la community Avanguardia Plus.
- **Il contenuto integrale della sezione "KPI overview"** e di alcune tabelle del command center menzionate a voce ("dodici tabelle") — il video ne mostra e nomina diverse ma non tutte e dodici sono state viste per intero a schermo.
- Il rateo esatto di frame non guardati e perché è dichiarato per intero in `coverage.md`.

---

## CONFRONTO CON DIGITAL EMPIRE

Vedi `confronto-tesoreria.md` (deliverable dedicato) per il confronto punto per punto fra questo AI CFO e la Tesoreria di Digital Empire (ADR-020).
