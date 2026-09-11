"use client";

import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

const stats = [
  { n: 7, suf: " gg", t: "Setup Completo", d: "Dal briefing al sistema in produzione. Nessuna attesa, nessun mese di sviluppo." },
  { n: 300, suf: "+", t: "Email al Giorno", d: "Messaggi personalizzati inviati in automatico ogni mattina su Gmail e Instagram." },
  { n: 0, suf: "€", t: "Canoni Mensili", d: "Il sistema gira sui tuoi server. Zero abbonamenti SaaS. Zero dipendenze da terze parti." },
];

export function ScienceStats() {
  return (
    <section className="bg-ink relative pb-24 pt-4">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-10">
          <Reveal>
            <span className="bubble-orange mb-6">I numeri parlano chiaro</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[24px] md:text-[34px] font-bold mt-4 tracking-tight">
              <span className="text-silver-white">AUTOMAZIONE AI PROPRIETARIA = </span>
              <span
                className="text-orange-pure"
                style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontWeight: 400, letterSpacing: "-0.01em", fontSize: "1.35em" }}
              >
                più tempo, <span style={{ whiteSpace: "nowrap" }}>più margine.</span>
              </span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-4 max-w-3xl mx-auto">
          {stats.map((s, i) => (
            <Reveal key={i} delay={0.2 + i * 0.1}>
              <div className="card-silver-orange h-full rounded-xl p-5 text-center">
                <div className="text-3xl md:text-4xl font-extrabold text-orange-pure leading-none mb-3">
                  <CountUp to={s.n} suffix={s.suf} />
                </div>
                <h3 className="text-[11px] font-black mb-2 uppercase tracking-[0.15em]" style={{ color: "#0a0a0a" }}>{s.t}</h3>
                <p className="text-[12px] leading-relaxed" style={{ color: "rgba(28,28,28,0.75)" }}>
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
