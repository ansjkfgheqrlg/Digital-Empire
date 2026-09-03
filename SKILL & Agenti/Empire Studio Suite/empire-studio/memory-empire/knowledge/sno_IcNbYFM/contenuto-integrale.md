# Contenuto Integrale — sno_IcNbYFM
## "Ho creato un CFO AI che controlla l'azienda H24 con Claude" — Giovanni Beggiato

**Fonte audio:** trascrizione italiana auto-generata YouTube (`sno_IcNbYFM.it.vtt`), letta
integralmente in `transcript_clean.txt` (849 righe con timestamp).
**Fonte visiva:** 82 frame guardati su 523 estratti (82 degli 226 frame unici indicati da
`scenes.md`), 0 illeggibili. Copertura dichiarata **parziale ma completa per capitolo** —
dettaglio in `runs/max17-v15/coverage.md`.
**Durata:** 34:52 (2092s) · **Canale:** Giovanni Beggiato ("Joe", agenzia AI "Gente Sei",
community Skool "Avanguardia Plus") · **Lingua:** italiano
**Run sorgente:** `empire-studio/runs/max17-v15`
**Archiviato:** 2026-09-03 (Memory Empire Stage C)

> **Regola applicata:** questo file **espande e riorganizza per categoria**
> `video-analysis.md` (walkthrough cronologico) senza riassumere. Ogni prompt, ogni soglia,
> ogni cifra della demo compare qui per intero.

---

## PARTE 1 — L'ARCHITETTURA A TRE FASI

### 1.1 La tesi

Quasi tutte le aziende hanno già i dati per tenere sotto controllo le finanze (gestionale
acceso, aggiornato ogni giorno), ma manca chi li **interpreti** per la direzione. Soluzione
costruita: un "AI CFO" che tiene sotto controllo l'azienda "24/7", analizza conto economico,
crediti, margine, ciclo di cassa, scostamento dal budget, e trasforma tutto in un report con
azioni per la leadership già ordinate per priorità.

### 1.2 Le tre fasi, mai mescolate

```
1. ESTRAZIONE                2. CALCOLO DETERMINISTICO       3. INTERPRETAZIONE
   solo dati grezzi              motore Python (non l'AI)        skill "ai-cfo"
   su disco, zero calcoli        fa tutte le somme, i punteggi,  legge i numeri già
   (QuickBooks via OAuth)        gli scostamenti budget           fissi, li traduce in
                                                                   report per la direzione
        |                              |                                |
        v                              v                                v
  "se un numero non torna,      test di determinismo:           verifica_dashboard.py:
   apri il file grezzo"         stessa SHA-256 su 13             blocca la consegna se un
                                 funzioni, ha trovato 2 bug       numero non ha origine
```

Principio ripetuto due volte con parole quasi identiche (2:59 e 32:35): **"il codice fa i
conti, l'AI li interpreta."** Motivazione tecnica esplicita, doppia: (a) sono formule
matematiche, il codice non consuma token per farle; (b) si passa da "stocasticità" a
"determinismo" — un LLM indovina il token successivo con una probabilità di sbagliare diversa
da zero, il codice fa sempre la stessa identica operazione.

### 1.3 Perché serve uno strato intermedio comune

Detto prima di scrivere qualunque riga di codice (8:16 circa): *"I dati finanziari arriveranno
da fonti diverse nel tempo. Oggi un gestionale via API, domani un export in foglio di calcolo,
dopodomani un altro gestionale. Le metriche e i prompt devono cambiare quando cambia la fonte.
Serve quindi uno strato intermedio che tutte le fonti attraversano e da cui esce sempre la
stessa forma."*

### 1.4 Perché l'estrazione e il calcolo restano fasi separate

*"Al momento non vogliamo ancora fare dei conti perché vogliamo tenere le due fasi abbastanza
distinte, altrimenti rischiamo di andare a far allucinare il nostro modello."* Motivazione di
costo aggiunta: *"Avere il dato grezzo sul disco permette di rifare i conti senza chiamare le
API... se un numero non torna, apri il file grezzo."* Regola generalizzata: *"Per la
piccola-media impresa i dati non sono poi così tanti da non poter essere contenuti dentro al
PC"* — a differenza di aziende con volumi enormi ("software SQL"), dove serve tutto in cloud.

### 1.5 Postura dichiarata su AI e lavoro finanziario

*"Non stiamo parlando di rimuovere persone o rimuovere i CFO, stiamo parlando di strumenti
che, se vengono utilizzati correttamente, possono aumentare drasticamente l'impatto che un
determinato CFO, un determinato team di analisi finanziaria può avere all'interno della nostra
azienda."* Ripetuto a chiusura video: *"parliamo qui di AI enhancement e non di rimpiazzare
lavori vari"* — la decisione finale resta sempre umana.

