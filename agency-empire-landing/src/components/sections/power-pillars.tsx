"use client";

import { Reveal } from "@/components/reveal";
import { Code2, Zap, TrendingUp, Banknote, HeadphonesIcon } from "lucide-react";

const pillars = [
  {
    mark: "C",
    icon: Code2,
    name: "CODICE",
    tagline: "Proprietà totale",
    desc: "Il codice sorgente del sistema è tuo per sempre. Nessun SaaS che ti blocca. Un asset aziendale permanente.",
    rotate: -6,
    translateY: 24,
  },
  {
    mark: "S",
    icon: Zap,
    name: "SETUP",
    tagline: "7 giorni al go-live",
    desc: "Dal contratto firmato al sistema in produzione: 7 giorni. Testato, calibrato, pronto a girare da solo.",
    rotate: -3,
    translateY: 8,
  },
  {
    mark: "V",
    icon: TrendingUp,
    name: "VOLUME",
    tagline: "300+ msg al giorno",
    desc: "Un umano manda 30 DM a mano. Il sistema manda 300+, personalizzati, con follow-up automatici. Non c'è confronto.",
    rotate: 0,
    translateY: -10,
    featured: true,
  },
  {
    mark: "Z",
    icon: Banknote,
    name: "ZERO",
    tagline: "€0 canoni mensili",
    desc: "Nessun abbonamento ricorrente dopo il setup. Solo API a consumo: pochi centesimi per operazione.",
    rotate: 3,
    translateY: 8,
  },
  {
    mark: "S",
    icon: HeadphonesIcon,
    name: "SUPPORT",
    tagline: "90 giorni dedicati",
    desc: "Novanta giorni di supporto tecnico diretto inclusi. Se qualcosa non va, lo sistemiamo noi. Garantito.",
    rotate: 6,
    translateY: 24,
  },
];

