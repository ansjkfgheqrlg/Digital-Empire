# AGENTE: Areus-1 — Areus (Aureus Agency OS) CRM Integration Agent
> **Versione:** 3.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Salvataggio & Sincronizzazione
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Areus-1` sincronizza i lead finali (post-qualifica) sul CRM interno **Areus** (Aureus Agency OS,
`EmpireDesk/platform/`) — la piattaforma unica dell'azienda dove vivono tutti i lead, freddi,
contattati, risposti/non risposti. Sostituisce la vecchia integrazione Google Sheets (v2.0):
niente più service account, niente credenziali esterne da configurare — scrive direttamente nel
file JSON condiviso `EmpireDesk/state/preventa_leads.json`, che `EmpireDesk/modules/preventa.py`
serve alla UI. Deduplica delegata al modulo condiviso `areus.py` — questo agente si limita a
orchestrare la chiamata.

**Bias comportamentale:** Best-effort, mai bloccante. Se il path Areus non è scrivibile, la
pipeline prosegue lo stesso (il CSV locale resta la fonte di verità di backup).
**Principio cardine:** *"Areus è la piattaforma unica dell'azienda: i lead vivono lì, non su un
foglio esterno."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `leads: List[Dict]` (lead finali), `city: str` |
| **Config** | `state_path` (default auto-calcolato: `EmpireDesk/state/preventa_leads.json`), `push_only_alta` |
| **Evento successo** | `areus.synced` → `{city, success: true, aggiunti, duplicati, path}` |
| **Evento fallimento** | `run.failed` → `{city, error}` |

---

## 3. Comportamento

1. Delega a `areus.upload_to_areus()`: dedup per telefono normalizzato, ogni lead nuovo entra con
   `stage="NEW"` (stesso enum `LeadStage` di `EmpireDesk/platform/types.ts`), filtro `only_alta`
   se richiesto.
2. Pubblica `areus.synced` con il conteggio di quanti lead sono stati aggiunti/scartati come
   duplicati.
3. In caso di eccezione (path non scrivibile, JSON corrotto): pubblica `run.failed` con l'errore
   e lo rilancia — il fallimento È bloccante, perché senza Areus i lead non sono tracciabili da
   nessuna parte per il team commerciale.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `EmpireDesk/state/` non esiste | Creata automaticamente (`mkdir -p`) |
| JSON state corrotto/illeggibile | Log warning, riparte da lista vuota senza perdere il file corrotto (non sovrascrive finché non ci sono nuovi lead) |
| Path non scrivibile (permessi) | Eccezione propagata dopo `run.failed` |

---

## 5. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Areus-1 — Areus (Aureus Agency OS) CRM Integration Agent
Owner: GAEL · Controllore: A2-QA · Versione: 3.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --input data/leads.csv [--state-path X] [--only-alta]
"""
from __future__ import annotations

import sys
import csv
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

import areus
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-integratore-areus")


class AreusAgent:
    """
    Agente APEX-7 responsabile della sincronizzazione dei lead finali sul CRM Areus
    (dedup e scrittura delegate al modulo condiviso `areus.py`). Nessuna credenziale
    esterna richiesta: scrive su un file JSON locale letto da EmpireDesk/modules/preventa.py.
    Documentazione completa → AGENTE.md.
    """

    def __init__(self, event_bus: Optional[EventBus] = None, state_path: str = "",
                 push_only_alta: bool = False):
        self.agent_id = "AreusAgent-1"
        self.event_bus = event_bus or EventBus()
        self.state_path = state_path or None
        self.push_only_alta = push_only_alta
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def upload(self, leads: List[Dict[str, Any]], city: str):
        log.info(f"📤 [{self.agent_id}] Inizio sincronizzazione su Areus per la città: {city}")
        try:
            result = areus.upload_to_areus(
                leads=leads,
                city=city,
                state_path=self.state_path,
                push_only_alta=self.push_only_alta,
            )
            self.event_bus.publish("areus.synced", self.agent_id, {"city": city, "success": True, **result})
            log.info(f"✅ [{self.agent_id}] Sync Areus completata per {city}: {result['aggiunti']} nuovi, {result['duplicati']} duplicati.")
        except Exception as e:
            self.event_bus.publish("run.failed", self.agent_id, {"city": city, "error": str(e)})
            raise e


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run AreusAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file CSV dei lead qualificati")
    parser.add_argument("--state-path", type=str, default="", help="Override path del JSON condiviso con EmpireDesk")
    parser.add_argument("--only-alta", action="store_true", help="Carica solo lead a priorità ALTA")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    leads = []
    with open(input_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)

    log.info(f"📤 Caricati {len(leads)} lead da CSV per sync su Areus...")
    agent = AreusAgent(state_path=args.state_path, push_only_alta=args.only_alta)
    agent.upload(leads, args.city)


if __name__ == "__main__":
    _cli()
```

---

## 6. CLI Standalone

```
python agente.py --input data/leads_finali.csv [--state-path /path/preventa_leads.json] [--only-alta]
```

---

## 7. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/areus.py`](../../02-AUTOMAZIONI-E-SCRIPTS/areus.py) — motore di scrittura condiviso (deduplica)
- [`../../../../EmpireDesk/modules/preventa.py`](../../../../EmpireDesk/modules/preventa.py) — modulo EmpireDesk che legge lo stesso file e lo serve alla UI Areus
- [`../gate/AGENTE.md`](../gate/AGENTE.md) — valuta il Gate L5→L6 prima di questo step

---

*Migrato da Google Sheets ad Areus (v3.0, 2026-07-28) su decisione di Max: "abbiamo tutto dentro
Areus, non serve un foglio esterno". Agente ricostruito in formato cartella-per-agente (Phase B,
2026-07-27) — logica invariata rispetto all'implementazione flat originale
(`agente_integratore_sheets.py`, Phase 3, 2026-07-25).*
