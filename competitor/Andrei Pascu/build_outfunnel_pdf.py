# -*- coding: utf-8 -*-
"""build_outfunnel_pdf.py — PDF standard-oro di OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.md"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "PIANO-MAESTRO", "scripts")))
from pdf_engine_empire import PDFDoc  # noqa: E402

doc = PDFDoc(
    title="outFunnel — documentazione ufficiale",
    doc_label="outFunnel · documentazione ufficiale · 9 settembre 2026",
    footer_left="outFunnel · Andrei Pascu · documentazione ufficiale",
    out_html=os.path.join(HERE, "OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.html"),
    out_pdf=os.path.join(HERE, "OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.pdf"),
)
head, tab, figure = doc.head, doc.tab, doc.figure

# 01 · copertina
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>out<span class='acc'>Funnel</span><br><span class='soft'>documentazione</span> ufficiale.</h1>
  <p class='cover-lead'>20 lezioni, 4 sezioni, 114 atomi di conoscenza. Corso completo del bundle
  Armageddon di Andrei Pascu, ingerito e sintetizzato per intero.</p>
  <div class='cover-meta'>
    <div><div class='k'>Stato</div><div class='v'>20/20 completo</div></div>
    <div><div class='k'>Tipo</div><div class='v'>100% teoria</div></div>
    <div><div class='k'>Framework</div><div class='v'>4 portanti</div></div>
    <div><div class='k'>Per</div><div class='v'>Digital Empire</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Emperator · 9 settembre 2026",
    foot_r="Studio Andrei Pascu",
)

# 02 · A — cos'e'
doc.page(
    head("A", "Il corso", "Quattro sezioni, <span class='soft'>venti lezioni.</span>",
         "Tutte classificate TEORIA — framework e strategia, nessuna dimostrazione software. "
         "Verificato lezione per lezione, non solo dal titolo.")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Sezione", "~Lezioni", "Argomento"],
        [
            ["*1 — Le basi", "~1-8", "Cos'è un funnel, consapevolezza, tipi, come si costruisce"],
            ["*2 — Esempi strategici", "~9-11", "Lead magnet, sequenze email, upsell/cross-sell"],
            ["*3 — Strategie avanzate", "~12-16", "Diagnosi fra step, KPI, segmentazione, evoluzione"],
            ["*4 — Esempi completi", "~17-20", "Quattro blueprint, dal gratuito al costoso"],
        ],
    )
    + "</div></div>"
)

# 03 · B — i quattro framework
doc.page(
    head("B", "Framework", "Quattro principi, <span class='soft'>ripetuti e composti.</span>",
         "Il corso non è 20 idee scollegate: quattro principi tornano piu' volte e si compongono "
         "nel blueprint finale (Lezione 20).")
    + """
<div class='body stack-tight'>
  <div class='unit step'>
    <div class='idx'>01</div>
    <div><h3>I 5 Livelli di Consapevolezza</h3>
    <p class='note'>Non consapevole → del problema → della soluzione → del prodotto →
    Completamente consapevole (Lezione 2, ripreso in 4/8/15). Ogni fase del funnel va scritta
    per il livello del lettore in quel punto.</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>02</div>
    <div><h3>"Paga poco oggi, paga tanto domani"</h3>
    <p class='note'>Il Tripwire (Lezioni 6/9/11/20), il principio piu' ripetuto del corso: un
    primo acquisto minimo predice acquisti futuri molto piu' grandi.</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>03</div>
    <div><h3>Misura prima di cambiare</h3>
    <p class='note'>CR, CPC, CPA, CPL, ROI per ogni step (Lezioni 13/14). L'errore piu' citato:
    dare per scontato che il problema sia sempre nell'ultimo step.</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>04</div>
    <div><h3>Il messaggio prima del funnel</h3>
    <p class='note'>Target Fixation (Lezione 4): si parte dal messaggio per il target, mai
    dall'obiettivo di vendita a secco.</p></div>
  </div>
