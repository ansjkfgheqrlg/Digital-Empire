# -*- coding: utf-8 -*-
"""parlato_misura.py -- FASE 3 dello studio EMP-DIOEDIT: il parlato, con i tempi.

REGOLA MADRE: la macchina misura, l'occhio giudica. Qui NON si interpreta niente.
Ogni riga di output e' o testo letterale detto nel video, o un numero misurato.

COSA FA, in ordine:
  1. estrae l'audio a 16 kHz mono (formato che il riconoscitore vuole);
  2. trascrive con faster-whisper IN LOCALE, con timestamp per segmento E per parola
     (nessun audio lascia questa macchina: il modello e' gia' in cache su disco);
  3. misura i silenzi sull'onda grezza con silencedetect di ffmpeg, a due soglie;
  4. misura il profilo di loudness momentaneo (EBU R128, campione ogni 100 ms);
  5. incrocia: pause fra le parole, parole al minuto minuto per minuto, loudness
     media di ogni segmento parlato e quali segmenti stanno sopra la mediana.

USO
    python parlato_misura.py --slug armageddon-home
    python parlato_misura.py --tutti
    python parlato_misura.py --tutti --modello base
"""

import argparse
import json
import os
import re
import subprocess
import sys
import statistics
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.dirname(HERE)                      # .../vsl-study
SORGENTI = os.path.join(STUDY, "sorgenti")
PARLATO = os.path.join(STUDY, "parlato")
# i wav sono materiale di lavorazione, non di studio: stanno fuori dal repo
TMP = os.environ.get("VSL_TMP") or os.path.join(os.environ.get("TEMP", "."), "vsl-parlato")

# soglia oltre la quale una pausa viene contata nel sommario
PAUSA_MIN = 0.5


def tc(s):
    """secondi -> mm:ss.cc"""
    if s is None:
        return "--:--.--"
    m = int(s) // 60
    r = s - m * 60
    return "%02d:%05.2f" % (m, r)


def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          universal_newlines=True, errors="replace")


# ---------------------------------------------------------------- audio grezzo

def estrai_audio(mp4, wav):
    if os.path.exists(wav) and os.path.getsize(wav) > 10000:
        return True
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", mp4,
           "-vn", "-ac", "1", "-ar", "16000", "-f", "wav", wav]
    return run(cmd).returncode == 0 and os.path.exists(wav)


def durata_media(mp4):
    p = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", mp4])
    try:
        return float(p.stdout.strip().splitlines()[0])
    except Exception:
        return None


RE_SIL_START = re.compile(r"silence_start:\s*(-?[\d.]+)")
RE_SIL_END = re.compile(r"silence_end:\s*(-?[\d.]+)\s*\|\s*silence_duration:\s*([\d.]+)")


def silenzi(wav, soglia_db, d=0.30):
    """silencedetect sull'onda grezza. Ritorna [{inizio,fine,durata}]."""
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", wav,
             "-af", "silencedetect=n=%ddB:d=%.2f" % (soglia_db, d),
             "-f", "null", "-"])
    fuori, aperto = [], None
    for riga in p.stdout.splitlines():
        m = RE_SIL_START.search(riga)
        if m:
            aperto = float(m.group(1))
            continue
        m = RE_SIL_END.search(riga)
        if m and aperto is not None:
            fine, dur = float(m.group(1)), float(m.group(2))
            fuori.append({"inizio": round(max(0.0, aperto), 2),
                          "fine": round(fine, 2), "durata": round(dur, 2)})
            aperto = None
    return fuori


RE_MEAN = re.compile(r"mean_volume:\s*(-?[\d.]+)\s*dB")
RE_MAX = re.compile(r"max_volume:\s*(-?[\d.]+)\s*dB")


