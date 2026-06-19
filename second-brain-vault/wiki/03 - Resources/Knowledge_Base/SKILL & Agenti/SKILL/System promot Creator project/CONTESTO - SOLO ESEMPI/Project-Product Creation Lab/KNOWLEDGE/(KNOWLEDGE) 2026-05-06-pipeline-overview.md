# PIPELINE_OVERVIEW
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > System promot Creator project > CONTESTO - SOLO ESEMPI > Project-Product Creation Lab > KNOWLEDGE]]

## Content

# ═══════════════════════════════════════════════════════════════
# 📄 PIPELINE_OVERVIEW.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC
# Priorità: P0 — BLOCCANTE (documento fondazionale del progetto)
# Dipendenze: Nessuna — questo è il file radice
# Referenziato da: Custom Instructions — Sezione 1.2, Sezione 2.1, Sezione 2.2, Sezione 2.4, Sezione 8.1
# ═══════════════════════════════════════════════════════════════

## 📋 SCOPO

Questo file contiene la visione d'insieme completa della pipeline di produzione del Product Creation Lab. È il documento fondazionale che spiega COME funziona la fabbrica di prodotti info, quali sono le 3 fasi, come si collegano tra loro, quali input servono, quali output producono, e quanto tempo richiede ogni tipo di prodotto.

Principio fondante: "Un prodotto info non si 'scrive'. Si INGEGNERIZZA. Ha un input (brief), un processo (3 fasi), un output (prodotto finito) e un sistema di controllo qualità (quality check + beta test). Come in una fabbrica: se il processo è robusto, il prodotto è costantemente eccellente."

---

## 📖 CONTENUTO PRINCIPALE

### 1. ARCHITETTURA DELLA PIPELINE
PIPELINE DI PRODUZIONE — VISTA COMPLETA
════════════════════════════════════════

text

                ┌─────────────────────────┐
                │    INFO-BUSINESS HQ     │
                │    (Progetto 7)          │
                │                         │
                │  Decide:                │
                │  • COSA creare          │
                │  • PER CHI              │
                │  • A CHE PREZZO         │
                │  • QUANDO               │
                │                         │
                │  Output: PRODUCT BRIEF  │
                │  (idea validata, score   │
                │   ≥60, MVP positivo)    │
                └────────────┬────────────┘
                            │
                            ▼
                ┌─────────────────────────┐
                │   PRODUCT CREATION LAB  │
                │   (QUESTO PROGETTO)     │
                │                         │
                │  Decide:                │
                │  • COME costruirlo      │
                │  • CON QUALE struttura  │
                │  • A QUALE standard     │
                │                         │
                └────────────┬────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
 ┌────────────────┐ ┌──────────────┐ ┌────────────────┐
 │   FASE 1       │ │   FASE 2     │ │   FASE 3       │
 │ ARCHITETTURA   │ │ PRODUZIONE   │ │ QUALITÀ &      │
 │                │ │              │ │ PACKAGING      │
 │ • Ricerca pre- │ │ • Scrittura  │ │ • Quality      │
 │   produzione   │ │   contenuti  │ │   check        │
 │ • Learning     │ │ • Script     │ │ • Beta test    │
 │   path         │ │   video      │ │   (se ≥€97)   │
 │ • Gap          │ │ • Template   │ │ • Fix & polish │
 │   competitor   │ │   + esempi   │ │ • Delivery     │
 │ • Outline      │ │ • Esercizi   │ │   package      │
 │   dettagliato  │ │ • Design     │ │ • Documento    │
 │                │ │ • Assemblaggio│ │  handoff      │
 │ Tempo: 2-8h    │ │ Tempo: 4-80h │ │ Tempo: 1-8h   │
 │                │ │              │ │                │
 │ File KB:       │ │ File KB:     │ │ File KB:       │
 │ • RICERCA_PRE  │ │ • TEMPLATE_  │ │ • QUALITY_     │
 │   PRODUZIONE   │ │   PRODUZIONE │ │   CHECK        │
 │ • TEMPLATE_    │ │ • BRAND_     │ │ • BETA_TEST    │
 │   ARCHITETTURA │ │   VOICE_     │ │ • HANDOFF_     │
 │ • STANDARD_    │ │   PRODOTTI   │ │   LAUNCH       │
 │   QUALITA      │ │ • WORKFLOW_  │ │                │
 │                │ │   PRODUZIONE │ │                │
 └───────┬────────┘ └──────┬───────┘ └───────┬────────┘
         │                 │                  │
         │    GATE 1       │     GATE 2       │
         │  "Outline       │   "Contenuti     │
         │   approvato?"   │    completi?"    │
         │                 │                  │
         └─────────────────┴──────────────────┘
                            │
                            ▼
                ┌─────────────────────────┐
                │   LAUNCH COMMAND        │
                │   (Progetto 4)          │
                │                         │
                │  Riceve:                │
                │  • Prodotto finito      │
                │  • Delivery package     │
                │  • Documento handoff    │
                │  • Testimonial beta     │
                │  • FAQ studenti         │
                │                         │
                │  Fa:                    │
                │  • Sales page           │
                │  • Funnel di lancio     │
                │  • Email sequence       │
                │  • Webinar              │
                │  • Go-to-market         │
                └─────────────────────────┘
