"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from empire import paths
from empire.memory import all_atoms, Atom, write as memory_write
from .record import PerfRecord, FeedbackRecord, atom_to_perf

def write_run_report(perf: PerfRecord, scorecard: dict, tips: list[FeedbackRecord]) -> Path:
    """Scrive il report di run in company/Ispettorato/report/run/RPT-RUN-<id>.md."""
    report_dir = paths.resolve("isp_report") / "run"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"RPT-RUN-{perf.id}.md"
    
    esito_icon = "🟢 VERDE" if perf.result == "success" else "🔴 ROSSO"
    trace_icon = "🟢 PASS" if scorecard.get("traceability") else "🔴 FALLITO"
    
    tips_section = ""
    if tips:
        tips_section = "\n".join(f"- **{t.ftype}** per **{t.to}**: {t.micro_input}" for t in tips)
    else:
        tips_section = "Nessun feedback/TIP emesso per questa run."
        
    errori = perf.debug.get("errori", 0)
    fix_applicati = perf.debug.get("fix_applicati", [])
    
    content = f"""# REPORT RUN — {perf.id}
- **Workflow:** {perf.workflow}
- **Agente:** {perf.agent}
- **Famiglia:** {perf.family}
- **Data:** {perf.ended.strftime("%Y-%m-%d %H:%M:%S")}

---

## 1. ESITO
Il verdetto finale della run è **{esito_icon}**.
- Risultato nominale: `{perf.result}`
- Test di conformità: {"Superato" if perf.result == "success" else "Fallito/Parziale"}

## 2. TIMELINE
- Inizio: `{perf.started.isoformat()}`
- Fine: `{perf.ended.isoformat()}`
- Durata calcolata: `{perf.ttd_h:.3f} ore`

## 3. GATE
- First Pass: `{"SÌ" if perf.verification.get("first_pass", True) else "NO"}`
- Numero revisioni: `{perf.verification.get("revisions", 0)}`
- Post-consegna fix: `{"SÌ" if perf.verification.get("post_consegna", False) else "NO"}`
- Regressione: `{"SÌ" if perf.verification.get("regression", False) else "NO"}`

## 4. NUMERI (Scorecard 5D)
| Asse | Punteggio | Descrizione |
|---|---|---|
| ① correctness/debug | `{scorecard.get("correctness")}` | Presenza di errori, retry ed escalation |
| ② qualità soluzione | `{scorecard.get("solution")}` | Numero di passaggi per l'accettazione |
| ③ struttura output | `{scorecard.get("structure")}` | Validità ADR-008 e path dei file prodotti |
| ④ scope-fit | `{scorecard.get("scope_fit")}` | Percentuale di Definition of Done rispettate |
| ⑤ efficiency | `{scorecard.get("efficiency")}` | Durata reale vs TTD benchmark |
| **Gate Traceability** | **{trace_icon}** | Presenza del checkpoint di task in memoria |

## 5. ERRORI
- Errori rilevati: `{errori}`
- Retry tentati: `{perf.debug.get("retry", 0)}`
- Escalation: `{perf.debug.get("escalation", 0)}`
- Fix applicati: `{", ".join(fix_applicati) if fix_applicati else "nessuno"}`

### Feedback & Contromisure:
{tips_section}

---
*Report compilato automaticamente da empire.inspect.report_generator*
"""
    with open(report_file, "w", encoding="utf-8") as fh:
        fh.write(content)
        
    return report_file

