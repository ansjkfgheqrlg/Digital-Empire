"""
Copertina KDP — porta a norma un'immagine di copertina ARRIVATA DA FUORI (2026-08-15).

NUOVO MODELLO DI LAVORO: l'immagine non la genera piu' nessun automatismo. Claude scrive un
prompt completo (scena, stile, effetti, e il TESTO della copertina), Gael lo usa sul suo
modello di immagini e salva il PNG. Da li' in poi lavora questo modulo: ritaglio al formato
KDP, risoluzione, verifica.

PERCHE' E' UN FILE NUOVO E NON UNA PARTE DI `cover_generator.py`: quel modulo importa
`lmarena_client` e `playwright` a livello di modulo, quindi archiviando l'automazione Arena
anche queste funzioni — che sono solo Pillow e non hanno mai avuto niente a che fare con un
modello — sarebbero diventate non importabili. Sono state SPOSTATE identiche, non riscritte:
ogni riga qui sotto ha gia' prodotto una copertina vera (The Quiet Hours, 2026-08-08).

Sequenza tipica su un PNG appena consegnato:

    verifica_copertina_kdp(png)      # va gia' bene cosi'?
    kdp = adatta_a_kdp(png)          # 2:3, 1800x2700 (6x9in @300dpi)
    verifica_copertina_kdp(kdp)      # controprova
    # e, se il titolo NON e' gia' disegnato dentro l'immagine:
    finale = aggiungi_titolo(kdp, titolo, autore)

Il controllo che il titolo sia davvero leggibile e scritto giusto vive altrove ed e' OCR,
non un modello: `validators.valida_copertina_testo`.
"""
from __future__ import annotations

from pathlib import Path

# Requisiti KDP reali per una copertina 6x9in (fonte: kdp.amazon.com, cover guidelines):
# rapporto altezza/larghezza 1.5, minimo 300 DPI sul trim con abbondanza.
KDP_ASPECT_RATIO = 1.5
KDP_ASPECT_TOLERANCE = 0.05
KDP_MIN_WIDTH_PX = 1600   # sotto questa larghezza KDP segnala bassa risoluzione


def verifica_copertina_kdp(path: Path) -> dict:
    """Controlla che l'immagine sia davvero utilizzabile su KDP (2026-08-08).

    Nato da un caso reale: la prima copertina generata per "The Quiet Hours" era bella e
    coerente ma **quadrata 1024x1024**, cioe' inutilizzabile per un 6x9 — e il codice
    l'aveva accettata perche' controllava solo che il file esistesse e pesasse piu' di 5KB.
    Un controllo sulla dimensione del file non dice NIENTE sull'usabilita': serve guardare
    le proporzioni e la risoluzione, come farebbe KDP al caricamento."""
    from PIL import Image

    with Image.open(path) as im:
        w, h = im.size
    ratio = h / w if w else 0
    problemi = []
    if abs(ratio - KDP_ASPECT_RATIO) > KDP_ASPECT_TOLERANCE:
        problemi.append(
            f"proporzioni sbagliate: 1:{ratio:.2f} invece di 1:{KDP_ASPECT_RATIO} "
            f"(6x9in) — KDP rifiuta o deforma"
        )
    if w < KDP_MIN_WIDTH_PX:
        problemi.append(f"risoluzione bassa: {w}px di larghezza, minimo {KDP_MIN_WIDTH_PX}px")
    return {"larghezza": w, "altezza": h, "rapporto": round(ratio, 3),
            "ok": not problemi, "problemi": problemi}


def adatta_a_kdp(src: Path, dest: Path | None = None,
                  larghezza_finale: int = 1800) -> Path:
    """Trasforma un'immagine qualsiasi in una copertina conforme a KDP (6x9in, 300 DPI).

    Perche' serve (2026-08-08): i modelli immagine restituiscono spesso un quadrato
    1024x1024 qualunque cosa chieda il prompt — verificato chiedendo il formato verticale
    sia in coda sia in apertura, in maiuscolo, con le proporzioni esplicite. Invece di
    rigenerare all'infinito sperando in un formato diverso, si adatta l'immagine ottenuta:
    deterministico, ripetibile, indipendente da chi l'ha prodotta.

    Come: ritaglio CENTRATO al rapporto 2:3 (i soggetti generati stanno praticamente
    sempre al centro), poi ingrandimento a risoluzione KDP con LANCZOS.

    Limite dichiarato, non nascosto: partendo da 1024px si ingrandisce di ~2.6x, quindi la
    resa e' buona ma non pari a un'illustrazione nativa ad alta risoluzione. Se il modello
    di immagini puo' produrre direttamente un 2:3 ad alta risoluzione, e' meglio — questa
    funzione lo rileva e non degrada nulla inutilmente."""
    from PIL import Image

    src = Path(src)
    dest = dest or src.with_name(src.stem + "_kdp.png")
    altezza_finale = int(larghezza_finale * KDP_ASPECT_RATIO)

    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        # ritaglio centrato al rapporto corretto
        if h / w < KDP_ASPECT_RATIO:          # troppo larga: taglio ai lati
            nuova_w = int(h / KDP_ASPECT_RATIO)
            sinistra = (w - nuova_w) // 2
            im = im.crop((sinistra, 0, sinistra + nuova_w, h))
        else:                                  # troppo alta: taglio sopra/sotto
            nuova_h = int(w * KDP_ASPECT_RATIO)
            alto = (h - nuova_h) // 2
            im = im.crop((0, alto, w, alto + nuova_h))
        im = im.resize((larghezza_finale, altezza_finale), Image.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, "PNG")

    print(f"[cover] adattata a KDP: {dest.name} ({larghezza_finale}x{altezza_finale}, 6x9in @300dpi)")
    return dest


