"use client";

import { Reveal } from "@/components/reveal";

const modules = [
  {
    id: "0",
    title: "Setup Rapido & Primo Agente",
    chapters: ["Perché Claude Code batte ChatGPT", "Installazione GUIDATA (No-Code)", "Il tuo primo operatore AI in 10 min"],
    tags: ["No-Code", "SetupFS"]
  },
  {
    id: "1",
    title: "Fondamenta: I.C.R.O.",
    chapters: ["La 'Lingua' di Claude: Context Mastery", "Framework I.C.R.O. deterministico", "Comandi Avanzati & Context Management"],
    tags: ["Context", "Logic"]
  },
  {
    id: "2",
    title: "Skill Builder: Sistemi riutilizzabili",
    chapters: ["L'AI come specialista (S.K.I.L.L.)", "Trigger Proattivi & Librerie Custom", "Creazione Libreria 15+ Skill"],
    tags: ["Skill.md", "Library"]
  },
  {
    id: "3",
    title: "Workflow & Agenti Collaborativi",
    chapters: ["Framework W.O.R.K. flussi multi-step", "Orchestrazione (Seq vs Parallel)", "The Architect Mindset"],
    tags: ["Agents", "Automation"]
  },
  {
    id: "4",
    title: "Progetti Reali: Portfolio",
    chapters: ["Progetto 1: Content System", "Progetto 2: Analisi Enterprise", "Progetto 3: Process Automation"],
    tags: ["Case Study", "Real World"]
  },
  {
    id: "5",
    title: "Monetizzazione & Business",
    chapters: ["Offerta & Pricing Strategico", "Il Metodo D.A.N. Outreach", "Chiusura & Prima Commessa"],
    tags: ["Business", "Sales"]
  }
];

export function MasteryMap() {
  return (
    <section className="bg-ink section section-border-t overflow-hidden">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-32">
          <Reveal>
            <span className="bubble-orange mb-6 text-[10px]">Curriculum Coorte 2026</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-5xl md:text-8xl font-black text-white mt-8 mb-8 leading-tight tracking-tighter">
              La <span className="text-silver-white">Mappa del</span> <br />
              <span className="text-silver-orange italic">Potere.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-xl text-white/50 max-w-2xl mx-auto leading-relaxed">
              Ogni nodo è un passo verso il tuo nuovo posizionamento. 21 lezioni verticali, 18 template, 4 framework.
            </p>
          </Reveal>
        </div>

        <div className="relative">
          {/* Vertical Circuit Line */}
          <div className="absolute left-[20px] md:left-1/2 top-0 bottom-0 w-[2px] bg-white/5 md:-translate-x-1/2">
            <div className="absolute top-0 bottom-0 w-full bg-gradient-to-b from-orange via-orange/50 to-orange shadow-[0_0_15px_#fb4604]" />
          </div>

          <div className="space-y-12 relative">
            {modules.map((m, i) => (
              <div key={i} className={`flex flex-col md:flex-row items-start md:items-center gap-10 md:gap-20 ${i % 2 === 0 ? "md:flex-row-reverse" : ""}`}>
                <div className="flex-1 w-full reveal">
                  <div className={`card-dark p-8 md:p-10 hover:border-orange/20 transition-all duration-500 ${i % 2 === 0 ? "md:text-right" : "md:text-left"}`}>
                    <div className={`flex items-center gap-4 mb-6 ${i % 2 === 0 ? "md:flex-row-reverse" : ""}`}>
                       <span className="text-orange font-black text-4xl italic leading-none">{m.id}</span>
                       <h3 className="text-2xl font-black text-white leading-tight uppercase tracking-tighter">{m.title}</h3>
                    </div>
                    <ul className={`space-y-3 mb-8 text-sm text-white/50 font-medium ${i % 2 === 0 ? "md:items-end flex flex-col" : ""}`}>
                      {m.chapters.map((c, j) => (
                        <li key={j} className="flex gap-3">
                          <span className="text-orange">✦</span> {c}
                        </li>
                      ))}
                    </ul>
                    <div className={`flex flex-wrap gap-2 ${i % 2 === 0 ? "md:justify-end" : ""}`}>
                      {m.tags.map((t, j) => (
                        <span key={j} className="px-3 py-1 bg-white/5 rounded-full text-[10px] uppercase font-bold text-white/30 border border-white/5">{t}</span>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="relative z-10 flex-shrink-0">
                  <div className="w-10 h-10 rounded-full bg-ink border-4 border-orange shadow-[0_0_20px_#fb4604] flex items-center justify-center">
                    <div className="w-2 h-2 rounded-full bg-orange animate-pulse" />
                  </div>
                </div>

                <div className="hidden md:block flex-1" />
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
