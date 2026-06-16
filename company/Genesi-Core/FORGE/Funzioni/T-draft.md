# T-draft — Funzione L4: Draft della Skill (skill-creator)

> **Ecosistema:** Genesi-Core / FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW
> **Motore reale:** `skill-creator` (`~/.claude/skills/skill-creator/SKILL.md`) — vedi `Motori/Mappa-Motori.md` #4
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]] · [[Motori/Mappa-Motori.md]]

---

## Missione
Tradurre la spec approvata (T-spec) **dentro il blueprint validato da ARCHITETTURA** in un `SKILL.md`
draft usando `skill-creator`, rispettando i vincoli di architettura (kernel ≤500 righe, progressive
disclosure, invarianti espliciti). È la fase di costruzione fisica del CONTENUTO: la forma vuota arriva
da ARCHITETTURA, T-draft la riempie.

---

## Responsabilità
- Usare `skill-creator init` per impostare la struttura base del `SKILL.md`.
- Scrivere il kernel (≤500 righe): descrizione, trigger, invarianti, processo, output.
- Creare `references/` per il dettaglio oltre il kernel (progressive disclosure, pattern #7).
- Scrivere la trigger description ottimizzata (poi rifinita da T-description-optimizer).
- Produrre almeno 1 esempio concreto nel contesto DE (non generico).
- Verificare che il kernel non incorpori conoscenza che dovrebbe stare in skill separate (pattern #6).

---

## Struttura `SKILL.md` prodotto
```markdown
---
name: nome-skill
description: "Trigger ottimizzata (quando sì / quando no)"
version: 1.0.0
tier: Haiku | Sonnet | Opus
ecosistema: XX-ECO   reparto: L2-REPARTO
---
# <Nome Skill>
## Invarianti (non negoziabili)
## Processo
## Input / Output
## Esempio concreto DE
## Quando NON usare questa skill
## Connessioni  (Usa: skill-A, skill-B · vedi references/)
```

---

## Regole di costruzione
1. **Kernel ≤500 righe** — il resto in `references/` (link dal kernel).
2. **Nessun placeholder** — ogni sezione completa o la skill non va in eval.
3. **Esempio DE, non generico** — casi reali di Digital Empire.
4. **Pattern #6** — il kernel referenzia skill, non ne duplica il contenuto.
5. **Materia prima da INTELLIGENCE** — se Empire Studio ha già ingerito materiale, il draft parte da lì (via content-forge, vedi T-... WORKFLOW-WORKS).
6. **Forma da ARCHITETTURA** — la struttura del SKILL.md è quella dello schema canonico `Schema-Skill`.

## Agente operatore
`frg-skill-smith` (Sonnet) — usa `skill-creator`.

## Output
`SKILL.md` completo (kernel + references/) · trigger pronta per T-description-optimizer · dichiarazione tier + costo per il registro HR.

## KPI
| Metrica | Target |
|---|---|
| Kernel oltre 500 righe al primo draft | < 10% (spec/blueprint troppo vaghi) |
| Draft con placeholder non compilati | 0 |
| Esempi concreti DE per skill | ≥ 1 |
