#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
misura_vsl.py — FASE 1 dello studio EMP-DIOEDIT (VSL di Andrei Pascu).

REGOLA MADRE: la macchina misura, l'occhio giudica.
Questo script NON interpreta niente. Produce numeri con timestamp e, per ogni
numero, il comando esatto con cui e' stato ottenuto.

Cosa produce, per ogni video sorgente:

    misure/<slug>/tecnica.json     ffprobe: durata, fps reale, risoluzione,
                                   bitrate, codec, numero di frame
    misure/<slug>/stacchi.json     tutti i tagli di montaggio al centesimo,
    misure/<slug>/stacchi.md       durata di ogni inquadratura, statistiche di
                                   ritmo, profilo minuto per minuto, tabella di
                                   sensibilita' alla soglia
    misure/<slug>/audio.json       loudness EBU R128 (M/S/I/LRA), true peak,
    misure/<slug>/audio.md         silenzi (due configurazioni), profilo del
                                   volume a finestre da 0,5 s (RMS, picco,
                                   zero-crossing rate), cambi di regime
    misure/<slug>/frames/          frame ogni 2 s (frame-NNN.png) + manifest.json
                                   con la riduzione ai soli frame in cui lo
                                   schermo cambia davvero
    misure/<slug>/frames/stacchi/  il primo fotogramma di ogni inquadratura
    misure/<slug>/_SOMMARIO.md     una pagina di soli numeri, con i comandi

Uso:
    python scripts/misura_vsl.py --slug armageddon-home
    python scripts/misura_vsl.py --tutti
    python scripts/misura_vsl.py --tutti --forza
    python scripts/misura_vsl.py --slug armageddon-home --soglia-scena 0.055

Idempotente: se le misure di un video esistono e sono complete con gli stessi
parametri, non le rifa'. Con --forza le rifa' comunque.

Console Windows cp1252: nessuna emoji, nessun carattere fuori ASCII in stampa.

Dipendenze: ffmpeg + ffprobe nel PATH, Pillow.
"""

import argparse
import json
import math
import os
import re
import shutil
import statistics
import struct
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ----------------------------------------------------------------------------
# Percorsi
# ----------------------------------------------------------------------------
RADICE = Path(__file__).resolve().parent.parent          # .../vsl-study
SORGENTI = RADICE / "sorgenti"
MISURE = RADICE / "misure"

# scene_detector.py di Empire Studio: si riusa, non si reinventa.
SCENE_DETECTOR = (
    RADICE.parents[2]
    / "SKILL & Agenti"
    / "Empire Studio Suite"
    / "empire-studio"
    / "scripts"
    / "scene_detector.py"
)

VERSIONE = "1.0.0"

# ----------------------------------------------------------------------------
# Parametri di misura (i default sono CALIBRATI, vedi PARAMETRI_MOTIVAZIONE)
# ----------------------------------------------------------------------------
SOGLIA_SCENA = 0.040        # ffmpeg scene score su luma ridotta a 320 px
SOGLIE_CONFRONTO = [0.028, 0.040, 0.055, 0.100]
FINESTRA_FUSIONE = 0.20     # s: due frame sopra soglia entro questo intervallo = un taglio solo
SCENA_LARGHEZZA = 320       # px: larghezza a cui si calcola lo scene score
CANDIDATO_MIN = 0.020       # si salvano su disco tutti i frame con score >= questo

SILENZIO_A = ("-40dB", 0.30)   # silenzio assoluto
SILENZIO_B = ("-30dB", 0.25)   # pausa del parlato

FINESTRA_AUDIO = 0.5        # s: passo del profilo di volume
PCM_HZ = 16000              # frequenza a cui si legge il PCM per il profilo
REGIME_SALTO_DB = 6.0       # dB: salto di RMS mediano fra blocchi che segna un cambio
REGIME_BLOCCO = 5.0         # s: durata del blocco su cui si calcola la mediana

PASSO_FRAME = 2.0           # s fra un frame denso e il successivo
LARGHEZZA_FRAME = 960       # px
DEDUP_SOGLIA = 3.0          # differenza percettiva 0-100 (metodo scene_detector.py)
DEDUP_MAX_GAP = 30.0        # s: presidio, un frame ogni N secondi comunque

PARAMETRI_MOTIVAZIONE = {
    "soglia_scena": (
        "0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. "
        "Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma "
        "prima e dopo un campione di candidati in quattro bande di punteggio e "
        "guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il "
        "resto e' movimento del soggetto dentro la stessa inquadratura); banda "
        "0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda "
        "0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. "
        "Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a "
        "0.043-0.068), che in questo materiale sono la maggioranza dei tagli."
    ),
    "limite_noto_soglia": (
        "Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi "
        "e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di "
        "armageddon-home il passaggio dal parlato al b-roll in bianco e nero "
        "segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione."
    ),
    "finestra_fusione": (
        "0.20 s. Un taglio secco puo' far superare la soglia a due fotogrammi "
        "consecutivi; entro 0.20 s si contano come un taglio solo."
    ),
    "silenzi": (
        "Due configurazioni dichiarate, perche' con la musica sotto la voce il "
        "silenzio assoluto quasi non esiste: -40 dB / 0.30 s misura il silenzio "
        "vero, -30 dB / 0.25 s misura la pausa del parlato."
    ),
    "profilo_audio": (
        "Finestre da 0.5 s sul PCM mono a 16 kHz: RMS in dBFS, picco in dBFS, "
        "zero-crossing rate. Il loudness EBU R128 (M a 400 ms, S a 3 s, I "
        "integrata) viene dal filtro ebur128 di ffmpeg con cadenza 100 ms."
    ),
    "cambio_regime": (
        "Meccanico, nessun giudizio: si calcola la mediana di RMS su blocchi da "
        "5 s e si segna ogni blocco che si discosta di 6 dB o piu' dal blocco "
        "precedente. Che cosa sia entrato (musica, stinger, voce sola) lo dira' "
        "l'occhio in Fase 2, non questo script."
    ),
    "frame": (
        "Un frame ogni 2 s a 960 px di larghezza. La riduzione ai soli frame in "
        "cui lo schermo cambia usa il metodo di "
        "empire-studio/scripts/scene_detector.py: miniatura 64x64 in scala di "
        "grigi, differenza media assoluta normalizzata 0-100, soglia 3.0, "
        "confronto con l'ultimo frame TENUTO, piu' il presidio che tiene un "
        "frame almeno ogni 30 s."
    ),
}


# ----------------------------------------------------------------------------
# Utilita'
# ----------------------------------------------------------------------------
def log(msg):
    """Stampa ASCII pura: la console Windows e' cp1252 e muore sugli accenti."""
    testo = str(msg)
    testo = (testo.replace("\u00e0", "a'").replace("\u00e8", "e'")
                  .replace("\u00e9", "e'").replace("\u00ec", "i'")
                  .replace("\u00f2", "o'").replace("\u00f9", "u'"))
    sys.stdout.write(testo.encode("ascii", "replace").decode("ascii") + "\n")
    sys.stdout.flush()