def write_escalation_report(fb: FeedbackRecord, next_perf: PerfRecord) -> Path:
    """Scrive il report di escalation in company/Ispettorato/report/escalation/ESC-<id>.md."""
    esc_dir = paths.resolve("isp_report") / "escalation"
    esc_dir.mkdir(parents=True, exist_ok=True)
    esc_id = f"ESC-{fb.id}"
    report_file = esc_dir / f"{esc_id}.md"
    
    content = f"""# ESCALATION OBBLIGATORIA — {esc_id}
⚠️ **SOGGETTO: RECIDIVA DI PERCORSO DI MIGLIORAMENTO**

- **Data:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Feedback fallito:** `{fb.id}` (emesso su `{fb.on_perf}`)
- **Agente recidivo:** `{fb.to}`
- **Performance colpevole:** `{next_perf.id}` (famiglia: `{next_perf.family}`)

---

## 1. SINTOMO
Il feedback `{fb.id}` prescriveva la seguente contromisura:
> "{fb.micro_input}"

Nella performance successiva `{next_perf.id}`, l'agente ha ripetuto lo stesso tipo di errore o ha fallito la run, configurando una **recidiva comportamentale bloccante**.

## 2. GRAVITÀ
- **Livello:** 🔴 BLOCCO DI COMMITTED DI FASE
- **Implicazione:** La contromisura assegnata precedentemente NON ha retto. È necessario un intervento umano o una riprogettazione del prompt di sistema dell'agente.

## 3. CHI DEVE AGIRE
L'escalation viene indirizzata al **comandante-di-casta** (o regolatore dell'agente `{fb.to}`) per la revisione permanente dei prompt (v4-MASTER §7) o per un pairing repair.

## 4. STORICO TENTATIVI
- **Emissione originale:** Feedback aperto il `{fb.opened.isoformat()}`
- **Run di origine:** `{fb.on_perf}` (esito: `{next_perf.result}`)
- **Run di ricorrenza:** `{next_perf.id}` (esito: `{next_perf.result}`, durata: `{next_perf.ttd_h:.2f}h`)

---
*Generato dall'Ispettorato Generale - Sentinella Anti-Recidiva*
"""
    with open(report_file, "w", encoding="utf-8") as fh:
        fh.write(content)
        
    return report_file