text


### 2. LE 3 FASI — DETTAGLIO
FASE 1: ARCHITETTURA
═════════════════════

SCOPO:
Progettare la struttura del prodotto PRIMA di
produrre una sola riga di contenuto. Come in
architettura: prima il progetto, poi la costruzione.

PERCHÉ SERVE:
├── Senza architettura → scrivi "a sentimento"
│ → il risultato è un prodotto disorganizzato
│ dove lo studente non sa dove sta andando
├── Con architettura → ogni modulo ha uno scopo,
│ ogni lezione ha un output, lo studente vede
│ il percorso dall'inizio
└── Il 70% dei prodotti info mediocri ha contenuto
buono ma STRUTTURA cattiva. La struttura fa
la differenza tra "utile" e "trasformativo".

INPUT RICHIESTO:
├── Product Brief da Info-Business HQ (P7):
│ ├── Target specifico (chi è lo studente)
│ ├── Problema che risolve (pain point principale)
│ ├── Formato scelto (PDF/Ebook/Mini-corso/Corso/Percorso)
│ ├── Fascia prezzo ipotizzata
│ └── Gap competitor identificati (almeno 3)
└── SE il brief non è disponibile → NON INIZIARE.
Torna a Info-Business HQ.

PROCESSO (4 step):

Ricerca pre-produzione
→ File: KB/RICERCA_PRE_PRODUZIONE.md
→ Output: Pain point reali, obiezioni, gap competitor

Definizione Learning Path
→ File: KB/TEMPLATE_ARCHITETTURA.md Sezione 2
→ Output: Stato PRIMA → Trasformazioni → Stato DOPO

Mappa Gap Competitor
→ File: KB/RICERCA_PRE_PRODUZIONE.md Sezione 3
→ Output: Tabella "Fanno / Non fanno / Tu farai"

Outline Dettagliato
→ File: KB/TEMPLATE_ARCHITETTURA.md Sezione 3
→ Output: Per ogni modulo: trasformazione, lezioni,
template, esercizi, checkpoint

GATE 1 — CRITERI DI APPROVAZIONE OUTLINE:
□ Ogni modulo ha UNA trasformazione chiara
□ Ogni lezione ha UN output pratico
□ L'ordine è sequenziale (modulo N richiede N-1)
□ Il learning path va da PRIMA a DOPO senza salti
□ I template previsti sono elencati con descrizione
□ Gli esercizi sono definiti con output misurabile
□ Gli standard minimi per il tipo di prodotto sono
soddisfatti (KB/STANDARD_QUALITA.md)
□ Almeno 3 gap competitor sono coperti

SE anche 1 criterio manca → l'outline NON è approvato.
Correggi prima di passare alla Fase 2.

──────────────────────────────────────────────────────

FASE 2: PRODUZIONE
══════════════════

SCOPO:
Trasformare l'outline approvato in contenuto reale:
lezioni scritte, video registrati, template creati,
esercizi progettati, tutto assemblato.

PERCHÉ SERVE SEPARARE DALLA FASE 1:
├── Se produci MENTRE progetti → riscrivi 3 volte
├── Se progetti TUTTO prima → scrivi 1 volta bene
├── L'outline è la mappa. La produzione è il viaggio.
│ Non parti senza mappa.
└── Batch production (registrare tutti i video insieme,
scrivere tutti i template insieme) è 3x più
efficiente che alternare progettazione e produzione

