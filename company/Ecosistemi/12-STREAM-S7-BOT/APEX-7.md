# APEX-7 — Sistema Nervoso Operativo

APEX-7 e' il sistema nervoso su cui gira lo Stream S7 (bot di trading Solana) e,
in generale, qualunque lavoro che richieda piu' agenti che collaborano senza
pestarsi i piedi. Sette livelli, sei gate: nessun livello avanza senza il PASS
del suo gate.

Questo documento e' la mappa del territorio. Il territorio e' il codice.

---

## 1. Architettura

Cinque componenti, una responsabilita' ciascuno, nessuno che chiama un altro
direttamente. Si parlano solo attraverso l'Event Bus.

| Componente | File | Fa | Non fa |
|---|---|---|---|
| **Orchestrator** | `orchestrator.py` | Assegna missioni, chiama l'ispettore, riassegna o escala | Non esegue il lavoro |
| **Worker** | `worker_agent.py` | Esegue i task che rientrano nelle sue competenze | Non giudica il proprio output |
| **Gate Agent** | `gate_agent.py` | Valuta l'output contro i criteri del gate | Non migliora l'output |
| **Meta-Agent** | `meta_agent.py` | Sorveglia, riconosce pattern, cambia strategia | Non lavora nel day-to-day |
| **Memory** | `memory_interface.py` | Ricorda con autore, fiducia, eta' | Non cancella mai davvero |

Infrastruttura trasversale: **Event Bus** (`event_bus.py`), **Quality Gates**
(`quality_gates.py` + `gate_verifiers.py`), **RuFLO adapter** (`ruflo_adapter.py`
+ `apex7_workflow.ruflo.yaml`), **prompt interni** (`prompts/`).

Regola di disaccoppiamento verificata automaticamente (gate L1, criterio C3):
nessun modulo agente importa la classe di un altro agente.

---

## 2. I sette livelli e i sei gate

Ogni gate ha criteri con **rubrica misurabile** e una **soglia** calibrata sul
livello, non una taglia unica.

| Gate | Da → A | Soglia | Tolleranza |
|---|---|---|---|
| `L1_TO_L2` | Fondamenta → Struttura connessa | 100% (5/5) | zero |
| `L2_TO_L3` | Struttura → Loop adattivi | 80% (4/5) | un criterio |
| `L3_TO_L4` | Loop → Parallelismo + RuFLO | 83% (5/6) | un criterio |
| `L4_TO_L5` | Parallelismo → Intelligence | 80% (4/5) | un criterio |
| `L5_TO_L6` | Intelligence → Self-Evolving | 100% (5/5) | zero (safety critical) |
| `L6_TO_L7` | Self-Evolving → APEX | 100% (7/7) | zero |

**Protocollo di escalation**: se un gate fallisce 3 volte di fila →
FREEZE → DIAGNOSE (Meta-Agent) → STRATEGY CHANGE (dallo Strategy Store) →
LOG del pattern → RETRY con nuova strategia → se ancora FAIL, umano.

Ogni criterio che si puo' controllare eseguendo viene controllato eseguendo:
`gate_verifiers.py` legge il codice sorgente vero, interroga il bus vero,
ispeziona la memoria vera. Un criterio senza rubrica vale FAIL — non si timbra
cio' che non si sa misurare.

---

## 3. Event Bus

Publish-subscribe puro: il publisher non sa chi riceve, il subscriber non sa chi
ha inviato. Zero coupling.

- **19 eventi catalogati** (`EVENT_CATALOG`), ognuno con priorita' e garanzia di consegna.
- **4 code di priorita' P0→P3**, drenate in ordine di severita': finche' c'e' un
  P0 in attesa, nessun P1 viene servito. Un P0 emesso durante la gestione di un
  P3 viene comunque servito prima.
- **Retry policy per priorita'**: P0 → 10 tentativi poi ALERT; P1/P2 → poi DLQ;
  P3 → poi DROP.
