# BACKBONE — 🌐 MULTI-BUSINESS

> Come MULTI-BUSINESS si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** proof (demo YT, libro) → AGENCY; brief contenuti → CONTENT-FACTORY

**Inbound (riceve):** script/copy ← MARKETING; video ← CONTENT-FACTORY

Handoff contract standard:
```json
{
  "from": "MULTI-BUSINESS",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `multibusiness/youtube, multibusiness/kdp, multibusiness/ecomm`

Ogni agente di MULTI-BUSINESS legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

QA video ffprobe (9:16, durata, orientamento)

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di MULTI-BUSINESS: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: parallel (YT Automation: N video in parallelo)

Namespace Ruflo: `ruflo memory init --namespace multibusiness`