</div>
"""
)

# 04 · C — i 20 blueprint (tabella grande, spezzata su due pagine)
doc.page(
    head("C", "I venti blueprint", "Ogni lezione, <span class='soft'>in una riga.</span>",
         "Il dettaglio con fonte esatta vive nei 20 lesson-analysis.md del run. Lezioni 1-11.")
    + "<div class='body'><div class='unit'>"
    + tab(
        ["#", "Lezione", "Cosa consegna"],
        [
            ["*1", "Cos'è un funnel", "Definizione, TOF/BOF, funnel classico a 7 step"],
            ["*2", "Livelli di consapevolezza", "I 5 livelli (framework Schwartz)"],
            ["*3", "Obiettivi di un funnel", "4 obiettivi: email, sales team, diretta, awareness"],
            ["*4", "Come creare un funnel", "3 fasi + Target Fixation + processo a 4 passi"],
            ["*5", "Funnel reali", "3 case study + tassonomia a 3 pattern"],
            ["*6", "Tipi di funnel", "8 tipologie catalogate"],
            ["*7", "Pezzi del puzzle", "Glossario: popup, thank you page, email, order bump"],
            ["*8", "Step di un funnel completo", "Le 7 fasi di costruzione"],
            ["*9", "Lead magnet", "10 tipologie, 'paga poco = predittore'"],
            ["*10", "Sequenze automatiche", "Blast / Automatica / Follow-up + timing"],
            ["*11", "Upsell/cross-sell", "Definizioni, mai svalutare il primo acquisto"],
        ],
    )
    + "</div></div>"
)
doc.page(
    head("C", "I venti blueprint", "Ogni lezione, <span class='soft'>in una riga.</span>",
         "Continua. Lezioni 12-20.")
    + "<div class='body'><div class='unit'>"
    + tab(
        ["#", "Lezione", "Cosa consegna"],
        [
            ["*12", "Considerazioni fra step", "Checklist a 7 fattori diagnostici"],
            ["*13", "Funnel troubleshooting", "CR per step, non fissarsi sull'ultimo"],
            ["*14", "KPIs", "5 formule (CR/CPC/CPA/CPL/ROI) + 6 KPI"],
            ["*15", "Segmentazione audience", "Copy apparente/specifico, tag, lead scoring"],
            ["*16", "Evoluzione nel tempo", "Evergreen vs Promozionale, ads a countdown"],
            ["*17", "Lead Magnet Funnel", "Blueprint a 5 step, redirect istantaneo"],
            ["*18", "Sales Page Funnel", "Blueprint a 3 livelli di maturità"],
            ["*19", "High-price sales team Funnel", "Soglia 3.000€, sales page come filtro"],
            ["*20", "Full funnel example", "Blueprint finale a 6 step, sintesi del corso"],
        ],
    )
    + "</div></div>"
)

# 05 · D — scoperta + candidati DE
doc.page(
    head("D", "Impatto", "Un cerchio <span class='soft'>che si chiude.</span>",
         "Il difetto piu' costoso mai misurato sul sito reale di Andrei Pascu e' l'errore esatto "
         "che il suo corso insegna a non fare.")
    + """
<div class='body stack'>
  <div class='unit fix'>
    <div class='tag'>Scoperta</div>
    <h3>L'autore vende il controllo che lo avrebbe salvato</h3>
    <p class='note'>La cassa reale di Armageddon (/vendita) manda a un 404 — il difetto piu'
    costoso misurato in tutto lo studio (<span class='mono'>ANATOMIA-DEI-LANCI.md</span>). La
    Lezione 13 di outFunnel insegna esattamente il controllo opposto: "non dare per scontato che
    il problema sia sempre nell'ultimo step". Controprova diretta che il controllo 8 del gate
    della Fabbrica Siti (ADR-024) e' quello giusto.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Tre candidati concreti per Digital Empire</div>
    <ul class='clean'>
      <li><strong>Blueprint Lezione 20</strong> (Tripwire → upsell) — diretto per
      TASK-LANCI-PIANO-DEFINITIVO-W3, il piano del primo lancio.</li>
      <li><strong>Test "copy apparente vs specifico"</strong> (Lezione 15) — arricchimento diretto
      di <span class='mono'>cro-copy-architect</span> (framework APSOC).</li>
      <li><strong>Ads dinamiche a countdown</strong> (Lezione 16) — spiega il meccanismo di
      scarsita' gia' osservato in produzione su Armageddon.</li>
    </ul>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Dove vive questo studio</div>
    <ul class='clean'>
      <li><strong>Documentazione:</strong> competitor/Andrei Pascu/OUTFUNNEL-DOCUMENTAZIONE-UFFICIALE.md</li>
      <li><strong>Dettaglio grezzo:</strong> runs/andrei-pascu-armageddon-outfunnel-001/ (20 lesson-analysis.md)</li>
      <li><strong>Miglioramenti proposti:</strong> competitor/Andrei Pascu/MIGLIORAMENTI-DIGITAL-EMPIRE.md</li>
      <li><strong>Profilo integrale:</strong> competitor/Andrei Pascu/ANDREI-PASCU-DOSSIER-COMPLETO.md</li>
    </ul>
  </div>
</div>
"""
)

if __name__ == "__main__":
    doc.build(html_only="--html-only" in sys.argv)
