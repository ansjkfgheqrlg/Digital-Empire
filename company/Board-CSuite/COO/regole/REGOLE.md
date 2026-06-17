---
Type: CONCEPT
Status: Active
Tags: #coo #regole #limiti #governance #ops
Created: 2026-06-17
Last updated: 2026-06-17
---

# REGOLE — COO (Chief Operating Officer)

> Limiti non negoziabili del dominio operations. Queste regole non si discutono in sessione:
> vengono applicate. Per cambiarle serve un ADR approvato da Max.
> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-COO.md` + v1 + ADR attivi

---

## REGOLA OPS-01 — Nessun INC chiuso senza post-mortem

Ogni incidente aperto (INC) può essere chiuso solo se contiene:
- Root cause identificata (anche "sconosciuta ma motivata")
- Fix applicato (temporaneo o definitivo)
- Prevenzione proposta
- Pattern bank entry assegnata

**Violazione:** coo-incident-handler blocca la chiusura e notifica il conductor.
**Rationale:** un INC chiuso senza imparare nulla è un INC che si ripeterà.

---

## REGOLA OPS-02 — Nessuna sessione senza WF-OPS-DAILY

Prima di toccare qualsiasi ecosistema, il team COO deve eseguire WF-OPS-DAILY e produrre
il semaforo operativo (verde/giallo/rosso). Non si parte "presumendo" che tutto sia verde.

**Violazione:** il conductor non ha autorità operativa finché il daily check non è completato.
**Rationale:** operare senza visibilità sullo stato è come volare senza strumenti.

---

## REGOLA OPS-03 — Flag COORDINAMENTO è bloccante

Se STATO-EMPIRE ha un flag `⚠️ COORDINAMENTO` su un'area, nessun agente COO (e nessun
socio) può modificare quell'area finché il flag non viene rimosso dall'owner.
La violazione di questa regola è la causa principale di conflitti Git catastrofici.

**Violazione:** coo-sync-keeper segnala immediatamente + alert all'umano che sta violando.
**Rationale:** ADR-004 è stato scritto dopo un'esperienza reale di collisione — rispettarlo è non ripeterla.

---

## REGOLA OPS-04 — Escalation con contesto completo

Quando il COO scala un problema al CEO/CFO/CTO, deve includere sempre:
- INC-ID o riferimento al problema
- Severità e impatto attuale
- Cosa è già stato tentato (contromisure applicate)
- Azione specifica richiesta al destinatario

**Violazione:** non si fa escalation con "c'è un problema, guarda tu". Chi riceve la
scalata deve poter agire immediatamente senza dover fare il triage da zero.
**Rationale:** l'escalation senza contesto è rumore, non segnale.

---

## REGOLA OPS-05 — Il COO non modifica il Backbone

Il COO monitora il Backbone (BUS, BRAIN, Governance, Observability, Coordination, Identity-HR)
ma non vi apporta modifiche dirette. Se rileva un'anomalia → segnala al CTO. Il CTO decide
e implementa. Il COO monitora l'esito.

**Violazione:** qualsiasi tentativo di fix diretto su componenti Backbone → INC aperto
sul comportamento del COO + escalation al CEO.
**Rationale:** il Backbone è infrastruttura condivisa. Modifiche non coordinate possono
rompere più di quanto riparano.

---

## REGOLA OPS-06 — Budget anomalo → stop immediato

Se una run supera il 95% del suo envelope di budget senza essere completata → la run viene
sospesa (non cancellata) e il coo-conductor notifica il CFO. Non si permette mai un overrun
silenzioso. La run può riprendere solo dopo approvazione esplicita del CFO.

**Violazione:** run che supera il 100% del budget senza alert → INC + escalation CEO/CFO.
**Rationale:** il budget è un contratto. Violarlo silenziosamente è una violazione di fiducia.

---

## REGOLA OPS-07 — Ogni HC rotto ha owner e deadline

Quando coo-handoff-auditor rileva un HC rotto o degradato, il coo-conductor assegna:
- Un owner (persona o agente responsabile del fix)
- Una deadline esplicita (non "presto" o "quando si può")
- Un follow-up schedulato (verifica completamento)

**Violazione:** HC rotto senza owner + deadline dopo 24h → escalation CEO.
**Rationale:** un problema senza owner non viene risolto. Un problema senza deadline si
trascina indefinitamente.

---

## REGOLA OPS-08 — La memoria è obbligatoria, non optionale

Ogni sessione COO si chiude con:
1. Checkpoint scritto in `company/Memory/checkpoints/`
2. STATO-EMPIRE aggiornato (sezione "Lavori in corso" + "RIPRESA DA")
3. `board/coo/stato-operativo` aggiornato in AgentDB

**Violazione:** sessione chiusa senza checkpoint → INC leggero aperto. Pattern di sessioni
senza checkpoint → escalation CEO (il sistema di memoria si sta degradando).
**Rationale:** ADR-002 (REGOLA ZERO MEMORY-FIRST). Nessun task è fatto finché non è in memoria.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[SKILLS]] · `skills/SKILLS.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[COO-README]] · `company/Board-CSuite/COO/README.md`
- [[ADR-002]] · `company/Memory/decisions/` (REGOLA ZERO MEMORY-FIRST)
- [[ADR-004]] · `company/Memory/decisions/` (sync Max↔Gael)
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
