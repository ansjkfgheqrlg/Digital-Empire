---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (gate APEX-7)
Origine: 12-STREAM-S7-BOT · Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first
Emesso: 2026-07-28 · Priorità: P1
Riferimenti: CP-20260727-002 (APEX-7 Level 2 chiuso) · APEX-7.md · STATO-RIPRESA.md ·
             company/Ecosistemi/12-STREAM-S7-BOT/test_apex7.py
---

> **STATO: ✅ FATTO (2026-07-28)** — tutti e 3 i lotti (G-A/G-B/G-C) chiusi, DoD verificata,
> `test_apex7.py` 13/13 verde. Dettagli, comandi e output reali:
> [CP-20260728-006](../checkpoints/CP-20260728-006.md). Un punto aperto per Max (non bloccante):
> `BACKLOG.md` B-010 (RPC provider a pagamento prima di LIVE).

# 🚨 ORDINE MAX — GAEL: rendi 12-STREAM-S7-BOT un bot che vende, non solo che compra

## 0. Perché (leggi, sono 10 righe, ti risparmiano un giorno)

Il bot ha l'impalcatura APEX-7 solida: event bus con priorità/retry/DLQ, memoria a 5 query,
6 Quality Gate (L1→L7) con criteri **eseguibili** (non testo che li descrive — codice che li
verifica), Gate Agent, Meta-Agent, Orchestrator. Sul dominio trading specifico: AnalysisEngine →
RiskManager → ExecutionEngine parlano solo via bus (era un bug reale: prima `main.py` eseguiva
ogni trade **due volte**, la seconda bypassando il controllo del rischio — risolto), la soglia di
spike si ricalibra da sola sui trade veri chiusi (feedback loop reale, non dichiarato), il
kill-switch legge il drawdown vero dal log invece di essere uno stub.

**Quello che manca non è architettura, è dominio**: il bot compra e basta. Non traccia le
posizioni, non ha uscita, e legge log finti (il parser cerca testo che non esiste su Solana vero).

Verifica subito che il terreno sia solido:
```bash
cd "<radice monorepo>/company/Ecosistemi/12-STREAM-S7-BOT"
python test_apex7.py     # deve stampare "9 sezioni, [OK] Tutti i controlli superati", exit 0
```
Se non da' 9/9 verde: `git pull`, il task non e' arrivato integro.

---

## 1. Cosa è già fatto e NON devi rifare

| File | Cosa fa | Stato |
|---|---|---|
| `event_bus.py` | P0-P3, retry, DLQ, replay, catalogo eventi completo | ✅ testato |
| `memory_interface.py` | 5 query (recall/decision/strategy/write/forget), indice, lock, checkpoint | ✅ |
| `quality_gates.py` + `gate_verifiers.py` | 6 gate L1-L7, criteri con rubrica **eseguibile** | ✅ |
| `gate_agent.py` | ispettore, macchina a stati reale | ✅ |
| `meta_agent.py` | registro agenti, pattern detection, spawn-limit, human_override | ✅ |
| `orchestrator.py` | ciclo task→gate→memoria generico | ✅ |
| `analysis_engine.py` | rileva spike, soglia auto-calibrata sui trade REALI chiusi | ✅ |
| `risk_manager.py` | unico varco segnale→esecuzione, kill-switch su drawdown REALE | ✅ |
| `execution_engine.py` | paper trading, scrive ogni esito in memoria | ✅ |
| `ruflo_adapter.py` + `.yaml` | config unica, backend intercambiabile | ✅ |
| `test_apex7.py` | 9 sezioni, gate L2→L3 e L6→L7 PASSED su dati reali del bot | ✅ verde |

**FILE CONGELATI** (fondazione APEX-7, condivisa con altri ecosistemi che la useranno):
`event_bus.py`, `memory_interface.py`, `quality_gates.py`, `gate_verifiers.py`, `gate_agent.py`,
`meta_agent.py`, `orchestrator.py`, `ruflo_adapter.py`, `apex7_workflow.ruflo.yaml`, `prompts/**`.
Puoi **estenderli** (nuovo evento nel catalogo, nuovo verifier, nuovo layer memoria). **Non**
rinominare/cambiare firme esistenti senza nota `⚠️ COORDINAMENTO` in `company/Memory/STATO-EMPIRE.md`
+ push.

