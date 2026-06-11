# BACKBONE — 🔨 FORGE

> Come FORGE si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** skill/agente/team finito → richiedente; update → IDENTITY-HR

**Inbound (riceve):** intake brief ← qualsiasi ecosistema

Handoff contract standard:
```json
{
  "from": "FORGE",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `forge/builds, forge/evals, forge/registry`

Ogni agente di FORGE legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

MKD obbligatorio + eval gate prima di ogni ship

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di FORGE: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: parallel (forge di skill multiple in parallelo)

Namespace Ruflo: `ruflo memory init --namespace forge`
