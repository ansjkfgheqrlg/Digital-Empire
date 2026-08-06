#!/usr/bin/env python3
"""
Regolatori (L3) della YouTube Automation Factory — controlli ESEGUIBILI, non specifiche.

Ogni regolatore risponde a una sola domanda e ha un solo potere: lasciar passare o BLOCCARE,
citando la regola violata. Non producono contenuti e non propongono alternative.
Organigramma: 03-AGENTI-E-RUOLI/ORGANIGRAMMA.md

Principio delle 3 firme: esegue un operatore (L2) -> approva il capo del reparto (L1) -> non
hanno bloccato i regolatori (L3). Questo modulo implementa il terzo passaggio.

Uso da riga di comando (diagnostica):
    python regolatori.py --tutti
    python regolatori.py --originalita mkaNzHTBw1M
"""
from __future__ import annotations
import os
import re
import sys
import json
import argparse
import subprocess

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")
TRANSCRIPTS_DIR = os.path.join(FACTORY_DIR, "transcripts")
MEMORY_DIR = os.path.join(FACTORY_DIR, "memory")
FIRME_PATH = os.path.join(MEMORY_DIR, "firme.json")


def esito(regolatore: str, passa: bool, motivo: str, **dettagli) -> dict:
    return {"regolatore": regolatore, "esito": "passa" if passa else "BLOCCO",
            "motivo": motivo, **dettagli}


_SEZIONI_NARRATE = ("HOOK", "INTRO", "CORPO", "CTA")


def testo_narrato(script_md: str) -> str:
    """Solo il testo che verra' DAVVERO narrato: le sezioni HOOK/INTRO/CORPO/CTA, senza le
    note di produzione (intestazione, "Note SEO inline", annotazioni "➕ ..." di regia).

    Serve perche' un regolatore deve giudicare cio' che arriva allo spettatore. Senza questo
    filtro, una nota di lavorazione come "non tech, non Claude Code — non nominare" faceva
    scattare un BLOCCO per un termine che era li' proprio per vietarlo (falso positivo reale,
    trovato il 2026-08-03)."""
    intestazioni = list(re.finditer(r"^## (\w+)[^\n]*\n", script_md or "", re.MULTILINE))
    pezzi = []
    for i, m in enumerate(intestazioni):
        if m.group(1).upper() not in _SEZIONI_NARRATE:
            continue
        fine = intestazioni[i + 1].start() if i + 1 < len(intestazioni) else len(script_md)
        pezzi.append(script_md[m.end():fine].split("➕")[0].strip())
    return "\n\n".join(pezzi)


# --------------------------------------------------------------------------------------
# regolatore-nicchia — la nicchia non cambia mai, e il canale vive SOLO di views
# --------------------------------------------------------------------------------------

# Residui del funnel "Manuale Claude Code" (progetto morto) e temi fuori nicchia. Sono termini
# che su un canale di spiritualita'/benessere per over-60 non hanno alcuna ragione di esistere.
_FUORI_NICCHIA = [
    "claude code", "manuale claude", "antigravity", "prompt engineering", "terminale",
    "installare il software", "workflow n8n", "saas", "funnel",
]
# CTA commerciali: questo canale non vende niente.
_CTA_COMMERCIALI = [
    "acquista", "compra ora", "carrello", "sconto del", "iscriviti al corso",
    "link per acquistare", "prezzo speciale", "offerta limitata",
]


def verifica_nicchia(testi: dict[str, str]) -> dict:
    """`testi`: {'script': ..., 'titolo': ..., 'descrizione': ...}"""
    trovati = []
    for nome, testo in testi.items():
        basso = (testo or "").lower()
        trovati += [f"{nome}: '{t}' (fuori nicchia)" for t in _FUORI_NICCHIA if t in basso]
        trovati += [f"{nome}: '{t}' (CTA commerciale)" for t in _CTA_COMMERCIALI if t in basso]
    if trovati:
        return esito("regolatore-nicchia", False,
                     "Contenuto fuori nicchia o CTA commerciale: questo canale vive solo di views.",
                     violazioni=trovati)
    return esito("regolatore-nicchia", True, "Contenuto dentro la nicchia, nessuna CTA commerciale.")


# --------------------------------------------------------------------------------------
# regolatore-originalita — mai una copia mascherata del video sorgente
# --------------------------------------------------------------------------------------
N_GRAM = 8
MIN_ELEMENTI_NUOVI = 3


def _normalizza(testo: str) -> list[str]:
    return re.findall(r"[a-zà-ù0-9]+", (testo or "").lower())


