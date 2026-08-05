---
Owner: Max (committente) · Esecutore: NERI (progettazione via Arena) → Claude/Gael (build) ·
        Controllore: Claude (gate APEX-7)
Origine: 12-STREAM-S7-BOT + 13-ARENA-APEX · Governo: ADR-006 (ciclo 9 passi) + PIANO-MAESTRO/
        27-ARENA-WORKFLOW-COMPLETO-METODO.md (metodo, non da reinventare) + REGOLA ZERO
        memory-first
Emesso: 2026-08-05 · Priorità: P1 (ordine diretto di Max)
Riferimenti: PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md (il metodo Arena→Workflow,
        leggilo per intero, questo task lo applica) · 13-ARENA-APEX/ECOSISTEMA.md (Regola APEX)
        · TASK-NERI-20260803-STREAM-S7-STRATEGIA.md (l'ALTRO task di Neri, leggi §"Tensione da
        risolvere" sotto — non sono la stessa cosa ma si toccano) · LOGICA-COMPLETA-S7.md ·
        CP-20260730-007 (verdetto NFT) · report-studio.md
---

> **STATO: da avviare.**

# 📋 TASK NERI — Progetta con Arena una "fabbrica di strategie" per Stream S7

## 0. Prompt originale di Max (verbatim, integrato come richiesto)

> Ok, in questi giorni ho avuto modo di realizzare quanto sia potente Arena, quindi voglio che
> dare un compito d'aria estremamente potente, ovvero oglio creare un workflow con arena Un
> morfolo che serva proprio per questo, per creare il volte in FT, quindi un prof. Facciamo un
> workflow che appunto facciamo qualcosa di bellissime azioni, tantissime cose o il workflow
> che fa le azioni Quindi diciamo quello che fa tutta l'operatività oppure facciamo il workflow
> che mantiene tutte le strategie e crea vari tipi di agenti per ogni strategia, facciamo
> meglio questo con l'arena, quindi voglio che mi direi un piano per farlo con un piano intendo
> semplicemente un prompt completo Che sia appunto una base per iniziare a creare questo
> workflow con l'arena Devi considerare che Alino non sa niente di questo, quindi devi dare
> tutto il contesto massimo che puoi fare tutto il prompt Successivamente io passerò tutto
> questo prompt a Neri che gestirà anche questa Task

**Nota di Claude (trasparenza, non censura del prompt)**: testo dettato, con refusi
("Alino" quasi certamente Arena o Neri stesso — non si capisce con certezza da chi lo riceve,
ma l'istruzione è chiara comunque: chi lo riceve non sa nulla, quindi contesto massimo).
Interpretazione sotto, separata.

## 1. Interpretazione operativa (Claude → Neri/Max, da confermare/correggere in corsa)

- **Le "due" opzioni del prompt non sono in conflitto** — le ho lette come un solo concetto a
  due livelli, non un bivio da scegliere:
  - "il workflow che fa le azioni... tutta l'operatività" = cosa fa OGNI agente generato
  - "il workflow che mantiene tutte le strategie e crea vari tipi di agenti per ogni strategia"
    = cosa fa il WORKFLOW nel suo complesso (il livello meta, la fabbrica)
  Sintesi: costruiamo una **fabbrica di strategie** — un workflow che mantiene un catalogo di
  strategie di trading (oggi: 2 già esistenti, memecoin e NFT — vedi §2) e per ognuna genera/
  mantiene un **agente operativo dedicato**, che a sua volta fa tutta l'operatività di quella
  singola strategia (ingest dati → segnale → check rischio → esecuzione → uscita posizione).
  Se questa lettura è sbagliata, correggi prima di incollare il prompt in Arena (sezione 5).
- **"Alino"**: chiunque sia, l'istruzione vale due volte — sia per Arena (che non ha memoria di
  questa azienda tra una sessione e l'altra, va sempre ricontestualizzata da zero) sia per Neri
  (che non ha mai lavorato su Stream S7 finora). Per questo il prompt in sezione 5 è
  interamente autosufficiente: non presuppone che chi lo legge abbia letto altro prima.
- **Tensione da risolvere, segnalata non nascosta**: Neri ha già un altro task aperto,
  `TASK-NERI-20260803-STREAM-S7-STRATEGIA.md`, che valuta se Stream S7 vada CONTINUATO, messo
  in PAUSA, RIDEFINITO o KILLATO — raccomandazione (REP1) non ancora consegnata. Questo nuovo
  task (progettare la fabbrica di strategie con Arena) **può procedere in parallelo senza
  aspettare REP1**, perché Arena progetta soltanto (MKD, spec, prompt di build — non tocca
  credenziali, non esegue, non alloca capitale, Regola già scritta in `13-ARENA-APEX/
  ECOSISTEMA.md`). Ma gli agenti che questa fabbrica genererà **non vanno collegati
  all'esecuzione reale/LIVE finché REP1 non è consegnato e Max non decide** — stesso vincolo
  già attivo sui due agenti-strategia esistenti (memecoin, NFT): restano paper trading.

---

## 2. Contesto — cosa esiste già (Neri parte da qui, non da zero)

**Stream S7** (`company/Ecosistemi/12-STREAM-S7-BOT/`) è il bot di trading Solana dell'azienda,
governato dal sistema nervoso **APEX-7** (agenti, quality gate a 7 livelli, event bus,
memoria). Oggi gira **solo in paper trading**, mai soldi veri.

**Due strategie già costruite e testate**, ognuna con il proprio "agente" (in senso lato: un
insieme di moduli Python collegati sull'Event Bus APEX-7):

| Strategia | Moduli | Stato test | Verdetto commerciale |
|---|---|---|---|
| **Memecoin volume-spike** (Pump.fun/Raydium) | `analysis_engine.py`, `risk_manager.py`, `execution_engine.py`, `position_monitor.py` | 13/13 test verdi, gate APEX L6→L7 PASSED 7/7 | `report-studio.md`: expectancy **negativa**, >85% rischio perdita capitale primo mese |
| **NFT floor-rarity mismatch** (Magic Eden) | `nft_analysis_engine.py`, `nft_monte_carlo.py`, `nft_ondata2-4.py` | 89/89 controlli reali | `CP-20260730-007`: **INVARIATO, bocciato per live** — edge non distinguibile da zero al 95% di confidenza |

Entrambe passano dallo stesso schema a 5 layer: **Data Manager → Analysis Engine → Risk
Manager → Execution Engine → Position Monitor**, comunicano solo via Event Bus (mai chiamate
dirette), e sono governate dagli stessi Quality Gate APEX-7 (L1→L7, soglie oggettive, vedi
`APEX-7.md`).

**Il problema che questo nuovo task risolve**: oggi, per aggiungere una TERZA strategia
(es. arbitraggio cross-DEX, sniping su un'altra chain, altro), bisognerebbe scrivere di nuovo a
mano tutti e 5 i layer da capo. Una **fabbrica di strategie** dovrebbe invece: (a) tenere un
catalogo delle strategie (esistenti + future), (b) generare per ognuna un agente operativo
completo (i 5 layer, cablati su APEX-7, con paper trading di default), (c) far sì che
aggiungere una strategia nuova sia un processo ripetibile, non una riscrittura da zero.

---

## 3. Il metodo — Arena → Workflow Completo (già scritto, non reinventarlo)

Leggi per intero `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md` prima di incollare
qualunque cosa in Arena. Riassunto minimo:

- **Arena** (LMArena.ai) è il cervello di progettazione: produce MKD (Master Knowledge
  Document), PLAN-v1, prompt di build. **Non esegue, non tocca credenziali, non pubblica.**
- **master-build-architecture** è la skill che Arena usa per progettare architetture
  multi-agente: ogni agente ha 7 file canonici (spec, system-prompt, tools, playbook, evals,
  failure-modes, memory).
- **APEX-7 è un vincolo non negoziabile** (Regola APEX, `13-ARENA-APEX/ECOSISTEMA.md`):
  *"Nessun agente esce dall'Arena senza aver integrato e testato la Skill APEX-7 nel proprio
  ciclo vitale."*
- **Il loop**: Max/Neri dà l'obiettivo ad Arena → Arena produce MKD+PLAN-v1+prompt di build →
  Claude Code (locale) costruisce nel ciclo a 9 passi (ADR-006) → Arena fa review indipendente
  (passo 5 del ciclo) → Claude committa (CP + STATO-EMPIRE + registro) → push.

---

## 4. Cosa deve fare Neri, concretamente

1. Legge questo file per intero (contesto già tutto qui, sezioni 2-3 sopra)
2. Apre Arena.ai, incolla il prompt della sezione 5 sotto **esattamente com'è** (è già
   completo — se manca qualcosa Arena farà domande, quello è normale, fase `ASK` del metodo)
3. Arena restituirà: MKD, PLAN-v1 (N agenti-strategia + il layer "fabbrica" che li genera/
   gestisce), un prompt di build, un pre-mortem (3+ modi in cui questo fallisce)
4. Se il PLAN-v1 non convince (troppo vago, manca concretezza): usa `ASK`→`CRITIQUE`→`PLAN-v2`
   (§A3 del metodo) — non accettare il primo output se non ha numeri/criteri misurabili
5. Consegna il prompt di build finale a Max, che lo passa a Claude Code/Gael per la Fase B
   (costruzione reale, fuori da questo task — Neri non scrive codice, coerente col suo ruolo)
6. Checkpoint con l'output di Arena allegato (MKD+PLAN-v1+prompt di build+pre-mortem)

---

## 5. IL PROMPT — da incollare in Arena.ai (completo, autosufficiente)

```
Sei l'architetto di un workflow completo per Digital Empire (agenzia AI multi-business che
gestisce, tra le altre cose, un bot di trading crypto sperimentale chiamato "Stream S7").

CONTESTO COMPLETO (non hai memoria di sessioni precedenti, leggi tutto prima di rispondere):

Digital Empire ha costruito un bot di trading Solana ("Stream S7") governato da un sistema
nervoso multi-agente chiamato APEX-7: 7 livelli di maturità, 6 quality gate con soglie
oggettive (es. gate finale richiede 7/7 criteri verificati eseguendo codice, non dichiarati),
un Event Bus publish-subscribe con priorità e retry, una memoria con 5 tipi di query
(recall/decision/strategy/write/forget). Tutto questo esiste già, è testato, è verde.

Sopra questo sistema nervoso girano oggi 2 "strategie" di trading, ognuna implementata come una
catena di 5 moduli che si parlano SOLO via Event Bus (mai chiamate dirette tra loro):
1. Data Manager — ingest dati grezzi (es. mempool blockchain)
2. Analysis Engine — rileva un segnale di opportunità (es. anomalia di volume) e lo pubblica
3. Risk Manager — unico cancello tra "ho trovato un segnale" e "eseguo davvero": controlla
   drawdown, limite posizioni aperte, kill-switch. Approva o rifiuta, mai bypassato
4. Execution Engine — esegue (oggi solo in simulazione/paper trading, mai capitale vero)
5. Position Monitor — sorveglia le posizioni aperte, chiude su take-profit/stop-loss

Le 2 strategie esistenti (memecoin volume-spike su Solana, NFT floor-price-mismatch su un
marketplace NFT) sono state costruite scrivendo a mano, ogni volta, tutti e 5 questi moduli da
capo. Entrambe sono tecnicamente solide (test automatici tutti verdi, gate di qualità superati)
ma **commercialmente bocciate per l'uso con capitale vero** da due analisi indipendenti
(problemi strutturali: latenza contro bot istituzionali, costo di infrastruttura, edge
statistico non distinguibile dal rumore). Restano quindi laboratori di paper trading, non
prodotti in produzione — questo NON è compito tuo da risolvere, è già stato analizzato altrove.

IL TUO COMPITO: progetta un workflow — la "S7 Strategy Factory" — che risolva un problema
diverso, architetturale: oggi aggiungere una TERZA strategia di trading richiede riscrivere a
mano tutti e 5 i moduli da zero. Voglio invece una fabbrica che:

1. Mantenga un CATALOGO di strategie (dati: nome, tipo di segnale che cerca, fonte dati,
   parametri di rischio, stato: attiva/paper/archiviata)
2. Per ogni strategia nel catalogo, GENERI un agente operativo completo che implementi i 5
   layer sopra (Data Manager/Analysis Engine/Risk Manager/Execution Engine/Position Monitor)
   specifico per quella strategia, ma condividendo l'infrastruttura comune (Event Bus, sistema
   di memoria, Risk Manager centrale con i suoi limiti — NON un Risk Manager duplicato per
   ogni strategia, uno solo condiviso, altrimenti i limiti di esposizione totale non hanno
   senso)
3. Renda ripetibile il processo "aggiungi una strategia nuova": oggi è una riscrittura, deve
   diventare un processo con input strutturato (spec della strategia) e output un agente
   pronto, testato, gated

USA IL METODO master-build-architecture: produci prima un Master Knowledge Document (MKD) di
questo workflow ("S7 Strategy Factory"), poi un PLAN-v1.

Il PLAN-v1 deve includere:
- N agenti specializzati (agent swarm, non un monolite) con 7 file canonici ciascuno: spec.md,
  system-prompt.md, tools.md, playbook.md, evals.md, failure-modes.md, memory.md — incluso
  almeno un "Factory Agent" (mantiene il catalogo, orchestra la generazione di nuovi
  agenti-strategia) e la definizione di cosa contiene esattamente un "agente-strategia" tipo
- Skill eseguibili (non solo prompt) per ogni step ripetibile del processo di generazione
- Flussi/automazioni event-driven, non a chiamata manuale dove possibile
- Memory ecosystem da subito: checkpoints/, decisions/, sessions/, plans/, MEMORY-INDEX.md
- OBBLIGATORIO: integrazione APEX-7 come layer di ragionamento/quality-gate — ogni
  agente-strategia generato deve avere un gate APEX-7 nel suo ciclo vitale PRIMA di essere
  considerato operativo, non aggiunto dopo
- OBBLIGATORIO: ogni agente-strategia generato nasce in modalità paper-trading/simulazione, MAI
  collegato a capitale vero per default — il passaggio a esecuzione reale è un gate separato,
  esplicito, mai automatico
- Come il Risk Manager centrale (condiviso, non duplicato) impone limiti aggregati su TUTTE le
  strategie insieme (es. mai più del 20% del capitale totale allocato attraverso tutte le
  strategie attive insieme), non solo per singola strategia

Segui il ciclo Empire a 9 passi (RECALL→SPEC→PRE-MORTEM→BUILD→GATE→REVIEW→TEST→COMMIT→RETRO) —
tu (Arena) fai review indipendente al passo 5, Claude Code locale costruisce.

Prima di consegnare il PLAN-v1, scrivi un PRE-MORTEM: almeno 3 modi concreti in cui questa
fabbrica di strategie fallisce nella pratica (es: gli agenti generati si assomigliano troppo e
non catturano davvero edge diversi; il Risk Manager centrale diventa un collo di bottiglia; la
generazione automatica produce codice che passa i test ma non ha logica di trading sensata) —
per ognuno, una contromisura concreta nel design, non una frase generica.

Fai domande se qualcosa non è chiaro (fase ASK del metodo) prima di produrre un PLAN-v1 vago.
```

---

## 6. Perimetro

| Area | Di chi è |
|---|---|
| Incollare il prompt in Arena, iterare ASK/CRITIQUE, consegnare l'output | **Neri**, in esclusiva |
| Costruzione reale (Fase B: codice, test, integrazione APEX-7) del PLAN-v1 che Arena produce | **Claude Code/Gael**, dopo, task separato — Neri non scrive codice |
| Decisione se/quando gli agenti-strategia generati toccano esecuzione reale | **Max**, dopo REP1 di `TASK-NERI-20260803-STREAM-S7-STRATEGIA.md` — mai automatico |

## 7. Definition of Done

- [ ] Prompt incollato in Arena, output ricevuto (MKD + PLAN-v1 + prompt di build + pre-mortem)
- [ ] Se il primo output è vago: almeno un giro ASK→CRITIQUE→PLAN-v2 fatto
- [ ] Pre-mortem con almeno 3 failure mode concreti + contromisura, non generico
- [ ] Vincolo paper-trading-by-default verificato presente nel PLAN-v1 (non assunto — controllato)
- [ ] Checkpoint scritto con l'output completo di Arena allegato/linkato
- [ ] `STATO-EMPIRE.md` aggiornato: prompt di build pronto, in attesa che Max/Claude aprano la
      Fase B

## 8. Ordine di marcia

1. Leggi questo file per intero (già autosufficiente)
2. (Opzionale ma consigliato) leggi `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md` per
   il metodo completo dietro questo task
3. Incolla il prompt di sezione 5 in Arena.ai
4. Itera se serve (ASK/CRITIQUE/PLAN-v2)
5. Checkpoint con output allegato → aggiorna `STATO-EMPIRE.md` → consegna a Max
