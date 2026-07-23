"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from empire import paths
from empire.memory import Atom, write as memory_write, all_atoms, read as memory_read
from .record import PerfRecord, perf_to_atom, atom_to_perf
from .collector import capture_run
from .analyst import calculate_scorecard
from .synth import synthesize_patterns
from .dispatch import dispatch_feedback
from .confirm import process_t5_confirm
from .report import write_daily_report, get_organ_status, write_run_report

def cmd_capture(a) -> int:
    try:
        started = datetime.fromisoformat(a.started)
        ended = datetime.fromisoformat(a.ended)
    except ValueError as e:
        print(f"ERRORE: Formato data non valido (usa ISO 8601): {e}", file=sys.stderr)
        return 1
        
    ttd_h = (ended - started).total_seconds() / 3600.0
    
    perf = PerfRecord(
        id="",
        agent=a.agent,
        task=a.task,
        workflow=a.wf,
        family=a.family,
        result=a.result,
        started=started,
        ended=ended,
        ttd_h=ttd_h,
        debug={
            "errori": a.errori,
            "retry": a.retry,
            "escalation": a.escalation,
            "fix_applicati": a.fix_applicati or []
        },
        output_ref=[Path(p) for p in (a.output_ref or [])],
        verification={
            "verificatore": a.verificatore,
            "first_pass": a.first_pass,
            "revisions": a.revisions,
            "post_consegna": a.post_consegna,
            "regression": a.regression,
            "dods_total": a.dods_total,
            "dods_verified": a.dods_verified,
        },
        scorecard={},
        feedback_ids=[]
    )
    
    captured = capture_run(perf)
    print(f"Run catturata con ID: {captured.id} (salvata in telemetria e memoria)")
    return 0

def cmd_analyze(a) -> int:
    perf_ids = []
    if a.perf:
        perf_ids.append(a.perf)
    else:
        for atom in all_atoms(kind="perf"):
            if not atom.extra.get("scorecard"):
                perf_ids.append(atom.id)
                
    if not perf_ids:
        print("Nessuna performance da analizzare.")
        return 0
        
    for pid in perf_ids:
        atom = memory_read(pid)
        if not atom:
            print(f"Performance {pid} non trovata.")
            continue
        perf = atom_to_perf(atom)
        
        # T2 analyze
        scorecard = calculate_scorecard(perf)
        perf.scorecard = scorecard
        
        # T3 synthesize
        synthesize_patterns(perf)
        
        # Aggiorna l'atomo perf con la scorecard
        updated_atom = perf_to_atom(perf)
        memory_write(updated_atom)
        
        # T4 dispatch
        tips = dispatch_feedback(perf.id, dry_run=False)
        perf.feedback_ids = [t.id for t in tips if t.id]
        
        # Ri-salva per includere i feedback_ids
        updated_atom = perf_to_atom(perf)
        memory_write(updated_atom)
        
        # Scrittura report
        report_path = write_run_report(perf, scorecard, tips)
        print(f"Analisi completata per {perf.id}. Report: {report_path.name}")
        
    return 0

def cmd_dispatch(a) -> int:
    count = 0
    for atom in all_atoms(kind="perf"):
        if not atom.refs:
            tips = dispatch_feedback(atom.id, dry_run=a.dry_run)
            if tips:
                count += len(tips)
                print(f"Dispacciati {len(tips)} feedback per {atom.id} (dry-run={a.dry_run})")
    if count == 0:
        print("Nessun feedback da dispacciare.")
    return 0

def cmd_confirm(a) -> int:
    updated = process_t5_confirm(a.family, a.agent)
    if updated:
        for fb in updated:
            print(f"Feedback {fb.id} aggiornato a stato: {fb.status}")
    else:
        print(f"Nessun feedback pendente per {a.agent} su {a.family} confermato o ricorso.")
    return 0

def cmd_report(a) -> int:
    date_str = a.date or datetime.now().strftime("%Y-%m-%d")
    date_str = date_str.strip()
    p = write_daily_report(date_str)
    print(f"Report daily scritto in: {p.name}")
    return 0

def cmd_status(a) -> int:
    status = get_organ_status()
    print("STATO ISPETTORATO GENERALE")
    print(f"  Loop aperti:      {status['open_loops_count']}")
    if status['open_loops']:
        print(f"    -> {', '.join(status['open_loops'])}")
    print(f"  TIP non confermati: {status['pending_tips_count']}")
    if status['pending_tips']:
        print(f"    -> {', '.join(status['pending_tips'])}")
    print(f"  Pattern in DRAFT:  {status['draft_patterns_count']}")
    if status['draft_patterns']:
        print(f"    -> {', '.join(status['draft_patterns'])}")
    return 0

