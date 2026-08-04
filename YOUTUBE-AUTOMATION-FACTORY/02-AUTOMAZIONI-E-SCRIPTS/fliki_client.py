#!/usr/bin/env python3
"""
Client reale per l'API Fliki Enterprise (https://developer.fliki.ai/).
Legge la spec reale di produzione-spec.json (scritta da run_phase_4, TASK-YT-002) e
lo script reale di F3, genera il video via API (non Playwright: qui esiste una vera
API con FLIKI_API_KEY), fa polling dello stato e scarica il file finale.

Endpoint reali usati (documentazione ufficiale, verificata 2026-07-29):
  GET  https://api.fliki.ai/v1/voices?languageId=..&dialectId=..
  POST https://api.fliki.ai/v1/generate/video
  GET  https://api.fliki.ai/v1/generate/status?fileId=...
"""
import os
import re
import sys
import json
import time
import argparse
import urllib.request
import urllib.error

# Forza stdout/stderr in utf-8 su Windows: senza, qualunque carattere non-ASCII nei print
# (es. "—") fa crashare con UnicodeEncodeError su cp1252. line_buffering=True e' OBBLIGATORIO:
# senza, quando l'output e' rediretto su file (non un terminale) lo stream usa il buffering a
# blocchi e i print restano invisibili per decine di minuti (bug reale trovato il 2026-07-30).
# reconfigure() (non un nuovo io.TextIOWrapper!) e' OBBLIGATORIO: questo script importa
# apex7_orchestrator, che fa lo stesso wrapping — con due TextIOWrapper distinti sullo stesso
# buffer, il garbage collector del primo chiude il buffer sottostante e il secondo esplode con
# "I/O operation on closed file" al primo print (bug reale trovato il 2026-07-30, appena dopo
# il fix precedente). reconfigure() modifica lo stream esistente, e' idempotente e sicuro anche
# se chiamato piu' volte da moduli diversi nello stesso processo.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

API_BASE = "https://api.fliki.ai/v1"

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")
VIDEOS_DIR = os.path.join(FACTORY_DIR, "06-DASHBOARD-E-METRICHE", "video-generati")


def _api_key() -> str:
    key = os.environ.get("FLIKI_API_KEY")
    if not key:
        env_path = os.path.join(FACTORY_DIR, ".env")
        if os.path.exists(env_path):
            for line in open(env_path, encoding="utf-8"):
                if line.strip().startswith("FLIKI_API_KEY="):
                    key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not key:
        raise SystemExit("[!] FLIKI_API_KEY non trovata (ne' in ambiente ne' in .env). "
                          "Impossibile chiamare l'API reale senza inventare nulla.")
    return key


def _request(method: str, path: str, key: str, body: dict | None = None, retries: int = 3) -> dict:
    url = f"{API_BASE}{path}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req_headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    last_err = None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, method=method, headers=req_headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="ignore")
            raise SystemExit(f"[!] Errore API reale {method} {path}: HTTP {e.code} — {detail}")
        except (TimeoutError, urllib.error.URLError) as e:
            # Timeout di rete transitorio (non un errore dell'API reale): ritenta invece di
            # far crashare tutto lo script dopo 15+ minuti di generazione gia' completata.
            last_err = e
            print(f"[!] Timeout di rete su {method} {path} (tentativo {attempt+1}/{retries}): {e}")
            time.sleep(5)
    raise SystemExit(f"[!] Rete non raggiungibile dopo {retries} tentativi su {method} {path}: {last_err}")


def _items(res) -> list:
    items = res.get("data", res) if isinstance(res, dict) else res
    if isinstance(items, dict):
        # alcuni endpoint annidano la lista sotto una chiave (es. {"languages": [...]})
        for v in items.values():
            if isinstance(v, list):
                return v
        return []
    return items


