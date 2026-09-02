#!/usr/bin/env python3
"""
Controllo pre-commit della memoria condivisa (B-009 + B-028).

Blocca DUE guasti che finora si scoprivano solo al merge, a ore di lavoro di
distanza da quando erano rimediabili:

  1. COLLISIONE DI ID CHECKPOINT — due sessioni parallele creano
     `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md` con lo stesso NNN.
     Successo storico: 5 volte (B-009). Il fix esiste da luglio
     (`python -m empire mem write`) ma nessuno lo usa, quindi qui non si
     "ricorda la regola": si blocca il commit.

  2. FINE-RIGA CRLF nei file di company/Memory — git li vede come file
     riscritti da capo (verificato: 100 righe cambiate invece di 12) e al
     merge non sa piu' cosa tenere. E' la forma esatta del guaio del
     2026-08-23, che stava per duplicare ~6500 righe di STATO-EMPIRE.md.

DIPENDENZE: nessuna oltre la stdlib e `git`. E' deliberato. Il controllo
precedente non veniva eseguito anche perche' moriva su `import yaml`: un
guardrail che puo' rompersi e' un guardrail che verra' disattivato.

Uso:
    python .githooks/check_memory.py            # controlla lo staged (pre-commit)
    python .githooks/check_memory.py --fix      # normalizza i CRLF e li ri-stagea
    python .githooks/check_memory.py --all      # controlla tutto il disco, non solo lo staged
"""
import argparse
import os
import re
import subprocess
import sys
from collections import defaultdict

CHECKPOINT_DIR = "company/Memory/checkpoints"
MEMORY_DIR = "company/Memory"
NOME_CP = re.compile(r"^CP-(\d{8})-(\d{3})\.md$")

