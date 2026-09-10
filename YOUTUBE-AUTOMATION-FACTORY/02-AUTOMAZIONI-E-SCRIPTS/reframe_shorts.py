#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regola che ordina questo script: A4-RC-10
(company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/RIPASSO_COSTRUTTIVO.py).

Buco che chiude, misurato sulla fabbrica: oggi la fabbrica genera UN formato per canale e non
riusa MAI un video orizzontale gia' esportato per ricavarne varianti verticali brevi
(build_candidate_pool.py e fliki_client.py non hanno alcuna logica di reframe). Da un video
lungo gia' prodotto si puo' ricavare un 9:16 con costo API aggiuntivo pari a zero (niente
rigenerazione da Fliki): oggi questa capacita' non esiste, non e' uno strumento diverso per
fare la stessa cosa.

COME FUNZIONA: individua il soggetto per fotogramma (mediapipe se installato, altrimenti Haar
cascade di opencv — nessun editor aperto a mano), calcola un centro-inquadratura stabilizzato
nel tempo (media mobile per evitare jitter) e produce un ritaglio verticale via ffmpeg (filtro
`crop` con posizione X espressa come funzione del tempo, poi `scale` alla risoluzione finale).

NON E' ANCORA AGGANCIATO: nessun file esistente (apex7_orchestrator.py, fliki_client.py,
build_candidate_pool.py, youtube_uploader_playwright.py) importa o chiama questo script.
L'aggancio avviene al gate di categoria (ADR-029).

Uso da riga di comando:
  python reframe_shorts.py --aiuto
  python reframe_shorts.py --input video-orizzontale.mp4 --output shorts/variante-01.mp4

Uso come libreria:
  from reframe_shorts import reframe_verticale
  risultato = reframe_verticale("video-orizzontale.mp4", "shorts/variante-01.mp4")
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

_HAS_CV2 = False
try:
    import cv2  # type: ignore
    _HAS_CV2 = True
except ImportError:
    cv2 = None  # type: ignore

_HAS_MEDIAPIPE = False
try:
    import mediapipe as mp  # type: ignore
    _HAS_MEDIAPIPE = True
except ImportError:
    mp = None  # type: ignore


def verifica_dipendenze() -> None:
    """
    Controlla che ffmpeg e opencv (il minimo indispensabile) siano presenti. Se manca
    qualcosa lo dice con un messaggio chiaro e si ferma — non prova a produrre un ritaglio
    a meta'.
    """
    mancanti = []
    if shutil.which("ffmpeg") is None:
        mancanti.append("ffmpeg (eseguibile non trovato nel PATH di sistema)")
    if not _HAS_CV2:
        mancanti.append("opencv-python (pip install opencv-python)")
    if mancanti:
        raise SystemExit(
            "[STOP] Dipendenze mancanti per reframe_shorts.py:\n  - " + "\n  - ".join(mancanti) +
            "\nInstalla quanto manca e rilancia. mediapipe e' opzionale (se assente si usa "
            "il rilevamento volti di opencv, gia' presente)."
        )


