
import { User, AcademyCategory, AcademyModule, Badge, Quest } from './types';
import { 
  LayoutDashboard, 
  KanbanSquare, 
  BarChart3, 
  Users, 
  BookOpen,
  Instagram,
  Briefcase,
  MonitorPlay,
  HelpCircle,
  GraduationCap,
  Zap,
  Wallet,
  HardDrive,
  Trophy
} from 'lucide-react';

export const NAV_ITEMS = [
  { label: 'Dashboard', path: '/', icon: LayoutDashboard },
  { label: 'The Arena', path: '/arena', icon: Trophy },
  { label: 'Attività & Progetti', path: '/tasks', icon: KanbanSquare },
  { label: 'CRM & Vendite', path: '/crm', icon: Briefcase },
  { label: 'Finanza', path: '/finance', icon: Wallet },
  { label: 'Vault & Assets', path: '/vault', icon: HardDrive },
  { label: 'Automazioni', path: '/automations', icon: Zap },
  { label: 'Academy & Formazione', path: '/academy', icon: GraduationCap },
  { label: 'Infobusiness', path: '/infobusiness', icon: MonitorPlay },
  { label: 'Editoriale', path: '/editorial', icon: BookOpen },
  { label: 'Social Media', path: '/social', icon: Instagram },
  { label: 'Analisi', path: '/analytics', icon: BarChart3 },
  { label: 'Team', path: '/team', icon: Users },
  { label: 'Guida Piattaforma', path: '/guide', icon: HelpCircle },
];

export const MOCK_USERS: User[] = [
  {
    id: 'u1',
    name: 'Maximilian',
    role: 'ADMIN',
    title: 'Founder & CEO',
    tags: ['Strategia', 'Controllo Totale', 'Management'],
    xp: 12500,
    level: 42
  },
  {
    id: 'u2',
    name: 'Gael',
    role: 'MEMBER',
    title: 'Specialista Automazioni',
    tags: ['Automazioni', '5 Pagine IG', 'Tech Stack'],
    xp: 8400,
    level: 28
  },
  {
    id: 'u3',
    name: 'Neri',
    role: 'MEMBER',
    title: 'Responsabile Editoriale',
    tags: ['Scrittura Libri', 'Creazione PDF', '5 Pagine IG'],
    xp: 6200,
    level: 21
  },
  {
    id: 'u4',
    name: 'Leonardo',
    role: 'MEMBER',
    title: 'Brand Face & Creator',
    tags: ['Video Content', 'Infobusiness', 'Public Speaking'],
    xp: 9100,
    level: 30
  },
  {
    id: 'u5',
    name: 'Giulia (Cliente)',
    role: 'CLIENT',
    title: 'CEO @ Digital Spa',
    tags: ['VIP', 'Retainer', 'Client Portal'],
    xp: 0,
    level: 1,
    accessCode: '1234' // CLIENT ACCESS CODE
  }
];

export const INITIAL_KPI = [
  { label: 'Fatturato (MRR)', value: '€0', trend: 0, trendLabel: 'Nessun dato', icon: 'dollar' },
  { label: 'Lead Attivi', value: '0', trend: 0, trendLabel: 'Nessun dato', icon: 'users' },
  { label: 'Task Pendenti', value: '0', trend: 0, trendLabel: 'Nessun dato', icon: 'activity' },
  { label: 'Prodotti Info', value: '0', trend: 0, trendLabel: 'Nessun dato', icon: 'book' },
];

// --- MOCK LEADS DATA WITH HISTORY ---
export const SEED_LEADS_HISTORY = [
    {
        id: 'act-1',
        type: 'SYSTEM',
        content: 'Lead creato nel sistema',
        date: new Date().toISOString(),
        author: 'System'
    },
    {
        id: 'act-2',
        type: 'STATUS_CHANGE',
        content: 'Stato cambiato da NEW a CONTACTED',
        date: new Date().toISOString(),
        author: 'Maximilian'
    }
];

