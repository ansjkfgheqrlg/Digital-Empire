"""
qa_gate.py — Gate di qualità A/B/C/D (Half B / Gael). Bloccanti.

Ogni gate è una funzione pura che ritorna (ok: bool, issues: list[str]).
Un gate rosso deve fermare la pipeline con messaggio chiaro (lo decide run.py / conductor).

Firme (HANDOFF-GAEL.md):
  gate_b(ctx) -> (bool, list)   traduzione
  gate_c(ctx) -> (bool, list)   prezzo (ricalcolo INDIPENDENTE)
  gate_d(ctx) -> (bool, list)   PDF finale
`dealer` è opzionale: se passato, i controlli diventano più forti (ricalcolo prezzo dai
parametri del dealer, re-render HTML per Gate D). run.py può chiamare gate_x(ctx, dealer).

Bonus: gate_a(ctx) — estrazione completa (motore dell'agente qa-extraction-verifier).
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from common import RunContext, load_json, validate_against_schema
from glossary_de_it import looks_german

MIN_PDF_BYTES = 20 * 1024
GALLERY_CAP = 9  # coerente con render_pdf (cover + fino a 9 in gallery)


# --------------------------------------------------------------------------- #
# GATE A — estrazione (bonus, indipendente dal check minimo di run.py)
# --------------------------------------------------------------------------- #
def gate_a(ctx: RunContext, dealer: dict[str, Any] | None = None) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not ctx.listing_path.exists():
        return False, ["listing.json assente (S2 non eseguito)"]
    listing = load_json(ctx.listing_path)

    errs = validate_against_schema(listing, "listing.schema.json")
    issues += [f"schema: {e}" for e in errs if not e.startswith("jsonschema non installato")]

    price = listing.get("price_listed_eur")
    if not isinstance(price, (int, float)) or price <= 0:
        issues.append(f"price_listed_eur non numerico/mancante: {price!r}")
    if not listing.get("make"):
        issues.append("make mancante")
    if not listing.get("model"):
        issues.append("model mancante")

    images = listing.get("images") or []
    if not images:
        issues.append("nessuna foto estratta")
    else:
        missing = [img.get("local_path") for img in images
                   if not (ctx.dir / (img.get("local_path") or "")).exists()]
        if missing:
            issues.append(f"{len(missing)} foto non presenti su disco: {missing[:3]}")
    if not (listing.get("description_de") or "").strip():
        issues.append("description_de vuota")
    return (not issues), issues


# --------------------------------------------------------------------------- #
# GATE B — traduzione
# --------------------------------------------------------------------------- #
def gate_b(ctx: RunContext, dealer: dict[str, Any] | None = None) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not ctx.listing_it_path.exists():
        return False, ["listing_it.json assente (S3 non eseguito)"]
    listing = load_json(ctx.listing_path)
    listing_it = load_json(ctx.listing_it_path)
    content = listing_it.get("content") or {}

    # campi obbligatori
    if not (content.get("title_it") or "").strip():
        issues.append("content.title_it mancante")
    if not (content.get("description_it") or "").strip():
        issues.append("content.description_it mancante")

    # allineamento optional 1:1
    eq_de = listing.get("equipment_de") or []
    eq_it = content.get("equipment_it") or []
    if len(eq_de) != len(eq_it):
        issues.append(f"equipment_it ({len(eq_it)}) non allineato 1:1 a equipment_de ({len(eq_de)})")

    # Tedesco residuo: BLOCCA solo se è nel TITOLO (imbarazzante) o è TANTO (traduzione rotta).
    # Un residuo minore in una riga optional (es. un morfema raro) → avviso, si consegna:
    # il PDF è italiano al 99%, non ha senso negare il preventivo per una parola in un optional.
    german = _german_tokens(content)
    if german:
        title_de = [t for t in re.findall(r"[A-Za-zÄÖÜäöüß-]+", content.get("title_it") or "")
                    if looks_german(t)]
        if title_de or len(german) > 3:
            issues.append(f"tedesco residuo significativo: {german[:8]}")
        else:
            ctx.logger.warning("Gate B: residuo tedesco minore (consegnato lo stesso): %s", german[:8])

    # niente prezzo nel titolo IT (il prezzo lo mette Max altrove)
    if re.search(r"\d[\d.\s]*€|€\s*\d", content.get("title_it") or ""):
        issues.append("title_it non deve contenere il prezzo")

    # numeri/specifiche invariati vs listing.json (no fatti alterati)
    issues += _specs_consistency(listing, content.get("specs_it") or {})

    # highlights nel range 0..6 (3-6 raccomandato; blocca solo se >6 fabbricati)
    if len(content.get("highlights_it") or []) > 6:
        issues.append("highlights_it > 6")
    return (not issues), issues


# --------------------------------------------------------------------------- #
# GATE C — prezzo (ricalcolo INDIPENDENTE)
# --------------------------------------------------------------------------- #
def gate_c(ctx: RunContext, dealer: dict[str, Any] | None = None) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not ctx.listing_it_path.exists():
        return False, ["listing_it.json assente"]
    listing = load_json(ctx.listing_path)
    listing_it = load_json(ctx.listing_it_path)
    price = listing_it.get("price") or {}
    if not price:
        return False, ["blocco price assente (S4 non eseguito)"]

    listed = listing.get("price_listed_eur")
    breakdown = price.get("breakdown") or {}

    # parametri: dal dealer se disponibile (davvero indipendente), altrimenti dal breakdown
    if dealer and dealer.get("pricing_resolved"):
        pr = dealer["pricing_resolved"]
        pct, f1, f2 = pr["surcharge_pct"], pr["fixed_1"], pr["fixed_2"]
    else:
        pct = breakdown.get("surcharge_pct")
        f1 = breakdown.get("fixed_1_eur")
        f2 = breakdown.get("fixed_2_eur")

    if listed in (None, "") or None in (pct, f1, f2):
        return False, [f"parametri prezzo incompleti: listed={listed}, pct={pct}, f1={f1}, f2={f2}"]

    recomputed = round(float(listed) * (1 + float(pct) / 100.0) + float(f1) + float(f2))
    declared = price.get("final_eur")
    if int(recomputed) != int(declared):
        issues.append(f"prezzo finale non riproducibile: ricalcolo={recomputed} vs dichiarato={declared}")

    # coerenza interna del breakdown
    if breakdown:
        surch = round(float(listed) * float(breakdown.get("surcharge_pct", 0)) / 100.0, 2)
        if abs(surch - float(breakdown.get("surcharge_eur", 0))) > 0.5:
            issues.append(f"surcharge_eur incoerente: {breakdown.get('surcharge_eur')} vs {surch}")

    # formato titolo: deve contenere il prezzo formattato + '€' e marca/modello
    title = price.get("final_title") or ""
    price_str = f"{int(declared):,}".replace(",", ".")
    if price_str not in title or "€" not in title:
        issues.append(f"final_title senza prezzo formattato corretto: {title!r} (atteso '{price_str} €')")
    if listing.get("make") and listing["make"].split()[0] not in title:
        issues.append(f"final_title senza marca: {title!r}")
    return (not issues), issues


# --------------------------------------------------------------------------- #
# GATE D — PDF finale
# --------------------------------------------------------------------------- #
def gate_d(ctx: RunContext, dealer: dict[str, Any] | None = None) -> tuple[bool, list[str]]:
    issues: list[str] = []
    listing = load_json(ctx.listing_path) if ctx.listing_path.exists() else {}
    listing_it = load_json(ctx.listing_it_path) if ctx.listing_it_path.exists() else {}
    content = listing_it.get("content") or {}
    price = listing_it.get("price") or {}

    # 1) PDF esiste e > 20KB
    pdfs = sorted(ctx.dir.glob("preventivo_*.pdf"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not pdfs:
        return False, ["nessun PDF preventivo_*.pdf in runs/<id>/"]
    pdf = pdfs[0]
    size = pdf.stat().st_size
    if size < MIN_PDF_BYTES:
        issues.append(f"PDF troppo piccolo ({size} byte < {MIN_PDF_BYTES})")

    # 2) sezioni/contenuto presenti
    if not (content.get("specs_it")):
        issues.append("scheda tecnica (specs_it) vuota")
    if not (content.get("description_it") or "").strip():
        issues.append("descrizione vuota")
    if not (content.get("equipment_it")):
        issues.append("dotazioni (equipment_it) vuote")

    # 3) prezzo nel titolo finale
    if not (price.get("final_title") and "€" in price["final_title"]):
        issues.append("final_title senza prezzo")

    # 4) foto: tutte quelle di listing.json presenti su disco (embed locale, no hotlink)
    images = listing.get("images") or []
    missing = [img.get("local_path") for img in images
               if not (ctx.dir / (img.get("local_path") or "")).exists()]
    if missing:
        issues.append(f"{len(missing)} foto mancanti su disco (gallery incompleta)")

    # 5) verifica profonda opzionale: re-render HTML, nessun placeholder, conteggio foto
    if dealer is not None:
        try:
            import render_pdf
            html = render_pdf._render_html(
                ctx, listing, content, price, dealer, dealer.get("preventivo") or {})
            if "{{" in html or "}}" in html:
                issues.append("placeholder Jinja non risolti nell'HTML")
            n_imgs = html.count("data:image/")
            expected = min(len(images), GALLERY_CAP) + (1 if images else 0) + \
                (1 if (dealer.get("logo_path") and (Path(dealer.get("_dir", "")) / dealer["logo_path"]).exists()) else 0)
            if images and n_imgs == 0:
                issues.append("nessuna immagine incorporata nell'HTML")
        except Exception as exc:  # noqa: BLE001
            issues.append(f"re-render HTML fallito: {exc}")
    return (not issues), issues


# --------------------------------------------------------------------------- #
# GATE IMG — immagini (R-09, agente qa-immagini)
# --------------------------------------------------------------------------- #
MIN_IMG_SIDE = 300  # px lato minimo accettabile


def gate_img(ctx: RunContext, dealer: dict[str, Any] | None = None) -> tuple[bool, list[str]]:
    """R-09: TUTTE le foto nel PDF, presenti su disco, risoluzione decente, MAI ritagliate."""
    issues: list[str] = []
    if not ctx.listing_path.exists():
        return False, ["listing.json assente"]
    listing = load_json(ctx.listing_path)
    images = listing.get("images") or []
    if not images:
        return False, ["nessuna foto nell'annuncio (R-09 richiede tutte le foto)"]

    # Qualità della SORGENTE (foto piccole/non scaricate/illeggibili) = NON è un difetto nostro:
    # si logga e si prosegue. Con 'contain' una foto piccola si vede INTERA (non stirata/tagliata).
    on_disk = 0
    for img in images:
        lp = img.get("local_path") or ""
        p = ctx.dir / lp
        if not p.exists():
            ctx.logger.warning("Gate IMG: foto non scaricata: %s (saltata)", lp)
            continue
        try:
            from PIL import Image
            with Image.open(p) as im:
                if min(im.size) < MIN_IMG_SIDE:
                    ctx.logger.warning("Gate IMG: foto %s piccola %s (caricata dal venditore) — inclusa intera",
                                       lp, im.size)
                on_disk += 1
        except Exception:
            ctx.logger.warning("Gate IMG: foto %s illeggibile (saltata)", lp)

    # BLOCCA solo su difetti VERI del nostro output: nessuna foto valida, PDF senza foto,
    # o foto senza 'fit' (rischio ritaglio). Il resto è qualità sorgente → si consegna.
    if on_disk == 0:
        return False, ["nessuna foto valida su disco (nessuna scaricata correttamente)"]
    if dealer is not None:
        try:
            import render_pdf
            listing_it = load_json(ctx.listing_it_path) if ctx.listing_it_path.exists() else {}
            html = render_pdf._render_html(ctx, listing, listing_it.get("content") or {},
                                           listing_it.get("price") or {}, dealer,
                                           dealer.get("preventivo") or {})
            n_in_pdf = html.count('class="photo-box"')
            if n_in_pdf == 0:
                issues.append("nessuna foto nel PDF")
            elif n_in_pdf < on_disk:
                ctx.logger.warning("Gate IMG: PDF con %d foto su %d disponibili (consegnato lo stesso)",
                                   n_in_pdf, on_disk)
            if "object-fit:" not in html:
                issues.append("foto senza 'fit' definito (rischio ritaglio)")
        except Exception as exc:  # noqa: BLE001
            issues.append(f"verifica render foto fallita: {exc}")
    return (not issues), issues


# --------------------------------------------------------------------------- #
# GATE R — regole sacre R-01…R-14 (agente qa-regole-checker)
# --------------------------------------------------------------------------- #
def gate_regole(ctx: RunContext, dealer: dict[str, Any] | None = None) -> tuple[bool, list[str]]:
    """Verifica le REGOLE-SACRE una per una sul PDF/HTML e scrive runs/<id>/regole-check.json.
    Richiede `dealer` per il re-render dell'HTML. Se assente, verifica solo il verificabile."""
    listing = load_json(ctx.listing_path) if ctx.listing_path.exists() else {}
    listing_it = load_json(ctx.listing_it_path) if ctx.listing_it_path.exists() else {}
    content = listing_it.get("content") or {}
    price = listing_it.get("price") or {}
    report: dict[str, dict[str, Any]] = {}

    html = ""
    if dealer is not None:
        try:
            import render_pdf
            html = render_pdf._render_html(ctx, listing, content, price, dealer,
                                           dealer.get("preventivo") or {})
        except Exception as exc:  # noqa: BLE001
            report["_render"] = {"pass": False, "note": f"re-render fallito: {exc}"}

    n_logo_only = html.count('class="page logo-only"')

    def rule(rid: str, ok: bool, note: str = "") -> None:
        report[rid] = {"pass": bool(ok), "note": note}

    rule("R-01", n_logo_only >= 1, "prima pagina solo logo")
    rule("R-02", 'class="logo-sm"' in html, "logo in ogni pagina di contenuto")
    company = (dealer or {}).get("legal") or {}
    rule("R-03", bool(company.get("vat")) and "P. IVA" in html and "PEC" in html, "dati azienda 2ª pagina")
    rule("R-04", bool((content.get("title_it") or "").strip()) and 'class="car-title"' in html, "titolo vettura")
    rule("R-05", "Scheda tecnica autovettura" in html, "scheda tecnica")
    rule("R-06", "Equipaggiamento principale" in html and bool(content.get("equipment_it")), "equipaggiamento")
    rule("R-07", "Condizioni di garanzia" in html, "condizioni di garanzia")
    rule("R-08", "Totale in strada (Iva inclusa)" in html and bool(price.get("final_eur")), "prezzo totale in strada")
    img_ok, img_issues = gate_img(ctx, dealer)
    rule("R-09", img_ok, "; ".join(img_issues) if img_issues else "immagini tutte/complete/non tagliate")
    rule("R-10", n_logo_only >= 2, "ultima pagina solo logo")
    b_ok, b_issues = gate_b(ctx, dealer)
    rule("R-11", b_ok, "; ".join(b_issues) if b_issues else "italiano, no tedesco, no invenzioni")
    c_ok, c_issues = gate_c(ctx, dealer)
    rule("R-12", c_ok and bool(listing.get("make")) and bool(listing.get("model")),
         "; ".join(c_issues) if c_issues else "prezzo verificato + dati coerenti")
    legal_name = (company.get("company") or "").strip()
    rule("R-13", bool(legal_name) and (legal_name in html), "dati/logo/colori dal config concessionaria")
    rule("R-14", all(v["pass"] for k, v in report.items() if k.startswith("R-") and k != "R-14"),
         "nessun elemento mancante")

    # scrive il report
    try:
        from common import save_json
        save_json(ctx.dir / "regole-check.json", report)
    except Exception:
        pass

    failed = [k for k, v in report.items() if k.startswith("R-") and not v["pass"]]
    issues = [f"{k}: {report[k]['note']}" for k in failed]
    return (not failed), issues


