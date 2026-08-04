"""
parser.py — S2 Normalizzazione (Half A / Max).

Trasforma raw.json (output dello scraper) nel contratto canonico listing.json
conforme a schema/listing.schema.json.

Priorità fonti: JSON-LD (Car/Vehicle/Product) -> DOM attributes -> meta.
Normalizza SOLO dati strutturali (numeri, enum tecniche DE->IT). La traduzione di
prosa/optional (equipment_de) NON si tocca qui: resta in tedesco per Half B (Gael).
"""
from __future__ import annotations

import re
from typing import Any

from common import RunContext, load_json, save_json, source_id_from_url, validate_against_schema

# --- mappe enum strutturali DE -> IT ---------------------------------------
FUEL_MAP = {
    "diesel": "Diesel", "benzin": "Benzina", "elektro": "Elettrica",
    "hybrid": "Ibrida", "plug-in-hybrid": "Ibrida Plug-in", "autogas": "GPL",
    "lpg": "GPL", "erdgas": "Metano", "cng": "Metano", "wasserstoff": "Idrogeno",
    "gasoline": "Benzina", "petrol": "Benzina", "electric": "Elettrica",
}
GEARBOX_MAP = {
    "schaltgetriebe": "Manuale", "manuell": "Manuale", "manual": "Manuale",
    "automatik": "Automatico", "automatic": "Automatico",
    "halbautomatik": "Semiautomatico", "automatisiert": "Automatizzato",
}
DRIVE_MAP = {
    "allrad": "Integrale", "4x4": "Integrale", "vorderrad": "Anteriore",
    "front": "Anteriore", "hinterrad": "Posteriore", "heck": "Posteriore",
}


# --------------------------------------------------------------------------- #
def parse(ctx: RunContext) -> dict[str, Any]:
    raw = load_json(ctx.raw_path)
    warnings: list[str] = list(raw.get("warnings", []))

    car = _pick_car_jsonld(raw.get("jsonld", []))
    attrs = raw.get("dom", {}).get("attributes", {}) or {}
    dom = raw.get("dom", {}) or {}

    listing: dict[str, Any] = {
        "source_url": raw.get("source_url"),
        "source_id": source_id_from_url(raw.get("source_url", "")),
        "scraped_at": raw.get("scraped_at"),
        "scrape_method": raw.get("scrape_method", "playwright"),
        "make": None, "model": None, "variant": None, "title_de": dom.get("title"),
        "year": None, "first_registration": None, "mileage_km": None,
        "price_listed_eur": None, "price_is_gross": None, "vat_deductible": None,
        "fuel": None, "gearbox": None, "power_kw": None, "power_hp": None,
        "body_type": None, "drivetrain": None, "doors": None, "seats": None,
        "color": None, "color_manufacturer": None, "interior": None,
        "emission_class": None, "co2_g_km": None, "vin": None,
        "equipment_de": [], "description_de": "",
        "raw_specs": {}, "seller": {}, "images": [], "warnings": warnings,
    }

    ad = raw.get("initial_state_ad")
    if ad:
        _from_initial_state(listing, ad)          # dati veri mobile.de (primario)
    else:
        _from_jsonld(listing, car)                # fallback
        _from_dom_attributes(listing, attrs)
    _finalize(listing, raw, dom, warnings)

    save_json(ctx.listing_path, listing)
    errs = validate_against_schema(listing, "listing.schema.json")
    if errs:
        ctx.logger.error("listing.json NON valido:\n - %s", "\n - ".join(errs))
    else:
        ctx.logger.info("listing.json valido. marca=%s modello=%s prezzo=%s",
                        listing["make"], listing["model"], listing["price_listed_eur"])
    listing["_schema_errors"] = errs  # informativo per il conductor (non parte del contratto)
    return listing


