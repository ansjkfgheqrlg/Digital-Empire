# -*- coding: utf-8 -*-
"""corso_ingest.py — ingestione di corsi su piattaforme a login con video protetti.

PERCHE' ESISTE (e perche' NON tocca yt_ingest.py — ADR-003: si avvolge, non si riscrive).
`yt_ingest.py` parla YouTube/TikTok via yt-dlp su URL pubblici. Il portale di un corso a
pagamento e' un'altra bestia, misurata il 2026-09-04 su corsi.muccarossa.com:

  - si entra solo con login (form dentro un iframe SSO);
  - i video NON hanno un tasto di scaricamento: arrivano a pezzi (HLS) da un CDN
    (`content.apisystem.tech`) con un GETTONE NELLA QUERY CHE SCADE;
  - non esistono sottotitoli, testo della lezione o allegati: la conoscenza sta
    tutta nel parlato e in cio' che appare a schermo.

Da qui le tre scelte di questo modulo:
  1. il gettone si cattura AL VOLO intercettando le richieste del browser, e si usa SUBITO
     (una lezione per volta, mai code lunghe: un gettone in coda e' un gettone scaduto);
  2. si scarica alla qualita' minima utile a leggere il testo a schermo (360p di default),
     non alla massima: i frame servono a leggere, non a fare bella figura;
  3. tutto e' idempotente e ripartibile: `stato.json` per lezione, e una lezione gia'
     completata non si riscarica.

USO
    python corso_ingest.py --mappa                      # censisce corsi/categorie/lezioni + durate
    python corso_ingest.py --lezione <lesson_id>        # scarica UNA lezione
    python corso_ingest.py --lezione <lesson_id> --qualita 720

I video e i frame NON vanno mai in git (ADR-013): vivono sotto `runs/` che e' gia' escluso.
"""

import argparse
import io
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
RUNS = os.path.join(STUDIO, "runs")

BASE = "https://corsi.muccarossa.com"

# I due corsi nel perimetro dato da Max il 2026-09-04. Il terzo del portale
# (Google Automation Platinum, 181 lezioni) resta FUORI: non e' una dimenticanza.
CORSI = {
    "aitubepro": "5ff04cd6-ed8a-49f6-bbbb-6a58de8ff5b2",   # AI TUBE PRO - SMART TUBE, 116 lezioni
    "bonus":     "da098baa-0e44-4192-8ef5-e7cdbf3fd2ee",   # Bonus Esclusivi, 51 lezioni
}

# Il CDN da cui arrivano i pezzi del video. Serve a riconoscere l'indirizzo giusto
# fra le decine di richieste che una pagina fa.
CDN_MARKER = "content.apisystem.tech"


# --------------------------------------------------------------------------- credenziali
def credenziali():
    """Le credenziali NON stanno nel codice: arrivano dall'ambiente o da un file fuori dal
    repository. Tre credenziali in chiaro sono gia' costate a questa azienda tre voci di
    backlog (B-020, B-021, B-023) e restano leggibili nella storia git per sempre."""
    email = os.environ.get("CORSO_EMAIL")
    pwd = os.environ.get("CORSO_PASSWORD")
    if email and pwd:
        return email, pwd
    fuori = os.path.join(os.path.expanduser("~"), ".claude", "corso-credenziali.json")
    if os.path.exists(fuori):
        with io.open(fuori, encoding="utf-8") as f:
            d = json.load(f)
        return d.get("email"), d.get("password")
    raise SystemExit(
        "[!] Credenziali assenti. Mettile in %s (email/password) oppure nelle variabili "
        "d'ambiente CORSO_EMAIL / CORSO_PASSWORD. Nel codice non ci vanno." % fuori)


# --------------------------------------------------------------------------- browser
def apri_browser(p, visibile=True):
    profilo = os.path.join(RUNS, "_profilo-corso")
    os.makedirs(profilo, exist_ok=True)
    return p.chromium.launch_persistent_context(
        user_data_dir=profilo, headless=not visibile, channel="chrome",
        args=["--start-maximized"], no_viewport=True)


