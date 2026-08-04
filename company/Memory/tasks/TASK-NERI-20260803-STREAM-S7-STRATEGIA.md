---
Owner: Max (committente) · Esecutore: NERI · Controllore: Claude (registra, non blocca)
Origine: 12-STREAM-S7-BOT (strato strategico) · Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO
        memory-first
Emesso: 2026-08-03 · Priorità: P1 (ordine diretto di Max)
Riferimenti: piano strategico integrale in sezione 2 di questo file (copiato da
        ../../Ecosistemi/12-STREAM-S7-BOT/PIANO-STRATEGICO-S7.md, che resta anche come file
        a sé) · STATO-RIPRESA.md (../../Ecosistemi/12-STREAM-S7-BOT/,
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
- **Il "piano strategico"** è quello alla sezione 2 qui sotto — copiato integrale (non solo
  linkato) da `PIANO-STRATEGICO-S7.md` (`12-STREAM-S7-BOT/`) apposta perché Max lo vuole tutto
  in un unico documento, non sparso tra file diversi.

**Aggiornamento 2026-08-04** (Max, di nuovo verbatim): *"tu dovresti avere il piano che neri
poi deve migliorare. I report che li deve fare, eccetera. Le ricerche che lo deve fare (...)
devi fornire a neri il piano che lui deve migliorare, analizzare, eccetera e successivamente
(...) le ricerche da fare EI report che deve fare. Procedi per favore aggiungi il tutto alla
sua task."* Fatto: piano copiato integrale in sezione 2 (non solo linkato), ricerche/report/
architetture restano sotto nello stesso file — un solo documento, come richiesto.

---

## 2. Il Piano Strategico — Neri lo studia, analizza, critica, MIGLIORA

> Testo integrale di `company/Ecosistemi/12-STREAM-S7-BOT/PIANO-STRATEGICO-S7.md` (stessa
> fonte, copiato qui perché sia tutto in un solo posto). Questo non è materiale di sfondo:
> è il primo output che Neri deve consegnare **migliorato** — non solo letto. Il piano
> originale resta anche nel file separato, come riferimento storico di partenza.

### Piano Strategico — Stream S7 (trading NFT/token)

> Questo documento NON è il task operativo (quello esiste già, è di Gael:
> `company/Memory/tasks/TASK-GAEL-20260731-STREAM-S7-NFT-SESSIONI.md`, fermo a "da avviare" da
> 3 giorni). Questo è un livello sopra: **la domanda che nessuno ha ancora risposto è se
> continuare a costruire, non come costruire.**

#### 1. Riepilogo onesto — dove siamo davvero (fatti verificati, non impressioni)

| Data | Evento | Fonte |
|---|---|---|
| 2026-07-23 | S7 approvato come R&D speculativo, 0€ nel piano revenue estate, esecuzione isolata da S1/S2 | DEC-EST-007 |
| ~2026-07-28 | Motore memecoin (Pump.fun/Raydium) chiuso: parser dati reale, position manager, fix spam. `report-studio.md`: **expectancy negativa, >85% rischio perdita capitale nel primo mese** | CP-20260728-006, report-studio.md |
| 2026-07-30 | Metodo NFT su Magic Eden costruito e verificato: 89/89 controlli reali, dati reali (non simulati) | CP-20260730-002→007 |
| 2026-07-30 | **Verdetto: INVARIATO, bocciato per live.** Solo 1 problema strutturale su 3 migliora, e solo parzialmente. Edge non distinguibile da zero al 95% di confidenza | CP-20260730-007 |
| 2026-07-31 | Max corregge il riferimento a mintify.xyz, chiede il flusso di tutte le sessioni verso l'operativo. Scritto: 12 sessioni, gate architetturale A/B/C | CP-20260731-004, TASK-GAEL-...-SESSIONI.md |
| 2026-07-31 → 2026-08-03 | **Zero sessioni del task Mintify aperte.** Resta "da avviare" | `TASK-GAEL-...-SESSIONI.md` |
| 2026-08-03 (stesso giorno di questo piano) | Gael ha chiesto ricognizione dopo fine crediti: `requirements.txt` non installabile corretto, `STATO-RIPRESA.md` riallineato. **Conclusione indipendente, stessa diagnosi**: *"non manca codice, manca una decisione"* | CP-20260803-001 |

**Il fatto che conta di più, non nascosto**: un task P1 esplicito è rimasto fermo 3 giorni. Non
per un blocco tecnico — per priorità reale. Questo è già un segnale, non solo un ritardo.
`STATO-RIPRESA.md` (riscritto lo stesso giorno, da un'altra sessione, su richiesta di Gael) è
arrivato in modo indipendente alla stessa identica conclusione — due letture separate degli
stessi fatti che convergono è un segnale più forte di una sola.

`STATO-RIPRESA.md` elenca già, con numeri reali (non stimati), i 4 prerequisiti aperti se si
andasse verso LIVE — Neri parte da questi, non li riscopre da zero:
1. RPC Solana a pagamento (`BACKLOG.md` B-010) — l'endpoint pubblico risponde 429 dopo 2
   chiamate `getTransaction`
2. Latenza misurata 2456-3624ms contro il benchmark MEV 300-800ms — non si compra, serve Jito
   bundles/bare-metal/riscrittura Rust
3. Nessun feed prezzo live — `position_monitor.py` esce su valore stimato, TP/SL non sono veri
4. Modalità LIVE non scritta — `execution_engine.py` rifiuta esplicitamente il ramo `!=
   SIMULATION`

#### 2. La domanda strategica vera

Non è "Magic Eden o Mintify". È:

> **Ha senso continuare a investire ore di ingegneria (di Gael, di Claude) in un ramo che ha
> già ricevuto due verdetti negativi consecutivi (memecoin + NFT), classificato 0€ revenue,
> mentre lo stesso ecosistema (S1/S2/Preventa/YouTube) ha lavoro reale che genera cassa e
> compete per lo stesso tempo di Gael?**

Il task Gael di 12 sessioni esiste ed è pronto — ma nessuno finora ha risposto a questa domanda
prima di scriverlo. È il gap che Neri deve colmare.

#### 3. Opzioni reali (non un'unica strada obbligata)

| Opzione | Cosa significa concretamente | Costo | Quando ha senso |
|---|---|---|---|
| **CONTINUA** | Gael esegue le 12 sessioni come scritte | Giorni di lavoro Gael sottratti a revenue | Se Neri trova un motivo concreto per cui questa volta l'esito cambierebbe |
| **PAUSA ESPLICITA** | Il task resta scritto, non si tocca, richiamato solo quando S1/S2/Preventa sono stabili | Zero, se non il tempo già investito | Se il costo-opportunità (REP2 sotto) conferma che oggi non conviene |
| **RIDEFINISCI IL BERSAGLIO** | Non "vendere sniping retail" ma altro uso dei dati NFT/on-chain (es. analytics come prodotto, non trading) | Ripensare l'obiettivo, non il codice | Se la ricerca (R1 sotto) trova che il valore reale non è nel trading |
| **KILLA** | Si archivia, si documenta il perché, si libera la capacità mentale/organizzativa | Zero futuro, si accetta la perdita del lavoro fatto | Se nessuna delle precedenti regge dopo l'analisi |

**Nessuna di queste è già decisa.** È il lavoro di Neri, prima che Gael riprenda in mano il
task operativo.

#### 4. Come Neri MIGLIORA questo piano (non solo lo esegue)

Il piano com'è oggi ha limiti che Neri deve trovare e colmare, non solo le 4 opzioni sopra
prese per buone. Almeno: (a) le 4 opzioni sono davvero esaustive o ne manca una? (b) i criteri
di "quando ha senso" nella tabella sono abbastanza oggettivi o restano vaghi? (c) manca una
soglia numerica esplicita per passare da un'opzione all'altra (es. "se costo €/mese > X, mai
CONTINUA")? La versione migliorata va scritta come nuovo file
`company/Ecosistemi/12-STREAM-S7-BOT/PIANO-STRATEGICO-S7-v2.md` (il v1 resta, non si
sovrascrive — si vede cosa è cambiato e perché).

---

## 3. Ricerche da fare (Neri — analisi/lettura, non codice)

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

## 4. Report da produrre (Neri — output scritti, gate della decisione)

**REP1 — Raccomandazione Go/No-Go.** Una delle 4 opzioni della sezione 2.3 sopra (CONTINUA /
PAUSA ESPLICITA / RIDEFINISCI IL BERSAGLIO / KILLA), motivata con R1+R2+R3 (sezione 3 sopra),
non a sensazione. Deve rispondere esplicitamente alla domanda strategica (sezione 2.2). Formato
libero, ma ogni affermazione con fonte (stesso standard già in uso su questo ecosistema: mai
un numero senza dove viene).

**REP2 — Costo-opportunità dei 3 giorni fermi.** Il task Gael è rimasto "da avviare" dal
2026-07-31 al 2026-08-03. Nello stesso periodo cos'ha fatto Gael invece (verificabile da
`git log`, checkpoint, `STATO-EMPIRE.md`)? È stata la priorità giusta? Questo report non serve
a giudicare Gael — serve a capire se il problema è "S7 non conviene" o "non c'è mai capacità
libera per S7 finché esiste lavoro revenue", che sono due diagnosi diverse con soluzioni
diverse.

**REP3 — Valutazione vendor Mintify vs alternative**, sintesi operativa di R2, con una riga di
raccomandazione finale (quale fonte dati, se una, usare se si procede).

## 5. Architetture da assegnare (Neri — di metodo/processo, non di codice)

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

## 6. Perimetro

| Area | Di chi è |
|---|---|
| Piano migliorato (v2), ricerche R1-R3, report REP1-REP3, architetture ARCH1-ARCH2 | **Neri**, in esclusiva |
| Codice/file operativi in `12-STREAM-S7-BOT/` (le 12 sessioni del task Gael) | **Gael** — invariato, non si tocca finché Neri/Max non decidono diversamente via REP1 |
| Decisione finale su quale opzione (sezione 2.3 del piano) adottare | **Max**, su raccomandazione di Neri — Neri raccomanda, non decide da solo (stesso principio già scritto in [[entities/Neri]]) |

## 7. Definition of Done

- [ ] `PIANO-STRATEGICO-S7-v2.md` scritto: piano migliorato, con cosa è cambiato e perché
      rispetto al v1 (sezione 2 sopra)
- [ ] R1, R2, R3 completate con fonti verificabili citate
- [ ] REP1 scritto: una delle 4 opzioni raccomandata, motivata
- [ ] REP2 scritto: diagnosi onesta (non-convenienza vs mancanza-di-capacità)
- [ ] REP3 scritto: raccomandazione vendor dati
- [ ] ARCH1 e ARCH2: documento di metodo, non codice
- [ ] Tutto salvato in Memory (checkpoint) prima di considerarsi fatto — REGOLA ZERO

## 8. Ordine di marcia

1. Leggi la sezione 2 (il piano) per intero, qui in questo stesso file
2. Migliora il piano → `PIANO-STRATEGICO-S7-v2.md`
3. R1 → R2 → R3 (le ricerche vengono prima, i report si basano su quelle, non il contrario)
4. REP1 → REP2 → REP3
5. ARCH1 → ARCH2
6. Checkpoint finale con tutti gli output linkati, aggiorna `STATO-EMPIRE.md` con la
   raccomandazione per Max

**Se una fonte non si trova o un dato resta ignoto** (capiterà, es. R1 potrebbe non avere
precedenti pubblici verificabili): scrivilo esplicitamente come "non trovato, verificato il
—" — mai riempire il vuoto con una stima presentata come fatto.
