# DIGITAL-EMPIRE / ESTATE-2026 REVENUE WORKSHOP 🏭
> Il piano estate trasformato in **workflow eseguibile**: reparti, agenti, skill, memoria, gates.
> Costruito il 21/07/2026 da CHIEF-FORGE. Plan of record: `01-PLANNING/PLANNING-P7-MASTER-PLAN.md`.

## Leggimi in 60 secondi
1. **Se sei Max** → apri `01-PLANNING/PLANNING-P7-MASTER-PLAN.md` §1: tre decisioni da 30 secondi (prezzo Manuale OGGI h20:00). Poi §2 corsia 🔵.
2. **Se sei Gael** → P7 §2 corsia 🟣, in ordine. Ogni task chiuso → checkpoint.
3. **Se sei Claude** → P7 §2 corsia 🤖. Batch copy 21/07 sera (script S1 già pronto in `03-WORKFLOWS/WF-S1-CONCESSIONARI.md`).

## Mappa
| Path | Cosa contiene |
|---|---|
| `00-MEMORY/` | 🧠 Ecosistema memoria: checkpoint, decisioni (con veto), piani, brainstorm, errori, metriche, ReasoningBank + `memory_manager.py` (CLI) |
| `01-PLANNING/` | Planning-by-planning P1→P7 (P7 = master plan finale, sostituisce il dossier 19/07) |
| `02-ARCHITECTURE/` | Architettura a livelli L0-L5 + ADR + runbook |
| `03-WORKFLOWS/` | `workflows.yaml` (orchestrazione macchina) + WF-MASTER + WF-S1..S6 |
| `04-AGENTS/` | Registry reparti + pack 7-file: chief-forge, memory-architect + YT-AGENT-PACK |
| `05-SKILLS/` | content-forge2.0, master-build-architecture, ruflo (clonati) |
| `06-NERVOUS-SYSTEM/` | Integrazione Ruflo: hooks, topologia swarm.estate.yaml |
| `07-CONTROL/` | Dashboard giornaliera + gates + protocollo RETRO |

## Comandi memoria (uso quotidiano)
```bash
cd DIGITAL-EMPIRE
python3 00-MEMORY/memory_manager.py status                    # salute memoria
python3 00-MEMORY/memory_manager.py checkpoint --task WF-S1 --note "lead 3-4-5 contattati"
python3 00-MEMORY/memory_manager.py metric --name s1_lead_contattati --value 5
python3 00-MEMORY/memory_manager.py search "Preventa"
```

## Le regole che non si negoziano
Revenue-first · DEC-001 chiusa OGGI (anche per default) · wrap mai rewrite · chiavi solo `.env` · 1 swarm pesante alla volta · task chiuso → checkpoint · solo date assolute · vendibile > perfetto · mentalita.brutale SOLO se 100% auto.

⛓️ Trace: `ARCH-ESTATE-2026#estate-2026` · memoria bootstrap: CP-001/002 · DEC-EST-001..004
