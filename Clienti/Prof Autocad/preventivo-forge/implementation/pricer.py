"""
pricer.py — S4 Pricing (Half A / Max). Deterministico.

Formula (per-concessionaria): finale = round(esposto * (1 + pct/100) + fixed_1 + fixed_2)
Genera anche il titolo del preventivo con il prezzo finale.

Scrive la sezione "price" di listing_it.json (merge: NON sovrascrive "content" di Half B).
La stessa logica è ricalcolata in modo indipendente da qa-price-verifier (Half B / Gael).
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from common import RunContext, load_json, save_json


def compute_price(listed_eur: float, surcharge_pct: float,
                  fixed_1: float, fixed_2: float) -> dict[str, Any]:
    surcharge_eur = listed_eur * surcharge_pct / 100.0
    final = round(listed_eur + surcharge_eur + fixed_1 + fixed_2)
    return {
        "listed_eur": listed_eur,
        "surcharge_pct": surcharge_pct,
        "surcharge_eur": round(surcharge_eur, 2),
        "fixed_1_eur": fixed_1,
        "fixed_2_eur": fixed_2,
        "final_eur": int(final),
    }


def format_eur(n: int | float) -> str:
    """Formato italiano: 21540 -> '21.540'."""
    return f"{int(round(n)):,}".replace(",", ".")


def build_title(make: str | None, model: str | None, variant: str | None,
                final_eur: int) -> str:
    name = " ".join(p for p in (make, model, variant) if p).strip()
    name = " ".join(name.split())  # collassa spazi
    return f"{name} {format_eur(final_eur)} €".strip()


def price(ctx: RunContext, dealer: dict[str, Any]) -> dict[str, Any]:
    listing = load_json(ctx.listing_path)
    listed = listing.get("price_listed_eur")
    if not listed:
        raise ValueError(
            "price_listed_eur mancante in listing.json: impossibile calcolare il prezzo. "
            "Controllare estrazione (S1/S2)."
        )

    pr = dealer.get("pricing_resolved") or {}
    breakdown = compute_price(
        float(listed),
        surcharge_pct=pr.get("surcharge_pct", 3.0),
        fixed_1=pr.get("fixed_1", 1500.0),
        fixed_2=pr.get("fixed_2", 1500.0),
    )

    # titolo: usa il nome IT se Half B l'ha già prodotto, altrimenti i campi raw
    listing_it = load_json(ctx.listing_it_path) if ctx.listing_it_path.exists() else {}
    content = listing_it.get("content") or {}
    make = listing.get("make")
    model = listing.get("model")
    variant = listing.get("variant")
    final_title = build_title(make, model, variant, breakdown["final_eur"])

    price_block = {
        "listed_eur": breakdown["listed_eur"],
        "final_eur": breakdown["final_eur"],
        "final_title": final_title,
        "breakdown": breakdown,
    }

    merged = {
        "source_url": listing.get("source_url"),
        "source_id": listing.get("source_id"),
        "make": make, "model": model, "variant": variant,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "_meta": {**(listing_it.get("_meta") or {}), "price_by": "op-pricer (Max)"},
        "content": content,                # preservato (Half B)
        "price": price_block,              # prodotto qui (Half A)
    }
    save_json(ctx.listing_it_path, merged)
    ctx.logger.info("Prezzo: esposto=%s -> finale=%s | titolo: %s",
                    format_eur(listed), format_eur(breakdown["final_eur"]), final_title)
    return price_block
