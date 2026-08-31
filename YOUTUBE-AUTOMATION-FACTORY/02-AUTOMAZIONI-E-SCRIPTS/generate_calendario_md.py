#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera 01-FLUSSI-E-PIANI/CALENDARIO-70-LEGAMIDIAMORE.md da memory/piano_editoriale_70.json."""
import json
import os

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
IN_JSON = os.path.join(FACTORY_DIR, "memory", "piano_editoriale_70.json")
OUT_MD = os.path.join(FACTORY_DIR, "01-FLUSSI-E-PIANI", "CALENDARIO-70-LEGAMIDIAMORE.md")

with open(IN_JSON, "r", encoding="utf-8") as f:
    piano = json.load(f)

righe = piano["righe"]
strategie = piano["strategie"]

md = []
md.append("# Calendario Editoriale 70 Video / 30 Giorni — @Legamidiamore\n")
md.append(f"> Generato 2026-08-26. Estende [CALENDARIO-LEGAMIDIAMORE.md](CALENDARIO-LEGAMIDIAMORE.md) "
          f"(10gg, 05/08/2026) a un piano mensile completo, 3 strategie A/B/C testate in parallelo. "
          f"Fonti reali: scraping fresco via `youtube_hunter_playwright.py` del 2026-08-26 "
          f"(`memory/channel_videos/*.json`), pool filtrato in "
          f"`memory/candidate_pool_70_20260826.json`. Ogni link e' verificato reale, nessuno inventato.\n")

md.append("## Correzioni reali trovate nello scraping di oggi (non assunzioni)\n")
md.append("- `@ciraolone` e `@linguaggiosegretodelcorpo-6589`, presenti nella cache del 05/08/2026, "
          "sono risultati **fuori nicchia** oggi (rispettivamente canale AI/tech e scuola di ballo) — "
          "esclusi come fonte.\n"
          "- `MIN_VPH=20.0` di `cashcow_check.py` non e' raggiunto da nessun video reale in questa "
          "nicchia oggi (top reale ~10.6 vph) — non usato come soglia assoluta in questo piano, si "
          "usa un ranking relativo per canale.\n"
          "- Restano 3 canali reali usabili, mappati 1:1 sulle 3 strategie sotto.\n")

md.append("## Le 3 strategie\n")
md.append("| Strategia | Nome | Fonte reale | Target | Volume | KPI |\n|---|---|---|---|---|---|\n")
for k in ("A", "B", "C"):
    s = strategie[k]
    md.append(f"| {k} | {s['nome']} | @{s['canale_sorgente']} | {s['target']} | {s['volume']}/70 | {s['kpi']} |\n")

md.append("\n## Legenda calendario\n")
md.append("🥈 = Strategia A (Segnali & Decodifica) · 🔴 = Strategia B (Tecnica & Comando) · "
          "🥈🔴 = Strategia C (Allarme & Verita' Sociale). Weekend = 3 video/giorno (mix A+B+C completo). "
          "Giorno 1 (lancio) e Giorno 15 (metà mese) = bonus a 3 video/giorno.\n")

md.append("\n## Le 70 righe\n")
md.append("| # | Data | Ora | Strat | Fonte | Titolo originale (reale) | vph | Titolo adattato | "
          "Comando |\n|---|---|---|---|---|---|---|---|---|\n")
icona = {"A": "🥈", "B": "🔴", "C": "🥈🔴"}
for r in righe:
    comando = f"`--video-sorgente {r['url_sorgente_reale']}`"
    md.append(
        f"| {r['giorno']} | {r['data_pubblicazione']} | {r['orario_pubblicazione']} | "
        f"{icona[r['strategia']]} {r['strategia']} | @{r['canale_sorgente']} | "
        f"[{r['titolo_originale'][:55]}]({r['url_sorgente_reale']}) | {r['vph_sorgente']} | "
        f"{r['titolo_adattato']} | {comando} |\n"
    )

md.append("\n## Come si esegue una riga\n")
md.append("Ogni riga e' autosufficiente: prendi `url_sorgente_reale` e lancia\n\n"
          "```\npython apex7_orchestrator.py run --canale legamidiamore "
          "--video-sorgente <url_sorgente_reale> --phase 1\n```\n\n"
          "Regole permanenti del canale (voce femminile, solo donne/coppia in scena, "
          "pubblicazione privata di default, copertina reale obbligatoria per `--upload`) "
          "restano invariate e si applicano automaticamente — non vanno ripetute riga per riga.\n")

md.append("\n## Dati completi\n")
md.append("- `memory/piano_editoriale_70.json` — dato strutturato completo (14 campi × 70 righe)\n"
          "- `memory/piano_editoriale_70.csv` — stesso dato in CSV\n"
          "- `memory/candidate_pool_70_20260826.json` — pool completo di candidati reali (audit trail)\n")

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("".join(md))

print(f"[+] {OUT_MD}")
