# -*- coding: utf-8 -*-
"""verifica_pronuncia.py — confronta cosa dice DAVVERO l'audio esportato con cosa doveva dire lo script.

REGOLA CHE LO ORDINA: A4-RC-13 (company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/
RIPASSO_COSTRUTTIVO.py). I sottotitoli Fliki nascono dal TESTO inviato, non dall'audio
generato: se il TTS storpia o salta una parola, i sottotitoli mentono in silenzio su cio' che si
sente davvero. Serve un ASR indipendente che ascolti il file esportato e lo confronti.

IL BUCO CHE CHIUDE: L12 @ 07:14-07:35 mostra il caso dal vivo — il docente sente una
trascrizione sbagliata ("grande affetto dei suoi figli") e la corregge A MANO, dopo averla
sentita lui. `qa-audio-video.md` §8 ordina di registrare gli errori di pronuncia nel lessico,
ma il lessico si riempie SOLO con cio' che un umano ha sentito per caso: zero automazione prima
di questo file (cercato `faster_whisper`, `whisper`, `ASR` in `02-AUTOMAZIONI-E-SCRIPTS/`: zero
occorrenze fuori da questo script).

MODELLO ASR — NON SI SCARICA DA SOLO. Su questa macchina lo scaricamento automatico e' fallito
piu' volte (SSL/antivirus, canale accelerato HuggingFace rotto): vedi
`SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/corso_trascrivi.py`, che questo
script copia nella scelta (non importa: file diverso, stessa tecnica) — `faster-whisper`,
`device="cpu"`, `compute_type="int8"`, e SOLO la copia locale in `modelli/faster-whisper-<nome>/`
(mai un download silenzioso). Se il modello non c'e' sul disco, lo script si ferma e lo dice.

NON E' ANCORA AGGANCIATO. Nessun file della catena di produzione importa questo modulo —
ADR-029, binario B: aspetta il gate di categoria. Le proposte prodotte NON vengono scritte
dentro `references/lessico-pronuncia.md` (file di produzione, mai toccato da questo script):
finiscono in un file di proposte separato, pronto per essere copiato a mano.

USO
    python verifica_pronuncia.py --aiuto
    python verifica_pronuncia.py --mp4 video.mp4 --script script.md
    python verifica_pronuncia.py --mp4 video.mp4 --script script.md --modello base --proposte-out proposte.md
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REPO_DIR = os.path.abspath(os.path.join(FACTORY_DIR, ".."))
MODELLI_DIR = os.path.join(REPO_DIR, "modelli")


def _esito(regolatore: str, passa: bool, motivo: str, **dettagli) -> dict:
    return {"regolatore": regolatore, "esito": "passa" if passa else "BLOCCO",
            "motivo": motivo, **dettagli}


# --------------------------------------------------------------------------------------
# Caricamento modello — stessa tecnica di corso_trascrivi.py, copiata non importata
# --------------------------------------------------------------------------------------
def carica_modello(nome_modello: str = "base"):
    """Ritorna (modello, errore). Se errore non e' None, il modello non e' utilizzabile: lo
    script chiamante deve fermarsi con quel messaggio, mai proseguire a meta'."""
    os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None, ("faster-whisper non e' installato in questo ambiente "
                      "(pip install faster-whisper). Impossibile trascrivere.")

    locale = os.path.join(MODELLI_DIR, f"faster-whisper-{nome_modello}")
    if not os.path.exists(os.path.join(locale, "model.bin")):
        return None, (f"modello ASR assente: {locale} non contiene model.bin. Questo script NON "
                      f"scarica dalla rete (vedi corso_trascrivi.py per come procurarselo con "
                      f"curl --retry --continue-at). Copie note: "
                      f"{', '.join(sorted(os.listdir(MODELLI_DIR))) if os.path.isdir(MODELLI_DIR) else '(nessuna, modelli/ assente)'}.")

    try:
        modello = WhisperModel(locale, device="cpu", compute_type="int8")
    except Exception as e:  # noqa: BLE001 — qualunque errore di caricamento va riportato, non propagato
        return None, f"impossibile caricare il modello da {locale}: {e}"
    return modello, None


