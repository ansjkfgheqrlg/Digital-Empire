#!/usr/bin/env python3
"""
Reparto COPY — agente `copy-researcher`.

Studia i titoli REALI di @dosementale e misura quali schemi di copy si accompagnano a una
velocity piu' alta. Scrive lo studio nel second brain (regola WIKI-FIRST del progetto), da
cui `capo-copy`, `script-writer`, `title-writer` e `thumbnail-copywriter` attingono.

Metodo, e i suoi limiti dichiarati:
- si confronta la velocity MEDIANA dei video CHE HANNO uno schema contro quelli che NON ce
  l'hanno. Guardare solo "i titoli vincenti hanno le maiuscole" non dice niente se ce l'hanno
  tutti: serve il confronto.
- la mediana, non la media: un solo virale sposterebbe la media e farebbe sembrare vincente
  uno schema che non lo e'.
- views ed eta' sono dati PUBBLICI. CTR e retention no (servono le analytics del proprietario):
  qui non compaiono e non vanno stimati.

Uso:
    python copy_study_dosementale.py
    python copy_study_dosementale.py --handle @altrocanale --min-campione 4
"""
import os
import re
import sys
import json
import argparse
import statistics
from datetime import date, datetime

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
EMPIRE_DIR = os.path.abspath(os.path.join(FACTORY_DIR, ".."))
CACHE_DIR = os.path.join(FACTORY_DIR, "memory", "channel_videos")
WIKI_SYNTHESIS = os.path.join(EMPIRE_DIR, "second-brain-vault", "wiki", "synthesis")
WIKI_LOG = os.path.join(EMPIRE_DIR, "second-brain-vault", "wiki", "log.md")
# Fino al 2026-08-05 questo studio finiva SOLO sulla wiki (Markdown, letto da un umano se e
# quando capitava): apex7_orchestrator.py non lo consumava mai in una run automatica. Questo
# file JSON e' il ponte. Va tenuto SEPARATO da memory/learned_rules.json apposta: quel file
# viene riscritto per intero da self_improve.py ad ogni Fase 6 (anche vuoto, se non ci sono
# ancora log di performance reali) — se ci scrivessimo qui dentro, il prossimo F6 lo
# cancellerebbe. learned_rules.json = performance reali post-pubblicazione (oggi vuoto, nessun
# video pubblicato). copy_intelligence.json = pattern del competitor, disponibili SUBITO senza
# aspettare un video pubblicato: due fonti distinte, stesso punto di consumo in F5.
COPY_INTELLIGENCE_PATH = os.path.join(FACTORY_DIR, "memory", "copy_intelligence.json")


# Ogni schema e' (nome, descrizione, test). Il test dice solo se il titolo CONTIENE lo schema:
# se sia vincente lo decidono i numeri, piu' sotto.
SCHEMI = [
    ("interpellazione_diretta", "Parla direttamente allo spettatore (hai / tu / ti / tuo)",
     lambda t: bool(re.search(r"\b(hai|tu|ti|tuo|tua|tuoi|sei)\b", t, re.I))),
    ("numero_secco", "Promette un numero preciso di cose ('le 2 parole', '3 azioni')",
     lambda t: bool(re.search(r"\b\d+\b", t))),
    ("comando_maiuscolo", "Un verbo imperativo tutto maiuscolo (SMETTI, STOP, ECCO)",
     lambda t: bool(re.search(r"\b[A-ZÀ-Ù]{4,}\b", t))),
    ("domanda", "Il titolo pone una domanda", lambda t: "?" in t),
    ("parentesi", "Aggiunge una precisazione fra parentesi", lambda t: "(" in t),
    ("allarme", "Segnale di allerta o urgenza (ALLARME, ATTENZIONE, 99%)",
     lambda t: bool(re.search(r"allarme|attenzione|pericol|mai|nessuno|99%", t, re.I))),
    ("rivelazione", "Promette di svelare qualcosa di nascosto",
     lambda t: bool(re.search(r"svela|smaschera|scopri|rivela|verità|segreto|davvero|veramente", t, re.I))),
    ("religioso", "Riferimento spirituale o biblico",
     lambda t: bool(re.search(r"\bdio\b|biblic|preghi|spirit|anima|buddis", t, re.I))),
    ("relazioni", "Tema relazioni/famiglia",
     lambda t: bool(re.search(r"famili|parent|amic|persone|relazion|famiglia", t, re.I))),
    ("salute_eta", "Tema salute o età",
     lambda t: bool(re.search(r"\banni\b|salute|corpo|camminare|dormi|bere|vivr", t, re.I))),
]


