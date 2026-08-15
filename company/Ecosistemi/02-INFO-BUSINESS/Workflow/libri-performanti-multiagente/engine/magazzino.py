"""
Magazzino argomenti — il "flusso atemporale" (2026-08-15).

IDEA DI GAEL: la ricerca non si rifa' a ogni libro. Una volta si cercano gli argomenti
buoni (io sul web, poi verificati con numeri veri di Amazon), se ne mette da parte una
settimana, e da li' in poi ogni libro ne consuma uno e parte subito. Cosi' la fase lenta e
di giudizio si paga una volta sola, e i giorni successivi sono solo scrittura.

COSA NON E': non e' un bot che sceglie da solo. Gli argomenti li scelgo io leggendo il
mercato; questo modulo e' il quaderno dove li appoggio, e il controllo che non ci finisca
dentro roba non verificata.

REGOLE, tutte nate da errori gia' visti su questo progetto:
- un argomento senza i numeri di Amazon non entra (niente "mi sembra una buona nicchia");
- un argomento che non e' una STORIA non entra: `story_validator` boccia diari, planner,
  journal e tracker prima che diventino un libro;
- un argomento gia' in uso non si riprende per sbaglio: lo stato e' scritto sul file.

Stato su disco in `LIBRI/magazzino_argomenti.json`.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

from . import config, story_validator

MAGAZZINO_PATH = config.LIBRI_DIR / "magazzino_argomenti.json"

LIBERO, IN_USO, FATTO = "libero", "in_uso", "fatto"

# Campi che un argomento DEVE avere per entrare. `dati_amazon` e' obbligatorio proprio
# perche' e' la differenza fra un argomento scelto e uno immaginato.
CAMPI_OBBLIGATORI = ("nicchia", "titolo_lavoro", "premessa", "dati_amazon")


@dataclass
class Argomento:
    nicchia: str
    titolo_lavoro: str
    premessa: str
    dati_amazon: dict
    aggiunto_il: str = ""
    stato: str = LIBERO
    slug_libro: str = ""

    def riga(self) -> str:
        d = self.dati_amazon or {}
        punteggio = d.get("punteggio", "?")
        marcatore = {LIBERO: " ", IN_USO: ">", FATTO: "x"}.get(self.stato, "?")
        return (f"[{marcatore}] {self.titolo_lavoro[:38]:<38} {self.nicchia[:26]:<26} "
                f"{punteggio!s:>5}/100  {self.stato}")


def _carica_grezzo() -> list[dict]:
    if not MAGAZZINO_PATH.exists():
        return []
    try:
        return json.loads(MAGAZZINO_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def carica() -> list[Argomento]:
    argomenti = []
    for d in _carica_grezzo():
        try:
            argomenti.append(Argomento(**d))
        except TypeError:
            continue  # voce scritta da una versione diversa: si salta, non si esplode
    return argomenti


def salva(argomenti: list[Argomento]) -> Path:
    MAGAZZINO_PATH.parent.mkdir(parents=True, exist_ok=True)
    MAGAZZINO_PATH.write_text(
        json.dumps([asdict(a) for a in argomenti], indent=2, ensure_ascii=False),
        encoding="utf-8")
    return MAGAZZINO_PATH


def valida_argomento(d: dict) -> list[str]:
    """Ritorna la lista dei problemi (vuota = si puo' inserire). Mai un'eccezione: chi
    chiama decide, stesso pattern degli altri validatori del progetto."""
    problemi = []
    for campo in CAMPI_OBBLIGATORI:
        valore = d.get(campo)
        if valore is None or (isinstance(valore, str) and not valore.strip()):
            problemi.append(f"campo obbligatorio mancante o vuoto: '{campo}'")

    dati = d.get("dati_amazon")
    if dati is not None and not isinstance(dati, dict):
        problemi.append("'dati_amazon' deve essere un oggetto con i numeri della ricerca")
    elif isinstance(dati, dict) and not dati:
        problemi.append("'dati_amazon' e' vuoto: un argomento entra solo con numeri veri")

    nicchia = (d.get("nicchia") or "").strip()
    premessa = (d.get("premessa") or "").strip()
    if nicchia:
        verdetto = story_validator.validate(nicchia, premessa)
        if not verdetto.is_go:
            problemi.append(f"non e' una storia: {verdetto.motivation}")
    return problemi


def aggiungi(nuovi: list[dict]) -> tuple[list[Argomento], list[str]]:
    """Inserisce argomenti nuovi, scartando quelli che non passano la validazione.
    Ritorna (inseriti, problemi) — mai un inserimento parziale silenzioso."""
    argomenti = carica()
    esistenti = {(a.nicchia.lower(), a.titolo_lavoro.lower()) for a in argomenti}
    inseriti, problemi = [], []

    for i, d in enumerate(nuovi, start=1):
        errori = valida_argomento(d)
        if errori:
            problemi.extend(f"argomento #{i} ('{d.get('titolo_lavoro', '?')}'): {e}"
                            for e in errori)
            continue
        chiave = (d["nicchia"].lower(), d["titolo_lavoro"].lower())
        if chiave in esistenti:
            problemi.append(f"argomento #{i}: gia' presente in magazzino "
                            f"('{d['titolo_lavoro']}')")
            continue
        a = Argomento(
            nicchia=d["nicchia"], titolo_lavoro=d["titolo_lavoro"],
            premessa=d["premessa"], dati_amazon=d["dati_amazon"],
            aggiunto_il=datetime.now().isoformat(timespec="seconds"),
        )
        argomenti.append(a)
        esistenti.add(chiave)
        inseriti.append(a)

    if inseriti:
        salva(argomenti)
    return inseriti, problemi


def prendi() -> Argomento | None:
    """Il prossimo argomento libero, marcato `in_uso`. None se il magazzino e' esaurito."""
    argomenti = carica()
    for a in argomenti:
        if a.stato == LIBERO:
            a.stato = IN_USO
            salva(argomenti)
            return a
    return None


def collega_libro(titolo_lavoro: str, slug: str) -> Argomento | None:
    """Lega un argomento al libro che ne e' nato, cosi' dal magazzino si risale al libro."""
    argomenti = carica()
    for a in argomenti:
        if a.titolo_lavoro.lower() == titolo_lavoro.lower():
            a.slug_libro = slug
            salva(argomenti)
            return a
    return None


def segna_fatto(slug: str) -> Argomento | None:
    argomenti = carica()
    for a in argomenti:
        if a.slug_libro == slug:
            a.stato = FATTO
            salva(argomenti)
            return a
    return None


def conteggi() -> dict:
    argomenti = carica()
    return {
        "totale": len(argomenti),
        LIBERO: sum(1 for a in argomenti if a.stato == LIBERO),
        IN_USO: sum(1 for a in argomenti if a.stato == IN_USO),
        FATTO: sum(1 for a in argomenti if a.stato == FATTO),
    }