def volume_medio(wav):
    """volumedetect: livello medio e di picco dell'intera traccia, in dBFS.
    Serve a fissare una soglia di silenzio RELATIVA a questo audio, invece che
    una soglia assoluta che su una traccia gia' normalizzata non trova niente."""
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", wav,
             "-af", "volumedetect", "-f", "null", "-"])
    mean = mx = None
    for riga in p.stdout.splitlines():
        m = RE_MEAN.search(riga)
        if m:
            mean = float(m.group(1))
        m = RE_MAX.search(riga)
        if m:
            mx = float(m.group(1))
    return mean, mx


RE_FRAME = re.compile(r"pts_time:([\d.]+)")
RE_M = re.compile(r"lavfi\.r128\.M=(-?[\d.]+)")


def loudness(wav):
    """EBU R128: loudness momentanea (finestra 400 ms) campionata ogni 100 ms.

    NOTA DI METODO: in ffmpeg 8 il log per-frame di `framelog=verbose` non esce piu'
    su stderr (misurato il 2026-09-10, ffmpeg 8.1.1). I valori si prendono dai
    metadati del filtro con `ametadata=print`, che e' anche una fonte piu' pulita:
    coppia deterministica pts_time / lavfi.r128.M, niente testo da indovinare.
    """
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-loglevel", "error", "-i", wav,
             "-af", "ebur128=metadata=1,ametadata=mode=print:key=lavfi.r128.M:file=-",
             "-f", "null", "-"])
    serie, t = [], None
    for riga in p.stdout.splitlines():
        m = RE_FRAME.search(riga)
        if m:
            t = float(m.group(1))
            continue
        m = RE_M.search(riga)
        if m and t is not None:
            mv = float(m.group(1))
            if mv < -70:            # silenzio digitale / finestra non ancora piena
                mv = -70.0
            serie.append((round(t, 2), round(mv, 1)))
            t = None
    return serie


def loudness_media(serie, a, b):
    """media aritmetica dei campioni M nell'intervallo [a,b]. LU, non energia:
    e' una media di valori gia' logaritmici, e va dichiarata come tale."""
    v = [m for t, m in serie if a <= t <= b]
    if not v:
        return None
    return round(sum(v) / len(v), 1)


# ------------------------------------------------------------- riconoscimento

def trascrivi(wav, modello):
    os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")     # nulla esce da questa macchina
    from faster_whisper import WhisperModel
    mdl = WhisperModel(modello, device="cpu", compute_type="int8")
    segs, info = mdl.transcribe(
        wav, language="it", vad_filter=True, word_timestamps=True,
        beam_size=5, condition_on_previous_text=False,
        vad_parameters={"min_silence_duration_ms": 400},
    )
    fuori = []
    for i, s in enumerate(segs):
        parole = []
        for w in (s.words or []):
            parole.append({"p": w.word.strip(),
                           "inizio": round(w.start, 2), "fine": round(w.end, 2)})
        fuori.append({"i": i,
                      "inizio": round(s.start, 2), "fine": round(s.end, 2),
                      "durata": round(s.end - s.start, 2),
                      "testo": s.text.strip(), "parole": parole})
        sys.stdout.write("\r    segmenti: %d  (fino a %s)" % (i + 1, tc(s.end)))
        sys.stdout.flush()
    print("")
    return fuori, info


# ------------------------------------------------------------------ incroci

def pause_da_parlato(segmenti, dur_tot):
    """buchi fra la fine di una parola e l'inizio della successiva, sull'intero video,
    piu' l'attacco iniziale e la coda finale."""
    parole = []
    for s in segmenti:
        parole.extend(s["parole"] or [])
    parole.sort(key=lambda w: w["inizio"])
    pause = []
    if parole:
        if parole[0]["inizio"] > 0.05:
            pause.append({"inizio": 0.0, "fine": parole[0]["inizio"],
                          "durata": round(parole[0]["inizio"], 2), "tipo": "attacco"})
        for a, b in zip(parole, parole[1:]):
            g = b["inizio"] - a["fine"]
            if g > 0.05:
                pause.append({"inizio": round(a["fine"], 2), "fine": round(b["inizio"], 2),
                              "durata": round(g, 2), "tipo": "interna",
                              "dopo": a["p"], "prima_di": b["p"]})
        if dur_tot and dur_tot - parole[-1]["fine"] > 0.05:
            pause.append({"inizio": round(parole[-1]["fine"], 2), "fine": round(dur_tot, 2),
                          "durata": round(dur_tot - parole[-1]["fine"], 2), "tipo": "coda"})
    return parole, pause


