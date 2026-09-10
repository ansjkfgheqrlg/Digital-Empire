# -*- coding: utf-8 -*-
"""
gate_siti.py — il gate che CLAUDE-SITI.md §9 nomina.

Perche' esiste. Dal 2026-09-06 la legge dice "una consegna che non passa
scripts/gate_siti.py non e' consegnata". Il 2026-09-10 quel file non esisteva:
la legge nominava un giudice che non era mai stato nominato. Questo lo nomina —
non tutto, e lo dichiara: implementa i controlli che nascono dallo studio del
metodo di Andrei Pascu (SINTESI-METODO.md §5, "Lucida solo dove si convince, e
lascia i difetti dove si transita") e stampa in chiaro quali dei dieci controlli
del canone restano debito della Fase 4.

I quattro controlli vivi sono le TRE COSE DA FARE MEGLIO DI LUI
(SINTESI-METODO.md, sezione omonima) piu' l'anno scritto a mano:

  CASSA      la cassa deve risolvere      scelta di Digital Empire  (ADR-024 c.8)
  PREZZO     il prezzo si legge           scelta di Digital Empire  (ADR-024 c.7)
  IMMAGINE   il numero non sta in un'immagine muta                  (ADR-024 c.6)
  PROVE      le prove si verificano       scelta di Digital Empire  (nuovo, §14)
  ANNO       nessun anno scritto a mano                             (ADR-024 c.5)

"Scelta di Digital Empire" significa: non e' una cosa che lui fa e noi copiamo.
E' una cosa che lui NON fa, misurata addosso a lui, e che noi facciamo apposta.

Uso:
  python .claude/skills/fabbrica-siti/scripts/gate_siti.py <cartella-o-file.html>

Esce 0 se PASS, 1 se FAIL. I WARN non fanno fallire. Nessuna emoji: console cp1252.
"""
import io
import json
import os
import re
import sys

try:
    from html import unescape          # py3
except ImportError:                    # pragma: no cover
    from HTMLParser import HTMLParser  # py2
    unescape = HTMLParser().unescape

QUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(QUI)
CANONE_JSON = os.path.join(SKILL, "canone", "canone.json")

# Quali gate del canone questo script sa davvero controllare, oggi.
# La mappa e' qui e non in un commento perche' viene STAMPATA: il debito si
# dichiara a ogni esecuzione, non si scopre leggendo il sorgente.
GATE_IMPLEMENTATI = {
    "6_accessibilita": "parziale - solo alt delle immagini (controllo IMMAGINE)",
    "8_meta_e_dati_strutturati": "parziale - solo i link interni che devono risolvere (controllo CASSA)",
}

COMMENTI = re.compile(r"<!--.*?-->", re.S)
SCRIPT = re.compile(r"<script\b.*?</script>", re.S | re.I)
STYLE_BLOCCO = re.compile(r"<style\b[^>]*>(.*?)</style>", re.S | re.I)
TAG = re.compile(r"<[^>]+>", re.S)
HREF = re.compile(r"""<a\b[^>]*\bhref\s*=\s*["']([^"']+)["'][^>]*>""", re.I)
IMG = re.compile(r"<img\b[^>]*>", re.I)
ATTR_ALT = re.compile(r"""\balt\s*=\s*["']([^"']*)["']""", re.I)
ANNO = re.compile(r"\b(19|20)\d{2}\b")
VALUTA = re.compile(r"(\d[\d.\s]*(?:[.,]\d{2})?)\s*(?:&euro;|€|EUR\b)", re.I)
PX = re.compile(r"(-?\d+(?:\.\d+)?)px")

MARCA_PROVA = re.compile(
    r"""class\s*=\s*["'][^"']*\b(prova|prove|testimon\w*|recension\w*|review\w*|social-proof)\b""",
    re.I)
NOME_CASSA = re.compile(r"(cassa|checkout|pagamento|-pre\b|pre-)", re.I)


def leggi(path):
    with io.open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def testo_visibile(html):
    """Solo cio' che un lettore vede: via commenti, script, style e tag."""
    h = COMMENTI.sub(" ", html)
    h = SCRIPT.sub(" ", h)
    h = re.sub(r"<style\b.*?</style>", " ", h, flags=re.S | re.I)
    h = TAG.sub(" ", h)
    # Le entita' si sciolgono: "47,00&nbsp;&euro;" e' un prezzo per chi legge, e
    # deve esserlo anche per il gate. Senza questo passo il controllo PREZZO
    # guarda una pagina diversa da quella che vede il cliente.
    return unescape(h)


