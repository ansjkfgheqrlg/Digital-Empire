"""
anatomia_lanci.py — ANATOMIA DEI LANCI, forma eseguibile.

Seconda delle tre forme del documento (Markdown -> Python -> PDF). Fonte:
`ANATOMIA-DEI-LANCI.md`, nella stessa cartella — se un numero qui non torna con quel file,
il file ha ragione, si corregge questo modulo.

Ogni struttura sotto e' interrogabile: chi costruisce l'ecosistema LANCI (ADR-025) chiama
dentro invece di rileggere prosa. La terza forma, il PDF in standard-oro (`pdf_engine_empire.py`,
dossier 28), nasce da queste stesse strutture con `build_pdf()`.

Uso:
    python anatomia_lanci.py                 # genera HTML + PDF + doppione in documentazione Empire
    python anatomia_lanci.py --html-only      # solo HTML, niente Chromium
    python anatomia_lanci.py --check          # stampa un riepilogo dei dati, nessun PDF
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_ENGINE_DIR = os.path.join(os.path.dirname(HERE), "..", "PIANO-MAESTRO", "scripts")
sys.path.insert(0, os.path.normpath(PDF_ENGINE_DIR))


# =============================================================================================
# PARTE I — il fatto: il lancio Armageddon, misurato
# =============================================================================================

PACCHETTO_ARMAGEDDON = {
    "prodotti": ["outEmail", "outFunnel", "outHeadline", "outViral"],
    "listino_sommato_eur": 585,
    "voucher_eur": 199,
    "valore_dichiarato_eur": 784,
    "prezzo_vendita_eur": 199,
    "sconto_dichiarato": "Risparmi €585",
    "link_pagamento": "uno solo, Stripe, identico su tutte e cinque le pagine",
    "costruzione": "artigianale, vanilla, zero piattaforma",
    "pagine": {"madre_px": 5103, "figlie": 4},
    "insegnamento": (
        "il pacchetto costa quanto il voucher: il cliente paga 199 EUR e riceve un buono da "
        "199 EUR piu' quattro prodotti. L'ancora e' la somma dei listini che esistono davvero "
        "sul negozio, verificabile da chiunque in trenta secondi."
    ),
}


# =============================================================================================
# PARTE II — come costruisce un lancio: sei mosse
# =============================================================================================

MOSSE = [
    {
        "n": 1,
        "titolo": "Non scrive pagine nuove. Specchia quelle che ha.",
        "testo": (
            "Le quattro pagine figlie sono le pagine prodotto del negozio, copiate e ripulite. "
            "Costo del lancio in ore di scrittura: quasi zero."
        ),
    },
    {
        "n": 2,
        "titolo": "Spoglia la piattaforma.",
        "testo": "Dal mirror sparisce ogni script Squarespace: una pagina statica che non puo' rompersi.",
    },
    {
        "n": 3,
        "titolo": "Ripunta tutto a una cassa sola.",
        "testo": "Tutte e cinque le pagine portano allo stesso identico link Stripe.",
    },
    {
        "n": 4,
        "titolo": "Sostituisce il prezzo con l'appartenenza.",
        "testo": (
            "Badge 'INCLUSO NEL PACCHETTO ARMAGEDDON' (#bc0807, 15,2px, peso 700) al posto del "
            "bottone-prezzo: il prodotto singolo smette di essere comprabile."
        ),
    },
    {
        "n": 5,
        "titolo": "Mantiene il mirror, non lo congela.",
        "testo": (
            "L'originale dice 'nel 2025', la copia catturata lo stesso giorno dice 'nel 2026': "
            "un mirror di lancio e' un artefatto vivo, va messo in manutenzione come tale."
        ),
    },
    {
        "n": 6,
        "titolo": "Tiene l'offerta su una pagina sola.",
        "testo": "Pagina madre 5.103px contro le 10.000-27.000px delle sue pagine di vendita normali.",
    },
]


# =============================================================================================
# PARTE III — il funnel intero
# =============================================================================================

FUNNEL_FREDDO = [
    {"url": "/define", "domanda": "Cos'e' il copywriting?", "px": 1802, "sezioni": 1, "video": 1, "bottoni": 1},
    {"url": "/asa", "domanda": "Come si monetizza", "px": 1936, "sezioni": 1, "video": 1, "bottoni": 1},
    {"url": "/copy-base", "domanda": "la pagina prodotto", "px": None, "sezioni": None, "video": None, "bottoni": None},
]

FUNNEL_FREDDO_PAROLE = 86
PAGINA_VENDITA_PAROLE_RANGE = (1140, 1560)

STAMPO_PRECASSA = [
    {"n": 1, "elemento": "occhiello in corsivo", "esempio": "«Stai acquistando…»"},
    {"n": 2, "elemento": "nome del prodotto, grande", "esempio": "«outFunnel», 68,3 px"},
    {"n": 3, "elemento": "istruzione + codice sconto", "esempio": 'codice "CWSHOP", 20% di sconto'},
    {"n": 4, "elemento": "la cifra, isolata", "esempio": "«98,00 €», 35,2 px"},
    {"n": 5, "elemento": "la condizione, attaccata", "esempio": "«Una tantum»"},
    {"n": 6, "elemento": "il bottone", "esempio": "«Acquista outFunnel»"},
]
STAMPO_PRECASSA_CATTURE = 9
STAMPO_PRECASSA_VARIABILI = [
    "nome", "prezzo", "colore", "porzione colorata del nome", "codice sconto (opzionale)", "testo del bottone",
]

TRE_DECISIONI_STAMPO = [
    "Lo sconto sta dopo la decisione: CWSHOP compare solo in pre-cassa (98€ -> 78,40€), non mentre il lettore valuta.",
    "'Stai acquistando…' in corsivo prima del nome: riafferma l'atto invece di ricominciare a vendere.",
    "'Una tantum' attaccato alla cifra: uccide il sospetto dell'abbonamento nel punto esatto in cui nasce.",
]

CODICE_SCONTO = {"codice": "CWSHOP", "percentuale": 20, "listino_vero_eur": 78.40, "prezzo_decorativo_eur": 98.00,
                  "pubblico_e_permanente": True}

GRADINI_NON_CASSA = ["/presto-disponibile", "/ricevi-email-di-andrei-pascu", "/aps-assistenza"]


# =============================================================================================
# PARTE IV — come costruisce l'offerta
# =============================================================================================

LEVE_OFFERTA = [
    {"leva": "Ancora", "come": "somma dei listini reali, verificabile", "misura": "585 €"},
    {"leva": "Regalo che vale quanto il prezzo", "come": "voucher", "misura": "199 € su 199 € pagati"},
    {"leva": "Sconto dichiarato", "come": "in grande, sopra tutto", "misura": "«Risparmi €585» a 81,6 px"},
    {"leva": "Prezzo pagato", "come": "in piccolo", "misura": "14,88 px"},
    {"leva": "Scarsita'", "come": "solo tempo, nessun limite di posti", "misura": "dichiarata e verificabile"},
    {"leva": "Bundle contro singolo", "come": "il singolo sparisce dietro il badge", "misura": "#bc0807"},
]

RAPPORTO_TIPOGRAFICO_OFFERTA = {"sconto_px": 81.6, "prezzo_pagato_px": 14.88, "corpo_faq_px": 16.5, "rapporto": 5.5}

SCALA_PREZZI = [
    {"prodotto": "outHeadline", "prezzo_eur": 98, "fonti_esterne": 0, "prova_sociale": False},
    {"prodotto": "Vendita101", "prezzo_eur": 400, "fonti_esterne": 2, "prova_sociale": True},
    {"prodotto": "Copy Mentorship", "prezzo_eur": 999, "fonti_esterne": 5, "prova_sociale": True},
]
SOGLIA_PROVA_SOCIALE_EUR = 349


# =============================================================================================
# PARTE V — otto costanti
# =============================================================================================

COSTANTI = [
    "Un lancio e' un pacchetto di cose che esistono gia'. Nessun prodotto nuovo.",
    "Le pagine si specchiano, non si scrivono.",
    "Una sola cassa, un solo link.",
    "Il singolo sparisce dietro il badge di inclusione.",
    "L'ancora e' verificabile, perche' e' la somma di listini pubblici.",
    "Il regalo vale quanto il prezzo — il voucher pareggia la cifra pagata.",
    "La scarsita' e' di tempo, mai di posti.",
    "La pagina madre annuncia, le figlie spiegano.",
]


# =============================================================================================
# PARTE VI/VII — come ragiona + cosa non fa mai
# =============================================================================================

PRINCIPI_RAGIONAMENTO = [
    "La piattaforma si sceglie dalla vita del pezzo: negozio permanente -> Squarespace, lancio con finestra -> a mano.",
    "Non personalizza dove non conta: il custom.css del negozio pesa lo 0,02% dei byte scaricati.",
    "Tutto cio' che si ripete diventa uno stampo (la pre-cassa e' un generatore a sei variabili).",
    "Lucida dove si convince, lascia i difetti dove si transita.",
]

COSA_NON_FA_MAI = [
    "Non chiede i soldi nella pagina che fa desiderare (il prezzo vive nella pre-cassa).",
    "Non mette lo sconto prima della decisione.",
    "Non usa limiti di posti su prodotti digitali.",
    "Non spiega il pacchetto nella pagina madre.",
    "Non dichiara un carattere tipografico sul negozio (38 pagine su 52 a sans-serif).",
    "Non nomina mai l'obiezione piu' ovvia del suo corso su Claude ('lo imparo gratis dalla documentazione').",
]


# =============================================================================================
# PARTE VIII — i sette difetti, sei diventati controlli di gate (ADR-024)
# =============================================================================================

DIFETTI = [
    {"n": 1, "difetto": "La cassa non risolve", "misura": "/vendita -> /acquista-v101: 404, cassa vera non linkata",
     "controllo": "Controllo 8 — primo gate obbligatorio di LANCI"},
    {"n": 2, "difetto": "Il prezzo e' un'immagine con alt vuoto", "misura": "outEmail 139€, outFunnel 98€, outHeadline",
     "controllo": "Controllo 6"},
    {"n": 3, "difetto": "La cifra pagata e' il testo piu' piccolo", "misura": "14,88px contro FAQ a 16,5px",
     "controllo": "Controllo 7"},
    {"n": 4, "difetto": "Anni scritti a mano", "misura": "«nel 2025» sul negozio vivo", "controllo": "Controllo 5"},
    {"n": 5, "difetto": "og:image placeholder identico su 3 pagine", "misura": "targato lovable.app",
     "controllo": "Controllo 3"},
    {"n": 6, "difetto": "Un campo del calcolatore non entra nel calcolo", "misura": "apsales.eu/landing-page",
     "controllo": "Controllo 4"},
    {"n": 7, "difetto": "Il codice sconto e' pubblico e permanente", "misura": "CWSHOP su pagina indicizzabile",
     "controllo": "pattern pre-cassa nasce con codice a scadenza e noindex"},
]
DIFETTO_PIU_COSTOSO_N = 1


# =============================================================================================
# PARTE IX — il modello per Digital Empire: dodici passi
# =============================================================================================

MODELLO_12_PASSI = [
    {"n": 1, "passo": "Scegli i pezzi che esistono gia'", "regola": "mai costruire prodotto nuovo per un lancio"},
    {"n": 2, "passo": "Somma i listini pubblici", "regola": "l'ancora dev'essere verificabile da un estraneo"},
    {"n": 3, "passo": "Aggiungi un regalo che valga quanto il prezzo", "regola": "il voucher pareggia la cifra"},
    {"n": 4, "passo": "Fissa una finestra di tempo", "regola": "mai limiti di posti su prodotti digitali"},
    {"n": 5, "passo": "Specchia le pagine prodotto", "regola": "pattern mirror-di-lancio"},
    {"n": 6, "passo": "Sostituisci i bottoni-prezzo col badge di inclusione", "regola": "un accento, due punti, zero dispersione"},
    {"n": 7, "passo": "Punta tutto a una cassa", "regola": "un solo link di pagamento"},
    {"n": 8, "passo": "Costruisci la pagina madre corta", "regola": "annuncia, non spiegare"},
    {"n": 9, "passo": "Metti il gradino di pre-cassa", "regola": "pattern pre-cassa, sei elementi in ordine"},
    {"n": 10, "passo": "Codice sconto a scadenza, nella pre-cassa, con noindex", "regola": "mai pubblico e permanente"},
    {"n": 11, "passo": "Prezzo pagabile >= corpo del testo di servizio, mai dentro un'immagine", "regola": "controlli 6 e 7"},
    {"n": 12, "passo": "Percorri la catena a macchina prima di aprire",
     "regola": "controllo 8: ogni CTA risolve 200, ogni cassa ha almeno un link che ci arriva"},
]
PASSO_CRITICO_N = 12  # se salta, annulla gli altri undici


# =============================================================================================
# PARTE X — cosa consegniamo a LANCI
# =============================================================================================

CONSEGNA_A_LANCI = [
    "Questo documento, nelle tre forme (Markdown, Python, PDF).",
    "Lo stampo di pre-cassa gia' costruito: .claude/skills/fabbrica-siti/pattern/pre-cassa/",
    "Il pattern pagina-ponte: .claude/skills/fabbrica-siti/pattern/pagina-ponte/",
    "Otto controlli di gate, di cui il numero 8 e' il primo gate obbligatorio di LANCI.",
    "Un funnel nostro gia' scritto e mai lanciato: chiamata-formazione.netlify.app "
    "(call 1:1 gratuita verso Claude Code Mastery a 397€, 18.770px, 25 sezioni, 506 blocchi, ferma su staging).",
]


# =============================================================================================
# funzioni di interrogazione
# =============================================================================================

def get_difetto(n: int) -> dict:
    for d in DIFETTI:
        if d["n"] == n:
            return d
    raise KeyError(f"difetto {n} non esiste (1-7)")


def get_passo(n: int) -> dict:
    for p in MODELLO_12_PASSI:
        if p["n"] == n:
            return p
    raise KeyError(f"passo {n} non esiste (1-12)")


def check() -> None:
    """Riepilogo dei dati sul terminale — nessuna generazione di file."""
    print(f"Pacchetto Armageddon: listino {PACCHETTO_ARMAGEDDON['listino_sommato_eur']}€ "
          f"+ voucher {PACCHETTO_ARMAGEDDON['voucher_eur']}€ = "
          f"{PACCHETTO_ARMAGEDDON['valore_dichiarato_eur']}€, venduto a "
          f"{PACCHETTO_ARMAGEDDON['prezzo_vendita_eur']}€")
    print(f"Mosse di costruzione: {len(MOSSE)}")
    print(f"Funnel freddo: {FUNNEL_FREDDO_PAROLE} parole, {len(FUNNEL_FREDDO)} gradini")
    print(f"Stampo pre-cassa: {STAMPO_PRECASSA_CATTURE} catture, {len(STAMPO_PRECASSA_VARIABILI)} variabili")
    print(f"Costanti del modello: {len(COSTANTI)}")
    print(f"Difetti misurati: {len(DIFETTI)} (il piu' costoso: #{DIFETTO_PIU_COSTOSO_N} - "
          f"{get_difetto(DIFETTO_PIU_COSTOSO_N)['difetto']})")
    print(f"Modello per Digital Empire: {len(MODELLO_12_PASSI)} passi "
          f"(critico: #{PASSO_CRITICO_N} - {get_passo(PASSO_CRITICO_N)['passo']})")
    print(f"Consegna a LANCI: {len(CONSEGNA_A_LANCI)} elementi")


# =============================================================================================
# terza forma — il PDF, standard-oro (pdf_engine_empire.py, dossier 28)
# =============================================================================================

def build_pdf(out_html: str, out_pdf: str, html_only: bool = False) -> None:
    from pdf_engine_empire import PDFDoc  # import qui: serve solo per generare il PDF

    doc = PDFDoc(
        title="Anatomia dei Lanci — Andrei Pascu",
        doc_label="Anatomia dei Lanci · Andrei Pascu · 9 settembre 2026",
        footer_left="Anatomia dei Lanci · Andrei Pascu",
        out_html=out_html,
        out_pdf=out_pdf,
    )
    head, tab, figure = doc.head, doc.tab, doc.figure

    # 01 · copertina -----------------------------------------------------------------------
    doc.page(
        """
