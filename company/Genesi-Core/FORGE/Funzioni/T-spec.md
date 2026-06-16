# T-spec — Funzione L4: Specification (SPARC fase S)

> **Ecosistema:** Genesi-Core / FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW
> **Motore reale:** `agent-specification` (`~/.claude/skills/agent-specification/`) — vedi `Motori/Mappa-Motori.md` #1
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]] · [[Motori/Mappa-Motori.md]]

---

## Missione
Produrre la **spec completa e approvata** prima di qualsiasi build. È la fase S di SPARC: senza spec
approvata non parte nessuna costruzione — né skill, né agente, né workflow. Nel Genesi Core la spec
viaggia insieme al blueprint di ARCHITETTURA: T-spec verifica che la richiesta sia *completa di senso*,
ARCHITETTURA che sia *completa di forma*.

---

## Responsabilità
- Raccogliere il "problema" (gap di capability) dall'ecosistema richiedente.
- Definire esattamente cosa fa l'artefatto e cosa **NON** fa (out-of-scope).
- Scrivere acceptance criteria misurabili (non "funziona bene" — ma "pass_rate ≥85% su benchmark X").
- Identificare le dipendenze (cosa usa; chi userà questo).
- Dichiarare il tier modello e il costo stimato per run (→ OPERATIONS budget guard).
- Proporre il trigger description preliminare (passa poi a T-description-optimizer).

---

## Output standard (`spec.md`)
```markdown
# Spec: <nome-artefatto>
**Tipo:** skill | agente | team | workflow
**Richiedente:** <ecosistema>   **Data:** YYYY-MM-DD
**Blueprint:** HC-ARCH-FORGE/<id> (da ARCHITETTURA)
**Approvazione:** frg-chief (firma prima di procedere)

## Problema
[Gap di capability — funzionalità concreta, non organigramma]
## Cosa FA / Cosa NON FA (out-of-scope)
## Acceptance criteria (misurabili)
- [ ] criterio con metrica
## Trigger description (preliminare)
Si attiva quando ... · NON si attiva quando ... (anti-falsi-positivi)
## Dipendenze · Tier modello · Costo stimato/run
```

---

## Posto nella catena Genesi Core
ARCHITETTURA consegna `HC-ARCH-FORGE` (spec strutturale + blueprint). T-spec è il primo controllo
FORGE: se la spec non ha acceptance misurabili → reject verso ARCHITETTURA, non si costruisce.

## Agente operatore
`frg-spec-writer` (Sonnet) — usa `agent-specification` come motore.

## Gate
**G-SPEC**: spec approvata (`frg-chief` firma) PRIMA che chiunque inizi a costruire. Nessun bypass.

## KPI
| Metrica | Target |
|---|---|
| Spec rifiutate al gate G-SPEC | < 30% (alta qualità intake) |
| Spec con acceptance criteria non misurabili | 0 |
| Tempo intake → spec approvata (skill semplice) | ≤ 4 ore |
