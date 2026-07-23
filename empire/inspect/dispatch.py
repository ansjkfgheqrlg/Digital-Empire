"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from empire.memory import all_atoms, write as memory_write
from .record import FeedbackRecord, feedback_to_atom

TZ = timezone(timedelta(hours=2))


def should_dispatch_tip(agent: str, family: str) -> bool:
    """Verifica la regola anti-nagging: stesso TIP allo stesso agente non ripetere entro 3 task."""
    feedbacks = list(all_atoms(kind="feedback"))
    feedbacks.sort(key=lambda x: x.ts, reverse=True)
    
    agent_fbs = [x for x in feedbacks if x.actor == agent and x.extra.get("ftype") == "TIP"]
    
    for old_fb in agent_fbs[:3]:
        old_on_perf = old_fb.refs[0] if old_fb.refs else ""
        from empire.memory import read as memory_read
        perf_atom = memory_read(old_on_perf)
        if perf_atom and perf_atom.extra.get("family") == family:
            return False
            
    return True

def dispatch_feedback(perf_id: str, dry_run: bool = False) -> list[FeedbackRecord]:
    """T4 - Emette micro-input (TIP, RULE-NOTE, MUTATION-PROP) e applica la regola anti-nagging."""
    from empire.memory import read as memory_read
    perf_atom = memory_read(perf_id)
    if not perf_atom:
        return []
        
    from .record import atom_to_perf
    perf = atom_to_perf(perf_atom)
    agent = perf.agent
    family = perf.family
    
    dispatched = []
    
    # 1. Se la performance è fallita o parziale, emettiamo un TIP
    if perf.result in ("failed", "partial"):
        if should_dispatch_tip(agent, family):
            micro_input = f"[TIP] Per il task di famiglia {family}: verifica sempre l'ambiente ed evita errori noti."
            
            note_lower = str(perf.verification.get("note", "")).lower()
            debug_lower = str(perf.debug).lower()
            text_to_check = (note_lower + " " + debug_lower + " " + perf.task + " " + perf.family).lower()
            
            if "ambiente senza" in text_to_check or "runtime" in text_to_check:
                micro_input = "[TIP] Assicurati che i runtime Python/Node siano installati sul PC prima di lanciare la build."
            elif "pyinstaller" in text_to_check or "_meipass" in text_to_check:
                micro_input = "[TIP] Con PyInstaller >=6.0, ricorda che i datas finiscono in _internal/, gestisci DATA_DIR."
            elif "collisione" in text_to_check or "due owner" in text_to_check:
                micro_input = "[TIP] Prima di modificare file sensibili, esegui git pull e leggi STATO-EMPIRE.md."
            elif "diff vuoto" in text_to_check:
                micro_input = "[TIP] Controlla sempre git show --stat prima di dichiarare un task completato."
                
            fb = FeedbackRecord(
                id="",
                ftype="TIP",
                to=agent,
                micro_input=micro_input[:200],
                on_perf=perf.id,
                status="open",
                opened=datetime.now(TZ)
            )
            if not dry_run:
                atom = feedback_to_atom(fb)
                saved_atom = memory_write(atom)
                fb.id = saved_atom.id
            dispatched.append(fb)
            
    # 2. Se c'è una ricorrenza >= 3, emettiamo una MUTATION-PROP al comandante
    pattern_count = 0
    for atom in all_atoms(kind="pattern"):
        if atom.extra.get("family") == family:
            pattern_count = max(pattern_count, atom.extra.get("occurrences", 0))
            
    if pattern_count >= 3:
        fb = FeedbackRecord(
            id="",
            ftype="MUTATION-PROP",
            to="comandante-di-casta",
            micro_input=f"[MUTATION-PROP] Modificare il prompt dell'agente {agent} per integrare la protezione permanente per {family}.",
            on_perf=perf.id,
            status="open",
            opened=datetime.now(TZ)
        )
        if not dry_run:
            atom = feedback_to_atom(fb)
            saved_atom = memory_write(atom)
            fb.id = saved_atom.id
        dispatched.append(fb)
        
    return dispatched
