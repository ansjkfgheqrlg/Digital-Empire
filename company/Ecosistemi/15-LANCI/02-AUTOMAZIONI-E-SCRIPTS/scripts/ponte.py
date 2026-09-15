# -*- coding: utf-8 -*-
"""Il ponte: come un programma fa lavorare un agente (ADR-014, documento 01 §4).

    claude -p --agent <id> --model <id esplicito> --output-format json  < prompt

Le quattro regole ereditate da ADR-014, gia' pagate una volta ciascuna:

1. il prompt passa da **standard input**, mai come argomento (il wrapper troncava i
   prompt multiriga alla prima riga, in silenzio);
2. si passa l'**identificativo esplicito** del modello letto dal registro
   (`agenti[].modello`), mai un alias (`--model sonnet` restituiva un altro
   modello e lo si pagava);
3. si legge `total_cost_usd` dalla risposta e si verifica il tetto **PRIMA** di
   ogni chiamata (il tetto e' stato sfondato in silenzio una volta);
4. si lavora a blocchi, non a unita' minima (~0,08-0,11 $ di sola tassa a chiamata)
   — questa e' una regola per chi scrive i prompt, non per questo modulo.

Ogni invocazione, anche fallita, lascia una riga in
`<dir_lancio>/registro-chiamate.jsonl` (schema in CONTRATTO-STATO.md). `costi()` e'
la somma di quelle righe: letta, mai stimata.

`esecutore` e' iniettabile (callable(argv, stdin_testo) -> (returncode, stdout)):
i test non lanciano mai `claude` davvero. Il default e' subprocess.run.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import time
from datetime import datetime, timezone

try:
    from .stato_lancio import ErroreLancio
    from .gates import _comune as gates
except ImportError:  # pragma: no cover
    from scripts.stato_lancio import ErroreLancio  # type: ignore
    from scripts.gates import _comune as gates  # type: ignore

NOME_REGISTRO_CHIAMATE = "registro-chiamate.jsonl"


class ErroreTetto(ErroreLancio):
    """Il tetto di spesa del lancio e' gia' raggiunto: la chiamata NON parte."""


class ErrorePonte(ErroreLancio):
    """La chiamata e' partita ma non ha dato una risposta usabile."""


def _adesso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def modello_di(agente_id: str) -> str:
    """L'identificativo esplicito del modello, dal registro. Agente sconosciuto -> errore."""
    for a in gates.registro().get("agenti", []):
        if a["id"] == agente_id:
            modello = a.get("modello")
            if not modello:
                raise ErroreLancio("L'agente %s non ha un modello nel registro" % agente_id)
            return modello
    raise ErroreLancio("Agente sconosciuto: %s (non e' in registro.agenti)" % agente_id)


def tetto_registro() -> float:
    return float(gates.registro().get("ponte", {}).get("tetto_spesa_per_lancio_usd", 0.0))


def percorso_registro_chiamate(dir_lancio: str) -> str:
    return os.path.join(dir_lancio, NOME_REGISTRO_CHIAMATE)


