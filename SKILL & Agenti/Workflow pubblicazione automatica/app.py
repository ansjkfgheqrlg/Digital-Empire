"""
Digital Empire — Auto Publisher
UI: pywebview (WebView2/Edge) con HTML/CSS premium
"""
import sys, json, subprocess, threading
from pathlib import Path
from datetime import datetime

import webview

# ── PATHS ────────────────────────────────────────────────────────────────────
if getattr(sys, "frozen", False):
    WORKFLOW = Path(sys.executable).parent
else:
    WORKFLOW = Path(__file__).parent

PUBLISH_SCRIPT = WORKFLOW / "scripts" / "ig_carousel_publish.py"
HEALTH_SCRIPT  = WORKFLOW / "scripts" / "health_check.py"
SETUP_SCRIPT   = WORKFLOW / "setup_scheduler.py"
PUBLISHED_LOG  = WORKFLOW / "published.json"
CAROSELLI_DIR  = Path(r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\Lancio corso skill beast\Page\caroselli - Agency\Nuovi")
PYTHON         = sys.executable if not getattr(sys, "frozen", False) else "python"
VALID_EXT      = {".png", ".jpg", ".jpeg", ".webp"}

# ── HELPERS ──────────────────────────────────────────────────────────────────
def _run(args, timeout=60):
    return subprocess.run(
        [PYTHON] + [str(a) for a in args],
        capture_output=True, text=True,
        encoding="utf-8", errors="replace",
        timeout=timeout, cwd=str(WORKFLOW),
    )

def _load_carousels():
    pub = {}
    if PUBLISHED_LOG.exists():
        try: pub = json.loads(PUBLISHED_LOG.read_text("utf-8"))
        except Exception: pass
    rows = []
    if not CAROSELLI_DIR.exists():
        return rows, pub
    for f in sorted(CAROSELLI_DIR.iterdir()):
        if not f.is_dir(): continue
        imgs = [x for x in f.iterdir() if x.suffix.lower() in VALID_EXT]
        cap  = (f / "caption.txt").exists()
        if f.name in pub:
            stato = "pubblicato"
            date  = pub[f.name].get("published_at", "")[:10]
        elif imgs and cap:
            stato = "pronto"
            date  = ""
        elif not imgs:
            stato = "no_img"
            date  = ""
        else:
            stato = "no_cap"
            date  = ""
        rows.append({"nome": f.name, "img": len(imgs), "stato": stato, "date": date})
    return rows, pub

# ── API (Python ↔ JS) ────────────────────────────────────────────────────────
class API:
    def __init__(self):
        self._win = None
        self._busy = False

    def health_check(self):
        try:
            r = _run([HEALTH_SCRIPT], timeout=30)
            ok = r.returncode == 0
            rows, _ = _load_carousels()
            n_ready = sum(1 for c in rows if c["stato"] == "pronto")
            n_pub   = sum(1 for c in rows if c["stato"] == "pubblicato")
            msg = f"{n_ready} pronti · {n_pub} pubblicati"
            if not ok:
                errs = [l for l in r.stdout.splitlines() if "[ERR]" in l]
                msg = errs[0].replace("[ERR]", "").strip() if errs else "Controlla errori"
            return {"ok": ok, "msg": msg, "n_ready": n_ready, "n_pub": n_pub}
        except Exception as e:
            return {"ok": False, "msg": str(e), "n_ready": 0, "n_pub": 0}

    def get_carousels(self):
        rows, _ = _load_carousels()
        return rows

    def publish_next(self):
        if self._busy:
            return {"ok": False, "msg": "Già in esecuzione"}
        rows, _ = _load_carousels()
        ready = [c for c in rows if c["stato"] == "pronto"]
        if not ready:
            return {"ok": False, "msg": "Nessun carosello pronto"}
        nome = ready[0]["nome"]
        self._busy = True
        def _do():
            try:
                r = _run([PUBLISH_SCRIPT, "--folder", nome, "--visible"], timeout=200)
                ok = r.returncode == 0
                out = r.stdout[-300:] if r.stdout else r.stderr[-300:]
                if self._win:
                    payload = json.dumps({"ok": ok, "nome": nome, "msg": out})
                    self._win.evaluate_js(f"onPublishDone({payload})")
            except Exception as e:
                if self._win:
                    payload = json.dumps({"ok": False, "nome": nome, "msg": str(e)})
                    self._win.evaluate_js(f"onPublishDone({payload})")
            finally:
                self._busy = False
        threading.Thread(target=_do, daemon=True).start()
        return {"ok": True, "nome": nome, "msg": "Avviato"}

    def set_schedule(self, time_str):
        try:
            r = _run([SETUP_SCRIPT, "--time", time_str], timeout=15)
            return {"ok": r.returncode == 0}
        except Exception as e:
            return {"ok": False, "msg": str(e)}

    def remove_schedule(self):
        try:
            r = _run([SETUP_SCRIPT, "--remove"], timeout=10)
            return {"ok": r.returncode == 0}
        except Exception as e:
            return {"ok": False, "msg": str(e)}

    def close_win(self):
        if self._win:
            self._win.destroy()

    def minimize_win(self):
        if self._win:
            self._win.minimize()

    def move_win(self, dx, dy):
        if self._win:
            try:
                x, y = self._win.x, self._win.y
                self._win.move(x + int(dx), y + int(dy))
            except Exception:
                pass

# ── HTML ─────────────────────────────────────────────────────────────────────
HTML = r"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DE Publisher</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  :root{
    --bg:#080808;
    --card:rgba(255,255,255,.035);
    --card-b:rgba(255,255,255,.07);
    --card2:rgba(255,255,255,.06);
    --acc:#FF3D00;
    --acc2:#CC2E00;
    --w:#FFFFFF;
    --g:#505050;
    --lg:#888;
    --green:#22C55E;
    --red:#EF4444;
    --warn:#F59E0B;
    --r:12px;
  }
  html,body{width:100%;height:100%;overflow:hidden;background:var(--bg)}
  body{
    font-family:'Segoe UI',system-ui,-apple-system,sans-serif;
    color:var(--w);
    background:
      radial-gradient(ellipse at 92% 3%, rgba(210,42,4,.22) 0%,
        rgba(140,20,0,.10) 28%, transparent 52%),
      var(--bg);
    display:flex;flex-direction:column;
    -webkit-user-select:none;user-select:none;
  }
  /* grain */
  body::before{
    content:'';position:fixed;inset:0;
    background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'
      width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence
      type='fractalNoise' baseFrequency='.75' numOctaves='4'
      stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200'
      filter='url(%23n)' opacity='1'/%3E%3C/svg%3E") repeat;
    opacity:.07;mix-blend-mode:screen;pointer-events:none;z-index:9999;
  }

  /* scrollbar */
  ::-webkit-scrollbar{width:4px}
  ::-webkit-scrollbar-track{background:transparent}
  ::-webkit-scrollbar-thumb{background:rgba(255,255,255,.1);border-radius:2px}

  /* title bar */
  #bar{
    height:44px;min-height:44px;
    display:flex;align-items:center;
    padding:0 16px;
    background:rgba(0,0,0,.5);
    border-bottom:1px solid rgba(255,255,255,.05);
    -webkit-app-region:drag;
    cursor:default;
    flex-shrink:0;
  }
  #bar-logo{font-size:13px;font-weight:700;color:var(--w);letter-spacing:.04em}
  #bar-logo span{color:var(--acc)}
  #bar-right{
    margin-left:auto;display:flex;gap:6px;
    -webkit-app-region:no-drag;
  }
  .wbtn{
    width:28px;height:28px;border-radius:6px;border:none;cursor:pointer;
    background:rgba(255,255,255,.05);color:var(--lg);font-size:13px;
    display:flex;align-items:center;justify-content:center;
    transition:background .15s,color .15s;
  }
  .wbtn:hover{background:rgba(255,255,255,.1);color:var(--w)}
  #btn-close:hover{background:rgba(239,68,68,.25);color:var(--red)}

  /* main scroll */
  #main{flex:1;overflow-y:auto;padding:16px 18px;display:flex;flex-direction:column;gap:10px}

  /* cards */
  .card{
    background:var(--card);
    border:1px solid var(--card-b);
    border-radius:var(--r);
    padding:14px 16px;
  }
  .card-label{font-size:9px;font-weight:700;letter-spacing:.12em;color:var(--g);text-transform:uppercase;margin-bottom:8px}

  /* status */
  #status-row{display:flex;align-items:center;gap:10px}
  #dot{
    width:10px;height:10px;border-radius:50%;background:var(--g);
    flex-shrink:0;transition:background .3s;
  }
  #dot.ok{background:var(--green);box-shadow:0 0 8px rgba(34,197,94,.5);animation:pulse 2.5s ease-in-out infinite}
  #dot.err{background:var(--red);box-shadow:0 0 8px rgba(239,68,68,.4)}
  #dot.warn{background:var(--warn)}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
  #status-text{font-size:14px;font-weight:600;color:var(--w);flex:1}
  #status-sub{font-size:11px;color:var(--lg);margin-top:4px}
  #btn-refresh{
    width:30px;height:30px;border-radius:7px;border:1px solid var(--card-b);
    background:transparent;color:var(--lg);font-size:15px;cursor:pointer;
    display:flex;align-items:center;justify-content:center;
    transition:all .15s;flex-shrink:0;
  }
  #btn-refresh:hover{background:var(--card2);color:var(--w)}
  #btn-refresh.spin{animation:spin .6s linear}
  @keyframes spin{to{transform:rotate(360deg)}}

  /* next */
  #next-row{display:flex;align-items:center;justify-content:space-between}
  #next-name{font-size:15px;font-weight:700;color:var(--w)}
  #next-slides{font-size:11px;color:var(--lg)}
  #next-badge{
    font-size:9px;font-weight:700;letter-spacing:.1em;
    background:rgba(34,197,94,.12);color:var(--green);
    border:1px solid rgba(34,197,94,.2);
    border-radius:4px;padding:3px 7px;
  }

  /* publish btn */
  #btn-pub{
    width:100%;height:56px;border-radius:var(--r);border:none;
    background:linear-gradient(135deg,#FF4500 0%,#CC2E00 100%);
    color:var(--w);font-size:16px;font-weight:700;letter-spacing:.03em;
    cursor:pointer;
    box-shadow:0 4px 24px rgba(255,61,0,.3);
    transition:all .15s;
    position:relative;overflow:hidden;
    display:flex;align-items:center;justify-content:center;gap:8px;
  }
  #btn-pub::before{
    content:'';position:absolute;inset:0;
    background:linear-gradient(135deg,rgba(255,255,255,.08) 0%,transparent 60%);
  }
  #btn-pub:hover:not(:disabled){
    transform:translateY(-1px);
    box-shadow:0 6px 32px rgba(255,61,0,.45);
  }
  #btn-pub:active:not(:disabled){transform:translateY(0)}
  #btn-pub:disabled{
    background:rgba(255,255,255,.06);
    box-shadow:none;color:var(--g);cursor:not-allowed;
  }

  /* schedule */
  #sched-row{display:flex;align-items:center;gap:8px}
  #sched-label{font-size:11px;color:var(--lg);flex:1}
  #time-in{
    width:72px;height:32px;border-radius:7px;
    border:1px solid rgba(255,255,255,.1);
    background:rgba(255,255,255,.04);
    color:var(--w);font-size:13px;font-weight:600;
    text-align:center;outline:none;
    transition:border-color .15s;
  }
  #time-in:focus{border-color:rgba(255,61,0,.5)}
  #time-in::placeholder{color:var(--g)}
  .sbtn{
    height:32px;padding:0 12px;border-radius:7px;border:1px solid rgba(255,255,255,.09);
    background:rgba(255,255,255,.05);color:var(--lg);font-size:11px;font-weight:600;
    cursor:pointer;letter-spacing:.04em;
    transition:all .15s;
  }
  .sbtn:hover{background:rgba(255,255,255,.09);color:var(--w)}
  #btn-remove-s{color:var(--red);padding:0 8px;font-size:14px}
  #btn-remove-s:hover{background:rgba(239,68,68,.12);border-color:rgba(239,68,68,.25)}

  /* list btn */
  #btn-list{
    width:100%;height:40px;border-radius:var(--r);
    border:1px solid rgba(255,255,255,.08);
    background:rgba(255,255,255,.03);
    color:var(--lg);font-size:13px;cursor:pointer;
    transition:all .15s;letter-spacing:.02em;
    display:flex;align-items:center;justify-content:center;gap:8px;
  }
  #btn-list:hover{background:rgba(255,255,255,.06);color:var(--w);border-color:rgba(255,255,255,.12)}

  /* log */
  #log-wrap{
    background:rgba(0,0,0,.4);border:1px solid rgba(255,255,255,.05);
    border-radius:var(--r);height:140px;overflow-y:auto;padding:10px 12px;
    flex-shrink:0;
  }
  .log-line{font-family:'Cascadia Code','Consolas','Courier New',monospace;font-size:10px;color:#444;line-height:1.7}
  .log-line.ok{color:#2d6e3e}
  .log-line.err{color:#7a2020}
  .log-line .ts{color:#333}

  /* footer */
  #footer{
    height:28px;min-height:28px;
    display:flex;align-items:center;justify-content:center;
    font-size:9px;color:rgba(255,255,255,.08);letter-spacing:.06em;
    border-top:1px solid rgba(255,255,255,.04);
    flex-shrink:0;
  }

  /* OVERLAY */
  #overlay{
    display:none;position:fixed;inset:0;
    background:rgba(0,0,0,.8);backdrop-filter:blur(8px);
    z-index:1000;align-items:center;justify-content:center;
  }
  #overlay.show{display:flex}
  #modal{
    background:#0F0F0F;border:1px solid rgba(255,255,255,.1);
    border-radius:16px;width:440px;max-height:500px;
    display:flex;flex-direction:column;overflow:hidden;
  }
  #modal-header{
    padding:16px 20px;border-bottom:1px solid rgba(255,255,255,.07);
    display:flex;align-items:center;
  }
  #modal-title{font-size:13px;font-weight:700;letter-spacing:.04em;color:var(--w);flex:1}
  #modal-close{
    width:26px;height:26px;border-radius:6px;border:none;cursor:pointer;
    background:rgba(255,255,255,.06);color:var(--lg);font-size:12px;
    transition:all .15s;
  }
  #modal-close:hover{background:rgba(239,68,68,.2);color:var(--red)}
  #modal-body{flex:1;overflow-y:auto;padding:12px 16px;display:flex;flex-direction:column;gap:6px}
  .row{
    display:flex;align-items:center;gap:10px;
    background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);
    border-radius:9px;padding:10px 14px;
  }
  .row-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
  .row-nome{font-size:12px;font-weight:600;color:var(--w);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .row-slides{font-size:10px;color:var(--g)}
  .row-stato{font-size:9px;font-weight:700;letter-spacing:.06em}

  /* confirm */
  #confirm{
    display:none;position:fixed;inset:0;
    background:rgba(0,0,0,.85);backdrop-filter:blur(12px);
    z-index:2000;align-items:center;justify-content:center;
  }
  #confirm.show{display:flex}
  #confirm-box{
    background:#111;border:1px solid rgba(255,255,255,.1);
    border-radius:14px;padding:28px;width:340px;text-align:center;
  }
  #confirm-title{font-size:13px;font-weight:700;color:var(--w);margin-bottom:8px}
  #confirm-sub{font-size:12px;color:var(--lg);line-height:1.5;margin-bottom:20px}
  #confirm-btns{display:flex;gap:8px}
  .cbtn{flex:1;height:38px;border-radius:8px;border:none;cursor:pointer;font-size:13px;font-weight:600;transition:all .15s}
  #cbtn-cancel{background:rgba(255,255,255,.07);color:var(--lg)}
  #cbtn-cancel:hover{background:rgba(255,255,255,.1);color:var(--w)}
  #cbtn-ok{background:var(--acc);color:var(--w)}
  #cbtn-ok:hover{background:var(--acc2)}

  /* toast */
  #toast{
    position:fixed;bottom:40px;left:50%;transform:translateX(-50%) translateY(20px);
    background:#1A1A1A;border:1px solid rgba(255,255,255,.1);
    border-radius:8px;padding:10px 18px;font-size:12px;color:var(--w);
    opacity:0;transition:all .25s;z-index:9998;pointer-events:none;
    white-space:nowrap;
  }
  #toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
  #toast.ok{border-color:rgba(34,197,94,.3);color:var(--green)}
  #toast.err{border-color:rgba(239,68,68,.3);color:var(--red)}
