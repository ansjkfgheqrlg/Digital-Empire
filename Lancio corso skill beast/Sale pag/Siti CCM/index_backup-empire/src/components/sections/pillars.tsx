"use client";

import { Reveal } from "@/components/reveal";
import { Zap, Shield, Target } from "lucide-react";

const pillars = [
  {
    icon: Shield,
    title: "Siamo Ingegneri, non artisti.",
    description: "L'eccellenza non è un atto, ma un'abitudine organizzativa. Ogni nostro progetto segue un'architettura rigorosa e processi millimetrici che non lasciano nulla al caso.",
  },
  {
    icon: Target,
    title: "Vendiamo Profitto, non like.",
    description: "Sfruttiamo l'intelligenza artificiale in modo estremamente architettato per massimizzare ogni singolo risultato. Non giochiamo con i prompt, costruiamo infrastrutture AI che dominano il mercato.",
  },
  {
    icon: Zap,
    title: "Creiamo Imperi, non siti.",
    description: "Un sito web è statico. Un impero digitale è dinamico, scalabile e domina il mercato. Non cerchiamo clienti a cui inviare fatture, ma partner con cui scalare vette.",
  },
];

export function Pillars() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6 text-center">
        <Reveal>
          <span className="bubble-orange mb-6">Differenziazione radicale</span>
        </Reveal>
        <Reveal delay={0.1}>
          <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 mt-6">
            <span className="text-silver-black">Perché </span>
            <span className="text-orange-pure" style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontWeight: 400 }}>Mastery?</span>
          </h2>
        </Reveal>

        <div className="grid md:grid-cols-3 gap-5 text-left relative">
          {pillars.map((p, i) => {
            const Icon = p.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.1}>
                <div className={`card-silver-orange h-full ${i === 2 ? "relative" : ""}`}>
                  {i === 2 && (
                    <div
                      aria-hidden="true"
                      className="hidden xl:block pointer-events-none"
                      style={{
                        position: "absolute",
                        top: "18%",
                        left: "calc(100% + 14px)",
                        width: "220px",
                        zIndex: 5,
                      }}
                    >
                      <svg viewBox="0 0 80 90" width="80" height="90" style={{ overflow: "visible", display: "block" }}>
                        <path
                          d="M 4 78 C 30 50, 50 22, 68 10"
                          fill="none"
                          stroke="#fb4604"
                          strokeWidth="1.6"
                          strokeLinecap="round"
                          style={{ filter: "drop-shadow(0 1px 2px rgba(251,70,4,0.4))" }}
                        />
                        <path
                          d="M 60 6 L 70 10 L 64 18"
                          fill="none"
                          stroke="#fb4604"
                          strokeWidth="1.6"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                      </svg>
                      <div
                        style={{
                          position: "absolute",
                          top: "-8px",
                          left: "78px",
                          width: "210px",
                          fontFamily: "var(--font-serif), Georgia, serif",
                          fontStyle: "italic",
                          fontWeight: 400,
                          fontSize: "16px",
                          lineHeight: 1.3,
                          color: "#1c1c1c",
                          textShadow: "0 1px 2px rgba(255,255,255,0.6)",
                          letterSpacing: "-0.005em",
                        }}
                      >
                        Sì, con l'AI puoi<br />
                        fare siti migliori<br />
                        di qualsiasi agenzia.
                      </div>
                    </div>
                  )}
                  <div className="w-12 h-12 rounded-xl bg-ink text-white flex items-center justify-center mb-6 shadow-lg">
                    <Icon className="h-6 w-6" />
                  </div>
                  <h3 className="text-xl font-bold mb-4 whitespace-pre-line leading-tight text-[#0a0a0a]">
                    {p.title}
                  </h3>
                  <p className="leading-relaxed text-[15px] text-[#1c1c1c]/85 font-medium">
                    {p.description}
                  </p>
                </div>
              </Reveal>
            );
          })}
        </div>
      </div>
    </section>
  );
}
