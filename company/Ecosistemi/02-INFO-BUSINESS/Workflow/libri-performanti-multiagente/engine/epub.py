"""
EPUB — il formato ebook, che mancava del tutto (2026-08-23).

PERCHE'. Fino a oggi il pacchetto conteneva `.docx` + PDF + copertina, cioe' **solo il
cartaceo**: `grep -ri epub` su tutto il progetto non trovava niente. Nei generi che stiamo
scrivendo (cozy fantasy, cozy mystery, romance suspense) il volume sta nell'ebook, e il
cartaceo e' il complemento. Si stava preparando con cura il canale secondario e saltando
quello principale, con un costo marginale prossimo a zero: i capitoli sono gia' file di
testo, mancava solo l'involucro.

COME. Niente librerie: un EPUB e' uno zip con dentro dei file XHTML e un paio di manifesti,
e `zipfile` sta nella libreria standard. Aggiungere una dipendenza per fare uno zip
sarebbe stato peggio — questo modulo non ha import esterni, quindi non puo' rompersi
per un aggiornamento altrui.

Vincoli veri del formato, tutti rispettati qui perche' altrimenti i lettori rifiutano il
file: `mimetype` per primo e NON compresso; `META-INF/container.xml` che punta all'OPF;
un manifest che elenca ogni file; un indice di navigazione (`nav.xhtml` per EPUB3 e
`toc.ncx` per i lettori vecchi, che KDP gradisce ancora).
"""
from __future__ import annotations

import re
import uuid
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html import escape
from pathlib import Path

CSS = """\
body { margin: 0 5%; text-align: justify; font-size: 1em; line-height: 1.4; }
h1 { text-align: center; font-size: 1.6em; margin: 2em 0 1.5em 0; page-break-before: always; }
h2 { text-align: center; font-size: 1.2em; margin: 1.5em 0 1em 0; }
p { text-indent: 1.2em; margin: 0; }
p.primo, h1 + p, h2 + p { text-indent: 0; }
p.centrato { text-indent: 0; text-align: center; margin: 0.6em 0; }
div.copertina { text-align: center; margin: 0; padding: 0; }
div.copertina img { max-width: 100%; max-height: 100%; }
"""

_MIME_IMMAGINI = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                  ".gif": "image/gif", ".svg": "image/svg+xml"}

# La copertina dentro l'EPUB non e' quella del cartaceo (2026-08-23). Il PNG a norma KDP e'
# 1800x2700 senza perdite e pesa fra i 2 e i 6 MB: infilato tal quale nell'ebook lo porta a
# pesare uguale, e su Kindle **la consegna si paga a MB** sul 70% di royalty. Un ebook da
# 6 MB si mangia una fetta di ogni copia venduta per un'immagine che il lettore vede alta
# 800 pixel. 1600 px sul lato lungo in JPEG di qualita' 85 e' la misura che Amazon stessa
# consiglia per la copertina ebook, e porta il file sotto il mezzo mega.
COPERTINA_EBOOK_LATO_MAX = 1600
COPERTINA_EBOOK_QUALITA = 85


@dataclass
class CapitoloEpub:
    titolo: str
    paragrafi: list[str]


@dataclass
class LibroEpub:
    titolo: str
    autore: str
    capitoli: list[CapitoloEpub]
    lingua: str = "en"
    sottotitolo: str = ""
    descrizione: str = ""
    copertina: Path | None = None
    # Pagine che non sono capitoli: frontespizio, copyright, ringraziamenti, "altri libri".
    # Ognuna e' (titolo, paragrafi, in_indice).
    pagine_iniziali: list[tuple[str, list[str], bool]] = field(default_factory=list)
    pagine_finali: list[tuple[str, list[str], bool]] = field(default_factory=list)


def _xhtml(titolo_pagina: str, corpo: str, lingua: str) -> str:
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
        f'xml:lang="{escape(lingua, quote=True)}" lang="{escape(lingua, quote=True)}">\n'
        f'<head><meta charset="utf-8"/><title>{escape(titolo_pagina)}</title>'
        '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
        f'<body>\n{corpo}\n</body>\n</html>\n'
    )


def _pagina(titolo: str, paragrafi: list[str], lingua: str, livello: str = "h1") -> str:
    parti = [f"<{livello}>{escape(titolo)}</{livello}>"] if titolo else []
    for i, p in enumerate(paragrafi):
        testo = escape(p.strip())
        if not testo:
            continue
        # Le righe di stacco fra scene restano centrate, come nell'impaginato cartaceo.
        classe = ' class="centrato"' if testo in {"* * *", "***", "#"} else (
            ' class="primo"' if i == 0 else "")
        parti.append(f"<p{classe}>{testo}</p>")
    return _xhtml(titolo or "", "\n".join(parti), lingua)