</style>
</head>
<body>

<!-- Title bar -->
<div id="bar">
  <div id="bar-logo">⚡ DIGITAL EMPIRE <span>· PUBLISHER</span></div>
  <div id="bar-right">
    <button class="wbtn" onclick="pywebview.api.minimize_win()">−</button>
    <button class="wbtn" id="btn-close" onclick="pywebview.api.close_win()">✕</button>
  </div>
</div>

<!-- Main -->
<div id="main">

  <!-- Status -->
  <div class="card">
    <div class="card-label">Stato sistema</div>
    <div id="status-row">
      <div id="dot"></div>
      <div id="status-text">Controllo...</div>
      <button id="btn-refresh" title="Aggiorna" onclick="doRefresh()">↻</button>
    </div>
    <div id="status-sub"></div>
  </div>

  <!-- Next -->
  <div class="card">
    <div class="card-label">Prossimo carosello</div>
    <div id="next-row">
      <div>
        <div id="next-name">—</div>
        <div id="next-slides" style="margin-top:3px"></div>
      </div>
      <div id="next-badge" style="display:none">PRONTO</div>
    </div>
  </div>

  <!-- Publish -->
  <button id="btn-pub" disabled onclick="askPublish()">
    <span>🚀</span><span id="pub-label">PUBBLICA ORA</span>
  </button>

  <!-- Schedule -->
  <div class="card">
    <div class="card-label">Pubblicazione automatica</div>
    <div id="sched-row">
      <div id="sched-label">Orario giornaliero</div>
      <input id="time-in" type="text" placeholder="18:00" maxlength="5">
      <button class="sbtn" onclick="doSetSched()">IMPOSTA</button>
      <button class="sbtn" id="btn-remove-s" title="Rimuovi scheduler" onclick="doRemoveSched()">✕</button>
    </div>
  </div>

  <!-- List -->
  <button id="btn-list" onclick="openList()">
    <span>📋</span><span>LISTA CAROSELLI</span>
  </button>

  <!-- Log -->
  <div class="card-label" style="margin-top:4px">LOG</div>
  <div id="log-wrap"></div>

