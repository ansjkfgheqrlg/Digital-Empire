# -*- coding: utf-8 -*-
"""build_piano_implementazione_pdf.py — PDF standard-oro di PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.md"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "PIANO-MAESTRO", "scripts")))
from pdf_engine_empire import PDFDoc  # noqa: E402

OUT = os.path.join(HERE, "piano-implementazione")

doc = PDFDoc(
    title="Piano di implementazione — Andrei Pascu",
    doc_label="Piano di implementazione · Andrei Pascu · 10 settembre 2026",
    footer_left="Piano di implementazione · studio Andrei Pascu",
    out_html=os.path.join(OUT, "PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.html"),
    out_pdf=os.path.join(OUT, "PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.pdf"),
)
head, tab, figure = doc.head, doc.tab, doc.figure

# 01 · copertina
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>Piano di <span class='acc'>implementazione</span>.<br><span class='soft'>Cosa cambia</span> davvero.</h1>
  <p class='cover-lead'>Tutto lo studio Andrei Pascu trasformato in azioni eseguibili, criticato
  tre volte prima di essere consegnato. Il giudizio e' uno solo: se fra un mese non e' entrato un
  euro e il documento e' ancora bello, e' fallito.</p>
  <div class='cover-meta'>
    <div><div class='k'>Azioni</div><div class='v'>34 + 5</div></div>
    <div><div class='k'>Giri di critica</div><div class='v'>tre</div></div>
    <div><div class='k'>Decisioni</div><div class='v'>7 chiuse</div></div>
    <div><div class='k'>Codice</div><div class='v'>gia' vivo</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Emperator · 10 settembre 2026",
    foot_r="EMP-APPLAN1",
)

# 02 · A — la pagina che conta
doc.page(
    head("A", "Le prime cinque", "Se leggi <span class='soft'>solo questa pagina,</span> hai il piano.",
         "Le altre 34 azioni vengono dopo queste cinque, non prima. La ragione e' un fatto "
         "verificato sul disco, non un'opinione: l'Impero possiede gia' il codice per incassare, "
         "e non l'ha mai acceso.")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["#", "Azione", "Chi", "Costo", "Cosa sblocca"],
        [
            ["*1", "Payment Link Stripe del Manuale a 67 EUR (e bump a 27), URL incollati",
             "solo Max", "10 min", "il primo euro: senza, non esiste cassa"],
            ["*2", "Accendere il rail nel checkout.config.json e spostare la scadenza gia' passata",
             "una sessione", "15 min", "la cassa diventa raggiungibile"],
            ["*3", "Adattare email-agent/main.py alla consegna del Manuale",
             "una sessione", "2-3 h", "chiude il ciclo euro -> prodotto"],
            ["*4", "Ruotare la chiave Brevo esposta in chiaro (B-020)",
             "solo Max", "10 min", "niente: e' rischio aperto, non incasso"],
            ["*5", "Contare il pubblico vero del giorno 1, e da quale canale",
             "Emperator + Max", "1 h", "decide se gli altri quattro valgono"],
        ],
        hi=0,
    )
    + "</div><div class='unit'><p>Nessuna di queste cinque blocca le altre: l'azione 4 e' urgente da "
      "sola, l'azione 5 blocca la <em>data</em> del lancio, mai la costruzione (ADR-028).</p></div></div>"
)

# 03 · B — il codice gia' vivo
doc.page(
    head("B", "Il ritrovamento", "Manca un gesto da <span class='soft'>dieci minuti,</span> non una build.",
         "Mentre si scrivevano 1.352 righe di specifica, due pezzi di codice funzionanti erano "
         "gia' sul disco, mai collegati fra loro.")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Pezzo", "Cosa fa gia'", "Cosa manca"],
        [
            ["*empire/tools/checkout.py", "13.819 byte, legge la configurazione della cassa",
             "gli URL dei rail: tutti spenti tranne l'ordine via email"],
            ["*checkout.config.json", "prezzo Manuale 67 lancio / 97 listino / 27 bump",
             "scadenza lancio ferma al 31/07/2026, gia' passata"],
            ["*email-agent/main.py", "webhook che verifica la firma Stripe e consegna il PDF via Gmail",
             "il prodotto giusto: oggi serve un altro ebook"],
        ],
    )
    + "</div><div class='unit'><p>Il campo del primo rail dice, testuale: <code>\"richiede\": "
      "\"MAX: crea Payment Link su Stripe\"</code>. Il prezzo non e' una scelta aperta: "
      "<strong>DEC-EST-001</strong> lo ha fissato il 21 luglio per silenzio-assenso, ed e' vivo nel "
      "file da allora. Una decisione presa e dimenticata costa quanto una decisione mai presa.</p>"
      "</div></div>"
)

# 04 · C — cosa cambia davvero (1)
doc.page(
    head("C", "Cosa cambia", "Dieci righe, <span class='soft'>lo studio intero</span> guardato insieme.",
         "Non lezione per lezione: la sostanza di metodo, visivo, copy e lanci messi uno accanto "
         "all'altro.")
    + """<div class='body stack'>