def estrai_audio(mp4: str, wav: str) -> tuple[bool, str | None]:
    if not shutil.which("ffmpeg"):
        return False, "ffmpeg non trovato sul PATH: impossibile estrarre l'audio."
    if not os.path.exists(mp4):
        return False, f"file MP4 inesistente: {mp4}"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", mp4,
           "-vn", "-ac", "1", "-ar", "16000", "-f", "wav", wav]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0 or not os.path.exists(wav):
        return False, f"estrazione audio fallita: {res.stderr[-500:]}"
    return True, None


def trascrivi_mp4(mp4: str, nome_modello: str = "base") -> tuple[str | None, str | None]:
    """Trascrive il parlato di un MP4. Ritorna (testo, errore): se errore non e' None, testo e'
    sempre None — lo script non produce mai un risultato parziale."""
    modello, errore = carica_modello(nome_modello)
    if errore:
        return None, errore

    with tempfile.TemporaryDirectory(prefix="verifica_pronuncia_") as cartella:
        wav = os.path.join(cartella, "audio.wav")
        ok, errore = estrai_audio(mp4, wav)
        if not ok:
            return None, errore

        try:
            segmenti, _info = modello.transcribe(wav, language="it", vad_filter=True, beam_size=5)
            testo = " ".join((s.text or "").strip() for s in segmenti if (s.text or "").strip())
        except Exception as e:  # noqa: BLE001
            return None, f"trascrizione fallita: {e}"

    return testo, None


# --------------------------------------------------------------------------------------
# Confronto parola per parola — funzione pura, testabile senza ASR/ffmpeg
# --------------------------------------------------------------------------------------
def _normalizza_parole(testo: str) -> list[str]:
    return re.findall(r"[a-zà-ù0-9']+", (testo or "").lower())


def confronta_pronuncia(script_atteso: str, testo_riconosciuto: str) -> dict:
    """Diff parola-per-parola fra cio' che lo script doveva dire e cio' che l'ASR ha sentito.
    Ogni scarto diventa una proposta per lessico-pronuncia.md (mai scritta li' direttamente)."""
    parole_attese = _normalizza_parole(script_atteso)
    parole_sentite = _normalizza_parole(testo_riconosciuto)

    sm = difflib.SequenceMatcher(None, parole_attese, parole_sentite, autojunk=False)
    scarti = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        atteso_seg = " ".join(parole_attese[i1:i2])
        sentito_seg = " ".join(parole_sentite[j1:j2])
        tipo = {"replace": "sostituita", "delete": "mancante", "insert": "extra_non_attesa"}[tag]
        scarti.append({"tipo": tipo, "atteso": atteso_seg, "sentito": sentito_seg})

    proposte = [
        {"si_scrive": s["atteso"],
         "si_legge_male_cosi": s["sentito"] or "(non pronunciata / non riconosciuta)",
         "si_scrive_per_farla_leggere_bene": ""}  # colonna da compilare a mano: serve l'orecchio umano
        for s in scarti if s["tipo"] in ("sostituita", "mancante") and s["atteso"]
    ]

    ok = len(scarti) == 0
    return _esito(
        "verifica-pronuncia", ok,
        "Nessuno scarto fra script atteso e audio riconosciuto." if ok else
        f"{len(scarti)} scarti fra script atteso e audio riconosciuto.",
        scarti=scarti, proposte_lessico=proposte,
        parole_attese=len(parole_attese), parole_sentite=len(parole_sentite),
    )


def verifica_pronuncia(mp4: str, script_atteso: str, nome_modello: str = "base") -> dict:
    """Funzione end-to-end importabile: estrae l'audio, trascrive, confronta."""
    testo_riconosciuto, errore = trascrivi_mp4(mp4, nome_modello)
    if errore:
        return _esito("verifica-pronuncia", False, errore)
    return confronta_pronuncia(script_atteso, testo_riconosciuto)