INPUT RICHIESTO:
├── Outline dettagliato approvato (Gate 1 superato)
├── Ricerca pre-produzione (per il linguaggio del target)
├── Brand Voice guide (per il tono di scrittura)
└── Standard per il tipo di prodotto

PROCESSO (5 step):

Scrittura contenuti (lezione per lezione)
→ File: KB/TEMPLATE_PRODUZIONE.md Sezione 1
→ Processo 6 passi: Rileggi outline → Brain dump
→ Struttura → Prima stesura → Template/Esercizio
→ Review

Produzione video (se applicabile)
→ File: KB/TEMPLATE_PRODUZIONE.md Sezione 2
→ Batch recording: tutte le lezioni talking head
in un giorno, tutti gli screen recording il giorno
dopo, editing il terzo giorno

Creazione template e materiali
→ File: KB/TEMPLATE_PRODUZIONE.md Sezione 3
→ Ogni template: Istruzioni + Template vuoto +
Esempio compilato + Criteri autovalutazione

Creazione esercizi
→ File: KB/TEMPLATE_PRODUZIONE.md Sezione 4
→ Ogni esercizio: Istruzioni step-by-step +
Input richiesto + Output atteso +
Esempio compilato + Autovalutazione

Assemblaggio prodotto
→ File: KB/TEMPLATE_PRODUZIONE.md Sezione 5
→ Caricamento piattaforma, verifica link,
welcome video, roadmap visuale, email onboarding

GATE 2 — CRITERI DI COMPLETAMENTO CONTENUTI:
□ Tutte le lezioni scritte/registrate
□ Tutti i template creati con esempio compilato
□ Tutti gli esercizi progettati con output misurabile
□ Welcome video registrato
□ Roadmap visuale del percorso creata
□ Email di onboarding scritta
□ Tutti i file scaricabili in cartella organizzata
□ Tutto caricato e funzionante sulla piattaforma

SE anche 1 criterio manca → la produzione NON è completa.
Completa prima di passare alla Fase 3.

──────────────────────────────────────────────────────

FASE 3: QUALITÀ & PACKAGING
════════════════════════════

SCOPO:
Verificare che il prodotto sia eccellente, raccogliere
feedback, fixare i problemi, e preparare tutto per
la consegna al Launch Command (P4).

PERCHÉ SERVE:
├── Un prodotto non verificato è una SCOMMESSA
│ → potresti scoprire i problemi solo dopo il lancio
│ → a quel punto i refund sono già arrivati e la
│ reputazione è già danneggiata
├── Il beta test costa 7-10 giorni
│ → Non farlo può costare MESI di danni
├── Il documento handoff è il PONTE tra chi produce
│ e chi vende. Senza handoff, il marketing non sa
│ come posizionare il prodotto
└── Il packaging (screenshot, bullet point, FAQ)
risparmia SETTIMANE di lavoro al Launch Command

INPUT RICHIESTO:
├── Prodotto assemblato e funzionante (Gate 2 superato)
├── Lista beta tester (per prodotti ≥€97)
└── Informazioni per il documento handoff

PROCESSO (4 step):

Quality Check interno
→ File: KB/QUALITY_CHECK.md
→ Checklist 5 aree: Chiarezza, Praticità,
Completezza, Qualità Tecnica, Differenziazione
→ 6 Red Flag non negoziabili

Beta Test (solo per prodotti ≥€97)
→ File: KB/BETA_TEST.md
→ 3-5 tester, 7-10 giorni, questionario 10 domande

Fix & Polish
→ Correggi problemi dal QC e beta test
→ Re-check solo sugli elementi fixati
→ Passaggio completo finale dall'inizio alla fine

Packaging & Handoff
→ File: KB/HANDOFF_LAUNCH.md
→ Delivery package + Documento handoff a Launch Command

CRITERI DI CONSEGNA FINALE:
□ Quality check superato (zero red flag)
□ Beta test completato con NPS ≥7 (se ≥€97)
□ Tutti i fix implementati
□ Delivery package completo
□ Documento handoff compilato e consegnato
□ Prodotto APPROVATO per il lancio

text


### 3. FLUSSO PER TIPO DI PRODOTTO
═══════════════════════════════════════════════════════════
TEMPI E FLUSSI PER OGNI TIPO DI PRODOTTO
═══════════════════════════════════════════════════════════

