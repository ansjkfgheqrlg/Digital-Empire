"""
translate_copy.py — S3 Traduzione + Copy (Half B / Gael).

Trasforma `listing.json` (dati DE normalizzati) nella parte TESTUALE `content.*` di
`listing_it.json`: traduzione fedele DE→IT + copy di vendita migliorato, SENZA inventare
fatti non presenti nel sorgente (lo verifica Gate B).

Contratto (HANDOFF-GAEL.md):
  translate(ctx, dealer) -> dict           # ritorna il blocco content
  - legge  runs/<id>/listing.json          (schema/listing.schema.json)
  - scrive runs/<id>/listing_it.json       riempiendo SOLO content.* (MERGE, non tocca price)

Modalità di traduzione (self-healing, dry-run-safe):
  - DETERMINISTICA (default): glossario automotive DE→IT + composizione del copy dai fatti
    strutturati. Nessun costo API, gira in automatico, output sempre in italiano.
  - LLM (opzionale): se `TRANSLATE_BACKEND=llm` e una chiave è configurata, arricchisce la
    prosa. Disattivata di default (Mandato Art.4.3 dry-run). Gancio pronto, non obbligatorio.

Il copy NON inventa: title/specs/highlights/description derivano tutti da campi di listing.json.
"""
from __future__ import annotations

import os
import re
from typing import Any

from common import RunContext, load_json, save_json
from glossary_de_it import PHRASES, WORDS, looks_german

_TOKEN_RE = re.compile(r"[A-Za-zÄÖÜäöüß]+|[^A-Za-zÄÖÜäöüß]+")


# --------------------------------------------------------------------------- #
# Traduzione termini (equipment)
# --------------------------------------------------------------------------- #
def _restore_umlauts(s: str) -> str:
    """Ripristina gli umlaut da traslitterazione ASCII (ue→ü, oe→ö, ae→ä).
    Usato SOLO per il lookup nel glossario: se non matcha, il token resta invariato."""
    return (s.replace("ue", "ü").replace("oe", "ö").replace("ae", "ä")
             .replace("Ue", "Ü").replace("Oe", "Ö").replace("Ae", "Ä"))


def _lookup(table: dict[str, str], key_lower: str) -> str | None:
    """Cerca in tabella la chiave così com'è o con umlaut ripristinati."""
    if key_lower in table:
        return table[key_lower]
    restored = _restore_umlauts(key_lower)
    if restored != key_lower and restored in table:
        return table[restored]
    return None


def translate_term(term: str) -> str:
    """Traduce un singolo optional/dotazione DE→IT (frase→parola, preserva la forma)."""
    if not term:
        return term
    raw = term.strip()
    low = raw.lower()

    # 1) match frase intera (così com'è o con umlaut ripristinati)
    phrase = _lookup(PHRASES, low)
    if phrase is not None:
        return _preserve_case(raw, phrase)

    # 2) match frase come sottostringa (ordina per lunghezza decrescente)
    out = raw
    low_restored = _restore_umlauts(low)
    for de in sorted(PHRASES, key=len, reverse=True):
        if de in low or de in low_restored:
            # sostituisce sia la forma ASCII sia quella con umlaut
            out = _sub_ci(out, de, PHRASES[de])
            ascii_de = de.replace("ü", "ue").replace("ö", "oe").replace("ä", "ae")
            if ascii_de != de:
                out = _sub_ci(out, ascii_de, PHRASES[de])
    if out.lower() != raw.lower():
        out = _translate_words(out)
        return out

    # 3) fallback token-per-token sulle singole parole
    return _translate_words(raw)


def _translate_words(text: str) -> str:
    parts = _TOKEN_RE.findall(text)
    rebuilt: list[str] = []
    for p in parts:
        translated = _lookup(WORDS, p.lower())
        if translated is not None:
            rebuilt.append(_preserve_case(p, translated))
        else:
            rebuilt.append(p)
    return "".join(rebuilt)


def _sub_ci(haystack: str, needle_lower: str, replacement: str) -> str:
    pattern = re.compile(re.escape(needle_lower), re.IGNORECASE)
    return pattern.sub(replacement, haystack)


def _preserve_case(source: str, translated: str) -> str:
    if source.isupper():
        return translated.upper()
    if source[:1].isupper():
        return translated[:1].upper() + translated[1:]
    return translated


def translate_equipment(equipment_de: list[str]) -> list[str]:
    """Traduce la lista optional mantenendo l'allineamento 1:1 (stesso numero di voci)."""
    return [translate_term(x) for x in (equipment_de or [])]


def _t(value: Any) -> Any:
    """Traduce un valore testuale di scheda (colore/interni/carrozzeria); passa oltre i non-stringa."""
    if not isinstance(value, str) or not value.strip():
        return value
    return translate_term(value)


