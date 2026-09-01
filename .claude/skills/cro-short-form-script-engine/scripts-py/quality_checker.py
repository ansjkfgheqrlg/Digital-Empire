#!/usr/bin/env python3
"""
Quality Checker for Short-Form Script Engine.

Runs the pre-registration checklist on a script to verify
it meets all quality standards before recording.

Usage:
    python quality_checker.py --hook "..." --tension "..." --payload "..." --cta "..." --type azione
    python quality_checker.py --script-file script.json
"""

import argparse
import json
import sys


# ═══════════════════════════════════════════
# CHECKLIST DEFINITIONS
# ═══════════════════════════════════════════

WORD_COUNT_RANGES = {
    "azione":    {"min": 40,  "max": 120},
    "educativo": {"min": 160, "max": 480},
    "prova":     {"min": 80,  "max": 240},
    "trend":     {"min": 20,  "max": 80}
}

FILLER_WORDS = [
    "fondamentalmente", "in pratica", "come sapete",
    "è importante dire che", "va detto che", "a dire il vero",
    "diciamo", "praticamente", "sostanzialmente",
    "ovviamente", "chiaramente", "naturalmente"
]

FORBIDDEN_HOOK_STARTS = [
    "ciao", "hey", "buongiorno", "buonasera", "ciao a tutti",
    "ciao ragazzi", "in questo video", "oggi parliamo",
    "in questo tutorial", "mi chiamo", "sono il", "sono un",
    "benvenuti", "bentornati", "salve"
]

CRO_KEYWORDS = [
    "checkout", "landing", "funnel", "form", "cta", "bottone",
    "headline", "above the fold", "bounce", "carrello",
    "conversion", "traffico", "click", "%", "€",
    "social proof", "test", "copy", "lead"
]