# --------------------------------------------------------------------------- #
def _from_initial_state(listing: dict, ad: dict) -> None:
    """Mappa il record REALE mobile.de (window.__INITIAL_STATE__ .ad) sullo schema."""
    import html as _html

    listing["make"] = ad.get("make") or listing["make"]
    listing["model"] = ad.get("model") or listing["model"]
    listing["title_de"] = ad.get("title") or ad.get("shortTitle") or listing["title_de"]

    price = ad.get("price") or {}
    if price.get("grossAmount") is not None:
        listing["price_listed_eur"] = float(price["grossAmount"])
        listing["price_is_gross"] = True
    if price.get("vat"):
        listing["vat_deductible"] = "mwst" in str(price["vat"]).lower()

    attrs = {a.get("tag"): a.get("value") for a in ad.get("attributes", []) if a.get("tag")}
    if "mileage" in attrs:
        listing["mileage_km"] = _to_int(attrs["mileage"])
    if "fuel" in attrs:
        listing["fuel"] = _norm(FUEL_MAP, attrs["fuel"])
    if "transmission" in attrs:
        listing["gearbox"] = _norm(GEARBOX_MAP, attrs["transmission"])
    if "numSeats" in attrs:
        listing["seats"] = _to_int(attrs["numSeats"])
    if "doorCount" in attrs:
        nums = re.findall(r"\d+", str(attrs["doorCount"]))
        if nums:
            listing["doors"] = int(nums[-1])
    if "color" in attrs:
        listing["color"] = attrs["color"]
    if "manufacturerColorName" in attrs:
        listing["color_manufacturer"] = attrs["manufacturerColorName"]
    if "interior" in attrs:
        listing["interior"] = attrs["interior"]
    if "emissionClass" in attrs:
        listing["emission_class"] = attrs["emissionClass"]
    if "category" in attrs:
        listing["body_type"] = str(attrs["category"]).split(",")[0].strip()
    if "trimLine" in attrs and not listing.get("variant"):
        listing["variant"] = str(attrs["trimLine"]).strip()
    if "firstRegistration" in attrs:
        listing["first_registration"] = attrs["firstRegistration"]
        y = re.search(r"(19|20)\d{2}", str(attrs["firstRegistration"]))
        if y:
            listing["year"] = int(y.group(0))
    if "power" in attrs:
        kw = re.search(r"(\d+)\s*kW", str(attrs["power"]))
        ps = re.search(r"(\d+)\s*PS", str(attrs["power"]))
        if kw:
            listing["power_kw"] = int(kw.group(1))
        if ps:
            listing["power_hp"] = int(ps.group(1))
    co2 = attrs.get("envkv.co2Emissions") or attrs.get("co2Emissions")
    if co2:
        listing["co2_g_km"] = _to_float(co2)

    feats = [f for f in (ad.get("features") or []) if isinstance(f, str)]
    listing["equipment_de"] = feats
    if any("allrad" in f.lower() for f in feats):
        listing["drivetrain"] = "Integrale"

    desc = ad.get("htmlDescription") or ""
    desc = re.sub(r"(?i)<br\s*/?>", "\n", desc)
    desc = re.sub(r"(?i)</(p|li|ul|ol|div|h\d|tr)>", "\n", desc)
    desc = re.sub(r"<[^>]+>", " ", desc)
    desc = _html.unescape(desc)
    desc = re.sub(r"[ \t]+", " ", desc)
    listing["description_de"] = re.sub(r"\n{3,}", "\n\n", desc).strip()

    def _scalar(v):
        if isinstance(v, (list, tuple)):
            return "; ".join(str(x) for x in v)
        if isinstance(v, dict):
            return "; ".join(f"{k}: {x}" for k, x in v.items())
        return v
    listing["raw_specs"] = {a.get("label"): _scalar(a.get("value"))
                            for a in ad.get("attributes", []) if a.get("label")}


# --------------------------------------------------------------------------- #
def _pick_car_jsonld(blocks: list[dict]) -> dict:
    pref = ("car", "vehicle", "product")
    for want in pref:
        for b in blocks:
            t = b.get("@type", "")
            types = t if isinstance(t, list) else [t]
            if any(want == str(x).lower() for x in types):
                return b
    return blocks[0] if blocks else {}


def _from_jsonld(listing: dict, car: dict) -> None:
    if not car:
        return
    brand = car.get("brand")
    if isinstance(brand, dict):
        listing["make"] = brand.get("name") or listing["make"]
    elif isinstance(brand, str):
        listing["make"] = brand
    listing["model"] = car.get("model") or listing["model"]
    if car.get("name"):
        listing["title_de"] = listing["title_de"] or car["name"]
    if car.get("description"):
        listing["description_de"] = car["description"]
    if car.get("color"):
        listing["color"] = car["color"]
    if car.get("vehicleIdentificationNumber"):
        listing["vin"] = car["vehicleIdentificationNumber"]

    listing["doors"] = _to_int(car.get("numberOfDoors")) or listing["doors"]
    listing["seats"] = _to_int(car.get("vehicleSeatingCapacity")) or listing["seats"]

    odo = car.get("mileageFromOdometer")
    if isinstance(odo, dict):
        listing["mileage_km"] = _to_int(odo.get("value")) or listing["mileage_km"]
    else:
        listing["mileage_km"] = _to_int(odo) or listing["mileage_km"]

    listing["fuel"] = _norm(FUEL_MAP, car.get("fuelType")) or listing["fuel"]
    listing["gearbox"] = _norm(GEARBOX_MAP, car.get("vehicleTransmission")) or listing["gearbox"]

    eng = car.get("vehicleEngine")
    if isinstance(eng, dict):
        power = eng.get("enginePower")
        if isinstance(power, dict):
            val = _to_int(power.get("value"))
            unit = str(power.get("unitText", "")).lower()
            if "ps" in unit or "hp" in unit:
                listing["power_hp"] = val
            else:
                listing["power_kw"] = val

    reg = car.get("dateVehicleFirstRegistered") or car.get("productionDate") or car.get("vehicleModelDate")
    if reg:
        listing["first_registration"] = str(reg)
        y = re.search(r"(19|20)\d{2}", str(reg))
        if y:
            listing["year"] = int(y.group(0))

    offers = car.get("offers")
    if isinstance(offers, list):
        offers = offers[0] if offers else {}
    if isinstance(offers, dict):
        listing["price_listed_eur"] = _to_float(offers.get("price")) or listing["price_listed_eur"]


