"""
Gate di blocco: il controllo da lanciare dopo ogni gruppo di capitoli (2026-08-19).

PERCHE' ESISTE. I tre libri di questo progetto hanno fallito nello stesso modo: il difetto
sistemico si e' scoperto alla fine, quando correggerlo costava tutto il libro.

  The Quiet Hours   24 capitoli in 18 minuti -> 84 pagine -> riscritto INTERO il giorno dopo
  The Ninth Winter  primi 8 capitoli a 1.041 parole -> scoperto al capitolo 24
  entrambi          193 righe di lineette riscritte a mano dopo che erano finiti

Trovare "sto scrivendo capitoli troppo corti" al capitolo 4 costa riscrivere 4 capitoli.
Trovarlo al capitolo 24 ne costa 24. E' tutta qui la differenza fra un libro in mezz'ora e
un libro in due giorni.

VINCOLO DI PROGETTO: deve girare in **meno di un secondo**. Percio' NON tocca il PDF (12s)
e NON fa l'OCR della copertina (10s): sono i due controlli costosi e restano alla consegna,
che si fa una volta sola a fine corsa. Qui dentro si guarda solo il testo.

Uso:
    python -m engine.kdp blocco <slug>

Esce 0 se si puo' proseguire, 1 se c'e' qualcosa da sistemare **adesso**.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from . import config, validators

# Un filo narrativo lasciato aperto piu' a lungo di cosi' non si chiude piu' da solo: o lo
# chiudi, o a fine libro serve una scena-toppa. Su The Ninth Winter, Efrain e' rimasto
# aperto dal capitolo 15 al 24 ed e' costato una scena aggiunta in coda.
MAX_CAPITOLI_FILO_APERTO = 6

# Un filo puo' essere dichiarato ad ARCO LUNGO: `- [cap 01, arco lungo] ...`. Serve perche'
# la domanda centrale di un libro resta aperta per costruzione fino all'ultimo capitolo, e
# un gate che la segnala a ogni blocco grida al lupo e si smette di ascoltarlo. Trovato al
# primo uso reale su The Second-Hand Spellbook: "perche' Maren non e' tornata per undici
# anni" e' il cuore del libro, si chiude al cap. 24, e il gate lo trattava come dimenticato.
_RE_FILO = re.compile(
    r"^\s*[-*]\s*\[cap\s*(\d{1,2})(,\s*arco\s+lungo)?\]\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
_RE_SEZIONE_CAP = re.compile(r"^###\s*cap[_\s]*(\d{1,2})", re.IGNORECASE | re.MULTILINE)


@dataclass
class EsitoBlocco:
    slug: str
    capitoli_scritti: int
    capitoli_totali: int
    parole: int
    media_per_capitolo: int
    proiezione: int
    minimo: int
    blocchi: list[str] = field(default_factory=list)
    avvisi: list[str] = field(default_factory=list)

    @property
    def si_prosegue(self) -> bool:
        return not self.blocchi

    def __str__(self) -> str:
        pagine_proiettate = round(self.proiezione / config.WORDS_PER_PAGE_ESTIMATE, 1)
        righe = [
            f"Blocco: {self.slug}  {self.capitoli_scritti}/{self.capitoli_totali} capitoli",
            f"  media {self.media_per_capitolo} parole/capitolo",
            f"  proiezione a fine libro: {self.proiezione} parole (~{pagine_proiettate} pagine), "
            f"minimo {self.minimo}",
        ]
        if self.blocchi:
            righe.append("")
            righe.append("DA SISTEMARE ADESSO (non al capitolo 24):")
            righe += [f"  - {b}" for b in self.blocchi]
        for a in self.avvisi:
            righe.append(f"  avviso: {a}")
        righe.append("")
        righe.append("SI PROSEGUE" if self.si_prosegue else "FERMARSI E CORREGGERE")
        return "\n".join(righe)


def _fili_aperti(riassunti: str) -> list[tuple[int, str]]:
    """Legge la sezione 'Fili aperti': righe come '- [cap 07] Efrain aspetta aprile'."""
    testa = riassunti.split("## Capitoli")[0]
    return [(int(n), testo.strip())
            for n, arco_lungo, testo in _RE_FILO.findall(testa)
            if not arco_lungo]


def controlla(progetto) -> EsitoBlocco:
    """Il gate. `progetto` e' un BookProject (passato cosi' per non creare un import ciclico)."""
    stato = progetto.stato()
    cfg = progetto._config()
    scritti = stato.capitoli_scritti
    totali = stato.capitoli_totali
    minimo = config.TARGET_WORD_COUNT_MIN

    media = round(stato.parole_scritte / len(scritti)) if scritti else 0
    proiezione = media * totali
    ritmo_bersaglio = cfg.get("parole_per_capitolo") or round(minimo / totali)

    esito = EsitoBlocco(
        slug=progetto.slug, capitoli_scritti=len(scritti), capitoli_totali=totali,
        parole=stato.parole_scritte, media_per_capitolo=media,
        proiezione=proiezione, minimo=minimo,
    )
    if not scritti:
        esito.blocchi.append("nessun capitolo scritto")
        return esito

    # 1. IL CONTROLLO CHE CONTA: a questo ritmo, dove atterra il libro?
    # Non "la media e' bassa" ma "il libro finira' corto", che e' la domanda vera.
    if proiezione < minimo:
        mancano = minimo - proiezione
        # Si indica il ritmo del BERSAGLIO, non quello del minimo. Indicare il minimo
        # rimanderebbe dritti al bordo della finestra, che e' l'errore che CP-1 ha appena
        # tolto di mezzo: The Ninth Winter atterrato a 115,2 pagine e quattro riprese per
        # tenerlo sopra. Trovato al primo uso reale, con una proiezione a 8 parole dal minimo.
        esito.blocchi.append(
            f"a {media} parole/capitolo il libro chiude a {proiezione} parole: "
            f"{mancano} sotto il minimo di {minimo}. Il bersaglio e' "
            f"{ritmo_bersaglio} parole/capitolo ({ritmo_bersaglio * totali} totali, "
            f"in mezzo alla finestra). Allunga QUESTI capitoli adesso, non i prossimi."
        )
    elif proiezione > config.TARGET_WORD_COUNT_MAX:
        esito.avvisi.append(
            f"a {media} parole/capitolo il libro chiude a {proiezione}, sopra il massimo "
            f"({config.TARGET_WORD_COUNT_MAX}). Puoi accorciare senza fretta."
        )

    # 2. Difetti di testo: costano poco qui, tantissimo a fine libro.
    testi = {n: progetto.path_capitolo(n).read_text(encoding="utf-8") for n in scritti}
    for n, testo in testi.items():
        for avviso in validators.valida_troncamento(testo, f"cap_{n:02d}"):
            esito.blocchi.append(avviso)
    lineette = validators.valida_lineette("\n\n".join(testi.values()))
    if lineette:
        esito.blocchi.append(
            f"{len(lineette)} righe con lineette lunghe fuori dal dialogo. "
            f"Toglile ora: a fine libro sono state 193 righe da riscrivere a mano."
        )

    # 3. Riassunti: se non sono aggiornati, il capitolo successivo si scrive alla cieca.
    riassunti = progetto.riassunti_path.read_text(encoding="utf-8") \
        if progetto.riassunti_path.exists() else ""
    documentati = {int(n) for n in _RE_SEZIONE_CAP.findall(riassunti)}
    non_documentati = sorted(set(scritti) - documentati)
    if non_documentati:
        esito.blocchi.append(
            f"riassunti.md non copre i capitoli {non_documentati}. Senza, il prossimo "
            f"blocco si scrive alla cieca e nessun controllo automatico se ne accorge."
        )

    # 4. Fili aperti da troppo: e' cio' che produce le scene-toppa in coda.
    ultimo = max(scritti)
    for da_capitolo, testo in _fili_aperti(riassunti):
        eta = ultimo - da_capitolo
        if eta > MAX_CAPITOLI_FILO_APERTO:
            esito.blocchi.append(
                f"filo aperto dal capitolo {da_capitolo} ({eta} capitoli fa): {testo}. "
                f"Chiudilo entro il blocco prossimo o diventera' una scena aggiunta in coda."
            )

    # 5. Capitoli che si ripetono (2026-08-23). E' il difetto piu' probabile quando si
    # scrivono 8 capitoli di fila con la scaletta sotto gli occhi: due che fanno la stessa
    # scena in due punti diversi del libro. Costa 828 confronti di insiemi su un libro
    # intero, cioe' niente, e la regola "mai un capitolo quasi identico a un altro" era la
    # sola delle sei non negoziabili che nessuna funzione faceva rispettare.
    ripetizioni = validators.valida_ripetizioni(
        {f"cap_{n:02d}": testo for n, testo in testi.items()})
    bloccanti_rip = validators.ripetizioni_bloccanti(ripetizioni)
    esito.blocchi += bloccanti_rip
    esito.avvisi += [r for r in ripetizioni if r not in bloccanti_rip]
    return esito