def find_italian_voice(key: str, prefer_gender: str = "male") -> str:
    # "it"/"it-IT" sono slug, non i veri _id richiesti dall'API: vanno risolti prima.
    languages = _items(_request("GET", "/languages", key))
    lang = next((l for l in languages if l.get("slug") == "it" or l.get("name") == "Italian"), None)
    if not lang:
        raise SystemExit(f"[!] Lingua italiana non trovata in /languages (risposta reale: {languages[:5]}...)")

    dialects = _items(_request("GET", "/dialects", key))
    dialect = next((d for d in dialects if str(d.get("slug", "")).startswith("it")), None)
    if not dialect:
        raise SystemExit(f"[!] Dialetto italiano non trovato in /dialects (risposta reale: {dialects[:5]}...)")

    print(f"[+] Lingua reale: {lang.get('name')} ({lang['_id']}) — Dialetto reale: {dialect.get('name')} ({dialect['_id']})")
    voices = _items(_request("GET", f"/voices?languageId={lang['_id']}&dialectId={dialect['_id']}", key))
    # L'API reale ritorna "MALE"/"FEMALE" in maiuscolo (verificato: un confronto case-sensitive
    # con "male" non trovava mai nulla e faceva sempre fallback sulla prima voce qualsiasi).
    candidates = [v for v in voices if str(v.get("gender", "")).lower() == prefer_gender.lower()] or voices
    if not candidates:
        raise SystemExit("[!] Nessuna voce italiana trovata dall'API reale.")
    chosen = candidates[0]
    print(f"[+] Voce scelta: {chosen.get('name')} ({chosen.get('_id')}, gender={chosen.get('gender')})")
    return chosen["_id"]


MAX_WORDS_PER_SCENE = 130


def _split_into_bounded_chunks(text: str, max_words: int) -> list[str]:
    """Divide un blocco di testo in pezzi di al massimo `max_words` parole, spezzando SEMPRE
    a fine frase (mai a meta'), raggruppando frasi consecutive finche' il limite non e' superato.
    Trovato il 2026-07-30: un singolo blocco da 594 parole (~4+ min di narrazione in UNA sola
    scena/clip stock) ha fatto restare un job Fliki bloccato in coda per oltre un'ora senza mai
    passare a 'processing' ne' dare un errore esplicito — nessuna scena deve superare questo
    limite."""
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZÀÈÉÌÒÙ])", text.strip())
    chunks, current, current_words = [], [], 0
    for sentence in sentences:
        n = len(sentence.split())
        if current and current_words + n > max_words:
            chunks.append(" ".join(current))
            current, current_words = [], 0
        current.append(sentence)
        current_words += n
    if current:
        chunks.append(" ".join(current))
    return chunks


def build_script_content() -> str:
    """Testo reale dallo script.md di F3, riusando Apex7Orchestrator._parse_script_scenes
    (stesse 4 sezioni HOOK/INTRO/CORPO/CTA), con 'sceneBreakdown: lineBreak' cosi' Fliki
    rispetta i confini di scena reali invece di indovinarli. Il merge Git che rendeva
    apex7_orchestrator.py non importabile e' stato risolto (verificato 2026-07-30): si
    reimporta il modulo reale invece di una copia standalone.

    Ogni sezione viene inoltre ri-divisa in blocchi di massimo MAX_WORDS_PER_SCENE parole
    (mai a meta' frase) — vedi _split_into_bounded_chunks per il perche'."""
    sys.path.insert(0, SCRIPT_DIR)
    import apex7_orchestrator as mod  # noqa: E402

    script_path = os.path.join(TEMPLATES_DIR, "script.md")
    with open(script_path, "r", encoding="utf-8") as f:
        script_text = f.read()
    orch = mod.Apex7Orchestrator(run_id="fliki-client")
    scenes = orch._parse_script_scenes(script_text)
    if not scenes:
        raise SystemExit("[!] Nessuna scena reale trovata in script.md.")

    all_chunks = []
    for s in scenes:
        section_text = s["text"].split("➕")[0].strip()
        all_chunks.extend(_split_into_bounded_chunks(section_text, MAX_WORDS_PER_SCENE))
    print(f"[+] Script diviso in {len(all_chunks)} scene (max {MAX_WORDS_PER_SCENE} parole ciascuna, "
          f"da {len(scenes)} sezioni originali).")
    return "\n\n".join(all_chunks)


# Modello di generazione video AI. `aiVideoClipPercentage` viene ignorato se questo campo NON
# e' impostato (documentazione ufficiale): e' il motivo per cui il video v10 aveva tutte le
# scene FERME nonostante il default del 20% — quel 20% non veniva mai applicato.
AI_VIDEO_MODEL = "runware-kling-2.5-turbo"
AI_VIDEO_CLIP_PERCENTAGE = 100   # tutte le scene come clip in movimento
IMAGE_ANIMATION_PRESET = "Mix"   # movimento anche su eventuali immagini residue