# --------------------------------------------------------------------------------------
def scrivi_proposte_lessico(proposte: list[dict], percorso_out: str, trovata_in: str = "") -> int:
    """Scrive le proposte in un file NUOVO (mai in lessico-pronuncia.md): righe pronte da
    incollare a mano dopo revisione umana della grafia fonetica corretta. Scrittura atomica:
    costruisce tutto in memoria e scrive un'unica volta, mai un file a meta'."""
    oggi = date.today().isoformat()
    righe = ["| si scrive | si legge male così | si scrive per farla leggere bene | trovata in | data |",
             "|---|---|---|---|---|"]
    for p in proposte:
        righe.append(
            f"| {p['si_scrive']} | {p['si_legge_male_cosi']} | {p['si_scrive_per_farla_leggere_bene']} "
            f"| {trovata_in} | {oggi} |"
        )
    contenuto = "\n".join(righe) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(percorso_out)) or ".", exist_ok=True)
    with open(percorso_out, "w", encoding="utf-8") as f:
        f.write(contenuto)
    return len(proposte)


def main() -> int:
    ap = argparse.ArgumentParser(
        add_help=False,
        description="Trascrive un MP4 con ASR locale e lo confronta parola per parola con lo "
                    "script atteso. A4-RC-13 — non ancora agganciato al gate.",
    )
    ap.add_argument("--aiuto", "-h", action="help", help="mostra questo aiuto ed esce")
    ap.add_argument("--mp4", required=True, help="percorso del video MP4 esportato")
    ap.add_argument("--script", required=True, help="percorso del file di testo/script atteso")
    ap.add_argument("--modello", default="base",
                    choices=["tiny", "base", "small", "medium", "large-v3"],
                    help="modello faster-whisper, cercato SOLO in modelli/faster-whisper-<nome>/")
    ap.add_argument("--proposte-out", default=None,
                    help="dove scrivere le proposte per lessico-pronuncia.md (default: accanto al mp4)")
    ap.add_argument("--json", action="store_true", help="stampa il risultato come JSON")
    args = ap.parse_args()

    if not os.path.exists(args.mp4):
        print(f"[!] File MP4 inesistente: {args.mp4}")
        return 1
    if not os.path.exists(args.script):
        print(f"[!] File script inesistente: {args.script}")
        return 1

    with open(args.script, encoding="utf-8") as f:
        script_atteso = f.read()

    risultato = verifica_pronuncia(args.mp4, script_atteso, args.modello)

    if risultato["regolatore"] == "verifica-pronuncia" and "scarti" not in risultato:
        # errore di dipendenza (ffmpeg/modello assente): fermarsi con messaggio chiaro, zero file scritti
        print(f"[!] {risultato['motivo']}")
        return 1

    proposte_out = args.proposte_out or (os.path.splitext(args.mp4)[0] + ".proposte-lessico.md")
    n_scritte = 0
    if risultato.get("proposte_lessico"):
        n_scritte = scrivi_proposte_lessico(risultato["proposte_lessico"], proposte_out,
                                            trovata_in=os.path.basename(args.mp4))

    if args.json:
        print(json.dumps(risultato, ensure_ascii=False, indent=2))
    else:
        simbolo = "[OK]" if risultato["esito"] == "passa" else "[BLOCCO]"
        print(f"{simbolo} {risultato['regolatore']} — {risultato['motivo']}")
        for s in risultato.get("scarti", []):
            print(f"      · {s['tipo']}: atteso='{s['atteso']}' sentito='{s['sentito']}'")
        if n_scritte:
            print(f"      {n_scritte} proposte scritte in {proposte_out} (da rivedere a mano prima di "
                  f"copiarle in references/lessico-pronuncia.md)")

    return 1 if risultato["esito"] == "BLOCCO" else 0


if __name__ == "__main__":
    sys.exit(main())
