"use client";

import { Reveal } from "@/components/reveal";
import { Database, Settings, TrendingUp } from "lucide-react";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.18' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.86 0 0 0 0 0.90 0 0 0 0 0.96 0 0 0 0.26 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const features = [
  {
    icon: Database,
    title: "Knowledge Base a Grafo",
    description:
      "Costruzione della knowledge base strutturata come rete interconnessa. Ogni nodo collegato agli altri — clienti, progetti, concetti, brand voice — navigabile visivamente come un grafo di relazioni.",
    link: "Struttura & Architettura",
    seed: "4",
    iconColor: "#78b8f0",
    iconBg: "rgba(80,150,230,0.22)",
    iconBorder: "rgba(90,160,240,0.40)",
    bg: [
      "radial-gradient(70% 55% at 14% 10%, rgba(255,255,255,0.28) 0%, transparent 48%)",
      "linear-gradient(148deg, #091628 0%, #102440 32%, #183a60 58%, #102234 82%, #050c18 100%)",
    ].join(", "),
    border: "rgba(90,150,230,0.36)",
    glow: "rgba(20,80,200,0.28)",
    linkColor: "#78b8f0",
  },
  {
    icon: Settings,
    title: "Integrazione LLM Avanzata",
    description:
      "Configurazione del context engineering: il Second Brain viene collegato ai tuoi strumenti AI. Ad ogni sessione, l'LLM riceve automaticamente il contesto giusto — zero briefing manuali, zero ripetizioni.",
    link: "Context Engineering",
    seed: "8",
    iconColor: "#9090e8",
    iconBg: "rgba(110,110,220,0.20)",
    iconBorder: "rgba(120,120,230,0.38)",
    bg: [
      "radial-gradient(70% 55% at 14% 10%, rgba(255,255,255,0.24) 0%, transparent 48%)",
      "linear-gradient(148deg, #0c0c24 0%, #181840 32%, #24245e 58%, #141430 82%, #060618 100%)",
    ].join(", "),
    border: "rgba(110,110,220,0.34)",
    glow: "rgba(60,60,180,0.25)",
    linkColor: "#9090e8",
  },
  {
    icon: TrendingUp,
    title: "Workflow di Aggiornamento",
    description:
      "Sistema per catturare e aggiornare la knowledge base in modo continuativo. Non è un file statico: è un organismo vivo che evolve con il business, sessione dopo sessione, arricchendosi di nuova conoscenza.",
    link: "Asset Permanente",
    seed: "12",
    iconColor: "#60c8e0",
    iconBg: "rgba(60,180,210,0.18)",
    iconBorder: "rgba(70,190,220,0.36)",
    bg: [
      "radial-gradient(70% 55% at 14% 10%, rgba(255,255,255,0.22) 0%, transparent 48%)",
      "linear-gradient(148deg, #061418 0%, #0c2832 32%, #123c50 58%, #0a2030 82%, #030a0e 100%)",
    ].join(", "),
    border: "rgba(60,180,210,0.34)",
    glow: "rgba(10,120,160,0.24)",
    linkColor: "#60c8e0",
  },
];

export function SecondBrainInside() {
  return (
    <section className="bg-ink section section-border-t">
      <style>{`
        .sbi-card {
          transition: transform 0.42s cubic-bezier(0.22,1,0.36,1), box-shadow 0.38s ease;
        }
        .sbi-card:hover { transform: translateY(-8px) scale(1.010); }
      `}</style>

      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">What&apos;s inside</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[1.9rem] md:text-[2.9rem] font-bold leading-tight mt-6 text-white">
              Cosa include il tuo{" "}
              <span
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  color: "rgba(255,255,255,0.50)",
                }}
              >
                Second Brain.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.18}>
            <p className="text-white/90 mt-4 text-[1.05rem] max-w-xl mx-auto leading-relaxed font-medium">
              Tre layer tecnici che si sovrappongono per dare all&apos;AI una memoria permanente,
              contestuale e sempre aggiornata sul tuo business.
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-5">
          {features.map((f, i) => {
            const Icon = f.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.10}>
                <div
                  className="sbi-card rounded-xl p-6 h-full flex flex-col"
                  style={{
                    backgroundImage: [GRAIN(f.seed), f.bg].join(", "),
                    backgroundSize: "200px 200px, 100% 100%, 100% 100%",
                    backgroundBlendMode: "screen, normal, normal",
                    border: `1.5px solid ${f.border}`,
                    boxShadow: [
                      `0 0 44px -16px ${f.glow}`,
                      "0 20px 50px -16px rgba(0,0,0,0.70)",
                      "0 2px 0 rgba(255,255,255,0.18) inset",
                      "0 -1px 0 rgba(0,0,0,0.30) inset",
                      "0 0 0 1px rgba(255,255,255,0.06) inset",
                    ].join(", "),
                  }}
                >
                  {/* Icon */}
                  <span
                    className="w-11 h-11 rounded-xl flex items-center justify-center mb-5 shrink-0"
                    style={{
                      background: f.iconBg,
                      border: `1px solid ${f.iconBorder}`,
                      boxShadow: `0 4px 16px ${f.glow}`,
                    }}
                  >
                    <Icon className="h-5 w-5" style={{ color: f.iconColor }} />
                  </span>

                  {/* Title */}
                  <h3
                    className="text-[1.05rem] font-bold leading-tight mb-3"
                    style={{ color: "#ffffff", textShadow: "0 1px 8px rgba(0,0,0,0.60)" }}
                  >
                    {f.title}
                  </h3>

                  {/* Description */}
                  <p
                    className="text-[0.9rem] leading-relaxed flex-1 mb-5"
                    style={{ color: "rgba(255,255,255,0.60)" }}
                  >
                    {f.description}
                  </p>

                  {/* Bottom link */}
                  <div
                    className="flex items-center gap-2 text-[0.85rem] font-bold mt-auto pt-4"
                    style={{
                      color: f.linkColor,
                      borderTop: `1px solid rgba(255,255,255,0.08)`,
                    }}
                  >
                    <Icon className="h-3.5 w-3.5" />
                    {f.link}
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
