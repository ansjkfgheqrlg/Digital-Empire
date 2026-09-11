#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
carica_pronti.py — il pezzo che guarda VIDEO-PRONTI/ e si accorge da solo di quali cartelle
sono davvero pronte al caricamento (A7, colma il buco trovato dal vivo il 2026-09-11).

IL PROBLEMA (misurato il 2026-09-11): VIDEO-PRONTI/video-01 .. video-07 avevano video.mp4,
copy.md/metadata.json e la copertina messa a mano da Max — e nessuno risultava caricato su
YouTube. Il flusso in .claude/commands/avvia-yt.md §6 dice di lanciare A MANO, un video alla
volta:

    python apex7_orchestrator.py run --canale <canale> --phase 5 --upload \
        --video-folder ../VIDEO-PRONTI/video-NN --skip-thumbnail

Max aveva messo 7 copertine, nessuno aveva lanciato 7 comandi. Non mancava la disciplina:
mancava il pezzo che guarda le cartelle e se ne accorge. Questo file e' quel pezzo.

QUESTO FILE NON REINVENTA L'UPLOAD. Non tocca apex7_orchestrator.py ne'
youtube_uploader_playwright.py: per ogni cartella pronta lancia ESATTAMENTE il comando
documentato sopra via subprocess, uno alla volta.

