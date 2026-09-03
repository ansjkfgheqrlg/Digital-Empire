# Confronto — Il CFO AI del video vs la Tesoreria di Digital Empire

> Fonti: `video-analysis.md` e `atoms.json` di questo run (video `sno_IcNbYFM`, guardato per
> davvero, frame reali) contro `company/Memory/decisions/ADR-020-reparto-tesoreria.md`,
> `scripts/tesoreria.py` (letto per intero), i cinque agenti `.claude/agents/tesoreria-*.md`
> (letti per intero) e l'output reale di `python scripts/tesoreria.py report` eseguito oggi,
> 2026-09-03: **la Tesoreria è vuota, zero movimenti registrati.** Questo confronto è quindi
> fra un sistema maturo mostrato a regime (dati sandbox ma un anno intero di storia) e un
> sistema appena nato, per scelta esplicita (ADR-020 §4, "la regola del passato vuoto").
> Il confronto tiene conto di questa differenza di stadio, non la nasconde.

---

## 1. Cosa fa il CFO del video che la Tesoreria NON fa ancora

### 1.1 Connessione diretta al gestionale (estrazione automatica)
Il video collega QuickBooks Online via OAuth 2.0 (app registrata su `developer.intuit.com`,
Client ID/Secret, redirect URI) e scarica in automatico piano dei conti, clienti, fornitori,
fatture, incassi. La Tesoreria oggi **non ha nessun connettore**: ogni movimento entra a mano
con `python scripts/tesoreria.py entrata/spesa`. Non c'è un equivalente di "estrazione" nel
senso del video — il "dato grezzo" della Tesoreria è già ciò che un umano digita.

### 1.2 Un motore delle metriche con test di determinismo che ha trovato bug veri
Il prompt 3 del video chiede esplicitamente riproducibilità bit-per-bit (stessa impronta
SHA-256 su tutte le funzioni, due esecuzioni identiche) e questo test **ha scovato due bug
reali** (confronto budget/consuntivo su calendari diversi, doppio arrotondamento). `tesoreria.py`
è deterministico per costruzione (somme e divisioni semplici, nessuna casualità), ma **non ha
nessun test automatico che lo dimostri o che lo protegga da una futura regressione** quando la
logica crescerà.

### 1.3 Un motore di allerta con soglie esplicite, commentate e quantificate in euro
Il prompt 4 definisce dieci soglie nominate (concentrazione cliente 20%, esposizione singolo
cliente 60.000€, crediti scaduti 25%, giorni di incasso 75, ciclo di cassa 60gg, calo margine
1,5 punti, EBITDA minimo 6%, copertura costi fissi 3 mesi, scostamento budget 10%...), ognuna
con un commento che ne spiega la ragione, e ogni alert ha sei campi obbligatori (gravità,
titolo, valore, soglia, impatto in euro, azione verificabile). **La Tesoreria non ha nulla di
equivalente in codice.** `tesoreria-entrate.md` e `tesoreria-spese.md` *descrivono a parole*
regole simili (fatture ferme da 30gg da sollecitare, previsti fermi da 60gg da declassare a
persi, abbonamenti ricorrenti da 6+ mesi da ricontrollare) ma **`scripts/tesoreria.py` non le
calcola**: sono discipline affidate all'agente che le applica a voce, non soglie nel motore.
ADR-020 §5 dichiara peraltro esplicitamente questo stesso buco: *"non esiste ancora un tetto di
spesa in euro... una percentuale del nulla non ferma nessuno" (B-048)*.

### 1.4 Un cancello anti-invenzione automatico sull'output interpretato dall'AI
`verifica_dashboard.py` (prompt 6) estrae ogni numero dall'HTML finale, lo confronta contro
l'insieme dei valori realmente calcolati (più le loro combinazioni elementari: ×100, differenze,
somme fra KPI...) con tolleranza 0,6%, ed esce con codice 1 se resta anche un solo numero senza
origine verificabile — bloccando la consegna. È un controllo **automatico e separato** dal
motore di calcolo, pensato apposta per la fase in cui un LLM interpreta e potrebbe "abbellire"
un numero. La Tesoreria ha la stessa filosofia scritta come principio (Legge 2 del
`tesoreria-conductor`: *"un numero che non esiste si dichiara, non si stima"*) ma **nessun
controllo automatico** che la faccia rispettare: oggi è affidata all'onestà dell'agente che
scrive la risposta, non a uno script che rifiuta di consegnare.

### 1.5 Scadenzario crediti per cliente, con priorità di chiamata
Il report finale del video elenca i clienti col credito scaduto più vecchio/più grande, con
giorni di ritardo e nota su cosa fare per ciascuno. `scripts/tesoreria.py` **non ha un campo data
di scadenza** sulle entrate (solo `data` = data di registrazione): non è possibile oggi calcolare
"da quanti giorni un cliente non paga" o produrre un elenco ordinato per priorità di chiamata.

