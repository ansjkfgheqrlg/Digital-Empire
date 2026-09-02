"""
Diagnosi: l'agente che guarda tutto il flusso libro e dice come sta davvero (2026-08-30).

Risponde a quattro domande, con misure e non con impressioni:

  1. QUANTO CI VUOLE a fare un libro completo (tempo reale, non stimato)
  2. QUANTO COSTA (dal log delle chiamate al modello, se il flusso automatico ha girato)
  3. DOVE SI BLOCCA (quali gate bocciano, quante volte, per quale motivo)
  4. COSA E' ROTTO adesso (import, dipendenze, comandi, artefatti mancanti)

REGOLA DELLA CASA: niente PASS finti. Se una cosa non e' stata verificata, qui si scrive
"non verificato", non "ok". Un referto che abbellisce e' peggio di nessun referto, perche'
ci si costruisce sopra.

Uso:
    python -m engine.kdp diagnosi              # tutto
    python -m engine.kdp diagnosi --slug X     # un libro solo
    python -m engine.kdp diagnosi --json       # per un altro programma
"""
from __future__ import annotations

import importlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

from . import config

RADICE = Path(__file__).resolve().parent.parent

# I moduli che devono importare perche' il flusso giri. Se uno cade, il flusso e' fermo
# anche se i test passano: e' successo davvero (browser_manager dei caroselli, 27 agosto).
MODULI = [
    "engine.book_project", "engine.gate_blocco", "engine.kdp", "engine.magazzino",
    "engine.metriche", "engine.validators", "engine.kdp_formatter", "engine.epub",
    "engine.copertina_kdp", "engine.paratesto", "engine.story_validator",
    "engine.niche_finder", "engine.amazon_research", "engine.scrittore", "engine.auto",
]

# Dipendenze esterne: (modulo, a cosa serve, blocca il flusso automatico?)
#
# RICAVATE DAGLI IMPORT REALI di engine/*.py, non dedotte. La prima versione di questa
# lista era indovinata e diceva due bugie nel referto (2026-08-30): dava `reportlab` come
# bloccante — il motore non lo usa affatto, il PDF lo fa `docx2pdf` pilotando Word — e
# `ebooklib` come generatore EPUB, che pure non e' importato da nessuna parte. Un referto
# che inventa una diagnosi manda a installare la cosa sbagliata.
DIPENDENZE = [
    ("docx", "scrittura del manoscritto .docx (python-docx)", True),
    ("docx2pdf", "PDF impaginato via Word: senza, niente conteggio pagine REALE", True),
    ("PIL", "copertina: ritaglio 2:3, upscale, controllo proporzioni", False),
    ("pytesseract", "OCR del titolo in copertina (B-016)", False),
]

ARTEFATTI_PACCHETTO = [
    ("*.docx", "manoscritto"),
    ("*.pdf", "PDF (l'unico che conta per le pagine)"),
    ("COPERTINA-PROMPT.md", "prompt copertina"),
    ("KDP_METADATA.txt", "copy Amazon"),
    ("validazione.json", "referto di validazione"),
]


@dataclass
class Referto:
    ambiente: dict = field(default_factory=dict)
    moduli: dict = field(default_factory=dict)
    dipendenze: dict = field(default_factory=dict)
    libri: list = field(default_factory=list)
    tempi: dict = field(default_factory=dict)
    costi: dict = field(default_factory=dict)
    guasti: list = field(default_factory=list)
    avvisi: list = field(default_factory=list)

    @property
    def bloccanti(self) -> list:
        return [g for g in self.guasti if g.get("blocca")]


