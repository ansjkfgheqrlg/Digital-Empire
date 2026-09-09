# -*- coding: utf-8 -*-
"""build_cs2online_pdf.py — PDF standard-oro di CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.md"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "PIANO-MAESTRO", "scripts")))
from pdf_engine_empire import PDFDoc  # noqa: E402

doc = PDFDoc(
    title="Claude Speedrun 2 — documentazione ufficiale",
    doc_label="Claude Speedrun 2 · documentazione ufficiale · 9 settembre 2026",
    footer_left="Claude Speedrun 2 · Andrei Pascu · documentazione ufficiale",
    out_html=os.path.join(HERE, "CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.html"),
    out_pdf=os.path.join(HERE, "CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.pdf"),
)
head, tab, figure = doc.head, doc.tab, doc.figure

# 01 · copertina
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>Claude<span class='acc'> Speedrun 2</span><br><span class='soft'>documentazione</span> ufficiale.</h1>
  <p class='cover-lead'>Corso a pagamento (249€) di Andrei Pascu sull'uso di Claude/AI per il
  business. Non marketing: freelance, copywriting, coding, produttivita'. Studio in corso,
  documentato con onesta' sullo stato reale.</p>
  <div class='cover-meta'>
    <div><div class='k'>Stato</div><div class='v'>20/40 — 50%</div></div>
    <div><div class='k'>Tipo</div><div class='v'>Teoria + pratica reale</div></div>
    <div><div class='k'>Blocchi</div><div class='v'>7 totali</div></div>
    <div><div class='k'>Per</div><div class='v'>Digital Empire</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Emperator · 9 settembre 2026",
    foot_r="Studio Andrei Pascu",
)

# 02 · A — cos'e' + tabella blocchi
doc.page(
    head("A", "Il corso", "Sette blocchi, <span class='soft'>meta' del cammino.</span>",
         "Piattaforma membership diversa da outFunnel (login via iframe). Qui esistono lezioni "
         "VERAMENTE pratiche — demo schermo reali, verificate frame-by-frame, non solo dal titolo.")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Blocco", "Lezioni", "Fatte", "Stato"],
        [
            ["*AI — Le basi", "9 (L1-L9)", "9/9", "completo"],
            ["*AI — produttivita'/freelance", "3 (L10-L12)", "2/3", "L12 pending"],
            ["*AI — copywriting", "4 (L13-L16)", "2/4", "L14-15 pending"],
            ["*AI — coding e simili", "7 (L17-L23)", "1/7", "L18-23 pending"],
            ["*AI — altri utilizzi", "1 (L24)", "0/1", "pending"],
            ["*Bonus", "6", "6/6", "completo"],
            ["*CS2 (sezione avanzata)", "10 (C1-C10)", "0/10", "tutta pending"],
        ],
    )
    + "</div></div>"
)

# 03 · B — i due blocchi completi
doc.page(
    head("B", "Completo", "Due blocchi, <span class='soft'>chiusi per intero.</span>",
         "Fondamenta e automazione per freelance: cio' che il corso ha gia' consegnato per intero.")
    + """
<div class='body stack-tight'>
  <div class='unit step'>
    <div class='idx'>01</div>
    <div><h3>AI — Le basi (9/9)</h3>
    <p class='note'>Cos'e' un LLM (non pensa, predice token), i 3 modelli principali (ChatGPT/
    Claude/Gemini) e perche' Claude, il principio 80/20 (l'AI fa il tattico, l'operatore il 20%
    strategico che genera l'80% del valore), tipi di contesto e come costruirlo (context
    engineering). 2 lezioni pratiche confermate con demo reali (L6 "Cucinando il tuo contesto",
    L9 "Come dare contesto alle AI").</p></div>
  </div>
  <div class='unit step'>
    <div class='idx'>02</div>
    <div><h3>Bonus (6/6)</h3>
    <p class='note'>SOP e automazione per freelance: documentare-eliminare-implementare come
    metodo per integrare l'AI nei processi esistenti; cadenza di aggiornamento AI trimestrale/
    semestrale (anti-ansia); advertising report per clienti, collegare Claude a servizi esterni,
    Claude Skills, automazione di processi con skill. Mix teoria/pratica, tutte confermate.</p></div>
  </div>
</div>
"""
)

# 04 · C — scoperta + patch applicata
doc.page(
    head("C", "Impatto", "Non solo un candidato: <span class='soft'>una patch reale.</span>",
         "L'unico caso, in tutto lo studio Andrei Pascu, in cui una lezione ha gia' modificato una "
         "skill esistente — non solo segnalato un candidato.")
    + """
<div class='body stack'>
  <div class='unit fix'>
    <div class='tag'>Scoperta</div>
    <h3>Convergenza confermata 3 volte indipendenti</h3>
    <p class='note'>La tecnica "ricerca voice-of-customer da recensioni YouTube" e' comparsa in 2
    video YouTube gratuiti (run <span class='mono'>andrei-pascu-001</span>) E nella Lezione 13 di
    questo corso a pagamento. Tre fonti indipendenti, stesso principio.</p>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Patch applicata</div>
    <ul class='clean'>
      <li><strong>Dove:</strong> <span class='mono'>.claude/skills/copywriting/SKILL.md</span>,
      sezione "Customer Language Over Company Language".</li>
      <li><strong>Quando:</strong> 2026-08-29.</li>
      <li><strong>Da cosa:</strong> cs2online Lezione 13 + 2 video YouTube gratuiti, convergenza
      a 3 fonti indipendenti.</li>
    </ul>
  </div>
</div>
"""
)

# 05 · D — anomalie + resta da fare
doc.page(
    head("D", "Aperto", "Un'anomalia chiusa, <span class='soft'>cinque blocchi da finire.</span>",
         "Cio' che resta, dichiarato senza arrotondare per non perderlo nel passaggio da run a "
         "documentazione ufficiale.")
    + """
<div class='body stack'>
  <div class='unit fix'>
    <div class='tag'>Anomalia — risolta 2026-09-09</div>
    <h3>2 skill cercate nel roster sbagliato</h3>
    <p class='note'><span class='mono'>prompt-engegniring-skill</span> (Lezione 2) e
    <span class='mono'>client-handover</span> (Lezione 10) erano state cercate solo nel roster
    globale <span class='mono'>C:\\Users\\Utente\\.claude\\skills\\</span>. Esistono entrambe nel
    roster locale di questo progetto (<span class='mono'>.claude/skills/</span>). Non era un
    disallineamento: era il raggio di ricerca incompleto.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Resta da fare (20/40)</div>
    <ul class='clean'>
      <li><strong>L12</strong> — preventivi con Claude, tensione aperta con
      <span class='mono'>beast-preventivi</span>.</li>
      <li><strong>L14-15</strong> — co-work, questionario ricerca copywriting con AI.</li>
      <li><strong>L18-23</strong> — blocco coding (diagrammi, caroselli, Sites, Sheets,
      dashboard, popup). Titoli UI non corrispondono agli slug URL, verificare il contenuto reale.</li>
      <li><strong>L24</strong> — brand guidelines con Claude.</li>
      <li><strong>C1-C10</strong> — intera sezione avanzata CS2 non ancora aperta.</li>
    </ul>
  </div>
</div>
"""
)

if __name__ == "__main__":
    doc.build(html_only="--html-only" in sys.argv)