def righe(dir_lancio: str) -> list[dict]:
    p = percorso_registro_chiamate(dir_lancio)
    if not os.path.exists(p):
        return []
    trovate = []
    with open(p, encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            try:
                trovate.append(json.loads(riga))
            except json.JSONDecodeError:
                continue  # una riga rotta non azzera il conto delle altre
    return trovate


def costi(dir_lancio: str) -> float:
    """Somma di total_cost_usd nel registro delle chiamate. Letta, mai stimata."""
    totale = 0.0
    for r in righe(dir_lancio):
        try:
            totale += float(r.get("total_cost_usd") or 0.0)
        except (TypeError, ValueError):
            continue
    return totale


def _accoda(dir_lancio: str, riga: dict) -> None:
    os.makedirs(dir_lancio, exist_ok=True)
    with open(percorso_registro_chiamate(dir_lancio), "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(riga, ensure_ascii=False) + "\n")


def _esecutore_vero(argv: list[str], stdin_testo: str) -> tuple[int, str]:
    eseguibile = shutil.which(argv[0]) or argv[0]
    try:
        r = subprocess.run([eseguibile] + argv[1:], input=stdin_testo, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
    except FileNotFoundError:
        raise ErrorePonte("Non trovo `%s` nel PATH: il ponte non ha nessuno dall'altra parte."
                          % argv[0])
    return r.returncode, r.stdout


def invoca(agente_id: str, prompt: str, dir_lancio: str, *, esecutore=None,
           tetto_usd: float | None = None) -> dict:
    """Invoca un agente del registro. Ritorna il JSON di risposta della CLI.

    - tetto raggiunto PRIMA della chiamata -> riga esito "tetto", ErroreTetto, nessuna chiamata;
    - chiamata fallita / risposta non JSON -> riga esito "errore", ErrorePonte;
    - ok -> riga esito "ok" con total_cost_usd letto dalla risposta.
    """
    modello = modello_di(agente_id)
    tetto = tetto_registro() if tetto_usd is None else float(tetto_usd)
    esecutore = esecutore or _esecutore_vero
    lancio_id = os.path.basename(os.path.normpath(dir_lancio))
    prompt_sha = hashlib.sha256(prompt.encode("utf-8")).hexdigest()

    def riga(esito, durata, costo, nota=None):
        return {"il": _adesso(), "lancio_id": lancio_id, "agente": agente_id,
                "modello": modello, "durata_s": round(durata, 3),
                "total_cost_usd": round(float(costo), 6), "esito": esito,
                "prompt_sha256": prompt_sha, "nota": nota}

    speso = costi(dir_lancio)
    if speso >= tetto:
        nota = "speso %.4f $ >= tetto %.2f $: chiamata non partita" % (speso, tetto)
        _accoda(dir_lancio, riga("tetto", 0.0, 0.0, nota))
        raise ErroreTetto("Tetto di spesa del lancio raggiunto (%s). Il lavoro e' salvato: "
                          "si riprende, non si ricomincia." % nota)

    argv = ["claude", "-p", "--agent", agente_id, "--model", modello,
            "--output-format", "json"]
    t0 = time.monotonic()
    try:
        codice, stdout = esecutore(argv, prompt)
    except ErrorePonte as e:
        _accoda(dir_lancio, riga("errore", time.monotonic() - t0, 0.0, str(e)))
        raise
    except Exception as e:  # noqa: BLE001 - qualunque guasto e' una riga, poi un errore chiaro
        _accoda(dir_lancio, riga("errore", time.monotonic() - t0, 0.0,
                                 "%s: %s" % (type(e).__name__, e)))
        raise ErrorePonte("Chiamata a %s fallita: %s: %s" % (agente_id, type(e).__name__, e))
    durata = time.monotonic() - t0

    try:
        risposta = json.loads(stdout) if stdout and stdout.strip() else None
    except json.JSONDecodeError:
        risposta = None
    if not isinstance(risposta, dict):
        _accoda(dir_lancio, riga("errore", durata, 0.0,
                                 "risposta non JSON (codice %s): %s" % (codice, (stdout or "")[:200])))
        raise ErrorePonte("L'agente %s non ha risposto in JSON (codice %s)." % (agente_id, codice))

    costo = risposta.get("total_cost_usd") or 0.0
    nota = None
    usati = risposta.get("modelUsage")
    if isinstance(usati, dict) and usati and modello not in usati:
        nota = "modello usato diverso da quello chiesto: %s" % ", ".join(sorted(usati))
    if codice != 0 or risposta.get("is_error"):
        _accoda(dir_lancio, riga("errore", durata, costo,
                                 nota or "codice %s: %s" % (codice, str(risposta.get("result", ""))[:200])))
        raise ErrorePonte("L'agente %s e' uscito con codice %s." % (agente_id, codice))

    _accoda(dir_lancio, riga("ok", durata, costo, nota))
    return risposta