// --- GAMIFICATION DATA ---
export const MOCK_BADGES: Badge[] = [
    { id: 'b1', title: 'Closer', description: 'Hai chiuso 5 deal consecutivi.', icon: 'Award', rarity: 'EPIC', earnedDate: '2024-02-15' },
    { id: 'b2', title: 'Speed Demon', description: 'Completato 10 task in 24h.', icon: 'Zap', rarity: 'RARE', earnedDate: '2024-03-01' },
    { id: 'b3', title: 'Architect', description: 'Creato il primo Funnel.', icon: 'Layout', rarity: 'COMMON', earnedDate: '2024-01-20' },
    { id: 'b4', title: 'Aureus Elite', description: 'Raggiunto il livello 40.', icon: 'Diamond', rarity: 'LEGENDARY' },
];

export const DAILY_QUESTS: Quest[] = [
    { id: 'q1', title: 'Focus Operativo', description: 'Completa 5 Task ad alta priorità.', progress: 2, total: 5, rewardXp: 500, isCompleted: false, type: 'DAILY' },
    { id: 'q2', title: 'Pipeline Hunter', description: 'Sposta 2 Lead in fase di Negoziazione.', progress: 1, total: 2, rewardXp: 800, isCompleted: false, type: 'DAILY' },
    { id: 'q3', title: 'Content Machine', description: 'Pianifica 3 post Social.', progress: 3, total: 3, rewardXp: 300, isCompleted: true, type: 'DAILY' },
];

// --- DOCUMENTATION STRUCTURE ---

export const INITIAL_ACADEMY_CATEGORIES: AcademyCategory[] = [
  { 
    id: 'cat-hq', 
    title: 'Mappa Organizzativa (HQ)', 
    description: 'DIGITAL EMPIRE: Struttura dei progetti, Chat GPT personalizzati e flussi di lavoro.',
    icon: 'Brain',
    color: 'text-white'
  },
  { 
    id: 'cat-ecom', 
    title: 'UGC & Video Ads AI', 
    description: 'Protocollo completo per creare video e-commerce che vendono con Arcads, Scripting e Montaggio.',
    icon: 'ShoppingCart',
    color: 'text-purple-400'
  },
  { 
    id: 'cat-sales', 
    title: 'Storytelling & Copywriting', 
    description: 'Guida completa alla narrazione per Email, VSL e Webinar. Psicologia della vendita.',
    icon: 'BookOpen',
    color: 'text-emerald-400'
  },
  { 
    id: 'cat-info', 
    title: 'Webinar & Funnel System', 
    description: 'Architettura del Funnel Unico e Scripting del Webinar Milionario.',
    icon: 'MonitorPlay',
    color: 'text-diamond-400'
  },
  { 
    id: 'cat-yt', 
    title: 'YouTube Automation', 
    description: 'Creazione canali Faceless, ricerca nicchia e script virali automatizzati.',
    icon: 'PlayCircle', // Youtube Red
    color: 'text-red-500'
  },
  { 
    id: 'cat-kdp', 
    title: 'Amazon KDP', 
    description: 'Self-publishing su Amazon: Ricerca keyword, creazione interni e lancio libri.',
    icon: 'Book', // Amazon Orange
    color: 'text-orange-400'
  },
  { 
    id: 'cat-sales-mastery', 
    title: 'Vendita', 
    description: 'Tecniche avanzate di negoziazione, gestione obiezioni e chiusura deal high-ticket.',
    icon: 'DollarSign', // Gold
    color: 'text-yellow-500'
  }
];