---

## PARTE 2 — I SEI PROMPT, INTEGRALI (dal documento Notion pubblico)

Tutti i prompt sono precompilati in un documento Notion condiviso in descrizione ("AI CFO —
tutti i prompt"), incollati uno per uno nella chat Claude, mai scritti a mano davanti alla
telecamera.

### Prompt 1 — Modello dati Python

Richiede: "Costruisci il modello dati di un sistema di analisi finanziaria in Python usando la
libreria standard" (nessuna dipendenza esterna). Contesto nel prompt: dati finanziari da fonti
diverse nel tempo, serve strato intermedio comune. Richiede quattro dataclass "non negotiable"
(voce = stringa, descrizione, importo = float, sempre nello stesso formato), funzioni di
collegamento, e due funzioni obbligatorie che devono restituire la contabilità: `carica_da_csv`
e `carica_da_quickbooks`.

### Prompt 2 — Collegare QuickBooks e scaricare i dati

Tre parti: (a) autenticazione OAuth 2.0; (b) una classe client Python per le chiamate API; (c)
estrazione pura, senza calcoli — le due fasi restano distinte per non far allucinare il
modello. Cose da estrarre: piano dei conti, clienti, fornitori, articoli, fatture di vendita,
incassi.

### Prompt 3 — Il motore delle metriche

Prompt lungo che richiede le funzioni del motore di calcolo deterministico — conto economico,
conto economico per periodo, scadenziario/documenti scaduti, punteggio di rischio clienti,
redditività per servizio, fra le altre. Include un vincolo esplicito di riproducibilità
bit-per-bit: *"a parità di dati due esecuzioni devono eseguire un output identico riga per
riga, dove ordini per punteggio aggiungi un criterio di parità (nome, ecc.)".*

### Prompt 4 — Allerte e Command Center

"Cosa fai: insegni al motore quando un numero è un problema, e impacchetti tutte le tabelle in
un file solo che l'agente leggerà." "Perché: un alert senza soglia scritta non è un alert, è
un'opinione. Qui le soglie diventano un elenco visibile che chiunque può discutere. È anche il
confine del sistema: da questo punto in poi non si calcola più niente, si interpreta soltanto."
Chiede di aggiungere al motore la funzione `alert(contabilita)` e scrivere
`costruisci_command_center.py`.

**Le dieci soglie, lette per intero** (dizionario in cima al modulo, un commento per ognuna):

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

Ogni alert ha **sei campi obbligatori**: gravità (critico/alto/medio), titolo (una frase che si
legge da sola), valore (il numero misurato, col confronto), soglia (il limite superato),
impatto (cosa significa in euro o in giorni, quantificato), azione (cosa si fa, in modo
verificabile). Alert da implementare elencati: margine lordo in calo oltre soglia, EBITDA sotto
soglia minima, giorni medi di incasso sopra soglia, ciclo di cassa sopra soglia, copertura dei
costi fissi sotto tre mesi, flusso di cassa negativo mentre l'utile è positivo ("la firma
inconfondibile del circolante che si mangia l'utile"), quota di crediti scaduti sopra soglia.

### Prompt 5 — La dashboard

"Cosa fai: produci la pagina che finisce davanti alla direzione, un file HTML solo, che si apre
anche senza rete." "Perché: chi dirige la legge nei primi trenta secondi oppure non la legge.
Quindi la difficoltà non è metterci dentro tutto: è togliere tutto quello che non porta a una
decisione. Metà di questo prompt dice cosa NON mettere." Output: salva in
`output/cfo-review-AAAA-MM-GG.html` e apri.

### Prompt 6 — Il controllo antinvenzione

Dichiarato a voce come "il prompt più importante di tutti — è quello che ti permette di
mettere la dashboard davanti a qualcuno senza doverla accompagnare con dei distinguo." Chiede
di scrivere `verifica_dashboard.py`, che controlla che ogni numero scritto nella dashboard
esista davvero nei dati, e insegna a risalire a un numero quando c'è un dubbio.

**PARTE A — il cancello automatico, sei passi integrali:**
1. estrai ogni numero dal testo dell'HTML, ignorando CSS, SVG e attributi (coordinate e
   larghezze, non dati);
2. costruisci l'insieme dei valori noti scavando ricorsivamente in `command_center.json` a
   qualunque profondità;