def _ngrammi(parole: list[str], n: int) -> set[str]:
    return {" ".join(parole[i:i + n]) for i in range(len(parole) - n + 1)}


# Fonti citabili, per TEMA. La prima lista nasceva sul video di salute e conteneva solo
# istituzioni di ricerca medica: su un contenuto spirituale non vedeva le citazioni bibliche e
# bloccava uno script che il valore aggiunto ce l'aveva (falso negativo reale, 2026-08-04).
# La nicchia copre spiritualita', psicologia, saggezza biblica E salute: servono entrambe.
_FONTI = re.compile(
    r"\b("
    # ricerca e istituzioni sanitarie
    r"Cleveland Clinic|Mayo Clinic|Stanford|Harvard|British Journal|PLOS|"
    r"Istituto Superiore di Sanit[àa]|OMS|Journal of|uno studio|una ricerca|"
    # testi e riferimenti della tradizione spirituale
    r"Vangelo|Bibbia|Proverbi|Matteo|Luca|Giovanni|Salmi|Qoelet|Siracide|"
    r"Scrittura|Genesi|Corinzi"
    r")\b",
    re.IGNORECASE,
)


def _elementi_nuovi(script: str) -> list[str]:
    """Segnali concreti e verificabili di valore aggiunto: fonti e riferimenti citati.

    Limite dichiarato: questa e' una misura *approssimata*. Un contributo originale puo'
    consistere in una struttura o in un ragionamento nuovi, che nessuna espressione regolare
    sa riconoscere. Per questo il giudizio finale sul valore aggiunto resta di `capo-copy`:
    qui si verifica solo che lo script non sia una parafrasi priva di apporti propri.
    """
    trovati = [m.group(0) for m in _FONTI.finditer(script)]
    return sorted({t.strip() for t in trovati})


def verifica_originalita(script: str, transcript: str) -> dict:
    """Misura la sovrapposizione letterale e il valore aggiunto.

    Attenzione dichiarata: se il video sorgente e' in inglese e il nostro in italiano, la
    sovrapposizione letterale sara' sempre zero e NON e' una prova di originalita'. In quel
    caso pesa solo il valore aggiunto (e la struttura, che va valutata a occhio da capo-copy).
    """
    p_script, p_source = _normalizza(script), _normalizza(transcript)
    if len(p_script) < N_GRAM or len(p_source) < N_GRAM:
        return esito("regolatore-originalita", True,
                     "Testi troppo brevi per un confronto n-grammi significativo.",
                     sequenze_condivise=0)

    condivisi = _ngrammi(p_script, N_GRAM) & _ngrammi(p_source, N_GRAM)
    nuovi = _elementi_nuovi(script)

    # Euristica per capire se le due lingue coincidono: quante parole piene del sorgente
    # compaiono nel nostro testo. Se pochissime, sono lingue diverse.
    comuni = len(set(p_script) & set(p_source)) / max(len(set(p_source)), 1)
    stessa_lingua = comuni > 0.25

    if condivisi:
        return esito("regolatore-originalita", False,
                     f"Trovate {len(condivisi)} sequenze di {N_GRAM}+ parole identiche al "
                     f"transcript sorgente: e' una copia, va riscritto.",
                     sequenze_condivise=len(condivisi), esempi=sorted(condivisi)[:3],
                     elementi_nuovi=nuovi)

    if len(nuovi) < MIN_ELEMENTI_NUOVI:
        return esito("regolatore-originalita", False,
                     f"Nessuna copia letterale, ma solo {len(nuovi)} elementi di valore aggiunto "
                     f"(minimo {MIN_ELEMENTI_NUOVI}): senza valore aggiunto il video non ha "
                     f"ragione di esistere.",
                     sequenze_condivise=0, elementi_nuovi=nuovi)

    nota = ("stessa lingua del sorgente" if stessa_lingua else
            "LINGUE DIVERSE: la sovrapposizione letterale nulla non prova l'originalita', "
            "la struttura va valutata da capo-copy")
    return esito("regolatore-originalita", True,
                 f"Nessuna sequenza identica, {len(nuovi)} elementi di valore aggiunto.",
                 sequenze_condivise=0, elementi_nuovi=nuovi, nota=nota)


# --------------------------------------------------------------------------------------
# regolatore-copy — standard di casa e rispetto del pubblico (70-80 anni)
# --------------------------------------------------------------------------------------
_ANGLICISMI = ["mindset", "workout", "boost", "tips", "lifestyle", "skill", "goal",
               "performance", "focus", "target", "step by step", "trend"]
