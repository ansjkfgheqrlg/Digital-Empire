---
Type: CONCEPT
Status: Active
Tags: #regole #copywriting #gate #L2-1 #mandato
Created: 2026-06-18
Last updated: 2026-06-18
---

# REGOLE — L2.1 Copywriting (non negoziabili)

> Le regole bloccanti del reparto. A differenza dei principi (orientano), le regole BLOCCANO.
> Dossier: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §L2.1, §7.

---

## R1 — Motore Copy Workflow intoccabile (ADR-003)

NESSUN file in `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` viene modificato da questo
reparto. Il reparto wrappa e registra; non riscrive. Qualsiasi evoluzione del motore passa da un
ADR dedicato, non da una modifica diretta. Violazione = rollback immediato.

## R2 — Gate A8 bloccante

Nessun copy esce con score A8 < soglia (80 standard · 85 sales page e proposte commerciali). Sotto
soglia → iterazione mirata (COPY-QA-LEAD decide fix vs rifacimento), massimo 3 cicli, poi escalation
umana. Mai consegna sotto soglia.

## R3 — P prima di S inviolabile

Se il Problema appare dopo la Soluzione nel copy: −15 automatico al punteggio. Non è discrezionale,
non si negozia, non dipende dal formato (Art.4.2 Mandato).

## R4 — Nessun claim senza proof (CPB)

Ogni affermazione centrale ha una proof esplicita. Un claim senza proof blocca il PASS
indipendentemente dallo score totale. La penna non inventa numeri: se non c'è il dato, si elimina
il claim o si segna [DM] e si richiede la proof al committente.

## R5 — Brand gate G2 non derogabile

Ogni copy passa il brand gate (voce diretta/provocatoria/trasparente, APSOC, pricing one-time
corretto, zero AI-slop, brand_kit dichiarato). Fail = blocco. Solo LX (Board) deroga (Art.4.1).

## R6 — Avatar obbligatorio prima di scrivere

Nessun copy si scrive senza ICP/avatar definito. Richiesta senza `icp` → spawna A2/T-AVATAR PRIMA.
Scrivere "a sensazione" senza avatar è vietato (regola contratto §1.2 dossier).

## R7 — Cold outreach: standard qui, esecuzione in 01-AGENCY

Il reparto possiede lo STANDARD del cold (APSOC+V) e ne fa QA via T-REVIEW. L'esecuzione operativa
del cold outreach (writer.py, invii) resta in 01-AGENCY. L2.1 non manda email cold, le standardizza.

## R8 — Naming e memoria

Ogni copy prodotto produce un record di score in `marketing/copy/scores` e, se vincente con evidenza,
un pattern in `marketing/copy/patterns/{icp}`. Nessun apprendimento si butta via.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[copy-qa-lead]] · `agenti/copy-qa-lead.md`
- [[MANDATO-EMPIRE]] Art.2 + Art.4
- [[ADR-003-migrazione-wrap-non-riscrittura]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