def cmd_backfill(a) -> int:
    """Carica i checkpoint reali in PerfRecord ed esegue analisi."""
    cp_dir = paths.resolve("memory_cp")
    if not cp_dir.exists():
        print("Cartella checkpoints non trovata.", file=sys.stderr)
        return 1
        
    import re
    from datetime import timezone, timedelta
    tz = timezone(timedelta(hours=2))
    
    count = 0
    # Ordiniamo i checkpoint per nome file per processarli in ordine cronologico
    for cp_file in sorted(cp_dir.glob("CP-*.md")):
        content = cp_file.read_text(encoding="utf-8", errors="replace")
        from empire.memory import parse as memory_parse
        try:
            atom = memory_parse(content)
        except Exception:
            continue
            
        if not atom or not atom.id:
            continue
            
        date_str = atom.ts[:10]
        m = re.search(r"(\d{4})-?(\d{2})-?(\d{2})", cp_file.name)
        if m:
            date_str = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
            
        try:
            if atom.ts.startswith("1970"):
                raise ValueError("1970 fallback timestamp detected")
            ended = datetime.fromisoformat(atom.ts)
        except Exception:
            ended = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=18, tzinfo=tz)
        started = ended - timedelta(hours=2)
        
        body_lower = atom.body.lower()
        result = "success"
        if "parziale" in body_lower or "failed" in body_lower or "⚠️" in body_lower:
            result = "partial"
            
        agent = atom.actor or "Gael"
        if "gael" in body_lower:
            agent = "Gael"
        elif "claude" in body_lower:
            agent = "Claude"
        elif "max" in body_lower:
            agent = "Max"
            
        family = "default"
        if "empiredesk" in body_lower or "app.py" in body_lower:
            family = "build-python"
        elif "outreach" in body_lower or "linkedin" in body_lower or "email" in body_lower:
            family = "copy-landing"
            
        errori = 0
        if "bug" in body_lower or "errore" in body_lower:
            errori = body_lower.count("bug") + body_lower.count("errore")
            
        perf = PerfRecord(
            id=atom.id.replace("CP-", "PERF-"),
            agent=agent,
            task=atom.task or atom.id,
            workflow=atom.workflow or "WF-MASTER",
            family=family,
            result=result,
            started=started,
            ended=ended,
            ttd_h=2.0,
            debug={
                "errori": errori,
                "retry": 0,
                "escalation": 0,
                "fix_applicati": []
            },
            output_ref=[],
            verification={
                "verificatore": "manual",
                "first_pass": result == "success",
                "revisions": 0 if result == "success" else 1,
                "post_consegna": False,
                "regression": False,
                "dods_total": 5,
                "dods_verified": 5 if result == "success" else 4,
            },
            scorecard={},
            feedback_ids=[]
        )
        
        # Scrive in telemetria e memoria centrale
        capture_run(perf)
        count += 1
        
    print(f"Backfill completato. Importati {count} checkpoint storici come PerfRecords.")
    
    # Esegue analyze su tutti i record importati
    class DummyArgs:
        perf = None
        all_pending = True
    cmd_analyze(DummyArgs())
    return 0

def register(sub) -> None:
    p = sub.add_parser("inspect", help="Ispettorato & Performance Loop (GEM-03)")
    ms = p.add_subparsers(dest="inspectcmd", required=True)
    
    # capture
    q = ms.add_parser("capture", help="T1 - Raccoglie la telemetria di una run")
    q.add_argument("--agent", required=True)
    q.add_argument("--task", required=True)
    q.add_argument("--wf", required=True)
    q.add_argument("--family", required=True)
    q.add_argument("--result", required=True, choices=["success", "partial", "failed"])
    q.add_argument("--started", required=True, help="ISO format started time")
    q.add_argument("--ended", required=True, help="ISO format ended time")
    q.add_argument("--errori", type=int, default=0)
    q.add_argument("--retry", type=int, default=0)
    q.add_argument("--escalation", type=int, default=0)
    q.add_argument("--fix-applicati", nargs="*", default=[])
    q.add_argument("--output-ref", nargs="*", default=[])
    q.add_argument("--verificatore", default="manual")
    q.add_argument("--first-pass", action="store_true", default=True)
    q.add_argument("--revisions", type=int, default=0)
    q.add_argument("--post-consegna", action="store_true", default=False)
    q.add_argument("--regression", action="store_true", default=False)
    q.add_argument("--dods-total", type=int, default=0)
    q.add_argument("--dods-verified", type=int, default=0)
    q.set_defaults(fn=cmd_capture)
    
    # analyze
    q = ms.add_parser("analyze", help="T2 - Esegue l'analisi delle performance")
    q.add_argument("--perf", help="ID della performance specifica")
    q.add_argument("--all-pending", action="store_true")
    q.set_defaults(fn=cmd_analyze)
    
    # dispatch
    q = ms.add_parser("dispatch", help="T4 - Emette i feedback e le proposte")
    q.add_argument("--dry-run", action="store_true")
    q.set_defaults(fn=cmd_dispatch)
    
    # confirm
    q = ms.add_parser("confirm", help="T5 - Verifica e chiude i feedback (confirmed/recurred)")
    q.add_argument("--family", required=True)
    q.add_argument("--agent", required=True)
    q.set_defaults(fn=cmd_confirm)
    
    # report
    q = ms.add_parser("report", help="Genera report aggregati")
    q.add_argument("--daily", action="store_true")
    q.add_argument("--date", help="Data per il report daily (YYYY-MM-DD)")
    q.set_defaults(fn=cmd_report)
    
    # status
    q = ms.add_parser("status", help="Stato attuale dell'organo di ispezione")
    q.set_defaults(fn=cmd_status)
    
    # backfill
    q = ms.add_parser("backfill", help="Backfill storico dei checkpoint reali")
    q.set_defaults(fn=cmd_backfill)
