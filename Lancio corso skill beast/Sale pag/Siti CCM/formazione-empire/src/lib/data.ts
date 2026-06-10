// ============================================================
//  MOCK DATA — Formazione Empire
//  Sostituire con dati da Supabase nella Fase 2.
// ============================================================

export type Resource = {
  id: string;
  title: string;
  type: "pdf" | "md" | "skill" | "zip" | "link";
  size?: string;
  href: string;
};

export type Lesson = {
  id: string;
  slug: string;
  title: string;
  description: string;
  longDescription: string;
  duration: number; // minutes
  videoUrl?: string;
  resources: Resource[];
  completed?: boolean;
};

export type Module = {
  id: string;
  slug: string;
  index: number;
  title: string;
  subtitle: string;
  description: string;
  lessons: Lesson[];
};

export type Course = {
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  tagline: string;
  description: string;
  cover?: string;
  owned: boolean;
  salesPageUrl?: string;
  modules: Module[];
  globalResources: Resource[];
  totalLessons: number;
  totalDuration: number;
  status?: "available" | "coming-soon";
};

// ============================================================
//  CCM — Claude Code Mastery
// ============================================================

const ccmModules: Module[] = [
  {
    id: "mod-0",
    slug: "setup-rapido",
    index: 0,
    title: "Setup Rapido & Primo Agente",
    subtitle: "Da zero al tuo primo operatore AI in 10 minuti",
    description: "Installazione guidata No-Code dell'intero ecosistema AI: Claude Code, Projects, Cowork, Perplexity, Manus. Il tuo primo operatore AI funzionante entro la fine del modulo.",
    lessons: [
      { id: "l-0-1", slug: "ecosistema", title: "L'ecosistema: Claude Code, Projects, Cowork, Perplexity, Manus", description: "Panoramica completa degli strumenti che useremo.", longDescription: "In questa lezione introduttiva facciamo una mappatura completa dell'ecosistema AI che utilizzeremo durante tutto il corso. Vedrai cos'è Claude Code, come si differenzia da Projects e Cowork, il ruolo di Perplexity e come Manus si integra nel workflow. Al termine avrai una visione chiara di quando usare ogni strumento.", duration: 12, resources: [{ id: "r1", title: "Mappa ecosistema AI (PDF)", type: "pdf", size: "2.1 MB", href: "#" }], completed: true },
      { id: "l-0-2", slug: "installazione-guidata", title: "Installazione GUIDATA (No-Code approach)", description: "Installa tutto senza scrivere una riga di codice.", longDescription: "Guida passo-passo per installare tutti gli strumenti dell'ecosistema senza necessità di competenze tecniche. Ogni comando viene spiegato nel dettaglio con screenshot e video demo. Troubleshooting dei problemi più comuni.", duration: 18, resources: [{ id: "r2", title: "Checklist installazione", type: "pdf", size: "0.8 MB", href: "#" }, { id: "r3", title: "Comandi copy-paste", type: "md", size: "12 KB", href: "#" }], completed: true },
      { id: "l-0-3", slug: "primo-operatore", title: "Il tuo primo operatore AI in 10 minuti", description: "Costruisci il tuo primo agente AI funzionante.", longDescription: "Passiamo dalla teoria alla pratica. Costruiamo insieme il tuo primo operatore AI: un assistente che analizza testi e produce report strutturati. Vedrai il potere di un singolo prompt ben strutturato.", duration: 22, resources: [{ id: "r4", title: "Template primo operatore", type: "skill", size: "4 KB", href: "#" }], completed: false },
    ],
  },
  {
    id: "mod-1",
    slug: "framework-icro",
    index: 1,
    title: "Fondamenta: Framework I.C.R.O.",
    subtitle: "Il framework per risultati deterministici con Claude",
    description: "La Lingua di Claude: impara il framework I.C.R.O. per ottenere output consistenti e professionali. Context Management avanzato e comandi per pilotare Claude con precisione chirurgica.",
    lessons: [
      { id: "l-1-1", slug: "lingua-claude", title: "La 'Lingua' di Claude: Context Mastery", description: "Come pensa Claude e come parlargli.", longDescription: "Capire come Claude processa il contesto è la differenza tra output mediocri e output eccellenti. In questa lezione smontiamo il modo in cui il modello ragiona e ti do i principi per comunicare con lui in modo ottimale.", duration: 25, resources: [{ id: "r5", title: "Guida Context Mastery", type: "pdf", size: "3.4 MB", href: "#" }], completed: false },
      { id: "l-1-2", slug: "icro", title: "Framework I.C.R.O. per risultati deterministici", description: "Input, Context, Role, Output — il sistema completo.", longDescription: "I.C.R.O. = Input, Context, Role, Output. Il framework proprietario che uso per ogni mia skill, agente e prompt professionale. Esempi pratici applicati a 5 use-case diversi.", duration: 32, resources: [{ id: "r6", title: "Framework ICRO (PDF)", type: "pdf", size: "2.8 MB", href: "#" }, { id: "r7", title: "Template ICRO compilabili", type: "md", size: "8 KB", href: "#" }], completed: false },
      { id: "l-1-3", slug: "context-management", title: "Comandi Avanzati & Context Management", description: "Slash commands, memoria, context engineering.", longDescription: "Tutti i comandi avanzati di Claude Code che fanno la differenza: /compact, /clear, /resume, memoria persistente, gestione del context window. Come evitare context rot e far lavorare Claude su task lunghi.", duration: 28, resources: [{ id: "r8", title: "Cheatsheet comandi", type: "pdf", size: "1.2 MB", href: "#" }], completed: false },
    ],
  },
  {
    id: "mod-2",
    slug: "skill-builder",
    index: 2,
    title: "Skill Builder: Sistemi Riutilizzabili",
    subtitle: "La tua libreria personale di 15+ skill AI",
    description: "L'AI come specialista: costruisci skill riutilizzabili con il framework S.K.I.L.L. Trigger proattivi, librerie custom, e la creazione della tua libreria personale di 15+ skill operative.",
    lessons: [
      { id: "l-2-1", slug: "skill-framework", title: "L'AI come specialista (Framework S.K.I.L.L.)", description: "Dallo script alla skill riutilizzabile.", longDescription: "Il salto di qualità: smettere di scrivere prompt one-shot e iniziare a costruire skill. Framework S.K.I.L.L. = Scope, Knowledge, Instructions, Limits, Links. Architettura di una skill professionale.", duration: 30, resources: [{ id: "r9", title: "Framework SKILL (PDF)", type: "pdf", size: "2.2 MB", href: "#" }], completed: false },
      { id: "l-2-2", slug: "trigger-proattivi", title: "Trigger Proattivi e Librerie Custom", description: "Skill che si attivano da sole al momento giusto.", longDescription: "Come configurare trigger proattivi affinché le skill si attivino automaticamente al rilevamento del contesto giusto. Librerie condivise, skill namespaces, gestione versioni.", duration: 26, resources: [{ id: "r10", title: "Esempi trigger", type: "md", size: "6 KB", href: "#" }], completed: false },
      { id: "l-2-3", slug: "tua-libreria", title: "Creazione della tua Libreria di 15+ Skill", description: "Costruiamo insieme 15 skill pronte all'uso.", longDescription: "Workshop completo: costruiamo 15 skill operative che puoi usare immediatamente nel tuo business. Content creation, data analysis, customer support, sales outreach, research e molto altro.", duration: 75, resources: [{ id: "r11", title: "15 Skill pronte (ZIP)", type: "zip", size: "480 KB", href: "#" }], completed: false },
    ],
  },
  {
    id: "mod-3",
    slug: "workflow-agenti",
    index: 3,
    title: "Workflow & Agenti Collaborativi",
    subtitle: "Orchestrazione multi-agente e mindset dell'architetto",
    description: "Framework W.O.R.K. per flussi multi-step. Orchestrazione di agenti in sequenziale vs parallelo. Sviluppa il mindset dell'architetto AI per progettare sistemi scalabili.",
    lessons: [
      { id: "l-3-1", slug: "work-framework", title: "Framework W.O.R.K. per flussi multi-step", description: "Da skill singole a workflow articolati.", longDescription: "Quando un task richiede più passaggi coordinati, servono i workflow. Framework W.O.R.K. = Workflow, Orchestration, Routing, Kernel. Casi d'uso reali nel business.", duration: 34, resources: [{ id: "r12", title: "Framework WORK", type: "pdf", size: "2.6 MB", href: "#" }], completed: false },
      { id: "l-3-2", slug: "orchestrazione", title: "Orchestrazione Agenti (Sequenziali vs Paralleli)", description: "Quando usare un agente solo, quando più agenti insieme.", longDescription: "Trade-off tra sequenziale e parallelo. Come distribuire task complessi su più agenti specializzati. Gestione dipendenze e sincronizzazione.", duration: 38, resources: [{ id: "r13", title: "Pattern orchestrazione", type: "md", size: "15 KB", href: "#" }], completed: false },
      { id: "l-3-3", slug: "mindset-architetto", title: "Il Mindset dell'Architetto AI", description: "Pensare in sistemi, non in prompt.", longDescription: "La transizione mentale da 'utente di AI' ad 'architetto AI'. Come progettare sistemi AI scalabili, manutenibili, e aggiornabili. Principi di software engineering applicati al prompt engineering.", duration: 22, resources: [], completed: false },
    ],
  },
  {
    id: "mod-4",
    slug: "progetti-portfolio",
    index: 4,
    title: "Progetti Reali: Il Portfolio",
    subtitle: "Tre progetti completi per il tuo portfolio professionale",
    description: "Costruiamo insieme 3 progetti reali di livello enterprise che puoi mostrare ai clienti o usare per te stesso: Content System, Report Enterprise, Business Process Automation.",
    lessons: [
      { id: "l-4-1", slug: "content-system", title: "Progetto 1: Content System Completo", description: "Sistema di content generation end-to-end.", longDescription: "Sistema AI che genera post, thread, articoli e newsletter partendo da un singolo topic. Pipeline completa con ricerca, outline, writing, editing, repurposing multi-piattaforma.", duration: 90, resources: [{ id: "r14", title: "Progetto Content System (ZIP)", type: "zip", size: "1.4 MB", href: "#" }], completed: false },
      { id: "l-4-2", slug: "report-enterprise", title: "Progetto 2: Analisi & Report Enterprise", description: "Sistema di analisi dati e report professionali.", longDescription: "Sistema AI che analizza dataset, genera insight, e produce report PDF multi-pagina di livello consulenziale. Ideale per agenzie e consulenti.", duration: 85, resources: [{ id: "r15", title: "Progetto Report Enterprise", type: "zip", size: "980 KB", href: "#" }], completed: false },
      { id: "l-4-3", slug: "automation", title: "Progetto 3: Business Process Automation", description: "Automazione processi aziendali completi.", longDescription: "Sistema che automatizza un intero processo aziendale: lead qualification, email outreach, CRM update, calendar booking, follow-up. Tutto orchestrato da agenti AI.", duration: 100, resources: [{ id: "r16", title: "Progetto BPA", type: "zip", size: "2.1 MB", href: "#" }], completed: false },
    ],
  },
  {
    id: "mod-5",
    slug: "monetizzazione",
    index: 5,
    title: "Monetizzazione & Business",
    subtitle: "Trasforma le skill in un business reale",
    description: "Come vendere le competenze appena acquisite: freelance, agenzia AI, prodotti digitali, automazioni, consulenze. Definizione offerta, pricing strategico, outreach con il Metodo D.A.N.",
    lessons: [
      { id: "l-5-1", slug: "vendere-skill", title: "Come vendere le competenze appena acquisite", description: "5 modelli di business applicabili da subito.", longDescription: "Panoramica dei 5 modelli di business più redditizi per chi sa usare Claude Code professionalmente. Pro, contro, time-to-first-money di ognuno.", duration: 28, resources: [{ id: "r17", title: "5 modelli di business (PDF)", type: "pdf", size: "1.8 MB", href: "#" }], completed: false },
      { id: "l-5-2", slug: "offerta-pricing", title: "Definizione offerta & pricing strategico", description: "Come posizionare e prezzare il tuo valore.", longDescription: "Metodologia per costruire un'offerta chiara e differenziata. Pricing strategico basato sul valore, non sul tempo. Esempi reali di offerte a 3k, 5k, 10k €.", duration: 35, resources: [{ id: "r18", title: "Template offerta", type: "md", size: "10 KB", href: "#" }], completed: false },
      { id: "l-5-3", slug: "metodo-dan", title: "Il Metodo D.A.N. per l'Outreach", description: "Messaggi di outreach che convertono davvero.", longDescription: "D.A.N. = Diagnosi, Aspirazione, Next Step. Il framework che uso per scrivere messaggi di outreach con tassi di risposta del 20%+. Template e script reali.", duration: 30, resources: [{ id: "r19", title: "Script outreach DAN", type: "pdf", size: "1.2 MB", href: "#" }], completed: false },
      { id: "l-5-4", slug: "prima-call", title: "Script di Chiusura e Prima Call con Cliente", description: "Come gestire la prima call e chiudere il deal.", longDescription: "Struttura della prima call: discovery, presentation, close. Script testati e ottimizzati. Come gestire obiezioni comuni.", duration: 32, resources: [{ id: "r20", title: "Script prima call", type: "pdf", size: "1.5 MB", href: "#" }], completed: false },
    ],
  },
  {
    id: "mod-6",
    slug: "claude-code-avanzato",
    index: 6,
    title: "Claude Code Avanzato",
    subtitle: "Sub-agenti, hook, MCP server — l'arsenale completo",
    description: "Costruzione di flussi end-to-end. Orchestrazione multi-agente su progetti complessi. Sub-agenti, hook, MCP server per estensioni custom. Tecniche avanzate di context engineering.",
    lessons: [
      { id: "l-6-1", slug: "flussi-end-to-end", title: "Costruzione di interi flussi di lavoro end-to-end", description: "Dal trigger iniziale al deliverable finale.", longDescription: "Progettazione di flussi di lavoro completi che partono da un singolo trigger (email, form, evento) e producono un deliverable finale senza intervento umano.", duration: 48, resources: [], completed: false },
      { id: "l-6-2", slug: "multi-agente-complessi", title: "Orchestrazione multi-agente su progetti complessi", description: "Quando servono 5+ agenti coordinati.", longDescription: "Scenari reali dove serve orchestrare 5, 10 o più agenti su progetti complessi. Pattern di coordinazione, shared state, checkpointing.", duration: 52, resources: [], completed: false },
      { id: "l-6-3", slug: "sub-agenti-hook-mcp", title: "Sub-agenti, hook e MCP server per estensioni custom", description: "Estendi Claude Code con tool custom.", longDescription: "Sub-agenti specializzati con tool set ristretti. Hook per automatizzare azioni su eventi. MCP server per integrare qualsiasi API o tool esterno.", duration: 55, resources: [{ id: "r21", title: "Template MCP server", type: "zip", size: "240 KB", href: "#" }], completed: false },
      { id: "l-6-4", slug: "context-engineering-advanced", title: "Tecniche avanzate di context engineering", description: "Ottimizzazione del context window per task lunghi.", longDescription: "Come mantenere Claude performante su task di ore o giorni. Context compaction strategica, memory files, checkpoint & resume patterns.", duration: 40, resources: [], completed: false },
    ],
  },
  {
    id: "mod-7",
    slug: "cowork-avanzato",
    index: 7,
    title: "Claude Cowork Avanzato",
    subtitle: "Automazione processi aziendali e web",
    description: "Automazione di qualsiasi processo aziendale. Azioni sul web (browsing, form, scraping controllato). Pipeline ibride Cowork + Projects + Perplexity + Manus.",
    lessons: [
      { id: "l-7-1", slug: "processi-aziendali", title: "Automazione di qualsiasi processo aziendale", description: "Mappa il processo e automatizzalo.", longDescription: "Metodologia per mappare un processo aziendale esistente e automatizzarlo con Cowork. Dal process mining all'implementazione.", duration: 42, resources: [], completed: false },
      { id: "l-7-2", slug: "azioni-web", title: "Automazione di azioni sul web", description: "Browsing, form, scraping controllato.", longDescription: "Come far eseguire a Claude azioni reali sul web: compilare form, estrarre dati, navigare dashboard, interagire con SaaS tools.", duration: 38, resources: [], completed: false },
      { id: "l-7-3", slug: "pipeline-ibride", title: "Pipeline ibride Cowork + Projects + Perplexity + Manus", description: "Il meglio di ogni strumento in un'unica pipeline.", longDescription: "Quando usare quale strumento. Pipeline ibride che sfruttano i punti di forza di ogni tool. Case study reali.", duration: 45, resources: [], completed: false },
      { id: "l-7-4", slug: "workflow-autoesecutivi", title: "Workflow auto-esecutivi che lavorano mentre dormi", description: "Scheduler, cron, trigger remoti.", longDescription: "Come configurare workflow che si eseguono automaticamente su schedule, eventi esterni, webhook. Il tuo business che lavora 24/7.", duration: 36, resources: [], completed: false },
    ],
  },
  {
    id: "mod-8",
    slug: "ricerca-mercato",
    index: 8,
    title: "Ricerca di Mercato",
    subtitle: "La skill più importante per il futuro",
    description: "Come leggere il mercato prima di costruire. Metodo di validazione: segnali reali di domanda vs rumore. Scovare nicchie scoperte e offerte già pagate dal mercato.",
    lessons: [
      { id: "l-8-1", slug: "cosa-funziona", title: "Come cercare sul mercato ciò che funziona DAVVERO", description: "Distinguere il rumore dai segnali.", longDescription: "Dove guardare per trovare prodotti, servizi, offerte che il mercato sta già comprando. Strumenti e fonti per la ricerca di mercato seria.", duration: 32, resources: [], completed: false },
      { id: "l-8-2", slug: "validazione", title: "Metodo di validazione: segnali reali vs rumore", description: "Come capire se c'è vera domanda.", longDescription: "Framework per validare un'idea in massimo 7 giorni. Segnali di domanda reale vs hype. Test a basso costo per validare prima di costruire.", duration: 30, resources: [], completed: false },
      { id: "l-8-3", slug: "nicchie-scoperte", title: "Scovare nicchie scoperte e offerte pagate dal mercato", description: "Dove il gold rush è ancora aperto.", longDescription: "Tecnica per trovare nicchie ancora poco presidiate ma con buona capacità di spesa. Come identificare offerte che i clienti già pagano ma sottoserviti.", duration: 28, resources: [], completed: false },
      { id: "l-8-4", slug: "leggere-mercato", title: "Leggere il mercato prima di costruire", description: "La skill che cambia la tua carriera.", longDescription: "La mentalità del market-first builder. Come smettere di costruire cose che nessuno vuole e iniziare a servire domanda esistente con offerte superiori.", duration: 35, resources: [], completed: false },
    ],
  },
];

