# BACKBONE — ⚙️ PLATFORM

> Come PLATFORM si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** tool/fix/siti → richiedente

**Inbound (riceve):** feature request ← qualsiasi ecosistema

Handoff contract standard:
```json
{
  "from": "PLATFORM",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `platform/deploy, platform/build-status`

Ogni agente di PLATFORM legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

Security Sentinel su ogni build; zero segreti in git; aidefence scan

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di PLATFORM: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: pipeline (build → test → deploy)

Namespace Ruflo: `ruflo memory init --namespace platform`
