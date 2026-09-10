# -*- coding: utf-8 -*-
"""
precassa.py — lo stampo di pre-cassa, a comando.

Perche' esiste. Misura di SINTESI-METODO.md §4: le nove pre-casse del concorrente
sono UN SOLO stampo. Aperte a video, la cornice e' identica al pixel e cambia solo
il riquadro centrale: sei variabili in tutto — nome prodotto, prezzo, colore,
porzione colorata del nome, codice sconto (opzionale), testo del bottone.
La prima delle CINQUE COSE DA RUBARE SUBITO e' esattamente questa, e la sintesi la
descrive cosi': "lo stampo di pre-cassa a sei variabili, GENERABILE A COMANDO".
Il pattern `pattern/pre-cassa/` era gia' in casa: era una pagina, non uno stampo.
Questo lo rende uno stampo.

Le sei variabili sono le sue. La settima e' nostra e non e' facoltativa: la
SCADENZA del codice. Il suo "CWSHOP" e' pubblico, permanente e indicizzato — uno
sconto che c'e' sempre non e' uno sconto, e' il prezzo (legge §11, ADR-024). Qui un
codice senza finestra di tempo non si genera: lo script si rifiuta.

Uso:
  python .claude/skills/fabbrica-siti/scripts/precassa.py \
      --prodotto "Manuale Claude Code" --accento "Code" \
      --prezzo "47,00" --bottone "Acquista il Manuale" \
      --cassa "https://pagamento.esempio.it/mcc" \
      [--codice GRAZIE24 --scadenza "24 ore"] [--out cantieri/x/pre-cassa.html]

Esce 0 se la pagina e' scritta e passa gate_siti.py, 1 altrimenti.
Nessuna emoji: console cp1252.
"""
import argparse
import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(QUI)
CANONE_JSON = os.path.join(SKILL, "canone", "canone.json")

MODELLO = u"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titolo)s</title>

<!-- GENERATA da scripts/precassa.py. Lo stampo e' pattern/pre-cassa/ e la legge e'
     CLAUDE-SITI.md §11: sei elementi, in quest'ordine, e solo questi sei.
     Rigenerare invece di modificare a mano: una pre-cassa modificata a mano smette
     di essere lo stesso stampo delle altre, ed e' esattamente cosi' che nove
     pagine identiche diventano nove pagine diverse. -->

<!-- noindex: una pre-cassa si raggiunge solo dopo un clic d'acquisto. Indicizzarla
     significa regalare il codice sconto a chiunque cerchi "prodotto + sconto" — il
     difetto misurato su /outfunnel-1 (scheda del pattern, "Il difetto da non copiare"). -->
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="%(canone)s">
<style>

.cassa { max-width: min(560px, 100%%); margin: 0 auto;
  padding: calc(var(--u) * 0.10) calc(var(--u) * 0.05); text-align: center; }

/* 1. Occhiello — 16/1440 misurato su capture/28-outfunnel-1 [y=149] */
.cassa__occhiello { margin: 0 0 clamp(10px, calc(var(--u) * 0.012), 16px);
  font-size: clamp(14px, calc(var(--u) * 0.0111111), 17px);
  font-style: italic; color: rgba(249, 249, 249, var(--t-78)); }

/* 2. Nome del prodotto — 68.3/1440 [y=189]. L'accento si spende QUI e solo qui (§12). */
.cassa__prodotto { margin: 0 0 clamp(20px, calc(var(--u) * 0.03), 40px);
  font-size: clamp(32px, calc(var(--u) * 0.0474306), 68px); }
.cassa__accento { color: %(colore)s; }

/* 3. Istruzione operativa + codice — 16/1440 [y=261]. Il codice resta neutro:
      colorarlo sarebbe una seconda occorrenza dell'accento (§12). */
.cassa__istruzione { max-width: 46ch; margin: 0 auto clamp(28px, calc(var(--u) * 0.035), 48px);
  font-size: clamp(14px, calc(var(--u) * 0.0111111), 17px);
  line-height: var(--leading-body); color: rgba(249, 249, 249, var(--t-76)); }
.cassa__istruzione strong { color: var(--fg); }
.cassa__codice { display: inline-block; padding: 0.15em 0.55em;
  border: 1px solid var(--line-hair); border-radius: var(--radius-sm);
  background: rgba(255, 255, 255, 0.04);
  font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
  font-size: 0.95em; color: var(--fg); letter-spacing: 0.02em; }

