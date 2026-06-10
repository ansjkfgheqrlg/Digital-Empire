#!/usr/bin/env python3
"""
Empire Studio - generate_strategy_manifest.py  (REALE)

Genera il Strategy Manifest per una run combinando: strategia di reparto +
strategia di tipo contenuto + stile di implementazione wiki. Usato dallo
strategy-coordinator. Salva in memory/strategy-applications/.

Uso:
  python scripts/generate_strategy_manifest.py --input-type youtube --focus design --run <run-id>
"""
import argparse
import json
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPS = ROOT / "memory" / "strategy-applications"

DEPT_STRATEGY = {
    "youtube": ("YouTube Department Strategy", ["frame per capitolo + intermedi", "long-form: visione densa"]),
    "tiktok": ("TikTok Department Strategy", ["frame densi ogni 3-8s", "hook visivo + output finale"]),
    "web": ("Web Department Strategy", ["Playwright render JS", "screenshot sezioni chiave"]),
    "projects": ("Projects/Repos Deep-Study Strategy", ["sola lettura", "architettura + perche' + trace a file:riga"]),
}
CONTENT_RULES = {
    "design": ("Design System Content", ["frame su componenti/export/token", "descrizioni visive >60 parole"], "Visual-Heavy Reference"),
    "marketing": ("Marketing Content", ["estrai framework + esempi + metriche"], "Playbook"),
    "automation": ("Automazioni/Tool Content", ["comandi esatti + gotchas mostrati"], "How-to Quick-Reference"),
    "tools": ("Tool Usage Content", ["passaggi UI + risultati a schermo"], "How-to"),
}


def build(input_type, focus, run_id):
    it = input_type.lower()
    f = focus.lower()
    dept_name, dept_rules = DEPT_STRATEGY.get(it, ("Generic Department Strategy", ["pipeline standard"]))
    ckey = next((k for k in CONTENT_RULES if k in f), None)
    if ckey:
        ct_name, ct_rules, wiki_style = CONTENT_RULES[ckey]
    else:
        ct_name, ct_rules, wiki_style = ("General Content", ["espansione, no riassunto"], "Atomic Notes + MOC")
    rules = dept_rules + ct_rules + ["ogni atomo con trace P12"]
    if any(k in f for k in ("design", "automation", "skill", "tool")):
        rules.append("genera update proposals per workflow esistenti")
    return {
        "run_id": run_id or f"run-{datetime.datetime.now():%Y%m%dT%H%M%S}",
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "input": {"type": input_type, "focus": focus},
        "selected_strategies": {"department": dept_name, "content_type": ct_name,
                                "wiki_implementation": wiki_style},
        "rules": rules,
        "rationale": f"Input {input_type} con focus '{focus}': {dept_name} + {ct_name} -> stile wiki {wiki_style}.",
        "trace": "generato da generate_strategy_manifest.py (strategy-coordinator)",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-type", required=True, help="youtube|tiktok|web|projects")
    ap.add_argument("--focus", default="", help="design|marketing|automation|tools|...")
    ap.add_argument("--run", default="")
    args = ap.parse_args()
    man = build(args.input_type, args.focus, args.run)
    APPS.mkdir(parents=True, exist_ok=True)
    base = man["run_id"]
    (APPS / f"manifest-{base}.json").write_text(json.dumps(man, indent=2, ensure_ascii=False), encoding="utf-8")
    md = [f"# Strategy Manifest - {base}", f"_{man['generated_at']}_", "",
          "## Strategie selezionate"]
    for k, v in man["selected_strategies"].items():
        md.append(f"- **{k}**: {v}")
    md += ["", "## Regole"] + [f"- {r}" for r in man["rules"]]
    md += ["", f"**Rationale:** {man['rationale']}", "", f"**Trace:** {man['trace']}"]
    (APPS / f"manifest-{base}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"[strategy] {man['selected_strategies']}")
    print(f"[strategy] -> memory/strategy-applications/manifest-{base}.json")


if __name__ == "__main__":
    main()