</div>

<!-- Footer -->
<div id="footer">DIGITAL EMPIRE  ·  AUTO PUBLISHER  ·  2026</div>

<!-- List overlay -->
<div id="overlay" onclick="closeList(event)">
  <div id="modal">
    <div id="modal-header">
      <div id="modal-title">TUTTI I CAROSELLI</div>
      <button id="modal-close" onclick="closeList()">✕</button>
    </div>
    <div id="modal-body" id="modal-body"></div>
  </div>
</div>

<!-- Confirm -->
<div id="confirm">
  <div id="confirm-box">
    <div id="confirm-title"></div>
    <div id="confirm-sub"></div>
    <div id="confirm-btns">
      <button class="cbtn" id="cbtn-cancel" onclick="confirmNo()">ANNULLA</button>
      <button class="cbtn" id="cbtn-ok" onclick="confirmYes()">PUBBLICA</button>
    </div>
  </div>
</div>

<!-- Toast -->
<div id="toast"></div>

<script>
let _confirmCb = null;
let _nextNome  = null;
let _publishing = false;

// ── init ────────────────────────────────────────────────────────────────────
window.addEventListener('pywebviewready', () => { doRefresh(); });

// ── log ────────────────────────────────────────────────────────────────────
function log(msg, type='') {
  const wrap = document.getElementById('log-wrap');
  const ts = new Date().toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
  const el = document.createElement('div');
  el.className = 'log-line' + (type ? ' '+type : '');
  el.innerHTML = `<span class="ts">[${ts}]</span> ${msg}`;
  wrap.appendChild(el);
  wrap.scrollTop = wrap.scrollHeight;
  if (wrap.children.length > 120) wrap.removeChild(wrap.firstChild);
}

