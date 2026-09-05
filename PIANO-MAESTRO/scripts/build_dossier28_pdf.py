"""
build_dossier28_pdf.py — Dossier 28 (Higgsfield + ElevenLabs) in PDF impaginato.

Contenuto di questo dossier sopra il motore riusabile `pdf_engine_empire.py` (standard-oro
dichiarato da Max il 2026-09-05). Il motore porta CSS, grana, `page/head/tab/figure`; qui
resta solo il contenuto, pagina per pagina.

Sorgente dei contenuti: `PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md`.
Il markdown resta l'originale; questo file ne fa l'edizione da leggere.

Uso:
    python build_dossier28_pdf.py
    python build_dossier28_pdf.py --html-only
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
    title="Dossier 28 — Higgsfield ed ElevenLabs",
    doc_label="Dossier 28 · revisione 5 · 5 settembre 2026",
    footer_left="Dossier 28 · Higgsfield ed ElevenLabs",
    out_html=os.path.join(DEST, "28-DOSSIER-HIGGSFIELD-ELEVENLABS.html"),
    out_pdf=os.path.join(DEST, "28-DOSSIER-HIGGSFIELD-ELEVENLABS.pdf"),
)
head = doc.head
tab = doc.tab
figure = doc.figure

# ============================================================ 01 · copertina
doc.page(
    """
<div class='cover-mid'>
  <h1 class='big'>Higgsfield<br><span class='soft'>ed</span> <span class='acc'>ElevenLabs</span>.</h1>
  <p class='cover-lead'>Sessantotto pagine dei due siti lette sul DOM renderizzato, i Termini
  d’uso e la normativa italiana. Il conto è fatto sul volume di produzione dichiarato, non su
  un video singolo. Tre conclusioni delle stesure precedenti erano sbagliate e qui sono
  corrette, ognuna segnata dov’è.</p>
  <div class='cover-meta'>
    <div><div class='k'>Volume</div><div class='v'>172 video · 904 min</div></div>
    <div><div class='k'>Mese di prova</div><div class='v'>circa €139</div></div>
    <div><div class='k'>A regime</div><div class='v'>€2.113 al mese</div></div>
    <div><div class='k'>Per</div><div class='v'>Max</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Emperator · 5 settembre 2026",
    foot_r="Piano d’acquisto",
)

# ============================================================ 02 · la prima mossa
doc.page(
    head(
        "A",
        "La prima mossa",
        "Un mese di prova, <span class='soft'>mensile.</span>",
        "Nessun impegno annuale finche' le prove non hanno risposto. L’annuale sconta il 30% "
        "ma blocca dodici mesi: su un mese di prova annullerebbe la prova stessa.",
    )
    + """
<div class='body stack'>
  <div class='unit grid3'>
    """
    + figure("Higgsfield · Ultra 3.000", "€129", "Mensile. Tutti i modelli, otto job in parallelo, Canvas, Vibe Motion, Supercomputer, e i sette giorni di Kling 3.0 unlimited.")
    + figure("ElevenLabs · Creator", "$11", "Primo mese al 50%, poi $22. Voice cloning professionale, 121.000 crediti di voce, 275 minuti di chiamate.")
    + figure("Totale del mese di prova", "€139", "Il prezzo dell’opzione di dire di no. Promozioni come il 30% vengono rimesse ogni due mesi.", acc=True)
    + """
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Perché Ultra e non Plus</div>
    <p class='note'>Plus costa €59 e da' 1.200 crediti; le prove ne chiedono 2.640, quindi
    servirebbero €66 di pacchetti. Totale €125, praticamente identico — ma con sei job
    paralleli invece di otto e <strong>zero margine per gli scarti</strong>. A parità di spesa
    si prende quello che non finisce a metà prova.</p>
  </div>
  <div class='unit push'>
    <p class='quote'>«Faremo un acquisto di prova solamente per un mese, il minimo indispensabile
    per fare tutte le prove possibili. Pero' considera che le prime prove saranno scarti, perché
    sbaglieremo qualcosa.»<span class='src'>Max — 5 settembre 2026</span></p>
  </div>
</div>
"""
)

