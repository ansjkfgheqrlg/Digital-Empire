---
Owner: Max (committente) · Esecutore: NERI · Controllore: Claude (registra, non blocca)
Origine: 12-STREAM-S7-BOT (strato strategico) · Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO
        memory-first
Emesso: 2026-08-03 · Priorità: P1 (ordine diretto di Max)
Riferimenti: PIANO-STRATEGICO-S7.md (../../Ecosistemi/12-STREAM-S7-BOT/PIANO-STRATEGICO-S7.md,
        leggilo PRIMA di questo file) · STATO-RIPRESA.md (../../Ecosistemi/12-STREAM-S7-BOT/,
        4 prerequisiti LIVE con numeri reali già elencati, non riscoprirli) ·
        TASK-GAEL-20260731-STREAM-S7-NFT-SESSIONI.md (task operativo, fermo) ·
        CP-20260730-007 (verdetto NFT) · CP-20260803-001 (ricognizione stessa diagnosi) ·
        report-studio.md · ECOSISTEMA.md
---

> **STATO: da avviare.** Primo incarico concreto assegnato a Neri (vedi
> `TASK-NERI-20260730-ONBOARDING.md`, che restava scaffolding vuoto in attesa di questo).

# 📋 TASK NERI — Strategia Stream S7: continuare, mettere in pausa, o altro

## 0. Prompt originale di Max (verbatim, integrato come richiesto)

> Continua esattamente da dove sei rimasto, fai un piano di produzione strategico per la
> produzione di quello che stai facendo - E APSSA TUTTA QUESTA TASK A NERI ADESSO PRIMA PERO
> FAI UN PIANO STRATEGICO CHE FARAI VEDRE A NERI E LUI LO STUDIERà ANALIZZERà E MIGLIORERA
> DAGLI ANCHE RICERCHE DA FARE DIGLI DEI REPORT CHE DEVE FARE E POI ASSEGNALI ARCHITETTATURE DA
> FARE. ADESSO

**Nota di Claude (trasparenza, non censura del prompt)**: testo dettato, riportato integrale.
Interpretazione sotto, esplicitamente separata.

## 1. Interpretazione operativa (Claude → Neri/Max, da confermare/correggere in corsa)

- **"Passa tutta questa task a Neri"** — interpretato come: **lo strato strategico/decisionale**
  passa a Neri (esattamente il suo ambito dichiarato: "gestione organizzativa — piani, metodi,
  processi", vedi [[entities/Neri]]). **Il task operativo (le 12 sessioni di build, codice,
  API, test) resta di Gael** — Neri non tocca codice/file operativi per suo stesso ruolo
  dichiarato ("non tocca operatività diretta"). Se questa lettura è sbagliata e Max vuole che
  Neri prenda in mano anche l'esecuzione tecnica, va detto esplicitamente: cambia il ruolo di
  Neri finora stabilito, non è una correzione minore.
- **"Continua da dove sei rimasto"**: il push del task Mintify (TASK-GAEL-...-SESSIONI.md,
  CP-20260731-004) era bloccato da un conflitto di merge con lavoro concorrente — risolto nel
  frattempo (verificato ora: `git status` pulito, in sync con `origin/main`, nessuna azione
  residua). Non c'è altro da riprendere su quel fronte.
- **Il "piano strategico"** è `PIANO-STRATEGICO-S7.md`, appena scritto, nella cartella
  `12-STREAM-S7-BOT/` — leggilo per intero prima di procedere qui sotto, questo file lo
  presuppone letto.

---

## 2. Ricerche da fare (Neri — analisi/lettura, non codice)

**R1 — Precedenti reali di sniping NFT/memecoin retail.** Esistono casi pubblici (post-mortem,
paper, thread di chi ci ha provato davvero con capitale reale) di bot retail che hanno raggiunto
expectancy positiva sostenuta contro l'infrastruttura MEV istituzionale descritta in
`report-studio.md`? Se sì, con quale differenza strutturale rispetto al nostro stack (non
"hanno avuto fortuna" — cosa hanno di diverso: infrastruttura, capitale, nicchia). Se la
risposta onesta è "non risultano casi verificabili", scrivilo così, non forzare un precedente
debole per giustificare la continuazione.

**R2 — Mintify e alternative, sul piano di business non tecnico.** Claude/Gael hanno già
verificato il lato tecnico (API, chain supportate — vedi CP-20260731-004). Manca il lato
business: pricing reale dei tier API (free vs a pagamento, limiti), Terms of Service (uso per
trading automatico è permesso o vietato?), e un confronto con almeno 2 alternative dirette
(es. Tensor su Solana, Reservoir su EVM) sullo stesso terreno.