// ── toast ───────────────────────────────────────────────────────────────────
function toast(msg, type='', ms=2800) {
  const el = document.getElementById('toast');
  el.textContent = msg;
  el.className = 'show' + (type ? ' '+type : '');
  setTimeout(() => { el.className = ''; }, ms);
}

// ── refresh ─────────────────────────────────────────────────────────────────
async function doRefresh() {
  const btn = document.getElementById('btn-refresh');
  btn.classList.add('spin');
  document.getElementById('status-text').textContent = 'Controllo...';
  document.getElementById('dot').className = '';
  log('Health check in corso...');

  try {
    const r = await window.pywebview.api.health_check();
    const dot = document.getElementById('dot');
    const stxt = document.getElementById('status-text');
    const ssub = document.getElementById('status-sub');

    if (r.ok) {
      dot.className = 'ok';
      stxt.textContent = 'Sistema pronto';
      log('Sistema OK — ' + r.msg, 'ok');
    } else {
      dot.className = 'err';
      stxt.textContent = 'Problema rilevato';
      log('ERRORE: ' + r.msg, 'err');
    }
    ssub.textContent = r.msg;

    // next carousel
    const rows = await window.pywebview.api.get_carousels();
    const ready = rows.filter(c => c.stato === 'pronto');
    const next = document.getElementById('next-name');
    const nsub = document.getElementById('next-slides');
    const nbadge = document.getElementById('next-badge');
    const pub = document.getElementById('btn-pub');

    if (ready.length > 0) {
      _nextNome = ready[0].nome;
      next.textContent = ready[0].nome;
      nsub.textContent = ready[0].img + ' slide';
      nbadge.style.display = 'block';
      pub.disabled = !r.ok;
    } else {
      _nextNome = null;
      next.textContent = 'Nessuno';
      nsub.textContent = 'Tutti pubblicati o mancano caption';
      nbadge.style.display = 'none';
      pub.disabled = true;
    }
  } catch(e) {
    log('Errore: ' + e, 'err');
  }

  btn.classList.remove('spin');
}

