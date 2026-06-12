> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L4 T-draft

# T-draft — Funzione L4: Draft della Skill (skill-creator)

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Tradurre la spec approvata (T-spec) in un **SKILL.md draft** usando `skill-creator`,
rispettando i vincoli di architettura (kernel ≤500 righe, progressive disclosure,
invarianti espliciti). È la fase di costruzione fisica dell'artefatto.

---

## Responsabilità

- Usare `skill-creator init` per impostare la struttura base del SKILL.md
- Scrivere il kernel (≤500 righe) con: descrizione, trigger, invarianti, processo, output
- Creare la cartella `references/` per il dettaglio oltre il kernel (progressive disclosure)
- Scrivere la trigger description ottimizzata (quando si attiva e quando NO)
- Produrre almeno 1 esempio concreto nel contesto DE (non generico)
- Verificare che il kernel non incorpori conoscenza che dovrebbe stare in skill separate (pattern #6)

---

## Struttura SKILL.md prodotto

```markdown
---
name: nome-skill
description: "Trigger description ottimizzata (quando sì / quando no)"
version: 1.0.0
tier: Haiku | Sonnet | Opus
ecosistema: XX-ECO
reparto: L2-REPARTO
---

# <Nome Skill>

## Invarianti (non negoziabili)
- invariante 1
- invariante 2

## Processo
1. passo 1
2. passo 2
...

## Input / Output
...

## Esempio concreto DE
...

## Quando NON usare questa skill
...

## Connessioni
- Usa: skill-A, skill-B
- Vedi references/ per dettaglio approfondito
```

---

## Regole di costruzione

1. **Kernel ≤500 righe** — tutto ciò che supera va in `references/` (link dal kernel)
2. **Nessun placeholder** — ogni sezione è completa o la skill non va in eval
3. **Esempio DE, non generico** — gli esempi usano casi reali di Digital Empire
4. **Pattern #6 rispettato** — il kernel referenzia skill, non ne duplica il contenuto
5. **Materia prima da INTELLIGENCE** — se Empire Studio ha già ingerito materiale, il draft parte da lì

---

## Agente operatore

`frg-skill-smith` (Sonnet) — usa `skill-creator` come strumento.

---

## Output

- `SKILL.md` completo (kernel + references/)
- Trigger description pronta per T-description-optimizer
- Dichiarazione tier + costo stimato per il registro HR

---

## KPI

| Metrica | Target |
|---|---|
| Kernel oltre 500 righe al primo draft | < 10% (segnale di spec troppo vaga) |
| Draft con placeholder non compilati | 0 |
| Esempi concreti DE per skill | ≥ 1 |
