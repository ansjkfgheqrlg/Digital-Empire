"use client";

import { Reveal } from "@/components/reveal";

const levels = [
  {
    lv: 1,
    t: "AI Consumer",
    d: "Usi i prompt passivamente. Sei alla mercé del modello. Se Claude non capisce, ti fermi.",
    status: "Base",
  },
  {
    lv: 2,
    t: "AI Orchestrator",
    d: "Sai concatenare più tool, ma il sistema è fragile. Un bug e tutto il workflow crolla.",
    status: "Intermedio",
  },
  {
    lv: 3,
    t: "System Architect",
    d: "Costruisci sistemi deterministici. Agenti, Skill e MCP. L'AI lavora per te, non il contrario.",
    status: "Target Empire",
    premium: true,
  },
];

export function Hierarchy() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">La scala del valore</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              In quale livello ti trovi oggi?<br />
              <span className="text-orange-pure italic font-medium">E dove vuoi essere domani.</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {levels.map((l, i) => (
            <Reveal key={i} delay={0.2 + i * 0.1}>
              <div className="card-glass h-full">
                <div className="eyebrow">{l.status}</div>
                <div
                  className="mb-6 inline-flex items-center justify-center rounded-xl bg-ink text-paper font-bold"
                  style={{ width: "2.5rem", height: "2.5rem", fontSize: "1rem" }}
                >
                  {l.lv}
                </div>
                <h3 className="text-2xl font-bold mb-4">{l.t}</h3>
                <p className="leading-relaxed">{l.d}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
