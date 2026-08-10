"""
Niche Finder (PIANO KDP V2) — sceglie la nicchia su cui scrivere il prossimo libro, con
dati REALI di Amazon e un punteggio trasparente. E' l'implementazione vera di quello che
nel blueprint originale erano 3 team di schede descrittive senza codice
(AmazonKeywordResearchTeam / KeywordExpansionTeam / SearchOptimizationTeam): qui ogni
"agente" e' una funzione che fa davvero il suo lavoro e mostra i numeri su cui decide.

COME DECIDE (nessun punteggio magico: ogni fattore e' visibile e motivato)

Una nicchia e' interessante quando c'e' domanda ma la concorrenza e' battibile:

- **Recensioni mediane basse** = i libri in prima pagina non sono corazzati, un titolo
  nuovo puo' emergere. E' il fattore che pesa di piu' (peso 50).
- **Concorrenti deboli in prima pagina** (libri con < 100 recensioni) = spazio reale
  (peso 30).
- **Prezzo medio alto** = margine migliore per copia venduta (peso 20).

Il punteggio e' 0-100 e serve a ORDINARE le candidate, non a decidere da solo: la scelta
finale resta di chi legge la tabella, che vede tutti i numeri grezzi accanto.

USO:
    python -m engine.niche_finder --keywords "cozy mystery cats" "small town romance"
    python -m engine.niche_finder --file keywords.txt --top 5
"""
from __future__ import annotations

import json
import statistics
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

from . import amazon_research, config, story_validator

REPORT_DIR = config.LIBRI_DIR / "_ricerca_nicchie"

# Soglie: dichiarate qui, non sparse nel codice, cosi' si possono tarare sui risultati veri.
CONCORRENTE_DEBOLE_MAX_RECENSIONI = 100
RECENSIONI_MEDIANE_OTTIME = 200     # sotto questa soglia: punteggio pieno sul fattore
RECENSIONI_MEDIANE_PESSIME = 5000   # sopra questa soglia: punteggio zero sul fattore
PREZZO_OTTIMO = 9.99                # sopra questo prezzo medio: punteggio pieno
PREZZO_MINIMO = 2.99

PESO_RECENSIONI = 50
PESO_CONCORRENTI_DEBOLI = 30
PESO_PREZZO = 20


@dataclass
class ValutazioneNicchia:
    keyword: str
    n_risultati: int
    recensioni_mediana: float | None
    recensioni_min: int | None
    concorrenti_deboli: int
    prezzo_medio: float | None
    rating_medio: float | None
    punteggio: float
    motivazione: str
    qualifica_storia: str = ""
    top_titoli: list[str] = field(default_factory=list)

    def riga_tabella(self) -> str:
        mediana = f"{self.recensioni_mediana:.0f}" if self.recensioni_mediana is not None else "?"
        prezzo = f"${self.prezzo_medio:.2f}" if self.prezzo_medio else "?"
        return (f"{self.punteggio:5.1f}  {self.keyword[:34]:<34} "
                f"rec.mediana={mediana:>6}  deboli={self.concorrenti_deboli:>2}/{self.n_risultati:<2}  "
                f"prezzo={prezzo:>7}")


def _prezzo_float(prezzo: str | None) -> float | None:
    if not prezzo:
        return None
    cifre = "".join(c for c in prezzo if c.isdigit() or c == ".")
    try:
        return float(cifre) if cifre else None
    except ValueError:
        return None


def _rating_float(rating: str | None) -> float | None:
    if not rating:
        return None
    try:
        return float(rating.split()[0].replace(",", "."))
    except (ValueError, IndexError):
        return None


def _punteggio_da_recensioni(mediana: float | None) -> float:
    """Meno recensioni hanno i concorrenti, piu' la nicchia e' aggredibile."""
    if mediana is None:
        return 0.0
    if mediana <= RECENSIONI_MEDIANE_OTTIME:
        return float(PESO_RECENSIONI)
    if mediana >= RECENSIONI_MEDIANE_PESSIME:
        return 0.0
    # interpolazione lineare fra le due soglie
    quota = (RECENSIONI_MEDIANE_PESSIME - mediana) / (RECENSIONI_MEDIANE_PESSIME - RECENSIONI_MEDIANE_OTTIME)
    return round(PESO_RECENSIONI * quota, 1)


