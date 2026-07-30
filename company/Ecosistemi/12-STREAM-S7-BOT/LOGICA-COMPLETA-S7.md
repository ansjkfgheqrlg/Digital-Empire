# Stream S7 — Logica Completa del Sistema (bozza del Metodo)

> Correzione: la versione precedente di questo documento era stata scritta per
> il sistema sbagliato (Preventa/outreach). Questa è quella giusta: il bot di
> trading Solana NFT/memecoin (Stream S7), governato dal sistema nervoso
> APEX-7, entrambi in `company/Ecosistemi/12-STREAM-S7-BOT/`.

## Overview — cosa è, cosa NON è ancora

**Stream S7** è un bot che ascolta il mempool di Solana in tempo reale, cerca
spike di volume anomali su token/NFT appena nati (Pump.fun, Raydium), e prova
a comprare prima che il prezzo salga ("sniping"). Oggi gira **solo in Paper
Trading** (soldi finti, log su CSV) — non ha mai toccato un wallet vero.

**Verdetto ufficiale già emesso** (`report-studio.md`, mandato GEM-07):
**BOCCIATO per produzione Live in questa forma.** Expectancy netta stimata
**negativa**, probabilità di perdere l'intero capitale di rischio **>85% nel
primo mese**. Motivo in breve più sotto (sezione Rischi). Per adesso S7 è
**R&D speculativo, 0€ revenue attesa** — non è un percorso verso incassi, è un
laboratorio. Il denaro vero, per ora, sta su S1/S2, non qui.

**Stato tecnico attuale**: APEX-7 (il sistema nervoso che orchestra e valida
il lavoro) è a **Level 2 operativo, testato, verde** (`test_apex7.py`
13/13). Il bot di trading vero e proprio (5 layer sotto) è collegato al Level
2 e ha superato il gate `L3_TO_L4` sui suoi dati reali. Prossimo livello:
L3→L4 consolidato su più dati, poi L4-L7 (non ancora costruiti, ma già
specificati con criteri misurabili).

---

## Le due metà del sistema

Ci sono **due logiche separate che si parlano**:

1. **APEX-7** — il sistema nervoso/metodo di lavoro: come si costruisce,
   verifica e fa evolvere il codice in sicurezza (agenti, gate, memoria,
   event bus). Non fa trading, governa *come* si costruisce chi fa trading.
2. **Il bot S7** — 5 layer che fanno il trading vero (in simulazione): Data
   Manager → Analysis Engine → Risk Manager → Execution Engine → Position
   Monitor.

I due si incontrano sull'**Event Bus**: i layer del bot pubblicano/ascoltano
eventi esattamente come farebbe un agente APEX-7.

---

## Mappa dei file

```
company/Ecosistemi/12-STREAM-S7-BOT/
├── main.py                  avvia il bot, cablaggio dei 5 layer sull'Event Bus
├── data_manager.py          Layer A — ascolto WebSocket mempool Solana
├── analysis_engine.py       Layer B — parser transazioni + rilevazione spike
├── risk_manager.py          Layer D — approvazione trade, limiti, kill-switch
├── execution_engine.py      Layer C — esecuzione (simulata) + log paper trade
├── position_monitor.py      Layer E — uscita TP/SL sulle posizioni aperte
├── event_bus.py             bus P0-P3, retry, DLQ, 19+ eventi catalogati
├── memory_interface.py      5 query, indice invertito, checkpoint/restore
├── orchestrator.py / gate_agent.py / meta_agent.py / worker_agent.py   APEX-7
├── quality_gates.py + gate_verifiers.py   6 gate L1→L7, criteri con rubrica
├── paper_trade_log.csv      log reale di ogni trade simulato
├── report-studio.md         verdetto ufficiale expectancy (bocciato per live)
├── APEX-7.md                documentazione del sistema nervoso
└── STATO-RIPRESA.md         dove riprendere il lavoro
```

---

## Il flusso di trading, passo per passo

