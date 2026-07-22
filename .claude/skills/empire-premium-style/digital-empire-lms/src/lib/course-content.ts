export type Lesson = {
  id: string;
  slug: string;
  title: string;
  duration?: string;
  type: "video" | "practice" | "framework";
};

export type Chapter = {
  id: string;
  slug: string;
  title: string;
  description: string;
  lessons: Lesson[];
};

export const courseContent: Chapter[] = [
  {
    id: "1",
    slug: "foundations",
    title: "Chapter 1: The Empire Genome",
    description: "Decodifica il DNA estetico di Digital Empire e imposta l'architettura base.",
    lessons: [
      { id: "1.1", slug: "aesthetic-dna", title: "Decoding the Empire DNA", duration: "12 min", type: "video" },
      { id: "1.2", slug: "scaffold-mastery", title: "Advanced Next.js Scaffolding", duration: "18 min", type: "practice" },
      { id: "1.3", slug: "token-logic", title: "Design Token Architecture", duration: "15 min", type: "framework" },
    ],
  },
  {
    id: "2",
    slug: "typography-motion",
    title: "Chapter 2: Motion Economics",
    description: "Maestria nella tipografia variabile e nel controllo del movimento fluido.",
    lessons: [
      { id: "2.1", slug: "variable-fonts", title: "Variable Font Mastery", duration: "10 min", type: "video" },
      { id: "2.2", slug: "framer-orchestration", title: "Framer Motion Orchestration", duration: "25 min", type: "practice" },
      { id: "2.3", slug: "lenis-deep-dive", title: "Lenis & Scroll Interaction", duration: "20 min", type: "tutorial" as any },
    ],
  },
  {
    id: "3",
    slug: "surface-texture",
    title: "Chapter 3: Surface & Texture",
    description: "Crea profondità con grana fine, gradienti silver-mixed e glassmorphism avanzato.",
    lessons: [
      { id: "3.1", slug: "grain-science", title: "The Science of Grain Texture", duration: "12 min", type: "video" },
      { id: "3.2", slug: "silver-gradient-secrets", title: "Silver-Mixed Gradient Secrets", duration: "22 min", type: "framework" },
      { id: "3.3", slug: "texture-blending", title: "Advanced Blending Modes", duration: "15 min", type: "practice" },
    ],
  },
  {
    id: "4",
    slug: "lms-architecture",
    title: "Chapter 4: LMS Engine Building",
    description: "Progetta la navigazione a capitoli e l'esperienza di apprendimento immersiva.",
    lessons: [
      { id: "4.1", slug: "chapter-logic", title: "Recursive Chapter Navigation", duration: "18 min", type: "practice" },
      { id: "4.2", slug: "video-ux", title: "The High-Fashion Video Player", duration: "15 min", type: "video" },
      { id: "4.3", slug: "resource-stack", title: "Downloadable Resource Ecosystem", duration: "12 min", type: "framework" },
    ],
  },
  {
    id: "5",
    slug: "delivery-scaling",
    title: "Chapter 5: Scaling the Empire",
    description: "Ottimizzazione build, performance editoriali e deployment di lusso.",
    lessons: [
      { id: "5.1", slug: "performance-audit", title: "The Luxury Performance Audit", duration: "15 min", type: "practice" },
      { id: "5.2", slug: "editorial-deployment", title: "Editorial Deployment Strategies", duration: "10 min", type: "video" },
      { id: "5.3", slug: "final-mastery", title: "Final Certification & Next Steps", duration: "8 min", type: "framework" },
    ],
  },
];
