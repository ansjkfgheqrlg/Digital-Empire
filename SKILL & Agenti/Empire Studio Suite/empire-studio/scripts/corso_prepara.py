# -*- coding: utf-8 -*-
"""corso_prepara.py — prepara IN BLOCCO le lezioni di una categoria, in sottofondo.

PERCHE' ESISTE, ed e' una correzione a un mio errore di metodo (2026-09-04).
Nella prima lezione ho lavorato in fila indiana: scarica, aspetta; trascrivi, aspetta; poi
studia. Risultato: la macchina ferma mentre leggevo, e io fermo mentre la macchina lavorava.
Su 167 lezioni quel modo di procedere e' insostenibile — non per la macchina, per il tempo
di Max.

Qui la catena diventa un nastro: questo script scarica e trascrive **tutte** le lezioni di
una categoria mentre io studio quelle gia' pronte. Quando arrivo alla lezione N, la N+1 e'
gia' in casa.

Perche' UNA per volta e non in parallelo:
  - il gettone del video scade: si cattura e si usa subito, mai si accoda;
  - il riconoscitore su CPU usa gia' tutti i core: due trascrizioni insieme non vanno il
    doppio piu' veloci, vanno il doppio piu' lente ciascuna.
La sequenzialita' qui non e' prudenza: e' la scelta piu' rapida davvero.

Idempotente: una lezione gia' scaricata o gia' trascritta viene saltata, quindi si puo'
rilanciare dopo un'interruzione senza rifare niente.

USO
    python corso_prepara.py --categoria "Metodo AI Tube"
    python corso_prepara.py --categoria "Metodo AI Tube" --da 5 --quante 8
"""

import argparse
import io
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
RUNS = os.path.join(STUDIO, "runs", "corso-aitubepro")


def lezioni_di(categoria, corso="aitubepro"):
    with io.open(os.path.join(RUNS, "mappa.json"), encoding="utf-8") as f:
        mappa = json.load(f)
    for c in mappa.get(corso, {}).get("categorie", []):
        if categoria.lower() in (c.get("titolo") or "").lower():
            return c["titolo"], sorted(c["lezioni"], key=lambda x: x.get("ordine") or 0)
    raise SystemExit("[!] Categoria %r non trovata." % categoria)


def gia_fatta(lesson_id):
    """Una lezione e' pronta quando ha il video E il parlato."""
    cartella = os.path.join(RUNS, lesson_id)
    mp4 = os.path.join(cartella, "video.mp4")
    txt = os.path.join(cartella, "parlato.txt")
    return (os.path.exists(mp4) and os.path.getsize(mp4) > 100000
            and os.path.exists(txt) and os.path.getsize(txt) > 500)


def esegui(script, args):
    cmd = [sys.executable, os.path.join(HERE, script)] + args
    amb = dict(os.environ, PYTHONIOENCODING="utf-8", HF_HUB_DISABLE_XET="1")
    return subprocess.run(cmd, env=amb, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def prepara(categoria, corso="aitubepro", da=0, quante=None, modello="base"):
    titolo, lezioni = lezioni_di(categoria, corso)
    fetta = lezioni[da:(da + quante) if quante else None]
    print("=== %s — %d lezioni, ne preparo %d (dalla %d) ===" % (titolo, len(lezioni), len(fetta), da))

    fatte, saltate, guasti = 0, 0, []
    t0 = time.time()
    for i, l in enumerate(fetta, start=1):
        lid, tit = l["lesson_id"], (l.get("titolo") or "")[:58]
        if gia_fatta(lid):
            print("[%2d/%2d] = %s  (gia' pronta)" % (i, len(fetta), tit))
            saltate += 1
            continue

        print("[%2d/%2d] . %s" % (i, len(fetta), tit), flush=True)
        r = esegui("corso_ingest.py", ["--lezione", lid, "--corso", corso, "--nascosto"])
        if r.returncode != 0 or not os.path.exists(os.path.join(RUNS, lid, "video.mp4")):
            coda = (r.stdout or "")[-200:] + (r.stderr or "")[-200:]
            print("        [!] scaricamento fallito: %s" % coda.replace("\n", " ")[-160:])
            guasti.append((lid, tit, "scaricamento"))
            continue

        r = esegui("corso_trascrivi.py", ["--lezione", lid, "--modello", modello])
        if not os.path.exists(os.path.join(RUNS, lid, "parlato.txt")):
            coda = (r.stdout or "")[-200:] + (r.stderr or "")[-200:]
            print("        [!] trascrizione fallita: %s" % coda.replace("\n", " ")[-160:])
            guasti.append((lid, tit, "trascrizione"))
            continue

        # una riga di esito, utile a colpo d'occhio
        riga = [x for x in (r.stdout or "").splitlines() if "parole in" in x]
        print("        + %s" % (riga[0].strip() if riga else "pronta"))
        fatte += 1

    print("\n=== FATTO in %.0f minuti — %d preparate, %d gia' pronte, %d guasti ==="
          % ((time.time() - t0) / 60, fatte, saltate, len(guasti)))
    for lid, tit, dove in guasti:
        print("   [!] %s — fallita in %s (%s)" % (tit, dove, lid))
    return 0 if not guasti else 1


def main():
    ap = argparse.ArgumentParser(description="Prepara in blocco le lezioni di una categoria.")
    ap.add_argument("--categoria", required=True)
    ap.add_argument("--corso", default="aitubepro")
    ap.add_argument("--da", type=int, default=0)
    ap.add_argument("--quante", type=int, default=None)
    ap.add_argument("--modello", default="base")
    a = ap.parse_args()
    return prepara(a.categoria, a.corso, a.da, a.quante, a.modello)


if __name__ == "__main__":
    sys.exit(main())