def hhmmss(s):
    if s is None:
        return "-"
    s = float(s)
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = s - h * 3600 - m * 60
    if h:
        return "%d:%02d:%05.2f" % (h, m, sec)
    return "%d:%05.2f" % (m, sec)


def scrivi_json(path, dati):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=1)


def scrivi_testo(path, testo):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(testo)


def esegui(cmd, stdout_file=None, timeout=3600):
    """Esegue un comando e ritorna (rc, stdout, stderr). stdout su file se chiesto."""
    if stdout_file is not None:
        with open(stdout_file, "wb") as f:
            p = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, timeout=timeout)
        return p.returncode, None, p.stderr.decode("utf-8", "replace")
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    return (p.returncode,
            p.stdout.decode("utf-8", "replace"),
            p.stderr.decode("utf-8", "replace"))


def cmd_str(cmd):
    fuori = []
    for c in cmd:
        fuori.append('"%s"' % c if (" " in c or "'" in c) else c)
    return " ".join(fuori)


def frazione(s):
    try:
        a, b = s.split("/")
        return float(a) / float(b) if float(b) else None
    except Exception:
        return None


def statistiche(valori):
    if not valori:
        return {}
    return {
        "n": len(valori),
        "media": round(statistics.mean(valori), 3),
        "mediana": round(statistics.median(valori), 3),
        "min": round(min(valori), 3),
        "max": round(max(valori), 3),
        "deviazione_standard": round(statistics.pstdev(valori), 3) if len(valori) > 1 else 0.0,
    }


# ----------------------------------------------------------------------------
# Riuso di scene_detector.py (Empire Studio) per la riduzione dei frame
# ----------------------------------------------------------------------------
def carica_scene_detector():
    """Importa firma() e differenza() da empire-studio/scripts/scene_detector.py.

    Se il file non c'e' (repo spostato) si usa la copia locale, identica nel
    metodo: miniatura 64x64 in scala di grigi, differenza media assoluta 0-100.
    """
    if SCENE_DETECTOR.is_file():
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("es_scene_detector", SCENE_DETECTOR)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod.firma, mod.differenza, str(SCENE_DETECTOR)
        except Exception as e:
            log("[misura] scene_detector.py non importabile (%s), uso la copia locale" % e)

    from PIL import Image

    def firma(path):
        with Image.open(path) as im:
            return list(im.convert("L").resize((64, 64), Image.BILINEAR).getdata())

    def differenza(a, b):
        if not a or not b:
            return 100.0
        tot = sum(abs(x - y) for x, y in zip(a, b))
        return (tot / len(a)) / 255.0 * 100.0

    return firma, differenza, "copia locale in misura_vsl.py (stesso metodo)"


# ----------------------------------------------------------------------------
# 1. TECNICA
# ----------------------------------------------------------------------------
def misura_tecnica(video, dest):
    cmd = ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video)]
    rc, out, err = esegui(cmd)
    if rc != 0:
        raise RuntimeError("ffprobe fallito: %s" % err.strip()[:300])
    d = json.loads(out)

    fmt = d.get("format", {})
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in d.get("streams", []) if s.get("codec_type") == "audio"), {})

    # numero di frame: se nb_frames manca, si conta davvero (mai a occhio)
    nb = v.get("nb_frames")
    metodo_frame = "ffprobe stream=nb_frames"
    if not nb:
        c2 = ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
              "-show_entries", "stream=nb_read_frames", "-of", "default=nw=1:nk=1", str(video)]
        rc2, out2, _ = esegui(c2)
        nb = out2.strip() if rc2 == 0 else None
        metodo_frame = "ffprobe -count_frames stream=nb_read_frames"

    dati = {
        "file": str(video),
        "peso_byte": int(fmt.get("size") or 0),
        "peso_MB": round(int(fmt.get("size") or 0) / 1048576.0, 1),
        "contenitore": fmt.get("format_name"),
        "durata_s": round(float(fmt.get("duration") or 0), 3),
        "durata_hhmmss": hhmmss(float(fmt.get("duration") or 0)),
        "bitrate_totale_bps": int(fmt.get("bit_rate") or 0),
        "video": {
            "codec": v.get("codec_name"),
            "profilo": v.get("profile"),
            "pix_fmt": v.get("pix_fmt"),
            "larghezza": v.get("width"),
            "altezza": v.get("height"),
            "fps_dichiarato": v.get("r_frame_rate"),
            "fps_reale": round(frazione(v.get("avg_frame_rate") or "0/0") or 0, 5),
            "frame_totali": int(nb) if nb else None,
            "frame_totali_metodo": metodo_frame,
            "durata_s": round(float(v.get("duration") or 0), 3),
            "bitrate_bps": int(v.get("bit_rate") or 0) if v.get("bit_rate") else None,
        },
        "audio": {
            "codec": a.get("codec_name"),
            "profilo": a.get("profile"),
            "sample_rate_hz": int(a.get("sample_rate") or 0) if a.get("sample_rate") else None,
            "canali": a.get("channels"),
            "durata_s": round(float(a.get("duration") or 0), 3),
            "bitrate_bps": int(a.get("bit_rate") or 0) if a.get("bit_rate") else None,
            "frame_audio": int(a.get("nb_frames")) if a.get("nb_frames") else None,
        },
        "comandi": [cmd_str(cmd)],
    }
    scrivi_json(dest / "tecnica.json", dati)
    return dati


# ----------------------------------------------------------------------------
# 2. STACCHI
# ----------------------------------------------------------------------------
def leggi_metadata_print(path):
    """Legge l'output di metadata=print: [(pts_time, {chiave: valore}), ...]."""
    voci = []
    t = None
    corrente = None
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for riga in f:
            if riga.startswith("frame:"):
                if corrente is not None and t is not None:
                    voci.append((t, corrente))
                m = re.search(r"pts_time:([-0-9.eE]+)", riga)
                t = float(m.group(1)) if m else None
                corrente = {}
            elif "=" in riga and corrente is not None:
                k, _, val = riga.strip().partition("=")
                corrente[k.strip()] = val.strip()
    if corrente is not None and t is not None:
        voci.append((t, corrente))
    return voci


def tagli_da_punteggi(punteggi, soglia, fusione, durata):
    """punteggi = [(t, score)] ordinati. Ritorna la lista dei tempi di taglio."""
    tagli = []
    for t, s in punteggi:
        if s <= soglia:
            continue
        if t <= 0.0:
            continue
        if t >= durata:
            continue
        if tagli and (t - tagli[-1]) < fusione:
            continue
        tagli.append(round(t, 2))
    return tagli