// ── publish ──────────────────────────────────────────────────────────────────
function askPublish() {
  if (!_nextNome || _publishing) return;
  document.getElementById('confirm-title').textContent = 'Pubblica su Instagram';
  document.getElementById('confirm-sub').innerHTML =
    'Stai per pubblicare:<br><strong style="color:#fff;font-size:14px">' + _nextNome + '</strong>';
  _confirmCb = doPublish;
  document.getElementById('confirm').classList.add('show');
}

async function doPublish() {
  _publishing = true;
  const pub = document.getElementById('btn-pub');
  pub.disabled = true;
  document.getElementById('pub-label').textContent = 'IN CORSO...';
  log('Avvio pubblicazione: ' + _nextNome);

  try {
    const r = await window.pywebview.api.publish_next();
    if (r.ok) {
      log('Avviato — attendo conferma IG...', 'ok');
    } else {
      _publishing = false;
      pub.disabled = false;
      document.getElementById('pub-label').textContent = 'PUBBLICA ORA';
      log('ERRORE: ' + r.msg, 'err');
      toast('Errore: ' + r.msg, 'err');
    }
  } catch(e) {
    _publishing = false;
    pub.disabled = false;
    document.getElementById('pub-label').textContent = 'PUBBLICA ORA';
    log('Errore: ' + e, 'err');
  }
}

