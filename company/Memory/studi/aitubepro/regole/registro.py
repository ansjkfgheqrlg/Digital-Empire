# -*- coding: utf-8 -*-
"""registro.py — carica, valida e interroga TUTTE le regole imparate dal corso.

E' lo strumento che impedisce allo studio di diventare un archivio morto. Risponde alle
domande che contano davvero quando le lezioni saranno decine:

    python registro.py                       elenco e conteggi
    python registro.py --verifica            controlla che ogni regola sia a norma
    python registro.py --verifica A4         solo una categoria
    python registro.py --tocca fliki_client  quali regole riguardano un certo file
    python registro.py --da-applicare        cosa non e' ancora entrato nella fabbrica

Un gate di categoria non si supera se `--verifica` non e' pulito (piano §9).
"""

import argparse
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import schema  # noqa: E402


def carica_tutte():
    """Percorre le cartelle di categoria e importa ogni script-lezione."""
    trovate = []
    for radice, _dirs, files in os.walk(HERE):
        for nome in sorted(files):
            if not nome.endswith(".py") or nome in ("registro.py", "schema.py"):
                continue
            percorso = os.path.join(radice, nome)
            chiave = os.path.relpath(percorso, HERE).replace(os.sep, "/")
            try:
                spec = importlib.util.spec_from_file_location("reg_%d" % len(trovate), percorso)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except Exception as e:
                trovate.append({"_file": chiave, "_errore": "non caricabile: %s" % e})
                continue
            for r in getattr(mod, "REGOLE", []) or []:
                r = dict(r)
                r["_file"] = chiave
                r["_lezione"] = getattr(mod, "LEZIONE", "")
                r["_fonte_corso"] = getattr(mod, "FONTE", "")
                r["_verifica"] = getattr(mod, "verifica", None)
                trovate.append(r)
    return trovate


# La fabbrica sta cinque livelli sopra questa cartella:
# regole/ -> aitubepro/ -> studi/ -> Memory/ -> company/ -> radice del repo
FABBRICA = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "..",
                                        "YOUTUBE-AUTOMATION-FACTORY"))


def stato_applicazione(regole, fabbrica):
    """Chiede a ogni lezione se la fabbrica rispetta gia' le sue regole.

    Senza questo, `--da-applicare` elencava TUTTE le regole per sempre, comprese quelle
    gia' entrate: un elenco che non cala non e' un elenco di lavoro, e' rumore. Ogni
    script-lezione espone `verifica(fabbrica)` che restituisce {id: True/False}; qui
    quelle risposte vengono raccolte in un colpo solo.

    Una regola il cui script non risponde resta 'ignota': non si dichiara applicata cio'
    che nessuno ha guardato.
    """
    cache, esiti = {}, {}
    for r in regole:
        fn = r.get("_verifica")
        chiave = r.get("_file")
        if fn is None:
            continue
        if chiave not in cache:
            try:
                cache[chiave] = fn(fabbrica) or {}
            except Exception as e:
                cache[chiave] = {"_errore": str(e)}
        esiti[r.get("id")] = cache[chiave].get(r.get("id"))
    return esiti


def verifica(regole, filtro=""):
    errori = []
    visti = {}
    for r in regole:
        if filtro and filtro.lower() not in r.get("_file", "").lower():
            continue
        ctx = "%s [%s]" % (r.get("_file", "?"), r.get("id", "senza-id"))
        if "_errore" in r:
            errori.append("%s: %s" % (r["_file"], r["_errore"]))
            continue
        errori.extend(schema.valida(r, ctx))
        ident = r.get("id")
        if ident:
            if ident in visti:
                errori.append("%s: id duplicato, gia' usato in %s" % (ctx, visti[ident]))
            visti[ident] = r.get("_file")
    return errori


def main():
    ap = argparse.ArgumentParser(description="Registro delle regole imparate dal corso.")
    ap.add_argument("--verifica", nargs="?", const="", default=None,
                    help="Controlla che le regole siano a norma (opz.: filtro categoria).")
    ap.add_argument("--tocca", help="Mostra le regole che riguardano un certo file.")
    ap.add_argument("--da-applicare", action="store_true",
                    help="Regole non ancora entrate nella fabbrica.")
    ap.add_argument("--fabbrica", default=FABBRICA,
                    help="Percorso di YOUTUBE-AUTOMATION-FACTORY (default: quella del repo).")
    ap.add_argument("--tutte", action="store_true",
                    help="Con --da-applicare: mostra anche le regole gia' applicate.")
    a = ap.parse_args()

    regole = carica_tutte()
    vere = [r for r in regole if "_errore" not in r]

    if a.verifica is not None:
        errori = verifica(regole, a.verifica)
        if errori:
            print("[!] %d problemi:" % len(errori))
            for e in errori:
                print("   -", e)
            return 1
        print("[+] %d regole, tutte a norma." % len(vere))
        return 0

    if a.tocca:
        sel = [r for r in vere if a.tocca.lower() in str(r.get("tocca", "")).lower()]
        print("Regole che toccano %r: %d" % (a.tocca, len(sel)))
        for r in sel:
            print("  %-16s [%s/%s] %s" % (r.get("id"), r.get("binario"), r.get("rischio"),
                                          str(r.get("regola"))[:80]))
        return 0

    if a.da_applicare:
        esiti = stato_applicazione(vere, a.fabbrica)
        sel = [r for r in vere if r.get("azione") in ("modifica", "nuovo")]
        if not a.tutte:
            sel = [r for r in sel if esiti.get(r.get("id")) is not True]
        applicate = sum(1 for r in vere if esiti.get(r.get("id")) is True)
        ignote = sum(1 for r in vere if esiti.get(r.get("id")) is None)
        print("Regole da applicare: %d (di cui binario B: %d) · gia' applicate: %d · non verificabili: %d"
              % (len(sel), sum(1 for r in sel if r.get("binario") == "B"), applicate, ignote))
        for r in sel:
            marca = {True: "FATTA", False: "manca", None: "ignota"}[esiti.get(r.get("id"))]
            print("  %-16s [%s/%s] %-6s %-22s %s"
                  % (r.get("id"), r.get("binario"), r.get("rischio"), marca,
                     str(r.get("tocca"))[:22], str(r.get("regola"))[:60]))
        return 0

    # riepilogo
    print("Regole caricate: %d (da %d file)"
          % (len(vere), len({r.get("_file") for r in regole})))
    for chiave in ("binario", "rischio", "azione", "tipo", "fonte"):
        conteggi = {}
        for r in vere:
            conteggi[r.get(chiave)] = conteggi.get(r.get(chiave), 0) + 1
        if conteggi:
            print("  %-9s %s" % (chiave, "  ".join("%s=%d" % kv for kv in sorted(conteggi.items(),
                                                                                key=lambda x: str(x[0])))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
