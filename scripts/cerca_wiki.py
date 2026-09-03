# -*- coding: utf-8 -*-
"""
CERCA WIKI - la memoria di Digital Empire smette di essere cieca.

Il problema che risolve
-----------------------
Il second brain ha 1.837 pagine e si cerca solo per parola esatta: chi cerca
"quanto spesso pubblicare" non trova una nota che dice "cadenza dei contenuti",
anche se e' la stessa cosa. Risultato: l'Impero si dimentica cose che possiede.

Cosa fa questo script
---------------------
1. Costruisce un indice di tutte le pagine (titolo, collegamenti, corpo).
2. Normalizza l'italiano: minuscole, via gli accenti, taglia le desinenze
   (pubblicare/pubblicato/pubblicazione diventano la stessa radice).
3. Espande la domanda con un DIZIONARIO DEI SINONIMI DEL MESTIERE, scritto a
   mano sul vocabolario vero di Digital Empire.
4. Ordina i risultati per pertinenza e mostra la riga in cui compare la cosa.

Cosa NON e' - dichiarato, non nascosto
--------------------------------------
NON e' ricerca per significato vera (embeddings). Non ci sono modelli di
significato installati in casa, e mandare fuori 1.837 pagine private a un
servizio esterno e' una decisione di Max, non mia. Questo copre il caso pratico
che rompeva la ricerca - il sinonimo mancato - non la comprensione del senso.
Per la ricerca semantica vera resta aperta la voce B-040.

Uso:
    python scripts/cerca_wiki.py "quanto spesso pubblicare"
    python scripts/cerca_wiki.py "gestione obiezioni prezzo" --n 15
    python scripts/cerca_wiki.py --ricostruisci      rifa' l'indice da zero

Console Windows: solo ASCII in output.
"""

import os
import re
import io
import sys
import json
import time
import math
import argparse
import unicodedata
from collections import defaultdict

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(RADICE, "second-brain-vault", "wiki")
INDICE = os.path.join(RADICE, "second-brain-vault", "wiki", ".indice-ricerca.json")

# --------------------------------------------------------------------------
# IL DIZIONARIO DEI SINONIMI DEL MESTIERE
# Ogni riga e' un gruppo di parole che per Digital Empire vogliono dire la stessa
# cosa. Cercando una qualsiasi si trovano tutte le altre.
# Ampliarlo e' il modo piu' economico di rendere la memoria meno cieca.
# --------------------------------------------------------------------------
SINONIMI = [
    # ATTENZIONE, due errori gia' fatti e corretti il 2026-09-03:
    # 1) una parola deve stare in UN SOLO gruppo. Se compare in due, il secondo se
    #    la prende e il primo perde il suo sinonimo, in silenzio. Il controllo
    #    automatico piu' sotto ora lo impedisce.
    # 2) niente parole generiche ("quanto", "cosa", "modo"): stanno in mezza wiki
    #    e sporcano ogni ricerca invece di aiutarla.
    ["pubblicare", "caricare", "postare", "pubblicazione", "upload", "rilascio",
     "uscita", "consegna"],
    ["cadenza", "frequenza", "ritmo", "calendario", "programmazione", "quotidiano",
     "settimanale", "giornaliero"],
    ["cliente", "lead", "prospect", "acquirente", "committente"],
    ["copy", "persuasione", "copywriting", "headline", "titolo"],
    ["obiezione", "dubbio", "resistenza", "scusa", "perplessita"],
    ["prezzo", "costo", "tariffa", "pricing", "listino", "preventivo"],
    ["conversione", "vendita", "chiusura", "closing", "cro"],
    ["outreach", "freddo", "prospezione", "scraping", "liste"],
    ["agente", "scagnozzo", "subagent", "sentinella"],
    ["skill", "strumento", "competenza"],
    ["funnel", "imbuto", "percorso"],
    ["landing", "atterraggio", "sito", "web"],
    ["video", "filmato", "clip", "youtube", "montaggio"],
    ["libro", "ebook", "kdp", "manoscritto", "romanzo", "amazon"],
    ["carosello", "slide", "instagram"],
    ["memoria", "wiki", "conoscenza", "archivio", "formazione", "brain"],
    ["soldi", "cassa", "fatturato", "revenue", "incasso", "ricavi", "guadagno",
     "entrate", "profitto", "margine"],
    ["team", "squadra", "soci", "collaboratori"],
    ["errore", "sbaglio", "guasto", "bug", "falla", "difetto"],
    ["migliorare", "potenziare", "ottimizzare", "arricchire"],
    ["controllo", "revisione", "verifica", "audit", "gate", "guardiano"],
    ["automazione", "workflow", "pipeline", "automatizzare"],
    ["concorrente", "competitor", "rivale"],
    ["parolachiave", "keyword", "seo", "posizionamento", "ranking"],
    ["annuncio", "sponsorizzata", "campagna", "advertising"],
    ["testimonianza", "recensione", "casostudio", "proof"],
    ["chiamata", "appuntamento", "consulenza", "briefing"],
    ["email", "newsletter", "mailing"],
    ["corso", "lezione", "modulo", "didattica", "insegnamento"],
    ["decisione", "adr", "delibera"],
    ["societa", "srl", "forfettario", "fiscale", "tasse", "partitaiva"],
    ["investimento", "obbligazione", "btp", "rendita", "immobiliare", "affitto"],
]