def misura_stacchi(video, dest, durata, fps, soglia, tmp):
    grezzo = tmp / "scene_scores.txt"
    filtro = "scale=%d:-2,select='gte(scene,0)',metadata=print:file=-" % SCENA_LARGHEZZA
    cmd = ["ffmpeg", "-v", "error", "-nostdin", "-i", str(video), "-an",
           "-vf", filtro, "-f", "null", "-"]
    t0 = time.time()
    rc, _, err = esegui(cmd, stdout_file=grezzo)
    if rc != 0:
        raise RuntimeError("ffmpeg scene detect fallito: %s" % err.strip()[:300])
    secondi_passata = round(time.time() - t0, 1)

    voci = leggi_metadata_print(grezzo)
    punteggi = []
    for t, m in voci:
        if "lavfi.scene_score" in m:
            try:
                punteggi.append((t, float(m["lavfi.scene_score"])))
            except ValueError:
                pass
    punteggi.sort(key=lambda x: x[0])

    tagli = tagli_da_punteggi(punteggi, soglia, FINESTRA_FUSIONE, durata)

    # inquadrature
    bordi = [0.0] + tagli + [round(durata, 2)]
    inquadrature = []
    for i in range(len(bordi) - 1):
        ini, fin = bordi[i], bordi[i + 1]
        if fin <= ini:
            continue
        inquadrature.append({
            "n": len(inquadrature) + 1,
            "inizio_s": round(ini, 2),
            "fine_s": round(fin, 2),
            "durata_s": round(fin - ini, 2),
            "inizio_hhmmss": hhmmss(ini),
        })
    durate = [q["durata_s"] for q in inquadrature]

    # profilo minuto per minuto
    minuti = int(math.ceil(durata / 60.0))
    profilo = []
    for m in range(minuti):
        a, b = m * 60.0, min((m + 1) * 60.0, durata)
        in_min = [q for q in inquadrature if a <= q["inizio_s"] < b]
        n_tagli = len([t for t in tagli if a <= t < b])
        profilo.append({
            "minuto": m + 1,
            "da_s": round(a, 2),
            "a_s": round(b, 2),
            "tagli": n_tagli,
            "inquadrature_iniziate": len(in_min),
            "durata_media_s": round(statistics.mean([q["durata_s"] for q in in_min]), 2) if in_min else None,
        })

    # tabella di sensibilita': stessa passata, soglie diverse
    sensibilita = []
    for s in sorted(set(SOGLIE_CONFRONTO + [soglia])):
        tt = tagli_da_punteggi(punteggi, s, FINESTRA_FUSIONE, durata)
        bb = [0.0] + tt + [durata]
        dd = [bb[i + 1] - bb[i] for i in range(len(bb) - 1) if bb[i + 1] > bb[i]]
        sensibilita.append({
            "soglia": s,
            "tagli": len(tt),
            "durata_media_s": round(statistics.mean(dd), 2) if dd else None,
            "durata_mediana_s": round(statistics.median(dd), 2) if dd else None,
            "inquadrature_sotto_1s": sum(1 for d in dd if d < 1.0),
            "usata": (abs(s - soglia) < 1e-9),
        })

    candidati = [{"t": round(t, 2), "score": round(s, 4)}
                 for t, s in punteggi if s >= CANDIDATO_MIN]

    dati = {
        "slug": dest.name,
        "metodo": {
            "comando": cmd_str(cmd),
            "filtro": filtro,
            "soglia_usata": soglia,
            "finestra_fusione_s": FINESTRA_FUSIONE,
            "larghezza_analisi_px": SCENA_LARGHEZZA,
            "frame_valutati": len(punteggi),
            "secondi_di_calcolo": secondi_passata,
            "motivazione_soglia": PARAMETRI_MOTIVAZIONE["soglia_scena"],
            "limite_noto": PARAMETRI_MOTIVAZIONE["limite_noto_soglia"],
            "motivazione_fusione": PARAMETRI_MOTIVAZIONE["finestra_fusione"],
        },
        "durata_s": round(durata, 3),
        "fps": fps,
        "tagli_n": len(tagli),
        "tagli_s": tagli,
        "tagli_al_minuto": round(len(tagli) / (durata / 60.0), 2) if durata else None,
        "inquadrature_n": len(inquadrature),
        "inquadrature": inquadrature,
        "statistiche_durata_inquadratura": statistiche(durate),
        "profilo_per_minuto": profilo,
        "sensibilita_soglia": sensibilita,
        "candidati_sopra_%.3f" % CANDIDATO_MIN: candidati,
    }
    scrivi_json(dest / "stacchi.json", dati)

    # stacchi.md
    st = dati["statistiche_durata_inquadratura"]
    r = []
    r.append("# Stacchi di montaggio - %s" % dest.name)
    r.append("")
    r.append("Misura a macchina. Nessuna interpretazione.")
    r.append("")
    r.append("| voce | valore |")
    r.append("|---|---|")
    r.append("| durata video | %s (%.3f s) |" % (hhmmss(durata), durata))
    r.append("| soglia scene score usata | **%.3f** |" % soglia)
    r.append("| tagli rilevati | **%d** |" % len(tagli))
    r.append("| inquadrature | %d |" % len(inquadrature))
    r.append("| tagli al minuto | %s |" % dati["tagli_al_minuto"])
    r.append("| durata media inquadratura | %s s |" % st.get("media"))
    r.append("| durata mediana | %s s |" % st.get("mediana"))
    r.append("| minima / massima | %s s / %s s |" % (st.get("min"), st.get("max")))
    r.append("| deviazione standard | %s s |" % st.get("deviazione_standard"))
    r.append("")
    r.append("Comando: `%s`" % cmd_str(cmd))
    r.append("")
    r.append("## Sensibilita' alla soglia (stessa passata, soglie diverse)")
    r.append("")
    r.append("| soglia | tagli | durata media | mediana | inquadrature < 1 s | |")
    r.append("|---|---|---|---|---|---|")
    for s in sensibilita:
        r.append("| %.3f | %d | %s s | %s s | %d | %s |" % (
            s["soglia"], s["tagli"], s["durata_media_s"], s["durata_mediana_s"],
            s["inquadrature_sotto_1s"], "**usata**" if s["usata"] else ""))
    r.append("")
    r.append("Perche' questa soglia: %s" % PARAMETRI_MOTIVAZIONE["soglia_scena"])
    r.append("")
    r.append("Limite noto: %s" % PARAMETRI_MOTIVAZIONE["limite_noto_soglia"])
    r.append("")
    r.append("## Profilo del ritmo, minuto per minuto")
    r.append("")
    r.append("| minuto | tagli | inquadrature iniziate | durata media |")
    r.append("|---|---|---|---|")
    for p in profilo:
        r.append("| %d | %d | %d | %s s |" % (
            p["minuto"], p["tagli"], p["inquadrature_iniziate"],
            p["durata_media_s"] if p["durata_media_s"] is not None else "-"))
    r.append("")
    r.append("## Tutte le inquadrature")
    r.append("")
    r.append("| n | inizio | fine | durata |")
    r.append("|---|---|---|---|")
    for q in inquadrature:
        r.append("| %d | %.2f | %.2f | %.2f |" % (q["n"], q["inizio_s"], q["fine_s"], q["durata_s"]))
    r.append("")
    scrivi_testo(dest / "stacchi.md", "\n".join(r))
    return dati


# ----------------------------------------------------------------------------
# 3. AUDIO
# ----------------------------------------------------------------------------
def db(x):
    return round(20.0 * math.log10(x), 2) if x > 0 else -120.0


