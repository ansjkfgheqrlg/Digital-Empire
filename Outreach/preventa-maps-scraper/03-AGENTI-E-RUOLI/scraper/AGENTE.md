# AGENTE: Scraper-1 — Playwright Browser Driver Agent
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Acquisizione Lead
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Scraper-1` è l'agente driver del browser Playwright: apre Google Maps, esegue la ricerca per
città+categoria e restituisce i lead grezzi (nome attività, telefono, sito web, recensioni) senza
alcuna qualifica — quella è responsabilità di `QualifierAgent` a valle.

**Bias comportamentale:** Esecutore meccanico. Non giudica un lead, lo estrae e basta.
**Principio cardine:** *"Un lead non estratto non esiste per il resto della pipeline."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `city: str`, `categoria: str`, `limit: int` + una `Page` Playwright già inizializzata |
| **Output** | Lista di dict lead grezzi (`nome_attivita`, `telefono`, `sito_web`, `numero_recensioni`, `media_recensioni`, ...) |
| **Evento successo** | `leads.extracted` → `{city, leads[], count}` |
| **Evento fallimento** | `run.failed` → `{city, error}` |

---

## 3. Comportamento

1. Pubblica `search.started` con città e categoria.
2. Richiede una `Page` Playwright valida — se assente, solleva `ValueError` esplicito (nessun
   fallback silenzioso: uno scraper senza browser è un bug di orchestrazione, non un caso limite).
3. Delega l'estrazione vera e propria a `browser.scrape_city()` (motore Playwright condiviso in
   `02-AUTOMAZIONI-E-SCRIPTS/browser.py`) — questo agente non contiene selettori CSS/XPath propri.
4. Pubblica `leads.extracted` con i lead grezzi, oppure `run.failed` in caso di eccezione, e la
   rilancia (l'orchestratore decide se ritentare, il singolo agente non nasconde l'errore).

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `page` non inizializzata | `ValueError` immediato, nessuno scraping tentato |
| Eccezione durante `browser.scrape_city` | Pubblica `run.failed` con l'errore, poi rilancia l'eccezione |
| Zero lead trovati | Non è un errore: pubblica `leads.extracted` con `count: 0`, il Gate L2→L3 a valle decide se bloccare |

---

## 5. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Scraper-1 — Playwright Browser Driver Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --city Como --categoria "concessionario auto" --limit 10
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

import browser
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-scraper")


class ScraperAgent:
    """
    Agente APEX-7 responsabile della raccolta lead grezzi da Google Maps via Playwright.
    Documentazione completa → AGENTE.md.
    """

    def __init__(self, page: Any = None, event_bus: Optional[EventBus] = None):
        self.agent_id = "ScraperAgent-1"
        self.page = page
        self.event_bus = event_bus or EventBus()
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def execute_scraping(self, city: str, categoria: str, limit: int) -> List[Dict[str, Any]]:
        log.info(f"🚀 [{self.agent_id}] Avvio scraping per la città: {city} | Categoria: {categoria} | Limit: {limit}")
        self.event_bus.publish("search.started", self.agent_id, {"city": city, "categoria": categoria})

        if not self.page:
            raise ValueError("Errore: Playwright page non inizializzata. Inizializzare l'agente con una pagina valida o usare la CLI.")

        try:
            raw_leads = browser.scrape_city(self.page, city, categoria, limit)
            self.event_bus.publish("leads.extracted", self.agent_id, {
                "city": city,
                "leads": raw_leads,
                "count": len(raw_leads)
            })
            log.info(f"✅ [{self.agent_id}] Scraping completato per {city}. Trovati {len(raw_leads)} lead.")
            return raw_leads
        except Exception as e:
            self.event_bus.publish("run.failed", self.agent_id, {"city": city, "error": str(e)})
            raise e


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run ScraperAgent Standalone CLI")
    parser.add_argument("--city", type=str, default="Como", help="Città da scansionare")
    parser.add_argument("--categoria", type=str, default="concessionario auto", help="Categoria di ricerca")
    parser.add_argument("--limit", type=int, default=2, help="Numero max di risultati")
    parser.add_argument("--output", type=str, default="data/raw_leads_output.json", help="Path output JSON")
    parser.add_argument("--headless", action="store_true", help="Avvia in modalità headless")
    args = parser.parse_args()

    log.info("🔧 Inizializzazione sessione standalone per ScraperAgent...")
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        br = p.chromium.launch(
            headless=args.headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--lang=it-IT,it",
            ]
        )
        context = br.new_context(
            viewport={"width": 1366, "height": 850},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="it-IT"
        )
        page = context.new_page()

        agent = ScraperAgent(page=page)
        results = agent.execute_scraping(args.city, args.categoria, args.limit)

        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        log.info(f"💾 Risultati grezzi salvati in: {output_path}")
        br.close()


if __name__ == "__main__":
    _cli()
```

---

## 6. CLI Standalone

```
python agente.py --city Como --categoria "concessionario auto" --limit 10 [--headless]
```
Lancia una sessione Playwright autonoma (utile per test manuali fuori pipeline) e salva i lead
grezzi in `data/raw_leads_output.json`.

---

## 7. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/browser.py`](../../02-AUTOMAZIONI-E-SCRIPTS/browser.py) — motore Playwright condiviso
- [`../../02-AUTOMAZIONI-E-SCRIPTS/agents.py`](../../02-AUTOMAZIONI-E-SCRIPTS/agents.py) — facade di orchestrazione (Conductor)
- [`../qualificatore/AGENTE.md`](../qualificatore/AGENTE.md) — agente a valle (qualifica dei lead estratti)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_scraper.py`, Phase 3, 2026-07-25).*
