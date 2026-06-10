"use client";

import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

const stats = [
  { n: 89, suf: "%", t: "Visione Leader", d: "dei leader crede nella costruzione AI proprietaria per scalare." },
  { n: 313, suf: "%", t: "Moltìplicatore", d: "di produttività media con workflow AI Strategici e deterministici." },
  { n: 68, suf: "%", t: "Debito Tecnico", d: "delle aziende non ha un workflow AI ripetibile. Un mercato vergine." },
];

export function ScienceStats() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-ink mb-6">...La scienza parla chiaro</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4">
              <span className="text-silver-white">SISTEMI AI CUSTOM = </span>
              <span className="text-orange-pure italic">PIÙ MARGINE.</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {stats.map((s, i) => (
            <Reveal key={i} delay={0.2 + i * 0.1}>
              <div className="stat-card-silver">
                <div className="text-5xl md:text-6xl font-bold text-orange-pure leading-none mb-4">
                  <CountUp to={s.n} suffix={s.suf} />
                </div>
                <h3 className="text-lg font-bold text-ink mb-2 uppercase tracking-tighter">{s.t}</h3>
                <p className="text-sm text-ink/70 leading-relaxed font-medium">
                  {s.d}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
