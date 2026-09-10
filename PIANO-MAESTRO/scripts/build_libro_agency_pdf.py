"""
build_libro_agency_pdf.py — Il Libro dell'Agency, in PDF impaginato.

Contenuto di questo dossier sopra il motore riusabile `pdf_engine_empire.py` (standard-oro
dichiarato da Max il 2026-09-05). Il motore porta CSS, grana, `page/head/tab/figure`; qui
resta solo il contenuto, pagina per pagina.

Sorgente dei contenuti (il testo integrale, mai riassunto): `PIANO-MAESTRO/34-LIBRO-AGENCY.md`.
Questo file ne fa l'edizione da leggere — una selezione dei numeri e dei meccanismi chiave,
pagina per pagina. Il markdown resta l'originale e la fonte di verita'.

Uso:
    python build_libro_agency_pdf.py
    python build_libro_agency_pdf.py --html-only
"""

from __future__ import annotations

import argparse
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.dirname(HERE)  # PIANO-MAESTRO/
sys.path.insert(0, HERE)

from pdf_engine_empire import PDFDoc  # noqa: E402

doc = PDFDoc(
    title="Il Libro dell'Agency",
    doc_label="Il Libro dell'Agency · Digital Empire · 10 settembre 2026",
    footer_left="Il Libro dell'Agency",
    out_html=os.path.join(DEST, "34-LIBRO-AGENCY.html"),
    out_pdf=os.path.join(DEST, "34-LIBRO-AGENCY.pdf"),
)
head = doc.head
tab = doc.tab
figure = doc.figure

# ============================================================ 01 · copertina
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>Il Libro<br><span class='soft'>dell'</span> <span class='acc'>Agency</span>.</h1>
  <p class='cover-lead'>Come Digital Empire acquisisce, vende, consegna e scala un'agenzia CRO —
  e la formazione esterna da cui quel metodo nasce, confrontato e in alcuni punti confermato.
  Due parti dichiarate e separate: il nostro sistema reale, poi le fonti.</p>
  <div class='cover-meta'>
    <div><div class='k'>Metodo</div><div class='v'>5 sezioni</div></div>
    <div><div class='k'>Formazione</div><div class='v'>3 capitoli · 7 fonti</div></div>
    <div><div class='k'>Fonte di verita'</div><div class='v'>34-LIBRO-AGENCY.md</div></div>
    <div><div class='k'>Per</div><div class='v'>Pubblico</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Digital Empire · 10 settembre 2026",
    foot_r="Edizione pubblica",
)

# ============================================================ 02 · posizionamento
doc.page(
    head(
        "1",
        "Il metodo · Introduzione",
        "L'agenzia progettata <span class='soft'>per essere licenziata.</span>",
        "Sprint produttizzati di 2-4 settimane, pay-on-performance. Reparti con confini netti,"
        " handoff strutturati, gate che bloccano — non promemoria.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Reparto", "Cosa decide", "Passa a"],
        [
            ["*A1 — Ricerca", "chi e' il cliente, secondo la scheda ICP", "A3"],
            ["*A3 — Preventivi", "il prezzo, mai prima della discovery", "A4"],
            ["*A4 — Delivery", "sette giorni, poi l'autonomia del cliente", "Tesoreria"],
        ],
        cap="Ogni passaggio porta un handoff strutturato (es. `HC-A3-A4-contratto`) — dati, non"
        " una conversazione informale.",
    )
    + "</div><div class='unit push'>"
    + "<p class='quote'>«Nessun passaggio si da' per scontato, ognuno si verifica.»"
    "<span class='src'>Principio di chiusura, Parte Prima §5</span></p>"
    + "</div></div>"
)

# ============================================================ 03 · acquisizione (metodo)
doc.page(
    head(
        "1",
        "Il metodo · Acquisizione",
        "Concentrazione, <span class='soft'>non volume.</span>",
        "Ogni lead passa prima da una scheda ICP esplicita — mai un giudizio a occhio.",
    )
    + "<div class='body stack'><div class='unit grid3'>"
    + figure("Soglia di passaggio ICP", "70/100", "Scoring pesato: email valida 30, dimensione 25, settore 25, problema evidente 20.")
    + figure("Test del riconoscimento", "1 secondo", "Il prospect deve pensare “questo sono io” leggendo il messaggio che ne deriva.")
    + figure("Sequenza cold email", "3-5 invii", "Gap crescenti, ogni email autosufficiente, finestra totale 1-2 mesi.", acc=True)
    + "</div><div class='unit'>"
    + "<div class='kicker'><span class='n'>—</span>I due campi che mancano quasi sempre</div>"
    "<ul class='clean'>"
    "<li><strong>Trigger evento:</strong> cosa e' successo poco prima che il cliente ci cercasse — non si indovina, si ricava dai clienti gia' vinti.</li>"
    "<li><strong>Dolore specifico:</strong> nelle parole del cliente, non nelle nostre. Senza questi due campi non si puo' scrivere un messaggio che il prospect riconosce in un secondo.</li>"
    "</ul></div></div>"
)

