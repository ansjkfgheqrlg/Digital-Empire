#!/usr/bin/env python3
"""gate_solo_aggiunte.py — su un sito online si AGGIUNGE soltanto (CLAUDE-SITI §13, ADR-030).

Prova meccanica, in due parti, che una nuova build di un sito già online non tocca nulla di ciò
che il committente vede oggi:

  A. TESTO  — il testo visibile del LIVE (HTML senza <script>/<style>/tag, spazi normalizzati) deve
             essere contenuto, nello stesso ordine, nel testo della BUILD. difflib deve produrre solo
             opcode `equal` e `insert`: un `delete` o un `replace` = qualcosa che c'era è cambiato → FAIL.
  B. CODICE — `git diff --numstat <base>..HEAD -- <cartella>` : ogni file che ESISTEVA nel commit base
             può avere solo righe aggiunte (deleted == 0). File nuovi: liberi. File cancellati: FAIL.
             Facoltativa (serve `--base`).

Uso:
  python gate_solo_aggiunte.py --live https://sito.vercel.app --build agency-empire-landing/out/index.html
  python gate_solo_aggiunte.py --live <url> --build <html|url> --base <tag|commit> --cartella agency-empire-landing
  python gate_solo_aggiunte.py --live <url> --build <html> --pagina prenota/      # un'altra pagina (senza «/» iniziale su Git Bash)
  aggiungere --mostra per stampare i blocchi inseriti (cosa è stato aggiunto, in chiaro).

Exit 0 = PASS (solo aggiunte). Exit 1 = FAIL (qualcosa di esistente è stato toccato). Exit 2 = uso/rete.

Eccezioni ammesse dal gate — entrambe sono DEROGHE e vanno scritte nel checkpoint, mai date per default:
  `--ignora "regex"`   toglie dal confronto le stringhe che cambiano da sole (anno del copyright, hash di build).
  `--consenti "regex"` una riga del live che combacia con la regex PUÒ cambiare (replace) — serve per correggere
                       un refuso in una sezione aggiunta da noi; NON vale per il testo del committente e non
                       ammette mai un `delete`. Ogni riga consentita viene stampata come DEROGA.
"""
import argparse, difflib, io, pathlib, re, subprocess, sys, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

UA = {"User-Agent": "Mozilla/5.0 (gate_solo_aggiunte)"}


def leggi(sorgente: str) -> str:
    if re.match(r"^https?://", sorgente):
        with urllib.request.urlopen(urllib.request.Request(sorgente, headers=UA), timeout=40) as r:
            return r.read().decode("utf-8", errors="replace")
    return pathlib.Path(sorgente).read_text(encoding="utf-8", errors="replace")


def testo(html: str, ignora: str | None) -> list[str]:
    """Testo visibile, una frase per riga: via script/style/noscript/template/commenti, via i tag,
    entità comuni, spazi normalizzati. Spezzato sui tag di blocco così il diff lavora per blocchi."""
    h = re.sub(r"(?is)<(script|style|noscript|template)\b.*?</\1>", " ", html)
    # i commenti `<!-- -->` di React separano due nodi di testo SENZA spazio: si tolgono, non si
    # sostituiscono con uno spazio — altrimenti «65includono» e «65 includono» sembrerebbero uguali.
    h = re.sub(r"(?s)<!--.*?-->", "", h)
    h = re.sub(r"(?i)</?(p|div|section|article|header|footer|main|li|ul|ol|h[1-6]|br|tr|td|th|blockquote|figure|figcaption|nav|aside|dt|dd|label|button)\b[^>]*>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&#x27;", "'"), ("&#39;", "'"), ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">"), ("&apos;", "'")):
        h = h.replace(a, b)
    righe = []
    for r in h.split("\n"):
        r = re.sub(r"\s+", " ", r).strip()
        if ignora:
            r = re.sub(ignora, "", r).strip()
        if r:
            righe.append(r)
    return righe


