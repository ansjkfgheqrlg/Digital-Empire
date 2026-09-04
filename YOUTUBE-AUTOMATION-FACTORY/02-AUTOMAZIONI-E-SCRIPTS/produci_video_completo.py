#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Un solo comando (= un solo pulsante in Aureus) che produce DAVVERO video + copertina.

Non reimplementa niente (ADR-003: wrap, mai riscrittura). Incatena i tre pezzi reali che
fino ad ora si lanciavano a mano uno dopo l'altro:

  1. apex7_orchestrator.py run --phase 5   -> F1 canale, F2 video sorgente, F3 script,
                                              F4 spec di produzione, F5 metadati + brief miniatura
  2. arena_thumbnail.py                    -> COPERTINA reale (Playwright su arena.ai)
  3. fliki_client.py                       -> VIDEO reale mp4 (API Fliki, consuma crediti veri)

Si ferma al primo fallimento e lo dichiara: nessun passo successivo parte su un artefatto
mancante (produrre un video da uno script che non c'e' e' peggio che non produrlo).

## Quale lavoro produce
La fabbrica NON genera il parlato a runtime — per scelta, non per limite: F3 pesca lo script
adattato scritto a mano in 05-TEMPLATES-E-KIT/script-adattati/<videoId>.md e si ferma se manca
(copiare il transcript verbatim non e' ammesso, vedi apex7_orchestrator.run_phase_3).
Quindi qui NON si sceglie un video a caso: si prende il primo lavoro **gia' pronto da produrre**
- script adattato scritto (<videoId>.md, non il brief <videoId>.DA-SCRIVERE.md)
- video sorgente presente in una cache reale (memory/channel_videos/*.json)
- non gia' prodotto (memory/video_prodotti.json, salvo qc fallito = da rilavorare)
L'ordine dei lavori sta in memory/coda_produzione.json. Se la coda e' vuota si scansiona la
cartella degli script adattati. Se non c'e' nulla di pronto lo si dice e si esce con 2: e'
lavoro di scrittura mancante, non un errore del programma.

Uso:
  python produci_video_completo.py                      # produce il prossimo lavoro pronto
  python produci_video_completo.py --preflight          # solo controlli, non spende NULLA
  python produci_video_completo.py --salta-video        # arriva alla copertina, niente Fliki
  python produci_video_completo.py --salta-copertina    # niente Arena (utile se la sessione e' scaduta)
  python produci_video_completo.py --canale legamidiamore --video-sorgente <url|videoId>

Codici di uscita: 0 fatto · 1 un passo e' fallito · 2 niente da produrre / prerequisito assente.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import shutil
import sys
import time

# Stesso trattamento degli altri script della fabbrica: senza questo, un accento nell'output
# fa crashare su cp1252, e senza line_buffering l'output rediretto (qui: la pipe di Empire
# Desk) resta invisibile per decine di minuti. reconfigure(), mai un nuovo TextIOWrapper.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
MEMORY_DIR = os.path.join(FACTORY_DIR, "memory")
TEMPLATES_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")
SCRIPT_ADATTATI_DIR = os.path.join(TEMPLATES_DIR, "script-adattati")
CHANNEL_VIDEOS_DIR = os.path.join(MEMORY_DIR, "channel_videos")
VIDEO_PRODOTTI_PATH = os.path.join(MEMORY_DIR, "video_prodotti.json")
CODA_PATH = os.path.join(MEMORY_DIR, "coda_produzione.json")
STATO_PATH = os.path.join(MEMORY_DIR, "produzione_completa_stato.json")
ARENA_PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-arena")
VIDEOS_DIR = os.path.join(FACTORY_DIR, "06-DASHBOARD-E-METRICHE", "video-generati")
# Cartella di CONSEGNA A MAX: e' qui che finisce il lavoro finito, un video per
# sottocartella (video.mp4 + copy.md + metadata.json), e Max ci mette la copertina.
VIDEO_PRONTI_DIR = os.path.join(FACTORY_DIR, "VIDEO-PRONTI")


# --------------------------------------------------------------------------- #
# Lettura stato reale (nessun valore inventato: se un file manca, si dichiara)
# --------------------------------------------------------------------------- #
def _leggi_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError, ValueError):
        return default


def scrivi_stato(fase: str, **extra) -> None:
    """Traccia leggibile dall'app (modules/yt_produzione.py) senza dover parsare il log."""
    dati = {"fase": fase, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), **extra}
    os.makedirs(MEMORY_DIR, exist_ok=True)
    with open(STATO_PATH, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def video_gia_prodotti() -> set[str]:
    """Stessa regola di Apex7Orchestrator._video_gia_prodotti: un video che ha FALLITO il
    controllo qualita' non e' 'fatto', il suo sorgente resta lavorabile."""
    prodotti = set()
    for voce in _leggi_json(VIDEO_PRODOTTI_PATH, []):
        sid = voce.get("source_video_id")
        if sid and voce.get("qc") != "fallito":
            prodotti.add(sid)
    return prodotti


def script_pronti() -> list[str]:
    """videoId con script adattato REALMENTE scritto. `<id>.DA-SCRIVERE.md` e' il brief con il
    transcript, non uno script: non conta (e' esattamente il lavoro che manca)."""
    if not os.path.isdir(SCRIPT_ADATTATI_DIR):
        return []
    out = []
    for nome in sorted(os.listdir(SCRIPT_ADATTATI_DIR)):
        if nome.endswith(".md") and not nome.endswith(".DA-SCRIVERE.md"):
            out.append(nome[:-3])
    return out


def cerca_in_cache(video_id: str) -> dict | None:
    """Il video sorgente DEVE stare in una cache reale: F2 rifiuta un URL che non c'e'
    (memory/channel_videos/*.json, scritte da youtube_hunter_playwright.py)."""
    if not os.path.isdir(CHANNEL_VIDEOS_DIR):
        return None
    for nome in os.listdir(CHANNEL_VIDEOS_DIR):
        if not nome.endswith(".json"):
            continue
        dati = _leggi_json(os.path.join(CHANNEL_VIDEOS_DIR, nome), {})
        for v in dati.get("videos", []):
            if v.get("videoId") == video_id:
                trovato = dict(v)
                trovato["canale_origine"] = dati.get("handle", nome[:-5])
                return trovato
    return None


def _estrai_video_id(testo: str) -> str:
    """Accetta sia un URL YouTube sia direttamente il videoId."""
    m = re.search(r"(?:v=|youtu\.be/|/shorts/)([\w-]{6,})", testo or "")
    if m:
        return m.group(1)
    return (testo or "").strip()


# --------------------------------------------------------------------------- #
# Scelta del lavoro
# --------------------------------------------------------------------------- #
def coda() -> dict:
    return _leggi_json(CODA_PATH, {"canale_predefinito": None, "coda": []})


def scegli_lavoro(canale_cli: str | None, sorgente_cli: str | None) -> tuple[dict | None, str]:
    """Ritorna (lavoro, motivo). lavoro = {video_id, url, canale, titolo, canale_origine}."""
    conf = coda()
    prodotti = video_gia_prodotti()
    pronti = script_pronti()

    def _componi(video_id: str, canale: str | None) -> tuple[dict | None, str]:
        if not canale:
            return None, (f"video {video_id} pronto ma canale di destinazione non indicato: "
                          f"usa --canale, oppure metti 'canale' nella voce di {CODA_PATH}")
        in_cache = cerca_in_cache(video_id)
        if not in_cache:
            return None, (f"video sorgente {video_id} non presente in nessuna cache reale "
                          f"({CHANNEL_VIDEOS_DIR}). F2 lo rifiuterebbe. Lancia prima "
                          f"youtube_hunter_playwright.py sul canale di origine.")
        return {
            "video_id": video_id,
            "url": in_cache.get("url") or f"https://www.youtube.com/watch?v={video_id}",
            "canale": canale,
            "titolo": in_cache.get("title", ""),
            "canale_origine": in_cache.get("canale_origine", "?"),
        }, "scelto"

    # 1) richiesta esplicita da riga di comando: vince sempre, anche se gia' prodotto
    #    (rilavorazione voluta) — ma lo script adattato deve esserci comunque.
    if sorgente_cli:
        vid = _estrai_video_id(sorgente_cli)
        if vid not in pronti:
            return None, (f"nessuno script adattato per {vid}: serve "
                          f"{os.path.join(SCRIPT_ADATTATI_DIR, vid + '.md')} (scritto a mano). "
                          f"F3 si fermerebbe qui.")
        return _componi(vid, canale_cli or conf.get("canale_predefinito"))

    # 2) coda esplicita
    for voce in conf.get("coda", []):
        vid = _estrai_video_id(voce.get("video_sorgente_id") or voce.get("video_sorgente") or "")
        if not vid or vid in prodotti or vid not in pronti:
            continue
        return _componi(vid, canale_cli or voce.get("canale") or conf.get("canale_predefinito"))

    # 3) scansione: primo script pronto non ancora prodotto
    for vid in pronti:
        if vid in prodotti:
            continue
        return _componi(vid, canale_cli or conf.get("canale_predefinito"))

    da_scrivere = []
    if os.path.isdir(SCRIPT_ADATTATI_DIR):
        da_scrivere = sorted(n for n in os.listdir(SCRIPT_ADATTATI_DIR)
                             if n.endswith(".DA-SCRIVERE.md"))
    return None, ("nessun lavoro pronto: ogni script adattato risulta gia' prodotto.\n"
                  f"    Brief con il transcript reale in attesa di scrittura: "
                  f"{', '.join(da_scrivere) if da_scrivere else 'nessuno'}\n"
                  "    Scrivi lo script (o lancia una nuova selezione video) e ripremi il pulsante.")


# --------------------------------------------------------------------------- #
# Prerequisiti — controllati PRIMA di spendere (Mandato Art.4.3: dry-run prima di spendere)
# --------------------------------------------------------------------------- #
def _chiave_fliki_presente() -> bool:
    if os.environ.get("FLIKI_API_KEY"):
        return True
    env_path = os.path.join(FACTORY_DIR, ".env")
    if not os.path.exists(env_path):
        return False
    for riga in open(env_path, encoding="utf-8"):
        if riga.strip().startswith("FLIKI_API_KEY=") and riga.strip().split("=", 1)[1].strip():
            return True
    return False


def preflight(lavoro: dict | None, motivo: str, salta_copertina: bool, salta_video: bool) -> bool:
    print("=== PREFLIGHT — controlli, nessuna spesa ===")
    ok = True

    if lavoro:
        print(f"[✓] Lavoro pronto: {lavoro['video_id']} — \"{lavoro['titolo'][:70]}\"")
        print(f"    sorgente: {lavoro['canale_origine']} · destinazione: {lavoro['canale']}")
        print(f"    script:   {os.path.join(SCRIPT_ADATTATI_DIR, lavoro['video_id'] + '.md')}")
    else:
        print(f"[✗] Nessun lavoro producibile — {motivo}")
        ok = False

    if salta_copertina:
        print("[–] Copertina: la fa Max a mano (default). Lo script si ferma al video "
              "e consegna cartella + titolo + indicazioni.")
    else:
        try:
            import playwright  # noqa: F401
            print("[✓] Playwright installato (copertina Arena)")
        except ImportError:
            print("[✗] Playwright NON installato: la copertina non puo' partire "
                  "(pip install playwright && playwright install chromium)")
            ok = False
        if os.path.isdir(ARENA_PROFILE_DIR):
            print(f"[✓] Profilo Arena presente: {ARENA_PROFILE_DIR}")
        else:
            print(f"[✗] Profilo Arena assente ({ARENA_PROFILE_DIR}): serve un login manuale "
                  f"una tantum → python arena_thumbnail.py --visibile")
            ok = False

    if salta_video:
        print("[–] Video saltato su richiesta (--salta-video)")
    elif _chiave_fliki_presente():
        print("[✓] FLIKI_API_KEY trovata (il video consumera' crediti Fliki reali)")
    else:
        print("[✗] FLIKI_API_KEY assente (ne' in ambiente ne' in .env): il video non puo' partire")
        ok = False

    print(f"=== PREFLIGHT: {'OK' if ok else 'BLOCCATO'} ===")
    return ok


# --------------------------------------------------------------------------- #
# Esecuzione dei passi reali
# --------------------------------------------------------------------------- #
def esegui(nome: str, argv: list[str]) -> int:
    """Lancia un passo reale inoltrando il suo output riga per riga (il pannello di Aureus
    mostra il log live: senza inoltro si vedrebbe una barra ferma per 40 minuti)."""
    print(f"\n{'=' * 70}\n▶ {nome}\n  $ {' '.join(argv[1:])}\n{'=' * 70}", flush=True)
    env = dict(os.environ, PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
    proc = subprocess.Popen(argv, cwd=SCRIPT_DIR, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                            text=True, bufsize=1, encoding="utf-8", errors="replace", env=env)
    assert proc.stdout is not None
    for riga in proc.stdout:
        print(riga.rstrip(), flush=True)
    code = proc.wait()
    print(f"◀ {nome}: exit {code}", flush=True)
    return code


def _slug(testo: str, fallback: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (testo or "").lower()).strip("-")[:60]
    return s or fallback


def _prossima_cartella_pronti() -> str:
    """VIDEO-PRONTI/video-NN progressivo, il primo numero libero."""
    os.makedirs(VIDEO_PRONTI_DIR, exist_ok=True)
    usati = []
    for nome in os.listdir(VIDEO_PRONTI_DIR):
        if nome.startswith("video-") and nome[6:].isdigit():
            usati.append(int(nome[6:]))
    return os.path.join(VIDEO_PRONTI_DIR, "video-%02d" % ((max(usati) + 1) if usati else 1))


def consegna_a_max(mp4: str, titolo: str, lavoro: dict) -> str | None:
    """Il pezzo che finora NON esisteva nel codice e veniva rifatto a mano ogni volta con
    script usa-e-getta (_finish_video02.py, _resume_video05_*.py ...): mettere il lavoro
    finito nella cartella dedicata del video, con dentro tutto tranne la copertina.

    REGOLA PERMANENTE DI MAX: la copertina la fa lui. Qui si consegna
    video.mp4 + copy.md + metadata.json in VIDEO-PRONTI/video-NN/, si apre la cartella, e ci
    si ferma. L'upload e' un atto separato, dopo che Max ha messo il .png dentro.
    """
    if not os.path.exists(mp4):
        print("[!] Consegna saltata: l'mp4 non esiste sul disco.")
        return None

    meta = _leggi_json(os.path.join(TEMPLATES_DIR, "metadati.json"), {})
    dest = _prossima_cartella_pronti()
    os.makedirs(dest, exist_ok=True)
    shutil.copy2(mp4, os.path.join(dest, "video.mp4"))

    with open(os.path.join(dest, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    titolo_finale = meta.get("title") or titolo
    tags = meta.get("tags") or []
    righe = [
        "# Copy - %s (%s)" % (os.path.basename(dest), lavoro.get("canale", "")),
        "",
        "**Fonte:** %s (%s) -> canale %s" % (lavoro.get("video_id", ""),
                                             lavoro.get("canale_origine", ""),
                                             lavoro.get("canale", "")),
        "**Generato via:** fliki_client.py (API reale)",
        "",
        "## Title",
        titolo_finale,
        "",
        "## Description",
        meta.get("description", ""),
        "",
        "## Tags",
        ", ".join(tags),
        "",
        "## Copertina - LA FA MAX (brief completo, da consegnare SEMPRE senza che lo chieda)",
        "",
        '**Titolo:** "%s"' % titolo_finale,
        "**Formato:** 16:9, stampo Legami d'Amore, testo oro/ambra.",
        "**Leggibilita':** il titolo deve leggersi anche in miniatura piccola.",
        "**Dove:** il file .png va messo dentro questa stessa cartella.",
        "**Dopo:** upload in privato con le pubblicita' attive.",
        "",
        "## Upload",
        "Quando la copertina e' in cartella, l'upload parte con:",
        "  python youtube_uploader_playwright.py --video <cartella>/video.mp4 \\",
        "      --thumbnail <cartella>/<copertina>.png --privato",
        "",
    ]
    with open(os.path.join(dest, "copy.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(righe))

    print("\n" + "=" * 70)
    print("CONSEGNATO A MAX")
    print("=" * 70)
    print("  Cartella:  %s" % dest)
    print("  Dentro:    video.mp4 - copy.md - metadata.json")
    print("")
    print("  --- BRIEF COPERTINA PER MAX (la fa lui, sempre) ---")
    print("  Titolo:    %s" % titolo_finale)
    print("  Formato:   16:9, stampo Legami d'Amore, testo oro/ambra")
    print("  Leggibile: il titolo deve leggersi anche in miniatura piccola")
    print("  Dove:      il .png va messo in questa stessa cartella")
    print("  Poi:       avvisa e parte l'upload in privato con le pubblicita' attive")
    try:
        subprocess.Popen(["explorer", dest])
    except OSError:
        pass
    return dest

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Produce video + copertina in un colpo solo, dalla catena reale della fabbrica.")
    ap.add_argument("--preflight", action="store_true",
                    help="Solo controlli: dice cosa produrrebbe e cosa manca. Non spende nulla.")
    ap.add_argument("--canale", default=None,
                    help="Canale di DESTINAZIONE (es. legamidiamore, dosementale). "
                         "Default: quello della voce in coda / canale_predefinito.")
    ap.add_argument("--video-sorgente", default=None,
                    help="URL o videoId da replicare, invece del prossimo lavoro in coda.")
    ap.add_argument("--salta-copertina", action="store_true",
                    help="(ormai ridondante) Non generare la copertina. E' gia' il comportamento "
                         "di default: la copertina la fa Max a mano.")
    ap.add_argument("--con-copertina", action="store_true",
                    help="ORDINE ESPLICITO DI MAX RICHIESTO. Genera la copertina via Arena. "
                         "REGOLA PERMANENTE (Max, 2026-08-29 e ribadita 2026-09-04): la copertina "
                         "la fa SEMPRE Max a mano, mai la macchina. Il compito dello script e' "
                         "fermarsi al video e consegnare cartella + titolo + due righe di indicazioni.")
    ap.add_argument("--salta-video", action="store_true", help="Non generare il video (niente crediti Fliki).")
    ap.add_argument("--visuals", choices=["ai", "stock"], default="ai",
                    help="Passato a fliki_client.py (default: ai, come in produzione).")
    args = ap.parse_args()

    # REGOLA PERMANENTE DI MAX: la copertina la fa lui, a mano. Il default e' quindi
    # "niente Arena", e per generarla serve un ordine esplicito (--con-copertina).
    # Prima questo era invertito e la macchina ci provava da sola: e' stato un errore
    # ripetuto, corretto qui alla radice invece che nella memoria di chi lancia lo script.
    if not args.con_copertina:
        args.salta_copertina = True

    print(f"🏭 YouTube Automation Factory — produzione completa · {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lavoro, motivo = scegli_lavoro(args.canale, args.video_sorgente)

    if args.preflight:
        return 0 if preflight(lavoro, motivo, args.salta_copertina, args.salta_video) else 2

    if not lavoro:
        print(f"\n[!] NIENTE DA PRODURRE — {motivo}")
        scrivi_stato("niente_da_produrre", motivo=motivo)
        return 2

    if not preflight(lavoro, motivo, args.salta_copertina, args.salta_video):
        print("\n[!] Prerequisiti mancanti: non parte niente (meglio fermarsi qui che a meta' spesa).")
        scrivi_stato("preflight_fallito", video_id=lavoro["video_id"])
        return 2

    scrivi_stato("avviato", video_id=lavoro["video_id"], titolo=lavoro["titolo"],
                 canale=lavoro["canale"])

    # --- Passo 1: F1→F5 (canale, video, script, spec di produzione, metadati + brief miniatura)
    code = esegui("F1→F5 — orchestratore APEX-7", [
        sys.executable, os.path.join(SCRIPT_DIR, "apex7_orchestrator.py"), "run",
        "--phase", "5", "--canale", lavoro["canale"], "--video-sorgente", lavoro["url"],
    ])
    if code != 0:
        print("\n[!] La catena si ferma qui: senza gli artefatti di F1-F5 (script.md, "
              "produzione-spec.json, brief-miniatura.json) copertina e video non hanno da "
              "cosa nascere. Il motivo esatto e' nel log qui sopra.")
        scrivi_stato("fallito", passo="orchestratore", exit_code=code, video_id=lavoro["video_id"])
        return 1

    spec = _leggi_json(os.path.join(TEMPLATES_DIR, "produzione-spec.json"), {})
    titolo_nostro = spec.get("title", lavoro["titolo"])
    nome_file = _slug(spec.get("video_id") or titolo_nostro, f"video-{lavoro['video_id']}")

    # --- Passo 2: copertina reale
    copertina_ok = None
    if not args.salta_copertina:
        scrivi_stato("copertina", video_id=lavoro["video_id"], titolo=titolo_nostro)
        code = esegui("COPERTINA — Arena (Playwright)",
                      [sys.executable, os.path.join(SCRIPT_DIR, "arena_thumbnail.py")])
        copertina_ok = code == 0
        if not copertina_ok:
            print("\n[!] Copertina non generata. Il video NON parte: pubblicare un video senza "
                  "miniatura adattata e' fuori standard. Se la sessione Arena e' scaduta: "
                  "python arena_thumbnail.py --visibile (login una tantum), poi ripremi il pulsante. "
                  "Per produrre comunque solo il video: --salta-copertina.")
            scrivi_stato("fallito", passo="copertina", exit_code=code, video_id=lavoro["video_id"])
            return 1

    # --- Passo 3: video reale (crediti Fliki veri)
    if args.salta_video:
        print("\n[–] Video saltato su richiesta (--salta-video).")
        scrivi_stato("completato_senza_video", video_id=lavoro["video_id"], titolo=titolo_nostro)
        return 0

    scrivi_stato("video", video_id=lavoro["video_id"], titolo=titolo_nostro, file=nome_file)
    # BUG REALE trovato 2026-08-29: --canale non veniva inoltrato a fliki_client.py, che
    # ricadeva sul suo default "dosementale" (voce MASCHILE) anche quando lavoro["canale"] era
    # "legamidiamore" (voce femminile richiesta) — un video con voce sbagliata generato per
    # davvero prima che la run fallisse per un problema di rete separato.
    code = esegui("VIDEO — Fliki (API reale, consuma crediti)", [
        sys.executable, os.path.join(SCRIPT_DIR, "fliki_client.py"),
        "--file-name", nome_file, "--visuals", args.visuals, "--canale", lavoro["canale"],
    ])
    if code != 0:
        print("\n[!] Video non prodotto. La copertina generata resta valida: "
              "ripremendo il pulsante con --salta-copertina non la si rigenera inutilmente.")
        scrivi_stato("fallito", passo="video", exit_code=code, video_id=lavoro["video_id"])
        return 1

    mp4 = os.path.join(VIDEOS_DIR, f"{nome_file}.mp4")
    stato_arena = _leggi_json(os.path.join(MEMORY_DIR, "arena_thumbnail_status.json"), {})
    copertine = stato_arena.get("immagini_salvate") or []

    print(f"\n{'=' * 70}\n🎉 FATTO — video + copertina prodotti davvero\n{'=' * 70}")
    print(f"  Titolo:    {titolo_nostro}")
    print(f"  Sorgente:  {lavoro['video_id']} ({lavoro['canale_origine']}) → canale {lavoro['canale']}")
    print(f"  Video:     {mp4}"
          f"{'' if os.path.exists(mp4) else '  [!] file non trovato sul disco: controlla il log Fliki'}")
    if os.path.exists(mp4):
        print(f"             {os.path.getsize(mp4) / 1_000_000:.1f} MB")
    print(f"  Copertina: {', '.join(copertine) if copertine else '(nessuna: passo saltato)'}")
    print("  Pubblicazione su YouTube: NON fatta da qui — resta un atto separato e voluto.")
    cartella = consegna_a_max(mp4, titolo_nostro, lavoro)
    scrivi_stato("completato", video_id=lavoro["video_id"], titolo=titolo_nostro,
                 video=mp4, copertine=copertine, cartella_consegna=cartella)
    return 0


if __name__ == "__main__":
    sys.exit(main())