<div class='cover-mid'>
  <h1 class='big'>Anatomia<br><span class='soft'>dei</span> <span class='acc'>Lanci</span>.</h1>
  <p class='cover-lead'>Un lancio in corso di Andrei Pascu, smontato pezzo per pezzo: 52 pagine
  catturate su 7 domini, oltre 100.000 parole di rapporti. Ogni numero qui dentro e' misurato
  sul disco — dove c'e' un'inferenza, e' scritto che lo e'.</p>
  <div class='cover-meta'>
    <div><div class='k'>Pacchetto</div><div class='v'>784€ -> 199€</div></div>
    <div><div class='k'>Funnel freddo</div><div class='v'>86 parole</div></div>
    <div><div class='k'>Pre-cassa</div><div class='v'>9 catture, 1 stampo</div></div>
    <div><div class='k'>Per</div><div class='v'>Ecosistema LANCI</div></div>
  </div>
</div>
""",
        cls="cover dark",
        foot_l="Emperator · 9 settembre 2026",
        foot_r="Studio Andrei Pascu",
    )

    # 02 · A — il fatto ----------------------------------------------------------------------
    doc.page(
        head("A", "Il fatto", "Un lancio <span class='soft'>colto mentre girava.</span>",
             "armageddon.bsns.it: pagina madre piu' quattro figlie, pagamento attivo. "
             + PACCHETTO_ARMAGEDDON["insegnamento"])
        + "<div class='body stack'><div class='unit'>"
        + tab(
            ["Misura", "Valore"],
            [
                ["*Prodotti nel pacchetto", ", ".join(PACCHETTO_ARMAGEDDON["prodotti"])],
                ["*Listino sommato", f"{PACCHETTO_ARMAGEDDON['listino_sommato_eur']} €"],
                ["*Voucher aggiunto", f"{PACCHETTO_ARMAGEDDON['voucher_eur']} €"],
                ["*Valore dichiarato", f"{PACCHETTO_ARMAGEDDON['valore_dichiarato_eur']} €"],
                ["*Prezzo di vendita", f"{PACCHETTO_ARMAGEDDON['prezzo_vendita_eur']} €"],
                ["*Link di pagamento", PACCHETTO_ARMAGEDDON["link_pagamento"]],
                ["*Costruzione", PACCHETTO_ARMAGEDDON["costruzione"]],
            ],
            hi=4,
        )
        + "</div></div>"
    )

    # 03 · B — sei mosse -----------------------------------------------------------------------
    doc.page(
        head("B", "Costruzione", "Sei mosse, <span class='soft'>sempre le stesse.</span>",
             "Come costruisce un lancio, ricavato dal confronto pixel per pixel col negozio.")
        + "<div class='body stack-tight'>"
        + "".join(
            f"<div class='unit step'><div class='idx'>M{m['n']:02d}</div>"
            f"<div><h3>{m['titolo']}</h3><p class='note'>{m['testo']}</p></div></div>"
            for m in MOSSE
        )
        + "</div>"
    )

    # 04 · C — il funnel freddo + il costo in parole -------------------------------------------
    doc.page(
        head("C", "Funnel", "Il percorso freddo, <span class='soft'>due domande e un prodotto.</span>",
             "Ogni pagina-ponte ha una sola decisione possibile. Il prodotto compare al terzo passo.")
        + "<div class='body stack'><div class='unit'>"
        + tab(
            ["URL", "Cosa chiede", "~px", "Video", "Bottoni"],
            [[f"*{s['url']}", s["domanda"], f"~{s['px']}" if s["px"] else "~—",
              str(s["video"]) if s["video"] else "—", str(s["bottoni"]) if s["bottoni"] else "—"]
             for s in FUNNEL_FREDDO],
        )
        + "</div><div class='unit grid3'>"
        + figure("Parole dall'apertura al clic", str(FUNNEL_FREDDO_PAROLE), "Il costo del percorso, in contenuto vero.", acc=True)
        + figure("Una pagina di vendita", f"{PAGINA_VENDITA_PAROLE_RANGE[0]}-{PAGINA_VENDITA_PAROLE_RANGE[1]}", "parole per convincere da sola.")
        + figure("Rapporto", "13-18x", "il funnel e' cosi' piu' economico in parole della pagina che convince.")
        + "</div><div class='unit'>"
        + "<p class='quote'>«Ti consiglio di vedere e finire il video prima di cliccare il pulsante "
        "per capirne i contenuti.»<span class='src'>/asa — controllo del consumo, non cortesia</span></p>"
        + "</div></div>"
    )

    # 05 · D — lo stampo della pre-cassa ---------------------------------------------------------
    doc.page(
        head("D", "Pre-cassa", "Non e' una pagina, <span class='soft'>e' un generatore.</span>",
             f"{STAMPO_PRECASSA_CATTURE} catture, un unico stampo: cornice identica al pixel, cambia "
             "solo il riquadro centrale.")
        + "<div class='body stack'><div class='unit'>"
        + tab(
            ["#", "Elemento", "Esempio misurato"],
            [[f"*{e['n']}", e["elemento"], e["esempio"]] for e in STAMPO_PRECASSA],
            cap=f"Sei variabili in tutto: {', '.join(STAMPO_PRECASSA_VARIABILI)}. Tutto il resto e' fisso.",
        )
        + "</div><div class='unit'>"
        + "<div class='kicker'><span class='n'>—</span>Le tre decisioni dentro lo stampo</div>"
        + "<ul class='clean'>" + "".join(f"<li>{d}</li>" for d in TRE_DECISIONI_STAMPO) + "</ul>"
        + "</div></div>"
    )

    # 06 · E — l'offerta -----------------------------------------------------------------------
    doc.page(
        head("E", "Offerta", "Il rapporto piu' aggressivo <span class='soft'>dell'ecosistema.</span>",
             f"La cifra che eccita ({RAPPORTO_TIPOGRAFICO_OFFERTA['sconto_px']}px) e' "
             f"{RAPPORTO_TIPOGRAFICO_OFFERTA['rapporto']} volte quella che addebita "
             f"({RAPPORTO_TIPOGRAFICO_OFFERTA['prezzo_pagato_px']}px) — piu' piccola perfino delle FAQ.")
        + "<div class='body stack'><div class='unit'>"
        + tab(["Leva", "Come la usa", "Misura"],
              [[l["leva"], l["come"], l["misura"]] for l in LEVE_OFFERTA])
        + "</div><div class='unit'>"
        + tab(
            ["Prodotto", "~Prezzo", "~Fonti esterne", "Prova sociale"],
            [[s["prodotto"], f"~{s['prezzo_eur']} €", f"~{s['fonti_esterne']}", "si'" if s["prova_sociale"] else "no"]
             for s in SCALA_PREZZI],
            cap=f"Il prezzo che sale non porta piu' obiezioni gestite: porta piu' fonti. Prova sociale vera "
            f"solo sopra {SOGLIA_PROVA_SOCIALE_EUR}€.",
        )
        + "</div></div>"
    )

    # 07 · F — otto costanti + principi + cosa non fa mai -----------------------------------------
    doc.page(
        head("F", "Il modello", "Otto costanti, <span class='soft'>ripetute sempre uguali.</span>",
             "Il modello ripetibile dietro ogni lancio, distillato dal confronto fra piu' lanci.")
        + "<div class='body stack'><div class='unit'>"
        + "<ul class='clean'>" + "".join(f"<li><strong>{i+1}.</strong> {c}</li>" for i, c in enumerate(COSTANTI)) + "</ul>"
        + "</div><div class='unit'>"
        + "<div class='kicker'><span class='n'>—</span>Cosa non fa mai</div>"
        + "<ul class='clean'>" + "".join(f"<li>{c}</li>" for c in COSA_NON_FA_MAI) + "</ul>"
        + "</div></div>"
    )

    # 08 · G — i sette difetti -------------------------------------------------------------------
    doc.page(
        head("G", "Difetti", "Sette difetti, <span class='soft'>sei diventati controlli.</span>",
             "Per noi valgono quanto i pregi: sei sono gia' dentro il gate della Fabbrica Siti (ADR-024).")
        + "<div class='body stack'><div class='unit'>"
        + tab(
            ["#", "Difetto", "Misura", "Nostro controllo"],
            [[f"*{d['n']}", d["difetto"], d["misura"], d["controllo"]] for d in DIFETTI],
            hi=0,
        )
        + "</div><div class='unit fix'>"
        + "<div class='tag'>Il difetto che vale da solo tutto lo studio</div>"
        + "<h3>La cassa vera e' irraggiungibile</h3>"
        + "<p class='note'>Un lancio con la pagina di vendita viva e la cassa irraggiungibile perde "
        "ogni euro che il copy ha guadagnato, e nessuno se ne accorge, perche' la pagina di vendita "
        "funziona benissimo.</p>"
        + "</div></div>"
    )

    # 09 · H — il modello in dodici passi ---------------------------------------------------------
    doc.page(
        head("H", "Esecuzione", "Il suo modello, <span class='soft'>senza i suoi difetti.</span>",
             "Non 'facciamo come lui': facciamo il suo modello senza i suoi difetti. Dodici passi, in ordine.")
        + "<div class='body stack-tight'>"
        + tab(
            ["#", "Passo", "Regola nostra"],
            [[f"*{p['n']}", p["passo"], p["regola"]] for p in MODELLO_12_PASSI],
            hi=PASSO_CRITICO_N - 1,
            cap=f"Il passo {PASSO_CRITICO_N} non e' l'ultimo per caso: e' il solo che, se salta, annulla gli altri undici.",
        )
        + "</div>"
    )

    # 10 · I — cosa consegniamo a LANCI ------------------------------------------------------------
    doc.page(
        head("I", "Consegna", "Cosa arriva <span class='soft'>a LANCI.</span>",
             "Il perimetro completo consegnato all'ecosistema che costruisce i lanci di Digital Empire.")
        + "<div class='body stack'><div class='unit push'>"
        + "<ul class='clean'>" + "".join(f"<li>{c}</li>" for c in CONSEGNA_A_LANCI) + "</ul>"
        + "</div><div class='unit'>"
        + "<div class='kicker'><span class='n'>—</span>Dove vive questo documento</div>"
        + "<ul class='clean'>"
        + "<li><strong>Markdown:</strong> competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md</li>"
        + "<li><strong>Python:</strong> competitor/Andrei Pascu/anatomia_lanci.py</li>"
        + "<li><strong>PDF:</strong> documentazione Empire/Lanci/ANATOMIA-DEI-LANCI.pdf</li>"
        + "<li><strong>Consegna:</strong> company/Memory/tasks/TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md</li>"
        + "</ul></div></div>"
    )

    doc.build(html_only=html_only)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--check", action="store_true", help="stampa il riepilogo dei dati, nessun file")
    args = ap.parse_args()

    if args.check:
        check()
        return 0

    out_html = os.path.join(HERE, "ANATOMIA-DEI-LANCI.html")
    out_pdf = os.path.join(HERE, "ANATOMIA-DEI-LANCI.pdf")
    build_pdf(out_html, out_pdf, html_only=args.html_only)

    if not args.html_only:
        doppione_dir = os.path.normpath(os.path.join(HERE, "..", "..", "documentazione Empire", "Lanci"))
        os.makedirs(doppione_dir, exist_ok=True)
        doppione_path = os.path.join(doppione_dir, "ANATOMIA-DEI-LANCI.pdf")
        shutil.copy2(out_pdf, doppione_path)
        print(f"[ok] doppione {doppione_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