def entra(page):
    """Login. Il form vive in un iframe (SSO) e il pulsante 'Accedi' non sempre invia:
    l'Invio nel campo password si e' rivelato l'unico modo affidabile, misurato dal vivo."""
    page.goto(BASE + "/courses", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    if "login" not in page.url.lower():
        return True  # sessione ancora valida nel profilo persistente

    email, pwd = credenziali()
    frame = None
    for fr in page.frames:
        try:
            if fr.locator("input[type='password']").count() > 0:
                frame = fr
                break
        except Exception:
            continue
    if frame is None:
        print("[!] Form di login non trovato.")
        return False

    frame.locator("input[type='text']").first.fill(email, timeout=15000)
    frame.locator("input[type='password']").first.fill(pwd, timeout=15000)
    try:
        frame.get_by_text("Accedi", exact=True).first.click(timeout=6000)
    except Exception:
        pass
    page.wait_for_timeout(2500)
    if "login" in page.url.lower():
        frame.locator("input[type='password']").first.press("Enter")
        page.wait_for_timeout(8000)
    ok = "login" not in page.url.lower()
    print("[%s] login" % ("+" if ok else "!"))
    return ok


# --------------------------------------------------------------------------- mappa
def mappa(visibile=True):
    """Censimento di categorie e lezioni.

    NON si clicca la barra laterale: naviga in JavaScript e non espone un solo collegamento
    vero (verificato dal vivo il 2026-09-04, zero href di lezione in pagina). Si intercetta
    invece la chiamata interna che il portale fa da se' — `user-purchase/categories` — che
    restituisce l'indice completo del corso in un colpo: categorie, lezioni, identificativi,
    ordine e tipo di contenuto. 116 lezioni lette cosi' contro 116 aperture di pagina.
    """
    from playwright.sync_api import sync_playwright
    fuori = {}
    with sync_playwright() as p:
        ctx = apri_browser(p, visibile)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        raccolte = {}

        def su_risposta(res):
            if "user-purchase/categories" not in res.url:
                return
            try:
                raccolte[res.url] = res.json()
            except Exception:
                pass

        page.on("response", su_risposta)

        if not entra(page):
            ctx.close()
            return 2

        for slug, corso_id in CORSI.items():
            print("\n=== CORSO %s ===" % slug)
            raccolte.clear()
            page.goto("%s/courses/products/%s" % (BASE, corso_id),
                      wait_until="domcontentloaded", timeout=60000)
            # l'indice arriva poco dopo il caricamento; si aspetta finche' non c'e'
            indice = None
            for _ in range(20):
                page.wait_for_timeout(1000)
                for u, d in raccolte.items():
                    if corso_id in u and (d.get("categories") if isinstance(d, dict) else None):
                        indice = d
                        break
                if indice:
                    break
            if not indice:
                print("  [!] Indice non ricevuto dal portale.")
                continue

            categorie = []
            n_lez = 0
            for c in indice.get("categories") or []:
                lezioni = []
                for post in (c.get("posts") or []):
                    lezioni.append({
                        "lesson_id": post.get("id"),
                        "titolo": (post.get("title") or "").strip(),
                        "ordine": post.get("sequenceNo"),
                        "tipo": post.get("contentType"),
                        "categoria_id": post.get("categoryId"),
                        "url": "%s/courses/products/%s/modules/%s/lessons/%s" % (
                            BASE, corso_id, post.get("categoryId"), post.get("id")),
                        "durata_s": None,          # si legge quando si apre la lezione
                        "stato": "da-fare",
                    })
                n_lez += len(lezioni)
                categorie.append({
                    "categoria_id": c.get("id"),
                    "titolo": (c.get("title") or "").strip(),
                    "ordine": c.get("sequenceNo"),
                    "n_lezioni": len(lezioni),
                    "lezioni": lezioni,
                })
                print("  %-45s %3d lezioni" % ((c.get("title") or "?")[:45], len(lezioni)))
            print("  TOTALE: %d lezioni in %d categorie" % (n_lez, len(categorie)))
            fuori[slug] = {"corso_id": corso_id, "n_lezioni": n_lez, "categorie": categorie}

        os.makedirs(os.path.join(RUNS, "corso-aitubepro"), exist_ok=True)
        dest = os.path.join(RUNS, "corso-aitubepro", "mappa.json")
        with io.open(dest, "w", encoding="utf-8") as f:
            json.dump(fuori, f, ensure_ascii=False, indent=2)
        totale = sum(v["n_lezioni"] for v in fuori.values())
        print("\n[+] Mappa salvata (%d lezioni in totale): %s" % (totale, dest))
        ctx.close()
    return 0


# --------------------------------------------------------------------------- una lezione
def carica_mappa():
    dest = os.path.join(RUNS, "corso-aitubepro", "mappa.json")
    if not os.path.exists(dest):
        raise SystemExit("[!] Mappa assente. Lancia prima: corso_ingest.py --mappa")
    with io.open(dest, encoding="utf-8") as f:
        return json.load(f)


def voce_lezione(lesson_id, corso="aitubepro"):
    """Trova la lezione nella mappa e restituisce la sua voce completa."""
    for c in carica_mappa().get(corso, {}).get("categorie", []):
        for l in c.get("lezioni", []):
            if l.get("lesson_id") == lesson_id:
                l = dict(l)
                l["categoria"] = c.get("titolo")
                return l
    raise SystemExit("[!] Lezione %s non trovata nella mappa del corso %s." % (lesson_id, corso))


def url_lezione(lesson_id, corso="aitubepro"):
    return voce_lezione(lesson_id, corso)["url"]



def durata_flusso(url):
    """Quanto dura il flusso che sta dietro a questo indirizzo, senza scaricarlo.

    ffprobe legge solo il manifesto (poche decine di KB) e risponde in un paio di
    secondi: e' quello che permette di scegliere il flusso GIUSTO prima di scaricare
    centinaia di frammenti.
    """
    # Alcuni manifesti del portale rispondono solo a chi si presenta come il lettore
    # della pagina: senza Referer e User-Agent tornano 403 e ffprobe non misura nulla
    # (visto il 2026-09-06 su L11, L12 e L18 — tre candidati, tutti "?" ).
    intestazioni = ("Referer: https://corsi.muccarossa.com/\r\n"
                    "Origin: https://corsi.muccarossa.com\r\n")
    agente = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
    for extra in (["-headers", intestazioni, "-user_agent", agente], []):
        try:
            out = subprocess.run(
                ["ffprobe", "-v", "error"] + extra +
                ["-show_entries", "format=duration",
                 "-of", "default=nw=1:nk=1", url],
                capture_output=True, text=True, timeout=45)
            return int(round(float(out.stdout.strip())))
        except Exception:
            continue
    return None


def scegli_flusso(catturati, durata_s):
    """Fra i flussi visti dal browser, sceglie quello che dura quanto la lezione.

    PERCHE' NON BASTA PRENDERNE UNO. Le pagine del portale caricano piu' lettori:
    oltre alla lezione ci sono video promozionali e registrazioni di webinar. Il
    2026-09-04 la lezione 81e4e28a e' arrivata a casa due volte col video sbagliato
    — prima l'introduzione di un altro modulo (119 s), poi un webinar di vendita
    (1.595 s) — mentre la lezione ne dura 935. Prendere il primo flusso, o l'ultimo,
    e' una scommessa: la durata invece e' un fatto, e si puo' misurare prima di
    scaricare.

    Se la durata della lezione non si conosce, si dichiara e si prende l'ultimo visto.
    """
    unici = []
    for u in catturati:
        if u not in unici:
            unici.append(u)
    if not durata_s:
        print("[!] Durata della lezione sconosciuta: prendo l'ultimo flusso visto "
              "(%d candidati). Il controllo sul file scaricato resta attivo." % len(unici))
        return unici[-1]

    tolleranza = max(10, 0.05 * durata_s)
    misure = []
    for u in unici:
        d = durata_flusso(u)
        misure.append((u, d))
        print("[i] candidato: %s s attesi %s -> %s"
              % (d if d else "?", durata_s, "SI" if d and abs(d - durata_s) <= tolleranza else "no"))
        if d and abs(d - durata_s) <= tolleranza:
            return u
    if len(unici) == 1:
        print("[!] Un solo flusso e non corrisponde alla durata attesa: lo scarico "
              "comunque, il controllo sul file lo marchera' sospetto.")
        return unici[0]
    # NESSUN candidato misurabile (tutte le durate "?"): non e' la stessa cosa di
    # "misurati e sbagliati". Rinunciare qui era troppo severo e bloccava tre lezioni
    # (2026-09-06): il controllo che conta davvero — `durata_reale` sul file scaricato,
    # che marca `1-sospetto` — resta comunque attivo dopo. Si prende l'ultimo visto,
    # come gia' si fa quando la durata della lezione non si conosce.
    if all(d is None for _u, d in misure):
        print("[!] Nessun candidato misurabile (%d flussi, tutte le durate ignote): "
              "prendo l'ultimo visto. Il controllo sul file scaricato resta attivo."
              % len(unici))
        return unici[-1]
    return None


def durata_reale(percorso):
    """Quanti secondi dura DAVVERO il file scaricato, secondo ffprobe.

    Serve a smascherare i due guasti che si assomigliano e sono opposti: il video di
    un'altra lezione (dura tutt'altro) e lo scaricamento interrotto a meta'. Senza
    questa misura, entrambi passano per lezione buona e si studiano per veri.
    """
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", percorso],
            capture_output=True, text=True, timeout=30)
        return int(round(float(out.stdout.strip())))
    except Exception:
        return None


