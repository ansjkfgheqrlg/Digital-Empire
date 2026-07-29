"""
EMPIRE — centro di comando: `python -m empire controllo`.

Owner: Claude · Origine: FORGE (controllo empire-wide, CP-20260728)

## Il modello dell'azienda: PLAYWRIGHT PER TUTTO

Digital Empire NON usa OAuth/API per agire verso l'esterno. Usa **Playwright** che pilota un
**browser reale gia' loggato** (profilo Chrome persistente / storage-state salvato). Pubblicare
su YouTube, mandare DM su Instagram, connettere su LinkedIn, scrapare Maps: tutto via browser
loggato, come farebbe una persona. Nessuna chiave API, nessun OAuth.

Percio' il gate reale di ogni porta d'uscita NON e' "c'e' l'OAuth?" (era un mio errore) ma:
**"c'e' una sessione browser loggata per quel servizio, ed e' ancora valida?"**

I materiali gia' presenti nel repo:
  - `EmpireDesk/chrome-profile/`           profilo Chrome persistente (YouTube via Playwright)
  - `Outreach/Instagram Automation/instagram_session.json`   sessione IG salvata
  - `Outreach/LinkedIn Automation/linkedin_session.json`     sessione LinkedIn salvata
  - `youtube_uploader_playwright.py` (launch_persistent_context) · run_today IG · 01-04 LinkedIn

## Onesta' sulla freschezza (il punto che conta)

Una sessione salvata "presente" NON e' "valida": i cookie social scadono in settimane/mesi.
Se la sessione e' vecchia, la prima azione reale e' **verificare/rifare il login una volta**
nel browser (unico atto che tocca a Max, e dura un minuto). Il comando segnala l'eta' della
sessione, cosi' non si promette un invio che poi sbatte su un login scaduto.

L'incasso resta l'unica porta legata a un conto (Stripe): un Payment Link si crea via Playwright
solo se il browser e' loggato su Stripe; ricevere denaro richiede comunque il conto di Max.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .paths import repo_root

__all__ = ["stato_workflow", "register"]

_RESET = "=" * 74


def _eta_giorni(p: Path) -> int | None:
    try:
        mtime = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
        return (datetime.now(timezone.utc) - mtime).days
    except OSError:
        return None


def _sessione(rel: str) -> tuple[bool, str]:
    """Ritorna (presente, nota-freschezza). La freschezza e' un giudizio prudente:
    oltre ~30 giorni una sessione social e' probabilmente da rifare."""
    p = repo_root() / rel
    if not p.exists():
        return False, "assente"
    g = _eta_giorni(p)
    if g is None:
        return True, "presente"
    if g > 30:
        return True, f"presente ma vecchia ({g}gg) — login probabilmente da rifare"
    return True, f"presente e recente ({g}gg)"


def _incasso() -> dict:
    p = repo_root() / "Crea siti" / "Siti CCM" / "checkout.config.json"
    stripe = False
    if p.exists():
        try:
            stripe = json.loads(p.read_text(encoding="utf-8")).get("rails", {}).get("stripe_base", {}).get("attivo", False)
        except Exception:  # noqa: BLE001
            pass
    if stripe:
        return {"nome": "INCASSO", "parte": True, "stato": "tier 1 — Stripe attivo", "serve": "-"}
    return {"nome": "INCASSO", "parte": False,
            "stato": "tier 2 — solo ordine via mail",
            "serve": "MAX: 2 Payment Link Stripe (creabili anche via Playwright se il browser e' "
                     "loggato su Stripe; ricevere denaro richiede il tuo conto)"}


def _youtube() -> dict:
    prof = repo_root() / "EmpireDesk" / "chrome-profile"
    ha_profilo = prof.exists() and any(prof.iterdir()) if prof.exists() else False
    video = list((repo_root() / "WORKFLOW-ESTATE" / "07-VIDEO-RUN").rglob("*.mp4"))
    if ha_profilo and video:
        return {"nome": "YOUTUBE (Playwright)", "parte": True,
                "stato": "profilo Chrome loggato + video pronto", "serve": "-"}
    manca = []
    if not ha_profilo:
        manca.append("profilo Chrome loggato su YouTube")
    if not video:
        manca.append("il VIDEO non e' renderizzato (c'e' lo script, manca l'.mp4)")
    stato = "profilo Chrome presente (upload via youtube_uploader_playwright)" if ha_profilo else "profilo assente"
    return {"nome": "YOUTUBE (Playwright)", "parte": False, "stato": stato,
            "serve": "MAX: " + " · ".join(manca)}


