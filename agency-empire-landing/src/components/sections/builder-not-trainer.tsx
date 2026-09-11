"use client";

import { Reveal } from "@/components/reveal";
import { Zap, Lock, Shield } from "lucide-react";

const stats = [
  {
    icon: Zap,
    n: "7 gg",
    l: "Setup completo chiavi in mano",
    color: "#fb4604",
    bg: "linear-gradient(155deg, rgba(251,70,4,0.10) 0%, #161616 38%, #0e0e0e 100%)",
    border: "rgba(251,70,4,0.30)",
    iconBg: "rgba(251,70,4,0.16)",
    iconBorder: "rgba(251,70,4,0.38)",
    glow: "0 0 40px -18px rgba(251,70,4,0.28)",
  },
  {
    icon: Lock,
    n: "€0",
    l: "Canoni o abbonamenti mensili",
    color: "#d9d6cf",
    bg: "linear-gradient(155deg, #1c1c1c 0%, #161616 40%, #0e0e0e 100%)",
    border: "rgba(255,255,255,0.11)",
    iconBg: "rgba(217,214,207,0.10)",
    iconBorder: "rgba(217,214,207,0.22)",
    glow: "0 0 0 transparent",
  },
  {
    icon: Shield,
    n: "100%",
    l: "Proprietà intellettuale del codice",
    color: "#d9d6cf",
    bg: "linear-gradient(155deg, #1c1c1c 0%, #161616 40%, #0e0e0e 100%)",
    border: "rgba(255,255,255,0.11)",
    iconBg: "rgba(217,214,207,0.10)",
    iconBorder: "rgba(217,214,207,0.22)",
    glow: "0 0 0 transparent",
  },
];

export function BuilderNotTrainer() {
  return (
    <section className="bg-ink-2 section">
      <style>{`
        .bnt-stat {
          transition: transform 0.38s cubic-bezier(0.22,1,0.36,1), box-shadow 0.35s ease;
        }
        .bnt-stat:hover { transform: translateY(-4px); }
      `}</style>

      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-2 gap-12 md:gap-16 items-center">

          {/* Left: copy */}
          <div>
            <Reveal>
              <span className="bubble-orange mb-8">Zero Teoria. 100% Campo.</span>
            </Reveal>

            <Reveal delay={0.1}>
              <h2
                className="text-[2.2rem] md:text-[3.2rem] font-black leading-[1.05] tracking-tight mt-6 mb-8"
                style={{
                  background: "linear-gradient(175deg, #ffffff 0%, #d9d6cf 42%, #fb4604 100%)",
                  WebkitBackgroundClip: "text",
                  WebkitTextFillColor: "transparent",
                  backgroundClip: "text",
                }}
              >
                Prendo quello che uso io{" "}
                <span
                  style={{
                    fontFamily: "var(--font-serif), Georgia, serif",
                    fontStyle: "italic",
                    fontWeight: 400,
                    WebkitTextFillColor: "transparent",
                  }}
                >
                  ogni singolo giorno
                </span>{" "}
                e lo adatto a te.
              </h2>
            </Reveal>

            <div className="space-y-4 text-white/90 text-[0.97rem] leading-relaxed">
              <Reveal delay={0.18}>
                <p>
                  Non ti sto vendendo codici scritti in laboratorio la notte scorsa o accrocchi
                  instabili assemblati su Zapier che si rompono al primo aggiornamento delle API.
                </p>
              </Reveal>
              <Reveal delay={0.26}>
                <p>
                  Questo stack rappresenta{" "}
                  <strong className="text-white">il cuore operativo del mio business — e presto del tuo</strong>.
                  Lo uso per scovare lead per la mia agenzia e generare contenuti ad alta
                  conversione per i miei clienti. Non dobbiamo ricreare nulla da zero: prendiamo
                  un&apos;infrastruttura d&apos;acciaio, la cuciamo su misura per il tuo brand e
                  la installiamo sui tuoi sistemi.
                </p>
              </Reveal>
              <Reveal delay={0.34}>
                <p className="text-orange-pure font-semibold" style={{ WebkitTextFillColor: "#fb4604" }}>
                  Non ti vendo una promessa. Ti installo la stessa infrastruttura che uso io,
                  oggi, per far girare Digital Empire.
                </p>
              </Reveal>
            </div>
          </div>

          {/* Right: 3 vertical stat cards */}
          <div className="flex flex-col gap-4">
            {stats.map((s, i) => {
              const Icon = s.icon;
              return (
                <Reveal key={i} delay={0.2 + i * 0.10}>
                  <div
                    className="bnt-stat relative rounded-xl px-7 py-5 flex items-center gap-5 overflow-hidden"
                    style={{
                      background: s.bg,
                      border: `1.5px solid ${s.border}`,
                      boxShadow: [
                        "inset 0 1px 0 rgba(255,255,255,0.07)",
                        "0 16px 40px -16px rgba(0,0,0,0.70)",
                        s.glow,
                      ].join(", "),
                    }}
                  >
                    {/* Icon */}
                    <span
                      className="w-11 h-11 rounded-xl flex items-center justify-center shrink-0"
                      style={{
                        background: s.iconBg,
                        border: `1px solid ${s.iconBorder}`,
                        boxShadow: `0 4px 14px ${s.iconBg}`,
                      }}
                    >
                      <Icon className="h-5 w-5" style={{ color: s.color }} />
                    </span>

                    {/* Metric */}
                    <div>
                      <div
                        className="text-[2rem] md:text-[2.5rem] font-black leading-none mb-0.5"
                        style={{
                          background: `linear-gradient(180deg, #ffffff 0%, ${s.color} 100%)`,
                          WebkitBackgroundClip: "text",
                          WebkitTextFillColor: "transparent",
                          backgroundClip: "text",
                          letterSpacing: "-0.04em",
                        }}
                      >
                        {s.n}
                      </div>
                      <div className="text-[11px] uppercase tracking-[0.18em] font-black text-white/75">
                        {s.l}
                      </div>
                    </div>
                  </div>
                </Reveal>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
