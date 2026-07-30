#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

Outreach Preventa — flusso giornaliero automatico (comando /avvia-outreach-preventa).

FASE 1 — SCRAPING (focus import): pesca N città/giorno a rotazione da
  05-TEMPLATES-E-KIT/cities.txt, cerca su Google Maps con query orientate a
  concessionari IMPORT (non filtra per nome dopo — il focus si ottiene dalla
  query di ricerca stessa, un filtro per keyword nel nome scarterebbe troppi
  lead veri che importano senza avere "import" scritto in ragione sociale).
  Ogni lead qualificato finisce in Areus (stage NEW).

FASE 2 — INVIO WHATSAPP: dai lead Areus con stage=NEW, telefono mobile,
  priorità ALTA/MEDIA (BASSA = già digitalizzati, non il target del pitch),
  manda fino a --daily-cap messaggi (default 50), un lead alla volta, ritmo
  umano (attesa random tra invii), stage->CONTACTED dopo ogni invio REALE.
  Si ferma subito se rileva segnali di blocco account (non insiste).

Uso:
    python outreach_giornaliero.py                     # run normale, cap 50
    python outreach_giornaliero.py --test               # run di prova, limiti minimi
    python outreach_giornaliero.py --solo-scraping      # solo fase 1
    python outreach_giornaliero.py --solo-invio         # solo fase 2 (usa Areus già popolato)
    python outreach_giornaliero.py --daily-cap 10       # cap invii personalizzato
"""
from __future__ import annotations

import argparse
import importlib.util
import logging
import os
import random
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
SCRIPTS = BASE / "02-AUTOMAZIONI-E-SCRIPTS"
CITIES_FILE = BASE / "05-TEMPLATES-E-KIT" / "cities.txt"
OUTREACH_ROOT = BASE.parent  # Outreach/
CAMPAIGN_DIR = OUTREACH_ROOT / "Outreach Workflow" / "campagne" / "concessionari-preventa"
WHATSAPP_DIR = OUTREACH_ROOT / "WhatsApp Automation"
LOG_DIR = BASE / "logs"

sys.path.insert(0, str(SCRIPTS))
import areus  # noqa: E402

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.outreach-giornaliero")

# ── Config focus import ──────────────────────────────────────────────────────
IMPORT_QUERIES = [
    "concessionario auto import",
    "concessionario auto import Germania",
    "auto import usate",
]
CITTA_PER_GIORNO = 6
LIMIT_PER_COMBO = 20
DAILY_CAP_DEFAULT = 50
DELAY_MIN_SEC = 45
DELAY_MAX_SEC = 120
MAX_FALLIMENTI_CONSECUTIVI = 5


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def carica_pool_citta() -> list[str]:
    if not CITIES_FILE.exists():
        log.error(f"File città non trovato: {CITIES_FILE}")
        return []
    righe = [l.strip() for l in CITIES_FILE.read_text(encoding="utf-8").splitlines() if l.strip() and not l.strip().startswith("#")]
    return righe


def citta_di_oggi(pool: list[str], n: int) -> list[str]:
    """Rotazione deterministica: giorno dell'anno % pool -> slice di n città consecutive."""
    if not pool:
        return []
    idx = date.today().timetuple().tm_yday % len(pool)
    scelte = []
    for i in range(n):
        scelte.append(pool[(idx + i) % len(pool)])
    return scelte


