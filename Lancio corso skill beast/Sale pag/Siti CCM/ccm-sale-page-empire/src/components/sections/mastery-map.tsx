"use client";

import { Reveal } from "@/components/reveal";

const modules = [
  {
    n: "0",
    label: "Modulo 0",
    title: "Setup Rapido & Primo Agente",
    items: [
      "Perché Claude Code batte ChatGPT",
      "Installazione GUIDATA (No-Code approach)",
      "Il tuo primo operatore AI in 10 minuti",
    ],
  },
  {
    n: "1",
    label: "Modulo 1",
    title: "Fondamenta: framework I.C.R.O.",
    items: [
      "La \"Lingua\" di Claude: Context Mastery",
      "Framework I.C.R.O. per risultati deterministici",
      "Comandi Avanzati & Context Management",
    ],
  },
  {
    n: "2",
    label: "Modulo 2",
    title: "Skill builder: sistemi riutilizzabili",
    items: [
      "L'AI come specialista (Framework S.K.I.L.L.)",
      "Trigger Proattivi e Librerie Custom",
      "Creazione della tua Libreria di 15+ Skill",
    ],
  },
  {
    n: "3",
    label: "Modulo 3",
    title: "Workflow & Agenti Collaborativi",
    items: [
      "Framework W.O.R.K. per flussi multi-step",
      "Orchestrazione Agenti (Sequenziali vs Paralleli)",
      "Il Mindset dell'Architetto AI",
    ],
  },
  {
    n: "4",
    label: "Modulo 4",
    title: "Progetti reali: il portfolio",
    items: [
      "Progetto 1: Content System Completo",
      "Progetto 2: Analisi & Report Enterprise",
      "Progetto 3: Business Process Automation",
    ],
  },
  {
    n: "5",
    label: "Modulo 5",
    title: "Monetizzazione & business",
    items: [
      "Definizione offerta & pricing strategico",
      "Il Metodo D.A.N. per l'Outreach",
      "Script di Chiusura e Prima Call con Cliente",
    ],
  },
];

export function MasteryMap() {
  return (
    <section className="bg-grey section section-border-t" id="mastery-map">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Curriculum completo</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-black">La </span>
              <span className="text-orange-pure italic font-medium">Mappa del Potere:</span>
              <br />
              <span className="text-silver-black">all'interno di Mastery</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#3a3a3a] text-lg max-w-2xl mx-auto">
              Ogni nodo è un passo verso il tuo nuovo posizionamento. 21 lezioni verticali, 18 template scaricabili, 4 framework proprietari.
            </p>
          </Reveal>
        </div>

        <div className="space-y-0 relative">
          {modules.map((m, i) => (
            <Reveal key={i} delay={i * 0.05}>
              <div className="flex gap-6 py-10 border-b border-[#131313]/10 last:border-b-0 group">
                <div className="step-num shrink-0 group-hover:bg-orange-pure group-hover:text-white transition-colors duration-300">
                  {m.n}
                </div>
                <div>
                  <span className="text-xs font-bold uppercase tracking-[0.2em] text-orange-pure mb-2 block">
                    {m.label}
                  </span>
                  <h3 className="text-2xl md:text-3xl font-bold mb-4 text-silver-black">
                    {m.title}
                  </h3>
                  <ul className="space-y-2">
                    {m.items.map((item, idx) => (
                      <li key={idx} className="flex gap-3 text-[#3a3a3a] text-[15px]">
                        <span className="text-orange-pure mt-1">→</span>
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
