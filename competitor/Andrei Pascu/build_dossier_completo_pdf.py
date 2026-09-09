# -*- coding: utf-8 -*-
"""build_dossier_completo_pdf.py — PDF standard-oro di ANDREI-PASCU-DOSSIER-COMPLETO.md"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "PIANO-MAESTRO", "scripts")))
from pdf_engine_empire import PDFDoc  # noqa: E402

doc = PDFDoc(
    title="Andrei Pascu — dossier completo",
    doc_label="Andrei Pascu · dossier completo · 9 settembre 2026",
    footer_left="Andrei Pascu · dossier completo · profilo integrale",
    out_html=os.path.join(HERE, "ANDREI-PASCU-DOSSIER-COMPLETO.html"),
    out_pdf=os.path.join(HERE, "ANDREI-PASCU-DOSSIER-COMPLETO.pdf"),
)
head, tab, figure = doc.head, doc.tab, doc.figure

# 01 · copertina
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>Andrei<span class='acc'> Pascu</span><br><span class='soft'>dossier</span> completo.</h1>
  <p class='cover-lead'>Profilo integrale del concorrente: chi e', come costruisce, cosa scrive,
  come lancia, cosa insegna contro cosa fa davvero. Indice ragionato su oltre 150.000 parole di
  studio — 52 pagine di siti, 40 lezioni di corso.</p>
  <div class='cover-meta'>
    <div><div class='k'>Domini</div><div class='v'>7 · 187 URL</div></div>
    <div><div class='k'>Pagine studiate</div><div class='v'>52</div></div>
    <div><div class='k'>Lezioni ingerite</div><div class='v'>40/70</div></div>
    <div><div class='k'>Per</div><div class='v'>Digital Empire</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Emperator · 9 settembre 2026",
    foot_r="Studio Andrei Pascu",
)

# 02 · A — chi e' + prodotti/prezzi
doc.page(
    head("A", "Chi e'", "Sette domini, <span class='soft'>187 URL, due fronti.</span>",
         "Concorrente diretto su copywriting/CRO (come l'agenzia) e su un corso Claude/AI per il "
         "business (in competizione col Manuale Claude Code).")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Prodotto", "Prezzo", "Cosa è"],
        [
            ["*outHeadline", "98 €", "strumento tecnico di copy"],
            ["*outEmail", "139 €", "email marketing"],
            ["*outFunnel", "434 €", "funnel — documentato per intero"],
            ["*Claude Speedrun 2", "249 €", "uso di Claude/AI per il business"],
            ["*Funnel Operator", "434 €", "percorso professionale"],
            ["*Vendita101", "400 €", "sales page, mai barrata"],
            ["*Copywriting Mentorship", "349 / 999 €", "BASE / COMPLETO, promessa ampia"],
            ["*Armageddon (bundle)", "199 €", "4 prodotti, listino 585 € + voucher 199 €"],
            ["*«Claude Code Mastery», 397 €", "—", "NON è suo: è di Digital Empire (Max)"],
        ],
    )
    + "</div></div>"
)

# 03 · B — il metodo
doc.page(
    head("B", "Il metodo", "Come costruisce, <span class='soft'>non come appare.</span>",
         "Cinque leggi misurate su 52 pagine e 7 domini.")
    + """
<div class='body stack-tight'>
  <div class='unit step'>
    <div class='idx'>01</div>
    <div><h3>La piattaforma si sceglie dal lavoro</h3>
    <p class='note'>Negozio permanente → Squarespace. Lancio a finestra breve → a mano. Agenzia
    B2B → a mano con kit condiviso. La disciplina cresce col valore del cliente, non col prezzo.</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>02</div>
    <div><h3>Non personalizza dove non conta</h3>
    <p class='note'>Il custom.css del negozio pesa lo 0,02% del peso scaricato. Il valore delle
    44 pagine di negozio sta nel copy e nella sequenza, non nel codice.</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>03</div>
    <div><h3>Il lancio si specchia, non si scrive</h3>
    <p class='note'>Pagine prodotto copiate e spogliate, tutte ripuntate a una cassa sola. Il
    mirror non è congelato: viene mantenuto (l'originale dice "2025", la copia dice "2026").</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>04</div>
    <div><h3>Tutto ciò che si ripete diventa uno stampo</h3>
    <p class='note'>La pre-cassa è un generatore a sei variabili. I blocchi di copy attraversano
    prodotti diversi identici carattere per carattere.</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>05</div>
    <div><h3>Lucida dove convince, lascia i difetti dove si transita</h3>
    <p class='note'>Non è sciatteria diffusa: è una scelta di dove spendere l'attenzione. Ha un
    costo che probabilmente non ha misurato — vedi §F.</p></div>
  </div>
</div>
"""
)

# 04 · C — sistema visivo + sistema di copy
doc.page(
    head("C", "Cosa scrive e come appare", "Due sistemi, <span class='soft'>una sola logica.</span>",
         "Sistema visivo: 52 pagine contate a macchina. Sistema di copy: 22 formule cablate.")
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Sistema visivo</div>
    <ul class='clean'>
      <li>Quattro volte meno immagini per pagina dove costruisce a mano rispetto a Squarespace.</li>
      <li>38 pagine su 52 non dichiarano un carattere proprio (sans-serif implicito).</li>
      <li>Il prezzo non governa la forma: è la <strong>temperatura del traffico</strong> a
      decidere — pagine fredde 4,9 CTA medie, pagine calde 16,2 CTA medie.</li>
    </ul>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Sistema di copy</div>
    <ul class='clean'>
      <li>Formula fissa a 11 tappe per le sales page complete, più chiusura legale che non devia mai.</li>
      <li>Più il prodotto è verificabile, più le prove sono esterne; più è un mindset, più
      l'effetto Barnum sostituisce la fonte (outHeadline 0 fonti → Mentorship 5).</li>
      <li>Il prezzo si ancora sempre prima di rivelarsi. Il codice sconto CWSHOP -20% è cablato,
      identico su 4 prodotti diversi.</li>
      <li>"Recensioni" copre due livelli opposti: widget Trustpilot reale contro 42 screenshot
      muti con <span class='mono'>alt=""</span> vuoto.</li>
    </ul>
  </div>
</div>
"""
)

