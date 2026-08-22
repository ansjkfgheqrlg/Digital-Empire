# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

Areus (Aureus Agency OS / EmpireDesk) integration: scrive i lead qualificati in un file
JSON condiviso che EmpireDesk/modules/preventa.py legge/serve alla UI. Sostituisce
Google Sheets (ADR: niente servizi esterni, niente credenziali da configurare — Areus
e' gia' la piattaforma unica dell'azienda, PIANO-MAESTRO/17-EMPIRE-DESK-APP.md).
"""
from __future__ import annotations

import json
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

log = logging.getLogger("preventa-pw.areus")

# Outreach/preventa-maps-scraper/02-AUTOMAZIONI-E-SCRIPTS/areus.py -> parents[3] = Digital Empire
_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_STATE_PATH = _REPO_ROOT / "EmpireDesk" / "state" / "preventa_leads.json"

# Stage iniziale = stesso enum LeadStage di EmpireDesk/platform/types.ts (NEW/CONTACTED/...)
STAGE_NEW = "NEW"
STAGE_CONTACTED = "CONTACTED"


def normalize_phone(p: str) -> str:
    return re.sub(r"\s+", "", p or "").replace("-", "").replace("(", "").replace(")", "")


def classifica_telefono_it(telefono: str) -> str:
    """
    "mobile" / "fisso" / "sconosciuto". Serve a filtrare chi e' raggiungibile su WhatsApp
    (solo mobile). Numeri italiani: mobile = 10 cifre che iniziano per 3 (o 39+10 cifre
    con prefisso internazionale gia' incluso); fisso = inizia per 0.
    """
    n = re.sub(r"[^\d+]", "", telefono or "").lstrip("+")
    if n.startswith("39") and len(n) == 12:
        n = n[2:]
    if len(n) != 10:
        return "sconosciuto"
    if n.startswith("3"):
        return "mobile"
    if n.startswith("0"):
        return "fisso"
    return "sconosciuto"


def _load(state_path: Path) -> Dict:
    if not state_path.exists():
        return {"leads": [], "aggiornato": None}
    try:
        return json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        log.warning(f"State Areus illeggibile ({state_path}), riparto da zero senza sovrascrivere finche' non ci sono nuovi dati")
        return {"leads": [], "aggiornato": None, "errore_lettura": str(state_path)}


def _save(state_path: Path, data: Dict) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    data["aggiornato"] = time.strftime("%Y-%m-%d %H:%M")
    state_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def upload_to_areus(leads: List[Dict], city: str, state_path: Optional[str] = None, push_only_alta: bool = False) -> Dict:
    """
    Aggiunge i lead nuovi (dedup per telefono normalizzato) al CRM Areus condiviso con
    EmpireDesk. Nessuna credenziale richiesta: e' un file locale sulla stessa macchina/repo.
    Ritorna {"aggiunti": n, "duplicati": n, "path": str}.
    """
    path = Path(state_path) if state_path else DEFAULT_STATE_PATH

    if push_only_alta:
        leads_to_push = [r for r in leads if r.get("priorita_lead") == "ALTA"]
        log.info(f"Filtro Areus: solo ALTA -> {len(leads_to_push)} su {len(leads)}")
    else:
        leads_to_push = leads

    data = _load(path)
    existing = {normalize_phone(l.get("telefono", "")) for l in data.get("leads", []) if l.get("telefono")}

    added = 0
    skipped = 0
    now = time.strftime("%Y-%m-%d %H:%M")
    for lead in leads_to_push:
        if not lead.get("nome_attivita"):
            continue
        phone_norm = normalize_phone(lead.get("telefono", ""))
        if phone_norm and phone_norm in existing:
            skipped += 1
            continue
        data.setdefault("leads", []).append({
            "nome_attivita": lead.get("nome_attivita", ""),
            "indirizzo": lead.get("indirizzo", ""),
            "telefono": lead.get("telefono", ""),
            "sito_web": lead.get("sito_web", ""),
            "ha_sito": lead.get("ha_sito", ""),
            "numero_recensioni": lead.get("numero_recensioni", 0),
            "media_recensioni": lead.get("media_recensioni", 0),
            "ha_ads_attive": lead.get("ha_ads_attive", ""),
            "priorita_lead": lead.get("priorita_lead", ""),
            "citta_ricerca": lead.get("citta_ricerca", city),
            "categoria": lead.get("categoria", ""),
            "note_qualifica": lead.get("note_qualifica", ""),
            "maps_url": lead.get("maps_url", ""),
            "data_estrazione": lead.get("data_estrazione", ""),
            "telefono_tipo": classifica_telefono_it(lead.get("telefono", "")),
            "stage": STAGE_NEW,
            "note": "",
            "aggiunto_il": now,
        })
        if phone_norm:
            existing.add(phone_norm)
        added += 1

    if added:
        _save(path, data)
        log.info(f"✅ Areus: {added} nuovi lead aggiunti ({city}), {skipped} duplicati saltati -> {path}")
    else:
        log.info(f"Areus: nessun nuovo lead da aggiungere per {city} ({skipped} duplicati)")

    return {"aggiunti": added, "duplicati": skipped, "path": str(path)}


def mark_contacted(telefono: str, canale: str = "", state_path: Optional[str] = None, testo: Optional[str] = None) -> bool:
    """Usato da contact_leads.py: segna un lead come CONTACTED in Areus dopo l'invio.
    `testo` (msg1 effettivamente inviato) viene salvato per permettere al rule-keeper del
    follow-up di controllare l'"angolo diverso" (Pilastro 6) contro cosa e' stato scritto."""
    path = Path(state_path) if state_path else DEFAULT_STATE_PATH
    data = _load(path)
    key = normalize_phone(telefono)
    if not key:
        return False
    found = False
    for lead in data.get("leads", []):
        if normalize_phone(lead.get("telefono", "")) == key:
            lead["stage"] = STAGE_CONTACTED
            lead["canale_contatto"] = canale
            lead["contattato_il"] = time.strftime("%Y-%m-%d %H:%M")
            if testo:
                lead["msg1_testo"] = testo
            found = True
    if found:
        _save(path, data)
    return found


def mark_followup_sent(telefono: str, step: int, testo: Optional[str] = None, state_path: Optional[str] = None) -> bool:
    """Segna l'invio di un follow-up (step=2 o 3) su un lead gia' CONTACTED. Non tocca lo
    stage (resta CONTACTED: solo un avanzamento manuale in EmpireDesk a PROPOSAL/NEGOTIATION/
    CLOSED_* segnala che il lead ha risposto e ferma i follow-up successivi, vedi
    `carica_lead_per_followup` — questo script non ha modo di leggere le risposte WhatsApp)."""
    if step not in (2, 3):
        raise ValueError(f"step deve essere 2 o 3, ricevuto {step}")
    path = Path(state_path) if state_path else DEFAULT_STATE_PATH
    data = _load(path)
    key = normalize_phone(telefono)
    if not key:
        return False
    found = False
    for lead in data.get("leads", []):
        if normalize_phone(lead.get("telefono", "")) == key:
            lead[f"msg{step}_inviato_il"] = time.strftime("%Y-%m-%d %H:%M")
            if testo:
                lead[f"msg{step}_testo"] = testo
            found = True
    if found:
        _save(path, data)
    return found


def _parse_ts(s: Optional[str]):
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M")
    except ValueError:
        return None


def _ore_trascorse(ts: Optional[str]) -> Optional[float]:
    dt = _parse_ts(ts)
    if dt is None:
        return None
    return (datetime.now() - dt).total_seconds() / 3600.0


def carica_lead_per_followup(step: int, ore_attesa: float, ore_min_dal_precedente: float = 0,
                              state_path: Optional[str] = None) -> List[Dict]:
    """Lead CONTACTED via WhatsApp pronti per il follow-up `step` (2 o 3), FIFO (piu' vecchi
    prima). Nessuna rilevazione automatica di risposta (send_message.py non legge la chat):
    il segnale "ha risposto, non mandare piu' follow-up" e' lo stage che avanza oltre
    CONTACTED (PROPOSAL/NEGOTIATION/CLOSED_*) fatto a mano in EmpireDesk. Se un lead resta
    CONTACTED, per questo script e' "silenzio" — coerente con la sequenza 20/40/30 della
    Bibbia (msg2/msg3 vanno mandati anche in assenza di risposta esplicita).

    step=2: soglia `ore_attesa` misurata da msg1 (contattato_il) — es. 24h di silenzio.
    step=3: soglia `ore_attesa` misurata da msg1 (contattato_il), non da msg2 — la regola
    originale in personalizza_messaggi.py e' "G+5 di silenzio dopo msg1", non dopo msg2.
    `ore_min_dal_precedente` e' una guardia separata su msg2 (default 24h nel chiamante) per
    non sparare msg2 e msg3 nello stesso run se msg2 e' partito in ritardo."""
    if step not in (2, 3):
        raise ValueError(f"step deve essere 2 o 3, ricevuto {step}")
    path = Path(state_path) if state_path else DEFAULT_STATE_PATH
    data = _load(path)
    leads = data.get("leads", [])

    campo_step = f"msg{step}_inviato_il"

    eligibili = []
    for lead in leads:
        if lead.get("stage") != STAGE_CONTACTED:
            continue
        if lead.get("canale_contatto") != "whatsapp":
            continue
        if lead.get(campo_step):
            continue  # follow-up di questo step gia' mandato
        if step == 3 and not lead.get("msg2_inviato_il"):
            continue  # msg3 richiede che msg2 sia gia' partito

        ore_da_msg1 = _ore_trascorse(lead.get("contattato_il"))
        if ore_da_msg1 is None or ore_da_msg1 < ore_attesa:
            continue

        if step == 3 and ore_min_dal_precedente:
            ore_da_msg2 = _ore_trascorse(lead.get("msg2_inviato_il"))
            if ore_da_msg2 is None or ore_da_msg2 < ore_min_dal_precedente:
                continue

        eligibili.append((ore_da_msg1, lead))

    eligibili.sort(key=lambda t: -t[0])  # piu' ore trascorse = piu' vecchio = prima
    return [l for _, l in eligibili]
