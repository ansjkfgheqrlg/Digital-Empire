# -*- coding: utf-8 -*-
"""
corpus_blog.py — l'onda F: il corpus del blog, preso dalla sitemap viva.

Il Passo 0 aveva CONTATO 105 articoli e non aveva SALVATO l'elenco: un numero
senza la sua lista non si puo' verificare. Questo script lo prende, lo salva e
ne misura la forma dei titoli — che e' il vero oggetto di studio del corpus.

Uso:
    python corpus_blog.py            scarica, salva corpus.json e stampa il conto
    python corpus_blog.py --offline  rilegge corpus.json senza toccare la rete
"""
import argparse
import io
import json
import os
import re
import sys
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUORI = os.path.join(BASE, "capture", "_corpus-blog")
SITEMAPS = [
    "https://www.andrei-copy.com/sitemap.xml",
]
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DigitalEmpire-study/1.0"}


def scarica(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def raccogli():
    visti, urls = set(), []
    coda = list(SITEMAPS)
    while coda:
        u = coda.pop(0)
        if u in visti:
            continue
        visti.add(u)
        try:
            xml = scarica(u)
        except Exception as e:
            print("[X] {} -> {}".format(u, e))
            continue
        # una sitemap di sitemap rimanda ad altre sitemap
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml):
            if loc.endswith(".xml"):
                coda.append(loc)
            else:
                urls.append(loc)
        print("[ok] {} -> {} loc".format(u.split("/")[-1], len(urls)))
    return sorted(set(urls))


def slug_titolo(u):
    """Il titolo leggibile ricavato dallo slug: e' cio' che il lettore vede in SERP."""
    s = u.rstrip("/").split("/")[-1]
    return s.replace("-", " ").strip()


def misura(articoli):
    """La forma dei titoli: e' il corpus, non le singole parole."""
    numeri = [a for a in articoli if re.search(r"\b\d+\b", a["titolo"])]
    domande = [a for a in articoli if re.match(
        r"^(come|cosa|perche|quando|quale|quanto|chi|dove|e)\b", a["titolo"], re.I)]
    parole = [len(a["titolo"].split()) for a in articoli] or [0]
    frequenze = {}
    for a in articoli:
        for p in re.findall(r"[a-zàèéìòù]{4,}", a["titolo"].lower()):
            frequenze[p] = frequenze.get(p, 0) + 1
    return {
        "totale": len(articoli),
        "con_numero": len(numeri),
        "domanda_o_come": len(domande),
        "parole_min": min(parole),
        "parole_max": max(parole),
        "parole_medie": round(sum(parole) / max(len(parole), 1), 1),
        "parole_piu_usate": sorted(frequenze.items(), key=lambda x: -x[1])[:25],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    a = ap.parse_args()
    os.makedirs(FUORI, exist_ok=True)
    fuori = os.path.join(FUORI, "corpus.json")

    if a.offline:
        with io.open(fuori, encoding="utf-8") as f:
            dati = json.load(f)
    else:
        urls = raccogli()
        # DIFETTO TROVATO IL 2026-09-09: la prima versione contava come "articoli" anche
        # /blog/category/... e /blog/tag/... -- 67 su 104. Il numero era falso del 64%,
        # e un numero falso e' peggio di nessun numero: le misure sui titoli finivano
        # calcolate su nomi di categoria. Ora si separano.
        blog = [u for u in urls if "/blog/" in u]
        indici = [u for u in blog if "/blog/category/" in u or "/blog/tag/" in u]
        articoli = [u for u in blog if u not in indici]
        altro = [u for u in urls if "/blog/" not in u]
        dati = {
            "preso_il": "2026-09-09",
            "url_totali": len(urls),
            "articoli": [{"url": u, "titolo": slug_titolo(u)} for u in articoli],
            "indici_tag_e_categoria": indici,
            "non_blog": altro,
        }
        dati["misure"] = misura(dati["articoli"])
        with io.open(fuori, "w", encoding="utf-8", newline="\n") as f:
            json.dump(dati, f, ensure_ascii=False, indent=2)

    m = dati["misure"]
    print("\nCORPUS DEL BLOG - contato sulla sitemap viva")
    print("=" * 60)
    print("  url totali nella sitemap : {}".format(dati["url_totali"]))
    print("  articoli di blog VERI    : {}".format(m["totale"]))
    print("  indici tag/categoria     : {}  (NON sono articoli)".format(
        len(dati.get("indici_tag_e_categoria", []))))
    print("  pagine non-blog          : {}".format(len(dati["non_blog"])))
    print("  titoli con un numero     : {} ({:.0f}%)".format(
        m["con_numero"], 100.0 * m["con_numero"] / max(m["totale"], 1)))
    print("  titoli domanda/come      : {} ({:.0f}%)".format(
        m["domanda_o_come"], 100.0 * m["domanda_o_come"] / max(m["totale"], 1)))
    print("  parole per titolo        : min {} · media {} · max {}".format(
        m["parole_min"], m["parole_medie"], m["parole_max"]))
    print("  parole piu' usate        : " + ", ".join(
        "{}({})".format(p, n) for p, n in m["parole_piu_usate"][:12]))
    print("\n  salvato in: {}".format(os.path.relpath(fuori, BASE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