ROSSO = "\033[31m"; GIALLO = "\033[33m"; VERDE = "\033[32m"; RESET = "\033[0m"
if os.name == "nt" and not os.environ.get("WT_SESSION"):
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleMode(
            ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        ROSSO = GIALLO = VERDE = RESET = ""

# La console di git-for-windows e' cp1252: qualunque carattere fuori da ASCII
# qui dentro fa morire il controllo mentre STA gia' segnalando un guasto, e il
# guasto passa. Successo davvero durante il test del 2026-08-27, ed e' la stessa
# forma di B-013. Percio': stdout tollerante + SOLO ASCII nei messaggi.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def git(*args, binary=False):
    """Esegue git e restituisce stdout. Stringa vuota se il comando fallisce."""
    try:
        r = subprocess.run(["git"] + list(args), capture_output=True, check=False)
    except FileNotFoundError:
        return b"" if binary else ""
    if r.returncode != 0:
        return b"" if binary else ""
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def identico_in_storia(path):
    """True se il file che sto committando e' IDENTICO a una versione gia' in storia
    git allo stesso percorso.

    PERCHE' ESISTE (2026-09-02, un'ora di commit bloccati):
    quando si integra il lavoro di un altro con un merge, il SUO checkpoint rientra
    nel commit di merge come file "aggiunto". Il controllo di collisione guardava solo
    il NOME e lo scambiava per due sessioni che avevano scelto lo stesso numero.
    Stesso nome + stesso contenuto = lo STESSO checkpoint, non una collisione: B-009
    e' due lavori diversi sullo stesso ID, e questo non lo e'.
    Il confronto e' sull'hash del blob, non sul testo: niente falsi negativi da CRLF.
    """
    mio = git("rev-parse", ":" + path).strip()
    if not mio:
        return False
    for commit in git("log", "--all", "--format=%H", "--", path).split()[:50]:
        if git("rev-parse", "%s:%s" % (commit, path)).strip() == mio:
            return True
    return False


def file_aggiunti_staged():
    """Solo i file NUOVI in staging (A). Modificare un checkpoint esistente e' lecito."""
    out = git("diff", "--cached", "--name-only", "--diff-filter=A", "-z")
    return [p for p in out.split("\0") if p]


def file_staged_tutti():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    return [p for p in out.split("\0") if p]


def checkpoint_gia_esistenti():
    """Ogni checkpoint mai aggiunto su QUALSIASI branch -> {nome: [dove]}.

    E' questo che intercetta il caso reale: due sessioni su due branch diversi.
    Guardare solo HEAD non basta, la collisione nasce proprio fuori da HEAD.
    """
    visti = defaultdict(set)
    # (a) tutti i branch/commit della storia
    out = git("log", "--all", "--diff-filter=A", "--format=%H", "--name-only",
              "--", CHECKPOINT_DIR)
    commit = None
    for riga in out.splitlines():
        riga = riga.strip()
        if not riga:
            continue
        if re.fullmatch(r"[0-9a-f]{40}", riga):
            commit = riga
            continue
        if riga.startswith(CHECKPOINT_DIR):
            visti[os.path.basename(riga)].add("storia git (%s)" % (commit or "?")[:8])
    # (b) file gia' presenti sul disco (anche non tracciati: l'altra sessione locale)
    if os.path.isdir(CHECKPOINT_DIR):
        for nome in os.listdir(CHECKPOINT_DIR):
            if NOME_CP.match(nome):
                visti[nome].add("disco")
    return visti


def ha_crlf(path):
    try:
        with open(path, "rb") as fh:
            return b"\r\n" in fh.read()
    except OSError:
        return False


def normalizza(path):
    with open(path, "rb") as fh:
        d = fh.read()
    if b"\r\n" not in d:
        return False
    with open(path, "wb") as fh:
        fh.write(d.replace(b"\r\n", b"\n"))
    return True


def controlla(fix=False, tutto=False):
    problemi = []
    avvisi = []

    # ------------------------------------------------ 1. collisioni checkpoint
    if tutto:
        nuovi = [os.path.join(CHECKPOINT_DIR, n).replace("\\", "/")
                 for n in os.listdir(CHECKPOINT_DIR)] if os.path.isdir(CHECKPOINT_DIR) else []
    else:
        nuovi = file_aggiunti_staged()

    nuovi_cp = [p for p in nuovi
                if p.replace("\\", "/").startswith(CHECKPOINT_DIR + "/")
                and NOME_CP.match(os.path.basename(p))]

    malformati = [p for p in nuovi
                  if p.replace("\\", "/").startswith(CHECKPOINT_DIR + "/")
                  and p.endswith(".md")
                  and not NOME_CP.match(os.path.basename(p))]
    for p in malformati:
        avvisi.append("nome fuori standard CP-YYYYMMDD-NNN.md: %s" % p)

    if nuovi_cp and not tutto:
        esistenti = checkpoint_gia_esistenti()
        for p in nuovi_cp:
            nome = os.path.basename(p)
            # "disco" e' il file che sto committando io: non e' una collisione
            dove = {d for d in esistenti.get(nome, set()) if d != "disco"}
            # Stesso nome MA stesso contenuto = lo stesso checkpoint che rientra da un
            # merge, non due sessioni in collisione. Vedi identico_in_storia().
            if dove and identico_in_storia(p):
                avvisi.append("%s rientra identico da un merge: non e' una collisione" % nome)
                dove = set()
            if dove:
                problemi.append(
                    "COLLISIONE ID CHECKPOINT: %s esiste gia' in %s.\n"
                    "        Due sessioni hanno scelto lo stesso numero (B-009, 5a volta).\n"
                    "        NON rinominarlo a mano: rigeneralo con l'ID libero vero:\n"
                    "            python -m empire mem write --kind checkpoint --view \\\n"
                    "                --title \"...\" --body - < il-tuo-testo.md"
                    % (nome, ", ".join(sorted(dove))))

    # doppioni dentro lo stesso commit
    conta = defaultdict(list)
    for p in nuovi_cp:
        conta[os.path.basename(p)].append(p)
    for nome, paths in conta.items():
        if len(paths) > 1:
            problemi.append("COLLISIONE nello stesso commit: %s aggiunto da %s"
                            % (nome, " e ".join(paths)))

    # ------------------------------------------------ 2. CRLF nella memoria
    candidati = (file_staged_tutti() if not tutto else
                 [os.path.join(r, f).replace("\\", "/")
                  for r, _, fs in os.walk(MEMORY_DIR) for f in fs])
    md_memory = [p for p in candidati
                 if p.replace("\\", "/").startswith(MEMORY_DIR + "/")
                 and p.endswith(".md") and os.path.exists(p)]
    sporchi = [p for p in md_memory if ha_crlf(p)]

    if sporchi and fix:
        for p in sporchi:
            if normalizza(p):
                git("add", "--", p)
        print("%s[fix]%s normalizzati a LF e ri-staged: %d file"
              % (VERDE, RESET, len(sporchi)))
        sporchi = [p for p in sporchi if ha_crlf(p)]

    for p in sporchi:
        problemi.append(
            "CRLF in un file di memoria: %s\n"
            "        Git lo vedra' come file riscritto da capo -> merge illeggibile\n"
            "        (e' cosi' che il 2026-08-23 stavano per duplicarsi ~6500 righe).\n"
            "        Correggi con:  python .githooks/check_memory.py --fix" % p)

    # ------------------------------------------------ esito
    for a in avvisi:
        print("%s[!]%s  %s" % (GIALLO, RESET, a))
    if problemi:
        print("\n%s==============================================================%s" % (ROSSO, RESET))
        print("%s  COMMIT BLOCCATO - memoria condivisa a rischio%s" % (ROSSO, RESET))
        print("%s==============================================================%s" % (ROSSO, RESET))
        for p in problemi:
            print("\n  %s[X]%s  %s" % (ROSSO, RESET, p))
        print("\n  (in emergenza: git commit --no-verify - ma stai committando il guasto)\n")
        return 1

    if nuovi_cp or md_memory:
        print("%s[OK]%s memoria: %d checkpoint nuovi, %d file .md, nessuna collisione, nessun CRLF"
              % (VERDE, RESET, len(nuovi_cp), len(md_memory)))
    return 0


def main():
    ap = argparse.ArgumentParser(description="Guardrail della memoria condivisa (B-009/B-028)")
    ap.add_argument("--fix", action="store_true", help="normalizza i CRLF e li ri-stagea")
    ap.add_argument("--all", action="store_true", help="controlla tutto il disco, non solo lo staged")
    args = ap.parse_args()
    try:
        return controlla(fix=args.fix, tutto=args.all)
    except Exception as e:
        # Un guardrail non deve MAI impedire di lavorare per un proprio bug.
        print("%s[!]%s check_memory non ha potuto girare (%s: %s) - commit permesso"
              % (GIALLO, RESET, type(e).__name__, e))
        return 0


if __name__ == "__main__":
    sys.exit(main())
