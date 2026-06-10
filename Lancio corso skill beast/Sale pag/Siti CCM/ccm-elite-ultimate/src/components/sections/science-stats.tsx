"use client";

import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

export function ScienceStats() {
  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-24">
          <Reveal>
            <span className="bubble-ink mb-6">...La scienza parla chiaro:</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-4xl md:text-6xl font-black mt-8">
              <span className="text-silver-white">SISTEMI AI CUSTOM = </span>
              <span className="text-orange italic">PIÙ MARGINE.</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-10">
          {/* DONUT 89% */}
          <Reveal delay={0.2}>
            <div className="card-dark text-center flex flex-col items-center">
              <div className="relative w-32 h-32 mb-10">
                <svg className="w-full h-full transform -rotate-90">
                  <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" className="text-white/5" />
                  <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" strokeDasharray="377" strokeDashoffset={377 * (1 - 0.89)} className="text-orange" />
                </svg>
                <div className="absolute inset-0 flex items-center justify-center text-3xl font-black text-orange">89%</div>
              </div>
              <h3 className="text-xl font-bold text-white mb-4 uppercase tracking-tighter">Visione Leader</h3>
              <p className="text-white/50 text-sm leading-relaxed">I leader credono nella costruzione AI proprietaria per scalare. Chi sa costruirli oggi, controlla il mercato.</p>
            </div>
          </Reveal>

          {/* BAR +313% */}
          <Reveal delay={0.3}>
            <div className="card-dark text-center border-orange/30">
              <div className="text-6xl font-black text-silver-orange mb-4 italic">+313%</div>
              <h3 className="text-xl font-bold text-white mb-4 uppercase tracking-tighter">Moltìplicatore</h3>
              <p className="text-white/80 text-sm leading-relaxed mb-8">Aumento di produttività media con workflow AI Strategici. Non è progresso, è un cambio di specie.</p>
              <div className="w-full h-3 bg-white/5 rounded-full overflow-hidden">
                <div className="h-full bg-orange rounded-full w-[85%]" />
              </div>
            </div>
          </Reveal>

          {/* DONUT 68% */}
          <Reveal delay={0.4}>
            <div className="card-dark text-center flex flex-col items-center">
              <div className="relative w-32 h-32 mb-10">
                <svg className="w-full h-full transform -rotate-90">
                  <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" className="text-white/5" />
                  <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" strokeDasharray="377" strokeDashoffset={377 * (1 - 0.68)} className="text-orange" />
                </svg>
                <div className="absolute inset-0 flex items-center justify-center text-3xl font-black text-orange">68%</div>
              </div>
              <h3 className="text-xl font-bold text-white mb-4 uppercase tracking-tighter">Debito Tecnico</h3>
              <p className="text-white/50 text-sm leading-relaxed">Le aziende non hanno un workflow AI ripetibile. Questo è il problema che verrai pagato per risolvere.</p>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