def wpm_per_minuto(parole, dur_tot):
    if not dur_tot:
        return []
    fuori = []
    n = int(dur_tot // 60) + 1
    for k in range(n):
        a, b = k * 60.0, min((k + 1) * 60.0, dur_tot)
        span = b - a
        if span <= 0:
            continue
        dentro = [w for w in parole if a <= w["inizio"] < b]
        voce = sum(min(w["fine"], b) - max(w["inizio"], a) for w in dentro) if dentro else 0.0
        fuori.append({
            "minuto": k,
            "da": round(a, 2), "a": round(b, 2),
            "parole": len(dentro),
            "parole_al_minuto": round(len(dentro) * 60.0 / span, 1),
            "secondi_di_voce": round(voce, 2),
            "densita_voce_pct": round(100.0 * voce / span, 1),
        })
    return fuori


def densita_segmenti(segmenti, dur_tot):
    """misura che vive anche senza trascrizione: quanto dell'audio e' segmento vocale."""
    voce = sum(s["durata"] for s in segmenti)
    return {
        "segmenti_vocali": len(segmenti),
        "secondi_di_parlato": round(voce, 2),
        "percentuale_di_parlato": round(100.0 * voce / dur_tot, 1) if dur_tot else None,
        "segmenti_al_minuto": round(len(segmenti) * 60.0 / dur_tot, 2) if dur_tot else None,
        "durata_media_segmento_s": round(voce / len(segmenti), 2) if segmenti else None,
    }


# ------------------------------------------------------------------- scrittura

def scrivi_md(path, slug, modello, info, segmenti, dur_tot):
    r = []
    r.append("# Trascrizione con tempi -- `%s`\n" % slug)
    r.append("**Strumento:** faster-whisper `%s`, in locale su CPU (nessun audio inviato fuori). "
             "**Lingua:** %s. **Durata media:** %s.\n"
             % (modello,
                (getattr(info, "language", "it") if info else "it"),
                tc(dur_tot)))
    r.append("Testo LETTERALE, nessuna correzione, nessuna interpretazione. "
             "Formato: `[inizio -> fine]` in `mm:ss.cc`.\n")
    r.append("---\n")
    for s in segmenti:
        r.append("**[%s -> %s]** %s\n" % (tc(s["inizio"]), tc(s["fine"]), s["testo"]))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(r))