def run_checklist(
    hook: str,
    tension: str,
    payload: str,
    cta: str,
    tipo_video: str,
    caption: str = ""
) -> dict:
    """
    Run the complete pre-registration quality checklist.

    Returns:
        dict with results per section, blockers, warnings, and verdict
    """

    all_text = f"{hook} {tension} {payload} {cta}"
    total_words = len(all_text.split())
    results = {
        "checks": [],
        "blockers": [],
        "warnings": [],
        "info": []
    }

    def add_check(check_id, section, description, passed, severity, fix=""):
        entry = {
            "id": check_id,
            "section": section,
            "check": description,
            "passed": passed,
            "severity": severity
        }
        results["checks"].append(entry)
        if not passed:
            msg = f"[{check_id}] {description}"
            if fix:
                msg += f" → {fix}"
            if severity == "BLOCKING":
                results["blockers"].append(msg)
            elif severity == "IMPORTANT":
                results["warnings"].append(msg)
            else:
                results["info"].append(msg)

    # ════════════ HOOK (B1) ════════════

    hook_lower = hook.lower().strip()
    hook_words = len(hook.split())

    # H1: Uses one of 8 formulas (heuristic: has number, starts with key words, etc.)
    has_hook_signal = (
        any(c.isdigit() for c in hook) or
        hook_lower.startswith(("se ", "pov", "ho ", "la maggior", "nessuno", "quand", "l'errore", "l'")) or
        "%" in hook
    )
    add_check("H1", "HOOK", "Prima frase usa una delle 8 formule hook",
              has_hook_signal, "BLOCKING",
              "Riscrivi con una delle 8 formule (vedi references/hook_system.md)")

    # H2: Doesn't start with forbidden words
    starts_forbidden = any(hook_lower.startswith(f) for f in FORBIDDEN_HOOK_STARTS)
    add_check("H2", "HOOK", "NON inizia con 'Ciao', 'Hey', 'In questo video'",
              not starts_forbidden, "BLOCKING",
              "Elimina il saluto. Prima parola DEVE essere l'hook.")

    # H3: CRO specific
    has_cro = any(kw in hook_lower for kw in CRO_KEYWORDS)
    add_check("H3", "HOOK", "Specifico per target CRO (non generico)",
              has_cro, "BLOCKING",
              "Aggiungi elemento specifico: metrica CRO, elemento pagina")

    # H4: Contains data/provocation/situation
    has_data_provocation = (
        any(c.isdigit() for c in hook) or
        any(w in hook_lower for w in ["non", "sbagliato", "errore", "pov", "quando"]) or
        "?" in hook
    )
    add_check("H4", "HOOK", "Contiene dato, provocazione, o situazione riconoscibile",
              has_data_provocation, "IMPORTANT")

    # H5: ≤15 words
    add_check("H5", "HOOK", f"Hook ≤15 parole (attuale: {hook_words})",
              hook_words <= 15, "IMPORTANT",
              "Taglia. Se non puoi dirlo in 15 parole, l'hook è troppo complesso.")

    # ════════════ TENSION (B2) ════════════

    if tipo_video != "trend":
        has_tension = len(tension.strip()) > 10
        add_check("T1", "TENSIONE", "Bridge tra hook e payload presente",
                  has_tension, "IMPORTANT",
                  "Aggiungi 2-3 frasi usando amplificazione, falsa pista, o promessa")

        # Open loop check
        open_loop_signals = [
            "perché", "il problema", "la parte peggiore", "e no",
            "non è", "ti faccio vedere", "ti mostro", "ecco",
            "la soluzione", "il motivo"
        ]
        has_open_loop = any(s in tension.lower() for s in open_loop_signals)
        add_check("T2", "TENSIONE", "Crea motivo per NON scrollare (open loop)",
                  has_open_loop, "BLOCKING" if has_tension else "IMPORTANT",
                  "La tensione deve creare un open loop: perché restare?")

    # ════════════ PAYLOAD (B3) ════════════

    payload_lower = payload.lower()

    # P1: One concept (heuristic: count major section headers)
    # Can't perfectly check this, but flag if obviously multi-topic
    add_check("P1", "PAYLOAD", "Contiene UN solo concetto principale",
              True, "BLOCKING")  # Manual check — always passes auto

    # P3: Has proof element
    proof_signals = [
        "cliente", "risultato", "esempio", "%", "€", "euro",
        "dati", "numeri", "abbiamo", "test", "screenshot",
        "mostra", "guarda"
    ]
    has_proof = any(s in payload_lower for s in proof_signals)
    add_check("P3", "PAYLOAD", "Ha almeno 1 elemento di prova (dato, esempio, screenshot)",
              has_proof, "BLOCKING",
              "Aggiungi: dato numerico, esempio cliente, o screenshot prima/dopo")

    # P4: Retention hooks (if >30 sec estimated)
    estimated_duration = total_words / 2.7
    if estimated_duration > 35:
        retention_signals = [
            "ma aspetta", "e qui arriva", "ora ti mostro", "stop",
            "dimenticati", "con un cliente", "non lo dico io",
            "vuoi sapere", "indovina", "scommetto", "fermati",
            "il vero motivo", "la parte interessante",
            "la maggior parte sbaglia", "il più importante"
        ]
        has_retention = any(s in payload_lower for s in retention_signals)
        add_check("P4", "PAYLOAD",
                  f"Retention hooks presenti (video stimato ~{int(estimated_duration)}s, >30s)",
                  has_retention, "IMPORTANT",
                  "Inserisci retention hooks ogni 20-30 sec (vedi references/retention_hooks.md)")

    # P5: Second person
    tu_words = ["tu", "tuo", "tua", "tuoi", "tue", "ti"]
    io_words = ["io", "noi", "mio", "mia", "nostro", "nostra"]
    tu_count = sum(1 for w in payload_lower.split() if w in tu_words)
    io_count = sum(1 for w in payload_lower.split() if w in io_words)
    add_check("P5", "PAYLOAD", f"Parla in seconda persona (tu:{tu_count} vs io/noi:{io_count})",
              tu_count >= io_count or tu_count >= 3, "IMPORTANT",
              "Riscrivi le frasi in 'io/noi' trasformandole in 'tu/il tuo'")

    # P6: Accessible language (check for heavy jargon)
    jargon = ["multivariate", "heatmap", "cohort", "attribution", "pixel",
              "server-side", "webhook", "API", "SDK", "regression"]
    jargon_found = [j for j in jargon if j.lower() in payload_lower]
    add_check("P6", "PAYLOAD", "Linguaggio accessibile (no gergo tecnico pesante)",
              len(jargon_found) == 0, "IMPORTANT",
              f"Semplifica: {', '.join(jargon_found)}" if jargon_found else "")

    # ════════════ CTA (B4) ════════════

    cta_lower = cta.lower().strip()

    # C1: CTA present
    add_check("C1", "CTA", "UNA CTA chiara presente",
              len(cta.strip()) >= 10, "BLOCKING",
              "Aggiungi CTA. Ogni video senza CTA è intrattenimento gratuito.")

    # C2: Says what they get
    value_signals = ["checklist", "25 punti", "gratis", "gratuita",
                     "ti mando", "ricevi", "link in bio", "scarica"]
    has_value = any(s in cta_lower for s in value_signals)
    add_check("C2", "CTA", "Dice cosa OTTENGONO (non solo cosa fare)",
              has_value, "IMPORTANT",
              "'Commenta AUDIT' → 'Commenta AUDIT e ti mando la checklist con 25 punti'")

    # C3: No double CTA
    action_words = ["commenta", "segui", "link in bio", "salva", "prenota", "scarica"]
    actions_found = [a for a in action_words if a in cta_lower]
    add_check("C3", "CTA", f"UNA sola azione richiesta (trovate: {len(actions_found)})",
              len(actions_found) <= 1, "BLOCKING" if len(actions_found) > 2 else "IMPORTANT",
              f"Doppia CTA rilevata: {actions_found}. Scegline UNA." if len(actions_found) > 1 else "")

    # C4: CTA in caption
    if caption:
        cta_in_caption = any(s in caption.lower() for s in ["commenta", "link in bio", "audit", "checklist"])
        add_check("C4", "CTA", "CTA ripetuta nella caption",
                  cta_in_caption, "IMPORTANT",
                  "Copia la CTA nella caption del post")

    # ════════════ TONE ════════════

    # BV4: Filler words
    fillers_found = [f for f in FILLER_WORDS if f in all_text.lower()]
    add_check("BV4", "TONO", "Zero riempitivi/filler",
              len(fillers_found) == 0, "IMPORTANT",
              f"Elimina: {', '.join(fillers_found)}" if fillers_found else "")

    # ════════════ LENGTH ════════════

    word_range = WORD_COUNT_RANGES.get(tipo_video, {"min": 20, "max": 480})
    in_range = word_range["min"] <= total_words <= word_range["max"]
    add_check("L1", "LUNGHEZZA",
              f"Parole nel range per {tipo_video}: {word_range['min']}-{word_range['max']} (attuale: {total_words})",
              in_range, "IMPORTANT",
              f"{'Troppo corto — aggiungi dettaglio' if total_words < word_range['min'] else 'Troppo lungo — taglia'}"
              if not in_range else "")

    # ════════════ SUMMARY ════════════

    total_checks = len(results["checks"])
    passed_checks = sum(1 for c in results["checks"] if c["passed"])
    percentage = round((passed_checks / total_checks) * 100) if total_checks > 0 else 0

    num_blockers = len(results["blockers"])

    if num_blockers == 0 and percentage >= 80:
        verdict = "✅ PRONTO PER REGISTRARE"
    elif num_blockers == 0:
        verdict = "⚠️ RIVEDERE — fix i warning prima di registrare"
    else:
        verdict = f"🚫 BLOCCATO — {num_blockers} check bloccanti da risolvere"

    results["summary"] = {
        "total_checks": total_checks,
        "passed": passed_checks,
        "percentage": percentage,
        "blockers_count": num_blockers,
        "warnings_count": len(results["warnings"]),
        "verdict": verdict,
        "estimated_duration_sec": round(total_words / 2.7),
        "total_words": total_words
    }

    return results