def righe_visibili(html):
    """Come testo_visibile, ma tenendo il numero di riga (per i WARN)."""
    h = COMMENTI.sub(lambda m: "\n" * m.group(0).count("\n"), html)
    h = SCRIPT.sub(lambda m: "\n" * m.group(0).count("\n"), h)
    h = re.sub(r"<style\b.*?</style>",
               lambda m: "\n" * m.group(0).count("\n"), h, flags=re.S | re.I)
    fuori = []
    for i, r in enumerate(h.split("\n"), 1):
        fuori.append((i, unescape(TAG.sub(" ", r))))
    return fuori


def pavimento_font(valore):
    """Il corpo minimo garantito da una dichiarazione font-size.

    clamp(14px, calc(...), 17px) -> 14. 16px -> 16. Unita' relative: ignorate,
    perche' senza render non si sa a cosa si riferiscono e un gate non indovina.
    """
    v = valore.strip()
    if v.startswith("clamp"):
        dentro = v[v.find("(") + 1:]
        primo = dentro.split(",")[0]
        m = PX.search(primo)
        return float(m.group(1)) if m else None
    m = PX.fullmatch(v) or PX.search(v)
    if m and "calc" not in v:
        return float(m.group(1))
    return None


def regole_css(html):
    """[(selettori, pavimento_font_size)] da tutti i blocchi <style> della pagina."""
    fuori = []
    for blocco in STYLE_BLOCCO.findall(html):
        blocco = re.sub(r"/\*.*?\*/", " ", blocco, flags=re.S)
        # niente parser CSS: si spezza sulle graffe, che per un file di pagina basta
        for pezzo in blocco.split("}"):
            if "{" not in pezzo:
                continue
            sel, corpo = pezzo.split("{", 1)
            m = re.search(r"font-size\s*:\s*([^;]+);", corpo + ";")
            if not m:
                continue
            fuori.append((sel.strip(), pavimento_font(m.group(1))))
    return fuori


# --------------------------------------------------------------------- CASSA
def controllo_cassa(pagine, radice):
    """La cassa deve risolvere. SCELTA DI DIGITAL EMPIRE.

    Difetto misurato addosso al concorrente (ADR-024, controllo 8): /vendita manda
    a /acquista-v101 che e' un 404, e la cassa vera non e' linkata da nessuna parte.
    Un lancio con la pagina di vendita viva e la cassa irraggiungibile perde ogni
    euro che il copy ha guadagnato, e nessuno se ne accorge.
    """
    errori, avvisi = [], []
    esistenti = {os.path.normcase(os.path.abspath(p)) for p in pagine}
    entranti = {}   # pagina -> quante altre pagine la linkano

    for p in pagine:
        entranti.setdefault(os.path.normcase(os.path.abspath(p)), 0)

    for p in pagine:
        html = COMMENTI.sub(" ", leggi(p))
        base = os.path.dirname(os.path.abspath(p))
        for href in HREF.findall(html):
            h = href.strip()
            if h.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:", "data:")):
                if h.startswith(("http://", "https://")):
                    avvisi.append("%s - link esterno non verificabile offline: %s"
                                  % (os.path.relpath(p, radice), h))
                continue
            pulito = h.split("#")[0].split("?")[0]
            if not pulito:
                continue
            bersaglio = os.path.normcase(os.path.abspath(os.path.join(base, pulito)))
            if os.path.isdir(bersaglio):
                bersaglio = os.path.normcase(os.path.join(bersaglio, "index.html"))
            if not os.path.exists(bersaglio):
                errori.append("%s - CASSA: il link \"%s\" non risolve (nessun file a quel percorso)"
                              % (os.path.relpath(p, radice), h))
            elif bersaglio in entranti and bersaglio != os.path.normcase(os.path.abspath(p)):
                entranti[bersaglio] += 1

    for p in pagine:
        chiave = os.path.normcase(os.path.abspath(p))
        html = leggi(p)
        e_cassa = bool(NOME_CASSA.search(os.path.basename(p))) or ("data-cassa-page" in html)
        if e_cassa and entranti.get(chiave, 0) == 0 and len(pagine) > 1:
            errori.append("%s - CASSA: e' una pagina di cassa e nessuna pagina del cantiere ci "
                          "arriva (difetto /vendita101-pre, ADR-024 c.8)" % os.path.relpath(p, radice))
    return errori, avvisi


