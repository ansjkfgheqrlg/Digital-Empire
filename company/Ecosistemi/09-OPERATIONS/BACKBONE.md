# BACKBONE — 🔧 OPERATIONS

> Come OPERATIONS si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** run result → richiedente; alert costo → CFO

**Inbound (riceve):** richiesta run ← qualsiasi ecosistema

Handoff contract standard:
```json
{
  "from": "OPERATIONS",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `operations/cost, operations/schedule, operations/swarm-state`

Ogni agente di OPERATIONS legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

Cost guard pre-sforo; dry-run obbligatorio prima di ogni spesa

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di OPERATIONS: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: è il gestore delle topologie swarm per tutti

Namespace Ruflo: `ruflo memory init --namespace operations`
