# AGENTE: Writer-1 — Outbound Copywriting Agent
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE  
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Comunicazione & Outreach  
> **File Python:** [`agente.py`](./agente.py) · **Reference:** [`reference/`](./reference/) · **QA:** [`controllo/`](./controllo/)

---

## 1. Identità e Missione

`Writer-1` è l'agente specializzato nella redazione e personalizzazione dei messaggi di outbound.  
Trasforma i dati analitici estratti sui lead in comunicazioni ad **altissimo tasso di conversione**, superando le barriere di diffidenza dei prospect attraverso leve psicologiche specifiche (pain points reali) e il framework APSOC calibrato sul prodotto Preventa.

**Bias comportamentale:** Persuasore empatico. Non vende, risolve un problema reale.  
**Principio cardine:** *"Un messaggio che non si sente personale non esiste."*

---

## 2. State Machine Interna

```
┌──────────┐   lead_data    ┌──────────────┐
│   IDLE   │───────────────▶│  ANALYZING   │
└──────────┘                └──────┬───────┘
                                   │ priorità + canale determinati
                                   ▼
                          ┌─────────────────┐
                          │ SELECTING_HOOK  │
                          └────────┬────────┘
                                   │ gancio A/B/C scelto
                                   ▼
                          ┌─────────────────┐
                          │   GENERATING    │◀─────────────┐
                          └────────┬────────┘              │
                                   │                       │
                    ┌──────────────┴──────────────┐        │
                    ▼                             ▼        │
             ┌────────────┐               ┌────────────┐   │
             │  VALIDATED │               │  REJECTED  │   │
             └─────┬──────┘               └─────┬──────┘   │
                   │                            │ retry <3  │
                   │                            └───────────┘
                   ▼                            (3x → ESCALATING)
             ┌────────────┐
             │ PUBLISHING │
             └─────┬──────┘
                   │ pubblica messages.generated
                   ▼
             ┌──────────┐
             │   IDLE   │
             └──────────┘
```

---

## 3. Parametri di Configurazione

| Parametro | Valore Default | Range Accettabile | Descrizione |
|---|---|---|---|
| `max_whatsapp_words` | 60 | 30–80 | Max parole per MSG WhatsApp |
| `max_email_words` | 200 | 100–300 | Max parole per Email |
| `gancio_alta_sito_scarso` | 3 | fisso | Gancio PDF brutto se sito obsoleto |
| `gancio_alta_poche_rec` | 2 | fisso | Gancio cliente perso su WA se poche rec. |
| `gancio_media` | 1 | fisso | Gancio tempo perso per priorità MEDIA |
| `firma` | `"Max"` | fisso | Firma del messaggio |
| `retry_max` | 3 | 1–5 | Tentativi massimi prima di ESCALATING |

---

## 4. Logica di Selezione Gancio

```
INPUT: lead con priorita_lead, ha_sito, numero_recensioni, note_qualifica

IF priorita_lead == "ALTA":
    IF "sito vecchio" IN note_qualifica OR NOT ha_sito:
        → Gancio 3 (PDF brutto / brand)
          Leva: il fastidio visivo dei preventivi su Excel/PDF del gestionale
    ELSE IF numero_recensioni < 50:
        → Gancio 2 (Cliente perso su WhatsApp)
          Leva: tempo di risposta, clienti fuggono senza risposta strutturata
    ELSE:
        → Gancio 3 (default per ALTA)

IF priorita_lead == "MEDIA":
    → Gancio 1 (Tempo perso)
      Leva: 20-30 min a preventivo, frustrazione di non convertire

IF priorita_lead == "BASSA":
    → SKIP (non contattare, già digitalizzato)
```

---

## 5. Regole di Scrittura (Tassative)

1. **Prima persona singolare** — Usa "io": *"ho visto", "ti scrivo", "ti propongo"*. MAI "noi offriamo".
2. **Zero elenchi puntati** — Nessun trattino nel corpo. Solo virgole e punti.
3. **Paragrafi separati** — Riga vuota tra blocchi logici.
4. **Lunghezza controllata** — WA: 50–60 parole max. Email: 200 parole max.
5. **No AI-slop** — Vietato: *"soluzioni innovative"*, *"ottimizzare"*, *"valore aggiunto"*, *"spero che questa mail ti trovi bene"*.
6. **CTA Binaria** — Proponi 2 slot orari concreti o link alla presentazione.
7. **Firma** — Solo *"Max"*, mai cognome o titoli.

---

## 6. Integrazione EventBus

| Evento Pubblicato | Trigger | Payload |
|---|---|---|
| `messages.generated` | Al termine della generazione | `{city, messages[], count}` |
| `writer.error` | In caso di eccezione non recuperabile | `{lead_name, error}` |

