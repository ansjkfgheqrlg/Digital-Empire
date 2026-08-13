"""
Nicchia attiva — la nicchia si sceglie UNA VOLTA e si segue (2026-08-12).

CORREZIONE DI UN ERRORE DI IMPOSTAZIONE. Fino a oggi il flusso rifaceva l'analisi di
mercato a ogni libro e sceglieva ogni volta una nicchia diversa: sbagliato, e Gael l'ha
detto chiaramente. Su KDP si costruisce un catalogo dentro UNA nicchia — i lettori di
"amish suspense" comprano il secondo libro dello stesso autore, l'algoritmo di Amazon
associa i titoli fra loro, le recensioni di un libro spingono gli altri. Saltare da una
nicchia all'altra a ogni titolo butta via tutto questo.

REGOLA: la nicchia resta finché è buona.

Prima di ogni libro si fa un CONTROLLO SALUTE (non una scelta): si rimisura la nicchia
attiva con gli stessi criteri con cui era stata scelta. Tre esiti:

  - **buona** → si scrive il libro successivo nella stessa nicchia, punto.
  - **peggiorata** → si cercano alternative, ma si cambia SOLO se una di esse è
    davvero migliore (di un margine netto, non per un punto di differenza).
  - **non misurabile** (Amazon non risponde) → NON si cambia nulla: si tiene la nicchia
    e si segnala. Un dato mancante non è un dato negativo.

Stato su disco in `LIBRI/nicchia_attiva.json`: chi legge quel file sa sempre su cosa
stiamo costruendo il catalogo e con che numeri quella scelta è stata fatta.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

from . import config

STATO_PATH = config.LIBRI_DIR / "nicchia_attiva.json"

# Sotto questo punteggio la nicchia non è più considerata sana e vale la pena guardarsi
# intorno. Non è un "cambia subito": è un "vai a vedere se c'è di meglio".
SOGLIA_SALUTE = 60.0

# Margine minimo perché valga la pena abbandonare una nicchia su cui si è già costruito.
# Cambiare costa: si perdono l'associazione fra titoli, le recensioni che si spingono a
# vicenda e il pubblico già raggiunto. Un vantaggio di 2-3 punti non ripaga quel costo.
MARGINE_PER_CAMBIARE = 12.0


@dataclass
class Nicchia:
    keyword: str
    punteggio_iniziale: float
    scelta_il: str
    motivazione: str
    libri_pubblicati: list[str] = field(default_factory=list)
    controlli: list[dict] = field(default_factory=list)

    @property
    def punteggio_corrente(self) -> float:
        return self.controlli[-1]["punteggio"] if self.controlli else self.punteggio_iniziale

    @property
    def sana(self) -> bool:
        return self.punteggio_corrente >= SOGLIA_SALUTE


def carica() -> Nicchia | None:
    """La nicchia su cui stiamo costruendo il catalogo, o None se non ne è mai stata scelta."""
    if not STATO_PATH.exists():
        return None
    try:
        return Nicchia(**json.loads(STATO_PATH.read_text(encoding="utf-8")))
    except (json.JSONDecodeError, TypeError, OSError):
        return None


def salva(n: Nicchia) -> Path:
    STATO_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATO_PATH.write_text(json.dumps(asdict(n), indent=2, ensure_ascii=False), encoding="utf-8")
    return STATO_PATH


def imposta(keyword: str, punteggio: float, motivazione: str) -> Nicchia:
    """Fissa la nicchia del catalogo. Da qui in poi tutti i libri nascono da questa."""
    n = Nicchia(keyword=keyword, punteggio_iniziale=punteggio,
                scelta_il=datetime.now().isoformat(timespec="seconds"),
                motivazione=motivazione)
    salva(n)
    return n


def registra_libro(titolo: str) -> Nicchia | None:
    n = carica()
    if n is None:
        return None
    if titolo not in n.libri_pubblicati:
        n.libri_pubblicati.append(titolo)
        salva(n)
    return n


def controlla_salute(headless: bool = True) -> dict:
    """Rimisura la nicchia attiva su Amazon. NON sceglie: dice solo come sta.

    Ritorna un dizionario con l'esito e cosa fare, senza fare nulla di irreversibile —
    la decisione di cambiare nicchia resta un passo separato e dichiarato."""
    from playwright.sync_api import sync_playwright

    from . import niche_finder

    n = carica()
    if n is None:
        return {"stato": "nessuna_nicchia",
                "messaggio": "Nessuna nicchia attiva: va scelta una volta con 'nicchia scegli'."}

    try:
        with sync_playwright() as p:
            v = niche_finder.valuta_keyword(p, n.keyword, headless=headless)
    except Exception as exc:
        # Amazon irraggiungibile NON è una nicchia peggiorata: non si tocca niente.
        return {"stato": "non_misurabile", "nicchia": n.keyword,
                "messaggio": f"Amazon non ha risposto ({exc}). Nicchia invariata, si procede."}

    n.controlli.append({
        "quando": datetime.now().isoformat(timespec="seconds"),
        "punteggio": v.punteggio,
        "recensioni_mediana": v.recensioni_mediana,
        "prezzo_medio": v.prezzo_medio,
        "concorrenti_deboli": v.concorrenti_deboli,
    })
    salva(n)

    delta = v.punteggio - n.punteggio_iniziale
    if v.punteggio >= SOGLIA_SALUTE:
        return {"stato": "sana", "nicchia": n.keyword, "punteggio": v.punteggio, "delta": delta,
                "messaggio": f"Nicchia sana ({v.punteggio}/100, {delta:+.1f} dall'inizio). "
                             f"Si scrive il prossimo libro qui."}
    return {"stato": "peggiorata", "nicchia": n.keyword, "punteggio": v.punteggio, "delta": delta,
            "messaggio": f"Nicchia sotto soglia ({v.punteggio}/100, minimo {SOGLIA_SALUTE}). "
                         f"Vale la pena cercare alternative — si cambia solo se una supera "
                         f"{v.punteggio + MARGINE_PER_CAMBIARE:.0f}."}


def valuta_cambio(candidate: list[str], headless: bool = True) -> dict:
    """Confronta la nicchia attiva con delle candidate e dice se conviene cambiare.

    Non cambia da sola: il cambio è una decisione che va presa sapendo cosa si lascia."""
    from playwright.sync_api import sync_playwright

    from . import niche_finder

    attuale = carica()
    if attuale is None:
        return {"stato": "nessuna_nicchia"}

    soglia = attuale.punteggio_corrente + MARGINE_PER_CAMBIARE
    esiti = []
    with sync_playwright() as p:
        for kw in candidate:
            try:
                v = niche_finder.valuta_keyword(p, kw, headless=headless)
                esiti.append(v)
            except Exception:
                continue

    esiti.sort(key=lambda v: v.punteggio, reverse=True)
    if not esiti:
        return {"stato": "non_misurabile", "messaggio": "Nessuna candidata misurabile."}

    migliore = esiti[0]
    conviene = migliore.punteggio >= soglia
    return {
        "stato": "conviene_cambiare" if conviene else "resta",
        "attuale": {"keyword": attuale.keyword, "punteggio": attuale.punteggio_corrente,
                     "libri": len(attuale.libri_pubblicati)},
        "migliore_candidata": {"keyword": migliore.keyword, "punteggio": migliore.punteggio,
                                "motivazione": migliore.motivazione},
        "soglia_richiesta": round(soglia, 1),
        "messaggio": (
            f"Conviene cambiare: '{migliore.keyword}' fa {migliore.punteggio} contro "
            f"{attuale.punteggio_corrente} (serviva almeno {soglia:.0f})."
            if conviene else
            f"Si resta su '{attuale.keyword}': la migliore candidata fa "
            f"{migliore.punteggio}, sotto la soglia di {soglia:.0f} che giustificherebbe "
            f"di abbandonare {len(attuale.libri_pubblicati)} libri gia' pubblicati li'."
        ),
        "tutte": [{"keyword": v.keyword, "punteggio": v.punteggio} for v in esiti],
    }