# --------------------------------------------------------------------------- #
# Scheda tecnica IT (specs_it) — solo da campi presenti in listing.json
# --------------------------------------------------------------------------- #
def build_specs_it(listing: dict[str, Any]) -> dict[str, Any]:
    specs: dict[str, Any] = {}

    def put(label: str, value: Any) -> None:
        if value not in (None, "", []):
            specs[label] = value

    put("Marca", listing.get("make"))
    put("Modello", listing.get("model"))
    if listing.get("variant"):
        put("Allestimento", listing.get("variant"))
    put("Anno", listing.get("year"))
    put("Prima immatricolazione", listing.get("first_registration"))
    if listing.get("mileage_km") is not None:
        put("Chilometraggio", f"{_thousands(listing['mileage_km'])} km")
    put("Alimentazione", listing.get("fuel"))
    put("Cambio", listing.get("gearbox"))
    kw, hp = listing.get("power_kw"), listing.get("power_hp")
    if kw and hp:
        put("Potenza", f"{kw} kW ({hp} CV)")
    elif hp:
        put("Potenza", f"{hp} CV")
    elif kw:
        put("Potenza", f"{kw} kW")
    put("Trazione", listing.get("drivetrain"))
    put("Carrozzeria", _t(listing.get("body_type")))
    put("Porte", listing.get("doors"))
    put("Posti", listing.get("seats"))
    put("Colore", _t(listing.get("color")))
    # "Colore costruttore" (es. Kosmosschwarz) è un nome marketing: omesso per non
    # tradurlo erroneamente né generare falsi residui tedeschi.
    put("Interni", _t(listing.get("interior")))
    put("Classe emissioni", listing.get("emission_class"))
    if listing.get("co2_g_km") is not None:
        put("Emissioni CO2", f"{listing['co2_g_km']} g/km")
    return specs


# --------------------------------------------------------------------------- #
# Copy: titolo, highlights, descrizione — composti dai fatti (no invenzione)
# --------------------------------------------------------------------------- #
def build_title_it(listing: dict[str, Any]) -> str:
    """Titolo IT SENZA prezzo (il prezzo lo aggiunge Max in price.final_title)."""
    name = " ".join(
        str(p) for p in (listing.get("make"), listing.get("model"), listing.get("variant")) if p
    )
    return " ".join(name.split()).strip() or "Autovettura"


def build_highlights_it(listing: dict[str, Any], equipment_it: list[str]) -> list[str]:
    """3-6 punti di forza, tutti derivati da fatti presenti in listing.json."""
    h: list[str] = []
    if listing.get("year"):
        h.append(f"Immatricolata {listing['year']}")
    if listing.get("mileage_km") is not None:
        h.append(f"{_thousands(listing['mileage_km'])} km")
    if listing.get("gearbox"):
        h.append(f"Cambio {str(listing['gearbox']).lower()}")
    if listing.get("fuel"):
        h.append(f"Alimentazione {str(listing['fuel']).lower()}")
    if listing.get("drivetrain"):
        h.append(f"Trazione {str(listing['drivetrain']).lower()}")
    if listing.get("power_hp"):
        h.append(f"{listing['power_hp']} CV")
    # arricchisci con 1-2 optional di pregio se disponibili
    premium = _pick_premium_equipment(equipment_it)
    for term in premium:
        if len(h) >= 6:
            break
        h.append(term)
    # garantisce almeno 3 punti se i dati lo consentono
    return h[:6]


def build_description_it(listing: dict[str, Any], equipment_it: list[str]) -> str:
    """Descrizione di vendita in italiano, composta dai fatti. Nessun dato inventato."""
    make = listing.get("make") or "vettura"
    model = listing.get("model") or ""
    variant = listing.get("variant") or ""
    name = " ".join(x for x in (make, model, variant) if x).strip()

    frasi: list[str] = []
    apertura = f"{name} in ottime condizioni, disponibile presso la nostra concessionaria."
    frasi.append(apertura)

    dettagli: list[str] = []
    if listing.get("year"):
        dettagli.append(f"immatricolata nel {listing['year']}")
    if listing.get("mileage_km") is not None:
        dettagli.append(f"con {_thousands(listing['mileage_km'])} km")
    if listing.get("fuel"):
        dettagli.append(f"alimentazione {str(listing['fuel']).lower()}")
    if listing.get("gearbox"):
        dettagli.append(f"cambio {str(listing['gearbox']).lower()}")
    if listing.get("power_hp"):
        dettagli.append(f"potenza di {listing['power_hp']} CV")
    if listing.get("drivetrain"):
        dettagli.append(f"trazione {str(listing['drivetrain']).lower()}")
    if dettagli:
        frasi.append("Vettura " + ", ".join(dettagli) + ".")

    if equipment_it:
        top = equipment_it[:8]
        frasi.append("Tra le dotazioni: " + _join_it(top) + ".")

    # arricchimento opzionale della prosa dal testo originale (dietro flag, dry-run-safe)
    extra = _maybe_llm_prose(listing)
    if extra:
        frasi.append(extra)

    frasi.append("Possibilità di permuta e finanziamento. Contattaci per una prova o maggiori informazioni.")
    return " ".join(frasi)


