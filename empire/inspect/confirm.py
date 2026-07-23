"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from empire.memory import all_atoms, write as memory_write, read as memory_read
from .record import atom_to_feedback, atom_to_perf, feedback_to_atom, FeedbackRecord
from .report import write_escalation_report

TZ = timezone(timedelta(hours=2))


def process_t5_confirm(family: str, agent: str) -> list[FeedbackRecord]:
    """T5 - Chiusura del loop: confirmed o recurred alla performance successiva."""
    pending_feedbacks = []
    for atom in all_atoms(kind="feedback"):
        if atom.actor == agent and atom.status in ("open", "acked", "proposto"):
            fb = atom_to_feedback(atom)
            perf_atom = memory_read(fb.on_perf)
            if perf_atom and perf_atom.extra.get("family") == family:
                pending_feedbacks.append(fb)
                
    if not pending_feedbacks:
        return []
        
    updated_feedbacks = []
    for fb in pending_feedbacks:
        successive_perfs = []
        for atom in all_atoms(kind="perf"):
            if atom.actor == agent and atom.extra.get("family") == family:
                perf = atom_to_perf(atom)
                if perf.started > fb.opened:
                    successive_perfs.append(perf)
                    
        if not successive_perfs:
            continue
            
        successive_perfs.sort(key=lambda x: x.started)
        next_perf = successive_perfs[0]
        
        if next_perf.result == "success":
            fb.status = "confirmed"
            fb.closed = datetime.now(TZ)
            atom = feedback_to_atom(fb)
            memory_write(atom)
            
            update_pattern_status(family, "confirmed")
            updated_feedbacks.append(fb)
        else:
            fb.status = "recurred"
            fb.closed = datetime.now(TZ)
            atom = feedback_to_atom(fb)
            memory_write(atom)
            
            write_escalation_report(fb, next_perf)
            updated_feedbacks.append(fb)
            
    return updated_feedbacks

def update_pattern_status(family: str, status: str) -> None:
    for atom in all_atoms(kind="pattern"):
        if atom.extra.get("family") == family and atom.status != status:
            atom.status = status
            memory_write(atom)
