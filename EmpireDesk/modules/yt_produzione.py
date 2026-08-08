# -*- coding: utf-8 -*-
"""
modules/yt_produzione.py — il PULSANTE di avvio della YouTube Automation Factory dentro Aureus.

Cosa aggiunge: una tile "Produci video + copertina" nella griglia Operazioni Reali. Premendola
parte davvero la catena completa della fabbrica (F1→F5 orchestratore → copertina Arena → video
Fliki), con log live ed exit code visibili come per ogni altra tile.

Regole vincolanti rispettate:
- ADR-003 (wrap, mai riscrittura): il lancio passa dalla tile standard kind="py" di EmpireDesk,
  che esegue `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py`.
  Qui NON vive nessuna logica di produzione: il runner e i tre script reali che incatena sono
  l'unica implementazione.
- Le route restano SOLA LETTURA (come modules/youtube.py e modules/libri.py): leggono file di
  stato gia' scritti su disco e riusano le funzioni di lettura del runner. Non lanciano processi,
  non toccano la rete, non ricalcolano niente a runtime (Mandato Art.2).
- Nessun numero inventato: se un file manca si dichiara "nessun dato" con il percorso atteso.
- La PUBBLICAZIONE su YouTube non e' in questa catena, per scelta: resta un atto separato.
"""
import importlib.util
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTORY_DIR = REPO_ROOT / "YOUTUBE-AUTOMATION-FACTORY"
SCRIPTS_DIR = FACTORY_DIR / "02-AUTOMAZIONI-E-SCRIPTS"
RUNNER = SCRIPTS_DIR / "produci_video_completo.py"


def _runner():
    """Importa il runner per riusarne le funzioni di LETTURA (coda, script pronti, prerequisiti).
    Ritorna None se assente/rotto: si dichiara, non si finge (stesso pattern di modules/youtube.py).
    L'import non esegue niente — il runner agisce solo sotto `if __name__ == '__main__'`."""
    if not RUNNER.exists():
        return None
    try:
        spec = importlib.util.spec_from_file_location("yt_produci_runner", RUNNER)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        return mod
    except Exception:  # noqa: BLE001 — runner rotto: il pannello lo dichiara, l'app non cade
        return None


def stato(payload=None):
    """POST /api/ytprod/stato — cosa produrrebbe il pulsante adesso, e cosa manca perche' parta.
    Equivalente in sola lettura di `produci_video_completo.py --preflight` (che pero' e' un
    processo: qui non si lancia nulla)."""
    mod = _runner()
    if mod is None:
        return {"stato": "nessun dato",
                "nota": "runner non trovato o non importabile",
                "fonte": str(RUNNER)}

    lavoro, motivo = mod.scegli_lavoro(None, None)
    prodotti = sorted(mod.video_gia_prodotti())
    pronti = mod.script_pronti()
    ultima = mod._leggi_json(mod.STATO_PATH, None)

    prerequisiti = {
        "script_adattato_pronto": bool(lavoro),
        "fliki_api_key": mod._chiave_fliki_presente(),
        "profilo_arena": os.path.isdir(mod.ARENA_PROFILE_DIR),
    }
    try:
        import playwright  # noqa: F401
        prerequisiti["playwright"] = True
    except ImportError:
        prerequisiti["playwright"] = False

    return {
        "stato": "ok",
        "prossimo_lavoro": lavoro,
        "motivo": motivo,
        "pronto_a_partire": all(prerequisiti.values()),
        "prerequisiti": prerequisiti,
        "script_adattati_scritti": pronti,
        "video_sorgente_gia_prodotti": prodotti,
        "ultima_esecuzione": ultima or "mai eseguito da qui",
        "catena": ["F1→F5 apex7_orchestrator.py (--phase 5)",
                   "copertina: arena_thumbnail.py",
                   "video: fliki_client.py (crediti Fliki reali)"],
        "pubblicazione_youtube": "non inclusa: atto separato e voluto",
        "fonte": str(RUNNER),
    }


def coda(payload=None):
    """POST /api/ytprod/coda — ordine dei lavori (memory/coda_produzione.json), letto com'e'."""
    mod = _runner()
    if mod is None:
        return {"stato": "nessun dato", "nota": "runner non importabile", "fonte": str(RUNNER)}
    if not os.path.exists(mod.CODA_PATH):
        return {"stato": "nessun dato",
                "nota": "coda_produzione.json assente: il runner ripiega sulla scansione degli "
                        "script adattati",
                "fonte": mod.CODA_PATH}
    dati = mod._leggi_json(mod.CODA_PATH, {})
    dati["stato"] = "ok"
    dati["fonte"] = mod.CODA_PATH
    return dati


PANEL_HTML = """
<div id="panel-ytprod" class="panel">
  <h2>\U0001F3AC YouTube — Produci video + copertina</h2>
  <p class="hint">La tile <b>Produci video + copertina</b> lancia la catena reale:
  F1→F5 (canale, video sorgente, script, spec, metadati) → copertina Arena → video Fliki.
  Il video consuma <b>crediti Fliki reali</b> e richiede decine di minuti. La pubblicazione su
  YouTube non è inclusa di proposito.</p>
  <p class="hint">Si produce solo ciò che ha già uno <b>script adattato scritto a mano</b>:
  la fabbrica non genera il parlato a runtime. Se non c'è nulla di pronto, il pulsante lo dice
  ed esce senza spendere.</p>

  <button class="btn" onclick="edApi('ytprod/stato',{}).then(r=>{
    document.getElementById('ytprod-out').textContent = JSON.stringify(r, null, 2);
  })">Cosa produrrebbe adesso (prerequisiti inclusi)</button>

  <button class="btn" onclick="edApi('ytprod/coda',{}).then(r=>{
    document.getElementById('ytprod-out').textContent = JSON.stringify(r, null, 2);
  })">Ordine dei lavori</button>

  <pre id="ytprod-out" class="log-pane">Premi un bottone.</pre>
</div>
"""

TILE = {
    "id": "ytprod",
    "icon": "\U0001F3AC",
    "name": "Produci video + copertina",
    "desc": "YouTube Factory: F1→F5 + copertina Arena + video Fliki (crediti reali, decine di minuti)",
    "kind": "py",
    "script": "YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py",
    "cwd": "YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS",
    "input": None,
}

MODULE = {
    "id": "yt_produzione",
    "tile": TILE,
    "routes": {
        "ytprod/stato": stato,
        "ytprod/coda": coda,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Verifica che il pulsante sia LANCIABILE, senza lanciarlo (Mandato Art.4.3: zero
    esecuzioni durante un selftest — qui girerebbe una produzione vera con spesa reale)."""
    if not RUNNER.exists():
        return False, f"yt_produzione: runner non trovato ({RUNNER})"
    mancanti = [str(p) for p in (SCRIPTS_DIR / "apex7_orchestrator.py",
                                 SCRIPTS_DIR / "arena_thumbnail.py",
                                 SCRIPTS_DIR / "fliki_client.py") if not p.exists()]
    if mancanti:
        return False, f"yt_produzione: pezzi della catena mancanti: {', '.join(mancanti)}"
    mod = _runner()
    if mod is None:
        return False, f"yt_produzione: runner presente ma non importabile ({RUNNER})"
    pronti = mod.script_pronti()
    da_fare = [s for s in pronti if s not in mod.video_gia_prodotti()]
    return True, (f"yt_produzione: catena completa presente, {len(pronti)} script adattati, "
                  f"{len(da_fare)} pronti da produrre "
                  f"({', '.join(da_fare) if da_fare else 'nessuno'})")
