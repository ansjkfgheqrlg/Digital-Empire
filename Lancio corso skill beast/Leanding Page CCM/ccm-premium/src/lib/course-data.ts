export type Lesson = {
  id: string;
  title: string;
  duration?: string;
  type: "video" | "concept" | "tutorial" | "practice" | "framework";
  slug: string;
};

export type Module = {
  id: string;
  title: string;
  description: string;
  lessons: Lesson[];
};

export const courseData: Module[] = [
  {
    id: "0",
    title: "SETUP — IL TUO PRIMO AGENTE IN 10 MINUTI",
    description: "Configura il tuo ambiente operativo e ottieni i primi risultati concreti con Claude Code.",
    lessons: [
      { id: "0.1", slug: "perche-claude-code", title: "Perché Claude Code e Non ChatGPT", duration: "10 min", type: "concept" },
      { id: "0.2", slug: "installazione-guidata", title: "Installazione Guidata Step-by-Step", duration: "15 min", type: "tutorial" },
      { id: "0.3", slug: "primo-agente", title: "Il Tuo Primo Agente in 10 Minuti", duration: "10 min", type: "practice" },
    ],
  },
  {
    id: "1",
    title: "FONDAMENTA — PARLA LA LINGUA DI CLAUDE CODE",
    description: "Impara a dare istruzioni strutturate, gestire il contesto e configurare l'identità del tuo assistente.",
    lessons: [
      { id: "1.1", slug: "come-pensa-claude", title: "Come Pensa Claude Code", duration: "12 min", type: "concept" },
      { id: "1.2", slug: "framework-claude-md", title: "Il Framework CLAUDE.md (I.C.R.O.)", duration: "18 min", type: "framework" },
      { id: "1.3", slug: "comandi-avanzati", title: "Comandi Avanzati e Context Management", duration: "25 min", type: "practice" },
    ],
  },
  {
    id: "2",
    title: "SKILL BUILDER — CREA SISTEMI RIUTILIZZABILI",
    description: "Trasforma task ripetitivi in skill atomiche e strutturate che compongono il tuo vero asset professionale.",
    lessons: [
      { id: "2.1", slug: "cosa-e-una-skill", title: "Cos'è una Skill e Perché Cambia Tutto", duration: "12 min", type: "concept" },
      { id: "2.2", slug: "framework-skill-md", title: "Il Framework S.K.I.L.L.", duration: "22 min", type: "framework" },
      { id: "2.3", slug: "skill-avanzate", title: "Skill Avanzate: Trigger e Catene", duration: "18 min", type: "tutorial" },
      { id: "2.4", slug: "libreria-skill", title: "Costruisci la Tua Libreria di Skill", duration: "18 min", type: "practice" },
    ],
  },
  {
    id: "3",
    title: "WORKFLOW & AGENTI — ORCHESTRA SISTEMI COMPLESSI",
    description: "Passa da operatore ad architetto: progetta catene di montaggio digitali e orchestrazione di agenti.",
    lessons: [
      { id: "3.1", slug: "mindset-architetto", title: "Il Mindset dell'Architetto AI", duration: "12 min", type: "concept" },
      { id: "3.2", slug: "framework-work", title: "Il Framework W.O.R.K. per i Workflow", duration: "20 min", type: "framework" },
      { id: "3.3", slug: "primo-workflow", title: "Costruisci il Tuo Primo Workflow", duration: "15 min", type: "practice" },
      { id: "3.4", slug: "agenti-specializzati", title: "Agenti Specializzati e Orchestrazione", duration: "18 min", type: "tutorial" },
    ],
  },
  {
    id: "4",
    title: "PROGETTI REALI — COSTRUISCI IL TUO PORTFOLIO",
    description: "Applica tutto ciò che hai imparato su 3 progetti reali che dimostrano il tuo valore al mercato.",
    lessons: [
      { id: "4.1", slug: "portfolio-builder", title: "Il Portfolio dell'AI Builder", duration: "10 min", type: "concept" },
      { id: "4.2", slug: "content-system", title: "Progetto 1: Content System Automatizzato", duration: "25 min", type: "practice" },
      { id: "4.3", slug: "analisi-report", title: "Progetto 2: Analisi e Report Automatizzati", duration: "20 min", type: "practice" },
      { id: "4.4", slug: "business-automation", title: "Progetto 3: Automazione Business Process", duration: "20 min", type: "practice" },
    ],
  },
  {
    id: "5",
    title: "MONETIZZAZIONE — TRASFORMA LA SKILL IN CLIENTI",
    description: "Dalla competenza al business: crea la tua offerta, pubblica il portfolio e trova i primi clienti paganti.",
    lessons: [
      { id: "5.1", slug: "offerta-builder", title: "L'Offerta dell'AI Builder", duration: "15 min", type: "framework" },
      { id: "5.2", slug: "portfolio-online", title: "Portfolio Online in 1 Ora", duration: "18 min", type: "tutorial" },
      { id: "5.3", slug: "primi-clienti", title: "Trova i Primi 10 Clienti", duration: "22 min", type: "practice" },
      { id: "5.4", slug: "prima-call", title: "La Prima Call con il Cliente", duration: "15 min", type: "concept" },
    ],
  },
];
