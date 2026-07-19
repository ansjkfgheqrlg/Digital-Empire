# -*- coding: utf-8 -*-
"""
A3 — modules/licenze.py (Half A, owner: Max — contratto dossier 17 §5.3)
Wrap di gestione-licenze.py (kill-switch concessionari PreventivoForge) — ADR-003: si wrappa,
mai riscrivere. Zero secrets qui: config Gist e auth gh vivono accanto allo script (gitignorati).
"""
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "Clienti" / "Prof Autocad" / "preventivo-forge" / "gestione-licenze.py"
CONFIG = SCRIPT.parent / "licenze.config.json"

AZIONI = {"stato": False, "sospendi": True, "attiva": True, "aggiungi": True, "rimuovi": True}
# valore = richiede <id> concessionario


def _run(azione: str, arg: str = "") -> dict:
    """Lancia lo script REALE e riporta stdout/exit code — mai esiti simulati."""
    if azione not in AZIONI:
        return {"errore": f"azione non valida: {azione}. Valide: {list(AZIONI)}"}
    if AZIONI[azione] and not arg:
        return {"errore": f"'{azione}' richiede l'id del concessionario"}
    if not SCRIPT.exists():
        return {"errore": f"script non trovato: {SCRIPT}"}
    cmd = [sys.executable, str(SCRIPT), azione] + ([arg] if arg else [])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60, cwd=str(SCRIPT.parent))
        return {"azione": azione, "id": arg or None, "exit_code": r.returncode,
                "output": (r.stdout or "").strip(), "stderr": (r.stderr or "").strip()}
    except subprocess.TimeoutExpired:
        return {"errore": "timeout 60s (gh/Gist non risponde?)", "azione": azione}
    except OSError as e:
        return {"errore": f"lancio fallito: {e}", "azione": azione}


def stato(payload=None):
    """POST /api/licenze/stato — stato reale di tutti i concessionari (legge il Gist)."""
    return _run("stato")


def comanda(payload=None):
    """POST /api/licenze/comanda — {azione, id}. Azioni che bloccano/sbloccano: conferma in UI."""
    p = payload or {}
    return _run(p.get("azione", ""), p.get("id", ""))


PANEL_HTML = """
<div id="panel-licenze" class="panel">
  <h2>🔑 Licenze Concessionari (kill-switch)</h2>
  <p class="hint">Comanda gestione-licenze.py (Gist reale via gh). Sospendi = l'app del cliente si BLOCCA.</p>
  <button class="btn" onclick="edApi('licenze/stato',{}).then(r=>{
    document.getElementById('licenze-out').textContent = r.output || JSON.stringify(r, null, 2);
  })">Stato licenze</button>
  <div style="margin-top:8px">
    <input id="lic-id" placeholder="id concessionario" class="inp"/>
    <button class="btn" onclick="var i=document.getElementById('lic-id').value;
      if(i && confirm('SOSPENDERE '+i+'? La sua app si blocca.'))
        edApi('licenze/comanda',{azione:'sospendi',id:i}).then(r=>{
          document.getElementById('licenze-out').textContent = r.output || JSON.stringify(r,null,2);})">⛔ Sospendi</button>
    <button class="btn" onclick="var i=document.getElementById('lic-id').value;
      if(i) edApi('licenze/comanda',{azione:'attiva',id:i}).then(r=>{
          document.getElementById('licenze-out').textContent = r.output || JSON.stringify(r,null,2);})">✅ Attiva</button>
  </div>
  <pre id="licenze-out" class="log-pane">Premi «Stato licenze».</pre>
</div>
"""

MODULE = {
    "id": "licenze",
    "tile": None,
    "routes": {"licenze/stato": stato, "licenze/comanda": comanda},
    "panel_html": PANEL_HTML,
}


def selftest():
    """Probe: script + config + gh presenti. NESSUN lancio reale (niente chiamate al Gist)."""
    if not SCRIPT.exists():
        return False, f"licenze: script non trovato ({SCRIPT})"
    problemi = []
    if not CONFIG.exists():
        problemi.append("licenze.config.json assente (kill-switch non ancora inizializzato)")
    try:
        subprocess.run(["gh", "--version"], capture_output=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        problemi.append("gh CLI non trovato")
    if problemi:
        return True, "licenze: script ok — AVVISO: " + "; ".join(problemi)
    return True, "licenze: script + config + gh presenti"