```
1. DATA MANAGER (Layer A)
   Si iscrive via WebSocket al Program ID di Pump.fun su Solana
   (logsSubscribe, commitment "processed"). Ogni log ricevuto →
   pubblica "data.raw_event_received" sul bus.
   Senza SOLANA_WSS_URL configurato → genera un mock stream (per test offline).

2. ANALYSIS ENGINE (Layer B) — il cervello
   Riceve l'evento grezzo (solo firma + log testuali, MAI gli account).
   Chiama getTransaction sull'RPC per leggere la transazione vera:
     - volume in SOL = maggior variazione di lamports tra preBalances/postBalances
     - token address = mint (≠ Wrapped SOL) con maggior variazione tra
       preTokenBalances/postTokenBalances
   Accumula gli eventi degli ultimi 60s. Se il volume totale della finestra
   supera una soglia (spike_threshold_sol) → pubblica "analysis.signal_detected"
   con action=BUY, token, confidence, slippage atteso, bribe consigliata.
   La soglia si AUTO-CALIBRA: ascolta trade.executed/trade.failed, ogni 2 esiti
   ricalcola il success_rate sugli ultimi 10 trade e alza/abbassa la soglia.

3. RISK MANAGER (Layer D) — l'unico cancello verso l'esecuzione
   Riceve "analysis.signal_detected". PRIMA di tutto ricontrolla la salute
   del portfolio (drawdown reale letto dal CSV dei trade). Poi valuta:
     - kill-switch attivo? → blocca
     - già 3 posizioni aperte? → blocca
     - altrimenti: alloca bankroll × max_position_pct% e approva
   Pubblica "risk.trade_approved" (con capitale allocato) oppure
   "risk.trade_rejected" (con motivo).

4. EXECUTION ENGINE (Layer C)
   Ascolta SOLO "risk.trade_approved" (mai il segnale grezzo — capitale
   sempre quello autorizzato dal rischio, mai un numero hardcoded).
   In modalità SIMULATION: calcola fee base + bribe, tira un numero
   casuale (10% di fallimento tipico da slippage/MEV), scrive la riga nel
   CSV, pubblica "trade.executed" o "trade.failed".
   In modalità LIVE: oggi rifiuta sempre ("gate non autorizzato") — il
   codice per firmare/inviare davvero non è stato scritto.

5. POSITION MONITOR (Layer E) — uscita
   Apre una posizione su "trade.executed" (indipendentemente dal Risk
   Manager, stesso evento). Ad ogni tick di mercato (ogni nuovo
   "data.raw_event_received") rivaluta il valore stimato della posizione
   con un random-walk (NON un prezzo reale — vedi Rischi). Se il PnL stimato
   supera +50% (take-profit) o -20% (stop-loss) → chiude, pubblica
   "position.closed" con PnL.

6. RISK MANAGER libera lo slot
   Ascolta "position.closed" → rimuove il token da open_positions →
   la 4ª posizione può ora essere accettata.
```

Un solo percorso, nessuna scorciatoia: un segnale che non passa dal Risk
Manager non arriva mai all'Execution Engine.

---

## Le regole di governo (APEX-7)

- **Disaccoppiamento totale**: nessun modulo importa la classe di un altro
  agente. Si parlano solo via Event Bus (publish-subscribe, il publisher non
  sa chi riceve).
- **Event Bus**: 4 code di priorità P0→P3 (P0 sempre servita per prima),
  retry per priorità (P0 → 10 tentativi poi ALERT; P1/P2 → poi Dead Letter
  Queue; P3 → drop), consegna EXACTLY_ONCE con deduplica, replay dello
  storico per ricostruire lo stato di un agente sostituito.
- **6 Gate, 7 livelli**, ognuno con criteri misurabili e soglia calibrata
  (non un numero a caso): L1→L2 100%, L2→L3 80%, L3→L4 83%, L4→L5 80%, L5→L6
  100% (safety critical), L6→L7 100% (zero tolleranza). Un criterio senza
  modo di essere verificato eseguendo codice vale FAIL — `gate_verifiers.py`
  legge il codice sorgente vero, non si fida di descrizioni.
- **Escalation**: gate fallito 3 volte di fila → FREEZE → diagnosi
  automatica → cambio strategia dalla memoria → retry → se fallisce ancora,
  passa a un umano.
- **Human override sempre disponibile**: `MetaAgent.human_override()` può
  congelare tutto, è l'unica funzione che nessun agente può chiamare da solo.
- **Tetto agli agenti**: max 12, oltre lo spawn viene negato.
- **Modifiche irreversibili rifiutate di default**: il sistema propone solo
  cambi reversibili, ogni proposta passa da un Quality Gate.

---

## Le regole per passare a LIVE (soldi veri)

Non negoziabili, in `LEGGIMI.md` + `APEX-7.md`:

1. `report-studio.md` deve dimostrare **expectancy positiva su almeno 30
   giorni di simulazione**. Oggi dice l'opposto.
2. Serve il **PASS del gate L5** prima di sbloccare il live trading nel
   codice (`Live trading solo dopo il PASS del gate L5` — oggi si è a L2/L3).
3. Passaggi tecnici quando/se il gate passa: creare un Hot Wallet
   "usa e getta" (mai il vault principale), `TRADE_MODE=LIVE` in `.env`,
   sostituire `_simulate_transaction` con firma reale via `solders.keypair`.
4. **Kill-switch**: si attiva da solo se il drawdown supera il 20% del
   bankroll, o manualmente. Blocca l'allocazione di nuovo capitale
   all'istante, senza chiudere le connessioni WebSocket.

---

## Rischi — il verdetto onesto (non nascosto, già scritto da Gemini in `report-studio.md`)

1. **Latenza contro i bot istituzionali**: i MEV searcher veri usano
   connessioni dirette ai validatori (Jito Labs), non RPC pubbliche. Un bot
   Python su RPC pubblica riceve il dato con **300-800ms di ritardo**.
   Quando `analysis_engine.py` manda il segnale BUY, il token è già stato
   comprato da altri.