# --------------------------------------------------------------------- ambiente
def _ambiente(ref: Referto) -> None:
    ref.ambiente["python"] = sys.version.split()[0]
    claude = shutil.which("claude")
    ref.ambiente["claude_cli"] = claude or "ASSENTE"
    if claude:
        try:
            v = subprocess.run(["claude", "--version"], capture_output=True,
                               timeout=60, text=True)
            ref.ambiente["claude_versione"] = (v.stdout or "").strip()[:40]
        except (subprocess.SubprocessError, OSError):
            ref.ambiente["claude_versione"] = "non interrogabile"
    else:
        ref.guasti.append({
            "dove": "ambiente", "blocca": True,
            "cosa": "la CLI `claude` non e' nel PATH: il comando automatico non puo' "
                    "scrivere il testo (e' lo scrittore)",
            "fare": "installare Claude Code, oppure passare allo scrittore via SDK"})


def _moduli(ref: Referto) -> None:
    for nome in MODULI:
        try:
            importlib.import_module(nome)
            ref.moduli[nome] = "ok"
        except Exception as e:
            ref.moduli[nome] = "%s: %s" % (type(e).__name__, str(e)[:120])
            ref.guasti.append({
                "dove": nome, "blocca": True,
                "cosa": "il modulo non importa: %s" % str(e)[:120],
                "fare": "correggere l'import prima di qualunque run"})


def _dipendenze(ref: Referto) -> None:
    for modulo, a_cosa, blocca in DIPENDENZE:
        try:
            importlib.import_module(modulo)
            ref.dipendenze[modulo] = "ok"
        except ImportError:
            ref.dipendenze[modulo] = "ASSENTE"
            voce = {"dove": "dipendenza %s" % modulo, "blocca": blocca,
                    "cosa": "manca %s, serve per: %s" % (modulo, a_cosa),
                    "fare": "pip install %s" % modulo}
            (ref.guasti if blocca else ref.avvisi).append(
                voce if blocca else "%s assente (%s)" % (modulo, a_cosa))


# ------------------------------------------------------------------------ libri
def _pagine_reali(cartella: Path) -> tuple[int | None, str]:
    """Pagine REALI dal PDF. Torna (pagine, nota) — la nota distingue i casi.

    E' l'unico numero che conta: la stima a parole ha sbagliato di 8 pagine su
    The Winter Term (120,9 stimate contro 113 reali).

    Usa `book_output_manager.conta_pagine_pdf`, che conta dai byte grezzi e non richiede
    nessuna libreria. La prima versione qui usava `pypdf`, non installato, e stampava
    "no PDF" su libri che il PDF ce l'hanno eccome: confondere "file assente" con "non so
    leggerlo" e' un falso negativo, cioe' la stessa bugia dei PASS finti al contrario.
    """
    pdf = next(iter(cartella.glob("*.pdf")), None)
    if not pdf:
        return None, "nessun PDF nel pacchetto"
    try:
        from .book_output_manager import conta_pagine_pdf
        n = conta_pagine_pdf(pdf)
    except Exception as e:
        return None, "PDF presente ma illeggibile (%s)" % type(e).__name__
    if not n:
        return None, "PDF presente ma il conteggio pagine non riesce"
    return n, ""


