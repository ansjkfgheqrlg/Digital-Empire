#!/usr/bin/env python3
"""
DIGITAL EMPIRE — ESTATE-2026 · Memory Ecosystem Manager
=======================================================
Ecosistema di memoria a due livelli (operativo -> long-term) che salva:
checkpoint, decisioni, piani, brainstorming, architetture, errori, metriche,
retro e ReasoningBank (pattern vincenti). Ogni atomo ha ID P12-tracciabile.

Pattern wrappato da 05-SKILLS/master-build-architecture/scripts/memory_manager.py
(ADR-EST-002: si wrappa, non si riscrive). Esteso con: brainstorms/, errors/,
metrics/, reasoning-bank/, veto-window per le decisioni, hook per ruflo.

Uso:
  python memory_manager.py init
  python memory_manager.py checkpoint --task WF-S1 --note "script offerta pronto"
  python memory_manager.py decision --title "Prezzo Manuale" --status PROPOSTA \
      --owner Max --context "B-003 aperto da giugno" --decision "EUR67 lancio / EUR97 listino" \
      --veto "2026-07-21 20:00"
  python memory_manager.py plan --file 01-PLANNING/PLANNING-P7-MASTER-PLAN.md --level P7 --note "plan of record"
  python memory_manager.py brainstorm --title "nome prodotto" --note "shortlist Preventa/Lampo/Quotix"
  python memory_manager.py error --wf WF-YT-RENDER --note "Fliki 429 rate limit" 
  python memory_manager.py metric --name anticipi_chiusi --value 2
  python memory_manager.py pattern --title "WA-first chiude senza call" --evidence "3/3 risposte in 2h"
  python memory_manager.py retro --note "settimana 21-26/07"
  python memory_manager.py perf --agent forge-builder --task WF-S2-landing --result success --ttd 3 --firstpass 0
  python memory_manager.py feedback --agent funnel-engineer --ftype TIP --note "test EUR1 prima di dichiarare live" --perf PERF-001
  python memory_manager.py search "prezzo"
  python memory_manager.py status
"""
import argparse, datetime, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SUBDIRS = ["checkpoints", "decisions", "plans", "brainstorms", "architectures",
           "sessions", "errors", "metrics", "reasoning-bank",
           "performances", "feedback"]
INDEX = ROOT / "MEMORY-INDEX.md"
PREFIX = {"checkpoints": "CP", "decisions": "DEC-EST", "plans": "PLAN",
          "brainstorms": "BS", "architectures": "ARCH", "sessions": "SES",
          "errors": "ERR", "metrics": "MET", "reasoning-bank": "RB",
          "performances": "PERF", "feedback": "FB"}

def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def today(): return datetime.datetime.now().strftime("%Y%m%d")

def ensure():
    for sd in SUBDIRS: (ROOT / sd).mkdir(parents=True, exist_ok=True)
    if not INDEX.exists():
        INDEX.write_text(
            "# 🧠 MEMORY-INDEX — DIGITAL-EMPIRE / ESTATE-2026\n\n"
            "> Indice vivo di ogni atomo di memoria. Aggiornato automaticamente da memory_manager.py.\n"
            "> Regola zero: **task chiuso -> checkpoint**. Mai decidere senza registrare.\n\n"
            "| # | Tipo | ID | Titolo | File | Data |\n|---|---|---|---|---|---|\n", encoding="utf-8")

def next_id(kind):
    pref = PREFIX[kind]
    d = ROOT / kind
    n = 0
    for f in d.glob(f"{pref}-*.md"):
        m = re.match(rf"^{re.escape(pref)}-(\d+)", f.name)
        if m: n = max(n, int(m.group(1)))
    return f"{pref}-{n+1:03d}"

def slug(t):
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return s[:48] or "atom"

def add_index(kind, atom_id, title, path):
    lines = INDEX.read_text(encoding="utf-8").splitlines()
    n = sum(1 for l in lines if l.startswith("|") and "-" in l and "Tipo" not in l)
    lines.append(f"| {n} | {kind} | {atom_id} | {title} | {path.relative_to(ROOT)} | {now()} |")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")