PDF GRATUITO (Lead Magnet)
───────────────────────────
Tempo totale: ~7 ore
Fase 1: 2.5h (Ricerca 1.5h + Outline 1h)
Fase 2: 3.5h (Scrittura 2.5h + Template 1h)
Fase 3: 1h (QC + Design)
Beta test: NO (è gratuito)
Complessità: ★☆☆☆☆

Contenuto tipico:
├── 8-20 pagine
├── 1 framework/sistema principale
├── 1 template/checklist inclusa
├── Design professionale
├── CTA verso prodotto successivo nella scala
└── Tempo di lettura per lo studente: 15-30 minuti

Scopo strategico:
├── Acquisire email (opt-in)
├── Dimostrare competenza ("se il gratis è così...")
├── Pre-qualificare il lead
└── Attivare il funnel (opt-in → nurture → vendita)

───────────────────────────
EBOOK (€4,99-47)
───────────────────────────
Tempo totale: ~20 ore
Fase 1: 4h (Ricerca 2h + Outline 2h)
Fase 2: 13h (Scrittura 10h + Template 3h)
Fase 3: 3h (QC 1.5h + Design 1.5h)
Beta test: OPZIONALE (consigliato se ≥€19,99)
Complessità: ★★☆☆☆

Contenuto tipico:
├── 40-80 pagine (€4,99-19,99)
├── 80-150 pagine (€19,99-47)
├── Struttura in capitoli chiari
├── Ogni capitolo = 1 concetto + 1 applicazione
├── Minimo 3 template/checklist
├── Minimo 5 esempi concreti compilati
├── Sommario + indice navigabile
└── CTA verso prodotto superiore nella scala

───────────────────────────
MINI-CORSO (€15-47)
───────────────────────────
Tempo totale: ~15 ore
Fase 1: 3h (Ricerca 1.5h + Outline 1.5h)
Fase 2: 10h (Script 4h + Registrazione 3h + Editing+Template 3h)
Fase 3: 2h (QC + Assemblaggio)
Beta test: OPZIONALE (consigliato se ≥€37)
Complessità: ★★★☆☆

Contenuto tipico:
├── 3-5 video (totale 45-90 minuti)
├── Ogni video ≤ 20 minuti (ideale: 8-12 min)
├── 1 PDF riassuntivo scaricabile
├── 1-2 template inclusi con esempio compilato
├── 1 esercizio guidato
├── Qualità audio impeccabile
└── Posizionamento: "guida pratica approfondita"
non "corso completo" (quello è il livello dopo)

───────────────────────────
CORSO COMPLETO (€97-297)
───────────────────────────
Tempo totale: ~40 ore
Fase 1: 8h (Ricerca 4h + Outline 4h)
Fase 2: 24h (Script 12h + Template/Esercizi 6h + Video 6h)
Fase 3: 8h (QC 2h + Beta test gestione 2h + Fix 3h + Packaging 1h)
Beta test: OBBLIGATORIO
Complessità: ★★★★☆

Contenuto tipico:
├── 4-6 moduli (max 7)
├── 15-30 lezioni totali
├── Ogni lezione 5-15 minuti
├── Totale video: 3-8 ore
├── Minimo 5 template scaricabili con esempio
├── Minimo 1 esercizio per modulo con autovalutazione
├── Minimo 1 esempio compilato per modulo
├── Checklist fine modulo per ogni modulo
├── PDF riassuntivo per modulo
├── Welcome video + roadmap visuale
├── Bonus: risorse extra (tool, link, letture)
└── Certificato completamento (opzionale)

───────────────────────────
PERCORSO PREMIUM (€497-997)
───────────────────────────
Tempo totale: ~70+ ore
Fase 1: 12h (Ricerca 5h + Outline 7h)
Fase 2: 45h+ (Script 20h + Template/Esercizi 10h + Video 10h + Materiali extra 5h)
Fase 3: 13h (QC 3h + Beta test 3h + Fix 5h + Packaging 2h)
Beta test: OBBLIGATORIO (con feedback più approfondito)
Complessità: ★★★★★

Contenuto tipico:
├── 6-10 moduli
├── 30-50+ lezioni totali
├── 8-15 ore di contenuto video
├── Tutto del corso completo, PIÙ:
├── Sessioni live (Q&A / coaching di gruppo)
├── Gruppo privato (community)
├── Feedback personalizzato su esercizi
├── Case study approfonditi (3+)
├── Aggiornamenti inclusi per 12 mesi
├── Supporto via email/chat
└── Percorso guidato settimana per settimana