def parte_a(live_righe, build_righe, mostra: bool, consenti: str | None = None) -> tuple[bool, list[str]]:
    sm = difflib.SequenceMatcher(a=live_righe, b=build_righe, autojunk=False)
    errori, inseriti, deroghe = [], [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        if op == "insert":
            inseriti.append((j1, build_righe[j1:j2]))
            continue
        if op == "replace" and consenti and all(re.search(consenti, r) for r in live_righe[i1:i2]):
            for r, n in zip(live_righe[i1:i2], build_righe[j1:j2]):
                deroghe.append(f"  DEROGA  «{r[:80]}» → «{n[:80]}»")
            continue
        # delete o replace: qualcosa del live non c'è più o è diverso
        for r in live_righe[i1:i2]:
            errori.append(f"  {op.upper():7} live[{i1}:{i2}] → «{r[:110]}»")
        if op == "replace":
            for r in build_righe[j1:j2]:
                errori.append(f"          build[{j1}:{j2}] ora dice «{r[:110]}»")
    if deroghe:
        print(f"\n— Righe cambiate SU DEROGA (--consenti): {len(deroghe)} — da dichiarare nel checkpoint")
        for d in deroghe:
            print(d)
    if mostra:
        print(f"\n— Blocchi inseriti: {len(inseriti)}")
        for pos, blocco in inseriti:
            print(f"  + @{pos}: {len(blocco)} righe · «{blocco[0][:90]}»" + (f" … «{blocco[-1][:60]}»" if len(blocco) > 1 else ""))
    return (not errori), errori


ARTEFATTI = re.compile(r"(\.tsbuildinfo$|(^|/)\.next/|(^|/)out/|(^|/)node_modules/)")


def parte_b(base: str, cartella: str) -> tuple[bool, list[str]]:
    """Ogni file esistente nel commit base: solo righe aggiunte. Gli artefatti di build (tsbuildinfo,
    .next/, out/) non sono sorgente e non contano: li riscrive la macchina, non l'agente."""
    esistenti = set(subprocess.run(["git", "ls-tree", "-r", "--name-only", base, "--", cartella], capture_output=True, text=True, encoding="utf-8").stdout.split())
    num = subprocess.run(["git", "diff", "--numstat", f"{base}..HEAD", "--", cartella], capture_output=True, text=True, encoding="utf-8").stdout
    errori = []
    for riga in num.splitlines():
        parti = riga.split("\t")
        if len(parti) != 3:
            continue
        add, dele, path = parti
        if ARTEFATTI.search(path) or path not in esistenti:
            continue  # file nuovo: libero
        if dele != "0" and dele != "-":
            errori.append(f"  {path}: -{dele} righe (file esistente nel base {base[:12]})")
    # file cancellati
    stato = subprocess.run(["git", "diff", "--name-status", f"{base}..HEAD", "--", cartella], capture_output=True, text=True, encoding="utf-8").stdout
    for riga in stato.splitlines():
        if riga.startswith("D\t") and not ARTEFATTI.search(riga):
            errori.append(f"  CANCELLATO: {riga.split(chr(9), 1)[1]}")
    return (not errori), errori


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--live", required=True, help="URL del sito online (il «prima»)")
    ap.add_argument("--build", required=True, help="HTML della build nuova: file (out/index.html) o URL di preview")
    ap.add_argument("--pagina", default="/", help="pagina da confrontare sul live e sul build-URL (default /)")
    ap.add_argument("--base", help="commit/tag che corrisponde al live: attiva la parte B (git)")
    ap.add_argument("--cartella", default=".", help="cartella del sito nel repo (parte B)")
    ap.add_argument("--ignora", help="regex di stringhe che cambiano da sole (deroga dichiarata)")
    ap.add_argument("--consenti", help="regex: righe del live (nostre) che possono cambiare — deroga dichiarata")
    ap.add_argument("--mostra", action="store_true", help="stampa i blocchi inseriti")
    a = ap.parse_args()
    # `--pagina prenota/` vale come `/prenota/` (Git Bash su Windows trasforma «/prenota/» in un path di sistema)
    a.pagina = "/" + a.pagina.lstrip("/")

    live_url = a.live.rstrip("/") + a.pagina
    build_src = a.build.rstrip("/") + a.pagina if re.match(r"^https?://", a.build) else a.build
    try:
        live_righe = testo(leggi(live_url), a.ignora)
        build_righe = testo(leggi(build_src), a.ignora)
    except Exception as e:  # rete o file
        print(f"ERRORE lettura: {e}")
        return 2

    print(f"gate_solo_aggiunte — live {live_url} ({len(live_righe)} righe di testo) vs build {build_src} ({len(build_righe)})")
    ok_a, err_a = parte_a(live_righe, build_righe, a.mostra, a.consenti)
    print(f"\nA. TESTO : {'PASS' if ok_a else 'FAIL'} — il testo del live {'è' if ok_a else 'NON è'} contenuto intatto nella build")
    for e in err_a[:40]:
        print(e)
    if len(err_a) > 40:
        print(f"  … e altre {len(err_a) - 40} righe")

    ok_b = True
    if a.base:
        ok_b, err_b = parte_b(a.base, a.cartella)
        print(f"\nB. CODICE: {'PASS' if ok_b else 'FAIL'} — file esistenti in {a.base}: {'solo righe aggiunte' if ok_b else 'righe rimosse o file cancellati'}")
        for e in err_b:
            print(e)
    else:
        print("\nB. CODICE: saltata (nessun --base)")

    esito = ok_a and ok_b
    print(f"\n=== {'PASS' if esito else 'FAIL'} — {'solo aggiunte' if esito else 'qualcosa di esistente è stato toccato: NON si deploya'} ===")
    return 0 if esito else 1


if __name__ == "__main__":
    sys.exit(main())
