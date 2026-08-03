# STATO-RIPRESA — APEX-7 / Stream S7

> Quando Max dice **"via"**, riparti da qui. Non re-derivare: e' gia' tutto scritto.

**Ultimo aggiornamento:** 2026-08-03
**Checkpoint Memory:** `CP-20260727-002.md`, `CP-20260728-004.md`, `CP-20260728-006.md`,
`CP-20260728-012.md`, `CP-20260730-002.md` … `CP-20260730-007.md`

---

## ⛔ LEGGI PRIMA DI TUTTO: non manca codice, manca una decisione

Il sistema e' **chiuso e verde**. `python test_apex7.py` → gate finale L6→L7 **PASSED 7/7,
score 1.0** (riverificato il 2026-08-03). Non c'e' lavoro tecnico bloccante.

Ma il verdetto commerciale e' **negativo, scritto due volte da analisi indipendenti**:

| Analisi | Verdetto |
|---|---|
| [report-studio.md](report-studio.md) — motore memecoin | Expectancy **NEGATIVA**, >85% di perdere il capitale entro il primo mese |
| [CP-20260730-007](../../Memory/checkpoints/CP-20260730-007.md) — layer NFT Magic Eden, **89/89** controlli reali | **INVARIATO**: bocciato per live. Risolve 1/3 problemi strutturali, e solo parzialmente |

