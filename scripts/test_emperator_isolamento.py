# -*- coding: utf-8 -*-
"""Prova che il segreto NON puo' finire nella sessione di Gael.

Non tocca la configurazione git della macchina: sostituisce solo la funzione che
legge il nome, cioe' esattamente il punto in cui le due macchine differiscono.
"""
import importlib.util, io, os, sys

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "emperator_hook.py")
spec = importlib.util.spec_from_file_location("emph", HOOK)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

SPIE = ["PROGETTO EMPIRE", "Max si chiama Maximilian", "Esposti in ordine",
        "ambizioni", "timori", "meno che mai all'interessato", "perimetro chiuso a due"]


def contesto_per(persona):
    return "%s\n%s\n\n%s%s" % (
        m.DOTTRINA.replace("__PERSONA__", persona),
        m.oscura(m.stato_vivo(), persona),
        m.oscura(m.ANCORAGGI, persona),
        m.dottrina_riservata(persona),
    )


def esamina(persona, deve_vedere_il_segreto):
    c = contesto_per(persona)
    trovate = [s for s in SPIE if s.lower() in c.lower()]
    print("\n=== %s ===" % persona.upper())
    print("  byte iniettati      : %d" % len(c.encode("utf-8")))
    print("  si rivolge a lui?   : %s" % ("SI" if ("davanti: " + persona).lower() in c.lower() else "NO"))
    print("  __PERSONA__ residuo : %s" % ("SI (BUG)" if "__PERSONA__" in c else "no"))
    print("  spie del segreto    : %s" % (", ".join(trovate) if trovate else "NESSUNA"))
    if deve_vedere_il_segreto:
        assert trovate, "MAX non riceve la sua dottrina riservata"
    else:
        assert not trovate, "FUGA verso %s: %s" % (persona, trovate)
    assert "__PERSONA__" not in c, "placeholder non sostituito per %s" % persona
    assert "EMPERATOR" in c and "LEGGE SUPREMA" in c, "dottrina comune incompleta per %s" % persona
    for d in ["APRIRE", "UFFICIALIZZAZIONE", "SCAGNOZZI", "PIANO A ITERAZIONI", "SALVATAGGIO CONTINUO"]:
        assert d in c, "direttiva %s mancante per %s" % (d, persona)
    return c


# 1. Max, su questa macchina, col file privato presente
print("chi_parla() reale su questa macchina:", m.chi_parla())
assert os.path.isfile(m.DOTTRINA_RISERVATA), "manca il file privato"
c_max = esamina("Max", True)

# 2. Gael: stessa macchina, ma il nome e' un altro
c_gael = esamina("Gael", False)

# 3. Neri
c_neri = esamina("Neri", False)

# 4. il caso peggiore: Gael su una macchina dove il file privato NON esiste proprio
vero = m.DOTTRINA_RISERVATA
m.DOTTRINA_RISERVATA = vero + ".inesistente"
c_gael2 = esamina("Gael", False)
m.DOTTRINA_RISERVATA = vero

print("\n" + "=" * 58)
print("Max riceve %d byte, Gael %d. Differenza = la dottrina riservata: %d byte."
      % (len(c_max.encode()), len(c_gael.encode()), len(c_max.encode()) - len(c_gael.encode())))
print("TUTTE LE PROVE PASSATE.")
