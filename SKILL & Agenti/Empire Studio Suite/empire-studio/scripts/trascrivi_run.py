# -*- coding: utf-8 -*-
"""trascrivi_run.py — ricostruisce il parlato di un run che non ha sottotitoli.

PERCHE' ESISTE. `yt_ingest.py` prende i sottotitoli gratis quando YouTube li ha.
Su `max18-v09` (AGENTI VOCALI IN CLAUDE CODE, 133 minuti) yt-dlp risponde
"has no automatic captions / has no subtitles": verificato il 2026-09-06. Senza
questo script quel corso si studierebbe muto, con i soli frame.

SCELTE, e il perche' (le stesse di corso_trascrivi.py, per non avere due dottrine):
  - `faster-whisper`: stessa qualita' di whisper, molto meno tempo di macchina, gira su CPU;
  - modello `small` di partenza: sull'italiano parlato chiaro di un tutorial basta;
  - audio 16 kHz mono: e' cio' che il riconoscitore vuole; lo stereo a 48 kHz peserebbe
    cinque volte tanto senza aggiungere una parola;
  - ogni riga porta il tempo in `[HH:MM:SS]`, identico al formato che `vtt_to_transcript.py`
    produce dai sottotitoli: le slice e le sentinelle non devono accorgersi della differenza.

USO
    python scripts/trascrivi_run.py --run max18-v09-NmoOZVTrTXA
    python scripts/trascrivi_run.py --run <run-id> --modello medium
"""
import argparse, json, os, subprocess, sys, time

NL = chr(10)
HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(os.path.dirname(HERE), "runs")


def log(m):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), m), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--modello", default="small")
    a = ap.parse_args()

    base = os.path.join(RUNS, a.run)
    if not os.path.isdir(base):
        sys.exit("run inesistente: %s" % base)

    out = os.path.join(base, "transcript.md")
    if os.path.exists(out) and os.path.getsize(out) > 2000:
        log("transcript.md gia' presente (%d KB): non lo rifaccio." % (os.path.getsize(out) // 1024))
        return

    ing = json.load(open(os.path.join(base, "ingest.json"), encoding="utf-8"))
    url = ing.get("url") or "https://www.youtube.com/watch?v=%s" % ing["id"]

    # 1. audio sorgente: si scarica la sola traccia audio, non il video
    m4a = os.path.join(base, "audio.m4a")
    if not os.path.exists(m4a):
        log("scarico la traccia audio di %s" % ing["id"])
        r = subprocess.run([sys.executable, "-m", "yt_dlp", "-f", "bestaudio",
                            "-o", m4a, "--no-playlist", url])
        if r.returncode != 0 or not os.path.exists(m4a):
            sys.exit("download audio fallito")
    log("audio: %.1f MB" % (os.path.getsize(m4a) / 1048576.0))

    # 2. formato che il riconoscitore vuole
    wav = os.path.join(base, "audio-16k.wav")
    if not os.path.exists(wav):
        log("converto a 16 kHz mono")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", m4a,
                        "-ac", "1", "-ar", "16000", wav], check=True)
    log("wav: %.1f MB" % (os.path.getsize(wav) / 1048576.0))

    # 3. riconoscimento
    from faster_whisper import WhisperModel
    log("carico il modello %s" % a.modello)
    model = WhisperModel(a.modello, device="cpu", compute_type="int8")
    segmenti, info = model.transcribe(wav, language="it", vad_filter=True,
                                      beam_size=5, condition_on_previous_text=False)
    log("durata riconosciuta: %d minuti" % (info.duration // 60))

    # si scrive man mano: se la macchina cade, il lavoro fatto resta
    parziale = out + ".parziale"
    n = 0
    with open(parziale, "w", encoding="utf-8") as f:
        f.write(NL)
        for s in segmenti:
            t = int(s.start)
            f.write("[%02d:%02d:%02d] %s%s" % (t // 3600, (t % 3600) // 60, t % 60, s.text.strip(), NL))
            n += 1
            if n % 50 == 0:
                f.flush()
                log("  %d righe (minuto %d)" % (n, t // 60))
    os.replace(parziale, out)
    log("scritto %s — %d righe" % (out, n))


if __name__ == "__main__":
    main()