def _libri(ref: Referto, solo_slug: str | None = None) -> None:
    from .book_project import BookProject, lista_progetti
    from . import metriche

    minuti = []
    for slug in sorted(lista_progetti()):
        if solo_slug and slug != solo_slug:
            continue
        voce = {"slug": slug}
        try:
            p = BookProject(slug)
            st = p.stato()
            voce.update(titolo=st.titolo, capitoli="%d/%d" % (len(st.capitoli_scritti),
                                                              st.capitoli_totali),
                        parole=st.parole_scritte, completo=st.completo)
        except Exception as e:
            voce["errore"] = "%s: %s" % (type(e).__name__, str(e)[:100])
            ref.libri.append(voce)
            ref.guasti.append({"dove": "libro %s" % slug, "blocca": False,
                               "cosa": "stato illeggibile: %s" % str(e)[:100],
                               "fare": "controllare progetto.json"})
            continue

        r = metriche.riepilogo(slug)
        voce["eventi"] = r.eventi
        voce["minuti"] = r.minuti_totali
        voce["gate_bocciati"] = r.blocchi_bocciati
        voce["gate_passati"] = r.blocchi_passati
        voce["motivi_bocciatura"] = r.motivi_bocciatura
        if r.minuti_totali:
            minuti.append(r.minuti_totali)

        # pacchetto consegnato?
        pronti = config.LIBRI_DIR / "libri_pronti" if hasattr(config, "LIBRI_DIR") else None
        cartella = None
        if pronti and pronti.exists():
            for d in pronti.iterdir():
                if d.is_dir() and d.name.lower().replace("_", "-").startswith(slug[:12]):
                    cartella = d
                    break
        if cartella:
            mancanti = [etichetta for schema, etichetta in ARTEFATTI_PACCHETTO
                        if not list(cartella.glob(schema))]
            voce["pacchetto"] = cartella.name
            voce["artefatti_mancanti"] = mancanti
            voce["pagine_pdf"], voce["nota_pdf"] = _pagine_reali(cartella)
            copertina = list(cartella.glob("*.png")) + list(cartella.glob("*.jpg"))
            voce["copertina"] = bool(copertina)
            if mancanti:
                ref.guasti.append({
                    "dove": "pacchetto %s" % cartella.name, "blocca": False,
                    "cosa": "mancano artefatti: %s" % ", ".join(mancanti),
                    "fare": "python -m engine.kdp pacchetto %s" % slug})
            if not copertina:
                ref.avvisi.append("%s: pacchetto senza copertina -> NON caricabile su KDP"
                                  % cartella.name)
        else:
            voce["pacchetto"] = None
            if voce.get("completo"):
                ref.avvisi.append("%s: capitoli completi ma nessun pacchetto consegnato"
                                  % slug)
        ref.libri.append(voce)

    if minuti:
        ref.tempi = {
            "libri_misurati": len(minuti),
            "minuti_min": round(min(minuti), 1),
            "minuti_max": round(max(minuti), 1),
            "minuti_medi": round(sum(minuti) / len(minuti), 1),
        }
    else:
        ref.tempi = {"libri_misurati": 0,
                     "nota": "nessun libro ha metriche: sono state introdotte il 2026-08-23"}


# ------------------------------------------------------------------------ costi
def _costi(ref: Referto) -> None:
    """Dal log reale delle chiamate al modello. Se non c'e', si dice che non c'e'."""
    log = RADICE / "LIBRI" / "chiamate.jsonl"
    if not log.exists():
        ref.costi = {"stato": "nessun dato",
                     "nota": "il flusso automatico non ha ancora girato: nessun costo "
                             "misurato. Le stime a priori non si scrivono qui."}
        return
    voci, per_libro = [], {}
    for riga in log.read_text(encoding="utf-8").splitlines():
        try:
            voci.append(json.loads(riga))
        except json.JSONDecodeError:
            continue
    for v in voci:
        libro = (v.get("etichetta") or "?").split("/")[0]
        per_libro.setdefault(libro, {"chiamate": 0, "costo": 0.0, "falliti": 0})
        per_libro[libro]["chiamate"] += 1
        per_libro[libro]["costo"] += v.get("costo_usd", 0.0)
        if not v.get("ok"):
            per_libro[libro]["falliti"] += 1
    ref.costi = {
        "stato": "misurato",
        "chiamate_totali": len(voci),
        "costo_totale_usd": round(sum(v.get("costo_usd", 0.0) for v in voci), 4),
        "chiamate_fallite": sum(1 for v in voci if not v.get("ok")),
        "per_libro": {k: {"chiamate": d["chiamate"], "costo_usd": round(d["costo"], 4),
                          "falliti": d["falliti"]} for k, d in per_libro.items()},
    }


