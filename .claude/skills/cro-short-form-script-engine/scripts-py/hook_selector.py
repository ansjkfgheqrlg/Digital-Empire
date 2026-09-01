#!/usr/bin/env python3
"""
Hook Selector + Validator for Short-Form Script Engine.

Usage:
    python hook_selector.py --type educativo --topic "above the fold" --has-data
    python hook_selector.py --validate "Il 67% dei carrelli viene abbandonato."
"""

import argparse
import json
import sys


# ═══════════════════════════════════════════
# HOOK FORMULAS DATABASE
# ═══════════════════════════════════════════

HOOK_FORMULAS = {
    "F1_DATO_SHOCK": {
        "nome": "Dato Shock",
        "icona": "📊",
        "template": "[Numero specifico]% [di cosa] [fa/non fa] [cosa].",
        "tipo_video_ideale": ["azione", "educativo"],
        "forza": 9,
        "richiede_dati": True
    },
    "F2_PROVOCAZIONE": {
        "nome": "Provocazione Diretta",
        "icona": "⚡",
        "template": "[Cosa che tutti credono/fanno] [è sbagliato/non funziona/ti sta costando soldi].",
        "tipo_video_ideale": ["azione", "educativo"],
        "forza": 8,
        "richiede_dati": False
    },
    "F3_POV_SITUAZIONE": {
        "nome": "POV / Situazione",
        "icona": "👁️",
        "template": "POV: [situazione specifica in cui il target si riconosce]",
        "tipo_video_ideale": ["trend", "azione"],
        "forza": 7,
        "richiede_dati": False
    },
    "F4_SE_ALLORA": {
        "nome": "Se...Allora",
        "icona": "🎯",
        "template": "Se [condizione specifica del target], [conseguenza negativa].",
        "tipo_video_ideale": ["azione", "educativo"],
        "forza": 9,
        "richiede_dati": False
    },
    "F5_DOMANDA_SCOMODA": {
        "nome": "Domanda Retorica Scomoda",
        "icona": "❓",
        "template": "Quand'è l'ultima volta che [azione che dovrebbero fare ma non fanno]?",
        "tipo_video_ideale": ["educativo", "azione"],
        "forza": 7,
        "richiede_dati": False
    },
    "F6_HO_TROVATO": {
        "nome": "Ho Trovato / Ho Appena",
        "icona": "🔍",
        "template": "Ho [appena/trovato/scoperto] [cosa] [dove/in chi] [e implicazione].",
        "tipo_video_ideale": ["azione", "prova"],
        "forza": 8,
        "richiede_dati": False
    },
    "F7_MAGGIOR_PARTE": {
        "nome": "La Maggior Parte / Nessuno",
        "icona": "👥",
        "template": "La maggior parte [di chi/delle aziende] [fa cosa sbagliata]. Ecco cosa fare invece.",
        "tipo_video_ideale": ["educativo", "azione"],
        "forza": 8,
        "richiede_dati": False
    },
    "F8_ERRORE": {
        "nome": "Errore / Cosa Sbagliata",
        "icona": "🚫",
        "template": "[Numero] errori che [uccidono/distruggono/costano] [cosa del target].",
        "tipo_video_ideale": ["azione", "educativo"],
        "forza": 9,
        "richiede_dati": False
    }
}

# Hook → Tension compatibility
TENSION_COMPATIBILITY = {
    "F1_DATO_SHOCK":      {"primaria": "T1_AMPLIFICAZIONE", "secondaria": "T3_PROMESSA_VALORE"},
    "F2_PROVOCAZIONE":    {"primaria": "T2_FALSA_PISTA",    "secondaria": "T1_AMPLIFICAZIONE"},
    "F3_POV_SITUAZIONE":  {"primaria": "T1_AMPLIFICAZIONE", "secondaria": "T3_PROMESSA_VALORE"},
    "F4_SE_ALLORA":       {"primaria": "T2_FALSA_PISTA",    "secondaria": "T1_AMPLIFICAZIONE"},
    "F5_DOMANDA_SCOMODA": {"primaria": "T2_FALSA_PISTA",    "secondaria": "T3_PROMESSA_VALORE"},
    "F6_HO_TROVATO":     {"primaria": "T3_PROMESSA_VALORE", "secondaria": "T1_AMPLIFICAZIONE"},
    "F7_MAGGIOR_PARTE":   {"primaria": "T1_AMPLIFICAZIONE", "secondaria": "T3_PROMESSA_VALORE"},
    "F8_ERRORE":          {"primaria": "T1_AMPLIFICAZIONE", "secondaria": "T2_FALSA_PISTA"}
}

