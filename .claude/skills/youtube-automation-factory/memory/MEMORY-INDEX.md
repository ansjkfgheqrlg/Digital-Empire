# MEMORY-INDEX — youtube-automation-factory

> Porta d'ingresso alla memoria della fabbrica. Una riga per checkpoint/decisione.
> Gestita da `memory-keeper` (invariante #6: memoria dal passo zero).

## Stato
- Fabbrica **v1.0** costruita 2026-07-21 (metodologia MBA + CF2). Non ancora usata su una nicchia reale.
- Nicchia attiva: _nessuna_ (RIPRESA DA: eseguire WF1 su una nicchia scelta da Max).

## Checkpoints
- [CP-000](checkpoints/CP-000.md) — bootstrap fabbrica (build iniziale).

## Decisions
- [DEC-000](decisions/DEC-000.md) — 7 sezioni canoniche in 1 file per agente (invece di 7 file).

## Convenzioni
- Checkpoint: `checkpoints/CP-<YYYYMMDD>-<n>.md` (idempotente).
- Decisione: `decisions/DEC-<slug>.md`.
- Ogni run di `/yt-factory` apre un CP a fine di ogni fase e chiude con RIPRESA DA.
