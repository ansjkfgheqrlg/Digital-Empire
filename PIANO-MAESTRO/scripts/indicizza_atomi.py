"""
indicizza_atomi.py — FASE 0, passo 1 del piano 35 (Libro dell'Agency, Edizione Integrale).

Legge OGNI file di atomi di conoscenza presente sul disco, li normalizza in un solo
schema, elimina i doppioni-specchio (la stessa run salvata due volte: una in `runs/`
e una in `memory-empire/knowledge/`) e produce:

  PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE/atomi-index.json   <- il registro completo
  PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE/shard/<run>.json   <- una fetta per agente classificatore
  PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE/CENSIMENTO.md      <- i numeri veri, contati

Regola madre (piano 35, errore 4): non si conta in righe, si conta in atomi.
Nessun atomo viene scartato: quelli poveri diventano peso "contesto", non spariscono.

Console Windows cp1252: nessuna emoji nei print.
"""

import hashlib
import json
import os
import re
import sys
from collections import defaultdict

# --------------------------------------------------------------------------- percorsi

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # PIANO-MAESTRO/
REPO = os.path.dirname(ROOT)                                          # Digital Empire/
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
SHARD_DIR = os.path.join(OUT_DIR, "shard")

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".next", "venv", ".venv",
             "dist", "build", ".cache-tools", "graphify-out"}

# --------------------------------------------------------------- tassonomia (piano 8.2)

LIBRI = {
    "I": "Il Metodo Digital Empire",
    "II": "Trovare clienti",
    "III": "Vendere e prezzare",
    "IV": "Consegnare e scalare",
    "V": "Costruire con l'AI",
    "VI": "Contenuto, brand, lanci",
    "VII": "Imparare e decidere",
    "VIII": "Apparati",
}
PESI = ("portante", "supporto", "contesto")

# --------------------------------------------------------------------------- lettura


def carica(path):
    """Ritorna la lista di atomi grezzi di un file, qualunque sia il suo involucro."""
    try:
        with open(path, encoding="utf-8") as fh:
            dati = json.load(fh)
    except UnicodeDecodeError:
        with open(path, encoding="utf-8", errors="replace") as fh:
            dati = json.load(fh)
    except Exception as exc:                                   # file rotto: lo si dichiara
        return None, "illeggibile: %s" % exc
    if isinstance(dati, list):
        return dati, None
    if isinstance(dati, dict):
        for chiave in ("atoms", "atomi", "knowledge_atoms", "ka"):
            if isinstance(dati.get(chiave), list):
                return dati[chiave], None
    return None, "schema non riconosciuto"


def campo(atomo, *nomi):
    for n in nomi:
        v = atomo.get(n)
        if isinstance(v, str) and v.strip():
            return v.strip()
        if isinstance(v, list) and v:
            return v
    return ""


def normalizza(atomo, run, fonte_file, indice):
    """Porta i due schemi noti (runs/ ricco, knowledge/ povero) allo stesso schema."""
    contenuto = campo(atomo, "contenuto", "atom", "content", "text", "testo")
    ka = campo(atomo, "id", "ka_id", "ka") or "KA-%03d" % (indice + 1)
    tags = atomo.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    return {
        "uid": "%s::%s" % (run, ka),
        "ka_id": ka,
        "run": run,
        "tipo": campo(atomo, "tipo", "category", "categoria"),
        "contenuto": contenuto,
        # `ancora` = citazione letterale della fonte. Solo lo schema ricco ce l'ha:
        # dove manca, il gate di densita' non potra' pretenderla (dichiarato, non aggirato).
        "ancora": campo(atomo, "ancora", "anchor", "quote", "verbatim"),
        "fonte": campo(atomo, "fonte", "source", "src"),
        "frame": campo(atomo, "frame", "frames"),
        "confidenza": campo(atomo, "confidenza", "confidence"),
        "tags": tags,
        "relazioni": atomo.get("relazioni") or atomo.get("relations") or [],
        "file_sorgente": fonte_file,
        "parole": len(contenuto.split()),
        # da riempire in Fase 0 passo 2 (agenti classificatori):
        "libro": None,
        "capitolo": None,
        "peso": None,
        # da riempire in Fase 0 passo 3 (dedup fra fonti):
        "principale_di": None,
    }


def impronta(testo):
    """Impronta di contenuto per riconoscere lo stesso atomo salvato due volte."""
    pulito = re.sub(r"\s+", " ", (testo or "").lower()).strip()[:400]
    return hashlib.md5(pulito.encode("utf-8")).hexdigest()