def scarica_lezione(lesson_id, corso="aitubepro", qualita=360, visibile=True):
    """Apre la lezione, cattura l'indirizzo del flusso col gettone, scarica subito.

    'Subito' e' la parola importante: il gettone scade. Per questo non si accodano
    lezioni — se ne prende una, la si porta a casa, e si passa alla successiva.
    """
    from playwright.sync_api import sync_playwright

    cartella = os.path.join(RUNS, "corso-aitubepro", lesson_id)
    os.makedirs(cartella, exist_ok=True)
    stato_path = os.path.join(cartella, "stato.json")
    mp4 = os.path.join(cartella, "video.mp4")

    if os.path.exists(mp4) and os.path.getsize(mp4) > 100000:
        print("[=] Gia' scaricata (%s, %.1f MB): non rifaccio niente."
              % (lesson_id, os.path.getsize(mp4) / 1e6))
        return 0

    catturati = []
    with sync_playwright() as p:
        ctx = apri_browser(p, visibile)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        def su_richiesta(req):
            if CDN_MARKER in req.url and "master.m3u8" in req.url:
                catturati.append(req.url)
        page.on("request", su_richiesta)

        if not entra(page):
            ctx.close()
            return 2

        # L'indirizzo di una lezione richiede ANCHE la categoria:
        #   /courses/products/<corso>/modules/<categoria>/lessons/<lezione>
        # Senza il pezzo `modules/` la pagina si apre ma il lettore non carica nulla, e si
        # scambia per "video assente" quello che e' solo un indirizzo incompleto
        # (sbagliato dal vivo il 2026-09-04). L'indirizzo esatto e' gia' nella mappa.
        url = url_lezione(lesson_id, corso)
        # Si azzera QUI: tutto cio' che il browser aveva chiesto prima di questa
        # navigazione appartiene a un'altra lezione. Il 2026-09-04 la lezione 81e4e28a
        # e' arrivata a casa col video sbagliato (l'introduzione di un altro modulo,
        # 119 s al posto dei suoi) proprio perche' si prendeva il PRIMO flusso visto.
        del catturati[:]
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(11000)

        titolo = ""
        durata_s = None
        # Prima si chiede al lettore stesso: e' l'unica fonte che parla di QUESTO video.
        # Il ripiego (leggere i mm:ss dal testo e prendere il massimo) prendeva la durata
        # piu' lunga presente in pagina, che spesso e' quella di un'ALTRA lezione
        # dell'elenco laterale: cosi' 81e4e28a risultava di 935 s quando ne dura 119.
        try:
            d = page.locator("video").first.evaluate(
                "v => (v && isFinite(v.duration) && v.duration > 0) ? v.duration : null",
                timeout=8000)
            if d:
                durata_s = int(round(float(d)))
        except Exception:
            pass
        try:
            testo = page.locator("body").inner_text(timeout=8000)
            righe = [r.strip() for r in testo.splitlines() if r.strip()]
            # ripiego: la durata compare nella barra del lettore come mm:ss
            if durata_s is None:
                for r in righe:
                    m = re.fullmatch(r"(\d{1,2}):(\d{2})", r)
                    if m:
                        s = int(m.group(1)) * 60 + int(m.group(2))
                        durata_s = max(durata_s or 0, s)
            for r in righe:
                if "/ Categories /" in r:
                    titolo = r.split("/")[-1].strip()
                    break
        except Exception:
            pass

        # se il lettore non ha ancora chiesto il flusso, lo si mette in moto
        if not catturati:
            try:
                page.locator("video").first.click(timeout=6000)
                page.wait_for_timeout(6000)
            except Exception:
                pass

        ctx.close()

    if not catturati:
        print("[!] Nessun flusso catturato: il lettore non ha caricato il video.")
        return 1

    flusso = scegli_flusso(catturati, durata_s)
    if flusso is None:
        print("[!] Nessun flusso corrisponde alla lezione: non scarico niente.")
        return 4
    print("[+] Flusso catturato (gettone valido adesso).")
    print("[+] Scarico a %dp ..." % qualita)

    # Il CDN del portale rifiuta con 403 chi non si presenta come il lettore della pagina
    # (visto il 2026-09-06 su L11, L12, L18: il flusso era catturato e valido, ma yt-dlp
    # prendeva 403 sul manifesto). Le stesse intestazioni che usa ffprobe in durata_flusso.
    AGENTE = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
    cmd = [sys.executable, "-m", "yt_dlp", "--no-warnings", "--quiet", "--no-progress",
           "--user-agent", AGENTE,
           "--add-header", "Referer:https://corsi.muccarossa.com/",
           "--add-header", "Origin:https://corsi.muccarossa.com",
           "-f", "bestvideo[height<=%d]+bestaudio/best[height<=%d]/best" % (qualita, qualita),
           "--merge-output-format", "mp4", "-o", mp4, flusso]
    esito = subprocess.run(cmd, cwd=cartella)
    ok = esito.returncode == 0 and os.path.exists(mp4)

    # Il video e' arrivato: ma e' IL video della lezione? Si misura, non si spera.
    durata_reale_s = durata_reale(mp4) if ok else None
    avviso = None
    if ok and durata_reale_s and durata_s:
        scarto = abs(durata_reale_s - durata_s)
        if scarto > max(10, 0.05 * durata_s):
            avviso = ("il file dura %d s ma la lezione ne dichiara %d (scarto %d s): "
                      "probabilmente e' il video di un'altra lezione, oppure lo "
                      "scaricamento si e' interrotto" % (durata_reale_s, durata_s, scarto))
    passo = "1-scaricato" if ok else "1-fallito"
    if ok and avviso:
        passo = "1-sospetto"

    with io.open(stato_path, "w", encoding="utf-8") as f:
        json.dump({
            "lesson_id": lesson_id,
            "corso": corso,
            "titolo": titolo,
            "durata_s": durata_s,
            "durata_reale_s": durata_reale_s,
            "scaricato": bool(ok),
            "qualita": qualita,
            "quando": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "passo": passo,
            "avviso": avviso,
        }, f, ensure_ascii=False, indent=2)

    if avviso:
        print("[!] SOSPETTA: %s" % avviso)
        return 3

    if ok:
        print("[+] Video: %s (%.1f MB)" % (mp4, os.path.getsize(mp4) / 1e6))
        if durata_s:
            print("[+] Durata letta dal lettore: %d s (%d:%02d)" % (durata_s, durata_s // 60, durata_s % 60))
        return 0
    print("[!] Scaricamento fallito (uscita %s)." % esito.returncode)
    return 1


def main():
    ap = argparse.ArgumentParser(description="Ingestione corsi a login con video protetti.")
    ap.add_argument("--mappa", action="store_true", help="Censisce corsi, lezioni e durate.")
    ap.add_argument("--lezione", help="lesson_id da scaricare.")
    ap.add_argument("--corso", default="aitubepro", choices=sorted(CORSI))
    ap.add_argument("--qualita", type=int, default=360, help="Altezza massima (default 360).")
    ap.add_argument("--nascosto", action="store_true", help="Browser invisibile.")
    a = ap.parse_args()

    if a.mappa:
        return mappa(visibile=not a.nascosto)
    if a.lezione:
        return scarica_lezione(a.lezione, a.corso, a.qualita, visibile=not a.nascosto)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
