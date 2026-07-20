# ADR-MB-003 — Wrappare i motori esistenti

- **Data:** 2026-07-20
- **Stato:** ATTIVO
- **Decisori:** ARCHITETTURA / FORGE

## Contesto

Esistono già `carousel-factory`, asset MB e `mentalita_orchestrator.py`. Riscriverli romperebbe ADR-003 globale e disperderebbe lavoro utile.

## Decisione

MB-OS usa il manifest come adapter. Carousel-factory continua a renderizzare; MB-OS valida, converte PNG→JPEG, effettua staging e pubblica. Il publisher legacy non viene cancellato; le sue configurazioni vengono solo bonificate dai segreti.

## Alternative scartate

- Nuovo renderer completo — duplicazione senza KPI che lo giustifichi.
- Modifica invasiva del renderer — rischio regressione su asset già prodotti.

## Conseguenze

Il seam è il manifest. Nuovi engine si aggiungono senza cambiare orchestrazione. La qualità visuale del renderer resta oggetto di gate/rework separato.

## Contradiction-check

Implementazione diretta di ADR-003 e ADR-008.
