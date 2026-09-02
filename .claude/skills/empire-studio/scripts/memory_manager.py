#!/usr/bin/env python3
"""
Empire Studio - Memory Manager (Windows-safe, multi-category)

Gestisce l'ecosistema di memoria reale dell'ecosistema Empire Studio.
A differenza della versione precedente (che generava nomi file con ( ) : +
non estraibili su Windows -> errore 0x80070057), QUI ogni nome file e'
sanitizzato e limitato in lunghezza.

Categorie supportate (cartelle reali sotto memory/):
  checkpoints decisions sessions plans architectures bugs errors updates
  workflow-state knowledge-state agent-state verification-logs
  strategy-applications strategy-versions projects-state repo-analysis

Uso tipico:
  python memory_manager.py --checkpoint "ingest youtube completato" --phase 1
  python memory_manager.py --decision "Vision via Claude" --context "no API" --rationale "Claude legge i PNG"
  python memory_manager.py --record bugs --title "ffmpeg timeout" --body "..."
  python memory_manager.py --session "run-youtube-001" --body "log della run"
  python memory_manager.py --plan 2 --body "PLAN-v2 contenuto"
  python memory_manager.py --index         # ricostruisce MEMORY-INDEX.md
  python memory_manager.py --status        # stato sintetico

Tutto append-only + INDEX vivo. Nessuna dipendenza esterna (stdlib only).
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

# memory/ e' la cartella sorella di scripts/ (root = empire-studio/)
ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / "memory"

CATEGORIES = [
    "checkpoints", "decisions", "sessions", "plans", "architectures",
    "bugs", "errors", "updates", "workflow-state", "knowledge-state",
    "agent-state", "verification-logs", "strategy-applications",
    "strategy-versions", "projects-state", "repo-analysis",
]

# Prefisso codice per categoria (per i contatori XXX)
PREFIX = {
    "checkpoints": "CP", "decisions": "DEC", "sessions": "SES",
    "architectures": "ARCH", "bugs": "BUG", "errors": "ERR",
    "updates": "UPD", "verification-logs": "VLOG",
    "strategy-applications": "SAPP", "projects-state": "PRJ",
    "repo-analysis": "REPO",
}

_WINDOWS_BAD = r'[<>:"/\\|?*+()\[\]]'  # caratteri vietati / problematici su Windows


def now_iso():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")


def now_human():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def slug(text, maxlen=48):
    """Crea uno slug Windows-safe: niente ( ) : + ? e simili, niente spazi,
    minuscolo, lunghezza limitata. Questa e' la fix dell'errore 0x80070057."""
    text = (text or "").strip().lower()
    text = re.sub(_WINDOWS_BAD, "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    if len(text) > maxlen:
        text = text[:maxlen].rstrip("-")
    return text or "entry"


def ensure_dirs():
    for c in CATEGORIES:
        (MEM / c).mkdir(parents=True, exist_ok=True)


def next_number(category):
    folder = MEM / category
    folder.mkdir(parents=True, exist_ok=True)
    nums = []
    for f in folder.glob("*.md"):
        m = re.match(r"[A-Z]+-(\d{3,})", f.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 0


def write_entry(category, title, body, extra_header=None):
    """Scrive un file di memoria con nome Windows-safe e aggiorna l'INDEX."""
    ensure_dirs()
    prefix = PREFIX.get(category)
    s = slug(title)
    if prefix:
        n = next_number(category)
        fname = f"{prefix}-{n:03d}-{s}-{now_iso()}.md"
    else:
        fname = f"{s}-{now_iso()}.md"
    # safety net finale sul nome file
    fname = re.sub(_WINDOWS_BAD, "", fname)
    path = MEM / category / fname

    header = [f"# {title}", ""]
    header.append(f"- **Category:** {category}")
    header.append(f"- **Timestamp:** {now_human()}")
    if extra_header:
        for k, v in extra_header.items():
            if v:
                header.append(f"- **{k}:** {v}")
    header.append("")
    content = "\n".join(header) + (body or "").strip() + "\n"
    path.write_text(content, encoding="utf-8")
    append_index(category, fname, title)
    print(f"[memory] {category}/{fname}")
    return path


