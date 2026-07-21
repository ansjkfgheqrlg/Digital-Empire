# 05-SKILLS — Registry (clonate il 21/07/2026)

| Skill | Repo | Uso nel workshop | Invocazione |
|---|---|---|---|
| **content-forge2.0** | github.com/ansjkfgheqrlg/content-forge2.0 | Motore Content Dept: materiale grezzo → MKD → artefatti (agenti, workflow, wiki). Usato da WF-S5 (script video), WF-S6 (kit), espansione agenti | `/forge <path> --target=<agent|team|skill|workflow|orchestration|wiki>` |
| **master-build-architecture** | github.com/ansjkfgheqrlg/master-build-architecture | Metodo architettura: 10 fasi, memory-first dal passo 0, formato 7-file/agente. Usato per ARCHITETTURA-ESTATE.md e per future architetture figlie | `/master-architect <vision> --target=<plan|swarm|skill|full-ecosystem>` |
| **ruflo** | github.com/ruvnet/ruflo | Sistema nervoso L1: swarm gerarchici, hooks, memoria AgentDB, control-plane. Config: `06-NERVOUS-SYSTEM/` | `npx ruflo init` (fallback: orchestrazione file-based) |

## Note operative
- Script utili già presenti: `content-forge2.0/scripts/` (atomizer, coverage_check, validate_dag, log_failure) — usare per gate zero-stub/coverage.
- Pattern memoria wrappato da `master-build-architecture/scripts/memory_manager.py` → esteso in `00-MEMORY/memory_manager.py` (ADR-EST-002: wrap, non rewrite).
- Package pesanti (zip .skill ~49MB) rimossi per tenere il workspace leggero: reinstallabili con `npx skills add` o re-clone.

## Motori esistenti dell'ecosistema (referenziati, si wrappano — ADR-EST-002)
carousel-factory (brand mentalita-brutale) · site-* (empire-premium-style) · case-study-forge · A1-scrape · A2-outreach runtime · beast-preventivi/pricing · cro-copy-architect (APSOC) · script A5/A8 (WF-CLOSING-PREP) · PreventivoForge + `/nuovo-concessionario` + kill-switch.