TENSION_NAMES = {
    "T1_AMPLIFICAZIONE": "Amplificazione del Problema",
    "T2_FALSA_PISTA": "Falsa Pista",
    "T3_PROMESSA_VALORE": "Promessa di Valore"
}


# ═══════════════════════════════════════════
# HOOK SELECTOR
# ═══════════════════════════════════════════

def select_hooks(
    tipo_video: str,
    argomento: str = "",
    ha_dati: bool = False,
    ha_caso_studio: bool = False,
    tono: str = "diretto"
) -> list:
    """
    Selects the 3 best hook formulas for the given context.

    Args:
        tipo_video: 'azione' | 'educativo' | 'prova' | 'trend'
        argomento: topic of the video
        ha_dati: whether data/statistics are available
        ha_caso_studio: whether a case study is available
        tono: 'diretto' | 'provocatorio' | 'educativo'

    Returns:
        List of top 3 hook formulas with scores and tension pairing
    """
    scores = {}

    for formula_id, formula in HOOK_FORMULAS.items():
        score = formula["forza"]

        # Match video type
        if tipo_video in formula["tipo_video_ideale"]:
            score += 3

        # Bonus if data available and formula uses it
        if ha_dati and formula["richiede_dati"]:
            score += 3
        if ha_dati and formula_id in ["F1_DATO_SHOCK", "F4_SE_ALLORA", "F8_ERRORE"]:
            score += 2

        # Bonus if case study available
        if ha_caso_studio and formula_id in ["F6_HO_TROVATO", "F1_DATO_SHOCK"]:
            score += 3

        # Tone matching
        if tono == "provocatorio" and formula_id in ["F2_PROVOCAZIONE", "F7_MAGGIOR_PARTE"]:
            score += 2
        elif tono == "educativo" and formula_id in ["F5_DOMANDA_SCOMODA", "F1_DATO_SHOCK"]:
            score += 2
        elif tono == "diretto" and formula_id in ["F4_SE_ALLORA", "F8_ERRORE"]:
            score += 2

        # Penalty for mismatch
        if tipo_video == "trend" and formula_id not in ["F3_POV_SITUAZIONE", "F7_MAGGIOR_PARTE"]:
            score -= 2
        if tipo_video == "prova" and formula_id not in ["F6_HO_TROVATO", "F1_DATO_SHOCK"]:
            score -= 1

        scores[formula_id] = score

    # Rank and return top 3
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    results = []
    for formula_id, score in ranked:
        formula = HOOK_FORMULAS[formula_id]
        tension = TENSION_COMPATIBILITY.get(formula_id, {})

        results.append({
            "formula_id": formula_id,
            "nome": formula["nome"],
            "icona": formula["icona"],
            "template": formula["template"],
            "score": score,
            "tensione_consigliata": {
                "primaria": TENSION_NAMES.get(tension.get("primaria", ""), ""),
                "secondaria": TENSION_NAMES.get(tension.get("secondaria", ""), "")
            }
        })

    return results


# ═══════════════════════════════════════════
# HOOK VALIDATOR
# ═══════════════════════════════════════════

FORBIDDEN_STARTS = [
    "ciao", "hey", "buongiorno", "buonasera", "ciao a tutti",
    "ciao ragazzi", "in questo video", "oggi parliamo",
    "in questo tutorial", "mi chiamo", "sono il", "sono un",
    "benvenuti", "bentornati", "salve"
]

GENERIC_QUESTIONS = [
    "vuoi fare più soldi", "vuoi migliorare",
    "ti piacerebbe avere più", "vuoi guadagnare"
]

CRO_SPECIFICS = [
    "checkout", "landing", "funnel", "form", "cta", "bottone",
    "headline", "above the fold", "bounce", "carrello",
    "abbandono", "conversion", "traffico", "click", "scroll",
    "%", "€", "social proof", "split test", "a/b test"
]


