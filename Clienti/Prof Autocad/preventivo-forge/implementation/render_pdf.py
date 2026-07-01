"""
render_pdf.py — S5 Render PDF preventivo (Half B / Gael).

Compone `listing_it.json` (content di Gael + price di Max) in un PDF professionale via
template Jinja2 (`templates/preventivo.html`). Le foto sono già scaricate in locale
(runs/<id>/foto/) e vengono INCORPORATE in base64 (mai hotlink — Gate D).

Contratto (HANDOFF-GAEL.md):  render(ctx, dealer) -> pathlib.Path

Motore PDF (self-healing, agnostico):
  1) Playwright (Chromium headless, page.pdf) — robusto su Windows, già dipendenza Half A.
  2) WeasyPrint — fallback se Playwright assente.
Se nessuno è disponibile, salva l'HTML e alza un errore con istruzioni chiare.
"""
from __future__ import annotations

import base64
import io
from pathlib import Path
from typing import Any

from common import RunContext, load_json, slugify

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
ACCENT = "#c8102e"  # rosso sobrio; sovrascrivibile da dealer.preventivo.accent_color

COVER_MAX_W = 1400
GALLERY_MAX_W = 800
LOGO_MAX_W = 400


# --------------------------------------------------------------------------- #
# Entry point (chiamato da run.py dopo S4)
# --------------------------------------------------------------------------- #
def render(ctx: RunContext, dealer: dict[str, Any]) -> Path:
    listing = load_json(ctx.listing_path)
    listing_it = load_json(ctx.listing_it_path) if ctx.listing_it_path.exists() else {}
    content = listing_it.get("content") or {}
    price = listing_it.get("price") or {}
    prev = (dealer.get("preventivo") or {})

    html = _render_html(ctx, listing, content, price, dealer, prev)

    make_model = f"{listing.get('make') or ''}-{listing.get('model') or 'auto'}"
    out_path = ctx.dir / f"preventivo_{slugify(make_model)}.pdf"

    engine = _html_to_pdf(html, out_path, ctx)
    ctx.logger.info("S5 PDF render: %s (motore=%s, %d KB).",
                    out_path.name, engine, out_path.stat().st_size // 1024 if out_path.exists() else 0)
    return out_path


# --------------------------------------------------------------------------- #
# HTML
# --------------------------------------------------------------------------- #
def _render_html(ctx: RunContext, listing: dict, content: dict, price: dict,
                 dealer: dict, prev: dict) -> str:
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("preventivo.html")

    images = listing.get("images") or []
    cover_uri = _image_data_uri(_resolve_image(ctx, images[0]) if images else None, COVER_MAX_W)
    gallery = [
        uri for uri in (
            _image_data_uri(_resolve_image(ctx, img), GALLERY_MAX_W) for img in images[:9]
        ) if uri
    ]
    logo_uri = _image_data_uri(_resolve_logo(dealer), LOGO_MAX_W)

    breakdown = price.get("breakdown") or {}
    bd_view = None
    if breakdown:
        bd_view = {
            "listed": _eur(breakdown.get("listed_eur")),
            "pct": _num(breakdown.get("surcharge_pct")),
            "surcharge": _eur(breakdown.get("surcharge_eur")),
            "fixed": _eur((breakdown.get("fixed_1_eur") or 0) + (breakdown.get("fixed_2_eur") or 0)),
        }

    ctx_data = {
        "accent": dealer.get("preventivo", {}).get("accent_color", ACCENT),
        "dealer_name": dealer.get("display_name") or "Concessionaria",
        "contacts": dealer.get("contacts") or {},
        "logo_data_uri": logo_uri,
        "title": content.get("title_it") or _fallback_title(listing),
        "headline": content.get("headline_it"),
        "price_display": _price_display(price),
        "cover_data_uri": cover_uri,
        "specs": content.get("specs_it") or {},
        "highlights": content.get("highlights_it") or [],
        "description": content.get("description_it") or "",
        "equipment": content.get("equipment_it") or [],
        "gallery": gallery,
        "show_breakdown": bool(prev.get("show_price_breakdown_to_customer")),
        "breakdown": bd_view,
        "validity_days": prev.get("validity_days"),
        "footer_note": prev.get("footer_note") or "",
        "generated_at": (listing_it_gen := listing.get("scraped_at")) and listing_it_gen[:10],
    }
    return template.render(**ctx_data)


# --------------------------------------------------------------------------- #
# Immagini → data URI (con normalizzazione Pillow)
# --------------------------------------------------------------------------- #
def _resolve_image(ctx: RunContext, img: dict | None) -> Path | None:
    if not img:
        return None
    lp = img.get("local_path")
    if not lp:
        return None
    p = ctx.dir / lp
    return p if p.exists() else None


def _resolve_logo(dealer: dict) -> Path | None:
    logo = dealer.get("logo_path")
    ddir = dealer.get("_dir")
    if not logo or not ddir:
        return None
    p = Path(ddir) / logo
    return p if p.exists() else None


def _image_data_uri(path: Path | None, max_w: int) -> str | None:
    if not path or not path.exists():
        return None
    try:
        from PIL import Image

        with Image.open(path) as im:
            im = im.convert("RGB")
            if im.width > max_w:
                ratio = max_w / float(im.width)
                im = im.resize((max_w, int(im.height * ratio)), Image.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, format="JPEG", quality=82, optimize=True)
            data = buf.getvalue()
        return "data:image/jpeg;base64," + base64.b64encode(data).decode("ascii")
    except Exception:
        # fallback: incorpora i byte grezzi senza normalizzazione
        try:
            raw = path.read_bytes()
            suffix = path.suffix.lower().lstrip(".") or "jpeg"
            mime = "jpeg" if suffix in ("jpg", "jpeg") else suffix
            return f"data:image/{mime};base64," + base64.b64encode(raw).decode("ascii")
        except Exception:
            return None


# --------------------------------------------------------------------------- #
# HTML → PDF (Playwright preferito, WeasyPrint fallback)
# --------------------------------------------------------------------------- #
def _html_to_pdf(html: str, out_path: Path, ctx: RunContext) -> str:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # 1) Playwright
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_content(html, wait_until="load")
            page.pdf(
                path=str(out_path),
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            browser.close()
        return "playwright"
    except Exception as exc:  # noqa: BLE001
        ctx.logger.warning("Playwright PDF non disponibile (%s), provo WeasyPrint...", exc)

    # 2) WeasyPrint
    try:
        from weasyprint import HTML  # type: ignore

        HTML(string=html).write_pdf(str(out_path))
        return "weasyprint"
    except Exception as exc:  # noqa: BLE001
        # salva l'HTML per non perdere il lavoro e alza errore azionabile
        html_path = out_path.with_suffix(".html")
        html_path.write_text(html, encoding="utf-8")
        raise RuntimeError(
            f"Nessun motore PDF disponibile. HTML salvato in {html_path}. "
            f"Installa Playwright (`pip install playwright && playwright install chromium`) "
            f"oppure WeasyPrint con le librerie GTK. Dettaglio: {exc}"
        ) from exc


# --------------------------------------------------------------------------- #
# Formattazione
# --------------------------------------------------------------------------- #
def _price_display(price: dict) -> str:
    final = price.get("final_eur")
    if final in (None, ""):
        return "Prezzo su richiesta"
    return f"{_eur(final)} €"


def _eur(n: Any) -> str:
    try:
        return f"{int(round(float(n))):,}".replace(",", ".")
    except (TypeError, ValueError):
        return "—"


def _num(n: Any) -> str:
    try:
        f = float(n)
        return str(int(f)) if f.is_integer() else str(f)
    except (TypeError, ValueError):
        return str(n)


def _fallback_title(listing: dict) -> str:
    name = " ".join(str(p) for p in (listing.get("make"), listing.get("model"),
                                     listing.get("variant")) if p)
    return " ".join(name.split()).strip() or "Autovettura"
