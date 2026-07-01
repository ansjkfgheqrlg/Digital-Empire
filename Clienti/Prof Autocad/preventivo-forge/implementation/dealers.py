"""
dealers.py — Multi-tenant (Half A / Max).

Carica la configurazione di una concessionaria da concessionarie/<dealer_id>/config.json.
Permette al workflow di servire MOLTE concessionarie con regole prezzo, logo, contatti
e impostazioni preventivo diverse. Prima concessionaria: prof-autocad.

I parametri prezzo nel config del dealer hanno PRIORITÀ sui default di .env.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from common import PROJECT_ROOT, load_config, load_json

DEALERS_DIR = PROJECT_ROOT / "concessionarie"
DEFAULT_DEALER = "prof-autocad"


def list_dealers() -> list[str]:
    if not DEALERS_DIR.exists():
        return []
    return sorted(p.name for p in DEALERS_DIR.iterdir() if (p / "config.json").exists())


def load_dealer(dealer_id: str | None = None) -> dict[str, Any]:
    """Ritorna il config della concessionaria, con prezzo risolto (dealer > .env)."""
    dealer_id = dealer_id or DEFAULT_DEALER
    cfg_path = DEALERS_DIR / dealer_id / "config.json"
    if not cfg_path.exists():
        raise FileNotFoundError(
            f"Concessionaria '{dealer_id}' non trovata in {DEALERS_DIR}. "
            f"Disponibili: {', '.join(list_dealers()) or '(nessuna)'}"
        )
    dealer = load_json(cfg_path)
    dealer["_dir"] = str(cfg_path.parent)

    env = load_config()
    pricing = dealer.get("pricing", {}) or {}
    dealer["pricing_resolved"] = {
        "surcharge_pct": float(pricing.get("surcharge_pct", env["price_surcharge_pct"])),
        "fixed_1": float(pricing.get("fixed_1", env["price_fixed_1"])),
        "fixed_2": float(pricing.get("fixed_2", env["price_fixed_2"])),
    }
    return dealer
