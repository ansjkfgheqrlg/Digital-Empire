# ADR-MB-002 — Autonomia progressiva, non binaria

- **Data:** 2026-07-20
- **Stato:** ATTIVO
- **Decisori:** MB Social Director / CF-R6 / CF-R7

## Contesto

La direttiva richiede operatività 100% automatizzata. Attivarla prima di token, staging, canary e post-check produrrebbe un'automazione solo dichiarata o pericolosa.

## Decisione

Quattro modalità: SHADOW, SUPERVISED, CERTIFIED_AUTO, PAUSED. Il target è CERTIFIED_AUTO, ma la transizione richiede evidence: 5 dry-run, token health, canary publish, post-check, insights e security scan.

## Alternative scartate

- Full auto immediato — nessuna prova live, rischio reputazionale.
- Review umana per sempre — non soddisfa il modello operativo autonomo.

## Conseguenze

Dopo certificazione non serve approvazione per-post, ma restano quality gate automatici, daily cap, idempotenza e kill switch.

## Contradiction-check

Evolve il vincolo storico di review umana senza bypassarlo: la review iniziale diventa un gate di certificazione del sistema, poi l'autorevisione è permessa solo nel perimetro certificato.
