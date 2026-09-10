#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regola che ordina questo script: A4-RC-07
(company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/RIPASSO_COSTRUTTIVO.py).

Buco che chiude, misurato sulla fabbrica: nessuno script del motore (apex7_orchestrator.py,
fliki_client.py, build_candidate_pool.py, youtube_uploader_playwright.py...) contiene logica
di cronometraggio. Il tempo di produzione oggi si stima a occhio ("ci vogliono 5 minuti"),
non si misura. Senza un numero reale per fase, "puntiamo sulla qualita'" resta una scusa non
falsificabile e non si sa DOVE la catena rallenta (candidate pool? transcript? script?
regolatori? Fliki? export? QA?).

COME E' FATTO: wrapper ESTERNO. Non importa, non modifica e non chiama nessuno dei file
citati sopra — cronometra qualunque fase avvolgendola dall'esterno, in due modi:
  1) come context manager Python (`with misura_fase(...)`) attorno a una chiamata in-process;
  2) come comando CLI (`cronometra`) che lancia un ALTRO processo (es. una delle fasi
     esistenti invocata da riga di comando) e ne misura la durata a bordo, senza toccare
     il codice di quella fase.

NON E' ANCORA AGGANCIATO a nessuna fase reale della catena: e' pronto per essere invocato,
ma nessun orchestratore lo richiama oggi. L'aggancio avviene al gate di categoria (ADR-029).

Uso da riga di comando:
  python misura_tempo_produzione.py --aiuto
  python misura_tempo_produzione.py cronometra --fase fliki --video-id V001 -- python fliki_client.py --file-id XYZ
  python misura_tempo_produzione.py report

Uso come libreria:
  from misura_tempo_produzione import misura_fase, cronometra_comando, genera_report
  with misura_fase("script", video_id="V001"):
      scrivi_lo_script()
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

# Su Windows la console e' cp1252: qualunque carattere fuori da quella tabella (incluse le
# emoji) fa crashare i print con UnicodeEncodeError. Questo script non usa emoji, ma
# riconfigura comunque lo stream in utf-8 (idiom gia' usato in fliki_client.py) per non
# rompersi sugli accenti italiani quando l'output viene rediretto su file.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR_DEFAULT = os.path.join(SCRIPT_DIR, "logs")
LOG_PATH_DEFAULT = os.path.join(LOG_DIR_DEFAULT, "tempi_produzione.jsonl")

# Nomi di fase attesi dalla catena reale (documentazione, non un vincolo: qualunque stringa
# e' accettata come fase, cosi' lo script resta utile anche per fasi non ancora nominate qui).
FASI_NOTE = (
    "candidate_pool", "transcript", "script", "regolatori", "fliki", "export", "qa",
)


def _log_path(log_path: str | None) -> str:
    percorso = log_path or LOG_PATH_DEFAULT
    os.makedirs(os.path.dirname(os.path.abspath(percorso)) or ".", exist_ok=True)
    return percorso


def _scrivi_riga(log_path: str, voce: dict) -> None:
    percorso = _log_path(log_path)
    with open(percorso, "a", encoding="utf-8") as f:
        f.write(json.dumps(voce, ensure_ascii=False) + "\n")


class misura_fase:
    """
    Context manager che cronometra un blocco di codice come una fase della produzione e
    scrive una riga JSONL nel log (fase, secondi, video_id, esito). Non solleva mai
    eccezioni proprie sull'uscita: se il blocco cronometrato fallisce, la registra come
    fallita e rilancia l'eccezione originale (non la inghiotte).

    Esempio:
        with misura_fase("transcript", video_id="V001"):
            testo = scarica_transcript(url)
    """

    def __init__(self, fase: str, video_id: str | None = None, log_path: str | None = None,
                 extra: dict | None = None):
        if not fase or not fase.strip():
            raise ValueError("Il nome della fase non puo' essere vuoto.")
        self.fase = fase
        self.video_id = video_id
        self.log_path = log_path
        self.extra = extra or {}
        self._t0 = None

    def __enter__(self):
        self._t0 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        secondi = round(time.perf_counter() - self._t0, 3)
        voce = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "fase": self.fase,
            "secondi": secondi,
            "video_id": self.video_id,
            "esito": "ok" if exc_type is None else "errore",
        }
        if exc_type is not None:
            voce["errore"] = f"{exc_type.__name__}: {exc_val}"
        if self.extra:
            voce["extra"] = self.extra
        _scrivi_riga(self.log_path, voce)
        return False  # non sopprime mai l'eccezione originale


