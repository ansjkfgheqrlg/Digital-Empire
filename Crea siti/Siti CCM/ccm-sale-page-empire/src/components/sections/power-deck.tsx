"use client";

import { Reveal } from "@/components/reveal";
import { Zap, Boxes, ShieldAlert, Cpu } from "lucide-react";

const cards = [
  {
    t: "Deep Focus Co-Pilot",
    d: "Configuriamo il tuo ambiente di lavoro per eliminare il 'Chat-Drifting'. Claude Code opererà come un senior partner al tuo fianco.",
    icon: Zap,
  },
  {
    t: "Agency Scaling Pack",
    d: "Sistemi pronti per gestire 10x clienti senza aumentare il personale. Delegazione deterministica al 100%.",
    icon: Boxes,
  },
  {
    t: "System Prototype Builder",
    d: "Dalla tua idea al primo prototipo funzionante in meno di 2 ore. Senza scrivere codice, solo architettando.",
    icon: ShieldAlert,
  },
  {
    t: "The Vault of Agents",
    d: "Accesso alla nostra libreria privata di Agenti, Skill e MCP già testati per business reali.",
    icon: Cpu,
  },
];

export function PowerDeck() {
  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Asset Inclusi</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4">
              <span className="text-silver-white">The Power Deck: </span>
              <span className="text-silver-orange italic font-medium">I tuoi vantaggi.</span>
            </h2>
          </Reveal>
        </div>

        <div className="space-y-24">
          {cards.map((c, i) => {
            const Icon = c.icon;
            return (
              <div key={i} className="sticky top-24">
                <Reveal delay={0.1} variant="scale">
                  <div className="card-dark border-orange/20 shadow-[0_0_50px_-20px_rgba(251,70,4,0.2)]">
                    <div className="w-12 h-12 rounded-xl bg-orange flex items-center justify-center mb-6">
                      <Icon className="h-6 w-6 text-white" />
                    </div>
                    <h3 className="text-2xl font-bold text-silver-white mb-4">{c.t}</h3>
                    <p className="text-white/70 leading-relaxed text-lg">{c.d}</p>
                  </div>
                </Reveal>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
