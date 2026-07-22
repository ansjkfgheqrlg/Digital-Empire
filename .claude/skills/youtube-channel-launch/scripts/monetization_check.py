#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
monetization_check.py — distanza dai requisiti YPP e stima economica di un canale.

Principio: NESSUN numero inventato. Tutti gli input arrivano dall'utente; l'RPM e' dichiarato
come STIMA con intervallo e il risultato lo segnala. Se manca un dato, si dice "dato mancante",
non si mette zero (coerente col Mandato Art.2 di Digital Empire).

Requisiti YPP (verificare sempre i valori correnti su YouTube):
  - 1.000 iscritti
  - 4.000 ore di visualizzazione pubbliche negli ultimi 12 mesi

Insight che il tool rende evidente:
  ORE = view x durata media VISTA (non la durata del video).
  Un format corto ha bisogno di molte piu' view per fare le stesse ore -> la durata del format
  e' una decisione economica.

Uso:
  python monetization_check.py --iscritti 320 --ore 850 --video-mese 12 \
      --view-per-video 1800 --durata-min 10 --retention 0.45 --rpm-min 1.5 --rpm-max 4.0
  python monetization_check.py --json canale.json
"""

import argparse
import json
import sys

YPP_ISCRITTI = 1000
YPP_ORE = 4000


def _num(v, default=None):
    """Converte in float; None/vuoto/non numerico -> default (dato mancante, non zero)."""
    if v is None or v == "":
        return default
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def compute(d: dict) -> dict:
    iscritti = _num(d.get("iscritti"))
    ore = _num(d.get("ore"))
    video_mese = _num(d.get("video_mese"))
    view_per_video = _num(d.get("view_per_video"))
    durata_min = _num(d.get("durata_min"))
    retention = _num(d.get("retention"), 0.4)  # frazione di video effettivamente vista
    rpm_min = _num(d.get("rpm_min"))
    rpm_max = _num(d.get("rpm_max"))

    mancanti = [k for k, v in {
        "iscritti": iscritti, "ore": ore, "video_mese": video_mese,
        "view_per_video": view_per_video, "durata_min": durata_min,
    }.items() if v is None]

    out = {
        "tool": "monetization_check",
        "requisiti_ypp": {"iscritti": YPP_ISCRITTI, "ore": YPP_ORE},
        "dati_mancanti": mancanti,
        "nota": "RPM = stima dichiarata dall'utente, non un dato YouTube. Verificare sui dati reali del canale.",
    }

    if mancanti:
        out["stato"] = "incompleto"
        out["messaggio"] = (
            "Dati mancanti: " + ", ".join(mancanti) +
            ". Non calcolo stime su dati assenti (mai numeri inventati)."
        )
        return out

    out["stato"] = "ok"

    # --- Stato attuale vs requisiti ---
    out["progresso"] = {
        "iscritti": {"attuali": iscritti, "mancanti": max(0, YPP_ISCRITTI - iscritti),
                     "percentuale": round(min(100.0, iscritti / YPP_ISCRITTI * 100), 1)},
        "ore": {"attuali": ore, "mancanti": max(0, YPP_ORE - ore),
                "percentuale": round(min(100.0, ore / YPP_ORE * 100), 1)},
    }

    # --- Produzione mensile: ore generate ---
    # ore = video/mese x view/video x (durata_min x retention) / 60
    durata_vista_min = durata_min * retention
    ore_mese = video_mese * view_per_video * durata_vista_min / 60.0
    view_mese = video_mese * view_per_video

    out["produzione_mensile"] = {
        "video": video_mese,
        "view": round(view_mese),
        "durata_media_vista_min": round(durata_vista_min, 2),
        "ore_generate": round(ore_mese, 1),
    }

    # --- Tempo stimato al traguardo (il collo di bottiglia e' il vincolo piu' lento) ---
    ore_mancanti = max(0, YPP_ORE - ore)
    mesi_ore = (ore_mancanti / ore_mese) if ore_mese > 0 else None

    # Iscritti: stimati come frazione delle view. Senza un tasso dichiarato dall'utente non lo
    # inventiamo: usiamo il tasso dichiarato, altrimenti segnaliamo che non e' stimabile.
    tasso_iscrizione = _num(d.get("tasso_iscrizione"))  # es. 0.005 = 0.5% delle view
    iscritti_mancanti = max(0, YPP_ISCRITTI - iscritti)
    if tasso_iscrizione and tasso_iscrizione > 0:
        iscritti_mese = view_mese * tasso_iscrizione
        mesi_iscritti = (iscritti_mancanti / iscritti_mese) if iscritti_mese > 0 else None
    else:
        iscritti_mese = None
        mesi_iscritti = None

    candidati = [m for m in (mesi_ore, mesi_iscritti) if m is not None]
    mesi_totali = max(candidati) if candidati else None

    if mesi_ore is not None and mesi_iscritti is not None:
        collo = "ore" if mesi_ore >= mesi_iscritti else "iscritti"
    elif mesi_ore is not None:
        collo = "ore (iscritti non stimabili: manca --tasso-iscrizione)"
    else:
        collo = "non determinabile"

    out["tempo_stimato"] = {
        "mesi_per_ore": round(mesi_ore, 1) if mesi_ore is not None else None,
        "mesi_per_iscritti": round(mesi_iscritti, 1) if mesi_iscritti is not None else None,
        "iscritti_stimati_mese": round(iscritti_mese) if iscritti_mese is not None else None,
        "mesi_al_traguardo": round(mesi_totali, 1) if mesi_totali is not None else None,
        "collo_di_bottiglia": collo,
    }

    # --- Stima ricavi (solo se l'utente ha dichiarato un intervallo RPM) ---
    if rpm_min is not None and rpm_max is not None:
        out["ricavi_stimati_mese"] = {
            "rpm_dichiarato": {"min": rpm_min, "max": rpm_max},
            "min_eur": round(view_mese / 1000.0 * rpm_min, 2),
            "max_eur": round(view_mese / 1000.0 * rpm_max, 2),
            "avviso": "Stima su RPM dichiarato dall'utente. Il valore reale si legge in YouTube Studio.",
        }
        costi = _num(d.get("costi_mese"))
        if costi is not None:
            out["ricavi_stimati_mese"]["costi_mese_eur"] = costi
            out["ricavi_stimati_mese"]["break_even"] = (
                "coperti" if view_mese / 1000.0 * rpm_min >= costi else "NON coperti nello scenario pessimista"
            )
    else:
        out["ricavi_stimati_mese"] = {"stato": "non calcolato", "motivo": "RPM non dichiarato (--rpm-min/--rpm-max)"}

    # --- Leva consigliata: l'insight sulla durata ---
    consigli = []
    if mesi_ore is not None and mesi_ore > 12:
        consigli.append(
            f"Alle ore attuali servono ~{mesi_ore:.0f} mesi. Le ore sono il vincolo: allungare il "
            f"format (ora {durata_min:g} min, visti {durata_vista_min:.1f}) o aumentare la cadenza."
        )
    if retention < 0.35:
        consigli.append(
            f"Retention {retention:.0%}: bassa. Le ore dipendono piu' dalla retention che dalle view: "
            "lavorare su hook e ritmo prima di aumentare la produzione."
        )
    if durata_min < 8:
        consigli.append(
            f"Format da {durata_min:g} min: per fare 4.000 ore servono molte piu' view di un format "
            "da 10-12 min. La durata e' una decisione economica."
        )
    out["consigli"] = consigli

    out["idoneo_ypp"] = bool(iscritti >= YPP_ISCRITTI and ore >= YPP_ORE)
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Progresso YPP e stima economica di un canale YouTube.")
    p.add_argument("--json", help="file JSON con i dati del canale")
    p.add_argument("--iscritti")
    p.add_argument("--ore", help="ore di visualizzazione ultimi 12 mesi")
    p.add_argument("--video-mese", dest="video_mese")
    p.add_argument("--view-per-video", dest="view_per_video")
    p.add_argument("--durata-min", dest="durata_min", help="durata media del video in minuti")
    p.add_argument("--retention", help="frazione vista, es. 0.45 (default 0.4)")
    p.add_argument("--tasso-iscrizione", dest="tasso_iscrizione", help="es. 0.005 = 0.5%% delle view")
    p.add_argument("--rpm-min", dest="rpm_min")
    p.add_argument("--rpm-max", dest="rpm_max")
    p.add_argument("--costi-mese", dest="costi_mese")
    args = p.parse_args()

    if args.json:
        with open(args.json, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {k: v for k, v in vars(args).items() if k != "json"}

    print(json.dumps(compute(data), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
