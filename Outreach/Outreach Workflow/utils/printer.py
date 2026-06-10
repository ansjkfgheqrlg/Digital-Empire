"""
Printer colorato per Digital Empire Outreach.
Usato da orchestrator, maps_browser_scraper, writer, ecc.
I colori passano attraverso il worker() di run_parallel.py via ANSI.
"""

import sys

# ── Colori ANSI ────────────────────────────────────────────────────────────
_RS   = "\033[0m"           # reset

# Fasi principali
_CYAN  = "\033[96m"         # SCRAPING / Maps
_VI    = "\033[95m"         # Email generation
_GR    = "\033[92m"         # Successo / inviata
_YL    = "\033[93m"         # Warning / attenzione
_RED   = "\033[91m"         # Errore
_BOLD  = "\033[1m"          # Titoli sezione
_DIM   = "\033[2m"          # Testo secondario

# ── Funzioni helper ────────────────────────────────────────────────────────

def scraping_header(settori_count: int, citta_count: int):
    """Banner iniziale fase scraping."""
    print(f"\n{_BOLD}{_CYAN}{'═'*60}{_RS}", flush=True)
    print(f"{_BOLD}{_CYAN}  SCRAPING GOOGLE MAPS{_RS}"
          f"{_DIM}  {settori_count} settori × {citta_count} città{_RS}", flush=True)
    print(f"{_BOLD}{_CYAN}{'═'*60}{_RS}\n", flush=True)


def scraping_query(settore: str, citta: str, trovati: int, totale: int):
    """Singola query di ricerca."""
    bar  = f"{_DIM}({trovati}/{totale}){_RS}"
    print(f"  {_CYAN}[MAPS]{_RS}  {_BOLD}{settore}{_RS} in {citta}  {bar}", flush=True)


def scraping_risultato(n: int, settore: str, citta: str):
    """Risultato di una query."""
    if n > 0:
        print(f"  {_CYAN}[MAPS]{_RS}  {_GR}+{n} trovati{_RS}  ({settore}/{citta})", flush=True)
    else:
        print(f"  {_CYAN}[MAPS]{_RS}  {_DIM}nessun risultato ({settore}/{citta}){_RS}", flush=True)


def scraping_done(n_business: int, n_con_email: int, n_nuovi: int):
    """Fine fase scraping."""
    print(f"\n  {_CYAN}[MAPS]{_RS}  {_BOLD}Completato:{_RS} "
          f"{_GR}{n_business} business{_RS} → "
          f"{n_con_email} email → "
          f"{_BOLD}{n_nuovi} nuovi{_RS}\n", flush=True)


def email_header(totale: int):
    """Banner iniziale fase generazione email."""
    print(f"\n{_BOLD}{_VI}{'═'*60}{_RS}", flush=True)
    print(f"{_BOLD}{_VI}  GENERAZIONE EMAIL  {_RS}{_DIM}({totale} da scrivere){_RS}", flush=True)
    print(f"{_BOLD}{_VI}{'═'*60}{_RS}\n", flush=True)


def email_generando(i: int, totale: int, nome: str, settore: str, citta: str):
    """Stampa il nome del business mentre genera l'email."""
    num   = f"{_DIM}[{i}/{totale}]{_RS}"
    label = f"{_VI}[EMAIL]{_RS}"
    biz   = f"{_BOLD}{nome}{_RS}"
    meta  = f"{_DIM}{settore} · {citta}{_RS}"
    print(f"  {num} {label}  {biz}  {meta}", flush=True)


def email_ok(nome: str, qa_score: float):
    """Email generata e passata QA."""
    print(f"  {_GR}[OK]{_RS}  {nome}  {_DIM}QA {qa_score:.1f}/10{_RS}", flush=True)


def email_scartata(nome: str, motivo: str):
    """Email scartata dal QA."""
    print(f"  {_RED}[SCARTATA]{_RS}  {nome}  {_DIM}{motivo}{_RS}", flush=True)


def sezione(titolo: str, colore: str = _BOLD):
    """Separatore visivo per una sezione."""
    print(f"\n{colore}  ── {titolo}{_RS}", flush=True)


def warn(msg: str):
    print(f"  {_YL}[WARN]{_RS}  {msg}", flush=True)


def errore(msg: str):
    print(f"  {_RED}[ERRORE]{_RS}  {msg}", flush=True)


def successo(msg: str):
    print(f"  {_GR}[OK]{_RS}  {msg}", flush=True)
