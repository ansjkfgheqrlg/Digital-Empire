"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

from pathlib import Path
from empire.memory import all_atoms
from empire import loader
from .record import PerfRecord
from .benchmarks import get_benchmark

def calculate_scorecard(perf: PerfRecord) -> dict:
    """Calcola la scorecard 5D deterministica e verifica la tracciabilità (Gate 3)."""
    # 1. Asse ① correctness/debug
    debug = perf.debug or {}
    errori = debug.get("errori", 0)
    retry = debug.get("retry", 0)
    escalation = debug.get("escalation", 0)
    penalty = errori + (retry * 0.5) + (escalation * 2.0)
    score_correctness = float(5.0 - min(4.0, penalty))
    
    # 2. Asse ② qualità soluzione
    verif = perf.verification or {}
    first_pass = verif.get("first_pass", True)
    revisions = verif.get("revisions", 0)
    post_consegna = verif.get("post_consegna", False)
    regression = verif.get("regression", False)
    
    if regression:
        score_solution = 1
    elif post_consegna:
        score_solution = 2
    elif revisions >= 2:
        score_solution = 3
    elif revisions == 1 or not first_pass:
        score_solution = 4
    else:
        score_solution = 5
        
    # 3. Asse ③ struttura output
    from empire.paths import repo_root
    
    if not perf.output_ref:
        score_structure = 5.0
    else:
        scores = []
        for path in perf.output_ref:
            p = Path(path)
            if not p.exists():
                scores.append(1.0)
            else:
                try:
                    p.resolve().relative_to(repo_root().resolve())
                    inside_repo = True
                except ValueError:
                    inside_repo = False
                
                fm = loader.load_frontmatter(p)
                prov = loader._provenance(p, fm)
                
                if inside_repo and prov.complete:
                    scores.append(5.0)
                else:
                    scores.append(3.0)
        score_structure = float(sum(scores) / len(scores))
        
    # 4. Asse ④ scope-fit
    dods_total = verif.get("dods_total", 0)
    dods_verified = verif.get("dods_verified", 0)
    if dods_total <= 0:
        score_scope = 5.0
    else:
        score_scope = float(1.0 + 4.0 * (min(dods_verified, dods_total) / dods_total))
        
    # 5. Asse ⑤ efficiency
    benchmark = get_benchmark(perf.family)
    ratio = perf.ttd_h / benchmark if benchmark > 0 else 1.0
    if ratio <= 0.8:
        score_efficiency = 5
    elif ratio <= 1.2:
        score_efficiency = 4
    elif ratio <= 2.0:
        score_efficiency = 3
    elif ratio <= 3.0:
        score_efficiency = 2
    else:
        score_efficiency = 1
        
    # Gate Traceability: checkpoint con lo stesso task ID in memoria centrale
    checkpoint_exists = False
    if perf.task:
        checkpoint_exists = any(
            atom.kind == "checkpoint" and atom.task == perf.task
            for atom in all_atoms(kind="checkpoint")
        )
        
    scorecard = {
        "correctness": score_correctness,
        "solution": score_solution,
        "structure": score_structure,
        "scope_fit": score_scope,
        "efficiency": score_efficiency,
        "traceability": checkpoint_exists
    }
    
    return scorecard
