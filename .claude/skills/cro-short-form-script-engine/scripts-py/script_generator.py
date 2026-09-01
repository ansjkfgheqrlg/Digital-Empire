#!/usr/bin/env python3
"""
Master Script Generator for Short-Form Script Engine.

Assembles a complete script skeleton by orchestrating all modules:
- Hook selection (hook_selector.py)
- Structure calculation (structure_calculator.py)
- Payload structure routing
- CTA selection
- Retention hook placement

Usage:
    python script_generator.py \
        --platform tiktok \
        --type azione \
        --topic "bottone CTA Submit" \
        --duration 30

    python script_generator.py \
        --platform ig_reel \
        --type prova \
        --topic "checkout optimization" \
        --duration 60 \
        --has-case-study \
        --lead-magnet "CRO Checklist 25 punti"
"""

import argparse
import json
import sys

# Import sibling modules
from hook_selector import select_hooks, TENSION_COMPATIBILITY, TENSION_NAMES
from structure_calculator import calculate_structure, PAYLOAD_DISTRIBUTION


# ═══════════════════════════════════════════
# CTA SELECTION
# ═══════════════════════════════════════════

CTA_TEMPLATES = {
    "keyword_comment": {
        "tiktok": 'Commenta "{keyword}" e ti mando la {lead_magnet}.',
        "ig_reel": 'Commenta "{keyword}" → ti mando la {lead_magnet} in DM.',
        "stories": "[Link sticker → {lead_magnet}]"
    },
    "link_in_bio": {
        "tiktok": "Link in bio per la {lead_magnet}.",
        "ig_reel": "Link in bio → {lead_magnet} gratuita.",
        "stories": "[Link sticker: 'Scarica gratis']"
    },
    "follow": {
        "tiktok": "Segui per altri teardown come questo.",
        "ig_reel": "Segui per altri teardown come questo.",
        "stories": "Segui per tip CRO ogni giorno."
    },
    "strategy_call": {
        "tiktok": "Se vuoi che analizzi il TUO funnel, link in bio. 15 minuti, gratis.",
        "ig_reel": "Vuoi un audit del tuo funnel? Link in bio — 15 minuti, gratis.",
        "stories": "Prenota un audit gratuito [Link sticker]"
    },
    "save": {
        "tiktok": "Salva questo video. Ti servirà quando lavori sul tuo funnel.",
        "ig_reel": "Salva questo video. La prossima volta che apri il tuo funnel, ti servirà.",
        "stories": "Screenshot questa story 📸"
    },
    "engagement": {
        "tiktok": "Fammi vedere il tuo checkout nei commenti — ti dico il primo errore che trovo.",
        "ig_reel": "Manda il link della tua landing nei commenti — ti faccio un mini-audit.",
        "stories": "Rispondi a questa story con il link del tuo funnel"
    }
}

# Decision matrix: type × platform → preferred CTA
CTA_DECISION = {
    ("azione",    "tiktok"):   "keyword_comment",
    ("azione",    "ig_reel"):  "keyword_comment",
    ("azione",    "stories"):  "link_in_bio",
    ("educativo", "tiktok"):   "keyword_comment",
    ("educativo", "ig_reel"):  "keyword_comment",
    ("educativo", "stories"):  "link_in_bio",
    ("prova",     "tiktok"):   "keyword_comment",
    ("prova",     "ig_reel"):  "link_in_bio",
    ("prova",     "stories"):  "link_in_bio",
    ("trend",     "tiktok"):   "follow",
    ("trend",     "ig_reel"):  "link_in_bio",
    ("trend",     "stories"):  "link_in_bio"
}