export const INITIAL_ACADEMY_MODULES: AcademyModule[] = [
  
  // --- 1. MAPPA ORGANIZZATIVA (HQ) ---
  {
    id: 'mod-hq-structure',
    categoryId: 'cat-hq',
    title: 'STRUTTURA PROGETTI CHATGPT',
    description: 'Come organizzare le chat e i progetti per la massima efficienza.',
    lessons: [
      {
        id: 'les-hq-strat',
        moduleId: 'mod-hq-structure',
        title: 'Progetto 1: DE_STRATEGY_HQ',
        type: 'TEXT',
        durationMinutes: 10,
        isCompleted: false,
        content: `# PROGETTO 1: DE_STRATEGY_HQ (Strategia & Direzione)

Questo è il cervello dell'azienda. Qui si prendono le decisioni di alto livello.

### Chat 1: Visione & KPI
*   Definizione obiettivi numerici.
*   Priorità mensili.
*   Focus del periodo.

### Chat 2: Roadmap Pilastri di Business
*   Pianificazione macro per: YouTube, KDP, Instagram, eCommerce, Trading, Agency.

### Chat 3: Framework Storytelling & Webinar
*   Struttura dei webinar.
*   Script VSL (Video Sales Letter).
*   Presentazioni Canva.
*   Script "uno-a-molti".

### Chat 4: Architettura Funnel Unico
*   Definizione e aggiornamento del funnel: PDF -> VSL -> Webinar -> Servizio.

### Chat 5: Decisioni Strategiche Veloci
*   Confronto idee.
*   Test di nuove opportunità.
*   Scelta priorità operative del mese.`
      },
      {
        id: 'les-hq-ops',
        moduleId: 'mod-hq-structure',
        title: 'Progetto 2: DE_OPERATIONS_CONTENT',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# PROGETTO 2: DE_OPERATIONS_CONTENT (Operatività)

Qui avviene la produzione pratica per YouTube, IG, KDP, eCommerce.

### Chat 1: YouTube Lab
*   Analisi competitor.
*   Scelta video da "copiare" (modellare).
*   Titoli, descrizioni, tag SEO/GEO.

### Chat 2: Instagram Theme Pages Lab
*   Idee caroselli/reel.
*   Caption, hashtag.
*   Script brevi (short form).
*   Posizionamento pagina.

### Chat 3: KDP Books Lab
*   Struttura libri.
*   Outline capitoli.
*   Richieste al GPT "Book Writer".
*   Ottimizzazione SEO Amazon.

### Chat 4: eCommerce & UGC Video Lab
*   Script UGC.
*   Storyboard video vendita.
*   Idee offerte per singolo prodotto.

### Chat 5: Trading/Crypto & Agency Ops
*   Comunicazione canali trading.
*   Copy per sala segnali.
*   Copy per servizi Agency.

### Chat 6: Operatività Giornaliera
*   To-do giornalieri per te, Neri e Gael.
*   Riepilogo task.
*   Micro-piani di lavoro.`
      },
      {
        id: 'les-hq-info',
        moduleId: 'mod-hq-structure',
        title: 'Progetto 3: DE_INFOBUSINESS',
        type: 'TEXT',
        durationMinutes: 10,
        isCompleted: false,
        content: `# PROGETTO 3: DE_INFOBUSINESS (Solo InfoBusiness)

Gestione specifica di corsi, PDF, webinar ed eventi.

### Chat 1: Funnel InfoBusiness Master
*   Costruzione e aggiornamento del funnel completo (PDF, corsettino, webinar, upsell).

### Chat 2: Script Formazione & Moduli Corso
*   Struttura dei corsi.
*   Lezione per lezione.
*   Script video, esercizi, workbook.

### Chat 3: Email Marketing & Storytelling
*   Sequenze email (benvenuto, pre-webinar, post-webinar).
*   Nurture settimanale.

### Chat 4: Sales Page & VSL InfoBusiness
*   Testi per landing page.
*   Headline, bullet points, CTA.
*   Scaletta VSL e slide Canva.

### Chat 5: Lanci & Eventi
*   Piani di lancio.
*   Calendari promozione.
*   Script per storie/shorts che spingono il funnel.`
      },
      {
        id: 'les-hq-gpts',
        moduleId: 'mod-hq-structure',
        title: 'GPT Personalizzati (Strumenti)',
        type: 'TEXT',
        durationMinutes: 5,
        isCompleted: false,
        content: `# GPT PERSONALIZZATI

Questi GPT non sostituiscono i progetti, li supportano. Li usi dentro le chat quando serve "potenza speciale".

### GPT_1 – Workflow Architect (AUTOMAZIONI & CODICE)
*   **Ruolo:** Progettare e scrivere workflow n8n, Zapier, Make. Disegnare architetture di automazione.
*   **Dove lo usi:** Progetto 1 (Chat 4), Progetto 2 (Chat 6), Progetto 3 (Chat 1 e 3).

### GPT_2 – KDP Master Book Writer (SCRITTURA LIBRI)
*   **Ruolo:** Specializzato in libri Amazon KDP. Scrittura capitoli lunghi, dettagliati e coerenti.
*   **Dove lo usi:** Progetto 2, Chat 3 (KDP Books Lab). Tu fai la ricerca, lui scrive.

### GPT_3 – Ad Strategist / Media Buyer (ADV)
*   **Ruolo:** Pensare e scrivere campagne pubblicitarie (Meta, TikTok, YouTube). Definire angoli, audience, offerte.
*   **Dove lo usi:** Progetto 2 (Chat 2 e 4) per ads di crescita e prodotto.`
      }
    ]
  },

  // --- 2. E-COMMERCE & UGC ---
  {
    id: 'mod-ugc-mastery',
    categoryId: 'cat-ecom',
    title: 'PROTOCOLLO UGC & VIDEO ADS',
    description: 'Guida operativa per creare video che vendono con AI e Psicologia.',
    lessons: [
      {
        id: 'les-ugc-prep',
        moduleId: 'mod-ugc-mastery',
        title: 'Step 1: Cosa devi avere pronto',
        type: 'TEXT',
        durationMinutes: 10,
        isCompleted: false,
        content: `# Cosa devi avere pronto (prima di aprire i siti)

### 1. Scheda prodotto (anche grezza):
*   Nome prodotto
*   3 benefici principali
*   Problema che risolve
*   Target (es. "donne 25-40, pelle secca")

### 2. 1 Script di base (20-30 secondi):
*   Hook
*   Problema
*   Soluzione = Prodotto
*   Benefici
*   CTA

### 3. Account necessari:
*   ChatGPT (già ce l'hai)
*   Arcads (registrazione base)
*   CapCut desktop o mobile (per montaggio finale)`
      },
      {
        id: 'les-ugc-script',
        moduleId: 'mod-ugc-mastery',
        title: 'Step 2: Generare lo Script (Prompt)',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Generare lo script con ChatGPT (super rapido)

1.  Apri ChatGPT.
2.  Incolla queste info: descrizione prodotto, target, problema.
3.  **Usa questo PROMPT esatto:**

> "Scrivimi uno script breve per un video UGC di massimo 30 secondi per vendere questo prodotto [incolla].
> Struttura: hook forte (prima frase), problema, soluzione (il prodotto), 2-3 benefici concreti, chiusura con 'Link in bio / clicca qui sotto'.
> Tono: naturale, come una ragazza che parla in camera e racconta la sua esperienza."

4.  Copia lo script che ti piace di più in un file testo.`
      },
      {
        id: 'les-ugc-arcads',
        moduleId: 'mod-ugc-mastery',
        title: 'Step 3: Creare il video in Arcads',
        type: 'TEXT',
        durationMinutes: 20,
        isCompleted: false,
        content: `# Creare il video AI UGC dentro Arcads (passo per passo)

### 2.1. Entrare e creare il progetto
*   Vai su Arcads -> Dashboard -> "Create project".

### 2.2. Scegliere il tipo di attore (AI actor)
*   Cerca la sezione "Sora 2 actors" (o "See more").
*   Scegli **"Sora 2 Actors"** o **"Sora 2 Pro"**.
*   Filtra e scegli l'attore giusto per il tuo target (es. ragazza 25-30 anni, pelle pulita, camera da letto).

### 2.3. Impostare l'audio: SPEECH-TO-SPEECH (Consigliato)
**Questa è la parte chiave.**
1.  Seleziona "Speech to Speech".
2.  Clicca "Record new" o "Start recording".
3.  **Leggi lo script con tono naturale**, come se parlassi a un'amica. Ritmo normale, un po' di energia.
4.  Se soddisfatto, clicca "Use this recording".
*Arcads userà il tuo audio come base, ma lo farà parlare con la bocca dell'attore AI.*

### 2.4. Impostare scena e prompt video
Nel box "Prompt" / "Scene description", scrivi in INGLESE.
*Esempio:*
"Vertical 9:16 video. Natural UGC style, filmed with an iPhone. Young woman, 25 years old, sitting in her bedroom next to a window with soft daylight. She holds a face moisturizer in her hand, shows the texture, applies it on her face, smiles. Soft, cozy background, blurred. Realistic lighting, no over-saturated colors."`
      },
      {
        id: 'les-ugc-edit',
        moduleId: 'mod-ugc-mastery',
        title: 'Step 4: Montaggio CapCut (Checklist)',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Montaggio veloce in CapCut (Testo + CTA + Logo)

Il video di Arcads è "quasi pronto", va rifinito.

### 1. Testo HOOK (primi 3 secondi)
*   Clicca su "Text" -> "Add text".
*   Scrivi una frase breve tipo: *"Non comprare nessun [categoria] finché non hai visto questo."*
*   Mettilo in alto o al centro, grande, leggibile.

### 2. Benefici come micro-bullet
*   In momenti chiave (mentre mostra il prodotto).
*   Aggiungi testo breve: "+ pelle più idratata", "+ zero aloni".

### 3. CTA Finale
*   Ultimi 2-3 secondi.
*   Testo grande: "Link in bio" o "Scopri di più qui sotto".

### 4. Logo / Nome Brand
*   Importa PNG del logo.
*   Mettilo in un angolo per tutta la durata.

**Export:** 1080x1920, 30fps, MP4.`
      },
      {
        id: 'les-ugc-structure',
        moduleId: 'mod-ugc-mastery',
        title: 'Struttura Base Video Vincente',
        type: 'TEXT',
        durationMinutes: 10,
        isCompleted: false,
        content: `# STRUTTURA BASE DI UN VIDEO VINCENTE (UGC / CREATOR / AI)

Quasi tutti i video che funzionano seguono questa struttura:

1.  **Hook (0-3 secondi):** Bloccare l'attenzione.
2.  **Empatia + Problema:** "So esattamente cosa stai vivendo".
3.  **Soluzione = Prodotto:** Introduzione naturale del prodotto.
4.  **Dimostrazione / Uso Reale:** Il prodotto in azione.
5.  **Benefici + Prove:** Cosa cambia davvero nella vita di chi lo usa.
6.  **Gestione Obiezioni:** Tempo, soldi, fiducia.
7.  **CTA Finale:** Cosa deve fare SUBITO chi guarda.`
      }
    ]
  },

  // --- 3. STORYTELLING ---
  {
    id: 'mod-story',
    categoryId: 'cat-sales',
    title: 'GUIDA COMPLETA STORYTELLING',
    description: 'Manuale operativo per usare le storie in Email, VSL e Webinar.',
    lessons: [
      {
        id: 'les-story-7blocks',
        moduleId: 'mod-story',
        title: 'I 7 Blocchi Narrativi',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Struttura Universale della Storia (I 7 Blocchi)

1.  **Contesto:** Dove siamo, chi è il protagonista, in che situazione si trova.
2.  **Desiderio:** Cosa vuole davvero (anche se non lo dice ad alta voce).
3.  **Conflitto:** Cosa glielo impedisce? Errori, paure, limiti, ambiente.
4.  **Tentativi falliti:** Cosa ha già provato che non ha funzionato (o ha peggiorato le cose).
5.  **Punto di svolta:** Nuova consapevolezza, incontro, metodo, evento che cambia la direzione.
6.  **Soluzione + Applicazione:** Entra in gioco il tuo metodo/prodotto e il protagonista lo applica.
7.  **Trasformazione + Morale + CTA:** Com'è cambiata la vita e cosa deve fare ora chi legge.`
      },
      {
        id: 'les-story-email',
        moduleId: 'mod-story',
        title: 'Storytelling nelle Email',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Storytelling nelle EMAIL

### Schema operativo per una email-storia

**1. Oggetto = Hook narrativo**
*   Deve sembrare l'inizio di una storia, non una promo.
*   *Esempi:* "La sera in cui ho quasi mollato tutto", "Perché Marco ha cancellato il carrello".

**2. Riga di apertura: entra in scena**
*   Una frase concreta, visiva.
*   "Ero seduto in cucina, il portatile aperto e il conto in banca quasi a zero."

**3. Contesto + Desiderio**
**4. Conflitto + Tentativi falliti**
**5. Punto di svolta**
**6. Soluzione + Applicazione pratica** (mostra la nuova logica senza spiegare tutti i dettagli tecnici).
**7. Trasformazione + Ponte verso il lettore + CTA** (Link alla VSL o Webinar).`
      },
      {
        id: 'les-story-vsl',
        moduleId: 'mod-story',
        title: 'Storytelling nelle VSL',
        type: 'TEXT',
        durationMinutes: 20,
        isCompleted: false,
        content: `# Storytelling nelle VSL (Video Sales Letter)

La VSL è una storia lunga che integra educazione e vendita.

### Struttura base (Blueprint)
1.  **Hook (0-20s):** Frase forte che tocca un problema o un desiderio.
2.  **Grande promessa + chi è il video per:** "In questo video ti mostro... Se sei [target]..."
3.  **Posizionamento personale con storia breve:** Origin Story compressa.
4.  **I 3 Pilastri / Segreti del metodo.**
5.  **Wall of proof:** 3-5 mini storie/casi studio veloci.
6.  **Transizione all'offerta con storia:** "A questo punto avevo due scelte..."
7.  **Pitch + CTA.**`
      },
      {
        id: 'les-story-webinar',
        moduleId: 'mod-story',
        title: 'Storytelling nei Webinar',
        type: 'TEXT',
        durationMinutes: 25,
        isCompleted: false,
        content: `# Storytelling nei WEBINAR

Il webinar è una VSL espansa, con più energia live.

**Macro struttura:**
1.  Intro + Grande Promessa.
2.  Per chi è + regole del gioco.
3.  **Tua Origin Story estesa:** Qui la racconti più lunga (Contesto, Desiderio, Conflitto profondo, Punto di svolta).
4.  **3 Segreti / Pilastri + Storie:** Per ogni segreto, usa una storia (cliente o tua) per dimostrarlo.
5.  Wall of proof + casi studio.
6.  Storia del programma (come l'hai creato).
7.  Pitch + gestione obiezioni con storie.
8.  Closing + Q&A.`
      }
    ]
  },

  // --- 4. WEBINAR & FUNNEL ---
  {
    id: 'mod-webinar',
    categoryId: 'cat-info',
    title: 'IL WEBINAR MILIONARIO',
    description: 'Script completo e struttura per presentazioni ad alta conversione.',
    lessons: [
      {
        id: 'les-web-promise',
        moduleId: 'mod-webinar',
        title: '1. La Grande Promessa',
        type: 'TEXT',
        durationMinutes: 10,
        isCompleted: false,
        content: `# La Grande Promessa (Idea centrale del webinar)

Domanda da farti: *"Qual è la grande promessa che voglio fargli credere?"*

**Nel nostro caso (Instagram Theme Page):**
"Se il mio pubblico crede davvero che usare pagine tema su Instagram, automatizzate con l'AI, è tutto ciò che li separa dal creare un'entrata extra stabile, allora tutte le altre obiezioni perdono importanza."

**Esempio di Titolo:**
"Come costruire pagine Instagram che ti generano entrate automatiche in 90 giorni usando l'AI (anche se parti da zero e non vuoi metterci la faccia)"

**Apertura Live:**
"Ragazzi, benvenuti a questo webinar. Oggi vi mostrerò, passo passo, tutto quello che vi serve per capire come costruire e far crescere pagine tema su Instagram..."`
      },
      {
        id: 'les-web-story',
        moduleId: 'mod-webinar',
        title: '2. Storia e Posizionamento',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Posizionamento personale ("Chi sono io per dirti questo?")

**Esempio narrazione:**
"Oggi magari mi vedete così: gestisco più pagine tema, alcune in Italia, altre internazionali... Ma non è sempre stato così."

**Il "Prima":**
"Qualche anno fa ero esattamente dalla parte opposta: lavoravo tante ore, a fine mese rimaneva poco o niente..."

**Il Punto di Svolta:**
"Il punto di svolta è arrivato quando ho scoperto due cose semplici:
1. Non devo essere un personaggio pubblico per guadagnare con Instagram.
2. Posso usare l'AI per creare contenuti senza impazzire."

**La Storia di "Marco" (Caso Studio):**
Racconta la storia di un cliente/studente che rappresenta il target. "Marco lavorava in un bar... Dopo 30 giorni la pagina aveva qualche migliaio di follower... Dopo 60 giorni il primo link affiliato."`
      },
      {
        id: 'les-web-3secrets',
        moduleId: 'mod-webinar',
        title: '3. I 3 Segreti',
        type: 'TEXT',
        durationMinutes: 20,
        isCompleted: false,
        content: `# I 3 Segreti del Metodo

**Segreto 1 - Il Veicolo (La Nuova Opportunità)**
"Non ti serve essere influencer, ti serve una pagina tema con un posizionamento chiaro."
*Smonta l'obiezione:* Non voglio metterci la faccia.
*Storia:* Sara, la segretaria che ha aperto una pagina sul benessere femminile.

**Segreto 2 - La Fattibilità (Internal Belief)**
"Ti bastano 30-45 minuti al giorno se hai esattamente dove mettere le mani."
*Smonta l'obiezione:* Non ho tempo.
*Storia:* Luca, magazziniere con turni massacranti, usava l'AI per preparare i contenuti in anticipo.

**Segreto 3 - Le Risorse (External Belief)**
"Puoi farlo ovunque tu sia, anche con poco tempo, poco budget e una vita incasinata."
*Smonta l'obiezione:* Non ho soldi / la mia vita è un casino.
*Storia:* Imprenditore che spendeva 300€ in cene fuori e li ha riallocati.`
      },
      {
        id: 'les-web-offer',
        moduleId: 'mod-webinar',
        title: '4. Pitch e Offerta',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Transizione all'offerta (Chiedere permesso)

"Quello che avete visto oggi è solo il 10% di quello che c'è dietro un sistema completo... Per questo ho preparato qualcosa di specifico per chi non vuole solo 'capire', ma vuole implementare davvero.
**Vi va se nei prossimi minuti vi mostro il percorso completo che ho creato per aiutarvi?**"

(Aspetti il "Sì" in chat)

**Struttura Offerta:**
1.  Riepilogo benefici.
2.  Contenuto (moduli, lezioni, accessi).
3.  Bonus (Checklist, Template, Community).
4.  Garanzia (Soddisfatto o rimborsato).
5.  Urgenza (Posti limitati / Bonus scadenza).
6.  **CTA Chiara:** Link in chat.`
      }
    ]
  },
  {
    id: 'mod-funnel-arch',
    categoryId: 'cat-info',
    title: 'ARCHITETTURA FUNNEL UNICO',
    description: 'La struttura tecnica definitiva per vendere servizi high-ticket.',
    lessons: [
      {
        id: 'les-funnel-steps',
        moduleId: 'mod-funnel-arch',
        title: 'I Passaggi del Funnel',
        type: 'TEXT',
        durationMinutes: 15,
        isCompleted: false,
        content: `# Funnel Unico Perfetto - Versione Definitiva

**Obiettivo:** Vendere un servizio/percorso premium presentato nel webinar.

### 1. Opt-in PDF Gratuito (Entrata)
*   Pagina semplice, senza VSL.
*   Headline forte sul beneficio del PDF.
*   Form: Nome, Email.

### 2. Pagina Upsell Mini-Corso (€15)
*   Si apre SUBITO dopo l'opt-in.
*   Messaggio: "Il tuo PDF sta arrivando... nel frattempo guarda questo."
*   VSL basso ticket.
*   Obiettivo: Liquidare le ads (Self-liquidating offer).

### 3. Pagina VSL Evento/Webinar
*   Sia chi compra il mini-corso, sia chi no, finisce qui.
*   VSL principale: "Iscriviti al webinar gratuito".

### 4. Webinar Perfetto
*   Giorno X dell'evento.
*   Presentazione del servizio premium.

### 5. Follow-up
*   Telefono/WhatsApp per chiudere i dubbiosi.`
      },
      {
        id: 'les-funnel-email',
        moduleId: 'mod-funnel-arch',
        title: 'Regole Email & Nurturing',
        type: 'TEXT',
        durationMinutes: 10,
        isCompleted: false,
        content: `# Regole Email - Struttura Generale

**1. Email di benvenuto (Subito)**
*   Oggetto: "Benvenuto in [Brand] + il tuo PDF".
*   Consegna valore e indottrina.

**2. Chi è iscritto al Webinar: 1 Email al giorno**
*   Storytelling (persone bloccate che hanno sbloccato la situazione).
*   Casi studio concreti.
*   "Mancano X ore".

**3. Chi NON è iscritto al Webinar**
*   Riceve 1 email ogni 7 giorni (Nurture settimanale).
*   Valore reale, link a video YouTube, inviti soft al prossimo webinar.`
      }
    ]
  }
];