# -------------------------------------------------------------------- PREZZO
def controllo_prezzo(path, html, radice):
    """Il prezzo si legge. SCELTA DI DIGITAL EMPIRE.

    Difetto misurato (ADR-024, controllo 7): sulla pagina madre del lancio la cifra
    che si paga sta a 14,88px, piu' piccola del corpo delle FAQ (16,5px), mentre
    "Risparmi 585 EUR" sta a 81,6px. La cifra che eccita e' 5,5 volte quella che
    addebita. Qui: il prezzo dichiara chi e' (data-prezzo) e non e' mai piu' piccolo
    del testo di servizio.
    """
    errori, avvisi = [], []
    rel = os.path.relpath(path, radice)
    # I commenti si tolgono PRIMA di cercare il marcatore: un commento che spiega
    # data-prezzo non e' un elemento marcato, ed e' il primo modo in cui questo
    # controllo si prende in giro da solo (trovato al collaudo, 2026-09-10).
    html = COMMENTI.sub(" ", html)
    ha_marcatore = "data-prezzo" in html
    testo = testo_visibile(html)
    ha_cifra = bool(VALUTA.search(testo))

    if ha_cifra and not ha_marcatore:
        avvisi.append("%s - PREZZO: c'e' una cifra in valuta ma nessun elemento marcato "
                      "data-prezzo: il gate non puo' misurare cio' che non e' dichiarato" % rel)
        return errori, avvisi
    if not ha_marcatore:
        return errori, avvisi

    # classi dell'elemento che porta data-prezzo
    m = re.search(r"<[^>]*\bdata-prezzo\b[^>]*>", html, re.I)
    classi = []
    if m:
        c = re.search(r"""\bclass\s*=\s*["']([^"']+)["']""", m.group(0), re.I)
        if c:
            classi = c.group(1).split()

    regole = regole_css(html)
    pav_prezzo = None
    for sel, pav in regole:
        if pav is None:
            continue
        for cl in classi:
            if ("." + cl) in sel:
                pav_prezzo = pav if pav_prezzo is None else min(pav_prezzo, pav)

    if pav_prezzo is None:
        avvisi.append("%s - PREZZO: elemento data-prezzo trovato ma nessuna regola CSS in pagina "
                      "ne fissa il corpo: non misurabile qui" % rel)
        return errori, avvisi

    servizio = re.compile(r"legal|faq|nota|note|footnote|servizio|piede|footer|disclaimer", re.I)
    for sel, pav in regole:
        if pav is None or not servizio.search(sel):
            continue
        if pav_prezzo < pav:
            errori.append("%s - PREZZO: la cifra che si paga e' %gpx, il testo di servizio "
                          "\"%s\" e' %gpx. Il prezzo non e' mai il testo piu' piccolo (ADR-024 c.7)"
                          % (rel, pav_prezzo, sel.strip()[:40], pav))
    return errori, avvisi


# ------------------------------------------------------------------ IMMAGINE
def controllo_immagine(path, html, radice):
    """Nessun numero critico dentro un'immagine muta (ADR-024, controllo 6).

    Difetto misurato: il prezzo di outEmail, 139 EUR, e' un'immagine con alt=""
    su entrambe le versioni. Un lettore di schermo non lo sente, un motore non lo
    indicizza, e nessun test automatico se ne accorge. Questo se ne accorge.
    """
    errori = []
    rel = os.path.relpath(path, radice)
    for tag in IMG.findall(COMMENTI.sub(" ", html)):
        m = ATTR_ALT.search(tag)
        decorativa = ('aria-hidden="true"' in tag.lower()) or ('role="presentation"' in tag.lower())
        if m is None:
            errori.append("%s - IMMAGINE: <img> senza attributo alt (ADR-024 c.6)" % rel)
        elif not m.group(1).strip() and not decorativa:
            errori.append("%s - IMMAGINE: <img> con alt vuoto e non dichiarata decorativa "
                          "(aria-hidden o role=presentation). Se dentro c'e' un numero, "
                          "quel numero non esiste per nessuno (ADR-024 c.6)" % rel)
    return errori


