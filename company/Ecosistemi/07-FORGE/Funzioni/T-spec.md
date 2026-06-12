> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L4 T-spec

# T-spec — Funzione L4: Specification (SPARC fase S)

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Produrre la **spec completa e approvata** prima di qualsiasi build. È la fase S di SPARC:
senza spec approvata non parte nessuna costruzione — né skill, né agente, né workflow.

---

## Responsabilità

- Raccogliere il "problema" (gap di capability) dall'ecosistema richiedente
- Definire esattamente cosa fa la skill/artefatto e cosa **NON** fa (out-of-scope)
- Scrivere acceptance criteria misurabili (non "funziona bene" — ma "pass_rate ≥85% su benchmark X")
- Identificare le dipendenze (skill/agenti che questa usa; skill che useranno questa)
- Dichiarare il tier modello e il costo stimato per run
- Proporre il trigger description (quando si attiva, quando NON si attiva — falsi positivi)

---

## Output standard (spec.md)

```markdown
# Spec: <nome-artefatto>
**Tipo:** skill | agente | team | workflow
**Richiedente:** <ecosistema>
**Data:** YYYY-MM-DD
**Approvazione:** frg-chief (firma richiesta prima di procedere)

## Problema
[Quale gap di capability risolve — in termini di funzionalità concreta, non di organigramma]

## Cosa FA
- ...

## Cosa NON FA (out-of-scope)
- ...

## Acceptance criteria (misurabili)
- [ ] criterio 1 con metrica
- [ ] criterio 2 con metrica

## Trigger description
**Si attiva quando:** ...
**NON si attiva quando:** ... (anti-falsi-positivi)

## Dipendenze
- Usa: skill-A, skill-B
- Usata da: ecosistema X, workflow Y

## Tier modello: Haiku | Sonnet | Opus
## Costo stimato/run: $X.XX
```

---

## Agente operatore

`frg-spec-writer` (Sonnet) — usa `agent-specification` come tool interno.

---

## Gate

**G-SPEC**: la spec è approvata (`frg-chief` firma) PRIMA che qualsiasi altro agente
inizia a costruire. Spec senza approvazione = spec invalida. Nessun bypass.

---

## KPI

| Metrica | Target |
|---|---|
| Spec rifiutate al gate G-SPEC | < 30% (alta qualità intake) |
| Spec con acceptance criteria non misurabili | 0 |
| Tempo intake → spec approvata | ≤ 4 ore (skill semplice) |
