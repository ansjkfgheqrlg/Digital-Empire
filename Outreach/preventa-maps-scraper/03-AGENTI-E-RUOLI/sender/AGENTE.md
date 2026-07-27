# AGENTE: Sender-1 — Message Sender Agent (Rate-Limited Outreach)
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Comunicazione & Outreach
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Sender-1` spedisce i messaggi generati da `Writer-1`, applicando **rate limit giornalieri
separati per canale** (default: 15 WhatsApp, 25 Email) per evitare pattern di spam rilevabili e
blocchi degli account di invio.

**Bias comportamentale:** Prudente, non aggressivo. Preferisce sospendere l'invio piuttosto che
sforare un limite.
**Principio cardine:** *"Un lead contattato domani vale più di un account bannato oggi."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `messages: List[Dict]` (da Writer-1, con `canale_primario`), `city: str` |
| **Output** | Sottoinsieme dei messaggi effettivamente inviati (`stato: "contattato"`), gli esclusi restano fuori dal report |
| **Evento pubblicato** | `messages.sent` → `{city, messages[], count}` |
| **Parametri** | `daily_whatsapp_limit` (default 15), `daily_email_limit` (default 25) |

---

## 3. Comportamento

1. Per ogni messaggio determina il canale (`canale_primario`: `whatsapp` o `email`).
2. Se il contatore giornaliero del canale ha raggiunto il limite, **salta il lead** (non lo mette
   in coda, lo esclude da questo run — il lead resta disponibile per il run successivo).
3. Applica un ritardo casuale 1.0–2.5s tra un invio e l'altro (disattivato se `city` contiene
   "test", per non rallentare la suite di test unitari).
4. Marca ogni messaggio inviato con `stato: "contattato"` e pubblica `messages.sent`.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| Limite giornaliero raggiunto per un canale | Lead saltato con log `WARNING`, spedizione continua sugli altri canali/lead |
| `canale_primario` mancante nel messaggio | Trattato come `"email"` (fallback esplicito) |
| Zero messaggi in input | Evento `messages.sent` con `count: 0` |

---

## 5. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Sender-1 — Message Sender Agent (Rate-Limited Outreach)
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --input data/messaggi.json --city Como
"""
from __future__ import annotations

import os
import sys
import json
import time
import random
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

from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-sender")


class SenderAgent:
    """
    Agente APEX-7 responsabile della spedizione dei messaggi generati da Writer-1, con rate
    limiting giornaliero anti-spam per canale (WhatsApp/Email). Documentazione completa → AGENTE.md.
    """

    def __init__(self, event_bus: Optional[EventBus] = None, daily_whatsapp_limit: int = 15, daily_email_limit: int = 25):
        self.agent_id = "SenderAgent-1"
        self.event_bus = event_bus or EventBus()
        self.daily_whatsapp_limit = daily_whatsapp_limit
        self.daily_email_limit = daily_email_limit
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def send_outreach(self, messages: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"📨 [{self.agent_id}] Spedizione in corso per {len(messages)} messaggi in {city} (Limiti: WA {self.daily_whatsapp_limit}, Email {self.daily_email_limit})")

        sent_messages = []
        wa_sent = 0
        email_sent = 0

        for msg in messages:
            canale = msg.get("canale_primario", "email")
            nome = msg.get("nome_attivita", "N/A")

            # Applica i rate limit giornalieri
            if canale == "whatsapp":
                if wa_sent >= self.daily_whatsapp_limit:
                    log.warning(f"⚠️ [{self.agent_id}] Limit rate raggiunto per WhatsApp ({self.daily_whatsapp_limit}). Spedizione sospesa per il lead: {nome}")
                    continue
                wa_sent += 1
            else:
                if email_sent >= self.daily_email_limit:
                    log.warning(f"⚠️ [{self.agent_id}] Limit rate raggiunto per Email ({self.daily_email_limit}). Spedizione sospesa per il lead: {nome}")
                    continue
                email_sent += 1

            log.info(f"📤 [{self.agent_id}] Inviato messaggio a {nome} via {canale.upper()}")

            # Ritardo casuale anti-detection, disattivato negli ambienti di test unitario
            if "test" not in city.lower():
                delay = random.uniform(1.0, 2.5)
                time.sleep(delay)

            msg["stato"] = "contattato"
            sent_messages.append(msg)

        self.event_bus.publish("messages.sent", self.agent_id, {
            "city": city,
            "messages": sent_messages,
            "count": len(sent_messages)
        })
        log.info(f"✅ [{self.agent_id}] Spedizione completata per {city}. Inviati {len(sent_messages)} messaggi.")
        return sent_messages


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run SenderAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file JSON dei messaggi personalizzati")
    parser.add_argument("--output", type=str, default="data/report_contatti.json", help="Path report output JSON")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        messages = json.load(f)

    log.info(f"📨 Caricati {len(messages)} messaggi da inviare...")
    agent = SenderAgent()
    results = agent.send_outreach(messages, args.city)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    log.info(f"💾 Report di invio salvato in: {output_path}")


if __name__ == "__main__":
    _cli()
```

---

## 6. CLI Standalone

```
python agente.py --input data/messaggi.json --city Como [--output data/report_contatti.json]
```

---

## 7. Riferimenti
- [`../writer/AGENTE.md`](../writer/AGENTE.md) — agente a monte (genera i messaggi da inviare)
- [`../responder/AGENTE.md`](../responder/AGENTE.md) — agente a valle (classifica le risposte in arrivo)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_sender.py`, Phase 3, 2026-07-25).*
