# L2 — RUNTIME (Esecuzione Swarm e Code)

> **Ecosistema:** 09-OPERATIONS · **Coordinator:** `ops-swarm-marshal` · **Direttore:** `ops-director`
> **Workflow L3:** `Workflow/WF-SWARM-RUN/` · `Workflow/WF-QUEUE/`
> **Funzioni L4:** `Funzioni/T-fanout/` · `Funzioni/T-worker-pool/` · `Funzioni/T-merge-results/` · `Funzioni/T-retry-failed/`

## Cosa fa

RUNTIME è il motore di **produzione di massa** della holding. Quando un ecosistema
business deve produrre N artefatti dello stesso tipo (50 caroselli, 30 capitoli KDP,
20 pagine sito, 100 email personalizzate), non spawna agenti a mano: consegna il
batch a RUNTIME, che lo esegue come **swarm coordinato** — pattern CF
`swarm.sh --parallel N --budget N`, portato in versione DE come skill `empire-swarm`.

Due capacità:
1. **WF-SWARM-RUN** — fan-out del lavoro in shard, worker pool parallelo, merge dei
   risultati, retry mirato dei soli shard falliti.
2. **WF-QUEUE** — render/job queue (pattern render queue CF): priorità, limiti di
   concorrenza, backpressure quando i worker sono saturi.

## Come si collega

| Con chi | Direzione | Cosa passa |
|---|---|---|
| Ecosistemi business (01-05) | inbound | batch: `{items[], template, budget_max, brand_kit, icp}` |
| COST-GUARD (stesso ecosistema) | bidirezionale | pre-run: approvazione budget; durante: consumo per shard; il cost-sentinel può fermare lo swarm |
| SCHEDULING | inbound | batch ricorrenti arrivano come job cron già approvati |
| MONITORING-DASHBOARD | outbound | heartbeat swarm, stato code, shard falliti |
| FORGE | inbound | nuovi template di worker (un team L4 per tipo di artefatto) |
| 10-MEMORY | outbound | a batch chiuso: HC-ME-POST con esiti e costi → CP |

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** Un handoff sul Bus con `type: directive` e `to: OPERATIONS/RUNTIME/*`,
oppure un job promosso da WF-CRON. Mai auto-attivazione: RUNTIME esegue solo lavoro
commissionato con budget dichiarato (gate G-BUDGET).

**Ragionamento del coordinator (`ops-swarm-marshal`):**
1. Valida l'handoff: items, acceptance criteria, `budget_max` presente? Se no → reject
   con note correttive (un handoff senza criteri è invalido per contratto).
2. **Dry-run obbligatorio** (G-DRYRUN): stima costo = items × costo/item del tier scelto.
   Stima > budget → STOP, propone: ridurre batch, scendere di tier, o chiedere ok umano.
3. Sceglie la topologia: shard disgiunti → parallel fan-out; dipendenze sequenziali →
   pipeline; default hierarchical sotto di sé.
4. Lancia il worker pool (T-worker-pool) con concorrenza N; ogni shard emette evento
   costo (G-ATTRIBUTION).
5. A fine corsa: T-merge-results unisce, T-retry-failed rilancia SOLO i falliti
   (max 2 retry, poi escalation), report finale al committente.

**Principio:** mai un agente solo quando più agenti coordinati possono lavorare in
parallelo — ma mai più worker di quanti il budget ne paghi.

*Fonte: dossier 06 §09 L2 RUNTIME · Aggiornato: 2026-06-11*