def cronometra_comando(fase: str, comando: list[str], video_id: str | None = None,
                        log_path: str | None = None, cwd: str | None = None) -> dict:
    """
    Lancia `comando` come sottoprocesso e cronometra la sua durata come `fase`, senza
    toccare il codice del comando stesso. E' il modo per misurare una fase reale della
    catena (es. una chiamata a fliki_client.py) senza modificare fliki_client.py.

    Ritorna un dict con fase, secondi, codice_uscita, video_id.
    """
    if not comando:
        raise ValueError("Nessun comando da eseguire (lista vuota).")
    t0 = time.perf_counter()
    esito = "ok"
    errore = None
    codice_uscita = None
    try:
        risultato = subprocess.run(comando, cwd=cwd)
        codice_uscita = risultato.returncode
        if codice_uscita != 0:
            esito = "errore"
            errore = f"codice di uscita {codice_uscita}"
    except OSError as e:
        esito = "errore"
        errore = f"{type(e).__name__}: {e}"
    secondi = round(time.perf_counter() - t0, 3)
    voce = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fase": fase,
        "secondi": secondi,
        "video_id": video_id,
        "esito": esito,
        "comando": comando,
    }
    if errore:
        voce["errore"] = errore
    _scrivi_riga(log_path, voce)
    return {
        "fase": fase,
        "secondi": secondi,
        "codice_uscita": codice_uscita,
        "video_id": video_id,
        "esito": esito,
    }


def leggi_log(log_path: str | None = None) -> list[dict]:
    """Legge il log JSONL e ritorna la lista delle voci (lista vuota se il file non esiste)."""
    percorso = log_path or LOG_PATH_DEFAULT
    if not os.path.isfile(percorso):
        return []
    voci = []
    with open(percorso, encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if riga:
                voci.append(json.loads(riga))
    return voci


def aggrega_per_fase(voci: list[dict]) -> dict:
    """
    Aggrega le voci del log per fase: conteggio, secondi totali, medi, minimi, massimi.
    Ordina per secondi totali decrescenti, cosi' la fase piu' lenta e' la prima riga:
    e' la risposta diretta a "dove rallenta la catena".
    """
    per_fase: dict[str, list[float]] = {}
    for voce in voci:
        per_fase.setdefault(voce["fase"], []).append(voce["secondi"])

    aggregato = {}
    for fase, tempi in per_fase.items():
        aggregato[fase] = {
            "conteggio": len(tempi),
            "secondi_totali": round(sum(tempi), 3),
            "secondi_medi": round(sum(tempi) / len(tempi), 3),
            "secondi_min": round(min(tempi), 3),
            "secondi_max": round(max(tempi), 3),
        }
    # ordina per secondi_totali decrescente
    return dict(sorted(aggregato.items(), key=lambda kv: kv[1]["secondi_totali"], reverse=True))


def genera_report(log_path: str | None = None) -> str:
    """Produce un report leggibile (tabella testuale) del tempo per fase, dal piu' lento al piu' veloce."""
    voci = leggi_log(log_path)
    if not voci:
        return "Nessuna misurazione registrata ancora (log vuoto o inesistente)."
    aggregato = aggrega_per_fase(voci)
    righe = [
        f"{'FASE':<20} {'N':>4} {'TOT s':>10} {'MEDIA s':>10} {'MIN s':>8} {'MAX s':>8}",
        "-" * 64,
    ]
    for fase, dati in aggregato.items():
        righe.append(
            f"{fase:<20} {dati['conteggio']:>4} {dati['secondi_totali']:>10.3f} "
            f"{dati['secondi_medi']:>10.3f} {dati['secondi_min']:>8.3f} {dati['secondi_max']:>8.3f}"
        )
    righe.append("-" * 64)
    righe.append(f"Voci totali nel log: {len(voci)} — file: {log_path or LOG_PATH_DEFAULT}")
    return "\n".join(righe)


def main():
    parser = argparse.ArgumentParser(
        prog="misura_tempo_produzione.py",
        description=(
            "Cronometra le fasi della produzione video (A4-RC-07). Wrapper esterno: non "
            "modifica ne' chiama in automatico nessuna fase esistente."
        ),
        add_help=False,
    )
    parser.add_argument("-h", "--help", "--aiuto", action="help", help="mostra questo messaggio ed esce")
    sotto = parser.add_subparsers(dest="sottocomando", required=True)

    p_cron = sotto.add_parser("cronometra", help="cronometra un comando esterno come una fase")
    p_cron.add_argument("--fase", required=True, help=f"nome fase (note della catena: {', '.join(FASI_NOTE)})")
    p_cron.add_argument("--video-id", default=None)
    p_cron.add_argument("--log", default=None, help=f"percorso log JSONL (default: {LOG_PATH_DEFAULT})")
    p_cron.add_argument("comando_esterno", nargs=argparse.REMAINDER,
                         help="comando da eseguire, es: -- python fliki_client.py --file-id XYZ")

    p_rep = sotto.add_parser("report", help="stampa il report aggregato per fase")
    p_rep.add_argument("--log", default=None)

    args = parser.parse_args()
    return _dispatch(args)


def _dispatch(args):
    if args.sottocomando == "report":
        print(genera_report(args.log))
        return 0

    if args.sottocomando == "cronometra":
        cmd = args.comando_esterno
        if cmd and cmd[0] == "--":
            cmd = cmd[1:]
        if not cmd:
            print("[STOP] Nessun comando indicato dopo 'cronometra'. Esempio: "
                  "cronometra --fase fliki -- python fliki_client.py --file-id XYZ")
            return 1
        risultato = cronometra_comando(args.fase, cmd, video_id=args.video_id, log_path=args.log)
        print(json.dumps(risultato, ensure_ascii=False, indent=2))
        return 0 if risultato["esito"] == "ok" else 1

    print("[STOP] Sotto-comando non riconosciuto. Usa --aiuto.")
    return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
