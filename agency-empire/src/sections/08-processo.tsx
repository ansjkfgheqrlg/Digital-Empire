"use client";

import { Reveal } from "@/components/reveal";
import { Phone, Map, Wrench, Rocket, BarChart2 } from "lucide-react";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.35' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.90 0 0 0 0 0.88 0 0 0 0 0.86 0 0 0 0.28 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const STEPS = [
  {
    num: "01",
    icon: Phone,
    title: "Demo Call",
    badge: "Gratuita · 30 min",
    body: "Nessuna vendita. Demo live di un workflow attivo nel tuo stesso settore. Se vedi il potenziale, passiamo al blueprint. Nessun impegno.",
    gradient: "linear-gradient(145deg, #1a0800 0%, #2d1200 38%, #6a2200 70%, #c93a0a 100%)",
    radial: "radial-gradient(90% 60% at 10% 14%, rgba(251,70,4,0.28) 0%, transparent 52%)",
    border: "1.5px solid rgba(251,70,4,0.38)",
    glow: "0 50px 90px -28px rgba(100,20,0,0.65), 0 2px 0 rgba(255,255,255,0.14) inset, 0 -2px 0 rgba(0,0,30,0.40) inset, 0 0 0 1px rgba(251,70,4,0.08)",
    numColor: "#fb4604",
    numShadow: "0 0 28px rgba(251,70,4,0.45)",
    iconBg: "linear-gradient(135deg, rgba(251,70,4,0.22) 0%, rgba(201,55,10,0.50) 100%)",
    iconBorder: "1px solid rgba(251,70,4,0.35)",
    seed: "3",
  },
  {
    num: "02",
    icon: Map,
    title: "Blueprint",
    badge: "1 settimana",
    body: "Mappiamo i tuoi processi, decidiamo cosa automatizzare e come. Documento dettagliato: flussi, trigger, integrazioni, metriche.",
    gradient: "linear-gradient(145deg, #0c0520 0%, #1e0848 38%, #4a1d85 70%, #7b4fb0 100%)",
    radial: "radial-gradient(90% 60% at 10% 14%, rgba(192,132,252,0.35) 0%, transparent 52%)",
    border: "1.5px solid rgba(192,132,252,0.40)",
    glow: "0 50px 90px -28px rgba(74,29,133,0.60), 0 2px 0 rgba(255,255,255,0.12) inset, 0 -2px 0 rgba(0,0,30,0.40) inset, 0 0 0 1px rgba(192,132,252,0.10)",
    numColor: "#d4aaff",
    numShadow: "0 0 28px rgba(192,132,252,0.50)",
    iconBg: "linear-gradient(135deg, rgba(192,132,252,0.25) 0%, rgba(90,24,184,0.55) 100%)",
    iconBorder: "1px solid rgba(192,132,252,0.40)",
    seed: "4",
  },
  {
    num: "03",
    icon: Wrench,
    title: "Build",
    badge: "2 settimane",
    body: "Costruiamo il workflow sui tuoi dati reali e lo testiamo su casi reali. Iteriamo finché non gira come deve. Solo sistemi che funzionano davvero.",
    gradient: "linear-gradient(145deg, #030d22 0%, #041840 38%, #0e3888 70%, #2a60c0 100%)",
    radial: "radial-gradient(90% 60% at 10% 14%, rgba(144,192,255,0.32) 0%, transparent 52%)",
    border: "1.5px solid rgba(58,107,192,0.50)",
    glow: "0 50px 90px -28px rgba(14,56,136,0.62), 0 2px 0 rgba(255,255,255,0.12) inset, 0 -2px 0 rgba(0,0,30,0.40) inset, 0 0 0 1px rgba(58,107,192,0.12)",
    numColor: "#90c0ff",
    numShadow: "0 0 28px rgba(58,107,192,0.55)",
    iconBg: "linear-gradient(135deg, rgba(58,107,192,0.30) 0%, rgba(14,56,136,0.58) 100%)",
    iconBorder: "1px solid rgba(144,192,255,0.35)",
    seed: "5",
  },
  {
    num: "04",
    icon: Rocket,
    title: "Go Live",
    badge: "Delivery + 1h formazione",
    body: "Consegna del workflow integrato con i tuoi strumenti. 1 ora di formazione: come monitorare, leggere i dati, cosa fare. Da qui gira in autonomia.",
    gradient: "linear-gradient(145deg, #010e0a 0%, #022018 38%, #044830 70%, #087848 100%)",
    radial: "radial-gradient(90% 60% at 10% 14%, rgba(100,220,160,0.30) 0%, transparent 52%)",
    border: "1.5px solid rgba(8,120,72,0.48)",
    glow: "0 50px 90px -28px rgba(4,72,48,0.62), 0 2px 0 rgba(255,255,255,0.12) inset, 0 -2px 0 rgba(0,0,30,0.40) inset, 0 0 0 1px rgba(8,120,72,0.12)",
    numColor: "#88e8b8",
    numShadow: "0 0 28px rgba(8,180,100,0.50)",
    iconBg: "linear-gradient(135deg, rgba(8,120,72,0.30) 0%, rgba(4,48,30,0.58) 100%)",
    iconBorder: "1px solid rgba(100,220,160,0.35)",
    seed: "6",
  },
  {
    num: "05",
    icon: BarChart2,
    title: "Ottimizzazione",
    badge: "30 giorni inclusi",
    body: "Il primo mese monitoriamo le performance, gestiamo imprevisti, ottimizziamo i flussi. Il workflow migliora con il tempo.",
    gradient: "linear-gradient(145deg, #120e00 0%, #2a2000 38%, #564000 70%, #8a6800 100%)",
    radial: "radial-gradient(90% 60% at 10% 14%, rgba(220,180,80,0.32) 0%, transparent 52%)",
    border: "1.5px solid rgba(180,140,40,0.45)",
    glow: "0 50px 90px -28px rgba(100,80,0,0.60), 0 2px 0 rgba(255,255,255,0.12) inset, 0 -2px 0 rgba(0,0,30,0.40) inset, 0 0 0 1px rgba(180,140,40,0.10)",
    numColor: "#f0c84a",
    numShadow: "0 0 28px rgba(200,160,40,0.55)",
    iconBg: "linear-gradient(135deg, rgba(180,140,40,0.28) 0%, rgba(100,75,0,0.58) 100%)",
    iconBorder: "1px solid rgba(220,180,80,0.38)",
    seed: "7",
  },
];