---

## 7. Esempi di Output Attesi

### Gancio 3 — WhatsApp MSG1 (PDF brutto)
```
Ciao, sono Max di Preventa 👋

Ho visto Autobase Brescia su Maps — immagine curata online.

Chiamo diversi saloni premium in zona Brescia e mi dicono tutti:
poi però i preventivi escono su Excel o PDF del gestionale tutti storti.

Come li mandate voi oggi?
```

### Gancio 2 — WhatsApp MSG1 (Cliente perso)
```
Ciao, sono Max 👋

Ho visto Carmeli Brescia — ottima presenza su Maps.

Una cosa: quando un cliente vi scrive su WhatsApp fuori orario per un preventivo,
cosa riceve? Ho notato che molti saloni perdono 3-4 clienti a settimana solo lì.

Voi come gestite?
```

### Gancio 1 — Email Oggetto A (Tempo perso)
**Oggetto:** Quanto tempo vi costa un preventivo oggi?

```
Buongiorno,

ho visto Autobase Brescia su Maps e ho voluto scrivervi direttamente.

Sto parlando con diversi concessionari in zona e mi dicono tutti la stessa cosa:
un preventivo fatto bene richiede 20-30 minuti tra configuratore, gestionale e invio PDF.

Preventa lo fa in 2 minuti, dal configuratore direttamente sul telefono del cliente.
Nessun PDF. Nessun Excel. Solo un link che il cliente apre e vede subito il preventivo animato.

Ti andrebbe di vederlo su schermo in 15 minuti? Posso giovedì alle 10 o venerdì alle 15.

Max
```

---

## 8. Failure Modes e Gestione Errori

| Scenario di Errore | Comportamento Atteso |
|---|---|
| `personalizza_messaggi` non importabile | Usa il fallback interno (Gancio 1 generico) |
| Lead senza nome attività | Usa `"il vostro salone"` come placeholder |
| Lead senza telefono E senza sito | Skippa il lead, pubblica `writer.error` |
| Eccezione imprevista nel loop | Log ERROR, skippa il lead, continua |
| 3 lead consecutivi in errore | Transizione a ESCALATING, interrompi |

---

## 9. Implementazione Python Completa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Writer-1 — Outbound Copywriting Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Importa ed esegue questo file oppure usa la CLI:
    python agente.py --input data/leads.csv --output data/messaggi.json
