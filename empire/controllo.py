"""
EMPIRE — centro di comando: `python -m empire controllo`.

Owner: Claude · Origine: FORGE (controllo empire-wide, CP-20260728)

## Perché

Max: "Digital Empire deve avere il controllo completo di tutti gli altri workflow
(YouTube, NFT/S7, Outreach) e far partire tutto — mandare, pubblicare, incassare — ORA".

Il Workflow Estate e' il cervello. Questo comando gli da' gli occhi e le mani su tutti i
workflow operativi: per ognuno legge lo stato REALE (credenziali, artefatti, gate) e
dichiara senza girarci intorno se PARTE o se serve un atto di Max — perche' alcune porte
(incassare, pubblicare su un canale, mandare a persone reali) dipendono per legge/tecnica
da credenziali o account che solo Max possiede. Nascondere questo con un "in corso" sarebbe
la bugia piu' costosa possibile: far credere che i soldi stiano arrivando quando la porta e'
chiusa.

Non esegue le azioni irreversibili verso l'esterno: le porta al bordo e dice cosa manca.
"""
from __future__ import annotations

from pathlib import Path

from .paths import repo_root

__all__ = ["stato_workflow", "register"]

_RESET = "=" * 74


def _env_ha_chiave(rel_env: str, chiave: str) -> bool:
    p = repo_root() / rel_env
    if not p.exists():
        return False
    try:
        for riga in p.read_text(encoding="utf-8", errors="replace").splitlines():
            if riga.startswith(chiave + "="):
                return bool(riga.split("=", 1)[1].strip())
    except OSError:
        return False
    return False


def _incasso() -> dict:
    """Legge il tier di checkout dal config."""
    import json
    p = repo_root() / "Crea siti" / "Siti CCM" / "checkout.config.json"
    if not p.exists():
        return {"nome": "INCASSO", "parte": False, "stato": "config assente",
                "serve": "MAX: creare checkout.config.json"}
    try:
        cfg = json.loads(p.read_text(encoding="utf-8"))
        rails = cfg.get("rails", {})
        stripe = rails.get("stripe_base", {}).get("attivo", False)
    except Exception:  # noqa: BLE001
        stripe, rails = False, {}
    if stripe:
        return {"nome": "INCASSO", "parte": True, "stato": "tier 1 — Stripe attivo",
                "serve": "-"}
    return {"nome": "INCASSO", "parte": False,
            "stato": "tier 2 — solo ordine via mail (nessun pagamento automatico)",
            "serve": "MAX: 2 Payment Link Stripe (10 min). Nessuno puo' incassare al posto tuo."}


def _outreach() -> dict:
    gmail = _env_ha_chiave("Outreach/Outreach Workflow/.env", "GMAIL_APP_PASSWORD")
    fb = _env_ha_chiave("Outreach/Outreach Workflow/.env", "FB_ACCESS_TOKEN")
    if gmail:
        return {"nome": "OUTREACH email", "parte": True,
                "stato": f"credenziali Gmail presenti{' + FB' if fb else ''}",
                "serve": "MAX: conferma esplicita del target e 'via' all'invio reale (dry-run prima)"}
    return {"nome": "OUTREACH email", "parte": False, "stato": "credenziali Gmail mancanti",
            "serve": "MAX: GMAIL_APP_PASSWORD nel .env"}


def _outreach_whatsapp() -> dict:
    p = repo_root() / "Outreach/Outreach Workflow/campagne/concessionari-preventa/stato_lead.csv"
    n = 0
    if p.exists():
        n = max(0, len(p.read_text(encoding="utf-8", errors="replace").splitlines()) - 1)
    return {"nome": "CONCESSIONARI WhatsApp", "parte": False,
            "stato": f"{n} lead con telefono/WhatsApp, nessuna WhatsApp Business API attiva",
            "serve": "MAX: invio manuale dei messaggi (gia' generati) OPPURE attivare WhatsApp Business API"}


def _youtube() -> dict:
    env = (repo_root() / "YOUTUBE-AUTOMATION-FACTORY" / ".env").exists()
    video = list((repo_root() / "WORKFLOW-ESTATE" / "07-VIDEO-RUN").rglob("*.mp4"))
    if env and video:
        return {"nome": "YOUTUBE pubblicazione", "parte": True,
                "stato": "credenziali + video pronti", "serve": "-"}
    manca = []
    if not env:
        manca.append("canale + OAuth (M-EST-8)")
    if not video:
        manca.append("il video non e' renderizzato (solo pacchetto-script)")
    return {"nome": "YOUTUBE pubblicazione", "parte": False,
            "stato": "pipeline dati reali pronta (F1-F3), ma non pubblicabile",
            "serve": "MAX: " + " · ".join(manca)}


def _s7() -> dict:
    files = list((repo_root() / "company" / "Ecosistemi" / "12-STREAM-S7-BOT").glob("*.py"))
    paper = False
    for f in files:
        try:
            if "PAPER TRADING" in f.read_text(encoding="utf-8", errors="replace"):
                paper = True
                break
        except OSError:
            continue
    return {"nome": "NFT / STREAM-S7", "parte": bool(files) and paper,
            "stato": "PAPER TRADING (per design: nessun capitale reale a rischio)",
            "serve": "MAX: decisione se passare a capitale reale dopo che il paper prova un edge"}


def stato_workflow() -> list[dict]:
    return [_incasso(), _outreach(), _outreach_whatsapp(), _youtube(), _s7()]


def _cmd_controllo(a) -> int:
    ws = stato_workflow()
    print(_RESET)
    print("  DIGITAL EMPIRE — CENTRO DI COMANDO — TUTTI I WORKFLOW")
    print(_RESET)
    partono = [w for w in ws if w["parte"]]
    for w in ws:
        segno = "PARTE " if w["parte"] else "MAX   "
        print(f"  [{segno}] {w['nome']}")
        print(f"           stato:  {w['stato']}")
        if w["serve"] != "-":
            print(f"           serve:  {w['serve']}")
    print(_RESET)
    print(f"  {len(partono)}/{len(ws)} workflow pronti a partire senza un tuo atto.")
    print()
    print("  LE PORTE CHE DIPENDONO SOLO DA TE (nessuno le apre al posto tuo):")
    for w in ws:
        if not w["parte"] and w["serve"] != "-":
            print(f"     - {w['nome']}: {w['serve']}")
    print(_RESET)
    return 0


def register(sub) -> None:
    """Registrato via plugin loop (empire.flow.cli). `empire/cli.py` resta congelato."""
    p = sub.add_parser("controllo",
                       help="centro di comando: stato reale di tutti i workflow + cosa serve da Max")
    p.set_defaults(fn=_cmd_controllo)
