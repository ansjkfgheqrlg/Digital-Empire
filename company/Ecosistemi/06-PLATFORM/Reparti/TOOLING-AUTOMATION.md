# TOOLING-AUTOMATION — 06-PLATFORM

> Reparto responsabile del codice interno: script, CLI, automazioni, pipeline — il "motore" che fa girare Digital Empire senza intervento manuale.

## Missione
Costruire e mantenere il codice non-product di Digital Empire: script di automazione (outreach, ingestioni, dashboard), CLI interni, tool di sviluppo, e la procedura di code custody (registry repo + handover clienti). Differisce da WEB-ENGINEERING (siti) e PRODUCT-ENGINEERING (SaaS): il suo output è codice operativo interno, non deliverable cliente.

**Regola critica — Outreach:** i file Python/Bat di `Digital Empire/Outreach/` sono workflow ATTIVI ($0/giorno, 6 team Nemotron). TOOLING-AUTOMATION li CENSI e li MONITORA nel registry, ma NON li tocca senza esplicita approvazione plt-director (rischio #4 Piano Maestro).

## Team Agenti
| ID | Agente | Tier | Ruolo |
|---|---|---|---|
| `plt-director` | Direttore PLATFORM | Opus | Approva modifiche a script attivi |
| `plt-cc-master` | Orchestratore Esecutivo | Sonnet | Coordina build tool interni |
| `plt-site-builder` | Builder | Sonnet | Implementazione script/CLI (esteso a tooling) |
| `plt-custodian` | Custodian | Haiku | Registry repo, code custody, handover |
| `plt-sec-sentinel` | Security Sentinel | Sonnet | Security su script (token, credenziali, PII) |
| `plt-qa-runner` | QA Runner | Haiku | Test script con verify + smoke runs |

## Workflow L3
| ID | Workflow | Descrizione |
|---|---|---|
| WF-TOOL-BUILD | Build Tool | script/CLI interni — build-implementation |
| WF-CODE-CUSTODY | Code Custody | repo hygiene, ownership, handover codice ai clienti |

## Funzioni L4
- **T-registry-audit** — censimento completo repo e script con owner e stato
- **T-script-wrap** — wrapping script legacy (non riscrivere — aggiungere layer registry + verify)
- **T-cli-build** — costruzione CLI interni (es. empire-verify, future dashboard CLI)
- **T-handover-prep** — preparazione pacchetto handover cliente (repo, .env doc, runbook, 90gg brief)
- **T-gitignore-enforce** — enforcement .gitignore DE standard + license su ogni repo
- **T-secret-audit** — verifica che nessun secret sia committato nei repo interni

## Asset Esistenti Usati
| Path | Utilizzo |
|---|---|
| `Digital Empire/Outreach/*.py`, `*.bat` | CENSI nel registry — NON modificare senza approvazione |
| `build-implementation` | Skill costruzione implementazioni |
| `github-automation` | Gestione repo, branch, trasferimenti |
| `client-handover` | Checklist handover codice cliente |
| `delivery-playbook` | Template procedura consegna |
| `verify` | Gate qualità su ogni script nuovo |

## Registry PLATFORM (struttura target)
```
registry.json
{
  "repos": [
    {
      "path": "Digital Empire/Outreach/",
      "owner": "ops-scheduler (OPERATIONS)",
      "stato": "produzione-attivo",
      "ultimo_deploy": "2026-06-13",
      "note": "WRAPPA solo — non modificare"
    },
    ...
  ]
}
```

## Gate di Qualità
```
G-SEC (plt-sec-sentinel: no secret/token committati, no PII hardcoded)
  → G-QA (plt-qa-runner: verify verde + smoke run manuale)
    → G-REGISTRY (plt-custodian: aggiunto al registry con owner e stato)
      → G-DEPLOY (solo per tool con deploy — plt-deploy-op)
```

## KPI
| KPI | Target |
|---|---|
| Repo censiti nel registry / repo totali | 100% |
| Script senza owner dichiarato | 0 |
| Handover clienti con pacchetto completo | 100% |
| Secret trovati in repo interni durante audit | 0 |

## Connessioni
- [[06-ECOSISTEMI-CORE]] — dossier padre
- [[SECURITY-QUALITY]] — collabora per secret audit
- [[plt-custodian]] — agente principale del reparto
- [[BACKBONE]] — registro agenti
