"""
empire.dash.cli — Sottocomandi CLI per la dashboard (python -m empire dash *).

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
import sys
import webbrowser
from pathlib import Path

from empire.paths import repo_root, safe_stdout
from empire.dash.collect import collect_all
from empire.dash.kpi import KPI_REGISTRY

safe_stdout()


def cmd_build(a) -> int:
    from empire.dash.render_md import render_md
    from empire.dash.render_html import render_html
    from empire.dash.history import save_snapshot, get_history_trend
    
    data = collect_all()
    
    # 1. Salva lo snapshot storico giornaliero
    snapshot_path = save_snapshot(data)
    
    # 2. Renderizza il Markdown
    md_path = render_md(data)
    
    # 3. Renderizza l'HTML con trend storico
    trend = get_history_trend()
    html_path = render_html(data, history_trend=trend)
    
    print(f"Dashboard rigenerata con successo:")
    print(f"  - Markdown: {md_path}")
    print(f"  - HTML:     {html_path}")
    print(f"  - Snapshot: {snapshot_path}")
    return 0


def cmd_show(a) -> int:
    root = repo_root()
    html_path = root / "empire" / ".data" / "dashboard.html"
    if not html_path.exists():
        print("La dashboard non è ancora stata compilata. Esegui prima: python -m empire dash build")
        return 1
    
    webbrowser.open(html_path.as_uri())
    print(f"Aperta la dashboard nel browser predefinito: {html_path.as_uri()}")
    return 0


def cmd_kpi(a) -> int:
    data = collect_all()
    kpi_id = a.kpi_id

    # Trova il KPI nel registro
    kpi = next((k for k in KPI_REGISTRY if k.id == kpi_id), None)
    if not kpi:
        print(f"KPI sconosciuto: {kpi_id}")
        return 1

    val = data.get(kpi_id, "n/d")
    status = kpi.evaluate_status(val)
    
    print(f"KPI: {kpi.label} ({kpi.id})")
    print(f"  Valore:      {val}")
    print(f"  Sorgente:    {kpi.source}")
    print(f"  Stato:       {status.upper()}")
    print(f"  Proprietario:{kpi.owner}")
    return 0


def cmd_trend(a) -> int:
    from empire.dash.history import get_history_trend
    days = int(a.days)
    trend = get_history_trend(days)
    
    if not trend:
        print("Nessuno storico disponibile. Esegui 'dash build' in giorni diversi per raccogliere i dati.")
        return 0

    print(f"=== TREND DEGLI ULTIMI {days} GIORNI ===")
    for date, snap in sorted(trend.items()):
        l_rotti = snap.get("link_rotti", "n/d")
        adr008 = snap.get("artefatti_adr008", "n/d")
        cf_grade = snap.get("agenti_cf_grade", "n/d")
        print(f"[{date}] Link Rotti: {l_rotti} | Conformi ADR-008: {adr008} | CF-Grade: {cf_grade}")
    return 0


def cmd_gates(a) -> int:
    data = collect_all()
    gates = data.get("gates_settimanali", [])

    if not gates:
        print("Nessun gate trovato in WF-MASTER.md.")
        return 0

    print("=== STATO DEI 6 GATE SETTIMANALI ===")
    for g in gates:
        print(f"[{g['status']}] {g['gate']:<10} Deadline: {g['deadline']:<12} Se: {g['condition']}")
    return 0


def register(sub) -> None:
    p = sub.add_parser("dash", help="gestione del cruscotto aziendale e delle metriche statiche")
    dash_sub = p.add_subparsers(dest="dash_cmd", required=True)

    # 1. dash build
    p_build = dash_sub.add_parser("build", help="compila la dashboard in HTML, Markdown e salva lo snapshot")
    p_build.set_defaults(fn=cmd_build)

    # 2. dash show
    p_show = dash_sub.add_parser("show", help="apre la dashboard HTML compilata nel browser locale")
    p_show.set_defaults(fn=cmd_show)

    # 3. dash kpi <id>
    p_kpi = dash_sub.add_parser("kpi", help="mostra le informazioni e il valore di un singolo KPI")
    p_kpi.add_argument("kpi_id", help="l'identificativo del KPI (es: link_rotti)")
    p_kpi.set_defaults(fn=cmd_kpi)

    # 4. dash trend [--days N]
    p_trend = dash_sub.add_parser("trend", help="mostra l'evoluzione storica dei KPI")
    p_trend.add_argument("--days", default="14", help="numero di giorni da tracciare nello storico")
    p_trend.set_defaults(fn=cmd_trend)

    # 5. dash gates
    p_gates = dash_sub.add_parser("gates", help="mostra lo stato sintetico dei 6 gate del lancio estivo")
    p_gates.set_defaults(fn=cmd_gates)