text


### 4. RELAZIONI CON GLI ALTRI PROGETTI E SKILL
═══════════════════════════════════════════════════════════
COME PRODUCT CREATION LAB SI COLLEGA ALL'ECOSISTEMA
═══════════════════════════════════════════════════════════

PROGETTI CHE ALIMENTANO IL LAB:
────────────────────────────────
P7 — Info-Business HQ
├── Fornisce: il Product Brief (cosa creare, per chi,
│ a che prezzo)
├── Fornisce: la validazione dell'idea (score ≥60)
├── Fornisce: il positioning del prodotto nel catalogo
└── REGOLA: Il Lab NON decide cosa creare. Lo decide P7.

P6 — Marketing University
├── Fornisce: competenze e conoscenze da trasformare
│ in prodotti info
├── Il ciclo "Studia-Estrai-Applica-Valida-Insegna"
│ di P6 alimenta il contenuto dei prodotti
└── Ogni competenza validata nel lavoro con i clienti
dell'agenzia (P1) può diventare un prodotto

P1 — Agency Operations
├── Fornisce: casi studio reali, framework testati,
│ template utilizzati con i clienti
├── Il lavoro quotidiano dell'agenzia genera la
│ MATERIA PRIMA per i prodotti info
└── I playbook di handover ai clienti possono
diventare corsi self-service

PROGETTI CHE IL LAB ALIMENTA:
─────────────────────────────
P4 — Launch Command
├── Riceve: il prodotto finito + delivery package
│ + documento handoff
├── Usa: i punti di forza per il copy della sales page
├── Usa: le frasi degli studenti beta per il marketing
├── Usa: le FAQ per il webinar e la sales page
└── REGOLA: Il Lab NON lancia. Lo fa P4.

P9 — Strategy Command Center
├── Riceve: i dati di qualità (NPS, refund rate,
│ completion rate) per la dashboard
├── I KPI di qualità del prodotto influenzano
│ le decisioni strategiche
└── La product ladder (catalogo) viene aggiornata
quando un nuovo prodotto è completato

SKILL UTILIZZATE NEL LAB:
──────────────────────────
┌────────────────────────────┬────────────────────────────┐
│ Skill │ Dove viene usata │
├────────────────────────────┼────────────────────────────┤
│ Client Research Engine │ Fase 1: Ricerca pre- │
│ │ produzione (estrazione │
│ │ pain point, obiezioni) │
├────────────────────────────┼────────────────────────────┤
│ Product Pricing Strategist │ Fase 1: Conferma pricing │
│ │ (verifica che il prezzo │
│ │ sia coerente con il valore │
│ │ e il tipo di prodotto) │
├────────────────────────────┼────────────────────────────┤
│ CRO Copy Architect │ Fase 2: Copy dei materiali │
│ │ (template, esercizi, │
│ │ istruzioni ben scritte) │
├────────────────────────────┼────────────────────────────┤
│ Digital Empire Brand Voice │ Fase 2: Tono coerente in │
│ │ tutto il prodotto (lezioni,│
│ │ template, email onboarding)│
├────────────────────────────┼────────────────────────────┤
│ Email Sequence Master │ Fase 2+3: Email di │
│ │ onboarding corso + email │
│ │ di follow-up post-corso │
├────────────────────────────┼────────────────────────────┤
│ Briefing Master Pro │ Fase 3: Checklist qualità │
│ │ (approccio sistematico │
│ │ alla validazione) │
└────────────────────────────┴────────────────────────────┘

text


### 5. IL PRINCIPIO FONDAMENTALE — PRODOTTO COME BIGLIETTO DA VISITA
═══════════════════════════════════════════════════════════
PERCHÉ LA QUALITÀ DEL PRODOTTO È NON NEGOZIABILE
═══════════════════════════════════════════════════════════

UN PRODOTTO CREATO MALE:
┌──────────────────────────────────────────────────────┐
│ • Refund rate alto (>15%) → revenue perso │
│ • NPS basso → zero passaparola → niente organico │
│ • Nessun testimonial → lancio successivo difficile │
│ • Reputazione danneggiata → trust bruciata │
│ • Impossibile fare upsell → cliente non torna │
│ • Bridge verso agenzia morto → "se insegna male, │
│ perché dovrei fargli fare il mio CRO?" │
│ │
│ COSTO REALE: Non è solo il refund. │
│ È il cliente che NON comprerà MAI PIÙ da te. │
│ È il passaparola NEGATIVO che allontana 10 lead. │
│ È la testimonial che NON avrai per il prossimo │
│ lancio. │
└──────────────────────────────────────────────────────┘

