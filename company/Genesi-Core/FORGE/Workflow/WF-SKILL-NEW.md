# WF-SKILL-NEW
## Blueprint skill (da ARCHITETTURA) → skill installata, valutata, registrata

> Organo: FORGE (Genesi Core) · Reparto owner: L2.1 SKILL-WORKS · Stato: DEFINED
> Riceve un **blueprint skill validato** da ARCHITETTURA (HC-ARCH-FORGE, schema `skill@v3`) e ci
> scrive dentro il CONTENUTO: SKILL.md (kernel ≤500 righe) + references/ + evals. Mai inventa la
> struttura — la struttura arriva già architettata e PASS. Motore reale: `skill-creator`.
> Collega: [[WF-ARCH-DESIGN]] · [[WF-FORGE-PIPELINE]] · [[ECOSISTEMA.md]]

---

## Trigger
- Arriva da ARCHITETTURA un blueprint con `forma_scelta = "skill"` (HC-ARCH-FORGE).
- `frg-chief` instrada a SKILL-WORKS dopo verifica `validazione=PASS`.
- Variante target Claude Browser → motore `omega-create` (fasi SPARC identiche, cambia solo il tool in R).
- **Natura:** è la specializzazione "skill" di WF-FORGE-PIPELINE; il MKD si applica se c'è materia prima.

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0617-014",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-014",
  "schema_usato": "skill@v3",
  "forma_scelta": "skill",
  "spec_ref": "architettura/blueprint/ARCH-2026-0617-014#spec",
  "pattern_riusati": ["competitor-profiling/progressive-disclosure"],
  "validazione": "PASS",
  "materia_prima": "intelligence/empire-studio/<run> | null",
  "kernel_target_righe": 380
}
```
- `validazione != PASS` → rigetto, ritorno ad ARCHITETTURA. Niente skill costruita al buio.

---

## Pipeline (passi · agente owner)
```
1. APERTURA + ANTI-DUPLICATO          (frg-chief → frg-skill-smith)
   └── verifica PASS; cerca in skills-map.yaml: duplicato? → WF-SKILL-IMPROVE (estendi, non copiare)

2. MATERIA-PRIMA → MKD (se serve)     (frg-mkd-forger · content-forge)
   └── materiale ingerito su questo tema? SÌ → MKD intermedio (espandere, non riassumere). NO → draft diretto.

3. DRAFT KERNEL + REFERENCES          (frg-skill-smith · skill-creator)
   └── SKILL.md kernel ≤500 righe (progressive disclosure #7) + references/ + trigger description esplicita
        DENTRO la struttura del blueprint (sezioni, references, evals già definiti da ARCHITETTURA)

4. EVAL                               (frg-eval-runner)   →  G-EVAL
   └── pass_rate misurato (mai "sembra buona") + variance analysis → ≥85% o iterazione (max 2 cicli)

5. DESCRIPTION-OPTIMIZER              (frg-skill-smith)
   └── trigger description ottimizzata su falsi positivi/negativi (triggering accuracy)

6. CONTRADICTION + PACKAGE            (frg-contradiction-gate → frg-skill-smith)
   └── analyzer VERDE vs skill esistenti → package + install in .claude/skills/ (globale o progetto)

7. CONSEGNA + REGISTRO                (frg-hr-registrar + frg-chief)
   └── build_ref CLOSED · pagina wiki tools/ · handoff a MAXIMILIAN → Mandato → Identity-HR
```

---

## Gate
- **G-FORGE0:** `validazione != PASS` → rigetto ad ARCHITETTURA.
- **G-EVAL:** pass_rate ≥ 85% (borderline 70-84% → decide `frg-chief`); mai eval soggettiva.
- **G-KERNEL:** SKILL.md kernel ≤500 righe; dettaglio in `references/` (pattern #7).
- **G-CONTRADICTION:** `skill-contradiction-analyzer` VERDE vs skill esistenti, altrimenti stop.
- **G-REGISTRY:** skill non si consegna senza skills-map.yaml aggiornato + pagina wiki → zero skill orfane.

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0617-014",
  "skill_id": "battle-card-forge",
  "artefatto_path": ".claude/skills/battle-card-forge/SKILL.md",
  "build_ref": "forge/builds/ARCH-2026-0617-014",
  "wiki_page": "second-brain-vault/wiki/tools/Tool_battle-card-forge.md",
  "eval": "PASS",
  "pass_rate": 0.91,
  "contraddizioni": "VERDE",
  "handoff_to": "MAXIMILIAN",
  "status": "delivered"
}
```

---

## Handoff
- **In ingresso:** HC-ARCH-FORGE da `WF-ARCH-DESIGN` (blueprint skill validato, schema `skill@v3`).
- **In uscita:** consegna a **MAXIMILIAN** (all'altezza di Max?) → **Mandato** (lecita?) → **Identity-HR** (registra in skills-map.yaml + wiki) → VIVO.
- **Confine:** ARCHITETTURA disegna sezioni/references/evals; SKILL-WORKS ci scrive il contenuto. Modifica della forma = nuovo giro ARCH.

---

## Dry-run
Blueprint validato di `battle-card-forge` (SKILL.md + references/ + evals, schema `skill@v3`, riuso
`competitor-profiling`). frg-skill-smith scrive il kernel (≤500 righe) dentro la forma data, frg-eval-runner
ottiene 0.91, description-optimizer pulisce i trigger, frg-contradiction-gate VERDE, package+install,
frg-hr-registrar registra → consegna a MAXIMILIAN. La struttura non è mai stata della FORGE.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — produce il blueprint skill in ingresso
- [[WF-FORGE-PIPELINE]] — motore generale di cui questo è la specializzazione "skill"
- [[WF-SKILL-IMPROVE]] — ramo per skill già esistente · [[WF-SKILL-AUDIT]] — gate anti-drift a monte
- [[frg-skill-smith]] · [[frg-eval-runner]] · [[frg-contradiction-gate]] · [[frg-hr-registrar]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.1 SKILL-WORKS — fonte di verità
