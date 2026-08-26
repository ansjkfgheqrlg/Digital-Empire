#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: NERI · Controllore: Emperator Agent · Origine: TASK-PREVENTA-CANALI-W1
Governo: MANDATO Art.8 + ADR-008

Passa sui lead gia' in Areus (EmpireDesk/state/preventa_leads.json) che hanno `sito_web`
ma non ancora `email`, e prova a estrarla dal sito reale (email_extractor.py: mailto/regex,
no login/browser). Scrive l'email trovata sul lead con areus.set_email().

Uso:
    python estrai_email_lead.py                # tutti i lead con sito_web e senza email
    python estrai_email_lead.py --limit 20      # solo i primi 20 (utile per un test rapido)
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path

SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "02-AUTOMAZIONI-E-SCRIPTS")
sys.path.append(SCRIPTS_DIR)

import areus  # noqa: E402
from email_extractor import estrai_email_da_sito  # noqa: E402

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.estrai-email")


def main():
    parser = argparse.ArgumentParser(description="Estrae email pubbliche dai siti dei lead Preventa gia' in Areus")
    parser.add_argument("--limit", type=int, default=0, help="Max lead da processare (0 = tutti)")
    parser.add_argument("--state-path", type=str, default="", help="Override path Areus (default: EmpireDesk/state/preventa_leads.json)")
    args = parser.parse_args()

    state_path = Path(args.state_path) if args.state_path else areus.DEFAULT_STATE_PATH
    data = areus._load(state_path)
    leads = data.get("leads", [])

    da_processare = [
        l for l in leads
        if (l.get("sito_web") or "").strip() and not (l.get("email") or "").strip()
    ]
    # dedup per sito_web: piu' lead possono condividere lo stesso sito (dedup gia' fatto a
    # monte da scraper.py per telefono, non per sito_web)
    siti_visti = {}
    for l in da_processare:
        siti_visti.setdefault(l["sito_web"].strip(), l)
    siti_unici = list(siti_visti.keys())

    if args.limit:
        siti_unici = siti_unici[: args.limit]

    log.info(f"Lead con sito_web e senza email: {len(da_processare)} ({len(siti_unici)} siti unici da visitare)")

    trovate = 0
    non_trovate = 0
    for i, sito in enumerate(siti_unici, 1):
        log.info(f"[{i}/{len(siti_unici)}] {sito}")
        email = estrai_email_da_sito(sito)
        if email:
            n_aggiornati = 0
            if areus.set_email(sito, email, state_path=str(state_path)):
                n_aggiornati = sum(1 for l in leads if (l.get("sito_web") or "").strip() == sito)
            log.info(f"  ✓ trovata: {email} (aggiornati {n_aggiornati} lead con questo sito)")
            trovate += 1
        else:
            log.info("  ✗ nessuna email pubblica trovata")
            non_trovate += 1
        time.sleep(0.5)  # cortesia verso i siti visitati, non serve di piu' (no rate limit noto)

    log.info("=" * 60)
    log.info(f"RIEPILOGO: {trovate} email trovate, {non_trovate} siti senza email su {len(siti_unici)} visitati")
    log.info(f"Stato aggiornato: {state_path}")


if __name__ == "__main__":
    main()
