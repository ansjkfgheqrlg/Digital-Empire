"use client";

import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

/* ════════════════════════════════════════════════════════════════════════
   REGOLA: qui vanno SOLO numeri che possiamo dimostrare in demo.

   Revisione 2026-07-27 (Arena). Prima c'erano "40+ automazioni consegnate",
   "100% task automatizzati" e "+300% produttività media, misurata dopo 4
   settimane". Nessuno dei tre aveva un riscontro su disco: il "+300%
   misurato" in particolare dichiarava una misurazione che non esiste.
   Sostituiti con i numeri della macchina Novacar, che sono contati sui file
   (fonte: Clienti/Prof Autocad/preventivo-forge/ — vedi 09b-prove-novacar).

   Se aggiungi una riga qui, deve avere una fonte su disco. Nessuna eccezione.
   ════════════════════════════════════════════════════════════════════════ */
const STATS = [
  {
    prefix: "",
    value: 65,
    suffix: "",
    label: "Documenti prodotti dalla macchina",
    sub: "Casi reali, dal 3 al 13 luglio 2026",
    numColor: "#fb4604",
    numShadow: "0 0 28px rgba(251,70,4,0.45)",
  },
  {
    prefix: "~",
    value: 2,
    suffix: " min",
    label: "Dal dato grezzo al documento finito",
    sub: "Tempo della macchina, misurato",
    numColor: "#7b4fb0",
    numShadow: "0 0 28px rgba(123,79,176,0.50)",
  },
  {
    prefix: "",
    value: 6,
    suffix: "",
    label: "Controlli prima di ogni consegna",
    sub: "Se uno fallisce, non consegna niente",
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
            <p className="mt-5 text-[0.95rem] text-white/60 font-light max-w-xl mx-auto">
              Sono i numeri di una macchina che gira da un cliente vero, contati
              sui file e non stimati. Preferiamo tre numeri veri a dieci
              impressionanti.
            </p>
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