def _rileva_centro_soggetto(frame, cascade=None, mp_detector=None):
    """
    Ritorna (centro_x_in_pixel, trovato: bool) del soggetto principale nel fotogramma.
    Preferisce mediapipe se disponibile (piu' robusto), altrimenti Haar cascade di opencv.
    Se nessun soggetto e' rilevato, ritorna il centro geometrico del frame come ripiego.
    """
    altezza, larghezza = frame.shape[:2]
    if mp_detector is not None:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        risultato = mp_detector.process(rgb)
        if risultato.detections:
            migliore = max(
                risultato.detections,
                key=lambda d: d.location_data.relative_bounding_box.width
                * d.location_data.relative_bounding_box.height,
            )
            bbox = migliore.location_data.relative_bounding_box
            cx = (bbox.xmin + bbox.width / 2) * larghezza
            return cx, True
        return larghezza / 2, False

    if cascade is not None and not cascade.empty():
        grigio = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dimensione_min = max(20, larghezza // 20)
        volti = cascade.detectMultiScale(
            grigio, scaleFactor=1.2, minNeighbors=5, minSize=(dimensione_min, dimensione_min)
        )
        if len(volti) > 0:
            x, y, fw, fh = max(volti, key=lambda b: b[2] * b[3])
            cx = x + fw / 2
            return cx, True
        return larghezza / 2, False

    return larghezza / 2, False


def _media_mobile(valori: list[float], finestra: int) -> list[float]:
    """Media mobile centrata, usata per stabilizzare il centro del soggetto nel tempo."""
    n = len(valori)
    if finestra <= 1 or n <= 1:
        return list(valori)
    meta = finestra // 2
    return [
        sum(valori[max(0, i - meta):min(n, i + meta + 1)]) / len(valori[max(0, i - meta):min(n, i + meta + 1)])
        for i in range(n)
    ]


def _comprimi_segmenti(campioni: list, soglia_px: float = 8.0) -> list:
    """
    Unisce campioni consecutivi con crop_x quasi identico in segmenti [tempo_inizio, crop_x]:
    accorcia l'espressione ffmpeg che descrive il movimento del ritaglio nel tempo.
    """
    segmenti = []
    for tempo_s, crop_x, _ in campioni:
        if segmenti and abs(crop_x - segmenti[-1][1]) <= soglia_px:
            continue
        segmenti.append([tempo_s, crop_x])
    return segmenti


def _costruisci_espressione_ffmpeg(segmenti: list) -> str:
    """
    Costruisce l'espressione ffmpeg 'if(lt(t,T),X,...)' annidata che sposta la finestra di
    ritaglio nel tempo secondo i segmenti calcolati. Con un solo segmento e' semplicemente
    la costante X (ritaglio statico).
    """
    if len(segmenti) == 1:
        return str(segmenti[0][1])
    espressione = str(segmenti[-1][1])
    for i in range(len(segmenti) - 2, -1, -1):
        soglia_t = segmenti[i + 1][0]
        valore_x = segmenti[i][1]
        espressione = f"if(lt(t,{soglia_t:.3f}),{valore_x},{espressione})"
    return espressione


def reframe_verticale(
    input_path: str,
    output_path: str,
    campioni_al_secondo: float = 2.0,
    larghezza_uscita: int = 1080,
    altezza_uscita: int = 1920,
    smoothing: int = 5,
    log=print,
) -> dict:
    """
    Produce un ritaglio verticale 9:16 da un MP4 orizzontale gia' esportato, tenendo il
    soggetto rilevato a centro-inquadratura. Nessuna rigenerazione da Fliki: costo API zero.

    Ritorna un dict con statistiche (campioni analizzati, percentuale di rilevazione,
    durata, risoluzione di uscita) — utile per decidere se il risultato va controllato a
    mano prima di usarlo.
    """
    verifica_dipendenze()
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File sorgente non trovato: {input_path}")

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise RuntimeError(f"Impossibile aprire il video con OpenCV: {input_path}")

    try:
        fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
        larghezza_src = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        altezza_src = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if larghezza_src <= 0 or altezza_src <= 0:
            raise RuntimeError(f"Risoluzione sorgente non valida letta da OpenCV: {input_path}")

        larghezza_crop = round(altezza_src * 9 / 16)
        if larghezza_crop > larghezza_src:
            larghezza_crop = larghezza_src  # sorgente gia' piu' stretta del target: nessuno slide

        passo_frame = max(1, round(fps / campioni_al_secondo))

        mp_detector = None
        cascade = None
        if _HAS_MEDIAPIPE:
            mp_detector = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
        else:
            percorso_cascade = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            cascade = cv2.CascadeClassifier(percorso_cascade)

        campioni = []  # [tempo_s, centro_x, trovato]
        idx = 0
        rilevati = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if idx % passo_frame == 0:
                tempo_s = idx / fps
                cx, trovato = _rileva_centro_soggetto(frame, cascade=cascade, mp_detector=mp_detector)
                if trovato:
                    rilevati += 1
                campioni.append([tempo_s, cx, trovato])
            idx += 1

        n_frame_letti = idx
        durata_s = n_frame_letti / fps if fps > 0 else 0.0

        if mp_detector is not None:
            mp_detector.close()
    finally:
        cap.release()

    if not campioni:
        raise RuntimeError("Nessun fotogramma campionato: video vuoto o illeggibile.")

    if rilevati == 0:
        # nessun soggetto rilevato in nessun campione: ritaglio statico centrato
        for c in campioni:
            c[1] = larghezza_src / 2

    centri = [c[1] for c in campioni]
    centri_lisci = _media_mobile(centri, smoothing)

    meta_crop = larghezza_crop / 2
    for c, centro in zip(campioni, centri_lisci):
        crop_x = max(0, min(larghezza_src - larghezza_crop, centro - meta_crop))
        c[1] = round(crop_x)

    segmenti = _comprimi_segmenti(campioni, soglia_px=8.0)
    espressione_x = _costruisci_espressione_ffmpeg(segmenti)

    filtro = (
        f"crop=w={larghezza_crop}:h={altezza_src}:x='{espressione_x}':y=0,"
        f"scale={larghezza_uscita}:{altezza_uscita}:flags=lanczos,setsar=1"
    )

    os.makedirs(os.path.dirname(os.path.abspath(output_path)) or ".", exist_ok=True)
    comando = [
        "ffmpeg", "-y", "-i", input_path,
        "-vf", filtro,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "128k",
        output_path,
    ]
    risultato = subprocess.run(comando, capture_output=True, text=True)
    if risultato.returncode != 0:
        raise RuntimeError(f"ffmpeg ha fallito (codice {risultato.returncode}):\n{risultato.stderr[-2000:]}")

    percentuale_rilevazione = round(100 * rilevati / len(campioni), 1)
    log(
        f"[OK] {output_path} — {len(campioni)} campioni, soggetto rilevato nel "
        f"{percentuale_rilevazione}% dei campioni, durata {durata_s:.1f}s"
    )
    return {
        "output": output_path,
        "campioni_totali": len(campioni),
        "campioni_con_soggetto": rilevati,
        "percentuale_rilevazione": percentuale_rilevazione,
        "segmenti_movimento": len(segmenti),
        "durata_secondi": round(durata_s, 2),
        "larghezza_crop": larghezza_crop,
        "risoluzione_uscita": f"{larghezza_uscita}x{altezza_uscita}",
        "rilevatore": "mediapipe" if _HAS_MEDIAPIPE else "opencv-haar",
    }


def main():
    parser = argparse.ArgumentParser(
        prog="reframe_shorts.py",
        description=(
            "Ritaglia un MP4 orizzontale in verticale 9:16 tenendo il soggetto a "
            "centro-inquadratura (A4-RC-10). Non agganciato alla catena di produzione."
        ),
        add_help=False,
    )
    parser.add_argument("-h", "--help", "--aiuto", action="help", help="mostra questo messaggio ed esce")
    parser.add_argument("--input", required=True, help="MP4 orizzontale gia' esportato")
    parser.add_argument("--output", required=True, help="percorso del file verticale 9:16 da produrre")
    parser.add_argument("--campioni-al-secondo", type=float, default=2.0, dest="campioni_al_secondo")
    parser.add_argument("--larghezza-uscita", type=int, default=1080, dest="larghezza_uscita")
    parser.add_argument("--altezza-uscita", type=int, default=1920, dest="altezza_uscita")
    parser.add_argument("--smoothing", type=int, default=5,
                         help="ampiezza (in campioni) della media mobile che stabilizza il centro")
    args = parser.parse_args()

    try:
        risultato = reframe_verticale(
            args.input, args.output,
            campioni_al_secondo=args.campioni_al_secondo,
            larghezza_uscita=args.larghezza_uscita,
            altezza_uscita=args.altezza_uscita,
            smoothing=args.smoothing,
        )
    except SystemExit:
        raise
    except Exception as e:
        print(f"[STOP] {e}")
        sys.exit(1)

    print(json.dumps(risultato, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
