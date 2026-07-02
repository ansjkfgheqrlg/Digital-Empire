"""
cdp.py — Motore browser via Chrome DevTools Protocol (Half A / Max).

Usa il **Google Chrome installato** sul PC, senza Playwright: lancia Chrome con la porta
DevTools e comunica in CDP via websocket. Serve sia allo scraping (bypassa Akamai con il
fingerprint del browser vero) sia al render PDF (Page.printToPDF).

Perché no Playwright: così l'app .exe (PyInstaller) NON deve impacchettare il driver node né
un chromium/GTK. Dipende solo da: requests + websocket-client + il Chrome del cliente.

API principale:
    chrome = find_chrome()
    proc = launch(port, profile, headless, url)
    wait_devtools(port)
    page = Page(port)
    page.wait_html(pred, timeout); page.html(); page.print_pdf()
    page.close(); kill_tree(proc)
"""
from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import time
from pathlib import Path

import requests

try:
    from websocket import create_connection  # websocket-client
except ImportError as _exc:  # pragma: no cover
    create_connection = None  # type: ignore
    _WS_ERR = _exc


# --------------------------------------------------------------------------- #
# Chrome discovery / launch
# --------------------------------------------------------------------------- #
def find_chrome() -> str | None:
    cands = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in cands:
        if c and os.path.exists(c):
            return c
    return (shutil.which("chrome") or shutil.which("google-chrome")
            or shutil.which("chrome.exe"))


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def launch(chrome: str, port: int, profile: str, headless: bool, url: str | None = None):
    args = [
        chrome, f"--remote-debugging-port={port}", f"--user-data-dir={profile}",
        "--no-first-run", "--no-default-browser-check",
        "--disable-blink-features=AutomationControlled", "--disable-features=Translate",
    ]
    if headless:
        args += ["--headless=new", "--disable-gpu", "--hide-scrollbars"]
    else:
        args.append("--start-maximized")
    if url:
        args.append(url)
    return subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def wait_devtools(port: int, timeout: float = 45) -> None:
    if create_connection is None:
        raise RuntimeError("websocket-client non installato (pip install websocket-client).")
    deadline = time.time() + timeout
    url = f"http://127.0.0.1:{port}/json/version"
    while time.time() < deadline:
        try:
            if requests.get(url, timeout=1).ok:
                return
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError("DevTools non risponde: Chrome non partito o profilo bloccato.")


def kill_tree(proc) -> None:
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            proc.terminate()
        proc.wait(timeout=8)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


# --------------------------------------------------------------------------- #
# Sessione CDP su un target "page"
# --------------------------------------------------------------------------- #
class Page:
    def __init__(self, port: int, connect_timeout: float = 20):
        self.port = port
        self._id = 0
        ws_url = self._page_ws(connect_timeout)
        self.ws = create_connection(ws_url, max_size=None, timeout=35)

    def _page_ws(self, timeout: float) -> str:
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                targets = requests.get(f"http://127.0.0.1:{self.port}/json", timeout=2).json()
                pages = [t for t in targets if t.get("type") == "page" and t.get("webSocketDebuggerUrl")]
                if pages:
                    return pages[0]["webSocketDebuggerUrl"]
            except Exception:
                pass
            time.sleep(0.4)
        raise RuntimeError("Nessun target 'page' disponibile su DevTools.")

    def call(self, method: str, params: dict | None = None, timeout: float = 35):
        self._id += 1
        mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        deadline = time.time() + timeout
        while time.time() < deadline:
            self.ws.settimeout(max(0.5, deadline - time.time()))
            try:
                msg = json.loads(self.ws.recv())
            except Exception:
                continue
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"CDP {method}: {msg['error']}")
                return msg.get("result", {})
        raise RuntimeError(f"CDP timeout su {method}")

    def navigate(self, url: str) -> None:
        self.call("Page.navigate", {"url": url})

    def html(self) -> str:
        r = self.call("Runtime.evaluate", {
            "expression": "document.documentElement.outerHTML",
            "returnByValue": True,
        })
        return ((r or {}).get("result") or {}).get("value") or ""

    def scroll(self, dy: int = 1200) -> None:
        try:
            self.call("Runtime.evaluate", {"expression": f"window.scrollBy(0,{dy})"})
        except Exception:
            pass

    def wait_html(self, predicate, timeout: float = 45, poll: float = 1.5) -> str:
        deadline = time.time() + timeout
        last = ""
        while time.time() < deadline:
            last = self.html()
            if predicate(last):
                return last
            self.scroll()
            time.sleep(poll)
        return last

    def print_pdf(self, print_background: bool = True) -> bytes:
        import base64
        self.call("Page.enable")
        r = self.call("Page.printToPDF", {
            "printBackground": print_background,
            "marginTop": 0, "marginBottom": 0, "marginLeft": 0, "marginRight": 0,
            "preferCSSPageSize": True,
        }, timeout=60)
        return base64.b64decode(r["data"])

    def close(self) -> None:
        try:
            self.ws.close()
        except Exception:
            pass