- **Dead Letter Queue** per gli eventi che non arrivano mai; `retry_dlq()` li ritenta.
- **EXACTLY_ONCE** garantito con deduplica `(event_id, subscriber)`.
- **Replay** dello storico per ricostruire lo stato di un agente sostituito.
- Un subscriber che esplode non ferma il bus: viene isolato e l'evento segue la
  sua retry policy.

---

## 4. Memory

"La memoria non e' un database. E' un cervello." Cinque modi di interrogarla,
uno solo di cambiarla.

| Query | Metodo | Risponde a |
|---|---|---|
| TYPE 1 | `contextual_recall` | Cosa e' rilevante adesso |
| TYPE 2 | `decision_lookup` | Ho gia' deciso questo? Com'e' andata? |
| TYPE 3 | `strategy_fetch` | Cosa ha funzionato per problemi come questo? |
| TYPE 4 | `write` | Salva, con lock e con autore |
| TYPE 5 | `forget` | Archivia, mai cancella |

- **Lettura**: non prende mai il lock. Ranking per `rilevanza × freschezza ×
  fiducia × importanza`.
- **Scrittura**: lock con timeout 100ms, scarto dei duplicati (soglia 0.95),
  metadati automatici, evento `memory.updated` sul bus.
- **Forget**: sposta in `ARCHIVED` con `reason` e `superseded_by`. Cancellare
  farebbe perdere la traccia dell'errore, che e' la parte utile.
- **Indice invertito** parola→record: niente scansione totale con migliaia di record.
- **Persistenza**: `checkpoint()` fotografa su disco, `restore()` riprende e
  ricostruisce l'indice. Una sessione interrotta non perde nulla.

---

## 5. Integrazione RuFLO

RuFLO non e' piu' "citato": e' mappato. `apex7_workflow.ruflo.yaml` e' la fonte
di verita' unica (agenti, timeout, permessi di memoria, soglie dei gate, retry
policy). `ruflo_adapter.py` la esegue:

- se il runtime **RuFLO** e' installato → consegna il grafo a lui;
- altrimenti → lo stesso grafo gira sull'**Event Bus interno**.

`adapter.validate()` verifica che yaml e codice raccontino la stessa storia:
soglie, retry, catalogo eventi, layer di memoria. Una configurazione che diverge
dal comportamento reale e' peggio di nessuna configurazione.

Ogni agente ha il suo **prompt interno** in `prompts/` (`planner`, `writer`,
`analyst`, `critic`, `refiner`, `gate`, `meta`): il comportamento, non il nome.

---

## 6. Sicurezza

Vincoli non negoziabili (`safety` nello yaml, applicati nel codice):

- **Human override sempre disponibile**: `MetaAgent.human_override()` congela il
  sistema in qualunque stato. E' l'unica funzione che nessun agente puo' chiamare.
- **Modifiche irreversibili rifiutate di default**: il sistema puo' proporre solo
  modifiche reversibili, e ogni proposta passa da un Quality Gate prima di
  applicarsi. Il resto lo decide Max.
- **Tetto agli agenti** (`MAX_AGENTS = 12`): oltre il limite lo spawn viene negato.
- **Live trading** solo dopo il PASS del gate L5.

---

## 7. Come si esegue

```bash
cd company/Ecosistemi/12-STREAM-S7-BOT
python test_apex7.py      # test end-to-end: 8 sezioni, ognuna con assert reali
python main.py            # avvia il bot S7 in modalita' simulata
```

Il test e' la prova che il sistema regge: valuta il proprio stesso codice
attraverso i gate reali, non attraverso mock. Il gate APEX (L6→L7) gira sui 7
criteri e riporta il verdetto motivato criterio per criterio.

---

## 8. Stato

Costruito fino al **Level 2** operativo end-to-end. I livelli L3-L7 hanno gate,
rubriche e verificatori gia' definiti: il sistema sa gia' come giudicarsi quando
li si costruira'. Prossimo passo: consolidare i loop adattivi (L2→L3) con dati
reali dal bot S7.
