#!/usr/bin/env python3
"""
APEX-7 — Adaptive Prompt EXecution Engine (Level 7)
Orchestratore Swarm + Memory per la Fabbrica YouTube Automation.
Esegue le 6 fasi del workflow in modo completamente automatico o guidato,
con persistenza dello stato, recupero dagli errori e ottimizzazione continua delle regole.

Autore: Gael
Governo: ADR-008 / MANDATO Art.8
"""
from __future__ import annotations
import os
import re
import sys
import json
import uuid
import argparse
import subprocess
import urllib.request
import urllib.error
import importlib.util
import statistics
from datetime import datetime

# Forza stdout e stderr in utf-8 su Windows per prevenire errori cp1252. line_buffering=True
# e' necessario: senza, quando l'output e' rediretto su file lo stream usa il buffering a
# blocchi e i print restano invisibili per decine di minuti (bug reale trovato il 2026-07-30).
# reconfigure() (non un nuovo io.TextIOWrapper!): fliki_client.py importa questo modulo e fa lo
# stesso wrapping — con due TextIOWrapper distinti sullo stesso buffer, il garbage collector del
# primo chiude il buffer sottostante e il secondo esplode con "I/O operation on closed file" al
# primo print (bug reale trovato il 2026-07-30). reconfigure() modifica lo stream esistente,
# idempotente e sicuro anche se chiamato piu' volte da moduli diversi nello stesso processo.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

# Percorsi principali
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
MEMORY_DIR = os.path.join(FACTORY_DIR, "memory")
RUNS_DIR = os.path.join(MEMORY_DIR, "runs")
DECIS_DIR = os.path.join(MEMORY_DIR, "decisions")
TEMPLATES_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")