def misura_audio(video, dest, durata, tmp):
    comandi = []

    # --- 3a. EBU R128, cadenza 100 ms, piu' il riepilogo integrato -----------
    eb_out = tmp / "ebur128.txt"
    eb_err = tmp / "ebur128_err.txt"
    filtro_eb = "ebur128=peak=true:metadata=1,ametadata=print:file=-"
    cmd_eb = ["ffmpeg", "-v", "info", "-nostdin", "-i", str(video), "-vn",
              "-af", filtro_eb, "-f", "null", "-"]
    with open(eb_out, "wb") as fo, open(eb_err, "wb") as fe:
        p = subprocess.run(cmd_eb, stdout=fo, stderr=fe)
    if p.returncode != 0:
        raise RuntimeError("ffmpeg ebur128 fallito")
    comandi.append(cmd_str(cmd_eb))

    voci = leggi_metadata_print(eb_out)
    r128 = []
    for t, m in voci:
        try:
            r128.append({
                "t": round(t, 2),
                "M": float(m.get("lavfi.r128.M", "nan")),
                "S": float(m.get("lavfi.r128.S", "nan")),
                "I": float(m.get("lavfi.r128.I", "nan")),
            })
        except ValueError:
            pass
    riepilogo = {}
    testo_err = open(eb_err, "r", encoding="utf-8", errors="replace").read()
    for chiave, patt in (("integrata_LUFS", r"I:\s*(-?[\d.]+)\s*LUFS"),
                         ("soglia_LUFS", r"Threshold:\s*(-?[\d.]+)\s*LUFS"),
                         ("LRA_LU", r"LRA:\s*(-?[\d.]+)\s*LU"),
                         ("LRA_basso_LUFS", r"LRA low:\s*(-?[\d.]+)\s*LUFS"),
                         ("LRA_alto_LUFS", r"LRA high:\s*(-?[\d.]+)\s*LUFS"),
                         ("true_peak_dBFS", r"True peak:\s*\n?\s*Peak:\s*(-?[\d.]+)\s*dBFS")):
        m = re.search(patt, testo_err)
        if m:
            riepilogo[chiave] = float(m.group(1))

    momentary = [v["M"] for v in r128 if v["M"] > -70]
    short = [v["S"] for v in r128 if v["S"] > -70]

    # --- 3b. Silenzi, due configurazioni ------------------------------------
    silenzi = {}
    for etichetta, (rumore, minimo) in (("silenzio_assoluto", SILENZIO_A),
                                        ("pausa_parlato", SILENZIO_B)):
        sd_err = tmp / ("silence_%s.txt" % etichetta)
        filtro_sd = "silencedetect=noise=%s:d=%s" % (rumore, minimo)
        cmd_sd = ["ffmpeg", "-v", "info", "-nostdin", "-i", str(video), "-vn",
                  "-af", filtro_sd, "-f", "null", "-"]
        with open(sd_err, "wb") as fe:
            subprocess.run(cmd_sd, stdout=subprocess.DEVNULL, stderr=fe)
        comandi.append(cmd_str(cmd_sd))
        testo = open(sd_err, "r", encoding="utf-8", errors="replace").read()
        inizi = [float(x) for x in re.findall(r"silence_start:\s*(-?[\d.]+)", testo)]
        fini = re.findall(r"silence_end:\s*([\d.]+)\s*\|\s*silence_duration:\s*([\d.]+)", testo)
        lista = []
        for i, (fine, dur) in enumerate(fini):
            ini = inizi[i] if i < len(inizi) else float(fine) - float(dur)
            lista.append({"inizio_s": round(max(ini, 0.0), 3),
                          "fine_s": round(float(fine), 3),
                          "durata_s": round(float(dur), 3)})
        if len(inizi) > len(fini):  # silenzio aperto in coda
            lista.append({"inizio_s": round(inizi[-1], 3),
                          "fine_s": round(durata, 3),
                          "durata_s": round(durata - inizi[-1], 3)})
        durate_sil = [s["durata_s"] for s in lista]
        silenzi[etichetta] = {
            "soglia_rumore": rumore,
            "durata_minima_s": minimo,
            "comando": cmd_str(cmd_sd),
            "n": len(lista),
            "totale_s": round(sum(durate_sil), 2),
            "percentuale_del_video": round(100.0 * sum(durate_sil) / durata, 2) if durata else None,
            "statistiche": statistiche(durate_sil),
            "elenco": lista,
        }

    # --- 3c. Profilo a finestre da 0,5 s dal PCM ----------------------------
    pcm = tmp / "audio.raw"
    cmd_pcm = ["ffmpeg", "-v", "error", "-nostdin", "-i", str(video), "-vn",
               "-ac", "1", "-ar", str(PCM_HZ), "-f", "s16le", "-"]
    rc, _, err = esegui(cmd_pcm, stdout_file=pcm)
    if rc != 0:
        raise RuntimeError("ffmpeg estrazione PCM fallita: %s" % err.strip()[:200])
    comandi.append(cmd_str(cmd_pcm))

    grezzo = pcm.read_bytes()
    n_camp = len(grezzo) // 2
    campioni = struct.unpack("<%dh" % n_camp, grezzo[:n_camp * 2])
    per_finestra = int(PCM_HZ * FINESTRA_AUDIO)
    profilo = []
    for i in range(0, n_camp - per_finestra + 1, per_finestra):
        blocco = campioni[i:i + per_finestra]
        somma = 0
        picco = 0
        incroci = 0
        prec = blocco[0]
        for v in blocco:
            somma += v * v
            av = v if v >= 0 else -v
            if av > picco:
                picco = av
            if (v >= 0) != (prec >= 0):
                incroci += 1
            prec = v
        rms = math.sqrt(somma / float(per_finestra)) / 32768.0
        profilo.append({
            "t": round(i / float(PCM_HZ), 2),
            "rms_dBFS": db(rms),
            "picco_dBFS": db(picco / 32768.0),
            "zcr": round(incroci / float(per_finestra), 4),
        })

    # picchi: le finestre col picco piu' alto, e dove stanno
    ordinati = sorted(profilo, key=lambda x: x["picco_dBFS"], reverse=True)
    picchi_top = [{"t": p["t"], "picco_dBFS": p["picco_dBFS"], "hhmmss": hhmmss(p["t"])}
                  for p in ordinati[:25]]

    # --- 3d. Cambi di regime, meccanici -------------------------------------
    per_blocco = int(REGIME_BLOCCO / FINESTRA_AUDIO)
    blocchi = []
    for i in range(0, len(profilo) - per_blocco + 1, per_blocco):
        seg = profilo[i:i + per_blocco]
        blocchi.append({"t": seg[0]["t"],
                        "rms_mediano_dBFS": round(statistics.median([s["rms_dBFS"] for s in seg]), 2),
                        "zcr_mediano": round(statistics.median([s["zcr"] for s in seg]), 4)})
    cambi = []
    for i in range(1, len(blocchi)):
        delta = blocchi[i]["rms_mediano_dBFS"] - blocchi[i - 1]["rms_mediano_dBFS"]
        if abs(delta) >= REGIME_SALTO_DB:
            cambi.append({"t": blocchi[i]["t"],
                          "hhmmss": hhmmss(blocchi[i]["t"]),
                          "delta_dB": round(delta, 2),
                          "da_dBFS": blocchi[i - 1]["rms_mediano_dBFS"],
                          "a_dBFS": blocchi[i]["rms_mediano_dBFS"],
                          "zcr_da": blocchi[i - 1]["zcr_mediano"],
                          "zcr_a": blocchi[i]["zcr_mediano"]})

    rms_tutti = [p["rms_dBFS"] for p in profilo]
    dati = {
        "slug": dest.name,
        "durata_s": round(durata, 3),
        "metodo": {
            "comandi": comandi,
            "finestra_profilo_s": FINESTRA_AUDIO,
            "pcm_hz": PCM_HZ,
            "motivazione_profilo": PARAMETRI_MOTIVAZIONE["profilo_audio"],
            "motivazione_silenzi": PARAMETRI_MOTIVAZIONE["silenzi"],
            "motivazione_regime": PARAMETRI_MOTIVAZIONE["cambio_regime"],
            "regime_salto_dB": REGIME_SALTO_DB,
            "regime_blocco_s": REGIME_BLOCCO,
        },
        "ebur128": {
            "riepilogo": riepilogo,
            "momentary_statistiche": statistiche(momentary),
            "short_term_statistiche": statistiche(short),
            "campioni_100ms_n": len(r128),
            "serie_100ms": [{"t": v["t"], "M": round(v["M"], 2), "S": round(v["S"], 2)}
                            for v in r128],
        },
        "picchi_massimi": picchi_top,
        "silenzi": silenzi,
        "profilo_volume_0_5s": profilo,
        "profilo_statistiche_rms_dBFS": statistiche(rms_tutti),
        "blocchi_5s": blocchi,
        "cambi_di_regime": cambi,
    }
    scrivi_json(dest / "audio.json", dati)

    # audio.md
    r = []
    r.append("# Audio - %s" % dest.name)
    r.append("")
    r.append("Misura a macchina. Nessuna interpretazione.")
    r.append("")
    r.append("| voce | valore |")
    r.append("|---|---|")
    r.append("| loudness integrata | %s LUFS |" % riepilogo.get("integrata_LUFS"))
    r.append("| loudness range (LRA) | %s LU (da %s a %s LUFS) |" % (
        riepilogo.get("LRA_LU"), riepilogo.get("LRA_basso_LUFS"), riepilogo.get("LRA_alto_LUFS")))
    r.append("| true peak | %s dBFS |" % riepilogo.get("true_peak_dBFS"))
    r.append("| momentary (400 ms) media / min / max | %s / %s / %s LUFS |" % (
        (momentary and round(statistics.mean(momentary), 2)),
        (momentary and round(min(momentary), 2)), (momentary and round(max(momentary), 2))))
    r.append("| RMS finestre 0,5 s media / min / max | %s / %s / %s dBFS |" % (
        round(statistics.mean(rms_tutti), 2), round(min(rms_tutti), 2), round(max(rms_tutti), 2)))
    r.append("| finestre da 0,5 s misurate | %d |" % len(profilo))
    for et in ("silenzio_assoluto", "pausa_parlato"):
        s = silenzi[et]
        r.append("| %s (%s, min %s s) | %d occorrenze, %s s totali (%s%% del video) |" % (
            et.replace("_", " "), s["soglia_rumore"], s["durata_minima_s"],
            s["n"], s["totale_s"], s["percentuale_del_video"]))
    r.append("| cambi di regime (>= %s dB su blocchi da %s s) | %d |" % (
        REGIME_SALTO_DB, REGIME_BLOCCO, len(cambi)))
    r.append("")
    for c in comandi:
        r.append("Comando: `%s`" % c)
        r.append("")
    r.append("## Cambi di regime del volume")
    r.append("")
    r.append("Regola meccanica: mediana RMS su blocchi da %s s, si segna ogni salto >= %s dB." % (
        REGIME_BLOCCO, REGIME_SALTO_DB))
    r.append("")
    if cambi:
        r.append("| t | hh:mm:ss | da dBFS | a dBFS | delta | zcr da | zcr a |")
        r.append("|---|---|---|---|---|---|---|")
        for c in cambi:
            r.append("| %.2f | %s | %s | %s | %+0.2f | %s | %s |" % (
                c["t"], c["hhmmss"], c["da_dBFS"], c["a_dBFS"], c["delta_dB"],
                c["zcr_da"], c["zcr_a"]))
    else:
        r.append("Nessun salto oltre soglia.")
    r.append("")
    r.append("## Silenzi")
    r.append("")
    for et in ("silenzio_assoluto", "pausa_parlato"):
        s = silenzi[et]
        r.append("### %s - soglia %s, durata minima %s s" % (
            et.replace("_", " "), s["soglia_rumore"], s["durata_minima_s"]))
        r.append("")
        r.append("%d occorrenze, %s s totali, %s%% del video. Media %s s, mediana %s s, max %s s." % (
            s["n"], s["totale_s"], s["percentuale_del_video"],
            s["statistiche"].get("media"), s["statistiche"].get("mediana"),
            s["statistiche"].get("max")))
        r.append("")
        if s["elenco"]:
            r.append("| inizio | fine | durata |")
            r.append("|---|---|---|")
            for x in s["elenco"]:
                r.append("| %.3f | %.3f | %.3f |" % (x["inizio_s"], x["fine_s"], x["durata_s"]))
        r.append("")
    r.append("## Picchi piu' alti (finestre da 0,5 s)")
    r.append("")
    r.append("| t | hh:mm:ss | picco dBFS |")
    r.append("|---|---|---|")
    for p in picchi_top:
        r.append("| %.2f | %s | %s |" % (p["t"], p["hhmmss"], p["picco_dBFS"]))
    r.append("")
    r.append("## Profilo del volume, blocchi da %s s" % REGIME_BLOCCO)
    r.append("")
    r.append("(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)")
    r.append("")
    r.append("| t | rms mediano dBFS | zcr mediano |")
    r.append("|---|---|---|")
    for b in blocchi:
        r.append("| %.2f | %s | %s |" % (b["t"], b["rms_mediano_dBFS"], b["zcr_mediano"]))
    r.append("")
    scrivi_testo(dest / "audio.md", "\n".join(r))
    return dati