def _from_dom_attributes(listing: dict, attrs: dict) -> None:
    def g(*labels: str) -> str | None:
        for k, v in attrs.items():
            kl = k.lower()
            if any(lbl.lower() in kl for lbl in labels):
                return v
        return None

    listing["first_registration"] = listing["first_registration"] or g("Erstzulassung")
    if listing["first_registration"] and not listing["year"]:
        y = re.search(r"(19|20)\d{2}", listing["first_registration"])
        if y:
            listing["year"] = int(y.group(0))
    listing["mileage_km"] = listing["mileage_km"] or _to_int(g("Kilometerstand"))
    listing["fuel"] = listing["fuel"] or _norm(FUEL_MAP, g("Kraftstoff"))
    listing["gearbox"] = listing["gearbox"] or _norm(GEARBOX_MAP, g("Getriebe"))
    listing["drivetrain"] = listing["drivetrain"] or _norm(DRIVE_MAP, g("Antriebsart"))
    listing["body_type"] = listing["body_type"] or g("Fahrzeugtyp", "Kategorie")
    listing["doors"] = listing["doors"] or _to_int(g("Türen"))
    listing["seats"] = listing["seats"] or _to_int(g("Sitzplätze"))
    listing["color"] = listing["color"] or g("Außenfarbe", "Farbe")
    listing["color_manufacturer"] = listing["color_manufacturer"] or g("Herstellerfarbe")
    listing["interior"] = listing["interior"] or g("Innenausstattung", "Polsterung")
    listing["emission_class"] = listing["emission_class"] or g("Schadstoffklasse", "Emissionsklasse")
    listing["co2_g_km"] = listing["co2_g_km"] or _to_float(g("CO2"))
    listing["vin"] = listing["vin"] or g("Identifizierungsnummer", "FIN")
    if not listing["make"]:
        listing["make"] = g("Marke")
    if not listing["model"]:
        listing["model"] = g("Modell")

    power = g("Leistung")
    if power:
        kw = re.search(r"(\d+)\s*kW", power)
        ps = re.search(r"(\d+)\s*PS", power)
        if kw and not listing["power_kw"]:
            listing["power_kw"] = int(kw.group(1))
        if ps and not listing["power_hp"]:
            listing["power_hp"] = int(ps.group(1))

    # conserva tutta la scheda grezza per audit
    listing["raw_specs"] = {k: v for k, v in attrs.items()}


def _finalize(listing: dict, raw: dict, dom: dict, warnings: list[str]) -> None:
    # prezzo da testo se JSON-LD non l'ha dato
    if not listing["price_listed_eur"] and dom.get("price_text"):
        listing["price_listed_eur"] = _to_float(dom["price_text"])
    # potenza derivata
    if listing["power_kw"] and not listing["power_hp"]:
        listing["power_hp"] = round(listing["power_kw"] * 1.35962)
    if listing["power_hp"] and not listing["power_kw"]:
        listing["power_kw"] = round(listing["power_hp"] / 1.35962)
    # equipment + descrizione
    if not listing["equipment_de"]:
        listing["equipment_de"] = dom.get("equipment", []) or []
    if not listing["description_de"]:
        listing["description_de"] = dom.get("description") or ""
    # marca/modello da titolo se mancano
    if (not listing["make"] or not listing["model"]) and listing.get("title_de"):
        parts = listing["title_de"].split()
        if not listing["make"] and parts:
            listing["make"] = parts[0]
        if not listing["model"] and len(parts) > 1:
            listing["model"] = parts[1]
    # variant: residuo del titolo dopo marca+modello
    if not listing["variant"] and listing.get("title_de") and listing["make"] and listing["model"]:
        tail = listing["title_de"]
        for token in (listing["make"], listing["model"]):
            tail = tail.replace(token, "", 1)
        tail = tail.strip(" -,")
        listing["variant"] = tail or None
    # immagini
    listing["images"] = raw.get("images", [])
    # guardie
    if not listing["price_listed_eur"]:
        warnings.append("price_listed_eur mancante: il pricing non potrà calcolare il prezzo finale")
    if not listing["images"]:
        warnings.append("nessuna immagine: il PDF non avrà gallery")
    if not listing["description_de"]:
        warnings.append("description_de vuota")


# --------------------------------------------------------------------------- #
def _norm(table: dict[str, str], value: Any) -> str | None:
    if not value:
        return None
    v = str(value).strip().lower()
    for key, out in table.items():
        if key in v:
            return out
    return str(value).strip()  # valore originale se non mappato


def _to_int(value: Any) -> int | None:
    f = _to_float(value)
    return int(round(f)) if f is not None else None


def _to_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value)
    # rimuove valuta/unità, tiene cifre e separatori
    s = re.sub(r"[^\d.,]", "", s)
    if not s:
        return None
    # formato tedesco: '.' migliaia, ',' decimali
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    else:
        # singolo punto: se sembra separatore migliaia (es. 28.900) rimuovilo
        if re.match(r"^\d{1,3}\.\d{3}$", s):
            s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None