def fase1_scraping(cities: list[str], limit: int, headless: bool) -> dict:
    log.info(f"FASE 1 — Scraping import-focus su {len(cities)} città: {cities}")
    cmd = [
        sys.executable, str(BASE / "scraper.py"),
        "--cities", ",".join(cities),
        "--categorie", ",".join(IMPORT_QUERIES),
        "--limit", str(limit),
    ]
    if headless:
        cmd.append("--headless")
    log.info(f"Comando: {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(BASE), capture_output=True, text=True, encoding="utf-8", errors="replace")
    log.info(proc.stdout[-4000:] if proc.stdout else "(nessun output)")
    if proc.returncode != 0:
        log.error(f"Scraping terminato con errore (exit {proc.returncode}):\n{proc.stderr[-2000:]}")
    return {"exit_code": proc.returncode, "stdout_tail": proc.stdout[-2000:] if proc.stdout else ""}


def carica_lead_da_contattare(daily_cap: int) -> list[dict]:
    data = areus._load(areus.DEFAULT_STATE_PATH)
    leads = data.get("leads", [])

    oggi = date.today().isoformat()
    gia_inviati_oggi = sum(
        1 for l in leads
        if (l.get("contattato_il") or "").startswith(oggi) and l.get("canale_contatto") == "whatsapp"
    )
    rimanenti = max(0, daily_cap - gia_inviati_oggi)
    if gia_inviati_oggi:
        log.info(f"Già inviati oggi: {gia_inviati_oggi}/{daily_cap} — rimangono {rimanenti} slot")

    def priorita_ok(l: dict) -> bool:
        # Lead import: il gancio 4 (annunci esteri) funziona a QUALSIASI priorita' sito —
        # il dolore non e' "sito vecchio", e' "tradurre annunci esteri". Per gli altri lead
        # (non-import) resta il filtro originale: BASSA = gia' digitalizzato, pitch non calza.
        if "import" in (l.get("categoria", "") or "").lower():
            return True
        return l.get("priorita_lead") in ("ALTA", "MEDIA")

    eligibili = [
        l for l in leads
        if l.get("stage") == areus.STAGE_NEW
        and l.get("telefono_tipo") == "mobile"
        and priorita_ok(l)
        and (l.get("telefono") or "").strip()
    ]
    ordine = {"ALTA": 0, "MEDIA": 1, "BASSA": 2}
    eligibili.sort(key=lambda l: ordine.get(l.get("priorita_lead"), 2))

    saltati_fisso = sum(1 for l in leads if l.get("stage") == areus.STAGE_NEW and l.get("telefono_tipo") == "fisso")
    if saltati_fisso:
        log.info(f"Lead NEW con telefono fisso (non WhatsApp-abili, restano per chiamata manuale): {saltati_fisso}")

    # Pool più grande del cap: non tutti gli "eligibili" risultano inviabili davvero (numero
    # non su WhatsApp, chat non caricata...). Senza margine, un fallimento riduce silenziosamente
    # il totale mandato sotto il minimo richiesto. Il loop di invio si ferma comunque appena
    # raggiunge `rimanenti` invii REALI, non consuma il pool intero.
    pool = eligibili[: max(rimanenti * 4, rimanenti)]
    return pool, rimanenti


def fase2_invio(daily_cap: int, dry_run: bool) -> dict:
    log.info(f"FASE 2 — Invio WhatsApp (cap giornaliero: {daily_cap}, dry_run={dry_run})")

    personalizza = _load_module(CAMPAIGN_DIR / "personalizza_messaggi.py", "personalizza_messaggi_gg")
    send_message = _load_module(WHATSAPP_DIR / "send_message.py", "send_message_gg")

    lead_da_contattare, rimanenti_oggi = carica_lead_da_contattare(daily_cap)
    log.info(f"Lead eligibili trovati (NEW + mobile + [import: ogni priorita' / altri: ALTA/MEDIA]): {len(lead_da_contattare)}")

    inviati = 0
    falliti = 0
    scartati_legittimi = 0  # numero non valido / non su WhatsApp: non e' un errore tecnico
    fallimenti_consecutivi = 0
    esiti_dettaglio = []
    # target = quanti invii REALI mancano oggi per arrivare al cap, non il cap intero
    # (altrimenti un rilancio nello stesso giorno ignora quanto gia' mandato e sfonda il cap).
    target = rimanenti_oggi if not dry_run else len(lead_da_contattare)

    for i, lead in enumerate(lead_da_contattare):
        if inviati >= target:
            log.info(f"Cap raggiunto ({inviati}/{daily_cap} invii reali) — fermo qui.")
            break

        nome = lead.get("nome_attivita", "?")
        telefono = lead.get("telefono", "")
        log.info(f"[{i+1}/{len(lead_da_contattare)}] {nome} ({telefono})")

        msg_data = personalizza.genera_messaggi(lead)
        testo = msg_data["whatsapp_msg1"]

        esito = send_message.invia_sync(telefono, testo, dry_run=dry_run)
        esiti_dettaglio.append({"nome": nome, "telefono": telefono, **esito})

        if esito["esito"] in ("account_limitato", "profilo_in_uso", "profilo_mancante"):
            log.error(f"STOP IMMEDIATO — {esito['esito']}: {esito.get('dettaglio','')}")
            break

        if esito["esito"] == "inviato":
            areus.mark_contacted(telefono, canale="whatsapp")
            inviati += 1
            fallimenti_consecutivi = 0
            log.info(f"  OK inviato ({inviati}/{daily_cap})")
        elif esito["esito"] == "dry_run_ok":
            log.info("  OK dry-run (non inviato davvero)")
            fallimenti_consecutivi = 0
        elif esito["esito"] in ("numero_non_valido", "numero_non_su_whatsapp"):
            # Scarto legittimo sul dato, non un problema tecnico: non conta per il
            # circuit-breaker (non e' segno che qualcosa nello script si e' rotto).
            scartati_legittimi += 1
            fallimenti_consecutivi = 0
            log.info(f"  Scartato ({esito['esito']}): {nome} — non contattabile su WhatsApp")
        else:
            falliti += 1
            fallimenti_consecutivi += 1
            log.warning(f"  Fallito: {esito['esito']} — {esito.get('dettaglio','')}")
            if fallimenti_consecutivi >= MAX_FALLIMENTI_CONSECUTIVI:
                log.error(f"STOP — {fallimenti_consecutivi} fallimenti consecutivi, qualcosa non va (WhatsApp Web cambiato? profilo rotto?)")
                break

        if i < len(lead_da_contattare) - 1:
            pausa = random.uniform(DELAY_MIN_SEC, DELAY_MAX_SEC)
            log.info(f"  Pausa {pausa:.0f}s prima del prossimo invio...")
            time.sleep(pausa)

    return {
        "inviati": inviati,
        "falliti": falliti,
        "scartati_legittimi": scartati_legittimi,
        "eligibili": len(lead_da_contattare),
        "dettaglio": esiti_dettaglio,
    }


def scrivi_report(risultato_scraping: dict | None, risultato_invio: dict | None):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    path = LOG_DIR / f"outreach_{date.today().isoformat()}.log"
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*70}\n{datetime.now().isoformat()}\n")
        if risultato_scraping is not None:
            f.write(f"SCRAPING: exit_code={risultato_scraping.get('exit_code')}\n")
        if risultato_invio is not None:
            f.write(f"INVIO: eligibili={risultato_invio['eligibili']} inviati={risultato_invio['inviati']} falliti={risultato_invio['falliti']} scartati_legittimi={risultato_invio.get('scartati_legittimi',0)}\n")
            for d in risultato_invio["dettaglio"]:
                f.write(f"  - {d['nome']} ({d['telefono']}): {d['esito']} {d.get('dettaglio','')}\n")
    log.info(f"Report scritto: {path}")