def select_cta(
    platform: str,
    tipo_video: str,
    lead_magnet: str = "CRO Checklist 25 punti",
    keyword: str = "AUDIT"
) -> dict:
    """Select the best CTA for the given context."""

    cta_type = CTA_DECISION.get((tipo_video, platform), "keyword_comment")
    templates = CTA_TEMPLATES.get(cta_type, {})
    template = templates.get(platform, templates.get("tiktok", ""))

    script = template.format(lead_magnet=lead_magnet, keyword=keyword)

    return {
        "tipo": cta_type,
        "script": script,
        "keyword": keyword if cta_type == "keyword_comment" else None,
        "nota": f"CTA '{cta_type}' selezionata per {platform} + {tipo_video}"
    }


# ═══════════════════════════════════════════
# VISUAL SUGGESTIONS
# ═══════════════════════════════════════════

VISUAL_SUGGESTIONS = {
    "azione": "Face-to-camera + screen recording con evidenziazioni (cerchio/freccia)",
    "educativo": "Face-to-camera alternato a screen recording. Numeri a schermo per ogni punto.",
    "prova": "Face-to-camera + grafici/screenshot risultati. Numeri grandi a schermo per il prima/dopo.",
    "trend": "Face-to-camera con espressioni (sarcastiche/sorprese) + screenshot sincronizzati con audio."
}

# ═══════════════════════════════════════════
# CAPTION SKELETON
# ═══════════════════════════════════════════

HASHTAG_POOL = {
    "sempre": ["#CRO", "#DigitalEmpire"],
    "checkout": "#CheckoutOptimization",
    "landing": "#LandingPage",
    "funnel": "#FunnelOptimization",
    "above the fold": "#AboveTheFold",
    "conversion": "#ConversionRate",
    "ecommerce": "#EcommerceTips",
    "e-commerce": "#EcommerceTips",
    "case study": "#CaseStudy",
    "caso studio": "#CaseStudy",
    "errori": "#CROtips",
    "tip": "#CROtips"
}


def suggest_hashtags(topic: str, max_total: int = 5) -> list:
    """Select relevant hashtags based on topic."""
    tags = list(HASHTAG_POOL["sempre"])

    topic_lower = topic.lower()
    for keyword, hashtag in HASHTAG_POOL.items():
        if keyword == "sempre":
            continue
        if keyword in topic_lower and hashtag not in tags:
            tags.append(hashtag)

    # Always include ConversionRate if not already there
    if "#ConversionRate" not in tags:
        tags.append("#ConversionRate")

    return tags[:max_total]


# ═══════════════════════════════════════════
# MASTER GENERATOR
# ═══════════════════════════════════════════

