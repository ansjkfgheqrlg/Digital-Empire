"use client";

import { Reveal } from "@/components/reveal";
import { Code2, Database, Settings } from "lucide-react";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.95 0 0 0 0 0.93 0 0 0 0 0.90 0 0 0 0.28 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const features = [
  {
    icon: Code2,
    title: "Core Automation Engine",
    description:
      "Sviluppo completo degli script di navigazione sicura per Instagram e Gmail, con simulazione delle impronte digitali ed orari variabili.",
    seed: "7",
    iconColor: "#ff8855",
    iconBg: "rgba(220,100,50,0.28)",
    iconBorder: "rgba(220,110,60,0.50)",
    bg: [
      "radial-gradient(72% 60% at 12% 10%, rgba(255,255,255,0.48) 0%, transparent 50%)",
      "linear-gradient(148deg, #5a1800 0%, #a03800 32%, #d85828 58%, #943000 82%, #320e00 100%)",
    ].join(", "),
    border: "rgba(230,140,100,0.55)",
    glow: "rgba(140,40,0,0.28)",
    shadow: "0 20px 50px -16px rgba(0,0,0,0.40)",
  },
  {
    icon: Database,
    title: "Proxy & Account Setup",
    description:
      "Integrazione e configurazione di proxy residenziali dedicati per blindare gli account ed eliminare qualsiasi rischio di ban di Meta.",
    seed: "3",
    iconColor: "#a0a8e8",
    iconBg: "rgba(140,148,220,0.22)",
    iconBorder: "rgba(150,158,230,0.42)",
    bg: [
      "radial-gradient(72% 60% at 12% 10%, rgba(255,255,255,0.38) 0%, transparent 50%)",
      "linear-gradient(148deg, #1e1e3a 0%, #383870 32%, #5858a0 58%, #2e2e5e 82%, #0e0e20 100%)",
    ].join(", "),
    border: "rgba(160,165,230,0.48)",
    glow: "rgba(50,50,150,0.22)",
    shadow: "0 20px 50px -16px rgba(0,0,0,0.38)",
  },
  {
    icon: Settings,
    title: "Dashboard UI & CRM",
    description:
      "Compilazione dell'applicazione web di gestione e notifica automatica dei lead qualificati verso Slack, email o il tuo CRM preferito.",
    seed: "11",
    iconColor: "#60cc80",
    iconBg: "rgba(60,180,90,0.22)",
    iconBorder: "rgba(70,190,100,0.42)",
    bg: [
      "radial-gradient(72% 60% at 12% 10%, rgba(255,255,255,0.36) 0%, transparent 50%)",
      "linear-gradient(148deg, #041a0c 0%, #0e3820 32%, #185e34 58%, #0c3022 82%, #020e06 100%)",
    ].join(", "),
    border: "rgba(90,190,120,0.48)",
    glow: "rgba(15,110,45,0.22)",
    shadow: "0 20px 50px -16px rgba(0,0,0,0.36)",
  },
];

export function OutreachInside() {
  return (
    <section className="bg-paper section section-border-t">
      <style>{`
        .oi-card {
          transition: transform 0.42s cubic-bezier(0.22,1,0.36,1), box-shadow 0.38s ease;
        }
        .oi-card:hover { transform: translateY(-8px) scale(1.010); }
      `}</style>

      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">What&apos;s inside</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[1.9rem] md:text-[2.9rem] font-bold leading-tight mt-6 text-silver-black">
              Cosa include la tua{" "}
              <span
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  color: "#888",
                }}
              >
                piattaforma di Outreach.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.18}>
            <p className="text-ink/75 mt-4 text-[1.05rem] max-w-xl mx-auto leading-relaxed font-medium">
              Tre moduli tecnici che compongono l&apos;infrastruttura completa installata sui tuoi server.
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-5">
          {features.map((f, i) => {
            const Icon = f.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.10}>
                <div
                  className="oi-card rounded-2xl p-6 h-full flex flex-col"
                  style={{
                    backgroundImage: [GRAIN(f.seed), f.bg].join(", "),
                    backgroundSize: "200px 200px, 100% 100%, 100% 100%",
                    backgroundBlendMode: "screen, normal, normal",
                    border: `1.5px solid ${f.border}`,
                    boxShadow: [
                      f.shadow,
                      `0 0 44px -18px ${f.glow}`,
                      "0 2px 0 rgba(255,255,255,0.30) inset",
                      "0 -1px 0 rgba(0,0,0,0.20) inset",
                      "0 0 0 1px rgba(255,255,255,0.08) inset",
                    ].join(", "),
                  }}
                >
                  {/* Icon badge */}
                  <span
                    className="w-11 h-11 rounded-xl flex items-center justify-center mb-5 shrink-0"
                    style={{
                      background: f.iconBg,
                      border: `1px solid ${f.iconBorder}`,
                      boxShadow: `0 4px 14px ${f.glow}`,
                    }}
                  >
                    <Icon className="h-5 w-5" style={{ color: f.iconColor }} />
                  </span>

                  {/* Title */}
                  <h3
                    className="text-[1.05rem] font-bold leading-tight mb-3"
                    style={{ color: "#ffffff", textShadow: "0 1px 6px rgba(0,0,0,0.55)" }}
                  >
                    {f.title}
                  </h3>

                  {/* Description */}
                  <p
                    className="text-[0.9rem] leading-relaxed flex-1"
                    style={{ color: "rgba(255,255,255,0.68)" }}
                  >
                    {f.description}
                  </p>
                </div>
              </Reveal>
            );
          })}
        </div>
      </div>
    </section>
  );
}
