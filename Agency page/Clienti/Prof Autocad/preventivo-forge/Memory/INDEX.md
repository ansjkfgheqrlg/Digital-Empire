# 🧠 Memory — PreventivoForge

Memoria viva del workflow: **ogni decisione** e **ogni preventivo prodotto** vengono registrati qui,
in ordine cronologico, perfettamente organizzati. È la storia completa del sistema.

## Struttura
- `decisioni/` — decisioni di design/prodotto (una per file, `DEC-NNN-*.md`). Regole, scelte, cambi.
- `storico-preventivi/` — un file per ogni preventivo generato (data + auto + id annuncio + esito + prezzo + path PDF).
- `regole/` → le regole sacre stanno in `../regole/REGOLE-SACRE.md` (verificate ad ogni run).

## Regola d'oro
Ogni volta che si genera un preventivo → si aggiunge una voce in `storico-preventivi/`.
Ogni volta che si prende una decisione → un file in `decisioni/` + una riga qui sotto.

## Decisioni (cronologia)
- [DEC-001](decisioni/DEC-001-template-novacar.md) — 2026-07-01 — Template PDF ufficiale = modello Novacar + REGOLE-SACRE inviolabili.

## Preventivi prodotti (cronologia)
- [2026-07-01 · Mercedes GLA 220 (456259857)](storico-preventivi/2026-07-01_mercedes-gla-220_456259857.md) — esposto 47.490 → finale 51.915 € · 4 gate verdi (formato pre-Novacar).
