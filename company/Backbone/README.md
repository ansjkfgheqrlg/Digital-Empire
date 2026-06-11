# 🔗 Corporate Backbone — Digital Empire Group

> Il sistema nervoso condiviso della holding.
> Nessun ecosistema lo possiede: tutti lo usano.
> Fonte: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §4, `07-BACKBONE-RUFLO-SKILLS.md`

## Componenti

| Componente | Funzione | Path | Stato |
|---|---|---|---|
| **BUS** | Message bus inter-ecosistema, handoff contract JSON | `Bus/` | da costruire F2 |
| **BRAIN** | AgentDB/HNSW + wiki bridge + ReasoningBank + Memory Empire | `Brain/` | parziale (wiki attiva) |
| **GOVERNANCE** | verify-empire.sh, gate qualità, contradiction-analyzer | `Governance/` | da costruire F2 |
| **IDENTITY-HR** | registro-agenti.yaml unico, gestione roster | `Identity-HR/` | da costruire F2 |
| **OBSERVABILITY** | metrics, dashboard, neural_train, autopilot, cost-attribution | `Observability/` | da costruire F8 |
| **COORDINATION** | Ruflo: swarm topologies, hive-mind consensus (raft) | `Coordination/` | ruflo installato |

## Dipendenze tra componenti

```
COORDINATION (Ruflo)
    ↓ agenda e coordina
BUS → BRAIN (legge/scrive AgentDB mentre consegna messaggi)
    ↓
GOVERNANCE (gate prima di ogni consegna)
    ↓
IDENTITY-HR (valida che mittente e destinatario esistano nel roster)
    ↓
OBSERVABILITY (logga ogni evento per metrics e training)
```

## Handoff contract standard (invariante)

```json
{
  "from": "<ecosistema_mittente>",
  "to": "<ecosistema_destinatario>",
  "contract_id": "HC-XX-YY-NN",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected",
  "timestamp": "ISO8601",
  "cost_attributed_to": "<ecosistema_mittente>"
}
```
