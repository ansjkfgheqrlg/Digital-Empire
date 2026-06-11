# BACKBONE — 🎬 CONTENT-FACTORY

> Come CONTENT-FACTORY si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** asset finiti → richiedente (AGENCY / INFO-BIZ / MULTI-BIZ)

**Inbound (riceve):** brief asset ← AGENCY / INFO-BIZ / MULTI-BIZ; copy ← MARKETING

Handoff contract standard:
```json
{
  "from": "CONTENT-FACTORY",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `content/produzione, content/performance, content/template`

Ogni agente di CONTENT-FACTORY legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

Brand gate G2 su ogni output (brand_kit obbligatorio)

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di CONTENT-FACTORY: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: parallel (produzione multi-formato in parallelo)

Namespace Ruflo: `ruflo memory init --namespace contentfactory`
