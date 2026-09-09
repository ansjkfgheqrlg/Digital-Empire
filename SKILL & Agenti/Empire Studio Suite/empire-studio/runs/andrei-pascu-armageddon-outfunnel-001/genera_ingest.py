# -*- coding: utf-8 -*-
"""Genera ingest.json per ogni lezione da _scrape_meta.json + classificazione TEORIA/PRATICA."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.join(HERE, "lessons")

# Tutte e 20 confermate TEORIA per lettura integrale del "Riassunto lezione" ufficiale:
# corso di strategia/framework, zero linguaggio da demo schermo/software in nessuna delle 20.
# Verifica durata/frame-campione tentata (yt-dlp) ma bloccata da rate-limit Vimeo dopo la
# raffica di 20 richieste ravvicinate — non riprovata perche' l'evidenza testuale e' gia'
# sufficiente (corso di puro copy/strategia, non un tutorial software come cs2online).
TIPO_MOTIVAZIONE = (
    "Lezione di puro framework/strategia (nessuna dimostrazione UI o software nella "
    "trascrizione ufficiale 'Riassunto lezione', letta integralmente). outFunnel e' un corso "
    "di marketing/copy, non di uso di strumenti: a differenza di cs2online (dove le lezioni "
    "'pratiche' mostravano schermate reali di Claude), qui anche le lezioni con 'esempi reali' "
    "nel titolo (5, 17-20) sono walkthrough testuali/schematici di strutture di funnel, non "
    "screen-recording. Frame-by-frame NON applicato (stessa regola Max 2026-08-27, cs2online)."
)

for n in range(1, 21):
    d = os.path.join(LESSONS, f"lezione-{n:02d}")
    meta = json.load(open(os.path.join(d, "_scrape_meta.json"), encoding="utf-8"))
    ingest = {
        "lesson_number": n,
        "section": meta["section"],
        "title": meta["title"],
        "url": meta["url"],
        "slug": meta["slug"],
        "vimeo_id": meta["vimeo_id"],
        "vimeo_embed": meta["vimeo_embed"],
        "tipo": "TEORIA",
        "tipo_motivazione": TIPO_MOTIVAZIONE,
        "risorse": {
            "trascrizione_ufficiale": "presente in pagina (sezione 'Riassunto lezione'), "
                                        "catturata integralmente in _page_raw.txt",
            "materiali_scaricabili": "nessuno trovato (a differenza di cs2online, outFunnel "
                                       "non ha link Google Drive/PDF per lezione)",
        },
        "data_ingestion": "2026-09-09",
        "pipeline": "Empire Studio Suite - adattamento corso membership (non YouTube), "
                    "stessa famiglia di andrei-pascu-cs2online-001",
    }
    with open(os.path.join(d, "ingest.json"), "w", encoding="utf-8") as f:
        json.dump(ingest, f, ensure_ascii=False, indent=2)

print("[OK] ingest.json scritto per 20 lezioni")