def scrivi_sommario(path, slug, dati, segmenti, dur_tot):
    pause = dati["pause_dal_parlato"]
    lunghe = [p for p in pause if p["durata"] >= PAUSA_MIN]
    piu_lunga = max(pause, key=lambda p: p["durata"]) if pause else None
    d = dati["densita"]
    r = []
    r.append("# Sommario del parlato -- `%s`\n" % slug)
    r.append("Solo misure e testo letterale. Nessun giudizio: quello arriva in Fase 4.\n")
    r.append("| misura | valore |")
    r.append("|---|---|")
    r.append("| durata del video | %s (%.2f s) |" % (tc(dur_tot), dur_tot))
    r.append("| durata totale del parlato | %s (%.2f s) |"
             % (tc(d["secondi_di_parlato"]), d["secondi_di_parlato"]))
    r.append("| percentuale di parlato | %s%% |" % d["percentuale_di_parlato"])
    r.append("| segmenti vocali | %d (%.2f al minuto) |"
             % (d["segmenti_vocali"], d["segmenti_al_minuto"]))
    r.append("| parole totali | %d |" % dati["parole_totali"])
    r.append("| parole al minuto (su tutto il video) | %s |" % dati["parole_al_minuto_medie"])
    r.append("| parole al minuto (sul solo parlato) | %s |" % dati["parole_al_minuto_sul_solo_parlato"])
    r.append("| pause sopra %.1f s | %d |" % (PAUSA_MIN, len(lunghe)))
    if piu_lunga:
        r.append("| pausa piu' lunga | **%.2f s** a %s -> %s (%s) |"
                 % (piu_lunga["durata"], tc(piu_lunga["inizio"]), tc(piu_lunga["fine"]),
                    piu_lunga.get("tipo", "interna")))
    r.append("| volume medio / massimo della traccia | %s / %s dBFS |"
             % (dati["volume_medio_dBFS"], dati["volume_massimo_dBFS"]))
    r.append("| silenzi grezzi -30 dBFS (>=0,30 s) | %d |" % len(dati["silenzi_-30dB"]))
    r.append("| silenzi grezzi -40 dBFS (>=0,30 s) | %d |" % len(dati["silenzi_-40dB"]))
    r.append("| silenzi a soglia relativa (%s dBFS, >=0,30 s) | %d |"
             % (dati["soglia_relativa_dB"], len(dati["silenzi_soglia_relativa"])))
    if dati.get("loudness"):
        L = dati["loudness"]
        r.append("| loudness mediana dei segmenti parlati | %s LUFS-M |" % L["mediana_segmenti_LUFS_M"])
        r.append("| picco momentaneo | %s LUFS-M a %s |"
                 % (L["picco_momentaneo_LUFS_M"], tc(L["picco_a_secondo"])))
        r.append("| segmenti sopra la mediana di +3 LU o piu' | %d |" % len(L["sopra_mediana_3LU"]))
    r.append("")

    r.append("## Le dieci pause piu' lunghe\n")
    r.append("| # | inizio | durata | dopo la parola | prima della parola |")
    r.append("|---|---|---|---|---|")
    for i, p in enumerate(sorted(pause, key=lambda x: -x["durata"])[:10], 1):
        r.append("| %d | %s | %.2f s | %s | %s |"
                 % (i, tc(p["inizio"]), p["durata"],
                    ("`%s`" % p["dopo"]) if p.get("dopo") else "-- (%s)" % p.get("tipo", ""),
                    ("`%s`" % p["prima_di"]) if p.get("prima_di") else "-- (%s)" % p.get("tipo", "")))
    r.append("")

    if dati.get("loudness") and dati["loudness"]["sopra_mediana_3LU"]:
        r.append("## Dove la voce sale -- segmenti a +3 LU o piu' sopra la mediana\n")
        r.append("| inizio | LUFS-M | delta | testo letterale |")
        r.append("|---|---|---|---|")
        for s in sorted(dati["loudness"]["sopra_mediana_3LU"],
                        key=lambda x: -x["delta_LU"])[:15]:
            r.append("| %s | %s | +%.1f LU | %s |"
                     % (tc(s["inizio"]), s["LUFS_M"], s["delta_LU"], s["testo"]))
        r.append("")

    r.append("## Come apre -- primi 15 secondi, testuali\n")
    ap = [s for s in segmenti if s["inizio"] < 15.0]
    if ap:
        for s in ap:
            r.append("**[%s -> %s]** %s\n" % (tc(s["inizio"]), tc(s["fine"]), s["testo"]))
    else:
        r.append("_Nessun parlato nei primi 15 secondi._\n")

    r.append("## Come chiude -- ultimi 20 secondi, testuali\n")
    ch = [s for s in segmenti if s["fine"] > dur_tot - 20.0]
    if ch:
        for s in ch:
            r.append("**[%s -> %s]** %s\n" % (tc(s["inizio"]), tc(s["fine"]), s["testo"]))
    else:
        r.append("_Nessun parlato negli ultimi 20 secondi._\n")

    r.append("## Ritmo minuto per minuto\n")
    r.append("| minuto | parole | parole/min | secondi di voce | densita' voce |")
    r.append("|---|---|---|---|---|")
    for m in dati["wpm_per_minuto"]:
        r.append("| %02d:00 | %d | %.1f | %.2f s | %.1f%% |"
                 % (m["minuto"], m["parole"], m["parole_al_minuto"],
                    m["secondi_di_voce"], m["densita_voce_pct"]))
    r.append("")
    r.append("---")
    r.append("Fonte: `sorgenti/%s/video.mp4`. Misure: `ritmo-parlato.json`. "
             "Testo integrale: `trascrizione.md` / `trascrizione.json`." % slug)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(r))