<div class='unit'><p><strong>1 · Non si scrivono pagine nuove per lanciare: si specchia e si
rilancia.</strong> E' il vantaggio vero di Andrei — non un funnel piu' pulito, ma il costo di
produzione vicino a zero. Applicato al nostro magazzino: i 25 pezzi finiti e mai usciti, il piu'
vecchio da oltre 142 giorni, sono materiale di lancio, non archivio.</p></div>
<div class='unit'><p><strong>2 · Prima si accende cio' che esiste, poi si costruisce.</strong>
ADR-003 vale anche per il denaro.</p></div>
<div class='unit'><p><strong>3 · Nessuna azione e' fatta finche' non nomina chi la consuma.</strong>
Uno script che nessun gate invoca e' un pezzo per ULTIMO METRO.</p></div>
<div class='unit'><p><strong>4 · Nessun numero senza fonte.</strong> Tre cifre del piano erano
inventate; una quarta era vera ma ne sostituiva silenziosamente un'altra.</p></div>
<div class='unit'><p><strong>5 · Il prezzo del Manuale era gia' deciso e nessuno lo sapeva.</strong>
Quattro documenti hanno discusso fasce alternative per settimane.</p></div>
</div>"""
)

# 05 · C2 — cosa cambia davvero (2)
doc.page(
    head("C", "Cosa cambia", "Le altre <span class='soft'>cinque righe.</span>", "")
    + """<div class='body stack'>
<div class='unit'><p><strong>6 · Un impedimento ferma solo se stesso.</strong> Per questo ogni
azione porta la colonna «blocca esattamente», e i due gesti che spettano a Max non fermano le altre
32 azioni (ADR-028).</p></div>
<div class='unit'><p><strong>7 · Le tre critiche non concordavano, e va bene cosi'.</strong> Due
Sentinelle sullo stesso angolo, che non si conoscevano, hanno prodotto conteggi diversi: e' la prova
che una critica sola non basta.</p></div>
<div class='unit'><p><strong>8 · La disciplina si aggiunge dove passa il denaro, non ovunque.</strong>
Su 34 azioni, zero producevano un euro diretto e l'82% era governo o documento. La proporzione si
inverte: prima la cassa, poi le griglie.</p></div>
<div class='unit'><p><strong>9 · Il gate si chiude collegandolo, non costruendolo.</strong> Il commit
che crea lo strumento contiene anche la riga che lo rende obbligatorio.</p></div>
<div class='unit'><p><strong>10 · Il piano stesso e' soggetto al proprio esame.</strong> Se fra un
mese e' ancora un bel documento senza un euro dietro, e' il pezzo 26 di ULTIMO METRO — e va detto,
non nascosto.</p></div>
</div>"""
)

# 06 · D — le decisioni
doc.page(
    head("D", "Decisioni", "Sei contraddizioni, <span class='soft'>sciolte una per una.</span>",
         "L'assemblaggio le ha lasciate aperte, come doveva. Da adesso valgono queste, e le "
         "versioni perdenti non si ridiscutono.")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["#", "La divergenza", "Decisione"],
        [
            ["*D1", "33 azioni o 34", "34, contate per ID distinto"],
            ["*D2", "AP-046b/047b: infrastruttura o abilita-un-euro", "abilita un euro"],
            ["*D3", "Prezzo Manuale: fascia 27-47 o altro", "67 / 97 / 27 bump — DEC-EST-001"],
            ["*D4", "Scala prezzi 98-434-999 o 98-400-999", "98 - 400 - 999, soglia prova a 349"],
            ["*D5", "AP-038 in corsia libera o riservata", "cartella riservata, contenuto libero"],
            ["*D6", "AP-041 riusa un campo o ne crea uno", "campo nuovo dedicato"],
        ],
        hi=0,
    )
    + "</div><div class='unit'><p><strong>Settima decisione, non una divergenza ma un ordine:</strong> "
      "lo script del gate finale scende dal rango 1. Si esegue in versione minima e solo nello stesso "
      "commit della riga che lo collega al gate. Mai separati.</p>"
      "<p><strong>Da correggere prima che diventi codice:</strong> la task viva della settimana 3 "
      "istruisce la scala prezzi con una cifra che non coincide con nessuna misura.</p></div></div>"
)

# 07 · E — il buco
doc.page(
    head("E", "Il buco", "La lezione che <span class='soft'>nessuno aveva</span> convertito.",
         "Cinque documenti, quattro autori diversi, e nessuno l'aveva vista. E' il pezzo di valore "
         "piu' alto di tutto il giro.")
    + """<div class='body stack'>