def nome_run(path_dir):
    """Nome leggibile della run: la cartella che contiene il file atoms."""
    return os.path.basename(path_dir.rstrip(os.sep)) or "sconosciuta"


def video_id(run):
    """Estrae l'id video (11 caratteri YouTube) dal nome della run, se c'e'."""
    m = re.search(r"([A-Za-z0-9_-]{11})$", run)
    return m.group(1) if m else None


# --------------------------------------------------------------------------- raccolta


def raccogli():
    trovati = []           # (path, run, root, atomi_grezzi)
    problemi = []
    for dp, dn, fn in os.walk(REPO):
        dn[:] = [d for d in dn if d not in SKIP_DIRS and not d.startswith(".git")]
        for f in fn:
            if not (f.startswith("atoms") or f.startswith("atomi")):
                continue
            if not f.endswith(".json"):
                continue
            if f in ("atomi-index.json",):
                continue
            path = os.path.join(dp, f)
            norm = path.replace(os.sep, "/")
            if "/36-LIBRO-AGENCY-INTEGRALE/" in norm:
                continue
            atomi, errore = carica(path)
            if errore:
                problemi.append((norm, errore))
                continue
            if not atomi:
                continue
            if "/runs/" in norm:
                root = "runs"
            elif "memory-empire/knowledge" in norm:
                root = "knowledge"
            else:
                root = "altro"
            trovati.append((norm, nome_run(dp), root, atomi))
    return trovati, problemi


def impronte_di(atomi):
    return {impronta(campo(a, "contenuto", "atom", "content", "text")) for a in atomi}


def scarta_parti(trovati):
    """
    Dentro una stessa cartella convivono `atoms.json` (l'intero) e `atoms-p1/p2/p3.json`
    (le fette con cui e' stato costruito). Vince l'intero; le fette si scartano solo
    se davvero contenute in lui.
    """
    per_dir = defaultdict(list)
    for voce in trovati:
        per_dir[os.path.dirname(voce[0])].append(voce)

    tenuti, scartati = [], []
    for _cartella, voci in per_dir.items():
        if len(voci) == 1:
            tenuti.append(voci[0])
            continue
        interi = [v for v in voci if os.path.basename(v[0]) in ("atoms.json", "atomi.json")]
        if not interi:
            tenuti.extend(voci)
            continue
        base = set()
        for v in interi:
            base |= impronte_di(v[3])
        tenuti.extend(interi)
        for v in voci:
            if v in interi:
                continue
            mie = impronte_di(v[3])
            quota = len(mie & base) / max(1, len(mie))
            if quota >= 0.80:
                scartati.append((v[0], v[1], "parte", len(v[3]), round(quota * 100)))
            else:
                tenuti.append(v)
    return tenuti, scartati


def scegli_canoniche(trovati):
    """
    Fra `runs/` e `knowledge/` la stessa run compare due volte. Vince `runs/`:
    ha l'ancora verbatim, che il gate di densita' pretende. La copia povera si
    scarta SOLO se il suo contenuto e' davvero coperto (>= 80% di impronte in comune).
    """
    per_root = defaultdict(list)
    for voce in trovati:
        per_root[voce[2]].append(voce)

    impronte_runs = defaultdict(set)     # video_id -> impronte
    impronte_runs_tutte = set()
    for norm, run, root, atomi in per_root["runs"]:
        vid = video_id(run)
        for a in atomi:
            h = impronta(campo(a, "contenuto", "atom", "content", "text"))
            impronte_runs_tutte.add(h)
            if vid:
                impronte_runs[vid].add(h)

    canoniche, scartate = [], []
    for voce in trovati:
        norm, run, root, atomi = voce
        if root == "runs":
            canoniche.append(voce)
            continue
        mie = {impronta(campo(a, "contenuto", "atom", "content", "text")) for a in atomi}
        coperte = len(mie & impronte_runs_tutte)
        quota = coperte / max(1, len(mie))
        if quota >= 0.80:
            scartate.append((norm, run, root, len(atomi), round(quota * 100)))
        else:
            canoniche.append(voce)
    return canoniche, scartate


# --------------------------------------------------------------------------- scrittura