# --------------------------------------------------------------------------- #
# Runner comodo
# --------------------------------------------------------------------------- #
def run_all(ctx: RunContext, dealer: dict[str, Any] | None = None) -> dict[str, tuple[bool, list[str]]]:
    return {
        "A": gate_a(ctx, dealer),
        "B": gate_b(ctx, dealer),
        "C": gate_c(ctx, dealer),
        "D": gate_d(ctx, dealer),
        "IMG": gate_img(ctx, dealer),
        "R": gate_regole(ctx, dealer),
    }


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _german_tokens(content: dict[str, Any]) -> list[str]:
    found: list[str] = []
    fields = [content.get("title_it"), content.get("headline_it"), content.get("description_it")]
    for item in content.get("equipment_it", []) or []:
        fields.append(item)
    for h in content.get("highlights_it", []) or []:
        fields.append(h)
    for val in (content.get("specs_it") or {}).values():
        fields.append(val)
    for field in fields:
        for tok in re.findall(r"[A-Za-zÄÖÜäöüß-]+", str(field or "")):
            if looks_german(tok) and tok not in found:
                found.append(tok)
    return found


def _specs_consistency(listing: dict[str, Any], specs_it: dict[str, Any]) -> list[str]:
    """Verifica che i numeri chiave in specs_it corrispondano a listing.json."""
    issues: list[str] = []

    def digits(v: Any) -> str:
        s = str(v if v is not None else "")
        # numero "puro" (incluso float tipo "0.0"/"15000.0") → normalizza a intero:
        # evita il falso positivo "0.0"->"00" vs "0" (auto nuova a 0 km).
        if re.match(r"^\s*-?\d+(?:\.\d+)?\s*$", s):
            try:
                return str(int(float(s)))
            except Exception:
                pass
        return re.sub(r"\D", "", s)

    if "Anno" in specs_it and listing.get("year"):
        if str(specs_it["Anno"]) != str(listing["year"]):
            issues.append(f"specs Anno alterato: {specs_it['Anno']} vs {listing['year']}")
    if "Chilometraggio" in specs_it and listing.get("mileage_km") is not None:
        if digits(specs_it["Chilometraggio"]) != digits(listing["mileage_km"]):
            issues.append(f"specs Chilometraggio alterato: {specs_it['Chilometraggio']} vs {listing['mileage_km']}")
    if "Potenza" in specs_it and listing.get("power_hp"):
        if str(listing["power_hp"]) not in str(specs_it["Potenza"]):
            issues.append(f"specs Potenza alterata: {specs_it['Potenza']} vs {listing['power_hp']} CV")
    return issues
