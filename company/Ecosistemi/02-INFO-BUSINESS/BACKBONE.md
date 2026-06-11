# BACKBONE — 📚 INFO-BUSINESS

> Come INFO-BUSINESS si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** brief copy → MARKETING; brief contenuti → CONTENT-FACTORY

**Inbound (riceve):** upsell lead ← AGENCY; copy finita ← MARKETING; contenuti ← CONTENT-FACTORY

Handoff contract standard:
```json
{
  "from": "INFO-BUSINESS",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `infobusiness/lanci, infobusiness/funnel, infobusiness/prodotti`

Ogni agente di INFO-BUSINESS legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

Gate lancio (validazione idea ≥60/100), Gate copy APSOC ≥80/100

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di INFO-BUSINESS: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: pipeline (lancio T-30→T+7)

Namespace Ruflo: `ruflo memory init --namespace infobusiness`