UN PRODOTTO CREATO BENE:
┌──────────────────────────────────────────────────────┐
│ • Refund rate <5% → revenue solido │
│ • NPS >8 → passaparola → lead organici GRATUITI │
│ • Testimonial potenti → social proof per lanci │
│ • Autorità costruita → prezzo premium giustificato │
│ • Upsell naturale → "se il base era così buono, │
│ il premium sarà incredibile" │
│ • Bridge verso agenzia → "se insegna così bene, │
│ voglio che lo faccia LUI per me" │
│ │
│ VALORE REALE: Non è solo il revenue diretto. │
│ È il flywheel: prodotto buono → testimonial → │
│ prossimo lancio più facile → più revenue → │
│ più budget per prodotti migliori → ciclo virtuoso │
└──────────────────────────────────────────────────────┘

REGOLA FONDAMENTALE:
"Il prodotto info È il tuo biglietto da visita.
Se è mediocre, tutto il resto (marketing, funnel,
webinar) non può salvarlo.
Se è eccezionale, anche un lancio imperfetto
produce risultati."

IMPLICAZIONE PRATICA:
├── Meglio 1 prodotto eccellente che 5 mediocri
├── Meglio ritardare il lancio di 1 settimana per
│ fixare un red flag che lanciare con il red flag
├── Meglio investire 2 ore in più nella ricerca
│ pre-produzione che risparmiarne 2 e scoprire
│ dopo il lancio che il prodotto non parla il
│ linguaggio del target
└── Il beta test non è un "optional nice-to-have".
Per prodotti ≥€97, è il firewall tra successo
e disastro.

text


### 6. KPI DI QUALITÀ PRODOTTO
═══════════════════════════════════════════════════════════
METRICHE PER VALUTARE LA QUALITÀ DEI PRODOTTI
═══════════════════════════════════════════════════════════

KPI POST-LANCIO (misurati dopo il lancio):
┌─────────────────────────┬──────────┬──────────┬──────────────────┐
│ Metrica │ Target │ Soglia │ Azione se sotto │
│ │ │ critica │ soglia │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ NPS studenti │ >8/10 │ <6/10 │ Ferma, analizza │
│ │ │ │ feedback, rivedi │
│ │ │ │ contenuto │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ Refund rate │ <5% │ >10% │ Identifica moduli│
│ │ │ │ deboli, migliora │
│ │ │ │ o riscrivi │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ Completion rate │ >40% │ <20% │ Lezioni troppo │
│ (% che finisce il corso)│ │ │ lunghe? Percorso │
│ │ │ │ confuso? Analizza│
│ │ │ │ dove abbandonano │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ Testimonial raccolti │ ≥3 per │ 0 dopo │ Prodotto non │
│ per prodotto │ prodotto │ 30gg │ genera entusiasmo│
│ │ │ │ → problema qualità│
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ Tempo medio │ Entro 2x │ >3x la │ Contenuto troppo │
│ completamento │ della │ stima │ denso o poco │
│ │ stima │ │ chiaro │
└─────────────────────────┴──────────┴──────────┴──────────────────┘

KPI DI PRODUZIONE (misurati durante la creazione):
┌─────────────────────────┬──────────────────────┬──────────────┐
│ Metrica │ Target │ Cadenza │
├─────────────────────────┼──────────────────────┼──────────────┤
│ Prodotti in pipeline │ ≥2 sempre │ Mensile │
├─────────────────────────┼──────────────────────┼──────────────┤
│ Tempo brief → prodotto │ PDF: ≤1 sett │ Per prodotto │
│ finito │ Mini-corso: ≤2 sett │ │
│ │ Corso: ≤5 sett │ │
│ │ Percorso: ≤8 sett │ │
├─────────────────────────┼──────────────────────┼──────────────┤
│ Template per prodotto │ Rispetta minimo per │ Per prodotto │
│ │ tipo (STANDARD_QUALITA)│ │
├─────────────────────────┼──────────────────────┼──────────────┤
│ Ricerca pre-produzione │ 100% dei prodotti │ Per prodotto │
│ completata prima di │ │ │
│ iniziare │ │ │
├─────────────────────────┼──────────────────────┼──────────────┤
│ Beta test completato │ 100% dei prodotti │ Per prodotto │
│ per prodotti ≥€97 │ ≥€97 │ │
├─────────────────────────┼──────────────────────┼──────────────┤
│ Quality check superato │ 100% dei prodotti │ Per prodotto │
│ (zero red flag) │ │ │
└─────────────────────────┴──────────────────────┴──────────────┘

