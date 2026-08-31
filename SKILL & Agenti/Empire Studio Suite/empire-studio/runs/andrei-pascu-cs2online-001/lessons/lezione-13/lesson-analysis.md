# Lezione 13 — Come faccio la ricerca di copywriting con l'AI

**Corso:** Claude Speedrun 2 | **Sezione:** AI – per copywriting (1/4)
**URL:** https://www.andrei-copy.com/cs2online/lezione-13-come-faccio-in-ricerca-di-copywriting-con-lai-ryx39
**Video:** Vimeo `1171986942`, durata 27:14 (1634s)
**Tipo:** **PRATICA** — demo end-to-end su cliente reale (Simone Ferretti / SoundBox Studio, servizio podcast).
**Metodo:** panoramica + "Cosa hai imparato" ufficiali (nessuna risorsa Drive per questa lezione) + 38 frame video visionati nativamente (28 scan 60s + 10 dense mirati).

---

## Mappa timeline (confermata con visione diretta)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–4:30 | Talking head — intro, principi generali (deliverable, contesto) | — |
| 8:00 | **Demo**: trascrizione call cliente via Gemini (doc "Call Onboarding - Casa Architettura...") | `frame-t8m00s...jpg` |
| 8:15 | **Demo**: struttura documenti ClickUp ("Client overview - [nome]" > Client overview, Servizio 1, Servizio 2) — sidebar reale agenzia AP Sales (spazi: AP Formazione, AP Sales, Clients con Onboarding/Active/Completed/Archive) | `frame-t8m15s...jpg` |
| 9:00–11:00 | **Demo**: documento "Client overview" compilato — sezioni Mission, Target audience, Profilo target | — |
| 10:00 | **Demo**: profilo cliente reale in CRM interno ("Simone Ferretti", contatti, presenza online) | `frame-t10m00s...jpg` |
| 11:30 | **Demo**: doc Client overview completo — "Agenzie passate", "Preferenze & contatti" (WhatsApp vs email, disponibilità call), "Service overview" (Strategy, Onboarding 15/03/2026, chiuso da Nicolas), "Cosa facciamo per lui" (descrizione servizio dettagliata) | `frame-t11m30s...jpg` |
| 12:00 | **Demo**: setup iniziale Claude Project | `frame-t12m00s...jpg` |
| 15:30 | **Demo**: Project Claude "Simone Ferretti" completo — descrizione, istruzioni ("Sono titolare di un'agenzia di marketing chiamata AP SALES..."), file `Client_overview_Simone_Ferretti.md` (206 righe) allegato, modello **Opus 4.6 Extended**. Overlay testo: **"Per dettare roba in questo modo al mio mac, uso l'app Wispr; devastante."** (tool dettatura vocale) | `frame-t15m30s...jpg` |
| 17:30 | **Demo — IL PROMPT ESATTO**: stesso identico prompt mandato in parallelo a Claude e Perplexity: *"Come vedi, sto facendo ricerca di copywriting per questo cliente, Simone Ferretti. Controlla il documento. Voglio che tu mi aiuti a svolgere il documento di ricerca iniziale, che deve essere rivisto in due categorie: 1. Ricerca che io ho raccolto, quindi informazioni dal mio client overview document e ricerca che tu hai fatto online. 2. Non utilizzare il mio blog; utilizza solo ed esclusivamente ricerche scientifiche. 3. Utilizza i blog solamente per opinioni, mentre per dati oggettivi utilizza le ricerche scientifiche."* | `frame-t17m30s...jpg` |
| 18:00 | **Demo**: setup Space Perplexity per il cliente | `frame-t18m00s...jpg` |
| 21:00 | **Demo**: documento "Sintesi operativa per il copy della sales page" — sezioni Pain point da toccare, Obiezioni da neutralizzare, TOV | `frame-t21m00s...jpg` |
| 21:30 | **Demo**: MarkEdit aperto su "Documento di Ricerca Iniziale — SoundBox Studio (Simone Ferretti).md" (197+ righe) — struttura reale: Executive Summary, Parte 1 Ricerca Interna, Parte 2 Ricerca Esterna, Sintesi operativa con Pain point numerati + fonte citata per ciascuno (es. dato "47% molla dopo 3 episodi"), bibliografia stile accademico (peer-reviewed, SAGE Open) | `frame-t21m30s...jpg` |
| 26:00 | **Demo**: file salvati in cartella Finder dedicata | `frame-t26m00s...jpg` |
| 27:00+ | Talking head, chiusura | — |

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Workflow di ricerca copywriting end-to-end (osservato per intero, cliente reale): call onboarding → trascrizione Gemini → documento ClickUp "Client overview" (Mission, Target audience, Preferenze contatto, Service overview, Cosa facciamo per lui) → Project Claude dedicato con questo doc allegato → ricerca in PARALLELO su Claude e Perplexity con lo stesso prompt → editing manuale in MarkEdit → documento finale con citazioni. | Timeline completa, frame t8m00s→t26m00s |
| KA-02 | Prompt esatto di ricerca copywriting (verbatim, osservato a schermo): vincola l'AI a separare "ricerca raccolta dall'utente" (client overview) da "ricerca fatta online" dall'AI, e vieta esplicitamente l'uso del blog personale come fonte dati oggettivi — solo "ricerche scientifiche" per dati, blog solo per opinioni. | frame-t17m30s |
| KA-03 | Claude e Perplexity usati IN PARALLELO sullo stesso identico prompt/task — poi si sceglie l'output migliore o si combinano (confermato: entrambi visibili simultaneamente a schermo, stesso testo). | frame-t17m30s, t18m00s |
| KA-04 | Struttura reale del documento di ricerca finale: Executive Summary → Parte 1 (Ricerca Interna, dal client overview) → Parte 2 (Ricerca Esterna, studi scientifici + blog solo opinioni) → Sintesi operativa per il copy (Pain point da toccare nel copy — ciascuno con dato/fonte numerata, es. "47% molla dopo 3 episodi[^2]" — e Obiezioni da neutralizzare, ciascuna con contro-argomento specifico). | frame-t21m30s |
| KA-05 | Modello usato per il Project cliente: **Opus 4.6 con Extended Thinking** (coerente con lezione 6: documento riusato indefinitamente → modello più potente). | frame-t15m30s |
| KA-06 | Tool di dettatura vocale menzionato di sfuggita: **Wispr** ("Per dettare roba in questo modo al mio mac, uso l'app Wispr; devastante.") — non nel testo ufficiale, solo overlay a schermo. | frame-t15m30s |
| KA-07 | Struttura organizzativa reale dell'agenzia (ClickUp): spazi separati "AP Formazione", "AP Sales", "Clients" (con sotto-cartelle Onboarding / Active clients / Completed projects / Archive) — ogni cliente ha un doc "Client overview - [nome]" con sotto-pagine per servizio. | frame-t8m15s |
| KA-08 | Regola esplicita (da "Cosa hai imparato"): togliere le fonti dal documento di contesto finale — se serve che Claude legga un sito specifico, glielo si fa leggere direttamente in quel momento; il documento di contesto serve per non dover ripetere l'operazione ogni volta, non per essere un archivio di link. | Panoramica ufficiale |
| KA-09 | Principio 80/20 applicato alla ricerca: l'AI fa il 90% del lavoro pesante (ricerca, organizzazione, compilazione), l'umano il 10% di controllo/editing — ma quel 10% resta "indispensabile" per giudicare se l'output è buono. | "Cosa hai imparato" |
| KA-10 | Regola su dove investire il tempo umano risparmiato: i primary text li fa Claude in 5 minuti, le ore risparmiate si investono sulla sales page che richiede più cura — non tutto il tempo libero va "risparmiato", va reinvestito nel lavoro a più alto valore. | "Cosa hai imparato" |
| KA-11 | Le mega-automazioni "full AI" sono dichiarate overkill per un freelancer: producono output mediocri e richiederebbero budget da azienda strutturata per funzionare bene — posizione esplicita anti-over-engineering. | "Cosa hai imparato" |
| KA-12 | Tecnica aggiuntiva di ricerca: andare su YouTube a cercare recensioni di servizi simili per capire il linguaggio reale del target (voice-of-customer) — **questa è la TERZA occorrenza dello stesso metodo nel corso/canale** (dopo video YouTube #1 e #3 del run `andrei-pascu-001`, entrambi backfillati). | "Cosa hai imparato" |

## Connessione con Knowledge Base esistente — RILEVANTE

**KA-12 raggiunge la soglia anti-overfitting**: il metodo "ricerca voice-of-customer da recensioni YouTube" è ora confermato **3 volte indipendenti** nel materiale Andrei Pascu (video YouTube #1, video YouTube #3, e questa lezione del corso a pagamento — fonte diversa, non ripetizione dello stesso video). Vedi enrichment-report per valutazione applicazione a `copywriting/SKILL.md`.

## Gate di qualità

| Check | Status | Note |
|---|---|---|
| NO-FINTO | PASS | 38 frame visionati nativamente, prompt esatto trascritto da screenshot reale non da inferenza |
| NO-STUB | PASS | Video 27 min intero mappato (scan 60s + densificazione mirata dichiarata) |
| P12 traceability | PASS | Ogni atom pratico ha timestamp + frame |
| Dato interessante non nel testo ufficiale segnalato | PASS | KA-06 (Wispr) trovato solo a schermo, non nella panoramica scritta — dimostra valore del frame-by-frame oltre la trascrizione |

**Prossima lezione:** Lezione 14 — "Come usare la modalità co-work"
