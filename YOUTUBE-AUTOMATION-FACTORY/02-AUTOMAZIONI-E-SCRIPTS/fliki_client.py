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


def _request(method: str, path: str, key: str, body: dict | None = None) -> dict:
    url = f"{API_BASE}{path}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="ignore")
        raise SystemExit(f"[!] Errore API reale {method} {path}: HTTP {e.code} — {detail}")


def find_italian_voice(key: str, prefer_gender: str = "male") -> str:
    voices = _request("GET", "/voices?languageId=it&dialectId=it-IT", key)
    items = voices.get("data", voices) if isinstance(voices, dict) else voices
    if isinstance(items, dict):
        items = items.get("voices", [])
    candidates = [v for v in items if v.get("gender") == prefer_gender] or items
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
    scenes = mod._parse_script_scenes(script_text)
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
