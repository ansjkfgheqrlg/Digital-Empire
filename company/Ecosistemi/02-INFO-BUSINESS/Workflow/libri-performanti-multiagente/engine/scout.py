"""
KDP-SCOUT: riempie il magazzino di argomenti DA SOLO, ogni settimana (2026-09-02).

    python -m engine.kdp scout                 # 7 argomenti nella nicchia attiva
    python -m engine.kdp scout --quante 10
    python -m engine.kdp scout --dry-run       # mostra cosa inserirebbe, non scrive

PERCHE' ESISTE. Il magazzino si e' svuotato ogni volta ed e' sempre ripartito da zero, a
mano: 3 argomenti totali, 0 liberi il 2026-09-01. Con un libro al giorno finisce mercoledi'.
Ordine di Gael (2026-09-02): *"gli argomenti settimanali li devi trovare in autonomia ogni
settimana"*. Quindi non un riempimento una tantum ma un comando ripetibile.

COME LAVORA, e dove NON si inventa niente:

    1. propone keyword di sotto-nicchia dentro la nicchia attiva        -> 1 chiamata modello
    2. le MISURA su Amazon davvero (niche_finder -> amazon_research)    -> nessun numero finto
    3. scarta quelle sotto la soglia di punteggio
    4. per quelle rimaste scrive titolo di lavoro + premessa            -> 1 chiamata modello
    5. inserisce passando dal validatore del magazzino, che pretende
       `dati_amazon` non vuoto e una premessa che sia una STORIA

I `dati_amazon` di ogni argomento sono i numeri REALI della sua sotto-nicchia, misurati
nella run che lo ha creato: non sono ereditati, non sono stimati, e portano la data. E'
esattamente il difetto che ha morso il 2026-09-01, quando la scelta di catalogo e' stata
fatta su punteggi di 19 giorni prima (una nicchia era passata da 83,1 a 72,9).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime

from . import magazzino, nicchia_attiva, niche_finder
from .scrittore import Budget, ScrittoreClaudeCLI

PUNTEGGIO_MINIMO = 60.0      # sotto questo non vale la pena scriverci un libro
KEYWORD_DA_PROVARE = 10      # se ne misurano piu' di quante ne servano: alcune cadono
BUDGET_SCOUT_USD = 1.0       # due chiamate: proposta keyword + premesse

_RE_JSON_ARRAY = re.compile(r"\[.*\]", re.DOTALL)


@dataclass
class EsitoScout:
    nicchia: str = ""
    keyword_misurate: int = 0
    keyword_promosse: int = 0
    inseriti: list = field(default_factory=list)
    scartati: list = field(default_factory=list)
    costo_usd: float = 0.0
    errore: str = ""

    def __str__(self) -> str:
        r = ["", "=" * 74, " KDP-SCOUT — %s" % (self.errore or "magazzino rifornito"),
             "=" * 74,
             "  nicchia   : %s" % self.nicchia,
             "  misurate  : %d keyword su Amazon" % self.keyword_misurate,
             "  promosse  : %d sopra il punteggio minimo (%.0f)" % (self.keyword_promosse,
                                                                    PUNTEGGIO_MINIMO),
             "  inseriti  : %d argomenti" % len(self.inseriti),
             "  costo     : $%.4f" % self.costo_usd]
        for a in self.inseriti:
            r.append("     %-42s %s" % (a.titolo_lavoro[:42],
                                        (a.dati_amazon or {}).get("punteggio")))
        for s in self.scartati[:6]:
            r.append("     [scartato] %s" % s[:90])
        r.append("")
        return "\n".join(r)


def _estrai_array(testo: str):
    m = _RE_JSON_ARRAY.search(testo or "")
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def _prompt_keyword(nicchia: str, quante: int) -> str:
    return f"""Sei un ricercatore di nicchie per Amazon KDP.

NICCHIA DEL CATALOGO: {nicchia}

Proponi {quante} keyword di SOTTO-NICCHIA dentro questa nicchia: espressioni che un lettore
digiterebbe davvero nella ricerca Amazon per trovare libri di questo tipo. Devono essere
vicine alla nicchia madre (stesso scaffale), non generiche e non identiche fra loro.

Rispondi SOLO con un array JSON di stringhe, senza testo attorno. Esempio di forma:
["keyword uno", "keyword due"]"""


def _prompt_premesse(nicchia: str, keyword_ok: list) -> str:
    elenco = "\n".join("  - %s (punteggio %.1f, recensioni mediana %s)"
                       % (v.keyword, v.punteggio, v.recensioni_mediana)
                       for v in keyword_ok)
    return f"""Sei un editor di narrativa per Amazon KDP.

NICCHIA DEL CATALOGO: {nicchia}
SOTTO-NICCHIE VALIDATE (una per libro):
{elenco}

Per OGNI sotto-nicchia scrivi un'idea di romanzo: un titolo di lavoro e una premessa.

