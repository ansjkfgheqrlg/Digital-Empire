# AGENTE: Orchestratore-1 — Pipeline Orchestration Agent
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Orchestrazione
> **File Python:** [`agente.py`](./agente.py) (alias di `Conductor` in [`../../02-AUTOMAZIONI-E-SCRIPTS/agents.py`](../../02-AUTOMAZIONI-E-SCRIPTS/agents.py))
> **CLI ufficiale:** [`../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py`](../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py)

---

## 1. Identità e Missione

`Orchestratore-1` coordina l'intera pipeline event-driven: Scraper → Qualifier → (Writer → Sender
opzionali) → Sheets, con Gate-1 a ogni transizione e MetaOptimizer a fine E2E. La sua
implementazione reale è la classe `Conductor` in `agents.py` — questo agente esiste come voce
canonica nella cartella-per-agente (per coerenza documentale e per i criteri C1-C6 di "agente
operativo"), ma **non introduce un secondo motore di orchestrazione**.

**⚠️ Nota architetturale — perché non c'è un secondo script CLI qui:** la Phase A (25/07) aveva
cancellato un `agente_orchestratore.py` da 252 righe che duplicava quasi integralmente
`orchestrator.py` (stessa inizializzazione di `EventBus`/`MemoryQueryInterface`/`GateAgent`/
`MetaOptimizer`, stesso ciclo Playwright, stessi argomenti CLI). Ricrearlo identico avrebbe
reintrodotto lo stesso rischio di doppia manutenzione che il pattern "canonico" dovrebbe eliminare.
Questo modulo espone quindi solo un alias (`OrchestratorAgent = Conductor`) e rimanda all'unico
entry point CLI reale.

**Bias comportamentale:** Coordinatore, non esecutore. Non contiene logica di dominio (scraping,
copywriting, invio) — solo sequenza, gate e gestione errori.
**Principio cardine:** *"Un solo posto dove la pipeline è definita, non due che devono restare sincronizzati a mano."*

---

## 2. Flusso Orchestrato (event-driven)

```
run_city_workflow(city, categoria, limit)
  → Gate L1→L2 (parametri)
  → ScraperAgent.execute_scraping           → evento leads.extracted
  → Gate L2→L3 (estrazione)
  → QualifierAgent.qualify_leads            → evento leads.qualified
  → Gate L3→L4 (priorità)
  → [se writer+sender configurati] WriterAgent.generate_messages → evento messages.generated
       → Gate L4→L5 (copy) → SenderAgent.send_outreach → evento messages.sent
    [altrimenti] salva direttamente i lead qualificati
  → _finalize_and_save: run.save_csv(...)   → Gate L5→L6 (salvataggio)
  → [se configurato] SheetsAgent.upload     → evento sheets.synced
  → Gate L6→L7 (fine E2E) → evento run.completed
       → MetaOptimizer.run_optimization_loop() (se configurato)
```

Su fallimento di un gate: `on_gate_failed` tenta un remediation loop (retry scraping / rotazione
strategia copywriting) fino a 3 tentativi, poi `ESCALATING`.

---

## 3. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `city, categoria, limit` per ogni città della campagna |
| **Dipendenze** | `scraper_agent`, `qualifier_agent`, `sheets_agent` (opz.), `qa_agent`, `output_csv_path`, `writer_agent`/`sender_agent` (opz.), `meta_optimizer` (opz.) |
| **Evento finale** | `run.completed` → `{city}` |

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| Gate fallito <3 volte | Remediation loop (retry mirato per il gate specifico) |
| Gate fallito ≥3 volte | `ESCALATING`, workflow per quella città interrotto |
| `writer_agent`/`sender_agent` assenti | Salta la fase di outreach, salva direttamente i lead qualificati (modalità solo-scraping+CSV+Sheets) |

---

## 5. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Orchestratore-1 — Pipeline Orchestration Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

NON duplicare logica qui: l'orchestrazione event-driven (Scraper → Qualifier → Writer → Sender →
Sheets → Gate E2E) vive nella classe Conductor di ../../02-AUTOMAZIONI-E-SCRIPTS/agents.py, e il
suo entry point CLI è ../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py. Questo modulo re-esporta
Conductor sotto il nome canonico OrchestratorAgent per coerenza col pattern cartella-per-agente,
senza ricreare un secondo script CLI ~250 righe quasi identico a orchestrator.py (era il difetto
del vecchio agente_orchestratore.py, wipeato in Phase A).

CLI:
    Usa direttamente ../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py (entry point ufficiale).
"""
from __future__ import annotations

import sys
from pathlib import Path

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from agents import Conductor as OrchestratorAgent  # noqa: E402,F401 — alias canonico per questo agente


def _load_rules() -> str:
    md = _AGENT_DIR / "AGENTE.md"
    return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"


if __name__ == "__main__":
    print(
        "Orchestratore-1 non ha una CLI propria: usa "
        "'python ../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py --city <città> ...' "
        "(entry point ufficiale della pipeline completa)."
    )
```

---

## 6. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/agents.py`](../../02-AUTOMAZIONI-E-SCRIPTS/agents.py) — implementazione reale (`Conductor`, `QAAgent`, `DebugAgent`)
- [`../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py`](../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py) — CLI ufficiale multi-città/multi-istanza Playwright
- [`../gate/AGENTE.md`](../gate/AGENTE.md) — i 6 gate applicati a ogni transizione

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27). A differenza degli altri
agenti ricostruiti, qui la logica NON è stata riportata dal file flat cancellato
(`agente_orchestratore.py`, che duplicava `orchestrator.py`): questa versione elimina la
duplicazione invece di reintrodurla.*
