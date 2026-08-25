"use client";

import { Reveal } from "@/components/reveal";

const levels = [
  {
    lv: "01",
    t: "AI Prompting Manuale",
    d: "Apri ChatGPT, scrivi una domanda, ricevi una risposta. È una commodity: chiunque può farlo, il valore è vicino allo zero.",
    price: "€0",
    status: "Commodity",
  },
  {
    lv: "02",
    t: "AI Automation",
    d: "Usi Zapier o Make per connettere le app. Utile, ma fragile e limitato a quello che i tool esterni permettono. Sei un assemblatore.",
    price: "€200-500",
    status: "Service",
  },
  {
    lv: "03",
    t: "AI Architecture",
    d: "Costruisci sistemi deterministici, agenti specializzati e workflow proprietari con Claude Code. Qui il valore è infinito.",
    price: "€2000+",
    status: "Empire Level",
    premium: true,
  },
];

export function Hierarchy() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-24">
          <Reveal>
            <span className="bubble-orange mb-6">La gerarchia del valore</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-4xl md:text-7xl font-black mt-8 text-silver-black leading-tight tracking-tighter">
              Perché "chattare" con l'AI <br />
              <span className="text-orange italic font-medium">oggi vale zero.</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {levels.map((l, i) => (
            <Reveal key={i} delay={0.2 + i * 0.1}>
              {l.premium ? (
                <div className="card-orange h-full relative overflow-hidden flex flex-col">
                  <div className="absolute top-8 right-10 text-white/20 font-black text-6xl italic">PRO</div>
                  <div className="bubble-silver mb-8 bg-white/20 border-white/20 text-white">{l.status}</div>
                  <div className="step-num bg-ink text-white mb-8 shadow-xl">{l.lv}</div>
                  <h3 className="text-3xl font-black mb-6 italic tracking-tight">{l.t}</h3>
                  <p className="text-white/80 leading-relaxed font-medium flex-1 mb-10">{l.d}</p>
                  <div className="text-4xl font-black italic tracking-tighter border-t border-white/20 pt-8">{l.price}</div>
                </div>
              ) : (
                <div className="card-paper h-full flex flex-col bg-grey/30 border-dashed border-ink/10 opacity-70">
                  <div className="text-[10px] font-black uppercase tracking-[0.3em] text-ink/30 mb-8">{l.status}</div>
                  <div className="step-num bg-grey text-ink/40 border-ink/5 mb-8">{l.lv}</div>
                  <h3 className="text-3xl font-black mb-6 text-ink tracking-tight">{l.t}</h3>
                  <p className="text-ink/60 leading-relaxed font-medium flex-1 mb-10">{l.d}</p>
                  <div className="text-4xl font-black italic tracking-tighter text-ink/20 border-t border-ink/5 pt-8">{l.price}</div>
                </div>
              )}
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
