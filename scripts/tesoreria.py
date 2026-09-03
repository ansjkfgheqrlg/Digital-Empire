# -*- coding: utf-8 -*-
"""
TESORERIA - il reparto che conta i soldi di Digital Empire.

Il fatto che l'ha resa necessaria
---------------------------------
Misurato il 2026-09-03: Digital Empire non misurava un solo euro. Ne' incassi, ne'
costi effettivi, ne' una metrica del percorso di vendita. Il direttore finanziario
sorvegliava le spese di un'azienda che non aveva mai contato un ricavo; lo stato
della pipeline commerciale era un'opinione. E' la ragione per cui nessuno si era
accorto che il magazzino era pieno di lavoro finito e le vendite erano zero
(voce B-043, ADR-016).

Cosa fa
-------
Registra ogni euro che entra e ogni euro che esce, e produce il rapporto in
qualunque momento: cassa, per motore di business, per mese, previsto contro
incassato, margine, autonomia residua.

Come tiene i dati
-----------------
Due file di testo ad accodamento (JSONL), uno per riga, in company/Memory/tesoreria/.
Scelta voluta: si leggono a occhio, si correggono a mano, e due soci che lavorano in
parallelo non si sovrascrivono a vicenda quando le loro modifiche si fondono.
Niente database: un database che nessuno sa aprire e' un altro posto dove i numeri
vanno a nascondersi.

Uso:
    python scripts/tesoreria.py entrata --importo 1500 --da "Concessionario X" \\
        --per agency --stato incassato --nota "sprint CRO gennaio"
    python scripts/tesoreria.py spesa --importo 20 --a "Anthropic" \\
        --categoria strumenti --ricorrente --nota "abbonamento"
    python scripts/tesoreria.py report
    python scripts/tesoreria.py report --mese 2026-09
    python scripts/tesoreria.py report --scrivi
    python scripts/tesoreria.py incassa --id E-20260903-001

Console Windows: solo ASCII in output.
"""

import os
import io
import sys
import json
import argparse
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "company", "Memory", "tesoreria")
ENTRATE = os.path.join(CARTELLA, "entrate.jsonl")
SPESE = os.path.join(CARTELLA, "spese.jsonl")
RAPPORTO = os.path.join(RADICE, "company", "Memory", "TESORERIA.md")

# I motori di business dell'Impero. Ogni euro appartiene a uno di questi:
# senza questo campo non si sa mai QUALE parte dell'azienda guadagna davvero,
# ed e' l'unica domanda che conta quando si decide dove mettere le ore.
MOTORI = ["agency", "kdp", "corsi", "youtube", "instagram", "saas",
          "formazione-az", "altro"]

# Stato di un'entrata. La distinzione non e' burocrazia: un preventivo mandato e
# un bonifico arrivato sono due cose diverse, e confonderle e' il modo classico
# di credersi ricchi mentre il conto e' vuoto.
STATI = ["previsto", "fatturato", "incassato", "perso"]

CATEGORIE_SPESA = ["strumenti", "pubblicita", "collaboratori", "tasse",
                   "servizi", "hardware", "formazione", "altro"]


def assicura_cartella():
    os.makedirs(CARTELLA, exist_ok=True)
    guida = os.path.join(CARTELLA, "README.md")
    if not os.path.exists(guida):
        testo = (
            "# Tesoreria - i dati veri\n"
            "\n"
            "Due file ad accodamento, una riga per movimento:\n"
            "\n"
            "- `entrate.jsonl` - ogni euro che entra o che dovrebbe entrare\n"
            "- `spese.jsonl` - ogni euro che esce\n"
            "\n"
            "Si scrivono con `python scripts/tesoreria.py` e si leggono a occhio.\n"
            "Si possono correggere a mano: sono testo, una riga per movimento.\n"
            "\n"
            "**Non cancellare righe.** Un movimento sbagliato si corregge\n"
            "aggiungendone uno di segno opposto con la nota che spiega perche':\n"
            "la storia dei soldi non si riscrive, si annota.\n"
        )
        with io.open(guida, "w", encoding="utf-8", newline="\n") as f:
            f.write(testo)