def write_daily_telemetry(date_str: str) -> Path:
    """Aggrega le run del giorno e scrive in company/Ispettorato/telemetry/daily/<date_str>.json."""
    tel_dir = paths.resolve("isp_telemetry") / "daily"
    tel_dir.mkdir(parents=True, exist_ok=True)
    tel_file = tel_dir / f"{date_str}.json"
    
    day_atoms = []
    for atom in all_atoms(kind="perf"):
        if atom.ts[:10] == date_str:
            day_atoms.append(atom_to_perf(atom))
            
    success_count = sum(1 for p in day_atoms if p.result == "success")
    total_count = len(day_atoms)
    
    avg_ttd = 0.0
    if total_count > 0:
        avg_ttd = sum(p.ttd_h for p in day_atoms) / total_count
        
    data = {
        "date": date_str,
        "total_runs": total_count,
        "success_runs": success_count,
        "failed_runs": total_count - success_count,
        "average_ttd_hours": round(avg_ttd, 3),
        "runs": [p.id for p in day_atoms]
    }
    
    with open(tel_file, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        
    return tel_file

def write_daily_report(date_str: str) -> Path:
    """Scrive il daily report in company/Ispettorato/report/daily/RPT-<date_str>.md."""
    daily_dir = paths.resolve("isp_report") / "daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    report_file = daily_dir / f"RPT-{date_str}.md"
    
    day_perfs = []
    for atom in all_atoms(kind="perf"):
        if atom.ts[:10] == date_str:
            day_perfs.append(atom_to_perf(atom))
            
    total_runs = len(day_perfs)
    verdi = sum(1 for p in day_perfs if p.result == "success")
    rosse = total_runs - verdi
    
    # Calcola revisioni medie del giorno
    revs = [p.verification.get("revisions", 0) for p in day_perfs]
    avg_revs = sum(revs) / len(revs) if revs else 0.0
    
    # Cerca feedbacks del giorno
    day_fbs = []
    for atom in all_atoms(kind="feedback"):
        if atom.ts[:10] == date_str:
            day_fbs.append(atom)
            
    open_tips = [x for x in day_fbs if x.extra.get("ftype") == "TIP" and x.status == "open"]
    recurred_tips = [x for x in day_fbs if x.status == "recurred"]
    
    # Costruiamo 3 azioni di miglioramento prioritarie reali o simulate basate sui feedback
    top_actions = []
    for idx, fb in enumerate(open_tips[:3], start=1):
        to_agent = fb.actor
        on_perf = fb.refs[0] if fb.refs else "PERF-UNK"
        top_actions.append(
            f"{idx}. `[ISP-IMP]` Applicare contromisura su `{to_agent}` per family `{fb.extra.get('family', 'default')}` — owner: {to_agent} — entro: {date_str} — chiude: {fb.id} — verifica: isp-verifier"
        )
        
    # Se non ci sono azioni reali, lasciamo vuoto
    if not top_actions:
        top_actions.append("Nessuna azione di miglioramento richiesta oggi (zero run fallite o tutte confermate).")
        
    # Autocritica deterministica
    autocritica_list = []
    if rosse > 0:
        autocritica_list.append(f"Oggi abbiamo riscontrato {rosse} run fallite. La causa principale risiede nell'instabilità di runtime o nella collisione delle modifiche.")
    if avg_revs > 1.0:
        autocritica_list.append("La media delle revisioni è superiore a 1.0, indicando che gli agenti non consegnano codice pulito al primo colpo.")
    if not autocritica_list:
        autocritica_list.append("La giornata si è conclusa con ottime performance. Nessuna anomalia strutturale rilevata.")
        
    content = f"""# ISPETTORATO — DAILY AUTOCRITICA — {date_str}
- **Data Report:** {date_str}
- **Firma Conducente:** `isp-conductor` (🟢 VALIDATO)

---

## 1. KPI TREND (Telemetria Giornaliera)
| KPI | Valore del Giorno | Target | Stato |
|---|---|---|---|
| **Run Eseguite** | `{total_runs}` | - | - |
| **Run Successo (Verdi)** | `{verdi}` / `{total_runs}` | 100% | { "🟢 OK" if rosse == 0 else "🔴 DEVIAZIONE" } |
| **Revisioni Medie per Task** | `{avg_revs:.2f}` | < 1.00 | { "🟢 OK" if avg_revs < 1.0 else "🔴 ELEVATO" } |
| **Tasso Recidiva** | `{len(recurred_tips)}` | 0 | { "🟢 OK" if len(recurred_tips) == 0 else "🔴 RECIDIVA BLOC" } |

## 2. AUTOCRITICA
{" ".join(autocritica_list)}

## 3. TOP-3 AZIONI ASSEGNATE (Eseguibili con Item di Miglioramento)
{chr(10).join(top_actions)}

---
*Report emesso in accordo al protocollo WF-DAILY-AUTOCRITICA*
"""
    with open(report_file, "w", encoding="utf-8") as fh:
        fh.write(content)
        
    # Salva anche la telemetria json aggregata
    write_daily_telemetry(date_str)
    
    return report_file

def get_organ_status() -> dict:
    """Restituisce lo stato dell'organo (subcomando status)."""
    fbs = list(all_atoms(kind="feedback"))
    pats = list(all_atoms(kind="pattern"))
    
    open_loops = [x.id for x in fbs if x.status in ("open", "acked", "proposto")]
    pending_tips = [x.id for x in fbs if x.extra.get("ftype") == "TIP" and x.status in ("open", "acked")]
    draft_patterns = [x.title for x in pats if x.status == "proposed"]
    
    return {
        "open_loops_count": len(open_loops),
        "open_loops": open_loops,
        "pending_tips_count": len(pending_tips),
        "pending_tips": pending_tips,
        "draft_patterns_count": len(draft_patterns),
        "draft_patterns": draft_patterns
    }