const ccmGlobalResources: Resource[] = [
  { id: "gr1", title: "Libreria completa delle 15 Skill", type: "zip", size: "620 KB", href: "#" },
  { id: "gr2", title: "Framework I.C.R.O. — Guida Completa", type: "pdf", size: "4.2 MB", href: "#" },
  { id: "gr3", title: "Framework S.K.I.L.L. — Guida Completa", type: "pdf", size: "3.8 MB", href: "#" },
  { id: "gr4", title: "Framework W.O.R.K. — Guida Completa", type: "pdf", size: "3.6 MB", href: "#" },
  { id: "gr5", title: "Metodo D.A.N. — Script Outreach", type: "pdf", size: "2.4 MB", href: "#" },
  { id: "gr6", title: "Template Prima Call con Cliente", type: "pdf", size: "1.8 MB", href: "#" },
  { id: "gr7", title: "Cheatsheet Comandi Claude Code", type: "pdf", size: "1.2 MB", href: "#" },
  { id: "gr8", title: "3 Progetti Portfolio (codice + prompt)", type: "zip", size: "4.5 MB", href: "#" },
];

export const ccmCourse: Course = {
  id: "ccm",
  slug: "claude-code-mastery",
  title: "Da AI User a System Architect",
  subtitle: "Il sistema completo per dominare Claude Code e costruirci un business reale",
  tagline: "Il percorso completo Empire",
  description: "9 moduli, 32+ lezioni, 3 progetti portfolio, 15+ skill riutilizzabili, 8 risorse premium. Il corso più completo in italiano per trasformare Claude Code in un'arma professionale.",
  owned: true,
  modules: ccmModules,
  globalResources: ccmGlobalResources,
  totalLessons: ccmModules.reduce((acc, m) => acc + m.lessons.length, 0),
  totalDuration: ccmModules.reduce((acc, m) => acc + m.lessons.reduce((a, l) => a + l.duration, 0), 0),
  status: "available",
};