def leggi(percorso):
    """Le righe illeggibili non fermano il conto: si saltano e si contano."""
    fuori = []
    rotte = 0
    if not os.path.exists(percorso):
        return fuori, rotte
    with io.open(percorso, encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            try:
                fuori.append(json.loads(riga))
            except ValueError:
                rotte += 1
    return fuori, rotte


def accoda(percorso, voce):
    assicura_cartella()
    with io.open(percorso, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(voce, ensure_ascii=False) + "\n")


def prossimo_id(percorso, lettera):
    voci, _ = leggi(percorso)
    oggi = datetime.now().strftime("%Y%m%d")
    n = sum(1 for v in voci if v.get("id", "").startswith("%s-%s" % (lettera, oggi)))
    return "%s-%s-%03d" % (lettera, oggi, n + 1)


# --------------------------------------------------------------------------
# SCRITTURA
# --------------------------------------------------------------------------

def registra_entrata(a):
    voce = {
        "id": prossimo_id(ENTRATE, "E"),
        "data": a.data or datetime.now().strftime("%Y-%m-%d"),
        "importo": round(float(a.importo), 2),
        "valuta": a.valuta,
        "da": a.da,
        "motore": a.per,
        "stato": a.stato,
        "nota": a.nota or "",
        "registrato": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    accoda(ENTRATE, voce)
    print("Registrata entrata %s: %.2f %s da %s (%s, %s)"
          % (voce["id"], voce["importo"], voce["valuta"], voce["da"],
             voce["motore"], voce["stato"]))
    if voce["stato"] == "previsto":
        print("  NOTA: e' PREVISTA, non incassata. Quando arrivano i soldi:")
        print("        python scripts/tesoreria.py incassa --id %s" % voce["id"])


def registra_spesa(a):
    voce = {
        "id": prossimo_id(SPESE, "S"),
        "data": a.data or datetime.now().strftime("%Y-%m-%d"),
        "importo": round(float(a.importo), 2),
        "valuta": a.valuta,
        "a": getattr(a, "a_chi"),
        "categoria": a.categoria,
        "motore": a.per,
        "ricorrente": bool(a.ricorrente),
        "nota": a.nota or "",
        "registrato": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    accoda(SPESE, voce)
    r = " (ricorrente, ogni mese)" if voce["ricorrente"] else ""
    print("Registrata spesa %s: %.2f %s a %s [%s]%s"
          % (voce["id"], voce["importo"], voce["valuta"], voce["a"],
             voce["categoria"], r))


def segna_incassata(ident):
    """Non riscrive la riga vecchia: ne accoda una di rettifica.
    La storia dei soldi non si riscrive, si annota."""
    voci, _ = leggi(ENTRATE)
    orig = None
    for v in voci:
        if v.get("id") == ident:
            orig = v
    if orig is None:
        print("Nessuna entrata con identificativo %s." % ident)
        return
    if orig.get("stato") == "incassato":
        print("%s risulta gia' incassata il %s." % (ident, orig.get("data")))
        return
    nuova = dict(orig)
    nuova["stato"] = "incassato"
    nuova["rettifica_di"] = ident
    nuova["id"] = prossimo_id(ENTRATE, "E")
    nuova["data"] = datetime.now().strftime("%Y-%m-%d")
    nuova["nota"] = (orig.get("nota", "") + " | incassata davvero").strip(" |")
    nuova["registrato"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    accoda(ENTRATE, nuova)
    print("%s risulta ora incassata (%.2f %s da %s). Riga di rettifica: %s"
          % (ident, nuova["importo"], nuova["valuta"], nuova["da"], nuova["id"]))


# --------------------------------------------------------------------------
# LETTURA
# --------------------------------------------------------------------------

def entrate_effettive(voci):
    """Le rettifiche sostituiscono l'originale: si conta una volta sola."""
    sostituite = set(v["rettifica_di"] for v in voci if "rettifica_di" in v)
    return [v for v in voci if v.get("id") not in sostituite]


def filtra_mese(voci, mese):
    if not mese:
        return voci
    return [v for v in voci if str(v.get("data", "")).startswith(mese)]


def euro(x):
    return "{:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")


def calcola(mese=None):
    ent_grezze, rotte_e = leggi(ENTRATE)
    spe, rotte_s = leggi(SPESE)
    ent = filtra_mese(entrate_effettive(ent_grezze), mese)
    spe = filtra_mese(spe, mese)

    incassato = sum(v["importo"] for v in ent if v.get("stato") == "incassato")
    fatturato = sum(v["importo"] for v in ent if v.get("stato") == "fatturato")
    previsto = sum(v["importo"] for v in ent if v.get("stato") == "previsto")
    perso = sum(v["importo"] for v in ent if v.get("stato") == "perso")
    uscite = sum(v["importo"] for v in spe)
    ricorrenti = sum(v["importo"] for v in spe if v.get("ricorrente"))

    per_motore = {}
    for v in ent:
        m = v.get("motore", "altro")
        d = per_motore.setdefault(m, {"incassato": 0.0, "atteso": 0.0, "speso": 0.0})
        if v.get("stato") == "incassato":
            d["incassato"] += v["importo"]
        elif v.get("stato") in ("fatturato", "previsto"):
            d["atteso"] += v["importo"]
    for v in spe:
        m = v.get("motore", "altro")
        d = per_motore.setdefault(m, {"incassato": 0.0, "atteso": 0.0, "speso": 0.0})
        d["speso"] += v["importo"]

    per_categoria = {}
    for v in spe:
        c = v.get("categoria", "altro")
        per_categoria[c] = per_categoria.get(c, 0.0) + v["importo"]

    return {
        "mese": mese,
        "n_entrate": len(ent),
        "n_spese": len(spe),
        "incassato": incassato,
        "fatturato": fatturato,
        "previsto": previsto,
        "perso": perso,
        "uscite": uscite,
        "ricorrenti": ricorrenti,
        "cassa": incassato - uscite,
        "per_motore": per_motore,
        "per_categoria": per_categoria,
        "righe_rotte": rotte_e + rotte_s,
    }


def stampa_report(d):
    titolo = "TESORERIA - " + (("mese %s" % d["mese"]) if d["mese"] else "da sempre")
    print("")
    print("=" * 78)
    print("  " + titolo)
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 78)

    if d["n_entrate"] == 0 and d["n_spese"] == 0:
        print("")
        print("  NESSUN MOVIMENTO REGISTRATO.")
        print("")
        print("  Non significa che l'azienda non incassi e non spenda: significa")
        print("  che non lo sta ancora scrivendo da nessuna parte. E' esattamente")
        print("  il buco che questo reparto esiste per chiudere (voce B-043).")
        print("")
        print("  Il primo movimento si registra cosi':")
        print('    python scripts/tesoreria.py entrata --importo 1500 \\')
        print('        --da "Nome cliente" --per agency --stato incassato')
        print('    python scripts/tesoreria.py spesa --importo 20 \\')
        print('        --a "Anthropic" --categoria strumenti --ricorrente')
        print("")
        print("=" * 78)
        print("")
        return

    print("")
    print("  LA CASSA:")
    print("    entrato davvero      %14s EUR" % euro(d["incassato"]))
    print("    uscito               %14s EUR" % euro(d["uscite"]))
    print("    " + "-" * 33)
    segno = "+" if d["cassa"] >= 0 else ""
    print("    IN CASSA             %14s EUR" % (segno + euro(d["cassa"])))
    print("")
    print("  QUELLO CHE NON E' ANCORA ENTRATO:")
    print("    fatturato, da incassare  %10s EUR" % euro(d["fatturato"]))
    print("    previsto, non fatturato  %10s EUR" % euro(d["previsto"]))
    if d["perso"]:
        print("    perso per strada         %10s EUR" % euro(d["perso"]))
    print("")

    if d["ricorrenti"]:
        print("  SPESE CHE TORNANO OGNI MESE: %s EUR" % euro(d["ricorrenti"]))
        if d["ricorrenti"] > 0:
            mesi = d["cassa"] / d["ricorrenti"] if d["ricorrenti"] else 0
            print("    con la cassa di oggi, coperte per %.1f mesi" % mesi)
        print("")

    if d["per_motore"]:
        print("-" * 78)
        print("")
        print("  QUALE PARTE DELL'AZIENDA GUADAGNA DAVVERO")
        print("")
        print("  %-16s %13s %13s %13s %10s"
              % ("MOTORE", "ENTRATO", "ATTESO", "SPESO", "MARGINE"))
        print("  " + "-" * 68)
        righe = sorted(d["per_motore"].items(),
                       key=lambda kv: -(kv[1]["incassato"] - kv[1]["speso"]))
        for m, v in righe:
            marg = v["incassato"] - v["speso"]
            print("  %-16s %13s %13s %13s %10s"
                  % (m, euro(v["incassato"]), euro(v["atteso"]),
                     euro(v["speso"]), euro(marg)))
        print("")

    if d["per_categoria"]:
        print("-" * 78)
        print("")
        print("  DOVE SE NE VANNO I SOLDI")
        print("")
        for c, v in sorted(d["per_categoria"].items(), key=lambda kv: -kv[1]):
            quota = 100.0 * v / d["uscite"] if d["uscite"] else 0
            print("    %-18s %12s EUR   %5.1f%%" % (c, euro(v), quota))
        print("")

    if d["righe_rotte"]:
        print("-" * 78)
        print("  ATTENZIONE: %d righe illeggibili nei file dei movimenti."
              % d["righe_rotte"])
        print("  Sono state saltate: i totali qui sopra NON le comprendono.")
        print("")

    print("=" * 78)
    print("  %d entrate e %d spese registrate." % (d["n_entrate"], d["n_spese"]))
    print("=" * 78)
    print("")


def scrivi_report(d):
    r = []
    r.append("# TESORERIA - i conti di Digital Empire")
    r.append("")
    r.append("> Rigenerato da `scripts/tesoreria.py report --scrivi` il %s"
             % datetime.now().strftime("%Y-%m-%d %H:%M"))
    r.append("> Non modificare a mano: si riscrive a ogni esecuzione.")
    r.append("> I dati veri stanno in `company/Memory/tesoreria/`.")
    r.append("")

    if d["n_entrate"] == 0 and d["n_spese"] == 0:
        r.append("## Nessun movimento registrato")
        r.append("")
        r.append("Non significa che l'azienda non incassi e non spenda: significa che non")
        r.append("lo sta ancora scrivendo da nessuna parte. E' il buco che questo reparto")
        r.append("esiste per chiudere (voce **B-043**).")
        r.append("")
        with io.open(RAPPORTO, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(r) + "\n")
        return

    r.append("## La cassa")
    r.append("")
    r.append("| | EUR |")
    r.append("|---|---:|")
    r.append("| Entrato davvero | **%s** |" % euro(d["incassato"]))
    r.append("| Uscito | %s |" % euro(d["uscite"]))
    r.append("| **In cassa** | **%s** |" % euro(d["cassa"]))
    r.append("| Fatturato da incassare | %s |" % euro(d["fatturato"]))
    r.append("| Previsto non fatturato | %s |" % euro(d["previsto"]))
    if d["ricorrenti"]:
        r.append("| Spese che tornano ogni mese | %s |" % euro(d["ricorrenti"]))
    r.append("")

    if d["per_motore"]:
        r.append("## Quale parte dell'azienda guadagna davvero")
        r.append("")
        r.append("| Motore | Entrato | Atteso | Speso | Margine |")
        r.append("|---|---:|---:|---:|---:|")
        righe = sorted(d["per_motore"].items(),
                       key=lambda kv: -(kv[1]["incassato"] - kv[1]["speso"]))
        for m, v in righe:
            r.append("| `%s` | %s | %s | %s | **%s** |"
                     % (m, euro(v["incassato"]), euro(v["atteso"]),
                        euro(v["speso"]), euro(v["incassato"] - v["speso"])))
        r.append("")

    if d["per_categoria"]:
        r.append("## Dove se ne vanno i soldi")
        r.append("")
        r.append("| Categoria | EUR | Quota |")
        r.append("|---|---:|---:|")
        for c, v in sorted(d["per_categoria"].items(), key=lambda kv: -kv[1]):
            quota = 100.0 * v / d["uscite"] if d["uscite"] else 0
            r.append("| %s | %s | %.1f%% |" % (c, euro(v), quota))
        r.append("")

    if d["righe_rotte"]:
        r.append("> ATTENZIONE: %d righe illeggibili nei file dei movimenti, saltate."
                 % d["righe_rotte"])
        r.append("> I totali qui sopra non le comprendono.")
        r.append("")

    r.append("---")
    r.append("")
    r.append("*%d entrate e %d spese registrate.*" % (d["n_entrate"], d["n_spese"]))
    r.append("")

    with io.open(RAPPORTO, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")


def main():
    ap = argparse.ArgumentParser(
        description="Tesoreria - il reparto che conta i soldi di Digital Empire")
    sub = ap.add_subparsers(dest="comando")

    e = sub.add_parser("entrata", help="registra un euro che entra")
    e.add_argument("--importo", required=True)
    e.add_argument("--da", required=True, help="chi paga")
    e.add_argument("--per", default="altro", choices=MOTORI,
                   help="quale motore di business")
    e.add_argument("--stato", default="incassato", choices=STATI)
    e.add_argument("--valuta", default="EUR")
    e.add_argument("--data", help="AAAA-MM-GG (default: oggi)")
    e.add_argument("--nota", default="")

    s = sub.add_parser("spesa", help="registra un euro che esce")
    s.add_argument("--importo", required=True)
    s.add_argument("--a", required=True, dest="a_chi", help="a chi va")
    s.add_argument("--categoria", default="altro", choices=CATEGORIE_SPESA)
    s.add_argument("--per", default="altro", choices=MOTORI,
                   help="quale motore di business")
    s.add_argument("--ricorrente", action="store_true", help="torna ogni mese")
    s.add_argument("--valuta", default="EUR")
    s.add_argument("--data", help="AAAA-MM-GG (default: oggi)")
    s.add_argument("--nota", default="")

    i = sub.add_parser("incassa", help="un'entrata prevista e' arrivata davvero")
    i.add_argument("--id", required=True, dest="ident")

    rp = sub.add_parser("report", help="il rapporto")
    rp.add_argument("--mese", help="AAAA-MM per un mese solo")
    rp.add_argument("--scrivi", action="store_true",
                    help="scrive anche company/Memory/TESORERIA.md")

    a = ap.parse_args()

    if a.comando == "entrata":
        registra_entrata(a)
    elif a.comando == "spesa":
        registra_spesa(a)
    elif a.comando == "incassa":
        segna_incassata(a.ident)
    elif a.comando == "report" or a.comando is None:
        mese = getattr(a, "mese", None)
        d = calcola(mese)
        stampa_report(d)
        if getattr(a, "scrivi", False):
            scrivi_report(d)
            print("Rapporto scritto in: company/Memory/TESORERIA.md")
            print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
