"""
Il libro di oggi: un comando, e parte (2026-09-02).

    python -m engine.kdp libro-del-giorno            # apre il libro di oggi dal piano
    python -m engine.kdp libro-del-giorno --auto     # e lo scrive tutto, senza fermarsi

NON IMPROVVISA MAI. Se il piano della settimana non c'e', si ferma e dice di lanciare
`kdp piano`. Un comando che inventa quando gli manca l'input e' esattamente il modo in cui
e' nato B-018: quattro libri, quattro nicchie, tre nomi d'autore, e la pagina "Also by" vuota
su tutti.

REGOLA 6, NON NEGOZIABILE: se c'e' gia' un libro aperto e incompleto, si finisce QUELLO.
Aprirne un altro sopra e' il modo in cui si accumulano quattro libri a meta'.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from . import metriche, piano as mod_piano
from .book_project import BookProject, lista_progetti, slugify


@dataclass
class EsitoGiorno:
    ok: bool = False
    giorno: int = 0
    titolo: str = ""
    slug: str = ""
    riga: dict = field(default_factory=dict)
    errore: str = ""
    ripresa: bool = False          # True se si riprende un libro gia' aperto

    def __str__(self) -> str:
        r = ["", "=" * 74,
             " LIBRO DEL GIORNO — %s" % ("PRONTO" if self.ok else "FERMO"),
             "=" * 74]
        if self.riga:
            d = self.riga.get("dati_amazon", {})
            r += ["  giorno    : %d (%s)" % (self.giorno, self.riga.get("data_produzione")),
                  "  titolo    : %s" % self.riga.get("titolo_lavoro"),
                  "  nicchia   : %s (punteggio %s, misurato il %s)"
                  % (self.riga.get("nicchia"), self.riga.get("punteggio_nicchia"),
                     d.get("misurato_il")),
                  "  autore    : %s" % self.riga.get("autore"),
                  "  slug      : %s" % self.slug]
            if self.riga.get("angolo_differenziante"):
                r.append("  angolo    : %s" % self.riga["angolo_differenziante"][:100])
        if self.ripresa:
            r += ["", "  RIPRESA: c'era gia' un libro aperto e incompleto.",
                  "  Regola 6: si finisce quello prima di aprirne un altro."]
        if self.errore:
            r += ["", "  %s" % self.errore]
        elif self.ok:
            r += ["", "  Prossimo passo: scrivi i capitoli a blocchi e dopo OGNI blocco",
                  "    python -m engine.kdp blocco %s" % self.slug,
                  "  Oppure lascia fare tutto al flusso automatico:",
                  "    python -m engine.kdp auto --slug %s" % self.slug]
        r.append("")
        return "\n".join(r)


def _incompleto() -> str | None:
    """Il primo libro aperto e non finito, se c'e'. E' la Regola 6."""
    for slug in sorted(lista_progetti()):
        try:
            if not BookProject(slug).stato().completo:
                return slug
        except Exception:
            continue
    return None


def apri(oggi: date | None = None, forza_giorno: int | None = None) -> EsitoGiorno:
    e = EsitoGiorno()
    oggi = oggi or date.today()

    dati = mod_piano.carica_piano(oggi)
    if dati is None:
        e.errore = ("nessun piano per la settimana del %s.\n"
                    "  Lancia prima:  python -m engine.kdp piano\n"
                    "  Non invento un libro a caso: e' cosi' che e' nato B-018."
                    % mod_piano.lunedi_di(oggi).isoformat())
        return e

    righe = dati.get("righe") or []
    giorno = forza_giorno or (oggi - mod_piano.lunedi_di(oggi)).days + 1
    e.giorno = giorno
    riga = next((r for r in righe if int(r.get("giorno", 0)) == giorno), None)
    if riga is None:
        e.errore = ("il piano della settimana non ha una riga per il giorno %d "
                    "(ne ha %d). Rigenera il piano o indica --giorno."
                    % (giorno, len(righe)))
        return e
    e.riga = riga
    e.titolo = str(riga.get("titolo_lavoro") or "")

    # --- Regola 6: prima si finisce quello che e' aperto --------------------- #
    aperto = _incompleto()
    if aperto:
        atteso = slugify(e.titolo)
        e.slug, e.ripresa, e.ok = aperto, True, True
        if aperto != atteso:
            e.errore = ("c'e' un libro aperto e incompleto: '%s'. Regola 6: si finisce "
                        "QUELLO prima di aprire '%s'. Se e' da abbandonare, dillo "
                        "esplicitamente e cancella la sua cartella." % (aperto, atteso))
            e.ok = False
        return e

    # --- apertura del progetto ---------------------------------------------- #
    try:
        p = BookProject.crea(e.titolo, str(riga.get("nicchia") or ""),
                             str(riga.get("autore") or "Digital Empire"),
                             int(riga.get("struttura_prevista", {}).get("capitoli", 24)),
                             int(riga.get("struttura_prevista", {})
                                 .get("parole_per_capitolo", 1600)))
    except FileExistsError:
        e.slug = slugify(e.titolo)
        e.errore = "il progetto '%s' esiste gia'." % e.slug
        return e

    # La riga del piano entra NEL progetto: chi lo riprende fra tre giorni trova
    # premessa e angolo li' dentro, non deve tornare al piano.
    p._aggiorna_config(piano={
        "settimana_dal": dati.get("settimana_dal"),
        "giorno": giorno,
        "premessa": riga.get("premessa"),
        "angolo_differenziante": riga.get("angolo_differenziante"),
        "dati_amazon": riga.get("dati_amazon"),
    })
    metriche.registra(p.slug, "progetto_creato", nicchia=riga.get("nicchia"),
                      autore=riga.get("autore"), da_piano=True, giorno=giorno)
    e.slug, e.ok = p.slug, True
    return e