def _instagram() -> dict:
    ok, nota = _sessione("Outreach/Instagram Automation/instagram_session.json")
    if ok and "vecchia" not in nota:
        return {"nome": "INSTAGRAM DM (Playwright)", "parte": True,
                "stato": f"sessione {nota} — run_today.py pronto", "serve": "-"}
    if ok:
        return {"nome": "INSTAGRAM DM (Playwright)", "parte": False,
                "stato": f"sessione {nota}", "serve": "MAX: rifare login IG una volta (1 min) via refresh_session.py"}
    return {"nome": "INSTAGRAM DM (Playwright)", "parte": False, "stato": "sessione assente",
            "serve": "MAX: primo login IG nel browser"}


def _linkedin() -> dict:
    ok, nota = _sessione("Outreach/LinkedIn Automation/linkedin_session.json")
    if ok and "vecchia" not in nota:
        return {"nome": "LINKEDIN (Playwright)", "parte": True,
                "stato": f"sessione {nota} — 02_send_connections/04_send_messages pronti", "serve": "-"}
    if ok:
        return {"nome": "LINKEDIN (Playwright)", "parte": False,
                "stato": f"sessione {nota}", "serve": "MAX: rifare login LinkedIn una volta (1 min)"}
    return {"nome": "LINKEDIN (Playwright)", "parte": False, "stato": "sessione assente",
            "serve": "MAX: primo login LinkedIn nel browser"}


def _outreach_email() -> dict:
    p = repo_root() / "Outreach" / "Outreach Workflow" / ".env"
    gmail = False
    if p.exists():
        for r in p.read_text(encoding="utf-8", errors="replace").splitlines():
            if r.startswith("GMAIL_APP_PASSWORD=") and r.split("=", 1)[1].strip():
                gmail = True
    if gmail:
        return {"nome": "OUTREACH email (SMTP)", "parte": True,
                "stato": "credenziali Gmail presenti", "serve": "MAX: 'via' sul target (dry-run prima)"}
    return {"nome": "OUTREACH email (SMTP)", "parte": False, "stato": "credenziali assenti",
            "serve": "MAX: GMAIL_APP_PASSWORD"}


def _s7() -> dict:
    d = repo_root() / "company" / "Ecosistemi" / "12-STREAM-S7-BOT"
    paper = any("PAPER TRADING" in f.read_text(encoding="utf-8", errors="replace")
                for f in d.glob("*.py") if f.is_file()) if d.exists() else False
    return {"nome": "NFT / STREAM-S7", "parte": paper,
            "stato": "PAPER TRADING (per design: nessun capitale reale)",
            "serve": "MAX: decisione capitale reale solo dopo che il paper prova un edge"}


def stato_workflow() -> list[dict]:
    return [_incasso(), _outreach_email(), _instagram(), _linkedin(), _youtube(), _s7()]


def _cmd_controllo(a) -> int:
    ws = stato_workflow()
    print(_RESET)
    print("  DIGITAL EMPIRE — CENTRO DI COMANDO — TUTTI I WORKFLOW (Playwright per tutto)")
    print(_RESET)
    for w in ws:
        print(f"  [{'PARTE ' if w['parte'] else 'MAX   '}] {w['nome']}")
        print(f"           stato:  {w['stato']}")
        if w["serve"] != "-":
            print(f"           serve:  {w['serve']}")
    partono = [w for w in ws if w["parte"]]
    print(_RESET)
    print(f"  {len(partono)}/{len(ws)} workflow pronti a partire adesso.")
    print()
    print("  ATTI DI MAX (nessuno li fa al posto tuo):")
    for w in ws:
        if not w["parte"] and w["serve"] != "-":
            print(f"     - {w['nome']}: {w['serve']}")
    print(_RESET)
    return 0


def register(sub) -> None:
    """Registrato via plugin loop (empire.flow.cli). `empire/cli.py` resta congelato."""
    p = sub.add_parser("controllo",
                       help="centro di comando: stato reale di tutti i workflow (Playwright) + atti di Max")
    p.set_defaults(fn=_cmd_controllo)
