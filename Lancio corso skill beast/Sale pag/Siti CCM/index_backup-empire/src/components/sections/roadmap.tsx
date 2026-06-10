"use client";

import { Reveal } from "@/components/reveal";

const weeks = [
  { t: "Deep Dive AI & Claude Code", d: "Installazione, configurazione e primi workflow deterministici.", note: "Context Engineering avanzato", side: "right" },
  { t: "The Architecture of Systems", d: "Come pensare a blocchi e agenti prima di scrivere un solo prompt.", note: "Prompt Architecture su misura", side: "left" },
  { t: "Sub-Agents & Skill Creation", d: "Costruiamo la memoria e le capacità estese del tuo sistema AI.", note: "Libreria di Skill riutilizzabili", side: "right" },
  { t: "Integration & MCP", d: "Connettiamo Claude a database, API e tool esterni in tempo reale.", note: "Claude Cowork, Projects, Perplexity, Manus", side: "left" },
  { t: "Deterministic Output & Validation", d: "Tecniche avanzate per garantire che il sistema non allucini mai.", note: "Zero allucinazioni, output affidabili", side: "right" },
  { t: "Launch & Scalability", d: "Ottimizzazione finale e deployment del tuo primo System AI.", note: "Dal prototipo al prodotto vendibile", side: "left" },
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
              <div className="relative">
                <div className="flex gap-6 card-paper items-start">
                  <div className="step-num shrink-0">{i + 1}</div>
                  <div>
                    <h3 className="text-xl md:text-2xl font-bold text-ink mb-1">Settimana {i + 1}: {w.t}</h3>
                    <p className="text-ink/70 leading-relaxed font-medium">{w.d}</p>
                  </div>
                </div>
                <div
                  aria-hidden="true"
                  className="hidden xl:flex pointer-events-none items-center gap-2"
                  style={{
                    position: "absolute",
                    top: "50%",
                    transform: "translateY(-50%)",
                    [w.side === "right" ? "left" : "right"]: "calc(100% + 28px)",
                    width: "230px",
                    fontFamily: "var(--font-serif), Georgia, serif",
                    fontStyle: "italic",
                    fontWeight: 600,
                    fontSize: "19px",
                    lineHeight: 1.3,
                    color: "#7a2a08",
                    letterSpacing: "-0.005em",
                    justifyContent: w.side === "right" ? "flex-start" : "flex-end",
                    textAlign: w.side === "right" ? "left" : "right",
                  } as React.CSSProperties}
                >
                  {w.side === "right" && <span style={{ color: "#fb4604", marginRight: 6 }}>→</span>}
                  <span>{w.note}</span>
                  {w.side === "left" && <span style={{ color: "#fb4604", marginLeft: 6 }}>←</span>}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