# 05 · D — come lancia
doc.page(
    head("D", "Come lancia", "Il caso Armageddon, <span class='soft'>smontato pezzo per pezzo.</span>",
         "Un lancio vivo colto mentre girava: 199€ pagati, 784€ dichiarati.")
    + """
<div class='body stack-tight'>
  <div class='unit fix'>
    <div class='tag'>Il fatto</div>
    <h3>Il pacchetto costa quanto il voucher</h3>
    <p class='note'>199€ pagati, voucher da 199€ + 4 prodotti (listino 585€). L'ancora è
    verificabile: è la somma dei listini reali del negozio.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Sei mosse ripetibili</div>
    <ul class='clean'>
      <li>Non scrive pagine nuove: le specchia dal negozio.</li>
      <li>Spoglia ogni script della piattaforma.</li>
      <li>Ripunta tutto a una cassa sola, un solo link Stripe.</li>
      <li>Sostituisce il prezzo con un badge di appartenenza ("INCLUSO NEL PACCHETTO").</li>
      <li>Mantiene il mirror vivo, non lo congela.</li>
      <li>Tiene l'offerta su una pagina madre corta (5.103px contro 10.000-27.000px normali).</li>
    </ul>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Lo stampo di pre-cassa</div>
    <p class='note'>Sei elementi fissi — occhiello, nome, istruzione+sconto, cifra isolata, "Una
    tantum", bottone. Un generatore, non una pagina. Il rapporto tipografico più aggressivo
    dell'ecosistema: "Risparmi €585" a 81,6px contro il prezzo pagato a 14,88px.</p>
  </div>
</div>
"""
)

# 06 · E — cosa insegna vs cosa fa
doc.page(
    head("E", "Il cerchio che si chiude", "Insegna <span class='soft'>l'esatto errore che commette.</span>",
         "Il difetto più costoso mai misurato in tutto lo studio.")
    + """
<div class='body stack'>
  <div class='unit fix'>
    <div class='tag'>Cosa insegna</div>
    <h3>outFunnel Lezione 13</h3>
    <p class='note'>"Non dare per scontato che il problema sia sempre nell'ultimo step" — misura
    il CR per ogni step del funnel prima di intervenire.</p>
  </div>
  <div class='unit fix'>
    <div class='tag'>Cosa fa</div>
    <h3>La cassa reale di Vendita101 risponde 404</h3>
    <p class='note'><span class='mono'>/vendita → /acquista-v101</span>: 404. La cassa vera
    (<span class='mono'>/vendita101-pre</span>, 400€) non è linkata da nessuna parte. Un prodotto
    da 400€ è orfano della sua pagina di vendita principale.</p>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Perché conta più degli altri difetti</div>
    <p class='note'>La pagina di vendita funziona benissimo — nessuno se ne accorge, ma la cassa
    irraggiungibile azzera ogni euro che il copy ha guadagnato. Controprova diretta del
    <strong>controllo 8 di ADR-024</strong>, primo gate obbligatorio dell'ecosistema LANCI.</p>
  </div>
</div>
"""
)

# 07 · F — stato dello studio
doc.page(
    head("F", "Stato reale", "Onesto, <span class='soft'>contato sul disco.</span>",
         "Cosa è chiuso, cosa resta, senza arrotondare.")
    + "<div class='body'><div class='unit'>"
    + tab(
        ["Corso/area", "Stato", "%"],
        [
            ["*outFunnel", "20/20 lezioni", "100%"],
            ["*Claude Speedrun 2 (cs2online)", "20/40 lezioni", "50%"],
            ["*outHeadline", "30/30 testo grezzo, 0 classificato", "0%"],
            ["*outEmail, outViral 2", "non iniziati", "0%"],
            ["*Studio dei siti", "52/187 URL catturate e chiuse", "~28%"],
        ],
    )
    + "</div></div>"
    + """
<div class='body' style='margin-top:12px'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Due anomalie mai risolte</div>
    <p class='note'><span class='mono'>prompt-engegniring-skill</span> e
    <span class='mono'>client-handover</span> — dichiarate nel roster del corso, non trovate su
    disco. Segnalato a Max due volte.</p>
  </div>
</div>
"""
)

if __name__ == "__main__":
    doc.build(html_only="--html-only" in sys.argv)