2. **Costo occulto delle bribe**: per passare avanti in coda serve pagare i
   validatori. Poco → transazione fallisce (ma la base fee si paga comunque).
   Tanto → si va in perdita anche vincendo.
3. **Rug pull**: il 99% dei progetti nuovi su Pump.fun/Raydium è una truffa
   dove i creatori prosciugano la liquidità. Uno spike di volume spesso *è*
   il truffatore che sta scaricando — comprare lì è comprare l'uscita del
   rug pull.
4. **Illiquidità NFT** (se si guarda a NFT invece che memecoin): anche
   trovando un mismatch di prezzo, non c'è garanzia di rivendere subito —
   capitale bloccato ("bagholding").
5. **RPC pubblico non regge il carico reale**: verificato a mano (checkpoint
   CP-20260728-006) — dopo **2 chiamate** `getTransaction` di fila, l'RPC
   pubblico risponde `429 Too Many Requests`. Un bot live avrebbe bisogno di
   un provider a pagamento (Helius/QuickNode/Alchemy), non ancora procurato
   — bloccante aperto per Max, in `BACKLOG.md` (B-010).
6. **Position Monitor non ha un prezzo reale**: dichiarato esplicitamente
   nel codice — il valore della posizione è un random-walk simulato
   (`PRICE_STEP_STD=0.03`), non collegato a un feed prezzo vero. Il PnL su
   take-profit/stop-loss è **stimato**, marcato `"estimated": True` in ogni
   record — mai spacciato per dato misurato. Prima di qualunque decisione
   basata su questi numeri, questo va tenuto a mente.
7. **Conclusione di Gemini**: probabilità di perdere l'intero capitale di
   rischio **>85% entro il primo mese** se si passasse a live oggi, così
   com'è. Raccomandazione: **non stanziare capitale reale** finché non si
   ha infrastruttura MEV di livello istituzionale (bundle Jito, server
   bare-metal vicino ai nodi, motore in Rust invece di Python). Fino ad
   allora S7 resta un laboratorio per capire i flussi di volume, non un
   prodotto.

---

## Bug reali già trovati e corretti (cronologia onesta, da CP-20260728-006)

- **G-A — il parser leggeva un mondo finto**: prima cercava il testo
  letterale `"Amount:"` nei log — funzionava solo sul mock, mai su Solana
  vero (una notifica reale porta solo firma + log di programma, mai gli
  account). Fix: legge `getTransaction` vera e ricava volume/token dalle
  variazioni di saldo. Validato su 5 transazioni mainnet reali (Raydium/
  Pump.fun), incluse le transazioni fallite (ritorna `None` corretto, non
  inventa un numero).
- **G-B — il limite posizioni non scattava mai**: `open_positions` era
  dichiarato ma non veniva mai scritto da nessuno. Fix: `RiskManager` si
  iscrive a `trade.executed`/`position.closed` e traccia davvero.
  Verificato: la 4ª posizione viene rifiutata finché una non si chiude.
- **G-C — spam di segnali duplicati**: una volta superata la soglia di
  spike, la finestra non si svuotava finché i 60s non scadevano da soli →
  ogni evento successivo nella stessa finestra ripubblicava lo stesso
  segnale. Fix: la finestra si azzera subito dopo aver segnalato.

Il fatto che questi bug fossero presenti (e siano stati trovati testando
con dati reali, non ipotetici) è il motivo per cui il verdetto "bocciato per
live" va preso sul serio: la logica ha già dimostrato di avere buchi non
ovvi anche dopo revisione.

---

## Cosa serve perché la logica diventi "Metodo" (prossimi passi)

- Procurare un RPC provider a pagamento (Helius/QuickNode/Alchemy) — oggi
  l'endpoint pubblico non regge il volume reale (429 dopo 2 chiamate).
- Risolvere il conflitto di versione in `requirements.txt`
  (`solana==0.33.0` richiede `websockets<12.0`, il file fissa `==12.0`) —
  non bloccante ora (il parser usa `urllib` puro), ma bloccante se si vuole
  usare la libreria `solana-py` per firmare transazioni vere.
- Collegare un feed prezzo reale al Position Monitor (oggi è random-walk
  dichiarato) — senza questo, TP/SL non hanno alcun significato economico.
- Consolidare i loop adattivi L2→L3 con più dati reali, poi costruire
  concretamente L4-L7 (oggi solo specificati con criteri, non implementati).
- Decisione esplicita di Max/Gael prima di stanziare qualunque capitale
  vero: il report attuale dice di no, punto.

---

## Come si esegue

```bash
cd company/Ecosistemi/12-STREAM-S7-BOT
python test_apex7.py      # test end-to-end, 13 sezioni con assert reali
python main.py             # avvia il bot in modalità simulata (paper trading)
```

Console Windows in cp1252: niente emoji nei print, solo marcatori ASCII.
