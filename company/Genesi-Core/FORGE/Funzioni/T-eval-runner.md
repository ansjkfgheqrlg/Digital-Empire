# T-eval-runner — Funzione L4: Valutazione Skill (Eval)

> **Ecosistema:** Genesi-Core / FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW · WF-SKILL-IMPROVE
> **Motore reale:** `skill-creator` (modulo eval/benchmark) — vedi `Motori/Mappa-Motori.md` #4
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]] · [[Motori/Mappa-Motori.md]]

---

## Missione
Misurare la qualità di una skill **con dati, non con opinioni**. Produce pass_rate, variance analysis
e un eval report che decide se la skill va in produzione o torna in draft. Soglia minima: ≥85% pass su
benchmark. È il **gate G-EVAL**, e precede i due gate Genesi Core a valle (MAXIMILIAN, Mandato): la FORGE
garantisce *contenuto eval-passed*, poi MAXIMILIAN giudica se è *all'altezza di Max*.

---

## Responsabilità
- Costruire/aggiornare il benchmark (casi con input/output attesi).
- Eseguire la skill sul benchmark e raccogliere i risultati.
- Calcolare pass_rate (casi superati / totali) e variance analysis (dove e perché fallisce).
- Per WF-SKILL-IMPROVE: confrontare baseline vs post-modifica.
- Archiviare l'eval report in `forge/evals/`.

---

## Struttura benchmark
- **Casi positivi** — input per cui la skill DEVE attivarsi e produrre output corretto.
- **Casi negativi** — input per cui NON deve attivarsi (anti-falsi-positivi).
- **Casi limite** — borderline che testano la robustezza della trigger description.
- **Casi DE reali** — scenari estratti da situazioni concrete di Digital Empire.

---

## Output: eval report
```markdown
# Eval Report: <nome-skill>
**Data:** YYYY-MM-DD · **Versione:** 1.x.x · **By:** frg-eval-runner
## Summary
Casi totali: N · Pass: X · Fail: Y · Pass_rate: XX%
Baseline (pre-improve): XX% · Delta: +/-XX%   (solo WF-SKILL-IMPROVE)
## Casi falliti (tabella: caso, input, atteso, prodotto, causa)
## Variance analysis (pattern di fallimento)
## Raccomandazione: PASS | FAIL | BORDERLINE
```

---

## Regola di soglia
- **≥85%** → G-EVAL verde → si procede a G-CONTRADICTION.
- **70-84%** → BORDERLINE: `frg-chief` decide se forzare iterazione o accettare con nota.
- **<70%** → FAIL: ritorna a T-draft con analisi cause.

## Agente operatore
`frg-eval-runner` (Haiku) — lavoro schematico, ripetitivo, misurabile: tier economico.

## KPI
| Metrica | Target |
|---|---|
| Skill in produzione con pass_rate <85% | 0 |
| Eval report senza variance analysis | 0 |
| Benchmark costruiti per skill rilasciata | 100% |
| Eval report archiviati in `forge/evals/` | 100% |