# ============================================================ 04 · vendita (metodo)
doc.page(
    head(
        "1",
        "Il metodo · Vendita",
        "Chi vende e' un dottore, <span class='soft'>non un venditore.</span>",
        "Domande sui sintomi, diagnosi del problema vero, spiegazione della causa. La cura si"
        " propone per ultima — e a quel punto il paziente la vuole.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Chi parla", "~% Tempo", "Tasso di chiusura osservato"],
        [
            ["*Il venditore", "~30%", "diagnostica → 30-45%"],
            ["*Il prospect", "~70%", "(il resto e' silenzio che elabora)"],
        ],
        cap="La regola del rapporto parola. Chi parla piu' del prospect sta vendendo, non"
        " diagnosticando — tasso osservato 8-12%, 3-5 volte peggio.",
    )
    + "</div><div class='unit'>"
    + "<div class='kicker'><span class='n'>—</span>Le quattro fasi della discovery</div>"
    "<ul class='clean'>"
    "<li><strong>Rapporto</strong> (2-3 min) — script diverso per provenienza del lead.</li>"
    "<li><strong>12 domande</strong> (15-20 min) — 4 blocchi: situazione, problema, desiderio, qualificazione silenziosa.</li>"
    "<li><strong>Diagnosi live</strong> (5-7 min) — si riformula il problema, se ne trova la causa.</li>"
    "<li><strong>Valore gratuito</strong> (8-10 min) — tre consigli applicabili subito, a prescindere dalla firma.</li>"
    "</ul></div></div>"
)

# ============================================================ 05 · prezzo (metodo)
doc.page(
    head(
        "1",
        "Il metodo · Prezzo",
        "Il preventivo e' una lettera <span class='soft'>di vendita.</span>",
        "Non una lista prezzi. Il prezzo non si da' mai prima della discovery.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Regola", "Conseguenza"],
        [
            ["*Sempre tre opzioni", "essenziale / professionale / full service — mai un listino a voce singola"],
            ["*Cushion 10%", "applicato al numero mentale prima di scriverlo"],
            ["*Numeri tondi", "2.000 €, non 1.980 €"],
            ["*Niente sconti", "si riduce lo scope, mai il prezzo"],
            ["*Presentazione a schermo", "mai per email senza commento — silenzio dopo il prezzo, nessuna giustificazione anticipata"],
        ],
    )
    + "</div><div class='unit push'>"
    + "<p class='quote'>«Il documento non dice ‘ecco cosa facciamo’, dice ‘ecco come"
    " risolviamo il tuo problema’.»<span class='src'>Principio cardine, Parte Prima §3</span></p>"
    + "</div></div>"
)

# ============================================================ 06 · consegna (metodo)
doc.page(
    head(
        "1",
        "Il metodo · Consegna",
        "Tre prodotti, <span class='soft'>sette giorni.</span>",
        "Il countdown parte quando l'ambiente del cliente e' verificato conforme — non alla firma.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Prodotto", "~Prezzo", "Cosa consegna"],
        [
            ["*Outreach Factory", "~4.000 €", "pipeline di acquisizione automatizzata sul server del cliente"],
            ["*Content Factory", "~3.500 €", "motore di produzione contenuti parametrizzato sul brand"],
            ["*Second Brain", "~2.500 €", "vault di conoscenza strutturato per la nicchia"],
        ],
        cap="Runbook giorno per giorno, identico nella sostanza per tutti e tre: l'ultimo giorno"
        " e' il CLIENTE, non l'agenzia, a eseguire la run finale da solo.",
    )
    + "</div><div class='unit'>"
    + "<div class='kicker'><span class='n'>—</span>Gate Delivery — tutto o niente</div>"
    "<ul class='clean'>"
    "<li>Sistema funzionante sul server del cliente, non solo in locale</li>"
    "<li>Run di test reale superata, UAT firmata dal cliente</li>"
    "<li>Pacchetto di autonomia consegnato (credenziali solo per nome, mai i valori)</li>"
    "<li>Nessuna dipendenza residua dall'agenzia · supporto 90 giorni come rete di sicurezza</li>"
    "</ul></div></div>"
)

# ============================================================ 07 · parte seconda, apertura
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>Parte Seconda<br><span class='soft'>La</span> <span class='acc'>Formazione</span>.</h1>
  <p class='cover-lead'>Sette fonti, tre capitoli, organizzati per fase. Ogni citazione porta la
  sua fonte esatta — video e minuto, o l'atomo di conoscenza che la ancora. Nessun taglio,
  nessun riassunto: qui sotto la selezione dei meccanismi piu' operativi di ciascuna fonte, il
  testo integrale resta nel documento sorgente.</p>
