"""
licenza.py — Kill-switch abbonamento (Half A / Max). Semplice e robusto.

L'app, PRIMA di generare un preventivo, verifica lo stato del concessionario leggendo uno
"stato online" che controlli TU (un JSON pubblico: Gist GitHub, file su hosting, endpoint).
Per revocare: cambi "active" in "suspended" nel JSON e salvi. Blocco al prossimo link.

Design "deve funzionare tutto" (non blocca mai chi paga per un blip di rete):
  - stato "active" / dealer non elencato ma URL raggiungibile  -> CONSENTI
  - stato "suspended"/"expired"/"blocked"                      -> BLOCCA (kill-switch)
  - LICENSE_URL non configurato                                -> CONSENTI (nessun controllo)
  - URL non raggiungibile (rete)                               -> usa ultima cache valida;
                                                                  se mai vista -> CONSENTI (grace)

Nessun segreto hardcoded: l'URL sta in .env (LICENSE_URL) o nel config del dealer (license_url).

Formato JSON accettato (uno dei due):
  {"novacar": "active", "altrodealer": "suspended"}
  {"dealers": {"novacar": {"status": "active", "note": "pagato fino 2026-08"}}}
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

CACHE_NAME = ".licenza_cache.json"
TIMEOUT_S = 8
ACTIVE = {"active", "attivo", "ok", "paid", "pagato", "", "trial", "valido"}
BLOCKED = {"suspended", "sospeso", "expired", "scaduto", "blocked", "bloccato",
           "revoked", "revocato", "unpaid", "insoluto", "disabled", "disattivo"}


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
def _license_url(dealer: dict[str, Any] | None) -> str:
    if dealer:
        u = (dealer.get("license_url") or "").strip()
        if u:
            return u
    return (os.environ.get("LICENSE_URL") or "").strip()


def _dealer_id(dealer: dict[str, Any] | None) -> str:
    if not dealer:
        return ""
    # il config del dealer usa la chiave "dealer_id" (es. "novacar")
    return str(dealer.get("dealer_id") or dealer.get("id")
               or dealer.get("display_name") or "").strip().lower()


def _cache_path() -> Path:
    """File di cache in una cartella SCRIVIBILE (accanto a runs/, quindi accanto all'exe)."""
    try:
        import common
        return common.RUNS_DIR.parent / CACHE_NAME
    except Exception:
        return Path(__file__).resolve().parent.parent / CACHE_NAME


# --------------------------------------------------------------------------- #
# Parsing stato
# --------------------------------------------------------------------------- #
def _status_for(data: Any, did: str) -> str | None:
    """Estrae lo stato del dealer dal JSON (supporta i due formati). None = non elencato."""
    if not isinstance(data, dict):
        return None
    dealers = data.get("dealers") if isinstance(data.get("dealers"), dict) else data
    if not isinstance(dealers, dict):
        return None
    val = dealers.get(did)
    if isinstance(val, dict):
        return str(val.get("status") or "").strip().lower()
    if val is None:
        return None
    return str(val).strip().lower()


def _read_cache(did: str) -> str | None:
    try:
        data = json.loads(_cache_path().read_text(encoding="utf-8"))
        entry = data.get(did)
        if isinstance(entry, dict):
            return str(entry.get("status") or "").strip().lower()
    except Exception:
        pass
    return None


def _write_cache(did: str, status: str) -> None:
    try:
        p = _cache_path()
        data: dict[str, Any] = {}
        if p.exists():
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                data = {}
        data[did] = {"status": status, "at": int(time.time())}
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass


# --------------------------------------------------------------------------- #
# API pubblica
# --------------------------------------------------------------------------- #
def check_license(dealer: dict[str, Any] | None) -> tuple[bool, str]:
    """Ritorna (consenti: bool, messaggio: str). Non solleva mai eccezioni."""
    url = _license_url(dealer)
    did = _dealer_id(dealer)
    if not url:
        return True, "licenza: nessun controllo configurato (LICENSE_URL assente)"
    if not did:
        return True, "licenza: dealer senza id, controllo saltato"

    status: str | None = None
    reachable = False
    try:
        import requests
        r = requests.get(url, timeout=TIMEOUT_S, headers={"Cache-Control": "no-cache"})
        if r.status_code == 200:
            reachable = True
            status = _status_for(r.json(), did)
    except Exception:
        reachable = False

    if reachable:
        s = status if status is not None else "active"  # non elencato ma URL ok = consentito
        _write_cache(did, s)
        if s in BLOCKED:
            return False, (f"Abbonamento SOSPESO per '{did}'. "
                           f"Contatta il fornitore per riattivare il servizio.")
        return True, f"licenza ok ({s or 'active'})"

    # URL non raggiungibile → grace con cache (non blocco chi paga per colpa della rete)
    cached = _read_cache(did)
    if cached in BLOCKED:
        return False, (f"Abbonamento SOSPESO per '{did}' (ultimo stato conosciuto). "
                       f"Contatta il fornitore per riattivare.")
    return True, "licenza: stato online non raggiungibile, consentito (grace/cache)"