**R3 — Costo reale in € dei 4 prerequisiti già elencati in `STATO-RIPRESA.md`** (non
riscoprirli — sono già lì, con i numeri tecnici esatti): (1) RPC Solana a pagamento
(Helius/QuickNode/Alchemy — B-010, 429 dopo 2 chiamate su endpoint pubblico), (2)
infrastruttura per chiudere il gap di latenza 2456-3624ms → 300-800ms (Jito bundles/bare-metal/
Rust), (3) feed prezzo live per `position_monitor.py`, (4) sviluppo della modalità LIVE in
`execution_engine.py`. Manca solo il prezzo. Trova un ordine di grandezza reale in €/mese per
(1)+(2) — sono i due che richiedono spesa ricorrente vs (3)+(4) che sono lavoro una tantum.
Questo numero è quello che manca per capire se "continua ma con più soldi" è un'opzione seria.

## 3. Report da produrre (Neri — output scritti, gate della decisione)

**REP1 — Raccomandazione Go/No-Go.** Una delle 4 opzioni di `PIANO-STRATEGICO-S7.md` §3
(CONTINUA / PAUSA ESPLICITA / RIDEFINISCI IL BERSAGLIO / KILLA), motivata con R1+R2+R3 sopra,
non a sensazione. Deve rispondere esplicitamente alla domanda di §2 del piano strategico.
Formato libero, ma ogni affermazione con fonte (stesso standard già in uso su questo
ecosistema: mai un numero senza dove viene).

**REP2 — Costo-opportunità dei 3 giorni fermi.** Il task Gael è rimasto "da avviare" dal
2026-07-31 al 2026-08-03. Nello stesso periodo cos'ha fatto Gael invece (verificabile da
`git log`, checkpoint, `STATO-EMPIRE.md`)? È stata la priorità giusta? Questo report non serve
a giudicare Gael — serve a capire se il problema è "S7 non conviene" o "non c'è mai capacità
libera per S7 finché esiste lavoro revenue", che sono due diagnosi diverse con soluzioni
diverse.

**REP3 — Valutazione vendor Mintify vs alternative**, sintesi operativa di R2, con una riga di
raccomandazione finale (quale fonte dati, se una, usare se si procede).

## 4. Architetture da assegnare (Neri — di metodo/processo, non di codice)

**ARCH1 — Gate decisionale per scommesse R&D speculative.** Non solo per S7: l'azienda farà
altre scommesse R&D in futuro (S7 non è la prima — vedi ADR-009 espansione ecosistemi). Serve
un'architettura di *decisione*, non di codice: quali criteri oggettivi dicono "continua a
investire" vs "pausa" vs "killa" per un ramo R&D, con quale cadenza si rivaluta, chi decide.
Usa `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` (ADR-006) come base — non reinventare il ciclo a 9
passi, capire se serve un gate aggiuntivo specifico per l'R&D speculativo che oggi non esiste.

**ARCH2 — Prioritizzazione capacità Gael su task P1 concorrenti.** Il segnale reale di questo
episodio: un P1 esplicito è rimasto fermo 3 giorni senza che nessuno lo segnalasse come
bloccato (perché non era bloccato — era solo dopo altro in coda). Serve un'architettura
leggera (non un tool nuovo da costruire — un metodo) per rendere visibile quando questo succede,
così la scelta "prima X poi Y" è esplicita e di Max, non implicita e scoperta 3 giorni dopo.

## 5. Perimetro

| Area | Di chi è |
|---|---|
| Ricerche R1-R3, report REP1-REP3, architetture ARCH1-ARCH2 | **Neri**, in esclusiva |
| Codice/file operativi in `12-STREAM-S7-BOT/` (le 12 sessioni del task Gael) | **Gael** — invariato, non si tocca finché Neri/Max non decidono diversamente via REP1 |
| Decisione finale su quale opzione (§3 del piano strategico) adottare | **Max**, su raccomandazione di Neri — Neri raccomanda, non decide da solo (stesso principio già scritto in [[entities/Neri]]) |

## 6. Definition of Done

- [ ] R1, R2, R3 completate con fonti verificabili citate
- [ ] REP1 scritto: una delle 4 opzioni raccomandata, motivata
- [ ] REP2 scritto: diagnosi onesta (non-convenienza vs mancanza-di-capacità)
- [ ] REP3 scritto: raccomandazione vendor dati
- [ ] ARCH1 e ARCH2: documento di metodo, non codice
- [ ] Tutto salvato in Memory (checkpoint) prima di considerarsi fatto — REGOLA ZERO

## 7. Ordine di marcia

1. Leggi `PIANO-STRATEGICO-S7.md` per intero
2. R1 → R2 → R3 (le ricerche vengono prima, i report si basano su quelle, non il contrario)
3. REP1 → REP2 → REP3
4. ARCH1 → ARCH2
5. Checkpoint finale con tutti gli output linkati, aggiorna `STATO-EMPIRE.md` con la
   raccomandazione per Max

**Se una fonte non si trova o un dato resta ignoto** (capiterà, es. R1 potrebbe non avere
precedenti pubblici verificabili): scrivilo esplicitamente come "non trovato, verificato il
—" — mai riempire il vuoto con una stima presentata come fatto.