</div>
""",
    cls="cover",
    foot_l="Il Libro dell'Agency",
    foot_r="Parte Seconda",
)

# ============================================================ 08 · capitolo 1 (formazione)
doc.page(
    head(
        "2",
        "Capitolo 1 · Acquisizione Clienti",
        "Organico <span class='soft'>contro</span> attivo.",
        "Due strade per lo stesso canale — LinkedIn — agli estremi opposti.",
    )
    + "<div class='body stack'><div class='unit grid3'>"
    + figure("Trivellato · buyer concentration", "92% vs 2%", "ICP match su 31K follower concentrati contro 200K generici.")
    + figure("Trivellato · fatturato attribuito", "$1,2M/anno", "Zero cold outreach, zero ads — solo contenuto + profilo come sales page.")
    + figure("Beggiato · sequenza risposta", "20/50/30%", "3 step, con la correzione dal vivo 40%→50% sul secondo tocco.", acc=True)
    + "</div><div class='unit'>"
    + "<div class='kicker'><span class='n'>—</span>Le 5 caratteristiche di un cold DM (Beggiato)</div>"
    "<p class='note'>Personalizzato (un dettaglio vero, non una variabile) · chiarire chi sei e"
    " perche' leggere · dare qualcosa prima di chiedere · micro-commitment · schema PROOF"
    " (“la avete” / “la create”) quando manca un case study reale.</p>"
    "</div></div>"
)

# ============================================================ 09 · capitolo 2 (formazione)
doc.page(
    head(
        "2",
        "Capitolo 2 · Vendita e Prezzo",
        "Il fatturato oscilla <span class='soft'>quando la vendita non e' un processo.</span>",
        "Barron: sistema a 5 fasi. Beggiato: value-based pricing con una proxy dichiarata.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Fase (Barron)", "Contenuto"],
        [
            ["*ICP", "chi e' il cliente, per iscritto"],
            ["*Meetings", "come si arriva alla call"],
            ["*Indoctrinate", "email pre-call, la call non parte da zero"],
            ["*Discovery Call", "6 passaggi: Pain, Trigger, Future Reality, ROI, Budget, Next Step"],
            ["*Business Case", "il documento che chiude, non la call stessa"],
        ],
        cap="“Questions first, Solutions later.”",
    )
    + "</div><div class='unit push'>"
    + "<p class='quote'>«Il prezzo vive in un solo posto: mai duplicato, mai a memoria.»"
    "<span class='src'>Principio pricing, Capitolo 2</span></p>"
    + "</div></div>"
)

# ============================================================ 10 · capitolo 3 (formazione)
doc.page(
    head(
        "2",
        "Capitolo 3 · Consegna, Servizio e Scala",
        "Chi giudica il lavoro <span class='soft'>non e' chi lo fa.</span>",
        "Tre fonti, tre livelli dello stesso problema: prezzo giusto, processo ripetibile,"
        " controllo indipendente.",
    )
    + "<div class='body stack'><div class='unit grid3'>"
    + figure("Beggiato guida · golden rule", "30%", "Close rate: sotto 20% troppo basso, sopra 60% quasi impossibile mantenerlo.")
    + figure("Team Marketing AI · tempo", "20 min", "Da un URL a pagella, ads, funnel, piano SEO, sequenza email, PDF cliente.")
    + figure("Belli/Codex · falle trovate", "3 casi su 3", "Un giudice di famiglia di modello diversa ha trovato falle Alte in deliverable gia' “pronti”.", acc=True)
    + "</div></div>"
)

# ============================================================ 11 · copertura e chiusura
doc.page(
    head(
        "—",
        "Copertura e fonti",
        "Contato sul disco, <span class='soft'>non dichiarato a memoria.</span>",
        "",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Misura", "Numero"],
        [
            ["*Pagine wiki fonte totali", "73"],
            ["*Taggate come pertinenti ad agenzia", "11"],
            ["*Entrate in questo libro", "7"],
            ["*Fuori perimetro (dichiarato)", "4 — copywriting freelance e infobusiness, corpus diverso"],
            ["*Skill di produzione DE citate in Parte Prima", "9"],
        ],
    )
    + "</div><div class='unit push'>"
    + "<div class='kicker'><span class='n'>—</span>Dove vive questo libro</div>"
    "<ul class='clean'>"
    "<li><strong>Originale:</strong> PIANO-MAESTRO/34-LIBRO-AGENCY.md</li>"
    "<li><strong>Missione:</strong> EMP-W4K7 — checkpoint CP-20260909-2CWF e successivi</li>"
    "<li><strong>Doppione:</strong> documentazione Empire/Piani/Agency/</li>"
    "</ul></div></div>"
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
    args = ap.parse_args()
    doc.build(html_only=args.html_only)
    return 0


if __name__ == "__main__":
    sys.exit(main())