def generate_video(key: str, content: str, voice_id: str, file_name: str,
                   visuals: str = "stock", art_style: str | None = None,
                   ai_video_model: str | None = None,
                   clip_percentage: int = AI_VIDEO_CLIP_PERCENTAGE) -> str:
    payload = {
        "payload": [{
            "workflowType": "script",
            "workflowFormat": "video",
            "content": content,
            "voiceId": voice_id,
            "aspectRatio": "16:9",
            "resolution": "1080p",
            # "stock" e' il DEFAULT APPROVATO (video v8). Con --visuals ai le immagini vengono
            # generate dal testo della scena invece di essere pescate da un archivio: le clip
            # stock che Fliki sceglie da sole a volte sono fuori target anagrafico (in una
            # scena del v8 compare una ragazza giovane mentre il testo parla a over-70).
            # L'API non offre alcun controllo per-scena sullo stock (verificato sulla
            # documentazione ufficiale): o si accetta la sua scelta, o si generano le immagini.
            "visuals": visuals,
            "sceneBreakdown": "lineBreak",
            "fileName": file_name,
            "shouldExport": True,
            # ⛔ CONFIGURAZIONE APPROVATA DA GAEL — NON MODIFICARE (2026-07-31)
            # Questi tre valori sono esattamente quelli che hanno prodotto il video v8, che
            # Gael ha giudicato PERFETTO con l'istruzione "non modificare le regole e non
            # cambiare niente, d'ora in poi falli tutti così".
            #
            # Avevo proposto di cambiarli (preset piu' grande e highlightSubtitles=False, per
            # avere frasi intere invece dell'effetto karaoke parola-per-parola): proposta
            # RESPINTA. L'effetto karaoke e' voluto. Non riproporlo.
            #
            # subtitlePresetId reale ottenuto cliccando "Copy subtitle preset ID" su
            # fliki.ai/info/subtitle via Playwright (non e' nell'HTML statico ne' in nessuna
            # chiamata di rete). I 30 preset reali sono in memory/fliki_subtitle_presets.json
            # (fliki_subtitle_presets.py) — elencati per riferimento, non per cambiare questo.
            "subtitlePresetId": "builtin-legacy-bold",
            "highlightSubtitles": True,
            # `duration` e' in MINUTI, range reale 1-15 (developer.fliki.ai): 720 e' fuori
            # range e viene ignorato dall'API — la durata segue la lunghezza del testo. Resta
            # qui perche' fa parte della configurazione approvata e rimuoverlo, pur essendo
            # inerte, sarebbe un cambiamento non richiesto.
            "duration": 720,
        }]
    }
    if visuals == "ai":
        if art_style:
            payload["payload"][0]["artStyle"] = art_style
        # Senza `aiVideoModel` il campo `aiVideoClipPercentage` viene IGNORATO e le scene
        # restano immagini ferme (verificato sul video v10: Gael — "sono meglio le immagini
        # che si muovono nel video, non le immagini fisse").
        if ai_video_model:
            payload["payload"][0]["aiVideoModel"] = ai_video_model
            payload["payload"][0]["aiVideoClipPercentage"] = clip_percentage
            payload["payload"][0]["imageAnimationPreset"] = IMAGE_ANIMATION_PRESET
    res = _request("POST", "/generate/video", key, payload)
    files_created = (res.get("data") or {}).get("filesCreated") or []
    if not files_created:
        raise SystemExit(f"[!] Risposta API reale senza filesCreated: {res}")
    file_id = files_created[0]
    print(f"[+] Generazione avviata, fileId={file_id}")
    return file_id


def poll_status(key: str, file_id: str, max_wait_s: int = 1800) -> str:
    waited = 0
    while waited < max_wait_s:
        res = _request("GET", f"/generate/status?fileId={file_id}", key)
        status = res.get("status")
        progress = res.get("progress")
        print(f"[status reale] {status} (progress={progress}, {waited}s trascorsi)")
        if status == "success":
            download = res.get("download")
            if not download:
                raise SystemExit(f"[!] Status 'success' ma nessun campo 'download': {res}")
            return download
        if status in ("error", "canceled"):
            raise SystemExit(f"[!] Generazione fallita lato Fliki: {res}")
        time.sleep(10)
        waited += 10
    raise SystemExit(f"[!] Timeout dopo {max_wait_s}s in stato '{status}'.")


