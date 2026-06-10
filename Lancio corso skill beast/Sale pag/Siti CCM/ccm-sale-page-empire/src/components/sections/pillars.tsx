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
    <section className="bg-ink section section-border-t">
      <div className="max-w-5xl mx-auto px-6 text-center">
        <Reveal>
          <span className="bubble-orange mb-6">Differenziazione radicale</span>
        </Reveal>
        <Reveal delay={0.1}>
          <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 mt-6">
            <span className="text-silver-white">Perché </span>
            <span className="text-silver-orange">Mastery?</span>
          </h2>
        </Reveal>

        <div className="grid md:grid-cols-3 gap-5 text-left">
          {pillars.map((p, i) => {
            const Icon = p.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.1}>
                <div className="card-dark h-full">
                  <div className="w-12 h-12 rounded-xl bg-orange-pure text-white flex items-center justify-center mb-6">
                    <Icon className="h-6 w-6" />
                  </div>
                  <h3 className="text-xl font-bold mb-4 text-silver-white whitespace-pre-line leading-tight">
                    {p.title}
                  </h3>
                  <p className="text-white/60 leading-relaxed text-[15px]">
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