### 1.6 Serie storica mensile del margine, con rilevamento del punto di rottura
Il video mostra un grafico mensile del margine lordo che isola il mese in cui è "crollato"
(gennaio) e dimostra che la media annuale lo nasconde. La Tesoreria ha `--mese AAAA-MM` per
isolare un mese solo, ma **nessuna vista che confronti mesi consecutivi** o segnali un punto di
rottura in una serie — anche perché, come dichiarato onestamente da `tesoreria-previsione.md`,
non esistono ancora abbastanza mesi di dati per farlo (ADR-020 §4: servono almeno tre mesi).

### 1.7 Un livello esplicito di "parametri esterni al gestionale" come input di prima classe
Il video tratta sconti contrattuali, margini di listino, budget di leadership e fido bancario
come input strutturati e distinti, con un prompt dedicato a integrarli. La Tesoreria ha i
"motori di business" come tassonomia fissa (agency, kdp, corsi...) ma non ha un concetto
equivalente di "dati che il sistema non genera da solo e vanno dichiarati a parte" — per ora
tutto ciò che entra nella Tesoreria è o un'entrata o una spesa, senza un terzo tipo di dato
"parametro esterno" (es. un fido di cassa, un budget annuale target).

---

## 2. Cosa fa già la Tesoreria che il video nemmeno tratta

### 2.1 Storia dei soldi collaborativa e mergiabile fra due soci
Il video è un flusso a operatore singolo (Beggiato, da solo, sul suo Mac). La Tesoreria è
progettata esplicitamente per **due soci che lavorano in parallelo**: JSONL ad accodamento
scelto apposta perché "si leggono a occhio, si correggono a mano, e due soci che lavorano in
parallelo non si sovrascrivono quando le loro modifiche si fondono" (ADR-020 §2). Il video non
affronta mai questo problema — non ne aveva bisogno.

### 2.2 Correzione per rettifica, mai per cancellazione — già collaudata
La Tesoreria non permette di modificare una riga: si accoda una rettifica con nota (implementato
in `segna_incassata()`, testato con 5 movimenti di prova prima del rilascio, ADR-020 §2). Il
video non discute mai come si corregge un dato sbagliato nel gestionale a monte — il problema
che risolve è "il motore calcola sbagliato", non "il dato di partenza era sbagliato e va
corretto senza cancellare la storia".

### 2.3 Distinzione previsto/fatturato/incassato/perso — la stessa disciplina del video, ma già codificata prima e indipendentemente
Il principio "previsto non è incassato, mai" (Legge 1 del `tesoreria-conductor`) è **lo stesso
identico principio** del video (separare source of truth da interpretazione), applicato però al
lato entrate con quattro stati distinti e un comando dedicato (`incassa --id`) — il video non ha
un concetto equivalente di "previsto" come stato di un dato, solo "budget" come parametro esterno
di confronto.

### 2.4 Organizzazione gerarchica in 5 agenti con responsabilità separate e supervisione C-suite
Il video ha due skill (estrazione+calcolo unificati in `analista-finanziario`, interpretazione in
`ai-cfo`). La Tesoreria ha cinque agenti con confini più stretti (entrate, spese, report,
previsione, più il conductor che coordina) e una collocazione esplicita nella gerarchia
aziendale (sotto `cfo-empire`, con legami dichiarati a `cro-empire` e `ceo-empire-conductor`).
Ogni agente dichiara per iscritto cosa NON è di sua competenza (es. `tesoreria-spese` non
autorizza spese, `tesoreria-previsione` non consiglia investimenti) — una disciplina di confini
che il video non mostra mai in questi termini.

### 2.5 Regola del passato vuoto, dichiarata come legge prima ancora di avere il problema
ADR-020 §4 vieta esplicitamente di ricostruire a memoria i mesi prima del 2026-09-03: *"un
numero non verificabile è peggio di un vuoto dichiarato, perché ha l'aria di una misura"*. Il
video non ha questo problema (QuickBooks aveva già un anno di storia sintetica pronta), ma la
disciplina di fondo — non fingere di sapere ciò che non è stato misurato — è la stessa del
principio "il codice fa i conti, l'AI li interpreta": entrambi i sistemi rifiutano di far passare
una stima per una misura. La Tesoreria l'ha semplicemente scritta come legge attiva anche in
assenza di dati, non solo come contromisura a un bug scoperto.

### 2.6 Autonomia (runway) come domanda di prima classe
`tesoreria-previsione` risponde esplicitamente a "quanto reggiamo se non entra più niente"
(cassa / spese ricorrenti) e "questo motore si ripaga" — con la soglia operativa già misurata di
capacità del team (2 motori pieni + 1 ridotto, non 7) incorporata come contesto. Il video calcola
la "copertura costi fissi in mesi" dentro il report ma non ha un agente/domanda dedicata al
"quanto dura l'azienda se si ferma tutto", né lega quel numero alla capacità operativa del team.