def download_file(url: str, out_path: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        with open(out_path, "wb") as f:
            f.write(resp.read())


VIDEO_PRODOTTI_PATH = os.path.join(FACTORY_DIR, "memory", "video_prodotti.json")


def registra_video_prodotto(out_path: str, file_name: str) -> None:
    """Annota nel registro che il video sorgente e' stato replicato.

    E' cosi' che F2 sa quali video NON riproporre: senza questo registro la fabbrica
    sceglierebbe ogni volta lo stesso video (il primo per velocity) e produrrebbe sempre lo
    stesso contenuto. Il videoId sorgente si legge dall'intestazione di script.md, dove F3 lo
    scrive insieme all'URL del riferimento.
    """
    script_path = os.path.join(TEMPLATES_DIR, "script.md")
    source_id = ""
    titolo = ""
    if os.path.exists(script_path):
        testo = open(script_path, encoding="utf-8").read()
        m = re.search(r"youtube\.com/watch\?v=([\w-]+)", testo)
        source_id = m.group(1) if m else ""
        t = re.search(r"^#\s*Script:\s*(.+)", testo, re.MULTILINE)
        titolo = t.group(1).strip() if t else ""
    if not source_id:
        print("[!] Video sorgente non ricavabile da script.md: registro non aggiornato. "
              "F2 potrebbe riproporre lo stesso video.")
        return

    os.makedirs(os.path.dirname(VIDEO_PRODOTTI_PATH), exist_ok=True)
    registro = []
    if os.path.exists(VIDEO_PRODOTTI_PATH):
        try:
            registro = json.load(open(VIDEO_PRODOTTI_PATH, encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            registro = []
    registro = [v for v in registro if v.get("source_video_id") != source_id]
    registro.append({
        "source_video_id": source_id,
        "titolo_nostro": titolo,
        "file": os.path.basename(out_path),
        "prodotto_il": time.strftime("%Y-%m-%dT%H:%M:%S"),
    })
    with open(VIDEO_PRODOTTI_PATH, "w", encoding="utf-8") as f:
        json.dump(registro, f, ensure_ascii=False, indent=2)
    print(f"[+] Registrato: il video sorgente {source_id} non verra' piu' riproposto da F2.")


def main():
    ap = argparse.ArgumentParser(description="Genera il video reale via API Fliki dalla spec F3/F4.")
    ap.add_argument("--file-name", default="dosementale-video")
    # Default "ai" dal 2026-08-03: Gael ha delegato la scelta ("scegli te") dopo il confronto
    # fra le due versioni. Le clip stock, scelte da Fliki in autonomia, finivano fuori bersaglio
    # (una ragazza di trent'anni mentre la voce parla a chi ha superato i settanta): con un
    # pubblico che guarda un video su se' stesso e' una rottura di credibilita'. Le immagini
    # generate nascono dal testo della scena, quindi restano sempre in tema.
    # "stock" resta disponibile come variante esplicita.
    ap.add_argument("--visuals", choices=["ai", "stock"], default="ai")
    ap.add_argument("--art-style", default="realistic",
                    help="Solo con --visuals ai. Valori reali: cinematic, realistic, illustration, "
                         "anime, comicBook, threeDimensionModel, fantasyArt, waterColor, lineArt, "
                         "modelingCompound, whimsical, biblical, filmNoir, tinyWorld, "
                         "technicalIllustration.")
    ap.add_argument("--ai-video-model", default=AI_VIDEO_MODEL,
                    choices=["runware-kling-2.5-turbo", "runware-seedance-pro-fast",
                             "runware-p-video", "runware-pixverse-v5-fast", "runware-ltx-2-fast",
                             "nessuno"],
                    help="Scene in MOVIMENTO invece che immagini ferme. 'nessuno' le lascia fisse.")
    ap.add_argument("--clip-percentage", type=int, default=AI_VIDEO_CLIP_PERCENTAGE,
                    help="Percentuale di scene resa come clip video (0-100).")
    args = ap.parse_args()

    key = _api_key()
    os.makedirs(VIDEOS_DIR, exist_ok=True)

    content = build_script_content()
    voice_id = find_italian_voice(key)
    modello = None if args.ai_video_model == "nessuno" else args.ai_video_model
    if args.visuals == "ai":
        print(f"[+] Visuals: ai (artStyle={args.art_style}, "
              f"video={modello or 'NESSUNO — scene ferme'}, clip={args.clip_percentage}%)")
    else:
        print("[+] Visuals: stock (clip di repertorio)")
    file_id = generate_video(key, content, voice_id, args.file_name,
                            visuals=args.visuals, art_style=args.art_style,
                            ai_video_model=modello, clip_percentage=args.clip_percentage)
    download_url = poll_status(key, file_id)

    out_path = os.path.join(VIDEOS_DIR, f"{args.file_name}.mp4")
    download_file(download_url, out_path)
    print(f"[+] Video reale scaricato: {out_path}")
    registra_video_prodotto(out_path, args.file_name)


if __name__ == "__main__":
    main()