<div class='unit'><p>Il vantaggio competitivo di Andrei non e' un funnel migliore: e' che <strong>non
scrive mai pagine nuove per lanciare</strong>. Specchia un negozio esistente, lo spoglia, punta a una
cassa sola. Digital Empire ha 25 pezzi finiti e mai pubblicati e nessuna delle 34 azioni applica quel
metodo a quel magazzino: il draft lo usa su un solo asset, trovato per caso.</p></div>
<div class='unit'><p><strong>Il secondo buco, piu' forte del primo:</strong> il codice per incassare
esiste gia' (pagina B) e nessuna delle 34 azioni lo tocca. Collegarlo e' lavoro di poche ore contro
le 28-46 ore stimate dal piano combinato.</p></div>
<div class='unit'><p><strong>Il terzo, aggiunto dall'ultimo giro:</strong> nessuno dei cinque
documenti chiede quante persone vere vedranno la pagina il giorno dell'apertura, mentre il canale
previsto e' spento da fine luglio. Prezzo firmato, cassa accesa, pagina viva e gate a posto,
moltiplicati per zero visitatori, fanno zero euro.</p></div>
<div class='unit'><p><strong>Rischio aperto, fuori piano:</strong> una chiave di servizio e' esposta
in chiaro sul repository da mesi, marcata come la piu' urgente e mai ruotata. Non blocca niente del
piano — ma non aspetta il piano.</p></div>
</div>"""
)

# 08 · F — come e' nato
doc.page(
    head("F", "Il metodo", "Criticato <span class='soft'>tre volte,</span> e ogni giro attacca il giro prima.",
         "Non il documento originale: il giro precedente. E' la regola che impedisce a un piano di "
         "innamorarsi di se stesso.")
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Giro", "Chi", "Cosa ha prodotto"],
        [
            ["*P0", "2 Doom Bot", "i due draft: 34 azioni e 4 verdetti go/no-go"],
            ["*P1", "3 Sentinelle indipendenti", "governo e collisioni; denaro e verita', due volte"],
            ["*P2", "Fable", "quali colpi delle critiche reggono e quali crollano"],
            ["*Assemblaggio", "Scagnozzo", "sei fonti in un documento, zero decisioni proprie"],
            ["*P3", "Emperator", "le sette decisioni, la prima pagina, questo PDF"],
        ],
    )
    + "</div><div class='unit'><p>Le due Sentinelle sull'angolo del denaro non sapevano l'una "
      "dell'altra: hanno contato le azioni in modo diverso e classificato due voci all'opposto. La "
      "contraddizione non e' stata nascosta — e' arrivata fino a qui, ed e' stata decisa a pagina D. "
      "Un colpo su tutti e' stato respinto dal giro successivo, e l'azione colpita e' tornata "
      "viva.</p></div></div>"
)

doc.build()
print("PDF fatto:", os.path.join(OUT, "PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.pdf"))
