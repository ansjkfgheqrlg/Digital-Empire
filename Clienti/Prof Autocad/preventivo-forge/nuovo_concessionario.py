#!/usr/bin/env python3
"""
nuovo_concessionario.py — FABBRICA di app per concessionario (Half A / Max).

Clona il lavoro per un NUOVO concessionario cambiando SOLO ciò che deve cambiare:
nome, dati legali/contatti, logo, prezzo, colori del preventivo. Il MOTORE resta UNO
(un bug corretto vale per tutti). Ogni concessionario ottiene la SUA app, identica,
col SUO nome e i preventivi col SUO stile.

Cosa fa:
  1. crea  concessionarie/<id>/config.json  (+ copia il logo)
  2. crea  ../<Cartella Cliente>/            (dentro Clienti/) con nota di consegna
  3. (--build) impacchetta l'app brandizzata in  ../<Cartella Cliente>/App/
       copiando dist/PreventivoForge + brand.json + il config del dealer accanto all'exe
  4. stampa i passi finali (registrare la licenza, consegnare)

Uso:
  python nuovo_concessionario.py --id acme --nome "Acme Auto srl" \
      --piva 01234567890 --sede "via Roma 1, Milano, 20100" \
      --tel "02 1234567" --email info@acme.it --pec acme@pec.it \
      --logo "C:/percorso/logo.png" [--pct 3 --f1 1500 --f2 1500] \
      [--accent "#2b2b2b" --highlight "#f2a200"] [--build]

Note:
  - <id> = slug minuscolo senza spazi (es. "acme"). È la chiave usata ovunque (licenza, config).
  - --build richiede che l'app motore sia già stata costruita una volta (dist/PreventivoForge).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

try:  # console UTF-8 (Windows cp1252 va in crash su ✅/emoji)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = Path(__file__).resolve().parent          # preventivo-forge/
CLIENTI_DIR = HERE.parent.parent                 # Clienti/
DEALERS_DIR = HERE / "concessionarie"
DIST_APP = HERE / "dist" / "PreventivoForge"     # onedir costruito dal build motore


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


def _build_config(a) -> dict:
    return {
        "dealer_id": a.id,
        "display_name": a.nome,
        "logo_path": "logo.png",
        "legal": {
            "company": a.nome,
            "vat": a.piva or "",
            "registered_office": a.sede or "",
        },
        "contacts": {
            "phone": a.tel or "",
            "email": a.email or "",
            "pec": a.pec or "",
            "address": a.sede or "",
            "website": a.sito or "",
        },
        "pricing": {
            "_formula": "finale = round(esposto * (1 + surcharge_pct/100) + fixed_1 + fixed_2)",
            "surcharge_pct": a.pct,
            "fixed_1": a.f1,
            "fixed_2": a.f2,
        },
        "preventivo": {
            "language": "it",
            "currency": "EUR",
            "validity_days": 15,
            "template": a.id,
            "footer_note": a.footer or "Offerta valida salvo disponibilità del fornitore",
            "show_price_breakdown_to_customer": True,
            "accent_color": a.accent,
            "highlight_color": a.highlight,
        },
    }


def _crea_config(a) -> Path:
    ddir = DEALERS_DIR / a.id
    if ddir.exists() and not a.force:
        sys.exit(f"❌ concessionarie/{a.id} esiste già. Usa --force per sovrascrivere.")
    ddir.mkdir(parents=True, exist_ok=True)

    logo_src = Path(a.logo)
    if not logo_src.exists():
        sys.exit(f"❌ logo non trovato: {logo_src}")
    shutil.copyfile(logo_src, ddir / "logo.png")

    cfg = _build_config(a)
    (ddir / "config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ config creato: concessionarie/{a.id}/config.json (+ logo.png)")
    return ddir


def _crea_cartella_cliente(a) -> Path:
    cart = CLIENTI_DIR / a.nome
    cart.mkdir(parents=True, exist_ok=True)
    nota = cart / "CONSEGNA.md"
    if not nota.exists():
        nota.write_text(
            f"# Consegna — {a.nome}\n\n"
            f"- ID interno: `{a.id}`\n"
            f"- App brandizzata: `App/PreventivoForge/PreventivoForge.exe` (dopo --build)\n"
            f"- Requisiti PC: Google Chrome + connessione normale (no VPN).\n"
            f"- Kill-switch: gestito da noi (`gestione-licenze.py sospendi {a.id}`).\n\n"
            f"Vedi la guida generale in preventivo-forge/CONSEGNA-NOVACAR.md (§requisiti/uso/SmartScreen).\n",
            encoding="utf-8")
    print(f"✅ cartella cliente: Clienti/{a.nome}/")
    return cart


def _impacchetta_app(a, cart: Path) -> None:
    if not DIST_APP.exists():
        print(f"⚠️  --build saltato: manca {DIST_APP}. Costruisci prima il motore (build_exe.bat).")
        return
    dst = cart / "App" / "PreventivoForge"
    if dst.exists():
        shutil.rmtree(dst, ignore_errors=True)
    dst.parent.mkdir(parents=True, exist_ok=True)
    print(f"   copio l'app motore in Clienti/{a.nome}/App/ ...")
    shutil.copytree(DIST_APP, dst)

    # brand.json = identità di QUESTA app (nome + dealer)
    (dst / "brand.json").write_text(
        json.dumps({"dealer_id": a.id, "display_name": a.nome}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    # config del dealer accanto all'exe (letto con priorità dall'app frozen)
    conc = dst / "concessionarie" / a.id
    conc.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(DEALERS_DIR / a.id / "config.json", conc / "config.json")
    shutil.copyfile(DEALERS_DIR / a.id / "logo.png", conc / "logo.png")
    print(f"✅ app brandizzata pronta: Clienti/{a.nome}/App/PreventivoForge/PreventivoForge.exe")


def main() -> int:
    ap = argparse.ArgumentParser(description="Fabbrica app per nuovo concessionario")
    ap.add_argument("--id", required=True, help="slug minuscolo (es. acme)")
    ap.add_argument("--nome", required=True, help="ragione sociale (es. 'Acme Auto srl')")
    ap.add_argument("--piva", default="")
    ap.add_argument("--sede", default="")
    ap.add_argument("--tel", default="")
    ap.add_argument("--email", default="")
    ap.add_argument("--pec", default="")
    ap.add_argument("--sito", default="")
    ap.add_argument("--logo", required=True, help="percorso al logo (png)")
    ap.add_argument("--pct", type=float, default=3.0)
    ap.add_argument("--f1", type=float, default=1500.0)
    ap.add_argument("--f2", type=float, default=1500.0)
    ap.add_argument("--accent", default="#2b2b2b")
    ap.add_argument("--highlight", default="#f2a200")
    ap.add_argument("--footer", default="")
    ap.add_argument("--build", action="store_true", help="impacchetta anche l'app brandizzata")
    ap.add_argument("--force", action="store_true", help="sovrascrive config esistente")
    a = ap.parse_args()

    a.id = _slug(a.id)
    if not a.id:
        sys.exit("❌ --id non valido")

    print(f"\n=== NUOVO CONCESSIONARIO: {a.nome} (id={a.id}) ===")
    _crea_config(a)
    cart = _crea_cartella_cliente(a)
    if a.build:
        _impacchetta_app(a, cart)

    print("\nPASSI FINALI:")
    print(f"  1. Registra la licenza (attiva l'abbonamento):  python gestione-licenze.py aggiungi {a.id}")
    if not a.build:
        print(f"  2. Costruisci l'app brandizzata:  python nuovo_concessionario.py --id {a.id} ... --build")
    print(f"  3. Consegna la cartella Clienti/{a.nome}/App/PreventivoForge/ al concessionario.")
    print("     (Requisiti sul suo PC: Google Chrome + linea normale.)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
