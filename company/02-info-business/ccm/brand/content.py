"""content.py — le pagine delle Brand Guidelines CCM.

Separato dal builder per una ragione pratica: qui vive solo il testo e la struttura,
in `build_brand_guidelines.py` vivono CSS, impaginazione e stampa. Si cambia il copy
senza toccare il motore.

`build(page, title_block)` riceve le due funzioni del builder e monta le pagine in ordine.
"""

from __future__ import annotations


def build(page, title_block) -> None:
    # ===================================================================== copertina
    page(
        '<div class="glow"></div>'
        '<div class="masthead"><span class="mk">DIGITAL EMPIRE</span>'
        "<span>Brand Guidelines · v1.0 · Settembre 2026</span></div>"
        '<h1><span class="silver-word" style="font-size:62px">Claude Code</span><br>'
        '<span class="silverorange-word" style="font-size:62px">Mastery</span></h1>'
        '<div class="sub">Il sistema visivo e verbale del lancio</div>'
        '<div class="meta">'
        '<div><div class="lb">Marca</div><div class="vl">Claude Code Mastery</div></div>'
        '<div><div class="lb">Casa</div><div class="vl">Digital Empire</div></div>'
        '<div><div class="lb">Stato</div><div class="vl">Vincolante dal lancio</div></div>'
        "</div>",
        kind="dark cover",
    )

    # ===================================================================== indice
    toc = [
        ("01", "Perché queste linee esistono", "03"),
        ("02", "La marca in una frase", "04"),
        ("03", "Il nome e la firma", "05"),
        ("04", "La voce", "06"),
        ("05", "Colore: il sistema", "07"),
        ("06", "La regola dell&rsquo;arancione", "08"),
        ("07", "L&rsquo;argento è la firma", "09"),
        ("08", "Tipografia", "10"),
        ("09", "I componenti", "11"),
        ("10", "Superfici e grana", "12"),
        ("11", "Le applicazioni del lancio", "13"),
        ("12", "Il confronto misurato", "14"),
        ("13", "Cosa non facciamo", "15"),
        ("14", "Checklist di conformità", "16"),
    ]
    rows = "".join(
        f'<div class="toc-row"><span class="n mono">{n}</span><span class="t">{t}</span>'
        f'<span class="d"></span><span class="p mono">{p}</span></div>'
        for n, t, p in toc
    )
    page(
        title_block(
            "",
            "Indice",
            'Quattordici capitoli. <span class="soft">Ogni regola è verificabile.</span>',
            "Non è un catalogo di gusti. Ogni capitolo chiude con qualcosa che si controlla a occhio o "
            "con un contagocce: o la regola è rispettata, o non lo è. Le regole che non si possono "
            "verificare non sono entrate in questo documento.",
        )
        + f'<div class="body">{rows}</div>',
        head="Indice",
        num=2,
    )

    # ===================================================================== 01 fondamento
    page(
        title_block(
            "01",
            "Perché queste linee esistono",
            'Il nostro arancione <span class="soft">non è più solo nostro.</span>',
            "Il 2 settembre 2026 abbiamo misurato il sito del concorrente diretto di CCM, "
            "claude-speedrun.com, leggendo i colori dal DOM renderizzato invece di stimarli da uno "
            "screenshot. Il risultato non è un&rsquo;impressione: è un&rsquo;identità sovrapposta.",
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="kicker"><span class="n">A</span>Quello che coincide, misurato</div>'
        + '<div class="datum"><span class="k">Colore d&rsquo;azione</span>'
        '<span class="v mono">#fb4604 &nbsp;—&nbsp; identico</span></div>'
        + '<div class="datum"><span class="k">Carattere</span>'
        '<span class="v mono">Onest &nbsp;—&nbsp; identico, 366 usi da loro</span></div>'
        + '<div class="datum"><span class="k">Raggio dei bottoni</span>'
        '<span class="v mono">12px &nbsp;—&nbsp; identico, 56 usi</span></div>'
        + '<div class="datum"><span class="k">Raggio delle pillole</span>'
        '<span class="v mono">9999px &nbsp;—&nbsp; identico, 65 usi</span></div>'
        + '<div class="datum"><span class="k">Fondo scuro</span>'
        '<span class="v mono">#131313 loro &nbsp;·&nbsp; #1c1c1c noi</span></div>'
        + "</div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>Quello che non coincide, ed è la via d&rsquo;uscita</div>'
        + '<p class="note">Nella loro tavolozza <strong>non esiste una famiglia argento</strong>: hanno un grigio '
        "piatto e nient&rsquo;altro. Noi abbiamo tre gradienti argento costruiti — sul bianco, sul nero e "
        "sull&rsquo;arancione — più le pillole argento flottanti e le card argento. È l&rsquo;unica parte del nostro "
        "sistema che loro non hanno, e non è un dettaglio: è metà del nostro linguaggio.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">C</span>La decisione che vincola tutto il resto</div>'
        + '<p class="note"><strong>L&rsquo;arancione è terreno conteso: smette di essere la nostra identità e resta '
        "il colore dell&rsquo;azione.</strong> L&rsquo;argento su fondo inchiostro diventa la firma. Chi vede una nostra "
        "thumbnail senza leggere il nome deve riconoscerci dall&rsquo;argento — perché sull&rsquo;arancione, a distanza, "
        "siamo indistinguibili da loro.</p></div>"
        + '<div class="unit" style="margin-top:auto"><div class="kicker">Come si verifica</div>'
        + '<p class="note">Copri il logo di un nostro pezzo e mostralo a qualcuno insieme a uno loro. Se non sa '
        "dire quale è nostro, il pezzo non rispetta questo capitolo.</p></div>"
        + "</div>",
        head="01 · Fondamento",
        num=3,
    )

    # ===================================================================== 02 posizionamento
    page(
        title_block(
            "02",
            "La marca in una frase",
            'Insegniamo a <span class="soft">costruire</span>, non a promptare.',
            "Ogni riga di copy, ogni thumbnail, ogni email del lancio deve poter essere ricondotta a questa "
            "frase. Se non ci si riconduce, non è CCM: è un altro corso sull&rsquo;AI.",
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="kicker"><span class="n">A</span>La promessa</div>'
        + '<p class="note">Da <strong>utente di chatbot</strong> a <strong>AI Builder professionista</strong>. '
        "Chi finisce CCM progetta architetture, istruisce agenti specializzati e orchestra workflow che "
        "risolvono problemi reali. Il metro non è quanto sa di AI: è cosa riesce a consegnare.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>Il nemico dichiarato</div>'
        + '<p class="note">Il prompt magico, e il corso che ti insegna «come scrivere prompt» lasciandoti '
        "esattamente dov&rsquo;eri. Noi vendiamo un metodo replicabile — i framework <strong>S.K.I.L.L.</strong> e "
        "<strong>W.O.R.K.</strong> — non una collezione di trucchi che invecchiano col prossimo modello.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">C</span>La prova che portiamo</div>'
        + '<ul class="clean">'
        "<li><strong>6 moduli, 21 lezioni, 6 settimane.</strong> Un percorso con una fine, non un abbonamento.</li>"
        "<li><strong>18 template</strong> pronti all&rsquo;uso e <strong>3 progetti portfolio</strong> reali: "
        "Content System, Data Analyzer, Business Automation.</li>"
        "<li><strong>Accesso a vita e aggiornamenti continui.</strong> Claude Code evolve, il corso con lui.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">D</span>A chi non parliamo</div>'
        + '<p class="note">A chi cerca la scorciatoia, a chi vuole «guadagnare con l&rsquo;AI» senza costruire '
        "niente, a chi non ha intenzione di aprire un terminale. Dirlo in pagina ci costa qualche iscritto e ci "
        "risparmia le richieste di rimborso.</p></div>"
        + "</div>",
        head="02 · Posizionamento",
        num=4,
    )

    # ===================================================================== 03 nome
    page(
        title_block(
            "03",
            "Il nome e la firma",
            'Si scrive <span class="soft">in un modo solo.</span>',
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="kicker"><span class="n">A</span>Le tre forme ammesse</div>'
        + '<div class="datum"><span class="k">Estesa</span><span class="v">Claude Code Mastery</span></div>'
        + '<div class="datum"><span class="k">Breve</span><span class="v">CCM</span></div>'
        + '<div class="datum"><span class="k">Con la casa</span>'
        '<span class="v">Claude Code Mastery · Digital Empire</span></div>'
        + '<p class="note" style="margin-top:5mm">La sigla <strong>CCM</strong> si usa solo dopo che il nome '
        "esteso è già comparso nello stesso pezzo. Mai come primo contatto: fuori dal nostro pubblico non "
        "significa niente.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>La pre-headline</div>'
        + '<p class="note">Sopra ai titoli grandi vive l&rsquo;occhiello in maiuscoletto spaziato. È la firma '
        "tipografica del lancio, e si scrive sempre così:</p>"
        + '<div style="margin-top:5mm;padding:7mm;background:#1c1c1c;border-radius:3px">'
        '<div class="pre-headline">Digital Empire presenta · Claude Code Mastery</div></div>'
        + '<div class="datum" style="margin-top:4mm"><span class="k">Valori esatti</span>'
        '<span class="v mono">9px · peso 600 · tracking 0.30em · #8a8594</span></div></div>'
        + '<div class="unit"><div class="kicker"><span class="n">C</span>Il separatore</div>'
        + '<p class="note">Il punto mediano <span class="mono">·</span> con uno spazio prima e dopo. Mai il '
        "trattino, mai la barra, mai «by» in un testo italiano. Il punto mediano è già nel marquee del sito e "
        "nei metadati: è la giunzione della casa.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">D</span>Cosa non si fa mai al nome</div>'
        + '<ul class="clean">'
        "<li>Non si traduce: mai «Padronanza di Claude Code».</li>"
        "<li>Non si accorcia in «Claude Mastery» o «Code Mastery»: il nome è dei tre pezzi.</li>"
        "<li>Non si scrive tutto maiuscolo se non dentro un occhiello o un&rsquo;etichetta.</li>"
        "<li>L&rsquo;accento arancione cade su <em>Mastery</em>, mai su <em>Claude</em>: il prodotto è nostro, "
        "il modello è di qualcun altro.</li>"
        "</ul></div>"
        + "</div>",
        head="03 · Nome",
        num=5,
    )

    # ===================================================================== 04 voce
    page(
        title_block(
            "04",
            "La voce",
            'Parliamo come chi <span class="soft">ha già costruito</span> la cosa.',
            "Il registro è quello di un professionista che mostra il proprio lavoro, non di un venditore che "
            "promette e non di un amico che ti prende in giro. Il tono da shitposting del nostro concorrente "
            "funziona per lui e ci farebbe perdere la metà seria del pubblico.",
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="kicker"><span class="n">A</span>Le quattro regole del registro</div>'
        + '<ul class="clean">'
        "<li><strong>Verbo concreto invece di aggettivo.</strong> «Costruisci un agente che qualifica i lead» "
        "batte «percorso rivoluzionario».</li>"
        "<li><strong>Un numero al posto di un superlativo.</strong> Se non abbiamo il numero, togliamo la frase: "
        "non la gonfiamo.</li>"
        "<li><strong>Il tu, mai il voi.</strong> Si parla a una persona che ha un problema, non a un pubblico.</li>"
        "<li><strong>Il freno subito dopo il claim forte.</strong> Quando diciamo una cosa grossa, la "
        "circoscriviamo nella riga dopo. È ciò che ci separa da chi promette.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>Due frasi a confronto</div>'
        + '<div class="yn">'
        '<div class="si"><div class="h">Così sì</div>'
        '<div class="q">«Domina Claude Code. Crea sistemi, non prompt.»</div>'
        '<div class="why">Due imperativi, un contrasto netto, zero aggettivi. Dice cosa cambia nel lettore, '
        "non quanto è bello il corso.</div></div>"
        '<div class="no"><div class="h">Così no</div>'
        '<div class="q">«Il corso definitivo e rivoluzionario per padroneggiare l&rsquo;intelligenza artificiale.»</div>'
        '<div class="why">Tre superlativi, nessun verbo che il lettore possa compiere, e una promessa che non '
        "possiamo dimostrare.</div></div>"
        "</div></div>"
        + '<div class="unit"><div class="kicker"><span class="n">C</span>Parole che non usiamo</div>'
        + '<p class="note"><span class="mono">rivoluzionario · definitivo · segreto · hack · guru · '
        "trucco · illimitato · garantito</span></p>"
        + '<p class="note" style="margin-top:3mm">Non per pudore: perché sono le parole di chi vende senza avere '
        "il prodotto, e il nostro pubblico le riconosce da lontano.</p></div>"
        + '<div class="unit" style="margin-top:auto"><div class="kicker">Come si verifica</div>'
        + '<p class="note">Cerca nel pezzo le parole della lista qui sopra: devono essere zero. Poi conta gli '
        "aggettivi nel primo paragrafo: se sono più dei verbi, il paragrafo va riscritto.</p></div>"
        + "</div>",
        head="04 · Voce",
        num=6,
    )

    # ===================================================================== 05 colore
    sw = [
        ("Ink", "#1c1c1c", "Il fondo di casa. Tutto il materiale di lancio nasce qui."),
        ("Ink profondo", "#0a0a0a", "Solo per stacchi e piedi di pagina. Mai come fondo principale."),
        ("Carta", "#fafafa", "Le sezioni che devono riposare l&rsquo;occhio e i documenti stampati."),
        ("Grigio", "#e8e8e6", "Il terzo fondo. Serve a non alternare solo nero e bianco."),
        ("Arancione", "#fb4604", "Solo azione: bottoni, link, il dato che deve essere letto."),
        ("Arancione chiaro", "#ff6a2e", "Solo dentro i gradienti e negli stati hover."),
        ("Arancione cupo", "#c9370a", "Solo la chiusura in basso dei gradienti."),
        ("Argento", "#d9d4e1", "La firma. Titoli, pillole flottanti, superfici di pregio."),
    ]
    cards = "".join(
        f'<div class="sw"><div class="chip" style="background:{hexv}"></div>'
        f'<div class="nm">{nm}</div><div class="hex mono">{hexv}</div>'
        f'<div class="use">{use}</div></div>'
        for nm, hexv, use in sw
    )
    page(
        title_block(
            "05",
            "Colore: il sistema",
            'Otto valori. <span class="soft">Nessun nono.</span>',
            "Sono letti dal foglio di stile del sito, non scelti a tavolino. Qualsiasi colore che non sia in "
            "questa pagina è un errore, non una variante.",
        )
        + f'<div class="body"><div class="swatches">{cards}</div>'
        + '<div class="unit" style="margin-top:12mm"><div class="kicker">Come si verifica</div>'
        + '<p class="note">Contagocce sul pezzo finito: ogni colore campionato deve corrispondere a uno di questi '
        "otto valori, oppure essere uno di questi otto con un&rsquo;opacità applicata. Le opacità ammesse sono quattro: "
        '<span class="mono">90% · 75% · 60% · 30%</span>. Nient&rsquo;altro.</p></div></div>',
        head="05 · Colore",
        num=7,
    )

    # ===================================================================== 06 regola arancione
    page(
        title_block(
            "06",
            "La regola dell&rsquo;arancione",
            'L&rsquo;arancione è <span class="soft">un verbo</span>, non un colore.',
            "Questa è la regola che ci separa dal concorrente che usa il nostro stesso #fb4604. Lui lo usa come "
            "identità e ne riempie fasce intere. Noi lo usiamo come segnale, e proprio per questo si vede di più.",
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="kicker"><span class="n">A</span>Dove l&rsquo;arancione è ammesso</div>'
        + '<ul class="clean">'
        "<li>Il bottone che porta all&rsquo;iscrizione, e i suoi stati.</li>"
        "<li>La parola dell&rsquo;occhiello sopra un titolo.</li>"
        "<li><strong>Una</strong> parola per titolo, quella su cui cade la promessa.</li>"
        "<li>Il numero di un dato che deve essere letto prima del testo intorno.</li>"
        "<li>Il punto vivo dentro una pillola argento.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>Dove non è mai ammesso</div>'
        + '<ul class="clean">'
        "<li>Come fondo di un paragrafo o di una card che contiene testo lungo.</li>"
        "<li>Su due parole diverse nello stesso titolo: se ce ne sono due, non ne conta nessuna.</li>"
        "<li>Sulla parola «Claude».</li>"
        "<li>Come fascia a piena larghezza: quella è la mossa del concorrente e a distanza ci confonde con lui.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">C</span>Il quoziente</div>'
        + '<p class="note">Su qualunque superficie — una schermata, una slide, una thumbnail, una pagina di questo '
        "documento — <strong>l&rsquo;arancione non supera il 10% dell&rsquo;area</strong>. Il resto è inchiostro, carta e "
        "argento. Il rapporto è la ragione per cui il 10% funziona.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">D</span>L&rsquo;unica eccezione, e va chiesta</div>'
        + '<p class="note">Il blocco evidenziato dietro una frase breve (<span class="mono">.hl-block</span>) è '
        "l&rsquo;unico caso in cui l&rsquo;arancione sta dietro al testo. Vale per una frase per pagina, mai per due, e "
        "mai per una frase più lunga di una riga.</p></div>"
        + '<div class="unit" style="margin-top:auto"><div class="kicker">Come si verifica</div>'
        + '<p class="note">Socchiudi gli occhi davanti al pezzo. Se la prima cosa che vedi è una massa arancione '
        "invece di una gerarchia, la regola è violata.</p></div>"
        + "</div>",
        head="06 · Colore",
        num=8,
    )

    # ===================================================================== 07 argento
    page(
        title_block(
            "07",
            "L&rsquo;argento è la firma",
            'Questo <span class="soft">loro non ce l&rsquo;hanno.</span>',
            "Tre gradienti costruiti, ciascuno con un compito. Sono l&rsquo;unica parte del sistema che il "
            "concorrente diretto non possiede, quindi sono la parte che va usata di più, non di meno.",
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="spec" style="background:#0a0a0a">'
        '<div class="label">Argento su scuro — titoli sul fondo inchiostro</div>'
        '<div class="silver-word">Crea sistemi</div>'
        '<div class="datum" style="margin-top:5mm"><span class="k">Gradiente</span>'
        '<span class="v mono">180° · #ffffff → #e8e3ef 35% → #b5afbd 72% → #8a8594</span></div>'
        "</div></div>"
        + '<div class="unit"><div class="spec" style="background:#0a0a0a">'
        '<div class="label">Argento-arancione — la parola della promessa, sempre in corsivo</div>'
        '<div class="silverorange-word">non prompt</div>'
        '<div class="datum" style="margin-top:5mm"><span class="k">Gradiente</span>'
        '<span class="v mono">135° · #ffffff → #d9d4e1 20% → #fb4604 55% → #ff8a4a 78% → #ffffff</span></div>'
        "</div></div>"
        + '<div class="unit"><div class="spec light" style="background:#fafafa">'
        '<div class="label">Argento-nero — titoli sulla carta</div>'
        '<div class="silverblack-word">Domina il metodo</div>'
        '<div class="datum" style="margin-top:5mm"><span class="k">Gradiente</span>'
        '<span class="v mono">180° · #3a3a3a → #1c1c1c 50% → #0a0a0a</span></div>'
        "</div></div>"
        + '<div class="unit"><div class="kicker">Le due regole dell&rsquo;argento</div>'
        + '<ul class="clean">'
        "<li><strong>Un gradiente per titolo.</strong> Argento e argento-arancione possono stare nello stesso "
        "titolo solo su righe diverse: mai nella stessa riga.</li>"
        "<li><strong>Solo sui titoli.</strong> Sotto i 24px il gradiente sparisce e resta testo slavato: "
        "il corpo del testo è pieno, mai sfumato.</li>"
        "</ul></div>"
        + "</div>",
        kind="dark",
        head="07 · Firma",
        num=9,
    )

    # ===================================================================== 08 tipografia
    scale = [
        ("Titolo di lancio", "62–72px", "700", "-0.038em", "Solo copertine e hero."),
        ("Titolo di sezione", "34–52px", "700", "-0.028em", "Uno per schermata."),
        ("Sottotitolo", "17–20px", "300", "normale", "Il peso leggero è voluto: fa respirare il titolo."),
        ("Corpo", "11–13px", "400", "normale", "Interlinea 1.68. Riga sotto i 65 caratteri."),
        ("Occhiello", "9px", "600", "0.30em", "Sempre maiuscolo."),
        ("Dato", "9–11px", "500", "normale", "IBM Plex Mono, cifre tabellari."),
    ]
    rows = "".join(
        f'<div class="datum"><span class="k">{nm}</span><span class="v">'
        f'<span class="mono">{sz}</span> &nbsp;·&nbsp; peso {w} &nbsp;·&nbsp; tracking {tr}'
        f'<div class="note" style="font-size:9px;margin-top:1mm">{note}</div></span></div>'
        for nm, sz, w, tr, note in scale
    )
    page(
        title_block(
            "08",
            "Tipografia",
            'Un carattere per parlare, <span class="soft">uno per misurare.</span>',
            "<strong>Onest</strong> porta tutto il discorso. <strong>IBM Plex Mono</strong> compare solo dove c&rsquo;è "
            "un dato: un prezzo, una durata, un valore. Il monospaziato dice «qui si misura» senza doverlo scrivere, "
            "ed è la seconda cosa che il concorrente non ha — lui usa un serif di sistema, generico.",
        )
        + f'<div class="body stack">{rows}'
        + '<div class="unit"><div class="kicker">Le tre regole della scala</div>'
        + '<ul class="clean">'
        "<li><strong>Il corsivo è riservato.</strong> Vive solo sulla parola in argento-arancione. Un corsivo "
        "altrove toglie forza a quello che conta.</li>"
        "<li><strong>Il grassetto non urla.</strong> Dentro un paragrafo si usa il peso 600, mai l&rsquo;800: "
        "l&rsquo;800 è dei titoli.</li>"
        "<li><strong>Mai il maiuscolo pieno su una frase.</strong> Solo su etichette e occhielli, "
        "e sempre con tracking almeno 0.16em.</li>"
        "</ul></div></div>",
        head="08 · Tipografia",
        num=10,
    )

    # ===================================================================== 09 componenti
    comps = [
        ('<span class="btn-orange">Inizia il percorso CCM</span>', "Bottone d&rsquo;azione",
         "Raggio 12px, alone arancione. Uno solo per schermata: se ce ne sono due, non c&rsquo;è gerarchia."),
        ('<span class="btn-ghost">Scopri il programma</span>', "Bottone secondario",
         "Bordo 2px al 18% di bianco. Accompagna il primo, non lo sostituisce mai."),
        ('<span class="bubble-orange">La skill più richiesta del 2026</span>', "Pillola arancione",
         "Occhiello sopra un titolo. Una per sezione."),
        ('<span class="bubble-silver">6 moduli · 21 lezioni</span>', "Pillola argento",
         "Per i dati neutri. Preferirla all&rsquo;arancione ovunque non ci sia un&rsquo;azione."),
        ('<span class="step-num">3</span>', "Numero di passo",
         "Solo dove esiste una sequenza vera. Mai come decorazione di una lista."),
        ('<span style="font-size:12px;color:#fff">Crea <span class="hl-block">sistemi veri</span></span>',
         "Frase evidenziata",
         "L&rsquo;unico arancione dietro al testo. Una frase per pagina, mai più lunga di una riga."),
    ]
    grid = "".join(
        f'<div class="comp"><div class="demo">{demo}</div>'
        f'<div class="nm">{nm}</div><div class="rule">{rule}</div></div>'
        for demo, nm, rule in comps
    )
    page(
        title_block(
            "09",
            "I componenti",
            'Sei mattoni. <span class="soft">Ognuno con una regola d&rsquo;uso.</span>',
        )
        + f'<div class="body"><div class="grid3" style="gap:8mm 7mm">{grid}</div>'
        + '<div class="unit" style="margin-top:11mm"><div class="kicker">Le pillole flottanti</div>'
        + '<div class="chipbox">'
        '<span class="silver-chip" style="top:2mm;left:0"><span class="dot"></span>6 Moduli</span>'
        '<span class="silver-chip" style="top:12mm;left:44mm"><span class="dot"></span>18 Template</span>'
        '<span class="silver-chip" style="top:3mm;right:6mm"><span class="dot"></span>3 Progetti Portfolio</span>'
        '<span class="silver-chip" style="bottom:1mm;left:22mm"><span class="dot"></span>Supporto AI-Pairing</span>'
        "</div>"
        + '<p class="note" style="color:rgba(244,242,246,0.6)">Vivono solo attorno all&rsquo;hero, mai dentro il '
        "corpo della pagina. Da tre a cinque, mai simmetriche, mai sovrapposte al testo. Il punto arancione è "
        "l&rsquo;unico arancione ammesso su di loro.</p></div></div>",
        kind="dark",
        head="09 · Componenti",
        num=11,
    )

    # ===================================================================== 10 superfici
    page(
        title_block(
            "10",
            "Superfici e grana",
            'Tre fondi che si alternano, <span class="soft">e una texture che non si spegne mai.</span>',
        )
        + '<div class="body stack">'
        + '<div class="unit"><div class="grid3">'
        '<div><div style="height:26mm;background:#1c1c1c;border-radius:3px"></div>'
        '<div class="nm" style="font-size:9.5px;font-weight:600;margin-top:3mm">Inchiostro</div>'
        '<div class="use" style="font-size:8.5px;color:#55535a;margin-top:2mm">La casa. Apertura, chiusura, '
        "tutto ciò che deve pesare.</div></div>"
        '<div><div style="height:26mm;background:#fafafa;border-radius:3px;box-shadow:inset 0 0 0 1px rgba(28,28,28,0.08)"></div>'
        '<div class="nm" style="font-size:9.5px;font-weight:600;margin-top:3mm">Carta</div>'
        '<div class="use" style="font-size:8.5px;color:#55535a;margin-top:2mm">Dove si spiega e si legge a lungo. '
        "Il riposo tra due sezioni scure.</div></div>"
        '<div><div style="height:26mm;background:#e8e8e6;border-radius:3px"></div>'
        '<div class="nm" style="font-size:9.5px;font-weight:600;margin-top:3mm">Grigio</div>'
        '<div class="use" style="font-size:8.5px;color:#55535a;margin-top:2mm">Il terzo tempo. Impedisce che '
        "l&rsquo;alternanza diventi un lampeggio.</div></div>"
        "</div></div>"
        + '<div class="unit"><div class="kicker"><span class="n">A</span>La regola dell&rsquo;alternanza</div>'
        + '<p class="note">Un cambio di fondo è un evento: annuncia che cambia il discorso. Se i fondi si '
        "alternano a ogni sezione, non annunciano più niente. <strong>Da due a tre inversioni in tutta una "
        "pagina lunga</strong>, non una ogni schermata.</p></div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>La grana</div>'
        + '<p class="note">Due strati sovrapposti, sempre attivi, su tutto: uno a <span class="mono">0.55</span> '
        'in <span class="mono">overlay</span>, uno a <span class="mono">0.28</span> in '
        '<span class="mono">hard-light</span>. È la cosa che rende le nostre superfici materiche invece che '
        "digitali, e nessun concorrente italiano sullo stesso argomento ce l&rsquo;ha.</p>"
        + '<p class="note" style="margin-top:3mm"><strong>In stampa non si usa il filtro SVG.</strong> Chromium lo '
        "rasterizza e il file supera i 16 MB: nei PDF la grana è un PNG ripetuto, come in questo documento. "
        "Sopra al testo piccolo si scende al 13% di opacità, altrimenti sporca la lettura.</p></div>"
        + '<div class="unit" style="margin-top:auto"><div class="kicker">Come si verifica</div>'
        + '<p class="note">Conta i cambi di fondo del pezzo. Più di tre in una pagina significa che nessuno di '
        "quei cambi sta dicendo qualcosa.</p></div>"
        + "</div>",
        head="10 · Superfici",
        num=12,
    )

    # ===================================================================== 11 applicazioni
    page(
        title_block(
            "11",
            "Le applicazioni del lancio",
            'Quattro superfici. <span class="soft">Stesse regole, misure diverse.</span>',
        )
        + '<div class="body stack-tight">'
        + '<div class="unit"><div class="kicker"><span class="n">A</span>Thumbnail YouTube — 1280×720</div>'
        + '<ul class="clean">'
        "<li>Fondo inchiostro. Da tre a cinque parole, in argento su scuro, mai più piccole di 90px.</li>"
        "<li>Arancione su <strong>una</strong> parola sola, o sul volto se c&rsquo;è.</li>"
        "<li>Niente frecce, niente cerchi rossi, niente facce stupite: sono il linguaggio di chi promette.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">B</span>Carosello Instagram — 1080×1350</div>'
        + '<ul class="clean">'
        "<li>Copertina inchiostro, slide interne su carta, ultima slide di nuovo inchiostro con l&rsquo;azione.</li>"
        "<li>Una sola idea per slide, e il numero di slide in monospaziato nell&rsquo;angolo.</li>"
        "<li>L&rsquo;occhiello con la pre-headline compare solo sulla copertina.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">C</span>Email del lancio</div>'
        + '<ul class="clean">'
        "<li>Testo, non immagini: un&rsquo;email che si vede solo a immagini attive è un&rsquo;email persa.</li>"
        "<li>Un bottone arancione, in fondo. I link nel corpo sono arancioni e sottolineati.</li>"
        "<li>L&rsquo;oggetto non contiene mai il nome del corso: contiene la cosa che il lettore vuole.</li>"
        "</ul></div>"
        + '<div class="unit"><div class="kicker"><span class="n">D</span>Slide di presentazione — 16:9</div>'
        + '<ul class="clean">'
        "<li>Un heading per slide. Se servono due titoli, servono due slide.</li>"
        "<li>Il dato in monospaziato e grande; la spiegazione piccola, sotto.</li>"
        "<li>Nessuna linea di separazione: lo stacco si fa con lo spazio, come in questo documento.</li>"
        "</ul></div>"
        + "</div>",
        head="11 · Applicazioni",
        num=13,
    )

    # ===================================================================== 12 confronto
    vs_rows = [
        ("Colore d&rsquo;azione", "#fb4604 — solo azione, max 10% dell&rsquo;area", "#fb4604 — identità, fasce piene", True),
        ("Carattere", "Onest + IBM Plex Mono sui dati", "Onest + serif di sistema", True),
        ("Famiglia argento", "Tre gradienti costruiti", "Assente", True),
        ("Registro", "Professionista che mostra il lavoro", "Shitposting, insulto affettuoso", False),
        ("Struttura del corso", "6 moduli, fine dichiarata", "Rilascio giornaliero, date esposte", False),
        ("Profondità tecnica", "Terminale, MCP, skill, agenti", "Una lezione sul terminale, una su MCP", True),
        ("Prova sociale", "Da costruire — oggi assente", "14 recensioni, numero dichiarato", False),
    ]
    body = (
        '<div class="vs">'
        '<div class="hd"></div><div class="hd us">Claude Code Mastery</div>'
        '<div class="hd them">claude-speedrun.com</div>'
    )
    for k, us, them, win in vs_rows:
        band = " band" if win else ""
        body += (
            f'<div class="k{band}">{k}</div>'
            f'<div class="c{band}">{us}</div>'
            f'<div class="c dim{band}">{them}</div>'
        )
    body += "</div>"
    page(
        title_block(
            "12",
            "Il confronto misurato",
            'Dove siamo uguali, <span class="soft">e dove possiamo vincere.</span>',
            "Righe in arancione: il terreno su cui possiamo distinguerci scegliendo. Righe neutre: il terreno su "
            "cui lui è avanti oggi, e va guardato senza raccontarsi storie.",
        )
        + f'<div class="body">{body}'
        + '<div class="unit" style="margin-top:12mm"><div class="kicker">La conclusione operativa</div>'
        + '<p class="note">Sul tono non lo inseguiamo: il suo registro gli funziona e a noi taglierebbe fuori il '
        "pubblico che paga. Sulla profondità tecnica lo battiamo già oggi — lui ha una lezione sul terminale, noi "
        "un corso intero. <strong>La riga che ci manca è l&rsquo;ultima: lui dichiara 14 recensioni vere, noi zero.</strong> "
        "Nessuna scelta grafica di questo documento vale quanto le prime dieci testimonianze reali del lancio.</p></div></div>",
        head="12 · Confronto",
        num=14,
    )

    # ===================================================================== 13 cosa non facciamo
    nos = [
        ("Il countdown e i posti limitati",
         "Se la scarsità non è vera, il pubblico che vogliamo la riconosce. Diciamo il contrario, "
         "esplicitamente: è un vantaggio che costa una riga."),
        ("La fascia arancione a piena larghezza",
         "È la mossa più riconoscibile del concorrente. Farla significa firmarsi col suo nome."),
        ("Le facce stupite e le frecce rosse",
         "Il linguaggio visivo di chi promette risultati. Noi mostriamo cosa si costruisce."),
        ("I numeri gonfiati",
         "Un numero dichiarato basso è più forte di uno alto non verificabile. «14 recensioni» batte «migliaia di studenti»."),
        ("Il gergo quando esiste la parola normale",
         "Si dice «agente che qualifica i lead», non «pipeline agentica di lead scoring»."),
        ("Il gradiente sotto il testo lungo",
         "I gradienti sono per i titoli. Sotto un paragrafo diventano rumore e uccidono la leggibilità."),
    ]
    items = "".join(
        f'<div class="unit" style="margin-bottom:7mm"><div class="kicker"><span class="n">✕</span>{t}</div>'
        f'<p class="note">{w}</p></div>'
        for t, w in nos
    )
    page(
        title_block(
            "13",
            "Cosa non facciamo",
            'Sei divieti. <span class="soft">Valgono più di sei permessi.</span>',
            "La restrizione è la prova di competenza più economica che esista: dice al lettore che abbiamo "
            "scelto, e che sappiamo perché.",
        )
        + f'<div class="body">{items}</div>',
        head="13 · Limiti",
        num=15,
    )

    # ===================================================================== 14 checklist
    checks = [
        ("Il pezzo si riconosce come nostro", "con il logo coperto, accanto a uno del concorrente."),
        ("L&rsquo;arancione sta sotto il 10%", "dell&rsquo;area totale della superficie."),
        ("Una sola parola arancione", "per titolo, e non è «Claude»."),
        ("Un solo heading", "per schermata, slide o pagina."),
        ("Ogni colore campionato", "è uno degli otto, puro o a una delle quattro opacità."),
        ("Il gradiente argento sta solo sui titoli", "sopra i 24px, mai nel corpo del testo."),
        ("Nessuna linea di separazione", "gli stacchi sono fatti di spazio."),
        ("Zero parole della lista nera", "rivoluzionario, definitivo, segreto, hack, guru, trucco, garantito."),
        ("Ogni numero in pagina è verificabile", "e se non lo è, è stato tolto invece che arrotondato."),
        ("La grana è attiva", "e scende al 13% dove il testo è piccolo."),
        ("Il nome è scritto per esteso", "almeno una volta prima di usare la sigla CCM."),
        ("C&rsquo;è una sola azione", "e si capisce al primo sguardo qual è."),
    ]
    items = "".join(
        f'<div class="check"><div class="box"></div><div class="t"><strong>{t}</strong> <span>{s}</span></div></div>'
        for t, s in checks
    )
    page(
        title_block(
            "14",
            "Checklist di conformità",
            'Dodici controlli. <span class="soft">Prima che il pezzo esca.</span>',
            "Nessuno di questi richiede una discussione sul gusto: si guardano e si rispondono. Un pezzo che non "
            "passa tutti e dodici non è pronto, anche se è bello.",
        )
        + f'<div class="body">{items}</div>',
        head="14 · Controllo",
        num=16,
    )

    # ===================================================================== colophon
    page(
        '<div class="glow"></div>'
        '<div class="masthead"><span class="mk">DIGITAL EMPIRE</span><span>Colophon</span></div>'
        '<div style="margin-top:auto">'
        '<h2 class="title" style="font-size:38px;color:#fff;max-width:24ch">'
        'Le regole valgono <span style="color:#8a8594">finché reggono alla misura.</span></h2>'
        '<p class="lead" style="color:rgba(244,242,246,0.6);max-width:60ch">Questo documento non nasce da un gusto: '
        "nasce dal foglio di stile del sito CCM e da una cattura forense del sito del concorrente diretto, letta dal "
        "DOM. Quando uno dei due cambia, cambia anche questo documento — e si rigenera con un comando.</p>"
        '<div class="meta" style="margin-top:14mm">'
        '<div><div class="lb">Fonte dei valori</div>'
        '<div class="vl mono" style="font-size:9px">ccm-premium/src/app/globals.css</div></div>'
        '<div><div class="lb">Fonte del confronto</div>'
        '<div class="vl mono" style="font-size:9px">site-study/capture/07-claude-speedrun</div></div>'
        "</div>"
        '<div class="meta" style="margin-top:8mm">'
        '<div><div class="lb">Si rigenera con</div>'
        '<div class="vl mono" style="font-size:9px">python build_brand_guidelines.py</div></div>'
        '<div><div class="lb">Versione</div><div class="vl">v1.0 · 3 settembre 2026</div></div>'
        "</div></div>",
        kind="dark cover",
    )