def _opf(libro: LibroEpub, voci: list[tuple[str, str, str]], id_libro: str,
         nome_copertina: str | None) -> str:
    """voci = [(id, nomefile, titolo)] nell'ordine di lettura."""
    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" '
                'properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="css" href="style.css" media-type="text/css"/>']
    if nome_copertina:
        tipo = _MIME_IMMAGINI.get(Path(nome_copertina).suffix.lower(), "image/jpeg")
        manifest.append(f'<item id="copertina-img" href="{nome_copertina}" '
                        f'media-type="{tipo}" properties="cover-image"/>')
    for ident, nome, _titolo in voci:
        manifest.append(f'<item id="{ident}" href="{nome}" '
                        f'media-type="application/xhtml+xml"/>')
    spine = "".join(f'<itemref idref="{ident}"/>' for ident, _n, _t in voci)
    sottotitolo = (f'<dc:title id="sub">{escape(libro.sottotitolo)}</dc:title>'
                   if libro.sottotitolo else "")
    descrizione = (f'<dc:description>{escape(libro.descrizione)}</dc:description>'
                   if libro.descrizione else "")
    quando = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
        'unique-identifier="libro-id">\n'
        '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        f'    <dc:identifier id="libro-id">urn:uuid:{id_libro}</dc:identifier>\n'
        f'    <dc:title>{escape(libro.titolo)}</dc:title>\n'
        f'    {sottotitolo}\n'
        f'    <dc:creator>{escape(libro.autore)}</dc:creator>\n'
        f'    <dc:language>{escape(libro.lingua)}</dc:language>\n'
        f'    {descrizione}\n'
        f'    <meta property="dcterms:modified">{quando}</meta>\n'
        + ('    <meta name="cover" content="copertina-img"/>\n' if nome_copertina else '')
        + '  </metadata>\n'
        '  <manifest>\n    ' + "\n    ".join(manifest) + '\n  </manifest>\n'
        f'  <spine toc="ncx">{spine}</spine>\n'
        '</package>\n'
    )


def _nav(libro: LibroEpub, in_indice: list[tuple[str, str, str]]) -> str:
    voci = "\n".join(f'      <li><a href="{nome}">{escape(titolo)}</a></li>'
                     for _i, nome, titolo in in_indice)
    corpo = ('<nav epub:type="toc" id="toc">\n  <h1>Contents</h1>\n  <ol>\n'
             f'{voci}\n  </ol>\n</nav>')
    return _xhtml("Contents", corpo, libro.lingua)


def _ncx(libro: LibroEpub, in_indice: list[tuple[str, str, str]], id_libro: str) -> str:
    punti = "\n".join(
        f'    <navPoint id="np{n}" playOrder="{n}">\n'
        f'      <navLabel><text>{escape(titolo)}</text></navLabel>\n'
        f'      <content src="{nome}"/>\n    </navPoint>'
        for n, (_i, nome, titolo) in enumerate(in_indice, start=1))
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
        f'  <head><meta name="dtb:uid" content="urn:uuid:{id_libro}"/></head>\n'
        f'  <docTitle><text>{escape(libro.titolo)}</text></docTitle>\n'
        f'  <navMap>\n{punti}\n  </navMap>\n</ncx>\n'
    )


def _nome_file(prefisso: str, n: int) -> str:
    return f"{prefisso}{n:02d}.xhtml"


def copertina_per_ebook(percorso: Path) -> tuple[str, bytes]:
    """(nome dentro l'epub, byte). Ridimensiona e comprime; se Pillow non c'e', copia.

    Non solleva mai: un ebook con la copertina pesante e' comunque meglio di un ebook che
    non esce. Se la conversione non riesce, il file originale viene incluso com'e'."""
    percorso = Path(percorso)
    try:
        from PIL import Image
        import io

        with Image.open(percorso) as img:
            img = img.convert("RGB")
            lato = max(img.size)
            if lato > COPERTINA_EBOOK_LATO_MAX:
                fattore = COPERTINA_EBOOK_LATO_MAX / lato
                img = img.resize((round(img.width * fattore), round(img.height * fattore)),
                                 Image.LANCZOS)
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=COPERTINA_EBOOK_QUALITA, optimize=True)
            return "copertina.jpg", buffer.getvalue()
    except Exception:  # noqa: BLE001
        return f"copertina{percorso.suffix.lower()}", percorso.read_bytes()


