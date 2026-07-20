# 🧠 MEMORY — carousel-factory (W4) — memory locale (MIR-1, 2026-07-20)

> Memory AGGIUNTIVA (wrap ADR-003). Owner: 03-CONTENT-FACTORY / CF-R5 · Controllore: CF-R6 QA & Gate + METHOD-GUARD.
> Motore: `carousel-factory/` vendored (node, generate). Brand attivi: mentalita-brutale, crea-illtuo_impero.

## Stato
- Tile EmpireDesk "Caroselli": fix B0 pushato da Gael (`2f885014`); verifica selftest 8/8 = task aperto di Gael (ordine pivot, NON tocco).
- Questa memory serve al reparto CF-R5 per esecuzioni ricorrenti (batch caroselli per funnel/pagine).

## Regole di lavoro
1. ADR-003: il motore vendored non si modifica; fix solo se upstream lo permette, altrimenti wrapper esterni + riga in REGISTRO-ERRORI.
2. Input caroselli = JSON in `carousel-factory/input/` (il motore richiede il path JSON come argomento: senza → exit 1, CE-1).
3. Ogni brand: configurazione in `carousel-factory/brands/`; non mischiare brand in una stessa run.
4. Errore reale → REGISTRO-ERRORI (causa+fix+regola) prima di riprovare.

## Note operative
- Output: `carousel-factory/output/`.
- I template in `carousel-factory/templates/` definiscono layout/branding (modifica = intervento CF-R5 con gate CF-R6).
- Collegamento noto col gestionale (dossier 16): S4 mentalita.brutale SOLO se pipeline 100% automatica (condizione Max).

## Storico eventi (ultima in cima)
- 2026-07-20 — Memory locale + REGISTRO-ERRORI creati (MIR-1/6, FORGE-AGENT-SKILL).