def carica_video(handle: str) -> list[dict]:
    percorso = os.path.join(CACHE_DIR, re.sub(r"[^a-zA-Z0-9_-]", "_", handle.lstrip("@")) + ".json")
    if not os.path.exists(percorso):
        raise SystemExit(f"[!] Nessun dato reale per {handle} in {percorso}.\n"
                         f"    Lancia prima: python youtube_hunter_playwright.py --handle {handle}")
    dati = json.load(open(percorso, encoding="utf-8"))
    video = [v for v in dati["videos"] if v.get("views") and v.get("age_hours")]
    for v in video:
        v["vph"] = v["views"] / max(v["age_hours"], 1.0)
    return video


def analizza(video: list[dict], min_campione: int) -> list[dict]:
    """Per ogni schema: velocity mediana di chi ce l'ha vs chi non ce l'ha."""
    risultati = []
    for nome, descrizione, test in SCHEMI:
        con = [v["vph"] for v in video if test(v["title"])]
        senza = [v["vph"] for v in video if not test(v["title"])]
        if len(con) < min_campione or len(senza) < min_campione:
            risultati.append({"schema": nome, "descrizione": descrizione, "n_con": len(con),
                              "n_senza": len(senza), "verdetto": "campione insufficiente"})
            continue
        med_con, med_senza = statistics.median(con), statistics.median(senza)
        delta = (med_con / med_senza - 1) * 100 if med_senza else 0.0
        risultati.append({
            "schema": nome, "descrizione": descrizione,
            "n_con": len(con), "n_senza": len(senza),
            "mediana_con": round(med_con, 2), "mediana_senza": round(med_senza, 2),
            "delta_pct": round(delta, 1),
            "verdetto": "favorevole" if delta > 20 else ("sfavorevole" if delta < -20 else "neutro"),
        })
    return sorted(risultati, key=lambda r: -(r.get("delta_pct") or -999))