def validate_hook(hook_text: str) -> dict:
    """
    Validates a hook against all quality rules.

    Args:
        hook_text: the hook text to validate

    Returns:
        dict with 'valid', 'score' (0-10), 'issues', 'suggestion'
    """
    issues = []
    score = 10
    hook_lower = hook_text.lower().strip()
    words = hook_text.split()
    word_count = len(words)

    # ── Length check ──
    if word_count > 20:
        issues.append(f"🚫 TROPPO LUNGO: {word_count} parole (max 15, tolleranza 20)")
        score -= 4
    elif word_count > 15:
        issues.append(f"⚠️ Lungo: {word_count} parole (ideale ≤15)")
        score -= 2

    # ── Forbidden openings ──
    for forbidden in FORBIDDEN_STARTS:
        if hook_lower.startswith(forbidden):
            issues.append(f"🚫 VIETATO: inizia con '{forbidden}'")
            score -= 5
            break

    # ── Generic questions ──
    for gq in GENERIC_QUESTIONS:
        if gq in hook_lower:
            issues.append(f"🚫 Domanda generica: '{gq}'")
            score -= 4
            break

    # ── Specificity check ──
    has_number = any(char.isdigit() for char in hook_text)
    has_specific = any(kw in hook_lower for kw in CRO_SPECIFICS)

    if not has_number and not has_specific:
        issues.append("⚠️ Poco specifico: aggiungi dato numerico o elemento CRO concreto")
        score -= 2

    # ── Second person check ──
    second_person = ["tu", "tuo", "tua", "tuoi", "tue", "ti"]
    has_second = any(w in hook_lower.split() for w in second_person)
    if not has_second:
        issues.append("⚠️ Manca seconda persona ('tu', 'il tuo')")
        score -= 1

    # ── Strong first word ──
    if words:
        first = words[0].lower().rstrip("'")
        strong_starts = [
            "il", "l", "se", "pov", "ho", "la", "un", "lo",
            "nessuno", "quanto", "quand", "stai", "smetti",
            "3", "5", "7", "ogni", "solo", "questo"
        ]
        is_number = first.replace("%", "").replace(".", "").isdigit()
        if not is_number and first not in strong_starts:
            issues.append(f"⚠️ Prima parola '{first}' potrebbe essere più forte")
            score -= 1

    score = max(0, min(10, score))
    has_blockers = any("🚫" in i for i in issues)

    return {
        "hook": hook_text,
        "valid": score >= 7 and not has_blockers,
        "score": score,
        "word_count": word_count,
        "issues": issues,
        "verdict": (
            "✅ Hook approvato"
            if score >= 7 and not has_blockers
            else "⚠️ Hook da rivedere — correggi i problemi"
            if score >= 4 and not has_blockers
            else "🚫 Hook bocciato — riscrivi con una delle 8 formule"
        )
    }


# ═══════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Hook Selector & Validator")
    subparsers = parser.add_subparsers(dest="command")

    # Select command
    sel = subparsers.add_parser("select", help="Select best hooks for context")
    sel.add_argument("--type", required=True, choices=["azione", "educativo", "prova", "trend"])
    sel.add_argument("--topic", default="", help="Video topic")
    sel.add_argument("--has-data", action="store_true", help="Data/statistics available")
    sel.add_argument("--has-case-study", action="store_true", help="Case study available")
    sel.add_argument("--tone", default="diretto", choices=["diretto", "provocatorio", "educativo"])

    # Validate command
    val = subparsers.add_parser("validate", help="Validate a hook text")
    val.add_argument("hook_text", help="Hook text to validate")

    args = parser.parse_args()

    if args.command == "select":
        results = select_hooks(
            tipo_video=args.type,
            argomento=args.topic,
            ha_dati=args.has_data,
            ha_caso_studio=args.has_case_study,
            tono=args.tone
        )
        print("\n🎯 TOP 3 HOOK FORMULAS:\n")
        for i, r in enumerate(results, 1):
            print(f"  {i}. {r['icona']} {r['nome']} (score: {r['score']})")
            print(f"     Template: {r['template']}")
            print(f"     Tensione: {r['tensione_consigliata']['primaria']}")
            print()

    elif args.command == "validate":
        result = validate_hook(args.hook_text)
        print(f"\n{'='*50}")
        print(f"HOOK: \"{result['hook']}\"")
        print(f"Score: {result['score']}/10 | Parole: {result['word_count']}")
        print(f"Verdict: {result['verdict']}")
        if result["issues"]:
            print(f"\nProblemi:")
            for issue in result["issues"]:
                print(f"  {issue}")
        print(f"{'='*50}\n")

        # Return non-zero exit code if invalid
        sys.exit(0 if result["valid"] else 1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()