def costruisci(libro: LibroEpub, destinazione: Path) -> Path:
    """Scrive l'EPUB e ritorna il percorso. Solleva se non c'e' nemmeno un capitolo."""
    if not libro.capitoli:
        raise ValueError("Un EPUB senza capitoli non si fa: il libro e' vuoto.")
    destinazione = Path(destinazione)
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    id_libro = str(uuid.uuid4())

    pagine: list[tuple[str, str, str, bool]] = []   # (id, nome, titolo, in_indice)
    contenuti: dict[str, str] = {}

    nome_copertina = None
    byte_copertina = b""
    if libro.copertina and Path(libro.copertina).exists():
        nome_copertina, byte_copertina = copertina_per_ebook(Path(libro.copertina))
        contenuti["cover.xhtml"] = _xhtml(
            "Cover",
            f'<div class="copertina"><img src="{nome_copertina}" '
            f'alt="{escape(libro.titolo, quote=True)}"/></div>',
            libro.lingua)
        pagine.append(("cover", "cover.xhtml", "Cover", False))

    for n, (titolo, paragrafi, in_indice) in enumerate(libro.pagine_iniziali, start=1):
        nome = _nome_file("front", n)
        contenuti[nome] = _pagina(titolo, paragrafi, libro.lingua, livello="h2")
        pagine.append((f"front{n:02d}", nome, titolo or f"Front {n}", in_indice))

    for n, capitolo in enumerate(libro.capitoli, start=1):
        nome = _nome_file("cap", n)
        contenuti[nome] = _pagina(capitolo.titolo, capitolo.paragrafi, libro.lingua)
        pagine.append((f"cap{n:02d}", nome, capitolo.titolo, True))

    for n, (titolo, paragrafi, in_indice) in enumerate(libro.pagine_finali, start=1):
        nome = _nome_file("back", n)
        contenuti[nome] = _pagina(titolo, paragrafi, libro.lingua, livello="h2")
        pagine.append((f"back{n:02d}", nome, titolo or f"Back {n}", in_indice))

    voci = [(i, nome, titolo) for i, nome, titolo, _ind in pagine]
    in_indice = [(i, nome, titolo) for i, nome, titolo, ind in pagine if ind]

    with zipfile.ZipFile(destinazione, "w", zipfile.ZIP_DEFLATED) as z:
        # Il mimetype deve essere il PRIMO file dell'archivio e NON compresso: e' l'unica
        # regola dell'EPUB che i lettori applicano alla lettera, e se salta il file viene
        # rifiutato senza spiegazioni.
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0" encoding="utf-8"?>\n'
                   '<container version="1.0" '
                   'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
                   '  <rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles>\n'
                   '</container>\n')
        z.writestr("OEBPS/style.css", CSS)
        z.writestr("OEBPS/content.opf", _opf(libro, voci, id_libro, nome_copertina))
        z.writestr("OEBPS/nav.xhtml", _nav(libro, in_indice))
        z.writestr("OEBPS/toc.ncx", _ncx(libro, in_indice, id_libro))
        for nome, testo in contenuti.items():
            z.writestr(f"OEBPS/{nome}", testo)
        if nome_copertina:
            z.writestr(f"OEBPS/{nome_copertina}", byte_copertina)
    return destinazione


def da_capitoli_markdown(titolo: str, autore: str, capitoli: list[tuple[str, list[str]]],
                         **extra) -> LibroEpub:
    """Scorciatoia: i capitoli come li tiene `book_project` (titolo + paragrafi)."""
    return LibroEpub(titolo=titolo, autore=autore,
                     capitoli=[CapitoloEpub(t, p) for t, p in capitoli], **extra)


_RE_SPAZI = re.compile(r"\s+")


def conta_parole_epub(percorso: Path) -> int:
    """Riconta le parole DENTRO l'epub appena scritto, non nella struttura in memoria.

    Stessa regola del resto del progetto: un file si controlla riaprendolo. Se l'EPUB
    esce con meno parole del manoscritto, qualcosa e' andato perso nella conversione e si
    deve vedere subito, non dopo il caricamento."""
    totale = 0
    with zipfile.ZipFile(percorso) as z:
        for nome in z.namelist():
            if not (nome.startswith("OEBPS/cap") and nome.endswith(".xhtml")):
                continue
            testo = z.read(nome).decode("utf-8")
            testo = re.sub(r"<[^>]+>", " ", testo)
            totale += len([p for p in _RE_SPAZI.split(testo) if p])
    return totale