# ============================================================ 03 · le nove prove
doc.page(
    head(
        "A",
        "Il mese di prova",
        "Nove prove, <span class='soft'>con lo scarto dentro al conto.</span>",
        "Tasso di scarto 3× invece di 2×: la prima volta si sbaglia il prompt, la reference o "
        "il formato. È messo nel conto, non sperato via.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Prova", "Composizione", "~Crediti"],
        [
            ["*1 · Video YouTube", "Un segmento da 2 min provato 3 volte, poi un video intero da 10 min", "~664"],
            ["*2 · Corti Vibe Motion", "3 corti, 3 iterazioni ciascuno, sfondi condivisi", "~552"],
            ["*3 · Misura del TTS", "5 campioni di lunghezza nota — incognita, budget", "~150"],
            ["*4 · Canvas", "Costruzione gratis, 3 esecuzioni del template", "~330"],
            ["*5 · Layers su slide Arena", "10 rigenerazioni del solo testo — incognita, budget", "~80"],
            ["*6 · Avatar UGC", "300 volti Soul 2.0, training del personaggio, 1 video da 30s", "~372"],
            ["*7 · Promo prodotto 30s", "Manuale Claude Code", "~144"],
            ["*8 · Confronto premium", "Seedance 2.0, Veo 3.1 e Sora 2 Pro sulla stessa scena", "~248"],
            ["*9 · MCP da Claude Code", "10 generazioni miste guidate da qui", "~100"],
            ["*Somma più 25% di margine", "2.640 + 660", "~3.300"],
        ],
        hi=2,
        cap="Ultra da' 3.000 crediti, quindi si è 300 sotto — <strong>ma solo sulla carta</strong>: "
        "i sette giorni di Kling 3.0 unlimited coprono a mano circa 900 crediti delle prove 1, 2, 7 "
        "e in parte 4. La finestra unlimited va usata per prima, non per ultima.",
    )
    + """</div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Le regole di condotta</div>
    <ul class='clean'>
      <li><strong>Tetto di spesa nel codice:</strong> nessuna generazione sopra 50 crediti senza via libera esplicito. L’MCP non ne ha uno nativo.</li>
      <li><strong>Registro delle prove:</strong> ogni generazione annotata con modello, crediti ed esito. Senza registro il mese produce impressioni, non numeri.</li>
      <li><strong>Data del rinnovo sul calendario</strong> il giorno stesso dell’acquisto. Disdetta se due prove su tre falliscono.</li>
      <li><strong>I crediti non si riportano al mese dopo:</strong> quello che non si spende è perso, quindi le prove si fanno tutte.</li>
    </ul>
  </div>
</div>"""
)

# ============================================================ 04 · il volume
doc.page(
    head(
        "B",
        "Il conto a regime",
        "Il volume vero <span class='soft'>di Digital Empire.</span>",
        "Le stesure precedenti costavano un video singolo e si fermavano lì. Questo è il "
        "conto che decide.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Formato", "Cadenza", "~Al mese", "~Minuti"],
        [
            ["*Video YouTube 10 min", "3-2-3-2 alternata, due giorni di stop", "~70", "~700"],
            ["*Corti 1-3 min", "Tre al giorno, sei una volta a settimana", "~102", "~204"],
            ["*Chiamate agente vocale", "Cento al giorno", "~3.000", "~6.000"],
        ],
        cap="Totale: <strong>172 video e 904 minuti di video finito al mese</strong>.",
    )
    + "</div><div class='unit'>"
    + tab(
        ["Scenario", "~Cr / video YT", "~Cr / corto", "~Crediti al mese", "~Higgsfield / mese"],
        [
            ["*Magro — poche clip, molte immagini; corti di sola grafica", "~176", "~45", "~16.890", "~€635"],
            ["*Medio — b-roll vero; corti con quattro sfondi in movimento", "~349", "~109", "~35.514", "~€1.496"],
            ["*Ricco — aperture Seedance 2.0; corti con otto clip", "~645", "~175", "~63.006", "~€2.768"],
        ],
        hi=1,
        cap="Base Ultra 9.000 (€270 annuale) più pacchetti a €0,046 il credito. Tasso di riprova 2×. "
        "Calcolo riproducibile: <strong>PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py</strong>",
    )
    + "</div><div class='unit grid3'>"
    + figure("Higgsfield, scenario medio", "€1.496", "35.514 crediti al mese: quattro volte il tetto acquistabile da soli.")
    + figure("ElevenLabs, tutto compreso", "€617", "Pro più eccedenza chiamate, telefonia italiana e modello.")
    + figure("Totale mensile", "€2.113", "Circa €25.400 all’anno. Con il tasso di riprova a 1,3: €1.604 al mese.", acc=True)
    + "</div></div>"
)

