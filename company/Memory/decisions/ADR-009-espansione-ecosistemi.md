# ADR-009: Espansione Holding da 10 a 13 Ecosistemi Permanenti

**Stato:** ATTIVA
**Data:** 2026-07-23
**Decisore:** Max (Owner)
**Controllore:** Claude

## Contesto
La regola originale `ADR-001` stabiliva che la holding "Digital Empire" fosse composta da esattamente 10 ecosistemi canonici. Nel tempo, l'innovazione della factory ha portato alla creazione di 3 nuovi poli di grande spessore:
- **APEX-7 CORE** (Sistema di ottimizzazione avanzato e Quality Gates chirurgici)
- **STREAM-S7-BOT** (Bot sperimentali per NFT/Memecoin)
- **ARENA-APEX** (Progetti legati all'arena e LMArena)

Inizialmente sono stati parcheggiati in `company/Ecosistemi/` con prefissi anomali (es. `00-`, e due `08-` e due `09-`), causando collisioni nella risoluzione dei path e fallimenti nel controllo conformità di sistema (`empire conform`).

## Decisione
Si decide di derogare all'ADR-001 ed espandere formalmente la Holding a **13 ecosistemi canonici**.

1. La cartella `company/Ecosistemi/` accetta ora 13 directory.
2. I nuovi ecosistemi vengono rinumerati per evitare conflitti con la numerazione classica (01-10):
   - `11-APEX-7-CORE` (ex 00-)
   - `12-STREAM-S7-BOT` (ex 08-)
   - `13-ARENA-APEX` (ex 09-)
3. L'ecosistema `11-APEX-7-CORE` assorbe come sua architettura portante ("Backbone") la *APEX-7 Deep Refinement - Iterazione Chirurgica*, stabilendo i concetti di Quality Gate, Gate Agent (GATE-1), Memory Query Interface ed Event Bus.

## Conseguenze
- Il comando `python -m empire conform` non andrà più in errore (block) per la presenza di questi ecosistemi.
- Ognuno di questi ecosistemi è vincolato all'Art. 8, necessitando di `ECOSISTEMA.md` e `BACKBONE.md`.
- Ogni futuro ecosistema (dal 14 in su) necessiterà di un nuovo ADR prima di poter essere inserito.