def valuta_keyword(playwright, keyword: str, headless: bool = True) -> ValutazioneNicchia:
    """Interroga Amazon DAVVERO per una keyword e calcola i numeri della nicchia."""
    listings = amazon_research.search_amazon(playwright, keyword, headless=headless)

    recensioni = [b.reviews_count for b in listings if b.reviews_count is not None]
    prezzi = [p for p in (_prezzo_float(b.price) for b in listings) if p and p >= PREZZO_MINIMO]
    ratings = [r for r in (_rating_float(b.rating) for b in listings) if r]

    mediana = statistics.median(recensioni) if recensioni else None
    deboli = sum(1 for r in recensioni if r < CONCORRENTE_DEBOLE_MAX_RECENSIONI)
    prezzo_medio = round(statistics.mean(prezzi), 2) if prezzi else None
    rating_medio = round(statistics.mean(ratings), 2) if ratings else None

    p_rec = _punteggio_da_recensioni(mediana)
    p_deb = round(PESO_CONCORRENTI_DEBOLI * (deboli / len(listings)), 1) if listings else 0.0
    p_prz = round(PESO_PREZZO * min(1.0, (prezzo_medio or 0) / PREZZO_OTTIMO), 1) if prezzo_medio else 0.0
    punteggio = round(p_rec + p_deb + p_prz, 1)

    motivazione = (
        f"recensioni mediane {mediana:.0f} -> {p_rec}/{PESO_RECENSIONI} | "
        f"{deboli} concorrenti sotto {CONCORRENTE_DEBOLE_MAX_RECENSIONI} recensioni su "
        f"{len(listings)} -> {p_deb}/{PESO_CONCORRENTI_DEBOLI} | "
        f"prezzo medio ${prezzo_medio or 0:.2f} -> {p_prz}/{PESO_PREZZO}"
    ) if mediana is not None else "dati recensioni non disponibili per questa ricerca"

    # La nicchia deve anche essere una STORIA, non un diario/planner (CP3, gia' verificato).
    verdetto = story_validator.validate(keyword, keyword)
    qualifica = "GO" if verdetto.is_go else f"NO-GO: {verdetto.motivation[:80]}"
    if not verdetto.is_go:
        punteggio = 0.0  # una nicchia non-storia non va scelta comunque, per quanto ricca

    return ValutazioneNicchia(
        keyword=keyword,
        n_risultati=len(listings),
        recensioni_mediana=mediana,
        recensioni_min=min(recensioni) if recensioni else None,
        concorrenti_deboli=deboli,
        prezzo_medio=prezzo_medio,
        rating_medio=rating_medio,
        punteggio=punteggio,
        motivazione=motivazione,
        qualifica_storia=qualifica,
        top_titoli=[b.title for b in listings[:5]],
    )


def trova_nicchie(keywords: list[str], headless: bool = True,
                   salva_report: bool = True) -> list[ValutazioneNicchia]:
    """Valuta piu' keyword e le ordina dalla piu' promettente alla meno.
    Una keyword che fallisce (Amazon irraggiungibile, blocco) viene segnalata e saltata,
    mai inventata: meglio una lista piu' corta ma vera."""
    from playwright.sync_api import sync_playwright

    risultati: list[ValutazioneNicchia] = []
    with sync_playwright() as p:
        for i, kw in enumerate(keywords, start=1):
            print(f"\n[{i}/{len(keywords)}] analizzo '{kw}'...")
            try:
                v = valuta_keyword(p, kw, headless=headless)
            except Exception as exc:
                print(f"  SALTATA — Amazon non ha risposto: {exc}")
                continue
            risultati.append(v)
            print(f"  punteggio {v.punteggio}/100 — {v.motivazione}")

    risultati.sort(key=lambda v: v.punteggio, reverse=True)

    if salva_report and risultati:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        path = REPORT_DIR / f"nicchie_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        path.write_text(json.dumps([asdict(v) for v in risultati], indent=2, ensure_ascii=False),
                        encoding="utf-8")
        print(f"\nReport salvato: {path}")
    return risultati


def stampa_classifica(risultati: list[ValutazioneNicchia], top: int = 10) -> None:
    print("\n" + "=" * 78)
    print("CLASSIFICA NICCHIE (punteggio alto = piu' facile entrare con un libro nuovo)")
    print("=" * 78)
    for v in risultati[:top]:
        print(v.riga_tabella())
    if risultati:
        migliore = risultati[0]
        print("\n" + "-" * 78)
        print(f"CONSIGLIATA: {migliore.keyword}  (punteggio {migliore.punteggio}/100)")
        print(f"  {migliore.motivazione}")
        print(f"  Qualifica storia: {migliore.qualifica_storia}")
        print("  Concorrenti in prima pagina:")
        for t in migliore.top_titoli:
            print(f"    - {t[:70]}")


if __name__ == "__main__":
    import argparse
    import sys

    cli = argparse.ArgumentParser(
        description="Trova la nicchia migliore su cui scrivere il prossimo libro (dati Amazon reali)")
    cli.add_argument("--keywords", nargs="+", help="keyword da valutare")
    cli.add_argument("--file", help="file di testo con una keyword per riga")
    cli.add_argument("--top", type=int, default=10)
    cli.add_argument("--visibile", action="store_true", help="mostra il browser (debug)")
    args = cli.parse_args()

    kws = list(args.keywords or [])
    if args.file:
        kws += [r.strip() for r in Path(args.file).read_text(encoding="utf-8").splitlines()
                if r.strip() and not r.startswith("#")]
    if not kws:
        cli.error("servono --keywords oppure --file")

    esiti = trova_nicchie(kws, headless=not args.visibile)
    stampa_classifica(esiti, top=args.top)
    sys.exit(0 if esiti else 1)
