> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L3 WF-SKILL-IMPROVE

# WF-SKILL-IMPROVE — Workflow L3: Miglioramento Skill Esistente

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Aggiornare una skill già in produzione con **nuova conoscenza** (da Empire Studio, ReasoningBank,
o feedback operativi), misurando il guadagno reale prima/dopo. Regola fondamentale: **backup +
diff + eval prima/dopo** prima di toccare qualsiasi skill attiva (G-SAFE-ENRICH di INTELLIGENCE,
ereditato da Memory Empire v3).

---

## Quando si usa

- Memory Empire segnala un enrichment che supera la soglia safe ma richiederebbe modifica
- INTELLIGENCE ha ingerito nuovo materiale rilevante per una skill esistente
- Il ReasoningBank ha distillato un pattern di fallimento ricorrente (≥3 conferme) su una skill
- Un ecosistema segnala reject rate in aumento su una skill (trigger da Quality-Sentinel)
- Eval score scende sotto 85% in monitor periodico di `frg-eval-runner`

---

## Fasi del workflow

| Fase | Attore | Output | Gate |
|---|---|---|---|
| **Snapshot backup** | `frg-skill-smith` | copia versionata della skill originale | backup presente prima di qualsiasi modifica |
| **Context enrichment** | `frg-mkd-forger` | MKD con la nuova conoscenza da integrare | MKD completo, non riassunto |
| **Diff proposto** | `frg-skill-smith` | diff annotato: cosa si cambia e perché | diff approvato da `frg-chief` prima di applicare |
| **Eval baseline** | `frg-eval-runner` | eval score sulla skill ORIGINALE (baseline) | score registrato in `forge/evals/` |
| **Integrazione** | `frg-skill-smith` | skill aggiornata con nuovo contenuto | kernel rimane ≤500 righe; nessuna regressione di formato |
| **Eval post** | `frg-eval-runner` | eval score post-modifica | G-EVAL: score post ≥ baseline e ≥ 85% |
| **Contradiction check** | `frg-contradiction-gate` | analyzer output verde | G-CONTRADICTION: nessuna contraddizione bloccante introdotta |
| **Rollback gate** | `frg-skill-smith` | decisione: deploy o rollback al backup | se score post < baseline → rollback automatico |

---

## Input / Output

**Input:**
```json
{
  "skill_id": "nome-skill da migliorare",
  "nuova_conoscenza": "link Empire Studio / pattern ReasoningBank / feedback operativi",
  "motivo": "descrizione del gap o fallimento",
  "approvazione": "frg-chief"
}
```

**Output:**
```json
{
  "skill_id": "nome-skill",
  "versione_prima": "eval_baseline_score",
  "versione_dopo": "eval_post_score",
  "diff_summary": "cosa è cambiato",
  "stato": "deployed | rolled_back"
}
```

---

## Regola non negoziabile

La skill migliorata non si consegna se il pass_rate post è inferiore al baseline.
Un miglioramento che peggiora le performance è un bug, non una feature — rollback immediato
e apertura di issue in `forge/evals/` per analisi causa radice.

## KPI

| Metrica | Target |
|---|---|
| Skill migliorate con gain positivo (post > baseline) | ≥ 80% delle improve |
| Rollback necessari (regressione) | < 20% |
| Tempo da segnalazione a deploy | ≤ 3 giorni |