_PROMESSE_MEDICHE = ["guarirai", "ti curerà", "cura definitiva", "elimina il dolore",
                     "guarisce", "sconfigge la malattia", "previene il cancro"]


def verifica_copy(testi: dict[str, str]) -> dict:
    problemi = []
    for nome, testo in testi.items():
        basso = (testo or "").lower()
        problemi += [f"{nome}: anglicismo '{a}'" for a in _ANGLICISMI if re.search(rf"\b{a}\b", basso)]
        problemi += [f"{nome}: promessa medica '{p}'" for p in _PROMESSE_MEDICHE if p in basso]
        if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", testo or ""):
            problemi.append(f"{nome}: emoji nel testo (pubblico 70-80 anni)")
    if problemi:
        return esito("regolatore-copy", False,
                     "Testo non conforme allo standard di casa o al pubblico del canale.",
                     violazioni=problemi)
    return esito("regolatore-copy", True, "Testi conformi: nessun anglicismo, promessa medica o emoji.")


# --------------------------------------------------------------------------------------
# regolatore-configurazione — la configurazione Fliki approvata da Gael non si tocca
# --------------------------------------------------------------------------------------
CONFIG_APPROVATA = {
    # Approvati da Gael il 2026-07-31 sul video v8 ("non cambiare niente, falli tutti cosi'").
    # L'effetto karaoke parola-per-parola dei sottotitoli E' VOLUTO: non e' un difetto.
    "subtitlePresetId": "builtin-legacy-bold",
    "highlightSubtitles": True,
    "duration": 720,          # inerte (l'API vuole 1-15 minuti) ma fa parte dell'approvato
    "sceneBreakdown": "lineBreak",
    "aspectRatio": "16:9",
    "resolution": "1080p",
    # Cambiato il 2026-08-03 su delega esplicita di Gael ("scegli te"), dopo confronto fra le
    # due versioni: le clip stock finivano fuori bersaglio anagrafico, le immagini generate
    # nascono dal testo della scena e restano in tema.
    "visuals": "ai",
}


def verifica_configurazione(payload: dict, flag_espliciti: dict | None = None) -> dict:
    """`flag_espliciti`: varianti autorizzate a riga di comando (es. {'visuals': 'ai'})."""
    flag_espliciti = flag_espliciti or {}
    differenze = []
    for campo, atteso in CONFIG_APPROVATA.items():
        trovato = payload.get(campo)
        if trovato == atteso:
            continue
        if campo in flag_espliciti and trovato == flag_espliciti[campo]:
            continue  # variante opt-in autorizzata dall'operatore umano
        differenze.append(f"{campo}: atteso {atteso!r}, trovato {trovato!r}")
    if differenze:
        return esito("regolatore-configurazione", False,
                     "Configurazione Fliki alterata rispetto a quella approvata da Gael il "
                     "2026-07-31 ('non modificare le regole e non cambiare niente').",
                     differenze=differenze)
    return esito("regolatore-configurazione", True, "Configurazione identica a quella approvata.")


# --------------------------------------------------------------------------------------
# regolatore-qualita — si misura il FILE VERO, mai la risposta dell'API
# --------------------------------------------------------------------------------------
DURATA_MINIMA_S = 720


