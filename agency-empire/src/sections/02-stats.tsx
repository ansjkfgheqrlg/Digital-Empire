"use client";

import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

const STATS = [
  {
    prefix: "",
    value: 40,
    suffix: "+",
    label: "Automazioni consegnate",
    sub: "Outreach · Content · Operations",
    numColor: "#fb4604",
    numShadow: "0 0 28px rgba(251,70,4,0.45)",
  },
  {
    prefix: "",
    value: 100,
    suffix: "%",
    label: "Task operativi automatizzati",
    sub: "Zero intervento manuale",
    numColor: "#7b4fb0",
    numShadow: "0 0 28px rgba(123,79,176,0.50)",
  },
  {
    prefix: "+",
    value: 300,
    suffix: "%",
    label: "Produttività media",
    sub: "Misurata dopo 4 settimane",
    numColor: "#1c1c1c",
    numShadow: "none",
  },
];

export function Stats() {
  return (
    <section
      className="bg-ink relative pt-4 pb-10 md:pb-20"
      aria-labelledby="stats-h2"
    >
      <div className="container-default">
        <Reveal>
          <div className="text-center mb-6 md:mb-12">
            <span className="bubble-gold mb-4">
              <span
                className="inline-block w-1.5 h-1.5 rounded-full"
                style={{
                  background: "#ffffff",
                  boxShadow: "0 0 8px rgba(255,255,255,0.6)",
                }}
              />
              Numeri reali
            </span>
            <h2 id="stats-h2" className="mt-6">
              <span className="text-silver-white">Quello che automatizziamo,</span>{" "}
              <span className="text-silver-gold font-accent italic">
                funziona.
              </span>
            </h2>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-3 gap-5">
          {STATS.map((s, i) => (
            <Reveal key={i} delay={0.10 + i * 0.10}>
              <div className="stat-card-silver">
                <div
                  className="font-display text-[2.75rem] md:text-[3.5rem] leading-none font-bold mb-3"
                  style={{ color: s.numColor, textShadow: s.numShadow }}
                >
                  <CountUp
                    to={s.value}
                    prefix={s.prefix}
                    suffix={s.suffix}
                    decimals={0}
                  />
                </div>
                <div className="text-[1rem] font-semibold mb-1.5 text-[#1c1c1c]">
                  {s.label}
                </div>
                <div className="text-[0.85rem] text-[#1c1c1c]/60">
                  {s.sub}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
