# AGENTE: Qualifier-1 — Lead Qualifier Agent (Site Analyst)
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Acquisizione Lead
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Qualifier-1` trasforma lead grezzi (usciti da `Scraper-1`) in lead **qualificati e prioritizzati**
(ALTA/MEDIA/BASSA), analizzando presenza/qualità del sito web e segnali di reputazione, in
parallelo per performance (`checker.qualify_leads_parallel`, ThreadPoolExecutor).

Da questa versione (v2.0) integra anche il **Data-Validator-Gate**: se collegato a un `GateAgent`,
ogni lead qualificato passa da `gate_agent.validate_lead()` prima di proseguire — scarta i lead
senza alcun canale di contatto (telefono E sito assenti) o con reputazione negativa consolidata.

**Bias comportamentale:** Analista scettico. Qualifica solo ciò che è verificabile dai dati, non
inferisce intenzioni.
**Principio cardine:** *"Una priorità ALTA non richiesta è peggio di zero lead."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `leads: List[Dict]` (lead grezzi da Scraper-1), `city: str` |
| **Output** | Lista di lead qualificati con `priorita_lead` (ALTA/MEDIA/BASSA) + eventuali campi di note |
| **Evento pubblicato** | `leads.qualified` → `{city, leads[], count}` |
| **Dipendenza opzionale** | `gate_agent: GateAgent` — se assente, nessun filtro Data-Validator applicato (comportamento legacy) |

---

## 3. Comportamento

1. Delega la qualifica parallela a `checker.qualify_leads_parallel()` (motore condiviso in
   `02-AUTOMAZIONI-E-SCRIPTS/checker.py`) — questo agente non contiene logica di scoring propria.
2. Se `gate_agent` è configurato, applica `validate_lead()` a ogni lead qualificato: i lead che
   falliscono (nessun canale di contatto, o reputazione <4.0/5 su ≥5 recensioni) vengono scartati
   e il conteggio degli scarti viene loggato.
3. Pubblica `leads.qualified` con la lista finale (post-gate se applicabile).

**Nota di progettazione:** il filtro Data-Validator-Gate è opzionale via constructor param, non
obbligatorio — questo permette a chiamanti legacy (test, script standalone) di istanziare
`QualifierAgent()` senza gate e mantenere il comportamento pre-v2.0 invariato.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `gate_agent` passato non implementa `validate_lead` | `AttributeError` catturato per-lead, il lead viene mantenuto (fail-open, non fail-closed: un gate rotto non deve bloccare l'intera pipeline) |
| Zero lead in input | `checker.qualify_leads_parallel([])` ritorna lista vuota, evento pubblicato con `count: 0` |
| Tutti i lead scartati dal gate | Evento `leads.qualified` con lista vuota — il Gate L3→L4 a valle decide se bloccare il workflow |

---

## 5. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Qualifier-1 — Lead Qualifier Agent (Site Analyst)
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --input data/raw_leads.json --city Como
"""
from __future__ import annotations

import os
import sys
import json
import logging
import argparse
from pathlib import Path
from typing import Any, List, Dict, Optional

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import checker
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-qualificatore")


class QualifierAgent:
    """
    Agente APEX-7 responsabile della qualifica parallela dei lead grezzi (priorità ALTA/MEDIA/BASSA)
    e, se collegato a un GateAgent, del filtro Data-Validator-Gate prima che il lead entri nella
    pipeline di contatto. Documentazione completa → AGENTE.md.
    """

    def __init__(self, event_bus: Optional[EventBus] = None, gate_agent: Optional[Any] = None):
        self.agent_id = "QualifierAgent-1"
        self.event_bus = event_bus or EventBus()
        self.gate_agent = gate_agent
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def qualify_leads(self, leads: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"🔍 [{self.agent_id}] Avvio qualifica in parallelo di {len(leads)} lead per la città: {city}")
        qualified = checker.qualify_leads_parallel(leads)

        # Data-Validator-Gate: se un GateAgent è configurato, filtra i lead qualificati
        if self.gate_agent:
            validated = []
            for lead in qualified:
                try:
                    val_res = self.gate_agent.validate_lead(lead)
                    if val_res.get("passed", True):
                        validated.append(lead)
                except AttributeError:
                    # Fallback se il gate_agent passato non implementa validate_lead
                    validated.append(lead)

            rejected_count = len(qualified) - len(validated)
            if rejected_count:
                log.info(f"🚫 [{self.agent_id}] Gate Agent ha scartato {rejected_count}/{len(qualified)} lead per {city} in base ai criteri di qualità.")
            qualified = validated

        self.event_bus.publish("leads.qualified", self.agent_id, {
            "city": city,
            "leads": qualified,
            "count": len(qualified)
        })
        log.info(f"✅ [{self.agent_id}] Qualifica completata per {city}.")
        return qualified


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run QualifierAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file JSON dei lead grezzi")
    parser.add_argument("--output", type=str, default="data/qualified_leads_output.json", help="Path output JSON")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        raw_leads = json.load(f)

    log.info(f"🔍 Caricati {len(raw_leads)} lead grezzi da qualificare...")
    agent = QualifierAgent()
    results = agent.qualify_leads(raw_leads, args.city)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    log.info(f"💾 Risultati qualificati salvati in: {output_path}")


if __name__ == "__main__":
    _cli()
```

---

## 6. CLI Standalone

```
python agente.py --input data/raw_leads.json --city Como [--output data/qualified.json]
```

---

## 7. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/checker.py`](../../02-AUTOMAZIONI-E-SCRIPTS/checker.py) — motore di qualifica parallela
- [`../gate/AGENTE.md`](../gate/AGENTE.md) — Data-Validator-Gate (`validate_lead`)
- [`../scraper/AGENTE.md`](../scraper/AGENTE.md) — agente a monte (fornisce i lead grezzi)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_qualificatore.py`, Phase 3, 2026-07-25), che già
includeva il wiring del Data-Validator-Gate.*