function onPublishDone(r) {
  _publishing = false;
  const pub = document.getElementById('btn-pub');
  document.getElementById('pub-label').textContent = 'PUBBLICA ORA';
  if (r.ok) {
    log('PUBBLICATO: ' + r.nome, 'ok');
    toast('Pubblicato! ' + r.nome, 'ok');
    doRefresh();
  } else {
    pub.disabled = false;
    log('FALLITO: ' + r.msg.slice(-100), 'err');
    toast('Pubblicazione fallita', 'err');
  }
}

// ── schedule ────────────────────────────────────────────────────────────────
async function doSetSched() {
  const t = document.getElementById('time-in').value.trim();
  if (!t || t.length !== 5 || !t.includes(':')) {
    toast('Formato: HH:MM (es. 18:00)', 'err'); return;
  }
  const r = await window.pywebview.api.set_schedule(t);
  if (r.ok) {
    log('Scheduler impostato: ' + t, 'ok');
    toast('Automatico ogni giorno alle ' + t, 'ok');
  } else {
    log('Errore scheduler', 'err');
    toast('Errore — prova come Amministratore', 'err');
  }
}

async function doRemoveSched() {
  const r = await window.pywebview.api.remove_schedule();
  if (r.ok) { log('Scheduler rimosso'); toast('Scheduler rimosso'); }
  else       { toast('Errore rimozione', 'err'); }
}

