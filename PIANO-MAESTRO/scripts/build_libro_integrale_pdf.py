"""
build_libro_integrale_pdf.py — il costruttore del Libro dell'Agency, Edizione Integrale.

Si rilancia dopo ogni ondata di scrittura: il libro cresce e si vede crescere (piano 35,
C1.3). Prende cio' che esiste in `capitoli/`, lo mette in ordine di tassonomia, genera gli
apparati da codice (sommario con numeri di pagina, indice delle fonti, indice di TUTTI gli
atomi) e produce:

    PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.md     (sorgente unica, tutto il libro)
    PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.html
    PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.pdf
    + doppione in  documentazione Empire/Piani/Agency/   (legge emperator.md 6.17)

Due passate di stampa: la prima per sapere su che pagina cade ogni capitolo, la seconda per
stampare il sommario coi numeri veri. Non si stima: si rilegge il PDF.

Console Windows cp1252: nessuna emoji nei print.
"""

from __future__ import annotations

import io
import json
import os
import re
import shutil
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_engine_libro import LibroDoc   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
CAP_DIR = os.path.join(OUT_DIR, "capitoli")
NOME = "36-LIBRO-AGENCY-INTEGRALE"
DOPPIONE_DIR = os.path.join(REPO, "documentazione Empire", "Piani", "Agency")

MARCATORE = re.compile(r"\[\[([^\]\[]+?)\]\]")
BLOCCO_DE = "#### Cosa fa Digital Empire su questo punto"


def chiave_cap(c: str):
    l, n = c.split(".")
    return (l, int(n))


def carica(nome):
    with open(os.path.join(OUT_DIR, nome), encoding="utf-8") as fh:
        return json.load(fh)


def parti_di(codice: str) -> list[str]:
    if not os.path.isdir(CAP_DIR):
        return []
    return sorted(f for f in os.listdir(CAP_DIR)
                  if f == "%s.md" % codice or (f.startswith("%s-" % codice) and f.endswith(".md")))


def leggi_capitolo(codice: str) -> tuple[str, str]:
    """Ritorna (corpo, blocco_de). Le parti si fondono; il blocco DE si prende una volta sola
    per parte e si concatena."""
    corpo, de = [], []
    for f in parti_di(codice):
        with open(os.path.join(CAP_DIR, f), encoding="utf-8") as fh:
            testo = fh.read()
        if BLOCCO_DE in testo:
            prima, dopo = testo.split(BLOCCO_DE, 1)
            corpo.append(prima.strip())
            de.append(dopo.strip())
        else:
            corpo.append(testo.strip())
    return "\n\n".join(corpo), "\n\n".join(de)


def marcatori_in_html(md: str, per_uid: dict) -> str:
    def sost(m):
        uid = m.group(1).strip()
        a = per_uid.get(uid)
        if not a:
            return "<sup class='kref'>%s</sup>" % uid
        return "<sup class='kref'>%s</sup>" % a["ka_id"]
    return MARCATORE.sub(sost, md)