def main():
    print("[1/4] scansione del disco...")
    trovati, problemi = raccogli()
    print("      file di atomi trovati: %d" % len(trovati))
    for norm, errore in problemi:
        print("      SALTATO (%s): %s" % (errore, norm))

    print("[2/4] scelta delle copie canoniche...")
    trovati, parti = scarta_parti(trovati)
    print("      fette interne scartate (atoms-pN dentro atoms.json): %d file" % len(parti))
    canoniche, specchi = scegli_canoniche(trovati)
    print("      canoniche: %d file   specchi knowledge/ scartati: %d file"
          % (len(canoniche), len(specchi)))
    scartate = parti + specchi

    print("[3/4] normalizzazione...")
    indice, per_run, viste = [], defaultdict(int), {}
    doppi_interni = 0
    for norm, run, root, atomi in sorted(canoniche, key=lambda v: v[1]):
        for i, grezzo in enumerate(atomi):
            rec = normalizza(grezzo, run, norm, i)
            if not rec["contenuto"]:
                continue
            h = impronta(rec["contenuto"])
            if h in viste:                       # stesso testo, gia' preso da un'altra run
                doppi_interni += 1
                rec["principale_di"] = viste[h]
            else:
                viste[h] = rec["uid"]
            rec["impronta"] = h
            indice.append(rec)
            per_run[run] += 1

    con_ancora = sum(1 for a in indice if a["ancora"])
    parole = sum(a["parole"] for a in indice)

    print("[4/4] scrittura...")
    os.makedirs(SHARD_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "atomi-index.json"), "w", encoding="utf-8") as fh:
        json.dump({
            "generato_da": "PIANO-MAESTRO/scripts/indicizza_atomi.py",
            "tassonomia": LIBRI,
            "pesi": list(PESI),
            "totale_atomi": len(indice),
            "run": len(per_run),
            "atomi_con_ancora": con_ancora,
            "atomi_doppioni_fra_run": doppi_interni,
            "atomi": indice,
        }, fh, ensure_ascii=False, indent=1)

    for run in sorted(per_run):
        fetta = [a for a in indice if a["run"] == run]
        nome = re.sub(r"[^A-Za-z0-9_.-]", "_", run)
        with open(os.path.join(SHARD_DIR, nome + ".json"), "w", encoding="utf-8") as fh:
            json.dump({"run": run, "totale": len(fetta), "atomi": fetta},
                      fh, ensure_ascii=False, indent=1)

    righe = ["# CENSIMENTO DEGLI ATOMI — contato sul disco, non stimato", ""]
    righe.append("- File di atomi trovati: **%d**" % len(trovati))
    righe.append("- File canonici usati: **%d** (specchi scartati: %d)"
                 % (len(canoniche), len(scartate)))
    righe.append("- **Atomi totali nell'indice: %d**, su **%d run**" % (len(indice), len(per_run)))
    righe.append("- Atomi con ancora verbatim: **%d** (%.0f%%) — il gate di densita' "
                 "puo' pretendere l'ancora solo su questi"
                 % (con_ancora, 100.0 * con_ancora / max(1, len(indice))))
    righe.append("- Atomi che ripetono un atomo di un'altra run: **%d** "
                 "(marcati `principale_di`, non cancellati)" % doppi_interni)
    righe.append("- Parole contenute negli atomi: **%d**" % parole)
    righe.append("")
    righe.append("## Atomi per run")
    righe.append("")
    righe.append("| Run | Atomi |")
    righe.append("|---|---|")
    for run, n in sorted(per_run.items(), key=lambda x: -x[1]):
        righe.append("| `%s` | %d |" % (run, n))
    if scartate:
        righe.append("")
        righe.append("## Specchi scartati (stessa run salvata due volte)")
        righe.append("")
        righe.append("| File | Atomi | Copertura trovata in `runs/` |")
        righe.append("|---|---|---|")
        for norm, run, root, n, quota in sorted(scartate, key=lambda x: -x[3]):
            righe.append("| `%s` | %d | %d%% |" % (norm, n, quota))
    if problemi:
        righe.append("")
        righe.append("## File saltati")
        righe.append("")
        for norm, errore in problemi:
            righe.append("- `%s` — %s" % (norm, errore))
    with open(os.path.join(OUT_DIR, "CENSIMENTO.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(righe) + "\n")

    print("")
    print("FATTO. atomi=%d  run=%d  con_ancora=%d  doppioni=%d"
          % (len(indice), len(per_run), con_ancora, doppi_interni))
    print("indice  -> %s" % os.path.join(OUT_DIR, "atomi-index.json"))
    print("fette   -> %s (%d file)" % (SHARD_DIR, len(per_run)))
    print("numeri  -> %s" % os.path.join(OUT_DIR, "CENSIMENTO.md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