// ============================================================
//  FUTURI CORSI (vetrina)
// ============================================================

export const vetrinaCourses: Course[] = [
  {
    id: "cro",
    slug: "cro-mastery",
    title: "CRO Copy Mastery",
    subtitle: "Scrivere copy che converte — il sistema Digital Empire",
    tagline: "Il sistema di copywriting che ha generato 7 cifre",
    description: "Il framework completo di Digital Empire per scrivere sale page, email, ads e VSL che convertono davvero. Dal mindset agli script reali.",
    owned: false,
    salesPageUrl: "#",
    modules: [],
    globalResources: [],
    totalLessons: 28,
    totalDuration: 720,
    status: "coming-soon",
  },
  {
    id: "launch",
    slug: "launch-mastery",
    title: "Launch Mastery",
    subtitle: "Il playbook per lanciare e vendere prodotti digitali",
    tagline: "Da idea a primo €10k in 30 giorni",
    description: "Il sistema end-to-end per lanciare un info-prodotto: validation, offerta, funnel, sale page, ads, email sequence, community.",
    owned: false,
    salesPageUrl: "#",
    modules: [],
    globalResources: [],
    totalLessons: 24,
    totalDuration: 560,
    status: "coming-soon",
  },
];

// ============================================================
//  STUDENT MOCK (current user)
// ============================================================

