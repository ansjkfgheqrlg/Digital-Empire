# BACKBONE — 🏢 AGENCY

> Come AGENCY si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** brief copy → MARKETING; asset richiesta → CONTENT-FACTORY; lead caldo → INFO-BIZ

**Inbound (riceve):** copy finita ← MARKETING; asset ← CONTENT-FACTORY; upsell lead ← INFO-BIZ

Handoff contract standard:
```json
{
  "from": "AGENCY",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `agency/outreach, agency/pipeline, agency/delivery`

Ogni agente di AGENCY legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

Gate Preventivo, Gate Delivery UAT, Bibbia outreach

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di AGENCY: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: hierarchical (coordinator outreach + workers per canale)

Namespace Ruflo: `ruflo memory init --namespace agency`
