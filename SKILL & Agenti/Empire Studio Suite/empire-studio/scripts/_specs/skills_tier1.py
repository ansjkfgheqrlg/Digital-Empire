# -*- coding: utf-8 -*-
"""Skill Tier-1 (di reparto): orchestrano le skill funzionali del proprio reparto."""

T = "tier1-department"


def pipe(name, dept_label, does, agents, scripts, trace, tagline):
    return {
        "name": name, "tier": T,
        "description": f"Skill di reparto che orchestra la pipeline {dept_label}: coordina le "
                       f"skill tier2 funzionali del reparto e applica il Strategy Manifest.",
        "tagline": tagline,
        "does": does,
        "usage": ["(invocata dal department-lead; coordina le skill tier2 del reparto)"],
        "uses_scripts": scripts,
        "controls": ["skill tier2 del reparto"],
        "agents": agents,
        "trace": trace,
    }


SKILLS = [
    pipe("youtube-pipeline-skill", "YouTube (ingest -> frame -> visione)",
         ["Coordina yt-ingest + frame-extractor + video-vision per i video YouTube.",
          "Applica la strategia YouTube (frame per capitolo, visione densa per long-form).",
          "Consegna le run analizzate al reparto Forge & Wiki."],
         ["youtube-department/department-lead"],
         ["../tier2-functional/yt-ingest-skill", "../tier2-functional/frame-extractor-skill"],
         "orchestra il reparto YouTube.", "La catena completa del reparto YouTube."),
    pipe("tiktok-pipeline-skill", "TikTok (video brevi, frame densi)",
         ["Coordina tiktok-ingest + frame-extractor (densi) + video-vision.",
          "Applica la strategia TikTok (frame ogni pochi secondi, quick-reference).",
          "Consegna le run analizzate al Forge."],
         ["tiktok-department/department-lead"],
         ["../tier2-functional/yt-ingest-skill", "../tier2-functional/frame-extractor-skill"],
         "orchestra il reparto TikTok.", "La catena del reparto TikTok (video brevi)."),
    pipe("web-pipeline-skill", "Web (ricerca + crawl + estrazione)",
         ["Coordina web-research (Playwright) + estrazione contenuto + screenshot.",
          "Applica la strategia Web (stile reference/MOC, screenshot sezioni chiave).",
          "Consegna il materiale testuale + screenshot al Forge."],
         ["web-department/department-lead"],
         ["../tier2-functional/web-research-skill"],
         "orchestra il reparto Web.", "La catena del reparto Web (ricerca e crawl)."),
    pipe("projects-study-skill", "Projects/Repos (deep study read-only)",
         ["Coordina repo-study (scan read-only) + deep analysis + estrazione atomi.",
          "Garantisce la regola di sola lettura (mai modifica l'originale).",
          "Consegna deep-analysis + atomi tracciati al Forge."],
         ["projects-repos-workloads-department/department-lead"],
         ["../tier2-functional/repo-study-skill", "../tier2-functional/update-proposer-skill"],
         "orchestra il 4o reparto (deep study).", "La catena del deep study di progetti/repo."),
    pipe("processing-pipeline-skill", "Processing & Vision (frame + visione + atomi)",
         ["Coordina frame-extractor + video-vision + transcript-clean + knowledge-extractor.",
          "Mette la visione reale di Claude al centro dell'analisi.",
          "Consegna analysis + atoms.json (tracciati) al Forge."],
         ["processing-vision-department/department-lead", "processing-vision-department/video-watcher"],
         ["../tier2-functional/video-vision-skill", "../tier2-functional/frame-extractor-skill",
          "../tier2-functional/transcript-clean-skill"],
         "orchestra il reparto Processing & Vision.", "La catena della visione e dell'analisi."),
    pipe("forge-wiki-skill", "Forge & Wiki (forge -> wiki -> update proposals)",
         ["Coordina content-forge-bridge + content-forge (/forge) + wiki-writer + cli-doc.",
          "Applica lo stile wiki del Strategy Manifest.",
          "Produce note wiki + REPORT + update proposals."],
         ["forge-wiki-department/department-lead"],
         ["../tier2-functional/content-forge-bridge-skill", "../tier2-functional/wiki-writer-skill",
          "../tier2-functional/cli-doc-skill", "../tier2-functional/update-proposer-skill"],
         "orchestra il reparto Forge & Wiki.", "La catena finale verso la wiki."),
]
