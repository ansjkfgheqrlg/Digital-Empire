#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: NERI · Controllore: Emperator Agent · Origine: TASK-PREVENTA-CANALI-W1
Governo: MANDATO Art.8 + ADR-008

Canale di invio Gmail per Preventa, accanto a WhatsApp (send_message.py). Non reinventa
il sender: riusa `EmailSenderAgent` gia' in produzione in
`Outreach/Outreach Workflow/agents/sender.py` (stesso motore delle campagne email di
Outreach Factory) — stesse credenziali Gmail in `Outreach Workflow/.env`.

Interfaccia compatibile con send_message.invia_sync() cosi' outreach_giornaliero.py puo'
trattare i due canali allo stesso modo: ritorna sempre {"esito": ..., "dettaglio": ...}.
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Optional

BASE = Path(__file__).resolve().parent
OUTREACH_ROOT = BASE.parent
SENDER_PATH = OUTREACH_ROOT / "Outreach Workflow" / "agents" / "sender.py"
ENV_PATH = OUTREACH_ROOT / "Outreach Workflow" / ".env"

try:
    from dotenv import load_dotenv
    load_dotenv(ENV_PATH)
except Exception:
    pass


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


_sender_mod = None
_agent = None


def _get_agent():
    """Lazy init: niente connessione SMTP finche' non serve davvero (dry-run non ne ha bisogno)."""
    global _sender_mod, _agent
    if _agent is not None:
        return _agent

    gmail_user = os.environ.get("GMAIL_USER", "")
    app_password = os.environ.get("GMAIL_APP_PASSWORD", "")
    if not gmail_user or not app_password:
        raise RuntimeError(
            f"GMAIL_USER/GMAIL_APP_PASSWORD mancanti. Verifica {ENV_PATH} "
            "(stesse credenziali gia' usate da Outreach Factory)."
        )

    if not SENDER_PATH.exists():
        raise RuntimeError(f"Sender non trovato: {SENDER_PATH}")

    _sender_mod = _load_module(SENDER_PATH, "email_sender_agent_gg")
    _agent = _sender_mod.EmailSenderAgent(gmail_user, app_password)
    return _agent


def invia_sync(email_dest: str, oggetto: str, corpo: str, dry_run: bool = True) -> dict:
    """Invia una singola email (o simula in dry-run). Stesso schema esiti di
    send_message.invia_sync(): 'inviato' / 'dry_run_ok' / 'numero_non_valido' (qui:
    email mancante/malformata) / 'errore_tecnico'."""
    email_dest = (email_dest or "").strip()
    if not email_dest or "@" not in email_dest:
        return {"esito": "email_non_valida", "dettaglio": f"email mancante o malformata: '{email_dest}'"}

    if dry_run:
        return {
            "esito": "dry_run_ok",
            "dettaglio": f"[DRY-RUN] a={email_dest} oggetto='{oggetto}' corpo_len={len(corpo)}",
        }

    try:
        agent = _get_agent()
    except RuntimeError as e:
        return {"esito": "errore_tecnico", "dettaglio": str(e)}

    risultati = agent.run(
        [{"email": email_dest, "oggetto": oggetto, "corpo": corpo}],
        anteprima=False,
        output_dir=str(BASE / "data" / "log_email"),
    )
    if not risultati:
        return {"esito": "errore_tecnico", "dettaglio": "sender non ha restituito risultati (credenziali? vedi log sopra)"}

    stato = risultati[0].get("stato")
    if stato == "inviata":
        return {"esito": "inviato", "dettaglio": ""}
    return {"esito": "errore_tecnico", "dettaglio": "invio fallito lato SMTP (email non valida o rifiutata)"}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Test invio email singola (Preventa)")
    parser.add_argument("--email", required=True)
    parser.add_argument("--oggetto", default="Test Preventa")
    parser.add_argument("--corpo", default="Messaggio di test.")
    parser.add_argument("--live", action="store_true", help="Invia davvero (default: dry-run)")
    args = parser.parse_args()
    esito = invia_sync(args.email, args.oggetto, args.corpo, dry_run=not args.live)
    print(esito)
