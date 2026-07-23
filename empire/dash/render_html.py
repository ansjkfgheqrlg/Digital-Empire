"""
empire.dash.render_html — Generatore del cruscotto HTML autocontenuto ed offline-safe.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
import json
import time
from pathlib import Path
from empire.paths import repo_root, rel
from empire.dash.kpi import KPI_REGISTRY


def generate_svg_gauge(value: float, total: float, color: str) -> str:
    """Genera una barra di progresso SVG inline."""
    pct = min(1.0, max(0.0, value / total)) if total > 0 else 0
    w = 200
    h = 16
    fill_w = int(w * pct)
    return f"""
    <svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="border-radius:8px; background: var(--bg-muted);">
        <rect x="0" y="0" width="{fill_w}" height="{h}" fill="{color}" />
        <text x="10" y="12" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="var(--text-color)">{value}/{total} ({int(pct*100)}%)</text>
    </svg>
    """


def render_html(data: dict, history_trend: dict | None = None) -> str:
    """Genera il file empire/.data/dashboard.html autocontenuto."""
    root = repo_root()
    out_file = root / "empire" / ".data" / "dashboard.html"
    out_file.parent.mkdir(parents=True, exist_ok=True)

    # Dati da incorporare
    json_data = json.dumps(data, indent=2, ensure_ascii=False)
    now_str = time.strftime("%Y-%m-%d %H:%M:%S")

    # Renderizzazione dei Gate
    gates_html = []
    for g in data.get("gates_settimanali", []):
        status_class = "gate-green" if g["status"] == "🟢" else "gate-red" if g["status"] == "🔴" else "gate-pending"
        gates_html.append(f"""
        <div class="gate-card {status_class}">
            <div class="gate-status-badge">{g["status"]}</div>
            <div class="gate-name">{g["gate"]}</div>
            <div class="gate-deadline">Deadline: {g["deadline"]}</div>
            <div class="gate-condition">{g["condition"]}</div>
        </div>
        """)

    # Renderizzazione dei KPI per categoria
    kpi_cards = {"health": [], "perf": [], "rev": []}
    
    health_ids = {"agenti_progettati", "agenti_cf_grade", "ecosistemi_completi", "artefatti_adr008", "link_rotti", "workflow_conformi", "spazio_sprecato"}
    perf_ids = {"runs_giornalieri", "scorecard_5d", "first_pass_rate", "ttd_medio", "tip_aperti", "traceability_rate"}
    rev_ids = {"anticipi_incassati", "decisioni_attive"}

    for k in KPI_REGISTRY:
        val = data.get(k.id, "n/d")
        status_color = k.evaluate_status(val)
        
        # Determina il tipo di sorgente per il bordo tratteggiato
        is_manual = "manuale" in k.source or k.id in ("anticipi_incassati", "lead_concessionari")
        is_nd = val is None or "n/d" in str(val)
        
        card_class = "kpi-card"
        if is_manual:
            card_class += " kpi-manual"
        if is_nd:
            card_class += " kpi-nd"
            
        status_badge = "status-gray"
        if not is_nd:
            status_badge = f"status-{status_color}"

        val_str = str(val)
        if k.fmt == "mb" and isinstance(val, (int, float)):
            val_str = f"{val:.2f} MB"
            
        # Widget visuale aggiuntivo se applicabile
        widget = ""
        if k.id == "agenti_cf_grade" and not is_nd:
            # Mostra progresso rispetto al target di 10
            widget = generate_svg_gauge(float(val), 10, "var(--primary-color)")
        elif k.id == "ecosistemi_completi" and not is_nd:
            widget = generate_svg_gauge(float(val), 10, "var(--primary-color)")
        elif k.id == "artefatti_adr008" and not is_nd:
            # Progresso rispetto al totale
            total_subj = data.get("agenti_progettati", 100)
            if isinstance(total_subj, (int, float)):
                widget = generate_svg_gauge(float(val), float(total_subj), "var(--success-color)")

        card_html = f"""
        <div class="{card_class}" title="Sorgente: {k.source}">
            <div class="kpi-header">
                <span class="kpi-label">{k.label}</span>
                <span class="status-dot {status_badge}"></span>
            </div>
            <div class="kpi-value">{val_str}</div>
            <div class="kpi-footer">
                <span class="kpi-owner">Owner: {k.owner}</span>
                <span class="kpi-source-type">{"Manuale" if is_manual else "N/D" if is_nd else "Misurato"}</span>
            </div>
            {f'<div class="kpi-widget">{widget}</div>' if widget else ''}
        </div>
        """
        
        if k.id in health_ids:
            kpi_cards["health"].append(card_html)
        elif k.id in perf_ids:
            kpi_cards["perf"].append(card_html)
        elif k.id in rev_ids:
            kpi_cards["rev"].append(card_html)

    # Tabella Lead Concessionari
    lead_rows = []
    for l in data.get("lead_concessionari", []):
        lead_rows.append(f"""
        <tr>
            <td><strong>{l.get("Concessionaria", "")}</strong></td>
            <td><span class="lead-badge">{l.get("Stato Relazione", "")}</span></td>
            <td>{l.get("Canale Preferito", "")}</td>
            <td>{l.get("Ultimo Contatto", "")}</td>
            <td>{l.get("Esito", "")}</td>
        </tr>
        """)
    
    lead_table_html = ""
    if lead_rows:
        lead_table_html = f"""
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Concessionaria</th>
                        <th>Stato Relazione</th>
                        <th>Canale</th>
                        <th>Ultimo Contatto</th>
                        <th>Esito</th>
                    </tr>
                </thead>
                <tbody>
                    {"".join(lead_rows)}
                </tbody>
            </table>
        </div>
        """
    else:
        lead_table_html = "<p class='hint'>Nessun lead qualificato inserito in lead.csv.</p>"

    # Generazione grafico di Trend Storico se disponibile
    trend_svg = ""
    if history_trend and len(history_trend) >= 2:
        sorted_dates = sorted(history_trend.keys())
        points = []
        max_val = 1
        for idx, date in enumerate(sorted_dates):
            snap = history_trend[date]
            val = snap.get("link_rotti", 0)
            try:
                val = float(val)
            except Exception:
                val = 0
            if val > max_val:
                max_val = val
        
        w, h = 500, 150
        padding = 30
        
        # Calcola le coordinate
        for idx, date in enumerate(sorted_dates):
            snap = history_trend[date]
            val = snap.get("link_rotti", 0)
            try:
                val = float(val)
            except Exception:
                val = 0
            
            x = padding + (idx * (w - 2 * padding) / (len(sorted_dates) - 1))
            y = h - padding - (val * (h - 2 * padding) / max_val)
            points.append((x, y))
            
        poly_points = " ".join(f"{x},{y}" for x, y in points)
        
        circles = []
        labels = []
        for idx, (x, y) in enumerate(points):
            date = sorted_dates[idx]
            val = history_trend[date].get("link_rotti", 0)
            circles.append(f'<circle cx="{x}" cy="{y}" r="4" fill="var(--primary-color)" />')
            labels.append(f'<text x="{x}" y="{h - 10}" font-family="sans-serif" font-size="8" fill="var(--text-muted)" text-anchor="middle">{date[5:]}</text>')
            labels.append(f'<text x="{x}" y="{y - 8}" font-family="sans-serif" font-weight="bold" font-size="9" fill="var(--text-color)" text-anchor="middle">{int(val)}</text>')
            
        trend_svg = f"""
        <div class="trend-chart-box">
            <h3>Discesa dei Link Rotti (Trend Storico)</h3>
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}">
                <line x1="{padding}" y1="{h - padding}" x2="{w - padding}" y2="{h - padding}" stroke="var(--border-color)" stroke-width="1" />
                <polyline points="{poly_points}" stroke="var(--primary-color)" fill="none" stroke-width="3" />
                {"".join(circles)}
                {"".join(labels)}
            </svg>
        </div>
        """

    # HTML Template
    html = f"""<!DOCTYPE html>
