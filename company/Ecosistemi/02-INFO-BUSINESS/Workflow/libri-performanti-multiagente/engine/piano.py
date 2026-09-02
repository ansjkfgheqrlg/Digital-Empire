"""
Piano editoriale settimanale dei libri: SCOUT -> EDITOR -> GATE (2026-09-02).

    python -m engine.kdp piano                # genera il piano della settimana
    python -m engine.kdp piano --giorni 7 --dry-run

Modellato su `YOUTUBE-AUTOMATION-FACTORY/memory/piano_editoriale_70.json`: chi apre il piano
al giorno 5 non deve decidere niente, deve solo eseguire. Ogni riga porta con se' nicchia,
numeri REALI di Amazon, titolo, premessa, angolo differenziante e **il comando gia' compilato**.

I TRE MESTIERI, SEPARATI DI PROPOSITO (chi scrive il piano non e' chi lo approva):

    KDP-SCOUT   trova e MISURA le nicchie          -> engine/scout.py
    KDP-EDITOR  trasforma le misure in 7 righe      -> `costruisci_righe()` qui
    KDP-GATE    verifica il piano PRIMA che giri    -> `verifica()` qui

Perche' GATE e' separato: nel flusso KDP il gate che blocca (`kdp blocco`) ha bocciato 2 volte
su 7 su The Winter Term e **aveva ragione tutte e due**. E' il pezzo che funziona meglio di
tutto il workflow. Il piano merita lo stesso trattamento.

VINCOLO DURO (Art.2, zero dati finti): ogni `dati_amazon` viene da un run vero di ricerca
nicchie e porta la data di misura. Se la rete non risponde, il piano esce con MENO righe e lo
dice: un numero inventato in un piano editoriale e' peggio di un piano assente, perche' ci si
costruisce sopra per giorni.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

from . import config, magazzino, nicchia_attiva
from .scrittore import Budget, ScrittoreClaudeCLI

PIANI_DIR = config.LIBRI_DIR / "_piani"
RICERCHE_DIR = config.LIBRI_DIR / "_ricerca_nicchie"
BUDGET_PIANO_USD = 1.0

CAPITOLI = 24
PAROLE_PER_CAPITOLO = 1600

# Campi che una riga DEVE avere. GATE non conosce eccezioni: se ne manca uno, BLOCK.
CAMPI_RIGA = ("giorno", "data_produzione", "nicchia", "punteggio_nicchia", "dati_amazon",
              "titolo_lavoro", "autore", "premessa", "struttura_prevista",
              "angolo_differenziante", "comando_cli")

_RE_JSON_ARRAY = re.compile(r"\[.*\]", re.DOTALL)


@dataclass
class Verdetto:
    ok: bool = False
    blocchi: list = field(default_factory=list)
    avvisi: list = field(default_factory=list)

    def __str__(self) -> str:
        r = ["KDP-GATE: %s" % ("PASS" if self.ok else "BLOCK")]
        for b in self.blocchi:
            r.append("  [BLOCCA] %s" % b)
        for a in self.avvisi:
            r.append("  [avviso] %s" % a)
        return "\n".join(r)


@dataclass
class EsitoPiano:
    ok: bool = False
    righe: list = field(default_factory=list)
    verdetto: Verdetto = field(default_factory=Verdetto)
    path_json: str = ""
    path_md: str = ""
    costo_usd: float = 0.0
    errore: str = ""

    def __str__(self) -> str:
        r = ["", "=" * 74,
             " PIANO EDITORIALE — %s" % ("SCRITTO" if self.ok else "NON SCRITTO"),
             "=" * 74,
             "  righe   : %d" % len(self.righe),
             "  costo   : $%.4f" % self.costo_usd]
        if self.path_json:
            r += ["  json    : %s" % self.path_json, "  md      : %s" % self.path_md]
        r.append("")
        r.append(str(self.verdetto))
        if self.errore:
            r += ["", "  %s" % self.errore]
        r.append("")
        return "\n".join(r)


# --------------------------------------------------------------- dati di ricerca
def _ultima_ricerca() -> dict:
    """Mappa keyword -> valutazione REALE dall'ultimo report di ricerca nicchie.
    Serve per i `top_titoli`: l'angolo differenziante nasce dai concorrenti LETTI."""
    if not RICERCHE_DIR.exists():
        return {}
    report = sorted(RICERCHE_DIR.glob("nicchie_*.json"))
    if not report:
        return {}
    try:
        voci = json.loads(report[-1].read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    if isinstance(voci, dict):
        voci = voci.get("valutazioni") or voci.get("risultati") or []
    return {str(v.get("keyword", "")).lower(): v for v in voci if isinstance(v, dict)}


# ------------------------------------------------------------------- KDP-EDITOR
def _prompt_editor(argomenti: list, ricerca: dict, autore: str) -> str:
    blocchi = []
    for a in argomenti:
        v = ricerca.get(a.nicchia.lower(), {})
        concorrenti = "\n".join("      - %s" % t[:110]
                                for t in (v.get("top_titoli") or [])[:5]) or "      (non disponibili)"
        blocchi.append(
            "  SOTTO-NICCHIA: %s (punteggio %s, recensioni mediana %s)\n"
            "    titolo di lavoro: %s\n"
            "    premessa attuale: %s\n"
            "    CONCORRENTI VERI in prima pagina Amazon:\n%s"
            % (a.nicchia, (a.dati_amazon or {}).get("punteggio"),
               (a.dati_amazon or {}).get("recensioni_mediana"),
               a.titolo_lavoro, a.premessa, concorrenti))
    return """Sei un editor di collana per Amazon KDP. Prepari il piano di produzione della settimana.

AUTORE UNICO DEL CATALOGO: %s
Tutti i libri escono sotto questo nome, nella stessa famiglia di nicchie: devono sembrare
una collana, non esordi separati.

ARGOMENTI GIA' MISURATI (i numeri NON si toccano, sono misure reali):
%s

Per OGNI argomento produci:
  - "premessa": 3-5 righe. Chi e' il protagonista, cosa gli succede, qual e' la posta in
    gioco, e qual e' il mistero o il conflitto centrale. Concreta, non un tema.
  - "angolo_differenziante": 1-2 frasi che dicono perche' questo libro NON e' uguale ai
    concorrenti elencati sopra. Deve riferirsi a quei titoli veri, non a concorrenti generici.

Rispondi SOLO con un array JSON, senza testo attorno:
[{"titolo_lavoro": "esattamente uno di quelli sopra",
  "premessa": "...",
  "angolo_differenziante": "..."}]""" % (autore, "\n\n".join(blocchi))


def costruisci_righe(argomenti: list, ricerca: dict, autore: str, giorni: int,
                     scrittore, inizio: date) -> tuple[list, str]:
    """KDP-EDITOR: da argomenti misurati a righe eseguibili."""
    r = scrittore.genera(_prompt_editor(argomenti, ricerca, autore), "piano/editor")
    if not r.ok:
        return [], "KDP-EDITOR: %s" % r.errore
    m = _RE_JSON_ARRAY.search(r.testo or "")
    if not m:
        return [], "KDP-EDITOR: la risposta non contiene un array JSON"
    try:
        idee = json.loads(m.group(0))
    except json.JSONDecodeError as e:
        return [], "KDP-EDITOR: JSON non valido (%s)" % e
    per_titolo = {str(i.get("titolo_lavoro", "")).strip().lower(): i
                  for i in idee if isinstance(i, dict)}

    righe = []
    for n, a in enumerate(argomenti[:giorni], start=1):
        idea = per_titolo.get(a.titolo_lavoro.strip().lower(), {})
        dati = dict(a.dati_amazon or {})
        righe.append({
            "giorno": n,
            "data_produzione": (inizio + timedelta(days=n - 1)).isoformat(),
            "nicchia": a.nicchia,
            "punteggio_nicchia": dati.get("punteggio"),
            "dati_amazon": dati,
            "titolo_lavoro": a.titolo_lavoro,
            "autore": autore,
            "premessa": str(idea.get("premessa") or a.premessa).strip(),
            "struttura_prevista": {
                "capitoli": CAPITOLI,
                "parole_per_capitolo": PAROLE_PER_CAPITOLO,
                "parole_totali_bersaglio": CAPITOLI * PAROLE_PER_CAPITOLO,
                "pagine_minime_reali": config.TARGET_PAGE_COUNT - config.TARGET_PAGE_COUNT_TOLERANCE,
            },
            "angolo_differenziante": str(idea.get("angolo_differenziante") or "").strip(),
            "comando_cli": 'python -m engine.kdp nuovo "%s" --nicchia "%s" --autore "%s"'
                           % (a.titolo_lavoro, a.nicchia, autore),
        })
    return righe, ""


# --------------------------------------------------------------------- KDP-GATE
def verifica(righe: list, giorni: int) -> Verdetto:
    """KDP-GATE. Non conosce cortesie: un campo mancante o un numero senza fonte = BLOCK."""
    v = Verdetto()
    if not righe:
        v.blocchi.append("il piano e' vuoto")
        return v
    if len(righe) < giorni:
        v.avvisi.append("il piano ha %d righe invece di %d: la ricerca ha prodotto meno "
                        "argomenti validi del previsto (meglio meno righe che righe finte)"
                        % (len(righe), giorni))

    visti = set()
    for r in righe:
        eti = "giorno %s" % r.get("giorno", "?")
        for campo in CAMPI_RIGA:
            val = r.get(campo)
            if val is None or (isinstance(val, str) and not val.strip()) or val == {}:
                v.blocchi.append("%s: campo mancante o vuoto '%s'" % (eti, campo))

        dati = r.get("dati_amazon") or {}
        if not dati.get("punteggio"):
            v.blocchi.append("%s: dati_amazon senza punteggio (numero non misurato)" % eti)
        if not dati.get("misurato_il"):
            v.blocchi.append("%s: dati_amazon senza data di misura. I numeri vecchi hanno "
                             "gia' fatto danni il 2026-09-01 (nicchia da 83,1 a 72,9)" % eti)
        if r.get("punteggio_nicchia") != dati.get("punteggio"):
            v.blocchi.append("%s: punteggio_nicchia non coincide con dati_amazon" % eti)

        cli = str(r.get("comando_cli") or "")
        if "kdp nuovo" not in cli or str(r.get("titolo_lavoro") or "") not in cli:
            v.blocchi.append("%s: comando_cli assente o non compilato col titolo" % eti)

        t = str(r.get("titolo_lavoro") or "").lower()
        if t in visti:
            v.blocchi.append("%s: titolo duplicato nel piano ('%s')" % (eti, t))
        visti.add(t)

        if len(str(r.get("premessa") or "").split()) < 20:
            v.blocchi.append("%s: premessa troppo corta per essere una storia" % eti)
        if not str(r.get("angolo_differenziante") or "").strip():
            v.blocchi.append("%s: manca l'angolo differenziante" % eti)

    v.ok = not v.blocchi
    return v


# ----------------------------------------------------------------- orchestrazione
def _markdown(righe: list, autore: str, nicchia: str, inizio: date) -> str:
    r = ["# Piano editoriale libri — settimana dal %s" % inizio.isoformat(), "",
         "> Generato il %s · nicchia di catalogo **%s** · autore **%s**"
         % (datetime.now().strftime("%Y-%m-%d %H:%M"), nicchia, autore),
         "> Ogni riga e' eseguibile cosi' com'e': chi la apre non deve decidere niente.", ""]
    for x in righe:
        d = x["dati_amazon"]
        r += ["## Giorno %d — %s (%s)" % (x["giorno"], x["titolo_lavoro"], x["data_produzione"]),
              "",
              "- **Nicchia**: `%s` — punteggio **%s/100** (misurato il %s)"
              % (x["nicchia"], x["punteggio_nicchia"], d.get("misurato_il")),
              "- **Numeri Amazon**: recensioni mediana %s · %s concorrenti deboli su %s · "
              "prezzo medio $%s" % (d.get("recensioni_mediana"), d.get("concorrenti_deboli"),
                                    d.get("concorrenti_analizzati"), d.get("prezzo_medio")),
              "- **Autore**: %s" % x["autore"],
              "- **Struttura**: %d capitoli x ~%d parole, minimo %d pagine reali"
              % (x["struttura_prevista"]["capitoli"],
                 x["struttura_prevista"]["parole_per_capitolo"],
                 x["struttura_prevista"]["pagine_minime_reali"]),
              "", "**Premessa**", "", x["premessa"], "",
              "**Angolo differenziante**", "", x["angolo_differenziante"], "",
              "**Comando**", "", "```bash", x["comando_cli"], "```", ""]
    return "\n".join(r)


def lunedi_di(giorno: date) -> date:
    return giorno - timedelta(days=giorno.weekday())


def genera(giorni: int = 7, dry_run: bool = False, scrittore=None,
           inizio: date | None = None) -> EsitoPiano:
    e = EsitoPiano()
    budget = Budget(limite_usd=BUDGET_PIANO_USD)
    if scrittore is None:
        scrittore = ScrittoreClaudeCLI(budget=budget)
    else:
        budget = getattr(scrittore, "budget", budget)

    attiva = nicchia_attiva.carica()
    if attiva is None:
        e.errore = "nessuna nicchia attiva: la decisione di catalogo viene prima del piano"
        return e
    autore = getattr(config, "AUTORE_CATALOGO", None) or "Maren Ashcroft"

    liberi = [a for a in magazzino.carica() if a.stato == magazzino.LIBERO]
    if not liberi:
        e.errore = ("magazzino vuoto: lancia prima `python -m engine.kdp scout`. "
                    "Un piano senza argomenti misurati sarebbe un piano inventato.")
        return e
    liberi.sort(key=lambda a: (a.dati_amazon or {}).get("punteggio") or 0, reverse=True)

    inizio = inizio or lunedi_di(date.today())
    righe, errore = costruisci_righe(liberi, _ultima_ricerca(), autore, giorni,
                                     scrittore, inizio)
    e.costo_usd = budget.speso_usd
    if errore:
        e.errore = errore
        return e

    e.righe = righe
    e.verdetto = verifica(righe, giorni)
    if not e.verdetto.ok:
        e.errore = ("KDP-GATE ha bloccato il piano: NON e' stato scritto niente. "
                    "Stessa regola di `kdp copy`: si valida prima di salvare.")
        return e
    if dry_run:
        e.errore = "DRY-RUN: piano valido ma non scritto"
        return e

    PIANI_DIR.mkdir(parents=True, exist_ok=True)
    pj = PIANI_DIR / ("piano_%s.json" % inizio.isoformat())
    pm = PIANI_DIR / ("piano_%s.md" % inizio.isoformat())
    pj.write_text(json.dumps({
        "generato_il": datetime.now().isoformat(timespec="seconds"),
        "nicchia_catalogo": attiva.keyword,
        "autore_catalogo": autore,
        "settimana_dal": inizio.isoformat(),
        "totale_libri": len(righe),
        "righe": righe,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pm.write_text(_markdown(righe, autore, attiva.keyword, inizio), encoding="utf-8")

    e.path_json, e.path_md, e.ok = str(pj), str(pm), True
    return e


def carica_piano(giorno: date | None = None) -> dict | None:
    """Il piano della settimana che contiene `giorno`. None se non c'e'."""
    inizio = lunedi_di(giorno or date.today())
    pj = PIANI_DIR / ("piano_%s.json" % inizio.isoformat())
    if not pj.exists():
        return None
    try:
        return json.loads(pj.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
