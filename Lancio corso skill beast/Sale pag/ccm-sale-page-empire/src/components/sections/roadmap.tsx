"use client";

import { Reveal } from "@/components/reveal";

const weeks = [
  { t: "Deep Dive AI & Claude Code", d: "Installazione, configurazione e primi workflow deterministici." },
  { t: "The Architecture of Systems", d: "Come pensare a blocchi e agenti prima di scrivere un solo prompt." },
  { t: "Sub-Agents & Skill Creation", d: "Costruiamo la memoria e le capacità estese del tuo sistema AI." },
  { t: "Integration & MCP", d: "Connettiamo Claude a database, API e tool esterni in tempo reale." },
  { t: "Deterministic Output & Validation", d: "Tecniche avanzate per garantire che il sistema non allucini mai." },
  { t: "Launch & Scalability", d: "Ottimizzazione finale e deployment del tuo primo System AI." },
];

export function Roadmap() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Il percorso</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              6 Settimane per diventare<br />
              <span className="text-orange-pure italic font-medium">un System Architect.</span>
            </h2>
          </Reveal>
        </div>

        <div className="space-y-6">
          {weeks.map((w, i) => (
            <Reveal key={i} delay={0.2 + i * 0.05}>
              <div className="flex gap-6 card-paper items-start">
                <div className="step-num shrink-0">{i + 1}</div>
                <div>
                  <h3 className="text-xl md:text-2xl font-bold text-ink mb-1">Settimana {i + 1}: {w.t}</h3>
                  <p className="text-ink/70 leading-relaxed font-medium">{w.d}</p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