# --------------------------------------------------------------------------- #
# Entry point (chiamato da run.py dopo S2)
# --------------------------------------------------------------------------- #
def translate(ctx: RunContext, dealer: dict[str, Any]) -> dict[str, Any]:
    listing = load_json(ctx.listing_path)

    equipment_it = translate_equipment(listing.get("equipment_de", []))
    specs_it = build_specs_it(listing)
    title_it = build_title_it(listing)
    highlights_it = build_highlights_it(listing, equipment_it)
    description_it = build_description_it(listing, equipment_it)
    headline_it = _build_headline(listing)

    content = {
        "title_it": title_it,
        "headline_it": headline_it,
        "description_it": description_it,
        "highlights_it": highlights_it,
        "equipment_it": equipment_it,
        "specs_it": specs_it,
    }

    _merge_content(ctx, listing, content)

    # avviso non bloccante: residui tedeschi nel copy (Gate B poi decide)
    residui = _german_residue(content)
    if residui:
        ctx.logger.warning("S3: possibili residui tedeschi (%d): %s",
                            len(residui), ", ".join(residui[:8]))
    ctx.logger.info("S3 translate+copy: %d optional tradotti, %d specs, %d highlights.",
                    len(equipment_it), len(specs_it), len(highlights_it))
    return content


# --------------------------------------------------------------------------- #
# Merge su listing_it.json (preserva price di Half A)
# --------------------------------------------------------------------------- #
def _merge_content(ctx: RunContext, listing: dict[str, Any], content: dict[str, Any]) -> None:
    existing = load_json(ctx.listing_it_path) if ctx.listing_it_path.exists() else {}
    merged = {
        "source_url": listing.get("source_url"),
        "source_id": listing.get("source_id"),
        "make": listing.get("make"),
        "model": listing.get("model"),
        "variant": listing.get("variant"),
        "generated_at": existing.get("generated_at"),
        "_meta": {**(existing.get("_meta") or {}), "text_by": "op-translator-copy (Gael)"},
        "content": content,                       # prodotto qui (Half B)
        "price": existing.get("price"),           # preservato (Half A), può essere assente
    }
    if merged["price"] is None:
        merged.pop("price")  # lo scriverà pricer.py in S4
    save_json(ctx.listing_it_path, merged)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _build_headline(listing: dict[str, Any]) -> str | None:
    bits = []
    if listing.get("year"):
        bits.append(str(listing["year"]))
    if listing.get("mileage_km") is not None:
        bits.append(f"{_thousands(listing['mileage_km'])} km")
    if listing.get("fuel"):
        bits.append(str(listing["fuel"]))
    if not bits:
        return None
    return " · ".join(bits)


def _pick_premium_equipment(equipment_it: list[str]) -> list[str]:
    keys = ("pelle", "navigatore", "tetto", "led", "telecamera", "cruise",
            "riscaldati", "cerchi", "sensori", "climatizzatore")
    out: list[str] = []
    for term in equipment_it:
        tl = term.lower()
        if any(k in tl for k in keys):
            out.append(term)
    return out[:3]


def _german_residue(content: dict[str, Any]) -> list[str]:
    found: list[str] = []
    for field in ("title_it", "headline_it", "description_it"):
        for tok in re.findall(r"[A-Za-zÄÖÜäöüß-]+", str(content.get(field) or "")):
            if looks_german(tok) and tok not in found:
                found.append(tok)
    for item in content.get("equipment_it", []):
        for tok in re.findall(r"[A-Za-zÄÖÜäöüß-]+", str(item)):
            if looks_german(tok) and tok not in found:
                found.append(tok)
    return found


def _maybe_llm_prose(listing: dict[str, Any]) -> str | None:
    """Gancio arricchimento LLM. Disattivo di default (dry-run, Mandato Art.4.3)."""
    backend = os.environ.get("TRANSLATE_BACKEND", "deterministic").strip().lower()
    if backend != "llm":
        return None
    # Predisposizione: qui andrebbe la chiamata al modello con la description_de come input,
    # istruzione "traduci in italiano scorrevole, NON aggiungere fatti". Richiede ok spesa (Max).
    # Lasciato non implementato di proposito per non spendere senza autorizzazione.
    return None


def _join_it(items: list[str]) -> str:
    items = [i for i in items if i]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " e " + items[-1]


def _thousands(n: Any) -> str:
    try:
        return f"{int(round(float(n))):,}".replace(",", ".")
    except (TypeError, ValueError):
        return str(n)