3. espandi l'insieme con le combinazioni elementari che un CFO fa a mente (il valore ×100 e
   /100 per le percentuali, il valore assoluto, arrotondamenti, migliaia, giorni × fatturato
   giornaliero, punti percentuali × ricavi, differenze e somme fra coppie di KPI);
4. ignora i numeri che compaiono per forza e non sono dati (anni, giorni del mese, percentuali
   di sezione, numeri delle barre);
5. confronta con tolleranza relativa dello 0,6%;
6. elenca quello che non trova — va guardato a mano, uno per uno, e o si giustifica o si
   corregge.

**Esce con codice 1 se resta anche un solo numero senza origine** — blocca la pipeline, non
solo segnala. Motivazione del doppio cancello (codice deterministico + questo controllo
separato): *"Perché dobbiamo mettere un altro cancello di verifica? Perché c'è
l'interpretazione del dato. Non vogliamo che nella parte in cui ci siamo distaccati dal codice
deterministico allora abbiamo cominciato poi ad introdurre degli errori."*

---

## PARTE 3 — IL TEST DI DETERMINISMO HA TROVATO UN BUG REALE

Documentato per iscritto nel Notion, non solo dichiarato a voce. Confrontando 12 mesi di
budget contro 8 mesi di consuntivo usciva uno scostamento del **−40,8%** — "un risultato che
non era un risultato, era un calendario". Corretto usando solo i mesi in comune fra budget e
consuntivo:

| | EUR |
|---|---:|
| budget anno intero | 4.431.983 |
| budget periodo confrontabile (8 mesi) | 2.711.483 |
| consuntivo periodo | 2.625.149 |
| **scostamento corretto** | **−86.334 (−3,2%)** |

Seconda correzione, stessa famiglia di bug: agosto 2026 tagliato al giorno 20, quindi il
budget deve coprire il mese pieno mentre il consuntivo copre venti giorni — introdotti i flag
`mese_parziale` e `consuntivo_al`. Senza quel flag agosto risultava a −33,8%, "sembrava un
crollo". Terza correzione, minore: una percentuale sul fatturato veniva arrotondata due volte
in punti diversi del codice, con risultati leggermente diversi nella stessa riga — corretta
arrotondando una volta sola. **Determinismo confermato con la stessa impronta SHA-256 su tutte
e 13 le funzioni, prima e dopo le modifiche.**

Due decisioni di progetto dichiarate esplicitamente nel documento: il punteggio di rischio è
**parziale e lo dichiara** (il fido non è compilato, quindi la componente esposizione — 30
punti su 100 — non è calcolabile; il punteggio si normalizza sul massimo effettivamente
calcolabile invece di far sembrare tutti a basso rischio). Le percentuali di recupero attese
sono scritte in una variabile `RECUPERO_ATTESO` "in cima al modulo, non dentro le formule" —
motivazione: *"Un numero scritto dentro una formula diventa invisibile: chi legge il risultato
non ha modo di sapere che una parte di quel risultato è una scelta e non una misura."* Limite
dichiarato di `redditivita_servizi()`: restituisce margini fra 25,2% e 26,0% su tutti e otto i
servizi perché, senza margini di listino per servizio, il ricarico viene distribuito in
proporzione ai ricavi — il codice porta un commento "NON DICE" a chiarirlo.

---

## PARTE 4 — LE DUE SKILL

**FASE 3. L'agente** (Notion): *"Il motore adesso produce numeri. Manca chi li legge, e
servono due teste diverse, non una."* Due skill già pronte, scaricabili dalla community privata
**Avanguardia Plus** su Skool (`skool.com/avanguardia-plus`, lezione "AI CFO") — non costruite
da zero nel video, scaricate come `.zip` e installate.

- **`analista-finanziario`** — "estrae da QuickBooks, normalizza e calcola. Produce le dodici
  tabelle del Command Center e si ferma lì. Nessun aggettivo, nessuna raccomandazione: 'i
  giorni per farsi pagare sono 93' è il suo lavoro, 'i giorni per farsi pagare sono
  preoccupanti' no."
- **`ai-cfo`** — "non tocca mai i conti. Da' per fatta l'analisi e comincia dopo: legge le
  dodici tabelle, decide qual è la cosa più importante, la traduce in impatto sulla cassa o sul
  margine, e la trasforma in azioni con un responsabile e una data. Consegna sempre e solo una
  dashboard HTML."

Frase evidenziata: *"La linea fra le due è il punto di tutto il sistema. Se una sconfina, o i
numeri diventano opinioni, o le opinioni diventano numeri."* Ogni skill porta anche sette
documenti di riferimento (come ragiona un CFO con esempi, quadri di analisi, glossario delle
metriche, specifica della dashboard, formule con i loro limiti, modello dati, trappole note di
QuickBooks, più il modello HTML della dashboard).

