"""
empire.dash.collect — Raccoglitore di metriche e dati per la dashboard.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
import csv
import json
from pathlib import Path

from empire.paths import repo_root, rel
from empire.registry import census, links
from empire import loader, conform




def collect_all() -> dict:
    """Raccoglie tutti i dati dei KPI da fonti programmate o manuali."""
    root = repo_root()

    # -------------------------------------------------------------
    # 1. Salute dell'Azienda (Company Health)
    # -------------------------------------------------------------
    try:
        agents = loader.load_agents()
        agenti_progettati = len(agents)
        agenti_cf_grade = len([a for a in agents if getattr(a, "cf_grade", False)])
    except Exception as e:
        agenti_progettati = "n/d"
        agenti_cf_grade = f"n/d (errore: {e})"

    try:
        ecos = loader.load_ecosystems()
        ecosistemi_completi = len([e for e in ecos if getattr(e, "has_backbone", False) and getattr(e, "has_ecosistema_md", False)])
    except Exception as e:
        ecosistemi_completi = f"n/d (errore: {e})"

    try:
        # Carica il censimento da cache census.json (se esiste) o lo rigenera
        artifacts = census.load_census()
        total_artifacts = len(artifacts)
        
        # Filtra i tipi di artefatto soggetti ad ADR-008
        subject_kinds = {"agent", "department", "ecosystem", "workflow", "skill", "script"}
        relevant_artifacts = [a for a in artifacts if getattr(a, "kind", "doc") in subject_kinds]
        
        # Conta quanti hanno provenienza completa
        adr008_count = len([a for a in relevant_artifacts if getattr(a, "prov", None) and a.prov.complete])
    except Exception as e:
        adr008_count = f"n/d (errore: {e})"
        artifacts = []

    try:
        # Risoluzione link ottimizzata con cache per evitare I/O ridondanti su migliaia di file
        resolved_cache = {}
        link_rotti = 0
        non_vendored_arts = [a for a in artifacts if not conform.is_vendored(a.path)]
        
        for a in non_vendored_arts:
            abs_dir = (root / a.path).parent
            for ref in getattr(a, "references", []):
                cache_key = (str(abs_dir), ref)
                if cache_key in resolved_cache:
                    is_ok = resolved_cache[cache_key]
                else:
                    # 1. Relativo al file
                    rel_to_file = abs_dir / ref
                    if rel_to_file.exists():
                        is_ok = True
                    else:
                        # 2. Relativo alla root
                        rel_to_root = root / ref.lstrip("./")
                        if rel_to_root.exists():
                            is_ok = True
                        else:
                            # 3. Via legacy
                            legacy_res = conform.resolve_legacy(ref, cited_from=abs_dir)
                            is_ok = (legacy_res is not None and legacy_res.exists())
                    resolved_cache[cache_key] = is_ok
                
                if not is_ok:
                    link_rotti += 1
    except Exception as e:
        link_rotti = f"n/d (errore: {e})"

    try:
        # Calcola workflow conformi ad Art.8
        wf_paths = set()
        for w in loader.load_workflows():
            # Estrae la cartella radice (es: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/ -> WORKFLOW-ESTATE)
            parts = Path(rel(w.path)).parts
            if parts:
                wf_paths.add(parts[0])

        compliant_wf = 0
        for wf_dir in wf_paths:
            wf_root = root / wf_dir
            if wf_root.is_dir():
                findings = conform.check_art8(wf_root)
                if not any(f.rule == "MANDATO-Art8" and f.severity == "block" for f in findings):
                    compliant_wf += 1
        workflow_conformi = compliant_wf
    except Exception as e:
        workflow_conformi = f"n/d (errore: {e})"

    try:
        dupes_file = root / "empire" / ".data" / "duplicates.json"
        if dupes_file.exists():
            with open(dupes_file, "r", encoding="utf-8") as f:
                dupes_data = json.load(f)
            spazio_sprecato = sum(d.get("wasted_bytes", 0) for d in dupes_data) / (1024 * 1024)
        else:
            spazio_sprecato = "n/d (duplicates.json mancante)"
    except Exception as e:
        spazio_sprecato = f"n/d (errore: {e})"

    # -------------------------------------------------------------
    # 2. Performance (Telemetry) - Assenti in attesa di GEM-03
    # -------------------------------------------------------------
    runs_giornalieri = "n/d (modulo inspect non ancora implementato)"
    scorecard_5d = "n/d (modulo inspect non ancora implementato)"
    first_pass_rate = "n/d (modulo inspect non ancora implementato)"
    ttd_medio = "n/d (modulo inspect non ancora implementato)"
    tip_aperti = "n/d (modulo inspect non ancora implementato)"
    traceability_rate = "n/d (modulo inspect non ancora implementato)"

    # -------------------------------------------------------------
    # 3. Revenue, Lead e Gate
    # -------------------------------------------------------------
    lead_list = []
    try:
        lead_file = root / "WORKFLOW-ESTATE" / "06-DASHBOARD-E-METRICHE" / "lead.csv"
        if lead_file.exists():
            with open(lead_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    lead_list.append(row)
    except Exception:
        pass

    try:
        # Conta quanti concessionari sono in stato "incassato" da lead.csv o state/revenue.json
        incassati_leads = len([l for l in lead_list if l.get("Stato Relazione", "").strip().lower() == "incassato" or l.get("Stato", "").strip().lower() == "incassato"])

        revenue_file = root / "EmpireDesk" / "state" / "revenue.json"
        incassati_rev = 0
        if revenue_file.exists():
            with open(revenue_file, "r", encoding="utf-8") as f:
                rev_data = json.load(f)
            incassati_rev = len([c for c in rev_data.get("concessionari", []) if c.get("stato") == "incassato"])
        
        anticipi_incassati = max(incassati_leads, incassati_rev)
    except Exception as e:
        anticipi_incassati = f"n/d (errore: {e})"

    decisioni_attive = "n/d (modulo memory non ancora implementato)"

    # Gate settimanali caricati da WF-MASTER.md
    gates_list = []
    try:
        wf_master_path = root / "WORKFLOW-ESTATE" / "01-FLUSSI-E-PIANI" / "WF-MASTER.md"
        if wf_master_path.exists():
            content = wf_master_path.read_text(encoding="utf-8")
            in_table = False
            for line in content.splitlines():
                if "| Gate |" in line:
                    in_table = True
                    continue
                if in_table and line.startswith("|"):
                    if "---|---" in line:
                        continue
                    parts = [p.strip() for p in line.split("|") if p.strip()]
                    if len(parts) >= 3:
                        gates_list.append({
                            "gate": parts[0],
                            "deadline": parts[1],
                            "condition": parts[2],
                            "status": "⏳"
                        })
                elif in_table and not line.strip():
                    in_table = False

        # Sovrascrive stati con gates_status.json
        gates_status_file = root / "empire" / ".data" / "gates_status.json"
        if gates_status_file.exists():
            with open(gates_status_file, "r", encoding="utf-8") as f:
                status_map = json.load(f)
            for g in gates_list:
                name = g["gate"]
                if name in status_map:
                    g["status"] = status_map[name]
        else:
            # Stato di default per la settimana estate
            for g in gates_list:
                if g["gate"] in ("DEC", "FUNNEL"):
                    g["status"] = "🟢"
                elif g["gate"] == "CONTATTI":
                    # Fino alle 12:00 del 23/07 è in corso / pendente
                    g["status"] = "⏳"
    except Exception:
        pass

    return {
        "agenti_progettati": agenti_progettati,
        "agenti_cf_grade": agenti_cf_grade,
        "ecosistemi_completi": ecosistemi_completi,
        "artefatti_adr008": adr008_count,
        "link_rotti": link_rotti,
        "workflow_conformi": workflow_conformi,
        "spazio_sprecato": spazio_sprecato,
        "runs_giornalieri": runs_giornalieri,
        "scorecard_5d": scorecard_5d,
        "first_pass_rate": first_pass_rate,
        "ttd_medio": ttd_medio,
        "tip_aperti": tip_aperti,
        "traceability_rate": traceability_rate,
        "anticipi_incassati": anticipi_incassati,
        "decisioni_attive": decisioni_attive,
        "lead_concessionari": lead_list,
        "gates_settimanali": gates_list
    }