---

## 3. Cinque consigli concreti, presi davvero dal video (non generici)

1. **Aggiungere un dizionario di soglie commentate a `scripts/tesoreria.py`**, sul modello esatto
   del prompt 4 del video (`PARTE A: IL MOTORE DI ALLERTA`, "un alert senza soglia esplicita non
   è un alert, è un'opinione. Metti tutte le soglie in un dizionario in cima al modulo, con un
   commento per ognuna"). Concretamente: portare in codice le regole che oggi vivono solo come
   prosa in `tesoreria-entrate.md`/`tesoreria-spese.md` (fatture ferme >30gg, previsti fermi
   >60gg da declassare a `perso`, ricorrenti attivi da >6 mesi da ricontrollare) come una funzione
   `alert(d)` dentro `calcola()`, che stampa nel report una sezione `ALERT` con gli stessi sei
   campi del video (gravità/titolo/valore/soglia/impatto €/azione) invece di lasciarle a
   discrezione dell'agente che risponde a voce.

2. **Aggiungere un campo `--scadenza` a `entrata --stato fatturato`** e uno scadenzario per
   cliente nel report — pattern preso 1:1 dalla sezione "5 — CREDITI" del video (scadenzario a
   fasce + tabella "da chiamare per primi" ordinata per impatto). Oggi `tesoreria.py` ha solo
   `data` di registrazione, non una data di scadenza attesa: senza quel campo la Tesoreria non
   potrà mai calcolare un DSO (giorni medi di incasso) reale né una lista di priorità di
   sollecito, che è esattamente il primo alert CRITICO del report del video.

3. **Costruire un `verifica_report.py` leggero** per qualunque risposta in prosa che
   `tesoreria-report`/`tesoreria-conductor` diano a Max (non solo l'output grezzo di
   `tesoreria.py report`), sul modello del "cancello automatico" del prompt 6: estrarre i numeri
   citati nella risposta dell'agente e confermare che risalgono a `calcola()`. Oggi la Legge 2
   del `tesoreria-conductor` ("un numero che non esiste si dichiara, non si stima") è affidata
   solo alla disciplina dell'agente — il video dimostra che anche un sistema onesto per principio
   beneficia di un controllo automatico separato, perché l'interpretazione è proprio il punto in
   cui gli errori si infilano.

4. **Aggiungere un test di determinismo/regressione a `tesoreria.py`** (equivalente più leggero
   del confronto SHA-256 del video): una piccola suite che, dato lo stesso `entrate.jsonl` /
   `spese.jsonl` di prova, verifica che `calcola()` restituisca sempre lo stesso output — utile
   fin da ora perché la funzione crescerà (soglie, scadenzario, alert) e il video mostra
   concretamente che è proprio quando la logica si complica che nascono bug silenziosi (il
   confronto budget/consuntivo su calendari diversi, il doppio arrotondamento).

5. **Introdurre un terzo tipo di dato "parametro esterno"** accanto a entrate/spese (es.
   `company/Memory/tesoreria/parametri.jsonl`: fido di cassa dichiarato, budget annuale per
   motore, target di margine per motore) — preso dal prompt di "Integrazione parametri esterni"
   del video, che tratta esplicitamente ciò che il gestionale non sa come input di prima classe
   e non come dato mancante. Senza questo, la Tesoreria non potrà mai calcolare uno scostamento
   dal budget o un punteggio di rischio comparabile a quello del video, perché quei parametri
   oggi non hanno nessun posto dove vivere.

---

## 4. In una frase

Il CFO del video è un sistema **maturo e a operatore singolo** che dimostra bene un principio che
la Tesoreria condivide già a livello di legge (*il codice calcola, l'interpretazione si verifica
separatamente*), ma lo applica con strumenti che la Tesoreria non ha ancora: soglie di allerta
in codice, scadenzario crediti, un cancello anti-invenzione automatico e un test di determinismo.
La Tesoreria, dal canto suo, risolve fin da subito un problema che il video non affronta mai —
essere uno strumento aziendale multi-persona, corretto per accumulo e non per riscrittura — ed è
partita, per scelta esplicita e non per pigrizia, da un registro vuoto invece che da un anno di
dati sintetici.

---

*Compilato il 2026-09-03 · Empire Studio · run `max17-v15` · fonti: `video-analysis.md`,
`atoms.json` (questo run) + `company/Memory/decisions/ADR-020-reparto-tesoreria.md`,
`scripts/tesoreria.py`, `.claude/agents/tesoreria-{conductor,entrate,spese,report,previsione}.md`
(tutti letti per intero) + output reale di `python scripts/tesoreria.py report` (2026-09-03,
registro vuoto confermato).*