# parole troppo comuni per dire qualcosa: si scartano
VUOTE = set("""
il lo la i gli le un uno una di a da in con su per tra fra del della dei delle
dal dalla al alla ai alle nel nella nei nelle sul sulla sui sulle e o ma se che
chi cui non piu meno molto poco tutto tutti tutte questo questa questi queste
quello quella quelli quelle come dove quando perche cosa come essere avere fare
sono sei siamo siete stato stata stati state ha hanno abbiamo avete puo possono
si ci vi mi ti ne li la le gli anche ancora gia sempre mai solo pure quindi
allora invece pero cioe ossia ovvero circa verso dopo prima durante mentre
the of and to in a for is on with as at by an be this that it or from
""".split())

DESINENZE = ["azioni", "azione", "amento", "amenti", "mente", "zioni", "zione",
             "ando", "endo", "arsi", "ersi", "irsi", "ata", "ate", "ati", "ato",
             "ita", "ite", "iti", "ito", "are", "ere", "ire", "ono", "ano",
             "che", "chi", "ghe", "ghi", "ie", "e", "i", "a", "o"]


def normalizza(parola):
    """Minuscolo, senza accenti, senza desinenza. Serve a far coincidere
    'pubblicazione', 'pubblicare' e 'pubblicato'."""
    p = unicodedata.normalize("NFKD", parola.lower())
    p = "".join(c for c in p if not unicodedata.combining(c))
    p = re.sub(r"[^a-z0-9]", "", p)
    if len(p) <= 4:
        return p
    for d in DESINENZE:
        if len(p) - len(d) >= 4 and p.endswith(d):
            return p[:-len(d)]
    return p


def costruisci_mappa_sinonimi():
    """Ogni radice punta al capogruppo, cosi' tutto il gruppo si trova insieme.

    Se la stessa parola compare in due gruppi, il secondo se la prende e il primo
    perde il suo sinonimo SENZA CHE NESSUNO SE NE ACCORGA. Per questo il conflitto
    qui si urla, non si assorbe: un dizionario che si rompe in silenzio e' peggio
    di nessun dizionario, perche' continua a dare risposte plausibili e sbagliate."""
    m = {}
    origine = {}
    conflitti = []
    for gruppo in SINONIMI:
        capo = normalizza(gruppo[0])
        for parola in gruppo:
            r = normalizza(parola)
            if r in origine and origine[r] != capo:
                conflitti.append((parola, origine[r], gruppo[0]))
            m[r] = capo
            origine[r] = capo
    if conflitti:
        print("ATTENZIONE - parole presenti in piu' gruppi di sinonimi:")
        for parola, primo, secondo in conflitti:
            print("  '%s' sta sia in '%s' sia in '%s' - vince il secondo"
                  % (parola, primo, secondo))
        print("  Correggi SINONIMI in cima a questo file: una parola, un gruppo.")
        print("")
    return m


MAPPA = costruisci_mappa_sinonimi()