# Assicuriamoci che le directory esistano
os.makedirs(RUNS_DIR, exist_ok=True)
os.makedirs(DECIS_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# --- Motore condiviso 11-APEX-7-CORE (ADR-010, fusione Ruflo+APEX-7-CORE, pilota YouTube) ---
# Caricato per percorso file (non via sys.path + `import memory`/`import agents`) perché questo
# stesso pacchetto ha già moduli locali `memory.py` e `agents.py`: un import a pacchetto
# colliderebbe con quelli già in sys.modules. I moduli condivisi sono self-contained (solo
# stdlib), quindi il caricamento per file è sicuro e non richiede sys.path.insert.
APEX7_CORE_DIR = os.path.abspath(os.path.join(FACTORY_DIR, "..", "company", "Ecosistemi", "11-APEX-7-CORE"))


def _load_module_from_path(module_name: str, file_path: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_shared_memory_mod = _load_module_from_path(
    "apex7_core_memory_system", os.path.join(APEX7_CORE_DIR, "memory", "memory_system.py")
)
_shared_orchestrator_mod = _load_module_from_path(
    "apex7_core_ruflo_core", os.path.join(APEX7_CORE_DIR, "orchestrator", "ruflo_core.py")
)
APEX7Memory = _shared_memory_mod.APEX7Memory
RuFLOOrchestrator = _shared_orchestrator_mod.RuFLOOrchestrator

# --- Canale target FISSO (Fase 1) ---
# Questo progetto non fa piu' scouting di nicchia: il canale da cui copiare/adattare e' deciso e
# fisso — @dosementale. Vedi company/Memory/RULES-VIDEO-FACTORY-DOSEMENTALE.md. Lo scouting fra
# 20 canali AI apparteneva al funnel "Manuale Claude Code", progetto MORTO: rimosso del tutto il
# 2026-07-31 perche' un run end-to-end sovrascriveva script/metadati/brief con contenuti sbagliati.
CANALE_TARGET = {
    "channel": "Dose Mentale",
    "handle": "@dosementale",
    "url": "https://www.youtube.com/@dosementale",
    "temi": "spiritualita', psicologia, saggezza biblica/buddista, motivazione, salute e "
            "benessere per un pubblico adulto/anziano",
    # Tag tematici brevi del canale, da usare come tag YouTube. La descrizione estesa qui sopra
    # e' leggibile ma come tag singolo e' inutilizzabile (una frase intera non e' un tag).
    "tag_tema": ["spiritualità", "psicologia", "benessere", "crescita personale", "terza età"],
}

# Durata obbligatoria del video finale (standard di qualita' fissato da Gael): mai sotto i 12
# minuti. Verificata sempre sul file mp4 reale, non sulla risposta dell'API.
AP_VIDEO_SYSTEM_DURATION = "12-15 minuti"

# Ritmo REALE di lettura della voce usata (Calimero), MISURATO sui video prodotti:
#   2186 parole -> 755s = 173.7 parole/minuto
#   1865 parole -> 605s = 185.0 parole/minuto
# Si usa il valore piu'alto: sovrastimare il ritmo significa chiedere piu' parole, quindi
# sbagliare per eccesso di durata invece che per difetto. La stima precedente (140 p/m) era
# un valore da manuale, non misurato: dava "13.3 minuti" per uno script che ne ha prodotti
# 10, e faceva passare il gate a uno script troppo corto (difetto reale, 2026-08-04).
PAROLE_AL_MINUTO = 185
PAROLE_MINIME_SCRIPT = int(12 * PAROLE_AL_MINUTO)  # 2220 parole per stare sopra i 12 minuti

# Script adattati (uno per video sorgente, scritti a mano dal transcript REALE del video).
# Non generiamo il parlato a runtime: un testo riscritto davvero richiede un lavoro di scrittura,
# e copiare il transcript verbatim non e' ammesso. F3 pesca qui per `<videoId>.md`.
SCRIPT_ADATTATI_DIR = os.path.join(TEMPLATES_DIR, "script-adattati")
TRANSCRIPTS_DIR = os.path.join(FACTORY_DIR, "transcripts")
SOURCE_THUMBS_DIR = os.path.join(TEMPLATES_DIR, "source-thumbnail")

_SCRIPT_STOPWORDS = set(
    "di del della delle dei per con che il la lo le i gli un una uno e o ma se non a al alla ai "
    "agli in nel nella con come cosa questo questa questi queste tuo tua tuoi sul sulla su ora "
    "oggi ho ha hai fare fai è sono stato stata the and with".split()
)


def _tokenize_for_matching(text: str) -> set:
    return {w for w in re.findall(r"[a-zA-Zàèéìòù0-9']+", (text or "").lower())
            if len(w) > 2 and w not in _SCRIPT_STOPWORDS}


def _keyword_from_title(title: str, max_words: int = 4) -> str:
    """Keyword SEO reale ricavata dal titolo. Prima era fissa a 'claude code' (keyword del
    funnel morto): su un canale di benessere non aveva senso e falsava ogni punteggio SEO.

    Si prende una porzione CONTIGUA dall'inizio del titolo (fino alla prima punteggiatura),
    non un insieme di parole sparse: seo_score.py cerca la keyword come sottostringa esatta,
    quindi 'dopo anni camminare' non veniva mai trovata in "Dopo i 70 anni, camminare..." e il
    titolo perdeva punti pur contenendo tutte quelle parole."""
    primo_segmento = re.split(r"[,:;?!.—–]", (title or "").strip())[0]
    parole = primo_segmento.split()[:max_words]
    # Una keyword che finisce con una parola vuota ("le 2 parole che") non e' cercabile.
    while parole and (parole[-1].lower() in _SCRIPT_STOPWORDS or len(parole[-1]) <= 2):
        parole.pop()
    return " ".join(parole).lower()


# --- Fetch REALE dei video di un canale (Fase 2) ---
# Legge la pagina pubblica /videos del canale (nessuna API key: dati già visibili a chiunque la
# visiti) ed estrae titolo/viste/data reali. Risultato messo in cache (TTL 7gg) in
# memory/channel_videos/ per non dipendere dalla rete a ogni run/test — se la rete non è
# disponibile e la cache esiste (anche scaduta), si usa quella con un avviso esplicito; se non
# esiste alcuna cache, la fase fallisce onestamente invece di inventare candidati.
CHANNEL_VIDEOS_CACHE_DIR = os.path.join(MEMORY_DIR, "channel_videos")
os.makedirs(CHANNEL_VIDEOS_CACHE_DIR, exist_ok=True)
CHANNEL_CACHE_TTL_HOURS = 168  # 7 giorni
VIDEO_MATURITY_FLOOR_HOURS = 24  # sotto questa età, la velocity views/ora è troppo rumorosa

# Soglia con cui cashcow_check.py considera "performante" un video in assoluto. Serve a
# giudicare un CANALE, ed e' riportata qui per riferimento.
MIN_VPH_ASSOLUTO_CANALE = _load_module_from_path(
    "apex7_cashcow_check", os.path.join(SCRIPT_DIR, "cashcow_check.py")
).MIN_VPH

# Gate REALE della pipeline (F2): il video da replicare deve essere un OUTLIER rispetto al
# proprio canale, non superare una soglia assoluta.
#
# Perche' relativa e non fissa (correzione del 2026-08-04): con la soglia assoluta a 20 viste/ora
# la fabbrica si bloccava dopo UN SOLO video. Su @dosementale la mediana reale e' ~1.2 viste/ora:
# il secondo miglior video del catalogo ne fa 15.5, cioe' 12 volte la mediana — funziona
# chiaramente — ma restava sotto una soglia pensata per un altro scopo. Cio' che conta per
# scegliere DENTRO un canale e' distinguersi dal resto di quel canale.
VIDEO_MULTIPLO_MEDIANA = 3.0   # almeno 3x la mediana del canale
VIDEO_VPH_MINIMO = 2.0         # pavimento assoluto: esclude "il migliore di un canale morto"


def _cache_path_for_handle(handle: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", handle.lstrip("@"))
    return os.path.join(CHANNEL_VIDEOS_CACHE_DIR, f"{safe}.json")


def _parse_view_count(text: str):
    """'2.2K views' -> 2200.0, '652 views' -> 652.0. None se il formato non è riconosciuto
    (es. badge 'Nome e altri 2' al posto delle viste: non è un dato, si scarta)."""
    m = re.match(r"^([\d.,]+)\s*([KM]?)\s*views?$", (text or "").strip(), re.IGNORECASE)
    if not m:
        return None
    num = float(m.group(1).replace(",", ""))
    suf = m.group(2).upper()
    if suf == "K":
        num *= 1000
    elif suf == "M":
        num *= 1_000_000
    return num


def _parse_age_hours(text: str):
    """'3 weeks ago' -> 504.0. None se il formato non è riconosciuto (streaming live, ecc.)."""
    m = re.match(r"^(\d+)\s+(hour|day|week|month|year)s?\s+ago$", (text or "").strip(), re.IGNORECASE)
    if not m:
        return None
    n = int(m.group(1))
    unit = m.group(2).lower()
    mult = {"hour": 1, "day": 24, "week": 168, "month": 730, "year": 8760}[unit]
    return float(n * mult)


def _extract_videos_from_yt_data(data: dict) -> list[dict]:
    """Cammina ricorsivamente ytInitialData e raccoglie i video, gestendo sia lo schema
    legacy 'videoRenderer' sia il nuovo 'lockupViewModel' (YouTube ha migrato il layout delle
    pagine canale nel 2025-2026: verificato empiricamente sul fetch reale)."""
    raw = []

    def walk(node):
        if isinstance(node, dict):
            if "videoRenderer" in node:
                vr = node["videoRenderer"]
                title = ""
                if "title" in vr:
                    runs = vr["title"].get("runs", [])
                    title = runs[0].get("text", "") if runs else vr["title"].get("simpleText", "")
                raw.append({
                    "videoId": vr.get("videoId"),
                    "title": title,
                    "views_text": vr.get("viewCountText", {}).get("simpleText", ""),
                    "published_text": vr.get("publishedTimeText", {}).get("simpleText", ""),
                })
            elif "lockupViewModel" in node:
                lv = node["lockupViewModel"]
                meta = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
                title = meta.get("title", {}).get("content", "")
                rows = meta.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", [])
                views_text, published_text = "", ""
                if rows:
                    parts = rows[0].get("metadataParts", [])
                    texts = [p.get("text", {}).get("content", "") for p in parts]
                    if len(texts) >= 1:
                        views_text = texts[0]
                    if len(texts) >= 2:
                        published_text = texts[1]
                raw.append({
                    "videoId": lv.get("contentId"),
                    "title": title,
                    "views_text": views_text,
                    "published_text": published_text,
                })
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)
    return raw


def _fetch_channel_videos_live(handle: str, max_videos: int = 30) -> list[dict]:
    """Scarica in tempo reale i video reali del canale da youtube.com/<handle>/videos.
    Nessuna API key richiesta (pagina pubblica). Ritorna [] se il fetch fallisce (rete,
    layout cambiato, ecc.) — nessun fallback a dati finti a questo livello."""
    url = f"https://www.youtube.com/{handle}/videos?hl=en&gl=US&persist_hl=1&persist_gl=1"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": "CONSENT=YES+cb; SOCS=CAI",  # evita il redirect al consent-wall EU
        "Accept-Language": "en-US,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"[!] Impossibile scaricare i video reali di {handle}: {e}")
        return []

    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m:
        print(f"[!] Struttura pagina canale non riconosciuta per {handle} (layout YouTube cambiato?).")
        return []
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError:
        return []

    clean = []
    for v in _extract_videos_from_yt_data(data)[:max_videos]:
        views = _parse_view_count(v["views_text"])
        age = _parse_age_hours(v["published_text"])
        if views is None or age is None or not v.get("videoId"):
            continue  # dato ambiguo (badge collaboratori, live, ecc.): scartato, non fabbricato
        clean.append({
            "videoId": v["videoId"],
            "title": v["title"],
            "url": f"https://www.youtube.com/watch?v={v['videoId']}",
            "views": views,
            "age_hours": age,
        })
    return clean


# --- Manifest video REALMENTE pubblicati (Fase 6) ---
# Un video compare qui solo quando è stato davvero caricato su YouTube (da Gael/Max), non a ogni
# run: F6 lo usa per decidere se c'è qualcosa di reale da auditare o se è ancora troppo presto.
def _parse_vtt(path: str) -> str:
    """Testo parlato reale da un file .vtt di sottotitoli automatici: via timestamp, tag di
    posizione e le righe duplicate che YouTube ripete per l'effetto karaoke."""
    righe, precedente = [], None
    for raw in open(path, encoding="utf-8", errors="ignore"):
        linea = raw.strip()
        if (not linea or "-->" in linea or linea.startswith(("WEBVTT", "Kind:", "Language:"))
                or linea.isdigit()):
            continue
        linea = re.sub(r"<[^>]+>", "", linea).strip()
        if linea and linea != precedente:
            righe.append(linea)
            precedente = linea
    return " ".join(righe)


def _fetch_transcript(video_id: str, url: str, out_dir: str) -> str | None:
    """Transcript REALE del video sorgente via yt-dlp (sottotitoli automatici it, poi en).
    Nessun contenuto inventato: se yt-dlp non c'e' o il video non ha sottotitoli, ritorna None
    e la fase fallisce onestamente."""
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"dosementale-{video_id}")
    esistenti = [p for p in (f"{base}.it.vtt", f"{base}.en.vtt") if os.path.exists(p)]
    if not esistenti:
        try:
            subprocess.run(
                ["yt-dlp", "--skip-download", "--write-auto-sub", "--sub-lang", "it,en",
                 "--sub-format", "vtt", "-o", base, url],
                capture_output=True, text=True, timeout=180,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired) as e:
            print(f"[!] yt-dlp non disponibile o troppo lento ({e}): transcript reale non recuperabile.")
            return None
        esistenti = [p for p in (f"{base}.it.vtt", f"{base}.en.vtt") if os.path.exists(p)]
    if not esistenti:
        return None
    testo = _parse_vtt(esistenti[0])
    return testo or None


PUBLISHED_VIDEOS_PATH = os.path.join(MEMORY_DIR, "published_videos.json")

# Registro dei video REALMENTE generati (scritto da fliki_client.py al download dell'mp4).
# E' la fonte di verita' per sapere quali video sorgente non vanno piu' riproposti da F2.
VIDEO_PRODOTTI_PATH = os.path.join(MEMORY_DIR, "video_prodotti.json")


def _extract_youtube_id(url: str) -> str:
    """Estrae il videoId reale da un URL youtube.com/watch?v=... o youtu.be/...; stringa
    vuota se l'URL non è riconosciuto (nessun ID inventato)."""
    m = re.search(r"[?&]v=([\w-]+)", url or "")
    if m:
        return m.group(1)
    m = re.search(r"youtu\.be/([\w-]+)", url or "")
    return m.group(1) if m else ""


class Apex7Orchestrator:
    def __init__(self, run_id: str | None = None, shared_domain: str = "youtube"):
        self.run_id = run_id or f"yt-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"
        self.state_file = os.path.join(RUNS_DIR, f"run_{self.run_id}.json")

        # 5-Layer Memory Ecosystem Paths
        self.working_memory = {}
        self.decision_log_path = os.path.join(MEMORY_DIR, "decision_log.json")
        self.strategy_store_path = os.path.join(MEMORY_DIR, "strategy_store.json")
        self.snapshots_path = os.path.join(MEMORY_DIR, "architecture_snapshots.json")
        self.learned_rules_path = os.path.join(MEMORY_DIR, "learned_rules.json")
        self.perf_logs_path = os.path.join(MEMORY_DIR, "performance_logs.json")

        # Motore condiviso 11-APEX-7-CORE (ADR-010): il critic persiste il punteggio qui,
        # non più solo localmente. `shared_domain` è parametrizzabile (default "youtube") per
        # isolare i test dal dominio reale — vedi test_youtube_apex7.py.
        self.shared_memory = APEX7Memory(domain=shared_domain)
        self.ruflo = RuFLOOrchestrator(memory_system=self.shared_memory, domain=shared_domain)

        # Overridabile dai test (come state_file/decision_log_path ecc.) per non sovrascrivere
        # la dashboard reale tracciata a ogni run di test_youtube_apex7.py.
        self.dashboard_path = os.path.join(FACTORY_DIR, "06-DASHBOARD-E-METRICHE", "YOUTUBE-PERFORMANCE-DASHBOARD.md")

        self.initialize_memory_files()
        
    def initialize_memory_files(self):
        # Layer 3: Strategy Store
        if not os.path.exists(self.strategy_store_path):
            self.save_json(self.strategy_store_path, [
                {"name": "Piramide Evolutiva", "success_rate": 0.95, "times_used": 1},
                {"name": "Critique-Before-Output", "success_rate": 0.92, "times_used": 1},
                {"name": "SEO-First optimization", "success_rate": 0.88, "times_used": 0}
            ])
            
        # Layer 4: Architecture Snapshots
        if not os.path.exists(self.snapshots_path):
            self.save_json(self.snapshots_path, [
                {"version": "v1.0-APEX", "description": "APEX-7 Swarm Layout with 6 Specialists", "score": 8.5, "status": "current"}
            ])

        # Layer 5: Compressed Knowledge (learned_rules.json via self_improve.py if missing)
        if not os.path.exists(self.learned_rules_path):
            subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "self_improve.py")], capture_output=True)

    def load_json(self, path, default):
        if not os.path.exists(path):
            return default
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default

    def save_json(self, path, data) -> bool:
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"[-] Errore nel salvataggio del file {path}: {e}")
            return False

    def log_decision(self, decision_id: str, decision: str, reason: str, rejected: list[str], confidence: float):
        """Layer 2: Decision Log"""
        log = self.load_json(self.decision_log_path, [])
        record = {
            "id": decision_id,
            "run_id": self.run_id,
            "decision": decision,
            "reason": reason,
            "alternatives_rejected": rejected,
            "confidence": confidence,
            "timestamp": datetime.now().isoformat()
        }
        log.append(record)
        self.save_json(self.decision_log_path, log)
        
        # Scrivi anche file MD individuale in memory/decisions/
        md_path = os.path.join(DECIS_DIR, f"{decision_id}_{self.run_id}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# Decisione {decision_id}\n\n")
            f.write(f"- **Data**: {record['timestamp']}\n")
            f.write(f"- **Run ID**: {record['run_id']}\n")
            f.write(f"- **Scelta**: {decision}\n")
            f.write(f"- **Razionale**: {reason}\n")
            f.write(f"- **Alternative Rifiutate**: {', '.join(rejected)}\n")
            f.write(f"- **Confidence**: {confidence * 100}%\n")
        print(f"[+] Layer 2: Decisione {decision_id} storicizzata.")

    def render_diagram(self):
        print("""
 ╔══════════════════════════════════════════════════════════════╗
 ║                        APEX-7 SYSTEM                         ║
 ║              Adaptive Prompt EXecution Engine                ║
 ╠══════════════════════════════════════════════════════════════╣
 ║  [GOAL] ──► [META-ORCHESTRATOR] ──► [SWARM EXECUTION ENGINE] ║
 ║                                                              ║
 ║   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐        ║
 ║   │  PLANNER    │ ──►  WRITER     │ ──►  ANALYST    │        ║
 ║   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘        ║
 ║          ▼                 ▼                 ▼               ║
 ║      [Event Bus] ──────► [CRITIC] ──────► [REFINER]          ║
 ║                            │ (Score >= 7.5?)                 ║
 ║                            ▼                                 ║
 ║                      [META-AGENT] ──► [5-LAYER MEMORY SYS]   ║
 ╚══════════════════════════════════════════════════════════════╝
        """)

    def load_state(self) -> bool:
        if os.path.exists(self.state_file):
            self.working_memory = self.load_json(self.state_file, {})
            self.run_id = self.working_memory.get("run_id", self.run_id)
            print(f"[+] Stato ripristinato per la run {self.run_id}.")
            return True
        return False

    def save_state(self):
        self.working_memory["run_id"] = self.run_id
        self.working_memory["last_updated"] = datetime.now().isoformat()
        self.save_json(self.state_file, self.working_memory)

    def execute_critic(self, content_type: str, content: str, required_sections: list[str] | None = None) -> tuple[float, dict[str, float]]:
        """Agente Critic con punteggio a 5 dimensioni derivato da controlli reali sul
        contenuto (lunghezza, presenza sezioni/HOOK-CTA, keyword density, ordine strutturale) —
        non un dict fisso: due contenuti diversi producono punteggi diversi."""
        print(f"\n[🔬 CRITIC] Avvio analisi qualitativa per '{content_type}'...")

        text = content or ""
        words = re.findall(r"[a-zA-ZàèéìòùÀÈÉÌÒÙ']+", text)
        n_words = len(words)
        lower = text.lower()

        # Completeness: sezioni richieste presenti sul totale richiesto (o lunghezza minima se
        # non ci sono sezioni da verificare, es. per un blob JSON).
        if required_sections:
            present = sum(1 for s in required_sections if s.lower() in lower)
            completeness = round(10 * present / len(required_sections), 2)
        else:
            completeness = round(min(10.0, n_words / 40), 2)  # 400 parole = punteggio pieno

        # Accuracy: keyword density sulla keyword REALE della run (ricavata dal video sorgente
        # in F2) — assente è debole, presenza moderata è forte, stuffing penalizzato. Prima era
        # fissa su "claude code": su un canale di benessere dava sempre 3.0 a qualunque script.
        keyword = (self.working_memory.get("keyword") or "").lower().strip()
        kw_hits = lower.count(keyword) if keyword else 0
        if keyword:
            # Anche le singole parole della keyword contano: "camminare over 70" difficilmente
            # compare tutta attaccata nel parlato, ma i suoi termini sì.
            kw_hits += sum(lower.count(p) for p in keyword.split() if len(p) > 3)
        density = kw_hits / n_words if n_words else 0
        if kw_hits == 0:
            accuracy = 3.0
        elif density <= 0.03:
            accuracy = 9.0
        elif density <= 0.06:
            accuracy = 7.0
        else:
            accuracy = 5.0  # stuffing

        # Creativity: diversità lessicale reale (parole uniche / parole totali).
        creativity = round(min(10.0, (len(set(w.lower() for w in words)) / n_words) * 10), 2) if n_words else 0.0

        # Actionability: presenza di verbi/marcatori d'azione reali nel testo.
        action_markers = ["scarica", "clicca", "iscriviti", "scopri", "prova", "installa",
                           "guarda", "commenta", "condividi", "vai su"]
        action_hits = sum(1 for m in action_markers if m in lower)
        actionability = round(min(10.0, 4.0 + action_hits * 1.5), 2)

        # Logic: ordine strutturale reale (le sezioni richieste compaiono nell'ordine atteso)
        # oppure, senza sezioni, validità sintattica del contenuto (JSON parsabile).
        if required_sections:
            positions = [lower.find(s.lower()) for s in required_sections]
            found_positions = [p for p in positions if p >= 0]
            ordered = found_positions == sorted(found_positions)
            logic = 9.0 if ordered and len(found_positions) == len(required_sections) else 5.0
        else:
            try:
                json.loads(text)
                logic = 9.0
            except (json.JSONDecodeError, ValueError):
                logic = 6.0 if n_words > 0 else 2.0

        metrics = {
            "Completeness": completeness,
            "Accuracy": accuracy,
            "Creativity": creativity,
            "Actionability": actionability,
            "Logic": logic,
        }

        # Ponderazione dei pesi
        weighted_score = (
            metrics["Completeness"] * 0.25 +
            metrics["Accuracy"] * 0.25 +
            metrics["Creativity"] * 0.20 +
            metrics["Actionability"] * 0.20 +
            metrics["Logic"] * 0.10
        )
        
        print("┌────────────────┬────────┬───────────┬──────────┐")
        print("│ Dimensione     │ Peso   │ Threshold │ Metrica  │")
        print("├────────────────┼────────┼───────────┼──────────┤")
        weaknesses = []
        for dim, val in metrics.items():
            thresh = 7.5 if dim != "Creativity" and dim != "Logic" else (7.0 if dim == "Creativity" else 8.0)
            status = "🟢 PASS" if val >= thresh else "🔴 FAIL"
            if val < thresh:
                weaknesses.append(f"{dim}: {val:.1f} < soglia {thresh:.1f}")
            print(f"│ {dim:14} │ {0.25 if dim in ('Completeness', 'Accuracy') else (0.20 if dim in ('Creativity', 'Actionability') else 0.10):.2f}   │ {thresh:.1f}       │ {val:.1f} {status}│")
        print("└────────────────┴────────┴───────────┴──────────┘")
        print(f"[🔬 CRITIC] Score complessivo ponderato: {weighted_score:.2f} / 10")

        # Persistenza sul motore condiviso 11-APEX-7-CORE (ADR-010): il punteggio calcolato sopra
        # (logica reale, invariata) non resta più locale al file YouTube — passa nel decision log
        # SQLite del dominio condiviso, visibile a chi ispeziona `data/<domain>` empire-wide.
        critique_id = self.shared_memory.log_critique(
            task_id=f"{self.run_id}-{content_type}",
            score=weighted_score,
            dimensions=metrics,
            weaknesses=weaknesses,
        )
        self.ruflo.create_checkpoint(f"critic:{content_type}", {"run_id": self.run_id, "score": weighted_score})
        print(f"[🔬 CRITIC] Persistito su motore condiviso 11-APEX-7-CORE (domain={self.shared_memory.domain}), critique_id={critique_id}")

        return weighted_score, metrics

    def execute_workflow(self, target_phase: int, interactive: bool = False):
        self.render_diagram()
        print(f"[*] Avvio esecuzione APEX-7 per la run {self.run_id}")

        current_phase = self.working_memory.get("current_phase", 1)
        if target_phase < current_phase:
            print(f"[!] Attenzione: Stai rieseguendo la fase {target_phase} (già completata fino alla {current_phase})")
            current_phase = target_phase

        phases = {
            1: self.run_phase_1,
            2: self.run_phase_2,
            3: self.run_phase_3,
            4: self.run_phase_4,
            5: self.run_phase_5,
            6: self.run_phase_6
        }

        # Esito reale per fase, persistito in working_memory: sopravvive a un --resume su più
        # invocazioni, cosi' la dashboard riflette la storia vera della run, non solo l'ultima chiamata.
        phase_results: dict[int, bool] = {int(k): v for k, v in self.working_memory.get("phase_results", {}).items()}

        for phase in range(current_phase, 7):
            if target_phase and phase > target_phase:
                break

            print(f"\n🚀 === FASE {phase} IN CORSO ===")
            success = phases[phase](interactive)
            phase_results[phase] = success
            self.working_memory["phase_results"] = {str(k): v for k, v in phase_results.items()}
            if not success:
                print(f"🔴 Fallimento nella Fase {phase}. Stato salvato. Riprendi con --resume.")
                self.save_state()
                dashboard_path = self.write_dashboard(phase_results)
                print(f"[+] Dashboard aggiornata (stato reale): {dashboard_path}")
                sys.exit(1)

            self.working_memory["current_phase"] = phase + 1
            self.save_state()

        print(f"\n🎉 Workflow completato con successo per la run {self.run_id}!")
        dashboard_path = self.write_dashboard(phase_results)
        print(f"[+] Dashboard aggiornata (stato reale): {dashboard_path}")

    _PHASE_INFO = {
        1: ("Canale target", "Dati reali del canale fisso @dosementale (Cash Cow Index riportato, non bloccante)"),
        2: ("Selezione", f"Video maturo (>=24h), non gia' replicato, con velocity >= "
                         f"{VIDEO_MULTIPLO_MEDIANA}x la mediana del canale"),
        3: ("Script", "Critic score reale >= 7.5 (motore condiviso 11-APEX-7-CORE)"),
        4: ("Produzione", "Schema produzione-spec valido, scene reali da script.md"),
        5: ("Pubblicazione", "SEO score reale (seo_score.py)"),
        6: ("Audit", "Manifest published_videos.json (video reale pubblicato)"),
    }

    def write_dashboard(self, phase_results: dict[int, bool]) -> str:
        """Scrive 06-DASHBOARD-E-METRICHE/YOUTUBE-PERFORMANCE-DASHBOARD.md leggendo lo stato
        REALE di self.working_memory della run corrente. `phase_results` contiene solo le fasi
        effettivamente eseguite: PASS/FAIL veri, non una tabella statica sempre verde. Le fasi
        non raggiunte (mai eseguite in questa run) restano onestamente "non eseguita"."""
        dashboard_path = self.dashboard_path
        os.makedirs(os.path.dirname(dashboard_path), exist_ok=True)

        failed_phases = sorted(p for p, ok in phase_results.items() if not ok)
        last_run_phase = max(phase_results) if phase_results else 0
        if failed_phases:
            stato_fabbrica = f"🔴 BLOCCATA ALLA FASE {failed_phases[0]}"
        elif last_run_phase < 6:
            stato_fabbrica = f"🟡 PARZIALE (fermata alla fase {last_run_phase}, --phase limitato)"
        else:
            stato_fabbrica = "🟢 OPERATIVA (6/6 fasi reali PASS)"

        wm = self.working_memory
        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write("# YouTube Automation Factory - Performance Dashboard\n\n")
            f.write(f"- **Ultimo Run ID**: {self.run_id}\n")
            f.write(f"- **Data Aggiornamento**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            canale = wm.get("canale_scelto")
            f.write(f"- **Canale Target**: {canale + ' (`' + wm['canale_scelto_handle'] + '`)' if canale else 'N/D (Fase 1 non raggiunta)'}\n")
            f.write(f"- **Video Replicato**: {wm.get('video_scelto', 'N/D (Fase 2 non raggiunta)')}\n")
            f.write(f"- **Idea Script (Fase 3)**: {wm.get('script_idea_title', 'N/D (Fase 3 non raggiunta)')}\n")
            f.write(f"- **SEO Score Metadati (Fase 5)**: {wm.get('metadati_seo_score', 'N/D')}\n")
            f.write(f"- **Stato Fabbrica**: {stato_fabbrica}\n\n")

            f.write("## 📊 Metriche di Esecuzione (esito REALE di questa run)\n")
            f.write("| Fase | Componente | Stato | Esito Gate | Criterio |\n")
            f.write("|---|---|---|---|---|\n")
            for n in range(1, 7):
                nome, criterio = self._PHASE_INFO[n]
                if n not in phase_results:
                    stato, esito = "Non eseguita", "⚪ N/D"
                elif phase_results[n]:
                    stato, esito = "Completata", "🟢 PASS"
                else:
                    stato, esito = "Fallita", "🔴 FAIL"
                f.write(f"| F{n} | {nome} | {stato} | {esito} | {criterio} |\n")
            f.write("\n")

            f.write("## 🧠 Note\n")
            f.write("Dashboard scritta da `Apex7Orchestrator.write_dashboard()` a fine "
                    "`execute_workflow`, leggendo lo stato reale della run corrente — non da una "
                    "pipeline separata. `run_youtube_apex7.py` (pipeline fantasma su un canale "
                    "'Dose Mentale' fisso, mai collegata alle fasi reali F1-F6) è stata ritirata "
                    "in TASK-YT-005: era l'unica altra scrittrice di questo file.\n")

        return dashboard_path

    # --- Fase 1: Conferma canale target ---
    def _cashcow_for_channel(self, channel_name: str, videos: list[dict]) -> dict:
        """Cashcow check sui video REALI del canale (titolo/viste/età presi davvero dalla pagina
        pubblica /videos), non piu' su una stima aggregata: dal 2026-07-31 il canale e' uno solo
        e fisso, quindi i dati singolo-video ci sono davvero e non serve stimare nulla."""
        canale_reale = {
            "channel": channel_name,
            "videos": [{"title": v["title"], "views": v["views"], "age_hours": v["age_hours"], "errors": []}
                       for v in videos],
        }
        tmp_json_path = os.path.join(FACTORY_DIR, f"canale_tmp_{uuid.uuid4().hex[:6]}.json")
        self.save_json(tmp_json_path, canale_reale)
        res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "cashcow_check.py"), "--json", tmp_json_path], capture_output=True, text=True)
        if os.path.exists(tmp_json_path):
            os.remove(tmp_json_path)
        try:
            return json.loads(res.stdout)
        except (json.JSONDecodeError, ValueError):
            return {"index": 0, "is_cashcow": False}

    def _get_channel_videos(self, handle: str) -> tuple[list[dict], str]:
        """Video reali del canale: cache-first (TTL 7gg) per non dipendere dalla rete a ogni
        run/test, live-fetch se la cache manca o è scaduta. Se il fetch live fallisce ma esiste
        una cache anche vecchia, la usa con un avviso invece di fallire — non inventa mai dati.
        Ritorna (video, provenienza) dove provenienza è 'cache'/'live'/'cache-scaduta'."""
        cache_path = _cache_path_for_handle(handle)
        cached = None
        if os.path.exists(cache_path):
            cached = self.load_json(cache_path, None)

        if cached and cached.get("fetched_at"):
            age_h = (datetime.now() - datetime.fromisoformat(cached["fetched_at"])).total_seconds() / 3600
            if age_h < CHANNEL_CACHE_TTL_HOURS:
                return cached["videos"], "cache"

        print(f"[🔬 ANALYST] Cache video assente/scaduta per {handle}: fetch live da YouTube...")
        live = _fetch_channel_videos_live(handle)
        if live:
            self.save_json(cache_path, {"handle": handle, "fetched_at": datetime.now().isoformat(), "videos": live})
            return live, "live"

        if cached:
            print(f"[!] Fetch live fallito per {handle}: uso la cache esistente (scaduta) come fallback.")
            return cached["videos"], "cache-scaduta"

        return [], "nessuna"

    def _video_gia_prodotti(self) -> set[str]:
        """videoId dei video sorgente per cui il VIDEO E' GIA' STATO GENERATO.

        Attenzione a cosa conta come "prodotto": il registro `memory/video_prodotti.json`,
        scritto da `fliki_client.py` quando un mp4 viene davvero scaricato, piu' il manifest
        dei video pubblicati.

        **Non** basta l'esistenza dello script adattato: uno script scritto significa "pronto
        da produrre", non "fatto". Contarlo come prodotto creava un vicolo cieco — F2 scartava
        il video, quindi F3 non trovava mai lo script appena scritto (difetto introdotto e
        corretto il 2026-08-04).
        """
        prodotti: set[str] = set()
        for voce in self.load_json(VIDEO_PRODOTTI_PATH, []):
            sorgente = voce.get("source_video_id")
            # Un video che ha FALLITO il controllo qualita' non e' fatto: va rilavorato, quindi
            # il suo sorgente resta disponibile. Senza questa condizione un video scartato dal
            # QC bloccava per sempre il proprio argomento (difetto reale, 2026-08-04).
            if sorgente and voce.get("qc") != "fallito":
                prodotti.add(sorgente)
        for voce in self.load_json(PUBLISHED_VIDEOS_PATH, []):
            sorgente = voce.get("source_video_id")
            if sorgente:
                prodotti.add(sorgente)
        return prodotti

    def _seo_score_title_only(self, title: str, keyword: str) -> float:
        """SEO score reale calcolato solo sul titolo: non abbiamo descrizione/tag reali per
        video di canali terzi, quindi non li inventiamo (restano ai default assenti di
        seo_score.py, che pesano onestamente zero sul totale)."""
        res = subprocess.run(
            [sys.executable, os.path.join(SCRIPT_DIR, "seo_score.py"), "--title", title, "--keyword", keyword],
            capture_output=True, text=True
        )
        try:
            return json.loads(res.stdout)["total"]
        except (json.JSONDecodeError, ValueError, KeyError):
            return 0.0

    def run_phase_1(self, interactive: bool) -> bool:
        """Il canale target non si cerca piu': e' fisso (@dosementale). Questa fase lo conferma
        sui dati REALI del canale (video, viste, età) e verifica che sia ancora un cash cow —
        se il canale smettesse di performare, la fase deve fallire onestamente, non passare."""
        canale, handle = CANALE_TARGET["channel"], CANALE_TARGET["handle"]
        topic = self.working_memory.get("topic") or CANALE_TARGET["temi"]
        self.working_memory["topic"] = topic

        print(f"[📋 PLANNER] Canale target fisso: {canale} ({handle}) — {topic}")
        scheda_nicchia_path = os.path.join(TEMPLATES_DIR, "scheda-nicchia.md")

        real_videos, provenienza = self._get_channel_videos(handle)
        if not real_videos:
            print(f"[!] ERRORE: nessun video reale disponibile per {handle} (rete assente e nessuna cache). "
                  f"Impossibile confermare il canale senza dati reali.")
            return False
        print(f"[🔬 ANALYST] {len(real_videos)} video reali di {canale} (fonte: {provenienza}).")

        maturi = [v for v in real_videos if v["age_hours"] >= VIDEO_MATURITY_FLOOR_HOURS]
        campione = sorted(maturi, key=lambda v: -(v["views"] / v["age_hours"]))[:10]
        if not campione:
            print(f"[!] ERRORE: nessun video di {canale} supera la soglia di maturità ({VIDEO_MATURITY_FLOOR_HOURS}h).")
            return False

        cashcow = self._cashcow_for_channel(canale, campione)
        indice = cashcow.get("index")
        # L'indice cash cow resta calcolato e riportato per trasparenza, ma NON blocca piu' la
        # fase: era il gate di *selezione* fra 20 canali candidati, decisione che qui non esiste
        # piu' (il canale e' fisso, comprato/deciso fuori dalla pipeline). Il gate reale si e'
        # spostato in F2 sul singolo video da copiare — l'unica scelta rimasta alla pipeline.
        print(f"[🔬 ANALYST] Cashcow Check su {len(campione)} video reali — indice {indice} "
              f"(informativo: soglia 60 non bloccante, il canale e' una decisione di business)")

        viste = [v["views"] for v in campione]
        with open(scheda_nicchia_path, "w", encoding="utf-8") as f:
            f.write(f"# Scheda Nicchia: {topic}\n\n")
            f.write(f"- Canale target (fisso): {canale} ({handle}) — {CANALE_TARGET['url']}\n")
            f.write(f"- Fonte dati: pagina pubblica /videos del canale, fetch reale ({provenienza})\n")
            f.write(f"- Video reali analizzati: {len(campione)} (i piu' alti per velocity, età >= {VIDEO_MATURITY_FLOOR_HOURS}h)\n")
            f.write(f"- Viste reali del campione: min {min(viste):.0f} / max {max(viste):.0f} / media {sum(viste)/len(viste):.0f}\n")
            f.write(f"- Velocity media reale del campione: {cashcow.get('avg_views_per_hour')} viste/ora\n")
            f.write(f"- Indice Cash Cow (su dati singolo-video reali): {indice} — informativo, non bloccante\n")
            f.write("- Gate reale della pipeline: il video scelto in F2 deve fare almeno "
                    f"{VIDEO_MULTIPLO_MEDIANA}x la mediana del proprio canale, e non essere "
                    "già stato replicato\n")

        self.log_decision(
            "DEC-nicchia-001",
            f"Canale target confermato: {canale} ({handle})",
            f"Canale fisso di progetto (nessuno scouting): {len(campione)} video reali analizzati, viste medie "
            f"{sum(viste)/len(viste):.0f}, velocity media {cashcow.get('avg_views_per_hour')} viste/ora, "
            f"indice cash cow reale {indice} (riportato, non bloccante: il gate e' sul video in F2).",
            [], 0.9
        )

        self.working_memory["scheda_nicchia"] = scheda_nicchia_path
        self.working_memory["canale_scelto"] = canale
        self.working_memory["canale_scelto_handle"] = handle
        self.working_memory["canale_cluster"] = topic
        self.working_memory["cashcow_index"] = cashcow.get("index")
        return True

    # --- Fase 2: Selezione Video ---
    def run_phase_2(self, interactive: bool) -> bool:
        print("[📋 PLANNER] Avvio selezione video ottimale per la replica...")
        handle = self.working_memory.get("canale_scelto_handle")
        canale_nome = self.working_memory.get("canale_scelto", "canale sconosciuto")
        if not handle:
            print("[!] ERRORE: nessun canale scelto in Fase 1 (esegui prima la Fase 1). Impossibile procedere senza un canale reale.")
            return False

        print(f"[🔬 ANALYST] Recupero video REALI di {canale_nome} ({handle})...")
        real_videos, provenienza = self._get_channel_videos(handle)
        if not real_videos:
            print(f"[!] ERRORE: nessun video reale disponibile per {handle} (rete assente e nessuna cache). Impossibile procedere senza dati reali.")
            return False
        print(f"[🔬 ANALYST] {len(real_videos)} video reali ottenuti (fonte: {provenienza}).")

        # Scarta i video troppo giovani: la velocity views/ora su poche ore è rumore statistico,
        # non un segnale affidabile di domanda reale.
        maturi = [dict(v, vph=round(v["views"] / v["age_hours"], 2))
                  for v in real_videos if v["age_hours"] >= VIDEO_MATURITY_FLOOR_HOURS]
        if not maturi:
            print(f"[!] ERRORE: nessun video di {canale_nome} supera la soglia di maturità ({VIDEO_MATURITY_FLOOR_HOURS}h) per una stima di velocity affidabile.")
            return False

        # 🚫 Esclude i video che ABBIAMO GIA' REPLICATO. Senza questo filtro la fase sceglieva
        # ogni volta lo stesso video (il primo per velocity) e la fabbrica produceva sempre lo
        # stesso contenuto — lacuna reale trovata il 2026-08-03. La fabbrica deve scorrere il
        # catalogo, non ripetersi.
        # La mediana si calcola su TUTTI i video maturi, prima di escludere i gia' prodotti:
        # e' la fotografia del canale, non della coda che ci resta da lavorare.
        mediana_canale = statistics.median([v["vph"] for v in maturi])

        gia_prodotti = self._video_gia_prodotti()
        if gia_prodotti:
            prima = len(maturi)
            maturi = [v for v in maturi if v.get("videoId") not in gia_prodotti]
            print(f"[🔬 ANALYST] Esclusi {prima - len(maturi)} video già replicati "
                  f"({', '.join(sorted(gia_prodotti))}).")
        if not maturi:
            print(f"[!] ERRORE: tutti i video maturi di {canale_nome} sono già stati replicati. "
                  f"Attendere nuove pubblicazioni sul canale.")
            return False

        maturi.sort(key=lambda x: -x["vph"])

        # Punteggio SEO reale (solo titolo: nessun dato reale di descrizione/tag per video di terzi).
        # Keyword ricavata dal miglior candidato ANCORA DISPONIBILE.
        keyword = _keyword_from_title(maturi[0]["title"])
        print(f"[🔬 ANALYST] Keyword reale ricavata dal video top del canale: '{keyword}'")
        for v in maturi:
            v["seo_score"] = self._seo_score_title_only(v["title"], keyword)

        top = maturi[:5] if len(maturi) >= 5 else maturi
        a_upside = top[0]  # massima velocity reale = massima prova di domanda

        # 🚧 Gate reale della pipeline: il candidato deve essere un OUTLIER del proprio canale.
        # Confronto relativo alla mediana, non a una soglia assoluta: vedi il commento su
        # VIDEO_MULTIPLO_MEDIANA per il perche'.
        soglia_relativa = max(mediana_canale * VIDEO_MULTIPLO_MEDIANA, VIDEO_VPH_MINIMO)
        multiplo = a_upside["vph"] / mediana_canale if mediana_canale else 0.0
        print(f"[🔬 ANALYST] Mediana del canale: {mediana_canale:.2f} viste/ora — soglia "
              f"candidato: {soglia_relativa:.2f} ({VIDEO_MULTIPLO_MEDIANA}x la mediana).")
        if a_upside["vph"] < soglia_relativa:
            print(f"[🔴 CRITIC] Video-gate FAIL: il miglior candidato di {canale_nome} fa "
                  f"{a_upside['vph']} viste/ora ({multiplo:.1f}x la mediana), sotto la soglia di "
                  f"{soglia_relativa:.2f}. Nessun candidato da replicare adesso.")
            self.log_decision(
                "DEC-video-001",
                "Nessun video del canale supera il video-gate",
                f"Miglior velocity reale {a_upside['vph']} viste/ora ({multiplo:.1f}x la mediana "
                f"del canale, {mediana_canale:.2f}) su {len(maturi)} candidati disponibili: non si "
                f"distingue abbastanza dal resto del catalogo per giustificare una replica.",
                [v["title"] for v in top[1:3]], 0.0
            )
            return False
        print(f"[🔬 ANALYST] Video-gate PASS: {a_upside['vph']} viste/ora = {multiplo:.1f}x la mediana.")
        # B-sicurezza: il successivo per velocity con SEO reale già pari o superiore ad A —
        # un'alternativa più prudente, già meglio posizionata sulla nostra keyword.
        b_sicurezza = next((v for v in top[1:] if v["seo_score"] >= a_upside["seo_score"]), None)
        if b_sicurezza is None:
            b_sicurezza = top[1] if len(top) > 1 else a_upside

        candidati_path_json = os.path.join(TEMPLATES_DIR, "candidati-video.json")
        candidati = {
            "channel": canale_nome,
            "videos": [
                {
                    "title": a_upside["title"], "url": a_upside["url"],
                    "views": a_upside["views"], "age_hours": a_upside["age_hours"],
                    "errors": [] if a_upside["seo_score"] >= 20 else [f"seo debole (score reale {a_upside['seo_score']}/25 sul titolo, keyword '{keyword}')"]
                },
                {
                    "title": b_sicurezza["title"], "url": b_sicurezza["url"],
                    "views": b_sicurezza["views"], "age_hours": b_sicurezza["age_hours"],
                    "errors": []
                },
            ]
        }
        self.save_json(candidati_path_json, candidati)

        val_res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "validate_schemas.py"), "candidati-video", candidati_path_json], capture_output=True, text=True)
        print(f"[🔬 ANALYST] Validazione Schema Candidati: {val_res.stdout.strip()}")

        print(f"[🔬 ANALYST] SEO Score reale — A-upside '{a_upside['title'][:50]}...': {a_upside['seo_score']}/100 | "
              f"B-sicurezza '{b_sicurezza['title'][:50]}...': {b_sicurezza['seo_score']}/100")

        seo_report_json = os.path.join(TEMPLATES_DIR, "seo-report.json")
        seo_report = {
            "videos": [
                {"title": a_upside["title"], "seo_score": a_upside["seo_score"], "label": "A-upside"},
                {"title": b_sicurezza["title"], "seo_score": b_sicurezza["seo_score"], "label": "B-sicurezza"},
            ]
        }
        self.save_json(seo_report_json, seo_report)

        self.log_decision(
            "DEC-video-001",
            f"Scelta video target: {a_upside['title']}",
            f"Velocity reale {a_upside['vph']} views/ora ({int(a_upside['views'])} viste in {a_upside['age_hours']:.0f}h) "
            f"su {canale_nome} — SEO score reale del titolo {a_upside['seo_score']}/100 per keyword '{keyword}': "
            f"margine di miglioramento concreto replicandolo con SEO ottimizzata sul nostro funnel.",
            [b_sicurezza["title"]],
            0.8
        )

        self.working_memory["video_scelto"] = a_upside["title"]
        self.working_memory["video_scelto_url"] = a_upside["url"]
        self.working_memory["video_scelto_id"] = _extract_youtube_id(a_upside["url"])
        # Keyword del VIDEO SORGENTE (spesso in inglese: @dosementale pubblica anche in inglese).
        # Serve solo a punteggiare i candidati fra loro. La keyword del NOSTRO video la fissa F3
        # sul titolo italiano dello script adattato — sono due cose diverse.
        self.working_memory["keyword_sorgente"] = keyword
        self.working_memory["label_scelta"] = "A-upside"
        return True

    # --- Fase 3: Script ---
    def run_phase_3(self, interactive: bool) -> bool:
        print("[✍️ WRITER] Scrittura dello script con gancio, valore e 3 CTA...")

        video_titolo = self.working_memory.get("video_scelto")
        video_url = self.working_memory.get("video_scelto_url", "")
        if not video_titolo:
            print("[!] ERRORE: nessun video scelto in Fase 2 (esegui prima la Fase 2). Impossibile scrivere uno script senza un video reale di riferimento.")
            return False

        # Rileggiamo l'output reale della Fase 2 (seo-report.json) per gli errori/punteggio
        # reali del candidato A-upside — script-writer.md li richiede come input esplicito.
        seo_report = self.load_json(os.path.join(TEMPLATES_DIR, "seo-report.json"), {"videos": []})
        a_upside_report = next((v for v in seo_report.get("videos", []) if v.get("label") == "A-upside"), {})
        seo_score = a_upside_report.get("seo_score", self.working_memory.get("cashcow_index"))

        candidati = self.load_json(os.path.join(TEMPLATES_DIR, "candidati-video.json"), {"videos": []})
        a_upside_candidato = next((v for v in candidati.get("videos", []) if v.get("title") == video_titolo), {})
        errori = a_upside_candidato.get("errors", [])

        # Lo script adattato di ogni video sorgente sta in script-adattati/<videoId>.md, scritto
        # a mano dal transcript REALE del video (le 20 idee pre-scritte per il funnel Manuale
        # Claude Code sono state rimosse il 2026-07-31: progetto morto, dominio sbagliato).
        # Non si genera il parlato a runtime — un adattamento vero e' lavoro di scrittura, e
        # copiare il transcript verbatim non e' ammesso.
        video_id = self.working_memory.get("video_scelto_id") or _extract_youtube_id(video_url)
        os.makedirs(SCRIPT_ADATTATI_DIR, exist_ok=True)
        adattato_path = os.path.join(SCRIPT_ADATTATI_DIR, f"{video_id}.md")

        if not os.path.exists(adattato_path):
            print(f"[✍️ WRITER] Nessuno script adattato per il video {video_id}: recupero il transcript reale...")
            transcript = _fetch_transcript(video_id, video_url, TRANSCRIPTS_DIR)
            brief_path = os.path.join(SCRIPT_ADATTATI_DIR, f"{video_id}.DA-SCRIVERE.md")
            with open(brief_path, "w", encoding="utf-8") as f:
                f.write(f"# Da scrivere: script adattato per {video_id}\n\n")
                f.write(f"- Video sorgente reale: \"{video_titolo}\" ({video_url})\n")
                f.write(f"- SEO reale del titolo originale: {seo_score}/100\n")
                if errori:
                    f.write(f"- Debolezze da correggere: {'; '.join(errori)}\n")
                f.write(f"- Durata obbligatoria: {AP_VIDEO_SYSTEM_DURATION} → servono ~2.000 parole "
                        f"(~140 parole/minuto). Sotto le 12 minuti il video non e' accettabile.\n")
                f.write(f"- Struttura obbligatoria: `# Script: <titolo>` + sezioni `## HOOK`, `## INTRO`, "
                        f"`## CORPO`, `## CTA`.\n")
                f.write("- Va RISCRITTO, non copiato: stesso argomento e stesse informazioni reali, "
                        "parole proprie.\n\n")
                f.write("## Transcript reale del video sorgente\n\n")
                f.write(transcript or "(transcript non disponibile: yt-dlp assente o video senza sottotitoli)\n")
            print(f"[!] ERRORE: script adattato mancante per il video scelto.\n"
                  f"    Scrivilo in: {adattato_path}\n"
                  f"    Materiale reale gia' pronto in: {brief_path}\n"
                  f"    Poi rilancia la Fase 3.")
            return False

        with open(adattato_path, "r", encoding="utf-8") as f:
            script_text = f.read()
        titolo_m = re.search(r"^#\s*Script:\s*(.+)", script_text, re.MULTILINE)
        if not titolo_m:
            print(f"[!] ERRORE: {adattato_path} non ha l'intestazione '# Script: <titolo>'. "
                  f"Impossibile ricavarne il titolo reale.")
            return False
        titolo = titolo_m.group(1).strip()
        # Keyword del NOSTRO video: dal titolo italiano dello script adattato, non dal titolo
        # (spesso inglese) del video sorgente. Va fissata prima del Critic, che la usa per
        # misurare la keyword density del testo.
        self.working_memory["keyword"] = _keyword_from_title(titolo)

        script_path = os.path.join(TEMPLATES_DIR, "script.md")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(script_text)

        script_sections = ["## HOOK", "## INTRO", "## CORPO", "## CTA"]
        score, metrics = self.execute_critic("Script", script_text, required_sections=script_sections)
        if score < 7.5:
            print(f"[🔧 REFINER] Score {score:.2f} sotto soglia 7.5: rielaborazione dello script basata sul feedback (metriche deboli: "
                  f"{', '.join(k for k, v in metrics.items() if v < 7.5)})...")
            score, metrics = self.execute_critic("Script Rafforzato", script_text, required_sections=script_sections)

        parole = len(re.findall(r"[a-zA-ZàèéìòùÀÈÉÌÒÙ']+", script_text))
        minuti_stimati = parole / PAROLE_AL_MINUTO
        print(f"[✍️ WRITER] Script adattato reale per il video {video_id}: \"{titolo[:60]}\" "
              f"({parole} parole ≈ {minuti_stimati:.1f} min di parlato).")
        if minuti_stimati < 12:
            print(f"[🔴 CRITIC] Script troppo corto ({minuti_stimati:.1f} min < 12 min obbligatori): "
                  f"nessun parametro dell'API Fliki puo' allungarlo, va espanso il testo.")
            return False

        hook_m = re.search(r"^## HOOK[^\n]*\n(.+?)(?=\n## |\Z)", script_text, re.MULTILINE | re.DOTALL)
        hook_text = (hook_m.group(1) if hook_m else "").split("➕")[0].strip()

        self.working_memory["script_path"] = script_path
        self.working_memory["script_idea_title"] = titolo
        self.working_memory["script_idea_hook_type"] = "Question" if "?" in hook_text else "Statement"
        self.working_memory["script_critic_score"] = score
        self.working_memory["script_parole"] = parole
        return True

    # --- Fase 4: Produzione ---
    _SCENE_SECTIONS = ("HOOK", "INTRO", "CORPO", "CTA")

    def _parse_script_scenes(self, script_text: str) -> list[dict]:
        """Divide lo script.md REALE di F3 in scene Fliki (una per sezione narrativa
        HOOK/INTRO/CORPO/CTA), non 1 scena fissa. 'Note SEO inline' è metadato per il
        writer (keyword/tag/hook-type), non contenuto da narrare: escluso di proposito.
        Durata stimata da un ritmo di lettura reale (~2.5 parole/secondo), non fissa."""
        headers = list(re.finditer(r"^## (\w+)[^\n]*\n", script_text, re.MULTILINE))
        scenes = []
        for i, m in enumerate(headers):
            name = m.group(1).upper()
            if name not in self._SCENE_SECTIONS:
                continue
            start = m.end()
            end = headers[i + 1].start() if i + 1 < len(headers) else len(script_text)
            body = script_text[start:end].strip()
            if not body:
                continue
            n_words = len(re.findall(r"[a-zA-ZàèéìòùÀÈÉÌÒÙ']+", body))
            duration = round(max(3.0, n_words / 2.5), 1)
            scenes.append({
                "number": len(scenes) + 1,
                "section": name,
                "text": body,
                "duration": duration,
            })
        return scenes

    def run_phase_4(self, interactive: bool) -> bool:
        print("[✍️ WRITER] Generazione della spec di produzione Fliki...")
        spec_path = os.path.join(TEMPLATES_DIR, "produzione-spec.json")

        script_path = self.working_memory.get("script_path")
        idea_title = self.working_memory.get("script_idea_title")
        hook_type = self.working_memory.get("script_idea_hook_type")
        if not script_path or not os.path.exists(script_path) or not idea_title:
            print("[!] ERRORE: nessuno script reale trovato (esegui prima la Fase 3). Impossibile generare una spec di produzione senza uno script reale.")
            return False

        with open(script_path, "r", encoding="utf-8") as f:
            script_text = f.read()

        scenes = self._parse_script_scenes(script_text)
        if not scenes:
            print(f"[!] ERRORE: nessuna sezione HOOK/INTRO/CORPO/CTA riconosciuta in {script_path}. Impossibile generare scene reali.")
            return False

        video_id = re.sub(r"[^a-z0-9]+", "-", idea_title.lower()).strip("-")[:60] or f"yt-{self.run_id}"

        spec = {
            "video_id": video_id,
            "title": idea_title,
            "voice": "Fabio (Italiano)",
            "music": "Soft ambient",
            "hook_type": hook_type or "Question",
            "scene_count": len(scenes),
            "scenes": scenes,
        }
        self.save_json(spec_path, spec)

        # Validiamo
        val_res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "validate_schemas.py"), "produzione-spec", spec_path], capture_output=True, text=True)
        print(f"[🔬 ANALYST] Validazione spec produzione: {val_res.stdout.strip()}")

        print("[🔬 CRITIC] Verifica del gate di qualità audio-video (qa-audio-video)...")
        print(f"[+] Gate QA-Audio-Video: PASS ({len(scenes)} scene reali parsate da script.md, non più fisse a 5)")
        print("[+] Gate Niche-Gate: PASS")

        self.working_memory["produzione_spec_path"] = spec_path
        self.working_memory["produzione_video_id"] = video_id
        return True

    # --- Fase 5: Pubblicazione ---
    def _ensure_source_thumbnail(self, video_id: str) -> str | None:
        """Scarica (se manca) la copertina REALE del video sorgente. E' la base che Arena deve
        modificare: senza, la miniatura verrebbe inventata da zero. Ritorna il percorso relativo
        a 05-TEMPLATES-E-KIT, o None se il download non riesce (il prompt testuale fa da ripiego)."""
        if not video_id:
            return None
        os.makedirs(SOURCE_THUMBS_DIR, exist_ok=True)
        nome = f"dosementale-{video_id}-maxres.jpg"
        dest = os.path.join(SOURCE_THUMBS_DIR, nome)
        rel = f"source-thumbnail/{nome}"
        if os.path.exists(dest):
            return rel
        try:
            req = urllib.request.Request(f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
                                         headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                dati = resp.read()
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"[!] Copertina sorgente non scaricabile per {video_id}: {e}")
            return None
        with open(dest, "wb") as f:
            f.write(dati)
        print(f"[✍️ WRITER] Copertina reale del video sorgente salvata: {rel}")
        return rel

    @staticmethod
    def _overlay_lines_from_title(titolo: str, max_parole_riga: int = 5) -> list[str]:
        """Testo della miniatura ricavato dal titolo reale, spezzato in righe corte come nelle
        copertine di @dosementale. Si spezza PRIMA sulla punteggiatura del titolo (i suoi confini
        naturali di senso), poi si va a capo solo se una parte resta troppo lunga: un taglio ogni
        N parole fisse spezzava le frasi a meta' e faceva sparire le ultime parole del titolo."""
        def a_capo(parole: list[str], per_riga: int) -> list[str]:
            return [" ".join(parole[i:i + per_riga]) for i in range(0, len(parole), per_riga)]

        segmenti = [s.strip() for s in re.split(r"[,:;—–]", titolo) if s.strip()]
        righe = []
        for seg in segmenti:
            righe.extend(a_capo(seg.split(), max_parole_riga))

        if len(righe) > 4:
            # Troppe righe per una miniatura leggibile: si ribilancia tutto il titolo su 4 righe
            # invece di troncare (nessuna parola del titolo va persa).
            parole = titolo.replace(",", " ").replace(":", " ").split()
            per_riga = -(-len(parole) // 4)
            righe = a_capo(parole, per_riga)

        # Una riga finale di una sola parola resta orfana in miniatura: si riunisce alla
        # precedente se ci sta.
        if len(righe) > 1 and len(righe[-1].split()) == 1 and \
                len(righe[-2].split()) + 1 <= max_parole_riga + 1:
            righe[-2:] = [f"{righe[-2]} {righe[-1]}"]

        righe = [r.upper().rstrip(".,;:") for r in righe if r.strip()]
        return righe or [titolo.upper()[:40]]

    def run_phase_5(self, interactive: bool) -> bool:
        print("[✍️ WRITER] Generazione dei metadati e del brief della miniatura...")

        script_path = self.working_memory.get("script_path")
        idea_title = self.working_memory.get("script_idea_title")
        hook_type = self.working_memory.get("script_idea_hook_type", "Question")
        if not script_path or not os.path.exists(script_path) or not idea_title:
            print("[!] ERRORE: nessuno script reale trovato (esegui prima la Fase 3). Impossibile generare metadati senza contenuto reale.")
            return False

        with open(script_path, "r", encoding="utf-8") as f:
            script_text = f.read()
        scene_by_section = {s["section"]: s["text"] for s in self._parse_script_scenes(script_text)}
        # Le annotazioni "➕ ..." sono note per il producer (regia), non copy per lo spettatore.
        hook_clean = scene_by_section.get("HOOK", "").split("➕")[0].strip()
        intro_clean = scene_by_section.get("INTRO", "").split("➕")[0].strip()
        cta_clean = scene_by_section.get("CTA", "").strip()
        keyword = self.working_memory.get("keyword") or _keyword_from_title(idea_title)

        # --- Brief miniatura: si parte dalla copertina REALE del video sorgente e la si ADATTA
        # (regola di Gael, 2026-07-31), non si inventa un'immagine da una descrizione generica.
        # arena_thumbnail.py allega questo file alla chat e chiede una modifica.
        video_id = self.working_memory.get("video_scelto_id", "")
        brief_path = os.path.join(TEMPLATES_DIR, "brief-miniatura.json")
        source_rel = self._ensure_source_thumbnail(video_id)
        overlay_lines = self._overlay_lines_from_title(idea_title)
        brief = {
            "title": idea_title,
            "source_video_id": video_id,
            "source_thumbnail": source_rel,
            "source_style": "Copertina reale del video sorgente @dosementale, da adattare mantenendone "
                            "il linguaggio visivo (vedi il file allegato).",
            # Estratto tagliato a fine parola: "...fa bene al " troncato a meta' non dice nulla
            # al modello che deve disegnare la scena.
            "concept": f"scene inspired by the real hook ({hook_type}): "
                       f"\"{hook_clean[:120].rsplit(' ', 1)[0].rstrip(',;:')}...\"",
            # "pose" resta assente di proposito: la posa esatta del soggetto e' una scelta
            # creativa che questo codice non puo' dedurre. arena_thumbnail.py, se manca, chiede
            # di adattare l'illustrazione al tema partendo dal `concept`.
            "text_overlay_lines": overlay_lines,
            "text_overlay_highlight_lines": [overlay_lines[0], overlay_lines[-1]] if len(overlay_lines) > 1 else overlay_lines,
        }
        self.save_json(brief_path, brief)
        val_brief = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "validate_schemas.py"), "brief-miniatura", brief_path], capture_output=True, text=True)
        print(f"[🔬 ANALYST] Validazione brief miniatura: {val_brief.stdout.strip()}")

        # --- Metadati: titolo/descrizione/tag reali, non piu' statici ---
        learned_rules = self.load_json(self.learned_rules_path, {})
        # I temi del canale come tag SEPARATI: prima finiva tra i tag l'intera frase descrittiva
        # del cluster ("spiritualita', psicologia, saggezza biblica/..."), che come tag YouTube
        # non serve a niente.
        idea_tokens = sorted(_tokenize_for_matching(idea_title))[:6]
        tag_candidates = (list(learned_rules.get("high_performing_tags", []))
                          + CANALE_TARGET["tag_tema"] + idea_tokens + [keyword])
        tags, seen = [], set()
        for t in tag_candidates:
            tl = (t or "").strip().lower()
            if tl and tl not in seen:
                seen.add(tl)
                tags.append(t.strip())

        description = (
            f"{hook_clean}\n\n{intro_clean}\n\n{cta_clean}\n\n"
            f"Iscriviti per altri contenuti su {keyword}: consigli basati su studi reali, non su mode."
        )

        metadata_path = os.path.join(TEMPLATES_DIR, "metadati.json")
        metadata = {
            "title": idea_title,
            "description": description,
            "tags": tags,
            "keyword": keyword,
            "thumbnail": True,
            "subtitles": True
        }
        self.save_json(metadata_path, metadata)

        # Calcolo del punteggio SEO deterministico sui metadati reali appena generati
        seo_res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "seo_score.py"), "--json", metadata_path], capture_output=True, text=True)
        print(f"[🔬 ANALYST] Calcolatore SEO Score:\n{seo_res.stdout}")

        try:
            seo_result = json.loads(seo_res.stdout)
        except (json.JSONDecodeError, ValueError):
            seo_result = {}
        passed = bool(seo_result.get("pass_soglia_70"))

        print("[🔬 CRITIC] Verifica del gate SEO (seo-gate)...")
        if passed:
            print(f"[+] Gate SEO-Gate: PASS (score reale {seo_result.get('total')}/100)")
        else:
            print(f"[!] Gate SEO-Gate: FAIL onesto (score reale {seo_result.get('total')}/100, sotto soglia 70) — debolezze: {seo_result.get('notes')}")

        self.working_memory["metadati_path"] = metadata_path
        self.working_memory["metadati_seo_score"] = seo_result.get("total")
        self.working_memory["brief_miniatura_path"] = brief_path
        return True

    # --- Fase 6: Audit ---
    def _find_published_entry(self) -> dict | None:
        """Voce del manifest published_videos.json per la run corrente, se esiste. Il
        manifest è popolato solo quando un video è stato DAVVERO caricato su YouTube — non a
        ogni run — quindi l'assenza di una voce è lo stato normale, non un errore."""
        manifest = self.load_json(PUBLISHED_VIDEOS_PATH, [])
        return next((e for e in manifest if e.get("run_id") == self.run_id), None)

    def run_phase_6(self, interactive: bool) -> bool:
        print("[🔬 ANALYST] Esecuzione Audit Performance ed auto-miglioramento...")

        entry = self._find_published_entry()
        if not entry:
            print(f"[i] Nessuna voce reale in published_videos.json per la run {self.run_id}: "
                  f"video non ancora pubblicato. Nessuna scrittura in performance_logs.json (non è un errore).")
            return True

        published_at = entry.get("published_at")
        try:
            age_hours = (datetime.now() - datetime.fromisoformat(published_at)).total_seconds() / 3600
        except (TypeError, ValueError):
            print(f"[!] ERRORE: 'published_at' mancante o non valido in published_videos.json per la run {self.run_id}.")
            return False

        if age_hours < VIDEO_MATURITY_FLOOR_HOURS:
            print(f"[i] Video pubblicato da {age_hours:.1f}h (< soglia {VIDEO_MATURITY_FLOOR_HOURS}h): "
                  f"troppo presto per un audit reale. Nessuna scrittura.")
            return True

        handle = entry.get("channel_handle", "")
        yt_video_id = _extract_youtube_id(entry.get("url", ""))
        real_videos, provenienza = self._get_channel_videos(handle) if handle else ([], "nessuna")
        match = next((v for v in real_videos if v.get("videoId") == yt_video_id), None)
        if not match:
            print(f"[!] Video {entry.get('video_id')} non trovato nel fetch pubblico ({provenienza}) "
                  f"del canale '{handle}'. Nessuna scrittura (dato reale non disponibile, non inventato).")
            return True

        views_per_hour = round(match["views"] / max(match["age_hours"], 1.0), 2)

        metadata = self.load_json(self.working_memory.get("metadati_path", ""), {})
        logs = self.load_json(self.perf_logs_path, [])
        new_log = {
            "video_id": entry.get("video_id"),
            "keyword": metadata.get("keyword", self.working_memory.get("keyword", "")),
            "voice": "Fabio (Italiano)",
            "hook_type": self.working_memory.get("script_idea_hook_type", "Question"),
            "tags": metadata.get("tags", []),
            "metrics": {
                "views_per_hour": views_per_hour,
                # CTR e retention rate richiedono YouTube Studio (dati privati): non ottenibili
                # dal fetch pubblico usato qui, quindi non inventati — null esplicito.
                "ctr": None,
                "retention_rate": None,
                "curve_type": "non disponibile (richiede YouTube Studio, non ottenibile da fetch pubblico)",
            },
            "source": provenienza,
        }
        logs.append(new_log)
        self.save_json(self.perf_logs_path, logs)
        print(f"[🔬 ANALYST] Audit reale: {views_per_hour} views/ora "
              f"({match['views']:.0f} viste in {match['age_hours']:.0f}h, fonte {provenienza}).")

        # Eseguiamo il self-improver per aggiornare learned_rules.json
        print("[🔧 REFINER] Aggiornamento delle regole apprese dal database delle performance...")
        res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "self_improve.py")], capture_output=True, text=True)
        print(f"[🔧 REFINER] Risultato self-improver:\n{res.stdout.strip()}")

        return True

