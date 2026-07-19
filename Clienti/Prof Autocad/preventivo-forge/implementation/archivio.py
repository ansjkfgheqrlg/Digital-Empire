"""
archivio.py — Archivio dei preventivi generati (per la GUI). Half A add-on.

Ogni preventivo creato viene salvato qui: il PDF + una foto miniatura + una riga di indice.
La GUI legge l'archivio e mostra i blocchi (foto, nome, prezzo, "Apri il preventivo").

Cartella (scrivibile, accanto all'exe in frozen): <RUNS_DIR.parent>/archivio/
  index.json          -> lista voci {id, title, price, price_eur, pdf, thumb_file, created}
  pdf/<id>.pdf        -> copia del preventivo
  foto/<id>.jpg       -> miniatura (per il blocco in archivio)
"""
from __future__ import annotations

import base64
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any


def _base() -> Path:
    try:
        import common
        base = common.RUNS_DIR.parent / "archivio"
    except Exception:
        base = Path(__file__).resolve().parent.parent / "archivio"
    (base / "pdf").mkdir(parents=True, exist_ok=True)
    (base / "foto").mkdir(parents=True, exist_ok=True)
    return base


def _index_path() -> Path:
    return _base() / "index.json"


def _load_index() -> list[dict[str, Any]]:
    p = _index_path()
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _save_index(items: list[dict[str, Any]]) -> None:
    _index_path().write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def _thumb(src: Path, dst: Path, max_w: int = 320) -> bool:
    """Salva una miniatura JPEG di `src` in `dst`. True se riuscito."""
    try:
        from PIL import Image
        with Image.open(src) as im:
            im = im.convert("RGB")
            if im.width > max_w:
                r = max_w / float(im.width)
                im = im.resize((max_w, int(im.height * r)), Image.LANCZOS)
            im.save(dst, format="JPEG", quality=82, optimize=True)
        return True
    except Exception:
        try:
            shutil.copyfile(src, dst)
            return True
        except Exception:
            return False


def add(pdf_path: str | Path) -> None:
    """Aggiunge il preventivo all'archivio. `pdf_path` = PDF nella cartella runs/<id>/
    (da cui si ricavano listing.json + foto). Mai bloccante: su errore non fa nulla."""
    try:
        pdf_path = Path(pdf_path)
        run_dir = pdf_path.parent
        listing = json.loads((run_dir / "listing.json").read_text(encoding="utf-8")) \
            if (run_dir / "listing.json").exists() else {}
        lit = json.loads((run_dir / "listing_it.json").read_text(encoding="utf-8")) \
            if (run_dir / "listing_it.json").exists() else {}
        price = (lit.get("price") or {})
        content = (lit.get("content") or {})

        rid = run_dir.name
        make = (listing.get("make") or "").strip()
        model = (listing.get("model") or "").strip()
        title = (content.get("title_it") or f"{make} {model}").strip() or "Preventivo"
        price_eur = price.get("final_eur")

        base = _base()
        # copia PDF
        dst_pdf = base / "pdf" / f"{rid}.pdf"
        try:
            shutil.copyfile(str(pdf_path), str(dst_pdf))
        except Exception:
            dst_pdf = pdf_path

        # miniatura da una foto dell'annuncio
        thumb_rel = ""
        fotos = sorted((run_dir / "foto").glob("*")) if (run_dir / "foto").exists() else []
        if fotos:
            dst_thumb = base / "foto" / f"{rid}.jpg"
            if _thumb(fotos[0], dst_thumb):
                thumb_rel = f"foto/{rid}.jpg"

        items = _load_index()
        items = [it for it in items if it.get("id") != rid]   # dedup (rigenerazioni)
        items.insert(0, {
            "id": rid,
            "title": title,
            "make": make,
            "model": model,
            "price": f"{int(price_eur):,}".replace(",", ".") + " €" if price_eur else "",
            "price_eur": price_eur,
            "pdf": str(dst_pdf),
            "thumb_file": thumb_rel,
            "created": datetime.now().strftime("%d/%m/%Y %H:%M"),
        })
        _save_index(items)
    except Exception:
        pass


def clear() -> None:
    """Svuota l'archivio: PDF copiati + miniature + indice. Chiamato alla CHIUSURA
    dell'app (l'archivio riparte vuoto a ogni riapertura). Mai bloccante: su errore
    non fa nulla. NON tocca i PDF nella cartella di output (quelli restano al cliente)."""
    try:
        base = _base()
        for sub in ("pdf", "foto"):
            shutil.rmtree(base / sub, ignore_errors=True)
        try:
            _index_path().unlink()
        except FileNotFoundError:
            pass
    except Exception:
        pass


def entries(limit: int = 200) -> list[dict[str, Any]]:
    """Voci per la GUI, con la miniatura incorporata come data-URI (self-contained)."""
    base = _base()
    out: list[dict[str, Any]] = []
    for it in _load_index()[:limit]:
        thumb_uri = ""
        tf = it.get("thumb_file") or ""
        if tf:
            p = base / tf
            if p.exists():
                try:
                    thumb_uri = "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode("ascii")
                except Exception:
                    thumb_uri = ""
        out.append({
            "id": it.get("id"),
            "title": it.get("title") or "Preventivo",
            "price": it.get("price") or "",
            "created": it.get("created") or "",
            "pdf": it.get("pdf") or "",
            "thumb": thumb_uri,
        })
    return out