**`SKILL.md` di `ai-cfo`, letto per intero:** Name: ai-cfo. Description: "Direttore finanziario
che legge analisi già fatte e le trasforma in decisioni. Usa ogni volta che arrivano risultati
finanziari da interpretare: KPI, conto economico, margini, scadenziario clienti o fornitori,
punteggio di rischio, previsione incassi, ciclo del circolante, budget contro consuntivo,
alert, pacchetti di reporting direzionale o export di dashboard. Si attiva anche a frasi come
'cosa vuol dire questo per l'azienda', 'guarda questi numeri da CFO', 'cosa devo fare', 'com'è
andato il mese'. NON fa contabilità, non registra documenti, non riconcilia, non ricalcola:
presuppone che l'analisi sia già stata fatta..." (testo tagliato dallo scroll del frame).

**Installazione mostrata dal vivo**: prompt in chat "Hey, all'interno del mio desktop ci sono
delle skill.zip che mi piacerebbe che tu importassi all'interno di questo progetto. Sono una
lista finanziaria e un AI CFO. Dimmi una volta che lo hai fatto." Claude cerca sul Desktop,
trova `skill-ai-cfo.zip`, elenca il contenuto **prima di estrarlo** (motivo dichiarato: "sono
istruzioni che finirebbero nel mio contesto, quindi le guardo prima di installarle"), verifica
che siano "legittime e coerenti col sistema", le installa: **10 file in tutto dentro
`.claude/skills/`** — `ai-cfo/{assets/, references/, SKILL.md}` e
`analista-finanziario/{references/, SKILL.md}`.

Claude stesso segnala una discrepanza prima di procedere: le skill descrivono percorsi diversi
da quelli reali (`labs/ai-cfo/engine/...` nelle skill contro `analisi/` +
`costruisci_command_center.py` nella radice del progetto reale), e citano due script che nel
progetto **non esistono ancora**: `verifica_dati.py` (dichiarato dalla skill come "passo 4
della procedura": controlla le coerenze contabili e blocca la consegna se un test fallisce) e
`pubblica_su_sheets.py` (con un suo file `dati/parametri/fogli_google.json`). Beggiato chiede
di allineare le skill al codice reale scrivendo `verifica_dati.py` prima di proseguire.

---

## PARTE 5 — I NUMERI DELLA DEMO (report "CFO Review", azienda sandbox Vento Logistica S.r.l.)

Mostrati identici sia nella demo iniziale (1:16) sia nel risultato finale ricostruito in
diretta (32:04–32:36) — confermando che non è un mockup diverso mostrato per hype, ma lo stesso
identico file HTML.

**Titolo:** "CFO Review — Vento Logistica S.r.l. — Verona — dati al 22 agosto 2026." Fonte:
Command Center, QuickBooks Online. Periodo di confronto: 12 mesi mobili, valuta EUR.

**Sezione 1 — CFO ALERT (5 alert):**
- CRITICO — clienti pagano 93 giorni in media (76 un anno fa), 18 giorni oltre soglia 75
  valgono 211.635€ fermi nei crediti → chiamare i dieci clienti con lo scaduto più alto entro
  questa settimana.
- CRITICO — esposizione 132.727€ su NordEst Commerce contro soglia 60.000€, 19 fatture aperte
  di cui 43.863€ già scadute → acconto sulle prossime consegne e fornitura ferma finché non
  rientra.
- ALTO — 31% dei crediti già scaduto (328.028€ su 1.074.203€ aperti, limite 25%) → giro di
  telefonate sui primi dieci per importo entro dieci giorni.
- ALTO — altre due esposizioni sopra soglia (ValDistribuzione 80.984€, GardaMetal 61.136€) →
  stesso trattamento, dopo NordEst.
- MEDIO — NordEst Commerce vale il 12% del fatturato, la sua perdita toglierebbe 229.353€ di
  margine → contratto pluriennale e tre clienti nuovi da settori diversi.

**Sezione 2 — Executive Summary:** fatturato 12 mesi 4.198.187€ (+17,4%), EBITDA +41,3% a
442.393€, cassa disponibile 205.053€ (3,9 mesi di costi fissi). Margine mensile rotto a
gennaio: da 26,84% (dicembre) a 20,61% (gennaio), mai più tornato sopra 25%, ultimo mese pieno
al 22,68%. Media 12 mesi 25,53% nasconde il problema perché contiene ancora il buon secondo
semestre 2025. Divario fra 22,68% e la media vale 119.648€/anno. Giorni di incasso passati da
76,5 a 93,4, immobilizzando altri 123.070€. Sintesi: *"Non è un problema commerciale: vendiamo
di più, al prezzo sbagliato, e incassiamo più tardi."* Tre card MOSSA 1/2/3 con raccomandazioni
operative.

**Sezione margine per linea di servizio (8 righe, ricavi/quota/margine):** Trasporto nazionale
2.014.763€/25,9%/25,18%; Groupage nazionale 1.695.771€/21,8%/25,32%; Trasporto internazionale
UE 1.535.869€/19,8%/25,17%; Deposito e magazzino 871.923€/11,2%/25,64%; Handling, picking,
imballo 633.863€/8,2%/25,33%; Pratiche doganali 499.293€/6,4%/25,99%; Distribuzione last mile
336.964€/4,3%/25,22%; Consulenza logistica 187.290€/2,4%/25,44%. Nota nella pagina: margini
tutti fra 25,17% e 25,99% perché il costo del venduto è ripartito in proporzione ai ricavi, non
usabile per decidere finché i margini di listino non sono dichiarati.

**Sezione margine mensile:** "4 — MARGINE, Il margine si è rotto a gennaio, e la media annuale
lo nasconde" — grafico con marcatore "rottura gennaio", media pre-rottura 26,7% vs media
post-rottura 22,8%.

**Sezione crediti:** "5 — CREDITI, Un milione fuori, un terzo già in ritardo" — scadenziario
1.074.203€ aperti totali a barre per fascia di ritardo. Tabella "Da chiamare per primi": 6
clienti sintetici — TartaroComponenti 11.708€/625gg ("ferma dal 2024, qui si decide se
svalutare"); CastelDesign 8.400€/494gg; BentivoglioOfficine 8.871€/311gg; un cliente a
16.809€/49gg ("importo più alto della lista, ritardo ancora recuperabile"); NordEst Commerce
13.782€/68gg ("il cliente più grande, la telefonata la fa la direzione"); GardaTrade
4.101€/441gg ("importo piccolo ma vecchissimo: chiudere la posizione").

---

## PARTE 6 — CONFRONTO CON DIGITAL EMPIRE (sintesi — dettaglio in `confronto-tesoreria.md`)

Deliverable dedicato del run: confronto punto per punto fra questo CFO AI e la **Tesoreria**
di Digital Empire (ADR-020, nata lo stesso giorno, 2026-09-03, registro ancora vuoto).

**Il video fa già, e la Tesoreria no:** connessione diretta al gestionale (OAuth QuickBooks vs
100% inserimento manuale), motore di allerta con soglie in codice, scadenzario crediti per
cliente, cancello anti-invenzione automatico sull'output interpretato, test di determinismo con
bug reali trovati, un livello esplicito di "parametri esterni" (budget, fido, margini) come
input di prima classe.

**La Tesoreria fa già, e il video non tratta:** pensata per due soci in parallelo (JSONL
mergiabile — il video è a operatore singolo), correzione per rettifica mai per cancellazione
(già collaudata), la stessa disciplina previsto/incassato ma codificata indipendentemente,
cinque agenti con confini scritti e supervisione C-suite, la regola del passato vuoto
dichiarata come legge attiva anche senza dati.

**Cinque consigli concreti dati:** dizionario di soglie commentate in `tesoreria.py`; campo
`--scadenza` sulle entrate fatturate per uno scadenzario reale; `verifica_report.py` leggero
per le risposte in prosa degli agenti Tesoreria; test di determinismo/regressione su
`calcola()`; un terzo tipo di dato "parametro esterno" accanto a entrate e spese.

---

## Tracciabilità

- Contenuto integrale: `memory-empire/knowledge/sno_IcNbYFM/contenuto-integrale.md` (questo file)
- Atoms: `memory-empire/knowledge/sno_IcNbYFM/atoms.json` (copia integrale di
  `runs/max17-v15/atoms.json`, 40 KA)
- Manifest: `memory-empire/knowledge/sno_IcNbYFM/ingest-manifest.json`
- Analisi visiva: `runs/max17-v15/video-analysis.md` (walkthrough cronologico completo)
- Coverage: `runs/max17-v15/coverage.md`
- Deliverable speciale: `runs/max17-v15/confronto-tesoreria.md`
- Pagina wiki: `second-brain-vault/wiki/sources/Source_Giovanni_Beggiato_CFO_AI_Claude.md`
- Checkpoint di chiusura: `company/Memory/checkpoints/` (vedi ultimo CP-20260903-*)
