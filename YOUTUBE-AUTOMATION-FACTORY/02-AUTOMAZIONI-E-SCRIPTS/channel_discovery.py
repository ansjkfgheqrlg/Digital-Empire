#!/usr/bin/env python3
"""
Reparto INTELLIGENCE — agente `channel-scout` (nuovo, 2026-08-05).

Tool ADVISORY: propone altri canali reali nella stessa nicchia di @dosementale, per non
dipendere da un'unica fonte. NON cambia mai CANALE_TARGET — scrive solo proposte in
memory/proposte_canali.json, che restano proposte finche' Gael/Max non decidono di persona
(stesso principio gia' scritto, ma mai collegato a nulla, in
youtube_automation_factory/src/youtube_automation_factory/agents/profitable_niche_agent.py:
"non cambia mai PRIMARY_NICHE, produce solo proposte").

Perche' questo tool e' diverso dallo scouting rimosso il 2026-07-31 (vedi
apex7_orchestrator.py righe 74-78, funnel morto "Manuale Claude Code" che sovrascriveva la
produzione): e' READ-ONLY sulla configurazione della fabbrica. Nessuna run di produzione legge
memory/proposte_canali.json — e' un file per un umano (o un capo-strategia futuro) da
consultare, non un input automatico.

Come funziona (tutto reale, nessun dato inventato):
1. Cerca DAVVERO su YouTube (Playwright, filtro nativo "Canale") le query di nicchia passate.
2. Per ogni canale trovato riusa youtube_hunter_playwright.raccogli() (stesso codice gia'
   testato su @dosementale) per prendere i suoi video reali.
3. Calcola l'indice Cash Cow reale con cashcow_check.py — stesso metodo, stesso numero
   comparabile a quello gia' misurato per @dosementale (21.0 al 2026-08-04).
4. Scrive le proposte ordinate per indice, senza toccare nessun file di produzione.

Uso:
    python channel_discovery.py --query "consigli per anziani" --query "saggezza spirituale"
    python channel_discovery.py --query "benessere over 60" --max-canali 5 --visibile
"""
import os
import re
import sys
import json
import time
import argparse
import subprocess
from datetime import datetime

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-youtube")
PROPOSTE_PATH = os.path.join(FACTORY_DIR, "memory", "proposte_canali.json")

sys.path.insert(0, SCRIPT_DIR)
import youtube_hunter_playwright as hunter  # noqa: E402

# Filtro nativo "Canale" della ricerca YouTube (parametro pubblico &sp=, non un endpoint
# privato: e' lo stesso link che produce l'interfaccia quando un utente clicca
# Filtri -> Tipo -> Canale). Se YouTube lo cambia, la pagina torna a risultati misti e
# _estrai_canali scarta comunque tutto cio' che non ha un link /@handle o /channel/.
FILTRO_CANALE = "EgIQAg%3D%3D"

_JS_ESTRAZIONE_CANALI = """
    (maxCanali) => {
      const out = [];
      const visti = new Set();
      const nodi = document.querySelectorAll('ytd-channel-renderer');
      for (const n of nodi) {
        const link = n.querySelector('a#main-link, a#channel-title, a[href^="/@"], a[href^="/channel/"]');
        if (!link) continue;
        const href = link.getAttribute('href') || '';
        if (visti.has(href)) continue;
        visti.add(href);
        const righe = (n.innerText || '').split('\\n').map(r => r.trim()).filter(Boolean);
        out.push({href, righe});
        if (out.length >= maxCanali) break;
      }
      return out;
    }
"""

_RE_ISCRITTI = re.compile(
    r"^([\d.,]+)\s*(k|m|mln|mila)?\s*(?:di\s+)?iscritti$|^([\d.,]+)\s*(K|M)?\s*subscribers?$",
    re.IGNORECASE)


def _parse_iscritti(text: str):
    if not text:
        return None
    m = _RE_ISCRITTI.match(text.strip())
    if not m:
        return None
    numero = (m.group(1) or m.group(3) or "").replace(",", ".")
    suffisso = (m.group(2) or m.group(4) or "").lower()
    try:
        valore = float(numero)
    except ValueError:
        return None
    return valore * {"k": 1_000, "mila": 1_000, "m": 1_000_000, "mln": 1_000_000}.get(suffisso, 1)


