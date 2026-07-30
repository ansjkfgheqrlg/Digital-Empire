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
import sys
import json
import time
import argparse
import urllib.request
import urllib.error

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


def build_script_content() -> str:
    """Testo reale dallo script.md di F3 (stesse 4 sezioni gia' parsate da
    _parse_script_scenes in apex7_orchestrator.py), con 'sceneBreakdown: lineBreak'
    cosi' Fliki rispetta i confini di scena reali invece di indovinarli."""
    sys.path.insert(0, SCRIPT_DIR)
    import apex7_orchestrator as mod  # noqa: E402

    script_path = os.path.join(TEMPLATES_DIR, "script.md")
    with open(script_path, "r", encoding="utf-8") as f:
        script_text = f.read()
    orch = mod.Apex7Orchestrator(run_id="fliki-client")
    scenes = orch._parse_script_scenes(script_text)
    if not scenes:
        raise SystemExit("[!] Nessuna scena reale trovata in script.md.")
    return "\n\n".join(s["text"].split("➕")[0].strip() for s in scenes)


def generate_video(key: str, content: str, voice_id: str, file_name: str) -> str:
    payload = {
        "payload": [{
            "workflowType": "script",
            "workflowFormat": "video",
            "content": content,
            "voiceId": voice_id,
            "aspectRatio": "16:9",
            "resolution": "1080p",
            "visuals": "stock",
            "sceneBreakdown": "lineBreak",
            "fileName": file_name,
            "shouldExport": True,
            # subtitlePresetId reale ottenuto cliccando il bottone "Copy subtitle preset ID"
            # su fliki.ai/info/subtitle via Playwright (l'ID non e' nell'HTML statico ne'
            # in nessuna chiamata di rete — va copiato dal bottone, come documentato).
            "subtitlePresetId": "builtin-legacy-bold",
            "highlightSubtitles": True,
            # Il video precedente (senza duration esplicita) e' uscito di soli 230s invece
            # dei ~15 minuti di contenuto reale scritto in script.md. Impostiamo una durata
            # target esplicita (secondi) coerente con la lunghezza reale dello script.
            "duration": 720,
        }]
    }
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


def main():
    ap = argparse.ArgumentParser(description="Genera il video reale via API Fliki dalla spec F3/F4.")
    ap.add_argument("--file-name", default="claude-code-installazione")
    args = ap.parse_args()

    key = _api_key()
    os.makedirs(VIDEOS_DIR, exist_ok=True)

    content = build_script_content()
    voice_id = find_italian_voice(key)
    file_id = generate_video(key, content, voice_id, args.file_name)
    download_url = poll_status(key, file_id)

    out_path = os.path.join(VIDEOS_DIR, f"{args.file_name}.mp4")
    download_file(download_url, out_path)
    print(f"[+] Video reale scaricato: {out_path}")


if __name__ == "__main__":
    main()
