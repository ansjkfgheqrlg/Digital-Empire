---
name: fas-qa-gate
reparto: FORGE-AGENT-SKILL
intestazione_adr008: { proprietario: 06b-FORGE (L2.5 METHOD-GUARD), controllore: Ispettorato Generale (audit), origine: FORGE, governo: ADR-002/006 }
versione: v1 (2026-07-20)
---

# fas-qa-gate — Gate bloccante di qualità (indipendente: verifica, non forgia)

## Scopo
Ultimo passaggio prima della registrazione: niente esce dal reparto senza verbale PASS/FAIL.

## Checklist di gate (tutti bloccanti)
1. **7 file canonici presenti** (o formato skill completo per skill) — niente stub, niente TODO/placeholder.
   **Se team (MIR-9, R2-bis):** anche `topology.md` compilato (tipo motivato, nodi = agenti 7-file reali
   — no agenti fantasma — edges con contratti, escalation, memory touchpoints, kill-criteria).
2. **MKD esiste** e copre la sorgente: coverage atomi ≥95% nel MKD (campione di 20 atomi a sorte).
3. **Failure-modes.md** con ≥5 righe compilate; **evals.md** con ≥5 casi e atteso.
4. **Intestazione ADR-008** presente in testa a spec.md/SKILL.md (proprietario/controllore/origine/governo reali — mai inventati).
5. **No collisioni**: slug libero in `skills-map.yaml` e `REGISTRO-IMPRESA.md`; nessun agente/skill esistente reso obsoleto senza ADR.
6. **Motori intatti**: diff su `copy-workflow/`, `content-forge2.0/`, `master-build-architecture/` = zero modifiche (ADR-003).
7. **Memoria**: piano in `memory/plans/` con **sezione `## ASK` compilata** (MIR-3, ASK-PROTOCOL: max 3 domande mirate con raccomandazione+default, oppure "0 domande" motivata; FAIL su domande-ombrello), verbale in `memory/checkpoints/`, CP globale predisposto.

## Output
Verbale in `FORGE-AGENT-SKILL/memory/checkpoints/GATE-<slug>-<data>.md`:
elenco controlli PASS/FAIL + difetti trovati. FAIL → ritorno al smith con lista difetti (max 2 giri,
poi escalation al conductor/Max). PASS → via libera alla registrazione.

## Anti-recidiva (regola Ispettorato, dossier 15)
Ogni FAIL ripetuto (stessa causa 2 volte) → regola nuova proposta in `FORGE-AGENT-SKILL/rules/`.
