#!/usr/bin/env python3
"""
run.py — Regia (conductor) di PreventivoForge. Half A / Max.

Pipeline: URL annuncio mobile.de (DE) -> preventivo italiano (PDF), prezzo finale nel titolo,
per una concessionaria specifica (multi-tenant).

Uso:
  python run.py <url-mobile.de>                         # live (Playwright), dealer default
  python run.py <url> --dealer prof-autocad             # sceglie la concessionaria
  python run.py <url> --manual annuncio.html --foto ./foto   # fallback senza scraping
  python run.py --list-dealers

Half B (Gael) = S3 traduzione+copy e S5 PDF + QA. Finché i suoi moduli non esistono,
la regia esegue S1+S2+S4 e si ferma con una nota di handoff (NON è un errore).
"""
from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

# rende importabili i moduli in implementation/
sys.path.insert(0, str(Path(__file__).resolve().parent / "implementation"))

from common import RunContext  # noqa: E402
import dealers as dealers_mod  # noqa: E402
import scraper  # noqa: E402
import parser as parser_mod  # noqa: E402
import pricer  # noqa: E402


def _optional(module_name: str):
    """Importa un modulo di Half B se presente, altrimenti None."""
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description="PreventivoForge — mobile.de (DE) -> preventivo IT (PDF)")
    ap.add_argument("url", nargs="?", help="URL annuncio mobile.de")
    ap.add_argument("--dealer", default=None, help="ID concessionaria (default: prof-autocad)")
    ap.add_argument("--manual", metavar="HTML", help="HTML salvato dell'annuncio (fallback no-scraping)")
    ap.add_argument("--foto", metavar="DIR", help="cartella foto (con --manual)")
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--list-dealers", action="store_true")
    args = ap.parse_args()

    if args.list_dealers:
        print("Concessionarie:", ", ".join(dealers_mod.list_dealers()) or "(nessuna)")
        return 0
    if not args.url and not args.manual:
        ap.error("serve <url> oppure --manual <html>")

    dealer = dealers_mod.load_dealer(args.dealer)
    url = args.url or f"file://{Path(args.manual).resolve()}"
    ctx = RunContext(url, run_id=args.run_id)
    ctx.logger.info("=== PreventivoForge run %s | dealer=%s ===", ctx.run_id, dealer["display_name"])

    # ---- S1 SCRAPING -------------------------------------------------------
    ctx.set_step("S1_scraping", "running")
    try:
        if args.manual:
            scraper.scrape_manual(ctx, args.manual, args.foto)
        else:
            scraper.scrape(ctx)
        ctx.set_step("S1_scraping", "done")
    except Exception as exc:  # noqa: BLE001
        ctx.set_step("S1_scraping", "failed", str(exc))
        ctx.logger.error("S1 fallito: %s", exc)
        return 2

    # ---- S2 PARSING --------------------------------------------------------
    ctx.set_step("S2_parsing", "running")
    listing = parser_mod.parse(ctx)
    schema_errs = listing.get("_schema_errors") or []
    ctx.set_step("S2_parsing", "done" if not schema_errs else "warning",
                 "; ".join(schema_errs[:3]))

    # ---- GATE A (estrazione) ----------------------------------------------
    if not _gate_extraction(ctx, listing):
        ctx.set_step("GATE_A_extraction", "blocked", "estrazione incompleta")
        ctx.logger.error("GATE A rosso: estrazione incompleta. Stop.")
        return 3
    ctx.set_step("GATE_A_extraction", "passed")

    # ---- S3 TRANSLATE+COPY (Half B / Gael, opzionale) ----------------------
    translate = _optional("translate_copy")
    if translate and hasattr(translate, "translate"):
        ctx.set_step("S3_translate_copy", "running")
        translate.translate(ctx, dealer)
        ctx.set_step("S3_translate_copy", "done")
    else:
        ctx.set_step("S3_translate_copy", "skipped", "Half B non presente (handoff Gael)")

    # ---- S4 PRICING (Half A / Max) ----------------------------------------
    ctx.set_step("S4_pricing", "running")
    try:
        price_block = pricer.price(ctx, dealer)
        ctx.set_step("S4_pricing", "done", price_block["final_title"])
    except Exception as exc:  # noqa: BLE001
        ctx.set_step("S4_pricing", "failed", str(exc))
        ctx.logger.error("S4 fallito: %s", exc)
        return 4

    # ---- S5 PDF RENDER (Half B / Gael, opzionale) -------------------------
    render = _optional("render_pdf")
    if render and hasattr(render, "render"):
        ctx.set_step("S5_pdf_render", "running")
        pdf_path = render.render(ctx, dealer)
        ctx.set_step("S5_pdf_render", "done", str(pdf_path))
        print(f"\n✅ Preventivo PDF: {pdf_path}")
    else:
        ctx.set_step("S5_pdf_render", "skipped", "Half B non presente (handoff Gael)")
        _print_handoff_note(ctx)

    print(f"\nRun completata: {ctx.dir}")
    print(f"  listing.json     -> {ctx.listing_path}")
    print(f"  listing_it.json  -> {ctx.listing_it_path}")
    return 0


def _gate_extraction(ctx: RunContext, listing: dict) -> bool:
    """Gate A minimo (built-in). Il QA completo è di Half B (qa-extraction-verifier)."""
    ok = True
    if not listing.get("price_listed_eur"):
        ctx.logger.error("Gate A: price_listed_eur mancante."); ok = False
    if not listing.get("images"):
        ctx.logger.error("Gate A: nessuna foto."); ok = False
    if not listing.get("make") or not listing.get("model"):
        ctx.logger.warning("Gate A: marca/modello incompleti (non bloccante).")
    return ok


def _print_handoff_note(ctx: RunContext) -> None:
    print(
        "\nℹ️  Half B (Gael) non ancora collegata: prodotti dati + prezzo, manca il PDF preventivo.\n"
        "   Mancano: implementation/translate_copy.py (S3), implementation/render_pdf.py (S5),\n"
        "   implementation/qa_gate.py (gate B/C/D). Vedi HANDOFF-GAEL.md."
    )


if __name__ == "__main__":
    raise SystemExit(main())
