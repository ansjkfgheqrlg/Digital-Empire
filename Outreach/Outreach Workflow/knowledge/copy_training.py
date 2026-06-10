"""
Copy Training Material — Digital Empire Outreach
Materiale di formazione esteso per il writer agent.

AGGIORNATO 2026-06-04 — PIVOT STRATEGICO.
Si vendono 3 implementazioni AI (workflow), non più landing page / CRO:
  - TEMPLATE_A = Outreach Factory  (target: agenzia, coach, smm_freelance, consulente)
  - TEMPLATE_B = Content Factory   (target: info_product, ecommerce)
  - TEMPLATE_C = Second Brain      (upsell trasversale: org strutturate / chi usa molto l'AI)

Costanti di contratto usate negli esempi:
  PRESENTATION_URL = https://presentazione-empire.vercel.app/
  AGENCY_URL       = https://agency-empire-landing.vercel.app
"""

# ─────────────────────────────────────────────────────────────────────────────
# ESEMPI APPROVATI — TEMPLATE A (OUTREACH FACTORY)
# settore: chiavi canoniche → agenzia, coach, smm_freelance, consulente
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE_A_APPROVED_EXAMPLES = [
    {
        "settore": "agenzia",
        "oggetto": "Ho automatizzato l'outreach al 100% — gira da solo ogni mattina",
        "corpo": """Io ho costruito un sistema che fa l'outreach al posto mio: ogni mattina scova i lead, scrive 300 email personalizzate e le invia via Gmail e social. Da solo.

Se gestisci un'agenzia, sai qual è il problema vero: l'acquisizione a freddo resta sempre indietro. Quando sei in delivery sui clienti, trovare e contattare nuovi prospect a mano si ferma — e ti porta via 8-12 ore a settimana quando lo fai.

Questo workflow lo automatizza al 100%: scraping lead, qualifica, scrittura personalizzata, invio e follow-up. Te lo installo sui tuoi server in 7 giorni, il codice sorgente è tuo, zero canoni mensili. Non noleggi un tool: possiedi un motore.

L'unica domanda sensata è "funziona davvero per me?". Non ti chiedo di crederci sulla parola: te lo mostro dal vivo mentre gira, in 20 minuti.

Ti lascio la presentazione qui: https://presentazione-empire.vercel.app/ — se ha senso, prenotiamo una call breve. Per chi parte questo mese c'è uno sconto early-adopter.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Hype operativo in apertura (prima persona), UN solo problema (outreach manuale), workflow al 100% con i 4 garanti, obiezione = fiducia sciolta dalla demo live, CTA con presentazione + sconto, firma con AGENCY_URL"
    },
    {
        "settore": "smm_freelance",
        "oggetto": "Il tuo outreach può girare mentre gestisci i social dei clienti",
        "corpo": """Io ho automatizzato il mio outreach al 100%: un workflow che ogni mattina trova i lead giusti, scrive le email una per una e parte. Senza che io tocchi niente.

Da freelance porti risultati ai clienti tutto il giorno — ma trovare i TUOI clienti nuovi è un lavoro manuale che non scala. Resta sempre l'ultima cosa in lista, e intanto la pipeline si svuota.

Questo è il sistema che lo risolve: scraping, qualifica, 300 email personalizzate al giorno, follow-up automatici. Te lo installo in 7 giorni sui tuoi server, il codice è tuo, zero canoni mensili. Lo possiedi tu, non lo affitti.

So che il dubbio è solo uno: funzionerà sul mio caso? Per questo non te lo racconto — te lo mostro dal vivo mentre gira, in 20 minuti.

Qui la presentazione: https://presentazione-empire.vercel.app/ — se ti convince, ci prendiamo 20 minuti. C'è uno sconto early-adopter per chi inizia questo mese.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Apertura hype prima persona, problema operativo unico e calzante per freelance, workflow con garanti, obiezione = fiducia + demo, CTA presentazione + sconto, vocabolario AI/automazione approvato"
    },
    {
        "settore": "coach",
        "oggetto": "Quando sei nei percorsi, l'acquisizione si ferma. L'ho automatizzata.",
        "corpo": """Io ho costruito un sistema che fa l'outreach al 100% da solo: ogni mattina trova i lead, scrive 300 email personalizzate e le manda via Gmail e social.

Il problema che conosci bene: quando sei dentro le sessioni e i percorsi dei clienti, l'acquisizione di nuovi si ferma del tutto. Cercare e contattare prospect a mano ti porta via 8-12 ore a settimana che non hai.

Questo workflow lo fa girare al posto tuo: scova i lead, li qualifica, scrive personalizzato e segue i follow-up. Te lo installo in 7 giorni sui tuoi server, codice tuo, zero canoni mensili. Un motore che possiedi, non un abbonamento.

L'unico vero dubbio è la fiducia: funziona per me? Te lo mostro dal vivo mentre lavora, 20 minuti, e decidi tu.

Ti lascio la presentazione: https://presentazione-empire.vercel.app/ — se ha senso facciamo una call breve. Per i primi che partono questo mese c'è uno sconto early-adopter.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Hype + prima persona, problema operativo singolo specifico per coach (acquisizione si ferma in delivery), workflow con garanti, fiducia sciolta dalla demo, CTA presentazione + call + sconto"
    },
    {
        "settore": "consulente",
        "oggetto": "Le ore che bruci a cercare prospect possono girare da sole",
        "corpo": """Io ho automatizzato l'outreach al 100%: un sistema che ogni mattina scova i lead, scrive 300 email personalizzate e le invia da solo via Gmail e social.

Da consulente il tuo tempo vale tanto, ma cercare e contattare nuovi prospect a mano è proprio l'attività non fatturabile che te ne brucia di più — facilmente 8-12 ore a settimana.

Questo workflow elimina quella parte: scraping, qualifica, scrittura personalizzata, invio, follow-up. Te lo installo in 7 giorni sui tuoi server, il codice è tuo, zero canoni mensili. Possiedi il motore, non lo affitti.

Il prodotto è chiaro, l'unico dubbio resta la fiducia. Per questo te lo mostro dal vivo mentre gira, in 20 minuti, sul tuo caso.

Qui la presentazione: https://presentazione-empire.vercel.app/ — se ti torna, prenotiamo una call. C'è uno sconto early-adopter per chi parte questo mese.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Prima persona + hype, problema operativo unico (ore non fatturabili su prospecting), workflow con i 4 garanti, obiezione = fiducia + demo live, CTA presentazione + call + sconto, firma corretta"
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# ESEMPI APPROVATI — TEMPLATE B (CONTENT FACTORY)
# settore: chiavi canoniche → info_product, ecommerce
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE_B_APPROVED_EXAMPLES = [
    {
        "settore": "info_product",
        "oggetto": "I contenuti di una settimana in un pomeriggio",
        "corpo": """Io ho costruito un motore AI che genera il copy e mi costruisce caroselli, grafiche e script video in automatico. Quello che prima era una settimana di lavoro, ora lo chiudo in un pomeriggio.

Se vendi corsi, i contenuti sono il tuo motore di vendita — ma anche il buco nero del tempo. Scrivere il copy, impaginare i caroselli, montare gli script ti porta via interi pomeriggi ogni settimana, ogni settimana.

Questo workflow produce tutto in pipeline: copy ottimizzato per convertire, caroselli e grafiche pronte, script video. Te lo installo in 7 giorni, gira sui tuoi server, il codice è tuo, zero canoni mensili. Non un tool in abbonamento: un motore di contenuti che possiedi.

L'unico dubbio sensato è la qualità dell'output. Per questo non te lo racconto: te lo mostro dal vivo mentre genera un carosello sul tuo brand, in 20 minuti.

Qui la presentazione: https://presentazione-empire.vercel.app/ — se ti convince, facciamo una demo. Per chi parte questo mese c'è uno sconto early-adopter.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Hype output-driven in prima persona, un solo problema operativo (produzione contenuti manuale), workflow con garanti, obiezione = qualità output → demo live sul brand, CTA presentazione + sconto"
    },
    {
        "settore": "ecommerce",
        "oggetto": "Contenuti nuovi in continuazione, prodotti in automatico",
        "corpo": """Io ho un motore AI che genera copy, schede, ads creative e script in automatico: i contenuti che ti servono in continuazione, prodotti senza più farli a mano.

Con un ecommerce il ritmo è il problema: servono schede prodotto, creatività per le ads, post social, e produrli a mano (o pagando freelance) non regge la cadenza e non scala con il catalogo.

Questo workflow lo fa girare in pipeline: copy ottimizzato, grafiche e caroselli pronti, script video. Te lo installo in 7 giorni sui tuoi server, il codice è tuo, zero canoni mensili. Scali la produzione senza assumere e senza dipendere da terzi.

Il dubbio vero è uno: l'output è abbastanza buono? Per questo te lo mostro dal vivo mentre genera contenuti sui tuoi prodotti, in 20 minuti.

Ti lascio la presentazione: https://presentazione-empire.vercel.app/ — se ti torna, ci prendiamo 20 minuti per una demo. C'è uno sconto early-adopter per chi inizia questo mese.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Prima persona + hype sul volume contenuti, problema operativo unico (ritmo produzione non scala), workflow con garanti, obiezione = qualità → demo sui prodotti, CTA presentazione + sconto, firma corretta"
    },
    {
        "settore": "info_product",
        "oggetto": "Ho automatizzato la produzione contenuti: copy, grafiche, script",
        "corpo": """Io ho costruito una pipeline dove l'AI scrive il copy ottimizzato e poi costruisce da sola caroselli, grafiche e script video. Un pomeriggio di lavoro vale la produzione di una settimana.

Se vivi di formazione e info-prodotti, pubblicare costante è ciò che ti tiene davanti al pubblico — ma è anche la cosa che ti costringe a scegliere ogni settimana tra creare contenuti e vendere. Il tempo non basta per entrambi.

Questo workflow ti toglie quella scelta: copy che converte, visual pronti, script per i video, tutto generato in automatico. Te lo installo in 7 giorni, gira sui tuoi server, codice tuo, zero canoni mensili. Lo possiedi.

L'unico dubbio è se la qualità tiene. Non te lo dico io: te lo mostro dal vivo mentre genera un contenuto sul tuo tema, in 20 minuti.

Qui la presentazione: https://presentazione-empire.vercel.app/ — se ti convince, facciamo una demo live. Per chi parte questo mese c'è uno sconto early-adopter.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Apertura hype prima persona, problema operativo unico (creare vs vendere), workflow con i 4 garanti, obiezione = qualità → demo sul tema, CTA presentazione + call + sconto"
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# ESEMPI APPROVATI — TEMPLATE C (SECOND BRAIN — Context Engineering)
# settore: org strutturate / chi usa molto l'AI → es. agenzia (con team), consulente
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE_C_APPROVED_EXAMPLES = [
    {
        "settore": "agenzia",
        "oggetto": "La tua AI dimentica tutto: ho risolto con un Second Brain",
        "corpo": """Io ho costruito un Second Brain a grafo che dà all'AI una memoria permanente: conosce i clienti, i processi, la brand voice e le decisioni, e non riparte più da zero a ogni chat.

Se in agenzia il team usa l'AI ogni giorno, il problema vero è uno solo: dimentica tutto. Ogni nuova chat riparte da zero, devi ri-spiegare contesto e tono di ogni cliente, e quello che esce resta generico e da rilavorare.

Questo è Context Engineering (lo chiama così Andrej Karpathy): una knowledge base interconnessa a grafo collegata all'LLM. Te la installo in 7 giorni sui tuoi server, il codice è tuo, zero canoni mensili. Da quel momento l'AI lavora con la memoria di tutta l'agenzia.

L'unico dubbio è se cambia davvero il risultato. Per questo te lo mostro dal vivo: faccio due domande all'AI prima e dopo il Second Brain, e vedi la differenza in 20 minuti.

Ti lascio la presentazione: https://presentazione-empire.vercel.app/ — se ti interessa, organizziamo una demo live. Per i primi che partono questo mese c'è uno sconto early-adopter.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Hype in prima persona sul Second Brain, un solo problema operativo (AI smemorata), Context Engineering con i 4 garanti, obiezione = fiducia → demo prima/dopo, CTA presentazione + sconto, firma corretta"
    },
    {
        "settore": "consulente",
        "oggetto": "Context Engineering: l'AI che conosce davvero i tuoi processi",
        "corpo": """Io ho dato all'AI una memoria permanente: un Second Brain a grafo che le fa conoscere clienti, processi, brand voice e decisioni — e smette di ripartire da zero ogni volta.

Da consulente l'AI è ormai parte del lavoro, ma il limite lo conosci: dimentica tutto. Ogni volta devi ri-caricare il contesto del cliente e delle metodologie, e il risultato resta generico finché non lo rilavori a mano.

Quello che ho costruito è Context Engineering (il termine è di Andrej Karpathy): tutta la tua conoscenza collegata a grafo e data in pasto all'LLM. Te lo installo in 7 giorni sui tuoi server, il codice è tuo, zero canoni mensili. L'AI inizia a lavorare con il contesto di tutto il tuo metodo.

Il prodotto è chiaro, l'unico dubbio è la fiducia: cambia davvero l'output? Te lo mostro dal vivo, due domande prima e dopo, in 20 minuti.

Qui la presentazione: https://presentazione-empire.vercel.app/ — se ti torna, facciamo una demo. C'è uno sconto early-adopter per chi parte questo mese.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Prima persona + hype, problema operativo unico (AI senza memoria), Context Engineering con garanti, obiezione = fiducia → demo prima/dopo, CTA presentazione + call + sconto"
    },
    {
        "settore": "info_product",
        "oggetto": "Ho dato all'AI una memoria permanente del mio business",
        "corpo": """Io ho costruito un Second Brain a grafo che dà all'AI una memoria stabile: conosce i miei prodotti, il pubblico, la brand voice e le decisioni passate, e non riparte più da zero.

Se usi l'AI ogni giorno per contenuti e business, il fastidio è sempre quello: dimentica tutto. Ogni chat ricomincia da capo, devi ri-spiegare chi sei e come parli, e l'output finisce per suonare come quello di chiunque altro.

Questo è Context Engineering (Andrej Karpathy lo chiama così): tutta la conoscenza del tuo business interconnessa e collegata all'LLM. Te lo installo in 7 giorni sui tuoi server, codice tuo, zero canoni mensili. L'AI smette di essere generica e inizia a suonare come te.

L'unico vero dubbio è se senti la differenza. Per questo te lo mostro dal vivo: stessa richiesta all'AI, prima e dopo il Second Brain, in 20 minuti.

Ti lascio la presentazione: https://presentazione-empire.vercel.app/ — se ti convince, organizziamo una demo live. Per chi parte questo mese c'è uno sconto early-adopter.

https://agency-empire-landing.vercel.app
Max | Digital Empire""",
        "perche_funziona": "Hype prima persona, problema operativo unico (AI smemorata e generica), Context Engineering con garanti, obiezione = fiducia → demo prima/dopo, CTA presentazione + sconto, firma corretta"
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# ANTI-ESEMPI — cosa NON fare (con spiegazione dettagliata) — pivot AI
# ─────────────────────────────────────────────────────────────────────────────

ANTI_EXAMPLES = [
    {
        "tipo": "vende_landing_page_generica",
        "email_sbagliata": """Oggetto: Migliora la tua presenza online

Ciao,

Mi chiamo Max e mi occupo di realizzare landing page e ottimizzare il conversion rate per aziende come la tua. Ho visto il tuo sito e penso che potremmo migliorare le tue conversioni con una nuova pagina di atterraggio.

Offriamo servizi di web design e CRO su misura per portarti più clienti.

Ti va di fissare una call per parlarne?

Max""",
        "perche_sbagliata": "È il vecchio posizionamento abbandonato: vende landing page / CRO, parla di 'conversioni' (offende chi fa marketing), usa 'mi occupo / offriamo servizi'. Zero hype AI, nessun prodotto chiaro, nessun workflow, nessuna presentazione. Dopo il pivot questa email è fuori target e fuori prodotto.",
        "come_correggere": "Aggancia con l'hype dell'automazione AI di UN processo (outreach/contenuti/memoria), presenta il workflow al 100% con i 4 garanti (codice tuo, €0 canoni, 7 giorni, tuoi server), chiudi con la presentazione (PRESENTATION_URL) + call. Parla di operatività, non di conversioni."
    },
    {
        "tipo": "offende_le_conversioni",
        "email_sbagliata": """Oggetto: Le tue conversioni sono basse

Ciao,

Ho analizzato la tua attività e ho notato che il tuo marketing non sta convertendo come dovrebbe. Le tue campagne perdono clienti e il tuo tasso di conversione è sotto la media del settore.

Io posso sistemare quello che tu non riesci a far funzionare e portarti finalmente dei risultati.

Fammi sapere.

Max""",
        "perche_sbagliata": "Dire a un'agenzia o a un marketer che 'le sue conversioni sono basse' o che 'non riesce a far funzionare' il suo lavoro è un insulto al loro mestiere: la leva sbagliata. La leva giusta del pivot è l'operatività ('ti stravolgo l'operatività'), non un giudizio sui loro risultati di marketing.",
        "come_correggere": "Non toccare la qualità del loro marketing. Offri di automatizzare un processo OPERATIVO che fanno a mano (outreach/contenuti). Tono da pari: 'io ho costruito un sistema che…', mai 'tu non ci riesci, io sì'."
    },
    {
        "tipo": "nessuna_chiarezza_prodotto",
        "email_sbagliata": """Oggetto: Soluzioni AI per il tuo business

Ciao,

Con l'intelligenza artificiale oggi si può fare di tutto. Io aiuto le aziende a sfruttare l'AI per automatizzare i processi, generare contenuti, gestire i dati, migliorare la produttività e tanto altro.

Posso costruirti soluzioni AI personalizzate per ogni tua esigenza.

Ti interessa approfondire?

Max""",
        "perche_sbagliata": "Vaghissima: promette 'tutto' con l'AI e quindi non vende nulla. La forza del pivot è la chiarezza assoluta — UN prodotto che risolve UN problema al 1000%. Elencare automazione + contenuti + dati + produttività azzera la chiarezza e lascia l'unica obiezione (la fiducia) senza nessuna leva.",
        "come_correggere": "Scegli UN solo prodotto-gancio in base al target (Outreach Factory / Content Factory / Second Brain), nomina UN solo problema operativo, presenta UN workflow con i 4 garanti e chiudi con presentazione + demo live."
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# MICRO-REGOLE PER SETTORE — chiavi CANONICHE del pivot
# Chiavi: agenzia, info_product, coach, smm_freelance, ecommerce, consulente, default
# ─────────────────────────────────────────────────────────────────────────────

SECTOR_MICRO_RULES = {
    "agenzia": [
        "Prodotto-gancio: OUTREACH FACTORY. Aggancia con l'hype 'outreach automatizzato al 100%'",
        "Problema unico: l'acquisizione a freddo resta indietro quando sei in delivery sui clienti",
        "Non parlare delle LORO conversioni (le curano loro): parla di operatività e ore liberate",
        "Usa vocabolario AI/automazione senza spiegarlo — è gente del settore, lo capisce al volo",
        "Garanti sempre: codice tuo, €0 canoni, setup 7 giorni, sui loro server. Chiudi con presentazione + call",
    ],
    "info_product": [
        "Prodotto-gancio: CONTENT FACTORY. Aggancia con 'i contenuti di una settimana in un pomeriggio'",
        "Problema unico: produrre copy + grafiche + script a mano divora i pomeriggi ogni settimana",
        "La tensione giusta: scegliere ogni settimana tra CREARE contenuti e VENDERE — l'AI toglie la scelta",
        "Obiezione = qualità dell'output → sciogli con la demo live che genera un contenuto sul loro tema",
        "Garanti sempre + presentazione (PRESENTATION_URL) nel CTA + sconto early-adopter",
    ],
    "coach": [
        "Prodotto-gancio: OUTREACH FACTORY. Aggancia con 'l'outreach gira mentre lavori coi clienti'",
        "Problema unico: quando sei nelle sessioni/percorsi, l'acquisizione di nuovi si ferma del tutto",
        "Tono peer-to-peer, da consulente a consulente; quantifica le ore (8-12/settimana)",
        "Mai parlare di conversioni: parla di tempo recuperato e pipeline che non si svuota",
        "Garanti sempre + demo live + presentazione + sconto per chi parte questo mese",
    ],
    "smm_freelance": [
        "Prodotto-gancio: OUTREACH FACTORY. Aggancia con 'il tuo outreach gira da solo ogni mattina'",
        "Problema unico: porti risultati ai clienti ma trovare i TUOI clienti nuovi non scala",
        "Vocabolario AI/automazione tecnico, senza spiegazioni — è un professionista del digitale",
        "L'angolo: liberi le ore che oggi bruci a fare prospecting manuale tra un cliente e l'altro",
        "Garanti sempre + presentazione nel CTA + sconto early-adopter + firma con AGENCY_URL",
    ],
    "ecommerce": [
        "Prodotto-gancio: CONTENT FACTORY. Aggancia con 'contenuti nuovi in continuazione, in automatico'",
        "Problema unico: il ritmo di schede/ads creative/social non regge se i contenuti li fai a mano",
        "L'angolo operativo: scalare la produzione senza assumere e senza dipendere da freelance",
        "Obiezione = qualità output → demo live che genera contenuti sui loro prodotti",
        "Garanti sempre + presentazione (PRESENTATION_URL) + sconto + firma con AGENCY_URL",
    ],
    "consulente": [
        "Prodotto-gancio: OUTREACH FACTORY. Aggancia con 'le ore di prospecting che girano da sole'",
        "Problema unico: il prospecting manuale è l'attività non fatturabile che brucia più tempo",
        "Tono molto peer-to-peer, da consulente a consulente; numeri concreti (8-12 ore/settimana)",
        "Mai parlare di conversioni: parla di tempo fatturabile recuperato e acquisizione costante",
        "Garanti sempre + demo live + presentazione + sconto early-adopter",
    ],
    "default": [
        "Aggancia con l'hype dell'automazione AI di UN processo specifico (prima persona singolare)",
        "Nomina UN SOLO problema operativo — chiarezza assoluta, niente lista di dolori",
        "Presenta il workflow al 100% con i 4 garanti: codice tuo, €0 canoni, 7 giorni, tuoi server",
        "Obiezione = solo fiducia → sciogli con 'te lo mostro dal vivo, demo live, 20 minuti'",
        "UNA sola CTA: guarda la presentazione (PRESENTATION_URL) + call; firma con AGENCY_URL + 'Max | Digital Empire'",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# OGGETTI EMAIL — libreria estesa di formule efficaci (hype / operatività, 3 prodotti)
# ─────────────────────────────────────────────────────────────────────────────

SUBJECT_LINE_FORMULAS = {
    "template_a": [  # Outreach Factory
        "Ho automatizzato l'outreach al 100% — gira da solo ogni mattina",
        "300 email personalizzate al giorno, zero mani umane",
        "Il tuo outreach può girare mentre dormi",
        "L'acquisizione clienti che si fa da sola ogni mattina",
        "Ho tolto l'outreach manuale di mezzo — ecco come",
        "Outreach al 100% automatico, codice tuo, €0 canoni",
        "Le ore che bruci a cercare lead possono girare da sole",
    ],
    "template_b": [  # Content Factory
        "I contenuti di una settimana in un pomeriggio",
        "Un'AI che mi scrive il copy e mi costruisce i caroselli",
        "Ho automatizzato la produzione contenuti — copy, grafiche, script",
        "Contenuti nuovi in continuazione, prodotti in automatico",
        "Il motore che genera copy + visual + script al posto tuo",
        "Smetti di scegliere tra creare contenuti e vendere",
        "Copy ottimizzato e caroselli pronti, senza farli a mano",
    ],
    "template_c": [  # Second Brain
        "La tua AI dimentica tutto: ho risolto con un Second Brain",
        "Ho dato all'AI una memoria permanente di tutta l'azienda",
        "Context Engineering: l'AI che conosce davvero i tuoi processi",
        "L'AI smette di ripartire da zero a ogni chat",
        "Una memoria a grafo per la tua AI: clienti, processi, brand voice",
        "Da AI generica a AI che suona come te",
        "Il Second Brain che dà contesto permanente al tuo LLM",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# PRINCIPI DI REVISIONE — come migliorare un'email non approvata (pivot AI)
# ─────────────────────────────────────────────────────────────────────────────

REVISION_PRINCIPLES = """
COME MIGLIORARE UN'EMAIL RESPINTA DAL QA (pivot: implementazioni AI)

SE IL PROBLEMA È: LINGUAGGIO AI/ROBOTICO (da bot, non da founder)
→ Nota: il LESSICO "AI/automazione/workflow" è ora APPROVATO. Il problema è il TONO da bot.
→ Elimina aperture generiche e corporate vuoto (sinergie, approccio olistico, soluzione innovativa)
→ Riscrivi in prima persona singolare: "io ho costruito…", "io ho automatizzato…"
→ Test: leggi ad alta voce — suona come un founder che mostra il suo motore, o come una brochure?

SE IL PROBLEMA È: NESSUNA CHIAREZZA DI PRODOTTO
→ Scegli UN solo prodotto-gancio (Outreach / Content / Second Brain) in base al target
→ Nomina UN SOLO problema operativo — togli ogni elenco di dolori
→ Aggiungi i 4 garanti del workflow: codice tuo, €0 canoni, 7 giorni, tuoi server

SE IL PROBLEMA È: PARLA DI CONVERSIONI (offende il marketer)
→ Sostituisci ogni riferimento a "conversioni / tasso di conversione / risultati di marketing"
  con operatività: ore liberate, processo che gira da solo, contenuti prodotti in automatico
→ La leva è "ti stravolgo l'operatività", mai "ti miglioro le conversioni"

SE IL PROBLEMA È: OBIEZIONE NON GESTITA
→ L'unica obiezione è la FIDUCIA. Aggiungi la riga demo live: "te lo mostro dal vivo, 20 minuti"
→ Ricorda: la presentazione di qualità estrema È la prova di professionalità che genera fiducia

SE IL PROBLEMA È: CTA / LINK
→ Il link presentazione (PRESENTATION_URL) DEVE essere nel CTA della prima email
→ Una sola CTA: guarda la presentazione + (eventuale) call. Cita lo sconto early-adopter
→ La firma deve avere la riga AGENCY_URL e "Max | Digital Empire"

SE L'EMAIL È FUORI LUNGHEZZA
→ Target corpo: ~160-260 parole. Sotto: manca sostanza al workflow/garanti.
→ Sopra: taglia transizioni e ripetizioni, tieni hype → 1 problema → workflow → fiducia → CTA
"""

# ─────────────────────────────────────────────────────────────────────────────
# STATISTICHE DI SETTORE — dati credibili sull'AUTOMAZIONE (chiavi PRESERVATE)
# Le 4 chiavi mobile_search / page_speed / first_response / phone_vs_online
# restano per compatibilità con copy_knowledge.py, ma ora descrivono l'automazione.
# ─────────────────────────────────────────────────────────────────────────────

SECTOR_STATISTICS = {
    # chiavi storiche RICICLATE con statistiche sull'automazione (NON rinominare le chiavi)
    "mobile_search": "Chi fa outreach a mano dedica in media 8-12 ore a settimana solo a cercare lead e scrivere email una per una",
    "page_speed": "Produrre a mano i contenuti di una settimana (copy + grafiche + script) porta via 2-3 pomeriggi pieni; un workflow li genera in poche ore",
    "first_response": "Un sistema di outreach automatizzato può inviare 300+ email personalizzate al giorno per mailbox, contro le poche decine fattibili a mano",
    "phone_vs_online": "Senza una memoria/contesto permanente, l'LLM riparte da zero a ogni sessione: gran parte del contesto va ri-fornito ogni volta, con output più generico",
    # statistiche aggiuntive sul pivot (chiavi nuove, libere da vincoli di import)
    "automation_roi": "Automatizzare al 100% un processo ripetitivo libera tempo che torna sul lavoro a valore: il ticket si ripaga eliminando ore manuali ricorrenti",
    "ownership": "Con codice sorgente di proprietà e €0 canoni mensili, il costo del workflow è una tantum: nessun abbonamento che cresce nel tempo",
    "setup_time": "Un'implementazione mirata su un singolo processo si installa tipicamente in circa 7 giorni, perché risolve un problema solo (chiarezza = velocità)",
    "context_engineering": "Il Context Engineering (knowledge base a grafo collegata all'LLM) dà all'AI memoria permanente di clienti, processi e brand voice, riducendo la rilavorazione manuale dell'output",
}
