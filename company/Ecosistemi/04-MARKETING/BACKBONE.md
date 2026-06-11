# BACKBONE — 📣 MARKETING

> Come MARKETING si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** copy finita → richiedente (qualsiasi ecosistema)

**Inbound (riceve):** brief copy ← qualsiasi ecosistema

Handoff contract standard:
```json
{
  "from": "MARKETING",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `marketing/copy/patterns/{icp}, marketing/analytics`

Ogni agente di MARKETING legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

G1 APSOC ≥80/100, G2 Brand gate (non derogabile)

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di MARKETING: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: hierarchical (copy-master + A1-A8 + S1-S3)

Namespace Ruflo: `ruflo memory init --namespace marketing`