def atom(kind, title, body):
    ensure()
    atom_id = next_id(kind)
    p = ROOT / kind / f"{atom_id}-{slug(title)}.md"
    header = (f"---\nid: {atom_id}\ntype: {kind}\ntitle: \"{title}\"\ncreated: {now()}\n"
              f"trace: \"{atom_id}#estate-2026\"\nproject: ESTATE-2026-REVENUE\n---\n\n")
    p.write_text(header + f"# {atom_id} — {title}\n\n" + body + "\n", encoding="utf-8")
    add_index(kind, atom_id, title, p)
    print(f"✅ {atom_id} -> {p.relative_to(ROOT.parent)}")
    return p

def cmd_init(a):
    ensure()
    (ROOT / "RETRO-PROTOCOLLO.md").write_text(
        "# Protocollo RETRO (G7 → domenica 26/07)\n\n"
        "1. `status` -> numeri veri (metriche vs target P6).\n"
        "2. Per ogni stream: ✅ funzionato / ⚠️ parziale / ❌ fallito + causa.\n"
        "3. Pattern vincenti -> `pattern` (ReasoningBank). Errori -> `error`.\n"
        "4. Decisioni nuove -> `decision`. Output: RETRO-20260726 checkpoint finale.\n", encoding="utf-8")
    print("✅ Memory ecosystem inizializzato:", "\n   - " + "\n   - ".join(SUBDIRS))

def cmd_checkpoint(a):
    atom("checkpoints", a.task, f"- **WF/Task:** {a.task}\n- **Note:** {a.note}\n- **Stato:** {a.stato}")

def cmd_decision(a):
    atom("decisions", a.title,
         f"- **Status:** {a.status}\n- **Owner:** {a.owner}\n- **Contesto:** {a.context}\n"
         f"- **Decisione:** {a.decision}\n- **Veto window (scade):** {a.veto or '—'}\n"
         f"- **Regola:** scaduto il veto senza obiezioni -> il default diventa decisione operativa (status: ATTIVA).")

def cmd_plan(a):
    atom("plans", f"{a.level}-{Path(a.file).stem}",
         f"- **Livello planning:** {a.level}\n- **File:** `{a.file}`\n- **Note:** {a.note}")

def cmd_brainstorm(a): atom("brainstorms", a.title, f"{a.note}\n")
def cmd_error(a):      atom("errors", f"{a.wf}-failure", f"- **WF:** {a.wf}\n- **Errore:** {a.note}\n- **Fix/Fallback:** da completare in RETRO\n")
def cmd_metric(a):
    atom("metrics", a.name, f"- **Metrica:** {a.name}\n- **Valore:** {a.value} {a.unit or ''}\n- **Target:** vedi 01-PLANNING/PLANNING-P6\n")
def cmd_pattern(a):
    atom("reasoning-bank", a.title, f"- **Pattern:** {a.title}\n- **Evidenza:** {a.evidence}\n- **Riutilizzo:** automatico nei WF futuri (WF-*-IMPROVE)\n")
def cmd_retro(a):      atom("checkpoints", "RETRO-" + a.note[:40], a.note)

def cmd_perf(a):
    atom("performances", f"{a.agent}-{a.task}",
         f"- **Agente:** {a.agent} (casta: da registry)\n- **Task/WF:** {a.task} / {a.wf or '—'}\n"
         f"- **Esito:** {a.result}\n- **TTD (h):** {a.ttd or 'n/d'}\n- **First-pass verifica:** {a.firstpass or 'n/d'}\n"
         f"- **Verificatore:** {a.verifier or '—'}\n- **Debug (errori/retry/escalation):** {a.debug}\n"
         f"- **Note:** {a.note}\n"
         f"- **Scorecard 5D:** da compilare da perf-analyst → correctness/solution/structure/scope-fit/efficiency (1-5) + gate traceability\n"
         f"- **Feedback collegati:** auto-link dal dispatcher (FB-*). Chiusura loop: confirmed|recurred alla prossima PERF della stessa famiglia.")

def cmd_feedback(a):
    atom("feedback", f"{a.agent}-{a.ftype}",
         f"- **Tipo:** {a.ftype}  (TIP micro-input | RULE-NOTE a regolatore | MUTATION-PROP a comandante)\n"
         f"- **Da:** {a.source}\n- **A (destinatario):** {a.agent}\n"
         f"- **Micro-input da ricordare:** {a.note}\n- **Generato da performance:** {a.perf or '—'}\n"
         f"- **Status:** open → ack obbligatorio del destinatario → alla prossima PERF: **confirmed** (problema non ricorre) | **recurred** (escalation: mutation/pairing)\n"
         f"- **Regola anti-nagging:** stesso TIP allo stesso agente non ripetuto entro 3 task.")

