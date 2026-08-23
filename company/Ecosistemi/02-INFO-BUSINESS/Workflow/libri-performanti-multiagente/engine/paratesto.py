"""
Paratesto: le pagine che non sono il romanzo (2026-08-23).

PERCHE' ESISTE. Il manoscritto era frontespizio + 24 capitoli e basta. Mancavano tre cose
che ogni libro pubblicato ha, e la piu' importante non e' formale:

  1. **pagina di copyright** — la mette qualunque libro, e la sua assenza e' una delle cose
     che fanno sembrare autopubblicato un libro autopubblicato;
  2. **richiesta di recensione in fondo** — nei primi 30 giorni la velocita' di recensioni
     e' la leva che decide se un titolo esiste o no, e il libro non la chiedeva a nessuno.
     Il lettore che arriva all'ultima pagina e' l'unico che la lascera' davvero;
  3. **"Also by"** — l'unico posto in cui tre libri finiti possono spingersi a vicenda
     senza spendere niente. Si costruisce da solo dagli altri libri del catalogo.

REGOLE DI KDP, rispettate nel testo qui sotto: si puo' chiedere una recensione ONESTA, non
si possono chiedere solo quelle positive, non si puo' offrire niente in cambio, e non si
puo' mandare il lettore fuori da Amazon per comprare (per questo il "Also by" elenca i
titoli e non mette link).

Il testo e' in inglese perche' i libri sono in inglese. Vive qui e non dentro
`kdp_formatter` perche' lo usano in due, il .docx e l'EPUB, e devono dire la stessa cosa.
"""
from __future__ import annotations

from datetime import datetime

DIVISORE = "* * *"


def pagina_copyright(titolo: str, autore: str, anno: int | None = None) -> tuple[str, list[str]]:
    anno = anno or datetime.now().year
    return ("Copyright", [
        titolo,
        f"Copyright © {anno} {autore}",
        "All rights reserved.",
        "This is a work of fiction. Names, characters, places and incidents are either the "
        "product of the author's imagination or are used fictitiously. Any resemblance to "
        "actual persons, living or dead, events or locales is entirely coincidental.",
        "No part of this book may be reproduced or transmitted in any form or by any means, "
        "electronic or mechanical, without written permission from the author, except for "
        "the use of brief quotations in a book review.",
        f"First edition {anno}",
    ])


def richiesta_recensione(titolo: str, autore: str) -> tuple[str, list[str]]:
    """Onesta e senza incentivi: e' quello che le regole KDP permettono, ed e' anche
    l'unica versione che un lettore non trova sgradevole."""
    return ("A Word Before You Go", [
        f"Thank you for reading {titolo}.",
        "Books like this one live or die on word of mouth. If you have two minutes, an "
        "honest review on Amazon, of any length and any number of stars, helps another "
        "reader decide whether this is a story for them. That is the whole of it.",
        "It matters more than it sounds like it should.",
        # Niente lineetta lunga nemmeno qui: la regola vale per tutto cio' che finisce
        # stampato, non solo per i capitoli. Una firma preceduta da "—" e' proprio il
        # dettaglio che fa dire "scritto dall'AI" nella pagina piu' letta del libro.
        f"With thanks, {autore}",
    ])


def nota_autore(autore: str, bio: str) -> tuple[str, list[str]] | None:
    if not bio or not bio.strip():
        return None
    return ("About the Author", [bio.strip()])


def altri_libri(autore: str, catalogo: list[dict], titolo_corrente: str) -> tuple[str, list[str]] | None:
    """`catalogo` = [{"titolo":..., "autore":..., "sottotitolo":...}] degli altri libri.

    Elenca SOLO i libri dello stesso nome d'autore: un lettore che ha finito un cozy
    fantasy firmato Maren Ashcroft non sta cercando un thriller firmato da un altro nome, e
    mescolarli fa sembrare la pagina una pubblicita'. E' anche la ragione per cui la
    disciplina di catalogo conta: con tre nomi d'autore diversi, questa pagina resta vuota
    su tutti e tre i libri."""
    voci = []
    for libro in catalogo:
        if (libro.get("autore") or "").strip().lower() != (autore or "").strip().lower():
            continue
        titolo = (libro.get("titolo") or "").strip()
        if not titolo or titolo.strip().lower() == titolo_corrente.strip().lower():
            continue
        sottotitolo = (libro.get("sottotitolo") or "").strip()
        voci.append(f"{titolo}" + (f": {sottotitolo}" if sottotitolo else ""))
    if not voci:
        return None
    return (f"Also by {autore}", voci + [
        "Available on Amazon in paperback and for Kindle."])


def catalogo_disponibile(escludi_slug: str = "") -> list[dict]:
    """Gli altri libri del catalogo: prima i pubblicati, poi quelli gia' impacchettati.

    Legge dai file, non da un elenco scritto a mano: un elenco a mano invecchia al secondo
    libro. Non solleva mai — un 'Also by' assente non e' un buon motivo per non consegnare
    un libro."""
    from . import config

    libri: list[dict] = []
    visti: set[str] = set()
    try:
        from . import pubblicazione
        for scheda in pubblicazione.elenco_pubblicati():
            titolo = (scheda.get("titolo") or "").strip()
            if titolo and titolo.lower() not in visti:
                libri.append(scheda)
                visti.add(titolo.lower())
    except Exception:  # noqa: BLE001
        pass

    try:
        import json
        cartella = config.LIBRI_DIR / "in_lavorazione"
        if cartella.exists():
            for progetto in sorted(cartella.iterdir()):
                if not progetto.is_dir() or progetto.name == escludi_slug:
                    continue
                f = progetto / "progetto.json"
                if not f.exists():
                    continue
                cfg = json.loads(f.read_text(encoding="utf-8"))
                titolo = (cfg.get("titolo") or "").strip()
                # Solo i libri gia' arrivati in fondo: un libro a 8 capitoli su 24 non si
                # annuncia in coda a un altro.
                pronto = (config.LIBRI_PRONTI_DIR /
                          _sanitize(titolo)).exists() if titolo else False
                if titolo and pronto and titolo.lower() not in visti:
                    libri.append({"titolo": titolo, "autore": cfg.get("autore", ""),
                                  "sottotitolo": (cfg.get("copy_kdp") or {}).get("sottotitolo", "")})
                    visti.add(titolo.lower())
    except Exception:  # noqa: BLE001
        pass
    return libri


def _sanitize(titolo: str) -> str:
    from . import book_output_manager
    return book_output_manager.sanitize_title(titolo)


def costruisci(titolo: str, autore: str, copy_kdp: dict | None, slug: str = "") -> dict:
    """Tutte le pagine di contorno di un libro, pronte sia per il .docx sia per l'EPUB.

    Ritorna {"iniziali": [(titolo, paragrafi)], "finali": [(titolo, paragrafi)]}."""
    copy_kdp = copy_kdp or {}
    iniziali = [pagina_copyright(titolo, autore)]
    finali = [richiesta_recensione(titolo, autore)]

    altri = altri_libri(autore, catalogo_disponibile(escludi_slug=slug), titolo)
    if altri:
        finali.append(altri)
    nota = nota_autore(autore, copy_kdp.get("bio_autore", ""))
    if nota:
        finali.append(nota)
    return {"iniziali": iniziali, "finali": finali}
