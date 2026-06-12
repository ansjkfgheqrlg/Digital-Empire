> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L4 T-eval-runner

# T-eval-runner — Funzione L4: Valutazione Skill (Eval)

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW · WF-SKILL-IMPROVE

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Misurare la qualità di una skill **con dati, non con opinioni**. Produce pass_rate,
variance analysis e un eval report che decide se la skill va in produzione o torna in
draft. Soglia minima: ≥85% pass su benchmark. Gate G-EVAL.

---

## Responsabilità

- Costruire o aggiornare il benchmark per la skill (set di casi di test con input/output attesi)
- Eseguire la skill sul benchmark e raccogliere i risultati
- Calcolare pass_rate (casi superati / casi totali)
- Produrre variance analysis (dove fallisce? perché? pattern di fallimento?)
- Per WF-SKILL-IMPROVE: confrontare score baseline vs score post-modifica
- Archiviare l'eval report in `forge/evals/`

---

## Struttura benchmark

Ogni benchmark contiene:
- **Casi positivi**: input per cui la skill DEVE attivarsi e produrre output corretto
- **Casi negativi**: input per cui la skill NON deve attivarsi (anti-falsi-positivi)
- **Casi limite**: input borderline che testano la robustezza della trigger description
- **Casi DE reali**: scenari estratti da situazioni concrete di Digital Empire

---

## Output: eval report

```markdown
# Eval Report: <nome-skill>
**Data:** YYYY-MM-DD · **Versione skill:** 1.x.x · **Eval by:** frg-eval-runner

## Summary
- Casi totali: N
- Pass: X | Fail: Y | Pass_rate: XX%
- Baseline (pre-improve): XX% (solo per WF-SKILL-IMPROVE)
- Delta: +/-XX%

## Casi falliti (analisi)
| Caso | Input | Output atteso | Output prodotto | Causa |
|---|---|---|---|---|

## Variance analysis
[Pattern di fallimento: dove la skill è debole?]

## Raccomandazione
PASS (deploy) | FAIL (ritorna a T-draft con note) | BORDERLINE (review frg-chief)
```

---

## Agente operatore

`frg-eval-runner` (Haiku) — lavoro schematico, ripetitivo, misurabile: tier economico.

---

## Regola di soglia

- **Pass_rate ≥85%** → G-EVAL verde, si procede a G-CONTRADICTION
- **Pass_rate 70-84%** → BORDERLINE: `frg-chief` decide se forzare iterazione o accettare con nota
- **Pass_rate <70%** → FAIL: ritorna a T-draft con analisi cause

---

## KPI

| Metrica | Target |
|---|---|
| Skill in produzione con pass_rate <85% | 0 |
| Eval report con variance analysis assente | 0 |
| Benchmark costruiti per skill rilasciata | 100% |
| Archiviazione eval report in forge/evals/ | 100% |