<html lang="it" data-theme="dark">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Empire — Dashboard Operativa</title>
    <style>
        :root[data-theme="light"] {{
            --bg-color: #f8fafc;
            --bg-card: #ffffff;
            --bg-muted: #f1f5f9;
            --text-color: #0f172a;
            --text-muted: #64748b;
            --border-color: #cbd5e1;
            --primary-color: #fb4604;
            --success-color: #10b981;
            --danger-color: #ef4444;
            --warning-color: #f59e0b;
        }}
        :root[data-theme="dark"] {{
            --bg-color: #0f172a;
            --bg-card: #1e293b;
            --bg-muted: #334155;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #475569;
            --primary-color: #fb4604;
            --success-color: #10b981;
            --danger-color: #ef4444;
            --warning-color: #f59e0b;
        }}
        
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 24px;
            line-height: 1.5;
            transition: background-color 0.3s, color 0.3s;
        }}
        
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 16px;
            margin-bottom: 24px;
        }}
        
        h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: 800;
            letter-spacing: -0.025em;
        }}
        
        h2 {{
            font-size: 18px;
            font-weight: 700;
            margin-top: 32px;
            margin-bottom: 16px;
            color: var(--primary-color);
        }}
        
        h3 {{
            font-size: 14px;
            font-weight: 600;
            margin: 0 0 12px 0;
        }}

        .theme-toggle {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
        }}
        
        /* Gates Grid */
        .gates-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}
        
        .gate-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            position: relative;
        }}
        
        .gate-name {{
            font-weight: bold;
            font-size: 16px;
            margin-bottom: 4px;
        }}
        
        .gate-deadline {{
            font-size: 12px;
            color: var(--text-muted);
            margin-bottom: 8px;
        }}
        
        .gate-condition {{
            font-size: 11px;
            font-weight: 500;
        }}
        
        .gate-status-badge {{
            position: absolute;
            top: 12px;
            right: 12px;
            font-size: 18px;
        }}

        .gate-green {{ border-left: 4px solid var(--success-color); }}
        .gate-red {{ border-left: 4px solid var(--danger-color); }}
        .gate-pending {{ border-left: 4px solid var(--warning-color); }}
        
        /* KPIs Grid */
        .kpis-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
        }}
        
        .kpi-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 100px;
        }}
        
        .kpi-manual {{
            border-style: dashed;
        }}
        
        .kpi-nd {{
            background: var(--bg-muted);
            opacity: 0.8;
        }}

        .kpi-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .kpi-label {{
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
        }}
        
        .kpi-value {{
            font-size: 24px;
            font-weight: 800;
            margin: 12px 0;
            font-variant-numeric: tabular-nums;
        }}
        
        .kpi-footer {{
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            color: var(--text-muted);
        }}
        
        .kpi-widget {{
            margin-top: 8px;
        }}

        .status-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
        }}
        
        .status-green {{ background-color: var(--success-color); }}
        .status-yellow {{ background-color: var(--warning-color); }}
        .status-red {{ background-color: var(--danger-color); }}
        .status-gray {{ background-color: var(--text-muted); }}
        
        /* Tables */
        .table-container {{
            width: 100%;
            overflow-x: auto;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            background: var(--bg-card);
            margin-top: 16px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 13px;
        }}
        
        th, td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}
        
        th {{
            background: var(--bg-muted);
            font-weight: 700;
            color: var(--text-muted);
        }}
        
        .lead-badge {{
            background: var(--bg-muted);
            color: var(--text-color);
            padding: 4px 8px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 11px;
        }}

        .trend-chart-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            margin-top: 24px;
        }}
        
        .hint {{
            font-size: 12px;
            color: var(--text-muted);
        }}
    </style>
