# -*- coding: utf-8 -*-
"""Tavola Estetica v2 — agency-empire-landing SOLO AGGIUNTE, riscritta su funneloperator.it e su §14/§15.
Regole (Dossier 38 v2, C7.2): ogni still al pixel nativo o più piccolo, intero (contain, contenitore col rapporto del file),
in una composizione che lo ospita (colonna), JPEG q90, nessun filtro che sfoca, grana MAI sopra le immagini;
gli schemi in HTML sono costruiti in HTML qui dentro."""
import base64, io, pathlib, random, html
from PIL import Image

ROOT = pathlib.Path(r"C:/Users/Utente/Desktop/qui tutto/Digital Empire")
AURA = ROOT / "Caroselli Style/immagini AURA"
HERE = pathlib.Path(__file__).parent
OUT = HERE / "tavola38v2.html"

def b64(path, maxw=1200, q=90):
    im = Image.open(path).convert("RGB")
    if im.width > maxw: im.thumbnail((maxw, 10000))
    b = io.BytesIO(); im.save(b, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode(), im.size

rnd = random.Random(3); g = Image.new("L", (160, 160)); g.putdata([rnd.randint(0, 255) for _ in range(160 * 160)])
_b = io.BytesIO(); g.save(_b, "PNG", optimize=True); GRANA = "data:image/png;base64," + base64.b64encode(_b.getvalue()).decode()

def still(fid): return b64(AURA / [f for f in AURA.iterdir() if f.name.startswith(fid)][0])

# still (riferimento) — id → (src, (w,h))
ST = {k: still(k) for k in ("09f6a36a", "9152a07f", "4c5c8eef", "36c6e5f1", "fad322cf", "d4d30e7b", "bb4e3094", "0ca8865c", "e37fed19", "ade7b464", "c8095318")}
PF_SCHEDA = b64(HERE / "pf-scheda.jpg", 900); PF_TOTALE = b64(HERE / "pf-totale.jpg", 900)
SHOT_HOME = b64(HERE / "qa-shots/mobile-specchio.png", 780); SHOT_PRENOTA = b64(HERE / "qa-shots/mobile-prenota.png", 780)

def img(src_size, w, alt, cls=""):
    """immagine intera: larghezza di resa = min(w, nativa/2*?)... regola: mai sopra il pixel nativo. w = larghezza CSS."""
    src, (nw, nh) = src_size
    w = min(w, nw)  # mai più grande del nativo
    h = round(w * nh / nw)
    return f'<img class="intera {cls}" src="{src}" width="{w}" height="{h}" alt="{html.escape(alt)}" style="aspect-ratio:{nw}/{nh};width:{w}px;max-width:100%">'

def nota(dove, h, inp, fo, extra="", html_only=False):
    r14 = "schema in HTML, testo selezionabile" if html_only else "immagine intera al pixel"
    return f'''<div class="nota"><div><span class="k">dove</span><b>{html.escape(dove)}</b></div><div><span class="k">altezza max</span><b>{h}</b></div><div><span class="k">input</span><b>{html.escape(inp)}</b></div><div><span class="k">strategia</span><b>{html.escape(fo)}</b></div><div><span class="k">§14 · §15</span><b>{r14} · {extra or "ritmo rispettato"}</b></div></div>'''

T = []
def tav(n, titolo, sub, corpo, dove, h, inp, fo, extra="", atto=""):
    html_only = "<img" not in corpo
    T.append(f'''<section class="tav" id="{n.lower()}">
  <div class="th"><div class="num">{n}<small>{html.escape(atto)}</small></div><div><h2>{titolo}</h2><p class="sub">{sub}</p></div></div>
  <div class="frame">{corpo}</div>
  {nota(dove, h, inp, fo, extra, html_only)}
</section>''')

# ---------------- ATTO I ----------------
tav("A01", "La firma — <i>il primo volto, sotto l'hero.</i>", "Ritratto vero di Max, intero, in colonna 1/1 al pixel; riga in prima persona; micro-CTA «↓». Lo still è il riferimento di luce e taglio.",
 f'''<div class="ink two"><div class="col-img">{img(ST["09f6a36a"], 368, "riferimento: ritratto, luce di taglio, fondo scuro")}<span class="rif">riferimento · in pagina il ritratto vero</span></div>
 <div class="col-txt"><p class="eyebrow">Fondatore</p><h3>Ho costruito il primo sistema per me.<br><i class="serif">Poi ho smesso di venderlo come «tool».</i></h3><p class="body mute">Maximilian — tre sistemi, tre persone, nati a gennaio 2026. Quello che vedi qui sotto gira per noi ogni giorno.</p><a class="giu" href="#a07">↓ Guarda come funziona</a></div></div>''',
 "dopo <Hero /> (y ≈ 1.100 = 2% della pagina)", "480 px", "ritratto di Max", "FO-S01 · S03 · I03", "volto al 2%", "Atto I · volto e fatti")

tav("A02", "Il rail dei quattro fatti — <i>numeri veri, con fonte.</i>", "Costruito in HTML: 4 fatti da <code>FATTI.ts</code>, icona mono, 37/17 px, nastro CSS a 70 s, fermo con reduced-motion. Superficie carta.",
 '''<div class="carta"><div class="rail-track"><div class="rail">''' + "".join(f'<div class="fatto"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/></svg><b>{n}</b><span>{d}</span></div>' for n, d in (("7 giorni", "dal contratto al go-live"), ("300", "messaggi al giorno, zero a mano"), ("0 €", "di canone, per sempre"), ("90 giorni", "di supporto inclusi"), ("7 giorni", "dal contratto al go-live"), ("300", "messaggi al giorno, zero a mano"), ("0 €", "di canone, per sempre"), ("90 giorni", "di supporto inclusi"))) + '''</div></div></div>''',
 "dopo <Firma />", "273 px", "nessuno (FATTI.ts)", "FO-E01", "prova al 3%", "Atto I")

# ---------------- ATTO II ----------------
tav("A04", "Lo Specchio — <i>la foto che mancava, intera.</i>", "La sezione è già online: si aggiunge la colonna con l'immagine 1/1 al pixel (400×400 nativi → 368). Testo identico a oggi.",
 f'''<div class="carta two"><div class="col-txt"><h3 class="ink-t">Ti voglio bene, ma <i class="serif or">lo stai facendo a mano.</i></h3><p class="body ink-m">Non è colpa tua: nessuno ti ha mai mostrato il sistema. Ti hanno mostrato un tool, un abbonamento, un corso. <span class="mute2">(testo già online, identico)</span></p></div>
 <div class="col-img">{img(ST["9152a07f"], 368, "riferimento: uomo con la mano sul viso")}<p class="riga-sotto">Ogni mattina. Trenta DM. A mano. Da tre anni.</p></div></div>''',
 "dentro specchio.tsx (colonna nuova)", "+0 px", "still generato 1/1 (brief: incisione argento su nero)", "FO-I01 · I02", "", "Atto II · il problema, visto")

tav("A05", "Prima / dopo — <i>«200 € al mese, per sempre» vs «4.000 € una volta. Tuo.»</i>", "Due immagini nostre, intere: a sinistra una fattura mensile ricostruita in HTML e desaturata; a destra il PDF che un nostro sistema genera davvero (banda sul dato del cliente). Titolo barrato / pieno.",
 f'''<div class="ink two-eq"><div class="pd"><h4 class="barrato">200 € al mese, per sempre</h4><div class="fattura"><div class="f-top"><span>ABBONAMENTO OUTREACH · PIANO PRO</span><span>Fattura n. 2026-0912</span></div><div class="f-row"><span>Canone mensile</span><b>200,00 €</b></div><div class="f-row"><span>Rinnovo automatico</span><b>12/10/2026</b></div><div class="f-row"><span>Proprietà del codice</span><b>—</b></div><div class="f-row tot"><span>Totale a 12 mesi</span><b>2.400,00 €</b></div><span class="rif">ricostruita in HTML, desaturata — non uno screenshot altrui</span></div></div>
 <div class="pd"><h4 class="pieno">4.000 € una volta. <span class="or">Tuo.</span></h4>{img(PF_TOTALE, 380, "PDF generato da PreventivoForge: totale in strada, dato del cliente coperto", "bordo-or")}<span class="rif">PDF vero del nostro sistema · dato del cliente coperto con banda</span></div></div>''',
 "dopo <Competitors />", "700 px", "nessuno (2 immagini nostre)", "FO-I06", "prima prova visiva al 16%", "Atto II")

# ---------------- ATTO III ----------------
STEP = [("01", "Chiamata", "30 minuti: vedi il sistema che gira"), ("02", "Proposta", "prezzo esatto, scritto"), ("03", "Contratto", "cosa fa il sistema, entro quando"), ("04", "Setup", "7 giorni sul tuo server"), ("05", "Go-live", "i primi messaggi veri davanti a te"), ("06", "30 giorni di guardia", "dashboard aperta, alert, correzioni"), ("07", "Gira da solo", "codice tuo. Per sempre.")]
scala = "".join(f'<li class="step {"fine" if i == 6 else ""}" style="--i:{i}"><span class="n">{n}</span><b>{t}</b><span class="d">{d}</span></li>' for i, (n, t, d) in enumerate(STEP))
tav("A07", "La scala a 7 gradini — <i>dalla chiamata al sistema che gira.</i>", "Costruita in HTML: card sfalsate, connettori tratteggiati a gomito, il traguardo è l'unico verde della pagina. Testo selezionabile: meglio del raster di funneloperator.",
 f'<div class="carta"><ol class="scala">{scala}</ol></div>',
 "dopo <FlowFramework />", "900 px", "nessuno", "FO-E02", "", "Atto III · il meccanismo")

CONS = [("Codice", "repository tuo, documentato, in chiaro"), ("Dashboard", "invii, risposte, lead — aperta 24/7"), ("Documentazione", "come gira, come si spegne, come si estende"), ("Formazione", "una sessione al tuo team, registrata")]
cart = "".join(f'<button class="linguetta {"attiva" if i == 0 else ""}">{t}</button>' for i, (t, _) in enumerate(CONS))
tav("A08", "La cartella delle consegne — <i>quattro linguette, quattro cose che ricevi.</i>", "Costruita in CSS: linguette in <code>clip-path</code> parametrico (container query), sono <code>button</code>. Ogni linguetta apre la lista.",
 f'<div class="ink"><div class="cartella"><div class="linguette">{cart}</div><div class="foglio"><p class="eyebrow">01 · Codice</p><h3 class="w">{CONS[0][1]}</h3><ul class="checks"><li>repository privato a tuo nome</li><li>README in italiano: avvio, stop, aggiornamento</li><li>nessuna dipendenza da un nostro account</li><li>licenza: tua, per sempre</li></ul></div></div></div>',
 "dopo <SystemsShowcase />", "700 px", "nessuno", "FO-E07", "", "Atto III")

tav("A09", "Guardalo girare — <i>il video vero del sistema, poi una cucitura in colonna.</i>", "Poster + play + durata dichiarata; l'iframe nasce solo al click. Sotto, l'immagine intera in colonna (mai in fascia): a fianco, la riga.",
 f'''<div class="ink"><div class="player"><div class="poster"><span class="play">▶</span><span class="dur">OUTREACH FACTORY · 1:30 · invii di oggi, risposte in coda, lead nel CRM</span></div></div>
 <div class="two cuc"><div class="col-img">{img(ST["4c5c8eef"], 300, "riferimento: figura in armatura seduta a colazione")}<span class="rif">riferimento · in pagina uno still generato 4/7, 2×</span></div><div class="col-txt"><p class="riga-grande">Ha già mandato <b>300</b> messaggi.<br>Tu stai facendo colazione.</p><p class="body mute">Il numero è <code>FATTI.messaggiGiorno</code>. La riga sta accanto all'immagine, non sopra: l'immagine si vede tutta.</p></div></div></div>''',
 "dopo <OutreachInside />", "620 px", "video (Max o mio oscurato) · still", "FO-E09 · T03 · I01", "", "Atto III")

tav("A10+A20", "Due tipi di aziende — <i>e le domande che non ci fate.</i>", "Card gemelle con il numero a 81 px e il bordo arancione solo sulla card giusta; sotto, tre domande ostili con risposta in una frase. Carta.",
 '''<div class="carta"><div class="gemelle"><div class="gem"><span class="big">1.</span><b>Chi affitta un tool</b><p>Paga ogni mese un abbonamento che non sa chi è. Se smette, sparisce tutto. Resta in affitto.</p></div><div class="gem giusta"><span class="big or">2.</span><b>Chi possiede il sistema</b><p>Lo paga una volta. Gira sui suoi account, sul suo server. Se ci licenzia, resta lì e continua a girare.</p></div></div>
 <div class="domande"><div><b>«Se funziona così bene, perché non lo tenete per voi?»</b><p>Lo teniamo: è l'Outreach Factory con cui probabilmente ti abbiamo trovato. Ne costruiamo altri perché il mestiere è quello.</p></div><div><b>«Perché la chiamata è gratis?»</b><p>Perché in trenta minuti capiamo entrambi se il sistema ti serve. Se no, hai perso un caffè.</p></div><div><b>«Cosa ci guadagnate?»</b><p>Il prezzo scritto nel contratto, una volta. Niente canoni: non abbiamo interesse a tenerti in ostaggio.</p></div></div></div>''',
 "dopo <ContentOutput />", "800 px", "nessuno (copy da COPY.md, gate_voce)", "FO-E04 · S08", "", "Atto III → IV")

# ---------------- ATTO IV ----------------
tav("A11", "Prove vere — <i>il PDF che il sistema genera, intero.</i>", "La sezione è online: si aggiungono le immagini vere (pagina reale di PreventivoForge, 1191×1685 nativi, resa 400, dato del cliente coperto con banda, mai sfocato).",
 f'''<div class="carta two"><div class="col-img">{img(PF_SCHEDA, 400, "PDF PreventivoForge: scheda tecnica generata dal sistema, dato del cliente coperto", "bordo")}</div><div class="col-txt"><p class="eyebrow ink-m">Un concessionario, luglio 2026 — preventivi</p><p class="body ink-t">65 preventivi generati su annunci veri in dieci giorni, 11 marche, circa 2 minuti dal link al PDF, 6 controlli automatici prima di ogni PDF. <span class="mute2">(testo già online)</span></p><p class="didascalia">↑ Pagina 2 di un PDF vero: scheda tecnica compilata dal sistema. La banda copre il dato del cliente finché non c'è il consenso al nome.</p></div></div>''',
 "dentro prove-vere.tsx", "+0 px", "nessuno (PDF nostro)", "FO-I07 · I01", "", "Atto IV · la prova")

rail_items = [("PreventivoForge", "PDF · scheda", PF_SCHEDA, 190), ("PreventivoForge", "PDF · totale", PF_TOTALE, 190), ("Sito agency", "specchio · mobile", SHOT_HOME, 190), ("/prenota/", "porta · mobile", SHOT_PRENOTA, 190)]
rail_html = "".join(f'<figure class="sys"><div class="shot">{img(s, w, t + " — " + d)}</div><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>' for t, d, s, w in rail_items)
rail_html += '<figure class="sys testo"><div class="shot txt"><b>Outreach Factory</b><span>dashboard · invii di oggi</span><em>screenshot reale in F3 (--oscura)</em></div><figcaption><b>Outreach Factory</b><span>dashboard</span></figcaption></figure>'
tav("A12", "Il rail dei sistemi in produzione — <i>≥ 5 immagini distinte, oscurate con banda.</i>", "Screenshot verticali interi, due nastri controcorrente. Il gate parte solo con 5 distinti (il suo ne ripete 3). Qui 4 reali + 1 da produrre in F3, dichiarato.",
 f'<div class="ink"><div class="rail-track lento"><div class="rail sys-rail">{rail_html}{rail_html}</div></div></div>',
 "dopo <ProveVere />", "520 px", "nessuno (screenshot nostri, --oscura)", "FO-E10 · gate ≥ 5", "", "Atto IV")

# ---------------- ATTO V ----------------
volti = "".join(f'<figure class="volto">{img(ST[k], 300, "riferimento di posa: ritratto")}<figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for k, n, r in (("36c6e5f1", "Maximilian", "fondatore · sistemi"), ("fad322cf", "Gael", "operazioni · outreach"), ("d4d30e7b", "Leonardo", "contenuti · Second Brain")))
tav("A14", "La stanza — <i>tre volti, interi, ognuno col suo rapporto.</i>", "Tre ritratti veri (1/1, 1/1, 4/5): ogni immagine tiene il proprio rapporto, nessuna viene forzata in una griglia uguale. Gli still sono riferimenti di posa.",
 f'<div class="ink"><p class="eyebrow">Chi c\'è dietro</p><h3 class="w" style="margin:6px 0 18px">Tre persone. <i class="serif">Nessun account manager in mezzo.</i></h3><div class="volti">{volti}</div><span class="rif">riferimenti · in pagina i ritratti veri</span></div>',
 "dopo <WhoGuides />", "640 px", "3 ritratti (Max, Gael, Leonardo)", "FO-I03", "", "Atto V · chi siamo")

dietro = "".join(f'<figure class="lav">{img(ST[k], 220, "riferimento di posa: foto di lavoro")}<figcaption>{d}</figcaption></figure>' for k, d in (("0ca8865c", "Max, la sera del primo go-live"), ("e37fed19", "la chiamata delle 18 con il cliente"), ("ade7b464", "Gael, il turno dei follow-up"), ("c8095318", "Leonardo, la riunione del lunedì")))
tav("A15", "Dietro le quinte — <i>quattro foto di lavoro, anche brutte.</i>", "Colonna stretta (670), foto a coppie, ognuna al proprio rapporto, una riga sotto. Mai stock. Gli still sono riferimenti di posa: in pagina le foto vere del team.",
 f'<div class="carta"><div class="dietro">{dietro}</div><span class="rif ink-m">riferimenti · foto vere di Max, Gael, Leonardo</span></div>',
 "dopo <BuilderNotTrainer />", "600 px", "4 foto di lavoro (Max)", "FO-S05", "", "Atto V")

tav("A16", "La mappa — <i>«Tu sei qui».</i>", "Albero in HTML: tre pillole, connettori con raccordo, puntatore arancione animato sul ramo Agency. Testo selezionabile, link veri al Manuale e alle app.",
 '''<div class="ink"><div class="albero"><div class="pill radice">✦ Digital Empire</div><div class="conn"></div><div class="rami"><div class="ramo"><div class="pill qui">Agency <span class="tag-qui">◉ Tu sei qui</span></div></div><div class="ramo"><div class="pill">Formazione</div></div><div class="ramo"><div class="pill">SaaS</div></div></div></div></div>''',
 "dopo <Dietro />", "600 px", "nessuno", "FO-E03", "", "Atto V")

# ---------------- ATTO VI ----------------
tav("A17", "La tessera del cliente — <i>quattro spunte e un QR.</i>", "Card verticale in HTML (il laccio è un PNG), le promesse in lista ✓, i prezzi da <code>listino.ts</code>, il QR porta a /prenota/. Carta.",
 '''<div class="carta two"><div class="col-txt"><p class="eyebrow ink-m">Cosa c'è scritto sulla tua tessera</p><h3 class="ink-t">Un sistema, <i class="serif or">una volta.</i></h3><p class="body ink-m">Outreach Factory 4.000 € · Content Factory 3.500 € · Second Brain 2.500 €. Metà alla firma, metà al go-live.</p></div>
 <div class="col-img"><div class="laccio"></div><div class="tessera"><div class="t-top"><span>DIGITAL EMPIRE · SISTEMA</span><span>№ 0001</span></div><h4>Sistema Empire</h4><ul class="checks dark"><li>Codice consegnato, tuo</li><li>90 giorni di supporto</li><li>Garanzia 30 giorni</li><li>Zero canoni, mai</li></ul><div class="qr" aria-label="QR verso /prenota/"></div><span class="t-foot">agency-empire-landing.vercel.app/prenota/</span></div></div></div>''',
 "dopo <PricingROI />", "600 px", "nessuno", "FO-E06", "prima porta nuova al ≈ 70%", "Atto VI · offerta e chiusura")

tav("A18", "Quanto costa non farlo — <i>la formula, visibile.</i>", "Ore al mese a mano × costo orario contro il setup una volta: «si ripaga in N mesi». Numeri da FATTI e LISTINO (<code>MESI_PAREGGIO</code>), mai scritti a mano.",
 '''<div class="ink"><div class="formula"><div class="f-col"><span class="k">Oggi</span><b>30 DM × 5 min</b><span>= 2,5 ore al giorno</span><span>≈ 55 ore al mese tue</span></div><div class="f-op">vs</div><div class="f-col or-b"><span class="k">Con il sistema</span><b>4.000 € una volta</b><span>300 messaggi al giorno</span><span>0 ore tue · 0 € al mese</span></div></div><p class="riga-grande center">Un SaaS da 200 €/mese costa 2.400 € l'anno, per sempre.<br>Il sistema <b class="or">ha pareggiato al ventesimo mese</b> — e da lì gira a costo zero.</p></div>''',
 "dopo <Clarity />", "500 px", "nessuno", "FO-S09", "", "Atto VI")

tav("A19", "Cosa succede se non funziona — <i>la garanzia come contratto, firmata col volto.</i>", "Due quadri incrociati («se il sistema non fa X entro Y → noi facciamo Z») e il ritratto di Max, intero, in colonna. Lo still (elmo) è il riferimento dell'oggetto: acciaio.",
 f'''<div class="carta two"><div class="col-txt"><p class="eyebrow ink-m">Garanzia · una frase, una condizione</p><h3 class="ink-t">Funziona come scritto nel contratto, <i class="serif or">o lo sistemiamo noi.</i></h3><div class="quadri"><div><b>Se</b><p>un risultato scritto nel contratto — messaggi mandati, contenuti pubblicati, lead nel CRM — non arriva entro 30 giorni dal go-live</p></div><div><b>Allora</b><p>il lavoro per farlo arrivare è nostro e non costa niente. Se non è risolvibile: rimborso integrale.</p></div></div></div>
 <div class="col-img">{img(ST["bb4e3094"], 280, "riferimento: elmo, luce laterale")}<span class="rif ink-m">riferimento · in pagina il ritratto di Max</span></div></div>''',
 "dopo <MyPromise />", "600 px", "ritratto di Max", "FO-S07", "", "Atto VI")

faq = [("Sistema", ["Chi possiede il codice? — Tu, dal primo giorno: repository a tuo nome.", "Su quale server gira? — Sul tuo (VPS 5-20 €/mese) o su uno che apriamo a tuo nome.", "Cosa succede se lo spegnete? — Non possiamo: non abbiamo accessi che tu non ci dia.", "Quanto dura il setup? — 7 giorni lavorativi dal contratto."]), ("Contratto e pagamento", ["Come si paga? — 50% alla firma, 50% al go-live, con fattura.", "Ci sono canoni? — No. Paghi il tuo VPS e le API a consumo.", "Se cambiamo idea a metà? — Tieni il lavoro fatto fino a lì, pagato quello.", "Rate? — Sì, su richiesta, in contratto."])]
faq_html = "".join(f'<div class="gruppo"><p class="eyebrow ink-m">{g}</p>' + "".join(f'<details {"open" if i == 0 else ""}><summary>{q.split(" — ")[0]}</summary><p>{q.split(" — ")[1]}</p></details>' for i, q in enumerate(qs)) + '</div>' for g, qs in faq)
tav("A21", "FAQ contratto e pagamento — <i>due gruppi, la prima aperta, JSON-LD dagli stessi dati.</i>", "Accordion unico, prima risposta aperta di default (il suo difetto corretto). Gli stessi array alimentano lo schema FAQPage.",
 f'<div class="carta"><div class="faq">{faq_html}</div></div>',
 "dopo <FAQ />", "700 px", "nessuno (copy da COPY.md)", "FO-E08 · T09", "", "Atto VI")

tav("A22", "La coda legale — <i>null finché i dati non ci sono.</i>", "Ragione sociale, P.IVA, sede, PEC, privacy, cookie, «Preferenze cookie». Il footer esistente resta: questa aggiunge ciò che manca.",
 '''<div class="ink"><div class="legale"><span>Digital Empire di ______ · P.IVA ______ · Sede ______ · PEC ______</span><span><a>Privacy</a> · <a>Cookie</a> · <a>Preferenze cookie</a></span></div><span class="rif">rende null finché legal.ts è vuoto — mai un dato inventato</span></div>''',
 "prima del <footer>", "160 px", "dati legali (Max)", "—", "", "Atto VI")

MAPPA = [("Header · Sticky (com'erano)", 0), ("Hero", 0), ("A01 La firma", 1), ("A02 Rail dei fatti", 1), ("VSL", 0), ("ScienceStats", 0), ("Audience", 0), ("Problems", 0), ("Specchio (+A04 foto)", 1), ("Competitors", 0), ("A05 Prima/dopo", 1), ("ListenUp", 0), ("divider", 0), ("Hierarchy", 0), ("Pillars", 0), ("FlowFramework", 0), ("A07 Scala a 7 gradini", 1), ("divider", 0), ("SystemsShowcase", 0), ("A08 Cartella delle consegne", 1), ("OutreachDeep", 0), ("OutreachInside", 0), ("A09 Guardalo girare", 1), ("ContentDeep", 0), ("ContentOutput", 0), ("A10+A20 Due tipi + domande", 1), ("BrainDeep", 0), ("SecondBrainInside", 0), ("Results", 0), ("ProveVere (+A11 PDF)", 1), ("A12 Rail dei sistemi", 1), ("NoFluff", 0), ("ToolStack", 0), ("divider", 0), ("PowerDeck", 0), ("divider", 0), ("WhoGuides", 0), ("A14 La stanza", 1), ("BuilderNotTrainer", 0), ("A15 Dietro le quinte", 1), ("A16 Mappa «Tu sei qui»", 1), ("Bonuses", 0), ("PricingROI", 0), ("A17 Tessera del cliente", 1), ("Clarity", 0), ("A18 Quanto costa non farlo", 1), ("MyPromise", 0), ("A19 Se non funziona", 1), ("Objections", 0), ("FAQ", 0), ("A21 FAQ contratto", 1), ("divider", 0), ("CosaOttieni", 0), ("FinalCTA", 0), ("FinalOffer", 0), ("AboutStory", 0), ("A22 Coda legale", 1), ("footer (com'era)", 0)]
mappa = "".join(f'<li class="{"add" if a else ""}">{html.escape(n)}</li>' for n, a in MAPPA)

HTML = f'''<title>Tavola Estetica v2 · Solo Aggiunte</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root{{--ink:#0a0a0a;--ink1:#1c1c1c;--ink2:#202021;--carta:#faf6ee;--carta2:#f3ede0;--or:#fb4604;--silver:#d9d4e1;--dim:#8f8a99;--hair:rgba(217,212,225,.16);--hairl:rgba(28,28,28,.14);--verde:#2d7a4f;
--sans:"Onest",system-ui,-apple-system,"Segoe UI",sans-serif;--serif:"Instrument Serif",Georgia,serif;--mono:"JetBrains Mono",Consolas,monospace}}
*{{box-sizing:border-box}} html{{background:var(--ink)}}
body{{margin:0;background:var(--ink);color:var(--silver);font-family:var(--sans);font-size:15.5px;line-height:1.55;-webkit-font-smoothing:antialiased}}
/* grana SOLO sul fondo della pagina (z sotto le tavole): mai sopra le immagini — §14 */
.grana{{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.12;mix-blend-mode:overlay;background:url({GRANA});background-size:160px}}
.wrap{{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:0 22px 90px}}
.eyebrow{{font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--dim)}} .eyebrow b{{color:var(--or);font-weight:500}}
h1,h2,h3,h4{{margin:0;font-weight:800;letter-spacing:-.02em;line-height:1.08;color:#fff;text-wrap:balance}}
h1 i,h2 i{{font-family:var(--serif);font-style:italic;font-weight:400;letter-spacing:0}} .serif{{font-family:var(--serif);font-style:italic;font-weight:400}} .or{{color:var(--or)}}
header.top{{padding:60px 0 36px;border-bottom:1px solid var(--hair)}}
header.top h1{{font-size:clamp(34px,5vw,62px);margin-top:14px;max-width:19ch}} header.top h1 i{{color:var(--or)}}
.tesi{{max-width:68ch;margin-top:20px;font-size:17px}}
.regole{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px}} @media(max-width:800px){{.regole{{grid-template-columns:1fr 1fr}}}}
.regole div{{border-top:1px solid var(--hair);padding-top:12px}} .regole b{{display:block;color:#fff;font-size:22px;letter-spacing:-.02em}} .regole span{{font-family:var(--mono);font-size:11px;color:var(--dim);line-height:1.5}}
.tav{{padding:56px 0 22px;border-bottom:1px solid var(--hair)}}
.th{{display:grid;grid-template-columns:130px 1fr;gap:20px;align-items:end;margin-bottom:18px}} @media(max-width:640px){{.th{{grid-template-columns:1fr}}}}
.num{{font-family:var(--mono);font-size:13px;color:var(--or);letter-spacing:.2em}} .num small{{display:block;color:var(--dim);letter-spacing:.1em;margin-top:4px;font-size:10.5px;text-transform:uppercase}}
.tav h2{{font-size:clamp(22px,2.6vw,32px)}} .sub{{margin:8px 0 0;color:var(--dim);max-width:78ch;font-size:14.5px}} .sub code{{color:#fff}}
.frame{{border:1px solid var(--hair);border-radius:6px;overflow:hidden;box-shadow:0 30px 80px -40px #000}}
.ink{{background:var(--ink1);padding:40px 44px}} .carta{{background:var(--carta);color:var(--ink1);padding:40px 44px}}
.ink-t{{color:var(--ink1)}} .ink-m{{color:#5e5a63}} .mute{{color:var(--dim)}} .mute2{{color:#9b958a;font-size:13px}} .w{{color:#fff}}
.two{{display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center}} .two-eq{{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start}}
@media(max-width:760px){{.two,.two-eq{{grid-template-columns:1fr}}}}
.col-img{{display:flex;flex-direction:column;gap:10px;align-items:flex-start}} .col-txt h3{{font-size:clamp(24px,2.8vw,36px)}} .col-txt .body{{margin:14px 0 0;max-width:46ch}}
img.intera{{display:block;height:auto;border-radius:6px;object-fit:contain;background:#000}} img.bordo{{border:1px solid var(--hairl)}} img.bordo-or{{border:1px solid var(--or)}}
.rif{{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--or)}}
.giu{{display:inline-block;margin-top:18px;font-family:var(--mono);font-size:12.5px;color:#fff;text-decoration:none;border-bottom:1px solid var(--or);padding-bottom:2px}}
.riga-sotto{{margin:0;font-weight:600;color:var(--ink1);font-size:17px;max-width:368px}}
.riga-grande{{font-size:clamp(20px,2.2vw,28px);line-height:1.3;color:#fff;font-weight:500;margin:0}} .riga-grande.center{{text-align:center;margin-top:22px;font-size:20px;color:var(--silver)}}
.didascalia{{font-size:13px;color:#5e5a63;margin-top:14px;max-width:44ch}}
/* rail */
.rail-track{{overflow:hidden;mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}}
.rail{{display:flex;gap:56px;width:max-content;animation:rail 40s linear infinite}} .rail-track:hover .rail{{animation-play-state:paused}} .lento .rail{{animation-duration:70s}}
@keyframes rail{{to{{transform:translateX(-50%)}}}} @media (prefers-reduced-motion:reduce){{.rail{{animation:none}}}}
.fatto{{display:flex;align-items:baseline;gap:12px;color:var(--ink1)}} .fatto svg{{align-self:center;color:var(--or)}} .fatto b{{font-size:37px;letter-spacing:-.03em;font-weight:800}} .fatto span{{font-size:17px;color:#5e5a63}}
.sys-rail{{gap:22px;align-items:flex-start}} .sys{{margin:0;width:190px}} .sys .shot{{border:1px solid var(--hair);border-radius:6px;overflow:hidden;background:#000}} .sys .shot img{{border-radius:0}}
.sys figcaption{{display:flex;flex-direction:column;margin-top:8px}} .sys figcaption b{{color:#fff;font-size:13px}} .sys figcaption span{{font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.1em;text-transform:uppercase}}
.shot.txt{{height:330px;display:flex;flex-direction:column;justify-content:center;padding:18px;gap:6px;border-style:dashed}} .shot.txt b{{color:#fff}} .shot.txt span{{color:var(--dim);font-size:12px}} .shot.txt em{{font-family:var(--mono);font-size:10.5px;color:var(--or);font-style:normal;margin-top:10px}}
/* prima/dopo */
.pd h4{{font-size:24px;margin-bottom:16px}} .barrato{{color:var(--dim);text-decoration:line-through;text-decoration-color:var(--or);text-decoration-thickness:3px}} .pieno{{color:#fff}}
.fattura{{background:#e6e3de;color:#3a3a3a;border-radius:6px;padding:18px 20px;filter:grayscale(1);font-size:13.5px;display:flex;flex-direction:column;gap:8px;width:380px;max-width:100%}} .f-top{{display:flex;justify-content:space-between;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;padding-bottom:8px;border-bottom:1px solid #bbb}}
.f-row{{display:flex;justify-content:space-between}} .f-row.tot{{border-top:1px solid #bbb;padding-top:8px;font-size:16px}} .fattura .rif{{color:#666;margin-top:6px}}
/* scala */
.scala{{list-style:none;margin:0;padding:0;display:grid;gap:14px}} .step{{position:relative;margin-left:calc(var(--i) * 7%);width:52%;background:#fff;border:1px solid var(--hairl);border-radius:24px;padding:16px 22px 16px 62px;color:var(--ink1)}}
.step .n{{position:absolute;left:20px;top:16px;font-family:var(--mono);font-size:12px;color:var(--or)}} .step b{{display:block;font-size:18px}} .step .d{{font-size:14px;color:#5e5a63}}
.step::before{{content:"";position:absolute;left:36px;bottom:-15px;width:7%;height:14px;border-left:1px dashed #9b958a;border-bottom:1px dashed #9b958a}} .step:last-child::before{{display:none}}
.step.fine{{background:var(--verde);border-color:var(--verde);color:#fff}} .step.fine .n,.step.fine .d{{color:#dff3e6}}
@media(max-width:640px){{.step{{margin-left:0;width:100%}} .step::before{{display:none}}}}
/* cartella */
.cartella{{container-type:inline-size}} .linguette{{display:flex;gap:6px;padding-left:12px}}
.linguetta{{font:600 14px var(--sans);color:var(--silver);background:#2a2a2b;border:0;padding:12px 26px 10px;clip-path:polygon(0 100%,10px 8%,16px 2%,24px 0,calc(100% - 24px) 0,calc(100% - 16px) 2%,calc(100% - 10px) 8%,100% 100%);cursor:pointer}} .linguetta.attiva{{background:var(--carta);color:var(--ink1)}}
.foglio{{background:var(--carta);color:var(--ink1);border-radius:0 6px 6px 6px;padding:28px 32px}} .foglio h3{{color:var(--ink1);font-size:26px;margin:6px 0 14px}}
.checks{{list-style:none;padding:0;margin:0;display:grid;gap:8px}} .checks li{{padding-left:26px;position:relative;font-size:15px}} .checks li::before{{content:"✓";position:absolute;left:0;color:var(--or);font-weight:700}} .checks.dark li{{color:var(--silver)}}
/* player */
.player{{margin-bottom:28px}} .poster{{aspect-ratio:16/8;border:1px solid var(--hair);border-radius:6px;background:radial-gradient(60% 80% at 50% 50%,#242425,#0a0a0a);display:grid;place-items:center;position:relative}}
.play{{width:64px;height:64px;border-radius:50%;background:var(--or);color:#fff;display:grid;place-items:center;font-size:22px}} .dur{{position:absolute;left:16px;bottom:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;color:var(--dim)}}
/* gemelle */
.gemelle{{display:grid;grid-template-columns:1fr 1fr;gap:16px}} @media(max-width:640px){{.gemelle{{grid-template-columns:1fr}}}}
.gem{{background:#fff;border:1px solid var(--hairl);border-radius:12px;padding:22px 24px;color:var(--ink1)}} .gem.giusta{{border:2px solid var(--or)}} .gem .big{{display:block;font-size:81px;line-height:1;font-weight:800;letter-spacing:-.05em;color:#c9c4bb}} .gem b{{display:block;font-size:20px;margin:8px 0 6px}} .gem p{{margin:0;color:#5e5a63;font-size:14.5px}}
.domande{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:26px;border-top:1px solid var(--hairl);padding-top:22px}} @media(max-width:760px){{.domande{{grid-template-columns:1fr}}}}
.domande b{{display:block;color:var(--ink1);font-size:15px}} .domande p{{margin:6px 0 0;color:#5e5a63;font-size:14px}}
/* volti / dietro */
.volti{{display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap}} .volto{{margin:0}} .volto figcaption{{display:flex;flex-direction:column;margin-top:8px}} .volto b{{color:#fff}} .volto span{{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}}
.dietro{{display:grid;grid-template-columns:repeat(4,auto);gap:18px;justify-content:start;max-width:960px}} @media(max-width:900px){{.dietro{{grid-template-columns:1fr 1fr}}}} .lav{{margin:0}} .lav figcaption{{font-size:13px;color:#5e5a63;margin-top:6px;max-width:220px}}
/* albero */
.albero{{display:flex;flex-direction:column;align-items:center;gap:0;padding:10px 0}} .pill{{border:1px solid var(--silver);border-radius:999px;padding:12px 26px;font-weight:700;color:#fff;background:var(--ink2);font-size:17px;position:relative}} .pill.qui{{border-color:var(--or)}}
.conn{{width:2px;height:34px;background:var(--silver)}} .rami{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;position:relative;padding-top:24px}} .rami::before{{content:"";position:absolute;left:16.6%;right:16.6%;top:0;border-top:2px solid var(--silver)}}
.ramo{{display:flex;flex-direction:column;align-items:center;position:relative}} .ramo::before{{content:"";width:2px;height:24px;background:var(--silver);margin-top:-24px;margin-bottom:0}}
.tag-qui{{position:absolute;left:50%;transform:translateX(-50%);top:-30px;font-family:var(--mono);font-size:11px;color:var(--or);white-space:nowrap;animation:su 1.6s ease-in-out infinite alternate}} @keyframes su{{to{{transform:translate(-50%,-4px)}}}} @media (prefers-reduced-motion:reduce){{.tag-qui{{animation:none}}}}
/* tessera */
.laccio{{width:14px;height:70px;background:linear-gradient(90deg,#3a3a3c,#1a1a1b);margin:0 auto -2px;border-radius:2px}}
.tessera{{width:295px;background:var(--ink1);color:var(--silver);border:1px solid var(--hair);border-radius:12px;padding:20px 20px 16px;display:flex;flex-direction:column;gap:12px}} .t-top{{display:flex;justify-content:space-between;font-family:var(--mono);font-size:10px;letter-spacing:.14em;color:var(--dim)}} .tessera h4{{font-size:24px}}
.qr{{width:84px;height:84px;background:repeating-conic-gradient(#fff 0 25%,#000 0 50%) 0 0/16px 16px;border:6px solid #fff;border-radius:4px;margin-top:6px}} .t-foot{{font-family:var(--mono);font-size:10px;color:var(--dim)}}
/* formula */
.formula{{display:grid;grid-template-columns:1fr auto 1fr;gap:26px;align-items:center}} @media(max-width:640px){{.formula{{grid-template-columns:1fr}}}}
.f-col{{border:1px solid var(--hair);border-radius:12px;padding:22px;display:flex;flex-direction:column;gap:4px}} .f-col.or-b{{border-color:var(--or)}} .f-col .k{{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim);margin-bottom:8px}} .f-col b{{font-size:28px;color:#fff;letter-spacing:-.02em}} .f-col span{{color:var(--silver)}} .f-op{{font-family:var(--serif);font-style:italic;font-size:34px;color:var(--dim)}}
/* quadri */
.quadri{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}} .quadri div{{border:1px solid var(--hairl);border-radius:12px;padding:16px 18px;background:#fff}} .quadri b{{color:var(--or);font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase}} .quadri p{{margin:6px 0 0;color:var(--ink1);font-size:14.5px}}
/* faq */
.faq{{display:grid;grid-template-columns:1fr 1fr;gap:34px}} @media(max-width:760px){{.faq{{grid-template-columns:1fr}}}} details{{border-top:1px solid var(--hairl);padding:12px 0}} summary{{cursor:pointer;font-weight:700;color:var(--ink1);list-style:none}} summary::after{{content:"+";float:right;color:var(--or)}} details[open] summary::after{{content:"−"}} details p{{margin:8px 0 0;color:#5e5a63;font-size:14.5px}}
.legale{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-family:var(--mono);font-size:11.5px;color:var(--dim)}} .legale a{{color:var(--silver);text-decoration:underline;text-underline-offset:3px}}
/* nota */
.nota{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:16px}} @media(max-width:900px){{.nota{{grid-template-columns:1fr 1fr}}}}
.nota div{{border-top:1px solid var(--hair);padding-top:9px;display:flex;flex-direction:column;gap:3px}} .nota .k{{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--or)}} .nota b{{font-weight:500;color:var(--silver);font-size:13px}}
.mappa{{padding:56px 0}} .mappa ol{{columns:3;column-gap:34px;margin:22px 0 0;padding-left:26px;font-size:13.5px;color:var(--dim)}} @media(max-width:800px){{.mappa ol{{columns:1}}}} .mappa li{{padding:3px 0;break-inside:avoid}} .mappa li.add{{color:#fff;font-weight:700}} .mappa li.add::marker{{color:var(--or)}}
code{{font-family:var(--mono);font-size:12px;background:rgba(255,255,255,.06);padding:1px 5px;border-radius:3px;color:#fff}} .carta code{{background:rgba(0,0,0,.06);color:var(--ink1)}}
.foot{{margin-top:40px;padding-top:18px;border-top:1px solid var(--hair);font-family:var(--mono);font-size:11.5px;color:var(--dim);display:flex;flex-wrap:wrap;gap:8px 22px}}
</style>
<div class="grana" aria-hidden="true"></div>
<div class="wrap">
<header class="top">
  <div class="eyebrow">Digital Empire · Tavola Estetica <b>v2</b> · agency-empire-landing.vercel.app · solo aggiunte · 13 settembre 2026</div>
  <h1>Il secondo strato: <i>sei atti, ogni immagine intera.</i></h1>
  <p class="tesi">Riscritta dopo lo studio di funneloperator.it (4 rapporti, 3.174 righe) e la critica di Max sulle immagini. Le 37 sezioni di giugno restano; sopra si stende un secondo strato che segue il ritmo di §15 — <b>volto → fatti → problema visto → meccanismo → prova → chi siamo → offerta → chiusura</b>. Ogni still sta <b>al suo pixel nativo o più piccolo, intero</b>, in una colonna che lo ospita; gli schemi sono costruiti in HTML qui dentro, come saranno in pagina.</p>
  <div class="regole"><div><b>18 + 3 + 1</b><span>inserimenti in pagina · estensioni di sezioni nostre · CTA fissa (nelle pagine nuove)</span></div><div><b>9 · 9</b><span>aggiunte con immagine · schemi in HTML puro (0 dipendenze)</span></div><div><b>+≤ 8.800 px</b><span>+23% su 38.683 · 7 superfici carta alternate · mai due chiare di fila</span></div><div><b>2% · 16% · 70%</b><span>primo volto · prima prova visiva · prima porta nuova (§15: ≤10 · ≤30 · &gt;50)</span></div></div>
</header>
{"".join(T)}
<section class="mappa">
  <div class="eyebrow">La pagina, dall'alto in basso</div>
  <h2 style="margin-top:12px;font-size:clamp(22px,2.6vw,32px)">Dove entra ogni cosa. <i style="color:var(--dim)">In bianco le aggiunte; il resto è com'era.</i></h2>
  <ol>{mappa}</ol>
</section>
<div class="foot"><span>PIANO-MAESTRO/38-PIANO-SITO-AGENCY-SOLO-AGGIUNTE-v2.md</span><span>ADR-030 §13 · ADR-031 §14 §15</span><span>reports/66-funneloperator-*.md</span><span>ripresa EMP-XR4F</span><span>build su «vai»</span></div>
</div>'''
OUT.write_text(HTML, encoding="utf-8")
print(OUT, len(HTML) // 1024, "KB")