# ============================================================ 05 · il listino
doc.page(
    head(
        "B",
        "Il listino",
        "Dove stanno <span class='soft'>i crediti economici.</span>",
        "Sorpresa del listino: i piani per squadre sono i crediti più cari di tutti, perché il "
        "prezzo è per posto con un minimo di cinque.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Piano Higgsfield", "~Crediti/mese", "~Costo/mese", "~Per credito"],
        [
            ["*Team — cinque posti", "~5.000", "~€325", "~€0,0650"],
            ["*Scale — cinque posti", "~12.500", "~€750", "~€0,0600"],
            ["*Pacchetti extra", "~a consumo", "~—", "~€0,0463"],
            ["*Plus", "~1.200", "~€47", "~€0,0392"],
            ["*Ultra 3.000", "~3.000", "~€99", "~€0,0330"],
            ["*Ultra 6.000", "~6.000", "~€194", "~€0,0323"],
            ["*Ultra 9.000", "~9.000", "~€270", "~€0,0300"],
        ],
        hi=6,
        cap="Tariffe annuali, IVA esclusa. <strong>Starter non accede a Seedance</strong>: il piano "
        "minimo utile è Plus. Ultra 9.000 è il massimo acquistabile senza passare da un commerciale.",
    )
    + "</div><div class='unit'>"
    + tab(
        ["Piano ElevenLabs", "~Canone", "~Eccedenza chiamate", "~Totale/mese", "Crediti voce bastano?"],
        [
            ["*Creator", "~$22", "~$458", "~$480", "No — 121k contro 204k"],
            ["*Pro", "~$99", "~$381", "~$480", "Si' — 600k, concorrenza 20"],
            ["*Scale", "~$299", "~$181", "~$480", "Si', ma margine inutile"],
            ["*Business", "~$990", "~$0", "~$990", "Si', e costa il doppio per nulla"],
        ],
        hi=1,
        cap="<strong>Scoperta che vale $510 al mese:</strong> i piani per gli agenti vocali sono "
        "perfettamente lineari a $0,08 al minuto, quindi salire di livello non fa risparmiare un "
        "centesimo sulle chiamate — cambia solo i crediti voce e la concorrenza. Si prende il più "
        "basso che copra i crediti, ed è Pro.",
    )
    + "</div></div>"
)

# ============================================================ 06 · le correzioni
doc.page(
    head(
        "C",
        "Onestà",
        "Dove mi ero <span class='soft'>sbagliato.</span>",
        "Tre conclusioni mie, corrette per iscritto invece che riscritte di nascosto. Nascono "
        "tutte dallo stesso difetto: rispondere sul caso singolo invece che sul sistema.",
    )
    + """
<div class='body stack'>
  <div class='unit fix'>
    <div class='tag'>Correzione 1 · Fliki</div>
    <h3>Higgsfield sostituisce Fliki, e fa un altro mestiere.</h3>
    <p class='note'>Avevo scritto che il tetto di quindici secondi per clip rendeva impraticabile
    un video da dieci minuti. Il conto era giusto <strong>solo se il video è tutto video</strong>.
    Esiste un modulo dedicato, <strong>AI Long Video Generator</strong>, che dichiara alla lettera
    il nostro caso d’uso: «Build YouTube and long-form content — faceless channels — full episodes
    with consistent voice and look».</p>
  </div>
  <div class='unit fix'>
    <div class='tag'>Correzione 2 · Caroselli</div>
    <h3>I caroselli restano su Arena. Il prezzo era l’asse sbagliato.</h3>
    <p class='note'>Le slide che Max produce in Arena sono un sistema di design coerente — tag
    pre-headline in pillola, grana, arancione sotto il dieci per cento come accento, grotesque
    bold col corsivo serif, card argento, numerazione, firma. Nano Banana Pro a due crediti
    genera <strong>la fotografia di una slide</strong>, non un layout. Su Arena il problema non è
    la qualità: è l’affidabilità dell’automazione, e quella va riparata, non sostituita.</p>
  </div>
  <div class='unit fix'>
    <div class='tag'>Correzione 3 · Il conto</div>
    <h3>Il costo di un video non è una risposta.</h3>
    <p class='note'>«€2,78 a video» era vero e inutile: su una decisione di spesa ricorrente il
    costo unitario va moltiplicato per il volume che l’azienda produce davvero — e il volume si
    chiede, se non lo si sa. Nello stesso errore stavano i corti, costati come dodici clip
    generative quando sono <strong>progetti Vibe Motion</strong>: da 239 a 109 crediti l’uno, e
    lì se ne andava metà del conto.</p>
  </div>
</div>
"""
)

