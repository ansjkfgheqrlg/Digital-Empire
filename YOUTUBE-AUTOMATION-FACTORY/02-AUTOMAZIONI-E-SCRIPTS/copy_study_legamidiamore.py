#!/usr/bin/env python3
"""
Reparto COPY — studio copy per @Legamidiamore (nicchia psicologia femminile/maschile,
segnali di attrazione). Stesso metodo di copy_study_dosementale.py (mediana con/senza schema,
non media — vedi quel file per i limiti dichiarati del metodo), SCHEMI diversi perche' la
nicchia e' diversa: qui non ha senso "salute_eta"/"religioso", ha senso "segnali"/"genere".

Aggrega PIU' canali reali (Legami d'Amore stesso + i competitor trovati da
channel_discovery.py il 2026-08-05), non un solo canale: con un campione piccolo per singolo
canale (es. @codicedonna, 3 video) il segnale sarebbe troppo debole da solo.

Uso:
    python copy_study_legamidiamore.py
    python copy_study_legamidiamore.py --handle @Legamidiamore --handle @altro
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
# Namespace SEPARATO da copy_intelligence.json di Dose Mentale: due canali, due fonti di
# intelligence, stesso motivo per cui learned_rules.json non viene toccato (vedi
# copy_study_dosementale.py) — non si mischiano dati di canali/nicchie diverse nello stesso file.
COPY_INTELLIGENCE_PATH = os.path.join(FACTORY_DIR, "memory", "copy_intelligence_legamidiamore.json")

# Canali di default: Legami d'Amore stesso + i 4 competitor reali on-topic trovati il
# 2026-08-05 (escluso @linguaggiosegretodelcorpo-6589: verificato al momento dello scrape che
# e' una scuola di ballo, non psicologia/attrazione — falso positivo della ricerca testuale,
# scartato a vista sui titoli reali, non incluso "perche' l'aveva trovato channel_discovery").
CANALI_DEFAULT = [
    "@Legamidiamore", "@PsicologiadellAttrazionee", "@PsicologiaFemminile-f8c",
    "@DinamicheSocialiAcademy", "@codicedonna",
]

# Schemi TEMATICI/STILISTICI di questa nicchia specifica, misurati sui titoli reali raccolti
# oggi. Gli schemi di stile generici (numero_secco, domanda, comando_maiuscolo,
# interpellazione_diretta, parentesi, rivelazione, allarme) sono identici a
# copy_study_dosementale.py — sono pattern di copywriting italiano, non legati al tema. Nuovi
# qui: segnali_espliciti e genere_esplicito, i due piu' ricorrenti nei titoli reali visti oggi
# ("5 Segnali Che piaci ad una DONNA...", "7 segnali che sei un uomo...").
SCHEMI = [
    ("segnali_espliciti", "La parola 'segnal-'/'segn-' nel titolo (il framing dominante della nicchia)",
     lambda t: bool(re.search(r"\bsegnal\w*|\bsegn[oi]\b", t, re.I))),
    ("genere_esplicito", "Nomina esplicitamente donna/uomo/donne/uomini",
     lambda t: bool(re.search(r"\bdonn[ae]|\buomini|\buomo\b", t, re.I))),
    ("interpellazione_diretta", "Parla direttamente allo spettatore (hai / tu / ti / tuo / sei)",
     lambda t: bool(re.search(r"\b(hai|tu|ti|tuo|tua|tuoi|sei|te)\b", t, re.I))),
    ("numero_secco", "Promette un numero preciso di cose ('7 segnali', '3 test')",
     lambda t: bool(re.search(r"\b\d+\b", t))),
    ("comando_maiuscolo", "Un verbo o termine tutto maiuscolo",
     lambda t: bool(re.search(r"\b[A-ZÀ-Ù]{4,}\b", t))),
    ("domanda", "Il titolo pone una domanda", lambda t: "?" in t),
    ("parentesi", "Aggiunge una precisazione fra parentesi", lambda t: "(" in t),
    ("rivelazione", "Promette di svelare qualcosa di nascosto (segreto, verita', nessuno te lo dira')",
     lambda t: bool(re.search(r"svela|smaschera|scopri|rivela|verità|segret[oi]|nessuno te lo dir|non te lo dir", t, re.I))),
    ("allarme_negativo", "Paura/minaccia/perdita (distrugge, blocca, single, sbagli)",
     lambda t: bool(re.search(r"distrugge|blocca|single|sbagli|paura|falso mito|attenzione", t, re.I))),
]


def carica_video(handles: list[str]) -> list[dict]:
    tutti = []
    for handle in handles:
        percorso = os.path.join(CACHE_DIR, re.sub(r"[^a-zA-Z0-9_-]", "_", handle.lstrip("@")) + ".json")
        if not os.path.exists(percorso):
            print(f"[!] Nessuna cache per {handle} in {percorso}, saltato "
                 f"(lancia prima: python youtube_hunter_playwright.py --handle {handle})")
            continue
        dati = json.load(open(percorso, encoding="utf-8"))
        video = [v for v in dati["videos"] if v.get("views") and v.get("age_hours")]
        for v in video:
            v["vph"] = v["views"] / max(v["age_hours"], 1.0)
            v["canale"] = handle
        tutti.extend(video)
        print(f"[+] {handle}: {len(video)} video reali caricati.")
    return tutti


def analizza(video: list[dict], min_campione: int) -> list[dict]:
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


def scrivi_studio(handles: list[str], video: list[dict], risultati: list[dict], percorso: str):
    mediana = statistics.median([v["vph"] for v in video])
    top = sorted(video, key=lambda v: -v["vph"])[:10]
    forti = [r for r in risultati if r.get("verdetto") == "favorevole"]
    deboli = [r for r in risultati if r.get("verdetto") == "sfavorevole"]

    with open(percorso, "w", encoding="utf-8") as f:
        f.write("---\nType: SYNTHESIS\nStatus: Active\n"
                "Tags: #youtube #copy #legamidiamore #ricerca #psicologia-attrazione\n"
                f"Created: {date.today()}\nLast updated: {date.today()}\n---\n\n")
        f.write(f"# Studio Copy — @Legamidiamore + competitor reali\n\n## Overview\n")
        f.write(f"Analisi degli schemi di copy su {len(video)} video reali aggregati da "
                f"{len(handles)} canali ({', '.join(handles)}), nicchia psicologia "
                f"femminile/maschile e segnali di attrazione. Serve alla produzione per "
                f"@Legamidiamore per scrivere titoli/hook su schemi gia' validati sul campo.\n\n")
        f.write(f"**Velocity mediana aggregata: {mediana:.2f} views/ora.** "
                f"(campione misto multi-canale: non e' un indice di un singolo canale)\n\n")

        f.write("## ⚠️ Come leggere questi numeri\n")
        f.write("- Stesso metodo di `copy_study_dosementale.py`: mediana con/senza schema, non "
                "media (un virale non deve falsare il verdetto).\n")
        f.write("- Campione MISTO fra canali diversi: la velocity assoluta di ogni canale "
                "dipende anche da iscritti/eta' del canale, non solo dal titolo — il segnale "
                "va letto come indizio di schema, non confronto diretto fra canali.\n")
        f.write("- Views ed eta' sono dati pubblici. CTR e retention no: non compaiono.\n\n")

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

        f.write("## Titoli reali piu' performanti (multi-canale)\n\n")
        for v in top:
            f.write(f"- `{v['vph']:.1f}` views/ora · {int(v['views']):,} viste · {v['canale']} — \"{v['title']}\"\n".replace(",", "."))

        f.write("\n## Connessioni\n")
        f.write("- [[Entity_Legami_dAmore_Channel]] — il canale che consuma questo studio\n")
        f.write("- [[Studio_Copy_Dose_Mentale]] — stesso metodo, altra nicchia\n")
        f.write("- `company/Memory/checkpoints/CP-20260805-009.md` — contesto del pivot\n")


def scrivi_copy_intelligence(handles: list[str], n_video: int, risultati: list[dict], percorso: str):
    dati = {
        "handles": handles,
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


def aggiorna_log_wiki(n_video: int, n_canali: int):
    riga = (f"\n## {date.today()}\n"
            f"- INGEST: studio copy @Legamidiamore + {n_canali - 1} competitor rigenerato su "
            f"{n_video} video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Legamidiamore.md)\n")
    with open(WIKI_LOG, "a", encoding="utf-8") as f:
        f.write(riga)


def main():
    ap = argparse.ArgumentParser(description="Studio dei copy reali per la nicchia di @Legamidiamore.")
    ap.add_argument("--handle", action="append", help="Ripetibile. Default: canale + competitor reali del 2026-08-05.")
    ap.add_argument("--min-campione", type=int, default=4)
    args = ap.parse_args()
    handles = args.handle or CANALI_DEFAULT

    video = carica_video(handles)
    if not video:
        raise SystemExit("[!] Nessun video reale trovato in cache per nessuno dei canali richiesti.")
    risultati = analizza(video, args.min_campione)

    os.makedirs(WIKI_SYNTHESIS, exist_ok=True)
    percorso = os.path.join(WIKI_SYNTHESIS, "Studio_Copy_Legamidiamore.md")
    scrivi_studio(handles, video, risultati, percorso)
    if os.path.exists(WIKI_LOG):
        aggiorna_log_wiki(len(video), len(handles))
    scrivi_copy_intelligence(handles, len(video), risultati, COPY_INTELLIGENCE_PATH)

    print(f"\n[+] Studio scritto su {len(video)} video reali ({len(handles)} canali) → {percorso}")
    print(f"[+] Copy intelligence → {COPY_INTELLIGENCE_PATH}\n")
    for r in risultati:
        if r["verdetto"] == "campione insufficiente":
            print(f"    {r['schema']:24} campione insufficiente ({r['n_con']}/{r['n_senza']})")
        else:
            print(f"    {r['schema']:24} {r['delta_pct']:+7.1f}%  {r['verdetto']}")


if __name__ == "__main__":
    main()