def main():
    parser = argparse.ArgumentParser(description="Outreach Preventa — flusso giornaliero automatico")
    parser.add_argument("--test", action="store_true", help="Run di prova: 1 città, limit basso, dry-run invio")
    parser.add_argument("--solo-scraping", action="store_true", help="Esegue solo la fase 1")
    parser.add_argument("--solo-invio", action="store_true", help="Esegue solo la fase 2 (Areus già popolato)")
    parser.add_argument("--daily-cap", type=int, default=DAILY_CAP_DEFAULT, help="Max messaggi WhatsApp da inviare oggi")
    parser.add_argument("--dry-run-invio", action="store_true", help="Fase 2 in dry-run: precompila ma non invia davvero")
    parser.add_argument("--headless", action="store_true", help="Scraping in modalità headless (default: headed, più stabile)")
    args = parser.parse_args()

    log.info("=" * 70)
    log.info(f"OUTREACH PREVENTA — RUN GIORNALIERO {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    log.info("=" * 70)

    if args.test:
        log.info("MODALITA' TEST — 1 città, limit 5, invio in dry-run")
        pool = carica_pool_citta()
        cities = citta_di_oggi(pool, 1)
        daily_cap = 2
        dry_run_invio = True
        limit = 5
    else:
        cities = citta_di_oggi(carica_pool_citta(), CITTA_PER_GIORNO)
        daily_cap = args.daily_cap
        dry_run_invio = args.dry_run_invio
        limit = LIMIT_PER_COMBO

    risultato_scraping = None
    risultato_invio = None

    if not args.solo_invio:
        risultato_scraping = fase1_scraping(cities, limit, args.headless)

    if not args.solo_scraping:
        risultato_invio = fase2_invio(daily_cap, dry_run_invio)

    scrivi_report(risultato_scraping, risultato_invio)

    log.info("=" * 70)
    log.info("RIEPILOGO GIORNATA")
    if risultato_invio:
        log.info(f"  Messaggi WhatsApp inviati: {risultato_invio['inviati']}/{daily_cap}")
        log.info(f"  Falliti (tecnici): {risultato_invio['falliti']}")
        log.info(f"  Scartati (numero non su WhatsApp/non valido): {risultato_invio.get('scartati_legittimi',0)}")
    log.info("=" * 70)


if __name__ == "__main__":
    main()