def format_results(results: dict) -> str:
    """Format results for terminal display."""
    lines = []
    summary = results["summary"]

    lines.append("\n" + "=" * 60)
    lines.append("  SCRIPT QUALITY CHECK — Pre-registrazione")
    lines.append("=" * 60)

    # Verdict
    lines.append(f"\n  {summary['verdict']}")
    lines.append(f"  Score: {summary['passed']}/{summary['total_checks']} ({summary['percentage']}%)")
    lines.append(f"  Parole totali: {summary['total_words']} (~{summary['estimated_duration_sec']}s)")

    # Blockers
    if results["blockers"]:
        lines.append(f"\n  🚫 BLOCCANTI ({len(results['blockers'])}):")
        for b in results["blockers"]:
            lines.append(f"     {b}")

    # Warnings
    if results["warnings"]:
        lines.append(f"\n  ⚠️ WARNING ({len(results['warnings'])}):")
        for w in results["warnings"]:
            lines.append(f"     {w}")

    # Info
    if results["info"]:
        lines.append(f"\n  ℹ️ INFO ({len(results['info'])}):")
        for i in results["info"]:
            lines.append(f"     {i}")

    # All checks
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  {'ID':<6} {'SEZ':<10} {'STATO':<6} {'CHECK'}")
    lines.append(f"  {'─' * 56}")
    for check in results["checks"]:
        status = "✅" if check["passed"] else ("🚫" if check["severity"] == "BLOCKING" else "⚠️")
        lines.append(f"  {check['id']:<6} {check['section']:<10} {status:<6} {check['check'][:45]}")

    lines.append("=" * 60 + "\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Script Quality Checker")

    # Option 1: Individual fields
    parser.add_argument("--hook", default="", help="Hook text (B1)")
    parser.add_argument("--tension", default="", help="Tension text (B2)")
    parser.add_argument("--payload", default="", help="Payload text (B3)")
    parser.add_argument("--cta", default="", help="CTA text (B4)")
    parser.add_argument("--caption", default="", help="Caption text")
    parser.add_argument("--type", default="azione", choices=["azione", "educativo", "prova", "trend"])

    # Option 2: JSON file
    parser.add_argument("--script-file", help="Path to script JSON file")

    # Output format
    parser.add_argument("--format", default="text", choices=["text", "json"])

    args = parser.parse_args()

    if args.script_file:
        with open(args.script_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        hook = data.get("hook", data.get("B1_HOOK", {}).get("testo", ""))
        tension = data.get("tension", data.get("B2_TENSIONE", {}).get("testo", ""))
        payload = data.get("payload", data.get("B3_PAYLOAD", {}).get("testo", ""))
        cta = data.get("cta", data.get("B4_CTA", {}).get("testo", ""))
        caption = data.get("caption", "")
        tipo = data.get("tipo_video", data.get("type", "azione"))
    else:
        hook = args.hook
        tension = args.tension
        payload = args.payload
        cta = args.cta
        caption = args.caption
        tipo = args.type

    if not hook and not args.script_file:
        parser.print_help()
        print("\n❌ Fornisci almeno --hook e --cta, oppure --script-file")
        sys.exit(1)

    results = run_checklist(hook, tension, payload, cta, tipo, caption)

    if args.format == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))

    # Exit code: 0 if ready, 1 if blocked
    sys.exit(0 if results["summary"]["blockers_count"] == 0 else 1)


if __name__ == "__main__":
    main()