La premessa deve essere una STORIA, non un tema: chi e' il protagonista, cosa vuole, cosa
gli si mette contro, e qual e' il mistero o il conflitto centrale. Due o tre frasi.
Deve contenere le parole della sotto-nicchia (es. witch, magic, bookshop, mystery): un
controllo automatico rifiuta le premesse che non sembrano narrativa di genere.

Ogni idea deve essere DIVERSA dalle altre: protagonisti, ambientazioni e conflitti distinti.

Rispondi SOLO con un array JSON, senza testo attorno:
[
  {{"keyword": "la sotto-nicchia esatta fra quelle sopra",
    "titolo_lavoro": "titolo in inglese, 2-5 parole",
    "premessa": "2-3 frasi in italiano che raccontano la storia"}}
]"""


def rifornisci(quante: int = 7, nicchia: str | None = None, dry_run: bool = False,
               scrittore=None, headless: bool = True) -> EsitoScout:
    """Trova, misura e inserisce argomenti nuovi. Non chiede niente."""
    e = EsitoScout()
    budget = Budget(limite_usd=BUDGET_SCOUT_USD)
    if scrittore is None:
        scrittore = ScrittoreClaudeCLI(budget=budget)
    else:
        budget = getattr(scrittore, "budget", budget)

    if not nicchia:
        attiva = nicchia_attiva.carica()
        if attiva is None:
            e.errore = ("nessuna nicchia attiva: scegline una con "
                        "`kdp nicchia-scegli --keywords \"...\"`")
            return e
        nicchia = attiva.keyword
    e.nicchia = nicchia

    # --- 1. keyword candidate ------------------------------------------------
    r = scrittore.genera(_prompt_keyword(nicchia, KEYWORD_DA_PROVARE), "scout/keyword")
    if not r.ok:
        e.errore = "proposta keyword fallita: %s" % r.errore
        e.costo_usd = budget.speso_usd
        return e
    keywords = _estrai_array(r.testo)
    if not keywords:
        e.errore = "la risposta non conteneva un array JSON di keyword"
        e.costo_usd = budget.speso_usd
        return e
    keywords = [str(k).strip() for k in keywords if str(k).strip()][:KEYWORD_DA_PROVARE]

    # --- 2. misura VERA su Amazon -------------------------------------------
    print("  misuro %d keyword su Amazon..." % len(keywords), flush=True)
    valutazioni = niche_finder.trova_nicchie(keywords, headless=headless, salva_report=True)
    e.keyword_misurate = len(valutazioni)
    promosse = [v for v in valutazioni if v.punteggio >= PUNTEGGIO_MINIMO][:quante]
    e.keyword_promosse = len(promosse)
    for v in valutazioni:
        if v.punteggio < PUNTEGGIO_MINIMO:
            e.scartati.append("%s: punteggio %.1f sotto il minimo" % (v.keyword, v.punteggio))
    if not promosse:
        e.errore = "nessuna keyword ha superato il punteggio minimo di %.0f" % PUNTEGGIO_MINIMO
        e.costo_usd = budget.speso_usd
        return e

    # --- 3. premesse ---------------------------------------------------------
    r2 = scrittore.genera(_prompt_premesse(nicchia, promosse), "scout/premesse")
    if not r2.ok:
        e.errore = "scrittura premesse fallita: %s" % r2.errore
        e.costo_usd = budget.speso_usd
        return e
    idee = _estrai_array(r2.testo) or []
    per_keyword = {v.keyword.lower(): v for v in promosse}

    nuovi = []
    for idea in idee:
        if not isinstance(idea, dict):
            continue
        v = per_keyword.get(str(idea.get("keyword", "")).strip().lower())
        if v is None:
            e.scartati.append("idea con keyword non misurata: %s" % idea.get("keyword"))
            continue
        nuovi.append({
            "nicchia": v.keyword,
            "titolo_lavoro": str(idea.get("titolo_lavoro", "")).strip(),
            "premessa": str(idea.get("premessa", "")).strip(),
            # NUMERI REALI della run di oggi, con la data: non ereditati, non stimati.
            "dati_amazon": {
                "punteggio": v.punteggio,
                "recensioni_mediana": v.recensioni_mediana,
                "prezzo_medio": v.prezzo_medio,
                "concorrenti_deboli": v.concorrenti_deboli,
                "concorrenti_analizzati": v.n_risultati,
                "misurato_il": datetime.now().strftime("%Y-%m-%d"),
            },
        })

    e.costo_usd = budget.speso_usd
    if dry_run:
        e.inseriti = [magazzino.Argomento(nicchia=n["nicchia"],
                                          titolo_lavoro=n["titolo_lavoro"],
                                          premessa=n["premessa"],
                                          dati_amazon=n["dati_amazon"]) for n in nuovi]
        e.errore = "DRY-RUN: niente scritto sul magazzino"
        return e

    inseriti, problemi = magazzino.aggiungi(nuovi)
    e.inseriti = inseriti
    e.scartati.extend(problemi)
    return e