**Quindi il prossimo passo non e' una task di sviluppo: e' una decisione di Max e Gael.**
S7 resta laboratorio di paper trading (e allora e' finito), oppure si investe sull'infrastruttura
per renderlo vero? Finche' questa decisione non e' presa, costruire altro qui e' lavoro a vuoto.

### Se si va verso LIVE, questi sono i prerequisiti aperti
1. **RPC Solana a pagamento** (Helius/QuickNode/Alchemy) — `BACKLOG.md` **B-010**. Bloccante duro:
   l'endpoint pubblico risponde `429` dopo **2 chiamate** `getTransaction`. Il parser e' corretto
   (5/5 coppie volume/token reali estratte), ma non regge il ritmo di un bot live.
2. **Latenza misurata 2456-3624ms** contro il benchmark MEV 300-800ms. Questo **non si compra**:
   richiede Jito bundles, bare-metal vicino ai validatori, riscrittura in Rust. E' il problema
   strutturale numero uno e resta intatto.
3. **Nessun feed prezzo live**: `position_monitor.py` esce sul valore **stimato**, non sul prezzo
   reale. TP/SL oggi non sono veri.
4. **Modalita' LIVE non implementata**: `execution_engine.py` rifiuta esplicitamente il ramo
   `!= SIMULATION` (logga errore, ritorna `False`). Va scritta, non solo abilitata.

---

## ✅ Cosa e' gia' chiuso

**APEX-7 Level 2 + dominio trading — operativo, testato, verde.**

```
python test_apex7.py    →   exit 0, gate finale L6->L7 PASSED 7/7, score 1.0
```

- **TASK GAEL trading (2026-07-28)** — `TASK-GAEL-20260728-STREAM-S7-BOT.md` **chiusa**, tutti e
  3 i lotti verificati su dati reali: G-A parser reale su `getTransaction`, G-B position manager
  con TP/SL, G-C fix spam segnali + **baseline L3→L4 PASSED**.
  Dettagli: [CP-20260728-006](../../Memory/checkpoints/CP-20260728-006.md).
- **TASK GAEL layer NFT (2026-07-30)** — `TASK-GAEL-20260730-STREAM-S7-NFT-METODO.md`
  **completa**: Fase 0 + Ondate 1-4 + Fase 2, **89/89 controlli reali** su dati Magic Eden veri
  (API pubblica, nessuna chiave), zero capitale vero, **zero file frozen toccati**.
  Verdetto in cima a questa pagina. [CP-20260730-007](../../Memory/checkpoints/CP-20260730-007.md).

## Mappa dei file (tutti in questa cartella)

| File | Ruolo | Stato |
|---|---|---|
| `event_bus.py` | Bus P0-P3, retry, DLQ, replay, 19 eventi | ✅ L2 · frozen |
| `memory_interface.py` | 5 query, indice, checkpoint/restore | ✅ L2 · frozen |
| `quality_gates.py` | 6 gate L1→L7, 33 criteri con rubrica | ✅ frozen |
| `gate_verifiers.py` | Verificatori eseguibili | ✅ frozen |
| `gate_agent.py` | Ispettore, macchina a stati reale | ✅ L2 · frozen |
| `meta_agent.py` | Registro, pattern, spawn-limit, override | ✅ L2 · frozen |
| `orchestrator.py` | Gate↔task, remediation, metriche | ✅ L2 · frozen |
| `worker_agent.py` | Claim per competenza | ✅ L2 |
| `ruflo_adapter.py` + `apex7_workflow.ruflo.yaml` | Config unica, backend intercambiabile | ✅ |
| `prompts/*.txt` | 7 prompt interni agenti | ✅ |
| `main.py` · `analysis_engine.py` · `data_manager.py` · `risk_manager.py` · `execution_engine.py` · `position_monitor.py` | Bot S7 memecoin | ✅ collegato al ciclo APEX (G-A/G-B/G-C) |
| `nft_magiceden_client.py` · `nft_analysis_engine.py` · `nft_monte_carlo.py` · `nft_ondata2-4.py` | Layer NFT (R&D) | ✅ 89/89 · verdetto negativo |
| `test_apex7.py` · `test_nft_s7.py` · `test_nft_ondata2-4.py` | Suite di test | ✅ verdi |

## ⚠️ Decisione architetturale ferma su Max

**TASK-YT-006 / G-YT-6** — ADR-010 prevedeva di migrare `event_bus`/`memory_interface`/
`quality_gates`/`gate_agent`/`meta_agent`/`orchestrator` verso `11-APEX-7-CORE`.
**Verificato e NON fatto, con motivazione scritta** (il gate stesso ammetteva l'alternativa):
Stream-S7 e' piu' maturo del motore condiviso — migrarlo sarebbe un **downgrade** su un sistema
verificato che esegue trade reali. Raccomandazione opposta: portare le funzionalita' di S7
**dentro** `11-APEX-7-CORE`. Vedi [CP-20260728-012](../../Memory/checkpoints/CP-20260728-012.md).

## Backlog aperto che tocca questo ecosistema
- **B-010** — RPC Solana a pagamento (vedi sopra, prerequisito LIVE).
- **B-012** — fee marketplace Magic Eden (2%) e royalty creator sono marcate **"DA CONFERMARE"**
  nel codice: la verifica da fonte primaria e' finita su `429`/`404`. Conta solo se si da' peso
  decisionale all'expectancy netta (oggi comunque bocciata per altri motivi).

## Come rieseguire i test

```bash
cd company/Ecosistemi/12-STREAM-S7-BOT
pip install -r requirements.txt
python test_apex7.py
```
Note:
- La console Windows e' cp1252 — i print usano marcatori ASCII, niente emoji.
- Le suite NFT (`test_nft_*.py`) chiamano l'API **reale** di Magic Eden: se la rete non risponde
  dichiarano `[SALTATO — NON misurabile adesso]` invece di inventare un numero.
- **`requirements.txt` corretto il 2026-08-03**: `solana==0.33.0` e `solders==0.21.0` erano
  attivi ma non importati da nessuna riga di codice, e `solana` richiede `websockets<12.0`
  mentre `data_manager.py` gira su `websockets==12.0` → `pip install -r requirements.txt`
  falliva con `ResolutionImpossible` su macchina pulita. Ora sono commentati con la nota del
  conflitto, da risolvere insieme quando si implementera' LIVE.

## Task parallelo richiesto da Max (non iniziato)

Usare **/content-forge** per convertire agenti / skill / flussi di lavoro da markdown descrittivo
a **agenti e skill OPERATIVI**, uno per uno, con checklist, applicando APEX-7 come metodo
(recall → spec → build → gate → test → commit).
⚠️ **Accertato in [CP-20260730-006](../../Memory/checkpoints/CP-20260730-006.md): `/content-forge`
non e' un comando disponibile in questo ambiente.** Serve prima decidere con cosa sostituirlo.

---

## 📜 Storico — dove eravamo prima (riferimento, non da rifare)

La versione precedente di questa pagina indicava come prossimo passo il **loop L2 → L3**
(collegare `analysis_engine`/`execution_engine` al ciclo Orchestrator → Gate → Memory, tarare le
soglie su esecuzioni misurate, far scrivere al bot le sue metriche nel layer `metrics`).
**Quel passo e' stato fatto e superato**: il collegamento e' avvenuto in CP-20260728-004, i 3
lotti G-A/G-B/G-C sono chiusi in CP-20260728-006 con **baseline L3→L4 PASSED**, e oggi gira il
gate finale **L6→L7 PASSED 7/7**. Lasciato qui perche' chi ripartiva da quella riga rifaceva
lavoro gia' fatto.
