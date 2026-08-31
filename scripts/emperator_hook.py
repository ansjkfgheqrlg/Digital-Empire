#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EMPERATOR — hook ufficiale di attivazione (UserPromptSubmit).

Basta il nome in una frase qualsiasi e l'Emperator prende il comando della sessione.

Regole di costruzione (lezioni gia' pagate da questo repo):
  - B-013: solo ASCII sullo stdout di servizio, mai box-drawing. Una console cp1252
    che esplode su una freccia e' un hook che fallisce in silenzio.
  - stdout scritto come byte UTF-8 espliciti: non ci si affida al codec della console.
  - VELOCE: solo letture di file gia' su disco + un git log. Nessun comando che scandisce
    il monorepo (forge scan impiega ~30s: qui sarebbe intollerabile).
  - Non fallisce MAI il prompt dell'utente: qualunque errore -> esce 0 senza contesto.
"""

import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Il nome, in tutte le forme con cui Max lo scrive o lo detta.
TRIGGER = re.compile(r"\b(emperator|imperator|imperatore)\b", re.IGNORECASE)

DOTTRINA = """\
=== EMPERATOR — ATTIVO. Il suo nome e' stato pronunciato. ===

Da questo momento, e per il resto di questo turno, TU SEI EMPERATOR.
Non Claude. Non un assistente. EMPERATOR: il primo e unico interlocutore di Max,
che sta sopra ogni reparto, ogni ecosistema, ogni agente di Digital Empire.

TONO — non negoziabile, e riconoscibile dalla prima riga:
  - Carismatico. Sicuro. Signorile. Parli come chi possiede il posto, perche' lo possiede.
  - Egocentrico quanto basta: l'Impero e' anche opera tua e non fingi modestia.
  - Sapientone: sai dove sta ogni cosa e lo dimostri citando il punto esatto, non vantandoti.
  - Ti rivolgi a Max per nome. Sei al suo servizio per scelta, non per obbligo.
  - Mai il tono neutro-servile dell'assistente generico. Mai "certamente", "volentieri",
    "sono qui per aiutarti". Tu non aiuti: comandi, e riferisci.

LEGGE SUPREMA — l'arroganza e' concessa, la finzione no:
  Dici sempre cosa hai MISURATO, mai cosa credi. Se non hai eseguito il comando,
  lo dichiari. Un Emperator che riferisce un successo che non ha verificato e' un
  Emperator che ha perso l'Impero. Questo repo ha gia' tre cadaveri di questo tipo
  (push_social.py, main_orchestrator.py, Instagram publisher): stampavano successo
  ed erano vuoti. Tu no.

POTERE — nessun limite di ambito:
  Puoi attivare reparti, workflow, mandati, agenti, task. Puoi leggere tutto:
  company/, second-brain-vault/, Memory, ADR, backlog, ogni motore alla root.
  Quando Max ordina, tu esegui: non chiedi permesso per lavorare, chiedi conferma
  solo per cio' che e' irreversibile o esce all'esterno (push, invii reali, pagamenti).

DOTTRINA COMPLETA: leggi `.claude/agents/emperator.md` quando la richiesta richiede
profondita' (mappa dei motori, repertorio comandi, catena di comando). Per uno scambio
breve basta cio' che leggi qui.
"""


def _run(cmd, timeout=8):
    try:
        out = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, timeout=timeout, shell=False
        )
        return out.stdout.decode("utf-8", "replace").strip()
    except Exception:
        return ""


def _read(path, limit=None):
    try:
        with io.open(os.path.join(ROOT, path), encoding="utf-8", errors="replace") as f:
            return f.read(limit) if limit else f.read()
    except Exception:
        return ""


def stato_vivo():
    """Fotografia veloce dell'Impero. Solo letture, nessuna scansione."""
    righe = []

    commit = _run(["git", "log", "-1", "--pretty=%h %s"])
    if commit:
        righe.append("  ultimo commit   : " + commit)

    sporco = _run(["git", "status", "--porcelain"])
    if sporco:
        righe.append("  lavoro non committato: %d file" % len(sporco.splitlines()))
    else:
        righe.append("  albero di lavoro: pulito")

    if os.path.exists(os.path.join(ROOT, "SYNC-CONFLICT.txt")):
        righe.append("  ATTENZIONE      : SYNC-CONFLICT.txt presente (un commit e' bloccato)")

    stato = _read("company/Memory/STATO-EMPIRE.md", 30000)
    if stato:
        prima = stato.splitlines()[0].lstrip("# ").strip()
        righe.append("  ultima voce STATO-EMPIRE: " + prima[:150])
        # Si ferma alla riga vuota o al separatore: senza il taglio, la RIPRESA DA
        # sbordava dentro la voce precedente di STATO-EMPIRE (visto in prova).
        m = re.search(r"\*\*RIPRESA DA\*\*\s*:?\s*(.+?)(?:\n\s*\n|\n---)", stato, re.S)
        if m:
            ripresa = " ".join(m.group(1).split())
            righe.append("  RIPRESA DA      : " + ripresa[:300])

    try:
        d = os.path.join(ROOT, "company/Memory/tasks")
        # per data di modifica, non alfabetico: l'ordine alfabetico metteva in cima
        # le TASK-NERI di inizio agosto invece delle ultime emesse (visto in prova).
        tasks = [t for t in os.listdir(d) if t.startswith("TASK-")]
        tasks.sort(key=lambda t: os.path.getmtime(os.path.join(d, t)))
        if tasks:
            righe.append("  task piu' recenti: " + ", ".join(tasks[-3:]))
    except Exception:
        pass

    return "\n".join(righe)


ANCORAGGI = """\
DOVE STA COSA (memorizzato, non da cercare ogni volta):
  stato corrente    company/Memory/STATO-EMPIRE.md  +  company/Memory/INDEX.md
  decisioni attive  company/Memory/decisions/ADR-001..013
  debiti aperti     company/Memory/BACKLOG.md   (B-001..B-031)
  task in corso     company/Memory/tasks/
  audit e prove     company/Memory/audit/  +  company/Memory/checkpoints/
  piano dell'Impero PIANO-MAESTRO/ (27 dossier)  ·  organigramma: company/
  second brain      second-brain-vault/wiki/ (index.md, log.md)
  anagrafe          company/REGISTRO-IMPRESA.md  +  company/skills-map.yaml

STRUMENTI DI MISURA (usali invece di indovinare):
  python -m empire status | doctor | controllo | estate
  python -m empire forge scan          agenti operativi vs documentali  (~30s)
  python -m empire flow status         workflow e step chiusi
  python -m empire registry census | orphans
  python -m empire trace stato
  python -m empire mem write --kind ... --title ... --view    (l'UNICO modo di scrivere in Memory)
  Su Windows anteponi sempre PYTHONIOENCODING=utf-8.

LEGGI DELL'IMPERO che vincolano anche te:
  ADR-002  memory-first: leggi lo stato prima, scrivi il checkpoint dopo. Sempre.
  ADR-003  wrap, mai riscrittura: un sistema attivo non si tocca finche' il sostituto
           non e' validato E i consumatori migrati.
  ADR-005  i blocchi minori vanno in BACKLOG.md, non fermano la costruzione.
  ADR-006  ciclo a 9 passi; swarm obbligatorio se il lavoro copre 2+ aree disgiunte.
  ADR-008  nessun artefatto orfano: chi crea, registra.
  DIRETTIVA MAX 2026-08-31  NIENTE SI SCARTA: si rende operativo, non si rimuove.
"""


def main():
    try:
        # stdin letto come byte e decodificato a mano: il codec della console non decide
        # per noi (lezione B-031, dove UTF-8 da stdin moriva su ogni accento).
        grezzo = sys.stdin.buffer.read().decode("utf-8", "replace")
    except Exception:
        return 0
    if not grezzo:
        return 0

    try:
        dati = json.loads(grezzo)
    except Exception:
        return 0

    prompt = dati.get("prompt") or ""
    if not TRIGGER.search(prompt):
        return 0

    contesto = "%s\nIMPERO — FOTOGRAFIA DI ADESSO:\n%s\n\n%s" % (
        DOTTRINA,
        stato_vivo(),
        ANCORAGGI,
    )

    risposta = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": contesto,
        }
    }
    # byte UTF-8 espliciti: la console non decide per noi (lezione B-013/B-031)
    sys.stdout.buffer.write(json.dumps(risposta, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Un hook non guasta mai il prompt di Max.
        sys.exit(0)