---

## 2. I TUOI 3 LOTTI (in quest'ordine)

### 🟣 G-A — Parser dati reale (P0, sblocca tutto il resto)

`analysis_engine._extract_volume_from_logs()` oggi cerca la stringa letterale `"Amount:"` o
`"Volume spike:"` nei log — funziona SOLO sul mock stream di `data_manager.py`, mai su Solana
vero (i log reali sono base64/struct, non testo leggibile in quella forma).

- Decodifica i log reali dei programmi Raydium/Pump.fun: via IDL noto o parsing euristico degli
  account coinvolti nell'istruzione, per ricavare **volume vero** in SOL
- Sostituisci `"mock_token_address_123"` hardcoded in `_detect_spike()` con l'indirizzo token
  reale estratto dalla transazione (e' negli `accounts` della tx, non nei log)
- Non toccare la logica di soglia/calibrazione: resta come e', cambia solo la fonte del dato

**Gate G-A**: fai girare `data_manager.py` con `SOLANA_WSS_URL` reale (vedi `.env.example`) per
10 minuti. Incolla nel checkpoint almeno 3 coppie volume/token estratte correttamente da
transazioni vere (screenshot o log, non "dovrebbe funzionare").

### 🟣 G-B — Position Manager + uscita (P0)

Il bot compra e non vende mai. `RiskManager.open_positions` e' dichiarato (`risk_manager.py:37`)
ma **mai scritto**: il limite "max 3 posizioni aperte" (`risk_manager.py:73`) non scatta mai
perche' il dizionario resta sempre vuoto.

- Quando arriva `trade.executed`, aggiungi la posizione a `open_positions`
  (token, entry_cost, timestamp)
- Crea un modulo nuovo `position_monitor.py` (Layer separato, si iscrive al bus come gli altri):
  - tiene sotto controllo il valore della posizione (anche stimato, se non c'e' un feed prezzo
    live — dillo esplicitamente nel checkpoint se e' una stima)
  - applica take-profit / stop-loss (soglie da nuove variabili in `.env`, es.
    `TAKE_PROFIT_PCT`, `STOP_LOSS_PCT`)
  - pubblica `position.closed` (nuovo evento, aggiungilo a `EVENT_CATALOG` in `event_bus.py`
    con priorita' P1) che: rimuove da `open_positions`, scrive il PnL reale in memoria
    (`global_memory.write("metrics", {"kind": "position_closed", ...})`)

**Gate G-B**: test con 3 posizioni aperte simulate → la 4a viene rifiutata da RiskManager
(`len(open_positions) >= 3`) → dopo la chiusura di una posizione, la 4a viene accettata.
Incolla l'output del test.

### 🟣 G-C — Fix spam segnali + baseline L3→L4 sul bot (P1)

`_detect_spike()` non svuota `recent_events` dopo aver emesso un segnale: una volta superata la
soglia, OGNI evento successivo ripubblica lo stesso segnale finche' la finestra di 60s non scade
da sola. Correggi: dopo `analysis.signal_detected`, svuota `recent_events` o marca la finestra
come "gia' segnalata" fino al prossimo reset naturale.

Poi registra una baseline di performance **reale** del bot (tempo tra log-ricevuto e
trade-eseguito — vedi `orchestrator.set_baseline()` gia' presente, stesso pattern) e fai passare
il gate `L3_TO_L4` (`quality_gates.py`) sui dati specifici del bot, non solo sul codice APEX
generico come oggi.

**Gate G-C**: nessun segnale duplicato sulla stessa finestra di spike (test con evento ripetuto).
Gate `L3_TO_L4` valutato via `gate_1.evaluate(...)` sul bot → PASSED, con baseline reale citata
nel report (segui il pattern gia' in `test_apex7.py` sezione 8 per come si invoca).

---

## 3. Perimetro — cosa NON tocchi

| Area | Di chi è |
|---|---|
| `event_bus.py`, `memory_interface.py`, `quality_gates.py`, `gate_verifiers.py`, `gate_agent.py`, `meta_agent.py`, `orchestrator.py`, `ruflo_adapter.py`, `apex7_workflow.ruflo.yaml`, `prompts/**` | Claude — fondazione APEX-7 condivisa |
| `execution_engine.py` **lato modalità LIVE** (firma vera, invio on-chain, `TRADE_MODE=LIVE`) | **NESSUNO senza ordine esplicito di Max** — soldi veri, serve gate L5 superato (safety critical, 5/5) + via libera umana. Puoi leggere/scrivere l'esito paper trading, non aprire la modalità live. |
| `worker_agent.py`, `test_apex7.py` sezioni 1-7 (parte generica APEX) | Claude |
| **Tuo, in esclusiva** | `analysis_engine.py` (parser + soglia), `risk_manager.py` (position tracking), `execution_engine.py` (solo lettura/scrittura esito paper, non la modalita'), `position_monitor.py` (nuovo), `test_apex7.py` sezione 8 (STREAM S7) |

---

## 4. Regole operative

1. **Paper trading resta l'unica modalità che esegui.** `TRADE_MODE=LIVE` non è compito tuo.
2. **Mai chiave privata in chiaro**: mai in `.env` committato, mai loggata, mai stampata.
3. **Windows-first**: zero emoji nei `print()`/`logger` — crashano su console cp1252 (già
   successo in questo bot, vedi commit di fix precedente). ASCII puro nei log.
4. **Prova, non dichiarazione**: nel checkpoint incolli comando + output reale.
   "Dovrebbe funzionare" = task non chiuso.
5. **ADR-006 ciclo a 9 passi** per ogni lotto: RECALL → SPEC → PRE-MORTEM → BUILD → GATE →
   REVIEW → TEST → COMMIT → RETRO.
6. Prima di ogni lotto e dopo: `python test_apex7.py` deve restare verde (9/9). Se lo rompi, non
   committi finché non torna verde.
7. **Task chiuso → checkpoint** in `company/Memory/checkpoints/CP-20260728-NNN.md` — prendi il
   primo numero libero al momento in cui parti.
8. **Item minori → `company/Memory/BACKLOG.md`** (ADR-005), non fermare la costruzione.

---

## 5. Definition of Done complessiva

- [ ] parser dati reale: volume e token_address estratti da log Solana veri, non testo mock
- [ ] posizioni tracciate: apertura in `open_positions`, chiusura, PnL scritto in memoria
- [ ] take-profit/stop-loss applicati almeno in simulazione
- [ ] limite "max 3 posizioni aperte" verificato scattare davvero (test incollato)
- [ ] nessun segnale duplicato sulla stessa finestra di spike
- [ ] gate `L3_TO_L4` PASSED sui dati reali del bot (non solo sul codice APEX generico)
- [ ] `python test_apex7.py` verde (9/9 sezioni) a fine lavoro
- [ ] zero modifiche a `execution_engine.py` lato modalità LIVE
- [ ] checkpoint con comandi e output reali incollati

---

## 6. Ordine di marcia

1. `git pull` → verifica `python test_apex7.py` verde (9/9) prima di toccare qualunque cosa
2. Leggi `APEX-7.md` e `STATO-RIPRESA.md` in `company/Ecosistemi/12-STREAM-S7-BOT/`
3. **G-A** (parser dati reale) → gate → commit
4. **G-B** (position manager + uscita) → gate → commit
5. **G-C** (fix spam segnali + baseline L3→L4) → gate → commit
6. checkpoint + RETRO + push

**Se qualcosa non torna** (un formato log imprevisto, un IDL ambiguo, una collisione):
**non indovinare**. Scrivi il problema con **comando esatto + errore esatto** in
`STATO-EMPIRE.md` e prosegui sul lotto successivo.