/* 4+5. La cifra e la sua condizione — 35.2/1440 [y=500] e 17.6/1440 [y=543].
        17,6 e' esattamente META' di 35,2: la condizione e' la meta' del corpo
        della cifra, un rapporto misurato, non un'estetica a occhio. */
.cassa__ricevuta { display: inline-flex; flex-direction: column; align-items: center;
  gap: clamp(4px, calc(var(--u) * 0.006), 8px);
  margin: 0 0 clamp(28px, calc(var(--u) * 0.04), 56px);
  padding: calc(var(--u) * 0.035) calc(var(--u) * 0.06); }
.cassa__ricevuta-nome { margin: 0; }
.cassa__cifra { margin: 0; font-family: var(--font-shout);
  font-size: clamp(24px, calc(var(--u) * 0.0244444), 35px);
  font-weight: 700; color: var(--fg); }
.cassa__condizione { margin: 0;
  font-size: clamp(12px, calc(var(--u) * 0.0122222), 18px);
  color: rgba(249, 249, 249, var(--t-55)); }

/* 6. Il bottone — canone .btn/.btn-orange as-is (§1). */
.cassa__bottone { margin: 0 auto; }

</style>
</head>
<body class="grain-fine">
<div class="page">

  <section class="cassa" aria-labelledby="cassa-prodotto">

    <p class="cassa__occhiello">Stai acquistando&hellip;</p>

    <h1 class="cassa__prodotto" id="cassa-prodotto">%(prodotto_html)s</h1>

    <p class="cassa__istruzione">%(istruzione)s</p>

    <div class="cassa__ricevuta card-dark">
      <p class="cassa__ricevuta-nome label">%(prodotto)s</p>
      <!-- data-prezzo: la cifra che si paga si dichiara, cosi' gate_siti.py puo'
           verificare §14.2 (il prezzo non e' mai il testo piu' piccolo). -->
      <p class="cassa__cifra num-tabular" data-prezzo>%(prezzo)s&nbsp;&euro;</p>
      <p class="cassa__condizione">%(condizione)s</p>
    </div>

    <a class="btn btn-orange cassa__bottone" href="%(cassa)s">%(bottone)s</a>

  </section>