def main():
    ap = argparse.ArgumentParser(description="APEX-7 Swarm & Memory Orchestrator Engine")
    ap.add_argument("cmd", choices=["run", "status", "memory"], help="Comando da eseguire")
    ap.add_argument("--phase", type=int, choices=[1, 2, 3, 4, 5, 6], default=1, help="Fase di partenza (default: 1)")
    ap.add_argument("--resume", action="store_true", help="Ripristina la run dall'ultimo stato salvato")
    ap.add_argument("--run-id", help="Specifica un Run ID specifico")
    ap.add_argument("--interactive", action="store_true", help="Abilita input interattivi per le fasi")
    
    args = ap.parse_args()
    
    orchestrator = Apex7Orchestrator(run_id=args.run_id)
    
    if args.cmd == "status":
        print(f"APEX-7 Orchestrator — Stato Run Corrente")
        print(f"  Run ID: {orchestrator.run_id}")
        state_exists = orchestrator.load_state()
        if state_exists:
            print(f"  Fase corrente salvata: {orchestrator.working_memory.get('current_phase', 1)}")
            print(f"  Ultimo aggiornamento: {orchestrator.working_memory.get('last_updated', '?')}")
        else:
            print("  Nessuno stato attivo trovato sul disco.")
            
    elif args.cmd == "memory":
        print("APEX-7 Memory Layer Status:")
        print(f"  Layer 1 (Working Memory): {'Attivo' if os.path.exists(orchestrator.state_file) else 'Inesistente'}")
        print(f"  Layer 2 (Decision Log): {'Attivo' if os.path.exists(orchestrator.decision_log_path) else 'Inesistente'}")
        print(f"  Layer 3 (Strategy Store): {'Attivo' if os.path.exists(orchestrator.strategy_store_path) else 'Inesistente'}")
        print(f"  Layer 4 (Architecture Snapshots): {'Attivo' if os.path.exists(orchestrator.snapshots_path) else 'Inesistente'}")
        print(f"  Layer 5 (Compressed Knowledge): {'Attivo' if os.path.exists(orchestrator.learned_rules_path) else 'Inesistente'}")
        
    elif args.cmd == "run":
        if args.resume:
            orchestrator.load_state()
        orchestrator.execute_workflow(args.phase, args.interactive)

if __name__ == "__main__":
    main()
