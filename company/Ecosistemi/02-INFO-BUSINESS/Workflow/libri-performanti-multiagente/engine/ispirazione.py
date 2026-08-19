"""
Scheda di ISPIRAZIONE di un libro (2026-08-19).

A cosa serve: ogni libro nasce guardando una nicchia e i concorrenti che ci stanno dentro.
Finora quell'analisi viveva nella testa di chi scriveva l'outline e spariva. Quando sei al
capitolo 15 e devi decidere se una scena e' giusta per il mercato, o quando fra due mesi
vuoi capire perche' un libro ha venduto e un altro no, quel dato non c'e' piu'.

Questo modulo lo mette su file dentro il progetto e lo porta nel pacchetto finale.

**L'unita' di misura e' la NICCHIA, non il singolo concorrente**, e non e' una comodita':
e' quello che il codice misura davvero. `niche_finder` restituisce mediana recensioni,
prezzo medio, concorrenti deboli e punteggio su 16-20 titoli in prima pagina. Il singolo
libro concorrente (titolo, autore, ASIN) e' un di piu' utile ma facoltativo, e va compilato
solo se qualcuno lo ha davvero aperto. Uno schema che pretendesse un ASIN si farebbe
riempire di ASIN inventati, e allora la scheda smetterebbe di valere qualcosa.

REGOLA: i numeri NON si inventano. `valida()` rifiuta una scheda senza i numeri della
nicchia, per la stessa ragione per cui `magazzino.valida_argomento()` rifiuta un argomento
senza `dati_amazon`. Una scheda con numeri finti e' peggio di nessuna scheda: sembra
ricerca e non lo e'.

Nessuna chiamata a modelli: i numeri li produce lo scraper Amazon gia' costruito, il
giudizio editoriale lo scrive Claude leggendo la concorrenza.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path

# Campi di giudizio editoriale senza i quali la scheda non dice niente di utile.
OBBLIGATORI_TESTO = (
    "nicchia", "genere", "lettore_tipo",
    "temi_chiave", "stile", "tono", "come_ci_distinguiamo",
)


@dataclass
class Ispirazione:
    """Da dove nasce il libro: la nicchia coi suoi numeri veri, e come ci mettiamo dentro."""

    nicchia: str = ""

    # --- numeri VERI della nicchia (da niche_finder / amazon_research) ------ #
    recensioni_mediana: float | None = None
    recensioni_minime: int | None = None
    prezzo_medio: float | None = None
    rating_medio: float | None = None
    concorrenti_analizzati: int | None = None
    concorrenti_deboli: int | None = None
    punteggio: float | None = None
    rilevato_il: str = ""

    # --- il singolo concorrente, SE qualcuno lo ha davvero aperto ----------- #
    titolo_concorrente: str = ""
    autore_concorrente: str = ""
    asin: str = ""
    prezzo_concorrente: float | None = None
    recensioni_concorrente: int | None = None

    # --- il giudizio editoriale -------------------------------------------- #
    genere: str = ""
    sottogenere: str = ""
    lettore_tipo: str = ""
    temi_chiave: list[str] = field(default_factory=list)
    stile: str = ""
    tono: str = ""
    struttura: str = ""
    cosa_funziona: list[str] = field(default_factory=list)
    dove_sono_deboli: list[str] = field(default_factory=list)
    come_ci_distinguiamo: str = ""

    scritta_il: str = field(default_factory=lambda: date.today().isoformat())

    def valida(self) -> tuple[bool, list[str]]:
        """(va bene, cosa manca). I numeri della nicchia pesano quanto il testo."""
        mancanti = [c for c in OBBLIGATORI_TESTO if not getattr(self, c)]
        if self.recensioni_mediana is None:
            mancanti.append("recensioni_mediana (numero vero, da niche_finder)")
        if self.prezzo_medio is None:
            mancanti.append("prezzo_medio (numero vero, da niche_finder)")
        if not self.rilevato_il:
            mancanti.append("rilevato_il (quando sono stati presi i numeri)")
        return not mancanti, mancanti

    def to_dict(self) -> dict:
        return asdict(self)

    def testo(self) -> str:
        """Versione leggibile, per chi apre la cartella invece del JSON."""
        def elenco(voci):
            return "\n".join(f"  - {v}" for v in voci) if voci else "  (non annotato)"

        def num(v, prefisso=""):
            return f"{prefisso}{v}" if v is not None else "non rilevato"

        righe = [
            "=" * 62,
            "DA DOVE NASCE QUESTO LIBRO",
            "=" * 62,
            "",
            f"Nicchia: {self.nicchia}",
            f"Genere:  {self.genere}" + (f" / {self.sottogenere}" if self.sottogenere else ""),
            f"Lettore: {self.lettore_tipo}",
            "",
            "--- NUMERI REALI DELLA NICCHIA SU AMAZON ---",
            f"(rilevati il {self.rilevato_il or 'data non registrata'}, "
            f"su {num(self.concorrenti_analizzati)} titoli in prima pagina)",
            "",
            f"  Recensioni, mediana:  {num(self.recensioni_mediana)}",
            f"  Recensioni, minimo:   {num(self.recensioni_minime)}",
            f"  Prezzo medio:         {num(self.prezzo_medio, '$')}",
            f"  Rating medio:         {num(self.rating_medio)}",
            f"  Concorrenti deboli:   {num(self.concorrenti_deboli)}"
            f"   <- lo spazio per entrare",
            f"  Punteggio nicchia:    {num(self.punteggio)}",
        ]

        if self.titolo_concorrente:
            righe += [
                "",
                "--- CONCORRENTE GUARDATO DA VICINO ---",
                f"  {self.titolo_concorrente}, "
                f"{self.autore_concorrente or 'autore non annotato'}",
                f"  ASIN {self.asin or 'non rilevato'} | "
                f"{num(self.prezzo_concorrente, '$')} | "
                f"{num(self.recensioni_concorrente)} recensioni",
            ]

        righe += [
            "",
            "--- LETTURA EDITORIALE ---",
            f"Stile:     {self.stile}",
            f"Tono:      {self.tono}",
            f"Struttura: {self.struttura or 'non annotata'}",
            "",
            "Temi che la nicchia si aspetta:",
            elenco(self.temi_chiave),
            "",
            "Cosa fanno bene (da imparare):",
            elenco(self.cosa_funziona),
            "",
            "Dove sono deboli (il nostro spazio):",
            elenco(self.dove_sono_deboli),
            "",
            "--- COME CI DISTINGUIAMO ---",
            self.come_ci_distinguiamo or "(non dichiarato)",
            "",
            "=" * 62,
        ]
        return "\n".join(righe)


def da_ricerca_nicchia(voce: dict) -> dict:
    """Traduce una voce di `LIBRI/_ricerca_nicchie/*.json` nei campi numerici.

    Cosi' i numeri veri entrano nella scheda per copia e non ribattuti a mano, che e' il
    modo piu' comune in cui un numero vero diventa un numero sbagliato."""
    return {
        "nicchia": voce.get("keyword", ""),
        "recensioni_mediana": voce.get("recensioni_mediana"),
        "recensioni_minime": voce.get("recensioni_min"),
        "prezzo_medio": voce.get("prezzo_medio"),
        "rating_medio": voce.get("rating_medio"),
        "concorrenti_analizzati": voce.get("n_risultati"),
        "concorrenti_deboli": voce.get("concorrenti_deboli"),
        "punteggio": voce.get("punteggio"),
    }


def carica(percorso: Path) -> Ispirazione:
    dati = json.loads(Path(percorso).read_text(encoding="utf-8"))
    dati.pop("_nota", None)
    return Ispirazione(**dati)


def salva(scheda: Ispirazione, percorso: Path) -> Path:
    percorso = Path(percorso)
    percorso.parent.mkdir(parents=True, exist_ok=True)
    dati = {"_nota": "Numeri rilevati su Amazon, mai stimati. Vedi engine/ispirazione.py.",
            **scheda.to_dict()}
    percorso.write_text(json.dumps(dati, indent=2, ensure_ascii=False), encoding="utf-8")
    return percorso