export function PowerPillars() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <style>{`
        .framework-tilt:hover { transform: rotate(0deg) translateY(-14px) scale(1.05) !important; z-index: 30 !important; }
      `}</style>
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 30%, rgba(251,70,4,0.08) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-6xl mx-auto px-6 relative">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Cinque garanzie strutturali</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mt-6">
              <span className="text-silver-white">I 5 pilastri che rendono </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  letterSpacing: "-0.01em",
                }}
              >
                il sistema inattaccabile.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/80 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Non sono promesse di vendita. Sono le caratteristiche tecniche e contrattuali che rendono ogni
              implementazione{" "}
              <span
                className="text-orange-pure"
                style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic" }}
              >
                un investimento solido.
              </span>
            </p>
          </Reveal>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-5 gap-4 md:gap-5 pt-10 pb-6">
          {pillars.map((p, i) => {
            const Icon = p.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.08} variant="scale">
                <div
                  className="framework-tilt group relative h-full"
                  style={{
                    transform: `rotate(${p.rotate}deg) translateY(${p.translateY}px)`,
                    transformOrigin: "center bottom",
                    zIndex: p.featured ? 10 : 5 - Math.abs(p.rotate ?? 0) / 3,
                    transition: "transform 500ms cubic-bezier(0.22,1,0.36,1)",
                  }}
                >
                <div
                  className="framework-card relative rounded-2xl p-5 md:p-6 h-full overflow-hidden"
                  style={{
                    background: p.featured
                      ? "linear-gradient(160deg, #f6f2ec 0%, #e9e3da 35%, #d8cfc2 70%, #c7b8a4 100%)"
                      : "linear-gradient(160deg, #fbfaf7 0%, #ece8e1 40%, #d6d1c8 80%, #b9b2a6 100%)",
                    border: p.featured
                      ? "1px solid rgba(251,70,4,0.7)"
                      : "1px solid rgba(180,170,155,0.55)",
                    boxShadow: p.featured
                      ? "inset 0 1px 0 rgba(255,255,255,0.9), inset 0 0 30px rgba(251,70,4,0.10), 0 20px 55px -15px rgba(251,70,4,0.5), 0 0 0 1px rgba(255,255,255,0.3)"
                      : "inset 0 1px 0 rgba(255,255,255,0.85), inset 0 -20px 40px rgba(251,70,4,0.04), 0 14px 40px -15px rgba(40,30,20,0.45), 0 0 0 1px rgba(255,255,255,0.3)",
                  }}
                >
                  <div
                    aria-hidden="true"
                    className="pointer-events-none absolute inset-0 rounded-2xl"
                    style={{
                      background:
                        "linear-gradient(135deg, rgba(255,255,255,0.7) 0%, transparent 35%, transparent 60%, rgba(251,70,4,0.18) 100%)",
                      mixBlendMode: "soft-light",
                    }}
                  />
                  <div
                    aria-hidden="true"
                    className="pointer-events-none absolute inset-2 rounded-xl"
                    style={{
                      border: p.featured ? "1px solid rgba(251,70,4,0.35)" : "1px solid rgba(140,125,105,0.35)",
                    }}
                  />

                  <div
                    className="absolute top-3 left-4 text-[13px] font-black tracking-widest"
                    style={{ color: p.featured ? "#fb4604" : "rgba(90,78,62,0.85)" }}
                  >
                    {p.mark}
                  </div>
                  <div
                    className="absolute bottom-3 right-4 text-[13px] font-black tracking-widest rotate-180"
                    style={{ color: p.featured ? "#fb4604" : "rgba(90,78,62,0.85)" }}
                  >
                    {p.mark}
                  </div>

                  <div className="relative flex flex-col items-center text-center pt-6 pb-4">
                    <div
                      className="w-14 h-14 rounded-full flex items-center justify-center mb-6 transition-transform duration-500 group-hover:scale-110"
                      style={{
                        background: p.featured
                          ? "radial-gradient(circle at 30% 30%, rgba(251,70,4,0.55), rgba(251,70,4,0.18) 60%, rgba(255,240,225,0.4) 85%)"
                          : "radial-gradient(circle at 30% 30%, rgba(255,255,255,0.95), rgba(220,210,195,0.5) 55%, rgba(251,70,4,0.15) 90%)",
                        border: p.featured
                          ? "1px solid rgba(251,70,4,0.7)"
                          : "1px solid rgba(160,145,125,0.55)",
                        boxShadow: p.featured
                          ? "0 0 30px -6px rgba(251,70,4,0.7), inset 0 1px 0 rgba(255,255,255,0.5)"
                          : "0 4px 14px -4px rgba(60,45,30,0.25), inset 0 1px 0 rgba(255,255,255,0.9)",
                      }}
                    >
                      <Icon
                        className="h-6 w-6"
                        style={{ color: p.featured ? "#fff" : "#5a4e3e", strokeWidth: 1.7 }}
                      />
                    </div>

                    <div
                      aria-hidden="true"
                      className="w-10 h-px mb-4"
                      style={{
                        background:
                          "linear-gradient(90deg, transparent, rgba(140,125,105,0.55) 30%, rgba(251,70,4,0.95) 50%, rgba(140,125,105,0.55) 70%, transparent)",
                      }}
                    />

                    <h3
                      className="text-xl md:text-2xl font-black mb-1 tracking-wide"
                      style={{
                        background: p.featured
                          ? "linear-gradient(180deg, #7a2a02 0%, #fb4604 55%, #9a2a02 100%)"
                          : "linear-gradient(180deg, #3a3228 0%, #6b5d4a 50%, #fb4604 100%)",
                        WebkitBackgroundClip: "text",
                        WebkitTextFillColor: "transparent",
                        backgroundClip: "text",
                      }}
                    >
                      {p.name}
                    </h3>
                    <div
                      className="text-[11px] uppercase tracking-[0.2em] font-black mb-5"
                      style={{ color: p.featured ? "#9a2a02" : "rgba(74,60,45,0.95)" }}
                    >
                      {p.tagline}
                    </div>

                    <p
                      className="text-[13px] leading-relaxed"
                      style={{ color: "rgba(50,42,32,0.82)" }}
                    >
                      {p.desc}
                    </p>
                  </div>
                </div>
                </div>
              </Reveal>
            );
          })}
        </div>
      </div>
    </section>
  );
}
