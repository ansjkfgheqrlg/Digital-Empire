> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# L2 TOOLING & AUTOMATION — Codice Interno

> Reparto L2 · Ecosistema: 06-PLATFORM
> Riferimento: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md` · `company/Ecosistemi/06-PLATFORM/BACKBONE.md`

---

## Missione

Costruire e custodire tutti gli script, CLI e automazioni **ad uso interno** di Digital Empire: pipeline Outreach, dashboard operative, tool di scaffolding, script di build/manutenzione. TOOLING & AUTOMATION scrive il codice che gli altri ecosistemi (OPERATIONS in particolare) usano per girare — non produce siti per i clienti (quello è WEB-ENGINEERING).

**Regola critica:** il codice Outreach attivo (`run_parallel.py`, `run_ig_email.py`, `AVVIA-*.bat`) NON viene modificato — viene **wrappato** con registry, verify e monitoring (rischio #4 Piano Maestro: workflow attivi a €0/giorno non si toccano).

---

## Workflow L3

| Workflow | Descrizione | Gate |
|---|---|---|
| **WF-TOOL-BUILD** | Richiesta tool/CLI → spec → build-implementation → verify → consegna | verify verde |
| **WF-CODE-CUSTODY** | Registry repo, ownership, handover codice ai clienti (€0 canoni = codice loro) | checklist code-custody completata |

---

## Funzioni L4

| ID Funzione | Descrizione |
|---|---|
| T-tool-spec | Specifica funzionale del tool (input, output, dipendenze) |
| T-tool-build | Implementazione (build-implementation) |
| T-tool-verify | Verifica con verify + test unitari |
| T-registry-update | Aggiornamento registro PLATFORM: path, owner, stato, tier |
| T-custody-handover | Procedura handover codice cliente: repo transfer, env, docs, 90gg supporto |
| T-outreach-wrap | Wrapping script Outreach: registry entry + verify gate + monitoring hook |

---

## Agenti L5 del reparto

| ID Agente | Ruolo | Tier |
|---|---|---|
| `plt-director` | Direttore PLATFORM — approva tool critici | Opus |
| `plt-cc-master` | Orchestratore WF-TOOL-BUILD | Sonnet |
| `plt-custodian` | Custode registry e handover clienti | Haiku |
| `plt-sec-sentinel` | Security review su ogni script (aidefence, has_pii) | Sonnet |
| `plt-qa-runner` | Verify + test tool consegnati | Haiku |

---

## Registry PLATFORM

Ogni script/CLI attivo in Digital Empire deve avere una entry nel registro con:

```yaml
path: "Outreach/run_parallel.py"
owner: "plt-custodian"
stato: "active | deprecated | orphan"
tier: "python-script"
ultima_verifica: "YYYY-MM-DD"
note: "wrappato, non modificare"
```

**DONE WHEN (P1):** 100% repo/script censiti nel registry.

---

## Asset esistenti

| Path | Stato |
|---|---|
| `Digital Empire/Outreach/*.py`, `*.bat` | WRAPPA — registry + verify, NON modificare |
| skill `build-implementation` | USA — standard per nuovi tool |
| skill `review-and-heal` | USA — review codice interno |
| skill `github-automation` | USA — automazione repo |

---

## Nuove skill da creare (via FORGE)

| Skill | Scopo | Priorità |
|---|---|---|
| `code-custody` | Checklist handover codice cliente (repo transfer, env, docs, 90gg) | ALTA |
| `empire-verify` | verify.sh versione DE: lint+build+playwright+brand gate | ALTA |

---

## KPI

| KPI | Target |
|---|---|
| Repo/script censiti nel registry | 100% |
| Tool consegnati con verify verde al primo giro | ≥ 90% |
| Script Outreach wrappati (non modificati) | 100% |

## Connessioni

- [[06-PLATFORM/ECOSISTEMA.md]] — panoramica PLATFORM
- [[06-PLATFORM/BACKBONE.md]] — namespace AgentDB `platform/deploy`
- [[06-PLATFORM/Reparti/Security-Quality.md]] — aidefence su ogni script
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo, sez. asset §5
