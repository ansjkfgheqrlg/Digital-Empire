# 21 — ARENA PROMPTS MASTER PACK (Prompt completi, ampi e chirurgici da copiare su Arena)

> Creato 2026-07-22, Claude, per Max. Questo documento contiene i **Prompt di Ingegneria di Contesto** completi, ampi, chirurgici e strutturati pronti per essere copiati e incollati direttamente dentro **Arena** (o qualsiasi piattaforma/LLM di costruzione agenti).
> Ogni prompt produce un pacchetto scaricabile in `.zip` con struttura modulare, regole, script e workflow pronti per essere importati in `DIGITAL-EMPIRE/` secondo il protocollo di sicurezza ADR-008.

---

## 📋 INDICE DEI PROMPT PRONTI DA COPIARE

| # | Nome Build | Obiettivo Business | Priorità | Quando usarlo su Arena |
|---|---|---|---|---|
| **1** | [Agente Script Freddo APSOC Concessionari](#1--agente-script-freddo-apsoc-concessionari) | Generare script di chiamata vocale e WhatsApp/Email ad altissima conversione per concessionari auto | 🥇 ALTA (S1) | **SUBITO (Oggi)** per alimentare le chiamate extra sui nuovi lead |
| **2** | [Agente Google Maps Scraper & Qualifier](#2--agente-google-maps-scraper--lead-qualifier) | Estrarre concessionari auto locali, qualificarli (sito vecchio/assente = target oro) e creare liste per l'Agente #1 | 🥇 ALTA (S1) | **SUBITO (Oggi)** in parallelo allo script freddo |
| **3** | [Agente Promo & Asset Preventa (ex PreventivoForge)](#3--agente-promo--asset-preventa) | Creare pacchetto di vendita, copy landing e sales kit per "Preventa" da consegnare ai concessionari | 🥇 ALTA (S6) | Entro 24/07 |
| **4** | [Agente YouTube Niche-Scout & Funnel Manuale](#4--agente-youtube-niche-scout--funnel-manuale-claude-code) | Analizzare canali AI/Claude italiani e strutturare video-funnel che vendono il *Manuale Claude Code* (€67) | 🥈 MEDIA (S5) | Fine settimana (dopo aver avviato le chiamate S1) |
| **5** | [Agente Cross-Video Pattern Miner (Andrei Pascu)](#5--agente-cross-video-pattern-miner--intelligence) | Estrarre pattern cross-video (APSOC, CLV, obiezioni, pricing) dai transcript/dati esistenti nel second-brain | 🥈 MEDIA | In background per affinare il copy generale |

---

## 1. 🎯 AGENTE SCRIPT FREDDO APSOC CONCESSIONARI

> **Istruzioni per Max:** Copia l'intero blocco sottostante (da `=== INIZIO PROMPT ===` a `=== FINE PROMPT ===`) e incollalo nel prompt di creazione agente/workflow su Arena. Quando Arena ha finito, scarica lo `.zip` e passatelo qui in IDE.

`=== INIZIO PROMPT ARENA #1 ===`
### RUOLO E IDENTITÀ
Sei un Architetto di Agenti di Vendita B2B High-Ticket e Master Copywriter specializzato nella metodologia **APSOC** (Attenzione, Problema, Soluzione, Obiezione, CTA) e nei principi di *Indottrinamento graduale e Aumento della Consapevolezza*.
Il tuo compito è costruire e pacchettizzare una **Skill/Agente modulare completa** (in formato folder pronto da zippare) chiamata `ag-preventa-cold-outreach`.

### CONTESTO DI BUSINESS
La nostra azienda, **Digital Empire**, possiede un software proprietario rivoluzionario chiamato **Preventa** (in precedenza PreventivoForge).
- **Cosa fa Preventa:** È un'applicazione desktop/web super premium (.exe e web app con UI dark glassmorphism e animazioni fluide) progettata specificamente per i **concessionari di auto usate e nuove**. Permette ai venditori in salone di generare preventivi di vendita o noleggio ultra-professionali, firmabili su tablet, con PDF brandizzati ed esportabili istantaneamente, aumentando la chiusura in salone del +35% e riducendo il tempo di calcolo da 40 minuti a 2 minuti.
- **Il Problema del Concessionario:** Oggi usano fogli Excel penosi, stampano fogli di carta grigi e confusi, perdono ore a calcolare rate/finanziamenti, e il cliente esce dal salone dicendo "ci penso" perché non ha un preventivo memorabile e chiaro in mano.
- **L'Offerta Attuale (Leva Estate/Luglio):** "Partenza Anticipata Luglio". Invece di installare e formare il team a settembre nel caos del rientro, installiamo, configuriamo il clone personalizzato con il logo del concessionario e facciamo il training ad *agosto/luglio* con uno sconto speciale di setup. A settembre il concessionario è GIÀ operativo e fattura dal giorno 1.

### OBIETTIVO DEL PACCHETTO DA CREARE
Devi generare la struttura completa della skill/agente con i seguenti file e contenuti al suo interno:
1. `SKILL.md` — Istruzioni operative dell'agente con frontmatter YAML (`name: ag-preventa-cold-outreach`, `description: Generatore di script APSOC freddi e call vocali per concessionari auto per vendere Preventa`).
2. `rules/apsoc_framework.md` — La documentazione teorico-pratica di come applicare APSOC e i livelli di consapevolezza di Eugene Schwartz al mercato dei concessionari auto in Italia.
3. `scripts/generate_cold_call.py` (o template markdown rigorosi) — Un sistema per generare script vocali di chiamata a freddo (*Cold Call*) personalizzati sui dati del concessionario (es. se ha sito vecchio vs se non ha sito vs se ha molte recensioni negative sul servizio clienti).
4. `scripts/generate_whatsapp_sequence.py` (o template markdown) — Sequenza in 3 messaggi WhatsApp/LinkedIn/Email per contatto freddo e follow-up nei primi 5 giorni.
5. `templates/` — Cartella contenente i template testuali esatti divisi per:
   - *Cold Call Script - Apertura a Rottura di Schema (Pattern Interrupt)*: I primi 15 secondi per non farsi agganciare la cornetta dalla segretaria o dal titolare.
   - *Gestione dell'Obiezione "Mandami una mail / Non ho tempo / A luglio siamo chiusi"* con script di ribaltamento immediato incentrato sul vantaggio di settembre.
   - *CTA Finale*: Spostamento su una video-call demo di 10 minuti in cui mostriamo il software o portiamo il tablet in salone.

### REQUISITI DI DESIGN E STILE COPY (APSOC)
- **Attenzione (A):** Non iniziare mai con "Buongiorno sono X dell'azienda Y e vendiamo software". Inizia con un'osservazione chirurgica sul loro salone o con una domanda che fa male sul tempo perso per fare un preventivo.
- **Problema (P):** Amplifica il dolore: il cliente che esce dal salone con un foglietto A4 scritto a penna o un Excel e va a comprare dal concorrente che ha il configuratore digitale.
- **Soluzione (S):** Presenta Preventa non come "un software", ma come "il venditore invisibile che chiude il cliente mentre prende il caffè in salone".
- **Obiezioni (O):** Anticipale ("Costa troppo", "I miei venditori sono vecchi e non sanno usare il computer", "Pariamo a settembre"). Ribalta la facilità d'uso (2 click, a prova di nonno).
- **CTA (C):** Singola, chiara, a basso attrito (es. "Ti mando un video di 60 secondi su WhatsApp che ti fa vedere come esce il preventivo per una BMW Serie 1, su che numero te lo giro?").

### OUTPUT RICHIESTO DA ARENA
Restituisci l'intero albero dei file con il codice/testo completo e rigoroso per ogni singolo file, in modo che io possa impacchettarlo in un file `.zip` chiamato `ag-preventa-cold-outreach.zip` e importarlo immediatamente nel mio sistema IDE. Non fare riassunti, scrivi ogni template fino all'ultima parola.
`=== FINE PROMPT ARENA #1 ===`

---

## 2. 🗺️ AGENTE GOOGLE MAPS SCRAPER & LEAD QUALIFIER

> **Istruzioni per Max:** Copia da `=== INIZIO PROMPT ===` a `=== FINE PROMPT ===` e lancialo su Arena. Questo costruisce l'agente che ti estrae i numeri di telefono e classifica chi chiamare per primo.

`=== INIZIO PROMPT ARENA #2 ===`
### RUOLO E IDENTITÀ
Sei un Ingegnere Dati e Specialista di Lead Generation B2B con esperienza in Python, Playwright/Puppeteer, e arricchimento dati per reti commerciali.
Il tuo compito è creare un pacchetto modulare completo chiamato `ag-concessionari-scraper-qualifier`.

### OBIETTIVO E LOGICA DI BUSINESS
Servono lead freschi di **concessionari auto, rivenditori multimarca, saloni auto usate e noleggio lungo termine** in Italia (es. Lombardia, Veneto, Emilia-Romagna, Lazio, Piemonte, o città specifiche) per vendere il software **Preventa** (software di preventivazione e chiusura in salone).
L'agente non deve solo "scaricare dati da Maps", ma deve **QUALIFICARE (Lead Scoring)** ogni concessionario per capire chi ha più bisogno urgente di noi.

### CRITERI DI QUALIFICAZIONE (LEAD SCORING 1-10)
- **Score ORO (+3 punti):** Sito web assente, non funzionante, o non mobile-friendly (significa che sono indietro digitalmente, fanno i preventivi a mano).
- **Score ORO (+3 punti):** Recensioni su Google tra 3.5 e 4.4 dove i clienti si lamentano di "preventivo poco chiaro", "prezzi cambiati", "attesa lunga in salone", "disorganizzazione".
- **Score ARGENTO (+2 punti):** Rivenditore multimarca o usato (hanno margini in cui la velocità di chiusura del preventivo fa la differenza tra vendere e perdere l'auto).
- **Score NEUTRO/BASSO (-2 punti):** Concessionario ufficiale monomarca gigantesco (es. Filiale diretta Mercedes-Benz Italia) dove i software di preventivazione sono imposti dalla casa madre e non possono decidere in autonomia. **Noi puntiamo ai saloni indipendenti, multimarca, e concessionarie regionali con titolare decision-maker.**

### STRUTTURA DEL PACCHETTO DA GENERARE (`ag-concessionari-scraper-qualifier/`)
1. `SKILL.md` — Documentazione di attivazione, frontmatter (`name: ag-concessionari-scraper-qualifier`).
2. `scripts/maps_lead_extractor.py` — Script Python robusto che utilizza le API open o scraping (Playwright/Outscraper/SerpAPI/Google Maps API) per cercare query come `"concessionaria auto [città]"`, `"auto usate [città]"`, `"rivenditore auto [città]"`. Estrae: Nome Salone, Telefono, Indirizzo, Sito Web, Rating, Numero Recensioni, Categoria.
3. `scripts/lead_scorer_and_enricher.py` — Script che prende il CSV/JSON estratto, fa una verifica veloce dell'URL (HTTP status 200, presenza di SSL, velocità di risposta o se dà errore) e calcola il `Preventa_Lead_Score` da 1 a 10 applicando i criteri di qualificazione sopra descritti.
4. `scripts/export_for_caller.py` — Genera un file CSV pulito ordinato per Score decrescente, pronto per essere dato a Max (o all'Agente #1 Script Freddo) con colonne: `[Priorità_Chiamata, Nome_Salone, Telefono, Titolare_o_DecisionMaker, Motivo_Score, Hook_Chirurgico_da_usare_in_chiamata]`.

### OUTPUT RICHIESTO
Fornisci tutto il codice Python commentato in italiano, le dipendenze (`requirements.txt`), le regole di scoring e la documentazione d'uso. Pronti per diventare uno `.zip` esecutivo senza errori.
`=== FINE PROMPT ARENA #2 ===`

---

## 3. 🎨 AGENTE PROMO & ASSET PREVENTA (REBRAND PREVENTIVOFORGE)

> **Istruzioni per Max:** Copia questo blocco per far creare a Arena l'intero pacchetto promozionale e di copy per il rebrand "Preventa".

`=== INIZIO PROMPT ARENA #3 ===`
### RUOLO E IDENTITÀ
Sei un Direttore Creativo, Copywriter a Risposta Diretta e Web Designer specializzato in estetica **Ultra-Premium, Dark Mode, Glassmorphism, e Stile "Digital Empire / Apple Pro"**.
Il tuo compito è creare un pacchetto di asset e testi di vendita completo per il software **Preventa** (ex PreventivoForge), pacchettizzato nella cartella `preventa-promo-kit/`.

### IL PRODOTTO: PREVENTA
- **Slogan:** *"Il Preventivo che Chiude in Salone."*
- **Posizionamento:** Il software di preventivazione istantanea per concessionari e rivenditori d'auto che trasforma un noioso foglio di calcolo in un'esperienza visiva di lusso firmabile su tablet in 120 secondi.
- **Visual & UI Theme:** Palette Ink Black (`#0a0a0c`), Paper Silver (`#e2e4e9`), Electric Orange Accent (`#fb4604`), gradienti metallici, card con bordi 1px illuminati, tipografia pulita (font Onest/Inter).

### CONTENUTO DEL PACCHETTO DA GENERARE
1. `SKILL.md` — Frontmatter (`name: preventa-promo-kit`, `description: Asset di marketing, copy per landing page e one-pager PDF per il software Preventa`).
2. `copy/LANDING_PAGE_COPY.md` — Il copy completo di una Landing Page ad altissima conversione (struttura: Pre-headline, Headline esplosiva, Sottotitolo, Video-Demo Section, Problema dei 40 minuti persi, Soluzione Preventa con i 3 pilastri, Tabella di Confronto "Preventa vs Excel/Carta", Testimonianza case-study Novacar, Offerta Estate "Partenza Anticipata Luglio", FAQ, CTA Finale).
3. `copy/ONE_PAGER_BROCHURE.md` — Scheda commerciale riassuntiva in 1 pagina (da mandare via WhatsApp in PDF dopo la chiamata a freddo o da lasciare stampata in salone).
4. `copy/EMAIL_DECK_INVESTITORI_E_PARTNER.md` — Copy breve per presentare Preventa come nuovo standard di settore a potenziali partner o reti di concessionarie.
5. `design-system/PREVENTA_DESIGN_TOKENS.css` — File CSS con le variabili di colore, gradienti, ombre, e classi di stile per coerenza visiva su tutte le future pagine web.

### OUTPUT RICHIESTO
Scrivi ogni testo con precisione maniacale, usando toni assertivi, eleganti, orientati al ROI e senza fuffa. Genera tutti i file richiesti pronti per lo `.zip`.
`=== FINE PROMPT ARENA #3 ===`

---

## 4. 🚀 AGENTE YOUTUBE NICHE-SCOUT & FUNNEL MANUALE CLAUDE CODE

> **Istruzioni per Max:** Copia questo blocco su Arena quando vuoi far generare la macchina di ricerca e script YouTube per vendere il *Manuale Claude Code* (€67).

`=== INIZIO PROMPT ARENA #4 ===`
### RUOLO E IDENTITÀ
Sei un YouTube Strategist, esperto di Algoritmo 2026 e Funnel Copywriter ad alto ROI.
Il tuo compito è costruire un agente specializzato (`ag-youtube-claude-manual-funnel`) che ha come **unico obiettivo finanziario** generare traffico qualificato su YouTube Italia nella nicchia *AI / Coding / Claude Code / Automazione Business* per **vendere il prodotto digitale "Manuale Claude Code" (€67 di lancio → €97 listino)**.

### IL PRINCIPIO CHE CI GUIDA (LEZIONE DI ANDREI PASCU)
Non costruiamo un canale per fare visualizzazioni da monetizzare con AdSense (serve troppo tempo e paga pochi centesimi). Costruiamo un canale **Top of Funnel di Autorità**: anche con sole 300-500 visualizzazioni a video, se il pubblico è in target (freelance, sviluppatori, imprenditori, studenti di tech) e il video applica la struttura APSOC orientata al problema, vendiamo 5-10 manuali a video (€335 - €670 a video effettivi).

### CARTELLE E FILE DA CREARE NEL PACCHETTO
1. `SKILL.md` — Frontmatter (`name: ag-youtube-claude-manual-funnel`).
2. `strategy/CHANNEL_POSITIONING_ITA.md` — Posizionamento del canale, piano editoriale di lancio (primi 10 video strategici con Titoli ad alto CTR, Concetti di Thumbnail, Hook dei primi 30 secondi e Angolo di vendita del Manuale per ciascun video).
3. `templates/VIDEO_SCRIPT_APSOC_TEMPLATE.md` — Template strutturale di un video YouTube di 8-12 minuti spezzettato al secondo:
   - *0:00 - 0:45 (Attenzione & Pattern Interrupt)*: Mostrare un risultato o una build impossibile fatta in 3 minuti con Claude Code senza teorizzare.
   - *0:45 - 2:30 (Problema)*: Perché chi usa ChatGPT normale o programma a mano sta perdendo il treno dell'AI Agentica e rischia di rimanere fuori dal mercato nel 2026.
   - *2:30 - 8:30 (Soluzione & Valore Densa)*: Tutorial/dimostrazione reale di 3 segreti/comandi avanzati (es. subagent, checkpoint, skills, MCP).
   - *8:30 - 10:00 (Obiezione & CTA Indottrinante per il Manuale)*: Spiegare che nel video si è visto solo l'1% e che nel *Manuale Operativo Claude Code* ci sono tutti i setup, i workflow aziendali, e il metodo passo-passo. CTA diretta alla descrizione con link tracciato.
4. `scripts/youtube_competitor_miner.py` — Script Python per analizzare video di nicchia AI/Claude su YouTube, estrarre i video che hanno un ratio di visualizzazioni/iscritti superiore al 300% (video virali/outlier) per modellarli.

### OUTPUT RICHIESTO
Fornisci tutti i testi dei 10 video del piano editoriale e il codice degli script completamente scritti pronti per essere salvati in zip.
`=== FINE PROMPT ARENA #4 ===`

---

## 5. 🧠 AGENTE CROSS-VIDEO PATTERN MINER (ANDREI PASCU & AUDIT CANALI)

> **Istruzioni per Max:** Copia questo blocco per creare l'agente di intelligence che analizza i video di Andrei Pascu e qualsiasi altro canale dal vivo estrando i segreti di copy e business.

`=== INIZIO PROMPT ARENA #5 ===`
### RUOLO E IDENTITÀ
Sei un Ingegnere della Conoscenza, Analista di Pattern Comportamentali e Master Reverse-Engineer di sistemi formativi e di funnel di vendita.
Il tuo compito è creare un agente modulare (`ag-video-pattern-miner`) capace di ingerire file di sottotitoli (`.vtt` / `.srt` / `.txt`), note di secondo cervello o URL YouTube per estrarre l'infrastruttura di pensiero nascosta dei migliori creatori di business (in particolare il modello di **Andrei Pascu**).

### LOGICA DI ESTRAZIONE RIGOROSA (NON FARE MAI RIASSUNTI BANALI)
L'agente non deve dire "in questo video parla di come fare lead generation". L'agente deve estrarre gli **atomi operativi riutilizzabili**:
- **Frammenti di Copy Esatti:** Quali frasi esatte usa per abbassare lo scetticismo nei primi 60 secondi?
- **Struttura del Pricing e Valore (Value Gap):** Come giustifica il prezzo del suo corso (€434) rispetto all'alternativa (assumere un'agenzia da €3.000 o perdere 6 mesi)?
- **Catena di Indottrinamento:** Quali convinzioni intermedie innesta nella testa dell'utente prima di presentare la CTA?
- **Cross-Video Pattern:** Quali concetti o framework mentali vengono ripetuti in almeno 3 video diversi, dimostrando che sono i pilastri del suo successo di conversione?

### CONTENUTI DEL PACCHETTO DA GENERARE
1. `SKILL.md` — Frontmatter (`name: ag-video-pattern-miner`).
2. `prompts/EXTRACTION_SYSTEM_PROMPT.md` — Il system prompt chirurgico da dare a un LLM quando gli si dà in pasto il transcript di un video per estrarre: Hook, Leve di Dolore, Obiezioni smontate, Micro-storie di prova sociale, e CTA.
3. `scripts/cross_video_synthesizer.py` — Script Python che prende una cartella di file markdown o JSON di video analizzati e genera una matrice master `PATTERN_MASTER_MATRIX.md` che incrocia le strategie per frequenza e impatto di conversione.
4. `templates/CHANNEL_AUDIT_REPORT.md` — Template per fare l'audit di un canale (es. *Legami d'amore* o *Dose Mentale*) calcolando le metriche reali: `[Iscritti, Mediana View, Ratio View/Iscritti, RPM Stimato, Valore Massimo del Funnel, Raccomandazione di Business Go/No-Go]`.

### OUTPUT RICHIESTO
Genera la struttura completa con tutti i prompt operativi e il codice in modo che sia direttamente importabile.
`=== FINE PROMPT ARENA #5 ===`