// ── list ────────────────────────────────────────────────────────────────────
async function openList() {
  const rows = await window.pywebview.api.get_carousels();
  const body = document.getElementById('modal-body');
  body.innerHTML = '';
  const colors = { pronto:'#22C55E', pubblicato:'#555', no_img:'#EF4444', no_cap:'#F59E0B' };
  const labels = { pronto:'PRONTO', pubblicato:'PUBBLICATO', no_img:'NO IMG', no_cap:'NO CAPTION' };
  rows.forEach(c => {
    const col = colors[c.stato] || '#555';
    const lbl = labels[c.stato] || c.stato;
    body.innerHTML += `<div class="row">
      <div class="row-dot" style="background:${col}"></div>
      <div class="row-nome">${c.nome}</div>
      <div class="row-slides">${c.img} slide</div>
      <div class="row-stato" style="color:${col}">${lbl}${c.date ? ' '+c.date : ''}</div>
    </div>`;
  });
  document.getElementById('overlay').classList.add('show');
}
function closeList(e) {
  if (!e || e.target === document.getElementById('overlay'))
    document.getElementById('overlay').classList.remove('show');
}

// ── confirm ─────────────────────────────────────────────────────────────────
function confirmYes() {
  document.getElementById('confirm').classList.remove('show');
  if (_confirmCb) { _confirmCb(); _confirmCb = null; }
}
function confirmNo() {
  document.getElementById('confirm').classList.remove('show');
  _confirmCb = null;
}
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    document.getElementById('overlay').classList.remove('show');
    document.getElementById('confirm').classList.remove('show');
  }
});

// ── time input formatting ────────────────────────────────────────────────────
document.getElementById('time-in').addEventListener('input', function(e) {
  let v = e.target.value.replace(/\D/g,'');
  if (v.length >= 3) v = v.slice(0,2) + ':' + v.slice(2,4);
  e.target.value = v;
});
</script>
</body>
</html>"""

# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    api = API()
    win = webview.create_window(
        title="DE Publisher",
        html=HTML,
        js_api=api,
        width=560,
        height=700,
        min_size=(560, 700),
        resizable=False,
        frameless=True,
        background_color="#080808",
        easy_drag=True,
    )
    api._win = win
    webview.start(debug=False, private_mode=False)

if __name__ == "__main__":
    main()