def _font(dimensione: int):
    """Carica un font di sistema leggibile. Ordine di preferenza: serif eleganti prima
    (stanno bene su un thriller), poi qualunque cosa esista, poi il font di default."""
    from PIL import ImageFont
    candidati = ["georgiab.ttf", "timesbd.ttf", "constanb.ttf", "arialbd.ttf", "segoeuib.ttf"]
    for nome in candidati:
        try:
            return ImageFont.truetype(nome, dimensione)
        except OSError:
            continue
    return ImageFont.load_default()


def aggiungi_titolo(cover_path: Path, titolo: str, autore: str = "Digital Empire",
                     dest: Path | None = None) -> Path:
    """Scrive titolo e autore sulla copertina con un font vero.

    RETE DI SICUREZZA, non piu' il percorso normale (2026-08-15). Dal nuovo flusso il titolo
    lo disegna il modello di immagini, perche' il prompt glielo chiede esplicitamente: in
    quel caso questa funzione NON va chiamata, altrimenti il titolo compare due volte.
    Serve quando l'immagine arriva senza testo, o col testo sbagliato — e il caso e' gia'
    successo davvero: un modello aveva scritto "New Voicemail" troncando "1 New Voicemail",
    ed e' il motivo per cui questa funzione fu scritta il 2026-08-10.

    Composizione: fascia scura semitrasparente in alto per il titolo (garantisce leggibilita'
    qualunque sia l'illustrazione sotto) e una in basso per l'autore."""
    from PIL import Image, ImageDraw

    cover_path = Path(cover_path)
    dest = dest or cover_path.with_name(cover_path.stem + "_titolo.png")

    with Image.open(cover_path) as im:
        im = im.convert("RGB")
        L, H = im.size
        disegno = ImageDraw.Draw(im, "RGBA")

        # --- titolo: a capo automatico per stare nei margini ------------------ #
        dim = int(L * 0.13)
        margine = int(L * 0.08)
        larghezza_max = L - 2 * margine
        while dim > 20:
            font = _font(dim)
            parole, righe, riga = titolo.upper().split(), [], ""
            for p in parole:
                prova = f"{riga} {p}".strip()
                if disegno.textlength(prova, font=font) <= larghezza_max:
                    riga = prova
                else:
                    if riga:
                        righe.append(riga)
                    riga = p
            if riga:
                righe.append(riga)
            if len(righe) <= 3:
                break
            dim = int(dim * 0.9)

        alt_riga = int(dim * 1.25)
        alt_blocco = alt_riga * len(righe)
        cima = int(H * 0.06)
        disegno.rectangle([0, cima - int(alt_riga * 0.4),
                            L, cima + alt_blocco + int(alt_riga * 0.35)], fill=(0, 0, 0, 165))
        for i, riga in enumerate(righe):
            w = disegno.textlength(riga, font=font)
            y = cima + i * alt_riga
            disegno.text(((L - w) / 2 + 3, y + 3), riga, font=font, fill=(0, 0, 0, 190))
            disegno.text(((L - w) / 2, y), riga, font=font, fill=(255, 255, 255, 255))

        # --- autore in basso -------------------------------------------------- #
        font_a = _font(int(L * 0.055))
        testo_a = autore.upper()
        wa = disegno.textlength(testo_a, font=font_a)
        ya = int(H * 0.90)
        disegno.rectangle([0, ya - int(L * 0.025), L, ya + int(L * 0.085)], fill=(0, 0, 0, 165))
        disegno.text(((L - wa) / 2 + 2, ya + 2), testo_a, font=font_a, fill=(0, 0, 0, 190))
        disegno.text(((L - wa) / 2, ya), testo_a, font=font_a, fill=(238, 232, 220, 255))

        im.save(dest, "PNG")

    print(f"[cover] titolo scritto sulla copertina: {dest.name}")
    return dest


def prepara_copertina(src: Path, titolo: str, autore: str = "Digital Empire",
                       dest_dir: Path | None = None,
                       titolo_gia_in_copertina: bool = True) -> dict:
    """Porta un PNG consegnato da fuori fino a essere una copertina KDP valida.

    `titolo_gia_in_copertina=True` (default, il nuovo modo di lavorare): il titolo l'ha
    disegnato il modello di immagini seguendo il prompt, quindi NON si sovrascrive niente.
    Metterlo a False fa scrivere titolo e autore con Pillow — la rete di sicurezza.

    Ritorna un dizionario con il path finale e l'esito della verifica, cosi' chi chiama
    sa se e' utilizzabile senza doverlo ricontrollare da solo."""
    src = Path(src)
    if not src.exists():
        raise FileNotFoundError(f"Copertina non trovata: {src}")

    dest_dir = Path(dest_dir) if dest_dir else src.parent
    prima = verifica_copertina_kdp(src)
    print(f"[cover] in ingresso: {prima['larghezza']}x{prima['altezza']} "
          f"(rapporto 1:{prima['rapporto']}) — {'gia a norma' if prima['ok'] else 'da adattare'}")

    kdp = adatta_a_kdp(src, dest_dir / f"{src.stem}_kdp.png")
    finale = kdp
    if not titolo_gia_in_copertina:
        finale = aggiungi_titolo(kdp, titolo, autore, dest_dir / f"{src.stem}_finale.png")

    esito = verifica_copertina_kdp(finale)
    for p in esito["problemi"]:
        print(f"[cover] ATTENZIONE: {p}")
    return {"path": finale, "verifica": esito, "originale": prima}
