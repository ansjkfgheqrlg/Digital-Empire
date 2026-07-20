# ADR-009 — Autonomia social certificata per account first-party

- **Data:** 2026-07-20
- **Stato:** ATTIVO
- **Decisori:** Max (direttiva automazione completa) / Chief-Forge / CF-R6 / CF-R7

## Contesto

Il Piano Maestro storico impone review umana pre-pubblicazione nelle fasi iniziali; il dossier 16 S4 impone che `mentalita.brutale` si riattivi solo con produzione→autorevisione→pubblicazione→analisi al 100% automatiche. Serviva una transizione misurabile tra i due vincoli, senza trasformare “full auto” in un bypass della qualità.

## Decisione

Per canali **first-party posseduti e amministrati** dalla holding, la review umana per-post può essere rimossa solo quando il tenant supera una certificazione progressiva:

1. `SHADOW` — zero side effect;
2. `SUPERVISED` — canary reali con conferma esplicita;
3. `CERTIFIED_AUTO` — scheduler autonomo senza review per-post;
4. `PAUSED` — kill switch.

Il passaggio a `CERTIFIED_AUTO` richiede evidence persistita: almeno 5 dry-run PASS, token/account health, canary publish, post-check/permalink, Insights e secret scan. Anche dopo la certificazione restano obbligatori: gate indipendente CF-R6, cap, token/quota check, idempotenza, audit trail e kill switch.

Questa ADR autorizza il modello; **non dichiara certificato alcun canale**. `mentalita.brutale` parte in SHADOW.

## Alternative scartate

- Full auto immediato — nessun OAuth/canary/evidence, rischio reputazionale e operativo.
- Review umana per sempre — contraddice il modello business richiesto e S4.
- Review casuale non formalizzata — non riproducibile, nessun criterio di cutover/rollback.

## Conseguenze

- CF-R7 aggiorna i workflow futuri: “review umana obbligatoria nelle fasi iniziali” diventa “certificazione obbligatoria; review per-post rimossa solo in CERTIFIED_AUTO”.
- Un errore di token, quota, gate, account mismatch, duplicato o safety porta a stop/PAUSED, non a retry cieco.
- Per account clienti/third-party restano necessari permessi, contratti, App Review e policy specifiche; questa ADR non concede automazione indiscriminata.

## Contradiction-check

Risolve esplicitamente la tensione tra il vincolo storico CF-R7 e S4 dossier 16. Coerente con ADR-002 (evidence/memoria), ADR-003 (wrap), ADR-006 (test/gate) e ADR-008 (owner/controller/origine/governo).
