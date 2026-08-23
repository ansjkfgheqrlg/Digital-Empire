"""
Metriche di produzione: quanto costa davvero fare un libro (2026-08-23).

PERCHE' ESISTE. "The Second-Hand Spellbook in 48 minuti, di cui 18 di rilavorazione perche'
il gate ha bocciato tre volte" e' scritto in un checkpoint, a mano, dopo. Nel progetto non
c'era niente che lo registrasse: il numero e' vero quando viene scritto e non e' piu'
verificabile il giorno dopo. Su un progetto la cui regola numero uno e' "nessun numero
dichiarato senza ricontrollo", il tempo di produzione era l'unico numero dichiarato e mai
misurato — e per giunta e' proprio l'obiettivo che Gael ha chiesto ("un libro in mezz'ora").

COSA FA. Un file `metriche.json` per libro, accanto ai capitoli, dove ogni comando lascia
una riga con l'orario. Da li' si legge senza ricostruire niente da git:

  - quanto tempo e' passato davvero dalla creazione alla consegna;
  - quante volte il gate ha bocciato un blocco, e per cosa (e' li' che va il tempo);
  - quante volte il libro e' stato riconsegnato (ogni riconsegna = un PDF rigenerato);
  - quanto si e' aspettata la copertina.

COSA NON FA. Non giudica e non blocca: e' un registratore. E non deve MAI far fallire un
comando — un errore di scrittura delle metriche non puo' costare un libro. Per questo ogni
funzione qui dentro inghiotte le proprie eccezioni e tira dritto.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from . import config

NOME_FILE = "metriche.json"


def _percorso(slug: str) -> Path:
    return config.LIBRI_DIR / "in_lavorazione" / slug / NOME_FILE


def _carica(slug: str) -> dict:
    p = _percorso(slug)
    if not p.exists():
        return {"slug": slug, "eventi": []}
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        d.setdefault("eventi", [])
        return d
    except (json.JSONDecodeError, OSError):
        # Un file di metriche illeggibile non e' un buon motivo per fermare un libro.
        return {"slug": slug, "eventi": []}


def registra(slug: str, cosa: str, **dati) -> None:
    """Aggiunge un evento con l'orario. Non solleva mai."""
    try:
        d = _carica(slug)
        evento = {"quando": datetime.now().isoformat(timespec="seconds"), "cosa": cosa}
        evento.update({k: v for k, v in dati.items() if v is not None})
        d["eventi"].append(evento)
        p = _percorso(slug)
        if not p.parent.exists():
            return  # progetto non ancora creato: niente da registrare, niente da rompere
        p.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception:  # noqa: BLE001 — deliberato: le metriche non fanno cadere il flusso
        pass


def _minuti(a: str, b: str) -> float:
    return round((datetime.fromisoformat(b) - datetime.fromisoformat(a)).total_seconds() / 60, 1)


@dataclass
class Riepilogo:
    slug: str
    eventi: int
    minuti_totali: float | None
    blocchi_passati: int
    blocchi_bocciati: int
    consegne: int
    consegne_bloccate: int
    motivi_bocciatura: list[str]
    minuti_attesa_copertina: float | None

    def __str__(self) -> str:
        if not self.eventi:
            return ("Metriche: nessun evento registrato per questo libro (progetto creato "
                    "prima del 2026-08-23, oppure nessun comando ancora lanciato).")
        righe = [f"Metriche: {self.eventi} eventi registrati"]
        if self.minuti_totali is not None:
            righe.append(f"  tempo dal primo all'ultimo comando: {self.minuti_totali} minuti")
        righe.append(f"  gate blocco: {self.blocchi_passati} passati, "
                     f"{self.blocchi_bocciati} bocciati")
        if self.motivi_bocciatura:
            for m in self.motivi_bocciatura:
                righe.append(f"    - {m}")
        righe.append(f"  consegne: {self.consegne} ({self.consegne_bloccate} non pubblicabili)")
        if self.minuti_attesa_copertina is not None:
            righe.append(f"  attesa copertina: {self.minuti_attesa_copertina} minuti "
                         f"dalla creazione del progetto alla prima consegna con copertina")
        if self.blocchi_bocciati or self.consegne > 1:
            righe.append("  NOTA: bocciature e riconsegne sono la rilavorazione, cioe' dove "
                         "va il tempo. Il codice, cronometrato, ne prende meno di un minuto.")
        return "\n".join(righe)


def riepilogo(slug: str) -> Riepilogo:
    d = _carica(slug)
    eventi = d.get("eventi", [])
    blocchi = [e for e in eventi if e.get("cosa") == "blocco"]
    bocciati = [e for e in blocchi if e.get("esito") == "bocciato"]
    consegne = [e for e in eventi if e.get("cosa") == "consegna"]
    creazione = next((e for e in eventi if e.get("cosa") == "progetto_creato"), None)
    con_cover = next((e for e in consegne if e.get("con_copertina")), None)

    motivi: list[str] = []
    for e in bocciati:
        for m in e.get("motivi", [])[:2]:
            testo = m if len(m) < 110 else m[:107] + "..."
            if testo not in motivi:
                motivi.append(testo)

    return Riepilogo(
        slug=slug,
        eventi=len(eventi),
        minuti_totali=_minuti(eventi[0]["quando"], eventi[-1]["quando"]) if len(eventi) > 1 else None,
        blocchi_passati=len(blocchi) - len(bocciati),
        blocchi_bocciati=len(bocciati),
        consegne=len(consegne),
        consegne_bloccate=sum(1 for e in consegne if e.get("esito") == "non_pubblicabile"),
        motivi_bocciatura=motivi,
        minuti_attesa_copertina=(_minuti(creazione["quando"], con_cover["quando"])
                                 if creazione and con_cover else None),
    )
