> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L3 WF-SKILL-NEW

# WF-SKILL-NEW — Workflow L3: Creazione Nuova Skill

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Trasformare una richiesta di capability in una **skill installata, valutata e registrata**,
pronta all'uso negli ecosistemi richiedenti. Pipeline end-to-end: richiesta → spec → draft →
eval → package → installazione. Nessuna fase si salta (guard: `frg-sparc-warden`).

---

## Trigger di attivazione

- Un ecosistema invia handoff `{capability mancante, contesto, KPI, budget}` a `frg-chief`
- Il dossier 06-ECOSISTEMI-CORE elenca una skill prioritaria (es. P0: empire-verify, context-pack)
- INTELLIGENCE segnala un enrichment che richiede una nuova skill
- Memory Empire propone un artefatto che supera la soglia di sicurezza safe-enrich

---

## Fasi del workflow (in ordine — nessun salto)

| Fase | Attore | Output | Gate |
|---|---|---|---|
| **T-spec** | `frg-spec-writer` (agent-specification) | spec.md: cosa fa, NON fa, acceptance, out-of-scope | G-SPEC approvato da `frg-chief` |
| **T-draft** | `frg-skill-smith` + skill-creator | SKILL.md draft: kernel ≤500 righe + references/ | nessun placeholder, trigger description esplicita |
| **T-eval-runner** | `frg-eval-runner` | eval report con pass_rate ≥85% e variance analysis | G-EVAL ≥85% |
| **T-contradiction** | `frg-contradiction-gate` | contradiction-analyzer output verde | G-CONTRADICTION verde vs 121+ skill esistenti |
| **T-description-optimizer** | `frg-skill-smith` | trigger description ottimizzata (falsi positivi/negativi) | trigger clara e non ambigua |
| **Package + Install** | `frg-skill-smith` | skill installata in `.claude/skills/` (globale o di progetto) | skill caricabile e invocabile |
| **Registry** | `frg-hr-registrar` | skill-map.yaml aggiornato + pagina wiki tools/ | G-REGISTRY: zero skill orfane |

---

## Input / Output

**Input (handoff da frg-chief):**
```json
{
  "capability_mancante": "descrizione del gap",
  "ecosistema_target": "es. PLATFORM",
  "kpi_attesi": "es. build-time < 48h",
  "budget_max": "USD stimato per la forgiatura",
  "materia_prima": "link Empire Studio / file esistente se disponibile"
}
```

**Output (handoff all'ecosistema richiedente):**
```json
{
  "skill_id": "nome-skill",
  "path_installazione": ".claude/skills/nome-skill/",
  "eval_report": "path eval",
  "wiki_page": "second-brain-vault/wiki/tools/Tool_nome-skill.md",
  "pass_rate": 0.00
}
```

---

## Regole operative

1. **Esiste già?** — cerca in skills-map.yaml: duplicato → riusa/estendi (mai creare copie)
2. **Materia prima prima** — interroga INTELLIGENCE (namespace `intelligence/`): Empire Studio ha materiale? Se sì → content-forge parte da quello
3. **Kernel ≤500 righe** — pattern #7 progressive disclosure; dettaglio in `references/`
4. **Mai eval soggettiva** — pass_rate misurato, non "sembra buona"
5. **Ship = installa + registra** — consegna solo con G-REGISTRY chiuso

## KPI

| Metrica | Target |
|---|---|
| Tempo spec → consegna (skill semplice) | ≤ 2 giorni |
| Eval pass_rate | ≥ 85% |
| Contraddizioni bloccanti al primo audit | 0 |
| Skill orfane post-consegna | 0 |