def radici(testo):
    """Le parole utili di un testo, gia' normalizzate e gia' ricondotte al
    capogruppo dei sinonimi."""
    fuori = []
    for grezza in re.findall(r"[A-Za-zÀ-ÿ0-9]+", testo):
        if grezza.lower() in VUOTE:
            continue
        r = normalizza(grezza)
        if len(r) < 3 or r in VUOTE:
            continue
        fuori.append(MAPPA.get(r, r))
    return fuori


def costruisci_indice():
    """Legge tutte le pagine e costruisce l'indice. Titolo e collegamenti pesano
    di piu' del corpo: dicono di cosa parla la pagina, non cosa cita."""
    if not os.path.isdir(WIKI):
        print("Cartella wiki non trovata: %s" % WIKI)
        return None

    indice = defaultdict(dict)   # radice -> {file: punteggio}
    titoli = {}
    stazza = {}                  # file -> quanto e' grossa, per non premiarla
    n = 0
    inizio = time.time()

    for radice_dir, dirs, files in os.walk(WIKI):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for nome in files:
            if not nome.endswith(".md"):
                continue
            pieno = os.path.join(radice_dir, nome)
            rel = os.path.relpath(pieno, RADICE).replace("\\", "/")
            try:
                with io.open(pieno, encoding="utf-8", errors="ignore") as f:
                    testo = f.read()
            except IOError:
                continue

            n += 1
            titolo = os.path.splitext(nome)[0].replace("_", " ")
            titoli[rel] = titolo

            # il titolo vale 8, i collegamenti fra pagine 4, il corpo 1
            for r in radici(titolo):
                indice[r][rel] = indice[r].get(rel, 0) + 8
            for link in re.findall(r"\[\[([^\]]+)\]\]", testo):
                for r in radici(link):
                    indice[r][rel] = indice[r].get(rel, 0) + 4
            corpo = radici(testo)
            for r in corpo:
                indice[r][rel] = indice[r].get(rel, 0) + 1
            stazza[rel] = max(len(corpo), 1)

    dati = {
        "creato": time.strftime("%Y-%m-%d %H:%M"),
        "pagine": n,
        "indice": {k: v for k, v in indice.items()},
        "titoli": titoli,
        "stazza": stazza,
    }
    with io.open(INDICE, "w", encoding="utf-8") as f:
        f.write(json.dumps(dati, ensure_ascii=False))

    print("Indice costruito: %d pagine, %d radici, in %.1f secondi."
          % (n, len(indice), time.time() - inizio))
    return dati


def carica_indice(forza=False):
    if forza or not os.path.exists(INDICE):
        return costruisci_indice()
    try:
        with io.open(INDICE, encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, IOError):
        print("Indice illeggibile, lo rifaccio.")
        return costruisci_indice()


def ascii_sicuro(testo):
    """La console Windows e' cp1252 e muore sui caratteri fuori tabella (frecce,
    trattini lunghi, emoji) che nelle pagine ci sono eccome. Qui si sostituisce
    cio' che non passa, invece di far cadere tutta la ricerca per un carattere."""
    fuori = []
    for c in testo:
        if ord(c) < 128:
            fuori.append(c)
        else:
            d = unicodedata.normalize("NFKD", c)
            d = "".join(x for x in d if ord(x) < 128)
            fuori.append(d if d else " ")
    return "".join(fuori)


def riga_di_contesto(percorso_rel, cercate):
    """La riga in cui la cosa compare davvero: senza, il risultato e' un nome
    di file e tocca aprirlo per sapere se serviva."""
    pieno = os.path.join(RADICE, percorso_rel)
    try:
        with io.open(pieno, encoding="utf-8", errors="ignore") as f:
            for riga in f:
                pulita = riga.strip()
                if len(pulita) < 25 or pulita.startswith(("---", "#", "|", ">")):
                    continue
                rr = set(radici(pulita))
                if rr & cercate:
                    return ascii_sicuro(pulita[:150])
    except IOError:
        pass
    return ""


