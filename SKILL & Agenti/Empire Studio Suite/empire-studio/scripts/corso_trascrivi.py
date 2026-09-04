# -*- coding: utf-8 -*-
"""corso_trascrivi.py — tira fuori il parlato da una lezione scaricata.

PERCHE' ESISTE. Su YouTube i sottotitoli arrivano gia' scritti e `yt_ingest.py` li prende
gratis. Il portale di questo corso non ne ha nemmeno uno: misurato il 2026-09-04, zero
tracce di sottotitoli, zero testo della lezione, zero allegati. La conoscenza sta solo nel
parlato e in cio' che appare a schermo — quindi il parlato va ricostruito, o si studierebbe
il corso muto.

SCELTE, e il perche':
  - `faster-whisper` invece di whisper: stessa qualita', molto meno tempo di macchina,
    e gira su CPU senza scheda video dedicata;
  - modello `small` di partenza: sull'italiano parlato chiaro di un tutorial e' sufficiente,
    e `medium` costerebbe circa il triplo del tempo per un guadagno che su questo materiale
    non si vede. Si puo' alzare con `--modello`;
  - audio estratto a 16 kHz mono: e' il formato che il riconoscitore vuole, e uno stereo a
    48 kHz sarebbe cinque volte piu' pesante senza aggiungere una parola;
  - ogni riga porta il MINUTO: senza il tempo, una trascrizione non e' citabile, e una
    conoscenza non citabile in questa casa non vale niente (tracciabilita' P12).

USO
    python corso_trascrivi.py --lezione <lesson_id>
    python corso_trascrivi.py --lezione <lesson_id> --modello medium
"""

import argparse
import io
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
RUNS = os.path.join(STUDIO, "runs", "corso-aitubepro")


def mmss(secondi):
    return "%02d:%02d" % (int(secondi) // 60, int(secondi) % 60)


def estrai_audio(mp4, wav):
    """16 kHz mono: il formato che il riconoscitore si aspetta."""
    if os.path.exists(wav) and os.path.getsize(wav) > 10000:
        return True
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", mp4,
           "-vn", "-ac", "1", "-ar", "16000", "-f", "wav", wav]
    return subprocess.run(cmd).returncode == 0 and os.path.exists(wav)


def trascrivi(lesson_id, modello="small"):
    cartella = os.path.join(RUNS, lesson_id)
    mp4 = os.path.join(cartella, "video.mp4")
    wav = os.path.join(cartella, "audio.wav")
    fuori_txt = os.path.join(cartella, "parlato.txt")
    fuori_json = os.path.join(cartella, "parlato.json")

    if not os.path.exists(mp4):
        print("[!] Video assente: scarica prima la lezione con corso_ingest.py.")
        return 1
    if os.path.exists(fuori_txt) and os.path.getsize(fuori_txt) > 500:
        print("[=] Parlato gia' presente: non rifaccio niente.")
        return 0

    print("[1/3] Estraggo l'audio ...")
    if not estrai_audio(mp4, wav):
        print("[!] Estrazione audio fallita.")
        return 1

    print("[2/3] Carico il riconoscitore (%s) ..." % modello)
    # Il trasferimento accelerato di HuggingFace (Xet) ha fatto morire il primo scaricamento
    # del modello con "CAS Client Error: error decoding response body" — misurato il
    # 2026-09-04. Il canale classico e' piu' lento a scaricare ma arriva in fondo, e questo
    # costo si paga una volta sola per tutte le lezioni.
    os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
    from faster_whisper import WhisperModel
    # int8 su CPU: la scelta che rende praticabili 167 lezioni su una macchina senza GPU.
    riconoscitore = WhisperModel(modello, device="cpu", compute_type="int8")

    print("[3/3] Trascrivo ...")
    t0 = time.time()
    segmenti, info = riconoscitore.transcribe(wav, language="it", vad_filter=True,
                                              beam_size=5)
    righe, blocchi, parole = [], [], 0
    for s in segmenti:
        testo = (s.text or "").strip()
        if not testo:
            continue
        parole += len(testo.split())
        righe.append("[%s] %s" % (mmss(s.start), testo))
        blocchi.append({"inizio": round(s.start, 2), "fine": round(s.end, 2), "testo": testo})

    durata = info.duration or 0
    with io.open(fuori_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(righe))
    with io.open(fuori_json, "w", encoding="utf-8") as f:
        json.dump({"lesson_id": lesson_id, "modello": modello,
                   "durata_s": round(durata, 1), "parole": parole,
                   "blocchi": blocchi}, f, ensure_ascii=False, indent=2)

    minuti = max(durata / 60.0, 0.01)
    ppm = parole / minuti
    impiegato = time.time() - t0
    print("\n[+] Parlato: %s" % fuori_txt)
    print("    %d parole in %d blocchi · %.0f parole/minuto · %.0f s di lavoro (%.1fx il video)"
          % (parole, len(blocchi), ppm, impiegato, impiegato / max(durata, 1)))

    # Criterio di FATTO del passo 2 (piano §6.1): sotto le 60 parole/minuto non e' una
    # lezione silenziosa, e' una trascrizione fallita — e va detto, non subito.
    if ppm < 60:
        print("[!] ATTENZIONE: %.0f parole/minuto, sotto la soglia di 60. La trascrizione "
              "NON e' affidabile: alza il modello (--modello medium) prima di studiarla." % ppm)
        return 2

    stato_path = os.path.join(cartella, "stato.json")
    stato = {}
    if os.path.exists(stato_path):
        with io.open(stato_path, encoding="utf-8") as f:
            stato = json.load(f)
    stato.update({"passo": "2-trascritto", "parole": parole,
                  "parole_al_minuto": round(ppm), "modello": modello})
    with io.open(stato_path, "w", encoding="utf-8") as f:
        json.dump(stato, f, ensure_ascii=False, indent=2)

    try:
        os.remove(wav)  # l'audio grezzo non serve piu': pesa e non si cita
    except OSError:
        pass
    return 0


def main():
    ap = argparse.ArgumentParser(description="Trascrive il parlato di una lezione scaricata.")
    ap.add_argument("--lezione", required=True)
    ap.add_argument("--modello", default="small",
                    choices=["tiny", "base", "small", "medium", "large-v3"])
    a = ap.parse_args()
    return trascrivi(a.lezione, a.modello)


if __name__ == "__main__":
    sys.exit(main())
