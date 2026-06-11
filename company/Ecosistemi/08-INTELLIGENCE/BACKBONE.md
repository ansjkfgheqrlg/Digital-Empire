# BACKBONE — 🔭 INTELLIGENCE

> Come INTELLIGENCE si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** knowledge pack / research → richiedente

**Inbound (riceve):** richiesta ricerca ← qualsiasi ecosistema; video/doc per ingestione ← qualsiasi

Handoff contract standard:
```json
{
  "from": "INTELLIGENCE",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `è il gestore del BRAIN: wiki + AgentDB + ReasoningBank`

Ogni agente di INTELLIGENCE legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

wiki-sync-guard: ogni operazione logga in wiki/log.md

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di INTELLIGENCE: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: parallel (Empire Studio: N video in parallelo)

Namespace Ruflo: `ruflo memory init --namespace intelligence`