# ---------------------------------------------------------------------- corpo

def lavora(slug, modello="small", rifai=False):
    mp4 = os.path.join(SORGENTI, slug, "video.mp4")
    if not os.path.exists(mp4):
        print("[!] %s: video assente" % slug)
        return 1
    fuori = os.path.join(PARLATO, slug)
    os.makedirs(fuori, exist_ok=True)
    os.makedirs(TMP, exist_ok=True)
    f_json = os.path.join(fuori, "trascrizione.json")
    f_md = os.path.join(fuori, "trascrizione.md")
    f_ritmo = os.path.join(fuori, "ritmo-parlato.json")
    f_som = os.path.join(fuori, "_SOMMARIO.md")

    if not rifai and all(os.path.exists(p) and os.path.getsize(p) > 400
                         for p in (f_json, f_md, f_ritmo, f_som)):
        print("[=] %s: gia' fatto, non tocco niente." % slug)
        return 0

    t0 = time.time()
    print("[%s] 1/5 audio 16 kHz mono ..." % slug)
    wav = os.path.join(TMP, slug + ".wav")
    if not estrai_audio(mp4, wav):
        print("[!] %s: estrazione audio fallita" % slug)
        return 1
    dur_tot = durata_media(mp4) or 0.0

    info = None
    riuso = (not rifai) and os.path.exists(f_json) and os.path.getsize(f_json) > 400
    if riuso:
        with open(f_json, encoding="utf-8") as f:
            vecchio = json.load(f)
        segmenti = vecchio["segmenti"]
        lingua = vecchio.get("lingua", "it")
        print("[%s] 2/5 trascrizione gia' su disco: riuso, non rifaccio." % slug)
    else:
        print("[%s] 2/5 trascrizione locale (faster-whisper %s) ..." % (slug, modello))
        segmenti, info = trascrivi(wav, modello)
        lingua = getattr(info, "language", "it")

    print("[%s] 3/5 silenzi grezzi (silencedetect, tre soglie) ..." % slug)
    sil30 = silenzi(wav, -30)
    sil40 = silenzi(wav, -40)
    v_mean, v_max = volume_medio(wav)
    soglia_rel = int(round(v_mean - 18)) if v_mean is not None else -35
    sil_rel = silenzi(wav, soglia_rel)

    print("[%s] 4/5 profilo di loudness (EBU R128) ..." % slug)
    serie = loudness(wav)

    print("[%s] 5/5 incroci e scrittura ..." % slug)
    parole, pause = pause_da_parlato(segmenti, dur_tot)
    wpm = wpm_per_minuto(parole, dur_tot)
    dens = densita_segmenti(segmenti, dur_tot)

    L = None
    if serie:
        for s in segmenti:
            s["loudness_M_media"] = loudness_media(serie, s["inizio"], s["fine"])
        val = [s["loudness_M_media"] for s in segmenti if s.get("loudness_M_media") is not None]
        med = round(statistics.median(val), 1) if val else None
        sopra = []
        if med is not None:
            for s in segmenti:
                v = s.get("loudness_M_media")
                if v is not None and v - med >= 3.0:
                    sopra.append({"i": s["i"], "inizio": s["inizio"], "fine": s["fine"],
                                  "LUFS_M": v, "delta_LU": round(v - med, 1),
                                  "testo": s["testo"]})
        picco = max(serie, key=lambda x: x[1])
        L = {
            "nota": "loudness momentanea EBU R128 (finestra 400 ms), campionata ogni 100 ms; "
                    "media per segmento = media aritmetica dei campioni M dentro il segmento",
            "campioni": len(serie),
            "mediana_segmenti_LUFS_M": med,
            "picco_momentaneo_LUFS_M": picco[1],
            "picco_a_secondo": picco[0],
            "sopra_mediana_3LU": sopra,
            "profilo_per_secondo": [{"t": t, "M": m} for t, m in serie
                                    if abs(t - round(t)) < 0.051],
        }

    n_parole = len(parole)
    dati = {
        "slug": slug,
        "fonte": "sorgenti/%s/video.mp4" % slug,
        "generato": time.strftime("%Y-%m-%d %H:%M"),
        "strumento_trascrizione": "faster-whisper %s, CPU int8, in locale (HF_HUB_OFFLINE=1)" % modello,
        "durata_video_s": round(dur_tot, 2),
        "densita": dens,
        "parole_totali": n_parole,
        "parole_al_minuto_medie": round(n_parole * 60.0 / dur_tot, 1) if dur_tot else None,
        "parole_al_minuto_sul_solo_parlato": (
            round(n_parole * 60.0 / dens["secondi_di_parlato"], 1)
            if dens["secondi_di_parlato"] else None),
        "wpm_per_minuto": wpm,
        "pause_sopra_0_5s": len([p for p in pause if p["durata"] >= PAUSA_MIN]),
        "pause_dal_parlato": pause,
        "volume_medio_dBFS": v_mean,
        "volume_massimo_dBFS": v_max,
        "silenzi_-30dB": sil30,
        "silenzi_-40dB": sil40,
        "soglia_relativa_dB": soglia_rel,
        "silenzi_soglia_relativa": sil_rel,
        "nota_silenzi": "silencedetect di ffmpeg, durata minima 0,30 s, tre soglie: due assolute "
                        "(-30 e -40 dBFS) e una relativa a questo audio (volume medio meno 18 dB). "
                        "Sotto una base musicale continua le soglie assolute possono restituire zero "
                        "silenzi: e' un dato, non un errore, e per questo c'e' la soglia relativa.",
        "loudness": L,
    }

    with open(f_json, "w", encoding="utf-8") as f:
        json.dump({"slug": slug,
                   "strumento": dati["strumento_trascrizione"],
                   "lingua": lingua,
                   "lingua_probabilita": (round(getattr(info, "language_probability", 0.0) or 0.0, 3)
                                          if info else None),
                   "durata_video_s": round(dur_tot, 2),
                   "segmenti": segmenti}, f, ensure_ascii=False, indent=1)
    with open(f_ritmo, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=1)
    scrivi_md(f_md, slug, modello, info, segmenti, dur_tot)
    scrivi_sommario(f_som, slug, dati, segmenti, dur_tot)

    print("[ok] %s -- %d segmenti, %d parole, %d pause >=%.1fs, video %.0f s, macchina %.0f s"
          % (slug, len(segmenti), n_parole, dati["pause_sopra_0_5s"], PAUSA_MIN,
             dur_tot, time.time() - t0))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--tutti", action="store_true")
    ap.add_argument("--modello", default="small")
    ap.add_argument("--rifai", action="store_true")
    a = ap.parse_args()
    if a.tutti:
        slugs = sorted(d for d in os.listdir(SORGENTI)
                       if os.path.isdir(os.path.join(SORGENTI, d)))
    elif a.slug:
        slugs = [a.slug]
    else:
        print("serve --slug o --tutti")
        return 2
    rc = 0
    for s in slugs:
        rc |= lavora(s, a.modello, a.rifai)
    return rc


if __name__ == "__main__":
    sys.exit(main())