def scrivi_studio(handle: str, video: list[dict], risultati: list[dict], percorso: str):
    mediana = statistics.median([v["vph"] for v in video])
    top = sorted(video, key=lambda v: -v["vph"])[:8]
    forti = [r for r in risultati if r.get("verdetto") == "favorevole"]
    deboli = [r for r in risultati if r.get("verdetto") == "sfavorevole"]

    with open(percorso, "w", encoding="utf-8") as f:
        f.write("---\nType: SYNTHESIS\nStatus: Active\n"
                "Tags: #youtube #copy #dosementale #ricerca\n"
                f"Created: {date.today()}\nLast updated: {date.today()}\n---\n\n")
        f.write(f"# Studio Copy — {handle}\n\n## Overview\n")
        f.write(f"Analisi degli schemi di copy nei titoli reali di `{handle}` ({len(video)} video), "
                f"misurati sulla velocity (views/ora). Serve al reparto COPY della "
                f"[[Youtube_Automation_Factory]] per scrivere titoli e hook che seguano schemi "
                f"gia' validati sul campo invece che intuizioni.\n\n")
        f.write(f"**Velocity mediana del canale: {mediana:.2f} views/ora.**\n\n")

        f.write("## ⚠️ Come leggere questi numeri\n")
        f.write("- Il confronto e' fra la velocity **mediana** dei video che hanno uno schema e "
                "quella dei video che non ce l'hanno. Uno schema presente in tutti i titoli non "
                "discrimina nulla, per quanto ricorrente sia.\n")
        f.write("- Mediana e non media: un singolo virale sposterebbe la media e farebbe sembrare "
                "vincente uno schema qualsiasi.\n")
        f.write("- **Views ed eta' sono dati pubblici. CTR e retention no** (richiedono le "
                "analytics del proprietario): qui non compaiono e non vanno stimati.\n")
        f.write(f"- Campione piccolo ({len(video)} video): questi sono **indizi**, non leggi.\n\n")

        f.write("## Schemi misurati\n\n")
        f.write("| Schema | Con | Senza | Mediana con | Mediana senza | Δ | Verdetto |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for r in risultati:
            if r["verdetto"] == "campione insufficiente":
                f.write(f"| `{r['schema']}` | {r['n_con']} | {r['n_senza']} | — | — | — | campione insufficiente |\n")
            else:
                f.write(f"| `{r['schema']}` | {r['n_con']} | {r['n_senza']} | {r['mediana_con']} | "
                        f"{r['mediana_senza']} | {r['delta_pct']:+.1f}% | **{r['verdetto']}** |\n")
        f.write("\n")

        if forti:
            f.write("## Schemi da usare\n")
            for r in forti:
                f.write(f"- **{r['schema']}** ({r['delta_pct']:+.1f}%, su {r['n_con']} video) — {r['descrizione']}\n")
            f.write("\n")
        if deboli:
            f.write("## Schemi da evitare\n")
            for r in deboli:
                f.write(f"- **{r['schema']}** ({r['delta_pct']:+.1f}%, su {r['n_con']} video) — {r['descrizione']}\n")
            f.write("\n")

        f.write("## Titoli reali piu' performanti\n\n")
        for v in top:
            f.write(f"- `{v['vph']:.1f}` views/ora · {int(v['views']):,} viste — \"{v['title']}\"\n".replace(",", "."))

        f.write("\n## Connessioni\n")
        f.write("- [[Youtube_Automation_Factory]] — la fabbrica che consuma questo studio\n")
        f.write("- [[Digital_Empire_6_Phase_Process]] — il metodo di cui fa parte\n")
        f.write("- `YOUTUBE-AUTOMATION-FACTORY/03-AGENTI-E-RUOLI/operatori/copy-researcher.md` — l'agente che lo mantiene\n")


def scrivi_copy_intelligence(handle: str, n_video: int, risultati: list[dict], percorso: str):
    """Stessi risultati dello studio wiki, in JSON strutturato per il consumo automatico da
    parte di apex7_orchestrator.py (tag F5, brief F3) — vedi nota su COPY_INTELLIGENCE_PATH sul
    perche' non e' semplicemente learned_rules.json."""
    dati = {
        "handle": handle,
        "generato": datetime.now().isoformat(),
        "n_video_campione": n_video,
        "schemi_favorevoli": [
            {"schema": r["schema"], "descrizione": r["descrizione"], "delta_pct": r["delta_pct"]}
            for r in risultati if r.get("verdetto") == "favorevole"
        ],
        "schemi_sfavorevoli": [
            {"schema": r["schema"], "descrizione": r["descrizione"], "delta_pct": r["delta_pct"]}
            for r in risultati if r.get("verdetto") == "sfavorevole"
        ],
    }
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def aggiorna_log_wiki(n_video: int):
    riga = (f"\n## {date.today()}\n"
            f"- INGEST: studio copy @dosementale rigenerato su {n_video} video reali "
            f"→ 1 pagina aggiornata (synthesis/Studio_Copy_Dose_Mentale.md)\n")
    with open(WIKI_LOG, "a", encoding="utf-8") as f:
        f.write(riga)


def main():
    ap = argparse.ArgumentParser(description="Studio dei copy reali di un canale YouTube.")
    ap.add_argument("--handle", default="@dosementale")
    ap.add_argument("--min-campione", type=int, default=3,
                    help="Sotto questa numerosita' uno schema non viene giudicato.")
    args = ap.parse_args()

    video = carica_video(args.handle)
    risultati = analizza(video, args.min_campione)

    os.makedirs(WIKI_SYNTHESIS, exist_ok=True)
    percorso = os.path.join(WIKI_SYNTHESIS, "Studio_Copy_Dose_Mentale.md")
    scrivi_studio(args.handle, video, risultati, percorso)
    if os.path.exists(WIKI_LOG):
        aggiorna_log_wiki(len(video))
    scrivi_copy_intelligence(args.handle, len(video), risultati, COPY_INTELLIGENCE_PATH)

    print(f"[+] Studio scritto su {len(video)} video reali → {percorso}")
    print(f"[+] Copy intelligence per la fabbrica → {COPY_INTELLIGENCE_PATH}\n")
    for r in risultati:
        if r["verdetto"] == "campione insufficiente":
            print(f"    {r['schema']:24} campione insufficiente ({r['n_con']}/{r['n_senza']})")
        else:
            print(f"    {r['schema']:24} {r['delta_pct']:+7.1f}%  {r['verdetto']}")


if __name__ == "__main__":
    main()
