#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Writer-1 — Outbound Copywriting Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md
Reference templates:      ./reference/
Test unitari:             ./controllo/test_writer.py

CLI:
    python agente.py --input data/leads.csv --output data/messaggi.json [--city Milano]
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

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"
_CAMPAIGN  = _ROOT_DIR.parent / "Outreach Workflow" / "campagne" / "concessionari-preventa"

for _p in [str(_SCRIPTS), str(_CAMPAIGN)]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

try:
    from event_bus import EventBus
except ImportError:
    EventBus = None  # type: ignore

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

# ── Costanti ─────────────────────────────────────────────────────────────────
MAX_WA_WORDS    = 60
MAX_EMAIL_WORDS = 200
FIRMA           = "Max"
RETRY_MAX       = 3

GANCIO_TEMPLATES: Dict[int, Dict[str, str]] = {
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
            "Preventa li genera in 2 minuti — un link animato, brandizzato, "
            "che il cliente apre sullo smartphone e firma digitalmente.\n\n"
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
            "Una cosa che noto spesso: quando un cliente scrive su WhatsApp nel weekend "
            "o la sera per un preventivo, molti saloni rispondono con un PDF del gestionale "
            "— o peggio, non rispondono affatto.\n\n"
            "Preventa permette di inviare un preventivo animato in 2 minuti, "
            "direttamente dal configuratore al telefono del cliente, in qualsiasi momento.\n\n"
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
    Documentazione completa → AGENTE.md (Sezione 9).
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
        self.agent_id            = "WriterAgent-1"
        self.event_bus           = event_bus or (EventBus() if EventBus else None)
        self.state               = self.STATE_IDLE
        self.rules               = self._load_rules()
        self._consecutive_errors = 0

    # ── Private helpers ───────────────────────────────────────────────────
    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        if md.exists():
            text = md.read_text(encoding="utf-8")
            log.debug(f"[{self.agent_id}] Regole caricate: {len(text)} chars da AGENTE.md")
            return text
        log.warning(f"[{self.agent_id}] AGENTE.md non trovato — regole non caricate")
        return ""

    def _transition(self, new_state: str) -> None:
        log.debug(f"[{self.agent_id}] {self.state} ──▶ {new_state}")
        self.state = new_state

    def _publish(self, event: str, payload: Dict) -> None:
        if self.event_bus:
            try:
                self.event_bus.publish(event, self.agent_id, payload)
            except Exception as exc:
                log.warning(f"[{self.agent_id}] EventBus publish error: {exc}")

    def _fmt(self, template: str, nome: str, citta: str) -> str:
        return template.format(nome=nome, citta=citta, firma=FIRMA).strip()

    def _select_hook(self, lead: Dict) -> int:
        """Seleziona il numero del gancio (1/2/3) in base al profilo del lead."""
        priorita = str(lead.get("priorita_lead", "")).upper()
        note     = str(lead.get("note_qualifica", "")).lower()
        ha_sito  = str(lead.get("ha_sito", "True")).lower() not in ("false", "0", "")
        try:
            n_rec = int(lead.get("numero_recensioni") or 0)
        except (ValueError, TypeError):
            n_rec = 0

        if priorita == "ALTA":
            if not ha_sito or "vecchio" in note or "scarso" in note:
                return 3
            return 2 if n_rec < 50 else 3
        if priorita == "MEDIA":
            return 1
        return 0  # BASSA → skip

    def _build_message(self, lead: Dict) -> Optional[Dict]:
        """Costruisce il dict messaggi per un singolo lead."""
        nome   = str(lead.get("nome_attivita") or "il vostro salone").strip()
        citta  = str(lead.get("citta_ricerca") or lead.get("citta", "")).strip()
        tel    = str(lead.get("telefono") or "").strip()
        canale = "whatsapp" if tel else "email"

        # Delega al modulo campagna ufficiale se disponibile
        if _HAS_PM:
            try:
                return _pm.genera_messaggi(lead)
            except Exception as e:
                log.warning(f"[{self.agent_id}] Fallback interno per {nome}: {e}")

        # Fallback interno con template embedded
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
        """
        Genera messaggi personalizzati per tutti i lead passati.

        Args:
            leads: Lista di dict con i dati del lead (da CSV/JSON).
            city:  Città di riferimento per log e payload eventi.

        Returns:
            Lista di dict contenenti i messaggi generati pronti per SenderAgent.
        """
        self._transition(self.STATE_ANALYZING)
        log.info(f"[{self.agent_id}] Generazione copy per {len(leads)} lead in {city}")

        generated: List[Dict] = []

        for lead in leads:
            self._transition(self.STATE_HOOK)
            nome = str(lead.get("nome_attivita", "?"))
            try:
                self._transition(self.STATE_GENERATING)
                msg = self._build_message(lead)
                if msg:
                    self._transition(self.STATE_VALIDATED)
                    generated.append(msg)
                    self._consecutive_errors = 0
                else:
                    log.debug(f"[{self.agent_id}] Lead skippato (priorità BASSA): {nome}")
            except Exception as exc:
                self._consecutive_errors += 1
                log.error(f"[{self.agent_id}] Errore su {nome}: {exc}")
                self._publish("writer.error", {"lead_name": nome, "error": str(exc)})
                self._transition(self.STATE_REJECTED)
                if self._consecutive_errors >= RETRY_MAX:
                    self._transition(self.STATE_ESCALATING)
                    log.error(f"[{self.agent_id}] {RETRY_MAX} errori consecutivi — ESCALATING. Pipeline interrotta.")
                    break

        self._transition(self.STATE_PUBLISHING)
        self._publish("messages.generated", {
            "city": city,
            "messages": generated,
            "count": len(generated),
        })
        log.info(f"[{self.agent_id}] ✅ Completato: {len(generated)}/{len(leads)} messaggi generati per {city}")
        self._transition(self.STATE_IDLE)
        return generated


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(
        prog="agente_writer",
        description="Writer-1 CLI — genera messaggi outbound personalizzati da CSV lead",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Esempi:\n"
            "  python agente.py --input data/leads.csv --city Milano\n"
            "  python agente.py --input data/leads.csv --output results/msg.json"
        ),
    )
    parser.add_argument("--input",  required=True,                            help="Path CSV dei lead qualificati")
    parser.add_argument("--output", default="data/messaggi_generati.json",    help="Path output JSON (default: data/messaggi_generati.json)")
    parser.add_argument("--city",   default="Italia",                         help="Città di riferimento per log (default: Italia)")
    parser.add_argument("--debug",  action="store_true",                      help="Abilita log DEBUG")
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    src = Path(args.input)
    if not src.exists():
        log.error(f"File non trovato: {src}")
        sys.exit(1)

    with open(src, newline="", encoding="utf-8-sig") as f:
        leads = list(csv.DictReader(f))
    log.info(f"Caricati {len(leads)} lead da {src}")

    agent   = WriterAgent()
    results = agent.generate_messages(leads, args.city)

    dst = Path(args.output)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info(f"💾 {len(results)} messaggi salvati → {dst}")


if __name__ == "__main__":
    _cli()
