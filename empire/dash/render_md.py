"""
empire.dash.render_md — Rendering della dashboard in formato Markdown.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
import time
from pathlib import Path
from empire.paths import repo_root, rel
from empire.dash.kpi import KPI_REGISTRY


def render_md(data: dict) -> str:
    """Rigenera il file DASHBOARD.md in WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/."""
    root = repo_root()
    out_file = root / "WORKFLOW-ESTATE" / "06-DASHBOARD-E-METRICHE" / "DASHBOARD.md"
    out_file.parent.mkdir(parents=True, exist_ok=True)

    now_str = time.strftime("%Y-%m-%d %H:%M:%S")

    # Costruisci l'intestazione conforme ADR-008
    md = []
    md.append("---")
    md.append("Owner: Max")
    md.append("Controllore: Claude")
    md.append("Origine: Genesi-Core/07-CONTROL/DASHBOARD-E-RETRO.md")
    md.append("Governo: company/Mandato/MANDATO-EMPIRE.md")
    md.append("---")
    md.append("")
    md.append(f"# 📊 DASHBOARD OPERATIVA — Digital Empire")
    md.append(f"> Generato automaticamente il: **{now_str}**")
    md.append("")
    md.append("---")
    md.append("")

    # Section 1: I 6 gate della settimana
    md.append("## 🟢 I 6 Gate della Settimana (Estate 2026)")
    md.append("")
    md.append("| Stato | Gate | Scadenza | Condizione di Successo |")
    md.append("|---|---|---|---|")
    for g in data.get("gates_settimanali", []):
        md.append(f"| {g['status']} | **{g['gate']}** | {g['deadline']} | {g['condition']} |")
    md.append("")
    md.append("---")
    md.append("")

    # Section 2: Tabelle dei KPI
    md.append("## 📈 Metriche Operative")
    md.append("")

    # Raggruppa i KPI per proprietario o categoria
    md.append("### 1. Salute dell'Azienda (Company Health)")
    md.append("")
    md.append("| KPI | Valore | Stato | Responsabile | Soglia Good |")
    md.append("|---|---|---|---|---|")
    
    health_ids = {"agenti_progettati", "agenti_cf_grade", "ecosistemi_completi", "artefatti_adr008", "link_rotti", "workflow_conformi", "spazio_sprecato"}
    for k in KPI_REGISTRY:
        if k.id in health_ids:
            val = data.get(k.id, "n/d")
            status_color = k.evaluate_status(val)
            status_emoji = "🟢" if status_color == "green" else "🟡" if status_color == "yellow" else "🔴" if status_color == "red" else "⚪"
            
            # Formattazione
            val_str = str(val)
            if k.fmt == "mb" and isinstance(val, (int, float)):
                val_str = f"{val:.2f} MB"
            
            md.append(f"| {k.label} | `{val_str}` | {status_emoji} | {k.owner} | `{k.good or '-'}` |")
            
    md.append("")
    md.append("### 2. Telemetria e Performance (L2/L3)")
    md.append("")
    md.append("| KPI | Valore | Stato | Responsabile | Nota Sorgente |")
    md.append("|---|---|---|---|---|")
    
    perf_ids = {"runs_giornalieri", "scorecard_5d", "first_pass_rate", "ttd_medio", "tip_aperti", "traceability_rate"}
    for k in KPI_REGISTRY:
        if k.id in perf_ids:
            val = data.get(k.id, "n/d")
            status_emoji = "⚪" if "n/d" in str(val) else "🟢"
            md.append(f"| {k.label} | `{val}` | {status_emoji} | {k.owner} | {k.source} |")

    md.append("")
    md.append("### 3. Commerciale & Revenue")
    md.append("")
    md.append("| KPI | Valore | Stato | Responsabile | Soglia Good |")
    md.append("|---|---|---|---|---|")
    
    rev_ids = {"anticipi_incassati", "decisioni_attive"}
    for k in KPI_REGISTRY:
        if k.id in rev_ids:
            val = data.get(k.id, "n/d")
            status_color = k.evaluate_status(val)
            status_emoji = "🟢" if status_color == "green" else "🟡" if status_color == "yellow" else "🔴" if status_color == "red" else "⚪"
            md.append(f"| {k.label} | `{val}` | {status_emoji} | {k.owner} | `{k.good or '-'}` |")

    md.append("")
    md.append("---")
    md.append("")

    # Section 3: Lista Lead Concessionari
    md.append("## 📋 Stato dei 7 Lead Concessionari (S1)")
    md.append("")
    lead_list = data.get("lead_concessionari", [])
    if not lead_list:
        md.append("*Nessun lead qualificato trovato nel file lead.csv (n/d).*")
    else:
        md.append("| Concessionaria | Stato Relazione | Canale Preferito | Ultimo Contatto | Esito / Dettagli |")
        md.append("|---|---|---|---|---|")
        for l in lead_list:
            md.append(f"| {l.get('Concessionaria', '')} | **{l.get('Stato Relazione', '')}** | {l.get('Canale Preferito', '')} | {l.get('Ultimo Contatto', '')} | {l.get('Esito', '')} |")

    md.append("")
    md.append("---")
    md.append("")
    md.append("> ℹ️ *Nota visiva: I KPI sono estratti automaticamente da sorgenti di codice misurabile (cerchi pieni). I KPI commerciali sono aggiornati a mano via lead.csv (bordo tratteggiato in versione HTML).*")

    out_file.write_text("\n".join(md), encoding="utf-8")
    return rel(out_file)