def _estrai_canali(page, max_canali: int) -> list[dict]:
    grezzi = page.evaluate(_JS_ESTRAZIONE_CANALI, max_canali)
    canali = []
    for g in grezzi:
        href = g["href"]
        m = re.search(r"/(@[\w.-]+|channel/[\w-]+)", href)
        if not m:
            continue
        handle = m.group(1)
        righe = g["righe"]
        nome = righe[0] if righe else handle
        iscritti = next((v for r in righe if (v := _parse_iscritti(r)) is not None), None)
        canali.append({"handle": handle if handle.startswith("@") else None,
                       "url": f"https://www.youtube.com{href}" if href.startswith("/") else href,
                       "nome": nome, "iscritti": iscritti})
    return canali


def cerca_canali(query: str, max_canali: int, *, headless: bool = True) -> list[dict]:
    os.makedirs(PROFILE_DIR, exist_ok=True)
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR, headless=headless,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        url = f"https://www.youtube.com/results?search_query={query}&sp={FILTRO_CANALE}"
        print(f"[+] Cerco canali: {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(2)
        for etichetta in ("Accetta tutto", "Accept all", "Rifiuta tutto", "Reject all"):
            try:
                page.get_by_role("button", name=etichetta).click(timeout=3000)
                time.sleep(1.5)
                break
            except Exception:
                continue
        try:
            page.wait_for_selector("ytd-channel-renderer", timeout=15000)
        except Exception:
            print(f"[i] Nessun canale trovato per '{query}' (layout cambiato o zero risultati: "
                  f"non si inventa nulla).")
            context.close()
            return []
        canali = _estrai_canali(page, max_canali)
        context.close()
    return canali


def indice_cashcow(handle: str) -> float | None:
    """Riusa hunter.raccogli() (gia' testato su @dosementale) + cashcow_check.py sullo
    stesso identico metodo usato per il canale target, cosi' i due indici sono comparabili."""
    video = hunter.raccogli(handle, max_video=20, headless=True)
    if not video:
        return None
    tmp = os.path.join(FACTORY_DIR, "memory", f"_tmp_cashcow_{re.sub(r'[^a-zA-Z0-9]', '_', handle)}.json")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"channel": handle, "videos": video}, f, ensure_ascii=False)
    try:
        res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "cashcow_check.py"), "--json", tmp],
                             capture_output=True, text=True, timeout=60)
        dati = json.loads(res.stdout)
        return dati.get("index")
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def main():
    ap = argparse.ArgumentParser(description="Propone altri canali reali nella nicchia (advisory, non cambia CANALE_TARGET).")
    ap.add_argument("--query", action="append", required=True, help="Query di ricerca canali (ripetibile).")
    ap.add_argument("--max-canali", type=int, default=5, help="Massimo canali da valutare PER query.")
    ap.add_argument("--visibile", action="store_true")
    args = ap.parse_args()

    trovati = {}
    for query in args.query:
        for c in cerca_canali(query, args.max_canali, headless=not args.visibile):
            chiave = c["handle"] or c["url"]
            if chiave not in trovati:
                trovati[chiave] = c
                trovati[chiave]["query_origine"] = [query]
            else:
                trovati[chiave]["query_origine"].append(query)

    if not trovati:
        raise SystemExit("[!] Nessun canale reale trovato su nessuna query. Nessuna proposta scritta.")

    print(f"\n[+] {len(trovati)} canali reali trovati, misuro l'indice Cash Cow di ciascuno...")
    proposte = []
    for chiave, c in trovati.items():
        handle = c["handle"]
        if not handle:
            print(f"    [!] {c['nome']}: nessun @handle risolvibile (link legacy /channel/id), saltato.")
            continue
        indice = indice_cashcow(handle)
        print(f"    {handle:30} indice Cash Cow: {indice if indice is not None else 'N/D (0 video reali raccolti)'}")
        proposte.append({**c, "cashcow_index": indice})

    proposte.sort(key=lambda p: -(p["cashcow_index"] or -1))
    os.makedirs(os.path.dirname(PROPOSTE_PATH), exist_ok=True)
    with open(PROPOSTE_PATH, "w", encoding="utf-8") as f:
        json.dump({"generato": datetime.now().isoformat(), "query": args.query,
                   "nota": "Proposte, non decisioni. Nessuna run di produzione legge questo "
                           "file. CANALE_TARGET cambia solo per decisione esplicita di Gael/Max.",
                   "canali": proposte}, f, ensure_ascii=False, indent=2)
    print(f"\n[+] {len(proposte)} proposte scritte → {PROPOSTE_PATH}")


if __name__ == "__main__":
    main()