# ============================================================ 07 · le leve
doc.page(
    head(
        "D",
        "Architettura",
        "Le quattro leve, <span class='soft'>in ordine di peso.</span>",
        "Il conto non si vince comprando un piano più grande. Si vince qui.",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>01</span>Il tasso di riprova — vale metà del conto</div>
    <p class='note'>Se una clip su due va buttata, si paga il doppio. Passare da 2× a 1,3× porta
    Higgsfield da €1.496 a <strong>€987</strong> al mese: <strong>seimila euro all’anno</strong>.
    Non è una trattativa col fornitore — è la nostra libreria di prompt e le reference. È il
    lavoro che rende di più in assoluto.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>02</span>Immagini al posto delle clip — rapporto 66 a 1</div>
    <p class='note'>Un’immagine Soul 2.0 costa <strong>0,12 crediti</strong>; un secondo di clip
    Kling 3.0 in 1080p ne costa 1,6. <strong>Sessantasei volte tanto.</strong> Il video lungo
    faceless va costruito su immagini mosse in montaggio, con le clip riservate a hook, stacchi e
    momenti che devono muoversi davvero.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>03</span>Lo stampo — Canvas e Vibe Motion</div>
    <p class='note'>Vibe Motion produce un <strong>asset strutturato e modificabile</strong>, non
    un video piatto: si costruisce il modello una volta e si rigenera solo il testo, cento volte.
    Canvas salva l’intero flusso come template riutilizzabile. È qui che 102 corti al mese
    smettono di essere 102 produzioni e diventano cinque stampi.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>04</span>Lo sprint dei sette giorni unlimited</div>
    <p class='note'>Kling 3.0 unlimited a inizio mese produce il girato senza toccare un credito.
    Ma la coda è rilassata — <strong>una generazione alla volta</strong> — e i Termini vietano
    l’automazione. A mano, sei ore al giorno per sette giorni, copre forse un quarto del
    fabbisogno. È una leva reale, non è la soluzione.</p>
  </div>
</div>
"""
)

# ============================================================ 08 · le due macchine
doc.page(
    head(
        "E",
        "La fabbrica",
        "Le due macchine <span class='soft'>da sapere a memoria.</span>",
        "A 172 video al mese non conta saper generare: conta saper costruire lo stampo.",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Canvas · l’officina a nodi</div>
    <ul class='clean'>
      <li><strong>Come si costruisce:</strong> nuova lavagna, nodo Text Prompt, lo colleghi a un nodo di generazione, scegli il modello, colleghi l’uscita al passo dopo. Ogni modello Higgsfield è un nodo, audio compreso.</li>
      <li><strong>Il dettaglio che fa sbagliare tutti:</strong> i nodi <strong>Seedance</strong> leggono le reference collegate solo se il prompt ne dichiara il ruolo; i nodi <strong>Kling</strong> trattano l’immagine collegata come primo fotogramma, e per il personaggio vogliono il tag @nome-elemento.</li>
      <li><strong>Crediti:</strong> costruire e collegare è gratis. Si paga solo quando un nodo genera. Quindi si progetta l’intera pipeline a costo zero.</li>
      <li><strong>Parallelo:</strong> otto job insieme su Ultra, output confrontabili a fianco. È così che si abbatte il tasso di riprova — si sceglie fra quattro varianti invece di rigenerare quattro volte la stessa.</li>
    </ul>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Vibe Motion · il motore da testo ad animazione</div>
    <ul class='clean'>
      <li><strong>Non genera pixel:</strong> costruisce la logica dell’animazione, e l’uscita è un asset modificabile. Un template si riusa cento volte cambiando solo il testo.</li>
      <li><strong>Colore:</strong> si inseriscono i codici HEX o RGB esatti. Il nostro <strong>#fb4604</strong> entra alla lettera, non «più o meno arancione».</li>
      <li><strong>Safe zone social:</strong> gli elementi si trascinano dove servono e i sottotitoli non finiscono sotto i bottoni dell’interfaccia.</li>
      <li><strong>Movimento e tipografia:</strong> durata, ritardo e curve di easing su cursori; font nostri, crenatura e interlinea, ridimensionamento senza perdita. Categorie native: Infografiche, Presentazioni, Kinematic Captions.</li>
      <li><strong>Il costo è l’incognita:</strong> le iterazioni bruciano in fretta. Stima di terzi 15-50 crediti a progetto — nel calcolatore vale 40, ed è da tarare sul campo.</li>
    </ul>
  </div>
</div>
"""
)

# ============================================================ 09 · il muro legale
doc.page(
    head(
        "F",
        "Vincolo",
        "Il muro sulle <span class='soft'>chiamate a freddo.</span>",
        "Non è prudenza: è aritmetica. Un agente vocale che chiama a freddo numeri italiani "
        "senza consenso e senza dichiararsi mette a rischio l’azienda per un ritorno che non "
        "vale la cifra.",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Cosa è cambiato quest’anno</div>
    <ul class='clean'>
      <li><strong>Legge 49/2026, dal 19 giugno.</strong> Modifica l’articolo 51 del Codice del Consumo: opt-in obbligatorio, consenso preventivo esplicito e tracciabile. Nasce sul settore energia, le fonti divergono sulla trasversalità — va verificato con un legale prima di costruire, non dopo.</li>
      <li><strong>Registro Pubblico delle Opposizioni:</strong> copre anche le utenze aziendali, e vale sia per l’operatore umano sia per le chiamate automatiche.</li>
      <li><strong>Il 68% dei numeri «aziendali»</strong> nelle liste è intestato a persone fisiche: GDPR pieno, consenso esplicito.</li>
      <li><strong>AI Act articolo 50, dal 2 agosto.</strong> Obbligo di dichiarare dentro la conversazione, al primo contatto, che si parla con un’AI e per conto di chi. La privacy policy non basta.</li>
      <li><strong>Fino a €20 milioni o il 4% del fatturato</strong>, con responsabilità in solido fra mandante e contact center: non ci si copre appaltando.</li>
    </ul>
  </div>
  <div class='unit fix'>
    <div class='tag'>La strada che resta, ed è migliore</div>
    <p class='note'>In Preventa la catena di consenso <strong>esiste già</strong>: mandiamo
    WhatsApp, il concessionario risponde. Quello è un contatto che ha manifestato interesse, ed
    è lì che entra l’agente vocale — richiamo del lead caldo entro cinque minuti, qualifica in
    entrata, conferma appuntamenti, riattivazione dormienti, post-vendita. Con la dichiarazione AI
    nei primi tre secondi e l’opt-out immediato è in regola, e converte più del freddo.</p>
  </div>
  <div class='unit fix mute'>
    <div class='tag'>Il vincolo vero, che non è il prezzo</div>
    <p class='note'>Tremila chiamate al mese richiedono <strong>tremila contatti con consenso
    tracciabile</strong>. La domanda da rispondere prima di attivare l’agente non è quanto costa:
    è se generiamo cento risposte al giorno da richiamare.</p>
  </div>
</div>
"""
)

# ============================================================ 10 · il piano
doc.page(
    head(
        "G",
        "Esecuzione",
        "Il piano, <span class='soft'>nell’ordine che conta.</span>",
        "Le prime tre mosse non costano niente e cambiano di quanto la quarta va dimensionata.",
    )
    + """
<div class='body stack-tight'>
  <div class='unit step'>
    <div class='idx'>F01</div>
    <div>
      <h3>Le tre mosse a costo zero, oggi</h3>
      <ul class='clean'>
        <li><strong>Startup Grant ElevenLabs.</strong> 33 milioni di caratteri contro un consumo di 204.000 al mese: vale oltre dieci anni di voce dei corti. Mezz’ora di lavoro.</li>
        <li><strong>Trattativa Enterprise con Higgsfield.</strong> Unico livello con sconti a volume per modello e crediti che si riportano al mese dopo — e con una cadenza 3-2-3-2 la produzione non è piatta. Richiede settimane: va aperta ora.</li>
        <li><strong>Riparare quality_gate.py:93.</strong> Ventuno fallimenti identici in memoria; a tre video al giorno quel gate ferma settanta produzioni al mese.</li>
      </ul>
    </div>
  </div>
  <div class='unit step'>
    <div class='idx'>F02</div>
    <div>
      <h3>Il mese di prova</h3>
      <p class='note'>Ultra 3.000 mensile più ElevenLabs Creator. Nove prove col budget crediti
      dichiarato, la finestra unlimited usata per prima, il registro delle prove aperto dal primo
      giorno. <strong>La misura del costo del TTS viene prima di ogni altra prova:</strong> senza
      quel numero nessun conto di questo dossier è chiuso.</p>
    </div>
  </div>
  <div class='unit step'>
    <div class='idx'>F03</div>
    <div>
      <h3>La fabbrica — settimane due-sei</h3>
      <ul class='clean'>
        <li><strong>Cinque template Canvas</strong>, uno per formato: YouTube lungo, corto prodotto, corto Preventa, promo, UGC.</li>
        <li><strong>Cinque template Vibe Motion</strong> con le Brand Guidelines dentro: safe zone, font, HEX esatti.</li>
        <li>Skill <strong>video-youtube-higgsfield</strong> al posto del ramo Fliki, sottotitoli nostri.</li>
        <li>Soul ID del personaggio di brand e libreria di reference — è la leva che abbassa il tasso di riprova, cioè metà del conto.</li>
        <li><strong>Riparazione del ramo Arena</strong> per i caroselli, che restano lì.</li>
      </ul>
    </div>
  </div>
  <div class='unit step'>
    <div class='idx'>F04</div>
    <div>
      <h3>L’agente vocale — settimane quattro-otto</h3>
      <p class='note'>Parere legale prima di tutto. Poi l’agente «richiamo lead caldo» su Preventa,
      dichiarazione AI nei primi tre secondi, opt-out immediato, registro dei consensi a prova di
      ispezione. Test su venti lead, poi si decide se salire.</p>
    </div>
  </div>
</div>
"""
)

# ============================================================ 11 · chiusura
doc.page(
    head(
        "H",
        "Metodo e limiti",
        "Cosa è misurato <span class='soft'>e cosa no.</span>",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Come è stato fatto</div>
    <p class='note'>Sessantotto pagine di higgsfield.ai lette con Playwright sul DOM renderizzato.
    Le pagine prezzi sono applicazioni a pagina singola: il fetch semplice le vede vuote e
    restituisce listini di terze parti, che nei fatti erano <strong>tutti sbagliati</strong> —
    davano Plus a $39 e Ultra a $99 in dollari, quando il listino reale in euro è €47 e €99 con
    una scala fino a €270. Più la documentazione API, l’help center, i Termini d’uso, i listini
    ElevenLabs e la documentazione del Voice Changer.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Le due incognite, dichiarate</div>
    <ul class='clean'>
      <li><strong>Il costo in crediti del Text-to-Speech Higgsfield.</strong> Non pubblicato da nessuna parte. Decide se i 700 minuti di voce dei video lunghi restano lì o vanno su ElevenLabs — cioè se a regime basta Pro o serve Scale.</li>
      <li><strong>Il costo reale di un progetto Vibe Motion.</strong> Nel calcolatore vale 40 crediti ed è una stima di terzi. Con 102 corti al mese, sbagliarla di venti crediti sposta €1.100 all’anno.</li>
    </ul>
    <p class='note'>Entrambe si misurano nella prima settimana del mese di prova. Sono scritte qui
    perché <strong>un numero non misurato resta non misurato</strong> anche quando fa comodo.</p>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Dove vive questo dossier</div>
    <ul class='clean'>
      <li><strong>Originale:</strong> PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md</li>
      <li><strong>Calcolatore:</strong> PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py</li>
      <li><strong>Checkpoint:</strong> company/Memory/checkpoints/CP-20260905-001.md — codice di ripresa EMP-HGFD</li>
      <li><strong>Wiki:</strong> second-brain-vault/wiki/tools/Tool_Higgsfield_ElevenLabs.md</li>
    </ul>
  </div>
</div>
"""
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
    args = ap.parse_args()
    doc.build(html_only=args.html_only)
    return 0


if __name__ == "__main__":
    sys.exit(main())
