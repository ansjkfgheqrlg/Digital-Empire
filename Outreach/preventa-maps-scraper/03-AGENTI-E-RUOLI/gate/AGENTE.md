# AGENTE: Gate-1 — Quality Gate Agent (Deterministic Pipeline Checkpoints)
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Controllo Qualità
> **File Python:** [`agente.py`](./agente.py) (estende [`../../02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py`](../../02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py))

---

## 1. Identità e Missione

`Gate-1` è il valutatore deterministico e pessimista di ogni transizione di fase della pipeline
(L1→L2 ... L6→L7): non genera testo, non usa LLM, applica controlli espliciti e loggabili. È anche
il **Data-Validator-Gate** per singolo lead (v2.0): scarta lead senza canale di contatto o con
reputazione negativa consolidata, prima che entrino nella fase di outreach.

**⚠️ Nota architetturale:** la logica di valutazione (`evaluate_output`, `validate_lead`) **non
vive qui** ma in `02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py`, condivisa da `orchestrator.py` e
`run.py`. Questo `agente.py` estende quella classe aggiungendo solo il caricamento di `AGENTE.md`
e i default comodi per uso standalone — per non triplicare ~200 righe della stessa logica in tre
punti diversi del repo (violerebbe il principio DRY dichiarato in `agents.py`).

**Bias comportamentale:** Pessimista per default — un output ambiguo è FAIL, non PASS.
**Principio cardine:** *"Un gate che passa sempre non è un gate, è un timbro."*

---

## 2. Ingresso / Uscita

| Metodo | Input | Output |
|---|---|---|
| `evaluate_output(gate_id, output_str)` | ID gate (`L1_L2`...`L6_L7`) + stringa da valutare | Report con `passed`, `score`, `threshold`, `criteria_results[]` |
| `validate_lead(lead: Dict)` | Singolo lead qualificato | `{lead, passed, reasons[]}` |

**Eventi pubblicati:** `gate.check.requested`, `lead.validated` / `lead.rejected` (con scrittura in
`decision_log` per i rigetti, `importance: 0.4`).

---

## 3. I 6 Gate della Pipeline

| Gate | Transizione | Criterio di verifica (deterministico) |
|---|---|---|
| L1→L2 | Input parametri | contiene "città" o "categoria" |
| L2→L3 | Estrazione (Scraper) | almeno 1 riga di output non vuota |
| L3→L4 | Qualifica priorità | contiene ALTA/MEDIA/BASSA |
| L4→L5 | Copywriting | output > 5 caratteri |
| L5→L6 | Salvataggio CSV | contiene "salvato" o output > 5 caratteri |
| L6→L7 | Fine E2E | contiene "completato" o output > 5 caratteri |

Dopo 3 fallimenti consecutivi sullo stesso gate → transizione a `ESCALATING` (vedi `Conductor.on_gate_failed` in `agents.py`).

---

## 4. Data-Validator-Gate (`validate_lead`)

Criteri di scarto di un lead qualificato, prima che raggiunga Writer/Sender:
- **Nessun canale di contatto:** telefono E sito web entrambi assenti.
- **Reputazione insufficiente:** `media_recensioni < 4.0` su almeno 5 recensioni (soglia scelta
  per non penalizzare i lead "senza sito" — l'obiettivo primario a priorità ALTA).

Ogni rigetto viene scritto in `decision_log` (memoria persistente) con il motivo esplicito, per
permettere audit successivi su quanti lead vengono scartati e perché.

---

## 5. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `gate_id` non riconosciuto | Ritorna `{"error": "Invalid gate_id ..."}`, nessuna eccezione |
| 3° fallimento consecutivo sullo stesso gate | Stato `ESCALATING`, l'orchestratore interrompe il workflow per quella città |
| Lead senza `numero_recensioni`/`media_recensioni` parsabili | Trattati come `0` (nessuna eccezione, nessun falso PASS) |

---

## 6. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Gate-1 — Quality Gate Agent (Deterministic Pipeline Checkpoints)
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

NON duplicare logica qui: l'implementazione dei controlli (evaluate_output, validate_lead) vive
in ../../02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py, condivisa anche da orchestrator.py e run.py.
Questo modulo si limita ad aggiungere il caricamento delle regole da AGENTE.md e la CLI
standalone, per rispettare il pattern cartella-per-agente senza triplicare ~200 righe di logica.

CLI:
    python agente.py --gate-id L1_L2 --content "città: Como, categoria: concessionario auto"
"""
from __future__ import annotations

import os
import sys
import logging
import argparse
from pathlib import Path
from typing import Any, Dict, Optional

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from event_bus import EventBus
from memory import MemoryQueryInterface
from gate_agent import GateAgent as _CoreGateAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-gate")


class GateAgent(_CoreGateAgent):
    """
    Estensione "operativa" del GateAgent canonico (02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py):
    stessa logica di valutazione (evaluate_output, validate_lead), più il caricamento delle
    regole comportamentali da AGENTE.md e costruttore con default comodi per uso standalone/CLI.
    Documentazione completa → AGENTE.md.
    """

    def __init__(self, memory: Optional[MemoryQueryInterface] = None, event_bus: Optional[EventBus] = None):
        memory = memory or MemoryQueryInterface(memory_filepath="data/memory_db.json")
        event_bus = event_bus or EventBus()
        super().__init__(memory, event_bus)
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run GateAgent Standalone CLI")
    parser.add_argument("--gate-id", type=str, required=True,
                         choices=["L1_L2", "L2_L3", "L3_L4", "L4_L5", "L5_L6", "L6_L7"],
                         help="ID del gate da valutare")
    parser.add_argument("--content", type=str, required=True, help="Contenuto dell'output da valutare")
    args = parser.parse_args()

    agent = GateAgent()
    report = agent.evaluate_output(args.gate_id, args.content)

    print("\n--- REPORT DI QUALITA' GATE ---")
    print(f"Gate ID: {report['gate_id']}")
    print(f"Passed: {'SI' if report['passed'] else 'NO'}")
    print(f"Score: {report['score']} (Soglia: {report['threshold']})")
    print("Dettaglio Criteri:")
    for c in report["criteria_results"]:
        print(f"  [{c['status']}] {c['criterion_id']}: {c['description']} | Note: {c.get('note')}")
    print("--------------------------------")


if __name__ == "__main__":
    _cli()
```

---

## 7. CLI Standalone

```
python agente.py --gate-id L1_L2 --content "città: Como, categoria: concessionario auto"
```

---

## 8. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py`](../../02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py) — implementazione canonica condivisa
- [`../../02-AUTOMAZIONI-E-SCRIPTS/quality_gate.py`](../../02-AUTOMAZIONI-E-SCRIPTS/quality_gate.py) — motore/definizioni dei gate (`GATE_DEFINITIONS`)
- [`../qualificatore/AGENTE.md`](../qualificatore/AGENTE.md) — consumatore diretto di `validate_lead`

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27). A differenza degli altri
agenti ricostruiti, qui la logica NON è stata riportata verbatim dal file flat cancellato
(`agente_gate.py`, che la duplicava già rispetto a `gate_agent.py`): questa versione delega
all'implementazione canonica per eliminare la duplicazione, non per reintrodurla.*