# ----------------------------------------------------------------------------
# 4. FRAME
# ----------------------------------------------------------------------------
def estrai_frame(video, dest, durata, tagli):
    frames = dest / "frames"
    stac = frames / "stacchi"
    if frames.exists():
        shutil.rmtree(frames)
    frames.mkdir(parents=True, exist_ok=True)
    stac.mkdir(parents=True, exist_ok=True)

    comandi = []

    # --- 4a. frame densi ogni 2 s -------------------------------------------
    filtro = "fps=1/%g,scale=%d:-2" % (PASSO_FRAME, LARGHEZZA_FRAME)
    cmd = ["ffmpeg", "-v", "error", "-nostdin", "-i", str(video),
           "-vf", filtro, "-y", str(frames / "frame-%04d.png")]
    rc, _, err = esegui(cmd)
    if rc != 0:
        raise RuntimeError("estrazione frame densi fallita: %s" % err.strip()[:200])
    comandi.append(cmd_str(cmd))

    densi = sorted(frames.glob("frame-*.png"))
    manifest_densi = []
    for i, f in enumerate(densi):
        manifest_densi.append({"file": f.name, "t": round(i * PASSO_FRAME, 2),
                               "hhmmss": hhmmss(i * PASSO_FRAME)})

    # --- 4b. riduzione ai soli frame in cui lo schermo cambia ---------------
    firma, differenza, fonte_metodo = carica_scene_detector()
    tenuti = []
    rif = None
    ultimo_t = None
    for v in manifest_densi:
        f = frames / v["file"]
        try:
            sig = firma(f)
        except Exception as e:
            v["differenza"] = None
            v["unico"] = True
            v["motivo"] = "frame illeggibile: %s" % e
            tenuti.append(v)
            continue
        if rif is None:
            d = 100.0
            motivo = "primo frame"
        else:
            d = differenza(rif, sig)
            motivo = "sopra soglia" if d >= DEDUP_SOGLIA else None
        presidio = (ultimo_t is not None and DEDUP_MAX_GAP > 0
                    and (v["t"] - ultimo_t) >= DEDUP_MAX_GAP)
        v["differenza"] = round(d, 2)
        if motivo or presidio:
            v["unico"] = True
            v["motivo"] = motivo or ("presidio: %.0f s dall'ultimo tenuto" % (v["t"] - ultimo_t))
            tenuti.append(v)
            rif = sig
            ultimo_t = v["t"]
        else:
            v["unico"] = False
            v["motivo"] = None
    if manifest_densi and not manifest_densi[-1]["unico"]:
        manifest_densi[-1]["unico"] = True
        manifest_densi[-1]["motivo"] = "ultimo frame"
        tenuti.append(manifest_densi[-1])

    # --- 4c. un frame sul primo fotogramma di ogni inquadratura -------------
    bordi = [0.0] + list(tagli)
    manifest_stacchi = []
    cmd_esempio = None
    for i, t in enumerate(bordi):
        nome = "stacco-%04d.png" % (i + 1)
        c = ["ffmpeg", "-v", "error", "-nostdin", "-ss", "%.3f" % max(t + 0.02, 0.0),
             "-i", str(video), "-frames:v", "1",
             "-vf", "scale=%d:-2" % LARGHEZZA_FRAME, "-y", str(stac / nome)]
        rc, _, _ = esegui(c, timeout=120)
        if cmd_esempio is None:
            cmd_esempio = cmd_str(c)
        if rc == 0 and (stac / nome).exists():
            manifest_stacchi.append({"file": "stacchi/" + nome, "n_inquadratura": i + 1,
                                     "t": round(t, 2), "hhmmss": hhmmss(t)})
    if cmd_esempio:
        comandi.append(cmd_esempio + "   (ripetuto per ogni inquadratura)")

    manifest = {
        "slug": dest.name,
        "metodo": {
            "comandi": comandi,
            "passo_s": PASSO_FRAME,
            "larghezza_px": LARGHEZZA_FRAME,
            "riduzione_soglia": DEDUP_SOGLIA,
            "riduzione_max_gap_s": DEDUP_MAX_GAP,
            "riduzione_fonte": fonte_metodo,
            "motivazione": PARAMETRI_MOTIVAZIONE["frame"],
            "nota_stacchi": "il frame di stacco e' preso a t+0.02 s, cioe' il primo "
                            "fotogramma dell'inquadratura nuova",
        },
        "frame_densi_n": len(manifest_densi),
        "frame_unici_n": len(tenuti),
        "frame_stacchi_n": len(manifest_stacchi),
        "frame_densi": manifest_densi,
        "frame_unici": [{"file": v["file"], "t": v["t"], "differenza": v.get("differenza"),
                         "motivo": v.get("motivo")} for v in tenuti],
        "frame_stacchi": manifest_stacchi,
    }
    scrivi_json(frames / "manifest.json", manifest)
    return manifest