# --------------------------------------------------------------------- PROVE
def controllo_prove(path, html, radice):
    """Le prove si verificano. SCELTA DI DIGITAL EMPIRE.

    Misura che la impone (SINTESI-METODO.md §6): il concorrente ha due regimi di
    prova sociale — un widget Trustpilot vero (4,9/5, 98 recensioni, badge
    "Verificata", nomi reali) sul prodotto d'ingresso, e 42 screenshot caricati a
    mano con alt="" e zero fonte esterna sul prodotto caro. Il regime debole sta
    dove il denaro e' piu' grande.

    La nostra regola: se una testimonianza non e' controllabile da un estraneo, non
    e' prova, e' decorazione. Un blocco di prova deve portare almeno una di queste
    tre cose: un link alla fonte, un <cite>, o un attributo data-fonte.
    """
    errori = []
    rel = os.path.relpath(path, radice)
    pulito = COMMENTI.sub(" ", html)

    posizioni = [m.start() for m in MARCA_PROVA.finditer(pulito)]
    posizioni += [m.start() for m in re.finditer(r"<blockquote\b", pulito, re.I)]
    posizioni = sorted(set(posizioni))

    for i, p in enumerate(posizioni):
        fine = posizioni[i + 1] if i + 1 < len(posizioni) else min(len(pulito), p + 1500)
        blocco = pulito[p:fine]
        ha_fonte = ("data-fonte" in blocco.lower()
                    or "<cite" in blocco.lower()
                    or re.search(r"""<a\b[^>]*href\s*=\s*["']https?://""", blocco, re.I))
        if not ha_fonte:
            riga = pulito[:p].count("\n") + 1
            errori.append("%s:%d - PROVE: blocco di prova sociale senza fonte controllabile "
                          "(serve un link esterno, un <cite> o data-fonte). Una prova che un "
                          "estraneo non puo' verificare e' decorazione" % (rel, riga))
    return errori


# ---------------------------------------------------------------------- ANNO
def controllo_anno(path, html, radice):
    """Nessun anno scritto a mano nel copy (ADR-024, controllo 5). Sempre WARN.

    Difetto misurato: la pagina prodotto viva dice "E adesso, nel 2025", la sua
    copia di lancio catturata lo stesso giorno dice "nel 2026". Si e' aggiornata
    solo la copia. Il difetto si ripresenta a ogni capodanno, da solo.
    """
    avvisi = []
    rel = os.path.relpath(path, radice)
    for n, riga in righe_visibili(html):
        for m in ANNO.finditer(riga):
            avvisi.append("%s:%d - ANNO: \"%s\" scritto a mano nel testo. Una pagina che vende "
                          "tutto l'anno invecchia da sola (ADR-024 c.5)" % (rel, n, m.group(0)))
    return avvisi


def raccogli(bersaglio):
    if os.path.isfile(bersaglio):
        return [bersaglio], os.path.dirname(os.path.abspath(bersaglio)) or "."
    pagine = []
    for radice, _dirs, file in os.walk(bersaglio):
        if "node_modules" in radice or os.sep + "." in radice:
            continue
        for f in sorted(file):
            if f.lower().endswith((".html", ".htm")):
                pagine.append(os.path.join(radice, f))
    return pagine, os.path.abspath(bersaglio)


def main(argv):
    if len(argv) < 2:
        print("USO: python gate_siti.py <cartella-cantiere | pagina.html>")
        return 2
    bersaglio = argv[1]
    if not os.path.exists(bersaglio):
        print("FAIL - non esiste: %s" % bersaglio)
        return 1

    pagine, radice = raccogli(bersaglio)
    if not pagine:
        print("FAIL - nessuna pagina .html trovata in %s" % bersaglio)
        return 1

    errori, avvisi = [], []
    e, a = controllo_cassa(pagine, radice)
    errori += e
    avvisi += a
    for p in pagine:
        html = leggi(p)
        e, a = controllo_prezzo(p, html, radice)
        errori += e
        avvisi += a
        errori += controllo_immagine(p, html, radice)
        errori += controllo_prove(p, html, radice)
        avvisi += controllo_anno(p, html, radice)

    print("GATE SITI - Fabbrica Siti (legge CLAUDE-SITI.md §9 e §14)")
    print("  bersaglio       : %s" % bersaglio)
    print("  pagine lette    : %d" % len(pagine))
    print("  controlli vivi  : CASSA - PREZZO - IMMAGINE - PROVE - ANNO")

    # Il debito si dichiara, non si nasconde.
    try:
        canone = json.loads(leggi(CANONE_JSON))
        mancanti = [g for g in sorted(canone.get("gate", {})) if g not in GATE_IMPLEMENTATI]
        print("  ancora debito   : %d dei gate del canone (Fase 4) - %s"
              % (len(mancanti), ", ".join(mancanti)))
    except Exception as exc:                                   # pragma: no cover
        print("  ancora debito   : canone.json non leggibile (%s)" % exc)

    if avvisi:
        print("\n  WARN - %d:" % len(avvisi))
        for w in avvisi:
            print("    - " + w)

    if errori:
        print("\n  FAIL - %d:" % len(errori))
        for x in errori:
            print("    - " + x)
        print("\n  Una consegna che non passa questo gate non e' consegnata (§9).")
        return 1

    print("\n  PASS - i cinque controlli vivi non hanno trovato niente.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