export const mockStudent = {
  id: "user-1",
  name: "Massimiliano",
  email: "max.infoproducer@gmail.com",
  avatar: null,
  enrolledCourses: ["ccm"],
};

// ============================================================
//  HELPERS
// ============================================================

export function getCourse(slug: string): Course | null {
  if (slug === ccmCourse.slug) return ccmCourse;
  return vetrinaCourses.find(c => c.slug === slug) ?? null;
}

export function getModule(courseSlug: string, moduleSlug: string): { course: Course; module: Module } | null {
  const course = getCourse(courseSlug);
  if (!course) return null;
  const module = course.modules.find(m => m.slug === moduleSlug);
  if (!module) return null;
  return { course, module };
}

export function getLesson(courseSlug: string, moduleSlug: string, lessonSlug: string) {
  const res = getModule(courseSlug, moduleSlug);
  if (!res) return null;
  const lesson = res.module.lessons.find(l => l.slug === lessonSlug);
  if (!lesson) return null;
  return { ...res, lesson };
}

export function getCourseProgress(course: Course): { completed: number; total: number; percentage: number } {
  const total = course.totalLessons;
  const completed = course.modules.reduce(
    (acc, m) => acc + m.lessons.filter(l => l.completed).length, 0
  );
  return { completed, total, percentage: total === 0 ? 0 : Math.round((completed / total) * 100) };
}

export function getModuleProgress(module: Module): { completed: number; total: number; percentage: number; isDone: boolean } {
  const total = module.lessons.length;
  const completed = module.lessons.filter(l => l.completed).length;
  const percentage = total === 0 ? 0 : Math.round((completed / total) * 100);
  return { completed, total, percentage, isDone: total > 0 && completed === total };
}