# ----------------------------------------------------------------------- report
def esegui(solo_slug: str | None = None) -> Referto:
    ref = Referto()
    _ambiente(ref)
    _moduli(ref)
    _dipendenze(ref)
    try:
        _libri(ref, solo_slug)
    except Exception as e:
        ref.guasti.append({"dove": "analisi libri", "blocca": True,
                           "cosa": "%s: %s" % (type(e).__name__, str(e)[:150]),
                           "fare": "controllare LIBRI/"})
    _costi(ref)
    return ref


def stampa(ref: Referto) -> None:
    print("=" * 74)
    print(" DIAGNOSI FLUSSO LIBRO")
    print("=" * 74)

    print("\n-- AMBIENTE --")
    for k, v in ref.ambiente.items():
        print("   %-18s %s" % (k, v))

    rotti = {k: v for k, v in ref.moduli.items() if v != "ok"}
    print("\n-- MOTORE --")
    print("   moduli: %d/%d importano" % (len(ref.moduli) - len(rotti), len(ref.moduli)))
    for k, v in rotti.items():
        print("   [X] %s -> %s" % (k, v))
    mancanti = {k: v for k, v in ref.dipendenze.items() if v != "ok"}
    print("   dipendenze: %d/%d presenti" % (len(ref.dipendenze) - len(mancanti),
                                             len(ref.dipendenze)))
    for k in mancanti:
        print("   [!] %s assente" % k)

    print("\n-- LIBRI --")
    if not ref.libri:
        print("   nessun progetto")
    for L in ref.libri:
        if "errore" in L:
            print("   [X] %-26s %s" % (L["slug"], L["errore"]))
            continue
        pag = L.get("pagine_pdf")
        stato_pdf = ("%d pag" % pag) if pag else (L.get("nota_pdf") or "nessun pacchetto")
        print("   %-26s %-7s %6d parole  %s%s"
              % (L["slug"], L.get("capitoli", "?"), L.get("parole", 0), stato_pdf,
                 "  [no copertina]" if L.get("pacchetto") and not L.get("copertina") else ""))
        if L.get("minuti"):
            print("       tempo %.1f min | gate: %d passati, %d bocciati"
                  % (L["minuti"], L.get("gate_passati", 0), L.get("gate_bocciati", 0)))
        for m in L.get("motivi_bocciatura", [])[:2]:
            print("         bocciato per: %s" % m)

    print("\n-- TEMPO PER LIBRO --")
    if ref.tempi.get("libri_misurati"):
        print("   misurati %d libri: min %.1f / medio %.1f / max %.1f minuti"
              % (ref.tempi["libri_misurati"], ref.tempi["minuti_min"],
                 ref.tempi["minuti_medi"], ref.tempi["minuti_max"]))
    else:
        print("   %s" % ref.tempi.get("nota", "nessun dato"))

    print("\n-- COSTO --")
    if ref.costi.get("stato") == "misurato":
        print("   %d chiamate, $%.4f totali, %d fallite"
              % (ref.costi["chiamate_totali"], ref.costi["costo_totale_usd"],
                 ref.costi["chiamate_fallite"]))
        for libro, d in ref.costi["per_libro"].items():
            print("     %-26s %2d chiamate  $%.4f  (%d fallite)"
                  % (libro, d["chiamate"], d["costo_usd"], d["falliti"]))
    else:
        print("   %s" % ref.costi.get("nota"))

    print("\n-- GUASTI --")
    if not ref.guasti:
        print("   nessuno")
    for g in ref.guasti:
        print("   %s %s: %s" % ("[X]" if g["blocca"] else "[!]", g["dove"], g["cosa"]))
        print("       -> %s" % g["fare"])
    for a in ref.avvisi:
        print("   [!] %s" % a)

    print("\n-- VERDETTO --")
    if ref.bloccanti:
        print("   FLUSSO BLOCCATO: %d guasti bloccanti (sopra, con [X])." % len(ref.bloccanti))
    else:
        print("   Nessun guasto bloccante: il flusso puo' girare.")
    print()


def come_json(ref: Referto) -> str:
    return json.dumps(asdict(ref), ensure_ascii=False, indent=2)