def generate_script_skeleton(
    platform: str,
    tipo_video: str,
    topic: str,
    duration: int = None,
    pilastro: str = None,
    has_data: bool = False,
    has_case_study: bool = False,
    lead_magnet: str = "CRO Checklist 25 punti",
    keyword: str = "AUDIT",
    tone: str = "diretto"
) -> dict:
    """
    Generate a complete script skeleton assembling all modules.

    This provides the structure, timing, hook suggestions, tension pairing,
    payload outline, CTA, and production notes. The actual script text
    needs to be written by the AI or user filling in the skeleton.
    """

    # ── Default duration if not specified ──
    if not duration:
        defaults = {"azione": 30, "educativo": 90, "prova": 60, "trend": 15}
        duration = defaults.get(tipo_video, 60)

    # ── Calculate structure ──
    structure = calculate_structure(duration, tipo_video)

    # ── Select hooks ──
    hooks = select_hooks(
        tipo_video=tipo_video,
        argomento=topic,
        ha_dati=has_data,
        ha_caso_studio=has_case_study,
        tono=tone
    )

    # ── Select CTA ──
    cta = select_cta(platform, tipo_video, lead_magnet, keyword)

    # ── Suggest visual ──
    visual = VISUAL_SUGGESTIONS.get(tipo_video, "Face-to-camera")

    # ── Suggest hashtags ──
    hashtags = suggest_hashtags(topic)

    # ── Retention hooks info ──
    ret = structure.get("retention_hooks", {})

    # ── Assemble skeleton ──
    skeleton = {
        "header": {
            "piattaforma": platform,
            "pilastro": pilastro or "Da specificare",
            "tipo": tipo_video,
            "durata_stimata": f"{duration} secondi",
            "parole_stimate": structure.get("totali", {}).get("parole_stimate", "N/A"),
            "visual": visual,
            "lead_magnet": lead_magnet
        },

        "B1_HOOK": {
            "durata": structure["blocchi"]["B1_HOOK"],
            "formule_suggerite": [
                {
                    "formula": h["nome"],
                    "icona": h["icona"],
                    "template": h["template"],
                    "score": h["score"]
                }
                for h in hooks
            ],
            "tensione_consigliata": hooks[0]["tensione_consigliata"] if hooks else {},
            "istruzioni": (
                f"Scrivi 1 frase hook (max 15 parole) su '{topic}'. "
                f"Usa formula '{hooks[0]['nome'] if hooks else 'F1'}'. "
                f"Prima parola forte. Seconda persona. Specifico."
            )
        },

        "B2_TENSIONE": {
            "durata": structure["blocchi"]["B2_TENSIONE"],
            "tecnica": hooks[0]["tensione_consigliata"]["primaria"] if hooks else "Amplificazione",
            "istruzioni": (
                "Scrivi 2-3 frasi che creano un open loop. "
                "Il viewer deve avere un motivo per NON scrollare."
            ) if tipo_video != "trend" else "N/A — integrata nel trend"
        },

        "B3_PAYLOAD": {
            "durata": structure["blocchi"]["B3_PAYLOAD"],
            "struttura_interna": structure["blocchi"]["B3_PAYLOAD"].get("struttura_interna", []),
            "retention_hooks": {
                "quanti": ret.get("quanti", 0),
                "posizioni": ret.get("posizioni_sec", [])
            },
            "istruzioni": (
                f"Segui la struttura '{tipo_video}' (vedi references/payload_structures.md). "
                f"Argomento: {topic}. UN concetto. Almeno 1 elemento di prova."
            )
        },

        "B4_CTA": {
            "durata": structure["blocchi"]["B4_CTA"],
            "cta_selezionata": cta,
            "istruzioni": "UNA CTA. Ripetila nella caption."
        },

        "caption": {
            "piattaforma": platform,
            "hashtags_suggeriti": hashtags,
            "struttura": (
                "TikTok: Hook → Espansione → CTA → Hashtag"
                if platform == "tiktok"
                else "IG: Prima riga ≤125 char (SECONDO HOOK) → Valore → ⬇️ CTA → Hashtag"
            )
        },

        "output_richiesto": [
            "Script parola per parola con timing e indicazioni visual",
            f"Caption completa ({platform})",
            "3 varianti hook (formule diverse)",
            "Note di produzione (inquadratura, visual, testo a schermo)"
        ],

        "warnings": structure.get("warnings", []),
        "visual_map": structure.get("visual_map", "")
    }

    return skeleton