export function Processo() {
  return (
    <section
      id="processo"
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="processo-h2"
    >
      {/* Glow ambientale — distingue la sezione dalle altre dark adiacenti */}
      <div
        aria-hidden
        className="pointer-events-none absolute z-0"
        style={{
          width: 700,
          height: 500,
          left: "50%",
          top: "40%",
          transform: "translate(-50%, -50%)",
          background:
            "radial-gradient(ellipse, rgba(251,70,4,0.10) 0%, transparent 70%)",
          filter: "blur(90px)",
        }}
      />

      <div className="container-default relative z-[1]">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full" style={{ background: "#fb4604" }} />
              Come lavoriamo
            </span>
            <h2 id="processo-h2" className="mt-6">
              <span className="text-silver-white">Cinque step,</span>{" "}
              <span className="text-silver-gold font-accent italic">
                zero ambiguità.
              </span>
            </h2>
            <p className="mt-5 text-[1.05rem] text-white/70 leading-relaxed font-light">
              Dalla demo live al workflow attivo in 3-4 settimane. Ogni fase è
              documentata, tracciata e hai sempre il controllo di cosa sta succedendo.
            </p>
          </div>
        </Reveal>

        <div className="flex flex-col gap-4 max-w-3xl mx-auto">
          {STEPS.map((s, i) => {
            const Icon = s.icon;
            return (
              <Reveal key={i} delay={0.08 + i * 0.08}>
                <article
                  style={{
                    borderRadius: 22,
                    border: s.border,
                    background: [GRAIN(s.seed), s.radial, s.gradient].join(", "),
                    backgroundSize: "200px 200px, 100% 100%, 100% 100%",
                    backgroundBlendMode: "screen, normal, normal",
                    boxShadow: s.glow,
                    padding: "2rem 2.25rem",
                    color: "#ffffff",
                    minHeight: 200,
                    transition: "transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s",
                  }}
                  className="relative flex flex-col md:flex-row md:items-start gap-6"
                  onMouseEnter={(e) => { (e.currentTarget as HTMLElement).style.transform = "translateY(-4px)"; }}
                  onMouseLeave={(e) => { (e.currentTarget as HTMLElement).style.transform = "translateY(0)"; }}
                >
                  {/* Left: step number + icon */}
                  <div className="flex md:flex-col items-center md:items-start gap-4 md:gap-3 md:shrink-0 md:w-20">
                    <span
                      className="font-display text-[3rem] md:text-[3.5rem] font-bold leading-none select-none"
                      style={{ color: s.numColor, textShadow: s.numShadow, opacity: 0.35 }}
                    >
                      {s.num}
                    </span>
                    <span
                      className="grid place-items-center w-12 h-12 rounded-2xl flex-shrink-0"
                      style={{
                        background: s.iconBg,
                        border: s.iconBorder,
                        boxShadow: `0 6px 18px rgba(0,0,30,0.40), inset 0 1px 0 rgba(255,255,255,0.20)`,
                      }}
                    >
                      <Icon className="h-5 w-5 text-white" strokeWidth={1.8} />
                    </span>
                  </div>

                  {/* Right: content */}
                  <div className="flex-1 flex flex-col">
                    <div
                      className="text-[0.68rem] uppercase tracking-[0.20em] font-bold mb-2"
                      style={{ color: s.numColor, opacity: 0.70 }}
                    >
                      {s.badge}
                    </div>
                    <h3 className="text-[1.5rem] md:text-[1.75rem] font-bold leading-tight tracking-tight text-white mb-3">
                      {s.title}
                    </h3>
                    <p className="text-[0.96rem] leading-relaxed text-white/85 font-light">
                      {s.body}
                    </p>
                  </div>

                  {/* Step marker right edge */}
                  <div
                    className="hidden md:flex items-center justify-center shrink-0 self-center w-8 h-8 rounded-full"
                    style={{
                      background: s.iconBg,
                      border: s.iconBorder,
                      boxShadow: `0 0 16px ${s.numColor}44`,
                    }}
                  >
                    <span
                      className="text-[0.6rem] font-bold"
                      style={{ color: s.numColor }}
                    >
                      {s.num}
                    </span>
                  </div>
                </article>
              </Reveal>
            );
          })}
        </div>
      </div>
    </section>
  );
}