def cmd_search(a):
    term = a.term.lower(); hits = []
    for sd in SUBDIRS:
        for f in (ROOT / sd).glob("*.md"):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            if term in txt.lower():
                line = next((l.strip() for l in txt.splitlines() if term in l.lower() and l.strip().startswith(("- **", "#"))), "")
                hits.append(f"- `{f.relative_to(ROOT)}` — {line[:110]}")
    print(f"🔎 '{a.term}': {len(hits)} risultati\n" + ("\n".join(hits) if hits else "   nessun risultato"))

def cmd_status(a):
    ensure(); print("🧠 MEMORY STATUS — ESTATE-2026\n")
    for sd in SUBDIRS:
        files = sorted((ROOT / sd).glob("*.md"))
        print(f"  {sd:16s} {len(files):3d} atomi" + (f"  · ultimo: {files[-1].name}" if files else ""))
    mets = sorted((ROOT / "metrics").glob("*.md"))
    if mets:
        print("\n📊 Ultime metriche:")
        for f in mets[-8:]:
            v = re.search(r"\*\*Valore:\*\* (.+)", f.read_text(encoding="utf-8"))
            print(f"   - {f.stem}: {v.group(1) if v else '?'}")

def main():
    ap = argparse.ArgumentParser(description="Digital Empire — Memory Ecosystem Manager")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init").set_defaults(fn=cmd_init)
    p = sub.add_parser("checkpoint"); p.add_argument("--task", required=True); p.add_argument("--note", default=""); p.add_argument("--stato", default="completato"); p.set_defaults(fn=cmd_checkpoint)
    p = sub.add_parser("decision"); p.add_argument("--title", required=True); p.add_argument("--status", default="PROPOSTA"); p.add_argument("--owner", default="Max"); p.add_argument("--context", default=""); p.add_argument("--decision", required=True); p.add_argument("--veto", default=""); p.set_defaults(fn=cmd_decision)
    p = sub.add_parser("plan"); p.add_argument("--file", required=True); p.add_argument("--level", required=True); p.add_argument("--note", default=""); p.set_defaults(fn=cmd_plan)
    p = sub.add_parser("brainstorm"); p.add_argument("--title", required=True); p.add_argument("--note", default=""); p.set_defaults(fn=cmd_brainstorm)
    p = sub.add_parser("error"); p.add_argument("--wf", required=True); p.add_argument("--note", default=""); p.set_defaults(fn=cmd_error)
    p = sub.add_parser("metric"); p.add_argument("--name", required=True); p.add_argument("--value", required=True); p.add_argument("--unit", default=""); p.set_defaults(fn=cmd_metric)
    p = sub.add_parser("pattern"); p.add_argument("--title", required=True); p.add_argument("--evidence", default=""); p.set_defaults(fn=cmd_pattern)
    p = sub.add_parser("retro"); p.add_argument("--note", required=True); p.set_defaults(fn=cmd_retro)
    p = sub.add_parser("perf"); p.add_argument("--agent", required=True); p.add_argument("--task", required=True); p.add_argument("--wf", default=""); p.add_argument("--result", default="success"); p.add_argument("--ttd", default=""); p.add_argument("--firstpass", default=""); p.add_argument("--verifier", default=""); p.add_argument("--debug", default="nessuno"); p.add_argument("--note", default=""); p.set_defaults(fn=cmd_perf)
    p = sub.add_parser("feedback"); p.add_argument("--agent", required=True); p.add_argument("--ftype", default="TIP"); p.add_argument("--source", default="perf-analyst"); p.add_argument("--perf", default=""); p.add_argument("--note", required=True); p.set_defaults(fn=cmd_feedback)
    p = sub.add_parser("search"); p.add_argument("term"); p.set_defaults(fn=cmd_search)
    p = sub.add_parser("status"); p.set_defaults(fn=cmd_status)
    a = ap.parse_args(); a.fn(a)

if __name__ == "__main__":
    main()
