"""Tool per annotare, triare e pianificare failure mode di `content-forge`.

Usage:
    python3 scripts/log_failure.py --quick "descrizione breve"
        → crea un FM-NNN-slug.md nuovo in failure-modes-log/logged/

    python3 scripts/log_failure.py --triage
        → interattivo: per ogni FM in logged/, chiede severity/category/scope
          e lo sposta in triaged/

    python3 scripts/log_failure.py --plan-phase10
        → genera PHASE-10-CANDIDATES.md con raggruppamento per categoria + priorità

    python3 scripts/log_failure.py --index
        → rigenera INDEX.md con la lista master

    python3 scripts/log_failure.py --list [logged|triaged|resolved|all]
        → stampa lista compatta

Part of: content-forge / failure-modes-log
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# === Paths ===
REPO_ROOT = Path(__file__).parent.parent
LOG_DIR = REPO_ROOT / "failure-modes-log"
LOGGED_DIR = LOG_DIR / "logged"
TRIAGED_DIR = LOG_DIR / "triaged"
RESOLVED_DIR = LOG_DIR / "resolved"
TEMPLATE_PATH = LOG_DIR / "TEMPLATE.md"
INDEX_PATH = LOG_DIR / "INDEX.md"
PHASE10_PATH = LOG_DIR / "PHASE-10-CANDIDATES.md"


# === Helpers ===

def slugify(text: str, max_len: int = 40) -> str:
    """Slug kebab-case ASCII."""
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[\s_]+", "-", s)
    return s[:max_len].rstrip("-")


def next_fm_id() -> str:
    """Prossimo ID FM-NNN incrementale."""
    existing_ids = []
    for d in (LOGGED_DIR, TRIAGED_DIR, RESOLVED_DIR):
        if d.exists():
            for f in d.glob("FM-*.md"):
                m = re.match(r"FM-(\d+)-", f.name)
                if m:
                    existing_ids.append(int(m.group(1)))
    next_n = (max(existing_ids) + 1) if existing_ids else 1
    return f"FM-{next_n:03d}"


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Ritorna (frontmatter dict, body)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = m.group(2)
    if yaml:
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception:
            fm = {}
    else:
        # Fallback parse molto basic
        fm = {}
        for line in fm_text.split("\n"):
            if ":" in line and not line.strip().startswith("-"):
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
    return fm, body


def write_with_frontmatter(path: Path, fm: dict, body: str) -> None:
    """Scrive file con frontmatter aggiornato."""
    if yaml:
        fm_text = yaml.safe_dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    else:
        # Fallback manuale
        lines = []
        for k, v in fm.items():
            if isinstance(v, list):
                if not v:
                    lines.append(f"{k}: []")
                else:
                    lines.append(f"{k}:")
                    for item in v:
                        lines.append(f"  - {item}")
            elif v is None:
                lines.append(f"{k}: null")
            else:
                lines.append(f"{k}: {v}")
        fm_text = "\n".join(lines) + "\n"
    path.write_text(f"---\n{fm_text}---\n{body}", encoding="utf-8")


def load_all_fms(directory: Path) -> list[tuple[Path, dict, str]]:
    """Ritorna lista (path, frontmatter, body) per ogni FM nella dir."""
    items = []
    if not directory.exists():
        return items
    for f in sorted(directory.glob("FM-*.md")):
        fm, body = parse_frontmatter(f)
        items.append((f, fm, body))
    return items


# === Commands ===

def cmd_quick(description: str) -> int:
    """Crea un nuovo FM pre-compilato in logged/ partendo da descrizione breve."""
    LOGGED_DIR.mkdir(parents=True, exist_ok=True)

    if not TEMPLATE_PATH.exists():
        print(f"ERROR: template non trovato in {TEMPLATE_PATH}", file=sys.stderr)
        return 1

    fm_id = next_fm_id()
    slug = slugify(description, max_len=40)
    if not slug:
        slug = "no-slug"

    filename = f"{fm_id}-{slug}.md"
    target = LOGGED_DIR / filename

    template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    # Sostituzioni
    today = dt.date.today().isoformat()
    template_text = template_text.replace("FM-NNN", fm_id, 1)  # in frontmatter
    template_text = template_text.replace("<slug-breve>", slug, 1)
    template_text = template_text.replace("<YYYY-MM-DD>", today, 1)
    # Riga del titolo
    template_text = template_text.replace(
        "# FM-NNN — <Titolo breve descrittivo>",
        f"# {fm_id} — {description}",
    )

    target.write_text(template_text, encoding="utf-8")

    # Aggiorna index
    rebuild_index()

    print(f"✅ Created {target.relative_to(REPO_ROOT)}")
    print(f"   ID: {fm_id}")
    print(f"   Slug: {slug}")
    print()
    print(f"Next: apri il file e riempi le sezioni 1-8 quando hai 5 minuti.")
    print(f"  $EDITOR {target}")
    return 0


def cmd_triage(non_interactive: bool = False) -> int:
    """Triage di tutti i FM in logged/. Per ognuno chiede severity/cat/scope."""
    items = load_all_fms(LOGGED_DIR)
    if not items:
        print("ℹ️  Nessun FM da triare in logged/")
        return 0

    print(f"📋 {len(items)} FM da triare in logged/")
    print()

    SEVERITY_OPTIONS = ["blocker", "major", "minor"]
    CATEGORY_OPTIONS = [
        "builder", "optimizer", "schema", "pipeline",
        "trigger", "docs", "packaging", "other",
    ]
    SCOPE_OPTIONS = ["hotfix-v1.1.x", "phase-10", "phase-11+"]
    CONFIDENCE_OPTIONS = ["low", "med", "high"]
    EFFORT_OPTIONS = ["30min", "2h", "1d", "multi-day"]

    if non_interactive:
        print("⚠️  --non-interactive: skip prompts. Run senza --non-interactive per triage reale.")
        return 0

    TRIAGED_DIR.mkdir(parents=True, exist_ok=True)

    for path, fm, body in items:
        title_match = re.search(r"^# (FM-\d+.*?)$", body, re.MULTILINE)
        title = title_match.group(1) if title_match else path.stem

        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"  {title}")
        print(f"  File: {path.relative_to(REPO_ROOT)}")
        print()

        # Mostra prime 10 righe del body
        body_preview = "\n".join(body.split("\n")[:15])
        print(body_preview[:500])
        if len(body) > 500:
            print("  [... troncato]")
        print()

        def prompt(label: str, options: list[str], default: str | None = None) -> str:
            print(f"  {label}:")
            for i, opt in enumerate(options, 1):
                marker = " ← default" if opt == default else ""
                print(f"    {i}. {opt}{marker}")
            while True:
                choice = input(f"    Scelta (1-{len(options)}, INVIO=default, 's'=skip): ").strip()
                if choice == "":
                    if default:
                        return default
                    print("    No default. Scegli un numero.")
                    continue
                if choice.lower() == "s":
                    return ""
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    return options[int(choice) - 1]
                print(f"    Input non valido. Riprova.")

        severity = prompt("Severity", SEVERITY_OPTIONS, default="major")
        if severity == "":
            print(f"  ⏭  Skip {fm.get('fm_id', path.stem)}")
            print()
            continue

        category = prompt("Category", CATEGORY_OPTIONS)
        scope = prompt("Scope", SCOPE_OPTIONS,
                       default="hotfix-v1.1.x" if severity == "blocker" else "phase-10")
        confidence = prompt("Confidence root cause", CONFIDENCE_OPTIONS, default="med")
        effort = prompt("Estimated effort", EFFORT_OPTIONS, default="2h")

        # Aggiorna frontmatter
        fm["status"] = "triaged"
        fm["severity"] = severity
        fm["category"] = category
        fm["scope"] = scope
        fm["confidence_root_cause"] = confidence
        fm["estimated_effort"] = effort
        fm["date_triaged"] = dt.date.today().isoformat()

        # Sposta in triaged/
        new_path = TRIAGED_DIR / path.name
        write_with_frontmatter(new_path, fm, body)
        path.unlink()  # remove from logged/

        print(f"  ✅ {fm.get('fm_id', path.stem)} → triaged/ ({severity}/{category}/{scope})")
        print()

    rebuild_index()
    print()
    print(f"🎉 Triage completato. Esegui `--plan-phase10` se hai 3+ FM major/blocker.")
    return 0


def cmd_plan_phase10() -> int:
    """Genera PHASE-10-CANDIDATES.md raggruppando i triaged per categoria + priorità."""
    triaged = load_all_fms(TRIAGED_DIR)
    if not triaged:
        print("ℹ️  Nessun FM triaged. Esegui prima --triage.")
        return 0

    # Filtra solo phase-10 e phase-11+
    phase_candidates = [
        (p, fm, b) for p, fm, b in triaged
        if fm.get("scope") in ("phase-10", "phase-11+")
    ]
    hotfixes = [
        (p, fm, b) for p, fm, b in triaged
        if fm.get("scope") == "hotfix-v1.1.x"
    ]

    if not phase_candidates and not hotfixes:
        print("ℹ️  Nessun FM con scope per Phase 10 o hotfix.")
        return 0

    # Raggruppa per categoria
    by_category = defaultdict(list)
    for p, fm, b in phase_candidates:
        by_category[fm.get("category", "other")].append((p, fm, b))

    # Ordina categorie per numero di FM (più FM = cluster = priorità)
    sorted_categories = sorted(by_category.items(), key=lambda x: -len(x[1]))

    severity_order = {"blocker": 0, "major": 1, "minor": 2}

    lines = [
        "# Phase 10 — Candidates",
        f"",
        f"> Generato il {dt.date.today().isoformat()} da `scripts/log_failure.py --plan-phase10`",
        f"> Sintesi automatica dei failure mode triaged.",
        f"",
        f"## Stats",
        f"",
        f"- **Candidati Phase 10/11+**: {len(phase_candidates)}",
        f"- **Hotfix immediati (v1.1.x)**: {len(hotfixes)}",
        f"- **Categorie coinvolte**: {len(by_category)}",
        f"",
    ]

    # Sezione hotfix
    if hotfixes:
        lines.append("## 🔴 HOTFIX IMMEDIATI (v1.1.x) — da fare PRIMA di Phase 10")
        lines.append("")
        for p, fm, b in sorted(hotfixes, key=lambda x: severity_order.get(x[1].get("severity", "minor"), 99)):
            title = extract_title(b)
            sev = fm.get("severity", "?")
            lines.append(f"- **{fm.get('fm_id', '?')}** [{sev}]: {title}")
            lines.append(f"  - Effort: {fm.get('estimated_effort', '?')}")
            lines.append(f"  - File: `{p.relative_to(REPO_ROOT)}`")
            lines.append("")

    # Sezione per categoria
    lines.append("## 📦 Phase 10 candidates per categoria")
    lines.append("")
    lines.append("> Categorie ordinate per numero di FM (cluster = priorità).")
    lines.append("")

    for category, fms in sorted_categories:
        # Conta severities nella categoria
        sev_counts = Counter(f.get("severity", "?") for _, f, _ in fms)
        sev_summary = " ".join(f"{n}{s[0]}" for s, n in sev_counts.most_common())
        # Determina priorità categoria
        if sev_counts.get("blocker", 0) > 0:
            priority = "🔴 P0 — blocca uso skill"
        elif sev_counts.get("major", 0) >= 2:
            priority = "🟡 P1 — cluster di problemi major"
        elif sev_counts.get("major", 0) == 1:
            priority = "🟡 P2 — 1 major"
        else:
            priority = "🟢 P3 — solo minor"

        lines.append(f"### {category} ({len(fms)} FM, {sev_summary}) — {priority}")
        lines.append("")

        for p, fm, b in sorted(fms, key=lambda x: severity_order.get(x[1].get("severity", "minor"), 99)):
            title = extract_title(b)
            sev = fm.get("severity", "?")
            conf = fm.get("confidence_root_cause", "?")
            eff = fm.get("estimated_effort", "?")
            comps = fm.get("related_components", []) or []
            comps_str = f" [{', '.join(comps)}]" if comps else ""
            lines.append(f"- **{fm.get('fm_id', '?')}** [{sev}, conf={conf}, eff={eff}]{comps_str}: {title}")

        lines.append("")

    # Suggerimenti finali
    lines.append("---")
    lines.append("")
    lines.append("## 💡 Suggerimenti per Phase 10 plan")
    lines.append("")

    if any(fm.get("severity") == "blocker" for _, fm, _ in phase_candidates):
        lines.append("- 🔴 Ci sono **blocker** scoperti come phase-10. Considerare hotfix v1.1.x invece di aspettare Phase 10 completa.")

    biggest_cat, biggest_fms = sorted_categories[0] if sorted_categories else (None, [])
    if biggest_cat and len(biggest_fms) >= 3:
        lines.append(f"- 🎯 Cluster denso in **{biggest_cat}** ({len(biggest_fms)} FM): probabilmente un problema sistemico, vale la pena un refactor mirato qui.")

    total_effort_days = estimate_total_effort(phase_candidates)
    lines.append(f"- ⏱  Effort totale stimato per Phase 10: **~{total_effort_days:.1f} giorni** di lavoro focalizzato")

    low_conf_count = sum(1 for _, fm, _ in phase_candidates if fm.get("confidence_root_cause") == "low")
    if low_conf_count > 0:
        lines.append(f"- ⚠️  {low_conf_count} FM hanno `confidence_root_cause=low` → considera un round di investigation prima di Phase 10")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ⏭ Next steps")
    lines.append("")
    lines.append("1. Review questa analisi")
    lines.append("2. Decidi se fare Phase 10 ora, hotfix incrementali, o continuare ad accumulare FM")
    lines.append("3. Se Phase 10 partita: usa questa lista come input per scrivere `PLAN-v7.md`")

    PHASE10_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Generato {PHASE10_PATH.relative_to(REPO_ROOT)}")
    print(f"   {len(phase_candidates)} candidati Phase 10/11+ analizzati")
    print(f"   {len(hotfixes)} hotfix immediati identificati")
    print(f"   {len(by_category)} categorie coinvolte")
    return 0


def cmd_index() -> int:
    """Rigenera INDEX.md."""
    rebuild_index()
    print(f"✅ {INDEX_PATH.relative_to(REPO_ROOT)} rigenerato")
    return 0


def cmd_list(filter_status: str = "all") -> int:
    """Lista compatta dei FM."""
    dirs_to_check = {
        "logged": LOGGED_DIR,
        "triaged": TRIAGED_DIR,
        "resolved": RESOLVED_DIR,
    }
    if filter_status != "all":
        dirs_to_check = {filter_status: dirs_to_check[filter_status]}

    for status, d in dirs_to_check.items():
        items = load_all_fms(d)
        if not items:
            continue
        print(f"\n{'━' * 60}")
        print(f"{status.upper()} ({len(items)} FM)")
        print(f"{'━' * 60}")
        for p, fm, b in items:
            title = extract_title(b)
            extra = ""
            if status == "triaged":
                sev = fm.get("severity", "?")
                cat = fm.get("category", "?")
                scope = fm.get("scope", "?")
                extra = f" [{sev}/{cat}/{scope}]"
            print(f"  {fm.get('fm_id', '?')}{extra}: {title}")
    return 0


# === Helpers per output ===

def extract_title(body: str) -> str:
    """Estrae il titolo H1 (es. 'FM-001 — Mio bug')."""
    m = re.search(r"^# (.+?)$", body, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        # Rimuovi prefisso FM-NNN —
        title = re.sub(r"^FM-\d+\s*—\s*", "", title)
        return title
    return "(no title)"


def estimate_total_effort(items: list) -> float:
    """Stima effort totale in giorni."""
    map_to_days = {"30min": 0.05, "2h": 0.25, "1d": 1.0, "multi-day": 3.0}
    return sum(map_to_days.get(fm.get("estimated_effort", "2h"), 0.25) for _, fm, _ in items)


def rebuild_index() -> None:
    """Rigenera INDEX.md con tutti i FM."""
    lines = [
        "# INDEX — Failure Modes Log",
        "",
        f"> Aggiornato: {dt.datetime.now().isoformat(timespec='seconds')}",
        "",
    ]

    for status, d in [("logged", LOGGED_DIR), ("triaged", TRIAGED_DIR), ("resolved", RESOLVED_DIR)]:
        items = load_all_fms(d)
        lines.append(f"## {status.upper()} ({len(items)})")
        lines.append("")

        if not items:
            lines.append("_(vuoto)_")
            lines.append("")
            continue

        for p, fm, b in items:
            title = extract_title(b)
            fm_id = fm.get("fm_id", "?")
            file_rel = p.relative_to(REPO_ROOT)
            if status == "triaged":
                sev = fm.get("severity", "?")
                cat = fm.get("category", "?")
                scope = fm.get("scope", "?")
                eff = fm.get("estimated_effort", "?")
                lines.append(f"- [{fm_id}]({file_rel}): {title}  \n  `{sev}/{cat}/{scope}` · effort: {eff}")
            else:
                lines.append(f"- [{fm_id}]({file_rel}): {title}")
        lines.append("")

    INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")



# === AGENT-FACING commands (auto mode) ===

def cmd_quick_auto(description: str, args) -> int:
    """Versione auto di --quick: crea FM con tutti i campi pre-popolati (usato da SI1)."""
    LOGGED_DIR.mkdir(parents=True, exist_ok=True)

    fm_id = next_fm_id()
    slug = slugify(description, max_len=40) or "no-slug"
    filename = f"{fm_id}-{slug}.md"
    target = LOGGED_DIR / filename

    today = dt.date.today().isoformat()

    # Frontmatter pre-popolato
    fm = {
        "fm_id": fm_id,
        "slug": slug,
        "status": "logged",
        "date_logged": today,
        "date_triaged": None,
        "date_resolved": None,
        "severity": None,
        "category": None,
        "scope": None,
        "confidence_root_cause": None,
        "estimated_effort": None,
        "related_fm": [],
        "related_components": [args.source_agent] if args.source_agent else [],
        "forge_version_observed": "1.1",
        "source_stage": args.source_stage or None,
        "logged_by_agent": "SI1",
    }

    # Body
    body_lines = [
        f"# {fm_id} — {description}",
        "",
        "## 1. Cosa è successo (1-3 frasi, fattuale)",
        "",
        args.observation or description,
        "",
        "## 2. Cosa ti aspettavi",
        "",
        "(da completare in triage se necessario — SI1 ha solo osservato l'anomalia)",
        "",
        "## 3. Come riprodurlo",
        "",
        f"- **Stage coinvolto**: {args.source_stage or '?'}",
        f"- **Agente coinvolto**: {args.source_agent or '?'}",
        "",
    ]

    if args.qa_context:
        body_lines.extend([
            "### QA Report context",
            "",
            "```json",
            args.qa_context,
            "```",
            "",
        ])

    body_lines.extend([
        "## 4. Dove si è rotto",
        "",
        f"Stage {args.source_stage or '?'} — agent {args.source_agent or '?'} (rilevato automaticamente da SI1)",
        "",
        "## 5. Impatto",
        "",
        "- **Detection mode**: auto (SI1)",
        "- **Workaround**: da valutare in triage",
        "",
        "## 6. Ipotesi di causa",
        "",
        "(da analizzare in triage da SI2)",
        "",
        "## 7. Suggerimento fix",
        "",
        "(da generare in plan-phase da SI3)",
        "",
        "## 8. Note libere",
        "",
        "FM creato automaticamente da `failure-detector-agent` (SI1).",
    ])

    body = "\n".join(body_lines)
    write_with_frontmatter(target, fm, body)
    rebuild_index()

    print(f"AUTO: created {target.relative_to(REPO_ROOT)}", file=sys.stderr)
    # Output JSON per agente caller
    print(json.dumps({"status": "ok", "fm_id": fm_id, "path": str(target.relative_to(REPO_ROOT))}))
    return 0


def cmd_triage_auto(args) -> int:
    """Versione auto di --triage: usa flag passati invece di prompt (usato da SI2)."""
    if not args.fm_id:
        print(json.dumps({"status": "error", "reason": "missing --fm-id"}), file=sys.stdout)
        return 2
    if not args.severity:
        print(json.dumps({"status": "error", "reason": "missing --severity"}), file=sys.stdout)
        return 2
    if not args.category:
        print(json.dumps({"status": "error", "reason": "missing --category"}), file=sys.stdout)
        return 2
    if not args.scope:
        # Auto-derive: blocker → hotfix; altrimenti phase-10
        args.scope = "hotfix-v1.1.x" if args.severity == "blocker" else "phase-10"

    # Cerca il FM in logged/
    matches = list(LOGGED_DIR.glob(f"{args.fm_id}-*.md"))
    if not matches:
        print(json.dumps({"status": "error", "reason": f"FM {args.fm_id} not found in logged/"}))
        return 2

    path = matches[0]
    fm, body = parse_frontmatter(path)

    fm["status"] = "triaged"
    fm["severity"] = args.severity
    fm["category"] = args.category
    fm["scope"] = args.scope
    fm["confidence_root_cause"] = args.confidence
    fm["estimated_effort"] = args.effort
    fm["date_triaged"] = dt.date.today().isoformat()
    fm["triaged_by_agent"] = "SI2"

    new_path = TRIAGED_DIR / path.name
    write_with_frontmatter(new_path, fm, body)
    path.unlink()
    rebuild_index()

    print(json.dumps({
        "status": "ok",
        "fm_id": args.fm_id,
        "moved_to": str(new_path.relative_to(REPO_ROOT)),
        "metadata": {
            "severity": args.severity,
            "category": args.category,
            "scope": args.scope,
        }
    }))
    return 0


def cmd_plan_phase(phase_num: int) -> int:
    """Generic plan-phase generator (usato da SI3). Generates PHASE-N-CANDIDATES.md."""
    triaged = load_all_fms(TRIAGED_DIR)
    if not triaged:
        print(json.dumps({"status": "skipped", "reason": "no triaged FMs"}))
        return 0

    phase_scope = f"phase-{phase_num}"
    phase_alt_scope = f"phase-{phase_num+1}+"  # accept N+ scope too

    phase_candidates = [
        (p, fm, b) for p, fm, b in triaged
        if fm.get("scope") in (phase_scope, phase_alt_scope, "phase-10", "phase-11+")
    ]
    hotfixes = [
        (p, fm, b) for p, fm, b in triaged
        if fm.get("scope") == "hotfix-v1.1.x"
    ]

    if not phase_candidates and not hotfixes:
        print(json.dumps({"status": "skipped", "reason": f"no candidates for phase {phase_num}"}))
        return 0

    plan_path = LOG_DIR / f"PHASE-{phase_num}-CANDIDATES.md"

    # (Riusa la logica esistente di cmd_plan_phase10 ma con phase_num parametrico)
    by_category = defaultdict(list)
    for p, fm, b in phase_candidates:
        by_category[fm.get("category", "other")].append((p, fm, b))

    sorted_categories = sorted(by_category.items(), key=lambda x: -len(x[1]))
    severity_order = {"blocker": 0, "major": 1, "minor": 2}

    lines = [
        f"# Phase {phase_num} — Candidates",
        f"",
        f"> Generato il {dt.date.today().isoformat()} da SI3 phase-planner-agent",
        f"> Auto-trigger: soglie failure mode raggiunte",
        f"",
        f"## Stats",
        f"",
        f"- **Candidati Phase {phase_num}**: {len(phase_candidates)}",
        f"- **Hotfix immediati (v1.1.x)**: {len(hotfixes)}",
        f"- **Categorie coinvolte**: {len(by_category)}",
        f"",
    ]

    if hotfixes:
        lines.append("## 🔴 HOTFIX IMMEDIATI (v1.1.x)")
        lines.append("")
        for p, fm, b in sorted(hotfixes, key=lambda x: severity_order.get(x[1].get("severity", "minor"), 99)):
            title = extract_title(b)
            sev = fm.get("severity", "?")
            lines.append(f"- **{fm.get('fm_id', '?')}** [{sev}]: {title}")
            lines.append(f"  - Effort: {fm.get('estimated_effort', '?')} | File: `{p.relative_to(REPO_ROOT)}`")
        lines.append("")

    lines.append(f"## 📦 Phase {phase_num} candidates per categoria")
    lines.append("")

    for category, fms in sorted_categories:
        sev_counts = Counter(f.get("severity", "?") for _, f, _ in fms)
        sev_summary = " ".join(f"{n}{s[0]}" for s, n in sev_counts.most_common())
        if sev_counts.get("blocker", 0) > 0:
            priority = "🔴 P0"
        elif sev_counts.get("major", 0) >= 2:
            priority = "🟡 P1 (cluster major)"
        elif sev_counts.get("major", 0) == 1:
            priority = "🟡 P2"
        else:
            priority = "🟢 P3"

        lines.append(f"### {category} ({len(fms)} FM, {sev_summary}) — {priority}")
        lines.append("")
        for p, fm, b in sorted(fms, key=lambda x: severity_order.get(x[1].get("severity", "minor"), 99)):
            title = extract_title(b)
            sev = fm.get("severity", "?")
            conf = fm.get("confidence_root_cause", "?")
            eff = fm.get("estimated_effort", "?")
            comps = fm.get("related_components", []) or []
            comps_str = f" [{', '.join(comps)}]" if comps else ""
            lines.append(f"- **{fm.get('fm_id', '?')}** [{sev}, conf={conf}, eff={eff}]{comps_str}: {title}")
        lines.append("")

    total_days = estimate_total_effort(phase_candidates)
    lines.append("---")
    lines.append("")
    lines.append(f"**Effort totale stimato**: ~{total_days:.1f} giorni")
    lines.append("")
    lines.append("**Notifica utente**: questo file è stato generato silenziosamente. Per vederlo:")
    lines.append('chiedi a Forge "Hai preparato un piano per la prossima phase?" → Conductor risponderà.')

    plan_path.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "phase": phase_num,
        "candidates": len(phase_candidates),
        "hotfixes": len(hotfixes),
        "categories": len(by_category),
        "estimated_days": round(total_days, 1),
        "plan_path": str(plan_path.relative_to(REPO_ROOT)),
    }))
    return 0


def cmd_check_thresholds() -> int:
    """Esce 0 se soglie raggiunte per phase plan. Usato da Conductor in Stage 10."""
    triaged = load_all_fms(TRIAGED_DIR)
    if not triaged:
        print(json.dumps({"thresholds_met": False, "reason": "no triaged FMs", "triaged_count": 0}))
        return 1

    sev_counts = Counter(fm.get("severity", "?") for _, fm, _ in triaged)
    by_category_sev = defaultdict(lambda: Counter())
    for _, fm, _ in triaged:
        by_category_sev[fm.get("category", "other")][fm.get("severity", "?")] += 1

    blocker_count = sev_counts.get("blocker", 0)
    major_count = sev_counts.get("major", 0)
    total = len(triaged)

    # Trova cluster (≥3 major in stessa categoria)
    cluster_categories = [
        cat for cat, counts in by_category_sev.items()
        if counts.get("major", 0) >= 3
    ]

    reasons_met = []
    if blocker_count >= 1:
        reasons_met.append(f"{blocker_count} blocker (hotfix needed)")
    if cluster_categories:
        reasons_met.append(f"cluster di major in: {cluster_categories}")
    if major_count >= 3:
        reasons_met.append(f"{major_count} major totali")
    if total >= 5:
        reasons_met.append(f"{total} FM triaged totali (massa critica)")

    thresholds_met = bool(reasons_met)

    print(json.dumps({
        "thresholds_met": thresholds_met,
        "reasons": reasons_met,
        "triaged_count": total,
        "blocker_count": blocker_count,
        "major_count": major_count,
        "cluster_categories": cluster_categories,
    }))
    return 0 if thresholds_met else 1



def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--quick", metavar="DESC", help="Crea nuovo FM con descrizione breve")
    group.add_argument("--triage", action="store_true", help="Triage interattivo dei FM in logged/")
    group.add_argument("--plan-phase", metavar="N", type=int, help="Genera PHASE-N-CANDIDATES.md")
    group.add_argument("--plan-phase10", action="store_true", help="(legacy) Genera PHASE-10-CANDIDATES.md")
    group.add_argument("--index", action="store_true", help="Rigenera INDEX.md")
    group.add_argument("--list", metavar="STATUS", nargs="?", const="all",
                       choices=["all", "logged", "triaged", "resolved"], help="Lista compatta")
    group.add_argument("--check-thresholds", action="store_true",
                       help="Esce con codice 0 se soglie phase plan raggiunte, 1 altrimenti. Usato da SI3.")

    # === Args per modalità AGENT (--auto) ===
    parser.add_argument("--auto", action="store_true",
                        help="Modalità non-interattiva per agenti (SI1/SI2/SI3)")
    parser.add_argument("--non-interactive", action="store_true",
                        help="(deprecato — alias di --auto)")
    parser.add_argument("--fm-id", help="(--triage --auto) FM specifico da triare")
    parser.add_argument("--severity", choices=["blocker", "major", "minor"],
                        help="(--auto) severity preassegnata")
    parser.add_argument("--category",
                        choices=["builder", "optimizer", "schema", "pipeline",
                                 "trigger", "docs", "packaging", "other"],
                        help="(--auto) category preassegnata")
    parser.add_argument("--scope", choices=["hotfix-v1.1.x", "phase-10", "phase-11+"],
                        help="(--auto) scope preassegnato")
    parser.add_argument("--confidence", choices=["low", "med", "high"], default="med",
                        help="(--auto) confidence preassegnata")
    parser.add_argument("--effort", choices=["30min", "2h", "1d", "multi-day"], default="2h",
                        help="(--auto) effort preassegnato")
    parser.add_argument("--observation", default="",
                        help="(--quick --auto) testo dettagliato dell'osservazione per pre-riempire il body")
    parser.add_argument("--source-stage", default="",
                        help="(--auto) stage del pipeline dove si è rotto (1-9)")
    parser.add_argument("--source-agent", default="",
                        help="(--auto) agente coinvolto (es. B2, O3)")
    parser.add_argument("--qa-context", default="",
                        help="(--auto) JSON serializzato del qa-report che ha triggerato la detection")

    args = parser.parse_args(argv)

    # Ensure dirs exist
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOGGED_DIR.mkdir(parents=True, exist_ok=True)
    TRIAGED_DIR.mkdir(parents=True, exist_ok=True)
    RESOLVED_DIR.mkdir(parents=True, exist_ok=True)

    auto = args.auto or args.non_interactive

    if args.quick:
        if auto:
            return cmd_quick_auto(args.quick, args)
        return cmd_quick(args.quick)
    if args.triage:
        if auto:
            return cmd_triage_auto(args)
        return cmd_triage(non_interactive=False)
    if args.plan_phase is not None:
        return cmd_plan_phase(args.plan_phase)
    if args.plan_phase10:
        return cmd_plan_phase(10)
    if args.index:
        return cmd_index()
    if args.list is not None:
        return cmd_list(args.list)
    if args.check_thresholds:
        return cmd_check_thresholds()

    return 1


if __name__ == "__main__":
    sys.exit(main())
