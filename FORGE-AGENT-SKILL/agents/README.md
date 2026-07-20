# 🎭 ROSTER — FORGE-AGENT-SKILL (4 agenti v1)

| Agente | Ruolo | Modello consigliato | Files |
|---|---|---|---|
| `fas-conductor` | Direttore del reparto: riceve richieste capability, scrive il PIANO DI FORGIA (MKD plan, 7-file plan, gate plan), smista a smith/qa, tiene la memoria | Sonnet | spec.md, system-prompt.md |
| `fas-agent-smith` | Forgia agenti e team: content-forge `--target=agent|team` + standard 7 file canonici impero | Sonnet | spec.md, system-prompt.md |
| `fas-skill-smith` | Forgia skill ufficiali: content-forge `--target=skill` + progressive disclosure (kernel ≤550r + references/) | Sonnet | spec.md, system-prompt.md |
| `fas-qa-gate` | Gate BLOCCANTE indipendente (non forgia: verifica): 7-file check, coverage ≥95%, 0 stub/TODO, failure-modes + evals presenti, intestazione ADR-008 presente, registrazione fatta | Haiku/Sonnet | spec.md, system-prompt.md |

**Estensione:** nuovi smith specializzati (workflow-smith, ecosystem-smith, wiki-smith) entrano qui
quando il volume lo richiede — decisione del conductor + ADR se cambia il mandato.

**Regola di non-conflitto (ADR-003):** i smith NON modificano mai i motori vendored
(`copy-workflow/`, `content-forge2.0/`, `master-build-architecture/`): li invocano. Il QA non forgia mai.