def verifica_qualita(percorso_mp4: str) -> dict:
    if not os.path.exists(percorso_mp4):
        return esito("regolatore-qualita", False, f"File inesistente: {percorso_mp4}")
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-show_entries", "stream=codec_type,codec_name,width,height",
             "-of", "json", percorso_mp4],
            capture_output=True, text=True, timeout=60)
        dati = json.loads(res.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        return esito("regolatore-qualita", False, f"Impossibile misurare il file con ffprobe: {e}")

    durata = float(dati.get("format", {}).get("duration", 0))
    stream = dati.get("streams", [])
    video = next((s for s in stream if s.get("codec_type") == "video"), None)
    audio = next((s for s in stream if s.get("codec_type") == "audio"), None)

    problemi = []
    if durata < DURATA_MINIMA_S:
        problemi.append(f"durata {durata:.0f}s < {DURATA_MINIMA_S}s richiesti")
    if not video:
        problemi.append("nessuno stream video")
    elif (video.get("width"), video.get("height")) != (1920, 1080):
        problemi.append(f"risoluzione {video.get('width')}x{video.get('height')}, attesa 1920x1080")
    if not audio:
        problemi.append("nessuno stream audio")

    misure = {"durata_s": round(durata, 2),
              "risoluzione": f"{video.get('width')}x{video.get('height')}" if video else None,
              "codec_video": video.get("codec_name") if video else None,
              "codec_audio": audio.get("codec_name") if audio else None}
    if problemi:
        return esito("regolatore-qualita", False,
                     "Il file non rispetta gli standard minimi.", problemi=problemi, misure=misure)
    return esito("regolatore-qualita", True,
                 "File conforme agli standard (misurato, non dedotto dall'API).", misure=misure,
                 nota="I sottotitoli vanno verificati a vista su >=3 fotogrammi: vedi capo-produzione.")


# --------------------------------------------------------------------------------------
# regolatore-copertina — la copertina generata deve essere visivamente distinta dalla sorgente
# --------------------------------------------------------------------------------------
# Fino al 2026-08-05 "riadattata, non ricalcata" era solo una frase nel prompt inviato ad Arena
# (arena_thumbnail.build_prompt): nessun controllo verificava il risultato. Qui si misura, non
# si deduce dal testo del prompt.
HASH_SIZE = 8
DISTANZA_MINIMA_BIT = 10  # su HASH_SIZE**2 bit totali (64): sotto, le due immagini sono troppo simili


def _average_hash(percorso_immagine: str) -> str:
    """Average hash 8x8: ridimensiona in scala di grigi, confronta ogni pixel con la media.
    Robusto a differenze di compressione/dimensione, sensibile a differenze di composizione —
    esattamente cio' che serve per distinguere 'stessa foto ricompressa' da 'foto riadattata'."""
    from PIL import Image
    img = Image.open(percorso_immagine).convert("L").resize((HASH_SIZE, HASH_SIZE), Image.LANCZOS)
    pixel = list(img.getdata())
    media = sum(pixel) / len(pixel)
    return "".join("1" if p > media else "0" for p in pixel)


def _distanza_hamming(a: str, b: str) -> int:
    return sum(1 for x, y in zip(a, b) if x != y)


def verifica_copertina(source_path: str | None, generated_path: str | None) -> dict:
    """Confronta la copertina generata con quella reale del competitor via hash percettivo.

    Limite dichiarato (come per regolatore-originalita sui testi): questa e' una misura
    approssimata di somiglianza visiva, non un giudizio di qualita' creativa. Una distanza
    alta non prova che la copertina sia buona; una distanza bassa prova solo che e' quasi
    identica alla sorgente — il minimo indispensabile perche' 'riadattata' non resti solo
    una parola nel prompt.
    """
    if not generated_path or not os.path.exists(generated_path):
        return esito("regolatore-copertina", False, f"Copertina generata inesistente: {generated_path}")
    if not source_path or not os.path.exists(source_path):
        return esito("regolatore-copertina", True,
                     "Nessuna copertina sorgente da confrontare (nessun adattamento da video "
                     "sorgente, prompt generico): controllo non applicabile.")
    try:
        hash_source = _average_hash(source_path)
        hash_generata = _average_hash(generated_path)
    except Exception as e:
        return esito("regolatore-copertina", False, f"Impossibile leggere le immagini: {e}")

    distanza = _distanza_hamming(hash_source, hash_generata)
    if distanza < DISTANZA_MINIMA_BIT:
        return esito("regolatore-copertina", False,
                     f"Copertina troppo simile alla sorgente (distanza percettiva {distanza}/"
                     f"{HASH_SIZE * HASH_SIZE} bit, minimo richiesto {DISTANZA_MINIMA_BIT}): "
                     f"non sembra riadattata.",
                     distanza_hash=distanza)
    return esito("regolatore-copertina", True,
                 f"Copertina visivamente distinta dalla sorgente (distanza percettiva "
                 f"{distanza}/{HASH_SIZE * HASH_SIZE} bit).",
                 distanza_hash=distanza)


# --------------------------------------------------------------------------------------
# Registro delle firme (principio delle 3 firme)
# --------------------------------------------------------------------------------------
VIDEO_PRODOTTI_PATH = os.path.join(MEMORY_DIR, "video_prodotti.json")


def aggiorna_qc_registro(source_video_id: str, superato: bool, motivo: str = "") -> None:
    """Scrive l'esito del controllo qualita' nel registro dei video prodotti.

    Serve a F2: un video che ha fallito il QC non e' fatto, quindi il suo argomento deve
    tornare disponibile per essere rilavorato. Senza questo passaggio un video scartato
    bloccava per sempre il proprio sorgente.
    """
    if not source_video_id or not os.path.exists(VIDEO_PRODOTTI_PATH):
        return
    try:
        registro = json.load(open(VIDEO_PRODOTTI_PATH, encoding="utf-8"))
    except (json.JSONDecodeError, ValueError):
        return
    cambiato = False
    for voce in registro:
        if voce.get("source_video_id") == source_video_id:
            voce["qc"] = "superato" if superato else "fallito"
            if motivo:
                voce["qc_motivo"] = motivo
            cambiato = True
    if cambiato:
        with open(VIDEO_PRODOTTI_PATH, "w", encoding="utf-8") as f:
            json.dump(registro, f, ensure_ascii=False, indent=2)
        stato = "superato" if superato else "FALLITO"
        print(f"[i] Registro aggiornato: QC {stato} per il sorgente {source_video_id}.")


def registra_firma(run_id: str, artefatto: str, operatore: str, capo: str,
                   verdetti: list[dict]) -> dict:
    """Registra le 3 firme di un artefatto. Se un regolatore ha bloccato, la firma NON e' valida."""
    blocchi = [v for v in verdetti if v["esito"] == "BLOCCO"]
    firma = {
        "run_id": run_id, "artefatto": artefatto,
        "esegue_L2": operatore, "approva_L1": capo,
        "regolatori_L3": [{"regolatore": v["regolatore"], "esito": v["esito"]} for v in verdetti],
        "valida": not blocchi,
        "blocchi": [{"regolatore": v["regolatore"], "motivo": v["motivo"]} for v in blocchi],
    }
    os.makedirs(MEMORY_DIR, exist_ok=True)
    registro = []
    if os.path.exists(FIRME_PATH):
        try:
            registro = json.load(open(FIRME_PATH, encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            registro = []
    registro.append(firma)
    with open(FIRME_PATH, "w", encoding="utf-8") as f:
        json.dump(registro[-200:], f, ensure_ascii=False, indent=2)
    return firma


# --------------------------------------------------------------------------------------
def _carica(percorso: str, default: str = "") -> str:
    return open(percorso, encoding="utf-8").read() if os.path.exists(percorso) else default


def main():
    ap = argparse.ArgumentParser(description="Esegue i regolatori L3 sugli artefatti correnti.")
    ap.add_argument("--tutti", action="store_true")
    ap.add_argument("--video-id", default=None, help="Per il confronto di originalita'.")
    ap.add_argument("--mp4", default=None, help="File video da misurare.")
    args = ap.parse_args()

    script_md = _carica(os.path.join(TEMPLATES_DIR, "script.md"))
    script = testo_narrato(script_md)  # solo cio' che viene narrato, non le note di produzione
    metadati_path = os.path.join(TEMPLATES_DIR, "metadati.json")
    metadati = json.load(open(metadati_path, encoding="utf-8")) if os.path.exists(metadati_path) else {}
    testi = {"script": script, "titolo": metadati.get("title", ""),
             "descrizione": metadati.get("description", "")}

    verdetti = [verifica_nicchia(testi), verifica_copy(testi)]

    video_id = args.video_id
    if not video_id:
        m = re.search(r"v=([\w-]+)", script_md)
        video_id = m.group(1) if m else None
    if video_id:
        transcript = ""
        for lingua in ("it", "en"):
            p = os.path.join(TRANSCRIPTS_DIR, f"dosementale-{video_id}.{lingua}.vtt")
            if os.path.exists(p):
                transcript = _carica(p)
                break
        if transcript:
            verdetti.append(verifica_originalita(script, transcript))

    if args.mp4:
        esito_qualita = verifica_qualita(args.mp4)
        verdetti.append(esito_qualita)
        # L'esito finisce nel registro: F2 deve poter rimettere in lavorazione un video
        # scartato dal controllo qualita'.
        if video_id:
            aggiorna_qc_registro(
                video_id,
                superato=esito_qualita["esito"] == "passa",
                motivo="; ".join(esito_qualita.get("problemi", [])),
            )

    for v in verdetti:
        simbolo = "🟢" if v["esito"] == "passa" else "🔴"
        print(f"{simbolo} {v['regolatore']:28} {v['esito']:6} — {v['motivo']}")
        for chiave in ("violazioni", "problemi", "differenze", "esempi"):
            for riga in v.get(chiave, []):
                print(f"      · {riga}")
        if v.get("elementi_nuovi"):
            print(f"      valore aggiunto: {', '.join(v['elementi_nuovi'])}")
        if v.get("nota"):
            print(f"      nota: {v['nota']}")

    return 1 if any(v["esito"] == "BLOCCO" for v in verdetti) else 0


if __name__ == "__main__":
    sys.exit(main())