def cerca(dati, domanda, quanti):
    cercate = set(radici(domanda))
    if not cercate:
        print("La domanda non contiene parole cercabili.")
        return

    indice = dati["indice"]
    titoli = dati.get("titoli", {})
    n_pagine = max(dati.get("pagine", 1), 1)
    stazza = dati.get("stazza", {})
    punteggi = defaultdict(float)
    trovate = defaultdict(set)

    # LA RARITA' DELLA PAROLA - senza questo la ricerca e' inutile.
    # Una parola che sta in 900 pagine su 1547 non dice niente su quale pagina
    # serva: cercando "obiezioni sul prezzo" venivano fuori le pagine piu' lunghe
    # che ripetevano "prezzo" trenta volte, non quelle che PARLANO di obiezioni.
    # Qui una parola pesa tanto quanto e' rara: se sta ovunque, vale quasi zero.
    for r in cercate:
        pagine_con_r = indice.get(r, {})
        if not pagine_con_r:
            continue
        rarita = math.log(1.0 + float(n_pagine) / len(pagine_con_r))
        for percorso, p in pagine_con_r.items():
            # la radice quadrata smorza la ripetizione: dire una cosa trenta volte
            # non rende una pagina trenta volte piu' pertinente
            # diviso per la stazza della pagina: un documento lungo accumula
            # punti per inerzia, non per pertinenza. Senza questo vincono sempre
            # i papiri generici invece della pagina che parla davvero della cosa.
            lungh = math.sqrt(stazza.get(percorso, 500))
            punteggi[percorso] += (math.sqrt(p) * rarita * 30.0) / lungh
            trovate[percorso].add(r)

    if not punteggi:
        print("")
        print("  Nessuna pagina trovata per: %s" % ascii_sicuro(domanda))
        print("")
        print("  ATTENZIONE - questo NON dimostra che l'Impero non sappia la cosa.")
        print("  Prova un'altra formulazione prima di dichiarare un vuoto:")
        print("  sinonimi, il termine inglese, il nome esatto invece della descrizione.")
        print("")
        return

    # chi contiene PIU' parole della domanda viene prima di chi ne ripete una sola
    tutti = sorted(punteggi.items(),
                   key=lambda kv: (-len(trovate[kv[0]]), -kv[1]))

    # la stessa pagina vive in piu' cartelle (copie di lavoro, cartelle CONTESTO
    # ripetute): mostrarla cinque volte riempie la lista e nasconde il resto.
    # Si tiene la copia col punteggio migliore.
    ordinati = []
    visti = set()
    for percorso, punti in tutti:
        chiave = titoli.get(percorso, os.path.basename(percorso)).strip().lower()
        if chiave in visti:
            continue
        visti.add(chiave)
        ordinati.append((percorso, punti))
        if len(ordinati) >= quanti:
            break

    print("")
    print("=" * 78)
    print("  CERCA WIKI - %s" % ascii_sicuro(domanda))
    print("  %d pagine indicizzate | cerco anche i sinonimi" % dati["pagine"])
    print("=" * 78)
    print("")

    for i, (percorso, p) in enumerate(ordinati, 1):
        n_parole = len(trovate[percorso])
        titolo = ascii_sicuro(titoli.get(percorso, os.path.basename(percorso)))
        print("  %2d. %s" % (i, titolo))
        print("      %s" % ascii_sicuro(percorso))
        print("      pertinenza %.1f | %d parole della domanda su %d"
              % (p, n_parole, len(cercate)))
        ctx = riga_di_contesto(percorso, cercate)
        if ctx:
            print("      \"%s\"" % ctx)
        print("")

    print("=" * 78)
    print("")


def main():
    ap = argparse.ArgumentParser(
        description="Cerca nella memoria di Digital Empire, sinonimi compresi")
    ap.add_argument("domanda", nargs="*", help="cosa cerchi, in parole tue")
    ap.add_argument("--n", type=int, default=10, help="quanti risultati (default 10)")
    ap.add_argument("--ricostruisci", action="store_true",
                    help="rifa' l'indice da zero")
    args = ap.parse_args()

    dati = carica_indice(forza=args.ricostruisci)
    if dati is None:
        return 1

    if not args.domanda:
        if not args.ricostruisci:
            print("Scrivi cosa cerchi. Esempio:")
            print('  python scripts/cerca_wiki.py "quanto spesso pubblicare"')
        return 0

    cerca(dati, " ".join(args.domanda), args.n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