</head>
<body>

    <header>
        <div>
            <h1>📊 DIGITAL EMPIRE</h1>
            <div class="hint">Cruscotto Metriche Aziendali &bull; Aggiornato il: {now_str}</div>
        </div>
        <button class="theme-toggle" onclick="toggleTheme()">Tema</button>
    </header>

    <h2>🟢 I 6 Gate della Settimana (Estate 2026)</h2>
    <div class="gates-grid">
        {"".join(gates_html)}
    </div>

    {trend_svg}

    <h2>📈 Salute dell'Azienda (Company Health)</h2>
    <div class="kpis-grid">
        {"".join(kpi_cards["health"])}
    </div>

    <h2>🛡️ Performance e Telemetria (Inspect L2/L3)</h2>
    <div class="kpis-grid">
        {"".join(kpi_cards["perf"])}
    </div>

    <h2>💰 Commerciale & Revenue (S1/S2)</h2>
    <div class="kpis-grid">
        {"".join(kpi_cards["rev"])}
    </div>

    <h2>📋 Stato dei 7 Lead Concessionari (S1)</h2>
    {lead_table_html}

    <script type="application/json" id="kpi-data">
        {json_data}
    </script>

    <script>
        function toggleTheme() {{
            const html = document.documentElement;
            const current = html.getAttribute('data-theme');
            const target = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', target);
        }}
    </script>
</body>
</html>
"""
    out_file.write_text(html, encoding="utf-8")
    return rel(out_file)