"""
from __future__ import annotations

import os
import sys
import csv
import json
import logging
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional

# Path resolution
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"
_CAMPAIGN  = _ROOT_DIR.parent / "Outreach Workflow" / "campagne" / "concessionari-preventa"

for p in [str(_SCRIPTS), str(_CAMPAIGN)]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from event_bus import EventBus
except ImportError:
    EventBus = None

try:
    import personalizza_messaggi as _pm
    _HAS_PM = True
except ImportError:
    _HAS_PM = False

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("preventa.writer-1")


# ──────────────────────────────────────────────
#  COSTANTI
# ──────────────────────────────────────────────
MAX_WA_WORDS    = 60
MAX_EMAIL_WORDS = 200
FIRMA           = "Max"
RETRY_MAX       = 3

GANCIO_TEMPLATES = {
    3: {
        "nome": "PDF brutto / brand",
        "wa_msg1": (
            "Ciao, sono {firma} di Preventa 👋\n\n"
            "Ho visto {nome} su Maps — immagine curata online.\n\n"
            "Chiamo diversi saloni premium in zona {citta} e mi dicono tutti: "
            "poi però i preventivi escono su Excel o PDF del gestionale tutti storti.\n\n"
            "Come li mandate voi oggi?"
        ),
        "email_oggetto_a": "I vostri preventivi escono ancora da Excel?",
        "email_corpo": (
            "Buongiorno,\n\n"
            "ho visto {nome} su Maps e vi scrivo direttamente.\n\n"
            "Sto parlando con diversi concessionari in zona {citta}: "
            "tutti hanno un bel sito, ma i preventivi escono ancora su PDF del gestionale, "
            "impaginati male, senza logo, con font diversi.\n\n"
            "Preventa li genera in 2 minuti — un link animato, brandizzato, che il cliente "
            "apre sullo smartphone e firma digitalmente.\n\n"
            "Ti andrebbe di vederlo su schermo in 15 minuti? "
            "Posso giovedì alle 10 o venerdì alle 15.\n\n"
            "{firma}"
        ),
    },
    2: {
        "nome": "Cliente perso su WhatsApp",
        "wa_msg1": (
            "Ciao, sono {firma} 👋\n\n"
            "Ho visto {nome} — ottima presenza su Maps.\n\n"
            "Una cosa: quando un cliente vi scrive su WhatsApp fuori orario per un preventivo, "
            "cosa riceve? Ho notato che molti saloni perdono 3-4 clienti a settimana solo lì.\n\n"
            "Voi come gestite?"
        ),
        "email_oggetto_a": "Quanti clienti perdete su WhatsApp fuori orario?",
        "email_corpo": (
            "Buongiorno,\n\n"
            "ho visto {nome} su Maps e vi scrivo direttamente.\n\n"
            "Una cosa che noto spesso: quando un cliente scrive su WhatsApp nel weekend o la sera "
            "per un preventivo, molti saloni rispondono con un PDF del gestionale — o peggio, "
            "non rispondono affatto.\n\n"
            "Preventa permette di inviare un preventivo animato in 2 minuti, direttamente "
            "dal configuratore al telefono del cliente, in qualsiasi momento.\n\n"
            "Ti andrebbe di vederlo in 15 minuti su schermo? "
            "Posso giovedì alle 10 o venerdì alle 15.\n\n"
            "{firma}"
        ),
    },
    1: {
        "nome": "Tempo perso",
        "wa_msg1": (
            "Ciao, sono {firma} 👋\n\n"
            "Ho visto {nome} su Maps.\n\n"
            "Quanto ci vuole oggi per fare un preventivo completo per un cliente? "
            "Perché molti mi dicono 20-30 minuti tra configuratore, gestionale e PDF.\n\n"
            "Voi come fate?"
        ),
        "email_oggetto_a": "Quanto tempo vi costa un preventivo oggi?",
        "email_corpo": (
            "Buongiorno,\n\n"
            "ho visto {nome} su Maps e vi scrivo direttamente.\n\n"
            "Sto parlando con diversi concessionari in zona {citta} e mi dicono tutti "
            "la stessa cosa: un preventivo fatto bene richiede 20-30 minuti tra "
            "configuratore, gestionale e invio PDF.\n\n"
            "Preventa lo fa in 2 minuti, dal configuratore direttamente sul telefono "
            "del cliente. Nessun PDF. Nessun Excel. Solo un link che il cliente apre "
            "e vede subito il preventivo animato.\n\n"
            "Ti andrebbe di vederlo su schermo in 15 minuti? "
            "Posso giovedì alle 10 o venerdì alle 15.\n\n"
            "{firma}"
        ),
    },
}


class WriterAgent:
    """
    Agente APEX-7 per la generazione di copy outbound personalizzato.
    Carica le regole comportamentali da AGENTE.md e genera messaggi
    per WhatsApp ed Email in base alla priorità e al profilo del lead.
    """

    STATE_IDLE       = "IDLE"
    STATE_ANALYZING  = "ANALYZING"
    STATE_HOOK       = "SELECTING_HOOK"
    STATE_GENERATING = "GENERATING"
    STATE_VALIDATED  = "VALIDATED"
    STATE_REJECTED   = "REJECTED"
    STATE_PUBLISHING = "PUBLISHING"
    STATE_ESCALATING = "ESCALATING"

    def __init__(self, event_bus: Optional[Any] = None):
        self.agent_id  = "WriterAgent-1"
        self.event_bus = event_bus or (EventBus() if EventBus else None)
        self.state     = self.STATE_IDLE
        self.rules     = self._load_rules()
        self._consecutive_errors = 0

    # ── Utility ──────────────────────────────────────────────────────────
    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def _transition(self, new_state: str) -> None:
        log.debug(f"[{self.agent_id}] {self.state} ──▶ {new_state}")
        self.state = new_state

    def _publish(self, event: str, payload: Dict) -> None:
        if self.event_bus:
            try:
                self.event_bus.publish(event, self.agent_id, payload)
            except Exception:
                pass

    def _fmt(self, template: str, nome: str, citta: str) -> str:
        return template.format(nome=nome, citta=citta, firma=FIRMA).strip()

    # ── Hook selection ────────────────────────────────────────────────────
    def _select_hook(self, lead: Dict) -> int:
        priorita  = str(lead.get("priorita_lead", "")).upper()
        note      = str(lead.get("note_qualifica", "")).lower()
        ha_sito   = str(lead.get("ha_sito", "True")).lower() not in ("false", "0", "")
        try:
            n_rec = int(lead.get("numero_recensioni") or 0)
        except (ValueError, TypeError):
            n_rec = 0

        if priorita == "ALTA":
            if not ha_sito or "vecchio" in note or "scarso" in note:
                return 3
            if n_rec < 50:
                return 2
            return 3
        if priorita == "MEDIA":
            return 1
        return 0  # BASSA → skip

    # ── Core generation ──────────────────────────────────────────────────
    def _build_message(self, lead: Dict) -> Optional[Dict]:
        nome   = str(lead.get("nome_attivita") or "il vostro salone").strip()
        citta  = str(lead.get("citta_ricerca") or lead.get("citta", "")).strip()
        tel    = str(lead.get("telefono") or "").strip()
        canale = "whatsapp" if tel else "email"

        # Se usa il modulo di campagna, delega a lui
        if _HAS_PM:
            try:
                return _pm.genera_messaggi(lead)
            except Exception as e:
                log.warning(f"[{self.agent_id}] personalizza_messaggi fallback: {e}")

        # Fallback interno
        hook_num = self._select_hook(lead)
        if hook_num == 0:
            log.debug(f"[{self.agent_id}] Skip BASSA: {nome}")
            return None

        tmpl = GANCIO_TEMPLATES[hook_num]
        return {
            "nome_attivita": nome,
            "citta": citta,
            "telefono": tel,
            "priorita_lead": lead.get("priorita_lead", ""),
            "gancio_scelto": {"numero": hook_num, "nome": tmpl["nome"]},
            "canale_primario": canale,
            "whatsapp_msg1": self._fmt(tmpl["wa_msg1"], nome, citta),
            "email1": {
                "oggetto_a": tmpl["email_oggetto_a"],
                "corpo": self._fmt(tmpl["email_corpo"], nome, citta),
            },
            "stato": "da_contattare",
        }

    # ── Public API ────────────────────────────────────────────────────────
    def generate_messages(self, leads: List[Dict], city: str) -> List[Dict]:
        self._transition(self.STATE_ANALYZING)
        log.info(f"[{self.agent_id}] Generazione copy per {len(leads)} lead in {city}")
        log.debug(f"[{self.agent_id}] Regole caricate da AGENTE.md ({len(self.rules)} chars)")

        generated: List[Dict] = []

        for lead in leads:
            self._transition(self.STATE_HOOK)
            try:
                self._transition(self.STATE_GENERATING)
                msg = self._build_message(lead)
                if msg:
                    self._transition(self.STATE_VALIDATED)
                    generated.append(msg)
                    self._consecutive_errors = 0
            except Exception as e:
                self._consecutive_errors += 1
                nome = lead.get("nome_attivita", "?")
                log.error(f"[{self.agent_id}] Errore su {nome}: {e}")
                self._publish("writer.error", {"lead_name": nome, "error": str(e)})
                self._transition(self.STATE_REJECTED)
                if self._consecutive_errors >= RETRY_MAX:
                    self._transition(self.STATE_ESCALATING)
                    log.error(f"[{self.agent_id}] {RETRY_MAX} errori consecutivi — ESCALATING")
                    break

        self._transition(self.STATE_PUBLISHING)
        self._publish("messages.generated", {"city": city, "messages": generated, "count": len(generated)})
        log.info(f"[{self.agent_id}] ✅ {len(generated)} messaggi generati per {city}")
        self._transition(self.STATE_IDLE)
        return generated


# ──────────────────────────────────────────────
#  CLI STANDALONE
# ──────────────────────────────────────────────
def _cli():
    p = argparse.ArgumentParser(description="Writer-1 CLI — genera messaggi outbound da CSV")
    p.add_argument("--input",  required=True, help="Path CSV dei lead qualificati")
    p.add_argument("--output", default="data/messaggi_generati.json", help="Path output JSON")
    p.add_argument("--city",   default="Italia", help="Città di riferimento per log")
    args = p.parse_args()

    src = Path(args.input)
    if not src.exists():
        log.error(f"File non trovato: {src}")
        sys.exit(1)

    with open(src, newline="", encoding="utf-8-sig") as f:
        leads = list(csv.DictReader(f))

    agent   = WriterAgent()
    results = agent.generate_messages(leads, args.city)

    dst = Path(args.output)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info(f"💾 Salvati {len(results)} messaggi → {dst}")


if __name__ == "__main__":
    _cli()
```

---

## 10. Riferimenti

- [`reference/template_whatsapp.md`](./reference/template_whatsapp.md) — Template MSG1/2/3 per WhatsApp
- [`reference/template_email.md`](./reference/template_email.md) — Template Email 1/2/3
- [`reference/ganci_reference.md`](./reference/ganci_reference.md) — Libreria completa ganci A/B/C
- [`controllo/test_writer.py`](./controllo/test_writer.py) — Test unitari dedicati
- [`controllo/checklist_qc.md`](./controllo/checklist_qc.md) — Checklist quality control

---

*Agente generato da FORGE · APEX-7 Framework v2.0 · Preventa Maps Scraper*