text


---

## 🔧 COME UTILIZZARE QUESTO FILE

**Quando consultarlo:**
- Quando l'utente chiede "come funziona il processo?" o "da dove inizio?"
- Quando l'utente non è chiaro su quale fase della pipeline è
- Quando serve capire le relazioni con altri progetti (P1, P4, P7, P9)
- Quando l'utente chiede i tempi stimati per un tipo di prodotto
- Quando serve ricordare i Gate (criteri di passaggio tra fasi)
- Quando l'utente mette in discussione la necessità di una fase ("posso saltare la ricerca?")

**Come integrare nella risposta:**
1. Usa la pipeline come MAPPA per orientare l'utente ("Sei nella Fase 1, step 2")
2. Usa i Gate per VERIFICARE che sia pronto a passare alla fase successiva
3. Usa i tempi stimati per PIANIFICARE il lavoro
4. Usa il principio del "biglietto da visita" quando l'utente vuole tagliare sulla qualità
5. Non citare "come da file PIPELINE_OVERVIEW" — integra naturalmente

---

## 🔗 COLLEGAMENTI

- **Alimenta**: TUTTI gli altri file della Knowledge Base (ogni file è una specifica di una parte della pipeline)
- **Dipende da**: Nessuno — è il file radice
- **Custom Instructions**: Sezione 1.2, 2.1, 2.2, 2.4, 8.1

---

## 💡 ESEMPI PRATICI

### Esempio: Orientare l'utente nella pipeline

**Situazione:** L'utente dice "Voglio creare un corso sul copywriting per e-commerce"

**Risposta tipo:**
FASE ATTUALE: Pre-Fase 1

Prima di iniziare la Fase 1 (Architettura), verifico:

□ Brief da Info-Business HQ (P7):

Target: [da definire]
Problema che risolve: [da definire]
Formato: Corso completo (hai detto "corso")
Fascia prezzo: [da definire — probabilmente €97-297]
Gap competitor: [da definire]
→ PROSSIMO STEP: Hai il brief da P7? Se sì, condividilo.
Se no, definiamo insieme: chi è lo studente ideale
di questo corso? Qual è il problema principale che
risolve? Quali competitor hai già guardato?

Una volta che abbiamo il brief, iniziamo con la
Ricerca Pre-Produzione (Fase 1, Step 1) — tempo
stimato: 4 ore.

text


---

## ⚠️ NOTE E AVVERTENZE

1. **La sequenza delle fasi NON è negoziabile.** Fase 1 → Fase 2 → Fase 3. Non si può fare la Fase 2 senza aver completato la Fase 1. Non si può fare la Fase 3 senza aver completato la Fase 2. I Gate esistono per un motivo.

2. **I tempi indicati sono STIME basate su un singolo produttore.** Se hai un team, i tempi si riducono. Se è il tuo primo prodotto, aggiungi 30-50% ai tempi (la curva di apprendimento è reale).

3. **"Prodotti in pipeline ≥2 sempre"** non significa che produci 2 contemporaneamente. Significa che mentre UN prodotto è in produzione (Fase 2), UN ALTRO è in fase di architettura (Fase 1) o in backlog pronto per iniziare. Non lavorare mai su 2 prodotti nella stessa fase contemporaneamente.

4. **Il beta test per prodotti ≥€97 non è opzionale.** È il firewall tra un prodotto mediocre e uno eccellente. I 7-10 giorni di beta test possono sembrare un "rallentamento" ma in realtà ACCELERANO il successo del lancio (meno refund, più testimonial, copy migliore basato sulle frasi degli studenti).

5. **Info-Business HQ (P7) decide COSA. Product Creation Lab decide COME.** Se ti trovi a decidere "quale prodotto creare" sei nel progetto sbagliato. Torna a P7, valida l'idea con lo Scoring Matrix, poi torna qui con il brief.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
