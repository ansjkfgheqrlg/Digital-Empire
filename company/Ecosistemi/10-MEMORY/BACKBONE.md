# BACKBONE — 🧠 MEMORY

> Come MEMORY si collega al Corporate Backbone.
> Per l'organigramma completo: `company/GRUPPO.md`
> Per i dettagli tecnici del Backbone: `company/Backbone/`

## BUS (Message bus)

**Outbound (manda):** stato / checkpoint / ADR → qualsiasi richiedente

**Inbound (riceve):** richiesta stato ← qualsiasi ecosistema (all'inizio di ogni task)

Handoff contract standard:
```json
{
  "from": "MEMORY",
  "to": "<ecosistema_destinazione>",
  "payload": {},
  "acceptance_criteria": [],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `fa parte del BRAIN: checkpoint + ADR + piani`

Ogni agente di MEMORY legge/scrive in questi namespace.
Fonte di verità umana: `second-brain-vault/wiki/` (projects/Agency/ o categoria corrispondente).

## GOVERNANCE (Gate qualità)

memory-first gate: obbligatorio prima e dopo ogni task

Verifica struttura: `scripts/verify-empire.sh` (da creare in F2).

## IDENTITY-HR (Registro agenti)

Agenti di MEMORY: censiti in `company/Backbone/Identity-HR/registro-agenti.yaml`
Nuove assunzioni/ritiri: tramite 07-FORGE → Chief Forge → registro.

## COORDINATION (Ruflo)

Topologia swarm preferita: N/A (è sincrona: interroga → risponde → riceve checkpoint)

Namespace Ruflo: `ruflo memory init --namespace memory`
