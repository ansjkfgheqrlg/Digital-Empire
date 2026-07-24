"""
EMPIRE TOOLS — pacchetto video S5: scaffolding, validazione, tentativo di render.

Owner: Claude · Origine: FORGE (LOTTO 5 completamento Workflow Estate, CP-20260723)

## Perché esiste

Lo stream S5 chiede UN video end-to-end. La ladder di render prevista dal workflow
(`WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-S5-YOUTUBE.md` §2) è:
  1. Fliki API  -> morta: `FLIKI_API_KEY` e' vuota
  2. script + stock + TTS + ffmpeg
  3. consegna del pacchetto-render + errore registrato

Questo tool serve a rendere il gradino 3 **verificabile**: senza di esso, "il pacchetto e'
completo" sarebbe un'affermazione che nessuno puo' controllare. `--check` la trasforma in
un comando con un exit code.

## Il vincolo che conta

`--render` **non finge mai**. Verifica ffmpeg con un comando vero (`ffmpeg -version`), e se
mancano gli asset lo scrive in `05-STATO.md` e esce diverso da zero. Un video dichiarato e
inesistente e' il difetto piu' costoso che questo sistema abbia gia' pagato: la dashboard
dava Gate-FUNNEL verde mentre il file conteneva ancora un placeholder.

Non legge MAI `.env` (vincolo di perimetro del lotto: nessun segreto passa da qui).
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RUN_ROOT = Path("WORKFLOW-ESTATE/07-VIDEO-RUN")

REQUIRED = {
    "00-SCELTA.md": "idea scelta e criterio",
    "01-SCRIPT-IT.md": "script italiano a scene",
    "02-TTS.txt": "testo pulito per sintesi vocale",
    "03-SHOTLIST.md": "cosa si vede a schermo, scena per scena",
    "04-SEO-PACK.md": "titolo, descrizione, tag, capitoli",
    "05-STATO.md": "dichiarazione onesta di cosa esiste",
}

VIDEO_EXT = (".mp4", ".mov", ".webm", ".mkv")
AUDIO_EXT = (".wav", ".mp3", ".m4a", ".ogg")

LOG_START = "<!-- VIDEO_PACK:RENDER-LOG:START -->"
LOG_END = "<!-- VIDEO_PACK:RENDER-LOG:END -->"

SKELETON = {
    "00-SCELTA.md": "# 00 — SCELTA\n\n> Idea scelta e perche' (criterio: domanda misurata, non gusto).\n",
    "01-SCRIPT-IT.md": "# 01 — SCRIPT IT\n\n> Script originale in italiano, diviso in scene con timing.\n",
    "02-TTS.txt": "Testo pulito per sintesi vocale. Niente markdown, niente note di regia.\n",
    "03-SHOTLIST.md": "# 03 — SHOTLIST\n\n> Per ogni scena: cosa si vede a schermo.\n",
    "04-SEO-PACK.md": "# 04 — SEO PACK\n\n> Titolo, descrizione (link al Manuale in alto), tag, capitoli.\n",
    "05-STATO.md": ("# 05 — STATO (onesta' sul render)\n\n> Dichiara ESATTAMENTE cosa esiste su "
                    "disco. Se non c'e' un video, dillo e spiega cosa serve.\n\n"
                    f"{LOG_START}\n{LOG_END}\n"),
}


def _repo_root() -> Path:
    """Radice del repo: risalita da questo file (empire/tools/video_pack.py)."""
    return Path(__file__).resolve().parents[2]


def _run_dir(run_id: str) -> Path:
    return _repo_root() / RUN_ROOT / run_id


def _p(msg: str) -> None:
    # Niente emoji: su Windows la console va in crash Unicode (CP-20260722-009).
    print(msg)


# ------------------------------------------------------------------ new

def cmd_new(run_id: str) -> int:
    d = _run_dir(run_id)
    created, kept = [], []
    d.mkdir(parents=True, exist_ok=True)
    for name, body in SKELETON.items():
        f = d / name
        if f.exists():
            kept.append(name)          # idempotente: non sovrascrive mai il lavoro fatto
            continue
        f.write_text(body, encoding="utf-8")
        created.append(name)
    _p(f"run: {d.relative_to(_repo_root())}")
    _p(f"  creati: {len(created)}   gia' presenti (non toccati): {len(kept)}")
    return 0


# ------------------------------------------------------------------ check

def cmd_check(run_id: str) -> int:
    d = _run_dir(run_id)
    if not d.exists():
        _p(f"ERRORE: run inesistente: {d}")
        return 1

    problemi: list[str] = []
    for name, scopo in REQUIRED.items():
        f = d / name
        if not f.exists():
            problemi.append(f"manca {name} ({scopo})")
            continue
        testo = f.read_text(encoding="utf-8")
        if not testo.strip():
            problemi.append(f"{name} e' vuoto")
            continue
        # Un file rimasto identico allo scheletro NON e' compilato. Senza questo
        # controllo `--check` dava verde su un pacchetto appena creato: lo scheletro
        # di 04-SEO-PACK.md contiene la parola "Manuale", e bastava quella a superare
        # la verifica del percorso revenue. Un controllo che approva i propri
        # segnaposto e' peggio di nessun controllo, perche' produce un falso verde.
        if name in SKELETON and testo.strip() == SKELETON[name].strip():
            problemi.append(f"{name} e' ancora lo scheletro, non e' stato compilato")

    tts = d / "02-TTS.txt"
    if tts.exists():
        text = tts.read_text(encoding="utf-8")
        # Il TTS va dato in pasto a un motore vocale: se contiene markdown, il motore
        # legge ad alta voce cancelletti e asterischi.
        for marca in ("##", "**", "](", "`"):
            if marca in text:
                problemi.append(f"02-TTS.txt contiene markdown ({marca!r}): va ripulito")
                break

    seo = d / "04-SEO-PACK.md"
    if seo.exists():
        low = seo.read_text(encoding="utf-8").lower()
        if "manuale" not in low:
            problemi.append("04-SEO-PACK.md non cita il Manuale: manca il percorso revenue")

    stato = d / "05-STATO.md"
    if stato.exists():
        dichiara_video = _has_media(d, VIDEO_EXT)
        testo = stato.read_text(encoding="utf-8").lower()
        promette = "video pubblicato" in testo or "video prodotto" in testo
        if promette and not dichiara_video:
            problemi.append("05-STATO.md dichiara un video che su disco non esiste")

    if problemi:
        _p(f"PACCHETTO INCOMPLETO: {len(problemi)} problemi")
        for x in problemi:
            _p(f"  - {x}")
        return 1

    _p(f"pacchetto completo: {len(REQUIRED)} file presenti e coerenti")
    _p(f"  video su disco: {'si' if _has_media(d, VIDEO_EXT) else 'NO (gradino 3 della ladder)'}")
    _p(f"  audio su disco: {'si' if _has_media(d, AUDIO_EXT) else 'NO'}")
    return 0


def _has_media(d: Path, exts: tuple[str, ...]) -> bool:
    return any(p.suffix.lower() in exts for p in d.rglob("*") if p.is_file())


# ------------------------------------------------------------------ render

def _ffmpeg_probe() -> tuple[bool, str]:
    exe = shutil.which("ffmpeg")
    if not exe:
        return False, "ffmpeg non trovato nel PATH"
    try:
        out = subprocess.run([exe, "-version"], capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError) as e:
        return False, f"ffmpeg presente ma non eseguibile: {e}"
    if out.returncode != 0:
        return False, f"ffmpeg -version exit {out.returncode}"
    prima_riga = (out.stdout or out.stderr).splitlines()[0] if (out.stdout or out.stderr) else "?"
    return True, prima_riga.strip()


def _write_log(stato: Path, righe: list[str]) -> None:
    blocco = "\n".join([LOG_START, "", *righe, "", LOG_END])
    if not stato.exists():
        stato.write_text(f"# 05 — STATO\n\n{blocco}\n", encoding="utf-8")
        return
    text = stato.read_text(encoding="utf-8")
    if LOG_START in text and LOG_END in text:
        pre = text.split(LOG_START)[0]
        post = text.split(LOG_END, 1)[1]
        stato.write_text(pre + blocco + post, encoding="utf-8")
    else:
        stato.write_text(text.rstrip() + "\n\n" + blocco + "\n", encoding="utf-8")


def cmd_render(run_id: str) -> int:
    d = _run_dir(run_id)
    if not d.exists():
        _p(f"ERRORE: run inesistente: {d}")
        return 1

    ts = datetime.now().astimezone().isoformat(timespec="seconds")
    ok_ffmpeg, dettaglio = _ffmpeg_probe()
    ha_audio = _has_media(d, AUDIO_EXT)
    ha_video = _has_media(d, VIDEO_EXT)

    righe = [
        f"*Ultimo tentativo di render: {ts}*", "",
        f"- ffmpeg: {'PRESENTE' if ok_ffmpeg else 'ASSENTE'} — {dettaglio}",
        f"- audio narrato su disco: {'si' if ha_audio else 'NO'}",
        f"- video su disco: {'si' if ha_video else 'NO'}",
    ]

    if ha_video:
        righe.append("- esito: **video gia' presente**, nessun render rifatto (idempotente).")
        _write_log(d / "05-STATO.md", righe)
        _p("video gia' presente: nessun render eseguito")
        return 0

    if not ok_ffmpeg:
        righe += ["- esito: **gradino 2 impossibile** (manca ffmpeg).",
                  "- si resta al **gradino 3**: pacchetto-render consegnato, video NON prodotto."]
        _write_log(d / "05-STATO.md", righe)
        _p("RENDER NON ESEGUITO: ffmpeg assente. Stato scritto in 05-STATO.md")
        return 2

    if not ha_audio:
        # Percorso completo dalla radice del repo: un percorso relativo alla run viene
        # letto da `conform` come riferimento rotto (non esiste `<run-id>/02-TTS.txt`
        # rispetto alla radice), e un log onesto non deve generare falsi allarmi.
        tts_rel = (RUN_ROOT / run_id / "02-TTS.txt").as_posix()
        righe += ["- esito: **gradino 2 incompleto**: ffmpeg c'e', manca la traccia audio narrata.",
                  f"- serve: sintesi vocale di `{tts_rel}` + registrazione schermo.",
                  "- si resta al **gradino 3**: pacchetto-render consegnato, video NON prodotto."]
        _write_log(d / "05-STATO.md", righe)
        _p("RENDER NON ESEGUITO: manca l'audio narrato. Stato scritto in 05-STATO.md")
        return 2

    righe.append("- esito: asset presenti — montaggio da eseguire con ffmpeg sui file di questa run.")
    _write_log(d / "05-STATO.md", righe)
    _p("asset presenti: montaggio eseguibile")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="video_pack.py",
        description="Pacchetto video S5: scaffolding, validazione, tentativo di render onesto.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--new", metavar="RUN_ID", help="crea lo scheletro di una run (idempotente)")
    g.add_argument("--check", metavar="RUN_ID", help="valida la completezza del pacchetto")
    g.add_argument("--render", metavar="RUN_ID", help="tenta il render e registra l'esito reale")
    a = ap.parse_args(argv)

    if a.new:
        return cmd_new(a.new)
    if a.check:
        return cmd_check(a.check)
    return cmd_render(a.render)


if __name__ == "__main__":
    sys.exit(main())
