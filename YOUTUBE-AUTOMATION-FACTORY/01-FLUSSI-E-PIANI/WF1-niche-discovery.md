# WF1 — Niche Discovery (Fase 1)

> Obiettivo: da un tema di partenza a una **nicchia validata** + **canali cash cow**, con gate.

## Precondizione (bloccante)
- Account YouTube **neutro** (vergine/dedicato) con **Video IQ** installato. Se manca → STOP, crealo.

## DAG
```
[input: tema]
   │
   ▼
niche-scout ── raccoglie canali+metriche (Video IQ) ──► cashcow_check.py (indice 0-100)
   │
   ▼
scheda-nicchia.md  (nicchia + 1-3 canali cash cow + esempi video top + note cross-lingua)
   │
   ▼
⟨ niche-gate ⟩  PASS? ──no──► torna a niche-scout (motivi elencati)
   │ sì
   ▼
[output: nicchia certificata]  → memory-keeper (DEC nicchia) → WF2
```

## Passi
1. `niche-scout`: verifica account neutro → esplora → compila `scheda-nicchia.md`.
2. `cashcow_check.py`: calcola l'indice per ogni canale candidato.
3. `niche-gate`: checklist bloccante (nicchia coerente · ≥1 cash cow ≥60 · replicabile Fliki).
4. `memory-keeper`: `DEC-nicchia-<slug>.md` + CP di fase.

## Output atteso
`scheda-nicchia.md` con verdetto niche-gate = PASS e nicchia registrata in memoria.

## Criteri di fatto (Definition of Done)
- [ ] Account neutro confermato
- [ ] ≥1 canale cash cow con indice ≥60
- [ ] Nicchia replicabile con Fliki
- [ ] niche-gate PASS + DEC salvata