</div>
</body>
</html>
"""

ISTRUZIONE_CON_CODICE = (u"Accedi con le credenziali che hai appena creato e completa il "
                         u"pagamento. Inserisci ora il codice "
                         u"<code class=\"cassa__codice\">%(codice)s</code>: vale "
                         u"<strong>solo %(scadenza)s</strong> e solo per questo acquisto.")
ISTRUZIONE_NUDA = (u"Accedi con le credenziali che hai appena creato e completa il pagamento. "
                   u"Ci vuole meno di un minuto.")


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def scrivi(path, testo):
    cartella = os.path.dirname(os.path.abspath(path))
    if cartella and not os.path.isdir(cartella):
        os.makedirs(cartella)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(testo)


def colore_valido(valore):
    """§1: nessun agente inventa un valore. Un token del canone, o un hex ammesso."""
    v = valore.strip()
    if v.startswith("var(") or v.startswith("--"):
        return "var(%s)" % v if v.startswith("--") else v, None
    canone = json.loads(leggi(CANONE_JSON))
    ammessi = {c.lower() for c in canone["colori"]["ammessi"]}
    if v.lower() in ammessi:
        return v, None
    return None, ("colore %s fuori canone. §1: se serve un valore che il canone non ha, "
                  "si aggiunge AL CANONE, non alla pagina. Ammessi: %s"
                  % (v, ", ".join(sorted(ammessi))))


def main(argv=None):
    p = argparse.ArgumentParser(description="Genera una pagina di pre-cassa (legge §11).")
    p.add_argument("--prodotto", required=True, help="nome del prodotto, come appare ovunque")
    p.add_argument("--accento", default="", help="la porzione del nome che porta l'accento (§12)")
    p.add_argument("--prezzo", required=True, help="la cifra che si paga, es. 47,00")
    p.add_argument("--bottone", required=True, help="testo del bottone: l'azione, mai il prezzo")
    p.add_argument("--cassa", required=True, help="indirizzo del pagamento vero")
    p.add_argument("--codice", default="", help="codice sconto (facoltativo)")
    p.add_argument("--scadenza", default="",
                   help="finestra del codice, es. \"nelle prossime 24 ore\". "
                        "Obbligatoria se c'e' un codice (§11).")
    p.add_argument("--colore", default="--orange",
                   help="accento: token del canone (default --orange) o hex ammesso")
    p.add_argument("--condizione", default="Una tantum",
                   help="la condizione attaccata alla cifra (§11, elemento 5)")
    p.add_argument("--out", default="", help="dove scrivere (default: ./pre-cassa-<slug>.html)")
    p.add_argument("--canone", default="", help="percorso di canone.css dalla pagina generata")
    a = p.parse_args(argv)

    errori = []

    # §11: un codice senza finestra di tempo non e' uno sconto, e' il prezzo.
    if a.codice and not a.scadenza.strip():
        errori.append("--codice senza --scadenza. §11 non ammette un codice eterno: "
                      "il difetto misurato su /outfunnel-1 (CWSHOP, pubblico e permanente) "
                      "e' esattamente questo.")
    if a.scadenza and not a.codice:
        errori.append("--scadenza senza --codice: non c'e' niente da far scadere.")

    # §12: l'accento si spende su una porzione del nome, quindi deve starci dentro.
    if a.accento and a.accento not in a.prodotto:
        errori.append("--accento \"%s\" non compare in --prodotto \"%s\": l'accento si spende "
                      "su una parola del nome, non su una parola nuova." % (a.accento, a.prodotto))

    # §8: un dato solo. Il bottone dice l'azione, il prezzo ha gia' il suo posto.
    cifre_prezzo = re.sub(r"[^\d]", "", a.prezzo)
    if cifre_prezzo and cifre_prezzo in re.sub(r"[^\d]", "", a.bottone):
        errori.append("il testo del bottone contiene il prezzo. §8: un dato solo nel sorgente. "
                      "Il bottone dice l'azione (\"Acquista il Manuale\"), non la cifra.")

    colore, err = colore_valido(a.colore)
    if err:
        errori.append(err)

    if errori:
        print("PRE-CASSA - rifiutata, %d motivi:" % len(errori))
        for e in errori:
            print("  - " + e)
        return 1

    slug = re.sub(r"[^a-z0-9]+", "-", a.prodotto.lower()).strip("-")
    out = a.out or ("pre-cassa-%s.html" % slug)

    canone_rel = a.canone
    if not canone_rel:
        cartella = os.path.dirname(os.path.abspath(out)) or os.getcwd()
        canone_rel = os.path.relpath(os.path.join(SKILL, "canone", "canone.css"),
                                     cartella).replace(os.sep, "/")

    if a.accento:
        prodotto_html = a.prodotto.replace(
            a.accento, "<span class=\"cassa__accento\">%s</span>" % a.accento, 1)
    else:
        prodotto_html = a.prodotto

    istruzione = (ISTRUZIONE_CON_CODICE % {"codice": a.codice, "scadenza": a.scadenza}
                  if a.codice else ISTRUZIONE_NUDA)

    pagina = MODELLO % {
        "titolo": "Stai acquistando %s" % a.prodotto,
        "canone": canone_rel,
        "colore": colore,
        "prodotto": a.prodotto,
        "prodotto_html": prodotto_html,
        "istruzione": istruzione,
        "prezzo": a.prezzo,
        "condizione": a.condizione,
        "cassa": a.cassa,
        "bottone": a.bottone,
    }
    scrivi(out, pagina)

    print("PRE-CASSA - Fabbrica Siti (legge §11, stampo pattern/pre-cassa)")
    print("  scritta         : %s" % out)
    print("  prodotto        : %s" % a.prodotto)
    print("  accento su      : %s" % (a.accento or "(nessuno)"))
    print("  cifra           : %s EUR - %s" % (a.prezzo, a.condizione))
    print("  codice          : %s" % (("%s, valido %s" % (a.codice, a.scadenza))
                                      if a.codice else "(nessuno)"))
    print("  cassa           : %s" % a.cassa)

    # Il generatore non si fida di se stesso: chiama il gate. E' l'anello che rende
    # vivi tutti e due — chi genera passa da chi controlla, sempre.
    sys.path.insert(0, QUI)
    try:
        import gate_siti
        print("")
        return gate_siti.main(["gate_siti.py", out])
    except Exception as exc:                                   # pragma: no cover
        print("  ATTENZIONE - gate_siti.py non eseguito (%s). Lanciarlo a mano." % exc)
        return 0


if __name__ == "__main__":
    sys.exit(main())