def main() -> int:
    tass = carica("TASSONOMIA.json")
    indice = carica("atomi-index.json")
    atomi = indice["atomi"]
    per_uid = {a["uid"]: a for a in atomi}
    libri = tass["libri"]
    capitoli = tass["capitoli"]

    per_libro = defaultdict(list)
    for cap in capitoli:
        if cap == "FUORI":
            continue
        per_libro[cap.split(".")[0]].append(cap)

    scritti = [c for c in capitoli if c != "FUORI" and parti_di(c)]
    print("capitoli scritti: %d su %d" % (len(scritti), len(capitoli) - 1))
    if not scritti:
        print("niente da costruire")
        return 1

    # ------------------------------------------------------------ sorgente MD unica
    md_tot = ["# Il Libro dell'Agency — Edizione Integrale\n"]
    for libro in ("I", "II", "III", "IV", "V", "VI", "VII"):
        md_tot.append("\n\n# Libro %s — %s\n" % (libro, libri[libro]))
        for cap in per_libro[libro]:
            corpo, de = leggi_capitolo(cap)
            if not corpo:
                continue
            md_tot.append("\n\n## %s — %s\n\n%s\n\n%s\n\n%s\n" % (cap, capitoli[cap], corpo, BLOCCO_DE, de))
    with io.open(os.path.join(ROOT, NOME + ".md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("".join(md_tot))

    # ------------------------------------------------------------ costruzione HTML
    def costruisci(pagine_di: dict[str, int] | None) -> LibroDoc:
        doc = LibroDoc(
            titolo="Il Libro dell'Agency — Edizione Integrale",
            out_html=os.path.join(ROOT, NOME + ".html"),
            out_pdf=os.path.join(ROOT, NOME + ".pdf"),
        )
        n_atomi = sum(1 for a in atomi if not a.get("principale_di"))
        n_portanti = sum(1 for a in atomi if not a.get("principale_di") and a["peso"] == "portante")
        doc.copertina(
            "Digital Empire · Edizione Integrale",
            "Il Libro <span class='soft'>dell'Agency.</span>",
            "Tutta la formazione acquisita dall'Impero, organizzata per argomento e non per fonte: "
            "ogni atomo di conoscenza citato, ogni fonte tracciata, ogni capitolo chiuso da cio' "
            "che Digital Empire fa davvero su quel punto.",
            [("Atomi di conoscenza", "%d" % n_atomi),
             ("Di cui portanti", "%d" % n_portanti),
             ("Capitoli scritti", "%d su %d" % (len(scritti), len(capitoli) - 1)),
             ("Libri", "8")],
        )

        # sommario (coi numeri di pagina alla seconda passata)
        voci = []
        for libro in ("I", "II", "III", "IV", "V", "VI", "VII", "VIII"):
            voci.append("<div class='libro'>Libro %s — %s</div>" % (libro, libri[libro]))
            if libro == "VIII":
                for c, t in (("VIII.1", "Indice delle fonti"), ("VIII.2", "Indice degli atomi")):
                    p = (pagine_di or {}).get(c, "")
                    voci.append("<div class='voce'><span class='c'>%s</span><span>%s</span>"
                                "<span class='p'>%s</span></div>" % (c, t, p))
                continue
            for cap in per_libro[libro]:
                stato = "" if parti_di(cap) else " <span style='color:var(--text-3)'>(non ancora scritto)</span>"
                p = (pagine_di or {}).get(cap, "")
                voci.append("<div class='voce'><span class='c'>%s</span><span>%s%s</span>"
                            "<span class='p'>%s</span></div>" % (cap, capitoli[cap], stato, p))
        doc.grezzo("<section class='cap-apre'><div class='occhiello'>Sommario</div>"
                   "<h2 class='cap-t'>Cosa c'e' <span class='soft'>e dove.</span></h2>"
                   "<div class='sommario'>%s</div></section>" % "".join(voci))

        # i sette libri
        for libro in ("I", "II", "III", "IV", "V", "VI", "VII"):
            caps = per_libro[libro]
            n_at = sum(1 for a in atomi if not a.get("principale_di") and a["libro"] == libro)
            doc.apertura_libro(
                libro, libri[libro],
                "%d atomi di conoscenza, %d capitoli." % (n_at, len(caps)),
                [(c, capitoli[c] + ("" if parti_di(c) else " — non ancora scritto")) for c in caps],
            )
            for cap in caps:
                corpo, de = leggi_capitolo(cap)
                if not corpo:
                    continue
                doc.capitolo(
                    cap, capitoli[cap],
                    marcatori_in_html(corpo, per_uid),
                    blocco_de=marcatori_in_html(de, per_uid) if de else "",
                )

        # ------------------------------------------------ Libro VIII — apparati
        doc.apertura_libro("VIII", libri["VIII"],
                           "Generati da codice, non scritti a mano: l'indice delle fonti e "
                           "l'indice di tutti gli atomi, nessuno escluso.",
                           [("VIII.1", "Indice delle fonti"), ("VIII.2", "Indice degli atomi")])

        # VIII.1 — fonti: run -> capitoli in cui compare
        per_run = defaultdict(lambda: defaultdict(int))
        for a in atomi:
            if a.get("capitolo") and a["capitolo"] != "FUORI":
                per_run[a["run"]][a["capitolo"]] += 1
        righe = ["| Fonte (run) | Atomi | Capitoli in cui entra |", "|---|---|---|"]
        for run in sorted(per_run, key=lambda r: -sum(per_run[r].values())):
            caps = sorted(per_run[run], key=chiave_cap)
            righe.append("| `%s` | %d | %s |" % (run, sum(per_run[run].values()),
                                                  ", ".join(caps)))
        doc.capitolo("VIII.1", "Indice delle fonti", "\n".join(righe))

        # VIII.2 — tutti gli atomi, compatti; i doppioni sotto il principale
        doppioni = defaultdict(list)
        for a in atomi:
            if a.get("principale_di"):
                doppioni[a["principale_di"]].append(a["uid"])
        blocchi = []
        ordinati = sorted((a for a in atomi if not a.get("principale_di")),
                          key=lambda a: (chiave_cap(a["capitolo"]) if a["capitolo"] not in (None, "FUORI")
                                         else ("Z", 0), a["run"], a["ka_id"]))
        for a in ordinati:
            testo = a["contenuto"].replace("|", "/").replace("\n", " ")
            if a["peso"] != "contesto":
                testo = testo[:160] + ("…" if len(testo) > 160 else "")
            extra = ""
            if doppioni.get(a["uid"]):
                extra = " <span style='color:var(--text-3)'>— detto anche da: %s</span>" % ", ".join(
                    doppioni[a["uid"]][:4])
            blocchi.append("<div class='app-atomo'><span class='u'>%s</span><span class='c'>%s · %s</span>"
                           "<span>%s%s</span></div>"
                           % (a["uid"], a["capitolo"] or "—", (a["peso"] or "—")[:4], testo, extra))
        doc.grezzo("<section class='cap-apre'><div class='occhiello'>Capitolo VIII.2</div>"
                   "<h2 class='cap-t'>Indice degli atomi</h2>"
                   "<p class='lead'>%d atomi unici, in ordine di capitolo. Gli atomi di contesto "
                   "compaiono qui per intero: e' il loro posto nel libro.</p>%s</section>"
                   % (len(ordinati), "".join(blocchi)))
        return doc

    # ---------------------------------------------- passata 1: dove cade ogni capitolo
    print("[passata 1] stampa per trovare le pagine dei capitoli...")
    doc = costruisci(None)
    doc.build()
    from pypdf import PdfReader
    lettore = PdfReader(doc.out_pdf)
    pagine_di: dict[str, int] = {}
    for i, p in enumerate(lettore.pages, 1):
        t = (p.extract_text() or "")
        for m in re.finditer(r"Capitolo ([IVX]+\.\d+)", t):
            pagine_di.setdefault(m.group(1), i)

    # ---------------------------------------------- passata 2: sommario coi numeri veri
    print("[passata 2] stampa definitiva col sommario...")
    doc = costruisci(pagine_di)
    n = doc.build()

    # ---------------------------------------------- doppione + riepilogo
    os.makedirs(DOPPIONE_DIR, exist_ok=True)
    shutil.copy2(doc.out_pdf, os.path.join(DOPPIONE_DIR, NOME + ".pdf"))
    print("[ok] doppione -> %s" % os.path.join(DOPPIONE_DIR, NOME + ".pdf"))

    parole = sum(len(leggi_capitolo(c)[0].split()) for c in scritti)
    print("")
    print("LIBRO: %d pagine, %d capitoli scritti su %d, %d parole di corpo"
          % (n, len(scritti), len(capitoli) - 1, parole))
    print("sorgente: %s" % os.path.join(ROOT, NOME + ".md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
