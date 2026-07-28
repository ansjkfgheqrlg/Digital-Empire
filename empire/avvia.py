"""
EMPIRE — accensione del sistema nervoso del Workflow Estate: `python -m empire avvia-estate`.

Owner: Claude · Origine: FORGE (accensione one-command, CP-20260728)

## Perché

Max: "voglio accendere tutto il sistema nervoso del Workflow Estate con UN solo comando".
Il cervello era già operativo (estate/forge/trace/dash) ma sparso su comandi diversi. Questo
e' l'interruttore unico: un colpo, e il cervello si accende, si misura e dice cosa fare adesso.

## Cosa fa (in ordine)

1. rigenera la dashboard (i KPI dai dati veri)
2. valuta i 6 gate + i controlli di completamento (riusa `estate.run_checks`)
3. misura gli agenti operativi (riusa `forge`)
4. conta i cicli di memoria (riusa `trace`)
5. scrive una traccia di SESSIONE "avvio" — l'accensione stessa lascia una traccia
6. stampa UN cruscotto: stato · cosa fare adesso · cosa resta a Max

Non fa partire invii/incassi/pubblicazioni: quelle sono le porte d'uscita, restano di Max
(regola estate = cervello, non muscolo). Accende il cervello, non spara verso l'esterno.
"""
from __future__ import annotations

from datetime import datetime

from .paths import repo_root

__all__ = ["accendi", "register"]

_RESET = "=" * 74


def _riga(ok: bool | None, etichetta: str, valore: str) -> str:
    segno = "  " if ok is None else ("OK" if ok else "!!")
    return f"  {segno}  {etichetta:32} {valore}"


def _step_dashboard() -> tuple[bool, str]:
    """Rigenera la dashboard con la stessa logica di `dash build` (collect -> render_md)."""
    try:
        from .dash.collect import collect_all  # noqa: PLC0415
        from .dash.render_md import render_md  # noqa: PLC0415
        data = collect_all()
        md_path = render_md(data)   # scrive il file e ritorna il path
        return True, f"rigenerata ({md_path})"
    except Exception as e:  # noqa: BLE001
        return False, f"non rigenerata: {e}"


def _step_gate() -> tuple[int, int, list]:
    from . import estate as _estate  # noqa: PLC0415
    checks = _estate.run_checks()
    verdi = [c for c in checks if c.ok]
    rossi_nostri = [c for c in checks if not c.ok and getattr(c, "owner", "noi") == "noi"]
    return len(verdi), len(checks), rossi_nostri


def _step_agenti() -> tuple[int, int]:
    try:
        from . import forge as _forge  # noqa: PLC0415
        schede = _forge.checklist()
    except Exception:  # noqa: BLE001
        return 0, 0
    operativi = sum(1 for s in schede if s.stato == "OPERATIVO")
    return operativi, len(schede)


def _step_tracce() -> int:
    try:
        from . import trace as _trace  # noqa: PLC0415
        return sum(_trace.conta().values())
    except Exception:  # noqa: BLE001
        return 0


def _step_scrivi_avvio() -> str:
    try:
        from . import trace as _trace  # noqa: PLC0415
        ts = datetime.now().astimezone().isoformat(timespec="minutes")
        p = _trace.scrivi(
            "sessione", f"Accensione sistema nervoso Workflow Estate ({ts})",
            autore="avvia-estate", prova="python -m empire avvia-estate eseguito",
            contesto="Interruttore unico: dashboard rigenerata, gate valutati, agenti misurati, tracce contate.",
            tags=["avvio", "estate", "sistema-nervoso"])
        return str(p.relative_to(repo_root()))
    except Exception as e:  # noqa: BLE001
        return f"(traccia avvio non scritta: {e})"


def accendi(*, verbose: bool = False) -> int:
    """Accende il cervello e stampa il cruscotto. Exit 0 = acceso e senza rossi di costruzione."""
    print(_RESET)
    print("  SISTEMA NERVOSO — WORKFLOW ESTATE — ACCENSIONE")
    print(_RESET)

    ok_dash, msg_dash = _step_dashboard()
    print(_riga(ok_dash, "dashboard", msg_dash))

    verdi, totali, rossi_nostri = _step_gate()
    print(_riga(not rossi_nostri, "controlli verdetto", f"{verdi}/{totali} verdi"))

    operativi, tot_ag = _step_agenti()
    print(_riga(None, "agenti operativi", f"{operativi} su {tot_ag}"))

    n_tracce = _step_tracce()
    print(_riga(None, "cicli di memoria (tracce)", str(n_tracce)))

    traccia = _step_scrivi_avvio()
    print(_riga(True, "traccia di avvio scritta", traccia))

    print(_RESET)
    if rossi_nostri:
        print(f"  ACCESO CON RISERVA: {len(rossi_nostri)} controlli di costruzione da chiudere:")
        for c in rossi_nostri:
            print(f"     - {c.name}: {c.detail}")
    else:
        print("  ✅ SISTEMA NERVOSO ACCESO. Cervello operativo.")

    print()
    print("  COSA FARE ADESSO (dettaglio: WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/AZIONI-MAX.md):")
    print("     1. Gate-CONTATTI  -> lead veri tracciabili (scraper province vere, M-EST-9)")
    print("     2. Gate-REV       -> 2 Payment Link Stripe (10 min) sbloccano l'incasso")
    print()
    print("  Comandi vivi:  empire estate  ·  empire forge scan  ·  empire trace stato")
    print(_RESET)

    return 1 if rossi_nostri else 0


def _cmd_avvia(a) -> int:
    return accendi(verbose=getattr(a, "verbose", False))


def register(sub) -> None:
    """Registrato dal loop di plugin (via empire.flow.cli). `empire/cli.py` resta congelato."""
    p = sub.add_parser("avvia-estate",
                       help="accende il sistema nervoso del Workflow Estate con un comando")
    p.add_argument("--verbose", "-v", action="store_true")
    p.set_defaults(fn=_cmd_avvia)