def append_index(category, fname, title):
    idx = MEM / "MEMORY-INDEX.md"
    if not idx.exists():
        rebuild_index()
        return
    line = f"- `{now_human()}` **[{category}]** {title} -> `{category}/{fname}`\n"
    with idx.open("a", encoding="utf-8") as f:
        f.write(line)


def rebuild_index():
    ensure_dirs()
    lines = [
        "# Empire Studio - MEMORY INDEX (living)",
        "",
        f"_Ultimo rebuild: {now_human()}_",
        "",
        "Fonte di verita' viva dell'ecosistema di memoria. Aggiornato dopo ogni azione.",
        "Due livelli: short-term (sessions/) + long-term (questo indice + categorie).",
        "",
        "## Conteggio per categoria",
        "",
    ]
    for c in CATEGORIES:
        cnt = len(list((MEM / c).glob("*.md")))
        lines.append(f"- **{c}**: {cnt}")
    lines += ["", "## Voci (cronologico)", ""]
    entries = []
    for c in CATEGORIES:
        for f in (MEM / c).glob("*.md"):
            entries.append((f.stat().st_mtime, c, f.name))
    for _, c, name in sorted(entries):
        lines.append(f"- **[{c}]** `{name}`")
    (MEM / "MEMORY-INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[memory] MEMORY-INDEX.md ricostruito ({len(entries)} voci)")


def status():
    ensure_dirs()
    total = 0
    print("Empire Studio memory status:")
    for c in CATEGORIES:
        cnt = len(list((MEM / c).glob("*.md")))
        total += cnt
        flag = "" if cnt else "  (vuota)"
        print(f"  {c:22s} {cnt}{flag}")
    print(f"  {'TOTALE':22s} {total}")


def main():
    p = argparse.ArgumentParser(description="Empire Studio Memory Manager (Windows-safe)")
    p.add_argument("--checkpoint", help="crea un CP con questa descrizione")
    p.add_argument("--phase", help="numero fase (per CP)")
    p.add_argument("--decision", help="titolo di una decisione (ADR)")
    p.add_argument("--context", help="contesto della decisione")
    p.add_argument("--rationale", help="razionale della decisione")
    p.add_argument("--alternatives", help="alternative considerate")
    p.add_argument("--session", help="id/descrizione sessione (SES)")
    p.add_argument("--plan", help="numero versione PLAN-vN")
    p.add_argument("--record", help="categoria generica (bugs|errors|updates|...)")
    p.add_argument("--title", help="titolo per --record/--session/--plan")
    p.add_argument("--body", default="", help="corpo testuale del file")
    p.add_argument("--trace", help="riferimento di tracciabilita' (P12)")
    p.add_argument("--index", action="store_true", help="ricostruisci INDEX")
    p.add_argument("--status", action="store_true", help="stato sintetico")
    args = p.parse_args()

    if args.index:
        rebuild_index(); return
    if args.status:
        status(); return

    if args.checkpoint:
        write_entry("checkpoints", args.checkpoint, args.body,
                    {"Phase": args.phase, "Trace": args.trace})
    elif args.decision:
        body = ""
        if args.context:      body += f"## Contesto\n{args.context}\n\n"
        if args.alternatives: body += f"## Alternative\n{args.alternatives}\n\n"
        if args.rationale:    body += f"## Decisione & Razionale\n{args.rationale}\n\n"
        body += args.body
        write_entry("decisions", args.decision, body, {"Trace": args.trace})
    elif args.session:
        write_entry("sessions", args.session, args.body, {"Trace": args.trace})
    elif args.plan:
        title = args.title or f"PLAN-v{args.plan}"
        path = MEM / "plans" / f"PLAN-v{slug(args.plan,6)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {title}\n\n_{now_human()}_\n\n{args.body}\n", encoding="utf-8")
        append_index("plans", path.name, title)
        print(f"[memory] plans/{path.name}")
    elif args.record:
        if args.record not in CATEGORIES:
            print(f"Categoria sconosciuta: {args.record}\nValide: {', '.join(CATEGORIES)}")
            sys.exit(1)
        write_entry(args.record, args.title or args.record, args.body, {"Trace": args.trace})
    else:
        status()
        print("\nNessuna azione. Usa --checkpoint/--decision/--record/--session/--plan/--index/--status")


if __name__ == "__main__":
    main()
