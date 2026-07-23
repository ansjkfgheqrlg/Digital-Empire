"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from empire.memory import Atom, all_atoms, write as memory_write
from .record import PerfRecord

# Mappa dei pattern reali documentati nei checkpoints storici
KNOWN_PATTERN_RULES = [
    {
        "title": "build dichiarato senza runtime disponibile",
        "keywords": ["runtime", "installato", "ambiente sessione senza", "senza python/node", "stub", "winget"],
        "body": "Il build viene dichiarato completato o pianificato, ma l'ambiente di esecuzione manca dei runtime necessari (Python, Node.js, ecc.)."
    },
    {
        "title": "verificato in dev, rotto nel frozen",
        "keywords": ["pyinstaller", "_meipass", "frozen", "exe buildata", "spec", "datas", "compresso"],
        "body": "Il codice funziona correttamente in ambiente di sviluppo (dev) ma fallisce una volta congelato o compilato in un eseguibile (frozen) a causa di percorsi di ricerca differenti."
    },
    {
        "title": "due owner sullo stesso file",
        "keywords": ["collisione", "conflitto", "parallel", "conteso", "rebase", "due sessioni", "due owner"],
        "body": "Due agenti o membri del team modificano in parallelo lo stesso file senza coordinamento preventivo in STATO-EMPIRE.md, causando conflitti di merge."
    },
    {
        "title": "dichiarato fatto, diff vuoto",
        "keywords": ["diff vuoto", "messaggio di commit", "scollegato", "dichiarato", "non esiste", "discrepanze"],
        "body": "Il commit o la notifica di completamento dichiara la consegna di molteplici moduli o funzionalità, ma il diff reale contiene pochissime righe o modifiche non correlate."
    }
]

def synthesize_patterns(perf: PerfRecord) -> list[Atom]:
    """T3 - Pattern detection + contatore ricorrenze (ReasoningBank)."""
    debug = perf.debug or {}
    text_to_check = " ".join([
        perf.task,
        perf.workflow,
        perf.family,
        perf.result,
        str(debug.get("errori", 0)),
        " ".join(debug.get("fix_applicati", [])),
        perf.verification.get("note", ""),
    ]).lower()
    
    from empire.memory import read as memory_read
    original_atom = memory_read(perf.id) if perf.id else None
    if original_atom and original_atom.body:
        text_to_check += " " + original_atom.body.lower()
        
    synthesized = []
    
    for rule in KNOWN_PATTERN_RULES:
        if any(kw in text_to_check for kw in rule["keywords"]):
            # Cerca se esiste già un atomo pattern con questo titolo
            existing_pattern = None
            for atom in all_atoms(kind="pattern"):
                if atom.title == rule["title"]:
                    existing_pattern = atom
                    break
            
            if existing_pattern:
                extra = existing_pattern.extra or {}
                occurrences = extra.get("occurrences", 1) + 1
                extra["occurrences"] = occurrences
                extra["last_seen_perf"] = perf.id
                existing_pattern.extra = extra
                memory_write(existing_pattern)
                synthesized.append(existing_pattern)
            else:
                from empire.memory import now_iso
                new_pat = Atom(
                    kind="pattern",
                    title=rule["title"],
                    body=rule["body"],
                    status="proposed",  # DRAFT
                    ts=now_iso(),
                    extra={
                        "occurrences": 1,
                        "family": perf.family,
                        "last_seen_perf": perf.id
                    }
                )
                saved_pat = memory_write(new_pat)
                synthesized.append(saved_pat)
                
    return synthesized