AVVISO IMPORTANTE PER CHI USA QUESTO SCRIPT IN PRODUZIONE (letto nel codice di
apex7_orchestrator.py, non un'illazione): il comando documentato in avvia-yt.md §6 NON passa
--resume ne' --run-id. Senza questi due, Apex7Orchestrator parte con working_memory vuota
(current_phase=1) e execute_workflow() esegue le fasi 1-4 DA CAPO (nuova selezione video,
nuovo script, nuovi metadati) prima di arrivare alla fase 5 — i metadati usati per l'upload
sono quelli generati da QUESTA nuova run, non necessariamente quelli scritti nel metadata.json
della cartella. Il file mp4/copertina caricati sono invece sempre quelli della cartella
(--video-folder li sceglie esplicitamente). Questo script non lo corregge (fuori perimetro:
non tocca l'orchestratore) — lo segnala qui e nel report finale, cosi' chi decide sa cosa sta
lanciando.

IL CASO "BOZZA" (scoperto dal vivo il 2026-09-11): YouTube Studio puo' lasciare il video in
stato di BOZZA ("This video is in a draft state"), non in privato — nessun pezzo del codice
esistente (youtube_uploader_playwright.py, apex7_orchestrator.py) rileva o riporta questo
stato oggi (verificato: zero occorrenze di "draft"/"bozza" in entrambi). Questo script prova a
leggerlo comunque dall'output testuale del comando lanciato (best-effort, vedi
_stato_osservato_da_testo) e lo riporta SEMPRE nel log e a schermo quando lo trova, cosi' si
sa se serve ancora un passaggio manuale.

Un video e' "pronto" quando la sua cartella ha: video.mp4, metadata.json, almeno un'immagine
.png/.jpg/.jpeg/.webp (la copertina di Max), e metadata.json NON ha ancora un campo
"youtube_id" (scritto da QUESTO script dopo un upload riuscito — ne' apex7_orchestrator.py ne'
youtube_uploader_playwright.py scrivono l'esito dell'upload nel metadata.json della cartella:
registrano solo il video_id ottenuto in youtube_uploader_playwright.py -> stdout "Risultato:
{...}" -> apex7_orchestrator.py legge quella riga a runtime, riga ~1620, e lo registra in
memory/published_videos.json indicizzato per run_id, MAI nel metadata.json della cartella
video. Senza una scrittura propria qui, un video gia' caricato tornerebbe "pronto" al giro
dopo: un doppio caricamento e' un duplicato sul canale, va impedito).

IL CANALE non si indovina: si legge da metadata.json (campo canale/channel/canale_id, se
presente) o dal testo di copy.md, cercando i marcatori dei canali noti (vedi CANALE_MARCATORI,
che rispecchia CANALI in apex7_orchestrator.py: "legamidiamore", "dosementale"). Se non si
trova un canale univoco, la cartella viene SALTATA e segnalata — mai indovinata: caricare un
video sul canale sbagliato e' peggio che non caricarlo.

TRE PROTEZIONI NON NEGOZIABILI:
  1. --prova (dry-run) e' il comportamento di default. Senza --conferma esplicito lo script
     elenca cosa caricherebbe e non lancia NIENTE.
  2. Un video alla volta, in ordine di anzianita' (il piu' vecchio prima, per mtime di
     video.mp4), e si ferma al primo fallimento invece di continuare a mitraglia.
  3. Ogni esecuzione scrive nel log (memory/carica_pronti.log) in append: data, cartella,
     canale, esito, id YouTube ottenuto, stato osservato. Anche le prove.

Console Windows cp1252: NIENTE EMOJI nell'output di questo script.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

# Stessa soluzione gia' in uso in apex7_orchestrator.py e pubblica_video.py per lo stesso
# problema (console Windows cp1252 che esplode su caratteri fuori tabella, es. le emoji che
# apex7_orchestrator.py stampa nel proprio output catturato qui sotto).
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
VIDEO_PRONTI_DIR = os.path.join(FACTORY_DIR, "VIDEO-PRONTI")
DEFAULT_LOG = os.path.join(FACTORY_DIR, "memory", "carica_pronti.log")
ORCHESTRATOR_FILE = "apex7_orchestrator.py"
TIMEOUT_SECONDI = 3600  # 1h: la fase 5 senza --resume puo' rieseguire le fasi 1-4 (vedi sopra)

IMMAGINE_EXT = (".png", ".jpg", ".jpeg", ".webp")

# Canali validi = chiavi di CANALI in apex7_orchestrator.py. Marcatori testuali con cui li si
# riconosce dentro metadata.json/copy.md — mai un elenco che "indovina" un canale non elencato.
CANALE_MARCATORI = (
    ("legamidiamore", "legamidiamore"),
    ("legami d'amore", "legamidiamore"),
    ("legami d’amore", "legamidiamore"),
    ("@legamidiamore", "legamidiamore"),
    ("dosementale", "dosementale"),
    ("dose mentale", "dosementale"),
    ("@dosementale", "dosementale"),
)

# Frasi che rivelano lo STATO in cui l'uploader ha lasciato il video, quando lo dice
# nell'output catturato. Best-effort: nessun pezzo del codice a monte struttura oggi questo
# dato (vedi nota "IL CASO BOZZA" in testa al file), quindi si cerca nel testo grezzo.
STATO_MARCATORI = (
    ("draft state", "BOZZA (draft) - serve un passaggio manuale su YouTube Studio"),
    ("in draft", "BOZZA (draft) - serve un passaggio manuale su YouTube Studio"),
    ("bozza", "BOZZA - serve un passaggio manuale su YouTube Studio"),
    ("still uploading", "upload ancora in corso quando il browser si e' fermato"),
    ("ancora caricando", "upload ancora in corso quando il browser si e' fermato"),
    ("pending", "IN ELABORAZIONE (pending) su YouTube Studio"),
    ("in elaborazione", "IN ELABORAZIONE su YouTube Studio"),
    ("id_non_estratto", "salvato ma id reale non estratto dall'URL - verificare a mano"),
)

RE_VIDEO_CARTELLA = re.compile(r"^video-(\d+)$", re.IGNORECASE)
RE_WATCH_URL = re.compile(r"https?://www\.youtube\.com/watch\?v=([\w-]+)")


# ---------------------------------------------------------------------------------------
# Lettura cartelle — funzioni pure, nessuna rete, nessun subprocess.
# ---------------------------------------------------------------------------------------

def trova_cartelle_video(video_pronti_dir):
    """Elenco delle sottocartelle video-NN, ordinate per numero (solo per la stampa del
    quadro completo — l'ordine di CARICAMENTO e' un'altra cosa, vedi ordina_per_anzianita)."""
    if not os.path.isdir(video_pronti_dir):
        return []
    trovate = []
    for nome in os.listdir(video_pronti_dir):
        percorso = os.path.join(video_pronti_dir, nome)
        if os.path.isdir(percorso) and RE_VIDEO_CARTELLA.match(nome):
            trovate.append((int(RE_VIDEO_CARTELLA.match(nome).group(1)), nome, percorso))
    trovate.sort(key=lambda t: t[0])
    return [(nome, percorso) for _, nome, percorso in trovate]


def _leggi_metadata(percorso_metadata):
    """Ritorna (dict, errore). errore e' None se tutto ok, o una stringa se il file manca o
    non e' JSON valido (mai un'eccezione che scoppia in faccia al chiamante)."""
    if not os.path.exists(percorso_metadata):
        return {}, "manca metadata.json"
    try:
        with open(percorso_metadata, "r", encoding="utf-8") as f:
            return json.load(f), None
    except (json.JSONDecodeError, ValueError) as e:
        return {}, "metadata.json non e' JSON valido: %s" % e


def _trova_immagine(cartella):
    """Prima immagine (ordine alfabetico, deterministico) trovata nella cartella, o None."""
    if not os.path.isdir(cartella):
        return None
    for nome in sorted(os.listdir(cartella)):
        if nome.lower().endswith(IMMAGINE_EXT):
            return nome
    return None


def _leggi_copy_md(cartella):
    percorso = os.path.join(cartella, "copy.md")
    if not os.path.exists(percorso):
        return ""
    try:
        with open(percorso, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def rileva_canale(metadata, testo_copy_md):
    """Canale letto da metadata.json (campo canale/channel/canale_id) o dal testo di
    copy.md, cercando i marcatori noti. Ritorna l'id canale (es. 'legamidiamore') o None se
    non si trova un riferimento univoco — MAI un indovinato per esclusione."""
    candidati = set()

    for chiave in ("canale", "channel", "canale_id", "canale_target"):
        valore = metadata.get(chiave)
        if isinstance(valore, str) and valore.strip():
            valore_l = valore.strip().lower()
            for marcatore, canale_id in CANALE_MARCATORI:
                if marcatore in valore_l:
                    candidati.add(canale_id)

    testo_l = (testo_copy_md or "").lower()
    for marcatore, canale_id in CANALE_MARCATORI:
        if marcatore in testo_l:
            candidati.add(canale_id)

    if len(candidati) == 1:
        return next(iter(candidati))
    return None  # 0 o >1 candidati: non si indovina


def analizza_cartella(nome, cartella):
    """Analizza UNA cartella video-NN e ritorna un dizionario con lo stato reale trovato sul
    disco. Non lancia mai eccezioni per condizioni attese (file mancanti): le riporta come
    stato, cosi' il chiamante puo' mostrare il quadro completo anche per le cartelle scartate."""
    video_path = os.path.join(cartella, "video.mp4")
    metadata_path = os.path.join(cartella, "metadata.json")

    ha_video = os.path.exists(video_path)
    metadata, errore_metadata = _leggi_metadata(metadata_path)
    immagine = _trova_immagine(cartella)
    testo_copy_md = _leggi_copy_md(cartella)
    titolo = metadata.get("title") or metadata.get("titolo") or ""
    youtube_id_esistente = metadata.get("youtube_id")

    esito = {
        "nome": nome,
        "cartella": cartella,
        "video_path": video_path,
        "metadata_path": metadata_path,
        "ha_video": ha_video,
        "ha_metadata": errore_metadata is None,
        "errore_metadata": errore_metadata,
        "immagine": immagine,
        "titolo": titolo,
        "youtube_id_esistente": youtube_id_esistente,
        "canale": None,
        "mtime_video": os.path.getmtime(video_path) if ha_video else None,
    }

    if not ha_video:
        esito["stato"] = "manca_video"
        esito["motivo"] = "manca video.mp4"
        return esito
    if errore_metadata is not None:
        esito["stato"] = "manca_metadata"
        esito["motivo"] = errore_metadata
        return esito
    if not immagine:
        esito["stato"] = "manca_copertina"
        esito["motivo"] = "nessuna copertina (.png/.jpg/.jpeg/.webp) nella cartella"
        return esito
    if youtube_id_esistente:
        esito["stato"] = "gia_caricato"
        esito["canale"] = rileva_canale(metadata, testo_copy_md)
        esito["motivo"] = "gia' caricato (youtube_id=%s in metadata.json)" % youtube_id_esistente
        return esito

    canale = rileva_canale(metadata, testo_copy_md)
    esito["canale"] = canale
    if not canale:
        esito["stato"] = "canale_sconosciuto"
        esito["motivo"] = ("canale non riconosciuto: manca in metadata.json (campo "
                            "canale/channel) e non c'e' un marcatore univoco in copy.md — "
                            "non indovino, va reso esplicito a mano")
        return esito

    esito["stato"] = "pronto"
    esito["motivo"] = "video.mp4 + metadata.json + copertina, canale=%s, mai caricato" % canale
    return esito


def costruisci_report(video_pronti_dir):
    """Analisi di TUTTE le cartelle video-NN trovate (anche quelle scartate: il quadro
    completo serve a Max per sapere cosa manca, non solo cosa e' pronto)."""
    return [analizza_cartella(nome, cartella)
            for nome, cartella in trova_cartelle_video(video_pronti_dir)]


def ordina_per_anzianita(report):
    """Solo le cartelle 'pronto', dalla piu' vecchia (mtime di video.mp4 piu' basso) alla piu'
    recente — cosi' chi aspetta da piu' tempo (18gg nel caso misurato) parte per primo."""
    pronte = [r for r in report if r["stato"] == "pronto"]
    return sorted(pronte, key=lambda r: r["mtime_video"])


def eta_giorni(mtime, adesso=None):
    adesso = adesso if adesso is not None else datetime.now().timestamp()
    return round((adesso - mtime) / 86400.0, 1)


# ---------------------------------------------------------------------------------------
# Esecuzione del comando documentato — subprocess isolato in una funzione sola, cosi' i
# test possono sostituirlo via monkeypatch senza toccare la rete o un browser vero.
# ---------------------------------------------------------------------------------------

def costruisci_comando(cartella, canale, script_dir=SCRIPT_DIR):
    """Il comando ESATTO documentato in avvia-yt.md paragrafo 6, un solo cambio per
    variabile (--canale, --video-folder): non si reinventa l'upload."""
    rel = os.path.relpath(cartella, start=script_dir)
    return [sys.executable, ORCHESTRATOR_FILE, "run", "--canale", canale,
            "--phase", "5", "--upload", "--video-folder", rel, "--skip-thumbnail"]


def esegui_comando(cmd, script_dir=SCRIPT_DIR, timeout=TIMEOUT_SECONDI):
    """Unico punto che chiama subprocess.run — i test sostituiscono `subprocess.run` con un
    doppio via monkeypatch, non c'e' nessun'altra chiamata al processo reale nel modulo."""
    try:
        return subprocess.run(cmd, cwd=script_dir, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired as e:
        classe = subprocess.CompletedProcess
        return classe(cmd, returncode=124, stdout=e.stdout or "",
                       stderr="timeout dopo %ds: %s" % (timeout, e))
    except OSError as e:
        classe = subprocess.CompletedProcess
        return classe(cmd, returncode=1, stdout="", stderr="impossibile avviare il comando: %s" % e)


def estrai_video_id_e_url(testo):
    """Ultima occorrenza di un URL watch?v= nell'output combinato: e' quella scritta dal
    messaggio finale di successo di apex7_orchestrator.py ('Upload reale completato — <url>')."""
    match_finali = RE_WATCH_URL.findall(testo or "")
    if not match_finali:
        return None, None
    video_id = match_finali[-1]
    return video_id, "https://www.youtube.com/watch?v=%s" % video_id


def stato_osservato_da_testo(testo):
    """Best-effort: cerca nel testo grezzo dell'output catturato una frase che riveli lo
    stato in cui l'uploader ha lasciato il video (bozza/pending/ecc — vedi nota in testa al
    file). Ritorna la prima descrizione trovata, o None se non c'e' nessun marcatore noto."""
    testo_l = (testo or "").lower()
    for marcatore, descrizione in STATO_MARCATORI:
        if marcatore in testo_l:
            return descrizione
    return None


def aggiorna_metadata_con_id(metadata_path, video_id, url):
    """Scrive youtube_id/caricato_il/youtube_url nel metadata.json della cartella, dopo un
    upload riuscito — cosi' il prossimo giro non lo trova piu' 'pronto' e non lo ricarica.
    Nessuno a monte scrive questo dato nel metadata.json della cartella (vedi nota in testa
    al file): senza questa scrittura, un doppio caricamento e' garantito al giro successivo."""
    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)
    metadata["youtube_id"] = video_id
    metadata["youtube_url"] = url
    metadata["caricato_il"] = datetime.now().isoformat()
    with open(metadata_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
        f.write("\n")


# ---------------------------------------------------------------------------------------
# Log in append — stesso stile a colonne di pubblica_video.py (memory/pubblicazioni.log).
# ---------------------------------------------------------------------------------------

def scrivi_log(cartella_nome, canale, esito, youtube_id="", stato_osservato="", dettaglio="",
               log_path=DEFAULT_LOG):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    riga = "%s | cartella=%s | canale=%s | esito=%s | youtube_id=%s | stato=%s | %s\n" % (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        cartella_nome, canale or "?", esito, youtube_id or "-", stato_osservato or "-",
        (dettaglio or "").replace("\n", " "),
    )
    with open(log_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(riga)
    return riga


# ---------------------------------------------------------------------------------------
# Orchestrazione — la funzione che il main() chiama, e che i test chiamano direttamente
# passando cartelle temporanee e un log temporaneo.
# ---------------------------------------------------------------------------------------

def esegui(video_pronti_dir=VIDEO_PRONTI_DIR, log_path=DEFAULT_LOG, conferma=False,
           script_dir=SCRIPT_DIR, timeout=TIMEOUT_SECONDI, stampa=print):
    report = costruisci_report(video_pronti_dir)

    stampa("=" * 78)
    stampa("CARICA PRONTI -- scansione di %s" % video_pronti_dir)
    stampa("Modalita'  : %s" % ("REALE (carica davvero, un video alla volta)" if conferma
                                 else "PROVA (dry-run, nessun comando lanciato)"))
    stampa("Log        : %s" % log_path)
    stampa("=" * 78)

    if not report:
        stampa("Nessuna cartella video-NN trovata in %s." % video_pronti_dir)
        return 0

    for r in report:
        if r["stato"] == "pronto":
            stampa("[PRONTO]   %s -- canale=%s, eta=%.1fg -- %s"
                   % (r["nome"], r["canale"], eta_giorni(r["mtime_video"]), r["titolo"] or "(senza titolo)"))
        elif r["stato"] == "gia_caricato":
            stampa("[FATTO]    %s -- %s" % (r["nome"], r["motivo"]))
        else:
            stampa("[SALTATO]  %s -- %s" % (r["nome"], r["motivo"]))

    candidati = ordina_per_anzianita(report)
    if not candidati:
        stampa("")
        stampa("Nessun video pronto al caricamento (vedi motivi sopra).")
        return 0

    stampa("")
    stampa("%d video pronti, in ordine di anzianita' (il piu' vecchio prima):" % len(candidati))
    for r in candidati:
        stampa("  - %s (eta=%.1fg, canale=%s)" % (r["nome"], eta_giorni(r["mtime_video"]), r["canale"]))

    if not conferma:
        stampa("")
        stampa("PROVA: nessun comando lanciato. Rilancia con --conferma per caricare davvero,")
        stampa("un video alla volta, fermandosi al primo fallimento.")
        for r in candidati:
            cmd = costruisci_comando(r["cartella"], r["canale"], script_dir=script_dir)
            scrivi_log(r["nome"], r["canale"], "PROVA", dettaglio=" ".join(cmd), log_path=log_path)
        return 0

    stampa("")
    codice_uscita = 0
    for r in candidati:
        cmd = costruisci_comando(r["cartella"], r["canale"], script_dir=script_dir)
        stampa("-" * 78)
        stampa("CARICO %s (canale=%s) -- comando:" % (r["nome"], r["canale"]))
        stampa("  %s" % " ".join(cmd))

        risultato = esegui_comando(cmd, script_dir=script_dir, timeout=timeout)
        testo_completo = (risultato.stdout or "") + "\n" + (risultato.stderr or "")
        stato_osservato = stato_osservato_da_testo(testo_completo)

        if risultato.returncode != 0:
            dettaglio = "returncode=%s" % risultato.returncode
            stampa("[FALLITO] %s -- %s" % (r["nome"], dettaglio))
            if stato_osservato:
                stampa("          stato osservato nell'output: %s" % stato_osservato)
            scrivi_log(r["nome"], r["canale"], "FALLITO", stato_osservato=stato_osservato or "",
                       dettaglio=dettaglio, log_path=log_path)
            stampa("Mi fermo qui: uno per volta, niente mitraglia dopo un fallimento.")
            codice_uscita = 1
            break

        video_id, url = estrai_video_id_e_url(testo_completo)
        if not video_id:
            dettaglio = ("returncode 0 ma nessun id YouTube trovato nell'output -- non scrivo "
                          "nulla in metadata.json per evitare un doppio caricamento al prossimo "
                          "giro. Verifica a mano su YouTube Studio prima di rilanciare.")
            stampa("[FALLITO] %s -- %s" % (r["nome"], dettaglio))
            scrivi_log(r["nome"], r["canale"], "FALLITO", stato_osservato=stato_osservato or "",
                       dettaglio=dettaglio, log_path=log_path)
            codice_uscita = 1
            break

        aggiorna_metadata_con_id(r["metadata_path"], video_id, url)
        stampa("[OK]      %s -- caricato, id=%s, url=%s" % (r["nome"], video_id, url))
        if stato_osservato:
            stampa("          stato osservato nell'output: %s" % stato_osservato)
        scrivi_log(r["nome"], r["canale"], "OK", youtube_id=video_id,
                   stato_osservato=stato_osservato or "", dettaglio=url, log_path=log_path)

    return codice_uscita


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Scansiona VIDEO-PRONTI/, trova i video con copertina pronti al "
                     "caricamento (video.mp4 + metadata.json + copertina + mai caricato) e "
                     "lancia per ognuno il comando documentato in avvia-yt.md par.6 "
                     "(apex7_orchestrator.py --upload) -- riusa l'upload, non lo reinventa. "
                     "--prova (dry-run) e' il default.")
    ap.add_argument("--conferma", action="store_true",
                     help="Carica davvero, un video alla volta in ordine di anzianita', "
                          "fermandosi al primo fallimento. Senza questo flag lo script e' "
                          "SEMPRE in modalita' prova, qualunque altra opzione sia passata.")
    ap.add_argument("--prova", action="store_true",
                     help="Rende esplicita la modalita' di prova (e' comunque il default se "
                          "--conferma non e' passato: qui solo per chiarezza nei comandi/log).")
    ap.add_argument("--video-pronti-dir", default=VIDEO_PRONTI_DIR,
                     help="Cartella da scansionare (default: VIDEO-PRONTI/ della fabbrica).")
    ap.add_argument("--log", default=DEFAULT_LOG,
                     help="File di log in append (default: memory/carica_pronti.log).")
    args = ap.parse_args(argv)

    return esegui(video_pronti_dir=args.video_pronti_dir, log_path=args.log,
                  conferma=args.conferma)


if __name__ == "__main__":
    sys.exit(main())
