# -*- coding: utf-8 -*-
"""
A4 — modules/youtube.py (Half A, owner: Max — contratto dossier 17 §5.3)
YouTube Automation Factory dentro Aureus: espone i TOOL DETERMINISTICI della skill
`.claude/skills/youtube-automation-factory/` (seo_score, cashcow_check) + la gerarchia
agenti/workflow, così la fabbrica è usabile dall'app.

Regole vincolanti:
- RIUSA i tool della skill (ADR-003: wrap, non riscrivere). Nessuna logica duplicata.
- MAI numeri inventati (Mandato Art.2): calcola SOLO su ciò che l'utente passa; se la skill
  o gli script mancano, si dichiara «nessun dato», non si finge.
- Solo lettura + calcolo puro: questo modulo non lancia processi né tocca la rete.
- La parte agentica completa (/yt-factory) resta in Claude Code: qui vivono i pezzi
  deterministici + l'indice navigabile della fabbrica.
"""
import importlib.util
import json
import time
from pathlib import Path

# EmpireDesk/modules/youtube.py -> repo root = parents[2]
REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / ".claude" / "skills" / "youtube-automation-factory"
SCRIPTS_DIR = SKILL_DIR / "scripts"


def _load_skill_script(stem: str):
    """Importa a runtime un modulo dagli script della skill (riuso, non duplicazione).
    Ritorna il modulo o None se assente (dichiarato, mai finto)."""
    path = SCRIPTS_DIR / f"{stem}.py"
    if not path.exists():
        return None
    try:
        spec = importlib.util.spec_from_file_location(f"yt_skill_{stem}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        return mod
    except Exception:  # noqa: BLE001 — script rotto: si dichiara assente, non si inventa
        return None


def _parse_bool(v) -> bool:
    return str(v).strip().lower() in {"1", "true", "yes", "si", "sì", "y", "on"}


def seo_score(payload=None):
    """POST /api/youtube/seo_score — punteggio SEO 0-100 dei metadati passati.
    payload: {title, description, tags (str csv o list), keyword, thumbnail, subtitles}."""
    mod = _load_skill_script("seo_score")
    if mod is None:
        return {"stato": "nessun dato",
                "nota": "script seo_score.py non trovato nella skill",
                "fonte": str(SCRIPTS_DIR / "seo_score.py")}
    p = payload or {}
    tags = p.get("tags", [])
    if isinstance(tags, str):
        tags = [t for t in tags.split(",") if t.strip()]
    meta = {
        "title": p.get("title", ""),
        "description": p.get("description", ""),
        "tags": tags,
        "keyword": p.get("keyword", ""),
        "thumbnail": _parse_bool(p.get("thumbnail", False)),
        "subtitles": _parse_bool(p.get("subtitles", False)),
    }
    try:
        result = mod.compute(meta)
    except Exception as e:  # noqa: BLE001
        return {"stato": f"errore calcolo: {e}", "fonte": str(SCRIPTS_DIR / "seo_score.py")}
    result["stato"] = "ok"
    result["gate_seo_pass"] = result.get("total", 0) >= 70  # soglia seo-gate
    return result


def cashcow(payload=None):
    """POST /api/youtube/cashcow — indice Cash Cow 0-100 di un canale.
    payload: {channel, videos:[{views, age_hours, errors:[]}]}."""
    mod = _load_skill_script("cashcow_check")
    if mod is None:
        return {"stato": "nessun dato",
                "nota": "script cashcow_check.py non trovato nella skill",
                "fonte": str(SCRIPTS_DIR / "cashcow_check.py")}
    p = payload or {}
    videos = p.get("videos", [])
    if isinstance(videos, str):
        # accetta anche JSON incollato come stringa dal pannello
        try:
            videos = json.loads(videos)
        except ValueError:
            return {"stato": "errore: 'videos' non è JSON valido"}
    channel = {"channel": p.get("channel", "?"), "videos": videos}
    if not videos:
        return {"stato": "nessun dato", "nota": "nessun video fornito: non invento metriche"}
    try:
        result = mod.compute(channel)
    except Exception as e:  # noqa: BLE001
        return {"stato": f"errore calcolo: {e}", "fonte": str(SCRIPTS_DIR / "cashcow_check.py")}
    result["stato"] = "ok"
    return result


def info(payload=None):
    """POST /api/youtube/info — gerarchia navigabile della fabbrica (letta dai file reali)."""
    if not SKILL_DIR.is_dir():
        return {"stato": "nessun dato", "nota": "skill non installata", "fonte": str(SKILL_DIR)}

    def _names(sub):
        d = SKILL_DIR / sub
        return sorted(p.stem for p in d.glob("*.md")) if d.is_dir() else []

    return {
        "stato": "ok",
        "skill": "youtube-automation-factory",
        "comando_agentico": "/yt-factory (in Claude Code)",
        "pipeline": ["F1 Scouting", "F2 Selezione video (A/B)", "F3 Script",
                     "F4 Produzione", "F5 Pubblicazione", "F6 Audit → loop"],
        "operatori": _names("agents/operatori"),
        "controllo_gate": _names("agents/controllo"),
        "supporto": _names("agents/supporto"),
        "workflow": _names("workflows"),
        "reference": _names("references"),
        "tool_deterministici": sorted(p.name for p in SCRIPTS_DIR.glob("*.py")) if SCRIPTS_DIR.is_dir() else [],
        "fonte": str(SKILL_DIR),
    }


PANEL_HTML = """
<div id="panel-youtube" class="panel">
  <h2>🎬 YouTube Automation Factory</h2>
  <p class="hint">Tool deterministici della skill <code>/yt-factory</code> — calcolo solo su dati reali che inserisci. La parte con gli agenti gira in Claude Code.</p>

  <button class="btn" onclick="edApi('youtube/info',{}).then(r=>{
    document.getElementById('yt-out').textContent = JSON.stringify(r, null, 2);
  })">Mostra fabbrica (agenti/workflow)</button>

  <h3>Punteggio SEO di un video</h3>
  <input class="inp" id="yt-title" placeholder="Titolo del video"/>
  <input class="inp" id="yt-kw" placeholder="Keyword principale"/>
  <textarea class="inp" id="yt-desc" placeholder="Descrizione (prime 2 righe = hook+valore)"></textarea>
  <input class="inp" id="yt-tags" placeholder="Tag separati da virgola"/>
  <label class="hint"><input type="checkbox" id="yt-thumb"/> miniatura pronta</label>
  <label class="hint"><input type="checkbox" id="yt-subs"/> sottotitoli</label>
  <button class="btn" onclick="edApi('youtube/seo_score',{
    title:document.getElementById('yt-title').value,
    keyword:document.getElementById('yt-kw').value,
    description:document.getElementById('yt-desc').value,
    tags:document.getElementById('yt-tags').value,
    thumbnail:document.getElementById('yt-thumb').checked,
    subtitles:document.getElementById('yt-subs').checked
  }).then(r=>{document.getElementById('yt-out').textContent = JSON.stringify(r, null, 2);})">Calcola SEO</button>

  <h3>Indice Cash Cow di un canale</h3>
  <textarea class="inp" id="yt-videos" placeholder='[{"views":120000,"age_hours":800,"errors":[]}]'></textarea>
  <button class="btn" onclick="edApi('youtube/cashcow',{
    channel:'canale', videos:document.getElementById('yt-videos').value
  }).then(r=>{document.getElementById('yt-out').textContent = JSON.stringify(r, null, 2);})">Calcola Cash Cow</button>

  <pre id="yt-out" class="log-pane">Premi un bottone.</pre>
</div>
"""

MODULE = {
    "id": "youtube",
    "tile": None,  # è un pannello (zero bottoni finti nel grid), come metrics
    "routes": {
        "youtube/info": info,
        "youtube/seo_score": seo_score,
        "youtube/cashcow": cashcow,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Verde se la skill è installata e gli script sono importabili. Non lancia nulla, non usa la rete."""
    if not SKILL_DIR.is_dir():
        return False, f"youtube: skill non trovata in {SKILL_DIR}"
    ok = []
    for stem in ("seo_score", "cashcow_check"):
        m = _load_skill_script(stem)
        ok.append(f"{stem}={'ok' if m and hasattr(m, 'compute') else 'MANCANTE'}")
    tutti = all("=ok" in x for x in ok)
    return tutti, f"youtube: skill presente, tool [{', '.join(ok)}] (generato {time.strftime('%H:%M')})"