def format_skeleton(skeleton: dict) -> str:
    """Format skeleton for human-readable display."""
    lines = []
    h = skeleton["header"]

    lines.append("\n" + "═" * 60)
    lines.append(f"  SCRIPT SKELETON — {h['tipo'].upper()}")
    lines.append("═" * 60)

    # Header
    lines.append(f"\n  Piattaforma:  {h['piattaforma']}")
    lines.append(f"  Pilastro:     {h['pilastro']}")
    lines.append(f"  Tipo:         {h['tipo']}")
    lines.append(f"  Durata:       {h['durata_stimata']}")
    lines.append(f"  Parole:       ~{h['parole_stimate']}")
    lines.append(f"  Visual:       {h['visual']}")
    lines.append(f"  Lead Magnet:  {h['lead_magnet']}")

    # Visual map
    if skeleton.get("visual_map"):
        lines.append(f"\n  {skeleton['visual_map']}")

    # Warnings
    for w in skeleton.get("warnings", []):
        lines.append(f"\n  {w}")

    # B1 Hook
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  B1 HOOK ({skeleton['B1_HOOK']['durata']['durata_sec']}s)")
    lines.append(f"  {skeleton['B1_HOOK']['istruzioni']}")
    lines.append(f"  Formule suggerite:")
    for f in skeleton["B1_HOOK"]["formule_suggerite"]:
        lines.append(f"    {f['icona']} {f['formula']} (score {f['score']}): {f['template']}")

    # B2 Tension
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  B2 TENSIONE ({skeleton['B2_TENSIONE']['durata']['durata_sec']}s)")
    lines.append(f"  Tecnica: {skeleton['B2_TENSIONE']['tecnica']}")
    lines.append(f"  {skeleton['B2_TENSIONE']['istruzioni']}")

    # B3 Payload
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  B3 PAYLOAD ({skeleton['B3_PAYLOAD']['durata']['durata_sec']}s)")
    for step in skeleton["B3_PAYLOAD"]["struttura_interna"]:
        lines.append(f"    ├── {step['nome']}: {step['durata_sec']}s (~{step['parole']} parole)")
        lines.append(f"    │   {step['nota']}")
    ret = skeleton["B3_PAYLOAD"]["retention_hooks"]
    if ret["quanti"] > 0:
        pos_str = ", ".join(f"~{p}s" for p in ret["posizioni"])
        lines.append(f"    └── Retention hooks: {ret['quanti']} alle posizioni {pos_str}")

    # B4 CTA
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  B4 CTA ({skeleton['B4_CTA']['durata']['durata_sec']}s)")
    cta = skeleton["B4_CTA"]["cta_selezionata"]
    lines.append(f"  Tipo: {cta['tipo']}")
    lines.append(f"  Script: \"{cta['script']}\"")

    # Caption
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  CAPTION ({skeleton['caption']['piattaforma']})")
    lines.append(f"  Struttura: {skeleton['caption']['struttura']}")
    lines.append(f"  Hashtags: {' '.join(skeleton['caption']['hashtags_suggeriti'])}")

    # Output required
    lines.append(f"\n  {'─' * 56}")
    lines.append(f"  OUTPUT RICHIESTO:")
    for o in skeleton["output_richiesto"]:
        lines.append(f"    ☐ {o}")

    lines.append("\n" + "═" * 60 + "\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Master Script Generator")
    parser.add_argument("--platform", "-p", required=True, choices=["tiktok", "ig_reel", "stories"])
    parser.add_argument("--type", "-t", required=True, choices=["azione", "educativo", "prova", "trend"])
    parser.add_argument("--topic", required=True, help="Video topic")
    parser.add_argument("--duration", "-d", type=int, help="Duration in seconds (auto if not set)")
    parser.add_argument("--pilastro", help="Content pillar")
    parser.add_argument("--has-data", action="store_true", help="Data/statistics available")
    parser.add_argument("--has-case-study", action="store_true", help="Case study available")
    parser.add_argument("--lead-magnet", default="CRO Checklist 25 punti")
    parser.add_argument("--keyword", default="AUDIT", help="CTA keyword for comments")
    parser.add_argument("--tone", default="diretto", choices=["diretto", "provocatorio", "educativo"])
    parser.add_argument("--format", "-f", default="text", choices=["text", "json"])

    args = parser.parse_args()

    skeleton = generate_script_skeleton(
        platform=args.platform,
        tipo_video=args.type,
        topic=args.topic,
        duration=args.duration,
        pilastro=args.pilastro,
        has_data=args.has_data,
        has_case_study=args.has_case_study,
        lead_magnet=args.lead_magnet,
        keyword=args.keyword,
        tone=args.tone
    )

    if args.format == "json":
        print(json.dumps(skeleton, indent=2, ensure_ascii=False))
    else:
        print(format_skeleton(skeleton))


if __name__ == "__main__":
    main()