# ----------------------------------------------------------------------------
# 5. SOMMARIO
# ----------------------------------------------------------------------------
def scrivi_sommario(dest, tec, sta, aud, fra, soglia, secondi):
    st = sta["statistiche_durata_inquadratura"]
    rip = aud["ebur128"]["riepilogo"]
    sa = aud["silenzi"]["silenzio_assoluto"]
    sp = aud["silenzi"]["pausa_parlato"]
    prs = aud["profilo_statistiche_rms_dBFS"]

    r = []
    r.append("# %s - sommario di misura" % dest.name)
    r.append("")
    r.append("Fase 1 di EMP-DIOEDIT. Solo numeri: nessun aggettivo, nessuna interpretazione.")
    r.append("Generato il %s da `scripts/misura_vsl.py` v%s in %.1f s." % (
        datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"), VERSIONE, secondi))
    r.append("")
    r.append("## Tecnica")
    r.append("")
    r.append("| voce | valore |")
    r.append("|---|---|")
    r.append("| durata | %s (%.3f s) |" % (tec["durata_hhmmss"], tec["durata_s"]))
    r.append("| risoluzione | %sx%s |" % (tec["video"]["larghezza"], tec["video"]["altezza"]))
    r.append("| fps reale | %s (dichiarato %s) |" % (tec["video"]["fps_reale"], tec["video"]["fps_dichiarato"]))
    r.append("| frame totali | %s (%s) |" % (tec["video"]["frame_totali"], tec["video"]["frame_totali_metodo"]))
    r.append("| codec video | %s %s, %s |" % (tec["video"]["codec"], tec["video"]["profilo"], tec["video"]["pix_fmt"]))
    r.append("| bitrate video | %s bps |" % tec["video"]["bitrate_bps"])
    r.append("| codec audio | %s %s, %s Hz, %s canali |" % (
        tec["audio"]["codec"], tec["audio"]["profilo"], tec["audio"]["sample_rate_hz"], tec["audio"]["canali"]))
    r.append("| bitrate audio | %s bps |" % tec["audio"]["bitrate_bps"])
    r.append("| bitrate totale | %s bps |" % tec["bitrate_totale_bps"])
    r.append("| peso | %s MB |" % tec["peso_MB"])
    r.append("")
    r.append("Come: `%s`" % tec["comandi"][0])
    r.append("")
    r.append("## Montaggio")
    r.append("")
    r.append("| voce | valore |")
    r.append("|---|---|")
    r.append("| soglia scene score usata | **%.3f** |" % soglia)
    r.append("| tagli | **%d** |" % sta["tagli_n"])
    r.append("| inquadrature | %d |" % sta["inquadrature_n"])
    r.append("| tagli al minuto | %s |" % sta["tagli_al_minuto"])
    r.append("| durata media inquadratura | %s s |" % st.get("media"))
    r.append("| durata mediana | %s s |" % st.get("mediana"))
    r.append("| durata minima | %s s |" % st.get("min"))
    r.append("| durata massima | %s s |" % st.get("max"))
    r.append("| deviazione standard | %s s |" % st.get("deviazione_standard"))
    minuti_ord = sorted(sta["profilo_per_minuto"], key=lambda p: p["tagli"], reverse=True)
    if minuti_ord:
        r.append("| minuto con piu' tagli | minuto %d, %d tagli |" % (minuti_ord[0]["minuto"], minuti_ord[0]["tagli"]))
        r.append("| minuto con meno tagli | minuto %d, %d tagli |" % (minuti_ord[-1]["minuto"], minuti_ord[-1]["tagli"]))
    r.append("")
    r.append("Come: `%s`" % sta["metodo"]["comando"])
    r.append("")
    r.append("Soglia: %s" % PARAMETRI_MOTIVAZIONE["soglia_scena"])
    r.append("")
    r.append("Limite noto: %s" % PARAMETRI_MOTIVAZIONE["limite_noto_soglia"])
    r.append("")
    r.append("Sensibilita' (stessa passata, soglie diverse):")
    r.append("")
    r.append("| soglia | tagli | durata media | |")
    r.append("|---|---|---|---|")
    for s in sta["sensibilita_soglia"]:
        r.append("| %.3f | %d | %s s | %s |" % (
            s["soglia"], s["tagli"], s["durata_media_s"], "**usata**" if s["usata"] else ""))
    r.append("")
    r.append("Tagli per minuto:")
    r.append("")
    r.append("| minuto | " + " | ".join(str(p["minuto"]) for p in sta["profilo_per_minuto"]) + " |")
    r.append("|---" * (len(sta["profilo_per_minuto"]) + 1) + "|")
    r.append("| tagli | " + " | ".join(str(p["tagli"]) for p in sta["profilo_per_minuto"]) + " |")
    r.append("")
    r.append("## Audio")
    r.append("")
    r.append("| voce | valore |")
    r.append("|---|---|")
    r.append("| loudness integrata | %s LUFS |" % rip.get("integrata_LUFS"))
    r.append("| loudness range | %s LU |" % rip.get("LRA_LU"))
    r.append("| true peak | %s dBFS |" % rip.get("true_peak_dBFS"))
    r.append("| RMS 0,5 s media / min / max | %s / %s / %s dBFS |" % (
        prs.get("media"), prs.get("min"), prs.get("max")))
    r.append("| silenzi assoluti (%s, min %s s) | %d, %s s totali (%s%%) |" % (
        sa["soglia_rumore"], sa["durata_minima_s"], sa["n"], sa["totale_s"], sa["percentuale_del_video"]))
    r.append("| pause del parlato (%s, min %s s) | %d, %s s totali (%s%%) |" % (
        sp["soglia_rumore"], sp["durata_minima_s"], sp["n"], sp["totale_s"], sp["percentuale_del_video"]))
    r.append("| cambi di regime del volume | %d |" % len(aud["cambi_di_regime"]))
    if aud["picchi_massimi"]:
        p0 = aud["picchi_massimi"][0]
        r.append("| picco piu' alto | %s dBFS a %s |" % (p0["picco_dBFS"], p0["hhmmss"]))
    r.append("")
    for c in aud["metodo"]["comandi"]:
        r.append("Come: `%s`" % c)
        r.append("")
    r.append("Silenzi: %s" % PARAMETRI_MOTIVAZIONE["silenzi"])
    r.append("")
    r.append("Cambi di regime: %s" % PARAMETRI_MOTIVAZIONE["cambio_regime"])
    r.append("")
    if aud["cambi_di_regime"]:
        r.append("| t | delta dB | da | a |")
        r.append("|---|---|---|---|")
        for c in aud["cambi_di_regime"]:
            r.append("| %s | %+0.2f | %s | %s |" % (c["hhmmss"], c["delta_dB"], c["da_dBFS"], c["a_dBFS"]))
        r.append("")
    r.append("## Frame")
    r.append("")
    r.append("| voce | valore |")
    r.append("|---|---|")
    r.append("| frame densi (uno ogni %s s, %s px) | %d |" % (PASSO_FRAME, LARGHEZZA_FRAME, fra["frame_densi_n"]))
    r.append("| frame in cui lo schermo cambia | %d |" % fra["frame_unici_n"])
    r.append("| frame sul primo fotogramma di ogni inquadratura | %d |" % fra["frame_stacchi_n"])
    r.append("| riduzione | %d su %d densi (%.1f%%) |" % (
        fra["frame_unici_n"], fra["frame_densi_n"],
        100.0 * fra["frame_unici_n"] / fra["frame_densi_n"] if fra["frame_densi_n"] else 0))
    r.append("")
    for c in fra["metodo"]["comandi"]:
        r.append("Come: `%s`" % c)
        r.append("")
    r.append("Riduzione: %s" % PARAMETRI_MOTIVAZIONE["frame"])
    r.append("")
    r.append("## File")
    r.append("")
    r.append("- `tecnica.json`")
    r.append("- `stacchi.json` / `stacchi.md`")
    r.append("- `audio.json` / `audio.md`")
    r.append("- `frames/frame-NNNN.png` + `frames/manifest.json`")
    r.append("- `frames/stacchi/stacco-NNNN.png`")
    r.append("")
    scrivi_testo(dest / "_SOMMARIO.md", "\n".join(r))


# ----------------------------------------------------------------------------
# Orchestrazione per video
# ----------------------------------------------------------------------------
def firma_parametri(soglia):
    return {
        "versione": VERSIONE,
        "soglia_scena": soglia,
        "finestra_fusione": FINESTRA_FUSIONE,
        "larghezza_analisi": SCENA_LARGHEZZA,
        "finestra_audio": FINESTRA_AUDIO,
        "silenzio_a": list(SILENZIO_A),
        "silenzio_b": list(SILENZIO_B),
        "passo_frame": PASSO_FRAME,
        "larghezza_frame": LARGHEZZA_FRAME,
        "dedup_soglia": DEDUP_SOGLIA,
    }


def gia_completo(dest, soglia, con_frame):
    stato = dest / "_stato.json"
    if not stato.is_file():
        return False
    try:
        s = json.loads(stato.read_text(encoding="utf-8"))
    except Exception:
        return False
    if s.get("parametri") != firma_parametri(soglia):
        return False
    if not s.get("completo"):
        return False
    attesi = ["tecnica.json", "stacchi.json", "stacchi.md", "audio.json", "audio.md", "_SOMMARIO.md"]
    if con_frame:
        attesi.append("frames/manifest.json")
    return all((dest / a).exists() for a in attesi)


def misura_video(slug, soglia, con_frame, forza):
    video = SORGENTI / slug / "video.mp4"
    if not video.is_file():
        log("[misura] %-24s SALTATO: manca %s" % (slug, video))
        return None
    dest = MISURE / slug
    if gia_completo(dest, soglia, con_frame) and not forza:
        log("[misura] %-24s gia' completo, salto (usa --forza per rifare)" % slug)
        return "saltato"

    dest.mkdir(parents=True, exist_ok=True)
    tmp = dest / "_tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    log("[misura] %-24s inizio" % slug)

    tec = misura_tecnica(video, dest)
    durata = tec["durata_s"]
    fps = tec["video"]["fps_reale"]
    log("[misura] %-24s tecnica: %s, %sx%s, %s fps, %s frame" % (
        slug, tec["durata_hhmmss"], tec["video"]["larghezza"], tec["video"]["altezza"],
        fps, tec["video"]["frame_totali"]))

    sta = misura_stacchi(video, dest, durata, fps, soglia, tmp)
    log("[misura] %-24s stacchi: %d tagli, %d inquadrature, media %s s" % (
        slug, sta["tagli_n"], sta["inquadrature_n"],
        sta["statistiche_durata_inquadratura"].get("media")))

    aud = misura_audio(video, dest, durata, tmp)
    log("[misura] %-24s audio: I=%s LUFS, %d silenzi assoluti, %d pause, %d cambi di regime" % (
        slug, aud["ebur128"]["riepilogo"].get("integrata_LUFS"),
        aud["silenzi"]["silenzio_assoluto"]["n"], aud["silenzi"]["pausa_parlato"]["n"],
        len(aud["cambi_di_regime"])))

    if con_frame:
        fra = estrai_frame(video, dest, durata, sta["tagli_s"])
        log("[misura] %-24s frame: %d densi -> %d unici, %d di stacco" % (
            slug, fra["frame_densi_n"], fra["frame_unici_n"], fra["frame_stacchi_n"]))
    else:
        fra = {"frame_densi_n": 0, "frame_unici_n": 0, "frame_stacchi_n": 0,
               "metodo": {"comandi": ["(frame non estratti: --no-frame)"]}}

    secondi = time.time() - t0
    scrivi_sommario(dest, tec, sta, aud, fra, soglia, secondi)

    shutil.rmtree(tmp, ignore_errors=True)
    scrivi_json(dest / "_stato.json", {
        "slug": slug,
        "completo": True,
        "con_frame": con_frame,
        "parametri": firma_parametri(soglia),
        "secondi": round(secondi, 1),
        "quando": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
    })
    log("[misura] %-24s FATTO in %.1f s" % (slug, secondi))
    return {"slug": slug, "tec": tec, "sta": sta, "aud": aud, "fra": fra, "secondi": secondi}


# ----------------------------------------------------------------------------
# Indice generale
# ----------------------------------------------------------------------------
def scrivi_indice():
    righe = []
    righe.append("# Misure Fase 1 - indice")
    righe.append("")
    righe.append("Prodotto da `scripts/misura_vsl.py` v%s. Solo numeri." % VERSIONE)
    righe.append("")
    righe.append("| slug | durata | fps | tagli | inquadrature | durata media | mediana | "
                 "I LUFS | silenzi | pause | cambi regime | frame unici |")
    righe.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for d in sorted(MISURE.iterdir()) if MISURE.is_dir() else []:
        if not d.is_dir():
            continue
        try:
            tec = json.loads((d / "tecnica.json").read_text(encoding="utf-8"))
            sta = json.loads((d / "stacchi.json").read_text(encoding="utf-8"))
            aud = json.loads((d / "audio.json").read_text(encoding="utf-8"))
        except Exception:
            continue
        try:
            fra = json.loads((d / "frames" / "manifest.json").read_text(encoding="utf-8"))
            unici = "%d/%d" % (fra["frame_unici_n"], fra["frame_densi_n"])
        except Exception:
            unici = "-"
        st = sta["statistiche_durata_inquadratura"]
        righe.append("| %s | %s | %s | %d | %d | %s s | %s s | %s | %d | %d | %d | %s |" % (
            d.name, tec["durata_hhmmss"], tec["video"]["fps_reale"], sta["tagli_n"],
            sta["inquadrature_n"], st.get("media"), st.get("mediana"),
            aud["ebur128"]["riepilogo"].get("integrata_LUFS"),
            aud["silenzi"]["silenzio_assoluto"]["n"], aud["silenzi"]["pausa_parlato"]["n"],
            len(aud["cambi_di_regime"]), unici))
    righe.append("")
    righe.append("Soglia scene score usata: %.3f. %s" % (
        SOGLIA_SCENA, PARAMETRI_MOTIVAZIONE["soglia_scena"]))
    righe.append("")
    scrivi_testo(MISURE / "_INDICE.md", "\n".join(righe))


# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="FASE 1 EMP-DIOEDIT: misura a macchina dei VSL")
    ap.add_argument("--slug", action="append", default=[],
                    help="slug da misurare (ripetibile)")
    ap.add_argument("--tutti", action="store_true", help="tutti gli slug in sorgenti/")
    ap.add_argument("--forza", action="store_true", help="rifa' anche se gia' completo")
    ap.add_argument("--soglia-scena", type=float, default=SOGLIA_SCENA,
                    help="soglia scene score (default %.3f)" % SOGLIA_SCENA)
    ap.add_argument("--no-frame", action="store_true", help="salta l'estrazione dei frame")
    args = ap.parse_args()

    for exe in ("ffmpeg", "ffprobe"):
        if shutil.which(exe) is None:
            log("[misura] ERRORE: %s non nel PATH" % exe)
            return 2
    try:
        import PIL  # noqa: F401
    except ImportError:
        log("[misura] ERRORE: manca Pillow (pip install --user Pillow)")
        return 2

    slugs = list(args.slug)
    if args.tutti or not slugs:
        slugs = sorted(d.name for d in SORGENTI.iterdir()
                       if d.is_dir() and (d / "video.mp4").is_file())
        # armageddon-home per primo: e' quello su cui si calibra
        if "armageddon-home" in slugs:
            slugs.remove("armageddon-home")
            slugs.insert(0, "armageddon-home")

    log("[misura] versione %s - soglia scena %.3f - %d video" % (
        VERSIONE, args.soglia_scena, len(slugs)))
    log("[misura] sorgenti: %s" % SORGENTI)
    log("[misura] misure:   %s" % MISURE)

    fatti, saltati, falliti = 0, 0, []
    t0 = time.time()
    for s in slugs:
        try:
            esito = misura_video(s, args.soglia_scena, not args.no_frame, args.forza)
            if esito == "saltato":
                saltati += 1
            elif esito:
                fatti += 1
        except Exception as e:
            falliti.append((s, str(e)))
            log("[misura] %-24s FALLITO: %s" % (s, e))

    scrivi_indice()
    log("[misura] ---------------------------------------------")
    log("[misura] completati %d, saltati %d, falliti %d, in %.1f s totali" % (
        fatti, saltati, len(falliti), time.time() - t0))
    for s, e in falliti:
        log("[misura]   FALLITO %s: %s" % (s, e))
    log("[misura] indice: %s" % (MISURE / "_INDICE.md"))
    return 0 if not falliti else 1


if __name__ == "__main__":
    sys.exit(main())
