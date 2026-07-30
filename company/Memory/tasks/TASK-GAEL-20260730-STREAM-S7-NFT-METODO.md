---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (gate APEX-7, su richiesta)
Origine: 12-STREAM-S7-BOT · Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first
Emesso: 2026-07-30 · Priorità: P1 (ordine diretto di Max) — classificazione ECOSISTEMA.md resta
        R&D speculativo, 0€ revenue attesa finché non passa il gate di expectancy: non sostituisce
        le priorità di cassa (S1/S2/Preventa/YouTube), lavora in parallelo.
Riferimenti: LOGICA-COMPLETA-S7.md · report-studio.md (verdetto attuale: BOCCIATO per live,
             expectancy negativa, >85% rischio perdita capitale primo mese) · APEX-7.md ·
             quality_gates.py · CP-20260728-006 (parser reale, position manager, fix spam)
---

> **STATO: ✅ CHIUSO 2026-07-30.** Tutti i lotti eseguiti (Fase 0 + Ondata 1-4 + Fase 2),
> **78/78 controlli reali superati**, zero file frozen toccati, zero capitale vero.
> **Verdetto: INVARIATO — bocciato per live**, coerente con `report-studio.md` (Controllo
> Chirurgico #2: solo 1 dei 3 problemi strutturali migliora, e solo parzialmente).
> Checkpoint: [CP-20260730-002](../checkpoints/CP-20260730-002.md) →
> [CP-20260730-007](../checkpoints/CP-20260730-007.md) (RETRO finale).

# 🚨 ORDINE MAX — Metodo logico-matematico per NFT/token (Stream S7)

## 0. Prompt originale di Max (verbatim, integrato come richiesto)

> bene so che Gael tu ha tirato fuori tutta la logica bene voglio Tutta questa logica, tutta
> tutta a parte che me la devi un attimo spiegare, voglio un file dove posso vederla tutta,
> voglio proprio un file Mk down Fin qui posso vedere un attimo tutta la logica proprio fatta
> bene e spiegata in modo semplice, compatto, veloce, tutti i passaggi, il flusso proprio il
> flusso del workflow. Ogni step che dovrà fare il flusso di tutte le varie regole che ci sono
> appunto per raggiungere gli incassi. E poi al punto bisogna vedere i rischi un attimo in
> tutto, come è stato creato la logica, lavorare sulla logica, quando la logica sarà tutta
> perfetta, ovvero sarà il metodo, quindi questa logica diventerà il metodo. A quel punto
> svilupperemo proprio in modo operativo questo botto, in modo che funzioni nella realtà.
>
> Senti tu devi creare un metodo logico matematico ed eficace - gli NFT nom token c'era un sito
> tipo magically qualcosa i cui si potevano comprare e vendere NFT.
>
> CREA UNA LOGICA PERFETTA MA NON PUOI FARLA IN UNA VOLTA MA IN TANTE TIPO 10 + 8 MIGLIORAMENTI
> + 4 PERFEZZIONAMENTI + 3 CONTROLLI CHIRURGICI
>
> questo è un piccolo flusso generico che puoi usare comunque devi calcolare analizzare
> prevedere in percentuale e ragionare su ogni dettaglio e casistica possibile...
>
> Quindi devi prima adottare una tecnica di studio e di analisi, una tecnica che crea piani di
> analisi e di studio chirurgici precisi. Per adottare quindi un intero flusso per creare un
> piano che dovrà come sempre avere 7 miglioramenti con questa logica di ragionamento: apex7
> ecc... poi con /content-forge + gh repo clone ansjkfgheqrlg/master-build-architecture
>
> ora a tutto questo ci pensa Gael questa è la task di Gael quindi lui fare partire tutto
> questo lui lo gestirà lui continuerà.

**Nota di Claude (trasparenza, non censura del prompt):** il testo sopra è dettato/trascritto,
con ripetizioni e refusi — riportato integrale come richiesto, senza correggerlo. Sotto è la
mia interpretazione operativa, esplicitamente separata dall'originale così Gael (o Max) può
correggermi dove ho letto male.

## 1. Interpretazione operativa (Claude → Gael, da confermare/correggere in corsa)

- **"Sito tipo magically qualcosa dove si comprano/vendono NFT"** → quasi certamente **Magic
  Eden** (magiceden.io), il marketplace NFT dominante su Solana — coerente con lo stack S7 già
  Solana-nativo (`data_manager.py` ascolta già il mempool Solana). Se Max intendeva un altro
  sito, correggi qui prima di partire: cambia le API da integrare ma non la struttura del
  metodo sotto.
- **Il "flusso per raggiungere gli incassi"** richiesto nel primo messaggio è già coperto da
  [LOGICA-COMPLETA-S7.md](../../Ecosistemi/12-STREAM-S7-BOT/LOGICA-COMPLETA-S7.md) (flusso,
  rischi, regole, bug già trovati) — non richiedere di nuovo, è già scritto e loggato
  (`second-brain-vault/wiki/log.md`, voce 2026-07-30 "CORREZIONE — Stream S7"). Questo task è
  il **passo successivo**: da "logica descritta" a "metodo logico-matematico verificato",
  applicato allo **scambio NFT su marketplace** (Magic Eden) in aggiunta/parallelo al motore
  memecoin (Pump.fun/Raydium) già costruito da G-A/G-B/G-C.
- **Punto che NON si aggira**: `report-studio.md` ha già emesso un verdetto — expectancy
  negativa, >85% probabilità di perdere il capitale nel primo mese, per il motivo strutturale
  di latenza/RPC/rug-pull spiegato lì. Il "metodo perfetto" richiesto qui deve o (a) risolvere
  concretamente uno o più di quei problemi strutturali con numeri veri, oppure (b) concludere
  di nuovo onestamente che non regge — **mai forzare un risultato positivo per compiacere**.
  Il Controllo Chirurgico #2 sotto esiste apposta per questo.

---

## 2. FASE 0 — Tecnica di studio e analisi (prima di tutto, 7 miglioramenti stile APEX-7)

Come chiesto esplicitamente da Max: prima di costruire il metodo NFT, costruisci **il modo in
cui lo si studia/analizza/prevede**. Non è burocrazia — è lo stesso principio già in
`analysis_engine.py` (la soglia non è "a numero scelto a mano", si calibra sui dati) applicato
al *processo di ricerca*, non solo al codice.

Riusa la logica APEX-7 già presente in questo stesso ecosistema (`quality_gates.py`,
`gate_verifiers.py`): ogni miglioramento è un piccolo gate con criterio verificabile, non
un'affermazione.

| # | Miglioramento della tecnica di studio | Criterio di gate (deve essere vero per passare) |
|---|---|---|
| 1 | Definizione dell'oggetto di studio | La domanda a cui il metodo deve rispondere è scritta in una frase misurabile (es. "expectancy per trade in % del capitale allocato"), non generica |
| 2 | Fonte dei dati dichiarata | Ogni numero usato ha una fonte citata (API Magic Eden, RPC Solana, dati storici) — nessun numero "a sensazione" |
| 3 | Unità di misura coerente | Tutto in SOL o € con tasso dichiarato, mai mischiare unità senza conversione esplicita |
| 4 | Casistiche enumerate | Lista esplicita degli scenari (successo, fallimento per illiquidità, fallimento per rug, fallimento per fee, fallimento per latenza) — non solo il caso positivo |
| 5 | Percentuali con intervallo, non solo media | Ogni stima riporta anche la varianza/intervallo di confidenza, non un singolo numero ottimistico |
| 6 | Confronto con un baseline noto | Ogni nuova stima si confronta con quanto già misurato in `report-studio.md`/CP-20260728-006 (non riparte da zero come se non esistesse storia) |
| 7 | Criterio di stop dichiarato | Prima di iniziare a costruire, è scritto ESPLICITAMENTE cosa farebbe fallire il metodo (soglia di expectancy minima sotto la quale si scarta, come già fa `report-studio.md`) |

**Gate FASE 0**: 7/7 devono essere PASS prima di passare alla Fase 1. Se uno fallisce 3 volte,
applica il protocollo di escalation già documentato in `APEX-7.md` (FREEZE → DIAGNOSE →
STRATEGY CHANGE → LOG → RETRY → umano).

---

## 3. FASE 1 — Il metodo, in 4 ondate (10 + 8 + 4 + 3 = 25 passaggi)

Non tutto insieme. Un pezzo alla volta, ognuno con **output verificabile** (numero, formula,
test), mai solo descrizione testuale — stesso principio già rispettato da `analysis_engine.py`
(parser dati reale, non regex su testo finto) e da `risk_manager.py` (drawdown letto dal log
vero, non dichiarato).

### ONDATA 1 — 10 Blocchi fondamentali (costruzione)

Ogni blocco = un modulo o una formula, con un test/numero reale a fine blocco, non "dovrebbe
funzionare".

1. **Edge dichiarato**: cosa si sfrutta esattamente — mismatch floor-price/rarity su Magic
   Eden (listing sottoprezzato rispetto al rank di rarità), non lo stesso edge memecoin già
   coperto da `analysis_engine.py`. Scrivi la frase precisa, è il criterio 1 della Fase 0.
2. **Fonte dati Magic Eden**: quali endpoint API (listings, activities, collection stats),
   rate limit, costo, se serve API key.
3. **Modello di fair value**: formula che stima il prezzo "giusto" di un NFT dato il suo rank
   di rarità nella collection (es. regressione su vendite storiche della collection).
4. **Soglia di ingresso statistica**: come `spike_threshold_sol` in `analysis_engine.py` ma
   per il mismatch NFT — calibrata sui dati, non a mano.
5. **Modello di costo reale**: fee marketplace Magic Eden (~2%), royalty creator, gas Solana,
   priority fee — edge netto dopo costi, non lordo.
6. **Modello di liquidità**: tempo medio storico per rivendere un NFT di quella collection
   (non solo il floor — un NFT può restare invenduto settimane, capitale bloccato).
7. **Position sizing**: quanto capitale allocare per trade, coerente con `RiskManager`
   esistente (stesso `max_position_pct`, non un sistema parallelo scollegato).
8. **Simulazione Monte Carlo**: expectancy simulata su dati storici di almeno N collection
   reali, prima di qualsiasi paper trading live.
9. **Integrazione architetturale**: nuovo layer (es. `nft_analysis_engine.py`) che pubblica/
   ascolta sull'Event Bus esistente — **non duplica** `RiskManager`/`PositionMonitor`, li
   riusa (stesso principio "file congelati" di `TASK-GAEL-20260728-STREAM-S7-BOT.md` §3).
10. **Paper trading dedicato**: log CSV separato per NFT (meccanica diversa da memecoin — qui
    non c'è mempool-sniping in senso stretto, è "listing sniping" su un marketplace con order
    book visibile).

### ONDATA 2 — 8 Miglioramenti (dopo che i 10 blocchi esistono e girano)

Non prima. Ogni miglioramento parte da un numero misurato nell'Ondata 1 e lo migliora,
documentando prima/dopo.

1. Auto-calibrazione della soglia di ingresso sui risultati reali (stesso pattern feedback
   loop già in `analysis_engine._on_trade_closed`).
2. Filtro anti-wash-trading (volume falso, comune sui marketplace NFT — gonfia la liquidità
   apparente).
3. Filtro anti-scam-collection (contratto verificato, storico del creator, età della
   collection).
4. Segmentazione del success-rate per fascia di prezzo (floor basso vs floor alto si
   comportano diversamente — non un unico numero medio).
5. Latenza reale detection→acquisto su Magic Eden (API vs interfaccia web) — misurata, non
   assunta.
6. Correlazione tra collection in portafoglio (evita concentrazione di rischio su
   collection correlate).
7. Tracciamento PnL reale per collection (non solo aggregato — serve per capire cosa
   funziona e cosa no).
8. Kill-switch specifico NFT (es. floor crolla oltre X% in Y minuti → stop, stesso principio
   del kill-switch già in `RiskManager.activate_kill_switch`).

### ONDATA 3 — 4 Perfezionamenti

1. Backtest su dati storici reali di più collection (non simulazioni astratte).
2. Stress test su scenari avversi (crash di mercato, rug, marketplace irraggiungibile).
3. Intervallo di confidenza sulle stime di expectancy, non solo la media puntuale.
4. Ogni percentuale nel report finale cita la fonte del dato — stesso standard già applicato
   in `report-studio.md` e nei checkpoint di questo ecosistema (mai un numero inventato).

### ONDATA 4 — 3 Controlli chirurgici (audit finale, indipendente da chi ha costruito)

1. **Controllo matematico indipendente**: ricalcolo delle formule di expectancy da zero,
   in un modulo/test separato — non fidarsi del codice che le ha prodotte.
2. **Controllo di coerenza con `report-studio.md`**: se il nuovo metodo conclude diversamente
   (expectancy positiva), deve spiegare ESATTAMENTE quale dei problemi strutturali già trovati
   (latenza 300-800ms, RPC pubblico che rate-limita dopo 2 chiamate, rug pull) risolve e come.
   Se non lo spiega, il verdetto resta quello già scritto: bocciato per live.
3. **Gate APEX-7 L1→L7** applicato a questo nuovo modulo (Claude fa da controllore su
   richiesta, stesso ruolo già avuto su G-A/G-B/G-C — vedi CP-20260728-006).

---

## 4. FASE 2 — Content-forge + repo esterno

Dopo che Fase 0 e Fase 1 hanno un primo giro completo (anche solo Ondata 1):

```bash
gh repo clone ansjkfgheqrlg/master-build-architecture
```

Poi usa `/content-forge` per far confluire i pattern architetturali di quel repo nel metodo
NFT appena costruito — stesso uso già fatto altrove in questo repo (vedi riferimento
`master-build-architecture` in `CP-20260721-002`, skill `youtube-automation-factory`: non è la
prima volta che questo pattern viene usato qui).

**Non verificato da me**: non ho controllato che il repo esista/sia raggiungibile (azione di
rete che spetta a chi esegue, non a chi scrive il task). Se `gh repo clone` fallisce, non
indovinare un nome alternativo — segnalalo in `STATO-EMPIRE.md` con l'errore esatto e prosegui
sul resto del task.

---

## 5. Perimetro — cosa non si tocca

| Area | Di chi è |
|---|---|
| `event_bus.py`, `memory_interface.py`, `quality_gates.py`, `gate_verifiers.py`, `gate_agent.py`, `meta_agent.py`, `orchestrator.py`, `ruflo_adapter.py`, `apex7_workflow.ruflo.yaml`, `prompts/**` | Claude — fondazione APEX-7 condivisa. Estendibile (nuovo evento nel catalogo), non riscrivibile senza nota `⚠️ COORDINAMENTO` |
| `analysis_engine.py`, `risk_manager.py`, `execution_engine.py`, `position_monitor.py` (motore memecoin già chiuso G-A/G-B/G-C) | Non toccare la logica esistente — il nuovo layer NFT si affianca, non sostituisce |
| `execution_engine.py` lato modalità LIVE | **Nessuno senza ordine esplicito di Max** — resta paper trading fino al PASS del gate L5 |
| Nuovo, in esclusiva di questo task | `nft_analysis_engine.py` (o nome equivalente), qualunque nuovo modulo NFT, sezione dedicata in `report-studio.md` o nuovo file `report-studio-nft.md` |

## 6. Regole operative (invariate rispetto al task precedente su questo ecosistema)

1. Paper trading resta l'unica modalità eseguita. Nessuna chiave privata vera, mai in chiaro.
2. Windows-first: zero emoji nei `print()`/log — console cp1252, già causa di crash in passato.
3. Prova, non dichiarazione: ogni blocco/miglioramento/perfezionamento/controllo si chiude con
   comando + output reale incollato nel checkpoint, non "dovrebbe funzionare".
4. ADR-006 ciclo a 9 passi per ogni ondata: RECALL → SPEC → PRE-MORTEM → BUILD → GATE → REVIEW
   → TEST → COMMIT → RETRO.
5. `python test_apex7.py` deve restare verde (13/13) prima e dopo ogni ondata.
6. Task chiuso (anche parzialmente, per ondata) → checkpoint in
   `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md`.
7. Item minori → `company/Memory/BACKLOG.md` (ADR-005), non fermare la costruzione.

## 7. Definition of Done

- [x] Fase 0: 7/7 criteri della tecnica di studio verificati, non solo dichiarati
      → `STUDIO-NFT-FASE0.md`, ogni criterio con comando/risposta reale (API Magic Eden, RPC
      Solana, CoinGecko). Criterio 7 (stop) scritto PRIMA di costruire.
- [x] Ondata 1: 10 blocchi costruiti, ognuno con un test/numero reale
      → `python test_nft_s7.py` **25/25 OK**. `nft_magiceden_client.py`, `nft_analysis_engine.py`,
      `nft_monte_carlo.py`. Expectancy MC su degods 20.31%, IC95% [-2.00%, 34.70%].
- [x] Ondata 2: 8 miglioramenti applicati, ognuno con prima/dopo misurato
      → `python test_nft_ondata2.py` **21/21 OK**. Es. z 1.5→1.35; fit banda bassa mad_lads
      R² 0.0400→0.2825; kill-switch floor-crash che riusa `RiskManager` e scatta davvero.
- [x] Ondata 3: 4 perfezionamenti, backtest reale incluso
      → `python test_nft_ondata3.py` **10/10 OK**. Backtest su 3 collection (solo 1/3 dà
      segnale), stress test, rug-pull breakeven 16.9%, bootstrap R² (fit instabile).
- [x] Ondata 4: 3 controlli chirurgici superati, incluso il confronto esplicito con
      `report-studio.md`
      → `python test_nft_ondata4.py` **15/15 OK**. Ricalcolo indipendente combacia; confronto
      numerico problema-per-problema; Gate APEX-7 `L3_TO_L4` reale **PASSED 6/6 score 1.0**.
- [x] Fase 2: repo clonato (o errore documentato) + `/content-forge` applicato
      → `gh repo clone ansjkfgheqrlg/master-build-architecture` riuscito (252 file).
      **`/content-forge` NON esiste in questo ambiente** — segnalato invece che indovinato
      (CP-20260730-006); applicati concretamente i suoi principi P09/P12 → `FAILURE-MODES-NFT.md`.
- [x] `python test_apex7.py` verde a fine lavoro → **13/13, `PASSED score 1.0`**, riverificato
      anche dopo il merge con `origin/main`.
- [x] Zero modifiche al motore memecoin già chiuso (G-A/G-B/G-C) e a `execution_engine.py`
      lato LIVE
      → verificato con `git diff origin/main --stat` sui 12 file frozen: **output vuoto**.
- [x] Checkpoint con comandi e output reali per ogni ondata
      → CP-20260730-002/003/004/005/006/007 (uno per fase + RETRO finale).

## 8. Ordine di marcia

1. `git pull` → verifica `python test_apex7.py` verde (13/13) prima di toccare qualunque cosa
2. Leggi `LOGICA-COMPLETA-S7.md`, `report-studio.md`, `APEX-7.md` in questo stesso ecosistema
3. **Fase 0** (tecnica di studio, 7 miglioramenti) → gate → commit
4. **Fase 1 / Ondata 1** (10 blocchi) → gate → commit
5. **Fase 1 / Ondata 2** (8 miglioramenti) → gate → commit
6. **Fase 1 / Ondata 3** (4 perfezionamenti) → gate → commit
7. **Fase 1 / Ondata 4** (3 controlli chirurgici, incluso confronto con report-studio.md) →
   commit
8. **Fase 2** (`gh repo clone` + `/content-forge`) → commit
9. Checkpoint finale + RETRO + push

**Se qualcosa non torna** (API Magic Eden ambigua, dato mancante, repo irraggiungibile):
**non indovinare**. Scrivi il problema con comando esatto + errore esatto in
`company/Memory/STATO-EMPIRE.md` e prosegui sull'ondata successiva dove possibile.
